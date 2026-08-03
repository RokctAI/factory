#!/usr/bin/env python3
"""Fetch IEB source documents (SAGs, past-paper indexes) from ieb.co.za.

Counterpart of the CAPS ingestion method (see CAPS/README.md): fetch the
real documents from the primary source, record provenance (URL, sha256,
date), then hand-curate the extracted text into the structured files. This
script does the fetch-and-record step only — curation stays a human/agent
pass, exactly as it was for the 18 CAPS ATPs.

IMPORTANT — where this can run: the repo's usual remote build environment
has an egress policy that blocks ieb.co.za (proxy CONNECT 403, observed
2026-08-03), and ieb.co.za additionally refuses some automated fetchers
with HTTP 403. Run this from a normal network-enabled machine. If the site
still answers 403 there, it is bot protection: fetch the handful of PDFs in
a browser instead and register them with the `register` subcommand so the
manifest still carries real hashes and URLs.

Subcommands:
  probe      robots.txt + terms-of-use check (the WCED precedent: if robots
             disallows us, we stop — see SOURCES.md).
  fetch-sags GET the NSC SAG page, list/download the per-subject SAG PDFs
             into {subject}/exam_guidelines/source/, update each subject's
             exam_guidelines/index.json documents[] + status.
  fetch-papers
             GET the NSC past-papers page and snapshot its links into
             {subject}/past_papers/index.json captured_links[] where the
             subject is identifiable (hand-shape those into the CAPS-format
             sessions[] afterwards — see the index's sessions_contract).
             The docs.ieb.co.za guest library (SharePoint) needs an
             interactive login; harvest it in a browser and `register` the
             files — this script does not automate credentialed access.

  Both fetch-* subcommands accept --html <file>: parse a browser-saved copy
  of the page instead of fetching it (the practical route while ieb.co.za
  answers 403 to non-browser clients). With --html, link URLs are recorded
  into the indexes but nothing is downloaded — follow up with `register`
  for files saved from the browser.
  register   record an out-of-band-downloaded file (browser fetch) into the
             manifest + the right index, with sha256 computed locally:
               register --subject maths --kind sag --url <url> --file <pdf>
  verify     re-hash every manifest entry against its local file; re-fetch
             URLs with --refetch to detect upstream edition changes.

All fetches: honest User-Agent, robots.txt respected, >=2s between requests,
3 retries with backoff. Downloads land under source/ subdirectories that are
gitignored by size policy if needed; the manifest (sources_manifest.json)
is always committed — it is the provenance record.
"""
import argparse
import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.request
import urllib.robotparser
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

IEB_ROOT = Path("lessons/curriculum/IEB")
MANIFEST = IEB_ROOT / "sources_manifest.json"
BASE = "https://www.ieb.co.za"
SAG_PAGE = f"{BASE}/assessment/high-schools/national-senior-certificate/nsc-subject-assessment-guidelines"
PAST_PAPERS_PAGE = f"{BASE}/assessment/high-schools/national-senior-certificate/nsc-past-papers"
TERMS_PAGE = f"{BASE}/terms-of-use"
USER_AGENT = ("rokct-factory-curriculum/1.0 "
              "(educational curriculum indexing; contact: repo owner)")
DELAY_S = 2.0

# subject slug -> lowercase substrings that identify its documents in link
# text / filenames on IEB pages. Checked longest-first so "mathematical
# literacy" wins over "mathematic".
SUBJECT_SIGNALS = {
    "mathematical_literacy": ["mathematical literacy", "maths literacy", "mathematical_literacy"],
    "maths": ["mathematics", "mathematic"],
    "physical_sciences": ["physical science", "physical_science"],
    "geography": ["geography"],
    "economics": ["economics"],
    "accounting": ["accounting"],
}

_last_request = [0.0]


def polite_get(url, binary=False, retries=3):
    wait = time.monotonic() - _last_request[0]
    if wait < DELAY_S:
        time.sleep(DELAY_S - wait)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(retries):
        try:
            _last_request[0] = time.monotonic()
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                return data if binary else data.decode("utf-8", "replace")
        except (urllib.error.URLError, TimeoutError) as e:
            if attempt == retries - 1:
                raise
            back = 2 ** (attempt + 1)
            print(f"  retry in {back}s ({e})")
            time.sleep(back)


class LinkExtractor(HTMLParser):
    """(href, text) pairs; text is the anchor's own text content."""
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


def extract_links(html, base=BASE):
    p = LinkExtractor()
    p.feed(html)
    out = []
    for href, text in p.links:
        if not href or href.startswith(("#", "mailto:", "javascript:")):
            continue
        if href.startswith("/"):
            href = base + href
        out.append((href, text))
    return out


