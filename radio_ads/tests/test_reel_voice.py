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


    def test_prefer_seeds_only_reorders(self):
        self.assertEqual(rvx.seed_rounds([33]), [[33], [11, 22], [44], [55]])
        self.assertEqual(rvx.seed_rounds([44]), [[44], [11, 22, 33], [55]])
        self.assertEqual(rvx.seed_rounds(), [[11, 22, 33], [44], [55]])
        b = self.load(batch(lines=[{"id": "x", "voice": "voice_a", "text": "Hello there you.", "prefer_seeds": [33]}]))
        self.assertEqual(sorted(s for r in b["lines"][0]["rounds"] for s in r), sorted(rvx.SEEDS))

    def test_prefer_seeds_must_be_seed_list_seeds(self):
        for bad in ([99], [33, 33], 33):
            with self.assertRaises(ValueError):
                self.load(batch(lines=[{"id": "x", "voice": "voice_a", "text": "Hello there you.", "prefer_seeds": bad}]))

    def test_inline_respelling_reaches_the_tts_only(self):
        b = self.load(batch(lines=[{"id": "x", "voice": "voice_a", "keep_through": "Rocket",
                                    "text": "Follow {{Rocket|Rock-it}} for more every day."}]))
        ln = b["lines"][0]
        self.assertEqual(ln["text"], "Follow Rocket for more every day.")
        self.assertEqual(ln["parts"], ["Follow Rocket for more every day."])
        self.assertEqual(ln["tts_parts"], ["Follow Rock-it for more every day."])
        self.assertEqual(ln["wild"], [["Rocket", "Rock-it"]])

    def test_malformed_markup_is_a_batch_error(self):
        with self.assertRaises(ValueError):
            self.load(batch(lines=[{"id": "x", "voice": "voice_a", "text": "Follow {{Rocket for more."}]))


class Cut(unittest.TestCase):
    def test_word_end_finds_a_respelled_word(self):
        from types import SimpleNamespace as NS
        words = [NS(word=w, end=float(i)) for i, w in enumerate(["Follow", "Rock", "it", "for", "more."])]
        self.assertEqual(rvx.word_end(words, "Follow Rocket", "for more.", [["Rocket", "Rock-it"]]), 2.0)

    def test_text_through(self):
        self.assertEqual(rvx.text_through("Hi, this is Rocket, with today's opportunity.", "Rocket"),
                         "Hi, this is Rocket,")
        self.assertIsNone(rvx.text_through("Hi there.", "Rocket"))

    def test_cut_after_waits_for_the_pause(self):
        import numpy as np
        sr = 24000
        t = np.arange(2 * sr) / sr
        tone = 0.3 * np.sin(2 * np.pi * 120 * t)
        x = np.concatenate([tone[: int(1.2 * sr)], np.zeros(int(0.3 * sr)), tone[: int(0.8 * sr)]])
        y = rvx.cut_after(x, sr, 1.0)
        self.assertAlmostEqual(len(y) / sr, 1.24, delta=0.02)
        self.assertEqual(float(y[-1]), 0.0)

    def test_cut_after_none_without_a_pause(self):
        import numpy as np
        sr = 24000
        x = 0.3 * np.sin(2 * np.pi * 120 * np.arange(2 * sr) / sr)
        self.assertIsNone(rvx.cut_after(x, sr, 0.5))

    def test_keep_through_needs_its_word(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "b.json"
            p.write_text(json.dumps(batch(lines=[{"id": "x", "voice": "voice_a", "text": "Hello there you.",
                                                  "keep_through": "Rocket"}])))
            with self.assertRaises(ValueError):
                rvx.load_batch(p)


class FakeMeter:
    """Seed 22 misses a word; every other take passes."""

    language = "en"

    def __init__(self, *a, **k):
        from types import SimpleNamespace as NS
        # One sentence "This is Rocket, today." -> "Rocket" ends at 0.5 s.
        words = [NS(word=" This", end=0.1), NS(word=" is", end=0.2), NS(word=" Rocket,", end=0.5)]
        self.asr = NS(transcribe=lambda *a, **k: ([NS(words=words)], None))

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
                    x = 0.3 * np.sin(2 * np.pi * 110 * t)
                    x[int(0.6 * 24000):int(0.8 * 24000)] = 0
                    sf.write(j["out"], x, 24000, subtype="PCM_16")
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
            b = batch()
            b["lines"][0].update(text="This is Rocket, today.", keep_through="Rocket", asset="voice_brand.wav")
            (d / "b.json").write_text(json.dumps(b))
            argv = ["reel_voice.py", str(d / "b.json"), "--voices", str(d / "voices"), "--scripts-dir", str(SCRIPTS),
                    "--model-path", "x", "--work", str(d / "work"), "--out", str(d / "out")]
            with mock.patch.object(rvx.subprocess, "run", fake_run), mock.patch.object(sys, "argv", argv):
                self.assertEqual(rvx.main(), 0)
            rep = json.loads((d / "out" / "report.json").read_text())
            line = rep["lines"][0]
            self.assertEqual(line["chosen_seeds"], [11, 33, 44])
            self.assertEqual([t["seed"] for t in line["takes"]], [11, 22, 33, 44])
            self.assertTrue((d / "out" / "brand_seed44.mp3").exists())
            self.assertTrue((d / "out" / "brand_seed44_cut.mp3").exists())
            self.assertEqual(line["asset"], "voice_brand.wav")
            # Every rendered take is kept to listen to, the failed seed 22 too.
            takes = sorted(f.name for f in (d / "out" / "takes").iterdir())
            self.assertEqual(takes, ["brand_seed11_PASS.mp3", "brand_seed11_cut_PASS.mp3", "brand_seed22_FAIL.mp3",
                                     "brand_seed33_PASS.mp3", "brand_seed33_cut_PASS.mp3",
                                     "brand_seed44_PASS.mp3", "brand_seed44_cut_PASS.mp3"])
            seed22 = next(t for t in line["takes"] if t["seed"] == 22)
            self.assertEqual(seed22["status"], "fail")
            self.assertEqual(seed22["listen_files"], ["takes/brand_seed22_FAIL.mp3"])
            self.assertEqual(seed22["listen"]["asr_word_errors"], 1)
            import soundfile as sf
            self.assertLess(sf.info(str(d / "out" / "assets" / "voice_brand.wav")).duration, 0.7)


if __name__ == "__main__":
    unittest.main()
