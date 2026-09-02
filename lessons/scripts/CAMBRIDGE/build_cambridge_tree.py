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

"""Materialise the CAMBRIDGE curriculum tree from the verified-facts registry.

Cambridge International is a curriculum AUTHOR, not (like the IEB) a body
that assesses someone else's national curriculum. So nothing here derives
from the CAPS tree: there is no Cambridge counterpart of
IEB/scripts/build_from_caps.py, and CAPS content must never be presented as
Cambridge content. What this generator consumes instead is
`subject_registry.json` — the hand-curated record of Cambridge facts, each
carrying its own source URLs and verification status.

Architecture (deliberately different from the IEB tree, and stricter):

    subject_registry.json  --build_cambridge_tree.py-->  the whole CAMBRIDGE tree
             ^
             |
    fetch_cambridge_sources.py writes fetch status + sha256 back HERE

The registry is the single writer-owned source of truth; the tree is a pure
function of it. The IEB tree had to split ownership between a generator and
a fetch script that mutated the same index files (fixed there by making the
indexes hand-owned); here the conflict cannot arise, because the fetch
script updates facts in the registry and the tree is then regenerated. That
also means `--check` is a total drift gate: every JSON file in the tree is
generated, so any hand edit to the tree is caught.

Generated per subject:
  {subject}/curriculum/cambridge_curriculum.json   qualifications + content authority
  {subject}/syllabus/grade{10,11,12}.json          stage-resolved, content pending ingestion
  {subject}/exam_guidelines/index.json             assessment-document index
  {subject}/skills/{grade}/candidates.json         prerequisite-skill transfer work-list
  {subject}/past_papers/index.json                 access + use-policy record (NOT a link index)

Generated at tree root:
  stage_alignment.json      Cambridge stage <-> repo grade convention
  RIGHTS.json               machine-readable rights posture (policy of record).
                            Same filename and gate vocabulary as
                            ../US/RIGHTS.json so a consumer can walk
                            curriculum/*/RIGHTS.json across every tree.

Usage:
  python3 lessons/scripts/CAMBRIDGE/build_cambridge_tree.py            # write
  python3 lessons/scripts/CAMBRIDGE/build_cambridge_tree.py --check    # drift gate

Run from the repository root. Deterministic: same registry -> byte-identical
tree, so any tree diff traces to a registry change or a generator change.
"""
import argparse
import json
import sys
from pathlib import Path

CAMBRIDGE = Path("lessons/curriculum/CAMBRIDGE")
CAPS = Path("lessons/curriculum/CAPS")
REGISTRY_PATH = Path(__file__).with_name("subject_registry.json")
GENERATED_BY = "lessons/scripts/CAMBRIDGE/build_cambridge_tree.py"
GRADES = (10, 11, 12)

POLICY_REF = "lessons/curriculum/CAMBRIDGE/RIGHTS.json"


def load_registry():
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


# --- root documents --------------------------------------------------------

def build_stage_alignment(reg):
    sa = reg["stage_alignment"]
    return {
        "curriculum": "CAMBRIDGE",
        "purpose": (
            "Resolves this repository's grade10/grade11/grade12 tree contract "
            "against Cambridge International's own stages. Read this before "
            "trusting any grade number in the CAMBRIDGE tree."),
        "problem": sa["problem"],
        "convention_status": sa["convention"],
        "default_pathway": sa["default_pathway"],
        "alternative_pathways": sa["alternative_pathways"],
        "unresolved": sa["unresolved"],
        "stages": reg["stages"],
        "verification": sa["verification"],
        "generated_by": GENERATED_BY,
    }


