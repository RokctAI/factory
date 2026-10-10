"""Model-free tests for voice_batch. Run: python -m pytest voice_batch/tests

Set AGENT_ROOT to a RokctAI/agent checkout to also check the real line
scripts (skipped otherwise; the scripts are private and never copied here).
"""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import batch  # noqa: E402
from lines import build_lines, spoken_text  # noqa: E402
from qc import TAIL_MAX_DB, pick, sim_threshold, stitch, tail_db, tail_ok  # noqa: E402
from textnorm import TAIL_PAD, norm_words, speak_text, split_sentences, tts_prompt, word_errors  # noqa: E402


class TextNorm(unittest.TestCase):
    def test_split(self):
        self.assertEqual(split_sentences("Right. Go on! Why?  Yes."), ["Right.", "Go on!", "Why?", "Yes."])
        self.assertEqual(split_sentences("Class starts in 3... 2... 1... Sharing now."),
                         ["Class starts in 3... 2... 1...", "Sharing now."])
        self.assertEqual(split_sentences("Wait... Then go. It's 10... ok."), ["Wait...", "Then go.", "It's 10...", "ok."])

    def test_speak_text_punctuation_only(self):
        self.assertEqual(speak_text("Method: a by c - two, three — done."), "Method, a by c, two, three, done.")
        self.assertEqual(norm_words(speak_text("Stay — with me.")), norm_words("Stay — with me."))

    def test_numbers_and_symbols(self):
        self.assertEqual(word_errors("two x squared minus five x minus one", "2x² - 5x - 1"), 0)
        self.assertEqual(word_errors("minus twelve", "-12"), 0)
        self.assertEqual(word_errors("forty minutes", "40 minutes."), 0)

    def test_spelling_and_punctuation(self):
        self.assertEqual(word_errors("Practise tomorrow's drill.", "Practice tomorrows drill"), 0)
        self.assertEqual(word_errors("Top-level work", "top level work"), 0)

    def test_asr_homophones(self):
        ref = "We move quickly and we move correctly — nothing in this session is guessed."
        self.assertEqual(word_errors(ref, "We move quickly and we move correctly, nothing in this session is guest."), 0)
        self.assertEqual(word_errors("Our guest.", "Our guessed."), 0)
        self.assertEqual(word_errors(ref, "We move quickly and we move correctly, nothing in this session is best."), 1)

    def test_tts_prompt_pads_the_end(self):
        self.assertEqual(TAIL_PAD, " ...")
        self.assertEqual(tts_prompt("Let us begin."), "Let us begin. ...")
        self.assertEqual(tts_prompt("Ready?"), "Ready? ...")
        self.assertEqual(tts_prompt("Not you, not today "), "Not you, not today. ...")

    def test_tts_prompt_ends_a_closing_countdown_with_a_full_stop(self):
        self.assertEqual(tts_prompt("Class starts in 3... 2... 1..."), "Class starts in 3... 2... 1. ...")
        self.assertEqual(tts_prompt("Wait..."), "Wait... ...")
        self.assertEqual(norm_words(tts_prompt("Class starts in 3... 2... 1...")),
                         norm_words("Class starts in 3... 2... 1..."))
        # the pad is punctuation only: the ASR words are unchanged
        self.assertEqual(norm_words(tts_prompt("Two x minus 3.")), norm_words("Two x minus 3."))

    def test_real_errors_count(self):
        self.assertEqual(word_errors("Let us start.", "Let's start."), 2)
        self.assertEqual(word_errors("Done.", ""), 1)


