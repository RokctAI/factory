#!/usr/bin/env python3
# Copyright (c) 2026 RokctAI
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Offline, CI-able audit of the US curriculum tree. Exit 1 on any failure.

This is the contract keeper. It runs nine checks:

  1. RIGHTS.json is well-formed and every framework declares a known gate.
  2. Generated layers match regeneration (drift check).
  3. No orphaned files - every committed file is either generator-owned,
     a declared hand-owned index, or documentation.
  4. RIGHTS GATE: a framework gated `blocked_pending_written_permission` must
     have EMPTY content arrays everywhere. This is the check that matters -
     it turns the rights decision into something CI enforces rather than
     something a future contributor has to remember.
  5. Excluded sources: no file cites a domain the audit excluded (the
     unofficial Common Core mirror, CED summarisers, question re-uploads).
  6. Attribution: every generated file under a framework carries that
     framework's rights block with the correct notice.
  7. Layout contract: required folders present; past_papers/ present exactly
     where the spec says it should be and absent where it should not.
  8. Hand-owned index contracts: required keys present.
  9. No copyrighted source PDFs committed.

Usage:
    python3 lessons/scripts/US/audit_tree.py
    python3 lessons/scripts/US/audit_tree.py --verbose
"""

import argparse
import fnmatch
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import us_spec as S  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
US_ROOT = os.path.join(REPO_ROOT, "lessons", "curriculum", "US")

FAILURES = []
NOTES = []

# Files that are allowed to NAME an excluded source, because naming it is the
# whole point: they are the audit records that exclude it.
EXCLUSION_SCAN_EXEMPT = {"RIGHTS.json", "SOURCES.md", "README.md"}

# Domains that must never appear as a source anywhere in the tree.
EXCLUDED_DOMAINS = [
    "thecorestandards.org",
    "studocu.com",
    "scribd.com",
    "coursehero.com",
    "uworld.com",
    "edisonos.com",
    "sparkl.me",
    "clacenter.com",
    "galvanizetestprep.com",
    "testprepkart.com",
    "oneprep.com",
    "catalysttestprep.com",
    "makon.ai",
    "ttprep.com",
    "testprepscout.com",
]

# Keys whose value must be an empty list while a framework's gate is closed.
GATED_LIST_KEYS = [
    "sessions", "captured_links", "documents", "units", "course_skills",
    "testing_points", "topics", "questions", "papers",
]


def fail(msg):
    FAILURES.append(msg)


def rel(path):
    return os.path.relpath(path, REPO_ROOT).replace(os.sep, "/")


def us_rel(path):
    return os.path.relpath(path, US_ROOT).replace(os.sep, "/")


def walk_files(root=US_ROOT):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in ("__pycache__", ".git")]
        for fn in sorted(filenames):
            yield os.path.join(dirpath, fn)


def load_json(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except Exception as exc:  # noqa: BLE001
        fail("{}: not valid JSON ({})".format(rel(path), exc))
        return None


def iter_strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from iter_strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from iter_strings(v)


def find_lists(obj, key):
    """Yield every value stored under `key` anywhere in a nested structure."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == key:
                yield v
            yield from find_lists(v, key)
    elif isinstance(obj, list):
        for v in obj:
            yield from find_lists(v, key)


# ---------------------------------------------------------------------------
# 1. RIGHTS.json
# ---------------------------------------------------------------------------

