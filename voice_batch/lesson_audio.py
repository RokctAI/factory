#!/usr/bin/env python3
"""Render lesson audio part by part: each speaker's lines of a session
package, in that speaker's approved voice, as soon as the voice exists.

    # which lesson parts still need audio -> matrix rows (stdout: step outputs)
    python voice_batch/lesson_audio.py plan --lessons-root _lessons --agent-root .agent \
        [--max-jobs 6 --job-words 4000 --only <lesson rel>,...]

    # one job: one persona, one or more lessons
    python voice_batch/lesson_audio.py render --lessons-root _lessons --agent-root .agent \
        --persona tutor_001 --lessons <rel>,<rel> --model-path <snapshot> --work $RUNNER_TEMP/la \
        [--checkpoint-cmd "bash voice_batch/ci/push_lessons.sh ..."]

    # a lesson whose tutor parts are all in: one audio.mp3 + timings.json
    python voice_batch/lesson_audio.py assemble --lessons-root _lessons --stems-root <dir> \
        --lesson <rel> --out <dir>

Who speaks what is lesson_lines.py. Stems (one MP3 per subtopic segment,
intro, Q&A turn and nervous-student script; mono 24 kHz 64 kbps) land under
<stems root>/<lesson rel>/voice/<persona>/ with manifest.json beside them.
The render is run.py's per-sentence render + QC gate, with one seed per
round (LESSON_SEED_ROUNDS) instead of three: lessons are ~40x the standing
lines, and a sentence that fails its seed still gets four more.

Logs carry lesson paths, line keys and numbers only, never line text.
"""
from __future__ import annotations

import argparse
import json
import os
import shlex
import shutil
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import lesson_lines as L  # noqa: E402

LESSON_SEED_ROUNDS = ([11], [22], [33], [44], [55])


def outputs(**kv) -> None:
    text = "".join(f"{k}={v}\n" for k, v in kv.items())
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a", encoding="utf-8") as f:
            f.write(text)
    print(text, end="")


# --- plan ---

def cmd_plan(args) -> int:
    voices = L.load_voices()
    only = {x for x in (args.only or "").split(",") if x} or None
    todo, stats = L.plan(Path(args.lessons_root), Path(args.agent_root),
                         L.curriculum_root(Path(args.lessons_root)), voices, only=only)
    jobs = L.pack(todo, args.max_jobs, args.job_words)
    print(f"lessons {stats['lessons']}: {stats['pending']} voiced part(s) pending, {stats['done']} done, "
          f"{stats['unvoiced']} waiting on a voice, {stats['blocked']} blocked, {stats['disabled']} disabled, "
          f"{stats['errors']} unresolved", file=sys.stderr)
    for j in jobs:
        print(f"  job {j['persona']}: {len(j['lessons'].split(','))} lesson(s), {j['words']} words", file=sys.stderr)
    if args.summary:
        by: dict[str, list[int]] = {}
        for t in todo:
            by.setdefault(t["persona"], [0, 0])
            by[t["persona"]][0] += 1
            by[t["persona"]][1] += t["words"]
        with open(args.summary, "a", encoding="utf-8") as f:
            f.write("| Voice | Lesson parts left | Words left |\n|---|---|---|\n")
            for p, (n, w) in sorted(by.items()):
                f.write(f"| {p} | {n} | {w} |\n")
            f.write(f"\n{stats['done']} part(s) done, {stats['unvoiced']} waiting on a voice, "
                    f"{len(jobs)} job(s) this run.\n")
    outputs(count=len(jobs), matrix_json=json.dumps([{"persona": j["persona"], "lessons": j["lessons"]}
                                                     for j in jobs], separators=(",", ":")))
    return 0


# --- render ---

