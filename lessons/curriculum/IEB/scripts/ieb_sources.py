#!/usr/bin/env python3
"""IEB source index tooling — list / audit / verify / fetch.

IEB-owned counterpart of the CAPS sourcing workflow (this tree's scripts live
here on purpose; lessons/scripts/ stays CAPS/DBE-only). Operates on the index
files under lessons/curriculum/IEB/{subject}/:

  curriculum/index.json          exam_guidelines/sag_index.json
  syllabus/grade{N}.json         skills/{grade}/manifest.json
  past_papers/index.json

Subcommands:
  list    every indexed source URL/document, one line each (offline).
  audit   structural + cross-reference validation (offline, CI-able):
          all five layers present per subject, required keys, every
          caps_* reference resolves to a real file, skills manifests in
          exact sync with the CAPS skills tree. Exit 1 on any failure.
  verify  request each indexed URL and report status; --stamp writes
          last_verified dates back into the index files. ieb.co.za fronts
          the site with bot blocking, so run this from a normal network and
          expect that a 403 here may still be a browser-reachable page —
          the report distinguishes the cases rather than guessing.
  fetch   download pending documents (SAG PDFs, past papers) to their
          fetch_path. PDFs are never committed (../.gitignore); IEB terms
          allow attributed, non-commercial internal use, not redistribution.
"""
import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

IEB_ROOT = Path(__file__).resolve().parent.parent          # lessons/curriculum/IEB
REPO_ROOT = IEB_ROOT.parents[2]                            # repo root
CAPS_ROOT = IEB_ROOT.parent / "CAPS"

SUBJECTS = sorted(p.name for p in IEB_ROOT.iterdir()
                  if p.is_dir() and p.name != "scripts" and not p.name.startswith("."))

LAYERS = ("curriculum", "exam_guidelines", "syllabus", "skills", "past_papers")

# Deliberately identifies itself and gives the IEB a contact route; do not
# disguise this client as a browser. If the front end refuses it, capture the
# URL in a real browser session instead (see scripts/README.md).
USER_AGENT = "rokct-factory-curriculum-sourcing/1.0 (education pipeline; contact: repo owner)"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def save(path, obj):
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def iter_index_files(subject):
    """(kind, path) for every index file a subject is expected to carry."""
    base = IEB_ROOT / subject
    yield "curriculum", base / "curriculum" / "index.json"
    yield "sag", base / "exam_guidelines" / "sag_index.json"
    for f in sorted((base / "syllabus").glob("grade*.json")):
        yield "syllabus", f
    for f in sorted((base / "skills").glob("grade*/manifest.json")):
        yield "skills", f
    yield "past_papers", base / "past_papers" / "index.json"


def collect_sources():
    """Every URL-bearing entry across the tree:
    [(file_path, json_pointer, url, stampable_obj)] where stampable_obj is the
    dict whose last_verified field a --stamp pass updates (None if the entry
    has no such field, e.g. bare portal strings)."""
    out = []
    for subject in SUBJECTS:
        for kind, path in iter_index_files(subject):
            if not path.exists():
                continue
            data = load(path)
            rel = path.relative_to(REPO_ROOT)
            for i, src in enumerate(data.get("sources", [])):
                if src.get("url"):
                    out.append((path, f"sources[{i}]({src.get('id', '?')})", src["url"], src))
            for i, doc in enumerate(data.get("documents", [])):
                if doc.get("url"):
                    out.append((path, f"documents[{i}]({doc.get('id', '?')})", doc["url"], doc))
            for si, sess in enumerate(data.get("sessions", [])):
                for pi, paper in enumerate(sess.get("papers", [])):
                    for field in ("question_paper_url", "memo_url"):
                        if paper.get(field):
                            out.append((path, f"sessions[{si}].papers[{pi}].{field}",
                                        paper[field], paper))
            for field in ("portal",):
                if data.get(field):
                    out.append((path, field, data[field], None))
            del rel
    return out


def cmd_list(args):
    rows = collect_sources()
    for path, pointer, url, _ in rows:
        print(f"{path.relative_to(REPO_ROOT)} :: {pointer} :: {url}")
    print(f"{len(rows)} indexed source reference(s) across {len(SUBJECTS)} subject(s).")
    return 0


# --- audit -----------------------------------------------------------------

REQUIRED_KEYS = {
    "curriculum": ["subject", "curriculum", "content_authority", "caps_reference",
                   "ieb_overlay", "sources", "verified"],
    "sag": ["subject", "curriculum", "document_family", "portal", "documents",
            "ingestion", "verified"],
    "syllabus": ["subject", "grade", "curriculum", "content_authority",
                 "caps_syllabus", "pacing", "scope_deltas", "sources", "parse_status"],
    "skills": ["subject", "grade", "curriculum", "basis", "caveat", "skills"],
    "past_papers": ["subject", "curriculum", "portal", "portal_coverage",
                    "grade_scope", "sessions"],
}


