#!/usr/bin/env python3
"""Resumable voice batch renders: the time budget, checkpoint pushes, and
which lines are already done. Stdlib only (the plan job's scan and the merge
job import it without the render dependencies).

A render job (run.py) renders its lines in chunks. Before every seed round
it asks the Budget whether the round still fits (RENDER_BUDGET_MINUTES,
measured from JOB_STARTED_AT, the job's first step). When it does not, the
job stops cleanly: lines that passed are installed, lines that ran out of
seed rounds are recorded as failed (final), and the rest are listed under
"remaining" in the job's manifest. After each chunk a Checkpoint commits and
pushes what is installed so far (push_agent.sh), at most every
RENDER_PUSH_MINUTES. The merge job counts "remaining" across the batch's
manifests; if any line is left it re-dispatches the workflow (a
continuation, at most CONTINUATION_CAP of them) and holds the agent PR back
until the batch is complete.

    python voice_batch/resume.py remaining MANIFEST [CATEGORY ...]   # prints a count
    python voice_batch/resume.py next CONTINUATION                     # step outputs
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from textnorm import TAIL_PAD  # noqa: E402

DEFAULT_BUDGET_MINUTES = 300.0   # the render job's timeout-minutes is 330
DEFAULT_CHUNK_LINES = 4
DEFAULT_PUSH_MINUTES = 15.0
CONTINUATION_CAP = 5


def env_float(name: str, default: float) -> float:
    try:
        return float(os.environ.get(name) or default)
    except ValueError:
        return default


class Budget:
    """Wall-clock budget for one render job. limit_minutes <= 0: unlimited.

    allows(n_takes) is False once the elapsed time reaches the limit, or when
    the next round (n_takes takes at the rate of the largest round seen so
    far) would end past it. The first round a job runs has no rate yet, so
    every job makes progress."""

    def __init__(self, limit_minutes: float, start: float | None = None, clock=time.time):
        self.limit = limit_minutes * 60 if limit_minutes and limit_minutes > 0 else None
        self.clock = clock
        self.start = clock() if start is None else start
        self._round: tuple[int, float] | None = None   # (takes, seconds) of the largest round

    def elapsed(self) -> float:
        return self.clock() - self.start

    def record(self, n_takes: int, seconds: float) -> None:
        if n_takes > 0 and (self._round is None or n_takes >= self._round[0]):
            self._round = (n_takes, seconds)

    def estimate(self, n_takes: int) -> float:
        return 0.0 if self._round is None else self._round[1] / self._round[0] * n_takes

    def allows(self, n_takes: int = 0) -> bool:
        if self.limit is None:
            return True
        el = self.elapsed()
        return el < self.limit and el + self.estimate(n_takes) <= self.limit


class Checkpoint:
    """Runs the push command (push_agent.sh) after a chunk, at most every
    `every_minutes` unless forced. A failed push is a warning: the job's
    final push step retries, and the next checkpoint carries the same files."""

    def __init__(self, cmd: list[str], every_minutes: float = DEFAULT_PUSH_MINUTES, clock=time.time, run=None):
        self.cmd, self.every, self.clock = cmd, every_minutes * 60, clock
        self.run = run or (lambda c: subprocess.run(c).returncode)
        self.last: float | None = None
        self.pushes = 0

    def push(self, force: bool = False) -> bool:
        if not self.cmd:
            return False
        if not force and self.last is not None and self.clock() - self.last < self.every:
            return False
        rc = self.run(self.cmd)
        self.last = self.clock()
        if rc:
            print(f"::warning::checkpoint push failed (exit {rc}); the job's final push retries")
            return False
        self.pushes += 1
        return True


def _same_render(prev: dict, it: dict, legacy_ok: bool) -> bool:
    if "render_sha256" in prev:
        return prev["render_sha256"] == it.get("render_sha256")
    # An entry from before pronunciations was rendered from the display text.
    return legacy_ok and "tts_text" not in it


def line_current(prev: dict | None, it: dict, ref_sha: str, manifest_ref: str | None = None,
                 legacy_ok: bool = True) -> bool:
    """A passed manifest entry is still current for this line: same text,
    same spoken text, same tail pad, same reference. Manifest fields only
    (no audio hash): the cheap check the scheduled scan uses."""
    return bool(prev and prev.get("text_sha256") == it["text_sha256"]
                and prev.get("tail_pad") == TAIL_PAD
                and _same_render(prev, it, legacy_ok)
                and prev.get("ref_sha256", manifest_ref or ref_sha) == ref_sha)


def failed_keys(it: dict, ref_sha: str) -> dict:
    """What a failed entry records so a later run knows it is final for this
    text and reference."""
    out = {"text_sha256": it["text_sha256"], "render_sha256": it.get("render_sha256"),
           "ref_sha256": ref_sha, "tail_pad": TAIL_PAD}
    if os.environ.get("RENDER_SERIES"):
        out["series"] = os.environ["RENDER_SERIES"]
    return out


def final_failed(prev: dict | None, it: dict, ref_sha: str, series: str | None = None) -> bool:
    """A failed entry is final for this line: it ran out of seed rounds on
    the same text and reference (and, given a series, in this series of
    runs, so a fresh run still retries it once). Entries from before this
    field set never match, so those lines are retried once."""
    return bool(prev and prev.get("text_sha256") == it["text_sha256"]
                and prev.get("render_sha256") == it.get("render_sha256")
                and prev.get("ref_sha256") == ref_sha and prev.get("tail_pad") == TAIL_PAD
                and (series is None or prev.get("series") == series))


def write_outputs(remaining: int) -> None:
    """incomplete / remaining step outputs (stdout when not in Actions)."""
    lines = f"incomplete={'true' if remaining else 'false'}\nremaining={remaining}\n"
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a", encoding="utf-8") as f:
            f.write(lines)
    print(lines, end="")


def count_remaining(manifest: dict, categories: list[str] | None = None) -> int:
    """Lines left in a manifest: a list (category / r3 manifests), or a
    {category: [ids]} map (a merged tutor manifest), limited to categories."""
    rem = manifest.get("remaining") or []
    if isinstance(rem, dict):
        return sum(len(v) for k, v in rem.items() if not categories or k in categories)
    return len(rem)


def next_continuation(current: str | int, cap: int = CONTINUATION_CAP) -> int | None:
    """The next continuation number, or None at the cap."""
    n = int(current or 0)
    return None if n >= cap else n + 1


def main(argv: list[str]) -> int:
    if len(argv) >= 2 and argv[0] == "remaining":
        p = Path(argv[1])
        m = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
        print(count_remaining(m, argv[2:] or None))
        return 0
    if len(argv) == 2 and argv[0] == "next":
        nxt = next_continuation(argv[1], int(env_float("CONTINUATION_CAP", CONTINUATION_CAP)))
        print("dispatch=false" if nxt is None else f"dispatch=true\nnext={nxt}")
        return 0
    print("usage: resume.py remaining MANIFEST [CATEGORY ...] | resume.py next CONTINUATION", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
