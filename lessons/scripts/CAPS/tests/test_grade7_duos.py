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

"""Grade 7 tutor duos: the roster's `grade_7` block (same subject keys as
senior_phase) REUSES existing duos (owner, 2026-10-04: no new tutors, and no
tutor in two classes at once): the Grades 4-6 duos teach Grade 7 maths
(tutor_013/014), Natural Sciences (tutor_015/016) and Social Sciences
(tutor_017/018), and the Economics duo (tutor_007/008) Grade 7 EMS. Grade 7
resolves through `grade_7` only, while Grades 4-6 keep intermediate_phase,
Grades 8-9 senior_phase and Grades 10-12 the top-level map. The roster is a
local fixture shaped like the agent repo's lms/team/tutors/CAPS/roster.json.

Run from the repo root:
    python3 -m pytest -q lessons/scripts/CAPS/tests
"""

import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import test_senior_phase_duos as base  # noqa: E402
from test_senior_phase_duos import card, ids, lp  # noqa: E402

ROSTER = copy.deepcopy(base.ROSTER)
ROSTER["intermediate_phase"] = {
    "grades": [4, 5, 6],
    "subjects": {
        "maths": {"expert": "tutor_013", "simplifier": "tutor_014"},
        "natural_sciences_and_technology": {"expert": "tutor_015",
                                            "simplifier": "tutor_016"},
        "social_sciences": {"expert": "tutor_017", "simplifier": "tutor_018"},
    },
}
ROSTER["grade_7"] = {
    "grades": [7],
    "subjects": {
        "maths": {"expert": "tutor_013", "simplifier": "tutor_014"},
        "natural_sciences": {"expert": "tutor_015", "simplifier": "tutor_016"},
        "social_sciences": {"expert": "tutor_017", "simplifier": "tutor_018"},
        "ems": {"expert": "tutor_007", "simplifier": "tutor_008"},
    },
}

GRADE7 = {
    ("lesson.maths", "Maths"): ["tutor_013", "tutor_014"],
    ("lesson.natural_sciences", "Natural Sciences"): ["tutor_015", "tutor_016"],
    ("lesson.social_sciences", "Social Sciences"): ["tutor_017", "tutor_018"],
    ("lesson.economic_and_management_sciences",
     "Economic and Management Sciences"): ["tutor_007", "tutor_008"],
}


class Grade7DuoTests(base._RosterCase):
    roster = ROSTER

    def setUp(self):
        super().setUp()
        for n in range(13, 19):
            tid = f"tutor_{n:03d}"
            (lp.TUTORS_DIR / tid).mkdir(exist_ok=True)
            (lp.TUTORS_DIR / tid / "tutor.md").write_text(
                f"# Tutor Persona: T{n}\n\nid: {tid}\ndisplay_name: T{n}\n"
                f"style: s{n}\n", encoding="utf-8")

    def test_grade_7_resolves_its_reused_duos(self):
        for (t, s), expected in GRADE7.items():
            for g in (7, "7", "grade7", "Grade 7"):
                with self.subTest(type=t, grade=g):
                    self.assertEqual(ids(lp.subject_duo_for(t, s, g)), expected)
            self.assertEqual(ids(lp.subject_duo(card(t, s, 7))), expected)

    def test_grade_7_expert_check(self):
        t = "lesson.economic_and_management_sciences"
        self.assertTrue(lp.is_expert_tutor(t, "", "tutor_007", 7))
        self.assertFalse(lp.is_expert_tutor(t, "", "tutor_008", 7))
        self.assertFalse(lp.is_expert_tutor(t, "", "tutor_005", 7))

    def test_no_new_grade_7_tutors(self):
        for (t, s), _ in GRADE7.items():
            got = ids(lp.subject_duo_for(t, s, 7))
            self.assertFalse({f"tutor_{n:03d}" for n in range(19, 27)} & set(got))

    def test_intermediate_phase_is_unchanged(self):
        for g in (4, 5, 6):
            self.assertEqual(ids(lp.subject_duo_for("lesson.maths", "", g)),
                             ["tutor_013", "tutor_014"])
            self.assertEqual(ids(lp.subject_duo_for(
                "lesson.natural_sciences_and_technology", "", g)),
                ["tutor_015", "tutor_016"])

    def test_grades_8_9_and_fet_are_unchanged(self):
        self.assertEqual(ids(lp.subject_duo_for("lesson.maths", "", 8)),
                         ["tutor_001", "tutor_002"])
        self.assertEqual(ids(lp.subject_duo_for(
            "lesson.economic_and_management_sciences", "", 9)),
            ["tutor_005", "tutor_006"])
        for g in (10, 11, 12, None):
            self.assertEqual(ids(lp.subject_duo_for("lesson.maths", "", g)),
                             ["tutor_001", "tutor_002"])
            self.assertEqual(
                lp.subject_duo_for("lesson.natural_sciences", "", g), [])


if __name__ == "__main__":
    unittest.main()