def build_rights(reg):
    """The policy of record, generated from the registry's researched facts.

    Filename, top-level shape and gate vocabulary deliberately match
    ../US/RIGHTS.json: a consumer walking curriculum/*/RIGHTS.json gets a
    comparable rights posture for every curriculum tree. The keyed unit
    differs (document_classes rather than frameworks) because Cambridge is a
    single rights holder whose permissions differ by document class - the
    registry records why.
    """
    cu = reg["content_use"]
    return {
        "policy_of_record": (
            "Rights posture for everything under lessons/curriculum/CAMBRIDGE. "
            "This file is the machine-readable half of SOURCES.md: "
            "scripts/audit_tree.py reads it and FAILS the build if gated "
            "material lands in the tree. Loosening a gate here is a rights "
            "decision, not a code change - it needs the owner, a written "
            "permission grant recorded in SOURCES.md in the same commit, and "
            "first-hand evidence. A gate may never be loosened on an "
            "assumption."),
        "policy_version": "1.0",
        "curriculum": "CAMBRIDGE",
        "checked": "2026-08-04",
        "rights_holder": cu["rights_holder"],
        "headline": cu["headline"],
        "verification_method": "web_search_only",
        "verification_caveat": reg["_verification_method"],
        "gate_levels": cu["gate_levels"],
        "gate_vocabulary_note": cu["_gate_vocabulary_note"],
        "document_classes": cu["documents"],
        "text_and_data_mining": cu["text_and_data_mining"],
        "third_party_material_inside_papers": cu["third_party_material_inside_papers"],
        "excluded_sources": cu["aggregators"],
        "prohibited_in_this_tree": cu["prohibited_in_this_tree"],
        "pipeline_consequences": [
            {
                "pipeline": ("past-paper worked examples - the CAPS/DBE pattern in "
                             "lessons/scripts/CAPS/past_papers.py"),
                "status": "NOT AVAILABLE for Cambridge",
                "reason": (
                    "That pipeline embeds real past-paper question text, memo working "
                    "and answers into lesson content. For Cambridge that is exactly "
                    "the electronic reproduction Cambridge refuses - and the refusal "
                    "is not conditioned on commercial use, so no reading of our use "
                    "clears it. Ease of access is irrelevant: the papers are openly "
                    "downloadable and still may not be reproduced."),
            },
            {
                "pipeline": "syllabus ingestion - the CAPS ATP / IEB SAG pattern",
                "status": "AVAILABLE, with a shipping gate",
                "reason": (
                    "Syllabus PDFs are public and ingesting them to derive structure "
                    "for internal curriculum mapping is the ordinary use of a "
                    "published syllabus. Shipping substantial syllabus prose in a "
                    "commercial product is a separate question carrying an "
                    "owner_decision_required gate."),
            },
        ],
        "open_questions": reg["_open_questions"],
        "summary_for_owner": cu["summary_for_owner"],
        "generated_by": GENERATED_BY,
    }


# --- per-subject documents -------------------------------------------------

def qualifications_for(subject, stage):
    return [q for q in subject.get("qualifications", []) if q["stage"] == stage]


def build_curriculum(slug, subject):
    return {
        "subject": subject["display"],
        "curriculum": "CAMBRIDGE",
        "curriculum_authority": (
            "Cambridge International Education (Cambridge Assessment "
            "International Education, part of Cambridge University Press & "
            "Assessment) authors its own syllabuses. Unlike the IEB tree - "
            "which assesses the DBE's CAPS curriculum and therefore "
            "references CAPS content - the Cambridge content authority is "
            "the per-subject Cambridge SYLLABUS DOCUMENT itself. No content "
            "in this tree may be derived from, or defaulted to, the CAPS or "
            "IEB trees."),
        "scope": (
            "Global. Cambridge qualifications are taught in schools "
            "worldwide and are not tied to any one country's national "
            "curriculum or school calendar."),
        "equivalence_to_repo_subject": subject["equivalence"],
        "equivalence_note": subject["equivalence_note"],
        "qualifications": [
            {
                "stage": q["stage"],
                "qualification": q["qualification"],
                "title": q["title"],
                "syllabus_code": q["code"],
                "landing_page": q["landing_page"],
                "landing_page_status": q["landing_page_status"],
                "verification": q["verification"],
                "source_urls": q["source_urls"],
            }
            for q in subject.get("qualifications", [])
        ],
        "adjacent_not_mapped": subject.get("adjacent_not_mapped", []),
        **({"primary_mapping": subject["primary_mapping"]}
           if "primary_mapping" in subject else {}),
        **({"consumer_rule": subject["consumer_rule"]}
           if "consumer_rule" in subject else {}),
        "content_status": (
            "pending_syllabus_ingestion: the syllabus documents that carry "
            "the actual curriculum content have not been fetched from this "
            "environment (Cambridge hosts are blocked by egress policy). "
            "Aims, content lists and assessment objectives come from those "
            "documents and are deliberately absent rather than guessed."),
        "rights": POLICY_REF,
        "generated_by": GENERATED_BY,
    }


