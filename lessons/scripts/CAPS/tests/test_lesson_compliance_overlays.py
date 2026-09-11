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

"""lesson_compliance R7 — curriculum overlays align with their shared
package: discovery finds overlays/<CURRICULUM>/label.json, any changed
file inside an overlay checks the whole overlay once, aligned overlays
pass, drifted refs / ids / labels fail.

Run from the repo root:
    python3 -m unittest discover -s lessons/scripts/CAPS/tests -v
"""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import curriculum_overlay as co  # noqa: E402
import lesson_compliance  # noqa: E402
import overlay_fixture as fx  # noqa: E402


class OverlayComplianceTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)
        _root, _twin_root, self.shared, _twin = fx.make_trees(self.tmp)
        self.target = co.write_overlay(
            self.shared,
            "IEB",
            mcq=fx.TWIN_MCQ,
            comprehension=fx.TWIN_CC,
            transcript=fx.TWIN_TRANSCRIPT,
            break_qa="# Break\n",
            exam_weight="pending\n",
            label=co.make_label("IEB"),
        )
        self.label = self.target / co.OVERLAY_LABEL

    def _violations(self, paths):
        violations, _warnings, checked = lesson_compliance.run(paths)
        return [v for v in violations if v[0] == "R7"], checked

    def test_aligned_overlay_passes_and_is_counted_once(self):
        r7, checked = self._violations(
            [self.label, self.target / "mcq.json", self.target / "break_qa.md"]
        )
        self.assertEqual(r7, [])
        self.assertEqual(checked["overlay"], 1)
        self.assertEqual(checked["script"], 0)

    def test_ref_drift_and_bad_label_fail(self):
        mcq = json.loads(json.dumps(fx.TWIN_MCQ))
        mcq["subtopics"][1]["ref"] = "subtopic_7"
        (self.target / "mcq.json").write_text(co.dumps(mcq), encoding="utf-8")
        r7, _ = self._violations([self.target / "mcq.json"])
        self.assertEqual(len(r7), 1)
        self.assertIn("subtopic_7", r7[0][1])
        self.label.write_text(co.dumps({"badge": "IEB"}), encoding="utf-8")
        r7, _ = self._violations([self.label])
        self.assertTrue(any("curriculum" in msg for _, msg in r7))

    def test_overlay_without_a_shared_package_fails(self):
        (self.shared / "mcq.json").unlink()
        r7, _ = self._violations([self.label])
        self.assertEqual(len(r7), 1)
        self.assertIn("shared mcq.json", r7[0][1])

    def test_discover_finds_overlay_labels(self):
        saved = os.getcwd()
        self.addCleanup(os.chdir, saved)
        os.chdir(self.tmp)
        (self.tmp / ".rokct" / "agent" / "jobs").mkdir(parents=True)
        found = lesson_compliance.discover()
        self.assertEqual(len(found), 7)
        overlays = found[-1]
        self.assertEqual([p.name for p in overlays], ["label.json"])
        self.assertIn("overlays", overlays[0].parts)
        self.assertEqual(lesson_compliance.RULES[-1], "R7")
        self.assertIn("R7", lesson_compliance.RULE_TITLES)

    def test_overlay_label_for(self):
        self.assertEqual(
            lesson_compliance.overlay_label_for(self.target / "mcq.json"), self.label
        )
        self.assertIsNone(lesson_compliance.overlay_label_for(self.shared / "mcq.json"))


if __name__ == "__main__":
    unittest.main()
