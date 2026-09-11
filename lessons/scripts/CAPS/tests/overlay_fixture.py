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

"""Shared fixture for the curriculum-overlay tests: one shared (CAPS)
session package and its IEB twin, written into a temp curriculum root
the way the real trees are laid out. The twin re-narrates the shared
lesson around a different worked case (R5 000 at 8 % vs R4 000 at 7 %,
`2ax` vs `3mp`), so the case-bound check has something to find."""

from __future__ import annotations

import json
from pathlib import Path

REL_PACKAGE = Path("maths/session/grade10/term3/finance-and-growth/simple-growth")
LESSON_ID = "maths_g10_finance-and-growth_simple-growth"

SHARED_SCRIPT = """# Part 1 — Expert

Today's anchor case: Zanele saves five thousand rand at eight percent simple
interest for three years, and the anchor expression is two a x plus two a y.

## Subtopic: The formula

Simple interest grows by the same amount every year: eight percent of
five thousand rand is four hundred rand, so three years add one thousand
two hundred rand and the total is R6 200.

Take the questions for this section now.

# Part 2 — Simplifier

## Subtopic: The check

Add the yearly amounts and compare with the formula's answer of R6 200.
"""

TWIN_SCRIPT = """# Part 1 — Expert

Today's anchor case: Thabo saves four thousand rand at seven percent simple
interest for three years, and the anchor expression is three m p plus three m q.

## Subtopic: The formula

Simple interest grows by the same amount every year: seven percent of
four thousand rand is two hundred and eighty rand, so three years add
eight hundred and forty rand and the total is R4 840.

Take the questions for this section now.

# Part 2 — Simplifier

## Subtopic: The check

Add the yearly amounts and compare with the formula's answer of R4 840.
"""

SUBTOPICS = {
    "subtopics": [
        {
            "ref": "subtopic_1",
            "title": "The formula",
            "start_seconds": 0,
            "end_seconds": 300,
        },
        {
            "ref": "subtopic_2",
            "title": "The check",
            "start_seconds": 300,
            "end_seconds": 600,
        },
    ]
}


def _q(qid, question, options, correct):
    return {
        "id": qid,
        "question": question,
        "options": options,
        "correct_index": correct,
        "time_limit_seconds": 30,
    }


SHARED_MCQ = {
    "subtopics": [
        {
            "ref": "subtopic_1",
            "title": "The formula",
            "questions": [
                _q(
                    "subtopic_1_q1",
                    "Simple interest is calculated on:",
                    ["The principal alone", "The growing balance"],
                    0,
                ),
                _q(
                    "subtopic_1_q2",
                    "R5 000 at 8% for 3 years grows to:",
                    ["R6 200", "R6 000"],
                    0,
                ),
            ],
        },
        {
            "ref": "subtopic_2",
            "title": "The check",
            "questions": [
                _q(
                    "subtopic_2_q1",
                    "The check that confirms the answer is:",
                    ["Adding the yearly amounts", "Guessing"],
                    0,
                ),
            ],
        },
    ]
}

TWIN_MCQ = {
    "subtopics": [
        {
            "ref": "subtopic_1",
            "title": "The formula",
            "questions": [
                _q(
                    "subtopic_1_q1",
                    "Simple interest is worked out on:",
                    ["The principal alone", "The growing balance"],
                    0,
                ),
                _q(
                    "subtopic_1_q2",
                    "R4 000 at 7% for 3 years grows to:",
                    ["R4 840", "R4 000"],
                    0,
                ),
            ],
        },
        {
            "ref": "subtopic_2",
            "title": "The check",
            "questions": [
                _q(
                    "subtopic_2_q1",
                    "The check that confirms the answer is:",
                    ["Adding the yearly amounts", "Guessing"],
                    0,
                ),
                _q(
                    "subtopic_2_q2",
                    "Factorising 3mp + 3mq gives:",
                    ["3m(p + q)", "3(mp + q)"],
                    0,
                ),
            ],
        },
    ]
}

SHARED_CC = {
    "questions": [
        {
            "id": "cc1",
            "question": "Explain why the yearly amount never changes.",
            "expected_answer": "The rate applies to the principal alone.",
        },
        {
            "id": "cc2",
            "question": "Describe the final check.",
            "expected_answer": "Add the yearly amounts and compare.",
        },
    ]
}

