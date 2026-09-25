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

"""Grade R-3 activity packs: the committed packs pass, and each rule bites."""
import copy
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import r3_pack_check as rc  # noqa: E402

EXAMPLE = rc.CAPS_DIR / "maths" / "r3_packs" / "gradeR" / "term1" / "w01_number_one.json"


class R3PackCheckTest(unittest.TestCase):
    def setUp(self):
        self.pack = json.loads(EXAMPLE.read_text(encoding="utf-8"))

    def errors(self, pack):
        return rc.check_pack(EXAMPLE, pack)

    def test_repo_packs_pass(self):
        paths = rc.pack_paths()
        self.assertTrue(paths)
        self.assertEqual(rc.run(paths), [])

    def test_example_passes(self):
        self.assertEqual(self.errors(self.pack), [])

    def test_source_must_be_a_switched_on_row(self):
        bad = copy.deepcopy(self.pack)
        bad["source"]["subtopic"] = "Not in the syllabus"
        self.assertTrue(any(e.startswith("P2") for e in self.errors(bad)))
        off = copy.deepcopy(self.pack)
        off["source"]["file"] = "lessons/curriculum/CAPS/english_home_language/syllabus/grade7.json"
        self.assertTrue(any("lessons_enabled false" in e for e in self.errors(off)))

    def test_tap_answer_must_be_an_option(self):
        bad = copy.deepcopy(self.pack)
        bad["rounds"][0]["answer"] = "numeral_9"
        self.assertTrue(any(e.startswith("P4") for e in self.errors(bad)))

    def test_unknown_round_type_fails(self):
        bad = copy.deepcopy(self.pack)
        bad["rounds"][0]["type"] = "free_chat"
        self.assertTrue(any(e.startswith("P3") for e in self.errors(bad)))

    def test_spoken_lines_short_and_bracket_free(self):
        bad = copy.deepcopy(self.pack)
        bad["hints"][0] = "Point at the picture (smiles)"
        bad["show"]["line"] = " ".join(["one"] * (rc.MAX_LINE_WORDS + 1))
        errs = [e for e in self.errors(bad) if e.startswith("P5")]
        self.assertEqual(len(errs), 2)

    def test_images_must_be_listed(self):
        bad = copy.deepcopy(self.pack)
        bad["images"].remove("nose")
        self.assertTrue(any(e.startswith("P6") for e in self.errors(bad)))


if __name__ == "__main__":
    unittest.main()
