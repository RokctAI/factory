#!/usr/bin/env python3
"""Prove rokct-media renders exactly what voice_batch renders.

Step 2 of the one-engine move: before lesson audio switches to rokct-media
(RokctAI/The-Rokct-Protocol core/utils/rokct_media), the same lines are
rendered and gated by both, on the same seeds, and every number is
compared. Nothing is written anywhere but the work folder; logs carry ids,
seeds, hashes and numbers only, never line text.

    # text only, no model: every lesson part of every speaker, both ways
    python voice_batch/ci/media_parity.py text --lessons-root _lessons

    # one voice: render + gate a fixed set of test lines with both engines
    python voice_batch/ci/media_parity.py audio --persona tutor_001 \
        --voice-root .voices --scripts-dir .agent/lms/team/scripts \
        --model-path <snapshot> --work $RUNNER_TEMP/parity [--seeds 11,22]

Pass = the same sentences, render text and ASR wildcards for every line
(text); the same take bytes, the same chosen seeds, the same gate verdicts
and the same final clip bytes (audio). Exit 1 on any difference.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

# Generic test lines, no lesson content and no names. Between them they
# cover what changed since rokct-media was cut: a short sentence that joins
# its neighbour, SA split thousands, a percentage, a countdown, -ise/-ize.
TEST_LINES = [
    ("parity/01", "Yes! Let us look at the next step together. Write the working "
                  "down neatly before you check your answer."),
    ("parity/02", "A deposit of R1 200 is twelve percent of the price, so organise "
                  "your notes first. We start in 3... 2... 1..."),
]
# What the gate reports and the comparison checks, per line.
LINE_KEYS = ("status", "gate", "seeds", "sha256", "duration_s", "median_f0_hz", "similarity",
             "asr_word_errors", "tail_db", "pauses_ms", "near_miss_sentences", "asr_lowered",
             "similarity_lowered", "checks")
TEXT_KEYS = ("text", "sentences", "render_text", "sentence_wild", "asr_text", "asr_wild",
             "pronounced", "render_sha256", "text_sha256", "tts_text")


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def both_fields(id_: str, text: str, pron: dict, names=()) -> tuple[dict, dict]:
    from lines import pronounced_fields as old
    from rokct_media.speech.plan import pronounced_fields as new
    return old(id_, text, pron, names), new(id_, text, pron, names)


def text_diff(a: dict, b: dict) -> list[str]:
    return [k for k in TEXT_KEYS if a.get(k) != b.get(k)]


# ------------------------------------------------------------------ text

def cmd_text(args) -> int:
    import lesson_lines as L
    import pronunciations
    from rokct_media.text import norm as new_norm
    import textnorm as old_norm

    lessons_root = Path(args.lessons_root).resolve()
    pron = pronunciations.load()
    lessons = parts = 0
    bad: list[tuple[str, str, list[str]]] = []
    for folder in L.discover(lessons_root):
        try:
            r = L.roles(lessons_root, folder)
        except Exception:  # noqa: BLE001 - a lesson the renderer cannot place is not a parity question
            continue
        lessons += 1
        for persona in {r["first"], r["second"], r["host"]} - {None}:
            for key, _source, text in L.part_texts(lessons_root, folder, r, persona):
                parts += 1
                id_ = f"{r['rel']}#{persona}/{key}"
                try:
                    a, b = both_fields(id_, text, pron)
                except Exception as exc:  # noqa: BLE001
                    bad.append((id_, "error", [type(exc).__name__]))
                    continue
                diff = text_diff(a, b)
                for s in a["sentences"]:
                    if old_norm.norm_words(s) != new_norm.norm_words(s):
                        diff.append("norm_words")
                        break
                if old_norm.tts_prompt(a["render_text"][0]) != new_norm.tts_prompt(b["render_text"][0]):
                    diff.append("tts_prompt")
                if diff:
                    bad.append((id_, "diff", diff))
    print(f"text parity: {lessons} lessons, {parts} lesson parts, {len(bad)} different")
    for id_, kind, what in bad[:50]:
        print(f"  {kind}: {id_}: {', '.join(what)}")
    if args.summary:
        with open(args.summary, "a", encoding="utf-8") as f:
            f.write(f"### Text parity\n\n{lessons} lessons, {parts} lesson parts: "
                    f"**{'same' if not bad else f'{len(bad)} different'}**\n\n")
    return 1 if bad or not parts else 0


# ----------------------------------------------------------------- audio

def write_work(work: Path, items: list[dict], seeds: list[int]) -> Path:
    """lines.json, takes_index.json and jobs.json for one engine."""
    work.mkdir(parents=True, exist_ok=True)
    (work / "lines.json").write_text(json.dumps(items, indent=1, ensure_ascii=False), encoding="utf-8")
    index, jobs = {}, []
    for it in items:
        for k, t in enumerate(it["render_text"], 1):
            key = f"{it['id']}#{k}"
            for seed in seeds:
                out = str(work / "takes" / f"{key.replace('/', '_').replace('#', '_s')}_seed{seed}.wav")
                index[out] = {"key": key, "seed": seed}
                jobs.append({"key": key, "text": t, "seed": seed, "out": out})
    (work / "takes_index.json").write_text(json.dumps(index, indent=1), encoding="utf-8")
    (work / "jobs.json").write_text(json.dumps(jobs, ensure_ascii=False), encoding="utf-8")
    return work / "jobs.json"


def run(cmd: list[str]) -> None:
    print("::group::" + " ".join(c for c in cmd[:4]), flush=True)
    try:
        subprocess.run(cmd, check=True)
    finally:
        print("::endgroup::", flush=True)


def cmd_audio(args) -> int:
    import lesson_lines as L
    import pronunciations

    voices = L.load_voices()
    if args.persona not in voices:
        print(f"::error::{args.persona} has no approved lesson voice (lesson_voices.json)")
        return 1
    v = voices[args.persona]
    ref = Path(args.voice_root).resolve() / v["ref_path"]
    if not ref.is_file() or sha256_file(ref) != v["ref_sha256"]:
        print("::error::reference sha256 does not match lesson_voices.json; refusing to render")
        return 1
    steps = int(v.get("ddpm_steps", 0) or 10)
    seeds = [int(s) for s in args.seeds.split(",")]
    pron = pronunciations.load()
    work = Path(args.work).resolve()
    old_items, new_items, text_bad = [], [], []
    for id_, text in TEST_LINES:
        a, b = both_fields(id_, text, pron)
        if text_diff(a, b):
            text_bad.append(id_)
        for items, f in ((old_items, a), (new_items, b)):
            items.append({"id": id_, **f, "file": f"{id_}.wav", "final_wav": f"{id_}.wav"})
    gate = ["--f0-target", str(v["f0_target_hz"]), "--f0-tolerance", str(v["f0_tolerance_hz"]),
            "--near-miss-words", str(args.near_miss)]

    old_jobs = write_work(work / "old", old_items, seeds)
    new_jobs = write_work(work / "new", new_items, seeds)
    run([sys.executable, str(HERE / "render_takes.py"), "--jobs", str(old_jobs), "--ref", str(ref),
         "--scripts-dir", args.scripts_dir, "--model-path", args.model_path, "--ddpm-steps", str(steps)])
    run([sys.executable, "-m", "rokct_media.speech.takes", "--jobs", str(new_jobs), "--ref", str(ref),
         "--engine", "voice_model", "--no-cache", "--engine-opts",
         json.dumps({"model_path": args.model_path, "cfg_scale": 1.3, "ddpm_steps": steps})])
    run([sys.executable, str(HERE / "qc.py"), "--work", str(work / "old"), "--ref", str(ref),
         "--scripts-dir", args.scripts_dir, "--asr-model", args.asr_model, *gate])
    run([sys.executable, "-m", "rokct_media.qc.worker", "sentences", "--work", str(work / "new"),
         "--ref", str(ref), "--asr-model", args.asr_model, *gate])

    rows, bad = [], list(text_bad)
    # Every take, byte for byte.
    oi = json.loads((work / "old" / "takes_index.json").read_text(encoding="utf-8"))
    ni = {(m["key"], m["seed"]): p for p, m in
          json.loads((work / "new" / "takes_index.json").read_text(encoding="utf-8")).items()}
    takes_same = 0
    for p, m in oi.items():
        q = ni.get((m["key"], m["seed"]))
        if q and Path(p).exists() and Path(q).exists() and sha256_file(Path(p)) == sha256_file(Path(q)):
            takes_same += 1
        else:
            bad.append(f"take {m['key']} seed{m['seed']}")
    # Every line's verdict and clip.
    old_r = {r["id"]: r for r in json.loads((work / "old" / "results.json").read_text(encoding="utf-8"))}
    new_r = {r["id"]: r for r in json.loads((work / "new" / "results.json").read_text(encoding="utf-8"))}
    for id_, _t in TEST_LINES:
        a, b = old_r.get(id_, {}), new_r.get(id_, {})
        diff = [k for k in LINE_KEYS if a.get(k) != b.get(k)]
        rows.append((id_, a.get("status"), b.get("status"), "same" if not diff else ", ".join(diff)))
        if diff:
            bad.append(f"line {id_}: {', '.join(diff)}")
    print(f"audio parity {args.persona} ({v['voice']}, {steps} steps, seeds {seeds}): "
          f"{takes_same}/{len(oi)} takes identical")
    for id_, so, sn, d in rows:
        print(f"  {id_}: voice_batch {so}, rokct-media {sn}: {d}")
    for b in bad:
        print(f"::error::parity: {b}")
    if args.summary:
        with open(args.summary, "a", encoding="utf-8") as f:
            f.write(f"### Audio parity: {args.persona}\n\n{steps} steps, seeds {seeds}: "
                    f"{takes_same}/{len(oi)} takes byte-identical\n\n"
                    "| Line | voice_batch | rokct-media | Compared |\n| --- | --- | --- | --- |\n")
            for id_, so, sn, d in rows:
                f.write(f"| {id_} | {so} | {sn} | {d} |\n")
            f.write("\n")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("text")
    t.add_argument("--lessons-root", required=True)
    a = sub.add_parser("audio")
    a.add_argument("--persona", required=True)
    a.add_argument("--voice-root", required=True)
    a.add_argument("--scripts-dir", required=True)
    a.add_argument("--model-path", required=True)
    a.add_argument("--work", required=True)
    a.add_argument("--seeds", default="11,22")
    a.add_argument("--near-miss", type=int, default=1)
    a.add_argument("--asr-model", default=os.environ.get("ASR_MODEL", "small.en"))
    for p in (t, a):
        p.add_argument("--summary", default=os.environ.get("GITHUB_STEP_SUMMARY", ""))
    args = ap.parse_args()
    return cmd_text(args) if args.cmd == "text" else cmd_audio(args)


if __name__ == "__main__":
    sys.exit(main())