def check_rights(verbose):
    path = os.path.join(US_ROOT, "RIGHTS.json")
    if not os.path.exists(path):
        fail("RIGHTS.json is missing - the tree has no policy of record.")
        return None
    rights = load_json(path)
    if rights is None:
        return None

    for key in ("policy_version", "checked", "verification_method",
                "gate_levels", "frameworks", "summary_for_owner"):
        if key not in rights:
            fail("RIGHTS.json: missing top-level key '{}'".format(key))

    levels = rights.get("gate_levels", {})
    for fw in S.FRAMEWORKS:
        if fw not in rights.get("frameworks", {}):
            fail("RIGHTS.json: framework '{}' not declared".format(fw))
            continue
        block = rights["frameworks"][fw]
        for key in ("rights_holder", "gate", "attribution_notice",
                    "commercial_reproduction", "primary_sources", "verdict"):
            if key not in block:
                fail("RIGHTS.json[{}]: missing key '{}'".format(fw, key))
        gate = block.get("gate")
        if gate not in levels:
            fail("RIGHTS.json[{}]: gate '{}' is not defined in gate_levels".format(fw, gate))
        if gate == "blocked_pending_written_permission" and not block.get("gated_paths"):
            fail("RIGHTS.json[{}]: gate is closed but gated_paths is empty - "
                 "nothing would actually be enforced.".format(fw))

    if verbose:
        NOTES.append("rights: {} frameworks declared, verification_method={}".format(
            len(rights.get("frameworks", {})), rights.get("verification_method")))
    return rights


# ---------------------------------------------------------------------------
# 2. drift
# ---------------------------------------------------------------------------

def check_drift(verbose):
    res = subprocess.run(
        [sys.executable, os.path.join(HERE, "build_us_tree.py"), "--check"],
        capture_output=True, text=True, cwd=REPO_ROOT)
    if res.returncode != 0:
        fail("generated-layer drift:\n" + (res.stdout or res.stderr).rstrip())
    elif verbose:
        NOTES.append("drift: " + res.stdout.strip())


# ---------------------------------------------------------------------------
# 3. orphans
# ---------------------------------------------------------------------------

def expected_paths():
    """Every path the tree is supposed to contain."""
    expected = set()
    layout = S.subtree_layout()
    for fw, subjects in layout.items():
        for subject, meta in subjects.items():
            base = "{}/{}".format(fw, subject)
            expected.add("{}/exam_guidelines/index.json".format(base))
            for g in meta["grades"]:
                expected.add("{}/syllabus/{}".format(base, S.grade_filename(g)))
            if meta["past_papers"]:
                expected.add("{}/past_papers/index.json".format(base))
    # generator-specific files
    expected.update({
        "COMMON_CORE/math/curriculum/ccss_math_k-12.json",
        "COMMON_CORE/ela/curriculum/ccss_ela_k-12.json",
        "NGSS/science/curriculum/ngss_k-12.json",
        "AP/courses.json",
    })
    for c, _ in S.CCSS_MATH_PRACTICES:
        expected.add("COMMON_CORE/math/skills/practices/{}.json".format(c.lower()))
    for k, _t, _n in S.CCSS_ELA_ANCHORS:
        expected.add("COMMON_CORE/ela/skills/practices/{}_anchors.json".format(k))
    for c, _ in S.NGSS_PRACTICES:
        expected.add("NGSS/science/skills/practices/{}.json".format(c.lower()))
    for c, _ in S.NGSS_CROSSCUTTING:
        expected.add("NGSS/science/skills/crosscutting/{}.json".format(c.lower()))
    for fw, subjects in layout.items():
        for subject, meta in subjects.items():
            for g in meta["grades"]:
                sub = "course" if g == "course" else "grade{}".format(g)
                expected.add("{}/{}/skills/{}/index.json".format(fw, subject, sub))
    for slug, _t, _c in S.AP_SCAFFOLDED_COURSES:
        expected.add("AP/{}/curriculum/ced.json".format(slug))
    for slug in S.SAT_SECTIONS:
        expected.add("SAT/{}/curriculum/sat_suite.json".format(slug))
    return expected


DOC_ALLOWLIST = {
    "README.md", "SOURCES.md", "RIGHTS.json", ".gitignore",
    "scripts/README.md", "scripts/us_spec.py", "scripts/build_us_tree.py",
    "scripts/audit_tree.py", "scripts/fetch_us_sources.py",
    "COMMON_CORE/README.md", "NGSS/README.md", "AP/README.md", "SAT/README.md",
    "sources_manifest.json",
}


