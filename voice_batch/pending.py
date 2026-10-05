#!/usr/bin/env python3
"""How many of a batch's lines are still to render (the scheduled scan).

    python voice_batch/pending.py --agent-root .agentmain --root .agentmain --root <branch manifests> BATCH_JSON
    python voice_batch/pending.py --agent-root .agentmain --scan LIST   # prints the first pending batch, or nothing

LIST has one "<batch path>\t<branch manifests dir>" line per batch, in scan
order (the dir is empty when the batch's agent branch does not exist); agent
main's manifests always count.

Builds the batch's lines from the agent checkout (scripts, voice specs, R-3
app sources) exactly as run.py does, then reads the batch's manifests under
every --root (agent main, and the files of the batch's agent branch exported
by ci/scan_pending.sh). A line is done when any of them has a current passed
entry for it (same text, spoken text, tail pad and reference: manifest
fields only, no audio hash) or a failed entry for the same text and
reference (it failed every seed round: final, not retried daily). Prints the
count of lines not done; exit 3 when the batch is not valid. Ids and counts
only, never text.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import batch as batchmod  # noqa: E402
import resume  # noqa: E402


def _load(p: Path) -> dict | None:
    try:
        m = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    return m if isinstance(m, dict) else None


def manifests(b: dict, root: Path) -> list[dict]:
    """The batch's manifests under one root: the merged one and the parts."""
    if b["kind"] == "r3":
        from r3_lines import AUDIO_DIR
        d = root / AUDIO_DIR
        paths = [d / f"r3_manifest.{b['voice']}.json", *sorted(d.glob(f"r3_manifest.{b['voice']}.part[0-9][0-9].json"))]
    else:
        from lines import team_rel
        d = root / team_rel(b["tutor"])
        paths = [d / f"{b['voice']}_manifest.json", *(d / f"{b['voice']}_manifest.{c}.json" for c in b["categories"])]
    return [m for m in map(_load, paths) if m is not None]


def batch_items(b: dict, agent_root: Path, factory_root: Path | None = None) -> list[dict]:
    if b["kind"] == "r3":
        from r3_lines import FACTORY, build_r3_lines
        return build_r3_lines(factory_root or FACTORY, b.get("packs"), b.get("lines"), b["locale"], agent_root)
    from lines import build_lines
    items = build_lines(agent_root, b["tutor"], b["categories"], kind=b["kind"])
    only = set(b.get("lines") or [])
    return [it for it in items if not only or it["id"] in only]


def is_done(it: dict, ms: list[dict], ref_sha: str, kind: str) -> bool:
    for m in ms:
        mref = (m.get("reference") or {}).get("sha256")
        for e in m.get("lines", []):
            # r3 entries always carry render_sha256 (run.py's r3 skip is strict)
            if e.get("id") == it["id"] and resume.line_current(e, it, ref_sha, mref, legacy_ok=kind != "r3"):
                return True
        for e in m.get("failed", []):
            if e.get("id") == it["id"] and resume.final_failed(e, it, ref_sha):
                return True
    return False


def pending_ids(batch_path: str | Path, agent_root: Path, roots: list[Path], factory_root: Path | None = None) -> list[str]:
    """Ids of the batch's lines not yet done. Raises batch.BatchError (or
    ValueError) for a batch that is not valid against this checkout."""
    b = batchmod.load_batch(batch_path, factory_root)
    ms = [m for r in roots for m in manifests(b, Path(r))]
    return [it["id"] for it in batch_items(b, Path(agent_root), factory_root)
            if not is_done(it, ms, b["ref_sha256"], b["kind"])]


def first_pending(batches: list[tuple[str, list[Path]]], agent_root: Path,
                  factory_root: Path | None = None) -> tuple[str, int] | None:
    """(path, pending count) of the first batch, in the given order, with a
    line still to render; None when every batch is done. A batch that is not
    valid is skipped with a warning."""
    for path, roots in batches:
        try:
            n = len(pending_ids(path, agent_root, roots, factory_root))
        except (batchmod.BatchError, ValueError, OSError) as exc:
            print(f"::warning::{path}: skipped by the scan ({type(exc).__name__})", file=sys.stderr)
            continue
        print(f"scan: {path}: {n} line(s) pending", file=sys.stderr)
        if n:
            return path, n
    return None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--agent-root", required=True, help="agent checkout the lines are built from")
    ap.add_argument("--root", action="append", default=[], help="a tree whose manifests count as done (repeatable)")
    ap.add_argument("--factory-root", default=None)
    ap.add_argument("--scan", help="file of '<batch>\\t<branch dir>' lines: print the first pending batch")
    ap.add_argument("batch", nargs="?")
    a = ap.parse_args(argv)
    agent = Path(a.agent_root)
    if a.scan:
        batches = []
        for ln in Path(a.scan).read_text(encoding="utf-8").splitlines():
            if ln.strip():
                path, _, extra = ln.partition("\t")
                batches.append((path, [agent, *([Path(extra)] if extra else [])]))
        hit = first_pending(batches, agent, Path(a.factory_root) if a.factory_root else None)
        if hit:
            print(hit[0])
        else:
            print("scan: nothing pending in any batch", file=sys.stderr)
        return 0
    if not a.batch:
        ap.error("BATCH_JSON or --scan is required")
    try:
        ids = pending_ids(a.batch, Path(a.agent_root), [Path(r) for r in a.root or [a.agent_root]],
                          Path(a.factory_root) if a.factory_root else None)
    except (batchmod.BatchError, ValueError, OSError) as exc:
        print(f"::warning::{a.batch}: not scanned ({type(exc).__name__})", file=sys.stderr)
        return 3
    print(len(ids))
    return 0


if __name__ == "__main__":
    sys.exit(main())
