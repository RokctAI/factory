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

"""Grade 7 tutor duos: the roster's `grade_7` block (its own duos,
tutor_019-026, same subject keys as senior_phase) resolves maths, Natural
Sciences, Social Sciences and EMS for Grade 7 only, while Grades 8-9 keep
the senior_phase duos and Grades 10-12 the top-level map. The roster is a
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
ROSTER["grade_7"] = {
    "grades": [7],
    "subjects": {
        "maths": {"expert": "tutor_019", "simplifier": "tutor_020"},
        "natural_sciences": {"expert": "tutor_021", "simplifier": "tutor_022"},
        "social_sciences": {"expert": "tutor_023", "simplifier": "tutor_024"},
        "ems": {"expert": "tutor_025", "simplifier": "tutor_026"},
    },
}

GRADE7 = {
    ("lesson.maths", "Maths"): ["tutor_019", "tutor_020"],
    ("lesson.natural_sciences", "Natural Sciences"): ["tutor_021", "tutor_022"],
    ("lesson.social_sciences", "Social Sciences"): ["tutor_023", "tutor_024"],
    ("lesson.economic_and_management_sciences",
     "Economic and Management Sciences"): ["tutor_025", "tutor_026"],
}


class Grade7DuoTests(base._RosterCase):
    roster = ROSTER

    def setUp(self):
        super().setUp()
        for n in range(19, 27):
            tid = f"tutor_{n:03d}"
            (lp.TUTORS_DIR / tid).mkdir(exist_ok=True)
            (lp.TUTORS_DIR / tid / "tutor.md").write_text(
                f"# Tutor Persona: T{n}\n\nid: {tid}\ndisplay_name: T{n}\n"
                f"style: s{n}\n", encoding="utf-8")

    def test_grade_7_resolves_its_own_duos(self):
        for (t, s), expected in GRADE7.items():
            for g in (7, "7", "grade7", "Grade 7"):
                with self.subTest(type=t, grade=g):
                    self.assertEqual(ids(lp.subject_duo_for(t, s, g)), expected)
            self.assertEqual(ids(lp.subject_duo(card(t, s, 7))), expected)

    def test_grade_7_expert_check(self):
        t = "lesson.economic_and_management_sciences"
        self.assertTrue(lp.is_expert_tutor(t, "", "tutor_025", 7))
        self.assertFalse(lp.is_expert_tutor(t, "", "tutor_026", 7))
        self.assertFalse(lp.is_expert_tutor(t, "", "tutor_007", 7))

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
