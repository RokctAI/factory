"""open_agent_pr.py against a local mock of the GitHub REST API.

    python -m unittest voice_batch/tests/test_open_agent_pr.py
"""
from __future__ import annotations

import io
import json
import os
import sys
import tempfile
import threading
import unittest
from contextlib import redirect_stdout
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ci"))
import open_agent_pr  # noqa: E402

TOKEN = "test-token"
HEAD = "rokct/r3-phonics-probe"
SECRET_TEXT = "Listen. a as in ant."
SECRET_ID = "english_home_language.gradeR.term1.w01_sound_a.show"


class FakeGitHub:
    def __init__(self):
        self.pulls: list[dict] = []
        self.comments: dict[int, list[dict]] = {}
        self.calls: list[tuple[str, str]] = []
        self.auth_ok = True

    def handler(self):
        gh = self

        class H(BaseHTTPRequestHandler):
            def log_message(self, *a):
                pass

            def reply(self, status, obj):
                data = json.dumps(obj).encode()
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)

            def route(self, method):
                u = urlparse(self.path)
                gh.calls.append((method, u.path))
                if self.headers.get("Authorization") != f"Bearer {TOKEN}":
                    gh.auth_ok = False
                    return self.reply(401, {"message": "Bad credentials"})
                body = json.loads(self.rfile.read(int(self.headers.get("Content-Length") or 0)) or b"null")
                if u.path == "/repos/RokctAI/agent/pulls" and method == "GET":
                    q = parse_qs(u.query)
                    return self.reply(200, [p for p in gh.pulls if p["state"] == "open"
                                            and f"RokctAI:{p['head']}" == q["head"][0] and p["base"] == q["base"][0]])
                if u.path == "/repos/RokctAI/agent/pulls" and method == "POST":
                    pr = {"number": 100 + len(gh.pulls), "state": "open", **body}
                    gh.pulls.append(pr)
                    return self.reply(201, pr)
                if u.path.startswith("/repos/RokctAI/agent/issues/") and u.path.endswith("/comments"):
                    num = int(u.path.split("/")[5])
                    if method == "GET":
                        return self.reply(200, gh.comments.get(num, []))
                    gh.comments.setdefault(num, []).append(body)
                    return self.reply(201, body)
                return self.reply(404, {"message": "Not Found"})

            def do_GET(self):
                self.route("GET")

            def do_POST(self):
                self.route("POST")

        return H


