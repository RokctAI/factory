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


def pace_cell(p) -> str:
    if not p or p.get("wpm") is None:
        return "n/a"
    flag = p.get("flag")
    return (f"{p['wpm']:.0f} ({p['target_wpm']:g}±{p['tolerance_wpm']:g})"
            + (f" **{flag}**" if flag in ("over", "under") else ""))


def summary(m: dict) -> str:
    rows = [("pass", e) for e in m.get("lines", [])] + [("FAIL", e) for e in m.get("failed", [])]
    listen = sum(bool(e.get("needs_listen")) for e in m.get("lines", []))
    rem = m.get("remaining") or []
    left = sum(len(v) for v in rem.values()) if isinstance(rem, dict) else len(rem)
    out = [f"### Voice batch `{m.get('tutor') or m.get('kind', '?')}` / `{m.get('voice', '?')}`", "",
           f"{len(m.get('lines', []))} passed, {len(m.get('failed', []))} failed"
           + (f", {listen} need a listen (phonics respelling or pronunciation)" if listen else "")
           + (f", {left} left for a continuation run (time budget)" if left else ""), "",
           "| id | category | duration s | median F0 Hz | similarity | ASR exact | wpm (target, report-only) | seeds | result |",
           "|---|---|---|---|---|---|---|---|---|"]
    failed = m.get("failed", [])
    if failed:
        # One line: count + ids (no text, no audio: this summary is public).
        out[4:4] = [f"QC failed (every seed round): {len(failed)} line(s): "
                    + ", ".join(f"`{e['id']}`" for e in failed), ""]
    for status, e in rows:
        out.append(f"| `{e['id']}` | {e.get('category', '')} | {fmt(e.get('duration', e.get('duration_s')))} | "
                   f"{fmt(e.get('median_f0', e.get('median_f0_hz')), 1)} | {fmt(e.get('similarity'), 3)} | "
                   f"{fmt(e.get('asr_match'))} | {pace_cell(e.get('pace'))} | {','.join(map(str, e.get('seeds') or e.get('seeds_tried') or []))} | {status} |")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    p = Path(sys.argv[1])
    print(summary(json.loads(p.read_text(encoding="utf-8"))) if p.exists() else "### Voice batch: no manifest written\n")