def audit_subject(subject, errors):
    base = IEB_ROOT / subject

    for layer in LAYERS:
        if not (base / layer).is_dir():
            errors.append(f"{subject}: missing layer directory {layer}/")

    seen = {}
    for kind, path in iter_index_files(subject):
        rel = path.relative_to(REPO_ROOT)
        if not path.exists():
            errors.append(f"{rel}: expected index file is missing")
            continue
        try:
            data = load(path)
        except json.JSONDecodeError as e:
            errors.append(f"{rel}: invalid JSON ({e})")
            continue
        seen.setdefault(kind, []).append((path, data))
        for key in REQUIRED_KEYS[kind]:
            if key not in data:
                errors.append(f"{rel}: missing required key '{key}'")
        if data.get("curriculum") != "IEB":
            errors.append(f"{rel}: curriculum must be 'IEB'")

    # Cross-references into the CAPS tree must resolve.
    for path, data in seen.get("curriculum", []):
        rel = path.relative_to(REPO_ROOT)
        for k, p in (data.get("caps_reference") or {}).items():
            if not (REPO_ROOT / p).exists():
                errors.append(f"{rel}: caps_reference.{k} -> {p} does not exist")
        overlay = data.get("ieb_overlay")
        if overlay and not (REPO_ROOT / overlay).exists():
            errors.append(f"{rel}: ieb_overlay -> {overlay} does not exist")

    caps_grades = sorted(int(p.stem.replace("grade", ""))
                         for p in (CAPS_ROOT / subject / "syllabus").glob("grade*.json"))
    ieb_grades = []
    for path, data in seen.get("syllabus", []):
        rel = path.relative_to(REPO_ROOT)
        ieb_grades.append(data.get("grade"))
        ref = data.get("caps_syllabus")
        if ref and not (REPO_ROOT / ref).exists():
            errors.append(f"{rel}: caps_syllabus -> {ref} does not exist")
        deltas = data.get("scope_deltas") or {}
        for i, item in enumerate(deltas.get("items", [])):
            if "source" not in item:
                errors.append(f"{rel}: scope_deltas.items[{i}] has no 'source' — every "
                              f"delta must cite the SAG passage it was transcribed from")
    if sorted(g for g in ieb_grades if g is not None) != caps_grades:
        errors.append(f"{subject}: syllabus grades {sorted(ieb_grades)} != CAPS grades {caps_grades}")

    # Skills manifests must be in exact sync with the CAPS skills tree.
    caps_skill_dirs = {p.name: p for p in sorted((CAPS_ROOT / subject / "skills").glob("grade*"))
                       if p.is_dir()} if (CAPS_ROOT / subject / "skills").exists() else {}
    manifest_dirs = {path.parent.name for path, _ in seen.get("skills", [])}
    for gname in caps_skill_dirs:
        if gname not in manifest_dirs:
            errors.append(f"{subject}: CAPS has skills/{gname} but IEB has no "
                          f"skills/{gname}/manifest.json")
    for gname in manifest_dirs - set(caps_skill_dirs):
        errors.append(f"{subject}: IEB skills/{gname} has no CAPS counterpart")
    for path, data in seen.get("skills", []):
        rel = path.relative_to(REPO_ROOT)
        gname = path.parent.name
        caps_dir = caps_skill_dirs.get(gname)
        if caps_dir is None:
            continue
        caps_refs = {}
        for f in sorted(caps_dir.glob("*.json")):
            caps_refs[load(f)["skill_ref"]] = f
        manifest_refs = {}
        for i, entry in enumerate(data.get("skills", [])):
            for key in ("skill_ref", "name", "caps_path", "transfers"):
                if key not in entry:
                    errors.append(f"{rel}: skills[{i}] missing '{key}'")
            if "caps_path" in entry and not (REPO_ROOT / entry["caps_path"]).exists():
                errors.append(f"{rel}: skills[{i}].caps_path -> {entry['caps_path']} does not exist")
            if "skill_ref" in entry:
                manifest_refs[entry["skill_ref"]] = entry
        for ref in caps_refs.keys() - manifest_refs.keys():
            errors.append(f"{rel}: CAPS skill '{ref}' ({caps_refs[ref].name}) missing from manifest")
        for ref in manifest_refs.keys() - caps_refs.keys():
            errors.append(f"{rel}: manifest lists '{ref}' which no CAPS {gname} skill defines")
        for ref, entry in manifest_refs.items():
            if ref in caps_refs and entry.get("name") != load(caps_refs[ref])["name"]:
                errors.append(f"{rel}: '{ref}' name drifted from CAPS "
                              f"('{entry.get('name')}' != '{load(caps_refs[ref])['name']}')")