def cmd_render(args) -> int:
    import pronunciations
    import run as R

    lessons_root, agent = Path(args.lessons_root).resolve(), Path(args.agent_root).resolve()
    stems = Path(args.stems_root).resolve()
    voices = L.load_voices()
    if args.persona not in voices:
        print(f"::error::{args.persona} has no approved lesson voice (lesson_voices.json)")
        return 1
    v = voices[args.persona]
    ref = agent / v["ref_path"]
    if not ref.is_file() or R.sha256_file(ref) != v["ref_sha256"]:
        print("::error::reference sha256 does not match lesson_voices.json; refusing to render")
        return 1
    args.voice, args.ref_sha256, args.ref_path = v["voice"], v["ref_sha256"], v["ref_path"]
    args.f0_target, args.f0_tolerance = float(v["f0_target_hz"]), float(v["f0_tolerance_hz"])
    args.pace_wpm, args.pace_tolerance = R.voice_pace(agent, args.persona)
    args.seed_rounds = LESSON_SEED_ROUNDS
    started = os.environ.get("JOB_STARTED_AT", "")
    args.budget = R.resume.Budget(args.budget_minutes, start=float(started) if started.isdigit() else None)
    args.checkpoint = (R.resume.Checkpoint(shlex.split(args.checkpoint_cmd), args.push_every_minutes)
                       if args.checkpoint_cmd else None)
    scripts = agent / "lms/team/scripts"
    pron = pronunciations.load()
    names = L.persona_names(agent)
    caps = L.curriculum_root(lessons_root)
    left_total = 0
    for rel in [x for x in args.lessons.split(",") if x]:
        folder = caps / rel
        if not args.budget.allows():
            print(f"::notice::time budget reached before {rel}; the next run picks it up")
            left_total += 1
            continue
        try:
            r = L.roles(lessons_root, folder)
        except L.LessonError as exc:
            print(f"::warning::skip {rel}: {exc}")
            continue
        why = L.blocked(agent, r, args.persona) or L.lesson_disabled(lessons_root, folder)
        if why:
            print(f"::warning::skip {rel} {args.persona}: {why}")
            continue
        try:
            built = L.build_items(lessons_root, folder, r, args.persona, pron, names)
        except pronunciations.PronunciationError as exc:
            print(f"::error::{exc}")
            continue
        errs = pronunciations.check_ambiguous(built, pron)
        if errs:
            for e in errs:
                print(f"::error::{e}")
            continue
        left_total += render_lesson(args, r, built, stems, caps, ref, scripts, agent)
    R.resume.write_outputs(left_total)
    return 0


