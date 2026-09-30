#!/usr/bin/env python3
"""Render sentence takes, one at a time, with fixed seeds.

    python voice_batch/render_takes.py --jobs jobs.json --ref REF.wav \
        --scripts-dir <agent>/lms/team/scripts --model-path <local snapshot dir>

jobs.json: [{"key": "<line id>#<n>", "text": "...", "seed": 11, "out": "takes/..wav"}]
Uses the agent repo's render_voices.Renderer (VibeVoice, CPU, cfg 1.3,
10 DDPM steps, 'Speaker 1:' prompt) and its -20 dBFS / 24 kHz / PCM_16
writer, so CI renders exactly like the local pipeline. Logs ids, seeds and
timings only; never the text.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
import time
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", required=True)
    ap.add_argument("--ref", required=True)
    ap.add_argument("--scripts-dir", required=True)
    ap.add_argument("--model-path", required=True)
    args = ap.parse_args()

    jobs = [j for j in json.loads(Path(args.jobs).read_text(encoding="utf-8")) if not Path(j["out"]).exists()]
    print(f"{len(jobs)} take(s) to render", flush=True)
    if not jobs:
        return 0
    sys.path.insert(0, args.scripts_dir)
    import numpy as np
    import torch
    import render_voices as rv

    r = rv.Renderer(args.model_path, "cpu", rv.DEFAULT_DDPM_STEPS, rv.DEFAULT_CFG_SCALE)
    r.load()
    ref = Path(args.ref)
    failures = 0
    for n, j in enumerate(jobs, 1):
        seed = int(j["seed"])
        torch.manual_seed(seed); np.random.seed(seed); random.seed(seed)
        t0 = time.time()
        try:
            audio = r.render(j["text"], ref)
            out = Path(j["out"]); out.parent.mkdir(parents=True, exist_ok=True)
            tmp = out.with_suffix(".part.wav")
            dur = rv.write_wav(tmp, rv.normalise(audio))
            tmp.rename(out)
        except Exception as exc:  # noqa: BLE001 - one bad take must not stop the batch
            failures += 1
            print(f"[{n}/{len(jobs)}] {j['key']} seed{seed} FAILED ({type(exc).__name__})", flush=True)
            continue
        print(f"[{n}/{len(jobs)}] {j['key']} seed{seed} {dur:.2f}s audio, {time.time() - t0:.0f}s wall", flush=True)
    return 0 if failures < len(jobs) else 1


if __name__ == "__main__":
    sys.exit(main())
