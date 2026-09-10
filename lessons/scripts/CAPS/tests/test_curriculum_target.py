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

"""Tests for curriculum_target — the --curriculum resolution the four index
builders share.

The property that matters most is the first one: a no-flag run, and an
explicit `--curriculum CAPS`, must resolve to exactly the paths the
builders used before the flag existed. If that regresses, every workflow
that commits lessons/*.json starts writing somewhere else.
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import curriculum_target as ct  # noqa: E402

REPO = Path("/repo")


class ParseCurriculumTests(unittest.TestCase):
    def test_absent_defaults_to_caps(self):
        self.assertEqual(ct.parse_curriculum([]), "CAPS")
        self.assertEqual(ct.parse_curriculum(None), "CAPS")

    def test_existing_publish_flag_is_ignored(self):
        self.assertEqual(ct.parse_curriculum(["--publish"]), "CAPS")

    def test_space_and_equals_forms(self):
        self.assertEqual(ct.parse_curriculum(["--curriculum", "IEB"]), "IEB")
        self.assertEqual(ct.parse_curriculum(["--curriculum=IEB"]), "IEB")

    def test_combined_with_publish(self):
        self.assertEqual(
            ct.parse_curriculum(["--curriculum", "IEB", "--publish"]), "IEB"
        )
        self.assertEqual(
            ct.parse_curriculum(["--publish", "--curriculum=IEB"]), "IEB"
        )

    def test_rejects_empty_and_path_traversal(self):
        for bad in ([" "], ["../etc"], ["a/b"], [".hidden"]):
            with self.assertRaises(ValueError):
                ct.parse_curriculum(["--curriculum"] + bad)

    def test_missing_value_falls_back_rather_than_crashing(self):
        # Trailing flag with no value: nothing to read, so the default holds.
        self.assertEqual(ct.parse_curriculum(["--curriculum"]), "CAPS")


class PathResolutionTests(unittest.TestCase):
    def test_caps_keeps_the_historical_flat_output_paths(self):
        for name in (
            "skills_index.json",
            "practice_bank.json",
            "knowledge_bites_index.json",
            "review_index.json",
        ):
            self.assertEqual(
                ct.output_path(REPO, "CAPS", name), REPO / "lessons" / name
            )

    def test_caps_root_unchanged(self):
        self.assertEqual(
            ct.curriculum_root(REPO, "CAPS"),
            REPO / "lessons" / "curriculum" / "CAPS",
        )

    def test_other_curricula_are_namespaced(self):
        self.assertEqual(
            ct.output_path(REPO, "IEB", "practice_bank.json"),
            REPO / "lessons" / "IEB" / "practice_bank.json",
        )
        self.assertEqual(
            ct.curriculum_root(REPO, "IEB"),
            REPO / "lessons" / "curriculum" / "IEB",
        )

    def test_no_curriculum_can_collide_with_caps_output(self):
        caps = ct.output_path(REPO, "CAPS", "review_index.json")
        for other in ("IEB", "CAMBRIDGE", "US"):
            self.assertNotEqual(ct.output_path(REPO, other, "review_index.json"), caps)

    def test_resolve_returns_the_triple(self):
        curriculum, root, out = ct.resolve(REPO, ["--curriculum", "IEB"], "x.json")
        self.assertEqual(curriculum, "IEB")
        self.assertEqual(root, REPO / "lessons" / "curriculum" / "IEB")
        self.assertEqual(out, REPO / "lessons" / "IEB" / "x.json")


class BuilderWiringTests(unittest.TestCase):
    """Each builder must import the helper and re-point BOTH globals, or a
    --curriculum run would read one tree and overwrite another's index."""

    BUILDERS = (
        "build_skills_index",
        "build_practice_bank",
        "build_knowledge_bites_index",
        "build_review_index",
    )

    def test_every_builder_is_wired(self):
        scripts = Path(__file__).resolve().parents[1]
        for name in self.BUILDERS:
            source = (scripts / f"{name}.py").read_text(encoding="utf-8")
            with self.subTest(builder=name):
                self.assertIn("import curriculum_target", source)
                self.assertIn("curriculum_target.resolve(", source)
                self.assertIn("global CAPS_ROOT, OUTPUT_PATH", source)


if __name__ == "__main__":
    unittest.main()