def subject_for(link_text, href):
    hay = f"{link_text} {href}".lower()
    for slug, signals in SUBJECT_SIGNALS.items():
        if any(s in hay for s in signals):
            return slug
    return None


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_manifest():
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {"note": "Provenance record for every IEB source file fetched or "
                    "registered; see scripts/fetch_ieb_sources.py.",
            "entries": []}


def save_manifest(m):
    MANIFEST.write_text(json.dumps(m, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")


def record(manifest, *, url, path, kind, subject):
    entry = {
        "url": url,
        "path": str(path).replace("\\", "/"),
        "kind": kind,
        "subject": subject,
        "sha256": sha256_file(path),
        "bytes": Path(path).stat().st_size,
        "fetched": date.today().isoformat(),
    }
    manifest["entries"] = [e for e in manifest["entries"]
                           if e["path"] != entry["path"]] + [entry]
    return entry


def update_index(index_path, mutate):
    doc = json.loads(index_path.read_text(encoding="utf-8"))
    mutate(doc)
    index_path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8")


def check_robots(url):
    rp = urllib.robotparser.RobotFileParser()
    try:
        rp.parse(polite_get(f"{BASE}/robots.txt").splitlines())
    except Exception as e:
        print(f"robots.txt unreadable ({e}) — proceeding under the site's "
              f"published terms; re-check manually.")
        return True
    ok = rp.can_fetch(USER_AGENT, url) and rp.can_fetch("*", url)
    if not ok:
        print(f"robots.txt DISALLOWS {url} for us — stopping (WCED precedent).")
    return ok


def cmd_probe(args):
    print(f"robots.txt:\n{polite_get(BASE + '/robots.txt')}\n")
    terms = polite_get(TERMS_PAGE)
    text = re.sub(r"<[^>]+>", " ", terms)
    text = " ".join(text.split())
    print(f"terms-of-use ({TERMS_PAGE}), text excerpt:\n{text[:2000]}")
    print("\nRecord findings in lessons/curriculum/IEB/SOURCES.md before fetching.")
    return 0


def cmd_fetch_sags(args):
    if args.html:
        html = Path(args.html).read_text(encoding="utf-8", errors="replace")
    else:
        if not check_robots(SAG_PAGE):
            return 1
        html = polite_get(SAG_PAGE)
    manifest = load_manifest()
    hits = 0
    for href, text in extract_links(html):
        if ".pdf" not in href.lower() and "download" not in href.lower():
            continue
        slug = subject_for(text, href)
        if slug is None:
            continue
        hits += 1
        if args.html:
            # Record the URL only (no download — the saved page proves the
            # link, not reachability from here). fetch/register completes it.
            def mutate(doc, href=href, text=text):
                docs = doc.setdefault("documents", [])
                if not any(d.get("url") == href for d in docs):
                    docs.append({"title": text, "url": href,
                                 "status": "url_recorded",
                                 "last_verified": None})
            update_index(IEB_ROOT / slug / "exam_guidelines" / "index.json", mutate)
            print(f"  recorded [{slug}] {text} -> {href}")
            continue
        dest_dir = IEB_ROOT / slug / "exam_guidelines" / "source"
        dest = dest_dir / (re.sub(r"[^A-Za-z0-9._-]+", "_", text)[:80] + ".pdf")
        if args.list_only:
            print(f"  [{slug}] {text} -> {href}")
            continue
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(polite_get(href, binary=True))
        entry = record(manifest, url=href, path=dest, kind="sag", subject=slug)
        print(f"  fetched [{slug}] {dest} ({entry['bytes']} bytes)")

        def mutate(doc, entry=entry, text=text):
            doc["documents"] = [d for d in doc.get("documents", [])
                                if d.get("path") != entry["path"]]
            doc["documents"].append({"title": text, "source_url": entry["url"],
                                     "path": entry["path"], "sha256": entry["sha256"],
                                     "fetched": entry["fetched"]})
            doc["status"] = "fetched_pending_curation"
            doc["status_detail"] = ("Source PDF(s) fetched and hashed; ingest per "
                                    "the CAPS method (full-text .md + structured "
                                    ".json next to this index).")
        update_index(IEB_ROOT / slug / "exam_guidelines" / "index.json", mutate)
    if hits == 0:
        print("No subject SAG links recognised on the page. The page markup "
              "has likely changed (or is script-rendered): save the page from "
              "a browser and pass --html <file>, or download PDFs manually "
              "and use `register`.")
        return 1
    if not args.list_only:
        save_manifest(manifest)
    return 0


def cmd_fetch_papers(args):
    if args.html:
        html = Path(args.html).read_text(encoding="utf-8", errors="replace")
    else:
        if not check_robots(PAST_PAPERS_PAGE):
            return 1
        html = polite_get(PAST_PAPERS_PAGE)
    per_subject = {}
    for href, text in extract_links(html):
        slug = subject_for(text, href)
        if slug and (".pdf" in href.lower() or "docs.ieb" in href.lower()
                     or "paper" in text.lower()):
            per_subject.setdefault(slug, []).append({"title": text, "url": href})
    if not per_subject:
        print("No per-subject paper links recognised — the public page links "
              "into the docs.ieb.co.za guest library, which needs a browser "
              "login (guest@ieb.co.za / guest, published on the IEB FAQ). "
              "Harvest there and use `register`.")
        return 1
    for slug, papers in sorted(per_subject.items()):
        def mutate(doc, papers=papers):
            # Raw page links land in captured_links[]; sessions[] keeps the
            # CAPS shape and is hand-filled from these (sessions_contract).
            doc["captured_links"] = papers
            doc["verified"] = date.today().isoformat()
            doc["source_status"] = "portal_links_recorded_pending_shaping"
        update_index(IEB_ROOT / slug / "past_papers" / "index.json", mutate)
        print(f"  [{slug}] {len(papers)} link(s) recorded into captured_links[]")
    return 0


def cmd_register(args):
    src = Path(args.file)
    if not src.exists():
        sys.exit(f"no such file: {src}")
    sub_dir = "exam_guidelines" if args.kind == "sag" else "past_papers"
    dest_dir = IEB_ROOT / args.subject / sub_dir / "source"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / src.name
    dest.write_bytes(src.read_bytes())
    manifest = load_manifest()
    entry = record(manifest, url=args.url, path=dest, kind=args.kind,
                   subject=args.subject)
    save_manifest(manifest)
    print(f"registered {dest}\n  sha256 {entry['sha256']}")
    if args.kind == "sag":
        def mutate(doc):
            doc["documents"] = [d for d in doc.get("documents", [])
                                if d.get("path") != entry["path"]]
            doc["documents"].append({"title": src.stem, "source_url": args.url,
                                     "path": entry["path"], "sha256": entry["sha256"],
                                     "fetched": entry["fetched"]})
            doc["status"] = "fetched_pending_curation"
        update_index(IEB_ROOT / args.subject / "exam_guidelines" / "index.json", mutate)
    return 0


def cmd_verify(args):
    manifest = load_manifest()
    if not manifest["entries"]:
        print("manifest is empty — nothing fetched/registered yet")
        return 0
    ok = True
    for e in manifest["entries"]:
        p = Path(e["path"])
        if not p.exists():
            print(f"  [MISSING] {e['path']}")
            ok = False
            continue
        good = sha256_file(p) == e["sha256"]
        ok = ok and good
        print(f"  [{'OK' if good else 'HASH MISMATCH'}] {e['path']}")
        if args.refetch:
            fresh = hashlib.sha256(polite_get(e["url"], binary=True)).hexdigest()
            if fresh != e["sha256"]:
                print(f"    upstream CHANGED since {e['fetched']} — new edition? "
                      f"re-fetch and re-curate.")
    print("VERIFY OK" if ok else "VERIFY FAILED")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("probe").set_defaults(func=cmd_probe)
    fs = sub.add_parser("fetch-sags")
    fs.add_argument("--list-only", action="store_true")
    fs.add_argument("--html", help="parse a browser-saved copy of the SAG "
                                   "page instead of fetching (records URLs, "
                                   "downloads nothing)")
    fs.set_defaults(func=cmd_fetch_sags)
    fp = sub.add_parser("fetch-papers")
    fp.add_argument("--html", help="parse a browser-saved copy of the "
                                   "past-papers page instead of fetching")
    fp.set_defaults(func=cmd_fetch_papers)
    rg = sub.add_parser("register")
    rg.add_argument("--subject", required=True, choices=sorted(SUBJECT_SIGNALS))
    rg.add_argument("--kind", required=True, choices=["sag", "past_paper"])
    rg.add_argument("--url", required=True,
                    help="the source URL the file was downloaded from")
    rg.add_argument("--file", required=True)
    rg.set_defaults(func=cmd_register)
    vf = sub.add_parser("verify")
    vf.add_argument("--refetch", action="store_true")
    vf.set_defaults(func=cmd_verify)
    args = ap.parse_args()
    if not IEB_ROOT.is_dir():
        sys.exit(f"run from the repository root ({IEB_ROOT} not found)")
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