TWIN_CC = {
    "questions": [
        {
            "id": "cc1",
            "question": "Explain why Thabo's yearly amount never changes.",
            "expected_answer": "Seven percent of the principal alone, R280 each year.",
        },
        {
            "id": "cc2",
            "question": "Describe the final check.",
            "expected_answer": "Add the yearly amounts and compare.",
        },
    ]
}

SHARED_TRANSCRIPT = """**Thandi:** Questions from the class! First: why does the interest never grow?

**Tutor:** Because the rate applies to the principal alone.

***

**Thandi:** Next: what does the check look like?

**Tutor:** Add the yearly amounts.
"""

TWIN_TRANSCRIPT = """**Thandi:** Class questions! First: why is Thabo's interest R280 every year?

**Tutor:** Because seven percent of four thousand rand is the same each year.

***

**Thandi:** Next: what does the check look like?

**Tutor:** Add the yearly amounts.
"""

OTHER_FILES = {
    "intro.md": "Today we grow money the simple way.\n",
    "reel_clip.json": json.dumps({"lesson_id": LESSON_ID, "hook": "x"}),
    "manim_scene.py": "from manim import Scene\n\nclass Lesson(Scene):\n    pass\n",
    "assistant_nervous_script.md": "**Mandy:** Is this on the test?\n",
}

# Tutor roster for resolve_tutors (the agent repo's lms/team layout).
ROSTER = {"subjects": {"maths": {"expert": "tutor_001", "simplifier": "tutor_002"}}}


def tutor_card(tid, name, style, role):
    return (
        f"# Tutor Persona: {name}\n\n"
        f"pipeline_label: {name} — {style}\n"
        f"id: {tid}\n"
        f"display_name: {name}\n"
        f"style: {style}\n"
        f"role: {role}\n"
        "subjects: [Maths]\n"
        f"real_name: Mr {name}\n"
    )


def write_package(folder: Path, *, script, mcq, cc, transcript):
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "script.md").write_text(script, encoding="utf-8")
    (folder / "mcq.json").write_text(json.dumps(mcq, indent=2) + "\n", encoding="utf-8")
    (folder / "comprehension_check.json").write_text(
        json.dumps(cc, indent=2) + "\n", encoding="utf-8"
    )
    (folder / "assistant_qa_transcript.md").write_text(transcript, encoding="utf-8")
    (folder / "subtopics.json").write_text(
        json.dumps(SUBTOPICS, indent=2), encoding="utf-8"
    )
    for name, text in OTHER_FILES.items():
        (folder / name).write_text(text, encoding="utf-8")
    return folder


def make_trees(tmp: Path):
    """(shared_root, twin_root, shared_folder, twin_folder) under tmp,
    laid out as lessons/curriculum/{CAPS,IEB}/..."""
    shared_root = tmp / "lessons" / "curriculum" / "CAPS"
    twin_root = tmp / "lessons" / "curriculum" / "IEB"
    shared = write_package(
        shared_root / REL_PACKAGE,
        script=SHARED_SCRIPT,
        mcq=SHARED_MCQ,
        cc=SHARED_CC,
        transcript=SHARED_TRANSCRIPT,
    )
    twin = write_package(
        twin_root / REL_PACKAGE,
        script=TWIN_SCRIPT,
        mcq=TWIN_MCQ,
        cc=TWIN_CC,
        transcript=TWIN_TRANSCRIPT,
    )
    return shared_root, twin_root, shared, twin


def make_team(tmp: Path) -> Path:
    """A TEAM_ROOT-shaped tutors dir: returns tutors/CAPS."""
    tutors = tmp / "team" / "tutors" / "CAPS"
    tutors.mkdir(parents=True, exist_ok=True)
    (tutors / "roster.json").write_text(json.dumps(ROSTER), encoding="utf-8")
    for tid, name, style, role in (
        ("tutor_001", "Sifiso Zulu", "formal", "expert"),
        ("tutor_002", "Naledi Dlamini", "simplistic", "simplifier"),
    ):
        (tutors / tid).mkdir(exist_ok=True)
        (tutors / tid / "tutor.md").write_text(
            tutor_card(tid, name, style, role), encoding="utf-8"
        )
    return tutors


def tree_digest(root: Path) -> dict:
    """{relative path: bytes} of every file under root — for proving a
    tree was not touched."""
    return {
        str(p.relative_to(root)): p.read_bytes()
        for p in sorted(root.rglob("*"))
        if p.is_file()
    }