def check_orphans(verbose):
    expected = expected_paths()
    found = set()
    for path in walk_files():
        r = us_rel(path)
        if r.endswith(".pyc"):
            continue
        found.add(r)
    unexpected = sorted(
        f for f in found
        if f not in expected and f not in DOC_ALLOWLIST
        and not f.endswith(".md")          # curated full-text lands beside indexes
        and not f.startswith("scripts/")
    )
    for f in unexpected:
        fail("orphan: {} is neither generator-owned nor a declared hand-owned "
             "file. If it is new curation, add it to the spec or the "
             "allowlist.".format(f))
    missing = sorted(f for f in expected if f not in found)
    for f in missing:
        fail("missing expected file: {}".format(f))
    if verbose:
        NOTES.append("layout: {} expected files present".format(len(expected)))


# ---------------------------------------------------------------------------
# 4. the rights gate
# ---------------------------------------------------------------------------

def path_matches(rel_path, patterns):
    return any(fnmatch.fnmatch(rel_path, p) for p in patterns)


def check_gate(rights, verbose):
    if not rights:
        return
    enforced = 0
    for fw, block in rights["frameworks"].items():
        if block.get("gate") != "blocked_pending_written_permission":
            continue
        patterns = block.get("gated_paths", [])
        for path in walk_files(os.path.join(US_ROOT, fw)):
            if not path.endswith(".json"):
                continue
            r = us_rel(path)
            if not path_matches(r, patterns):
                continue
            enforced += 1
            data = load_json(path)
            if data is None:
                continue
            for key in GATED_LIST_KEYS:
                for value in find_lists(data, key):
                    if isinstance(value, list) and value:
                        fail("RIGHTS GATE VIOLATION: {} has a non-empty '{}' "
                             "({} item(s)) while {} is gated "
                             "'blocked_pending_written_permission'. Content "
                             "from this rights holder may not be ingested "
                             "until written permission is recorded in "
                             "RIGHTS.json.".format(r, key, len(value), fw))
        # A closed gate must not have fetched sources either.
        manifest = os.path.join(US_ROOT, fw, "sources_manifest.json")
        if os.path.exists(manifest):
            fail("RIGHTS GATE VIOLATION: {}/sources_manifest.json exists - "
                 "documents were fetched from a rights holder whose gate is "
                 "closed.".format(fw))
    if verbose:
        NOTES.append("gate: {} gated file(s) checked and clean".format(enforced))


# ---------------------------------------------------------------------------
# 5. excluded sources
# ---------------------------------------------------------------------------

def check_excluded_sources(verbose):
    hits = 0
    for path in walk_files():
        base = us_rel(path)
        if base in EXCLUSION_SCAN_EXEMPT or os.path.basename(path) in EXCLUSION_SCAN_EXEMPT:
            continue
        if base.startswith("scripts/"):
            continue
        if not path.endswith(".json"):
            continue
        data = load_json(path)
        if data is None:
            continue
        for text in iter_strings(data):
            for dom in EXCLUDED_DOMAINS:
                if dom in text:
                    hits += 1
                    fail("excluded source cited: {} references '{}', which "
                         "SOURCES.md excludes. Use the primary source."
                         .format(base, dom))
    if verbose and not hits:
        NOTES.append("sources: no excluded domain cited anywhere in the tree")


# ---------------------------------------------------------------------------
# 6. attribution
# ---------------------------------------------------------------------------

def check_attribution(rights, verbose):
    if not rights:
        return
    checked = 0
    for fw, block in rights["frameworks"].items():
        notice = block.get("attribution_notice")
        patterns = block.get("must_carry_notice_paths", [])
        if not patterns:
            continue
        for path in walk_files(os.path.join(US_ROOT, fw)):
            if not path.endswith(".json"):
                continue
            r = us_rel(path)
            if not path_matches(r, patterns):
                continue
            data = load_json(path)
            if not isinstance(data, dict):
                continue
            if "generated_by" not in data:
                continue          # hand-owned files are checked in check_indexes
            rb = data.get("rights")
            if not isinstance(rb, dict):
                fail("attribution: {} carries no rights block".format(r))
                continue
            if rb.get("attribution_notice") != notice:
                fail("attribution: {} has a stale or missing notice - it must "
                     "match RIGHTS.json[{}].attribution_notice verbatim"
                     .format(r, fw))
            if rb.get("gate") != block.get("gate"):
                fail("attribution: {} records gate '{}' but RIGHTS.json says "
                     "'{}' - regenerate.".format(r, rb.get("gate"), block.get("gate")))
            checked += 1
    if verbose:
        NOTES.append("attribution: {} generated file(s) carry a correct rights block".format(checked))


