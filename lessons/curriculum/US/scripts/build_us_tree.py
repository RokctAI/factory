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

"""Generate the derivable layers of the US curriculum tree.

Ownership split, copied deliberately from the IEB tree so the two behave the
same way:

  GENERATED (this script owns, overwrites freely, --check verifies)
      {framework}/{subject}/curriculum/*.json
      {framework}/{subject}/syllabus/*.json
      {framework}/{subject}/skills/**/*.json
      AP/courses.json

  HAND-OWNED (seeded once when absent, then never touched again)
      {framework}/{subject}/exam_guidelines/index.json
      {framework}/{subject}/past_papers/index.json

The seed-once rule is the whole point: those two indexes are where fetch
provenance and rights decisions get recorded, so a regenerate must never be
able to clobber them. This script writes a hand-owned file only if it does not
already exist, and `--check` deliberately does not compare them.

Usage:
    python3 lessons/curriculum/US/scripts/build_us_tree.py
    python3 lessons/curriculum/US/scripts/build_us_tree.py --check
"""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import us_spec as S  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
US_ROOT = os.path.dirname(HERE)
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(US_ROOT)))
GENERATOR = "lessons/curriculum/US/scripts/build_us_tree.py"

_written = []
_skipped_handowned = []
_drift = []


def rel(path):
    return os.path.relpath(path, REPO_ROOT).replace(os.sep, "/")


def dump(obj):
    return json.dumps(obj, indent=2, ensure_ascii=False) + "\n"


def write_generated(path, obj, check):
    text = dump(obj)
    if check:
        if not os.path.exists(path):
            _drift.append("MISSING: {}".format(rel(path)))
        elif open(path, encoding="utf-8").read() != text:
            _drift.append("DRIFTED: {}".format(rel(path)))
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    _written.append(rel(path))


def seed_handowned(path, obj, check):
    """Write only if absent. Never overwrite - this is provenance territory."""
    if os.path.exists(path):
        _skipped_handowned.append(rel(path))
        return
    if check:
        _drift.append("MISSING (hand-owned seed): {}".format(rel(path)))
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(dump(obj))
    _written.append(rel(path) + "  [seeded]")


def load_rights():
    with open(os.path.join(US_ROOT, "RIGHTS.json"), encoding="utf-8") as fh:
        return json.load(fh)


# ---------------------------------------------------------------------------
# shared blocks
# ---------------------------------------------------------------------------

def rights_block(rights, framework):
    fw = rights["frameworks"][framework]
    block = {
        "rights_holder": fw["rights_holder"],
        "gate": fw["gate"],
        "gate_meaning": rights["gate_levels"][fw["gate"]],
        "attribution_notice": fw["attribution_notice"],
        "policy_of_record": "lessons/curriculum/US/RIGHTS.json",
        "audit": "lessons/curriculum/US/SOURCES.md",
    }
    if fw["gate"] == "blocked_pending_written_permission":
        block["ai_use"] = fw["ai_use"]
        block["blocked_note"] = (
            "Nothing from this rights holder may be transcribed into this "
            "subtree, or passed to a model, until written permission is "
            "obtained. Structure, links and metadata only."
        )
    return block


def pending(reason):
    return {
        "status": "pending_source_ingest",
        "reason": reason,
        "rule": (
            "An empty list here means 'not yet transcribed from the official "
            "source', never 'the framework has none'. Consumers must treat a "
            "pending layer as absent rather than as an empty curriculum."
        ),
    }


# ---------------------------------------------------------------------------
# COMMON CORE
# ---------------------------------------------------------------------------

