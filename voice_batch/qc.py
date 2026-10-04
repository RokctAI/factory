#!/usr/bin/env python3
"""Measure takes, pick one per sentence, stitch each line, gate the result.

    python voice_batch/qc.py --work WORK --ref REF.wav --scripts-dir <agent>/lms/team/scripts \
        [--f0-target 102 --f0-tolerance 8] [--language en]

Reads WORK/lines.json and WORK/takes_index.json ({take path: {key, seed}}),
caches per-take measurements in WORK/takes_measure.json and writes
WORK/results.json. Logs ids and numbers only.

Per take : faster-whisper transcript (word-exact after number/punctuation
           normalisation), median F0 (pYIN), upward swings (runs of >= 3
           voiced frames above the reference's 90th-percentile F0),
           Resemblyzer cosine similarity to the reference.
Selection: among the sentence's passing takes, median F0 closest to
           the target (default 102 Hz), then fewest upward swings, then
           higher similarity. A passing take is word-exact AND has F0
           within target +/- tolerance (default 94-110 Hz) AND
           similarity >= 0.83; if a sentence has none of those, word-exact
           takes are used (tier 2) and the final gate decides. A take whose
           last 50 ms is above -34 dB of its loudest frame (it ends mid-word)
           never counts, even when the ASR still heard the clipped word.
Stitch   : trim at -40 dB with 40 ms padding, 12 ms fades, 200-240 ms
           silence (280-320 ms pauses between words), -20 dBFS, 24 kHz
           mono PCM_16. Lead-in after the trim and before normalising: the
           silence before the first sound is padded up to 200 ms (only the
           shortfall), with a 10 ms fade-in on the first sound.
Gate     : final file median F0 within target +/- tolerance (default
           94-110 Hz, tuned to Voice A; a batch sets f0_target_hz and
           f0_tolerance_hz for another voice); similarity >= 0.88 (>= 5 s)
           or >= 0.83 (< 5 s); word-exact ASR against the line's asr_text
           (the TTS respelling for an R-3 phonics line, else the text);
           tail: the file's last 50 ms at or below -34 dB of its loudest
           10 ms frame.
           Clip checks (clip_checks): pace within the voice's target +/-
           tolerance wpm (voice spec `pace`, default 149 +/- 15); integrated
           level within +/-2.0 dB of the -20 dBFS normalise target; >= 180 ms
           silence before the first audible sample; no clipping (peak below
           -0.3 dBFS, or fewer than 3 consecutive full-scale samples); first
           50 ms RMS below -60 dBFS and the first onset rising over >= 5 ms.
           A failing line is retried and then excluded like any other gate.
Timings  : faster-whisper word timestamps of the final file go to
           results.json "timings" ({text, duration_s, wpm, words, gaps >= 80 ms}).
Word-exact: every word except the ones a pronunciation respelled
           (pronunciations.py: pronunciations.json or inline
           {{word|respelling}}), which are wildcards for 1-N words.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pronunciations import word_errors_wild  # noqa: E402

SR = 24_000
# Voice A defaults; batch.py's f0_target_hz / f0_tolerance_hz override them.
TARGET_F0 = 102.0
F0_TOLERANCE = 8.0
F0_RANGE = (TARGET_F0 - F0_TOLERANCE, TARGET_F0 + F0_TOLERANCE)
SIM_LONG, SIM_SHORT, LONG_S = 0.88, 0.83, 5.0
TAKE_SIM_MIN = SIM_SHORT
GAPS_S = (0.22, 0.20, 0.24, 0.22)   # + 2 x 40 ms padding = 300/280/320/300 ms pauses
PAD_S, FADE_S = 0.04, 0.012
# Tail check: the last TAIL_WIN_S of a take or line, relative to its loudest
# 10 ms frame, must be below TAIL_MAX_DB. Speech still sounding there means
# the model stopped mid-word (the ASR often still hears the clipped word).
# Tuned on tutor_001's Voice A lines (25 sentence ends): clean ends measure
# -37.8 dB or lower, clipped ends -30.0 dB or higher. The 50 ms window is
# just over the stitch's 40 ms pad.
TAIL_WIN_S, TAIL_MAX_DB = 0.05, -34.0
# Lead-in (mirrors rokct_media speech/stitch.py): silence before the first
# sound of every finished clip, padded only by the shortfall.
LEAD_S, LEAD_FADE_S = 0.20, 0.010
LEAD_TOP_DB = 40.0          # below -40 dB of the peak counts as silence (matches the trim)
# Clip checks on the finished file.
PACE_WPM, PACE_TOL_WPM = 149.0, 15.0     # default when the voice spec has no `pace`
# Loudness: gated integrated level (silence excluded) vs the normaliser's
# whole-file RMS target. On tutor_001's accepted renders after lead_in +
# normalise the gated level reads 0.4-1.52 dB above -20 (more silence, more
# bias), so 1.5 dB rejected a good clip; 2.0 dB clears them with margin and
# still catches a normaliser that backed off or a mis-scaled file.
NORM_TARGET_DB, LOUDNESS_TOL_DB = -20.0, 2.0
LEAD_MIN_S = 0.18
CLIP_PEAK_DBFS, CLIP_FULL_SCALE, CLIP_RUN_MAX = -0.3, 0.999, 3
HOT_WIN_S, HOT_FLOOR_DBFS = 0.05, -60.0
# First onset: from the first sample above -40 dB of the peak to 90 % of the
# loudest sample in the 50 ms after it must take >= 5 ms (the stitch's 12 ms
# fade and the lead-in's 10 ms fade both give ~9-12 ms; a hard edge gives ~0).
ONSET_RISE_MIN_S, ONSET_WIN_S, ONSET_REACH = 0.005, 0.05, 0.9
GAP_MIN_S = 0.08


def lead_in(x, sr: int = SR, lead_s: float = LEAD_S, fade_s: float = LEAD_FADE_S):
    """`x` with silence at the front up to `lead_s`; the silence it already
    has counts, so only the shortfall is added, with a fade-in on the first sound."""
    import numpy as np
    x = np.asarray(x, dtype=np.float64).reshape(-1)
    peak = float(np.max(np.abs(x))) if x.size else 0.0
    want = int(round(lead_s * sr))
    if peak <= 0.0 or want <= 0:
        return x
    loud = np.nonzero(np.abs(x) > peak * 10 ** (-LEAD_TOP_DB / 20))[0]
    have = int(loud[0]) if loud.size else len(x)
    if have >= want:
        return x
    y = x.copy()
    fade = min(int(round(fade_s * sr)), len(y) - have)
    if fade > 0:
        y[have:have + fade] *= np.linspace(0, 1, fade)
    return np.concatenate([np.zeros(want - have), y])


def _db(v: float) -> float:
    import math
    return max(-120.0, 20 * math.log10(max(v, 1e-12)))


def lead_s(x, sr: int = SR) -> float:
    """Seconds before the first sample above -LEAD_TOP_DB of the peak."""
    import numpy as np
    x = np.abs(np.asarray(x, dtype=np.float64).reshape(-1))
    peak = float(x.max()) if x.size else 0.0
    if peak <= 0.0:
        return len(x) / sr
    return int(np.argmax(x > peak * 10 ** (-LEAD_TOP_DB / 20))) / sr


def integrated_db(x, sr: int = SR) -> float:
    """Gated integrated level in dBFS RMS: 400 ms blocks (100 ms hop), blocks
    under -70 dBFS dropped, then blocks 10 dB under their mean dropped."""
    import numpy as np
    x = np.asarray(x, dtype=np.float64).reshape(-1)
    n, hop = int(0.4 * sr), int(0.1 * sr)
    if len(x) < n:
        ms = np.array([np.mean(x ** 2)]) if x.size else np.array([0.0])
    else:
        ms = np.array([np.mean(x[i:i + n] ** 2) for i in range(0, len(x) - n + 1, hop)])
    ms = ms[ms > 10 ** (-70 / 10)]
    if not ms.size:
        return -120.0
    ms = ms[ms > np.mean(ms) * 10 ** (-10 / 10)]
    return round(10 * float(np.log10(np.mean(ms))), 2)


def longest_full_scale_run(x, full: float = CLIP_FULL_SCALE) -> int:
    import numpy as np
    hot = np.abs(np.asarray(x, dtype=np.float64).reshape(-1)) >= full
    best = run = 0
    for h in hot:
        run = run + 1 if h else 0
        best = max(best, run)
    return best


def onset_rise_s(x, sr: int = SR) -> float:
    """Seconds from the first sample above -40 dB of the peak to the first
    reaching ONSET_REACH of the loudest sample in the ONSET_WIN_S after it
    (one sample = a hard, clicky onset)."""
    import numpy as np
    a = np.abs(np.asarray(x, dtype=np.float64).reshape(-1))
    peak = float(a.max()) if a.size else 0.0
    if peak <= 0.0:
        return 0.0
    start = int(np.argmax(a > peak * 10 ** (-LEAD_TOP_DB / 20)))
    seg = a[start:start + max(1, int(ONSET_WIN_S * sr))]
    return int(np.argmax(seg >= ONSET_REACH * float(seg.max()))) / sr


def pace_spec(spec: dict | None) -> tuple[float, float]:
    """(target wpm, tolerance) from a voice spec's `pace` (a number or
    {wpm|target_wpm, tolerance_wpm|tolerance}); defaults when absent."""
    p = (spec or {}).get("pace")
    if isinstance(p, (int, float)):
        return float(p), PACE_TOL_WPM
    if isinstance(p, dict):
        t = p.get("wpm", p.get("target_wpm", PACE_WPM))
        tol = p.get("tolerance_wpm", p.get("tolerance", PACE_TOL_WPM))
        return float(t), float(tol)
    return PACE_WPM, PACE_TOL_WPM


def clip_checks(x, sr: int = SR, wpm: float | None = None, pace: tuple[float, float] = (PACE_WPM, PACE_TOL_WPM),
                target_db: float = NORM_TARGET_DB) -> tuple[dict, dict]:
    """(gate booleans, measurements) for a finished, normalised clip."""
    import numpy as np
    x = np.asarray(x, dtype=np.float64).reshape(-1)
    peak = float(np.max(np.abs(x))) if x.size else 0.0
    head = x[:max(1, int(HOT_WIN_S * sr))]
    m = {"wpm": None if wpm is None else round(float(wpm), 1), "integrated_db": integrated_db(x, sr),
         "lead_in_ms": round(lead_s(x, sr) * 1000, 1), "peak_dbfs": round(_db(peak), 2),
         "full_scale_run": longest_full_scale_run(x), "head_rms_dbfs": round(_db(float(np.sqrt(np.mean(head ** 2)))), 2),
         "onset_rise_ms": round(onset_rise_s(x, sr) * 1000, 2)}
    t, tol = pace
    gate = {"pace": wpm is not None and abs(wpm - t) <= tol,
            "loudness": abs(m["integrated_db"] - target_db) <= LOUDNESS_TOL_DB,
            "lead_in": m["lead_in_ms"] >= LEAD_MIN_S * 1000,
            "clipping": m["peak_dbfs"] < CLIP_PEAK_DBFS or m["full_scale_run"] < CLIP_RUN_MAX,
            "onset": m["head_rms_dbfs"] < HOT_FLOOR_DBFS and m["onset_rise_ms"] >= ONSET_RISE_MIN_S * 1000}
    return gate, m


def timings(text: str, words: list, duration_s: float) -> dict:
    """{text, duration_s, wpm, words:[{w,start,end}], gaps:[{start,end}] >= GAP_MIN_S}."""
    ws = [{"w": str(w["w"]).strip(), "start": round(float(w["start"]), 3), "end": round(float(w["end"]), 3)}
          for w in words if str(w["w"]).strip()]
    span = ws[-1]["end"] - ws[0]["start"] if ws else 0.0
    wpm = round(len(ws) / span * 60, 1) if span > 0 else 0.0
    gaps = [{"start": a["end"], "end": b["start"]} for a, b in zip(ws, ws[1:])
            if b["start"] - a["end"] >= GAP_MIN_S - 1e-9]
    return {"text": text, "duration_s": round(float(duration_s), 3), "wpm": wpm, "words": ws, "gaps": gaps}


def tail_db(x, sr: int = SR, win_s: float = TAIL_WIN_S) -> float:
    """dB of the last `win_s` of `x` relative to its loudest 10 ms frame."""
    import numpy as np
    x = np.asarray(x, dtype=np.float64).reshape(-1)
    n = max(1, int(0.01 * sr))
    frames = x[: len(x) // n * n].reshape(-1, n) if len(x) >= n else x.reshape(1, -1)
    ref = float(np.sqrt(np.mean(frames ** 2, axis=1)).max())
    if ref <= 0.0:
        return -120.0
    tail = x[-max(1, int(win_s * sr)):]
    return round(max(-120.0, 20 * float(np.log10(max(float(np.sqrt(np.mean(tail ** 2))), 1e-12) / ref))), 2)


def tail_ok(db: float) -> bool:
    return db <= TAIL_MAX_DB


def sim_threshold(duration_s: float) -> float:
    return SIM_LONG if duration_s >= LONG_S else SIM_SHORT


def f0_range(target: float = TARGET_F0, tolerance: float = F0_TOLERANCE) -> tuple[float, float]:
    return (target - tolerance, target + tolerance)


def pyin_bounds(target: float = TARGET_F0, tolerance: float = F0_TOLERANCE) -> tuple[float, float]:
    """pYIN search range: 50-300 Hz for Voice A, widened for a voice whose
    gate reaches outside it (e.g. a higher R-3 voice)."""
    lo, hi = f0_range(target, tolerance)
    return min(50.0, round(lo * 0.6)), max(300.0, hi * 2)


def take_rank(m: dict, target: float = TARGET_F0) -> tuple:
    return (abs(m["f0"] - target), m["swings"], -m["res"])


def pick(cands: list[dict], target: float = TARGET_F0, tolerance: float = F0_TOLERANCE) -> tuple[dict | None, int]:
    """(best take, tier) — tier 1 strict pass, tier 2 word-exact only, 0 none."""
    lo, hi = f0_range(target, tolerance)
    # A take that ends mid-word never counts, however well the ASR heard it.
    exact = [c for c in cands if c["err"] == 0 and tail_ok(c.get("tail_db", -120.0))]
    strict = [c for c in exact if lo <= c["f0"] <= hi and c["res"] >= TAKE_SIM_MIN]
    rank = lambda c: take_rank(c, target)  # noqa: E731
    if strict:
        return min(strict, key=rank), 1
    if exact:
        return min(exact, key=rank), 2
    return None, 0


def stitch(arrays: list, sr: int = SR):
    import librosa
    import numpy as np
    fade, pad = int(FADE_S * sr), int(PAD_S * sr)
    out, pauses = [], []
    for j, x in enumerate(arrays):
        x = np.asarray(x, dtype=np.float64)
        _, (s, e) = librosa.effects.trim(x, top_db=40, frame_length=512, hop_length=128)
        x = x[max(0, s - pad):min(len(x), e + pad)].copy()
        ramp = np.linspace(0, 1, fade) ** 2
        x[:fade] *= ramp
        x[-fade:] *= ramp[::-1]
        out.append(x)
        if j < len(arrays) - 1:
            g = GAPS_S[j % len(GAPS_S)]
            out.append(np.zeros(int(round(g * sr))))
            pauses.append(int(round((g + 2 * PAD_S) * 1000)))
    # Lead-in after the trim, before normalise (the caller normalises).
    return lead_in(np.concatenate(out), sr), pauses


class Meter:
    def __init__(self, ref: Path, asr_model: str, language: str = "en",
                 pyin: tuple[float, float] = (50.0, 300.0)):
        self.language = language
        self.pyin_bounds = pyin
        import librosa  # noqa: F401
        from faster_whisper import WhisperModel
        from resemblyzer import VoiceEncoder, preprocess_wav
        self._pre = preprocess_wav
        self.enc = VoiceEncoder("cpu", verbose=False)
        self.asr = WhisperModel(asr_model, device="cpu", compute_type="int8",
                                download_root=os.environ.get("ASR_DOWNLOAD_ROOT") or None)
        w = self.r16(ref)
        self.R = self.enc.embed_utterance(preprocess_wav(w))
        import numpy as np
        f, v = self._pyin(w)
        self.hi = float(np.percentile(f[v], 90))

    @staticmethod
    def r16(p):
        import librosa
        import soundfile as sf
        w, sr = sf.read(str(p))
        w = w.mean(1) if w.ndim > 1 else w
        return librosa.resample(w, orig_sr=sr, target_sr=16000)

    def _pyin(self, w):
        import librosa
        fmin, fmax = self.pyin_bounds
        f, v, _ = librosa.pyin(w, fmin=fmin, fmax=fmax, sr=16000, frame_length=1024, hop_length=256)
        return f, v

    def measure(self, p, text: str, wild: list | None = None) -> dict:
        import numpy as np
        w = self.r16(p)
        segs, _ = self.asr.transcribe(str(p), beam_size=5, language=self.language, word_timestamps=True)
        segs = list(segs)
        tx = " ".join(s.text.strip() for s in segs)
        words = [{"w": w.word, "start": w.start, "end": w.end} for s in segs for w in (getattr(s, "words", None) or [])]
        f, v = self._pyin(w)
        fv = f[v]
        hi = np.where(v, f, 0) > self.hi
        swings, run = 0, 0
        for h in list(hi) + [False]:
            if h:
                run += 1
            else:
                swings += run >= 3
                run = 0
        import soundfile as sf
        x, sr = sf.read(str(p))
        x = x.mean(1) if x.ndim > 1 else x
        e = self.enc.embed_utterance(self._pre(w))
        res = float(np.dot(e, self.R) / np.linalg.norm(e) / np.linalg.norm(self.R))
        return {"dur": round(len(w) / 16000, 3), "res": round(res, 4), "err": word_errors_wild(text, tx, wild),
                "f0": round(float(np.median(fv)), 2) if len(fv) else 0.0, "swings": int(swings), "transcript": tx,
                "tail_db": tail_db(x, sr), "words": words}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", required=True)
    ap.add_argument("--ref", required=True)
    ap.add_argument("--scripts-dir", required=True)
    ap.add_argument("--asr-model", default=os.environ.get("ASR_MODEL", "small.en"))
    ap.add_argument("--f0-target", type=float, default=TARGET_F0)
    ap.add_argument("--f0-tolerance", type=float, default=F0_TOLERANCE)
    ap.add_argument("--language", default="en")
    ap.add_argument("--pace-wpm", type=float, default=PACE_WPM)
    ap.add_argument("--pace-tolerance", type=float, default=PACE_TOL_WPM)
    args = ap.parse_args()
    lo, hi = f0_range(args.f0_target, args.f0_tolerance)
    sys.path.insert(0, args.scripts_dir)
    import numpy as np
    import soundfile as sf
    import render_voices as rv

    work = Path(args.work)
    lines = json.loads((work / "lines.json").read_text(encoding="utf-8"))
    index = json.loads((work / "takes_index.json").read_text(encoding="utf-8"))
    mpath = work / "takes_measure.json"
    M = json.loads(mpath.read_text(encoding="utf-8")) if mpath.exists() else {}
    meter = Meter(Path(args.ref), args.asr_model, args.language, pyin_bounds(args.f0_target, args.f0_tolerance))
    sentence_of = {f"{it['id']}#{k}": s for it in lines for k, s in enumerate(it["sentences"], 1)}
    wild_of = {f"{it['id']}#{k}": w for it in lines for k, w in enumerate(it.get("sentence_wild", []), 1)}

    for p, meta in index.items():
        if p in M or not Path(p).exists():
            continue
        m = meter.measure(p, sentence_of[meta["key"]], wild_of.get(meta["key"]))
        m.pop("words", None)
        M[p] = {**m, **meta}
        print(f"take {meta['key']} seed{meta['seed']}: err={m['err']} f0={m['f0']} swings={m['swings']} "
              f"sim={m['res']} dur={m['dur']} tail={m['tail_db']}", flush=True)
        mpath.write_text(json.dumps(M, indent=1), encoding="utf-8")

    results = []
    for it in lines:
        picks, tiers, lacking = [], [], []
        for k in range(1, len(it["sentences"]) + 1):
            key = f"{it['id']}#{k}"
            cands = [dict(m, path=p) for p, m in M.items() if m["key"] == key]
            best, tier = pick(cands, args.f0_target, args.f0_tolerance)
            picks.append(best); tiers.append(tier)
            if tier != 1:
                lacking.append({"key": key, "tier": tier})
        tried = sorted({m["seed"] for m in M.values() if m["key"].split("#")[0] == it["id"]})
        r = {"id": it["id"], "seeds_tried": tried, "lacking": lacking}
        if any(t == 0 for t in tiers):
            r["status"] = "incomplete"
            results.append(r)
            print(f"line {it['id']}: incomplete (no word-exact take for {sum(t == 0 for t in tiers)} sentence(s))")
            continue
        arrays = []
        for b in picks:
            x, sr = sf.read(b["path"])
            assert sr == SR, "unexpected sample rate"
            arrays.append(x)
        y, pauses = stitch(arrays)
        y = rv.normalise(y).astype(np.float32)
        dst = work / "final" / it.get("final_wav", it["file"])
        dst.parent.mkdir(parents=True, exist_ok=True)
        sf.write(str(dst), y, SR, subtype="PCM_16")
        fm = meter.measure(dst, it.get("asr_text", it["text"]), it.get("asr_wild"))
        x, _ = sf.read(str(dst))
        dur = round(len(x) / SR, 3)
        thr = sim_threshold(dur)
        tm = timings(it["text"], fm.get("words", []), dur)
        cgate, cm = clip_checks(x, SR, tm["wpm"] if tm["words"] else None, (args.pace_wpm, args.pace_tolerance))
        gate = {"f0": lo <= fm["f0"] <= hi, "similarity": fm["res"] >= thr, "asr": fm["err"] == 0,
                "tail": tail_ok(fm["tail_db"]), **cgate}
        r.update({
            "status": "pass" if all(gate.values()) else "fail", "gate": gate, "final_path": str(dst),
            "duration_s": dur, "median_f0_hz": fm["f0"], "upward_swings": fm["swings"],
            "similarity": fm["res"], "similarity_threshold": thr, "asr_match": fm["err"] == 0,
            "asr_word_errors": fm["err"], "asr_transcript": fm["transcript"], "tail_db": fm["tail_db"],
            "rms_dbfs": round(float(20 * np.log10(np.sqrt(np.mean(x ** 2)))), 2),
            "peak": round(float(np.max(np.abs(x))), 4), "pauses_ms": pauses,
            "wpm": tm["wpm"], "checks": cm, "timings": tm,
            "sha256": hashlib.sha256(dst.read_bytes()).hexdigest(),
            "seeds": [b["seed"] for b in picks],
            "takes": [{"sentence": k, "seed": b["seed"], "tier": t, "median_f0_hz": b["f0"],
                       "upward_swings": b["swings"], "similarity": b["res"], "duration_s": b["dur"],
                       "tail_db": b.get("tail_db")}
                      for k, (b, t) in enumerate(zip(picks, tiers), 1)],
        })
        results.append(r)
        print(f"line {it['id']}: {r['status']} dur={dur}s f0={fm['f0']} sim={fm['res']} (>= {thr}) "
              f"asr_errors={fm['err']} tail={fm['tail_db']} wpm={tm['wpm']} checks={cm} seeds={r['seeds']}", flush=True)
    (work / "results.json").write_text(json.dumps(results, indent=1, ensure_ascii=False), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
