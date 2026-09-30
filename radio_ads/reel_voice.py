#!/usr/bin/env python3
"""Render the Reel's voice-over lines with voice_batch's per-sentence
renderer and QC gate, so they meet the tutor voices' quality bar.

    python radio_ads/reel_voice.py radio_ads/reel_voices/<batch>.json --validate
    python radio_ads/reel_voice.py radio_ads/reel_voices/<batch>.json \
        --voices radio_ads/voices --scripts-dir <agent>/lms/team/scripts \
        --model-path <pinned snapshot dir> --work $RUNNER_TEMP/reel --out radio_ads/out/<batch id>

A batch lists lines ({"id", "voice", "text", optional "takes", default 1;
optional "keep_through": a word to cut a passing take after, gated again;
optional "asset": the social/facebook/assets file name the first passing
take, or its cut, is written as under OUT/assets/; optional "prefer_seeds":
seeds from the seed rounds to try first, in that order, so a take already
heard and approved is rendered, and chosen, before the others; the other
seeds keep their rounds)
and, per voice, the F0 gate ("f0_target_hz", "f0_tolerance_hz"). A take is
one seed's rendering of a whole line:

Render : textnorm.split_sentences, then any sentence of two words or fewer
         joins its neighbour (a one-word sentence such as "Begin." comes
         out as "Mm-hmm"); voice_batch/render_takes.py renders each part as
         textnorm.tts_prompt (part + " ...") at cfg 1.3, 10 DDPM steps.
         Pronunciations (voice_batch/pronunciations.py) apply as in the
         tutor batches: inline {{Rocket|Rock-it}} or a global
         pronunciations.json entry changes only what the TTS is given; the
         display text is what the ASR check compares against, with each
         respelled word a wildcard there.
QC     : qc.Meter measures each part (qc.pick: word-exact with a clean
         tail, else the take fails), qc.stitch joins them, and the stitched
         take is gated on median F0 within target +/- tolerance, similarity
         >= 0.88 (>= 0.83 under 5 s), word-exact ASR and qc.tail_ok.
Seeds  : voice_batch's rounds, 11/22/33 then 44 then 55, until the line has
         its number of passing takes. A line with no passing take fails the
         run.

Render and QC run as separate processes (as in voice_batch/run.py) so the
TTS model and the ASR/speaker models are never resident together. Writes
OUT/<line>_seed<N>.wav and .mp3 for every passing take, and OUT/report.json.

Every take rendered, passing or not, is also written for listening as
OUT/takes/<line>_seed<N>[_cut]_<PASS|FAIL>.mp3 (64 kbps mono): the full take
is PASS when it passes the full-take gate, the cut when it passes the cut's
gate (a take whose cut fails therefore has a PASS full take and a FAIL cut,
and is still a failed take). A take with a sentence that failed qc.pick is
stitched from its sentences anyway, only to be heard; its report entry keeps
the reason and gains "listen" (the stitched take's measurements, not gated).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
VB = HERE.parent / "voice_batch"
sys.path.insert(0, str(VB))
import mp3  # noqa: E402
import pronunciations  # noqa: E402
import qc  # noqa: E402
import textnorm  # noqa: E402
from run import SEED_ROUNDS, safe, sha256_file, versions  # noqa: E402

ID_RE = r"[a-z][a-z0-9_]{0,40}"
MAX_TAKES = sum(len(r) for r in SEED_ROUNDS)
SEEDS = [s for r in SEED_ROUNDS for s in r]


def seed_rounds(prefer: list[int] | None = None) -> list[list[int]]:
    """SEED_ROUNDS with the preferred seeds first, one round each: the same
    seeds, only in a different order."""
    prefer = list(prefer or [])
    rest = [[s for s in r if s not in prefer] for r in SEED_ROUNDS]
    return [[s] for s in prefer] + [r for r in rest if r]


def render_parts(text: str) -> list[str]:
    """Sentences to render one at a time; a sentence of two words or fewer
    joins the next one (the previous one when it is last)."""
    parts = textnorm.split_sentences(text)
    while len(parts) > 1:
        short = next((i for i, s in enumerate(parts) if len(s.split()) <= 2), None)
        if short is None:
            break
        j = short + 1 if short + 1 < len(parts) else short - 1
        a, b = sorted((short, j))
        parts[a:b + 1] = [f"{parts[a]} {parts[b]}"]
    return parts


def text_through(text: str, word: str) -> str | None:
    """`text` up to and including the first occurrence of `word`
    (case and punctuation ignored), or None when it is not there."""
    words = text.split()
    for i, w in enumerate(words):
        if textnorm.norm_words(w) == textnorm.norm_words(word):
            return " ".join(words[: i + 1])
    return None


def cut_after(x, sr: int, word_end_s: float, quiet_db: float = -42.0, quiet_s: float = 0.08,
              search_s: float = 0.6):
    """`x` cut in the first quiet stretch (`quiet_s` below `quiet_db` of the
    loudest 10 ms frame) that starts after `word_end_s`, keeping 40 ms of it
    and fading out over the stitch's 12 ms. None when no quiet stretch starts
    within `search_s` (the word runs straight into the next one)."""
    import numpy as np
    x = np.asarray(x, dtype=np.float64).reshape(-1)
    n = max(1, int(0.01 * sr))
    frames = x[: len(x) // n * n].reshape(-1, n)
    rms = np.sqrt(np.mean(frames ** 2, axis=1))
    db = 20 * np.log10(np.maximum(rms, 1e-12) / max(float(rms.max()), 1e-12))
    need = max(1, int(round(quiet_s / 0.01)))
    first, last = int(word_end_s / 0.01), min(len(db) - need, int((word_end_s + search_s) / 0.01))
    for i in range(max(0, first), last + 1):
        if (db[i:i + need] < quiet_db).all():
            y = x[: min(len(x), (i + int(qc.PAD_S / 0.01)) * n)].copy()
            fade = int(qc.FADE_S * sr)
            y[-fade:] *= np.linspace(1, 0, fade) ** 2
            return y
    return None


def load_batch(path: Path, pron: dict | None = None) -> dict:
    b = json.loads(path.read_text(encoding="utf-8"))
    pron = pronunciations.load() if pron is None else pron
    if not re.fullmatch(ID_RE, str(b.get("id", ""))):
        raise ValueError(f"batch id must match {ID_RE}")
    voices = b.get("voices") or {}
    for v, g in voices.items():
        if not re.fullmatch(ID_RE, v):
            raise ValueError(f"voice name must match {ID_RE}: {v!r}")
        for k in ("f0_target_hz", "f0_tolerance_hz"):
            if not isinstance(g.get(k), (int, float)):
                raise ValueError(f"voices.{v}.{k} must be a number")
    seen = set()
    for ln in b.get("lines") or []:
        if not re.fullmatch(ID_RE, str(ln.get("id", ""))) or ln["id"] in seen:
            raise ValueError(f"line ids must be unique and match {ID_RE}: {ln.get('id')!r}")
        seen.add(ln["id"])
        if ln.get("voice") not in voices:
            raise ValueError(f"line {ln['id']}: voice {ln.get('voice')!r} has no entry under 'voices'")
        if not str(ln.get("text", "")).strip():
            raise ValueError(f"line {ln['id']}: empty text")
        ln.setdefault("takes", 1)
        if not (isinstance(ln["takes"], int) and 1 <= ln["takes"] <= MAX_TAKES):
            raise ValueError(f"line {ln['id']}: takes must be 1-{MAX_TAKES}")
        try:
            said = [pronunciations.apply(p, pron) for p in render_parts(ln["text"])]
        except pronunciations.PronunciationError as exc:
            raise ValueError(f"line {ln['id']}: {exc}") from None
        for w in pronunciations.ambiguous_uses(ln["text"], pron):
            raise ValueError(pronunciations.ambiguous_error(ln["id"], w, pron))
        # "text" and "parts" are the display text (the ASR reference);
        # "tts_parts" is what the model is given.
        ln["source_text"] = ln["text"]
        ln["parts"] = [d for d, _, _ in said]
        ln["text"] = " ".join(ln["parts"])
        ln["tts_parts"] = [t for _, t, _ in said]
        ln["part_wild"] = [w for _, _, w in said]
        ln["wild"] = [x for w in ln["part_wild"] for x in w]
        prefer = ln.get("prefer_seeds", [])
        if not (isinstance(prefer, list) and all(s in SEEDS for s in prefer) and len(set(prefer)) == len(prefer)):
            raise ValueError(f"line {ln['id']}: prefer_seeds must be distinct seeds from {SEEDS}")
        ln["rounds"] = seed_rounds(prefer)
        if "keep_through" in ln and text_through(ln["text"], ln["keep_through"]) is None:
            raise ValueError(f"line {ln['id']}: keep_through {ln['keep_through']!r} is not a word of its text")
        if "asset" in ln and not re.fullmatch(r"[a-z][a-z0-9_]{0,40}\.wav", str(ln["asset"])):
            raise ValueError(f"line {ln['id']}: asset must be a file name like voice_open.wav")
    if not seen:
        raise ValueError("batch has no lines")
    return b


def word_end(words: list, want: str, rest: str, wild: list | None) -> float | None:
    """End time of the transcript word that closes `want` when the words
    after it match `rest`: how keep_through finds a respelled word, whose
    transcript spelling is not the display word ("Rock it" for Rocket)."""
    end = None
    for k in range(1, len(words) + 1):
        head = " ".join(w.word for w in words[:k])
        tail = " ".join(w.word for w in words[k:])
        if (pronunciations.word_errors_wild(want, head, wild) == 0
                and pronunciations.word_errors_wild(rest, tail, wild) == 0):
            end = words[k - 1].end
    return end


def keep_through(meter, dst: Path, t: dict) -> dict:
    """Cut a passing take after its keep_through word (faster-whisper word
    timestamps, then the next quiet stretch) and gate the cut: word-exact
    against the text through that word, a clean tail and similarity. A cut
    that fails fails the take."""
    import soundfile as sf
    want = text_through(t["text"], t["keep_through"])
    segs, _ = meter.asr.transcribe(str(dst), beam_size=5, language=meter.language, word_timestamps=True)
    words = [w for s in segs for w in (s.words or [])]
    ends = [w.end for w in words if textnorm.norm_words(w.word) == textnorm.norm_words(t["keep_through"])]
    if not ends:
        ends = [e for e in [word_end(words, want, t["text"][len(want):], t.get("wild"))] if e is not None]
    x, sr = sf.read(str(dst))
    y = cut_after(x, sr, ends[0]) if ends else None
    if y is None:
        return {"status": "fail", "reason": f"could not cut after {t['keep_through']!r}"}
    cut = dst.with_name(dst.stem + "_cut.wav")
    sf.write(str(cut), y, sr, subtype="PCM_16")
    m = meter.measure(cut, want, t.get("wild"))
    gate = {"similarity": m["res"] >= qc.SIM_SHORT, "asr": m["err"] == 0, "tail": qc.tail_ok(m["tail_db"])}
    out = {"cut": {"text": want, "gate": gate, "duration_s": m["dur"], "median_f0_hz": m["f0"],
                   "similarity": m["res"], "asr_word_errors": m["err"], "asr_transcript": m["transcript"],
                   "tail_db": m["tail_db"], "sha256": sha256_file(cut)}, "cut_path": str(cut)}
    if not all(gate.values()):
        out.update({"status": "fail", "reason": "the cut fails the gate"})
    return out


def listen_take(meter, t: dict, r: dict, rv) -> None:
    """Stitch a take whose sentence failed qc.pick from every sentence it
    rendered, only so it can be heard: measured (report "listen"), not gated."""
    import numpy as np
    import soundfile as sf
    arrays = [sf.read(p)[0] for p in t["paths"] if Path(p).exists()]
    if not arrays:
        return
    y, _ = qc.stitch(arrays)
    dst = Path(t["final"])
    dst.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(dst), rv.normalise(y).astype(np.float32), qc.SR, subtype="PCM_16")
    m = meter.measure(dst, t["text"], t["wild"])
    r["final_path"] = str(dst)
    r["listen"] = {"duration_s": m["dur"], "median_f0_hz": m["f0"], "similarity": m["res"],
                   "asr_word_errors": m["err"], "asr_transcript": m["transcript"], "tail_db": m["tail_db"]}


def write_listen_takes(line_id: str, takes: list[dict], out: Path) -> None:
    """OUT/takes/<line>_seed<N>[_cut]_<PASS|FAIL>.mp3 for every take rendered;
    each file is labelled by its own gate (see the module docstring)."""
    d = out / "takes"
    for t in takes:
        files = []
        for key, gate in (("final_path", t.get("gate")), ("cut_path", (t.get("cut") or {}).get("gate"))):
            if not t.get(key) or not Path(t[key]).exists():
                continue
            ok = bool(gate) and all(gate.values())
            name = f"{line_id}_seed{t['seed']}{'_cut' if key == 'cut_path' else ''}_{'PASS' if ok else 'FAIL'}.mp3"
            mp3.encode(t[key], d / name, bitrate_kbps=64)
            files.append(f"takes/{name}")
        if files:
            t["listen_files"] = files


def gate_takes(args) -> int:
    """QC process: gate every (line, seed) in --qc's jobs file."""
    import numpy as np
    import soundfile as sf
    sys.path.insert(0, args.scripts_dir)
    import render_voices as rv

    spec = json.loads(Path(args.qc).read_text(encoding="utf-8"))
    target, tol = spec["f0_target_hz"], spec["f0_tolerance_hz"]
    lo, hi = qc.f0_range(target, tol)
    meter = qc.Meter(Path(spec["ref"]), args.asr_model, "en", qc.pyin_bounds(target, tol))
    results = []
    for t in spec["takes"]:
        r = {"id": t["id"], "seed": t["seed"], "status": "fail"}
        parts, arrays = [], []
        for text, p, wild in zip(t["parts"], t["paths"], t["part_wild"]):
            if not Path(p).exists():
                parts.append({"missing": True})
                continue
            m = meter.measure(p, text, wild)
            best, tier = qc.pick([m], target, tol)
            parts.append({"tier": tier, "median_f0_hz": m["f0"], "similarity": m["res"], "asr_word_errors": m["err"],
                          "asr_transcript": m["transcript"], "tail_db": m["tail_db"], "duration_s": m["dur"]})
            if best is not None:
                x, sr = sf.read(p)
                assert sr == qc.SR, "unexpected sample rate"
                arrays.append(x)
        r["parts"] = parts
        if len(arrays) != len(t["parts"]):
            r["reason"] = "a sentence has no word-exact take with a clean tail"
            listen_take(meter, t, r, rv)
            results.append(r)
            print(f"take {t['id']} seed{t['seed']}: fail ({r['reason']})", flush=True)
            continue
        y, pauses = qc.stitch(arrays)
        dst = Path(t["final"])
        dst.parent.mkdir(parents=True, exist_ok=True)
        sf.write(str(dst), rv.normalise(y).astype(np.float32), qc.SR, subtype="PCM_16")
        fm = meter.measure(dst, t["text"], t["wild"])
        dur = fm["dur"]
        thr = qc.sim_threshold(dur)
        gate = {"f0": lo <= fm["f0"] <= hi, "similarity": fm["res"] >= thr, "asr": fm["err"] == 0,
                "tail": qc.tail_ok(fm["tail_db"])}
        r.update({"status": "pass" if all(gate.values()) else "fail", "gate": gate, "final_path": str(dst),
                  "duration_s": dur, "median_f0_hz": fm["f0"], "similarity": fm["res"],
                  "similarity_threshold": thr, "asr_word_errors": fm["err"], "asr_transcript": fm["transcript"],
                  "tail_db": fm["tail_db"], "pauses_ms": pauses, "sha256": sha256_file(dst)})
        if r["status"] == "pass" and t.get("keep_through"):
            r.update(keep_through(meter, dst, t))
        results.append(r)
        print(f"take {t['id']} seed{t['seed']}: {r['status']} dur={dur}s f0={fm['f0']} sim={fm['res']} "
              f"(>= {thr}) asr_errors={fm['err']} tail={fm['tail_db']}", flush=True)
    Path(args.qc_out).write_text(json.dumps(results, indent=1, ensure_ascii=False), encoding="utf-8")
    return 0