def build_common_core(rights, check):
    root = os.path.join(US_ROOT, "COMMON_CORE")
    src = rights["frameworks"]["COMMON_CORE"]["primary_sources"]
    rb = rights_block(rights, "COMMON_CORE")

    # --- curriculum -------------------------------------------------------
    write_generated(os.path.join(root, "math", "curriculum", "ccss_math_k-12.json"), {
        "subject": "Mathematics",
        "framework": "Common Core State Standards",
        "framework_type": "content_standards",
        "document": "Common Core State Standards for Mathematics",
        "jurisdiction": "United States - adopted state by state; not a federal curriculum",
        "grade_span": "K-12",
        "rights": rb,
        "architecture": {
            "standards_for_mathematical_practice": [
                {"code": c, "statement": t} for c, t in S.CCSS_MATH_PRACTICES
            ],
            "practice_note": (
                "The eight practice standards are stated identically at every "
                "grade K-12. They are modelled once, in ../skills/practices/, "
                "rather than duplicated per grade."
            ),
            "content_organisation": (
                "K-8 by grade, each grade divided into domains, each domain "
                "into clusters, each cluster into numbered standards. High "
                "school is organised into conceptual categories that span "
                "grades 9-12 instead of by grade."
            ),
            "identifier_grammar": (
                "Grade-level standards are cited as CCSS.MATH.CONTENT.<grade>."
                "<domain>.<cluster letter>.<number>, e.g. CCSS.MATH.CONTENT.5."
                "NF.A.1. High school swaps the grade for the conceptual "
                "category, e.g. CCSS.MATH.CONTENT.HSA.REI.B.3. Practice "
                "standards are CCSS.MATH.PRACTICE.MP1 ... MP8."
            ),
            "domains_by_grade": {
                g: [{"code": c, "name": n} for c, n in S.CCSS_MATH_DOMAINS[g]]
                for g in S.CCSS_MATH_GRADES
            },
        },
        "source": {
            "site": src["site"],
            "pdf": src["math_pdf"],
            "ccsso_mirror_pdf": src["ccsso_mirror_math_pdf"],
            "status": "urls_recorded_not_verified",
            "fetch_with": "lessons/curriculum/US/scripts/fetch_us_sources.py",
        },
        "full_text": pending(
            "The standards PDF has not been fetched: this environment's egress "
            "policy blocks corestandards.org. Once fetched, curate as "
            "ccss_math_k-12.md (full decoded text) beside this file, following "
            "the CAPS ATP method."
        ),
        "generated_by": GENERATOR,
    }, check)

    write_generated(os.path.join(root, "ela", "curriculum", "ccss_ela_k-12.json"), {
        "subject": "English Language Arts and Literacy",
        "framework": "Common Core State Standards",
        "framework_type": "content_standards",
        "document": ("Common Core State Standards for English Language Arts & "
                     "Literacy in History/Social Studies, Science, and "
                     "Technical Subjects"),
        "jurisdiction": "United States - adopted state by state; not a federal curriculum",
        "grade_span": "K-12",
        "rights": rb,
        "architecture": {
            "anchor_standards": [
                {"strand": k, "title": t, "count": n}
                for k, t, n in S.CCSS_ELA_ANCHORS
            ],
            "anchor_note": (
                "The College and Career Readiness anchor standards are the "
                "cross-grade backbone: each grade-specific standard is a "
                "grade-appropriate articulation of one anchor. Modelled once, "
                "in ../skills/practices/."
            ),
            "strands_k5": [{"code": c, "name": n} for c, n in S.CCSS_ELA_STRANDS_K5],
            "strands_6_12": [{"code": c, "name": n} for c, n in S.CCSS_ELA_STRANDS_612],
            "strand_notes": (
                "Reading: Foundational Skills (RF) exists only in K-5. The "
                "literacy strands RH, RST and WHST exist only in 6-12 and are "
                "addressed to history/social-studies, science and technical "
                "teachers rather than to the ELA teacher."
            ),
            "identifier_grammar": (
                "CCSS.ELA-LITERACY.<strand><grade>.<number>, e.g. "
                "CCSS.ELA-LITERACY.RL.4.3; grade bands appear as written, e.g. "
                "CCSS.ELA-LITERACY.RI.9-10.1; literacy strands carry their own "
                "prefix, e.g. CCSS.ELA-LITERACY.RST.6-8.3."
            ),
        },
        "source": {
            "site": src["site"],
            "pdf": src["ela_pdf"],
            "ccsso_mirror_pdf": src["ccsso_mirror_ela_pdf"],
            "status": "urls_recorded_not_verified",
            "fetch_with": "lessons/curriculum/US/scripts/fetch_us_sources.py",
        },
        "full_text": pending(
            "The standards PDF has not been fetched: this environment's egress "
            "policy blocks corestandards.org. Once fetched, curate as "
            "ccss_ela_k-12.md beside this file."
        ),
        "generated_by": GENERATOR,
    }, check)

    # --- syllabus ---------------------------------------------------------
    for grade in S.CCSS_MATH_GRADES:
        hs = grade == "9-12"
        write_generated(
            os.path.join(root, "math", "syllabus", S.grade_filename(grade)), {
                "subject": "Mathematics",
                "grade": grade,
                "framework": "Common Core State Standards",
                "curriculum": "COMMON_CORE",
                "organising_unit": "conceptual category" if hs else "domain",
                "grade_axis_note": (
                    "CCSS high school mathematics is organised by conceptual "
                    "category across grades 9-12, not grade by grade. One file "
                    "covers the whole high school span because splitting it "
                    "into grade9..grade12 would invent a sequencing decision "
                    "the standards leave to states and districts."
                ) if hs else None,
                "rights": rb,
                "domains": [
                    {"code": c, "name": n, "clusters": [], "standards": []}
                    for c, n in S.CCSS_MATH_DOMAINS[grade]
                ],
                "practices_apply": [c for c, _ in S.CCSS_MATH_PRACTICES],
                "content_status": pending(
                    "Domain names and the grade's domain set are recorded (the "
                    "framework's architecture); cluster headings and standard "
                    "text are transcribed only from the fetched official PDF."
                ),
                "pacing": {
                    "status": "not_applicable",
                    "note": (
                        "Common Core prescribes no pacing. There is no CCSS "
                        "equivalent of a DBE Annual Teaching Plan - term and "
                        "week placement is a state, district or school "
                        "decision, so no `terms` array is emitted. A scheduler "
                        "wanting US pacing must source a district scope-and-"
                        "sequence, which is a different document with its own "
                        "rights position."
                    ),
                },
                "source_url": src["math_pdf"],
                "parse_status": "architecture_recorded_pending_source_ingest",
                "generated_by": GENERATOR,
            }, check)

    for grade in S.CCSS_ELA_GRADES:
        k5 = grade in ("K", "1", "2", "3", "4", "5")
        strands = S.CCSS_ELA_STRANDS_K5 if k5 else S.CCSS_ELA_STRANDS_612
        write_generated(
            os.path.join(root, "ela", "syllabus", S.grade_filename(grade)), {
                "subject": "English Language Arts and Literacy",
                "grade": grade,
                "framework": "Common Core State Standards",
                "curriculum": "COMMON_CORE",
                "organising_unit": "strand",
                "grade_axis_note": (
                    "A band file, because the CCSS themselves state these "
                    "standards for the band rather than per grade."
                ) if "-" in grade else None,
                "rights": rb,
                "strands": [
                    {"code": c, "name": n, "standards": []} for c, n in strands
                ],
                "anchors_apply": [k for k, _t, _n in S.CCSS_ELA_ANCHORS],
                "content_status": pending(
                    "Strand set per grade is recorded (the framework's "
                    "architecture); standard text is transcribed only from the "
                    "fetched official PDF."
                ),
                "pacing": {
                    "status": "not_applicable",
                    "note": "See the mathematics syllabus files - CCSS prescribes no pacing.",
                },
                "source_url": src["ela_pdf"],
                "parse_status": "architecture_recorded_pending_source_ingest",
                "generated_by": GENERATOR,
            }, check)

    # --- skills -----------------------------------------------------------
    for code, statement in S.CCSS_MATH_PRACTICES:
        write_generated(
            os.path.join(root, "math", "skills", "practices",
                         "{}.json".format(code.lower())), {
                "skill_ref": "ccss.math.practice.{}".format(code.lower()),
                "name": statement,
                "code": "CCSS.MATH.PRACTICE.{}".format(code),
                "subject": "Mathematics",
                "framework": "Common Core State Standards",
                "curriculum": "COMMON_CORE",
                "scope": "K-12",
                "scope_note": (
                    "A cross-grade practice standard, not a grade-scoped "
                    "prerequisite. It lives in skills/practices/ rather than "
                    "skills/{grade}/ because the CCSS state it identically at "
                    "every grade - copying it into thirteen grade folders "
                    "would be duplication, not fidelity."
                ),
                "rights": rb,
                "teaching_content": {
                    "status": "pending_authoring",
                    "contract": (
                        "A skill refreshes rather than teaches: 1-2 diagnostic "
                        "questions to skip ahead, a 250-700 word method recap, "
                        "a 2-5 question exit check, optionally one Manim "
                        "scene - the same contract the CAPS skills follow "
                        "(see lessons/curriculum/CAPS/README.md). Authoring "
                        "these is editorial work that is deliberately not "
                        "attempted here: this commit builds the curriculum "
                        "layer only."
                    ),
                },
                "importance": {
                    "summary": (
                        "Practice standards carry no marks of their own - "
                        "there is no CCSS examination. Their weight is that "
                        "state assessments built on the CCSS assess them "
                        "through the content standards."
                    ),
                    "exam_weight": None,
                    "exam_weight_note": (
                        "Deliberately null. Common Core sets no papers, so "
                        "there are no section marks to cite. Any weighting "
                        "would have to come from a specific state assessment "
                        "programme, which is a separate source."
                    ),
                },
                "generated_by": GENERATOR,
            }, check)

    for key, title, count in S.CCSS_ELA_ANCHORS:
        write_generated(
            os.path.join(root, "ela", "skills", "practices",
                         "{}_anchors.json".format(key)), {
                "skill_ref": "ccss.ela.anchors.{}".format(key),
                "name": title,
                "subject": "English Language Arts and Literacy",
                "framework": "Common Core State Standards",
                "curriculum": "COMMON_CORE",
                "scope": "K-12",
                "anchor_count": count,
                "scope_note": (
                    "The anchor standards are stated once for K-12 and "
                    "articulated per grade, so they are modelled once here."
                ),
                "rights": rb,
                "anchors": [],
                "anchors_status": pending(
                    "Anchor count is recorded (architecture); anchor text is "
                    "transcribed only from the fetched official PDF."
                ),
                "teaching_content": {"status": "pending_authoring"},
                "importance": {"exam_weight": None,
                               "exam_weight_note": "No CCSS examination exists - see the maths practice skills."},
                "generated_by": GENERATOR,
            }, check)

    for subject, grades in (("math", S.CCSS_MATH_GRADES), ("ela", S.CCSS_ELA_GRADES)):
        for grade in grades:
            write_generated(
                os.path.join(root, subject, "skills", "grade{}".format(grade), "index.json"), {
                    "subject": subject,
                    "grade": grade,
                    "framework": "Common Core State Standards",
                    "curriculum": "COMMON_CORE",
                    "rights": rb,
                    "skills": [],
                    "status": "pending_authoring",
                    "contract": (
                        "Grade-scoped prerequisite skills for this grade, one "
                        "JSON per skill beside this index, mirroring "
                        "lessons/curriculum/CAPS/{subject}/skills/{grade}/. "
                        "Authoring waits on the standards text being ingested "
                        "so each skill can anchor to real standard codes. "
                        "Cross-grade practice/anchor skills are NOT listed "
                        "here - they live in ../practices/."
                    ),
                    "generated_by": GENERATOR,
                }, check)

    # --- exam_guidelines (hand-owned seed) --------------------------------
    for subject, human in (("math", "Mathematics"),
                           ("ela", "English Language Arts and Literacy")):
        seed_handowned(
            os.path.join(root, subject, "exam_guidelines", "index.json"), {
                "subject": human,
                "framework": "Common Core State Standards",
                "curriculum": "COMMON_CORE",
                "applicability": "no_examining_body",
                "explanation": (
                    "Common Core is a content-standards framework, not an "
                    "examining body. It publishes no examination guideline, "
                    "sets no papers and awards no certificate, so there is no "
                    "CCSS counterpart to a DBE Examination Guideline or an IEB "
                    "SAG. This folder is kept - rather than omitted like "
                    "past_papers/ - because the assessment layer for CCSS does "
                    "exist, it just belongs to somebody else: the state "
                    "assessment programmes built on the standards."
                ),
                "assessment_is_downstream": {
                    "note": (
                        "Each adopting state assesses the CCSS through its own "
                        "programme, historically via the two federally-funded "
                        "consortia and increasingly via state-specific tests. "
                        "Each has its own rights holder and its own terms - "
                        "none of which are covered by the CCSS public licence. "
                        "Audit any such programme separately before ingesting."
                    ),
                    "known_programmes": [
                        {"name": "Smarter Balanced Assessment Consortium",
                         "rights_note": "separate rights holder - not covered by the CCSS public licence"},
                        {"name": "PARCC (legacy; succeeded by state programmes and vendor successors)",
                         "rights_note": "separate rights holder"},
                        {"name": "State-specific assessments in states that left the consortia",
                         "rights_note": "separate rights holder per state"},
                    ],
                    "status": "not_audited",
                },
                "documents": [],
                "maintained_by": (
                    "hand-owned: seeded once by build_us_tree.py and never "
                    "regenerated. Record any assessment-programme audit here."
                ),
            }, check)