def build_syllabus(slug, subject, grade, reg):
    """One file per repo grade, stage-resolved through the default pathway."""
    alignment = reg["stage_alignment"]["default_pathway"][f"grade{grade}"]
    quals = qualifications_for(subject, alignment["stage"])

    doc = {
        "subject": subject["display"],
        "grade": grade,
        "curriculum": "CAMBRIDGE",
        "grade_alignment": {
            "status": "REPOSITORY CONVENTION - not a Cambridge statement",
            "resolves_to": alignment,
            "detail": (
                "Cambridge does not number school years the way this tree's "
                "grade contract does; placement is a decision each school "
                "makes. See lessons/curriculum/CAMBRIDGE/stage_alignment.json "
                "for the default pathway, the alternatives, and the "
                "unresolved A2 year."),
            "alignment_document": "lessons/curriculum/CAMBRIDGE/stage_alignment.json",
        },
        "equivalence": subject["equivalence"],
    }

    if subject["equivalence"] == "none":
        doc["qualifications"] = []
        doc["content_status"] = "no_equivalent_qualification"
        doc["equivalence_note"] = subject["equivalence_note"]
        doc["consumer_rule"] = subject["consumer_rule"]
        doc["adjacent_not_mapped"] = subject.get("adjacent_not_mapped", [])
    else:
        doc["qualifications"] = [
            {
                "qualification": q["qualification"],
                "title": q["title"],
                "syllabus_code": q["code"],
                "course_year": alignment.get("course_year"),
                **({"component_of_pair": q["component_of_pair"]}
                   if "component_of_pair" in q else {}),
                "syllabus_documents": q["syllabus_documents"],
                "verification": q["verification"],
            }
            for q in quals
        ]
        doc["content_status"] = (
            "pending_syllabus_ingestion: topic and subtopic content for this "
            "grade comes from the Cambridge syllabus document(s) listed "
            "above, which have not been fetched (Cambridge hosts blocked "
            "from this build environment). No topics are listed because none "
            "have been read from source - an empty list here means 'not yet "
            "ingested', never 'this grade has no content'.")
        doc["topics"] = []
        if subject["equivalence"] == "composite":
            doc["composite_note"] = subject["equivalence_note"]
        if not quals:
            doc["qualification_gap"] = (
                "No qualification in the registry sits at this grade's "
                "resolved stage. That is a registry gap to fill, not "
                "evidence that Cambridge lacks the qualification.")

    doc["caps_relationship"] = (
        "None. Cambridge authors its own curriculum; CAPS topic lists are "
        "NOT a valid fallback for this file.")
    doc["rights"] = POLICY_REF
    doc["generated_by"] = GENERATED_BY
    return doc


