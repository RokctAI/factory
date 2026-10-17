"""voice_paths.py: the one switch for where voice audio lives. Model-free.

    python -m pytest voice_batch/tests/test_voice_paths.py
"""
import importlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import voice_paths as vp  # noqa: E402


class Layout(unittest.TestCase):
    def test_defaults_are_lessons_voices(self):
        self.assertEqual(vp.VOICE_REPO, "RokctAI/lessons")
        self.assertEqual(vp.VOICE_ROOT, "voices")
        self.assertEqual(vp.refs_dir(), "voices/refs")
        self.assertEqual(vp.r3_dir(), "voices/r3")
        self.assertEqual(vp.samples_dir(), "voices/samples")
        self.assertEqual(vp.team_dir("tutor_001"), "voices/team/tutors/CAPS/tutor_001")
        self.assertEqual(vp.team_dir("assistant_005"), "voices/team/assistants/CAPS/assistant_005")
        self.assertEqual(vp.target_dir("pronunciation", "voice_a"), "voices/samples/pronunciation/voice_a")
        for bad in ("../x", "tutor_1", "r3x"):
            with self.assertRaises(ValueError):
                vp.team_dir(bad)
        with self.assertRaises(ValueError):
            vp.target_dir("pronunciation", "../x")

    def test_empty_root_is_the_agent_layout(self):
        self.assertEqual(vp.refs_dir(""), "lms/team/voice_refs")
        self.assertEqual(vp.r3_dir(""), "lms/dart/templates/assets/r3_packs/audio")
        self.assertEqual(vp.samples_dir(""), "lms/team/voices/samples")
        self.assertEqual(vp.team_dir("tutor_001", ""), "lms/team/tutors/CAPS/tutor_001")
        p = "lms/team/tutors/CAPS/tutor_001/greetings/01.m4a"
        self.assertEqual(vp.map_agent_path(p, ""), p)

    def test_env_switch(self):
        """VOICE_REPO / VOICE_ROOT flip every path; "." means the agent layout."""
        try:
            with mock.patch.dict(os.environ, {"VOICE_REPO": "RokctAI/agent", "VOICE_ROOT": "."}):
                m = importlib.reload(vp)
                self.assertEqual((m.VOICE_REPO, m.VOICE_ROOT), ("RokctAI/agent", ""))
                self.assertEqual(m.r3_dir(), "lms/dart/templates/assets/r3_packs/audio")
                self.assertEqual(m.ref_path_re(), r"lms/team/voice_refs/[A-Za-z0-9_]+\.wav")
            with mock.patch.dict(os.environ, {"VOICE_ROOT": "audio/"}):
                m = importlib.reload(vp)
                self.assertEqual(m.r3_dir(), "audio/r3")
        finally:
            importlib.reload(vp)

    def test_ref_path_re(self):
        import re
        self.assertRegex("voices/refs/voice_a_ref.wav", "^" + vp.ref_path_re() + "$")
        for bad in ("lms/team/voice_refs/voice_a_ref.wav", "voices/refs/../x.wav", "voicesXrefs/a.wav"):
            self.assertIsNone(re.fullmatch(vp.ref_path_re(), bad), bad)