# ---------------------------------------------------------------------------
# NGSS
# ---------------------------------------------------------------------------

def build_ngss(rights, check):
    root = os.path.join(US_ROOT, "NGSS", "science")
    fw = rights["frameworks"]["NGSS"]
    src = fw["primary_sources"]
    rb = rights_block(rights, "NGSS")
    rb["trademark_gate"] = fw["trademark_gate"]

    write_generated(os.path.join(root, "curriculum", "ngss_k-12.json"), {
        "subject": "Science",
        "framework": "Next Generation Science Standards",
        "framework_type": "content_standards",
        "document": "Next Generation Science Standards: For States, By States (2013)",
        "jurisdiction": "United States - adopted or adapted state by state",
        "grade_span": "K-12",
        "rights": rb,
        "architecture": {
            "model": "three-dimensional",
            "explanation": (
                "An NGSS performance expectation is not a content statement. "
                "It braids three dimensions - a science and engineering "
                "practice, a disciplinary core idea and a crosscutting concept "
                "- into a single assessable expectation. This is the structural "
                "difference from CAPS and from Common Core, and any lesson "
                "generator targeting NGSS has to carry all three dimensions "
                "rather than flattening to a topic list."
            ),
            "science_and_engineering_practices": [
                {"code": c, "name": n} for c, n in S.NGSS_PRACTICES
            ],
            "crosscutting_concepts": [
                {"code": c, "name": n} for c, n in S.NGSS_CROSSCUTTING
            ],
            "disciplinary_core_idea_domains": [
                {"code": c, "name": n} for c, n in S.NGSS_DCI_DOMAINS
            ],
            "identifier_grammar": (
                "Performance expectations are coded <grade or band>-<DCI "
                "domain+number>-<sequence>, e.g. K-PS2-1, 3-LS1-1, MS-PS1-1, "
                "HS-LS1-1. Elementary grades use the digit; middle school uses "
                "MS; high school uses HS. Engineering expectations are banded "
                "across grades, e.g. K-2-ETS1-1."
            ),
            "grade_organisation": (
                "K-5 grade by grade, then two bands: middle school (6-8) and "
                "high school (9-12). Within a band, states choose the course "
                "sequence, so NGSS itself does not assign band expectations to "
                "a specific grade."
            ),
        },
        "source": {
            "site": src["site"],
            "standards": src["standards"],
            "publisher": src["publisher"],
            "status": "urls_recorded_not_verified",
            "fetch_with": "lessons/curriculum/US/scripts/fetch_us_sources.py",
        },
        "full_text": pending(
            "nextgenscience.org is blocked by this environment's egress policy. "
            "Once fetched, curate as ngss_k-12.md beside this file."
        ),
        "generated_by": GENERATOR,
    }, check)

    for grade in S.NGSS_GRADES:
        band = grade in ("6-8", "9-12")
        write_generated(os.path.join(root, "syllabus", S.grade_filename(grade)), {
            "subject": "Science",
            "grade": grade,
            "framework": "Next Generation Science Standards",
            "curriculum": "NGSS",
            "code_prefix": {"6-8": "MS", "9-12": "HS"}.get(grade, grade),
            "organising_unit": "performance expectation",
            "grade_axis_note": (
                "A band file, because NGSS states these performance "
                "expectations for the band and leaves the course sequence "
                "inside it to states and districts."
            ) if band else None,
            "rights": rb,
            "dci_domains_available": [
                {"code": c, "name": n} for c, n in S.NGSS_DCI_DOMAINS
            ],
            "performance_expectations": [],
            "content_status": pending(
                "Which DCIs a grade actually carries, and the performance "
                "expectations themselves, are transcribed only from the "
                "fetched official standards - not from memory and not from a "
                "third-party re-host. The domain list above is the set NGSS "
                "draws from, not a claim about this grade's coverage."
            ),
            "pe_contract": (
                "Each entry: {code, statement, sep, dci, ccc, "
                "clarification_statement, assessment_boundary} - the last two "
                "reproduced verbatim from the standard, because an NGSS "
                "assessment boundary changes what may be taught and must not "
                "be paraphrased."
            ),
            "pacing": {
                "status": "not_applicable",
                "note": "NGSS prescribes no pacing; sequencing is a state/district decision.",
            },
            "source_url": src["standards"],
            "parse_status": "architecture_recorded_pending_source_ingest",
            "generated_by": GENERATOR,
        }, check)

        write_generated(
            os.path.join(root, "skills", "grade{}".format(grade), "index.json"), {
                "subject": "science",
                "grade": grade,
                "framework": "Next Generation Science Standards",
                "curriculum": "NGSS",
                "rights": rb,
                "skills": [],
                "status": "pending_authoring",
                "contract": (
                    "Grade-scoped prerequisite skills, one JSON per skill "
                    "beside this index. Cross-grade dimensions (practices and "
                    "crosscutting concepts) live in ../practices/ and "
                    "../crosscutting/ instead."
                ),
                "generated_by": GENERATOR,
            }, check)

    for folder, items, kind in (
        ("practices", S.NGSS_PRACTICES, "science and engineering practice"),
        ("crosscutting", S.NGSS_CROSSCUTTING, "crosscutting concept"),
    ):
        for code, name in items:
            write_generated(
                os.path.join(root, "skills", folder, "{}.json".format(code.lower())), {
                    "skill_ref": "ngss.{}.{}".format(folder, code.lower()),
                    "name": name,
                    "code": code,
                    "dimension": kind,
                    "subject": "Science",
                    "framework": "Next Generation Science Standards",
                    "curriculum": "NGSS",
                    "scope": "K-12",
                    "scope_note": (
                        "NGSS states this dimension across all of K-12, with "
                        "grade-band elaborations of what it looks like at each "
                        "level. Modelled once here; the band elaborations "
                        "attach after the standards are ingested."
                    ),
                    "rights": rb,
                    "grade_band_elaborations": [],
                    "elaborations_status": pending(
                        "Band-by-band elaborations come from the NGSS "
                        "appendices (Appendix F for practices, Appendix G for "
                        "crosscutting concepts) - fetch required."
                    ),
                    "teaching_content": {"status": "pending_authoring"},
                    "importance": {
                        "exam_weight": None,
                        "exam_weight_note": (
                            "NGSS sets no papers. State science assessments "
                            "built on NGSS are separate programmes with "
                            "separate rights."
                        ),
                    },
                    "generated_by": GENERATOR,
                }, check)

    seed_handowned(os.path.join(root, "exam_guidelines", "index.json"), {
        "subject": "Science",
        "framework": "Next Generation Science Standards",
        "curriculum": "NGSS",
        "applicability": "no_examining_body",
        "explanation": (
            "NGSS is a standards framework, not an examining body: no papers, "
            "no guidelines, no certificate. Kept for the same reason as the "
            "Common Core folder - the assessment layer exists but belongs to "
            "state science assessment programmes, each with its own rights "
            "holder and terms."
        ),
        "assessment_is_downstream": {
            "note": (
                "NGSS-aligned state science assessments are built "
                "state-by-state. The NGSS reuse grant does not extend to them; "
                "audit each separately."
            ),
            "status": "not_audited",
        },
        "documents": [],
        "maintained_by": "hand-owned: seeded once by build_us_tree.py and never regenerated.",
    }, check)


