#!/usr/bin/env python3
"""Fold the per-engine fragments into baseline_manifest.json and print a
Markdown summary table (for $GITHUB_STEP_SUMMARY).

    merge.py FRAGMENT_DIR OUT_JSON

Every engine in ENGINES appears in the manifest: an engine whose job wrote
no fragment is recorded as failed with that reason.
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

ENGINES = [
    "tutor_voice", "radio_ad", "reel_voices", "social_reel", "lesson6",
    "tiktok_post", "still_tutor_images", "still_tour", "still_typed_pr202", "guided_tour",
]


def main() -> int:
    frag_dir, out = Path(sys.argv[1]), Path(sys.argv[2])
    frags = {}
    for p in sorted(frag_dir.rglob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        frags[d["engine"]] = d
    engines = []
    for name in ENGINES + sorted(set(frags) - set(ENGINES)):
        engines.append(frags.get(name) or {
            "engine": name, "status": "failed",
            "error": "its job wrote no manifest fragment (it failed before recording; see the job log)"})
    server = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    manifest = {
        "kind": "rokct-media regression baseline (step 0: old engines)",
        "schema": 1,
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "run": {"url": f"{server}/{repo}/actions/runs/{os.environ.get('GITHUB_RUN_ID', '')}",
                "repo": repo, "ref": os.environ.get("GITHUB_REF", ""), "sha": os.environ.get("GITHUB_SHA", ""),
                "run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT", "")},
        "posting": "off: no posting credentials in any job, render functions called directly, "
                   "read-only token, no credentials left in any checkout, nothing pushed",
        "artifacts": "one artifact per engine, baseline-<engine>; cloned-voice audio is hashed and "
                     "measured but not uploaded (public repository)",
        "engines": engines,
    }
    out.write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    print("### Media regression baseline (old engines)\n")
    print("| engine | status | files (uploaded) | time | detail |")
    print("|---|---|---|---|---|")
    for e in engines:
        outs = e.get("outputs", [])
        up = sum(1 for o in outs if o.get("uploaded"))
        detail = (e.get("reason") or e.get("error") or "").replace("\n", " ").replace("|", "/")[:160]
        dur = f"{e['duration_s']:.0f}s" if isinstance(e.get("duration_s"), (int, float)) else ""
        print(f"| {e['engine']} | {e['status']} | {len(outs)} ({up}) | {dur} | {detail} |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
