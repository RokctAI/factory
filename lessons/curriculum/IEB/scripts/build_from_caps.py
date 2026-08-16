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

"""Generate the derivable layers of the IEB curriculum tree from the CAPS tree.

The IEB examines the National Senior Certificate on the same DBE CAPS
curriculum; what differs is assessment (the IEB Subject Assessment
Guidelines — SAGs) and pacing (the IEB publishes no ATP equivalent; schools
set their own). So three IEB layers are *derived*, not hand-authored:

  {subject}/curriculum/ieb_gr10-12.json   pointer at the shared CAPS policy
                                          statement + the pending SAG overlay
  {subject}/syllabus/grade{N}.json        CAPS content scope (topics,
                                          subtopics, prior knowledge, weeks,
                                          skills links) with every
                                          DBE-assessment-specific field
                                          (sba, sba_weighting, sba_guidelines,
                                          control_test_scope, exam_structure)
                                          stripped — those are SAG territory
  {subject}/skills/{grade}/{skill}.json   inheritance pointers at the CAPS
                                          skill files (skill content is
                                          curriculum-neutral; only the DBE
                                          exam_weight block does not carry)

Ownership split — the generator owns ONLY the three CAPS-derived layers
above. The assessment-layer indexes ({subject}/exam_guidelines/index.json,
{subject}/past_papers/index.json) and the per-subject scope-delta ledgers
({subject}/syllabus/scope_deltas.json) are hand-owned: they are seeded once
and then mutated by fetch_ieb_sources.py (fetch/register runs record
documents, hashes and links into them) and by SAG curation passes. Putting
them under the generator would clobber that recorded data on the next
regenerate — audit_tree.py validates their contract instead. Ingested
documents likewise get their own files next to the index (e.g.
exam_guidelines/sag_2026.md); the generator never touches files it does
not own.

Usage:
  python3 lessons/curriculum/IEB/scripts/build_from_caps.py            # write
  python3 lessons/curriculum/IEB/scripts/build_from_caps.py --check    # drift
                                          check: exit 1 if a committed file
                                          differs from regeneration (run after
                                          editing the CAPS tree)

Run from the repository root. Deterministic: same CAPS input -> byte-identical
output, so diffs in generated files always trace to a CAPS change or a
generator change.
"""
import argparse
import json
import sys
from pathlib import Path

CAPS = Path("lessons/curriculum/CAPS")
IEB = Path("lessons/curriculum/IEB")

# Subject slug -> display name for the assessment-facing layers (matches the
# CAPS exam_guidelines/past_papers naming, e.g. "Mathematics" not "Maths").
SUBJECTS = {
    "maths": "Mathematics",
    "mathematical_literacy": "Mathematical Literacy",
    "physical_sciences": "Physical Sciences",
    "geography": "Geography",
    "economics": "Economics",
    "accounting": "Accounting",
}

GRADES = (10, 11, 12)

GENERATED_BY = "lessons/curriculum/IEB/scripts/build_from_caps.py"

SAG_PAGE = ("https://www.ieb.co.za/assessment/high-schools/"
            "national-senior-certificate/nsc-subject-assessment-guidelines")

# DBE-assessment machinery that does not apply to IEB assessment. The IEB
# SAG replaces all of it; carrying DBE values into IEB files would be wrong
# data, not a helpful default (unlike pacing, where the ATP weeks are a
# reasonable default for a school that must pace the same content somehow).
DBE_ONLY_TOP_KEYS = ("sba_weighting", "sba_guidelines", "exam_structure")
DBE_ONLY_TERM_KEYS = ("sba", "control_test_scope")


def _subtopic_name(sub):
    """CAPS subtopic entries are plain strings, or objects carrying
    factory-pipeline directives (e.g. {"name": ..., "tutors": [...]}).
    Those directives steer lesson generation, not curriculum content, so
    only the name string carries into the derived IEB tree (mirrors
    _subtopic_name in lessons/scripts/lesson_pipeline.py — tutors and any
    other non-name keys are stripped)."""
    return sub.get("name", "") if isinstance(sub, dict) else sub


def derive_syllabus(caps_doc):
    terms = []
    for t in caps_doc["terms"]:
        nt = {k: v for k, v in t.items() if k not in DBE_ONLY_TERM_KEYS}
        if nt.get("topics"):
            topics = []
            for topic in nt["topics"]:
                ntopic = dict(topic)
                if ntopic.get("subtopics"):
                    ntopic["subtopics"] = [_subtopic_name(s)
                                           for s in ntopic["subtopics"]]
                topics.append(ntopic)
            nt["topics"] = topics
        terms.append(nt)
    out = {
        "subject": caps_doc["subject"],
        "grade": caps_doc["grade"],
        "curriculum": "IEB",
        "content_basis": "CAPS",
        "caps_source": str(CAPS / caps_doc["_slug"] / "syllabus"
                           / f"grade{caps_doc['grade']}.json").replace("\\", "/"),
        "caps_atp_edition": caps_doc["atp_edition"],
        "caps_source_url": caps_doc["source_url"],
        "parse_status": "derived_from_caps",
        "generated_by": GENERATED_BY,
        "pacing_note": (
            "The IEB publishes no ATP equivalent; term placement and week "
            "spans are the DBE ATP pacing carried over as a default. IEB "
            "schools set their own pacing — treat weeks as advisory."),
        "assessment_note": (
            "DBE SBA programmes, control-test scopes and exam structures are "
            "deliberately stripped: IEB assessment is specified by the IEB "
            "Subject Assessment Guidelines (see ../exam_guidelines/), which "
            "have not been ingested yet. Do not fall back to the CAPS "
            "exam_structure for IEB papers."),
        "scope_deltas": (
            "SAG-stated content-scope differences vs the CAPS/DBE "
            "prescription are recorded in scope_deltas.json in this folder "
            "(hand-maintained, SAG-transcribed only; an empty ledger means "
            "'not yet transcribed', never 'no differences')."),
        "terms": terms,
    }
    if "notes" in caps_doc:
        out["caps_notes"] = caps_doc["notes"]
    return out


