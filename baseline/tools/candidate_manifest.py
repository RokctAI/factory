#!/usr/bin/env python3
"""Fold the candidate's manifest fragments into candidate_manifest.json, in
the baseline manifest's shape, with each output's gate numbers attached as
"qc" (from candidate.py collect) for rokct-media compare.

    candidate_manifest.py FRAGMENT_DIR QC_DIR OUT_JSON ROKCT_MEDIA_REF
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path


def main() -> int:
    frag_dir, qc_dir, out, ref = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), sys.argv[4]
    engines = []
    for p in sorted(frag_dir.glob("*.json")):
        e = json.loads(p.read_text(encoding="utf-8"))
        qp = qc_dir / f"{e['engine']}.json"
        qc = json.loads(qp.read_text(encoding="utf-8")) if qp.is_file() else {}
        for o in e.get("outputs", []):
            if o["path"] in qc:
                o["qc"] = qc[o["path"]]
        engines.append(e)
    server = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    manifest = {
        "kind": "rokct-media regression candidate (step 2: voice_batch lifted into rokct-media)",
        "schema": 1,
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "run": {"url": f"{server}/{repo}/actions/runs/{os.environ.get('GITHUB_RUN_ID', '')}",
                "repo": repo, "ref": os.environ.get("GITHUB_REF", ""), "sha": os.environ.get("GITHUB_SHA", ""),
                "run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT", "")},
        "rokct_media": {"repo": "RokctAI/The-Rokct-Protocol", "ref": ref,
                        "subdirectory": "core/utils/rokct_media", "extra": "voice"},
        "posting": "off: read-only token, no posting credentials, deliver local only, nothing pushed",
        "engines": engines,
    }
    out.write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    for e in engines:
        print(f"{e['engine']}: {e['status']}, {len(e.get('outputs', []))} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
