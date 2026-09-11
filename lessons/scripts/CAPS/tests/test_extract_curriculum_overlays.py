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

"""Unit tests for lessons/scripts/CAPS/extract_curriculum_overlays.py —
the case-bound vocabulary, the derivation (what is copied, what is never
copied, what is flagged), alignment reporting, the report, drift mode and
the twin tree staying untouched.

Run from the repo root:
    python3 -m unittest discover -s lessons/scripts/CAPS/tests -v
"""

import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import curriculum_overlay as co  # noqa: E402
import extract_curriculum_overlays as x  # noqa: E402
import overlay_fixture as fx  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[4]


def _extract(transcript_md):
    out = []
    for line in transcript_md.splitlines():
        if line.startswith("**Thandi:**"):
            out.append({"question": line.split(":**", 1)[1].strip()})
    return out


class ValueTokenTests(unittest.TestCase):
    """The vocabulary both sides of the check are reduced to."""

    def test_item_tokens_numerals_currency_percent_decimals(self):
        tokens = x.item_tokens("R4 000 at 7% for 3 years; factor 1,07 and 0,21")
        self.assertIn("4000", tokens)
        self.assertIn("7", tokens)
        self.assertIn("3", tokens)
        self.assertIn("1.07", tokens)
        self.assertIn("0.21", tokens)
        self.assertNotIn("R", tokens)

    def test_item_tokens_algebraic_terms_and_names(self):
        tokens = x.item_tokens("Factorise 3mp + 3mq − np − nq when Thabo asks.")
        self.assertIn("3mp", tokens)
        self.assertIn("3mq", tokens)
        self.assertIn("np", tokens)
        self.assertIn("nq", tokens)
        self.assertIn("Thabo", tokens)
        # Sentence-initial capitals and hyphenated words are not values.
        self.assertNotIn("Factorise", tokens)
        self.assertNotIn("one", x.item_tokens("The one-sentence difference"))
        self.assertNotIn("hen", x.item_tokens("The hen-coop deal"))

    def test_script_vocabulary_normalises_spoken_forms(self):
        vocab = x.script_vocabulary(
            "Thabo saves four thousand rand at seven percent; the factor "
            "is one comma zero seven, the term three m p, and minus n q."
        )
        self.assertIn("4000", vocab)
        self.assertIn("7", vocab)
        self.assertIn("1.07", vocab)
        self.assertIn("3mp", vocab)
        self.assertIn("nq", vocab)
        self.assertIn("Thabo", vocab)
        self.assertIn("280", x.script_vocabulary("two hundred and eighty rand"))

    def test_case_bound_is_the_twin_minus_shared_difference(self):
        twin = x.script_vocabulary(fx.TWIN_SCRIPT)
        shared = x.script_vocabulary(fx.SHARED_SCRIPT)
        self.assertEqual(
            x.case_bound_tokens("R4 000 at 7% for 3 years", twin, shared), ["4000", "7"]
        )  # 3 years is taught by both scripts
        self.assertEqual(
            x.case_bound_tokens(
                "Simple interest is on the principal alone", twin, shared
            ),
            [],
        )
        # A number neither script teaches (a distractor) is not case-bound.
        self.assertEqual(x.case_bound_tokens("R9 999", twin, shared), [])


class DerivationTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)
        (self.shared_root, self.twin_root, self.shared, self.twin) = fx.make_trees(
            self.tmp
        )

    def _run(self, check=False, report=True):
        out = io.StringIO()
        with redirect_stdout(out):
            code, rep = x.run(
                self.shared_root,
                self.twin_root,
                "IEB",
                check=check,
                filter_text="",
                break_extractor=_extract,
                report_json=self.tmp / "report.json" if report else None,
                report_md=self.tmp / "report.md" if report else None,
            )
        return code, rep, out.getvalue()

    def test_case_bound_items_are_flagged_others_copied_as_is(self):
        code, rep, _ = self._run()
        self.assertEqual(code, 0)
        ov = co.read_overlay(self.shared, "IEB")
        by_id = {q["id"]: q for q in co.mcq_questions(ov["mcq"])}
        self.assertNotIn(co.NEEDS_REAUTHOR, by_id["subtopic_1_q1"])
        self.assertTrue(by_id["subtopic_1_q2"][co.NEEDS_REAUTHOR])
        self.assertEqual(
            by_id["subtopic_1_q2"][co.CASE_BOUND_TOKENS], ["4000", "4840", "7"]
        )
        self.assertTrue(by_id["subtopic_2_q2"][co.NEEDS_REAUTHOR])
        self.assertIn("3mp", by_id["subtopic_2_q2"][co.CASE_BOUND_TOKENS])
        cc = {q["id"]: q for q in ov["comprehension"]["questions"]}
        self.assertTrue(cc["cc1"][co.NEEDS_REAUTHOR])
        self.assertNotIn(co.NEEDS_REAUTHOR, cc["cc2"])
        # Everything else is the twin verbatim.
        self.assertEqual(
            by_id["subtopic_1_q1"]["question"], "Simple interest is worked out on:"
        )
        self.assertEqual(ov["transcript"], fx.TWIN_TRANSCRIPT)
        entry = rep["lessons"][0]
        self.assertEqual(entry["id"], fx.LESSON_ID)
        self.assertEqual(
            [c["id"] for c in entry["mcq"]["case_bound"]],
            ["subtopic_1_q2", "subtopic_2_q2"],
        )
        self.assertEqual(entry["break_asks"]["total"], 2)
        self.assertEqual([c["ask"] for c in entry["break_asks"]["case_bound"]], [1])

    def test_never_copied_files_stay_out_and_the_six_files_land(self):
        self._run()
        target = co.overlay_dir(self.shared, "IEB")
        self.assertEqual(
            sorted(p.name for p in target.iterdir()), sorted(co.OVERLAY_FILES)
        )
        for name in x.NEVER_COPIED:
            self.assertFalse((target / name).exists(), name)
        # The shared package's own files are untouched.
        self.assertEqual(
            (self.shared / "script.md").read_text("utf-8"), fx.SHARED_SCRIPT
        )
        self.assertEqual(
            json.loads((self.shared / "mcq.json").read_text()), fx.SHARED_MCQ
        )

    def test_label_break_qa_and_exam_weight_content(self):
        self._run()
        ov = co.read_overlay(self.shared, "IEB")
        label = ov["label"]
        self.assertEqual(label["curriculum"], "IEB")
        self.assertEqual(label["content_basis"], "CAPS")
        self.assertEqual(label["sag_status"], "pending_fetch")
        self.assertEqual(label["needs_reauthor"], 3)
        self.assertEqual(label["break_asks_case_bound"], 1)
        self.assertEqual(label["break_audio"]["status"], "pending_recording")
        self.assertTrue(label["source_twin"].endswith(str(fx.REL_PACKAGE)))
        self.assertIn("break_qa.IEB.mp3", ov["break_qa"])
        self.assertIn("status: pending_recording", ov["break_qa"])
        self.assertTrue(
            ov["break_qa"].rstrip("\n").endswith(fx.TWIN_TRANSCRIPT.rstrip("\n"))
        )
        self.assertIn("pending SAG", ov["exam_weight"])

    def test_alignment_is_reported_not_repaired(self):
        _, rep, _ = self._run()
        align = rep["lessons"][0]["alignment"]
        self.assertTrue(align["mcq_refs_match"])
        self.assertFalse(align["mcq_layout_match"])  # twin adds subtopic_2_q2
        self.assertTrue(align["comprehension_ids_match"])
        self.assertTrue(align["subtopic_refs_match"])
        self.assertEqual(rep["summary"]["mcq_layout_mismatches"], 1)
        ov = co.read_overlay(self.shared, "IEB")
        self.assertEqual(
            co.mcq_ids_by_ref(ov["mcq"])["subtopic_2"],
            ["subtopic_2_q1", "subtopic_2_q2"],
        )

    def test_report_files_and_caps_wording_list(self):
        (self.shared / "intro.md").write_text(
            "In the CAPS course we grow money.\n", encoding="utf-8"
        )
        _, rep, _ = self._run()
        self.assertEqual(rep["summary"]["packages_scanned"], 1)
        self.assertEqual(rep["summary"]["overlays_written"], 1)
        self.assertEqual(rep["summary"]["items_case_bound"], 3)
        self.assertEqual(rep["summary"]["lessons_with_case_bound"], 1)
        self.assertEqual(rep["caps_wording"]["count"], 1)
        self.assertTrue(rep["caps_wording"]["files"][0]["file"].endswith("intro.md"))
        self.assertEqual(json.loads((self.tmp / "report.json").read_text()), rep)
        md = (self.tmp / "report.md").read_text(encoding="utf-8")
        self.assertIn("| Overlays written | 1 |", md)
        self.assertIn(f"`{fx.LESSON_ID}`", md)
        self.assertIn("intro.md` (1)", md)
        self.assertNotIn("generated_at", json.dumps(rep))

    def test_deterministic_and_check_mode_detects_drift(self):
        self._run()
        first = fx.tree_digest(co.overlay_dir(self.shared, "IEB"))
        self._run()
        self.assertEqual(first, fx.tree_digest(co.overlay_dir(self.shared, "IEB")))
        code, _, out = self._run(check=True)
        self.assertEqual(code, 0)
        self.assertIn("overlays match their twins", out)
        label = co.overlay_dir(self.shared, "IEB") / co.OVERLAY_LABEL
        label.write_text(label.read_text() + "\n", encoding="utf-8")
        code, _, out = self._run(check=True)
        self.assertEqual(code, 1)
        self.assertIn("DRIFT", out)
        # --check never writes: the drifted file is still drifted.
        self.assertTrue(label.read_text().endswith("\n\n"))

    def test_twin_tree_is_never_written(self):
        before = fx.tree_digest(self.twin_root)
        self._run()
        self._run(check=True)
        self.assertEqual(fx.tree_digest(self.twin_root), before)
        self.assertFalse((self.twin / co.OVERLAY_DIR).exists())

    def test_package_without_twin_gets_no_overlay(self):
        lonely = self.shared_root / "maths/session/grade11/term1/t/lonely"
        fx.write_package(
            lonely,
            script=fx.SHARED_SCRIPT,
            mcq=fx.SHARED_MCQ,
            cc=fx.SHARED_CC,
            transcript=fx.SHARED_TRANSCRIPT,
        )
        _, rep, _ = self._run()
        self.assertEqual(rep["summary"]["packages_scanned"], 2)
        self.assertEqual(rep["summary"]["packages_with_twin"], 1)
        self.assertFalse((lonely / co.OVERLAY_DIR).exists())


class RepoTreeTests(unittest.TestCase):
    """The committed IEB twin tree carries no overlay and gains no file."""

    def test_ieb_session_tree_has_no_overlays(self):
        ieb = REPO_ROOT / "lessons" / "curriculum" / "IEB"
        if not ieb.is_dir():
            self.skipTest("IEB tree not present")
        self.assertEqual(list(ieb.rglob(co.OVERLAY_DIR)), [])
        for folder in x.discover_packages(ieb):
            names = {p.name for p in folder.iterdir()}
            self.assertFalse(
                names - set(x.TWIN_SOURCES) - set(x.NEVER_COPIED),
                f"{folder} carries files beyond the 9-file contract",
            )


if __name__ == "__main__":
    unittest.main()
