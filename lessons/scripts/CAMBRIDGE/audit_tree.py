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

"""Audit the CAMBRIDGE curriculum tree (offline, CI-able, exit 1 on failure).

Four independent checks. The last one is the important one and is the reason
this script exists rather than relying on build_cambridge_tree.py --check alone.

1. STRUCTURE      every subject carries the five layers; the tree's subject
                  set is deliberate (documented divergence from CAPS/IEB is
                  allowed, silent divergence is not).

2. TOTAL DRIFT    every JSON file in the tree is generated from
                  subject_registry.json, so the tree must match regeneration
                  exactly AND contain no file the generator does not own.
                  Facts are edited in the registry, never in the tree.

3. REGISTRY       provenance contract: nothing claims 'corroborated' without
                  >= 2 source_urls; every recorded URL carries a url_status;
                  every URL points at a Cambridge host (never an aggregator).

3b. RIGHTS        RIGHTS.json is well-formed, every document class declares a
                  gate defined in gate_levels, every closed gate gives a
                  rationale, and the assessment-material gates are still
                  closed. Same shape and vocabulary as ../US/RIGHTS.json.

4. CONTENT GUARD  the legal one. Cambridge prohibits electronic reproduction
                  of past-paper questions, mark schemes and examiner reports
                  (see ../RIGHTS.json and ../SOURCES.md). This
                  check fails the build if such material - or an unauthorised
                  aggregator URL, or a committed source PDF - ever appears in
                  the tree, so the prohibition survives edits by people who
                  never read the policy. It also catches CAPS content copied
                  into Cambridge syllabus files, which would be a different
                  curriculum's data wearing a Cambridge label.

  python3 lessons/scripts/CAMBRIDGE/audit_tree.py
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
CAMBRIDGE = REPO_ROOT / "lessons" / "curriculum" / "CAMBRIDGE"
CAPS_ROOT = CAMBRIDGE.parent / "CAPS"
REGISTRY = Path(__file__).with_name("subject_registry.json")

LAYERS = ("curriculum", "exam_guidelines", "syllabus", "skills", "past_papers")

# Hosts a URL in this tree may point at. Cambridge primary sources only, plus
# the British Council syllabus-list PDFs used as a corroborating second source
# for syllabus codes (a public body's copy of Cambridge's own subject list,
# recorded as corroboration only - never as a document source to fetch).
ALLOWED_HOSTS = {
    "www.cambridgeinternational.org",
    "cambridgeinternational.org",
    "help.cambridgeinternational.org",
    "schoolsupporthub.cambridge.org",
    "www.cambridge.org",
    "cambridge.org",
    "www.britishcouncil.lk",
}

# Unauthorised redistributors of Cambridge material. Their presence anywhere
# in the tree is a sourcing failure, not a style issue.
AGGREGATOR_SIGNALS = (
    "papacambridge", "gceguide", "dynamicpapers", "savemyexams",
    "physicsandmathstutor", "paper.sc", "bestexamhelp", "studocu",
    "scribd", "studypool", "xtremepapers", "smartedu", "revisionworld",
)

# Field names the CAPS past-paper pipeline writes (lessons/scripts/past_papers.py
# and its paper.json extractions). If any of these appear in the Cambridge
# tree, someone has started ingesting exam-paper content here.
PAST_PAPER_CONTENT_FIELDS = (
    "memo_answer", "memo_working", "solution_method", "paper_id",
    "scene_data", "recompute", "checkable", "past_paper_examples",
    "question_paper_url", "memo_url",
)


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path):
    return path.relative_to(REPO_ROOT)


def subjects():
    return sorted(p.name for p in CAMBRIDGE.iterdir()
                  if p.is_dir() and p.name != "scripts" and not p.name.startswith("."))


def walk_strings(node, path="$"):
    """(json_pointer, string) for every string anywhere in a document."""
    if isinstance(node, dict):
        for k, v in node.items():
            yield from walk_strings(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk_strings(v, f"{path}[{i}]")
    elif isinstance(node, str):
        yield path, node


def walk_keys(node, path="$"):
    if isinstance(node, dict):
        for k, v in node.items():
            yield f"{path}.{k}", k
            yield from walk_keys(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk_keys(v, f"{path}[{i}]")


URL_RE = re.compile(r"https?://([^/\s\"')]+)")


# --- 1. structure ----------------------------------------------------------

def check_structure(errors):
    subs = subjects()
    if not subs:
        errors.append(f"no subject directories under {rel(CAMBRIDGE)}")
        return
    reg = load(REGISTRY)
    registry_subs = sorted(reg["subjects"])
    if subs != registry_subs:
        errors.append(f"tree subjects {subs} != registry subjects {registry_subs}")
    for s in subs:
        for layer in LAYERS:
            if not (CAMBRIDGE / s / layer).is_dir():
                errors.append(f"{s}: missing layer directory {layer}/")
        for g in (10, 11, 12):
            if not (CAMBRIDGE / s / "skills" / f"grade{g}").is_dir():
                errors.append(f"{s}: missing skills/grade{g}/")

    # Divergence from the CAPS subject set must be deliberate: every CAPS
    # subject needs either a Cambridge counterpart or a registry entry saying
    # why it has no equivalent.
    caps_subs = sorted(p.name for p in CAPS_ROOT.iterdir()
                       if p.is_dir() and (p / "syllabus").is_dir())
    for s in caps_subs:
        if s not in subs:
            errors.append(f"CAPS subject '{s}' has no CAMBRIDGE counterpart "
                          f"and no registry record explaining its absence")
        elif reg["subjects"][s]["equivalence"] == "none" and \
                not reg["subjects"][s].get("consumer_rule"):
            errors.append(f"{s}: equivalence 'none' requires a consumer_rule "
                          f"telling consumers what to do instead")


# --- 2. total drift --------------------------------------------------------

def check_drift(errors):
    spec = importlib.util.spec_from_file_location(
        "build_cambridge_tree", Path(__file__).with_name("build_cambridge_tree.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    files = mod.build(mod.load_registry())
    owned = {Path(p).resolve() for p in files}
    for path, text in files.items():
        p = Path(path)
        if not p.exists():
            errors.append(f"{path}: generated file missing — run build_cambridge_tree.py")
        elif p.read_text(encoding="utf-8") != text:
            errors.append(f"{path}: drifted — edit subject_registry.json, not the tree")
    for f in sorted(CAMBRIDGE.rglob("*.json")):
        if f.resolve() in owned or f.parent.name == "scripts":
            continue
        errors.append(f"{rel(f)}: not generated by build_cambridge_tree.py. Every JSON in "
                      f"this tree is generated; add the fact to "
                      f"subject_registry.json instead of hand-writing a file "
                      f"(ingested source documents get their own non-.json "
                      f"home and a manifest entry).")


# --- 3. registry provenance ------------------------------------------------

def check_registry(errors):
    reg = load(REGISTRY)
    r = "scripts/subject_registry.json"
    for slug, subject in reg["subjects"].items():
        for q in subject.get("qualifications", []):
            where = f"{r}: {slug} {q.get('code', '?')}"
            if q.get("verification") == "corroborated" and len(q.get("source_urls", [])) < 2:
                errors.append(f"{where}: claims 'corroborated' with "
                              f"{len(q.get('source_urls', []))} source_url(s) — "
                              f"needs >= 2 independent sources")
            if q.get("landing_page") and not q.get("landing_page_status"):
                errors.append(f"{where}: landing_page without landing_page_status")
            for d in q.get("syllabus_documents", []):
                if d.get("url") and not d.get("url_status"):
                    errors.append(f"{where}: syllabus document url without url_status")
                if d.get("url") and not d.get("status"):
                    errors.append(f"{where}: syllabus document url without fetch status")
        if subject["equivalence"] == "none" and subject.get("qualifications"):
            errors.append(f"{r}: {slug} declares equivalence 'none' but lists "
                          f"qualifications")


# --- 4. content guard (the legal one) --------------------------------------

def check_rights(errors):
    """RIGHTS.json is the policy of record; its own contract is checked first."""
    path = CAMBRIDGE / "RIGHTS.json"
    if not path.exists():
        errors.append(f"{rel(path)}: missing — the tree has no policy of record")
        return
    try:
        rights = load(path)
    except json.JSONDecodeError as e:
        errors.append(f"{rel(path)}: invalid JSON ({e})")
        return
    for key in ("policy_of_record", "policy_version", "rights_holder",
                "verification_method", "gate_levels", "document_classes",
                "prohibited_in_this_tree", "summary_for_owner"):
        if key not in rights:
            errors.append(f"{rel(path)}: missing top-level key '{key}'")
    levels = rights.get("gate_levels", {})
    for name, block in (rights.get("document_classes") or {}).items():
        gate = block.get("gate")
        if gate is None:
            errors.append(f"{rel(path)}: document class '{name}' declares no gate")
        elif gate not in levels:
            errors.append(f"{rel(path)}: document class '{name}' gate '{gate}' is "
                          f"not defined in gate_levels")
        if gate == "blocked_pending_written_permission" and not block.get("gate_rationale"):
            errors.append(f"{rel(path)}: '{name}' is blocked but carries no "
                          f"gate_rationale — a closed gate must say why")
    # A closed gate on assessment material is the whole point of this tree's
    # guard; if someone opens it, that must be a deliberate, evidenced act.
    for name in ("past_papers", "mark_schemes_examiner_reports"):
        block = (rights.get("document_classes") or {}).get(name, {})
        if block.get("gate") != "blocked_pending_written_permission":
            errors.append(
                f"{rel(path)}: '{name}' gate is '{block.get('gate')}', not "
                f"'blocked_pending_written_permission'. Cambridge refuses electronic "
                f"reproduction of this material; loosening this gate requires a written "
                f"permission grant recorded in SOURCES.md and first-hand evidence.")


def check_content_guard(errors):
    gitignore = CAMBRIDGE / ".gitignore"
    if not gitignore.exists() or "*.pdf" not in gitignore.read_text(encoding="utf-8"):
        errors.append(f"{rel(gitignore)}: missing or does not ignore *.pdf — "
                      f"fetched Cambridge source documents must never be committed")

    for stray in list(CAMBRIDGE.rglob("*.pdf")):
        errors.append(f"{rel(stray)}: a Cambridge source PDF is committed. "
                      f"Remove it — Cambridge material may not be redistributed.")

    caps_topic_index = _caps_topic_index()

    for f in sorted(CAMBRIDGE.rglob("*.json")):
        if f.parent.name == "scripts" and f.name != "subject_registry.json":
            continue
        try:
            doc = load(f)
        except json.JSONDecodeError as e:
            errors.append(f"{rel(f)}: invalid JSON ({e})")
            continue

        # (a) exam-paper content fields
        for pointer, key in walk_keys(doc):
            if key in PAST_PAPER_CONTENT_FIELDS:
                errors.append(
                    f"{rel(f)}: field '{key}' at {pointer} is past-paper "
                    f"pipeline content. Cambridge prohibits electronic "
                    f"reproduction of past-paper questions, mark schemes and "
                    f"examiner reports without written permission — see "
                    f"RIGHTS.json. Remove it, or record the "
                    f"written grant in SOURCES.md first.")

        # (b) aggregator references and non-Cambridge hosts
        for pointer, s in walk_strings(doc):
            low = s.lower()
            for sig in AGGREGATOR_SIGNALS:
                if sig in low:
                    # Naming an aggregator in an exclusion rule is the point of
                    # that rule; a URL to one is a sourcing failure.
                    if f"://{sig}" in low or f".{sig}." in low or f"//www.{sig}" in low:
                        errors.append(
                            f"{rel(f)}: URL to unauthorised redistributor "
                            f"'{sig}' at {pointer} — excluded by SOURCES.md")
            for host in URL_RE.findall(s):
                if host not in ALLOWED_HOSTS:
                    errors.append(
                        f"{rel(f)}: URL host '{host}' at {pointer} is not an "
                        f"approved Cambridge source host")

        # (c) CAPS content copied into Cambridge syllabus files
        if f.parent.name == "syllabus" and f.name.startswith("grade"):
            topics = doc.get("topics")
            if topics:
                slug = f.parents[1].name
                grade = doc.get("grade")
                caps_topics = caps_topic_index.get((slug, grade))
                names = {t.get("name") for t in topics if isinstance(t, dict)}
                if caps_topics and names and names <= caps_topics:
                    errors.append(
                        f"{rel(f)}: topic list is a subset of the CAPS "
                        f"grade{grade} topics for '{slug}'. Cambridge authors "
                        f"its own curriculum — content must come from the "
                        f"Cambridge syllabus, never from CAPS.")


def _caps_topic_index():
    """{(subject, grade): {topic names}} from the CAPS syllabus files."""
    index = {}
    for sub_dir in sorted(CAPS_ROOT.iterdir()):
        syl = sub_dir / "syllabus"
        if not syl.is_dir():
            continue
        for f in sorted(syl.glob("grade*.json")):
            try:
                doc = load(f)
            except json.JSONDecodeError:
                continue
            names = set()
            for term in doc.get("terms", []):
                for t in term.get("topics", []):
                    if isinstance(t, dict) and t.get("name"):
                        names.add(t["name"])
            if names:
                index[(sub_dir.name, doc.get("grade"))] = names
    return index


def main():
    errors = []
    check_structure(errors)
    check_drift(errors)
    check_registry(errors)
    check_rights(errors)
    check_content_guard(errors)
    for e in errors:
        print(f"  [FAIL] {e}")
    n = sum(1 for _ in CAMBRIDGE.rglob("*.json"))
    print(f"AUDIT {'FAILED' if errors else 'OK'} — {len(subjects())} subject(s), "
          f"{n} json file(s), {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