def render_lesson(args, r: dict, built: list[dict], stems: Path, records: Path, ref: Path, scripts: Path,
                  agent: Path) -> int:
    """Render one persona's pending lines of one lesson: MP3s into the stems
    root (uploaded to the stems pre-release by the checkpoint command), the
    manifest + qc_failed.json into the lesson folder (`records`, the lessons
    checkout). Returns how many lines are left for a later run."""
    import mp3
    import run as R

    mpath = L.manifest_path(records, r, args.persona)
    manifest = R.load_json(mpath)
    redo = L.load_redo(records, r, args.persona)
    items = L.pending_items(built, manifest, args.ref_sha256, redo)
    label = f"{r['rel']} {args.persona}"
    if not items:
        print(f"{label}: nothing to render")
        return 0
    print(f"{label}: {len(items)} of {len(built)} line(s) to render ({L.words(items)} words)")
    by_id = {it["id"]: it for it in items}
    order = {it["id"]: n for n, it in enumerate(built)}
    lines = {e["id"]: e for e in manifest.get("lines", []) if e["id"] in order}
    failed = {e["id"]: e for e in manifest.get("failed", []) if e["id"] in order}
    manifest.update({"kind": "lesson", "lesson": r["rel"], "lesson_id": r["lesson_id"], "persona": args.persona,
                     "roles": {k: r[k] for k in ("first", "second", "host", "split")},
                     **R.run_header(args, ref, agent)})
    manifest["reference"]["path"] = args.ref_path
    manifest["settings"]["output"] = {"format": "mp3", "bitrate_kbps": mp3.BITRATE_KBPS,
                                      "sample_rate": mp3.SAMPLE_RATE, "channels": 1}
    tally = {"pass": 0, "fail": 0}

    def install(results: list[dict]) -> None:
        for res in results:
            it = by_id[res["id"]]
            tally["pass" if res["status"] == "pass" else "fail"] += 1
            base = {"id": it["id"], "key": it["key"], "script": it["script"], "text_sha256": it["text_sha256"],
                    "render_sha256": it["render_sha256"], "ref_sha256": args.ref_sha256, "tail_pad": R.TAIL_PAD}
            if res["status"] == "pass":
                dst = stems / it["file"]
                encoder = mp3.encode(res["final_path"], dst)
                lines[it["id"]] = {**base, "file": Path(it["file"]).name, **R.score_fields(res),
                                   "sha256": R.sha256_file(dst), "wav_sha256": res["sha256"], "encoder": encoder,
                                   **({"pronounced": it["pronounced"], "needs_listen": True}
                                      if it.get("pronounced") else {}),
                                   "seeds_tried": res["seeds_tried"]}
                failed.pop(it["id"], None)
            else:
                failed[it["id"]] = {**base, **R.failed_fields(res), **R.qc_failed.entry_fields(it, res)}
                lines.pop(it["id"], None)
                stale = stems / it["file"]
                if stale.exists():
                    stale.unlink()

    def write(remaining: list[str]) -> None:
        # The checkpoint command records each uploaded stem's release asset
        # in the manifest on disk; keep that for every line it still matches.
        on_disk = {e["id"]: e for e in R.load_json(mpath).get("lines", [])}
        for e in lines.values():
            prev = on_disk.get(e["id"])
            if prev and prev.get("asset") and prev.get("sha256") == e.get("sha256"):
                e["asset"] = prev["asset"]
        manifest["lines"] = sorted(lines.values(), key=lambda e: order.get(e["id"], 1e9))
        manifest["failed"] = sorted(failed.values(), key=lambda e: order.get(e["id"], 1e9))
        if remaining:
            manifest["remaining"] = remaining
        else:
            manifest.pop("remaining", None)
        manifest["complete"] = not remaining and len(manifest["lines"]) == len(built)
        mpath.parent.mkdir(parents=True, exist_ok=True)
        mpath.write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        R.qc_failed.write(mpath.with_name(R.qc_failed.QC_FAILED), manifest["failed"])

    started = time.time()
    remaining: list[str] = []
    # A redo (a passed line the owner rejected on listening) renders with
    # seeds it has not had: each rejection of a key shifts its seeds by 100.
    groups: dict[int, list[dict]] = {}
    for it in items:
        groups.setdefault(L.redo_shift(redo, it["key"]), []).append(it)
    for shift, group in sorted(groups.items()):
        args.seed_rounds = tuple([s + shift for s in rnd] for rnd in LESSON_SEED_ROUNDS)
        work = Path(args.work).resolve() / r["lesson_id"] / args.persona / f"shift{shift}"
        remaining += R.drive(group, work, ref, scripts, args, label, install, write)
        shutil.rmtree(work, ignore_errors=True)
        if remaining:
            break
    remaining += [it["id"] for g in groups.values() for it in g
                  if it["id"] not in lines and it["id"] not in failed and it["id"] not in remaining]
    write(remaining)
    print(f"{label}: {tally['pass']} passed, {tally['fail']} failed, {len(remaining)} left "
          f"of {len(items)} line(s) in {time.time() - started:.0f}s")
    return len(remaining)


# --- assemble ---

def tutor_keys(lessons_root: Path, r: dict) -> list[tuple[str, str]]:
    """[(persona, segment key)] in play order: the script segments that make
    the lesson's audio.mp3 (what release_on_complete times and plays)."""
    _rel, lm, _ar = L._import_release(lessons_root)
    folder = L.curriculum_root(lessons_root) / r["rel"]
    out = []
    for idx, text in lm.split_script_into_segments((folder / "script.md").read_text(encoding="utf-8")):
        if not text:
            continue
        who = r["first"] if r["split"] is None or idx < r["split"] else r["second"]
        out.append((who, f"seg{idx:02d}"))
    return out


