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

"""Syllabus files marked "pipeline_enabled": false stay out of load_seed_entries."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import lesson_pipeline as lp  # noqa: E402


def _syllabus(grade, **extra):
    return {
        "subject": "Maths",
        "grade": grade,
        "curriculum": "CAPS",
        "terms": [{"term": 1, "topics": [{"name": "Whole numbers", "subtopics": ["Counting"]}]}],
        **extra,
    }


class PipelineHoldTest(unittest.TestCase):
    def test_held_syllabus_is_skipped(self):
        with tempfile.TemporaryDirectory() as tmp:
            syl = Path(tmp) / "maths" / "syllabus"
            syl.mkdir(parents=True)
            (syl / "grade10.json").write_text(json.dumps(_syllabus(10)), encoding="utf-8")
            (syl / "grade9.json").write_text(
                json.dumps(_syllabus(9, pipeline_enabled=False)), encoding="utf-8")
            with mock.patch.object(lp, "CAPS_DIR", Path(tmp)), \
                    mock.patch.object(lp, "CAPS_TYPE_BY_FOLDER", {"maths": "lesson.maths"}), \
                    mock.patch.object(lp, "load_caps_skills", return_value={}):
                rows = lp.load_seed_entries()
        self.assertEqual({r["grade"] for r in rows}, {10})

    def test_lessons_disabled_file_and_topic_are_skipped(self):
        with tempfile.TemporaryDirectory() as tmp:
            syl = Path(tmp) / "maths" / "syllabus"
            syl.mkdir(parents=True)
            live = _syllabus(8)
            live["terms"][0]["topics"].append(
                {"name": "History: off-scope strand", "subtopics": ["X"], "weeks": [2],
                 "lessons_enabled": False})
            (syl / "grade8.json").write_text(json.dumps(live), encoding="utf-8")
            (syl / "grade7.json").write_text(
                json.dumps(_syllabus(7, lessons_enabled=False)), encoding="utf-8")
            with mock.patch.object(lp, "CAPS_DIR", Path(tmp)), \
                    mock.patch.object(lp, "CAPS_TYPE_BY_FOLDER", {"maths": "lesson.maths"}), \
                    mock.patch.object(lp, "load_caps_skills", return_value={}):
                rows = lp.load_seed_entries()
        self.assertEqual([(r["grade"], r["topic"]) for r in rows], [(8, "Whole numbers")])

    def test_lessons_disabled_subtopic_is_skipped(self):
        with tempfile.TemporaryDirectory() as tmp:
            syl = Path(tmp) / "maths" / "syllabus"
            syl.mkdir(parents=True)
            data = _syllabus(0)
            data["terms"][0]["topics"][0]["subtopics"].append(
                {"name": "Creative Arts: finger painting", "lessons_enabled": False})
            (syl / "gradeR.json").write_text(json.dumps(data), encoding="utf-8")
            with mock.patch.object(lp, "CAPS_DIR", Path(tmp)), \
                    mock.patch.object(lp, "CAPS_TYPE_BY_FOLDER", {"maths": "lesson.maths"}), \
                    mock.patch.object(lp, "load_caps_skills", return_value={}):
                rows = lp.load_seed_entries()
        self.assertEqual([r["subtopic"] for r in rows], ["Counting"])

    def test_repo_has_no_pipeline_rows_below_grade_10(self):
        grades = {str(r["grade"]) for r in lp.load_seed_entries() if "category" not in r}
        self.assertTrue(grades <= {"10", "11", "12"}, grades)


if __name__ == "__main__":
    unittest.main()
