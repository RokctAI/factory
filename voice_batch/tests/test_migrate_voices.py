"""ci/migrate_voices_to_lessons.py on temp checkouts. Model-free.

    python -m pytest voice_batch/tests/test_migrate_voices.py
"""
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE / "ci"))
sys.path.insert(0, str(HERE))
import migrate_voices_to_lessons as mig  # noqa: E402

SCRIPT = HERE / "ci" / "migrate_voices_to_lessons.py"
T = "lms/team/tutors/CAPS/tutor_001"
A = "lms/team/assistants/CAPS/assistant_005"
R3 = "lms/dart/templates/assets/r3_packs/audio"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


class Migrate(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = Path(self.tmp.name)
        self.agent, self.lessons = d / "agent", d / "lessons"
        self.lessons.mkdir()
        (self.lessons / "school").mkdir()
        manifest = {"voice": "voice_a", "reference": {"path": "lms/team/voice_refs/voice_a_ref.wav", "sha256": "ab"},
                    "lines": [{"id": "tutor_001/greetings/01", "file": f"{T}/greetings/01.m4a",
                               "script": f"{T}/greetings/01.md", "text": "Hello, café."}],
                    "failed": [{"id": "tutor_001/greetings/02", "file_not_committed": f"{T}/greetings/02.m4a"}]}
        r3 = {"kind": "r3", "settings": {"output": {"dir": R3}},
              "lines": [{"id": "k.show", "file": f"{R3}/k.show.mp3", "script": "school/curriculum/CAPS/m/p.json"}]}
        files = {
            "lms/team/voice_refs/voice_a_ref.wav": b"RIFFref",
            f"{R3}/k.show.mp3": b"ID3mp3",
            f"{R3}/k.show.timings.json": b'{"words": []}\n',
            f"{R3}/r3_manifest.voice_a.json": (json.dumps(r3, indent=1) + "\n").encode(),
            f"{R3}/qc_failed.voice_a.json": b'{"failed": []}\n',
            f"{T}/greetings/01.m4a": b"m4a-1",
            f"{T}/greetings/01.timings.json": b'{"w": 1}\n',
            f"{T}/greetings/qc_failed.json": b'{"failed": []}\n',
            f"{T}/voice_a_manifest.json": (json.dumps(manifest, indent=1, ensure_ascii=False) + "\n").encode(),
            f"{T}/voice_a_manifest.greetings.json": b'{"lines": []}',
            f"{A}/intro/new.m4a": b"m4a-a",
            "lms/team/voices/samples/tutor_008.wav": b"RIFFsample",
            "lms/team/voices/samples/pronunciation/voice_a/audition.json":
                json.dumps({"clips": {"x": {"file": "lms/team/voices/samples/pronunciation/voice_a/x.mp3"}}}).encode(),
            "lms/team/voices/samples/pronunciation/voice_a/x.mp3": b"ID3x",
            # stay in agent
            f"{T}/greetings/01.md": b"Hello.\n",
            f"{T}/samples.json": b"{}",
            f"{T}/tutor.md": b"display_name: X\n",
            f"{T}/appearance/still.png": b"PNG",
            "lms/team/tutors/CAPS/roster.json": b"{}",
            "lms/team/voices/tutor_001.voice.json": b"{}",
            "lms/team/scripts/render_voices.py": b"#",
        }
        for rel, data in files.items():
            p = self.agent / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(data)
        self.files = files
        self.before = {rel: sha(self.agent / rel) for rel in files}

    def tearDown(self):
        self.tmp.cleanup()

    def agent_untouched(self):
        now = {p.relative_to(self.agent).as_posix(): sha(p) for p in self.agent.rglob("*") if p.is_file()}
        self.assertEqual(now, self.before)

    def test_check_writes_nothing(self):
        rep = mig.migrate(self.agent, self.lessons, check=True)
        self.assertEqual(rep["copied"], 14)
        self.assertEqual({k: v["files"] for k, v in rep["areas"].items()}, {"refs": 1, "r3": 4, "team": 6, "samples": 3})
        self.assertEqual([p.name for p in self.lessons.iterdir()], ["school"])
        self.agent_untouched()

    def test_copy_verify_rewrite(self):
        rep = mig.migrate(self.agent, self.lessons)
        self.assertEqual((rep["copied"], rep["same"], rep["conflicts"], rep["failed"]), (14, 0, [], []))
        L = self.lessons
        # bytes preserved for everything that is not a rewritten JSON
        for old, new in (("lms/team/voice_refs/voice_a_ref.wav", "voices/refs/voice_a_ref.wav"),
                         (f"{R3}/k.show.mp3", "voices/r3/k.show.mp3"),
                         (f"{R3}/k.show.timings.json", "voices/r3/k.show.timings.json"),
                         (f"{T}/greetings/01.m4a", "voices/team/tutors/CAPS/tutor_001/greetings/01.m4a"),
                         (f"{T}/greetings/qc_failed.json", "voices/team/tutors/CAPS/tutor_001/greetings/qc_failed.json"),
                         (f"{T}/voice_a_manifest.greetings.json",
                          "voices/team/tutors/CAPS/tutor_001/voice_a_manifest.greetings.json"),
                         (f"{A}/intro/new.m4a", "voices/team/assistants/CAPS/assistant_005/intro/new.m4a"),
                         ("lms/team/voices/samples/tutor_008.wav", "voices/samples/tutor_008.wav")):
            self.assertEqual((L / new).read_bytes(), self.files[old], new)
        # nothing that stays in agent was copied
        copied = {p.relative_to(L).as_posix() for p in L.rglob("*") if p.is_file()}
        self.assertEqual(len(copied), 14)
        self.assertFalse(any(p.endswith((".md", ".png", "roster.json", ".voice.json", ".py", "samples.json"))
                             for p in copied))
        # paths inside JSON manifests point at the new layout; scripts stay agent paths
        m = json.loads((L / "voices/team/tutors/CAPS/tutor_001/voice_a_manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(m["reference"]["path"], "voices/refs/voice_a_ref.wav")
        self.assertEqual(m["lines"][0]["file"], "voices/team/tutors/CAPS/tutor_001/greetings/01.m4a")
        self.assertEqual(m["lines"][0]["script"], f"{T}/greetings/01.md")
        self.assertEqual(m["lines"][0]["text"], "Hello, café.")
        self.assertEqual(m["failed"][0]["file_not_committed"], "voices/team/tutors/CAPS/tutor_001/greetings/02.m4a")
        self.assertIn('\n "voice": "voice_a"', (L / "voices/team/tutors/CAPS/tutor_001/voice_a_manifest.json")
                      .read_text(encoding="utf-8"))     # indent kept
        r3 = json.loads((L / "voices/r3/r3_manifest.voice_a.json").read_text())
        self.assertEqual((r3["settings"]["output"]["dir"], r3["lines"][0]["file"], r3["lines"][0]["script"]),
                         ("voices/r3", "voices/r3/k.show.mp3", "school/curriculum/CAPS/m/p.json"))
        au = json.loads((L / "voices/samples/pronunciation/voice_a/audition.json").read_text())
        self.assertEqual(au["clips"]["x"]["file"], "voices/samples/pronunciation/voice_a/x.mp3")
        self.assertEqual((rep["rewritten_json"], rep["rewritten_paths"]), (3, 6))
        self.agent_untouched()

        # Idempotent: a second run copies nothing; --check agrees.
        again = mig.migrate(self.agent, self.lessons)
        self.assertEqual((again["copied"], again["same"]), (0, 14))
        self.assertEqual(mig.migrate(self.agent, self.lessons, check=True)["copied"], 0)

    def test_conflict_is_not_overwritten(self):
        dst = self.lessons / "voices/r3/k.show.mp3"
        dst.parent.mkdir(parents=True)
        dst.write_bytes(b"other")
        rep = mig.migrate(self.agent, self.lessons)
        self.assertEqual(rep["conflicts"], ["voices/r3/k.show.mp3"])
        self.assertEqual(dst.read_bytes(), b"other")
        rep = mig.migrate(self.agent, self.lessons, overwrite=True)
        self.assertEqual(rep["conflicts"], [])
        self.assertEqual(dst.read_bytes(), b"ID3mp3")

    def test_cli_summary_and_exit(self):
        r = subprocess.run([sys.executable, str(SCRIPT), "--agent", str(self.agent), "--lessons", str(self.lessons),
                            "--check"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("check only", r.stdout)
        self.assertIn("would copy: 14", r.stdout)
        self.assertIn("MB", r.stdout)
        self.assertNotIn("café", r.stdout)       # never file contents
        self.assertFalse((self.lessons / "voices").exists())
        r = subprocess.run([sys.executable, str(SCRIPT), "--agent", str(self.agent), "--lessons", str(self.agent)],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 2)
        dst = self.lessons / "voices/refs/voice_a_ref.wav"
        dst.parent.mkdir(parents=True)
        dst.write_bytes(b"x")
        r = subprocess.run([sys.executable, str(SCRIPT), "--agent", str(self.agent), "--lessons", str(self.lessons)],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 1)
        self.assertIn("conflict", r.stdout)
        self.agent_untouched()


if __name__ == "__main__":
    unittest.main()
