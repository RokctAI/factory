"""reel_voice.py without a model: sentence joining, batch checks, and the
seed rounds with a stand-in renderer and meter.

    python -m unittest discover -s radio_ads/tests -v

The round test needs numpy, soundfile and librosa (voice_batch's QC
stitch) and the agent repo's render_voices.py beside this checkout
(../agent/lms/team/scripts); it is skipped without them.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))

import reel_voice as rvx  # noqa: E402

SCRIPTS = HERE.parent.parent / "agent" / "lms" / "team" / "scripts"


def batch(**over):
    b = {"id": "reel", "voices": {"voice_a": {"f0_target_hz": 102, "f0_tolerance_hz": 8}},
         "lines": [{"id": "brand", "voice": "voice_a", "text": "This is Rocket.", "takes": 3}]}
    b.update(over)
    return b


class Parts(unittest.TestCase):
    def test_one_sentence(self):
        self.assertEqual(rvx.render_parts("This is Rocket."), ["This is Rocket."])

    def test_short_sentence_joins_next(self):
        self.assertEqual(rvx.render_parts("Begin. Now we start the lesson."), ["Begin. Now we start the lesson."])

    def test_short_last_sentence_joins_previous(self):
        self.assertEqual(rvx.render_parts("We go now. Begin."), ["We go now. Begin."])

    def test_long_sentences_stay_apart(self):
        self.assertEqual(rvx.render_parts("Looking for funding? Here's one you can apply for, right now."),
                         ["Looking for funding?", "Here's one you can apply for, right now."])


class Batch(unittest.TestCase):
    def load(self, b):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "b.json"
            p.write_text(json.dumps(b))
            return rvx.load_batch(p)

    def test_committed_batch_is_valid(self):
        b = rvx.load_batch(HERE / "reel_voices" / "facebook_reel.json")
        self.assertEqual({ln["voice"] for ln in b["lines"]}, {"voice_a", "voice_b"})

    def test_unknown_voice(self):
        with self.assertRaises(ValueError):
            self.load(batch(lines=[{"id": "x", "voice": "voice_z", "text": "Hello there you."}]))

    def test_too_many_takes(self):
        with self.assertRaises(ValueError):
            self.load(batch(lines=[{"id": "x", "voice": "voice_a", "text": "Hello there you.", "takes": 6}]))


class FakeMeter:
    """Seed 22 misses a word; every other take passes."""

    def __init__(self, *a, **k):
        pass

    def measure(self, p, text, wild=None):
        bad = "seed22" in str(p)
        return {"dur": 1.2, "res": 0.9, "err": int(bad), "f0": 103.0, "swings": 0, "transcript": "",
                "tail_db": -60.0}


@unittest.skipUnless((SCRIPTS / "render_voices.py").exists(), "agent checkout not beside this repo")
class Rounds(unittest.TestCase):
    def test_rounds_until_three_takes_pass(self):
        import numpy as np
        import soundfile as sf

        real_run = subprocess.run

        def fake_run(cmd, check=False):
            if cmd[1].endswith("render_takes.py"):
                for j in json.loads(Path(cmd[cmd.index("--jobs") + 1]).read_text()):
                    Path(j["out"]).parent.mkdir(parents=True, exist_ok=True)
                    t = np.arange(24000) / 24000
                    sf.write(j["out"], 0.3 * np.sin(2 * np.pi * 110 * t) * np.hanning(t.size), 24000,
                             subtype="PCM_16")
                return subprocess.CompletedProcess(cmd, 0)
            if "--qc" in cmd:
                ns = argparse.Namespace(qc=cmd[cmd.index("--qc") + 1], qc_out=cmd[cmd.index("--qc-out") + 1],
                                        scripts_dir=str(SCRIPTS), asr_model="small.en")
                with mock.patch.object(rvx.qc, "Meter", FakeMeter):
                    rvx.gate_takes(ns)
                return subprocess.CompletedProcess(cmd, 0)
            return real_run(cmd, check=check)

        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            (d / "voices").mkdir()
            sf.write(str(d / "voices" / "voice_a.wav"), np.zeros(24000), 24000)
            (d / "b.json").write_text(json.dumps(batch()))
            argv = ["reel_voice.py", str(d / "b.json"), "--voices", str(d / "voices"), "--scripts-dir", str(SCRIPTS),
                    "--model-path", "x", "--work", str(d / "work"), "--out", str(d / "out")]
            with mock.patch.object(rvx.subprocess, "run", fake_run), mock.patch.object(sys, "argv", argv):
                self.assertEqual(rvx.main(), 0)
            rep = json.loads((d / "out" / "report.json").read_text())
            line = rep["lines"][0]
            self.assertEqual(line["chosen_seeds"], [11, 33, 44])
            self.assertEqual([t["seed"] for t in line["takes"]], [11, 22, 33, 44])
            self.assertTrue((d / "out" / "brand_seed44.mp3").exists())


if __name__ == "__main__":
    unittest.main()
