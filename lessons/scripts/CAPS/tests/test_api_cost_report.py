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

"""Unit tests for lessons/scripts/CAPS/api_cost_report.py (stdlib unittest).

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

import api_cost_report  # noqa: E402

# Synthetic fixtures only — no real model identifiers.
LEGACY_CALL = {"api": "groq", "kind": "chat", "model": "model-alpha",
               "prompt_tokens": 100, "completion_tokens": 50,
               "total_tokens": 150, "ts": "2026-08-01T10:00:00Z"}
TAGGED_CALL = {"api": "groq", "kind": "chat", "model": "model-alpha",
               "prompt_tokens": 200, "completion_tokens": 100,
               "total_tokens": 300, "ts": "2026-08-02T10:00:00Z",
               "run_id": "111", "job_id": "card_abc", "retries": 2}
JULES_CALL = {"api": "jules", "kind": "create_session", "title": "t",
              "session": "s", "prompt_chars": 42,
              "ts": "2026-08-02T11:00:00Z", "run_id": "111"}
RL_EVENT = {"api": "groq", "kind": "rate_limit", "status": 429,
            "retry_after": 7, "attempt": 1, "ts": "2026-08-02T09:59:00Z",
            "run_id": "111", "job_id": "card_abc"}
FAIL_EVENT = {"api": "groq", "kind": "call_failed", "status": 429,
              "retries": 4, "ts": "2026-08-03T09:00:00Z", "run_id": "222"}


def write_log(tmpdir, lines):
    path = Path(tmpdir) / "api_usage.jsonl"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


class ParseTests(unittest.TestCase):
    def test_missing_file_is_empty(self):
        records, malformed = api_cost_report.parse_usage("/nonexistent/x.jsonl")
        self.assertEqual(records, [])
        self.assertEqual(malformed, 0)

    def test_malformed_and_legacy_lines(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = write_log(tmp, [
                json.dumps(LEGACY_CALL),
                "{not json at all",
                '"a bare string, not an object"',
                "",
                json.dumps(TAGGED_CALL),
            ])
            records, malformed = api_cost_report.parse_usage(path)
        self.assertEqual(len(records), 2)
        self.assertEqual(malformed, 2)
        # Legacy record keeps working with no new fields present.
        self.assertNotIn("run_id", records[0])


class AggregateTests(unittest.TestCase):
    def setUp(self):
        self.agg = api_cost_report.aggregate(
            [LEGACY_CALL, TAGGED_CALL, JULES_CALL, RL_EVENT, FAIL_EVENT])

    def test_by_model_tokens_calls_retries(self):
        groq = self.agg["by_model"][("groq", "model-alpha")]
        self.assertEqual(groq["calls"], 2)
        self.assertEqual(groq["prompt_tokens"], 300)
        self.assertEqual(groq["completion_tokens"], 150)
        self.assertEqual(groq["total_tokens"], 450)
        self.assertEqual(groq["retries"], 2)
        self.assertEqual(groq["rate_limit_hits"], 0)

    def test_events_group_without_model_and_are_not_calls(self):
        ev = self.agg["by_model"][("groq", "-")]
        self.assertEqual(ev["calls"], 0)
        self.assertEqual(ev["rate_limit_hits"], 1)
        self.assertEqual(ev["failed"], 1)

    def test_per_run_grouping_with_untagged_legacy(self):
        by_run = self.agg["by_run"]
        self.assertEqual(by_run["111"]["calls"], 2)  # groq tagged + jules
        self.assertEqual(by_run["111"]["rate_limit_hits"], 1)
        self.assertEqual(by_run["222"]["failed"], 1)
        self.assertEqual(by_run["untagged"]["calls"], 1)  # legacy record
        self.assertEqual(by_run["untagged"]["total_tokens"], 150)


class PricingTests(unittest.TestCase):
    def _render(self, lines, env):
        with tempfile.TemporaryDirectory() as tmp:
            path = write_log(tmp, lines)
            out = api_cost_report.render_dashboard_section(path, env=env)
        return "\n".join(out)

    def test_configured_price_table(self):
        with tempfile.TemporaryDirectory() as tmp:
            table = Path(tmp) / "prices.json"
            table.write_text(json.dumps({
                "currency": "USD",
                "prices": {
                    "groq": {"model-alpha": {"prompt_per_1m": 1000000.0,
                                             "completion_per_1m": 2000000.0}},
                    "jules": {"*": {"per_call": 0.5}},
                },
            }), encoding="utf-8")
            env = {"API_PRICE_TABLE": str(table)}
            text = self._render(
                [json.dumps(LEGACY_CALL), json.dumps(TAGGED_CALL),
                 json.dumps(JULES_CALL)], env)
        # groq: 300 prompt tok * 1 + 150 completion tok * 2 = 600.0
        self.assertIn("USD 600.0000", text)
        # jules: 1 call * 0.5
        self.assertIn("USD 0.5000", text)
        # grand total row
        self.assertIn("USD 600.5000", text)
        self.assertIn("Est. cost", text)
        self.assertNotIn("Pricing not configured", text)

    def test_unconfigured_pricing_shows_no_cost(self):
        text = self._render([json.dumps(LEGACY_CALL)], env={})
        self.assertIn("Pricing not configured", text)
        self.assertIn("API_PRICE_TABLE", text)
        self.assertNotIn("Est. cost", text)
        self.assertNotIn("Estimated total spend", text)
        # Tokens still reported.
        self.assertIn("150", text)

    def test_unreadable_table_treated_as_unconfigured(self):
        env = {"API_PRICE_TABLE": "/nonexistent/prices.json"}
        text = self._render([json.dumps(LEGACY_CALL)], env=env)
        self.assertIn("could not be read", text)
        self.assertNotIn("Est. cost", text)

    def test_model_without_price_entry_shows_no_number(self):
        with tempfile.TemporaryDirectory() as tmp:
            table = Path(tmp) / "prices.json"
            table.write_text(json.dumps({
                "prices": {"groq": {"some-other-model":
                                    {"prompt_per_1m": 1.0}}},
            }), encoding="utf-8")
            env = {"API_PRICE_TABLE": str(table)}
            text = self._render([json.dumps(LEGACY_CALL)], env=env)
        self.assertIn("no price", text)
        self.assertIn("no entry in the", text)


class RenderTests(unittest.TestCase):
    def test_section_shape_and_malformed_note(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = write_log(tmp, [json.dumps(LEGACY_CALL), "oops-not-json"])
            out = api_cost_report.render_dashboard_section(path, env={})
        self.assertEqual(out[0], "## Cost / rate-limits")
        self.assertEqual(out[-1], "")
        text = "\n".join(out)
        self.assertIn("### By API / model", text)
        self.assertIn("### By run", text)
        self.assertIn("untagged (legacy records)", text)
        self.assertIn("1 malformed log line(s) skipped", text)

    def test_empty_log(self):
        out = api_cost_report.render_dashboard_section(
            "/nonexistent/x.jsonl", env={})
        self.assertIn("No API usage recorded yet.", "\n".join(out))


if __name__ == "__main__":
    unittest.main()
