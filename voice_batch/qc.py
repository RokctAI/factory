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
           takes are used (tier 2) and the final gate decides.
Stitch   : trim at -40 dB with 40 ms padding, 12 ms fades, 200-240 ms
           silence (280-320 ms pauses between words), -20 dBFS, 24 kHz
           mono PCM_16.
Gate     : final file median F0 within target +/- tolerance (default
           94-110 Hz, tuned to Voice A; a batch sets f0_target_hz and
           f0_tolerance_hz for another voice); similarity >= 0.88 (>= 5 s)
           or >= 0.83 (< 5 s); word-exact ASR against the line's asr_text
           (the TTS respelling for an R-3 phonics line, else the text).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from textnorm import word_errors  # noqa: E402

SR = 24_000
# Voice A defaults; batch.py's f0_target_hz / f0_tolerance_hz override them.
TARGET_F0 = 102.0
F0_TOLERANCE = 8.0
F0_RANGE = (TARGET_F0 - F0_TOLERANCE, TARGET_F0 + F0_TOLERANCE)
SIM_LONG, SIM_SHORT, LONG_S = 0.88, 0.83, 5.0
TAKE_SIM_MIN = SIM_SHORT
GAPS_S = (0.22, 0.20, 0.24, 0.22)   # + 2 x 40 ms padding = 300/280/320/300 ms pauses
PAD_S, FADE_S = 0.04, 0.012


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
    exact = [c for c in cands if c["err"] == 0]
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
    return np.concatenate(out), pauses


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

    def measure(self, p, text: str) -> dict:
        import numpy as np
        w = self.r16(p)
        segs, _ = self.asr.transcribe(str(p), beam_size=5, language=self.language)
        tx = " ".join(s.text.strip() for s in segs)
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
        e = self.enc.embed_utterance(self._pre(w))
        res = float(np.dot(e, self.R) / np.linalg.norm(e) / np.linalg.norm(self.R))
        return {"dur": round(len(w) / 16000, 3), "res": round(res, 4), "err": word_errors(text, tx),
                "f0": round(float(np.median(fv)), 2) if len(fv) else 0.0, "swings": int(swings), "transcript": tx}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", required=True)
    ap.add_argument("--ref", required=True)
    ap.add_argument("--scripts-dir", required=True)
    ap.add_argument("--asr-model", default=os.environ.get("ASR_MODEL", "small.en"))
    ap.add_argument("--f0-target", type=float, default=TARGET_F0)
    ap.add_argument("--f0-tolerance", type=float, default=F0_TOLERANCE)
    ap.add_argument("--language", default="en")
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

    for p, meta in index.items():
        if p in M or not Path(p).exists():
            continue
        m = meter.measure(p, sentence_of[meta["key"]])
        M[p] = {**m, **meta}
        print(f"take {meta['key']} seed{meta['seed']}: err={m['err']} f0={m['f0']} swings={m['swings']} "
              f"sim={m['res']} dur={m['dur']}", flush=True)
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
        fm = meter.measure(dst, it.get("asr_text", it["text"]))
        x, _ = sf.read(str(dst))
        dur = round(len(x) / SR, 3)
        thr = sim_threshold(dur)
        gate = {"f0": lo <= fm["f0"] <= hi, "similarity": fm["res"] >= thr, "asr": fm["err"] == 0}
        r.update({
            "status": "pass" if all(gate.values()) else "fail", "gate": gate, "final_path": str(dst),
            "duration_s": dur, "median_f0_hz": fm["f0"], "upward_swings": fm["swings"],
            "similarity": fm["res"], "similarity_threshold": thr, "asr_match": fm["err"] == 0,
            "asr_word_errors": fm["err"], "asr_transcript": fm["transcript"],
            "rms_dbfs": round(float(20 * np.log10(np.sqrt(np.mean(x ** 2)))), 2),
            "peak": round(float(np.max(np.abs(x))), 4), "pauses_ms": pauses,
            "sha256": hashlib.sha256(dst.read_bytes()).hexdigest(),
            "seeds": [b["seed"] for b in picks],
            "takes": [{"sentence": k, "seed": b["seed"], "tier": t, "median_f0_hz": b["f0"],
                       "upward_swings": b["swings"], "similarity": b["res"], "duration_s": b["dur"]}
                      for k, (b, t) in enumerate(zip(picks, tiers), 1)],
        })
        results.append(r)
        print(f"line {it['id']}: {r['status']} dur={dur}s f0={fm['f0']} sim={fm['res']} (>= {thr}) "
              f"asr_errors={fm['err']} seeds={r['seeds']}", flush=True)
    (work / "results.json").write_text(json.dumps(results, indent=1, ensure_ascii=False), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
