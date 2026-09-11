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

"""The factory-owned curriculum registry (lessons/curriculum/curricula.json):
exactly CAPS, IEB and Cambridge; Cambridge is "soon", content blocked
pending permission, with no overlay anywhere; labels, the manifest
`curricula` list and badges derive from the registry; every generator and
validator refuses a Cambridge overlay.

Run from the repo root:
    python3 -m unittest discover -s lessons/scripts/CAPS/tests -v
"""

import io
import sys
import tempfile
import unittest
from contextlib import redirect_stderr
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_practice_bank as bank  # noqa: E402
import curriculum_overlay as co  # noqa: E402
import curriculum_target as ct  # noqa: E402
import extract_curriculum_overlays as x  # noqa: E402
import lesson_compliance  # noqa: E402
import overlay_fixture as fx  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[4]


class RegistryContentTests(unittest.TestCase):
    def test_registry_names_exactly_caps_ieb_cambridge(self):
        entries = ct.registry_entries()
        self.assertEqual([e["id"] for e in entries], ["CAPS", "IEB", "CAMBRIDGE"])
        self.assertEqual([e["name"] for e in entries], ["CAPS", "IEB", "Cambridge"])
        self.assertEqual(ct.load_registry()["default"], ct.DEFAULT_CURRICULUM)
        self.assertEqual(ct.REGISTRY_PATH, Path("lessons/curriculum/curricula.json"))
        self.assertTrue((REPO_ROOT / ct.REGISTRY_PATH).is_file())

    def test_cambridge_is_soon_blocked_and_has_no_overlay(self):
        cam = ct.curriculum_entry("CAMBRIDGE")
        self.assertEqual(cam["status"], "soon")
        self.assertEqual(cam["content"], "blocked_pending_permission")
        self.assertIsNone(cam["delivery"])
        self.assertEqual(cam["badge"], "Cambridge")
        self.assertFalse(ct.content_allowed("CAMBRIDGE"))
        lessons = REPO_ROOT / "lessons"
        self.assertEqual(list(lessons.rglob("overlays/CAMBRIDGE")), [])
        self.assertEqual(list(lessons.rglob("overlays/Cambridge")), [])

    def test_caps_and_ieb_are_live_and_allowed(self):
        self.assertEqual(ct.status("CAPS"), "live")
        self.assertEqual(ct.curriculum_entry("CAPS")["delivery"], "package")
        self.assertEqual(ct.status("IEB"), "live")
        self.assertEqual(ct.curriculum_entry("IEB")["delivery"], "overlay")
        self.assertEqual(ct.curriculum_entry("IEB")["content_basis"], "CAPS")
        self.assertTrue(ct.content_allowed("CAPS"))
        self.assertTrue(ct.content_allowed("IEB"))
        self.assertFalse(ct.content_allowed("US"))
        self.assertEqual(
            ct.ordered({"IEB", "CAPS", "CAMBRIDGE", "US"}), ["CAPS", "IEB", "CAMBRIDGE"]
        )

    def test_committed_overlays_are_only_live_curricula(self):
        seen = {
            p.name for p in (REPO_ROOT / "lessons").rglob("overlays/*") if p.is_dir()
        }
        self.assertEqual(seen, {"IEB"})


class DerivedFromRegistryTests(unittest.TestCase):
    def test_label_badge_and_manifest_order_come_from_the_registry(self):
        self.assertEqual(co.make_label("IEB")["badge"], ct.badge("IEB"))
        bad = co.make_label("IEB")
        bad["badge"] = "IEB (beta)"
        self.assertTrue(any("registry badge" in p for p in co.validate_label(bad)))
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / "lesson"
            folder.mkdir()
            co.write_overlay(
                folder,
                "IEB",
                mcq=fx.TWIN_MCQ,
                comprehension=fx.TWIN_CC,
                transcript="",
                break_qa="",
                exam_weight="",
                label=co.make_label("IEB"),
            )
            block = co.build_variants(
                folder,
                fx.SHARED_MCQ,
                fx.SHARED_CC,
                [],
                break_question_extractor=lambda t: [],
            )
        self.assertEqual(block["curricula"], ct.ordered(["IEB", "CAPS"]))
        self.assertEqual(block["variants"]["CAPS"]["label"]["badge"], ct.badge("CAPS"))
        self.assertEqual(block["variants"]["IEB"]["label"]["badge"], ct.badge("IEB"))


class CambridgeRefusalTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)
        self.shared_root, _, self.shared, self.twin = fx.make_trees(self.tmp)

    def _cambridge_overlay(self):
        target = co.overlay_dir(self.shared, "CAMBRIDGE")
        target.mkdir(parents=True)
        (target / co.OVERLAY_MCQ).write_text(co.dumps(fx.TWIN_MCQ))
        (target / co.OVERLAY_COMPREHENSION).write_text(co.dumps(fx.TWIN_CC))
        label = co.make_label("IEB")
        label["curriculum"] = label["badge"] = "CAMBRIDGE"
        (target / co.OVERLAY_LABEL).write_text(co.dumps(label))
        return target

    def test_make_label_refuses_cambridge(self):
        with self.assertRaises(co.OverlayError):
            co.make_label("CAMBRIDGE")

    def test_extraction_refuses_cambridge(self):
        err = io.StringIO()
        with redirect_stderr(err), self.assertRaises(SystemExit) as cm:
            x.main(
                [
                    "--curriculum",
                    "CAMBRIDGE",
                    "--root",
                    str(self.shared_root),
                    "--twin-root",
                    str(self.twin.parents[5]),
                    "--no-report",
                ]
            )
        self.assertNotEqual(cm.exception.code, 0)
        self.assertIn("blocked_pending_permission", err.getvalue())
        self.assertFalse((self.shared / co.OVERLAY_DIR).exists())

    def test_r7_and_assembly_refuse_a_cambridge_overlay(self):
        target = self._cambridge_overlay()
        r7 = [
            v
            for v in lesson_compliance.run([target / co.OVERLAY_LABEL])[0]
            if v[0] == "R7"
        ]
        self.assertTrue(any("blocked_pending_permission" in m for _, m in r7))
        with self.assertRaises(co.OverlayError):
            co.build_variants(
                self.shared,
                fx.SHARED_MCQ,
                fx.SHARED_CC,
                [],
                break_question_extractor=lambda t: [],
            )

    def test_practice_bank_refuses_cambridge(self):
        with self.assertRaises(ValueError):
            bank.parse_overlay_curricula(
                ["--include-overlay-curricula", "CAMBRIDGE"], environ={}
            )
        with self.assertRaises(ValueError):
            bank.parse_overlay_curricula(
                [], environ={"ROKCT_PRACTICE_OVERLAY_CURRICULA": "IEB,CAMBRIDGE"}
            )
        self.assertEqual(bank.parse_overlay_curricula([], environ={}), ())
        self.assertEqual(
            bank.parse_overlay_curricula(
                ["--include-overlay-curricula=IEB"], environ={}
            ),
            ("IEB",),
        )
        self.assertEqual(
            bank.parse_overlay_curricula(
                [], environ={"ROKCT_PRACTICE_OVERLAY_CURRICULA": "IEB"}
            ),
            ("IEB",),
        )


if __name__ == "__main__":
    unittest.main()