def build_exam_guidelines(slug, subject, reg):
    return {
        "subject": subject["display"],
        "curriculum": "CAMBRIDGE",
        "role": (
            "Cambridge has no standalone 'examination guidelines' document "
            "of the DBE kind. The examinable scope, assessment objectives, "
            "paper structure, durations, marks and weightings are printed "
            "INSIDE each Cambridge syllabus document, supplemented by "
            "specimen papers and (for teachers) examiner reports. This index "
            "records where those live for this subject."),
        "assessment_documents": [
            {
                "kind": "syllabus (contains the assessment specification)",
                "public": True,
                "status": "pending_fetch",
                "per_qualification": [
                    {
                        "syllabus_code": q["code"],
                        "qualification": q["qualification"],
                        "landing_page": q["landing_page"],
                        "syllabus_documents": q["syllabus_documents"],
                    }
                    for q in subject.get("qualifications", [])
                ],
            },
            {
                "kind": "specimen / sample assessment materials",
                "public": "unconfirmed",
                "status": "pending_first_hand_check",
                "note": (
                    "Cambridge publishes specimen papers for new syllabus "
                    "editions. Whether they sit on the public subject page "
                    "or only behind the School Support Hub login was NOT "
                    "established from this environment - check on the first "
                    "network-enabled visit. If they are login-gated they "
                    "fall under the same reproduction prohibition as past "
                    "papers."),
            },
            {
                "kind": "examiner reports",
                "public": False,
                "status": "not_obtainable_here",
                "note": (
                    "School Support Hub only (registered centres), and "
                    "named explicitly in Cambridge's refusal of electronic "
                    "reproduction. Do not ingest."),
            },
        ],
        "assessment_structure": {
            "status": "pending_syllabus_ingestion",
            "rule": (
                "Paper counts, durations, marks, tier splits (IGCSE "
                "core/extended) and assessment-objective weightings must be "
                "transcribed from the fetched official syllabus PDF only - "
                "never from a third-party summary or an aggregator site, and "
                "never carried over from the CAPS or IEB exam structures."),
        },
        "exam_series": reg["_exam_series"],
        "rights": POLICY_REF,
        "generated_by": GENERATED_BY,
    }


def caps_skill_refs(slug, grade):
    """CAPS prerequisite skills defined for this subject/grade, if any."""
    d = CAPS / slug / "skills" / f"grade{grade}"
    if not d.is_dir():
        return []
    out = []
    for f in sorted(d.glob("*.json")):
        doc = json.loads(f.read_text(encoding="utf-8"))
        out.append({
            "skill_ref": doc["skill_ref"],
            "name": doc["name"],
            "caps_definition": str(f).replace("\\", "/"),
        })
    return out


def build_skills_candidates(slug, subject, grade):
    """A WORK-LIST, not an inheritance manifest.

    The IEB tree inherits CAPS skills wholesale because the IEB teaches CAPS
    content. Cambridge teaches its own content, so no CAPS skill can be
    declared to transfer until the Cambridge syllabus has been read. Each
    entry is therefore a candidate with transfers=null (unknown), never true.
    """
    candidates = [] if subject["equivalence"] == "none" else caps_skill_refs(slug, grade)
    return {
        "subject": subject["display"],
        "grade": grade,
        "curriculum": "CAMBRIDGE",
        "kind": "transfer_candidate_register",
        "basis": (
            "Prerequisite-skill units that ALREADY EXIST in this "
            "repository's CAPS tree and are plausibly curriculum-neutral "
            "(e.g. laws of exponents, the mole concept, double entry). They "
            "are listed as CANDIDATES for a Cambridge stream so the "
            "curation pass has a work-list - NOT as confirmed transfers."),
        "rules": [
            "transfers is null (unknown) until the Cambridge syllabus for "
            "this subject/stage has been ingested and shown to require the "
            "skill. It may never be set true by assumption.",
            "A CAPS skill's importance.exam_weight (DBE paper section marks) "
            "and covered_by (pointers into CAPS lessons) NEVER transfer - "
            "they describe a different qualification's papers and a "
            "different curriculum's lessons.",
            "Cambridge may require prerequisite skills that CAPS does not "
            "define at all. This register is a starting point, not a "
            "ceiling: new Cambridge-specific skills get authored here after "
            "syllabus ingestion.",
            "Skill teaching content is not duplicated. A confirmed transfer "
            "references the CAPS definition; a Cambridge-specific skill is "
            "authored as its own file in this folder.",
        ],
        "status": "pending_syllabus_ingestion",
        "candidates": [
            {**c, "transfers": None, "transfer_assessment": "pending_syllabus_ingestion"}
            for c in candidates
        ],
        "rights": POLICY_REF,
        "generated_by": GENERATED_BY,
    }