class Mapper(unittest.TestCase):
    CASES = {
        "lms/team/voice_refs/voice_a_ref.wav": "voices/refs/voice_a_ref.wav",
        "lms/dart/templates/assets/r3_packs/audio/maths.gradeR.term1.w01.show.mp3":
            "voices/r3/maths.gradeR.term1.w01.show.mp3",
        "lms/dart/templates/assets/r3_packs/audio/x.show.timings.json": "voices/r3/x.show.timings.json",
        "lms/dart/templates/assets/r3_packs/audio/r3_manifest.voice_a.part03.json":
            "voices/r3/r3_manifest.voice_a.part03.json",
        "lms/dart/templates/assets/r3_packs/audio/qc_failed.voice_a.json": "voices/r3/qc_failed.voice_a.json",
        "lms/dart/templates/assets/r3_packs/audio/r3.r3_praise_yes.af.m4a": "voices/r3/r3.r3_praise_yes.af.m4a",
        "lms/dart/templates/assets/r3_packs/audio": "voices/r3",
        "lms/team/tutors/CAPS/tutor_001/greetings/02.m4a": "voices/team/tutors/CAPS/tutor_001/greetings/02.m4a",
        "lms/team/tutors/CAPS/tutor_001/greetings/02.timings.json":
            "voices/team/tutors/CAPS/tutor_001/greetings/02.timings.json",
        "lms/team/tutors/CAPS/tutor_001/samples/sample_line.wav":
            "voices/team/tutors/CAPS/tutor_001/samples/sample_line.wav",
        "lms/team/tutors/CAPS/tutor_001/voice_a_manifest.json": "voices/team/tutors/CAPS/tutor_001/voice_a_manifest.json",
        "lms/team/tutors/CAPS/tutor_001/voice_a_manifest.greetings.json":
            "voices/team/tutors/CAPS/tutor_001/voice_a_manifest.greetings.json",
        "lms/team/tutors/CAPS/tutor_001/greetings/qc_failed.json":
            "voices/team/tutors/CAPS/tutor_001/greetings/qc_failed.json",
        "lms/team/assistants/CAPS/assistant_005/intro/new@tutor_001+tutor_002.m4a":
            "voices/team/assistants/CAPS/assistant_005/intro/new@tutor_001+tutor_002.m4a",
        "lms/team/voices/samples/tutor_008.wav": "voices/samples/tutor_008.wav",
        "lms/team/voices/samples/pronunciation/voice_a/mahikeng--mah-hee-keng.mp3":
            "voices/samples/pronunciation/voice_a/mahikeng--mah-hee-keng.mp3",
        "lms/team/voices/samples/pronunciation/voice_a/audition.json":
            "voices/samples/pronunciation/voice_a/audition.json",
        "/lms/team/voice_refs/v.wav": "voices/refs/v.wav",
    }
    STAY = (
        "lms/team/tutors/CAPS/tutor_001/greetings/02.md",
        "lms/team/tutors/CAPS/tutor_001/samples.json",
        "lms/team/tutors/CAPS/tutor_001/tutor.md",
        "lms/team/tutors/CAPS/tutor_001/appearance/still.json",
        "lms/team/tutors/CAPS/tutor_001/appearance/still.png",
        "lms/team/tutors/CAPS/roster.json",
        "lms/team/assistants/CAPS/roster.json",
        "lms/team/voices/tutor_001.voice.json",
        "lms/team/scripts/render_voices.py",
        "lms/dart/lib/src/translations/lms_en_translations.dart",
        "lms/dart/templates/assets/r3_packs/audio_extra/x.mp3",
        "lms/team/voice_refs_old/x.wav",
        "school/curriculum/CAPS/maths/r3_packs/gradeR/term1/w01.json",
        "voices/refs/voice_a_ref.wav",
    )

    def test_mapped(self):
        for old, new in self.CASES.items():
            self.assertEqual(vp.map_agent_path(old), new, old)
            self.assertEqual(vp.voice_path(old), new, old)

    def test_stays_in_agent(self):
        for p in self.STAY:
            self.assertIsNone(vp.map_agent_path(p), p)
        with self.assertRaises(ValueError):
            vp.voice_path("lms/team/tutors/CAPS/tutor_001/tutor.md")

    def test_line_files_land_in_the_voice_repo(self):
        """lines.py and r3_lines.py name their audio at voice-repo paths."""
        import lines
        with tempfile.TemporaryDirectory() as d:
            t = Path(d, "lms/team/tutors/CAPS/tutor_009/greetings")
            t.mkdir(parents=True)
            (t / "01.md").write_text("Hello there.\n")
            (it,) = lines.build_lines(d, "tutor_009", ["greetings"], {})
            self.assertEqual(it["file"], "voices/team/tutors/CAPS/tutor_009/greetings/01.m4a")
            self.assertEqual(it["script"], "lms/team/tutors/CAPS/tutor_009/greetings/01.md")

    def test_manifest_patterns(self):
        self.assertEqual(vp.manifest_patterns(), [
            "/voices/team/tutors/CAPS/*/*manifest*.json",
            "/voices/team/assistants/CAPS/*/*manifest*.json",
            "/voices/r3/*manifest*.json"])


class Cli(unittest.TestCase):
    def run_cli(self, *args, env=None):
        return subprocess.run([sys.executable, str(HERE / "voice_paths.py"), *args], capture_output=True, text=True,
                              env={**os.environ, **(env or {})})

    def test_cli(self):
        env = {"VOICE_REPO": "", "VOICE_ROOT": "voices"}
        self.assertEqual(self.run_cli("repo", env=env).stdout.strip(), "RokctAI/lessons")
        self.assertEqual(self.run_cli("dir", "r3", env=env).stdout.strip(), "voices/r3")
        self.assertEqual(self.run_cli("dir", "tutor_001", env=env).stdout.strip(), "voices/team/tutors/CAPS/tutor_001")
        self.assertEqual(self.run_cli("dir", "pronunciation", "voice_b", env=env).stdout.strip(),
                         "voices/samples/pronunciation/voice_b")
        self.assertEqual(self.run_cli("refs", env=env).stdout.strip(), "voices/refs")
        self.assertEqual(self.run_cli("samples", env=env).stdout.strip(), "voices/samples")
        self.assertEqual(len(self.run_cli("manifests", env=env).stdout.split()), 3)
        r = self.run_cli("map", "lms/team/tutors/CAPS/tutor_001/tutor.md", env=env)
        self.assertEqual((r.returncode, r.stdout), (1, ""))
        self.assertEqual(self.run_cli("dir", "../x", env=env).returncode, 1)
        self.assertEqual(self.run_cli("nope", env=env).returncode, 2)
        legacy = {"VOICE_REPO": "RokctAI/agent", "VOICE_ROOT": "."}
        self.assertEqual(self.run_cli("dir", "r3", env=legacy).stdout.strip(), "lms/dart/templates/assets/r3_packs/audio")
        self.assertEqual(self.run_cli("repo", env=legacy).stdout.strip(), "RokctAI/agent")


class Inputs(unittest.TestCase):
    """Every committed batch and lesson voice pins its reference in the voice repo."""

    def test_batches_and_lesson_voices(self):
        import re
        root = HERE.parent
        files = sorted((root / "voice_batches").glob("*/*.json"))
        self.assertTrue(files)
        for p in files:
            b = json.loads(p.read_text(encoding="utf-8"))
            self.assertRegex(b["ref_path"], "^" + vp.ref_path_re() + "$", p.name)
        for v in json.loads((HERE / "lesson_voices.json").read_text(encoding="utf-8"))["voices"].values():
            self.assertIsNotNone(re.fullmatch(vp.ref_path_re(), v["ref_path"]))


if __name__ == "__main__":
    unittest.main()