class OpenAgentPr(unittest.TestCase):
    def setUp(self):
        self.gh = FakeGitHub()
        self.srv = ThreadingHTTPServer(("127.0.0.1", 0), self.gh.handler())
        threading.Thread(target=self.srv.serve_forever, daemon=True).start()
        self.tmp = tempfile.TemporaryDirectory()
        self.manifest = Path(self.tmp.name, "r3_manifest.voice_a.json")
        self.manifest.write_text(json.dumps({
            "lines": [{"id": SECRET_ID, "text": SECRET_TEXT, "needs_listen": True, "ci_run_id": "7"},
                      {"id": "old", "text": "Old.", "ci_run_id": "3"}],
            "failed": [{"id": "r3.r3_praise_yes", "ci_run_id": "7", "text": "Yes!", "attempts": 5,
                        "rounds": [{"round": 3, "failing": {"asr": {"asr_word_errors": 1},
                                                            "loudness": {"integrated_db": -26.0}}}]}]}))
        self.env = {"AGENT_PAT": TOKEN, "GITHUB_API_URL": f"http://127.0.0.1:{self.srv.server_port}",
                    "NO_PROXY": "127.0.0.1", "no_proxy": "127.0.0.1"}
        self._old = {k: os.environ.get(k) for k in self.env}
        os.environ.update(self.env)
        for k in ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"):
            self._old.setdefault(k, os.environ.pop(k, None))

    def tearDown(self):
        self.srv.shutdown()
        self.tmp.cleanup()
        for k, v in self._old.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v

    def run_it(self, run_id="7", head=HEAD, target="r3"):
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = open_agent_pr.main(["--repo", "RokctAI/agent", "--head", head, "--target", target,
                                     "--voice", "voice_a", "--manifest", str(self.manifest),
                                     "--run-id", run_id, "--run-url", f"https://github.com/RokctAI/factory/actions/runs/{run_id}"])
        return rc, buf.getvalue()

    def test_opens_ready_pr_once_then_comments_once_per_run(self):
        rc, out = self.run_it()
        self.assertEqual(rc, 0, out)
        self.assertEqual(len(self.gh.pulls), 1)
        pr = self.gh.pulls[0]
        self.assertIs(pr["draft"], False)
        self.assertEqual((pr["head"], pr["base"]), (HEAD, "main"))
        self.assertEqual(pr["title"], "r3 voice_a: rendered audio (voice batch)")
        body = pr["body"]
        self.assertTrue(body.startswith("<!-- ccr-projects-attribution -->\n_Requested by **Ray** via a Claude Code Project_"))
        self.assertTrue(body.rstrip().endswith("https://claude.ai/code/session_01WVrZ3ZtDLBuD78jnGwzGHF"))
        self.assertIn("🤖 Generated with [Claude Code](https://claude.com/claude-code)", body)
        self.assertIn("Before", body)
        self.assertIn("Merging this PR ships the audio into the app bundle", body)
        self.assertIn("https://github.com/RokctAI/factory/actions/runs/7", body)
        self.assertIn("This run: 1 passed, 1 failed, 1 respelled for phonics", body)
        self.assertIn("Branch manifest total: 2 passed, 1 failed", body)
        for secret in (SECRET_TEXT, SECRET_ID, "Old.", "Yes!"):
            self.assertNotIn(secret, body)
        # Failed QC: the final-failed line's id, attempts and last-round gates (never its text).
        self.assertIn("## Failed QC", body)
        self.assertIn("| `r3.r3_praise_yes` |  | 5 | asr, loudness |", body)
        self.assertTrue(self.gh.auth_ok)

        # Same run again (step re-run): no second PR, one comment.
        rc, out = self.run_it()
        self.assertEqual(rc, 0, out)
        self.assertEqual(len(self.gh.pulls), 1)
        self.assertEqual(len(self.gh.comments[100]), 1)
        c = self.gh.comments[100][0]["body"]
        self.assertIn("<!-- voice-batch-run:7 -->", c)
        self.assertIn("1 passed, 1 failed", c)
        self.assertNotIn(SECRET_ID, c)
        self.assertIn("## Failed QC", c)
        self.assertNotIn("Yes!", c)
        # ...and again: the marker stops a duplicate comment.
        rc, out = self.run_it()
        self.assertIn("already noted", out)
        self.assertEqual(len(self.gh.comments[100]), 1)
        # A new run adds exactly one more.
        self.run_it(run_id="8")
        self.assertEqual(len(self.gh.comments[100]), 2)
        self.assertIn("This run: 0 passed, 0 failed", self.gh.comments[100][1]["body"])
        self.assertNotIn(TOKEN, out)

    def test_tutor_title_and_refusals(self):
        rc, _ = self.run_it(target="tutor_001")
        self.assertEqual(rc, 0)
        self.assertEqual(self.gh.pulls[0]["title"], "tutor_001 voice_a: rendered audio (voice batch)")
        n = len(self.gh.calls)
        for kw in ({"head": "main"}, {"head": "rokct/../main"}, {"head": "claude/r3-phonics-probe"}, {"target": "tutor_1; rm"}):
            rc, _ = self.run_it(**kw)
            self.assertEqual(rc, 1, kw)
        self.assertEqual(len(self.gh.calls), n)  # refused before any API call


if __name__ == "__main__":
    unittest.main()
