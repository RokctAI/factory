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

"""Unit tests for lessons/scripts/CAPS/api_call_logged.py (stdlib unittest).

The delegate HTTP layer is mocked with a fake delegate script that fails
with a 429-style error N times (tracked in a state file) before succeeding
and appending a usage record — mirroring what the pin-fetched
delegate_to_agent.py does on a real call.

Run from the repo root:
    python3 -m unittest discover -s lessons/scripts/CAPS/tests -v
"""

import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import api_call_logged  # noqa: E402

FAKE_DELEGATE = """\
import json, os, sys
state = os.environ["FAKE_STATE"]
n = int(open(state).read()) if os.path.exists(state) else 0
open(state, "w").write(str(n + 1))
mode = os.environ.get("FAKE_MODE", "rate_limit_then_ok")
fails = int(os.environ.get("FAKE_FAILS", "2"))
if mode == "hard_error":
    sys.stderr.write("Traceback: boom, credentials missing\\n")
    sys.exit(2)
if n < fails:
    sys.stderr.write(
        "requests.exceptions.HTTPError: 429 Client Error: "
        "Too Many Requests for url: https://api.example/chat\\n"
        "Retry-After: 0\\n")
    sys.exit(1)
with open(os.environ["API_USAGE_LOG"], "a", encoding="utf-8") as fh:
    fh.write(json.dumps({
        "api": "groq", "kind": "chat", "model": "model-alpha",
        "prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15,
        "ts": "2026-08-14T00:00:00Z"}) + "\\n")
sys.stdout.write("FAKE RESPONSE TEXT")
"""


class WrapperTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        base = Path(self.tmp.name)
        self.delegate = base / "fake_delegate.py"
        self.delegate.write_text(FAKE_DELEGATE, encoding="utf-8")
        self.log = base / "api_usage.jsonl"
        # A pre-existing legacy line the wrapper must never touch.
        self.legacy = json.dumps({"api": "groq", "kind": "chat",
                                  "model": "model-alpha", "total_tokens": 9,
                                  "ts": "2026-07-01T00:00:00Z"})
        self.log.write_text(self.legacy + "\n", encoding="utf-8")
        self.state = base / "state.txt"
        self._old_env = dict(os.environ)
        os.environ.update({
            "API_DELEGATE_SCRIPT": str(self.delegate),
            "API_USAGE_LOG": str(self.log),
            "API_CALL_BACKOFF_BASE": "0",
            "FAKE_STATE": str(self.state),
            "GITHUB_RUN_ID": "424242",
        })
        os.environ.pop("FAKE_MODE", None)
        os.environ.pop("FAKE_FAILS", None)

    def tearDown(self):
        os.environ.clear()
        os.environ.update(self._old_env)
        self.tmp.cleanup()

    def _run(self, argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = api_call_logged.main(argv)
        return code, out.getvalue(), err.getvalue()

    def _log_records(self):
        return [json.loads(l) for l in
                self.log.read_text(encoding="utf-8").splitlines()]

    def test_429_retry_then_success_logs_events_and_annotates(self):
        os.environ["FAKE_FAILS"] = "2"
        code, out, err = self._run(
            ["--api", "groq", "--job-id", "card_xyz",
             "groq", "--prompt", "hello"])
        self.assertEqual(code, 0)
        self.assertEqual(out, "FAKE RESPONSE TEXT")  # stdout passthrough
        self.assertEqual(self.state.read_text(), "3")  # 2 failures + 1 ok

        recs = self._log_records()
        # Legacy first line untouched.
        self.assertEqual(json.dumps(recs[0]), self.legacy)
        rl = [r for r in recs if r.get("kind") == "rate_limit"]
        self.assertEqual(len(rl), 2)
        self.assertEqual(rl[0]["status"], 429)
        self.assertEqual(rl[0]["retry_after"], 0)
        self.assertEqual(rl[0]["run_id"], "424242")
        self.assertEqual(rl[0]["job_id"], "card_xyz")
        final = recs[-1]
        self.assertEqual(final["kind"], "chat")
        self.assertEqual(final["retries"], 2)
        self.assertEqual(final["run_id"], "424242")
        self.assertEqual(final["job_id"], "card_xyz")

    def test_success_first_try_annotates_zero_retries(self):
        os.environ["FAKE_FAILS"] = "0"
        code, out, _ = self._run(["--api", "groq", "groq", "--prompt", "x"])
        self.assertEqual(code, 0)
        final = self._log_records()[-1]
        self.assertEqual(final["retries"], 0)
        self.assertEqual(final["run_id"], "424242")
        self.assertNotIn("job_id", final)  # none given

    def test_retries_exhausted_logs_call_failed_and_fails(self):
        os.environ["FAKE_FAILS"] = "99"
        code, _, err = self._run(
            ["--api", "groq", "--max-retries", "2", "groq", "--prompt", "x"])
        self.assertEqual(code, 1)
        self.assertEqual(self.state.read_text(), "3")  # 1 + 2 retries, bounded
        recs = self._log_records()
        self.assertEqual(
            len([r for r in recs if r.get("kind") == "rate_limit"]), 3)
        self.assertEqual(recs[-1]["kind"], "call_failed")
        self.assertEqual(recs[-1]["status"], 429)
        self.assertIn("giving up", err)

    def test_non_rate_limit_failure_passes_through_without_retry(self):
        os.environ["FAKE_MODE"] = "hard_error"
        code, _, err = self._run(["--api", "groq", "groq", "--prompt", "x"])
        self.assertEqual(code, 2)
        self.assertEqual(self.state.read_text(), "1")  # no retry
        self.assertIn("boom", err)
        recs = self._log_records()
        self.assertEqual(len(recs), 1)  # only the legacy line; no events


if __name__ == "__main__":
    unittest.main()
