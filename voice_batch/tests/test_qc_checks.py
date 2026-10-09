"""Lead-in, clip checks and word-timings shape (synthetic signals; no models)."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import qc  # noqa: E402

SR = qc.SR


def tone(dur_s, amp=0.1, f=150.0, rise_s=0.02):
    t = np.arange(int(dur_s * SR)) / SR
    x = amp * np.sin(2 * np.pi * f * t)
    r = int(rise_s * SR)
    if r:
        x[:r] *= np.linspace(0, 1, r)
    return x


def good_clip():
    x = np.concatenate([np.zeros(int(0.2 * SR)), tone(2.0)])
    return x * (10 ** (qc.NORM_TARGET_DB / 20) / np.sqrt(np.mean(tone(2.0) ** 2)))


def checks(x, wpm=149.0, pace=(149.0, 15.0)):
    return qc.clip_checks(x, SR, wpm, pace)


class LeadIn(unittest.TestCase):
    def test_pads_shortfall_only(self):
        x = np.concatenate([np.zeros(int(0.05 * SR)), np.full(SR // 2, 0.1)])
        y = qc.lead_in(x)
        self.assertEqual(len(y), len(x) + int(0.15 * SR))
        self.assertAlmostEqual(qc.lead_s(y), 0.20, places=3)

    def test_no_pad_when_enough(self):
        x = np.concatenate([np.zeros(int(0.3 * SR)), tone(0.5)])
        self.assertEqual(len(qc.lead_in(x)), len(x))

    def test_fade_in_applied(self):
        x = np.ones(SR) * 0.5
        y = qc.lead_in(x)
        n0 = int(0.2 * SR)
        self.assertEqual(y[n0], 0.0)
        self.assertLess(y[n0 + 100], 0.5)
        self.assertAlmostEqual(y[n0 + int(0.01 * SR) + 5], 0.5)

    def test_silence_untouched(self):
        self.assertEqual(len(qc.lead_in(np.zeros(100))), 100)

    def test_stitch_leads_in_before_normalise(self):
        from types import SimpleNamespace as NS
        from unittest import mock
        fake = NS(effects=NS(trim=lambda x, **kw: (x, (0, len(x)))))   # trim keeps the whole take
        with mock.patch.dict(sys.modules, {"librosa": fake}):
            y, _ = qc.stitch([tone(0.5, rise_s=0), tone(0.5, rise_s=0)])
        self.assertGreaterEqual(qc.lead_s(y), 0.199)


class ClipChecks(unittest.TestCase):
    def test_good_clip_passes(self):
        gate, m = checks(good_clip())
        self.assertTrue(all(gate.values()), (gate, m))

    def test_pace_report_only(self):
        for wpm, flag in ((120, "under"), (203, "over"), (149, "ok"), (None, None)):
            gate, m = checks(good_clip(), wpm=wpm)
            self.assertNotIn("pace", gate)            # never fails or retries a clip
            self.assertTrue(all(gate.values()))
            self.assertEqual(m["pace"]["flag"], flag)
        self.assertEqual(qc.pace_report(125, (130, 10)),
                         {"wpm": 125.0, "target_wpm": 130.0, "tolerance_wpm": 10.0, "flag": "ok"})

    def test_summary_shows_pace(self):
        import summary
        m = {"voice": "voice_a", "lines": [{"id": "a", "pace": qc.pace_report(170, (135, 15))}], "failed": []}
        self.assertIn("170 (135±15) **over**", summary.summary(m))

    def test_pace_spec(self):
        self.assertEqual(qc.pace_spec(None), (149.0, 15.0))
        self.assertEqual(qc.pace_spec({"pace": {"wpm": 140, "tolerance_wpm": 10}}), (140.0, 10.0))
        self.assertEqual(qc.pace_spec({"pace": 160}), (160.0, 15.0))

    def test_loudness(self):
        self.assertFalse(checks(good_clip() * 10 ** (2.5 / 20))[0]["loudness"])
        self.assertTrue(checks(good_clip() * 10 ** (1.5 / 20))[0]["loudness"])

    def test_measured_tutor_001_renders(self):
        """Numbers measured on tutor_001's accepted renders after lead_in +
        normalise (audio is private, so only the numbers live here)."""
        for integ, lead_ms, peak, head, rise in [(-18.48, 206.5, -4.14, -120.0, 35.21), (-18.95, 204.2, -3.8, -120.0, 29.5),
                                                 (-19.03, 204.6, -3.12, -120.0, 47.88), (-19.62, 204.1, -4.04, -120.0, 26.92),
                                                 (-18.79, 211.5, -1.18, -120.0, 21.96), (-19.41, 206.0, -1.01, -120.0, 44.54)]:
            self.assertLessEqual(abs(integ - qc.NORM_TARGET_DB), qc.LOUDNESS_TOL_DB)
            self.assertGreaterEqual(lead_ms, qc.LEAD_MIN_S * 1000)
            self.assertLess(peak, qc.CLIP_PEAK_DBFS)
            self.assertLess(head, qc.HOT_FLOOR_DBFS)
            self.assertGreaterEqual(rise, qc.ONSET_RISE_MIN_S * 1000)

    def test_lead_in(self):
        x = good_clip()[int(0.05 * SR):]   # 150 ms lead-in
        self.assertFalse(checks(x)[0]["lead_in"])

    def test_clipping(self):
        x = good_clip()
        x[SR:SR + 10] = 1.0
        self.assertFalse(checks(x)[0]["clipping"])
        y = good_clip()
        y[SR] = 1.0                       # single full-scale sample: under the run limit
        self.assertTrue(checks(y)[0]["clipping"])

    def test_hiss_in_head(self):
        x = good_clip() + np.random.default_rng(0).normal(0, 0.003, len(good_clip()))
        gate, m = checks(x)
        self.assertGreater(m["head_rms_dbfs"], qc.HOT_FLOOR_DBFS)
        self.assertFalse(gate["onset"])

    def test_hard_onset(self):
        sq = np.concatenate([np.zeros(int(0.2 * SR)), np.full(SR, 0.1)])
        gate, m = checks(sq)
        self.assertLess(m["onset_rise_ms"], 5)
        self.assertFalse(gate["onset"])

    def test_faded_onset_at_4_96_ms_passes(self):
        """tutor_001 greetings/05 measured 4.96 ms with a silent head in every
        round: a faded onset, not a hard edge."""
        self.assertGreaterEqual(4.96, qc.ONSET_RISE_MIN_S * 1000)
        self.assertGreater(qc.ONSET_RISE_MIN_S * 1000, 1.0)


class Timings(unittest.TestCase):
    def test_shape(self):
        words = [{"w": " Hello", "start": 0.2, "end": 0.5}, {"w": " there", "start": 0.55, "end": 0.8},
                 {"w": " friend.", "start": 1.0, "end": 1.4}]
        t = qc.timings("Hello there friend.", words, 1.6)
        self.assertEqual(set(t), {"text", "duration_s", "wpm", "words", "gaps"})
        self.assertEqual(t["words"][0], {"w": "Hello", "start": 0.2, "end": 0.5})
        self.assertEqual(t["gaps"], [{"start": 0.8, "end": 1.0}])   # 50 ms gap dropped, 200 ms kept
        self.assertAlmostEqual(t["wpm"], 150.0)
        json.dumps(t)

    def test_write_next_to_clip(self):
        import run
        with tempfile.TemporaryDirectory() as d:
            clip = Path(d) / "line_001.wav"
            run.write_timings(clip, {"timings": qc.timings("Hi", [{"w": "Hi", "start": 0.2, "end": 0.4}], 0.6)})
            data = json.loads((Path(d) / "line_001.timings.json").read_text())
            self.assertEqual(data["words"][0]["w"], "Hi")
            self.assertEqual(data["gaps"], [])

    def test_voice_pace_from_agent(self):
        import run
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(run.voice_pace(Path(d), "tutor_001"), (149.0, 15.0))
            self.assertEqual(run.voice_pace(Path(d), None), (149.0, 15.0))
            p = Path(d) / "lms/team/voices/tutor_001.voice.json"
            p.parent.mkdir(parents=True)
            p.write_text(json.dumps({"pitch": {"target_f0_hz": 104, "tolerance_hz": 15},
                                     "pace": {"wpm": 135, "tolerance_wpm": 15, "pause_style": "short"}}))
            self.assertEqual(run.voice_pace(Path(d), "tutor_001"), (135.0, 15.0))


class MeterWordTimestamps(unittest.TestCase):
    def test_measure_requests_word_timestamps(self):
        from types import SimpleNamespace as NS
        from unittest import mock
        seen = {}

        class ASR:
            def transcribe(self, p, **kw):
                seen.update(kw)
                return iter([NS(text=" Hi", words=[NS(word=" Hi", start=0.2, end=0.4)])]), None

        m = qc.Meter.__new__(qc.Meter)
        m.language, m.asr, m.hi = "en", ASR(), 1e9
        m._pyin = lambda w: (np.full(10, 100.0), np.ones(10, bool))
        m._pre = lambda w: w
        m.enc = NS(embed_utterance=lambda w: np.ones(3))
        m.R = np.ones(3)
        x = good_clip()
        with mock.patch.object(qc.Meter, "r16", staticmethod(lambda p: x)), \
             mock.patch.dict(sys.modules, {"soundfile": NS(read=lambda p: (x, SR))}):
            out = m.measure("x.wav", "Hi")
        self.assertTrue(seen.get("word_timestamps"))
        self.assertEqual(out["words"], [{"w": " Hi", "start": 0.2, "end": 0.4}])


if __name__ == "__main__":
    unittest.main()
