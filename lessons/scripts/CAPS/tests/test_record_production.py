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

"""record_production: --base-url is optional. Level 6 no longer publishes
releases, so it records checksums/sizes without writing download URLs.

Run from the repo root:
    python3 -m unittest discover -s lessons/scripts/CAPS/tests -v
"""

import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import record_production as rp  # noqa: E402

CARD = "---\nid: x\nstatus: producing\n---\nbody\n"


class RecordProductionTests(unittest.TestCase):
    def run_main(self, *extra):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            for name in ("manifest.json", "audio.mp3", "animations.json"):
                (d / name).write_bytes(b"x" * 3)
            card = d / "card.md"
            card.write_text(CARD, encoding="utf-8")
            argv = ["rp", "--card", str(card), "--out-dir", str(d), *extra]
            with mock.patch.object(sys, "argv", argv):
                rp.main()
            return card.read_text(encoding="utf-8")

    def test_without_base_url_no_url_fields(self):
        out = self.run_main()
        self.assertNotIn("_url:", out)
        self.assertIn("manifest_checksum:", out)
        self.assertIn("audio_size_bytes: 3", out)
        self.assertIn("produced_at:", out)

    def test_with_base_url_writes_urls(self):
        out = self.run_main("--base-url", "https://h/d")
        self.assertIn("manifest_url: https://h/d/manifest.json", out)
        self.assertIn("animation_url: https://h/d/animations.json", out)


if __name__ == "__main__":
    unittest.main()
