"""Which batch lanes have a voice batch run in flight.

    gh api .../runs --jq '... | .display_title' | python3 busy_lanes.py
    python3 busy_lanes.py --lane voice_batches/inbox/r3_packs_0_gradeR.json

Reads the titles of the other voice batch runs that are not completed, one
per line, and prints each one's lane once: "r3" for the R-3 batches (they
share one voice branch and one r3_manifest), else the batch path. A run
started with batch_path is titled "Voice batch: <path>" (run-name in
voice_batch.yml); any other title is a run whose batch is unknown (a
scheduled or push run, or one started before run-name) and prints "*".
--lane prints the lane of one batch path.
"""
from __future__ import annotations

import sys

PREFIX = "Voice batch: "


def lane(batch_path: str) -> str:
    return "r3" if "/r3_packs_" in batch_path else batch_path


def busy(titles: list[str]) -> list[str]:
    out: list[str] = []
    for t in titles:
        t = t.strip()
        if not t:
            continue
        key = lane(t[len(PREFIX):].strip()) if t.startswith(PREFIX) else "*"
        if key not in out:
            out.append(key)
    return out


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if argv[:1] == ["--lane"] and len(argv) == 2:
        print(lane(argv[1]))
        return 0
    if argv:
        print(__doc__, file=sys.stderr)
        return 2
    for key in busy(sys.stdin.read().splitlines()):
        print(key)
    return 0


if __name__ == "__main__":
    sys.exit(main())
