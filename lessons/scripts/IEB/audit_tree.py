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

"""Structural + cross-reference audit of the IEB curriculum tree (offline, CI-able).

One command validates the whole tree; exit 1 on any failure. Two halves:

1. Generated layers ({subject}/curriculum, syllabus/grade*.json, skills/) —
   regenerated in-process via build_from_caps.py and compared byte-for-byte
   (the --check drift gate), PLUS orphan detection the generator cannot do:
   a committed generated file whose CAPS source no longer exists.

2. Hand-owned layers (exam_guidelines/index.json, past_papers/index.json,
   syllabus/scope_deltas.json) — these are seeded once and then mutated by
   fetch_ieb_sources.py and SAG curation passes, so they cannot be
   drift-checked against a generator. Instead their CONTRACT is enforced:
   required keys, documents[] entry shapes (pending / url_recorded /
   fetched), sessions[] in the CAPS shape with primary-source URLs only,
   and scope-delta items that cite the SAG passage they were transcribed
   from (the ledger rule: empty means 'not yet transcribed', never 'no
   differences').

Run after any hand edit to the tree, and in CI next to build_from_caps.py:

  python3 lessons/scripts/IEB/audit_tree.py
"""
import importlib.util
import json
import sys
import urllib.parse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
IEB_ROOT = REPO_ROOT / "lessons" / "curriculum" / "IEB"
CAPS_ROOT = IEB_ROOT.parent / "CAPS"

LAYERS = ("curriculum", "exam_guidelines", "syllabus", "skills", "past_papers")

EXAM_GUIDELINES_KEYS = ("subject", "curriculum", "document_family", "grades",
                        "role", "source_page", "status", "terms_note",
                        "documents", "ingestion")
PAST_PAPERS_KEYS = ("subject", "curriculum", "grade_scope", "portal",
                    "library", "portal_coverage", "marking_guidelines_note",
                    "terms_note", "sessions", "sessions_contract",
                    "captured_links")
SCOPE_DELTAS_KEYS = ("subject", "curriculum", "status", "rule", "items")

ALLOWED_URL_HOSTS = ("ieb.co.za", "www.ieb.co.za", "docs.ieb.co.za")


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path):
    return path.relative_to(REPO_ROOT)


def subjects():
    return sorted(p.name for p in IEB_ROOT.iterdir()
                  if p.is_dir() and p.name != "scripts" and not p.name.startswith("."))


