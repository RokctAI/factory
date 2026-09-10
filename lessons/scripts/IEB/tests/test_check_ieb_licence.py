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

"""Unit tests for lessons/scripts/IEB/check_ieb_licence.py (stdlib unittest).

Two things are worth pinning. First, the gate must pass on the tree as it
stands today — a guard that is red on arrival gets disabled rather than
respected, so "empty or absent index is clear" is a test, not an assumption.
Second, it must actually fail on content, fail closed on an index it cannot
parse, and lift only on the explicit permission token — a gate that can be
opened by an accidental empty file is not a gate.

The real repository tree is also asserted to be clear, so this suite fails
the day IEB bite content lands without permission even if the gate's own
workflow is not what runs.

Run from the repo root:
    python3 -m unittest discover -s lessons/scripts/IEB/tests -v
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import check_ieb_licence as gate  # noqa: E402


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def index_with(bites) -> str:
    return json.dumps({"version": 1, "generated_at": "2026-01-01T00:00:00Z",
                       "bites": bites})


A_BITE = {
    "bite_slug": "ieb-physical-sciences-g12-p2-2024-nov-q7-1",
    "subject": "physical_sciences",
    "grade": 12,
    "title": "Past-Paper Worked Example - Q7.1",
    "question_md": "# Past-Paper Worked Example - Q7.1\n\nfull question text\n",
}


class CheckIebLicenceTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def index_path(self) -> Path:
        return self.root / gate.INDEX_PATH

    def grant_permission(self, text=None):
        write(self.root / gate.PERMISSION_PATH,
              text if text is not None else
              f"# IEB permission\n\n{gate.PERMISSION_TOKEN}\n")

    # --- the states that must pass -------------------------------------

    def test_absent_index_is_clear(self):
        code, report = gate.check(self.root)
        self.assertEqual(code, 0)
        self.assertIn("does not exist", report)

    def test_empty_bites_map_is_clear(self):
        write(self.index_path(), index_with({}))
        code, report = gate.check(self.root)
        self.assertEqual(code, 0)
        self.assertIn("empty", report)

    def test_lesson_key_with_no_bites_is_clear(self):
        write(self.index_path(), index_with({"some-lesson": []}))
        self.assertEqual(gate.check(self.root)[0], 0)

    # --- the state that must fail --------------------------------------

    def test_one_bite_blocks(self):
        write(self.index_path(), index_with({"momentum-and-impulse": [A_BITE]}))
        code, report = gate.check(self.root)
        self.assertEqual(code, 1)
        self.assertIn("BLOCKED", report)
        self.assertIn("1 knowledge bite(s)", report)

    def test_block_message_explains_itself(self):
        write(self.index_path(), index_with({"a": [A_BITE], "b": [A_BITE]}))
        code, report = gate.check(self.root)
        self.assertEqual(code, 1)
        # Why, not just what.
        self.assertIn("may not be reproduced for commercial gain", report)
        self.assertIn("WRITTEN permission", report)
        self.assertIn("NOT A BUG", report)
        # The paths someone needs in order to act on it.
        self.assertIn(gate.SOURCES_PATH.as_posix(), report)
        self.assertIn(gate.PERMISSION_PATH.as_posix(), report)
        self.assertIn(gate.PERMISSION_TOKEN, report)
        self.assertIn("2 knowledge bite(s) across 2 lesson(s)", report)

    def test_unparseable_index_fails_closed(self):
        write(self.index_path(), "{ not json")
        code, report = gate.check(self.root)
        self.assertEqual(code, 1)
        self.assertIn("fails closed", report)

    def test_bites_wrong_type_fails_closed(self):
        write(self.index_path(), json.dumps({"bites": "plenty"}))
        self.assertEqual(gate.check(self.root)[0], 1)

    # --- lifting the gate ----------------------------------------------

    def test_permission_token_lifts_the_gate(self):
        write(self.index_path(), index_with({"momentum-and-impulse": [A_BITE]}))
        self.grant_permission()
        code, report = gate.check(self.root)
        self.assertEqual(code, 0)
        self.assertIn("lifted", report)

    def test_empty_marker_file_does_not_lift_the_gate(self):
        write(self.index_path(), index_with({"momentum-and-impulse": [A_BITE]}))
        self.grant_permission(text="")
        self.assertEqual(gate.check(self.root)[0], 1)

    def test_marker_without_token_does_not_lift_the_gate(self):
        write(self.index_path(), index_with({"momentum-and-impulse": [A_BITE]}))
        self.grant_permission(text="We have asked the IEB and are waiting.\n")
        self.assertEqual(gate.check(self.root)[0], 1)

    def test_permission_alone_is_not_a_failure(self):
        """The marker on an empty tree is harmless, not an error."""
        self.grant_permission()
        self.assertEqual(gate.check(self.root)[0], 0)

    # --- the tree as it actually is ------------------------------------

    def test_real_repository_tree_is_clear(self):
        code, report = gate.check(gate.repo_root_from_here())
        self.assertEqual(code, 0, report)

    def test_main_returns_zero_on_real_tree(self):
        self.assertEqual(gate.main([]), 0)

    def test_main_returns_one_on_a_non_empty_fixture(self):
        write(self.index_path(), index_with({"momentum-and-impulse": [A_BITE]}))
        self.assertEqual(gate.main(["--repo-root", str(self.root)]), 1)


if __name__ == "__main__":
    unittest.main()