# ---------------------------------------------------------------------------
# 7. layout contract
# ---------------------------------------------------------------------------

def check_layout(verbose):
    layout = S.subtree_layout()
    for fw, subjects in layout.items():
        for subject, meta in subjects.items():
            base = os.path.join(US_ROOT, fw, subject)
            for folder in ("curriculum", "exam_guidelines", "syllabus", "skills"):
                if not os.path.isdir(os.path.join(base, folder)):
                    fail("layout: {}/{} is missing required folder '{}'"
                         .format(fw, subject, folder))
            pp = os.path.join(base, "past_papers")
            if meta["past_papers"] and not os.path.isdir(pp):
                fail("layout: {}/{} should have past_papers/ but does not"
                     .format(fw, subject))
            if not meta["past_papers"] and os.path.isdir(pp):
                fail("layout: {}/{} must NOT have past_papers/ - it is a "
                     "standards framework with no examining body. An empty "
                     "folder here would imply papers exist and are merely "
                     "un-indexed.".format(fw, subject))
    if verbose:
        NOTES.append("layout: folder contract satisfied for all subjects")


# ---------------------------------------------------------------------------
# 8. hand-owned index contracts
# ---------------------------------------------------------------------------

def check_indexes(verbose):
    layout = S.subtree_layout()
    n = 0
    for fw, subjects in layout.items():
        for subject, meta in subjects.items():
            eg = os.path.join(US_ROOT, fw, subject, "exam_guidelines", "index.json")
            if os.path.exists(eg):
                data = load_json(eg)
                if isinstance(data, dict):
                    if "maintained_by" not in data:
                        fail("index contract: {} lacks 'maintained_by' - the "
                             "ownership rule must be stated in the file itself."
                             .format(us_rel(eg)))
                    if "documents" not in data:
                        fail("index contract: {} lacks 'documents'".format(us_rel(eg)))
                    n += 1
            if not meta["past_papers"]:
                continue
            pp = os.path.join(US_ROOT, fw, subject, "past_papers", "index.json")
            if os.path.exists(pp):
                data = load_json(pp)
                if isinstance(data, dict):
                    for key in ("sessions", "sessions_contract", "status", "maintained_by"):
                        if key not in data:
                            fail("index contract: {} lacks '{}'".format(us_rel(pp), key))
                    n += 1
    if verbose:
        NOTES.append("indexes: {} hand-owned index(es) satisfy their contract".format(n))


# ---------------------------------------------------------------------------
# 9. no committed PDFs
# ---------------------------------------------------------------------------

def check_no_pdfs(verbose):
    found = [us_rel(p) for p in walk_files() if p.lower().endswith(".pdf")]
    for f in found:
        fail("copyrighted source PDF committed: {} - .gitignore blocks *.pdf; "
             "fetched documents stay local, only the manifest is committed."
             .format(f))
    if verbose and not found:
        NOTES.append("pdfs: none committed (correct)")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    rights = check_rights(args.verbose)
    check_drift(args.verbose)
    check_orphans(args.verbose)
    check_gate(rights, args.verbose)
    check_excluded_sources(args.verbose)
    check_attribution(rights, args.verbose)
    check_layout(args.verbose)
    check_indexes(args.verbose)
    check_no_pdfs(args.verbose)

    for note in NOTES:
        print("  " + note)

    if FAILURES:
        print("\nAUDIT FAILED - {} problem(s):\n".format(len(FAILURES)))
        for f in FAILURES:
            print("  * " + f)
        return 1
    print("\nAUDIT PASSED - US curriculum tree is internally consistent and "
          "every rights gate is respected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