def cmd_audit(args):
    errors = []
    if not SUBJECTS:
        errors.append("no subject directories found under lessons/curriculum/IEB")
    caps_subjects = sorted(p.name for p in CAPS_ROOT.iterdir()
                           if p.is_dir() and (p / "syllabus").exists())
    for s in caps_subjects:
        if s not in SUBJECTS:
            errors.append(f"CAPS subject '{s}' has no IEB counterpart directory")
    for subject in SUBJECTS:
        audit_subject(subject, errors)
    for e in errors:
        print(f"  [FAIL] {e}")
    n = sum(1 for s in SUBJECTS for _ in iter_index_files(s))
    print(f"AUDIT {'FAILED' if errors else 'OK'} — {len(SUBJECTS)} subject(s), "
          f"{n} index file(s), {len(errors)} error(s)")
    return 1 if errors else 0


# --- verify / fetch --------------------------------------------------------

def request(url, method, timeout):
    req = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT})
    return urllib.request.urlopen(req, timeout=timeout)


def probe(url, timeout):
    """(status_code_or_None, detail)"""
    for method in ("HEAD", "GET"):
        try:
            with request(url, method, timeout) as resp:
                return resp.status, method
        except urllib.error.HTTPError as e:
            if method == "GET" or e.code not in (403, 405, 501):
                return e.code, method
        except (urllib.error.URLError, OSError, TimeoutError) as e:
            return None, f"{type(e).__name__}: {getattr(e, 'reason', e)}"
    return None, "unreachable"


def cmd_verify(args):
    rows = collect_sources()
    if not rows:
        print("No indexed sources with URLs yet (documents[]/sessions[] are pending "
              "capture — see README.md gap status).")
        return 0
    today = date.today().isoformat()
    ok = blocked = failed = 0
    ok_urls = {}  # path -> set of URLs that answered OK (only these get stamped)
    for path, pointer, url, stampable in rows:
        status, detail = probe(url, args.timeout)
        rel = path.relative_to(REPO_ROOT)
        if status and 200 <= status < 400:
            ok += 1
            print(f"  [OK {status}] {url}  ({rel} :: {pointer})")
            if args.stamp and stampable is not None and "last_verified" in stampable:
                ok_urls.setdefault(path, set()).add(url)
        elif status in (401, 403, 429, 503):
            blocked += 1
            print(f"  [BLOCKED {status}] {url}  ({rel} :: {pointer}) — likely the "
                  f"bot-blocking front end, not a dead link; confirm in a browser")
        else:
            failed += 1
            print(f"  [FAIL {status or detail}] {url}  ({rel} :: {pointer})")
    if args.stamp and ok_urls:
        # collect_sources handed back per-entry references into throwaway
        # parses, so stamp through a fresh load of each touched file.
        for path, urls in ok_urls.items():
            data = load(path)
            for url in urls:
                _stamp_matching(data, url, today)
            save(path, data)
            print(f"  stamped last_verified={today} -> {path.relative_to(REPO_ROOT)}")
    print(f"VERIFY: {ok} ok, {blocked} blocked, {failed} failed of {len(rows)}")
    return 1 if failed else 0


def _stamp_matching(node, url, today):
    if isinstance(node, dict):
        if node.get("url") == url and "last_verified" in node:
            node["last_verified"] = today
        for v in node.values():
            _stamp_matching(v, url, today)
    elif isinstance(node, list):
        for v in node:
            _stamp_matching(v, url, today)


def cmd_fetch(args):
    fetched = skipped = failed = 0
    for subject in SUBJECTS:
        for kind, path in iter_index_files(subject):
            if not path.exists():
                continue
            data = load(path)
            for doc in data.get("documents", []):
                url, fp = doc.get("url"), doc.get("fetch_path")
                if not url or not fp:
                    continue
                host = urllib.parse.urlparse(url).hostname or ""
                if not host.endswith("ieb.co.za") and not args.allow_any_host:
                    print(f"  [SKIP] {url} — host {host} is not ieb.co.za "
                          f"(pass --allow-any-host to override)")
                    skipped += 1
                    continue
                dest = REPO_ROOT / fp
                if dest.exists():
                    print(f"  [HAVE] {dest.relative_to(REPO_ROOT)}")
                    skipped += 1
                    continue
                try:
                    with request(url, "GET", args.timeout) as resp:
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        dest.write_bytes(resp.read())
                    doc["status"] = "fetched"
                    save(path, data)
                    print(f"  [FETCHED] {url} -> {dest.relative_to(REPO_ROOT)}")
                    fetched += 1
                except Exception as e:
                    print(f"  [FAIL] {url} — {type(e).__name__}: {e}")
                    failed += 1
    print(f"FETCH: {fetched} fetched, {skipped} skipped, {failed} failed")
    return 1 if failed else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list").set_defaults(func=cmd_list)
    sub.add_parser("audit").set_defaults(func=cmd_audit)
    v = sub.add_parser("verify")
    v.add_argument("--stamp", action="store_true",
                   help="write last_verified dates back into the index files")
    v.add_argument("--timeout", type=int, default=30)
    v.set_defaults(func=cmd_verify)
    f = sub.add_parser("fetch")
    f.add_argument("--allow-any-host", action="store_true")
    f.add_argument("--timeout", type=int, default=60)
    f.set_defaults(func=cmd_fetch)
    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
