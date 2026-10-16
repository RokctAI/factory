#!/usr/bin/env python3
"""A/B listening test: does rendering a whole line in one go sound less flat
than the batch method (one sentence at a time, the take nearest the target
pitch with the fewest upward swings)?

    python voice_batch/ab_style.py --agent-root .agent --voice-persona assistant_005 \
        --r3 <key>,<key> [--lesson <rel>] --model-path <snapshot> --out DIR

B renders each line's whole text as ONE prompt on seeds 11, 22 and 33, with
no take selection, so the listener hears the model's own phrasing across
sentences. A is the line as the batch rendered it (passed in by the
workflow from the agent branch or the stems pre-release). Writes
DIR/<n>-<key>-B<seed>.mp3 (with the batch's 200 ms lead-in) and
DIR/ab.json (keys, seeds, durations; no text). Logs keys and numbers only.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

SEEDS = (11, 22, 33)


def texts(args) -> list[tuple[str, str]]:
    """[(key, spoken text)] for the requested lines, as the batch speaks them."""
    import pronunciations
    from textnorm import speak_text
    out = []
    keys = [k for k in args.r3.split(",") if k]
    if keys:
        from r3_lines import build_r3_lines
        by_key = {it["key"]: it for it in build_r3_lines(only=keys, agent_root=Path(args.agent_root))}
        out += [(k, " ".join(by_key[k]["render_text"])) for k in keys if k in by_key]
    if args.lesson:
        import lesson_lines as L
        lr = Path(args.lessons_root)
        folder = L.curriculum_root(lr) / args.lesson
        r = L.roles(lr, folder)
        for key, _src, text in L.part_texts(lr, folder, r, args.voice_persona):
            if key == "nervous":
                parts = [pronunciations.apply(s, pronunciations.load())[1] for s in
                         __import__("textnorm").split_sentences(text)]
                out.append((f"{args.lesson.rsplit('/', 1)[1]}.nervous", " ".join(speak_text(p) for p in parts)))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--agent-root", required=True)
    ap.add_argument("--lessons-root", default=os.environ.get("LESSONS_ROOT", ""))
    ap.add_argument("--voice-persona", required=True)
    ap.add_argument("--r3", default="")
    ap.add_argument("--lesson", default="")
    ap.add_argument("--model-path", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    import lesson_lines as L
    v = L.load_voices()[args.voice_persona]
    agent = Path(args.agent_root).resolve()
    ref = agent / v["ref_path"]
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    work = out / "_work"
    lines = texts(args)
    jobs = [{"key": f"{n}-{key}", "text": text, "seed": s, "out": str(work / f"{n}-{key}-B{s}.wav")}
            for n, (key, text) in enumerate(lines, 1) for s in SEEDS]
    (work).mkdir(exist_ok=True)
    (work / "jobs.json").write_text(json.dumps(jobs), encoding="utf-8")
    subprocess.run([sys.executable, str(HERE / "render_takes.py"), "--jobs", str(work / "jobs.json"),
                    "--ref", str(ref), "--scripts-dir", str(agent / "lms/team/scripts"),
                    "--model-path", args.model_path], check=True)
    import mp3
    import numpy as np
    import soundfile as sf
    report = []
    for j in jobs:
        wav = Path(j["out"])
        if not wav.is_file():
            report.append({"file": None, "key": j["key"], "seed": j["seed"], "status": "render failed"})
            continue
        # The batch's 200 ms lead-in, without ffmpeg (hosted runners lack it).
        x, sr = sf.read(str(wav), dtype="float32", always_2d=True)
        x = x.mean(axis=1)
        padded = wav.with_name(wav.stem + ".lead.wav")
        sf.write(str(padded), np.concatenate([np.zeros(sr // 5, dtype="float32"), x]), sr, subtype="PCM_16")
        dst = out / f"{j['key']}-B{j['seed']}.mp3"
        mp3.encode(padded, dst)
        report.append({"file": dst.name, "key": j["key"], "seed": j["seed"]})
        print(f"{dst.name}")
    shutil.rmtree(work, ignore_errors=True)
    (out / "ab.json").write_text(json.dumps({"voice": v["voice"], "method_B": "whole line, one prompt, no take "
                                             "selection", "takes": report}, indent=1) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