class Batch(unittest.TestCase):
    good = {"tutor": "tutor_001", "voice": "voice_a", "ref_path": "lms/team/voice_refs/voice_a_ref.wav",
            "ref_sha256": "0" * 64, "agent_branch": "rokct/x-y", "categories": ["teaching", "greetings"]}

    def load(self, d):
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump(d, f)
        return batch.load_batch(f.name)

    def test_good(self):
        self.assertEqual(self.load(self.good)["categories"], ["greetings", "teaching"])

    def test_rejects(self):
        for k, v in [("agent_branch", "main"), ("agent_branch", "rokct/../main"), ("ref_path", "../x.wav"),
                     ("tutor", "tutor_1; rm"), ("categories", ["all"]), ("ref_sha256", "abc")]:
            with self.assertRaises(batch.BatchError, msg=k):
                self.load(dict(self.good, **{k: v}))

    def test_voice_b_batch1(self):
        """tutor_011's first Voice B batch pins the agent reference and its
        own F0 gate (196 +/- 12 Hz), and renders to a rokct/ branch."""
        b = batch.load_batch(Path(__file__).resolve().parents[2]
                             / "voice_batches/inbox/tutor_011_voice_b_batch1.json")
        self.assertEqual((b["tutor"], b["voice"], b["ref_path"], b["ref_sha256"]), (
            "tutor_011", "voice_b", "lms/team/voice_refs/voice_b_ref.wav",
            "30c7ab70671dcd2c7239337d8de2dd2e6c9b468a11c0e7028646cc244ab6564d"))
        self.assertEqual((b["f0_target_hz"], b["f0_tolerance_hz"]), (196.0, 12.0))
        self.assertEqual(b["agent_branch"], "rokct/tutor-011-voice-b-batch1")
        self.assertEqual(b["categories"], list(batch.CATEGORIES))
        self.assertNotIn("lines", b)

    def test_lines_filter(self):
        b = self.load(dict(self.good, lines=["tutor_001/greetings/02", "tutor_001_sample_line"]))
        self.assertEqual(b["categories"], ["greetings", "teaching"])
        for bad in (["tutor_002/greetings/01"], ["tutor_001/signoffs/01"], [], ["tutor_001/greetings/1"]):
            with self.assertRaises(batch.BatchError):
                self.load(dict(self.good, lines=bad))


class Selection(unittest.TestCase):
    def t(self, err, f0, sw, res):
        return {"err": err, "f0": f0, "swings": sw, "res": res}

    def test_order(self):
        a, b, c = self.t(0, 104, 2, 0.9), self.t(0, 101, 5, 0.85), self.t(1, 102, 0, 0.99)
        self.assertIs(pick([a, b, c])[0], b)
        d = self.t(0, 101, 1, 0.84)
        self.assertIs(pick([b, d])[0], d)
        e = self.t(0, 101, 1, 0.9)
        self.assertIs(pick([d, e])[0], e)

    def test_tiers(self):
        self.assertEqual(pick([self.t(0, 120, 0, 0.9)])[1], 2)
        self.assertEqual(pick([self.t(2, 100, 0, 0.9)]), (None, 0))
        self.assertEqual(sim_threshold(4.99), 0.83)
        self.assertEqual(sim_threshold(5.0), 0.88)

    def test_stitch_pauses(self):
        import numpy as np
        sr = 24000
        tone = lambda s: 0.3 * np.sin(np.arange(int(s * sr)) * 2 * np.pi * 110 / sr)
        pad = np.zeros(int(0.5 * sr))
        y, pauses = stitch([np.concatenate([pad, tone(1), pad])] * 3, sr)
        self.assertEqual(pauses, [300, 280])
        self.assertTrue(all(280 <= p <= 320 for p in pauses))
        # + the lead-in shortfall (the faded pad is mostly under -40 dB, so ~200 ms is added)
        self.assertAlmostEqual(len(y) / sr, 3 + 6 * 0.04 + 0.22 + 0.20 + 0.20, delta=0.1)  # trim works in 128-sample hops
        self.assertAlmostEqual(float(y[0]), 0.0, places=6)