def derive_curriculum(slug, display):
    caps_curr = CAPS / slug / "curriculum" / "caps_gr10-12.json"
    caps_meta = json.loads(caps_curr.read_text(encoding="utf-8"))
    return {
        "subject": display,
        "curriculum": "IEB",
        "document": caps_meta["document"],
        "content_authority": (
            "The IEB administers the National Senior Certificate on the DBE "
            "CAPS curriculum; the content policy statement is the same CAPS "
            "document, maintained once in the CAPS tree."),
        "caps_reference": {
            "metadata": str(caps_curr).replace("\\", "/"),
            "full_text": str(caps_curr.with_suffix(".md")).replace("\\", "/"),
            "source_url": caps_meta["source_url"],
        },
        "ieb_overlay": {
            "document": f"IEB Subject Assessment Guidelines (SAG): {display}",
            "role": (
                "Defines IEB-specific assessment: SBA composition, exam "
                "paper structure, cognitive-level weightings, and any "
                "content emphases that differ from DBE assessment. Reissued "
                "for each examination year."),
            "source_page": SAG_PAGE,
            "status": "pending_fetch",
            "fetch_with": "lessons/curriculum/IEB/scripts/fetch_ieb_sources.py",
        },
        "generated_by": GENERATED_BY,
    }


def derive_skill_pointer(slug, grade_dir, skill_path):
    caps_skill = json.loads(skill_path.read_text(encoding="utf-8"))
    return {
        "skill_ref": caps_skill["skill_ref"],
        "name": caps_skill["name"],
        "subject": caps_skill["subject"],
        "grade": caps_skill["grade"],
        "curriculum": "IEB",
        "inherits_from": str(skill_path).replace("\\", "/"),
        "inheritance": (
            "full — the skill's teaching content (example_problem, "
            "diagnostic, recap, exit check, covered_by, requires chain) is "
            "curriculum-neutral and maintained once, in the CAPS file. "
            "skill_ref is kept identical so requires_skills links in the "
            "IEB syllabus files resolve against the same skill."),
        "overrides_pending": [
            "importance.exam_weight — the CAPS block cites DBE paper "
            "sections/marks, which do not describe IEB papers; re-derive "
            "from the IEB SAG exam structure once ingested. Until then "
            "consumers must not show DBE marks in an IEB context.",
        ],
        "generated_by": GENERATED_BY,
    }


def build():
    """-> {relative_path: json_text} for every file this generator owns."""
    out = {}
    for slug, display in SUBJECTS.items():
        base = IEB / slug
        # curriculum pointer
        out[base / "curriculum" / "ieb_gr10-12.json"] = derive_curriculum(slug, display)
        # syllabus, one per grade, from the CAPS file
        for g in GRADES:
            src = CAPS / slug / "syllabus" / f"grade{g}.json"
            caps_doc = json.loads(src.read_text(encoding="utf-8"))
            caps_doc["_slug"] = slug
            out[base / "syllabus" / f"grade{g}.json"] = derive_syllabus(caps_doc)
        # skills pointers, mirroring exactly the grades CAPS defines
        skills_root = CAPS / slug / "skills"
        if skills_root.is_dir():
            for grade_dir in sorted(skills_root.iterdir()):
                if not grade_dir.is_dir():
                    continue
                for skill_path in sorted(grade_dir.glob("*.json")):
                    out[base / "skills" / grade_dir.name / skill_path.name] = \
                        derive_skill_pointer(slug, grade_dir, skill_path)
    return {p: json.dumps(d, indent=2, ensure_ascii=False) + "\n" for p, d in out.items()}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="verify committed files match regeneration; write nothing")
    args = ap.parse_args()
    if not CAPS.is_dir():
        sys.exit(f"run from the repository root ({CAPS} not found)")

    files = build()
    drift = []
    for path, text in sorted(files.items()):
        if args.check:
            if not path.exists():
                drift.append(f"MISSING  {path}")
            elif path.read_text(encoding="utf-8") != text:
                drift.append(f"DIFFERS  {path}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
            print(f"wrote {path}")
    if args.check:
        if drift:
            print("\n".join(drift))
            print(f"DRIFT: {len(drift)} generated file(s) out of date — "
                  f"re-run {GENERATED_BY}")
            return 1
        print(f"OK: all {len(files)} generated files match the CAPS tree")
    else:
        print(f"generated {len(files)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
