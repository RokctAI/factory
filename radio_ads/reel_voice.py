#!/usr/bin/env python3
"""Render the Reel's voice-over lines with voice_batch's per-sentence
renderer and QC gate, so they meet the tutor voices' quality bar.

    python radio_ads/reel_voice.py radio_ads/reel_voices/<batch>.json --validate
    python radio_ads/reel_voice.py radio_ads/reel_voices/<batch>.json \
        --voices radio_ads/voices --scripts-dir <agent>/lms/team/scripts \
        --model-path <pinned snapshot dir> --work $RUNNER_TEMP/reel --out radio_ads/out/<batch id>

A batch lists lines ({"id", "voice", "text", optional "takes", default 1})
and, per voice, the F0 gate ("f0_target_hz", "f0_tolerance_hz"). A take is
one seed's rendering of a whole line:

Render : textnorm.split_sentences, then any sentence of two words or fewer
         joins its neighbour (a one-word sentence such as "Begin." comes
         out as "Mm-hmm"); voice_batch/render_takes.py renders each part as
         textnorm.tts_prompt (part + " ...") at cfg 1.3, 10 DDPM steps.
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
import qc  # noqa: E402
import textnorm  # noqa: E402
from run import SEED_ROUNDS, safe, sha256_file, versions  # noqa: E402

ID_RE = r"[a-z][a-z0-9_]{0,40}"
MAX_TAKES = sum(len(r) for r in SEED_ROUNDS)


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


def load_batch(path: Path) -> dict:
    b = json.loads(path.read_text(encoding="utf-8"))
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
        ln["parts"] = render_parts(ln["text"])
    if not seen:
        raise ValueError("batch has no lines")
    return b


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
        for text, p in zip(t["parts"], t["paths"]):
            if not Path(p).exists():
                parts.append({"missing": True})
                continue
            m = meter.measure(p, text)
            best, tier = qc.pick([m], target, tol)
            parts.append({"tier": tier, "median_f0_hz": m["f0"], "similarity": m["res"], "asr_word_errors": m["err"],
                          "tail_db": m["tail_db"], "duration_s": m["dur"]})
            if best is not None:
                x, sr = sf.read(p)
                assert sr == qc.SR, "unexpected sample rate"
                arrays.append(x)
        r["parts"] = parts
        if len(arrays) != len(t["parts"]):
            r["reason"] = "a sentence has no word-exact take with a clean tail"
            results.append(r)
            print(f"take {t['id']} seed{t['seed']}: fail ({r['reason']})", flush=True)
            continue
        y, pauses = qc.stitch(arrays)
        dst = Path(t["final"])
        dst.parent.mkdir(parents=True, exist_ok=True)
        sf.write(str(dst), rv.normalise(y).astype(np.float32), qc.SR, subtype="PCM_16")
        fm = meter.measure(dst, t["text"])
        dur = fm["dur"]
        thr = qc.sim_threshold(dur)
        gate = {"f0": lo <= fm["f0"] <= hi, "similarity": fm["res"] >= thr, "asr": fm["err"] == 0,
                "tail": qc.tail_ok(fm["tail_db"])}
        r.update({"status": "pass" if all(gate.values()) else "fail", "gate": gate, "final_path": str(dst),
                  "duration_s": dur, "median_f0_hz": fm["f0"], "similarity": fm["res"],
                  "similarity_threshold": thr, "asr_word_errors": fm["err"], "asr_transcript": fm["transcript"],
                  "tail_db": fm["tail_db"], "pauses_ms": pauses, "sha256": sha256_file(dst)})
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
    for rnd, seeds in enumerate(SEED_ROUNDS, 1):
        todo = [ln for ln in lines if sum(t["status"] == "pass" for t in taken[ln["id"]]) < ln["takes"]]
        if not todo:
            break
        jobs, takes = [], []
        for ln in todo:
            for seed in seeds:
                paths = []
                for k, part in enumerate(ln["parts"], 1):
                    out = str(work / "takes" / f"{safe(ln['id'] + '#' + str(k))}_seed{seed}.wav")
                    jobs.append({"key": f"{ln['id']}#{k}", "text": part, "seed": seed, "out": out})
                    paths.append(out)
                takes.append({"id": ln["id"], "seed": seed, "text": ln["text"], "parts": ln["parts"], "paths": paths,
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
            for t in taken[ln["id"]]:
                t.pop("final_path", None)
            report["lines"].append({"id": ln["id"], "voice": voice, "text": ln["text"], "parts": ln["parts"],
                                    "takes_wanted": ln["takes"], "takes_passed": len(passed),
                                    "chosen_seeds": [t["seed"] for t in passed], "takes": taken[ln["id"]]})
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