class Tail(unittest.TestCase):
    """A take or line whose last 50 ms still has speech energy was cut off."""
    sr = 24000

    def tone(self, s, amp=0.3):
        import numpy as np
        return amp * np.sin(np.arange(int(s * self.sr)) * 2 * np.pi * 110 / self.sr)

    def test_abrupt_end_fails(self):
        self.assertGreater(tail_db(self.tone(1.0), self.sr), TAIL_MAX_DB)
        self.assertFalse(tail_ok(tail_db(self.tone(1.0), self.sr)))

    def test_clean_end_passes(self):
        import numpy as np
        x = np.concatenate([self.tone(1.0), np.zeros(int(0.1 * self.sr))])
        self.assertTrue(tail_ok(tail_db(x, self.sr)))
        # a natural decay into silence passes too
        decay = self.tone(0.3) * np.exp(-np.arange(int(0.3 * self.sr)) / (0.03 * self.sr))
        self.assertTrue(tail_ok(tail_db(np.concatenate([self.tone(1.0), decay]), self.sr)))

    def test_silence_and_short(self):
        import numpy as np
        self.assertEqual(tail_db(np.zeros(1000), self.sr), -120.0)
        self.assertTrue(tail_ok(tail_db(np.zeros(10), self.sr)))

    def test_stitch_keeps_a_clipped_end_detectable(self):
        # the 12 ms fade must not hide a take that stopped mid-word
        import numpy as np
        pad = np.zeros(int(0.5 * self.sr))
        decay = self.tone(0.3) * np.exp(-np.arange(int(0.3 * self.sr)) / (0.02 * self.sr))
        clean = np.concatenate([pad, self.tone(1.0), decay, pad])  # speech dies away, then silence
        clipped = np.concatenate([pad, self.tone(1.0)])            # the take stops mid-sound
        self.assertTrue(tail_ok(tail_db(stitch([clean, clean])[0], self.sr)))
        self.assertFalse(tail_ok(tail_db(stitch([clean, clipped])[0], self.sr)))

    def test_pick_skips_clipped_takes(self):
        good = {"err": 0, "f0": 110, "swings": 3, "res": 0.84, "tail_db": -45.0}
        cut = {"err": 0, "f0": 102, "swings": 0, "res": 0.95, "tail_db": -12.0}
        self.assertIs(pick([cut, good])[0], good)
        self.assertEqual(pick([cut]), (None, 0))
        # measurements cached before the tail check existed still count
        old = {"err": 0, "f0": 102, "swings": 0, "res": 0.95}
        self.assertEqual(pick([old]), (old, 1))

    def test_rendered_before_fix_is_rerendered(self):
        import hashlib
        import run
        with tempfile.TemporaryDirectory() as d:
            f = Path(d, "a.wav")
            f.write_bytes(b"x")
            it = {"text_sha256": "t", "file": "a.wav"}
            prev = {"text_sha256": "t", "sha256": hashlib.sha256(b"x").hexdigest()}
            self.assertFalse(run.unchanged(prev, it, Path(d), "r"))
            self.assertTrue(run.unchanged(dict(prev, tail_pad=TAIL_PAD), it, Path(d), "r"))


class Lines(unittest.TestCase):
    def test_spoken_text_strips_markdown(self):
        md = "---\nid: x\n---\n# Heading\n<!-- note -->\nSay **this** now.\n"
        self.assertEqual(spoken_text(md), "Say this now.")

    def test_layout(self):
        with tempfile.TemporaryDirectory() as d:
            t = Path(d, "lms/team/tutors/CAPS/tutor_009")
            (t / "greetings").mkdir(parents=True)
            (t / "greetings/01.md").write_text("One. Two.\n")
            (t / "samples.json").write_text(json.dumps({"samples": [{"id": "tutor_009_sample_01", "script": "A. B."}]}))
            Path(d, "lms/team/voices").mkdir(parents=True)
            Path(d, "lms/team/voices/tutor_009.voice.json").write_text(json.dumps({"sample_line": "C."}))
            items = build_lines(d, "tutor_009", ["greetings", "teaching"])
            self.assertEqual([i["file"] for i in items], [
                "lms/team/tutors/CAPS/tutor_009/greetings/01.wav",
                "lms/team/tutors/CAPS/tutor_009/samples/tutor_009_sample_01.wav",
                "lms/team/tutors/CAPS/tutor_009/samples/sample_line.wav"])
            self.assertEqual(items[0]["sentences"], ["One.", "Two."])

    @unittest.skipUnless(os.environ.get("AGENT_ROOT"), "AGENT_ROOT not set")
    def test_real_tutor_001(self):
        cats = ["acknowledgements", "greetings", "signoffs", "teaching"]
        items = build_lines(os.environ["AGENT_ROOT"], "tutor_001", cats)
        self.assertEqual(len(items), 13)
        self.assertEqual(sum(len(i["sentences"]) for i in items), 34)
        for i in items:
            self.assertNotIn("#", i["text"])
            self.assertEqual(word_errors(i["text"], " ".join(i["render_text"])), 0, i["id"])
            for r in i["render_text"]:
                self.assertNotIn(" - ", r)
                self.assertNotIn("—", r)

    @unittest.skipUnless(os.environ.get("AGENT_ROOT"), "AGENT_ROOT not set")
    def test_real_tutor_011(self):
        cats = ["acknowledgements", "greetings", "signoffs", "teaching"]
        items = build_lines(os.environ["AGENT_ROOT"], "tutor_011", cats)
        self.assertEqual(len(items), 13)
        for i in items:
            self.assertNotIn("#", i["text"])
            self.assertEqual(word_errors(i["text"], " ".join(i["render_text"])), 0, i["id"])
            for r in i["render_text"]:
                self.assertNotIn(" - ", r)
                self.assertNotIn("—", r)


if __name__ == "__main__":
    unittest.main()