def build_past_papers(slug, subject, reg):
    """Deliberately NOT a link index.

    The CAPS and IEB past-paper indexes list source URLs because those
    bodies publish papers publicly. Cambridge does not: papers sit behind
    the School Support Hub login, and Cambridge refuses electronic
    reproduction of their questions outright. So this file records ACCESS
    and POLICY, and carries no URLs to paper content at all.
    """
    return {
        "subject": subject["display"],
        "curriculum": "CAMBRIDGE",
        "index_kind": "access_and_policy_record",
        "why_not_a_link_index": (
            "The CAPS and IEB trees index public past-paper download URLs "
            "because the DBE and the IEB publish papers openly. Cambridge "
            "does neither: there is no public past-paper download on "
            "Cambridge's own site, and Cambridge refuses permission for "
            "electronic reproduction of past-paper questions in any format. "
            "Recording third-party aggregator URLs instead would mean "
            "sourcing from unauthorised redistributors - excluded by "
            "SOURCES.md - so this file carries no paper URLs by design, not "
            "by omission."),
        "access": {
            "public_download": False,
            "route": (
                "Cambridge School Support Hub (login). Teacher accounts are "
                "created by the school's Support Hub coordinator, so access "
                "presupposes being a registered Cambridge centre."),
            "available_to_this_project": "no_unless_a_registered_centre_account_is_provided",
        },
        "use_policy": {
            "reference": POLICY_REF,
            "summary": (
                "Electronic reproduction of past-paper questions, mark "
                "schemes and examiner reports is prohibited without written "
                "permission from Cambridge - including non-commercial use, "
                "and including publication on a school's own website or "
                "intranet."),
            "worked_example_pipeline": "blocked_pending_written_permission",
        },
        "aggregators_excluded": {
            "rule": (
                "Sites that redistribute Cambridge past papers "
                "(papacambridge, gceguide, dynamicpapers, savemyexams, "
                "physicsandmathstutor and similar) are NOT recorded here and "
                "must not be used as sources. No evidence was found that any "
                "is authorised by Cambridge, and Cambridge's own help "
                "material cites misuse of its material online - including "
                "resale - as the reason it refuses web publication."),
            "recorded_urls": [],
        },
        "sessions": [],
        "sessions_note": (
            "Intentionally empty and expected to STAY empty unless a "
            "written permission grant is obtained and recorded in "
            "SOURCES.md. This is a legal blocker, not a fetch backlog."),
        "if_permission_is_granted": [
            "Record the written grant (scope, date, signatory, expiry) in SOURCES.md before anything else.",
            "Re-read RIGHTS.json and narrow the gate to exactly what the grant covers - never wider.",
            "Only then design an ingestion path; it must live in lessons/scripts/CAMBRIDGE, not lessons/scripts/CAPS.",
        ],
        "generated_by": GENERATED_BY,
    }


# --- assembly --------------------------------------------------------------

def build(reg):
    out = {}
    out[CAMBRIDGE / "stage_alignment.json"] = build_stage_alignment(reg)
    out[CAMBRIDGE / "RIGHTS.json"] = build_rights(reg)
    for slug, subject in reg["subjects"].items():
        base = CAMBRIDGE / slug
        out[base / "curriculum" / "cambridge_curriculum.json"] = build_curriculum(slug, subject)
        out[base / "exam_guidelines" / "index.json"] = build_exam_guidelines(slug, subject, reg)
        out[base / "past_papers" / "index.json"] = build_past_papers(slug, subject, reg)
        for g in GRADES:
            out[base / "syllabus" / f"grade{g}.json"] = build_syllabus(slug, subject, g, reg)
            out[base / "skills" / f"grade{g}" / "candidates.json"] = \
                build_skills_candidates(slug, subject, g)
    return {p: json.dumps(d, indent=2, ensure_ascii=False) + "\n" for p, d in out.items()}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="verify the committed tree matches regeneration; write nothing")
    args = ap.parse_args()
    if not CAPS.is_dir():
        sys.exit(f"run from the repository root ({CAPS} not found)")

    files = build(load_registry())
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
            print(f"DRIFT: {len(drift)} file(s) out of date — edit "
                  f"subject_registry.json (not the tree) and re-run {GENERATED_BY}")
            return 1
        print(f"OK: all {len(files)} generated files match the registry")
    else:
        print(f"generated {len(files)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
