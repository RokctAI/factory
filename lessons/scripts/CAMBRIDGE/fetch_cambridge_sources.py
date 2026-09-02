#!/usr/bin/env python3
# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""Fetch Cambridge International source documents and record their provenance.

The fetch-and-record half of the ingestion method the CAPS tree documents
(fetch the real document from the primary source, hash it, then curate by
hand). Two things make this script different from its CAPS/IEB counterparts,
both driven by Cambridge's terms:

1. It fetches SYLLABUSES ONLY — and the reason is rights, not access.
   Cambridge publishes syllabuses, question papers, mark schemes and examiner
   reports openly on its own site, so this script could technically download
   any of them. But Cambridge separately refuses permission for electronic
   reproduction of past-paper questions, mark schemes and examiner reports in
   any format, commercial or not. Being able to fetch a document is not
   permission to reproduce it. The `past-papers` subcommand therefore exists
   only to REFUSE, with the reason — because someone will eventually try, and
   a refusal that explains itself is worth more than a missing feature. There
   is deliberately no flag that overrides a rights gate.

2. It writes fetch results back into `subject_registry.json`, not into the
   tree. The tree is a pure function of the registry (see
   build_cambridge_tree.py), so after any fetch you re-run the generator. That
   is why the tree's drift check can be total.

Subcommands:
  probe             read robots.txt and the copyright/terms pages first, and
                    print what they say, so SOURCES.md can be updated from
                    first-hand text rather than search snippets.
  discover          harvest syllabus PDF URLs from a subject landing page (or
                    a browser-saved copy via --html) into the registry.
  fetch-syllabuses  download the registry's recorded syllabus PDFs, hash
                    them, update the manifest and the registry.
  register          record a file downloaded out of band (browser), keeping
                    the real source URL + sha256.
  verify            re-hash every manifest entry; --refetch also re-downloads
                    to detect a new syllabus edition upstream.
  past-papers       refuses, and explains the policy.

