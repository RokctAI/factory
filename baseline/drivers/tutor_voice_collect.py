#!/usr/bin/env python3
"""Collect the tutor voice batch's baseline render into the output folder.

    tutor_voice_collect.py FIXTURE_JSON AGENT_ROOT WORK_DIR COMMITTED_MANIFEST OUT_DIR

voice_batch/run.py installs a passing line into the agent checkout and
records it in <voice>_manifest.<category>.json. This copies that file (and
every per-seed take the run rendered) into OUT_DIR and writes scores.json:
the line's gate numbers, with every text field dropped (tutor scripts are
private), beside the sha256 the committed manifest recorded for the same
line, so the baseline also says whether today's render reproduces what is
in the agent repo.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import sys
from pathlib import Path

KEEP_STR = {"id", "category", "file", "status", "sha256", "tail_pad", "ci_run_id"}


def clean(v, key=""):
    """Numbers, booleans and ids only: never line text or transcripts."""
    if isinstance(v, dict):
        return {k: c for k, x in v.items() if (c := clean(x, k)) is not None}
    if isinstance(v, list):
        items = [clean(x, key) for x in v]
        return [x for x in items if x is not None]
    if isinstance(v, (bool, int, float)) or v is None:
        return v
    if isinstance(v, str) and key in KEEP_STR:
        return v
    return None


def main() -> int:
    fixture = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    agent, work, committed_path, out = (Path(p) for p in sys.argv[2:6])
    out.mkdir(parents=True, exist_ok=True)
    line, voice, tutor, cat = fixture["line"], fixture["voice"], fixture["tutor"], fixture["category"]
    committed = json.loads(committed_path.read_text(encoding="utf-8")) if committed_path.is_file() else {}
    before = next((e for e in committed.get("lines", []) if e["id"] == line), None)
    new = json.loads((agent / f"lms/team/tutors/CAPS/{tutor}/{voice}_manifest.{cat}.json").read_text(encoding="utf-8"))
    passed = next((e for e in new.get("lines", []) if e["id"] == line), None)
    failed = next((e for e in new.get("failed", []) if e["id"] == line), None)
    scores = {"line": line, "voice": voice, "category": cat}
    if passed:
        src = agent / passed["file"]
        dst = out / "final" / Path(passed["file"]).name
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
        got = hashlib.sha256(dst.read_bytes()).hexdigest()
        scores.update(status="pass", entry=clean(passed), sha256=got)
    else:
        scores.update(status="fail", entry=clean(failed or {}),
                      note="the line failed the gate after every seed round; run.py installs nothing")
    if before:
        scores["committed"] = {"sha256": before.get("sha256"), "tail_pad": before.get("tail_pad"),
                               "seeds": before.get("seeds")}
        scores["matches_committed"] = bool(passed) and scores.get("sha256") == before.get("sha256")
    takes = sorted((work / cat / "takes").glob("*.wav"))
    for t in takes:
        d = out / "takes" / t.name
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(t, d)
    scores["takes"] = [t.name for t in takes]
    header = {k: new.get(k) for k in ("engine", "settings", "reference")}
    scores["run_header"] = clean(header)
    (out / "scores.json").write_text(json.dumps(scores, indent=1) + "\n", encoding="utf-8")
    print(f"{line}: {scores['status']}, {len(takes)} take(s)"
          + (f", matches committed: {scores['matches_committed']}" if "matches_committed" in scores else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