# ---------------------------------------------------------------------------
# AP
# ---------------------------------------------------------------------------

def build_ap(rights, check):
    root = os.path.join(US_ROOT, "AP")
    fw = rights["frameworks"]["AP"]
    src = fw["primary_sources"]
    rb = rights_block(rights, "AP")

    write_generated(os.path.join(root, "courses.json"), {
        "framework": "Advanced Placement Program",
        "rights": rb,
        "registry_note": (
            "Course names are facts and naming one is not reproduction. "
            "Everything else about an AP course - its units, topics, big "
            "ideas, skills and exam content - is College Board copyrighted "
            "material and is NOT recorded here. See RIGHTS.json."
        ),
        "scaffolded": [
            {"slug": s, "title": t, "category": c, "status": "scaffolded"}
            for s, t, c in S.AP_SCAFFOLDED_COURSES
        ],
        "not_yet_scaffolded": [
            {"slug": s, "title": t, "category": c, "status": "not_yet_scaffolded"}
            for s, t, c in S.AP_OTHER_COURSES
        ],
        "scaffolding_rationale": (
            "The scaffolded set lines up with the subject spine this "
            "repository already teaches (mathematics, physical sciences, "
            "economics, geography) plus the English pair that matches Common "
            "Core ELA. Scaffolding another is a one-line edit to "
            "AP_SCAFFOLDED_COURSES in scripts/us_spec.py plus a regenerate - "
            "no new code. There is little value in scaffolding all forty while "
            "the rights gate blocks content ingestion for every one of them."
        ),
        "course_list_currency": (
            "Verify against apcentral.collegeboard.org before relying on this "
            "list: the College Board adds and retires courses (AP Precalculus "
            "and AP African American Studies are recent additions). Recorded "
            "from search results on 2026-08-04, not read first-hand."
        ),
        "generated_by": GENERATOR,
    }, check)

    for slug, title, category in S.AP_SCAFFOLDED_COURSES:
        cdir = os.path.join(root, slug)

        write_generated(os.path.join(cdir, "curriculum", "ced.json"), {
            "course": title,
            "slug": slug,
            "category": category,
            "framework": "Advanced Placement Program",
            "curriculum": "AP",
            "document_family": "AP Course and Exam Description (CED)",
            "rights": rb,
            "role": (
                "The CED is the AP counterpart of a CAPS curriculum statement "
                "and a DBE examination guideline at once: it defines the "
                "course framework (units, topics, learning objectives, "
                "essential knowledge), the course skills or practices, and how "
                "the exam assesses them."
            ),
            "architecture_note": (
                "That a CED is built from units, big ideas and course skills "
                "is a publicly stated fact about the document's shape and is "
                "recorded as such. The unit list, topic list, learning "
                "objectives and essential knowledge statements are College "
                "Board content and are NOT recorded - not from the CED, and "
                "specifically not from third-party CED summarisers, which is "
                "the tempting shortcut and the one that would launder a "
                "prohibited reproduction."
            ),
            "content": {
                "status": "blocked_pending_written_permission",
                "units": [],
                "course_skills": [],
                "blocked_reason": (
                    "College Board terms require express written permission to "
                    "reproduce its content, and separately refuse permission "
                    "for that content to be used with generative AI or to "
                    "train AI systems. This repository generates lessons with "
                    "a model, so ingesting a CED is precisely the prohibited "
                    "act. Nothing may be transcribed here until permission "
                    "covering reproduction, commercial use and AI use is "
                    "obtained."
                ),
                "unblock_via": src["permission_request_form"],
            },
            "source": {
                "site": src["site"],
                "status": "urls_recorded_not_verified",
                "note": (
                    "Recorded so a permitted future fetch knows where to look. "
                    "Recording a URL is not reproduction."
                ),
            },
            "generated_by": GENERATOR,
        }, check)

        write_generated(os.path.join(cdir, "syllabus", "course.json"), {
            "course": title,
            "slug": slug,
            "framework": "Advanced Placement Program",
            "curriculum": "AP",
            "organising_unit": "unit (per the CED)",
            "grade_axis_note": (
                "AP has no grade axis. The College Board prescribes no grade "
                "for an AP course - schools place them where their sequence "
                "allows - so this layer is partitioned by course, one file, "
                "rather than by an invented grade10/11/12 split. Same "
                "reasoning that omits past_papers/ from the standards "
                "frameworks: do not manufacture a distinction the framework "
                "does not make."
            ),
            "rights": rb,
            "units": [],
            "content_status": {
                "status": "blocked_pending_written_permission",
                "reason": "See ../curriculum/ced.json - the unit structure is College Board content.",
            },
            "pacing": {
                "status": "blocked",
                "note": (
                    "The CED does publish suggested unit pacing and unit exam "
                    "weightings. Both are College Board content and are gated "
                    "with everything else."
                ),
            },
            "parse_status": "structure_only_content_gated",
            "generated_by": GENERATOR,
        }, check)

        write_generated(os.path.join(cdir, "skills", "course", "index.json"), {
            "course": title,
            "slug": slug,
            "framework": "Advanced Placement Program",
            "curriculum": "AP",
            "rights": rb,
            "skills": [],
            "status": "blocked_pending_written_permission",
            "partition_note": (
                "skills/course/ rather than skills/{grade}/ for the same "
                "reason the syllabus is one file: AP courses are not grade-"
                "scoped."
            ),
            "contract": (
                "AP course skills/practices are named and defined in the CED, "
                "which is gated. Prerequisite skills that are NOT College "
                "Board content - e.g. the algebra a student needs before "
                "Calculus AB - may be authored here without waiting on "
                "permission, provided they are written from general "
                "mathematical knowledge and not transcribed from a CED."
            ),
            "generated_by": GENERATOR,
        }, check)

        seed_handowned(os.path.join(cdir, "exam_guidelines", "index.json"), {
            "course": title,
            "slug": slug,
            "framework": "Advanced Placement Program",
            "curriculum": "AP",
            "document_family": "AP Course and Exam Description (CED), exam section",
            "source_page": src["site"],
            "status": "blocked_pending_written_permission",
            "status_detail": (
                "The exam format, section weights, timings and scoring "
                "guidelines all live in College Board documents. Even the "
                "format summary is deliberately left empty here rather than "
                "filled from a test-prep blog: those blogs are third-party "
                "reproductions and are excluded by the same rule that excluded "
                "Studocu re-uploads from the IEB audit."
            ),
            "rights": rb,
            "exam_structure": None,
            "documents": [],
            "unblock_via": src["permission_request_form"],
            "maintained_by": (
                "hand-owned: seeded once by build_us_tree.py, then mutated only "
                "by fetch_us_sources.py or a curation pass - never regenerated."
            ),
        }, check)

        seed_handowned(os.path.join(cdir, "past_papers", "index.json"), {
            "course": title,
            "slug": slug,
            "framework": "Advanced Placement Program",
            "curriculum": "AP",
            "portal": src["past_exam_questions"],
            "portal_coverage": (
                "The College Board publishes released free-response questions "
                "with scoring guidelines, sample responses and scoring "
                "distributions for recent years; older sets are restricted to "
                "the secure teacher site. Recorded from search results, not "
                "verified first-hand."
            ),
            "status": "blocked_pending_written_permission",
            "status_detail": (
                "This is the hard gate. College Board terms permit a teacher "
                "to download released questions and copy them for their own "
                "students in a classroom; they forbid posting them online or "
                "redistributing them electronically for any reason, forbid "
                "commercial use, and expressly refuse permission for the "
                "content to be used with generative AI or to train AI. "
                "Embedding an AP question as a worked example in this product "
                "would breach all four. Do not fetch, do not transcribe, do "
                "not pass to a model."
            ),
            "rights": rb,
            "sessions": [],
            "sessions_contract": (
                "Same shape as the CAPS/IEB per-subject index once unblocked: "
                "{\"session\": \"2025 AP Exam\", \"papers\": [{\"section\": "
                "\"free-response\", \"question_paper_url\": ..., "
                "\"scoring_guidelines_url\": ...}]}. Left empty and MUST stay "
                "empty until permission is granted - audit_tree.py fails the "
                "build if it is populated while the gate is closed."
            ),
            "captured_links": [],
            "unblock_via": src["permission_request_form"],
            "maintained_by": (
                "hand-owned: seeded once by build_us_tree.py, then mutated only "
                "by fetch_us_sources.py or a curation pass - never regenerated."
            ),
        }, check)