def render_voice(voice: str, gate: dict, lines: list[dict], args, work: Path) -> dict[str, list[dict]]:
    """Seed rounds for one voice's lines; returns every gated take per line."""
    ref = Path(args.voices) / f"{voice}.wav"
    if not ref.exists():
        raise SystemExit(f"::error::{ref} not found (install_voices.sh installs the cloned voices)")
    work.mkdir(parents=True, exist_ok=True)
    taken: dict[str, list[dict]] = {ln["id"]: [] for ln in lines}
    for rnd in range(1, max(len(ln["rounds"]) for ln in lines) + 1):
        todo = [ln for ln in lines if len(ln["rounds"]) >= rnd
                and sum(t["status"] == "pass" for t in taken[ln["id"]]) < ln["takes"]]
        if not todo:
            continue
        seeds = sorted({s for ln in todo for s in ln["rounds"][rnd - 1]})
        jobs, takes = [], []
        for ln in todo:
            for seed in ln["rounds"][rnd - 1]:
                paths = []
                for k, (part, said) in enumerate(zip(ln["parts"], ln["tts_parts"]), 1):
                    out = str(work / "takes" / f"{safe(ln['id'] + '#' + str(k))}_seed{seed}.wav")
                    jobs.append({"key": f"{ln['id']}#{k}", "text": said, "seed": seed, "out": out})
                    paths.append(out)
                takes.append({"id": ln["id"], "seed": seed, "text": ln["text"], "parts": ln["parts"], "paths": paths,
                              "part_wild": ln["part_wild"], "wild": ln["wild"],
                              "keep_through": ln.get("keep_through"),
                              "final": str(work / "final" / f"{ln['id']}_seed{seed}.wav")})
        (work / "jobs.json").write_text(json.dumps(jobs, ensure_ascii=False), encoding="utf-8")
        (work / "qc.json").write_text(json.dumps({"ref": str(ref), **gate, "takes": takes}, ensure_ascii=False),
                                      encoding="utf-8")
        print(f"::group::{voice} round {rnd}: seeds {seeds}, {len(todo)} line(s)", flush=True)
        subprocess.run([sys.executable, str(VB / "render_takes.py"), "--jobs", str(work / "jobs.json"),
                        "--ref", str(ref), "--scripts-dir", args.scripts_dir, "--model-path", args.model_path],
                       check=True)
        subprocess.run([sys.executable, __file__, args.batch, "--qc", str(work / "qc.json"),
                        "--qc-out", str(work / "qc_results.json"), "--scripts-dir", args.scripts_dir,
                        "--asr-model", args.asr_model], check=True)
        print("::endgroup::", flush=True)
        for r in json.loads((work / "qc_results.json").read_text(encoding="utf-8")):
            taken[r["id"]].append(r)
    return taken


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("batch")
    ap.add_argument("--validate", action="store_true", help="check the batch and print its render plan")
    ap.add_argument("--voices", default=str(HERE / "voices"))
    ap.add_argument("--scripts-dir", help="the agent repo's lms/team/scripts (render_voices.py)")
    ap.add_argument("--model-path", help="local snapshot of the pinned VibeVoice-1.5B revision")
    ap.add_argument("--work")
    ap.add_argument("--out")
    ap.add_argument("--asr-model", default=os.environ.get("REEL_ASR_MODEL", "small.en"))
    ap.add_argument("--qc", help=argparse.SUPPRESS)
    ap.add_argument("--qc-out", help=argparse.SUPPRESS)
    args = ap.parse_args()
    if args.qc:
        return gate_takes(args)
    try:
        b = load_batch(Path(args.batch))
    except (ValueError, json.JSONDecodeError) as exc:
        print(f"::error::{args.batch}: {exc}")
        return 1
    if args.validate:
        for ln in b["lines"]:
            print(f"{ln['id']}: {ln['voice']}, {ln['takes']} take(s), {len(ln['parts'])} render part(s)")
        return 0
    for need in ("scripts_dir", "model_path", "work", "out"):
        if not getattr(args, need):
            ap.error(f"--{need.replace('_', '-')} is required to render")

    started = time.time()
    work, out = Path(args.work).resolve(), Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    report = {
        "batch": b["id"],
        "engine": {"tts_model": os.environ.get("TTS_MODEL", ""), "model_revision": os.environ.get("TTS_MODEL_REVISION", ""),
                   "fork_commit": os.environ.get("VIBEVOICE_REF", ""), "asr_model": args.asr_model,
                   "speaker_encoder": "resemblyzer", "device": "cpu", "library_versions": versions()},
        "settings": {"prompt": textnorm.tts_prompt("<sentence>"), "cfg_scale": 1.3, "ddpm_steps": 10,
                     "seed_rounds": [list(s) for s in SEED_ROUNDS], "join_parts_of_words_le": 2,
                     "similarity_min_ge_5s": qc.SIM_LONG, "similarity_min_lt_5s": qc.SIM_SHORT,
                     "tail_max_db": qc.TAIL_MAX_DB, "tail_window_ms": int(qc.TAIL_WIN_S * 1000)},
        "voices": {}, "lines": [],
    }
    if os.environ.get("GITHUB_RUN_ID"):
        report["ci_run"] = (f"{os.environ.get('GITHUB_SERVER_URL')}/{os.environ.get('GITHUB_REPOSITORY')}"
                            f"/actions/runs/{os.environ['GITHUB_RUN_ID']}")
    failed = []
    for voice, gate in b["voices"].items():
        lines = [ln for ln in b["lines"] if ln["voice"] == voice]
        if not lines:
            continue
        lo, hi = qc.f0_range(gate["f0_target_hz"], gate["f0_tolerance_hz"])
        report["voices"][voice] = {"reference_sha256": sha256_file(Path(args.voices) / f"{voice}.wav"),
                                   "median_f0_hz": [lo, hi]}
        taken = render_voice(voice, gate, lines, args, work / voice)
        for ln in lines:
            passed = [t for t in taken[ln["id"]] if t["status"] == "pass"][: ln["takes"]]
            for t in passed:
                name = f"{ln['id']}_seed{t['seed']}"
                shutil.copyfile(t["final_path"], out / f"{name}.wav")
                mp3.encode(out / f"{name}.wav", out / f"{name}.mp3")
                t["files"] = [f"{name}.wav", f"{name}.mp3"]
                if t.get("cut_path"):
                    shutil.copyfile(t["cut_path"], out / f"{name}_cut.wav")
                    mp3.encode(out / f"{name}_cut.wav", out / f"{name}_cut.mp3")
                    t["files"] += [f"{name}_cut.wav", f"{name}_cut.mp3"]
            # The first passing take (its cut, when the line has one) is the
            # line's asset: the file social/facebook/assets/ uses.
            if passed and ln.get("asset"):
                (out / "assets").mkdir(exist_ok=True)
                shutil.copyfile(passed[0].get("cut_path") or passed[0]["final_path"], out / "assets" / ln["asset"])
            write_listen_takes(ln["id"], taken[ln["id"]], out)
            for t in taken[ln["id"]]:
                t.pop("final_path", None)
                t.pop("cut_path", None)
            said = ({"source_text": ln["source_text"], "tts_parts": ln["tts_parts"]}
                    if ln["tts_parts"] != ln["parts"] else {})
            report["lines"].append({"id": ln["id"], "voice": voice, "text": ln["text"], "parts": ln["parts"], **said,
                                    "seed_order": [s for r in ln["rounds"] for s in r],
                                    "takes_wanted": ln["takes"], "takes_passed": len(passed),
                                    "chosen_seeds": [t["seed"] for t in passed], "asset": ln.get("asset") if passed else None,
                                    "takes": taken[ln["id"]]})
            print(f"line {ln['id']}: {len(passed)}/{ln['takes']} passing take(s), seeds {[t['seed'] for t in passed]}")
            if not passed:
                failed.append(ln["id"])
    report["elapsed_s"] = round(time.time() - started)
    (out / "report.json").write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    if failed:
        print(f"::error::no take passed the gate for: {', '.join(failed)} (seeds {sum(SEED_ROUNDS, [])} tried)")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
