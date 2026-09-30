"""push_agent.sh against a local token-protected git HTTP server.

Reproduces the CI layout: a sparse, blob-less, depth-1 checkout with no
persisted credentials, and a sibling category job that pushes first, so our
push is rejected and must rebase. The rebase lazily fetches blobs from the
promisor remote and needs the auth header too.

    python -m unittest voice_batch/tests/test_push_agent.py
"""
from __future__ import annotations

import base64
import os
import shutil
import subprocess
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "voice_batch" / "ci" / "push_agent.sh"
TOKEN = "test-token"
EXPECTED = "Basic " + base64.b64encode(f"x-access-token:{TOKEN}".encode()).decode()
BRANCH = "rokct/tutor-001-voice-a-test"
TDIR = "lms/team/tutors/CAPS/tutor_001"
ADIR = "lms/dart/templates/assets/r3_packs/audio"


def http_backend() -> str | None:
    try:
        exec_path = subprocess.run(["git", "--exec-path"], capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None
    p = Path(exec_path) / "git-http-backend"
    return str(p) if p.exists() else None


def make_handler(project_root: str, backend: str):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def _serve(self):
            if self.headers.get("Authorization", "").lower() != EXPECTED.lower():
                self.send_response(401)
                self.send_header("WWW-Authenticate", 'Basic realm="test"')
                self.send_header("Content-Length", "0")
                self.end_headers()
                return
            path, _, query = self.path.partition("?")
            body = self.rfile.read(int(self.headers.get("Content-Length") or 0))
            env = {
                "PATH": os.environ["PATH"],
                "GIT_PROJECT_ROOT": project_root,
                "GIT_HTTP_EXPORT_ALL": "1",
                "REMOTE_USER": "x-access-token",
                "REQUEST_METHOD": self.command,
                "PATH_INFO": path,
                "QUERY_STRING": query,
                "CONTENT_TYPE": self.headers.get("Content-Type", ""),
                "CONTENT_LENGTH": str(len(body)),
                "GIT_CONFIG_NOSYSTEM": "1",
                "GIT_CONFIG_GLOBAL": os.devnull,
            }
            if self.headers.get("Git-Protocol"):
                env["GIT_PROTOCOL"] = self.headers["Git-Protocol"]
            if self.headers.get("Content-Encoding"):
                env["HTTP_CONTENT_ENCODING"] = self.headers["Content-Encoding"]
            out = subprocess.run([backend], input=body, capture_output=True, env=env).stdout
            head, _, payload = out.partition(b"\r\n\r\n")
            status, headers = 200, []
            for line in head.decode().split("\r\n"):
                if not line:
                    continue
                k, _, v = line.partition(":")
                if k.lower() == "status":
                    status = int(v.split()[0])
                else:
                    headers.append((k, v.strip()))
            self.send_response(status)
            for k, v in headers:
                self.send_header(k, v)
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

        do_GET = do_POST = _serve

    return Handler


@unittest.skipUnless(http_backend() and shutil.which("bash"), "needs git-http-backend and bash")
class PushAgentRebaseTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.env = {
            **os.environ,
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_TERMINAL_PROMPT": "0",
            "GIT_ASKPASS": "",
            "SSH_ASKPASS": "",
            "NO_PROXY": "127.0.0.1,localhost",
            "no_proxy": "127.0.0.1,localhost",
            "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.com",
            "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.com",
        }
        self.env.pop("GIT_CONFIG_PARAMETERS", None)
        remote = self.tmp / "srv" / "agent.git"
        self.git("init", "--quiet", "--bare", "-b", "main", str(remote))
        for k, v in (("uploadpack.allowFilter", "true"), ("uploadpack.allowAnySHA1InWant", "true"),
                     ("http.receivepack", "true")):
            self.git("config", k, v, cwd=remote)
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(str(self.tmp / "srv"), http_backend()))
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.url = f"http://127.0.0.1:{self.server.server_port}/agent.git"
        self.hdr = f"http.http://127.0.0.1:{self.server.server_port}/.extraheader=AUTHORIZATION: {EXPECTED}"

        seed = self.tmp / "seed"
        self.git("init", "--quiet", "-b", BRANCH, str(seed))
        self.write(seed, "lms/team/voice_refs/voice_a_ref.wav", b"ref")
        self.write(seed, "outside/big.bin", b"x" * 1000)
        self.write(seed, f"{TDIR}/README", b"tutor")
        self.write(seed, f"{ADIR}/README.md", b"r3 audio")
        self.git("add", "-A", cwd=seed)
        self.git("commit", "--quiet", "-m", "seed", cwd=seed)
        self.git("-c", self.hdr, "push", "--quiet", self.url, f"HEAD:refs/heads/{BRANCH}", cwd=seed)

    def tearDown(self):
        self.server.shutdown()
        shutil.rmtree(self.tmp, ignore_errors=True)

    def git(self, *args, cwd=None, check=True):
        return subprocess.run(["git", *args], cwd=cwd, env=self.env, capture_output=True, text=True, check=check)

    @staticmethod
    def write(repo: Path, rel: str, data: bytes):
        p = repo / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)

    def checkout(self, name: str) -> Path:
        """Like actions/checkout with sparse-checkout, fetch-depth 1, persist-credentials false."""
        d = self.tmp / name
        self.git("init", "--quiet", str(d))
        self.git("remote", "add", "origin", self.url, cwd=d)
        self.git("config", "remote.origin.promisor", "true", cwd=d)
        self.git("config", "remote.origin.partialclonefilter", "blob:none", cwd=d)
        self.git("sparse-checkout", "set", TDIR, ADIR, "lms/team/voice_refs", cwd=d)
        self.git("-c", self.hdr, "fetch", "--quiet", "--filter=blob:none", "--depth=1", "origin",
                 f"+refs/heads/{BRANCH}:refs/remotes/origin/{BRANCH}", cwd=d)
        self.git("-c", self.hdr, "checkout", "--quiet", "-B", BRANCH, f"refs/remotes/origin/{BRANCH}", cwd=d)
        return d

    def push(self, repo: Path, category: str, target: str = "tutor_001", voice: str = "voice_a", branch: str = BRANCH):
        return subprocess.run(["bash", str(SCRIPT), str(repo), branch, target, voice, category],
                              env={**self.env, "AGENT_PAT": TOKEN}, capture_output=True, text=True)

    def remote_files(self):
        return self.git("ls-tree", "-r", "--name-only", BRANCH, cwd=self.tmp / "srv" / "agent.git").stdout.split()

    def test_r3_shards_then_merge(self):
        a, b = self.checkout("shard1"), self.checkout("shard2")
        key1 = "english_home_language.gradeR.term1.w01_sound_a.show"
        self.write(a, f"{ADIR}/{key1}.mp3", b"mp3-1")
        self.write(a, f"{ADIR}/r3_manifest.voice_x.part01.json", b'{"lines": []}\n')
        # Never staged: a subfolder, another extension, another voice's manifest, outside the folder.
        self.write(a, f"{ADIR}/sub/{key1}.mp3", b"nested")
        self.write(a, f"{ADIR}/notes.txt", b"no")
        self.write(a, f"{ADIR}/r3_manifest.voice_y.json", b"{}")
        self.write(a, f"{TDIR}/greetings/01.wav", b"tutor-audio")
        self.write(a, "lms/team/voice_refs/voice_a_ref.wav", b"changed-ref")
        self.write(b, f"{ADIR}/r3.r3_praise_yes.mp3", b"mp3-2")
        self.write(b, f"{ADIR}/r3_manifest.voice_x.part02.json", b'{"lines": []}\n')

        first = self.push(a, "r3 shard 1/2", "r3", "voice_x")
        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        second = self.push(b, "r3 shard 2/2", "r3", "voice_x")
        self.assertEqual(second.returncode, 0, second.stdout + second.stderr)
        self.assertIn("push rejected (attempt 1)", second.stdout)
        files = self.remote_files()
        for f in (f"{ADIR}/{key1}.mp3", f"{ADIR}/r3.r3_praise_yes.mp3",
                  f"{ADIR}/r3_manifest.voice_x.part01.json", f"{ADIR}/r3_manifest.voice_x.part02.json"):
            self.assertIn(f, files)
        for f in (f"{ADIR}/sub/{key1}.mp3", f"{ADIR}/notes.txt", f"{ADIR}/r3_manifest.voice_y.json",
                  f"{TDIR}/greetings/01.wav"):
            self.assertNotIn(f, files)
        self.assertEqual(self.git("show", f"{BRANCH}:lms/team/voice_refs/voice_a_ref.wav",
                                  cwd=self.tmp / "srv" / "agent.git").stdout, "ref")

        # The merge job: fold the parts into one manifest and remove them.
        m = self.checkout("merge")
        for n in ("01", "02"):
            (m / ADIR / f"r3_manifest.voice_x.part{n}.json").unlink()
        self.write(m, f"{ADIR}/r3_manifest.voice_x.json", b'{"lines": [1, 2]}\n')
        merged = self.push(m, "manifest", "r3", "voice_x")
        self.assertEqual(merged.returncode, 0, merged.stdout + merged.stderr)
        files = self.remote_files()
        self.assertIn(f"{ADIR}/r3_manifest.voice_x.json", files)
        self.assertNotIn(f"{ADIR}/r3_manifest.voice_x.part01.json", files)
        self.assertIn(f"{ADIR}/README.md", files)
        again = self.push(m, "manifest", "r3", "voice_x")
        self.assertIn("nothing new to commit", again.stdout)

    def test_r3_refuses_unexpected_and_bad_args(self):
        a = self.checkout("bad")
        self.write(a, f"{ADIR}/k.mp3", b"ok")
        self.write(a, f"{TDIR}/sneaky.txt", b"x")
        self.git("add", f"{TDIR}/sneaky.txt", cwd=a)
        r = self.push(a, "r3 shard 1/1", "r3", "voice_x")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("unexpected staged path", r.stdout)
        self.assertNotEqual(self.push(a, "x", "r3", "voice_x", branch="main").returncode, 0)
        self.assertNotEqual(self.push(a, "x", "r3", "voice_x", branch="claude/x").returncode, 0)
        self.assertNotEqual(self.push(a, "x", "../r3", "voice_x").returncode, 0)
        self.assertNotEqual(self.push(a, "x", "r3", "Voice X").returncode, 0)

    def test_rejected_push_rebases_with_auth(self):
        a, b = self.checkout("teaching"), self.checkout("greetings")
        self.write(a, f"{TDIR}/samples/sample_line.wav", b"teaching-audio")
        self.write(a, f"{TDIR}/voice_a_manifest.teaching.json", b'{"lines": []}\n')
        self.write(b, f"{TDIR}/greetings/01.wav", b"greetings-audio")
        self.write(b, f"{TDIR}/voice_a_manifest.greetings.json", b'{"lines": []}\n')

        first = self.push(a, "teaching")
        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        second = self.push(b, "greetings")
        self.assertEqual(second.returncode, 0, second.stdout + second.stderr)
        self.assertIn("push rejected (attempt 1)", second.stdout)
        self.assertIn("pushed", second.stdout)

        files = self.git("ls-tree", "-r", "--name-only", BRANCH, cwd=self.tmp / "srv" / "agent.git").stdout.split()
        for f in (f"{TDIR}/samples/sample_line.wav", f"{TDIR}/greetings/01.wav",
                  f"{TDIR}/voice_a_manifest.teaching.json", f"{TDIR}/voice_a_manifest.greetings.json",
                  "outside/big.bin"):
            self.assertIn(f, files)
        # The token never lands in the checkout's config.
        self.assertNotIn(TOKEN, (b / ".git" / "config").read_text())
        self.assertNotIn(EXPECTED.split()[1], (b / ".git" / "config").read_text())


if __name__ == "__main__":
    unittest.main()
