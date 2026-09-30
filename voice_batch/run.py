#!/usr/bin/env python3
"""Render, QC and install one category of a tutor's lines, or one shard of
the Grades R-3 pack lines.

    python voice_batch/run.py --agent-root .agent --tutor tutor_001 --voice voice_a \
        --ref .agent/lms/team/voice_refs/voice_a_ref.wav --ref-sha256 <hex> \
        --category greetings --model-path <snapshot dir> --work $RUNNER_TEMP/vb

    python voice_batch/run.py --kind r3 --batch voice_batches/inbox/<r3 batch>.json --shard 3/8 \
        --agent-root .agent --voice <voice> --ref .agent/<ref> --ref-sha256 <hex> \
        --model-path <snapshot dir> --work $RUNNER_TEMP/vb [--f0-target 102 --f0-tolerance 8]

Rounds: seeds 11/22/33, then 44, then 55. After each round qc.py picks and
gates every line. A line that is not yet passing gets the next seed for
the sentences that lack a strictly passing take (all of its sentences if
each already has one and the stitched file still fails). A line still
failing after seed 55 is recorded as failed and its audio is not installed.

Render and QC run as separate processes so the TTS model (~12 GB) and the
ASR/speaker models are never resident together. Tutor lines: passing files
are copied beside their scripts in the agent checkout and recorded in
<tutor dir>/<voice>_manifest.<category>.json. R-3 lines: passing files are
encoded to <key>.mp3 in lms/dart/templates/assets/r3_packs/audio/ and
recorded in r3_manifest.<voice>.partNN.json beside them (merge_manifest.py
folds the parts into r3_manifest.<voice>.json). Logs ids and numbers only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from importlib import metadata
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import pronunciations  # noqa: E402
from lines import build_lines  # noqa: E402
from qc import F0_TOLERANCE, TARGET_F0, f0_range  # noqa: E402

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




def load_json(p: Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def render_rounds(items: list[dict], work: Path, ref: Path, scripts: Path, args, label: str) -> list[dict]:
    """Seed rounds of render + QC until every line passes or the seeds run out."""
    work.mkdir(parents=True, exist_ok=True)
    (work / "lines.json").write_text(json.dumps(items, indent=1, ensure_ascii=False), encoding="utf-8")
    index_path = work / "takes_index.json"
    index = json.loads(index_path.read_text(encoding="utf-8")) if index_path.exists() else {}
    text_of = {f"{it['id']}#{k}": t for it in items for k, t in enumerate(it["render_text"], 1)}
    pending = set(text_of)
    results: list[dict] = []
    for rnd, seeds in enumerate(SEED_ROUNDS, 1):
        jobs = []
        for key in sorted(pending):
            for seed in seeds:
                out = str(work / "takes" / f"{safe(key)}_seed{seed}.wav")
                index[out] = {"key": key, "seed": seed}
                jobs.append({"key": key, "text": text_of[key], "seed": seed, "out": out})
        index_path.write_text(json.dumps(index, indent=1), encoding="utf-8")
        (work / "jobs.json").write_text(json.dumps(jobs, ensure_ascii=False), encoding="utf-8")
        print(f"::group::{label} round {rnd}: seeds {seeds}, {len(pending)} sentence(s)", flush=True)
        subprocess.run([sys.executable, str(HERE / "render_takes.py"), "--jobs", str(work / "jobs.json"),
                        "--ref", str(ref), "--scripts-dir", str(scripts), "--model-path", args.model_path],
                       check=True)
        subprocess.run([sys.executable, str(HERE / "qc.py"), "--work", str(work), "--ref", str(ref),
                        "--scripts-dir", str(scripts), "--asr-model", args.asr_model,
                        "--f0-target", str(args.f0_target), "--f0-tolerance", str(args.f0_tolerance),
                        "--language", args.language], check=True)
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
    return results


def run_header(args, ref: Path, agent: Path) -> dict:
    lo, hi = f0_range(args.f0_target, args.f0_tolerance)
    ref_rel = str(ref.relative_to(agent)) if ref.is_relative_to(agent) else ref.name
    head = {
        "voice": args.voice,
        "reference": {"path": ref_rel, "sha256": args.ref_sha256},
        "engine": {
            "tts_model": os.environ.get("TTS_MODEL", ""),
            "model_snapshot": os.environ.get("TTS_MODEL_REVISION", Path(args.model_path).name),
            "fork": os.environ.get("VIBEVOICE_REPO", ""),
            "fork_commit": os.environ.get("VIBEVOICE_REF", ""),
            "asr_model": args.asr_model, "asr_language": args.language,
            "speaker_encoder": "resemblyzer", "device": "cpu",
            "library_versions": versions(),
        },
        "settings": {
            "prompt": "Speaker 1: <sentence>", "cfg_scale": 1.3, "ddpm_steps": 10,
            "seed_rounds": [list(s) for s in SEED_ROUNDS], "per_sentence": True,
            "pause_ms": [280, 320], "fade_ms": 12, "trim_top_db": 40,
            "loudness_dbfs": -20.0, "sample_rate": 24000, "channels": 1, "subtype": "PCM_16",
            "selection": f"word-exact takes; median F0 closest to {args.f0_target:g} Hz, then fewest upward swings, then higher similarity",
            "gate": {"median_f0_hz": [round(lo, 2), round(hi, 2)], "f0_target_hz": args.f0_target,
                     "f0_tolerance_hz": args.f0_tolerance,
                     "similarity_min_ge_5s": 0.88, "similarity_min_lt_5s": 0.83, "asr": "word-exact"},
        },
        "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    if os.environ.get("GITHUB_RUN_ID"):
        head["ci_run"] = f"{os.environ.get('GITHUB_SERVER_URL')}/{os.environ.get('GITHUB_REPOSITORY')}/actions/runs/{os.environ['GITHUB_RUN_ID']}"
    return head


def run_id() -> dict:
    """Per-entry CI run id, so a later step can count what this run did."""
    return {"ci_run_id": os.environ["GITHUB_RUN_ID"]} if os.environ.get("GITHUB_RUN_ID") else {}


def score_fields(r: dict) -> dict:
    return {**run_id(), "duration": r["duration_s"], "seeds": r["seeds"], "median_f0": r["median_f0_hz"],
            "similarity": r["similarity"], "asr_match": r["asr_match"],
            "similarity_threshold": r["similarity_threshold"], "upward_swings": r["upward_swings"],
            "rms_dbfs": r["rms_dbfs"], "peak": r["peak"], "pauses_ms": r["pauses_ms"]}


def failed_fields(r: dict) -> dict:
    return {**run_id(), "status": r["status"], "seeds_tried": r["seeds_tried"],
            **{k: r[k] for k in ("duration_s", "median_f0_hz", "similarity", "similarity_threshold",
                                 "asr_match", "gate") if k in r}}


def unchanged(prev: dict | None, it: dict, agent: Path, ref_sha: str, extra: tuple = ()) -> bool:
    return bool(prev and prev.get("text_sha256") == it["text_sha256"]
                and all(prev.get(k) == it[k] for k in extra)
                and prev.get("ref_sha256", ref_sha) == ref_sha
                and (agent / it["file"]).exists() and sha256_file(agent / it["file"]) == prev.get("sha256"))


def run_tutor(args, agent: Path, ref: Path, scripts: Path) -> int:
    only = {x for x in args.lines.split(",") if x}
    tutor_rel = f"lms/team/tutors/CAPS/{args.tutor}"
    # One manifest per category so parallel category jobs never touch the same
    # file; merge_manifest.py folds them into <voice>_manifest.json afterwards.
    manifest_path = agent / tutor_rel / f"{args.voice}_manifest.{args.category}.json"
    manifest = load_json(manifest_path)
    done = {e["id"]: e for e in manifest.get("lines", [])}
    same_ref = manifest.get("reference", {}).get("sha256") == args.ref_sha256
    pron = pronunciations.load()
    try:
        built = [it for it in build_lines(agent, args.tutor, [args.category], pron) if not only or it["id"] in only]
    except pronunciations.PronunciationError as exc:
        print(f"::error::{exc}")
        return 1
    errs = pronunciations.check_ambiguous(built, pron)
    for e in errs:
        print(f"::error::{e}")
    if errs:
        return 1
    items = []
    for it in built:
        prev = done.get(it["id"])
        # An entry from before pronunciations has no render_sha256: it was
        # rendered from the display text, so it is current unless a
        # pronunciation now changes what is spoken.
        legacy = prev is not None and "render_sha256" not in prev and "tts_text" not in it
        same_render = legacy or (prev or {}).get("render_sha256") == it["render_sha256"]
        if same_ref and same_render and unchanged(prev, it, agent, args.ref_sha256):
            print(f"line {it['id']}: already rendered for this text and reference, skipping")
            continue
        items.append(it)
    if not items:
        print(f"category {args.category}: nothing to render")
        return 0

    started = time.time()
    results = render_rounds(items, Path(args.work).resolve() / args.category, ref, scripts, args, args.category)
    by_id = {it["id"]: it for it in items}
    manifest.update({"tutor": args.tutor, "category": args.category, **run_header(args, ref, agent)})
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
                "render_sha256": it["render_sha256"],
                **({"tts_text": it["tts_text"], "pronounced": it["pronounced"], "needs_listen": True}
                   if "tts_text" in it else {}),
                "script": it["script"], "file": it["file"], **score_fields(r), "sha256": r["sha256"],
                "sentences": [dict(t, text=s) for t, s in zip(r["takes"], it["sentences"])],
                "seeds_tried": r["seeds_tried"],
            }
            failed.pop(it["id"], None)
        else:
            failed[it["id"]] = {"id": it["id"], "category": it["category"], "file_not_committed": it["file"],
                                **failed_fields(r)}
            lines.pop(it["id"], None)
    order = {it["id"]: n for n, it in enumerate(build_lines(agent, args.tutor, ["acknowledgements", "greetings", "signoffs", "teaching"]))}
    manifest["lines"] = sorted(lines.values(), key=lambda e: order.get(e["id"], 1e9))
    manifest["failed"] = sorted(failed.values(), key=lambda e: order.get(e["id"], 1e9))
    manifest_path.write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    passed = sum(r["status"] == "pass" for r in results)
    print(f"category {args.category}: {passed}/{len(results)} line(s) passed in {time.time() - started:.0f}s")
    return 0


def run_r3(args, agent: Path, ref: Path, scripts: Path) -> int:
    import mp3
    from batch import load_batch
    from r3_lines import AUDIO_DIR, build_r3_lines, shard

    b = load_batch(args.batch, Path(args.factory_root).resolve())
    k, n = (int(x) for x in args.shard.split("/"))
    common = dict(factory_root=Path(args.factory_root).resolve(), packs=b.get("packs"),
                  locale=b["locale"], agent_root=agent)
    items_all = build_r3_lines(only=b.get("lines"), **common)
    mine = shard(items_all, k, n)
    audio = agent / AUDIO_DIR
    audio.mkdir(parents=True, exist_ok=True)
    merged = load_json(audio / f"r3_manifest.{args.voice}.json")
    part_path = audio / f"r3_manifest.{args.voice}.part{k:02d}.json"
    part = load_json(part_path)
    done = {e["id"]: e for m in (merged, part) for e in m.get("lines", [])}
    label = f"r3 shard {k}/{n}"
    items = []
    for it in mine:
        if unchanged(done.get(it["id"]), it, agent, args.ref_sha256, ("render_sha256",)):
            print(f"line {it['id']}: already rendered for this text and reference, skipping")
            continue
        items.append(it)
    print(f"{label}: {len(mine)} line(s), {len(items)} to render "
          f"({sum(it['needs_listen'] for it in items)} respelled for phonics)")
    if not items:
        return 0

    started = time.time()
    results = render_rounds(items, Path(args.work).resolve() / f"r3_shard{k:02d}", ref, scripts, args, label)
    by_id = {it["id"]: it for it in items}
    part.update({"kind": "r3", "locale": b["locale"], "shard": f"{k}/{n}", **run_header(args, ref, agent)})
    part["settings"]["output"] = {"format": "mp3", "bitrate_kbps": mp3.BITRATE_KBPS, "sample_rate": mp3.SAMPLE_RATE,
                                  "channels": 1, "dir": AUDIO_DIR}
    lines = {e["id"]: e for e in part.get("lines", [])}
    failed = {e["id"]: e for e in part.get("failed", [])}
    for r in results:
        it = by_id[r["id"]]
        base = {"id": it["id"], "key": it["key"], "locale": it["locale"], "category": "r3",
                "needs_listen": it["needs_listen"]}
        if r["status"] == "pass":
            dst = agent / it["file"]
            encoder = mp3.encode(r["final_path"], dst)
            lines[it["id"]] = {
                **base, "text": it["text"], **({"tts_text": it["tts_text"]} if "tts_text" in it else {}),
                **({"pronounced": it["pronounced"]} if it.get("pronounced") else {}),
                "text_sha256": it["text_sha256"], "render_sha256": it["render_sha256"], "script": it["script"],
                "file": it["file"], **score_fields(r), "sha256": sha256_file(dst), "wav_sha256": r["sha256"],
                "encoder": encoder, "ref_sha256": args.ref_sha256,
                "sentences": [dict(t, text=s) for t, s in zip(r["takes"], it["sentences"])],
                "seeds_tried": r["seeds_tried"],
            }
            failed.pop(it["id"], None)
        else:
            failed[it["id"]] = {**base, "file_not_committed": it["file"], **failed_fields(r)}
            lines.pop(it["id"], None)
    order = {it["id"]: i for i, it in enumerate(build_r3_lines(**common))}
    part["lines"] = sorted(lines.values(), key=lambda e: order.get(e["id"], 1e9))
    part["failed"] = sorted(failed.values(), key=lambda e: order.get(e["id"], 1e9))
    part_path.write_text(json.dumps(part, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    passed = sum(r["status"] == "pass" for r in results)
    print(f"{label}: {passed}/{len(results)} line(s) passed in {time.time() - started:.0f}s")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kind", choices=("tutor", "r3"), default="tutor")
    ap.add_argument("--agent-root", required=True)
    ap.add_argument("--voice", required=True)
    ap.add_argument("--ref", required=True)
    ap.add_argument("--ref-sha256", required=True)
    ap.add_argument("--model-path", required=True)
    ap.add_argument("--work", required=True)
    ap.add_argument("--asr-model", default=os.environ.get("ASR_MODEL", "small.en"))
    ap.add_argument("--language", default="en", help="ASR language")
    ap.add_argument("--f0-target", type=float, default=TARGET_F0)
    ap.add_argument("--f0-tolerance", type=float, default=F0_TOLERANCE)
    # tutor
    ap.add_argument("--tutor")
    ap.add_argument("--category")
    ap.add_argument("--lines", default="", help="tutor: optional comma-separated line ids to limit the run to")
    # r3
    ap.add_argument("--batch", help="r3: the batch JSON (packs / lines / locale come from it)")
    ap.add_argument("--shard", default="1/1", help="r3: k/n, this job's contiguous share of the lines")
    ap.add_argument("--factory-root", default=str(HERE.parent))
    args = ap.parse_args()
    if args.kind == "tutor" and not (args.tutor and args.category):
        ap.error("--tutor and --category are required for kind tutor")
    if args.kind == "r3" and not (args.batch and re.fullmatch(r"[1-9]\d*/[1-9]\d*", args.shard)):
        ap.error("--batch and --shard k/n are required for kind r3")

    agent = Path(args.agent_root).resolve()
    ref = Path(args.ref).resolve()
    if sha256_file(ref) != args.ref_sha256:
        print("::error::reference sha256 does not match the batch; refusing to render")
        return 1
    scripts = agent / "lms/team/scripts"
    if args.kind == "r3":
        return run_r3(args, agent, ref, scripts)
    return run_tutor(args, agent, ref, scripts)


if __name__ == "__main__":
    sys.exit(main())
