#!/usr/bin/env python3
"""Step-2 candidate: the voice fixtures as rokct-media job folders, and their
outputs laid out like the step-0 baseline so the two manifests compare.

    candidate.py jobs AGENT_ROOT JOBS_DIR
        Writes two job folders from the baseline fixtures:
          JOBS_DIR/tutor_voice/  script.md (the fixture line's script, read
                                 from the private agent checkout) + voice.txt
                                 naming the tutor id. No job.json: the
                                 folder conventions decide.
          JOBS_DIR/reel_voices/  job.json: the fixture's one line, Voice B,
                                 whole-take selection, prefer_seeds and asset
                                 exactly as the batch has them.
        Job folders stay on the runner (they hold private text).

    candidate.py collect ENGINE JOB_DIR OUT_DIR QC_JSON
        Copies the job's out/ (and, for the tutor line, its takes) into
        OUT_DIR under the baseline's file names, copies result.json (ids,
        numbers and hashes only), and writes QC_JSON: {output path: gate
        numbers} for rokct-media compare.

Never prints line text.
"""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
TUTOR = json.loads((HERE / "fixtures/tutor_voice.json").read_text(encoding="utf-8"))
REEL = json.loads((HERE / "fixtures/reel_voices_batch.json").read_text(encoding="utf-8"))


def safe(key: str) -> str:
    return key.replace("/", "_").replace("#", "_s")


def jobs(agent: Path, root: Path) -> int:
    t = root / "tutor_voice"
    t.mkdir(parents=True, exist_ok=True)
    tutor, cat, stem = TUTOR["line"].split("/")
    shutil.copyfile(agent / f"lms/team/tutors/CAPS/{tutor}/{cat}/{stem}.md", t / "script.md")
    (t / "voice.txt").write_text(TUTOR["tutor"] + "\n", encoding="utf-8")

    r = root / "reel_voices"
    r.mkdir(parents=True, exist_ok=True)
    (line,) = REEL["lines"]
    seg = {"id": line["id"], "role": "narrator", "text": line["text"]}
    for k in ("asset", "prefer_seeds", "takes", "keep_through"):
        if k in line:
            seg[k] = line[k]
    job = {"schema": "rokct-media/job@1", "id": REEL["id"], "cast": {"narrator": {"voice": line["voice"]}},
           "speech": {"selection": "whole_take"}, "segments": [seg], "deliver": [{"sink": "local"}]}
    (r / "job.json").write_text(json.dumps(job, indent=1) + "\n", encoding="utf-8")
    print(f"job folders: tutor_voice ({TUTOR['line']}, zero JSON), reel_voices ({REEL['id']}, job.json)")
    return 0


def qc_of(result: dict, seg_id: str, take_seed: int | None = None) -> dict:
    seg = next(s for s in result["segments"] if s["id"] == seg_id)
    voice = result["voices"][seg["voice"]]
    q = {"f0_window_hz": voice["gate"]["median_f0_hz"], "profile": "clip_wav"}
    src = seg
    if take_seed is not None:
        src = next(t for t in seg["takes"] if t["seed"] == take_seed)
    for k in ("median_f0_hz", "similarity", "similarity_threshold", "duration_s", "asr_word_errors", "tail_db",
              "gate", "seeds"):
        if k in src:
            q[k] = src[k]
    return q


def collect(engine: str, job: Path, out: Path, qc_path: Path) -> int:
    result = json.loads((job / "out/result.json").read_text(encoding="utf-8"))
    out.mkdir(parents=True, exist_ok=True)
    qc: dict[str, dict] = {}
    if result.get("status") != "pass":
        print(f"{engine}: rokct-media status {result.get('status')}")
    if engine == "tutor_voice":
        (seg,) = [s for s in result["segments"]]
        stem = TUTOR["line"].split("/")[-1]
        src = job / "out" / f"{seg['id']}.wav"
        if src.is_file():
            (out / "final").mkdir(exist_ok=True)
            shutil.copyfile(src, out / "final" / f"{stem}.wav")
            qc[f"final/{stem}.wav"] = qc_of(result, seg["id"])
        takes = sorted((job / ".work/speech").glob("*/takes/*.wav"))
        for t in takes:
            name = safe(TUTOR["line"]) + t.name[len(seg["id"]):]
            (out / "takes").mkdir(exist_ok=True)
            shutil.copyfile(t, out / "takes" / name)
        print(f"{engine}: {result.get('status')}, {len(takes)} take(s)")
    elif engine == "reel_voices":
        (line,) = REEL["lines"]
        for p in sorted((job / "out").rglob("*")):
            if not p.is_file() or p.name == "result.json":
                continue
            rel = p.relative_to(job / "out").as_posix()
            if rel == line.get("asset"):
                rel = f"assets/{rel}"
            dst = out / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(p, dst)
            if rel.endswith(".wav"):
                seed = next((int(x[4:]) for x in Path(rel).stem.split("_") if x.startswith("seed")), None)
                seg = result["segments"][0]
                qc[rel] = qc_of(result, seg["id"], seed if seed is not None else seg["chosen_seeds"][0])
        print(f"{engine}: {result.get('status')}")
    else:
        raise SystemExit(f"unknown engine {engine}")
    shutil.copyfile(job / "out/result.json", out / "result.json")
    qc_path.parent.mkdir(parents=True, exist_ok=True)
    qc_path.write_text(json.dumps(qc, indent=1) + "\n", encoding="utf-8")
    return 0


def main() -> int:
    if sys.argv[1:2] == ["jobs"]:
        return jobs(Path(sys.argv[2]), Path(sys.argv[3]))
    if sys.argv[1:2] == ["collect"]:
        return collect(sys.argv[2], Path(sys.argv[3]), Path(sys.argv[4]), Path(sys.argv[5]))
    raise SystemExit(__doc__)


if __name__ == "__main__":
    sys.exit(main())
