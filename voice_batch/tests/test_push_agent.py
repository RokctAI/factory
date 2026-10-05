"""push_agent.sh against a local token-protected git HTTP server.

Reproduces the CI layout: a sparse, blob-less, depth-1 checkout with no
persisted credentials, and a sibling category job that pushes first, so our
push is rejected and must rebase. The rebase lazily fetches blobs from the
promisor remote and needs the auth header too. Also the deleted-branch path:
resolve_agent_ref.sh falls back to main, the jobs start the branch from it,
the first push recreates it and the siblings that lose the race rebase onto it,
including truly concurrent pushers. And the plan job's --create path.

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
RESOLVE = ROOT / "voice_batch" / "ci" / "resolve_agent_ref.sh"
TOKEN = "test-token"
EXPECTED = "Basic " + base64.b64encode(f"x-access-token:{TOKEN}".encode()).decode()
BRANCH = "rokct/tutor-001-voice-a-test"
TDIR = "lms/team/tutors/CAPS/tutor_001"
ADIR = "lms/dart/templates/assets/r3_packs/audio"
PDIR = "lms/team/voices/samples/pronunciation"


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
        self.git("-c", self.hdr, "push", "--quiet", self.url, f"HEAD:refs/heads/{BRANCH}", "HEAD:refs/heads/main",
                 cwd=seed)
        self.seed = seed

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

    def checkout(self, name: str, ref: str = BRANCH, patterns: tuple | None = None) -> Path:
        """Like actions/checkout with sparse-checkout, fetch-depth 1, persist-credentials false.
        patterns: non-cone sparse patterns (the workflow's kind assistant) instead of cone mode."""
        d = self.tmp / name
        self.git("init", "--quiet", str(d))
        self.git("remote", "add", "origin", self.url, cwd=d)
        self.git("config", "remote.origin.promisor", "true", cwd=d)
        self.git("config", "remote.origin.partialclonefilter", "blob:none", cwd=d)
        if patterns:
            self.git("sparse-checkout", "set", "--no-cone", *patterns, cwd=d)
        else:
            self.git("sparse-checkout", "set", TDIR, ADIR, PDIR, "lms/team/voice_refs", cwd=d)
        self.git("-c", self.hdr, "fetch", "--quiet", "--filter=blob:none", "--depth=1", "origin",
                 f"+refs/heads/{ref}:refs/remotes/origin/{ref}", cwd=d)
        self.git("-c", self.hdr, "checkout", "--quiet", "-B", ref, f"refs/remotes/origin/{ref}", cwd=d)
        return d

    def resolve(self, branch: str = BRANCH, cwd=None, create: bool = False):
        r = subprocess.run(["bash", str(RESOLVE), *(["--create"] if create else []), branch, self.url], cwd=cwd,
                           env={**{k: v for k, v in self.env.items() if k != "GITHUB_OUTPUT"}, "AGENT_PAT": TOKEN},
                           capture_output=True, text=True)
        out = dict(line.split("=", 1) for line in r.stdout.splitlines() if "=" in line and "::" not in line)
        return r, out

    def delete_remote_branch(self):
        self.git("update-ref", "-d", f"refs/heads/{BRANCH}", cwd=self.tmp / "srv" / "agent.git")

    def start_from_main(self, name: str) -> Path:
        """The workflow's deleted-branch path: check out main, then create the branch locally."""
        d = self.checkout(name, "main")
        self.git("checkout", "--quiet", "-b", BRANCH, cwd=d)
        return d

    def push(self, repo: Path, category: str, target: str = "tutor_001", voice: str = "voice_a", branch: str = BRANCH):
        return subprocess.run(["bash", str(SCRIPT), str(repo), branch, target, voice, category],
                              env={**self.env, "AGENT_PAT": TOKEN}, capture_output=True, text=True)

    def push_concurrently(self, jobs):
        """Start every (repo, category) push at once, as parallel matrix jobs do."""
        procs = [(cat, subprocess.Popen(["bash", str(SCRIPT), str(d), BRANCH, "tutor_001", "voice_a", cat],
                                        env={**self.env, "AGENT_PAT": TOKEN}, stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE, text=True)) for d, cat in jobs]
        outs = [(cat, *p.communicate()) for cat, p in procs]
        return [(cat, p.returncode, out, err) for (cat, out, err), (_, p) in zip(outs, procs)]

    def remote_sha(self, ref: str) -> str:
        return self.git("rev-parse", ref, cwd=self.tmp / "srv" / "agent.git").stdout.strip()

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

    def test_pronunciation_audition_two_voices_missing_branch(self):
        """Both voice jobs start the deleted branch from main; the second
        push rebases onto the first. Only <voice>/<slug>.mp3 + audition.json."""
        self.delete_remote_branch()
        a, b = self.start_from_main("va"), self.start_from_main("vb")
        self.write(a, f"{PDIR}/voice_a/mahikeng--mah-hee-keng.mp3", b"a1")
        self.write(a, f"{PDIR}/voice_a/audition.json", b"{}\n")
        self.write(a, f"{PDIR}/voice_a/Bad Name.mp3", b"no")
        self.write(a, f"{PDIR}/voice_a/sub/x.mp3", b"no")
        self.write(a, f"{PDIR}/voice_b/x.mp3", b"no")
        self.write(a, f"{TDIR}/greetings/01.wav", b"no")
        self.write(b, f"{PDIR}/voice_b/mahikeng--mah-hee-keng.mp3", b"b1")
        self.write(b, f"{PDIR}/voice_b/audition.json", b"{}\n")
        first = self.push(a, "audition", "pronunciation", "voice_a")
        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        second = self.push(b, "audition", "pronunciation", "voice_b")
        self.assertEqual(second.returncode, 0, second.stdout + second.stderr)
        files = self.remote_files()
        for f in (f"{PDIR}/voice_a/mahikeng--mah-hee-keng.mp3", f"{PDIR}/voice_a/audition.json",
                  f"{PDIR}/voice_b/mahikeng--mah-hee-keng.mp3", f"{PDIR}/voice_b/audition.json"):
            self.assertIn(f, files)
        for f in (f"{PDIR}/voice_a/Bad Name.mp3", f"{PDIR}/voice_a/sub/x.mp3", f"{PDIR}/voice_b/x.mp3",
                  f"{TDIR}/greetings/01.wav"):
            self.assertNotIn(f, files)

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

    def test_tutor_clip_timings_are_committed(self):
        """<clip>.timings.json next to a committed clip goes to the agent
        branch with it; a stray timings file or any other extra does not."""
        a = self.checkout("timings")
        self.write(a, f"{TDIR}/greetings/01.wav", b"greetings-audio")
        self.write(a, f"{TDIR}/greetings/01.timings.json", b'{"wpm": 120}\n')
        self.write(a, f"{TDIR}/voice_a_manifest.greetings.json", b'{"lines": []}\n')
        self.write(a, f"{TDIR}/greetings/orphan.timings.json", b"{}\n")
        self.write(a, f"{TDIR}/greetings/notes.txt", b"no")
        self.write(a, f"{TDIR}/greetings/01.results.json", b"{}\n")
        r = self.push(a, "greetings")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn(f"{TDIR}/greetings/01.timings.json", r.stdout)
        files = self.remote_files()
        for f in (f"{TDIR}/greetings/01.wav", f"{TDIR}/greetings/01.timings.json",
                  f"{TDIR}/voice_a_manifest.greetings.json"):
            self.assertIn(f, files)
        for f in (f"{TDIR}/greetings/orphan.timings.json", f"{TDIR}/greetings/notes.txt",
                  f"{TDIR}/greetings/01.results.json"):
            self.assertNotIn(f, files)
        self.assertEqual(self.git("show", f"{BRANCH}:{TDIR}/greetings/01.timings.json",
                                  cwd=self.tmp / "srv" / "agent.git").stdout, '{"wpm": 120}\n')
        # A re-render that changes only the timings still commits them.
        b = self.checkout("timings2")
        self.write(b, f"{TDIR}/greetings/01.timings.json", b'{"wpm": 118}\n')
        r = self.push(b, "greetings")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(self.git("show", f"{BRANCH}:{TDIR}/greetings/01.timings.json",
                                  cwd=self.tmp / "srv" / "agent.git").stdout, '{"wpm": 118}\n')
        self.assertIn("nothing new to commit", self.push(b, "greetings").stdout)

    def test_resolve_existing_and_missing_branch(self):
        r, out = self.resolve()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        # setUp seeded the branch and main with the same commit.
        self.assertEqual(out, {"ref": BRANCH, "create": "false", "empty": "true"})
        self.delete_remote_branch()
        r, out = self.resolve()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(out, {"ref": "main", "create": "true", "empty": "false"})
        # The token only ever appears masked, never in the clear.
        self.assertNotIn(TOKEN, r.stdout + r.stderr)
        for bad in ("main", "claude/x"):
            r, _ = self.resolve(bad)
            self.assertNotEqual(r.returncode, 0)
            self.assertIn("non-rokct/", r.stdout)
        # A bad token is an error, not a silent fallback to main.
        r = subprocess.run(["bash", str(RESOLVE), BRANCH, self.url], env={**self.env, "AGENT_PAT": "wrong"},
                           capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0)
        self.assertNotIn("ref=", r.stdout)

    def test_resolve_inside_checkout_with_persisted_credentials(self):
        """CI runs the script in the factory checkout, where actions/checkout
        (persist-credentials true) left its own token as an extraheader for the
        same host. That header must not be sent alongside (ahead of) ours."""
        ws = self.tmp / "factory"
        self.git("init", "--quiet", str(ws))
        port = self.server.server_port
        stale = base64.b64encode(b"x-access-token:factory-github-token").decode()
        self.git("config", "--local", f"http.http://127.0.0.1:{port}/.extraheader",
                 f"AUTHORIZATION: basic {stale}", cwd=ws)
        r, out = self.resolve(cwd=ws)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(out, {"ref": BRANCH, "create": "false", "empty": "true"})
        self.delete_remote_branch()
        r, out = self.resolve(cwd=ws)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(out, {"ref": "main", "create": "true", "empty": "false"})

    def test_missing_branch_is_recreated_from_main(self):
        self.delete_remote_branch()
        a = self.start_from_main("teaching")
        self.write(a, f"{TDIR}/samples/sample_line.wav", b"teaching-audio")
        self.write(a, f"{TDIR}/voice_a_manifest.teaching.json", b'{"lines": []}\n')
        r = self.push(a, "teaching")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("pushed", r.stdout)
        self.assertNotIn("rejected", r.stdout)
        files = self.remote_files()
        for f in (f"{TDIR}/samples/sample_line.wav", f"{TDIR}/voice_a_manifest.teaching.json", "outside/big.bin"):
            self.assertIn(f, files)
        main = self.git("rev-parse", "main", cwd=self.tmp / "srv" / "agent.git").stdout.strip()
        self.assertEqual(self.git("rev-parse", f"{BRANCH}~1", cwd=self.tmp / "srv" / "agent.git").stdout.strip(), main)

    def test_missing_branch_race_first_creates_rest_rebase(self):
        self.delete_remote_branch()
        a, b = self.start_from_main("teaching"), self.start_from_main("greetings")
        # main moves on before the third job checks out: its rebase must replay
        # only its own commit, not main's new one.
        self.write(self.seed, "outside/later.txt", b"later")
        self.git("add", "-A", cwd=self.seed)
        self.git("commit", "--quiet", "-m", "later on main", cwd=self.seed)
        self.git("-c", self.hdr, "push", "--quiet", self.url, "HEAD:refs/heads/main", cwd=self.seed)
        c = self.start_from_main("praise")
        for d, cat in ((a, "teaching"), (b, "greetings"), (c, "praise")):
            self.write(d, f"{TDIR}/{cat}/01.wav", f"{cat}-audio".encode())
            self.write(d, f"{TDIR}/voice_a_manifest.{cat}.json", b'{"lines": []}\n')

        first = self.push(a, "teaching")
        self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
        self.assertNotIn("rejected", first.stdout)
        for d, cat in ((b, "greetings"), (c, "praise")):
            r = self.push(d, cat)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            self.assertIn("push rejected (attempt 1)", r.stdout)
            self.assertIn("pushed", r.stdout)

        files = self.remote_files()
        for cat in ("teaching", "greetings", "praise"):
            self.assertIn(f"{TDIR}/{cat}/01.wav", files)
            self.assertIn(f"{TDIR}/voice_a_manifest.{cat}.json", files)
        self.assertNotIn("outside/later.txt", files)
        log = self.git("rev-list", "--count", f"main~1..{BRANCH}", cwd=self.tmp / "srv" / "agent.git").stdout.strip()
        self.assertEqual(log, "3")
        self.assertNotIn(TOKEN, (c / ".git" / "config").read_text())

    def test_concurrent_pushers_to_new_branch_all_land(self):
        """The run 37242154621 shape: the branch is missing, every category
        job starts it from main and they all push at the same moment."""
        self.delete_remote_branch()
        cats = ("intro", "handover", "signoff", "timekeeping")
        jobs = []
        for cat in cats:
            d = self.start_from_main(cat)
            self.write(d, f"{TDIR}/{cat}/01.wav", f"{cat}-audio".encode())
            self.write(d, f"{TDIR}/voice_a_manifest.{cat}.json", b'{"lines": []}\n')
            jobs.append((d, cat))
        for cat, rc, out, err in self.push_concurrently(jobs):
            self.assertEqual(rc, 0, f"{cat}: {out}{err}")
            self.assertIn("pushed", out)
            self.assertNotIn("::error::", out)
        files = self.remote_files()
        for cat in cats:
            self.assertIn(f"{TDIR}/{cat}/01.wav", files)
            self.assertIn(f"{TDIR}/voice_a_manifest.{cat}.json", files)
        self.assertEqual(self.git("rev-list", "--count", f"main..{BRANCH}", cwd=self.tmp / "srv" / "agent.git")
                         .stdout.strip(), str(len(cats)))

    def test_plan_creates_branch_then_concurrent_pushers_append(self):
        self.delete_remote_branch()
        r, out = self.resolve(create=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(out, {"ref": BRANCH, "create": "false", "empty": "true"})
        self.assertIn("created from main", r.stdout)
        self.assertEqual(self.remote_sha(BRANCH), self.remote_sha("main"))
        self.assertNotIn(TOKEN, r.stdout + r.stderr)
        # Idempotent: an existing branch is left alone.
        r, out = self.resolve(create=True)
        self.assertEqual(out, {"ref": BRANCH, "create": "false", "empty": "true"})
        self.assertNotIn("created", r.stdout)
        # The render jobs now check the branch out (no local -b) and push together.
        jobs = []
        for cat in ("teaching", "greetings"):
            d = self.checkout(cat)
            self.write(d, f"{TDIR}/{cat}/01.wav", f"{cat}-audio".encode())
            self.write(d, f"{TDIR}/voice_a_manifest.{cat}.json", b'{"lines": []}\n')
            jobs.append((d, cat))
        for cat, rc, out, err in self.push_concurrently(jobs):
            self.assertEqual(rc, 0, f"{cat}: {out}{err}")
        files = self.remote_files()
        for cat in ("teaching", "greetings"):
            self.assertIn(f"{TDIR}/{cat}/01.wav", files)
        self.assertEqual(self.remote_sha(f"{BRANCH}~2"), self.remote_sha("main"))
        # The merge job now sees a non-empty branch.
        r, out = self.resolve()
        self.assertEqual(out, {"ref": BRANCH, "create": "false", "empty": "false"})
        for bad in ("main", "claude/x"):
            r, _ = self.resolve(bad, create=True)
            self.assertNotEqual(r.returncode, 0)
            self.assertIn("non-rokct/", r.stdout)
        self.assertEqual(self.remote_sha("main"), self.remote_sha(f"{BRANCH}~2"))

    def test_non_cone_checkout_lazy_fetches_root_gitignore_with_auth(self):
        """The run 37273277808 shape (kind assistant): a non-cone sparse
        checkout leaves the root .gitignore and .gitattributes out of the
        worktree, so git add of a manifest reads .gitignore from the index and
        lazily fetches its blob from the promisor remote. That fetch must carry
        the auth header, or it dies with "could not read Username" / "could not
        fetch ... from promisor remote" at the first git add."""
        adir = "lms/team/assistants/CAPS/assistant_005"
        self.write(self.seed, ".gitignore", b"*.tmp\n__pycache__/\n")
        self.write(self.seed, ".gitattributes", b"* text=auto\n*.py text eol=lf\n")
        self.write(self.seed, f"{adir}/voice_b_manifest.intro.json", b'{"lines": ["intro"]}\n')
        self.git("add", "-A", cwd=self.seed)
        self.git("commit", "--quiet", "-m", "root files and an earlier manifest", cwd=self.seed)
        self.git("-c", self.hdr, "push", "--quiet", self.url, f"HEAD:refs/heads/{BRANCH}", cwd=self.seed)
        patterns = (f"/{adir}/", "/lms/team/voice_refs/")
        a = self.checkout("handover", patterns=patterns)
        self.assertFalse((a / ".gitignore").exists())
        ignore_blob = self.git("rev-parse", "HEAD:.gitignore", cwd=a).stdout.strip()
        missing = self.git("rev-list", "--objects", "--missing=print", "HEAD", cwd=a).stdout
        self.assertIn("?" + ignore_blob, missing.split())
        self.write(a, f"{adir}/handover/01.wav", b"handover-audio")
        self.write(a, f"{adir}/voice_b_manifest.handover.json", b'{"lines": []}\n')
        self.write(a, f"{adir}/voice_b_manifest.intro.json", b'{"lines": ["intro", "again"]}\n')
        r = self.push(a, "handover", "assistant_005", "voice_b")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertNotIn("promisor remote", r.stderr)
        self.assertIn("pushed", r.stdout)
        files = self.remote_files()
        for f in (f"{adir}/handover/01.wav", f"{adir}/voice_b_manifest.handover.json", ".gitignore"):
            self.assertIn(f, files)
        self.assertEqual(self.git("show", f"{BRANCH}:{adir}/voice_b_manifest.intro.json",
                                  cwd=self.tmp / "srv" / "agent.git").stdout, '{"lines": ["intro", "again"]}\n')
        # The token never lands in the checkout's config or the log.
        for secret in (TOKEN, EXPECTED.split()[1]):
            self.assertNotIn(secret, (a / ".git" / "config").read_text())
            self.assertNotIn(secret, r.stdout.replace(f"::add-mask::{EXPECTED.split()[1]}", "") + r.stderr)

    def test_unexpected_git_failure_is_annotated(self):
        """A git command that dies outside the push loop names itself in an
        ::error:: line instead of a bare exit code."""
        a = self.checkout("broken")
        self.write(a, f"{TDIR}/greetings/01.wav", b"audio")
        (a / ".git" / "index.lock").write_text("")
        r = self.push(a, "greetings")
        self.assertNotEqual(r.returncode, 0)
        self.assertRegex(r.stdout, r"::error::push_agent\.sh line \d+: .*git add.* exited 128")


if __name__ == "__main__":
    unittest.main()
