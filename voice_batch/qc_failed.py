#!/usr/bin/env python3
"""The durable log of lines that failed QC in every seed round.

A line that runs out of seed rounds is recorded in the job's manifest
"failed" list with its per-round gate failures (run.py). This module
projects those entries into qc_failed.json files committed next to the
clips on the agent branch (the private agent repo only, never factory):

  tutor / assistant  <team dir>/<clip dir>/qc_failed.json, per category
                     (greetings/, signoffs/, samples/ for teaching, ...),
                     written by the render job with its manifest
  r3                 lms/dart/templates/assets/r3_packs/audio/qc_failed.<voice>.json,
                     written by the merge job from the merged manifest
                     (parallel shards share that folder)

Each entry: line id, line text, the failing gates and their values for
every round (for the ASR gate, what the ASR heard: the stitched line's
transcript, or each sentence's distinct take transcripts), the attempt count, the batch file, the CI run id and a UTC
date. A line that later passes leaves the manifest's failed list, so it
drops out of the file; an empty file is deleted. Stdlib only.
"""
from __future__ import annotations

import json
import os
import time
from pathlib import Path

QC_FAILED = "qc_failed.json"


def _pick(d: dict, *keys: str) -> dict:
    return {k: d.get(k) for k in keys}


def failing(r: dict) -> dict:
    """{gate: measured value(s)} for every gate a QC result failed."""
    if r.get("status") == "incomplete":
        # No word-exact take at all for some sentence: the ASR gate.
        out = {"sentences_without_word_exact_take": sum(1 for x in r.get("lacking", []) if x.get("tier") == 0)
               or len(r.get("lacking", []))}
        heard = [{"sentence": int(x["key"].rsplit("#", 1)[1]), "heard": x["heard"]}
                 for x in r.get("lacking", []) if x.get("heard")]
        return {"asr": {**out, **({"heard": heard} if heard else {})}}
    checks = r.get("checks") or {}
    values = {
        "f0": lambda: _pick(r, "median_f0_hz"),
        "similarity": lambda: _pick(r, "similarity", "similarity_threshold"),
        "asr": lambda: _pick(r, "asr_word_errors", "asr_transcript"),
        "tail": lambda: _pick(r, "tail_db"),
        "loudness": lambda: _pick(checks, "integrated_db"),
        "lead_in": lambda: _pick(checks, "lead_in_ms"),
        "clipping": lambda: _pick(checks, "peak_dbfs", "full_scale_run"),
        "onset": lambda: _pick(checks, "head_rms_dbfs", "onset_rise_ms"),
    }
    return {g: values[g]() if g in values else None for g, ok in (r.get("gate") or {}).items() if not ok}


def round_record(rnd: int, seeds: list, r: dict) -> dict:
    return {"round": rnd, "seeds": list(seeds), "status": r.get("status"), "failing": failing(r)}


def entry_fields(it: dict, r: dict) -> dict:
    """The fields run.py adds to a failed manifest entry for this log."""
    return {"text": it["text"], "attempts": len(r.get("seeds_tried") or []), "rounds": r.get("rounds", []),
            "batch": os.environ.get("BATCH_FILE", ""), "run_id": os.environ.get("GITHUB_RUN_ID", "local"),
            "date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}


def project(e: dict) -> dict:
    keys = ("id", "category", "text", "file_not_committed", "attempts", "seeds_tried", "rounds", "batch", "run_id", "date")
    return {k: e[k] for k in keys if k in e}


def write(path: Path, failed_entries: list[dict]) -> None:
    """qc_failed.json at path from manifest failed entries; deleted when none."""
    entries = sorted((project(e) for e in failed_entries), key=lambda e: e["id"])
    if entries:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"failed": entries}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    elif path.exists():
        path.unlink()


def write_by_clip_dir(agent: Path, clip_dirs: set[str], failed_entries: list[dict]) -> None:
    """One qc_failed.json per clip folder of a category (tutor / assistant)."""
    for d in sorted(clip_dirs):
        write(agent / d / QC_FAILED, [e for e in failed_entries
                                      if str(Path(e.get("file_not_committed", "")).parent) == d])


def last_failing(e: dict) -> str:
    """'gate, gate' failed in the entry's last round (for tables)."""
    rounds = e.get("rounds") or []
    gates = (rounds[-1].get("failing") or {}) if rounds else {g: None for g, ok in (e.get("gate") or {}).items() if not ok}
    return ", ".join(sorted(gates)) or e.get("status", "fail")
