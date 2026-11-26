"""MEDIA_ENGINE switch (step 3 of the one-engine move). Model-free."""
import os
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import run as R  # noqa: E402

ARGS = SimpleNamespace(model_path="/m", ddpm_steps=0, f0_target=110.0, f0_tolerance=12.0, sim_short=0.8,
                       sim_long=0.88, language="en", pace_wpm=149.0, pace_tolerance=15.0, asr_model="small.en")


class MediaEngine(unittest.TestCase):
    def cmds(self, engine, near_miss=0):
        with mock.patch.dict(os.environ, {"MEDIA_ENGINE": engine}):
            return R.engine_commands(Path("/w"), Path("/ref.wav"), Path("/s"), ARGS, near_miss)

    def test_default_is_voice_batch(self):
        with mock.patch.dict(os.environ, {}, clear=False):
            os.environ.pop("MEDIA_ENGINE", None)
            self.assertEqual(R.media_engine(), "voice_batch")
        render, gate = self.cmds("")
        self.assertTrue(render[1].endswith("render_takes.py"))
        self.assertTrue(gate[1].endswith("qc.py"))

    def test_rokct_media_same_settings(self):
        render, gate = self.cmds("rokct-media", near_miss=1)
        self.assertEqual(render[1:3], ["-m", "rokct_media.speech.takes"])
        self.assertIn('"cfg_scale": 1.3', render[-1])
        self.assertIn('"ddpm_steps": 10', render[-1])  # approved Voice A setting
        self.assertEqual(gate[1:4], ["-m", "rokct_media.qc.worker", "sentences"])
        # Both engines get the identical gate arguments.
        old_gate = self.cmds("voice_batch", near_miss=1)[1]
        tail = lambda c: c[c.index("--f0-target"):]  # noqa: E731
        self.assertEqual(tail(gate), tail(old_gate))
        self.assertEqual(tail(gate)[-2:], ["--near-miss-words", "1"])

    def test_per_voice_steps(self):
        args = SimpleNamespace(**{**vars(ARGS), "ddpm_steps": 20})
        with mock.patch.dict(os.environ, {"MEDIA_ENGINE": "rokct-media"}):
            render = R.engine_commands(Path("/w"), Path("/r"), Path("/s"), args, 0)[0]
        self.assertIn('"ddpm_steps": 20', render[-1])

    def test_unknown_engine_refused(self):
        with mock.patch.dict(os.environ, {"MEDIA_ENGINE": "other"}):
            with self.assertRaises(SystemExit):
                R.media_engine()


if __name__ == "__main__":
    unittest.main()
