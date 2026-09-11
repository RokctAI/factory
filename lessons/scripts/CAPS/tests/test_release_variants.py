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

"""release_on_complete.assemble() with curriculum overlays: the manifest
gains `curricula` / `default_curriculum` / `variants` ADDITIVELY, every
pre-existing field is byte-identical with or without an overlay, and a
package without overlays assembles exactly as before. Audio measurement
and animation export are stubbed at their seams (no ffprobe/manim in the
unit-test runner); tutors resolve from a roster fixture.

Run from the repo root:
    python3 -m unittest discover -s lessons/scripts/CAPS/tests -v
"""

import io
import json
import re
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import curriculum_overlay as co  # noqa: E402
import extract_curriculum_overlays as x  # noqa: E402
import lesson_pipeline  # noqa: E402
import overlay_fixture as fx  # noqa: E402
import release_on_complete as roc  # noqa: E402

SCHEDULED_RE = re.compile(r'"scheduled_at": "[^"]*"')
NEW_KEYS = ("curricula", "default_curriculum", "variants")


class AssembleVariantsTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)
        (self.shared_root, self.twin_root, self.shared, self.twin) = fx.make_trees(
            self.tmp
        )
        tutors = fx.make_team(self.tmp)
        self._saved_tutors = lesson_pipeline.TUTORS_DIR
        lesson_pipeline.TUTORS_DIR = tutors
        self.addCleanup(setattr, lesson_pipeline, "TUTORS_DIR", self._saved_tutors)
        # Seams: the audio root holds no mp3 and no ffprobe/manim exists
        # here, so both acquisition steps are stubbed to fixed values.
        self._saved = (roc.acquire_audio, roc.build_animations)
        roc.acquire_audio = lambda src, out_dir: 600.0
        roc.build_animations = lambda folder, scene_dir, out_dir, secs: {
            "version": "1",
            "scene": "",
            "duration_seconds": secs,
            "primitives": [],
        }
        self.addCleanup(self._restore)

    def _restore(self):
        roc.acquire_audio, roc.build_animations = self._saved

    def _assemble(self, tag):
        ident = roc.lesson_identity(self.shared, self.shared_root)
        out_dir = self.tmp / "out" / tag
        shutil.rmtree(out_dir, ignore_errors=True)
        with redirect_stdout(io.StringIO()):
            path = roc.assemble(
                self.shared, ident, self.shared / "audio.mp3", self.shared, out_dir
            )
        text = SCHEDULED_RE.sub('"scheduled_at": "T"', path.read_text("utf-8"))
        return text, json.loads(text)

    def _extract_overlay(self):
        with redirect_stdout(io.StringIO()):
            x.run(
                self.shared_root,
                self.twin_root,
                "IEB",
                check=False,
                filter_text="",
                break_extractor=roc.extract_session_break_questions,
                report_json=None,
                report_md=None,
            )

    def test_no_overlay_no_new_keys(self):
        _, manifest = self._assemble("plain")
        for key in NEW_KEYS:
            self.assertNotIn(key, manifest)
        self.assertEqual(manifest["session_id"], fx.LESSON_ID)
        self.assertIn("questions", manifest)

    def test_pre_existing_fields_are_byte_identical_with_an_overlay(self):
        before_text, before = self._assemble("before")
        self._extract_overlay()
        after_text, after = self._assemble("after")
        self.assertNotEqual(before_text, after_text)
        stripped = {k: v for k, v in after.items() if k not in NEW_KEYS}
        self.assertEqual(json.dumps(stripped, indent=2), json.dumps(before, indent=2))
        self.assertEqual(set(after) - set(before), set(NEW_KEYS))
        # Key order of the shared fields is unchanged; the new keys are
        # appended after them.
        self.assertEqual(list(after)[: len(before)], list(before))

    def test_variants_carry_the_overlay_and_default_banks(self):
        self._extract_overlay()
        _, manifest = self._assemble("variants")
        self.assertEqual(manifest["curricula"], ["CAPS", "IEB"])
        self.assertEqual(manifest["default_curriculum"], "CAPS")
        caps = manifest["variants"]["CAPS"]
        ieb = manifest["variants"]["IEB"]
        self.assertEqual(caps["questions"], manifest["questions"])
        self.assertEqual(caps["comprehension_check"], manifest["comprehension_check"])
        (brk,) = [t for t in manifest["tracks"] if t["type"] == "break_start"]
        self.assertEqual(caps["break_questions"], brk["questions"])
        self.assertEqual(
            ieb["questions"]["subtopic_1_q2"]["question"],
            "R4 000 at 7% for 3 years grows to:",
        )
        self.assertTrue(ieb["questions"]["subtopic_1_q2"][co.NEEDS_REAUTHOR])
        self.assertEqual(ieb["needs_reauthor"], 3)
        self.assertEqual(
            ieb["exercise_by_ref"], {"subtopic_2": ["subtopic_2_q1", "subtopic_2_q2"]}
        )
        self.assertEqual(
            [q["question"] for q in ieb["break_questions"]],
            [
                q["question"]
                for q in roc.extract_session_break_questions(fx.TWIN_TRANSCRIPT)
            ],
        )
        self.assertIsNone(ieb["break_audio"])
        self.assertEqual(ieb["break_audio_status"]["asset"], "break_qa.IEB.mp3")
        self.assertEqual(ieb["break_audio_status"]["status"], "pending_recording")
        self.assertEqual(ieb["label"]["badge"], "IEB")
        self.assertIn("pending SAG", ieb["exam_weight"])

    def test_shared_ids_and_tag_are_kept_no_ieb_prefix(self):
        self._extract_overlay()
        _, manifest = self._assemble("ids")
        ident = roc.lesson_identity(self.shared, self.shared_root)
        self.assertEqual(manifest["session_id"], ident["id"])
        self.assertEqual(ident["tag"], f"lesson-{fx.LESSON_ID}")
        self.assertFalse(ident["id"].startswith("ieb_"))
        self.assertEqual(manifest["lesson_slug"], "simple-growth")

    def test_overlay_files_join_the_package_gate(self):
        self._extract_overlay()
        files = co.overlay_files(self.shared)
        self.assertEqual(len(files), 6)
        self.assertTrue(all(co.OVERLAY_DIR in p.parts for p in files))
        # discover_folders still sees exactly the one package: the overlay
        # directory is not a package.
        self.assertEqual(roc.discover_folders(self.shared_root), [self.shared])


if __name__ == "__main__":
    unittest.main()
