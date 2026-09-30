#!/usr/bin/env python3
"""Markdown pass/fail table from a voice manifest: ids and numbers only
(no line text, transcripts or audio), because the factory repo is public.

    python voice_batch/summary.py <agent>/lms/team/tutors/CAPS/<tutor>/<voice>_manifest.json >> "$GITHUB_STEP_SUMMARY"
    python voice_batch/summary.py <agent>/lms/dart/templates/assets/r3_packs/audio/r3_manifest.<voice>.json >> "$GITHUB_STEP_SUMMARY"
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def fmt(v, nd=2):
    return "n/a" if v is None else (f"{v:.{nd}f}" if isinstance(v, float) else str(v))


def summary(m: dict) -> str:
    rows = [("pass", e) for e in m.get("lines", [])] + [("FAIL", e) for e in m.get("failed", [])]
    listen = sum(bool(e.get("needs_listen")) for e in m.get("lines", []))
    out = [f"### Voice batch `{m.get('tutor') or m.get('kind', '?')}` / `{m.get('voice', '?')}`", "",
           f"{len(m.get('lines', []))} passed, {len(m.get('failed', []))} failed"
           + (f", {listen} respelled for phonics (needs a listen)" if listen else ""), "",
           "| id | category | duration s | median F0 Hz | similarity | ASR exact | seeds | result |",
           "|---|---|---|---|---|---|---|---|"]
    for status, e in rows:
        out.append(f"| `{e['id']}` | {e.get('category', '')} | {fmt(e.get('duration', e.get('duration_s')))} | "
                   f"{fmt(e.get('median_f0', e.get('median_f0_hz')), 1)} | {fmt(e.get('similarity'), 3)} | "
                   f"{fmt(e.get('asr_match'))} | {','.join(map(str, e.get('seeds') or e.get('seeds_tried') or []))} | {status} |")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    p = Path(sys.argv[1])
    print(summary(json.loads(p.read_text(encoding="utf-8"))) if p.exists() else "### Voice batch: no manifest written\n")