# ---------------------------------------------------------------------------
# SAT
# ---------------------------------------------------------------------------

def build_sat(rights, check):
    root = os.path.join(US_ROOT, "SAT")
    fw = rights["frameworks"]["SAT"]
    src = fw["primary_sources"]
    rb = rights_block(rights, "SAT")
    bands = dict(S.SAT_GRADE_BANDS)

    for slug, meta in S.SAT_SECTIONS.items():
        sdir = os.path.join(root, slug)

        write_generated(os.path.join(sdir, "curriculum", "sat_suite.json"), {
            "section": meta["title"],
            "slug": slug,
            "framework": "SAT Suite of Assessments",
            "curriculum": "SAT",
            "rights": rb,
            "role": (
                "The SAT Suite has no curriculum in the CAPS sense - it does "
                "not tell a school what to teach. What it publishes is an "
                "assessment specification: the content domains each section "
                "reports on, and the skill/knowledge testing points inside "
                "them. That specification is the nearest analogue and is what "
                "this layer would hold."
            ),
            "content_domains": meta["domains"],
            "content_domains_note": (
                "Domain NAMES are the test's public reporting structure - "
                "facts about how scores are broken out, not reproduced test "
                "content. The skill/knowledge testing points beneath each "
                "domain are College Board content and are gated."
            ),
            "suite": [
                {"grade_band": g, "assessment": bands[g]} for g, _ in S.SAT_GRADE_BANDS
            ],
            "suite_note": (
                "The Suite is vertically scaled: the same content domains run "
                "across PSAT 8/9, PSAT 10, PSAT/NMSQT and the SAT, with "
                "difficulty rather than domain set changing by band. That is "
                "why the grade axis here is the Suite's own band structure."
            ),
            "detail": {
                "status": "blocked_pending_written_permission",
                "testing_points": [],
                "reason": "See lessons/curriculum/US/RIGHTS.json - same College Board policy as AP.",
                "unblock_via": src["permission_request_form"],
            },
            "source": {"site": src["site"], "status": "urls_recorded_not_verified"},
            "generated_by": GENERATOR,
        }, check)

        for band, _label in S.SAT_GRADE_BANDS:
            write_generated(
                os.path.join(sdir, "syllabus", S.grade_filename(band)), {
                    "section": meta["title"],
                    "grade": band,
                    "assessment": bands[band],
                    "framework": "SAT Suite of Assessments",
                    "curriculum": "SAT",
                    "rights": rb,
                    "content_domains": meta["domains"],
                    "testing_points": [],
                    "content_status": {
                        "status": "blocked_pending_written_permission",
                        "reason": (
                            "Domain names are recorded as reporting-structure "
                            "facts; the testing points inside them are College "
                            "Board content."
                        ),
                    },
                    "pacing": {
                        "status": "not_applicable",
                        "note": (
                            "The SAT Suite is an assessment, not a taught "
                            "course - there is no pacing to record."
                        ),
                    },
                    "parse_status": "structure_only_content_gated",
                    "generated_by": GENERATOR,
                }, check)

            write_generated(
                os.path.join(sdir, "skills", "grade{}".format(band), "index.json"), {
                    "section": meta["title"],
                    "grade": band,
                    "assessment": bands[band],
                    "framework": "SAT Suite of Assessments",
                    "curriculum": "SAT",
                    "rights": rb,
                    "skills": [],
                    "status": "pending_authoring",
                    "contract": (
                        "Prerequisite skills for this band. These may be "
                        "authored from general subject knowledge without "
                        "waiting on College Board permission - what may NOT "
                        "happen is transcribing College Board skill/knowledge "
                        "testing points, or deriving skills by working "
                        "backwards from released questions."
                    ),
                    "generated_by": GENERATOR,
                }, check)

        seed_handowned(os.path.join(sdir, "exam_guidelines", "index.json"), {
            "section": meta["title"],
            "slug": slug,
            "framework": "SAT Suite of Assessments",
            "curriculum": "SAT",
            "source_page": src["site"],
            "rights": rb,
            "published_format": S.SAT_FORMAT,
            "published_format_basis": (
                "Recorded as factual reporting about the test's shape - how "
                "many questions, how long, how the adaptive modules work - "
                "which College Board itself publishes and which is not "
                "creative expression. It is NOT reproduced test content. The "
                "figures were corroborated across multiple secondary sources "
                "in August 2026 but NOT confirmed against College Board's own "
                "specification, which this environment could not reach; the "
                "confidence field says so and must be resolved before any "
                "student-facing use."
            ),
            "scoring": {
                "status": "not_recorded",
                "note": (
                    "Score scales and concordance tables are College Board "
                    "content; not recorded pending permission."
                ),
            },
            "documents": [],
            "status": "format_recorded_content_gated",
            "unblock_via": src["permission_request_form"],
            "maintained_by": (
                "hand-owned: seeded once by build_us_tree.py, then mutated only "
                "by fetch_us_sources.py or a curation pass - never regenerated."
            ),
        }, check)

        seed_handowned(os.path.join(sdir, "past_papers", "index.json"), {
            "section": meta["title"],
            "slug": slug,
            "framework": "SAT Suite of Assessments",
            "curriculum": "SAT",
            "analogue_note": (
                "The SAT's past-paper analogue is the released full-length "
                "practice tests plus the SAT Suite Question Bank, rather than "
                "a yearly sat paper - College Board does not release live "
                "forms the way the DBE releases NSC papers."
            ),
            "portal": src["site"],
            "status": "blocked_pending_written_permission",
            "status_detail": (
                "College Board licenses the Question Bank and released "
                "questions for classroom teaching and internal reporting only, "
                "revocably, and forbids uploading, posting online, caching, "
                "reproducing, modifying, displaying, editing, altering or "
                "enhancing them without express written permission. The "
                "Official SAT Practice Test may be used by a student in a "
                "non-commercial educational setting but explicitly NOT in a "
                "test prep course. Add the generative-AI refusal and there is "
                "no route by which this repository may ingest SAT questions "
                "today."
            ),
            "rights": rb,
            "sessions": [],
            "sessions_contract": (
                "Once unblocked: {\"session\": \"Official Practice Test N\", "
                "\"papers\": [{\"section\": ..., \"question_paper_url\": ..., "
                "\"answer_explanations_url\": ...}]}. MUST stay empty while "
                "the gate is closed - audit_tree.py enforces this."
            ),
            "captured_links": [],
            "unblock_via": src["permission_request_form"],
            "maintained_by": (
                "hand-owned: seeded once by build_us_tree.py, then mutated only "
                "by fetch_us_sources.py or a curation pass - never regenerated."
            ),
        }, check)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="verify committed generated files match regeneration; exit 1 on drift")
    args = ap.parse_args()

    rights = load_rights()
    build_common_core(rights, args.check)
    build_ngss(rights, args.check)
    build_ap(rights, args.check)
    build_sat(rights, args.check)

    if args.check:
        if _drift:
            print("DRIFT DETECTED ({} file(s)):".format(len(_drift)))
            for d in _drift:
                print("  " + d)
            print("\nRun build_us_tree.py to regenerate.")
            return 1
        print("OK: generated layers match regeneration "
              "({} hand-owned file(s) skipped by design).".format(len(_skipped_handowned)))
        return 0

    print("Wrote {} file(s).".format(len(_written)))
    if _skipped_handowned:
        print("Preserved {} hand-owned file(s) (not overwritten):".format(len(_skipped_handowned)))
        for p in _skipped_handowned[:5]:
            print("  " + p)
        if len(_skipped_handowned) > 5:
            print("  ... and {} more".format(len(_skipped_handowned) - 5))
    return 0


if __name__ == "__main__":
    sys.exit(main())