def audit_generated(errors):
    """Drift gate + orphan detection for the generator-owned layers."""
    spec = importlib.util.spec_from_file_location(
        "build_from_caps", Path(__file__).with_name("build_from_caps.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    files = mod.build()  # {Path: text} — everything the generator owns
    owned = set()
    for path, text in files.items():
        owned.add(Path(path).resolve())
        if not Path(path).exists():
            errors.append(f"{path}: generated file missing — run build_from_caps.py")
        elif Path(path).read_text(encoding="utf-8") != text:
            errors.append(f"{path}: drifted from regeneration — run build_from_caps.py")
    # Orphans: committed files in generator-owned locations that the
    # generator no longer produces (e.g. a CAPS skill was deleted/renamed).
    for subject in subjects():
        base = IEB_ROOT / subject
        candidates = (list((base / "curriculum").glob("*.json"))
                      + list((base / "syllabus").glob("grade*.json"))
                      + list((base / "skills").glob("grade*/*.json")))
        for f in candidates:
            if f.resolve() not in owned:
                errors.append(f"{rel(f)}: orphan — in a generator-owned location "
                              f"but no CAPS source generates it (stale after a "
                              f"CAPS deletion/rename?)")


def check_url(errors, where, url, allow_none=False):
    if url is None:
        if not allow_none:
            errors.append(f"{where}: url is null")
        return
    parts = urllib.parse.urlparse(url)
    if parts.scheme != "https":
        errors.append(f"{where}: non-https url {url}")
    elif parts.hostname not in ALLOWED_URL_HOSTS:
        errors.append(f"{where}: host {parts.hostname} is not an IEB primary "
                      f"source ({url}) — third-party re-uploads are excluded "
                      f"by SOURCES.md")


def audit_exam_guidelines(path, errors):
    doc = load(path)
    r = rel(path)
    for k in EXAM_GUIDELINES_KEYS:
        if k not in doc:
            errors.append(f"{r}: missing required key '{k}'")
    if doc.get("curriculum") != "IEB":
        errors.append(f"{r}: curriculum must be 'IEB'")
    for i, d in enumerate(doc.get("documents", [])):
        where = f"{r}: documents[{i}]"
        if "title" not in d:
            errors.append(f"{where}: missing 'title'")
        if "sha256" in d:
            # fetched/registered shape (written by fetch_ieb_sources.py)
            for k in ("source_url", "path", "fetched"):
                if k not in d:
                    errors.append(f"{where}: fetched entry missing '{k}'")
        else:
            # pending / url_recorded shape
            for k in ("status",):
                if k not in d:
                    errors.append(f"{where}: pending entry missing '{k}'")
            if d.get("url") is None and "url_note" not in d:
                errors.append(f"{where}: null url without url_note")
            check_url(errors, where, d.get("url"), allow_none=True)


def audit_past_papers(path, errors):
    doc = load(path)
    r = rel(path)
    for k in PAST_PAPERS_KEYS:
        if k not in doc:
            errors.append(f"{r}: missing required key '{k}'")
    if doc.get("curriculum") != "IEB":
        errors.append(f"{r}: curriculum must be 'IEB'")
    for si, sess in enumerate(doc.get("sessions", [])):
        where = f"{r}: sessions[{si}]"
        if "session" not in sess:
            errors.append(f"{where}: missing 'session'")
        for pi, paper in enumerate(sess.get("papers", [])):
            pwhere = f"{where}.papers[{pi}]"
            if "paper" not in paper:
                errors.append(f"{pwhere}: missing 'paper'")
            if "question_paper_url" not in paper:
                errors.append(f"{pwhere}: missing 'question_paper_url'")
            for field in ("question_paper_url", "memo_url"):
                if field in paper:
                    check_url(errors, f"{pwhere}.{field}", paper[field])


def audit_scope_deltas(path, errors):
    doc = load(path)
    r = rel(path)
    for k in SCOPE_DELTAS_KEYS:
        if k not in doc:
            errors.append(f"{r}: missing required key '{k}'")
    for i, item in enumerate(doc.get("items", [])):
        for k in ("grade", "statement", "source"):
            if k not in item:
                errors.append(f"{r}: items[{i}] missing '{k}' — every delta "
                              f"must cite the SAG passage it came from")


def audit_subject(subject, errors):
    base = IEB_ROOT / subject
    for layer in LAYERS:
        if not (base / layer).is_dir():
            errors.append(f"{subject}: missing layer directory {layer}/")

    # Every JSON in the subject tree must parse.
    for f in sorted(base.rglob("*.json")):
        try:
            load(f)
        except json.JSONDecodeError as e:
            errors.append(f"{rel(f)}: invalid JSON ({e})")

    # Hand-owned contracts.
    for path, fn in (
            (base / "exam_guidelines" / "index.json", audit_exam_guidelines),
            (base / "past_papers" / "index.json", audit_past_papers),
            (base / "syllabus" / "scope_deltas.json", audit_scope_deltas)):
        if not path.exists():
            errors.append(f"{rel(path)}: expected hand-owned file is missing")
            continue
        try:
            fn(path, errors)
        except json.JSONDecodeError:
            pass  # already reported by the parse sweep

    # Skills: exact two-way sync with the CAPS tree, refs and pointers intact.
    caps_skills = CAPS_ROOT / subject / "skills"
    caps_files = {f.relative_to(caps_skills): f
                  for f in sorted(caps_skills.glob("grade*/*.json"))} if caps_skills.is_dir() else {}
    ieb_skills = base / "skills"
    ieb_files = {f.relative_to(ieb_skills): f
                 for f in sorted(ieb_skills.glob("grade*/*.json"))} if ieb_skills.is_dir() else {}
    for missing in sorted(set(caps_files) - set(ieb_files)):
        errors.append(f"{subject}: CAPS skill {missing} has no IEB pointer file")
    for extra in sorted(set(ieb_files) - set(caps_files)):
        errors.append(f"{subject}: IEB skill pointer {extra} has no CAPS counterpart")
    for name in sorted(set(caps_files) & set(ieb_files)):
        try:
            caps_doc, ieb_doc = load(caps_files[name]), load(ieb_files[name])
        except json.JSONDecodeError:
            continue
        r = rel(ieb_files[name])
        if ieb_doc.get("skill_ref") != caps_doc.get("skill_ref"):
            errors.append(f"{r}: skill_ref '{ieb_doc.get('skill_ref')}' != CAPS "
                          f"'{caps_doc.get('skill_ref')}'")
        if ieb_doc.get("name") != caps_doc.get("name"):
            errors.append(f"{r}: name drifted from CAPS")
        inherits = ieb_doc.get("inherits_from")
        if not inherits or not (REPO_ROOT / inherits).exists():
            errors.append(f"{r}: inherits_from -> {inherits} does not exist")

    # Curriculum pointer must resolve into the CAPS tree.
    curr = base / "curriculum" / "ieb_gr10-12.json"
    if curr.exists():
        try:
            doc = load(curr)
            for k, v in (doc.get("caps_reference") or {}).items():
                if k != "source_url" and not (REPO_ROOT / v).exists():
                    errors.append(f"{rel(curr)}: caps_reference.{k} -> {v} does not exist")
        except json.JSONDecodeError:
            pass


def main():
    errors = []
    subs = subjects()
    if not subs:
        errors.append(f"no subject directories under {rel(IEB_ROOT)}")
    caps_subjects = sorted(p.name for p in CAPS_ROOT.iterdir()
                           if p.is_dir() and (p / "syllabus").is_dir())
    for s in caps_subjects:
        if s not in subs:
            errors.append(f"CAPS subject '{s}' has no IEB counterpart directory")
    for s in subs:
        if s not in caps_subjects:
            errors.append(f"IEB subject '{s}' has no CAPS counterpart")

    gitignore = IEB_ROOT / ".gitignore"
    if not gitignore.exists() or "*.pdf" not in gitignore.read_text(encoding="utf-8"):
        errors.append(f"{rel(gitignore)}: missing or does not ignore *.pdf "
                      f"(copyrighted source PDFs must never be committed)")

    audit_generated(errors)
    for s in subs:
        audit_subject(s, errors)

    for e in errors:
        print(f"  [FAIL] {e}")
    n_files = sum(1 for s in subs for _ in (IEB_ROOT / s).rglob("*.json"))
    print(f"AUDIT {'FAILED' if errors else 'OK'} — {len(subs)} subject(s), "
          f"{n_files} json file(s), {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
