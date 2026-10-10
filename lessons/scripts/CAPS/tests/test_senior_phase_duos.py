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

"""Grade 8-9 (Senior Phase) tutor duos: the roster's `senior_phase` block
resolves Natural Sciences, Social Sciences, EMS (per-grade duos) and maths
for Grades 8-9, while Grade 10-12 keeps resolving through the top-level
"subjects" map exactly as before. Also covers release_on_complete's
identity/display for the three new session-tree folders. The roster is a
local fixture shaped like the agent repo's lms/team/tutors/CAPS/roster.json.

Run from the repo root:
    python3 -m pytest -q lessons/scripts/CAPS/tests
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import lesson_pipeline as lp  # noqa: E402
import release_on_complete as roc  # noqa: E402

ROSTER = {
    "subjects": {
        "maths": {"expert": "tutor_001", "simplifier": "tutor_002"},
        "physical_sciences": {"expert": "tutor_003", "simplifier": "tutor_004"},
        "accounting": {"expert": "tutor_005", "simplifier": "tutor_006"},
        "economics": {"expert": "tutor_007", "simplifier": "tutor_008"},
        "geography": {"expert": "tutor_009", "simplifier": "tutor_010"},
        "maths_literacy": {"expert": "tutor_011", "simplifier": "tutor_012"},
    },
    "senior_phase": {
        "grades": [8, 9],
        "subjects": {
            "maths": {"expert": "tutor_001", "simplifier": "tutor_002"},
            "natural_sciences": {"expert": "tutor_003", "simplifier": "tutor_004"},
            "social_sciences": {"expert": "tutor_009", "simplifier": "tutor_010"},
            "ems": {"grade_duos": {
                "8": {"expert": "tutor_007", "simplifier": "tutor_008"},
                "9": {"expert": "tutor_005", "simplifier": "tutor_006"},
            }},
        },
        "subject_names": {
            "maths": "Mathematics",
            "natural_sciences": "Natural Sciences",
            "social_sciences": "Social Sciences",
            "ems": "Economic and Management Sciences",
        },
    },
}

NEW_FOLDERS = {
    "natural_sciences": "Natural Sciences",
    "social_sciences": "Social Sciences",
    "economic_and_management_sciences": "Economic and Management Sciences",
}

SUBTOPICS = {"subtopics": [{"ref": "subtopic_1", "title": "One"},
                           {"ref": "subtopic_2", "title": "Two"}]}
SCRIPT = ("# Part 1\n\n## Subtopic: One\n\nExpert teaches.\n\n"
          "# Part 2\n\n## Subtopic: Two\n\nSimplifier teaches.\n")


def write_team(tmp, roster):
    tutors = tmp / "team" / "tutors" / "CAPS"
    tutors.mkdir(parents=True, exist_ok=True)
    (tutors / "roster.json").write_text(json.dumps(roster), encoding="utf-8")
    for n in range(1, 13):
        tid = f"tutor_{n:03d}"
        (tutors / tid).mkdir(exist_ok=True)
        (tutors / tid / "tutor.md").write_text(
            f"# Tutor Persona: T{n}\n\nid: {tid}\ndisplay_name: T{n}\n"
            f"style: s{n}\n", encoding="utf-8")
    return tutors


def card(type_str, subject, grade):
    return f"---\ntype: {type_str}\nsubject: {subject}\ngrade: {grade}\n---\n"


def ids(duo):
    return [slug for slug, _ in duo]


class _RosterCase(unittest.TestCase):
    roster = ROSTER

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)
        saved = lp.TUTORS_DIR
        lp.TUTORS_DIR = write_team(self.tmp, self.roster)
        self.addCleanup(setattr, lp, "TUTORS_DIR", saved)


class SeniorPhaseDuoTests(_RosterCase):
    def assertDuo(self, type_str, subject, grade, expected):
        self.assertEqual(ids(lp.subject_duo(card(type_str, subject, grade))),
                         expected)
        self.assertEqual(ids(lp.subject_duo_for(type_str, subject, grade)),
                         expected)

    def test_natural_sciences_grades_8_and_9(self):
        for g in (8, 9):
            self.assertDuo("lesson.natural_sciences", "Natural Sciences", g,
                           ["tutor_003", "tutor_004"])

    def test_social_sciences_grades_8_and_9(self):
        for g in (8, 9):
            self.assertDuo("lesson.social_sciences", "Social Sciences", g,
                           ["tutor_009", "tutor_010"])

    def test_ems_uses_per_grade_duos(self):
        t = "lesson.economic_and_management_sciences"
        s = "Economic and Management Sciences"
        self.assertDuo(t, s, 8, ["tutor_007", "tutor_008"])
        self.assertDuo(t, s, 9, ["tutor_005", "tutor_006"])

    def test_maths_grades_8_and_9(self):
        for g in (8, 9):
            self.assertDuo("lesson.maths", "Maths", g,
                           ["tutor_001", "tutor_002"])

    def test_grade_forms_accepted(self):
        t = "lesson.economic_and_management_sciences"
        for g in ("9", "grade9", "Grade 9"):
            self.assertEqual(ids(lp.subject_duo_for(t, "", g)),
                             ["tutor_005", "tutor_006"])

    def test_is_expert_tutor_is_grade_aware(self):
        t, s = "lesson.economic_and_management_sciences", "EMS"
        self.assertTrue(lp.is_expert_tutor(t, s, "tutor_007", 8))
        self.assertTrue(lp.is_expert_tutor(t, s, "tutor_005", 9))
        self.assertFalse(lp.is_expert_tutor(t, s, "tutor_007", 9))
        self.assertFalse(lp.is_expert_tutor(t, s, "tutor_006", 9))

    def test_fet_grades_resolve_through_top_level_subjects(self):
        for g in (10, 11, 12, "", None):
            for key, (exp, simp) in (("maths", ("tutor_001", "tutor_002")),
                                     ("physical_sciences", ("tutor_003", "tutor_004")),
                                     ("accounting", ("tutor_005", "tutor_006")),
                                     ("maths_literacy", ("tutor_011", "tutor_012"))):
                self.assertEqual(ids(lp.subject_duo_for(f"lesson.{key}", "", g)),
                                 [exp, simp])
            # The senior-only folders have no FET duo: unchanged (empty).
            self.assertEqual(lp.subject_duo_for("lesson.natural_sciences", "", g), [])
            self.assertEqual(lp.subject_duo_for(
                "lesson.economic_and_management_sciences", "", g), [])

    def test_fet_card_resolves_exactly_as_before(self):
        # A Grade 10-12 job card must resolve to the top-level entry, the
        # same duo the pre-change lookup (subjects[key]) gave.
        for g in (10, 11, 12):
            c = card("lesson.accounting", "Accounting", g)
            self.assertEqual(ids(lp.subject_duo(c)), ["tutor_005", "tutor_006"])
            self.assertEqual(lp.roster_entry("accounting", g),
                             ROSTER["subjects"]["accounting"])
            self.assertTrue(lp.is_expert_tutor("lesson.accounting", "", "tutor_005", g))

    def test_senior_grade_falls_back_for_unlisted_subject(self):
        self.assertEqual(
            ids(lp.subject_duo_for("lesson.physical_sciences", "", 8)),
            ["tutor_003", "tutor_004"])


class SeniorBlockIsolationTests(_RosterCase):
    """A senior-phase entry that differs from the top-level one proves the
    block is read only for Grades 8-9."""
    roster = {
        "subjects": {"maths": {"expert": "tutor_001", "simplifier": "tutor_002"}},
        "senior_phase": {"grades": [8, 9], "subjects": {
            "maths": {"expert": "tutor_011", "simplifier": "tutor_012"}}},
    }

    def test_only_senior_grades_read_the_block(self):
        self.assertEqual(ids(lp.subject_duo_for("lesson.maths", "", 8)),
                         ["tutor_011", "tutor_012"])
        for g in (10, 11, 12, None):
            self.assertEqual(ids(lp.subject_duo_for("lesson.maths", "", g)),
                             ["tutor_001", "tutor_002"])


class NoSeniorBlockTests(_RosterCase):
    roster = {"subjects": ROSTER["subjects"]}

    def test_roster_without_senior_phase_keeps_old_lookup(self):
        self.assertEqual(ids(lp.subject_duo_for("lesson.maths", "", 8)),
                         ["tutor_001", "tutor_002"])
        self.assertEqual(lp.subject_duo_for("lesson.natural_sciences", "", 8), [])


class ReleaseIdentityTests(_RosterCase):
    def package(self, folder, grade):
        root = self.tmp / "lessons" / "curriculum" / "CAPS"
        pkg = (root / folder / "session" / f"grade{grade}" / "term1"
               / "some-topic" / "some-subtopic")
        pkg.mkdir(parents=True)
        return root, pkg

    def test_identity_and_display_for_new_folders(self):
        for folder, display in NEW_FOLDERS.items():
            for g in (8, 9):
                root, pkg = self.package(folder, g)
                ident = roc.lesson_identity(pkg, root)
                self.assertEqual(ident["type"], f"lesson.{folder}")
                self.assertEqual(ident["subject"], display)
                self.assertEqual(ident["grade"], g)
                self.assertEqual(ident["subject_key"], folder)

    def test_intermediate_phase_nst_display_keeps_lowercase_and(self):
        for g in (4, 5, 6):
            root, pkg = self.package("natural_sciences_and_technology", g)
            ident = roc.lesson_identity(pkg, root)
            self.assertEqual(ident["subject"], "Natural Sciences and Technology")
            self.assertEqual(ident["type"], "lesson.natural_sciences_and_technology")
            self.assertEqual(ident["grade"], g)

    def test_new_folders_stay_out_of_the_seed_map(self):
        for folder in NEW_FOLDERS:
            self.assertNotIn(folder, lp.CAPS_TYPE_BY_FOLDER)

    def test_release_resolves_grade_duo(self):
        expected = {
            ("natural_sciences", 8): ("tutor_003", "tutor_004"),
            ("natural_sciences", 9): ("tutor_003", "tutor_004"),
            ("social_sciences", 8): ("tutor_009", "tutor_010"),
            ("social_sciences", 9): ("tutor_009", "tutor_010"),
            ("economic_and_management_sciences", 8): ("tutor_007", "tutor_008"),
            ("economic_and_management_sciences", 9): ("tutor_005", "tutor_006"),
            ("maths", 8): ("tutor_001", "tutor_002"),
            ("maths", 9): ("tutor_001", "tutor_002"),
        }
        for (folder, g), (exp, simp) in expected.items():
            root, pkg = self.package(folder, g)
            ident = roc.lesson_identity(pkg, root)
            first, second, split_ref = roc.resolve_tutors(ident, SUBTOPICS, SCRIPT)
            self.assertEqual((first["id"], second["id"], split_ref),
                             (exp, simp, "subtopic_2"), (folder, g))

    def test_release_fet_package_unchanged(self):
        root, pkg = self.package("accounting", 11)
        ident = roc.lesson_identity(pkg, root)
        first, second, _ = roc.resolve_tutors(ident, SUBTOPICS, SCRIPT)
        self.assertEqual((first["id"], second["id"]), ("tutor_005", "tutor_006"))


if __name__ == "__main__":
    unittest.main()