def missing_segments(lessons_root: Path, stems: Path, r: dict) -> list[str]:
    miss = []
    for who, key in tutor_keys(lessons_root, r):
        if not (stems / L.stem_rel(r, who, key)).is_file():
            miss.append(f"{who}/{key}")
    return miss


def cmd_assemble(args) -> int:
    lessons_root = Path(args.lessons_root).resolve()
    stems = Path(args.stems_root).resolve()
    folder = L.curriculum_root(lessons_root) / args.lesson
    r = L.roles(lessons_root, folder)
    miss = missing_segments(lessons_root, stems, r)
    if miss:
        print(f"::error::{args.lesson}: {len(miss)} segment stem(s) missing: {', '.join(miss)}")
        return 1
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    ff = shutil.which("ffmpeg")
    if not ff:
        print("::error::ffmpeg is needed to assemble lesson audio")
        return 1
    parts = [stems / L.stem_rel(r, who, key) for who, key in tutor_keys(lessons_root, r)]
    bounds, t = [], 0.0
    for p in parts:
        d = probe_seconds(p)
        bounds.append({"start": round(t, 3), "end": round(t + d, 3)})
        t += d
    lst = out / "concat.txt"
    lst.write_text("".join(f"file '{p}'\n" for p in parts), encoding="utf-8")
    import mp3
    wav = out / "audio.wav"
    subprocess.run([ff, "-nostdin", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
                    "-ac", "1", "-ar", str(mp3.SAMPLE_RATE), "-c:a", "pcm_s16le", str(wav)], check=True)
    mp3.encode(wav, out / "audio.mp3")
    wav.unlink()
    lst.unlink()
    (out / "timings.json").write_text(json.dumps(bounds, indent=1) + "\n", encoding="utf-8")
    print(f"{args.lesson}: {len(parts)} segment(s), {t:.1f}s -> audio.mp3 + timings.json")
    return 0


def probe_seconds(p: Path) -> float:
    ffprobe = shutil.which("ffprobe") or "ffprobe"
    r = subprocess.run([ffprobe, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                       check=True, capture_output=True, text=True)
    return float(r.stdout.strip())


def main(argv: list[str] | None = None) -> int:
    import resume
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("plan")
    p.add_argument("--lessons-root", required=True)
    p.add_argument("--agent-root", required=True)
    p.add_argument("--max-jobs", type=int, default=L.env_int("LESSON_AUDIO_JOBS", 6))
    p.add_argument("--job-words", type=int, default=L.env_int("LESSON_AUDIO_JOB_WORDS", 4000))
    p.add_argument("--only", default="", help="comma-separated lesson rels to limit the scan to")
    p.add_argument("--summary", help="append a markdown table here (e.g. $GITHUB_STEP_SUMMARY)")
    p = sub.add_parser("render")
    p.add_argument("--lessons-root", required=True)
    p.add_argument("--agent-root", required=True)
    p.add_argument("--stems-root", required=True, help="where the MP3 stems are written (outside the checkout)")
    p.add_argument("--persona", required=True)
    p.add_argument("--lessons", required=True)
    p.add_argument("--model-path", required=True)
    p.add_argument("--work", required=True)
    p.add_argument("--asr-model", default=os.environ.get("ASR_MODEL", "small.en"))
    p.add_argument("--language", default="en")
    p.add_argument("--budget-minutes", type=float,
                   default=resume.env_float("RENDER_BUDGET_MINUTES", resume.DEFAULT_BUDGET_MINUTES))
    p.add_argument("--chunk-lines", type=int, default=int(resume.env_float("RENDER_CHUNK_LINES", 2)))
    p.add_argument("--push-every-minutes", type=float,
                   default=resume.env_float("RENDER_PUSH_MINUTES", resume.DEFAULT_PUSH_MINUTES))
    p.add_argument("--checkpoint-cmd", default="")
    p = sub.add_parser("assemble")
    p.add_argument("--lessons-root", required=True)
    p.add_argument("--stems-root", required=True)
    p.add_argument("--lesson", required=True)
    p.add_argument("--out", required=True)
    args = ap.parse_args(argv)
    return {"plan": cmd_plan, "render": cmd_render, "assemble": cmd_assemble}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
