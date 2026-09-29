#!/usr/bin/env python3
"""Turn a list of ad JSON paths into the CI render matrix.

    python radio_ads/ci/plan.py ads.txt      # prints {"include": [{"file": ..., "id": ...}]}

Run after `make_ad.py --validate`, so every file is already known to parse
and to carry a schema-valid id. Fails if two files share an id, since both
would render into out/<id>/ and upload as the same artifact name.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def plan(paths: list[str]) -> dict:
    include, seen = [], {}
    for p in paths:
        ad_id = json.loads(Path(p).read_text(encoding="utf-8"))["id"]
        if ad_id in seen:
            raise SystemExit(f"::error::{p} and {seen[ad_id]} both use id '{ad_id}'; ids must be unique")
        seen[ad_id] = p
        include.append({"file": p, "id": ad_id})
    return {"include": include}


def main(argv: list[str]) -> int:
    paths = [line.strip() for line in Path(argv[1]).read_text(encoding="utf-8").splitlines() if line.strip()]
    print(json.dumps(plan(paths), separators=(",", ":")))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
