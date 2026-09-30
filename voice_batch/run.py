#!/usr/bin/env python3
"""Render, QC and install one category of a tutor's lines.

    python voice_batch/run.py --agent-root .agent --tutor tutor_001 --voice voice_a \
        --ref .agent/lms/team/voice_refs/voice_a_ref.wav --ref-sha256 <hex> \
        --category greetings --model-path <snapshot dir> --work $RUNNER_TEMP/vb

Rounds: seeds 11/22/33, then 44, then 55. After each round qc.py picks and
gates every line. A line that is not yet passing gets the next seed for
the sentences that lack a strictly passing take (all of its sentences if
each already has one and the stitched file still fails). A line still
failing after seed 55 is recorded as failed and its audio is not installed.

Render and QC run as separate processes so the TTS model (~12 GB) and the
ASR/speaker models are never resident together. Passing files are copied
beside their scripts in the agent checkout and recorded in
<tutor dir>/<voice>_manifest.<category>.json. Logs ids and numbers only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from importlib import metadata
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from lines import build_lines  # noqa: E402

SEED_ROUNDS = ([11, 22, 33], [44], [55])


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def versions() -> dict:
    out = {"python": sys.version.split()[0]}
    for pkg in ("torch", "transformers", "vibevoice", "faster-whisper", "ctranslate2", "resemblyzer",
                "librosa", "numpy", "soundfile"):
        try:
            out[pkg] = metadata.version(pkg)
        except metadata.PackageNotFoundError:
            pass
    return out


def safe(key: str) -> str:
    return key.replace("/", "_").replace("#", "_s")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--agent-root", required=True)
    ap.add_argument("--tutor", required=True)
    ap.add_argument("--voice", required=True)
    ap.add_argument("--ref", required=True)
    ap.add_argument("--ref-sha256", required=True)
    ap.add_argument("--category", required=True)
    ap.add_argument("--model-path", required=True)
    ap.add_argument("--work", required=True)
    ap.add_argument("--asr-model", default=os.environ.get("ASR_MODEL", "small.en"))
    ap.add_argument("--lines", default="", help="optional comma-separated line ids to limit the run to")
    args = ap.parse_args()
    only = {x for x in args.lines.split(",") if x}

    agent = Path(args.agent_root).resolve()
    ref = Path(args.ref).resolve()
    if sha256_file(ref) != args.ref_sha256:
        print("::error::reference sha256 does not match the batch; refusing to render")
        return 1
    scripts = agent / "lms/team/scripts"
    tutor_rel = f"lms/team/tutors/CAPS/{args.tutor}"
    # One manifest per category so parallel category jobs never touch the same
    # file; merge_manifest.py folds them into <voice>_manifest.json afterwards.
    manifest_path = agent / tutor_rel / f"{args.voice}_manifest.{args.category}.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    done = {e["id"]: e for e in manifest.get("lines", [])}

    items = []
    for it in build_lines(agent, args.tutor, [args.category]):
        if only and it["id"] not in only:
            continue
        prev = done.get(it["id"])
        if (prev and prev.get("text_sha256") == it["text_sha256"]
                and manifest.get("reference", {}).get("sha256") == args.ref_sha256
                and (agent / it["file"]).exists() and sha256_file(agent / it["file"]) == prev.get("sha256")):
            print(f"line {it['id']}: already rendered for this text and reference, skipping")
            continue
        items.append(it)
    if not items:
        print(f"category {args.category}: nothing to render")
        return 0

    work = Path(args.work).resolve() / args.category
    work.mkdir(parents=True, exist_ok=True)
    (work / "lines.json").write_text(json.dumps(items, indent=1, ensure_ascii=False), encoding="utf-8")
    index_path = work / "takes_index.json"
    index = json.loads(index_path.read_text(encoding="utf-8")) if index_path.exists() else {}
    text_of = {f"{it['id']}#{k}": t for it in items for k, t in enumerate(it["render_text"], 1)}
    pending = set(text_of)
    results: list[dict] = []
    started = time.time()

    for rnd, seeds in enumerate(SEED_ROUNDS, 1):
        jobs = []
        for key in sorted(pending):
            for seed in seeds:
                out = str(work / "takes" / f"{safe(key)}_seed{seed}.wav")
                index[out] = {"key": key, "seed": seed}
                jobs.append({"key": key, "text": text_of[key], "seed": seed, "out": out})
        index_path.write_text(json.dumps(index, indent=1), encoding="utf-8")
        (work / "jobs.json").write_text(json.dumps(jobs, ensure_ascii=False), encoding="utf-8")
        print(f"::group::{args.category} round {rnd}: seeds {seeds}, {len(pending)} sentence(s)", flush=True)
        subprocess.run([sys.executable, str(HERE / "render_takes.py"), "--jobs", str(work / "jobs.json"),
                        "--ref", str(ref), "--scripts-dir", str(scripts), "--model-path", args.model_path],
                       check=True)
        subprocess.run([sys.executable, str(HERE / "qc.py"), "--work", str(work), "--ref", str(ref),
                        "--scripts-dir", str(scripts), "--asr-model", args.asr_model], check=True)
        print("::endgroup::", flush=True)
        results = json.loads((work / "results.json").read_text(encoding="utf-8"))
        pending = set()
        for r in results:
            if r["status"] == "pass":
                continue
            lacking = [x["key"] for x in r.get("lacking", [])]
            if r["status"] == "fail" and not lacking:
                lacking = [k for k in text_of if k.split("#")[0] == r["id"]]
            pending.update(lacking)
        if not pending:
            break

    # Install passing lines, update the manifest.
    by_id = {it["id"]: it for it in items}
    ref_rel = str(ref.relative_to(agent)) if ref.is_relative_to(agent) else ref.name
    manifest.update({
        "tutor": args.tutor, "voice": args.voice, "category": args.category,
        "reference": {"path": ref_rel, "sha256": args.ref_sha256},
        "engine": {
            "tts_model": os.environ.get("TTS_MODEL", ""),
            "model_snapshot": os.environ.get("TTS_MODEL_REVISION", Path(args.model_path).name),
            "fork": os.environ.get("VIBEVOICE_REPO", ""),
            "fork_commit": os.environ.get("VIBEVOICE_REF", ""),
            "asr_model": args.asr_model, "speaker_encoder": "resemblyzer", "device": "cpu",
            "library_versions": versions(),
        },
        "settings": {
            "prompt": "Speaker 1: <sentence>", "cfg_scale": 1.3, "ddpm_steps": 10,
            "seed_rounds": [list(s) for s in SEED_ROUNDS], "per_sentence": True,
            "pause_ms": [280, 320], "fade_ms": 12, "trim_top_db": 40,
            "loudness_dbfs": -20.0, "sample_rate": 24000, "channels": 1, "subtype": "PCM_16",
            "selection": "word-exact takes; median F0 closest to 102 Hz, then fewest upward swings, then higher similarity",
            "gate": {"median_f0_hz": [94, 110], "similarity_min_ge_5s": 0.88, "similarity_min_lt_5s": 0.83,
                     "asr": "word-exact"},
        },
        "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    })
    if os.environ.get("GITHUB_RUN_ID"):
        manifest["ci_run"] = f"{os.environ.get('GITHUB_SERVER_URL')}/{os.environ.get('GITHUB_REPOSITORY')}/actions/runs/{os.environ['GITHUB_RUN_ID']}"
    lines = {e["id"]: e for e in manifest.get("lines", [])}
    failed = {e["id"]: e for e in manifest.get("failed", [])}
    for r in results:
        it = by_id[r["id"]]
        if r["status"] == "pass":
            dst = agent / it["file"]
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(r["final_path"], dst)
            lines[it["id"]] = {
                "id": it["id"], "category": it["category"], "text": it["text"], "text_sha256": it["text_sha256"],
                "script": it["script"], "file": it["file"], "duration": r["duration_s"], "seeds": r["seeds"],
                "median_f0": r["median_f0_hz"], "similarity": r["similarity"], "asr_match": r["asr_match"],
                "similarity_threshold": r["similarity_threshold"], "upward_swings": r["upward_swings"],
                "rms_dbfs": r["rms_dbfs"], "peak": r["peak"], "pauses_ms": r["pauses_ms"], "sha256": r["sha256"],
                "sentences": [dict(t, text=s) for t, s in zip(r["takes"], it["sentences"])],
                "seeds_tried": r["seeds_tried"],
            }
            failed.pop(it["id"], None)
        else:
            failed[it["id"]] = {
                "id": it["id"], "category": it["category"], "file_not_committed": it["file"],
                "status": r["status"], "seeds_tried": r["seeds_tried"],
                **{k: r[k] for k in ("duration_s", "median_f0_hz", "similarity", "similarity_threshold",
                                     "asr_match", "gate") if k in r},
            }
            lines.pop(it["id"], None)
    order = {it["id"]: n for n, it in enumerate(build_lines(agent, args.tutor, ["acknowledgements", "greetings", "signoffs", "teaching"]))}
    manifest["lines"] = sorted(lines.values(), key=lambda e: order.get(e["id"], 1e9))
    manifest["failed"] = sorted(failed.values(), key=lambda e: order.get(e["id"], 1e9))
    manifest_path.write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    passed = sum(r["status"] == "pass" for r in results)
    print(f"category {args.category}: {passed}/{len(results)} line(s) passed in {time.time() - started:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
