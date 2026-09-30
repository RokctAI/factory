#!/usr/bin/env python3
"""Validate a voice batch JSON and print its fields as GitHub step outputs.

    python voice_batch/batch.py voice_batches/inbox/<batch>.json >> "$GITHUB_OUTPUT"

A batch names WHAT to render; the audio and the reference live only in the
private agent repo. Every field is pattern-checked because it flows into
paths, git refs and shell arguments.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

CATEGORIES = ("acknowledgements", "greetings", "signoffs", "teaching")
PATTERNS = {
    "tutor": r"tutor_\d{3}",
    "voice": r"[a-z][a-z0-9_]{0,31}",
    "ref_path": r"lms/team/voice_refs/[A-Za-z0-9_]+\.wav",
    "ref_sha256": r"[0-9a-f]{64}",
    "agent_branch": r"claude/[A-Za-z0-9._-]+(/[A-Za-z0-9._-]+)*",
}


class BatchError(ValueError):
    pass


def category_of(line_id: str, tutor: str) -> str | None:
    """Category of a line id: '<tutor>/<category>/NN', '<tutor>_sample_NN'
    or '<tutor>_sample_line' (teaching). None if it is not one of those."""
    m = re.fullmatch(rf"{tutor}/(acknowledgements|greetings|signoffs)/\d{{2}}", line_id)
    if m:
        return m.group(1)
    if re.fullmatch(rf"{tutor}_sample_(\d{{2}}|line)", line_id):
        return "teaching"
    return None


def load_batch(path: str | Path) -> dict:
    try:
        raw = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise BatchError(f"unreadable batch JSON ({type(exc).__name__})") from None
    if not isinstance(raw, dict):
        raise BatchError("batch must be a JSON object")
    out = {}
    for key, pat in PATTERNS.items():
        val = raw.get(key)
        if not isinstance(val, str) or not re.fullmatch(pat, val):
            raise BatchError(f"field '{key}' missing or not matching {pat}")
        out[key] = val
    if ".." in out["agent_branch"] or out["agent_branch"].endswith((".", "/", ".lock")):
        raise BatchError("agent_branch is not a safe branch name")
    cats = raw.get("categories")
    if not isinstance(cats, list) or not cats or any(c not in CATEGORIES for c in cats):
        raise BatchError(f"categories must be a non-empty subset of {list(CATEGORIES)}")
    out["categories"] = [c for c in CATEGORIES if c in cats]
    lines = raw.get("lines")
    if lines is not None:
        if not isinstance(lines, list) or not lines or not all(isinstance(x, str) for x in lines):
            raise BatchError("lines, when given, must be a non-empty list of line ids")
        for x in lines:
            if category_of(x, out["tutor"]) not in out["categories"]:
                raise BatchError(f"line id {x!r} is not a {out['tutor']} line in the batch's categories")
        out["lines"] = sorted(set(lines))
        # Only run the categories the filter actually touches.
        out["categories"] = [c for c in out["categories"] if any(category_of(x, out["tutor"]) == c for x in lines)]
    unknown = set(raw) - set(PATTERNS) - {"categories", "lines"} - {k for k in raw if k.startswith("_")}
    if unknown:
        raise BatchError(f"unknown field(s): {sorted(unknown)}")
    return out


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: batch.py BATCH_JSON", file=sys.stderr)
        return 2
    try:
        b = load_batch(argv[1])
    except BatchError as exc:
        print(f"::error::{argv[1]}: {exc}", file=sys.stderr)
        return 1
    for key in PATTERNS:
        print(f"{key}={b[key]}")
    print(f"categories={' '.join(b['categories'])}")
    print(f"lines={','.join(b.get('lines', []))}")
    print("categories_json=" + json.dumps(b["categories"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
