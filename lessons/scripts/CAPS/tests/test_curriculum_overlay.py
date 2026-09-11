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

"""Unit tests for lessons/scripts/CAPS/curriculum_overlay.py — the overlay
schema (label shape, file set), the writer/reader round trip, R7
validation and the additive manifest `variants` block.

Run from the repo root:
    python3 -m unittest discover -s lessons/scripts/CAPS/tests -v
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import curriculum_overlay as co  # noqa: E402
import overlay_fixture as fx  # noqa: E402


def _extract(transcript_md):
    """A stand-in break extractor: the **Thandi:** asks, question part."""
    out = []
    for line in transcript_md.splitlines():
        if line.startswith("**Thandi:**"):
            out.append({"question": line.split(":**", 1)[1].strip()})
    return out


class LabelSchemaTests(unittest.TestCase):
    def test_make_label_carries_contract_keys_and_pending_break_audio(self):
        label = co.make_label(
            "IEB", source_twin="lessons/curriculum/IEB/x", sag_status="pending_fetch"
        )
        self.assertEqual(label["curriculum"], "IEB")
        self.assertEqual(label["badge"], "IEB")
        self.assertEqual(label["content_basis"], "CAPS")
        self.assertEqual(label["break_audio"]["asset"], "break_qa.IEB.mp3")
        self.assertEqual(label["break_audio"]["status"], "pending_recording")
        self.assertEqual(label["sag_status"], "pending_fetch")
        self.assertEqual(co.validate_label(label, "IEB"), [])

    def test_validate_label_rejects_bad_shapes(self):
        self.assertTrue(co.validate_label("nope"))
        self.assertTrue(co.validate_label({"curriculum": "IEB"}))
        wrong_dir = co.make_label("IEB")
        self.assertTrue(co.validate_label(wrong_dir, "CAMBRIDGE"))
        basis = co.make_label("IEB")
        basis["content_basis"] = "IEB"
        self.assertTrue(any("content_basis" in p for p in co.validate_label(basis)))
        audio = co.make_label("IEB")
        audio["break_audio"] = "break_qa.IEB.mp3"
        self.assertTrue(any("break_audio" in p for p in co.validate_label(audio)))

    def test_overlay_file_set_is_the_six_contract_files(self):
        self.assertEqual(
            set(co.OVERLAY_FILES),
            {
                "mcq.json",
                "comprehension_check.json",
                "assistant_qa_transcript.md",
                "break_qa.md",
                "exam_weight.md",
                "label.json",
            },
        )


class WriteReadTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.folder = Path(tmp.name) / "lesson"
        self.folder.mkdir()

    def _write(self, curriculum="IEB"):
        return co.write_overlay(
            self.folder,
            curriculum,
            mcq=fx.TWIN_MCQ,
            comprehension=fx.TWIN_CC,
            transcript=fx.TWIN_TRANSCRIPT,
            break_qa="# Break\n",
            exam_weight="IEB exam weighting: pending SAG ingestion.\n",
            label=co.make_label(curriculum),
        )

    def test_round_trip_and_listing(self):
        self.assertEqual(co.list_overlays(self.folder), [])
        target = self._write()
        self.assertEqual(
            sorted(p.name for p in target.iterdir()), sorted(co.OVERLAY_FILES)
        )
        self.assertEqual(co.list_overlays(self.folder), ["IEB"])
        ov = co.read_overlay(self.folder, "IEB")
        self.assertEqual(ov["mcq"], fx.TWIN_MCQ)
        self.assertEqual(ov["comprehension"], fx.TWIN_CC)
        self.assertEqual(ov["transcript"], fx.TWIN_TRANSCRIPT)
        self.assertEqual(ov["label"]["curriculum"], "IEB")
        self.assertEqual(len(co.overlay_files(self.folder)), 6)

    def test_directory_without_label_is_not_an_overlay(self):
        (self.folder / "overlays" / "IEB").mkdir(parents=True)
        (self.folder / "overlays" / "IEB" / "mcq.json").write_text("{}")
        self.assertEqual(co.list_overlays(self.folder), [])
        with self.assertRaises(co.OverlayError):
            co.read_overlay(self.folder, "IEB")

    def test_write_is_deterministic(self):
        first = {p.name: p.read_bytes() for p in self._write().iterdir()}
        second = {p.name: p.read_bytes() for p in self._write().iterdir()}
        self.assertEqual(first, second)
        self.assertTrue(first["mcq.json"].endswith(b"\n"))


class ValidateOverlayTests(unittest.TestCase):
    def _overlay(self, mcq=None, cc=None, label=None):
        return {
            "curriculum": "IEB",
            "mcq": mcq or fx.TWIN_MCQ,
            "comprehension": cc or fx.TWIN_CC,
            "label": label or co.make_label("IEB"),
        }

    def test_aligned_overlay_is_valid(self):
        self.assertEqual(
            co.validate_overlay(self._overlay(), fx.SHARED_MCQ, fx.SHARED_CC), []
        )

    def test_unknown_ref_and_comprehension_id_fail(self):
        mcq = json.loads(json.dumps(fx.TWIN_MCQ))
        mcq["subtopics"][0]["ref"] = "subtopic_9"
        cc = json.loads(json.dumps(fx.TWIN_CC))
        cc["questions"][0]["id"] = "cc9"
        problems = co.validate_overlay(
            self._overlay(mcq, cc), fx.SHARED_MCQ, fx.SHARED_CC
        )
        self.assertTrue(any("subtopic_9" in p for p in problems))
        self.assertTrue(any("cc9" in p for p in problems))

    def test_duplicate_ids_and_non_boolean_flag_fail(self):
        mcq = json.loads(json.dumps(fx.TWIN_MCQ))
        mcq["subtopics"][1]["questions"][0]["id"] = "subtopic_1_q1"
        mcq["subtopics"][0]["questions"][0][co.NEEDS_REAUTHOR] = "yes"
        problems = co.validate_overlay(self._overlay(mcq), fx.SHARED_MCQ, fx.SHARED_CC)
        self.assertTrue(any("duplicate" in p for p in problems))
        self.assertTrue(any("boolean" in p for p in problems))

    def test_bad_label_is_reported_under_the_overlay(self):
        problems = co.validate_overlay(
            self._overlay(label={"badge": "IEB"}), fx.SHARED_MCQ, fx.SHARED_CC
        )
        self.assertTrue(problems)
        self.assertTrue(all(p.startswith("IEB: ") for p in problems))


class BuildVariantsTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.folder = Path(tmp.name) / "lesson"
        self.folder.mkdir()
        self.break_questions = _extract(fx.SHARED_TRANSCRIPT)

    def _write_overlay(self, mcq=None, cc=None, exam_weight="IEB pending\n"):
        mcq = json.loads(json.dumps(mcq or fx.TWIN_MCQ))
        co.write_overlay(
            self.folder,
            "IEB",
            mcq=mcq,
            comprehension=cc or fx.TWIN_CC,
            transcript=fx.TWIN_TRANSCRIPT,
            break_qa="# Break\n",
            exam_weight=exam_weight,
            label=co.make_label("IEB", sag_status="pending_fetch"),
        )

    def _variants(self):
        return co.build_variants(
            self.folder,
            fx.SHARED_MCQ,
            fx.SHARED_CC,
            self.break_questions,
            break_question_extractor=_extract,
        )

    def test_no_overlay_means_no_keys_at_all(self):
        self.assertEqual(self._variants(), {})

    def test_block_shape_and_curricula_order(self):
        self._write_overlay()
        block = self._variants()
        self.assertEqual(set(block), {"curricula", "default_curriculum", "variants"})
        self.assertEqual(block["curricula"], ["CAPS", "IEB"])
        self.assertEqual(block["default_curriculum"], "CAPS")
        self.assertEqual(list(block["variants"]), ["CAPS", "IEB"])

    def test_default_variant_is_the_shared_banks(self):
        self._write_overlay()
        caps = self._variants()["variants"]["CAPS"]
        self.assertEqual(
            caps["questions"], {q["id"]: q for q in co.mcq_questions(fx.SHARED_MCQ)}
        )
        self.assertEqual(
            caps["comprehension_check"], {q["id"]: q for q in fx.SHARED_CC["questions"]}
        )
        self.assertEqual(caps["break_questions"], self.break_questions)
        self.assertEqual(caps["label"]["badge"], "CAPS")
        self.assertIsNone(caps["break_audio"])
        self.assertEqual(caps["break_audio_status"]["status"], "pending_recording")
        self.assertNotIn("exercise_by_ref", caps)

    def test_overlay_variant_carries_its_own_files(self):
        self._write_overlay()
        ieb = self._variants()["variants"]["IEB"]
        self.assertEqual(
            ieb["label"],
            {
                "curriculum": "IEB",
                "badge": "IEB",
                "content_basis": "CAPS",
                "sag_status": "pending_fetch",
            },
        )
        self.assertIn("subtopic_2_q2", ieb["questions"])
        self.assertEqual(
            ieb["comprehension_check"]["cc1"]["question"],
            fx.TWIN_CC["questions"][0]["question"],
        )
        self.assertEqual(ieb["break_questions"], _extract(fx.TWIN_TRANSCRIPT))
        self.assertIsNone(ieb["break_audio"])
        self.assertEqual(
            ieb["break_audio_status"],
            {
                "asset": "break_qa.IEB.mp3",
                "status": "pending_recording",
                "script": "overlays/IEB/break_qa.md",
            },
        )
        self.assertEqual(ieb["exam_weight"], "IEB pending")

    def test_exercise_by_ref_only_where_the_layout_differs(self):
        self._write_overlay()
        ieb = self._variants()["variants"]["IEB"]
        # The twin adds subtopic_2_q2 under subtopic_2; subtopic_1 matches.
        self.assertEqual(
            ieb["exercise_by_ref"], {"subtopic_2": ["subtopic_2_q1", "subtopic_2_q2"]}
        )
        self._write_overlay(mcq=fx.SHARED_MCQ)
        self.assertNotIn("exercise_by_ref", self._variants()["variants"]["IEB"])

    def test_needs_reauthor_is_counted_not_dropped(self):
        mcq = json.loads(json.dumps(fx.TWIN_MCQ))
        mcq["subtopics"][0]["questions"][1][co.NEEDS_REAUTHOR] = True
        self._write_overlay(mcq=mcq)
        ieb = self._variants()["variants"]["IEB"]
        self.assertEqual(ieb["needs_reauthor"], 1)
        self.assertTrue(ieb["questions"]["subtopic_1_q2"][co.NEEDS_REAUTHOR])

    def test_break_questions_follow_the_shared_lessons_two_part_status(self):
        # A single-voice lesson emits no break list at top level, so no
        # variant may invent one.
        self._write_overlay()
        block = co.build_variants(
            self.folder,
            fx.SHARED_MCQ,
            fx.SHARED_CC,
            [],
            break_question_extractor=_extract,
        )
        self.assertEqual(block["variants"]["IEB"]["break_questions"], [])


if __name__ == "__main__":
    unittest.main()