All network calls: honest User-Agent, robots.txt respected, >=2s spacing,
retries with backoff. Downloaded PDFs land in gitignored source/ directories
and must never be committed; the manifest is the committed record.
"""
import argparse
import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

CAMBRIDGE = Path("lessons/curriculum/CAMBRIDGE")
REGISTRY_PATH = CAMBRIDGE / "scripts" / "subject_registry.json"
MANIFEST = CAMBRIDGE / "sources_manifest.json"
POLICY = CAMBRIDGE / "RIGHTS.json"

BASE = "https://www.cambridgeinternational.org"
TERMS_PAGES = [
    "https://www.cambridge.org/legal/copyright",
    "https://help.cambridgeinternational.org/hc/en-gb/categories/200545072-Publications-and-copyright",
]
USER_AGENT = ("rokct-factory-curriculum/1.0 "
              "(educational curriculum indexing; contact: repo owner)")
DELAY_S = 2.0
_last_request = [0.0]

SYLLABUS_PDF_RE = re.compile(r"/Images/\d+-[\d\-]+-syllabus\.pdf", re.I)


def polite_get(url, binary=False, retries=3, timeout=60):
    wait = time.monotonic() - _last_request[0]
    if wait < DELAY_S:
        time.sleep(DELAY_S - wait)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(retries):
        try:
            _last_request[0] = time.monotonic()
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = r.read()
                return data if binary else data.decode("utf-8", "replace")
        except (urllib.error.URLError, TimeoutError) as e:
            if attempt == retries - 1:
                raise
            back = 2 ** (attempt + 1)
            print(f"  retry in {back}s ({e})")
            time.sleep(back)


class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self._href = None
        self._text = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self._href = dict(attrs).get("href")
            self._text = []

    def handle_data(self, data):
        if self._href is not None:
            self._text.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self._href is not None:
            self.links.append((self._href, " ".join("".join(self._text).split())))
            self._href = None


def extract_links(html):
    p = LinkExtractor()
    p.feed(html)
    out = []
    for href, text in p.links:
        if not href or href.startswith(("#", "mailto:", "javascript:")):
            continue
        if href.startswith("/"):
            href = BASE + href
        out.append((href, text))
    return out


def check_robots(url):
    rp = urllib.robotparser.RobotFileParser()
    try:
        rp.parse(polite_get(f"{BASE}/robots.txt").splitlines())
    except Exception as e:
        print(f"robots.txt unreadable ({e}) — stopping. Confirm the rules by "
              f"hand before fetching; do not assume permission.")
        return False
    ok = rp.can_fetch(USER_AGENT, url) and rp.can_fetch("*", url)
    if not ok:
        print(f"robots.txt DISALLOWS {url} for us — stopping (the WCED "
              f"precedent recorded in ../CAPS/past_papers/SOURCES.md).")
    return ok


def load_registry():
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def save_registry(reg):
    REGISTRY_PATH.write_text(json.dumps(reg, indent=2, ensure_ascii=False) + "\n",
                             encoding="utf-8")
    print(f"  registry updated — re-run build_cambridge_tree.py to propagate into the tree")


def load_manifest():
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {
        "note": ("Provenance record for every Cambridge source document "
                 "fetched or registered: URL, sha256, size, date. The "
                 "documents themselves are gitignored and never committed "
                 "(Cambridge terms) — this file records what was read "
                 "without republishing it."),
        "entries": [],
    }


def save_manifest(m):
    MANIFEST.write_text(json.dumps(m, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def record(manifest, *, url, path, kind, subject, code):
    entry = {
        "url": url,
        "path": str(path).replace("\\", "/"),
        "kind": kind,
        "subject": subject,
        "syllabus_code": code,
        "sha256": sha256_file(path),
        "bytes": Path(path).stat().st_size,
        "fetched": date.today().isoformat(),
    }
    manifest["entries"] = [e for e in manifest["entries"]
                           if e["path"] != entry["path"]] + [entry]
    return entry


def iter_qualifications(reg):
    for slug, subject in reg["subjects"].items():
        for q in subject.get("qualifications", []):
            yield slug, subject, q


# --- subcommands -----------------------------------------------------------

def cmd_probe(args):
    print(f"--- {BASE}/robots.txt ---")
    try:
        print(polite_get(f"{BASE}/robots.txt"))
    except Exception as e:
        print(f"(unreadable: {e})")
    for page in TERMS_PAGES:
        print(f"\n--- {page} ---")
        try:
            text = re.sub(r"<[^>]+>", " ", polite_get(page))
            print(" ".join(text.split())[:3000])
        except Exception as e:
            print(f"(unreadable: {e})")
    print("\nRecord what these actually say in "
          "lessons/curriculum/CAMBRIDGE/SOURCES.md, and reconcile any "
          "difference against RIGHTS.json BEFORE fetching.")
    return 0


def cmd_discover(args):
    """Harvest syllabus PDF URLs from a subject landing page into the registry."""
    if args.html:
        html = Path(args.html).read_text(encoding="utf-8", errors="replace")
    else:
        if not args.url:
            sys.exit("give --url <subject landing page> or --html <saved page>")
        if not check_robots(args.url):
            return 1
        html = polite_get(args.url)

    found = []
    for href, text in extract_links(html):
        if SYLLABUS_PDF_RE.search(href):
            found.append((href, text))
    if not found:
        print("No syllabus PDF links found. The page may be script-rendered: "
              "save it from a browser and pass --html.")
        return 1

    reg = load_registry()
    target = None
    for slug, subject, q in iter_qualifications(reg):
        if q["code"] == args.code:
            target = (slug, q)
            break
    if target is None:
        sys.exit(f"syllabus code {args.code} is not in the registry")
    slug, q = target

    for href, text in found:
        edition = re.search(r"-([\d\-]+)-syllabus\.pdf", href)
        entry = {
            "edition": edition.group(1) if edition else "unknown",
            "url": href,
            "url_status": "discovered_first_hand",
            "status": "pending_fetch",
            "link_text": text,
            "discovered": date.today().isoformat(),
        }
        docs = q.setdefault("syllabus_documents", [])
        if not any(d.get("url") == href for d in docs):
            docs.append(entry)
        print(f"  [{slug} {args.code}] {text or '(no link text)'} -> {href}")
    if args.url:
        q["landing_page"] = args.url
        q["landing_page_status"] = "verified_first_hand"
    save_registry(reg)
    return 0


def cmd_fetch_syllabuses(args):
    reg = load_registry()
    manifest = load_manifest()
    fetched = skipped = failed = 0
    for slug, subject, q in iter_qualifications(reg):
        if args.subject and slug != args.subject:
            continue
        for doc in q.get("syllabus_documents", []):
            url = doc.get("url")
            if not url:
                continue
            host = urllib.parse.urlparse(url).hostname or ""
            if not host.endswith("cambridgeinternational.org"):
                print(f"  [SKIP] {url} — not a Cambridge host")
                skipped += 1
                continue
            if not check_robots(url):
                failed += 1
                continue
            dest_dir = CAMBRIDGE / slug / "exam_guidelines" / "source"
            dest = dest_dir / f"{q['code']}_{doc.get('edition', 'unknown')}_syllabus.pdf"
            if dest.exists() and not args.force:
                print(f"  [HAVE] {dest}")
                skipped += 1
                continue
            try:
                dest_dir.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(polite_get(url, binary=True))
            except Exception as e:
                print(f"  [FAIL] {url} — {type(e).__name__}: {e}")
                failed += 1
                continue
            entry = record(manifest, url=url, path=dest, kind="syllabus",
                           subject=slug, code=q["code"])
            doc["status"] = "fetched_pending_curation"
            doc["sha256"] = entry["sha256"]
            doc["fetched"] = entry["fetched"]
            print(f"  [FETCHED] {dest} ({entry['bytes']} bytes)")
            fetched += 1
    if fetched:
        save_manifest(manifest)
        save_registry(reg)
    print(f"FETCH: {fetched} fetched, {skipped} skipped, {failed} failed")
    return 1 if failed else 0


def cmd_register(args):
    src = Path(args.file)
    if not src.exists():
        sys.exit(f"no such file: {src}")
    reg = load_registry()
    target = None
    for slug, subject, q in iter_qualifications(reg):
        if q["code"] == args.code:
            target = (slug, q)
            break
    if target is None:
        sys.exit(f"syllabus code {args.code} is not in the registry")
    slug, q = target

    dest_dir = CAMBRIDGE / slug / "exam_guidelines" / "source"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / src.name
    dest.write_bytes(src.read_bytes())
    manifest = load_manifest()
    entry = record(manifest, url=args.url, path=dest, kind=args.kind,
                   subject=slug, code=args.code)
    save_manifest(manifest)

    docs = q.setdefault("syllabus_documents", [])
    doc = next((d for d in docs if d.get("url") == args.url), None)
    if doc is None:
        doc = {"edition": args.edition or "unknown", "url": args.url,
               "url_status": "registered_from_browser_download"}
        docs.append(doc)
    doc.update(status="fetched_pending_curation", sha256=entry["sha256"],
               fetched=entry["fetched"])
    save_registry(reg)
    print(f"registered {dest}\n  sha256 {entry['sha256']}")
    return 0


def cmd_verify(args):
    manifest = load_manifest()
    if not manifest["entries"]:
        print("manifest is empty — nothing fetched or registered yet")
        return 0
    ok = True
    for e in manifest["entries"]:
        p = Path(e["path"])
        if not p.exists():
            print(f"  [MISSING] {e['path']} (gitignored — re-fetch on a new checkout)")
            continue
        good = sha256_file(p) == e["sha256"]
        ok = ok and good
        print(f"  [{'OK' if good else 'HASH MISMATCH'}] {e['path']}")
        if args.refetch:
            fresh = hashlib.sha256(polite_get(e["url"], binary=True)).hexdigest()
            if fresh != e["sha256"]:
                print(f"    upstream CHANGED since {e['fetched']} — new syllabus "
                      f"edition? re-fetch and re-curate.")
    print("VERIFY OK" if ok else "VERIFY FAILED")
    return 0 if ok else 1


def cmd_past_papers(args):
    """Exists to refuse. See the module docstring."""
    policy = json.loads(POLICY.read_text(encoding="utf-8")) if POLICY.exists() else {}
    pp = policy.get("document_classes", {}).get("past_papers", {})
    print("REFUSED — Cambridge past papers are not fetchable by this project.\n")
    print(f"  Gate:           {pp.get('gate')}")
    print(f"  Public access:  {pp.get('public_access')}  "
          f"(open access is NOT permission — see below)")
    print(f"  Reproduction:   {pp.get('reproduce_electronically')}")
    print(f"  Commercial?:    {pp.get('commercial_or_not')}\n")
    print(f"  Rule:           {pp.get('rule')}\n")
    print(f"  Permission:     {pp.get('permission_route')}\n")
    print("Note what is NOT the blocker here. Cambridge publishes these papers\n"
          "openly on its own site, so this script could technically download\n"
          "them. The blocker is rights, not access: Cambridge refuses\n"
          "electronic reproduction of past-paper questions, mark schemes and\n"
          "examiner reports in any format, and that refusal is not conditioned\n"
          "on commercial use. Being able to fetch a document is not permission\n"
          "to reproduce it, so this subcommand refuses by policy rather than\n"
          "by capability.\n\n"
          "If written permission is ever granted, record the grant (scope,\n"
          "date, signatory, expiry) in CAMBRIDGE/SOURCES.md and narrow\n"
          "RIGHTS.json to exactly what it covers BEFORE writing\n"
          "any ingestion code. audit_tree.py will keep failing the build on\n"
          "past-paper content until the policy says otherwise.")
    return 1


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("probe").set_defaults(func=cmd_probe)

    d = sub.add_parser("discover")
    d.add_argument("--code", required=True, help="syllabus code, e.g. 0580")
    d.add_argument("--url", help="subject landing page to harvest")
    d.add_argument("--html", help="browser-saved copy of the landing page")
    d.set_defaults(func=cmd_discover)

    f = sub.add_parser("fetch-syllabuses")
    f.add_argument("--subject", help="limit to one repo subject slug")
    f.add_argument("--force", action="store_true", help="re-download existing files")
    f.set_defaults(func=cmd_fetch_syllabuses)

    r = sub.add_parser("register")
    r.add_argument("--code", required=True)
    r.add_argument("--url", required=True, help="the URL the file was downloaded from")
    r.add_argument("--file", required=True)
    r.add_argument("--edition")
    r.add_argument("--kind", default="syllabus", choices=["syllabus", "specimen"])
    r.set_defaults(func=cmd_register)

    v = sub.add_parser("verify")
    v.add_argument("--refetch", action="store_true")
    v.set_defaults(func=cmd_verify)

    sub.add_parser("past-papers").set_defaults(func=cmd_past_papers)

    args = ap.parse_args()
    if not CAMBRIDGE.is_dir():
        sys.exit(f"run from the repository root ({CAMBRIDGE} not found)")
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
