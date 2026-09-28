#!/usr/bin/env python3
"""Markdown job summary for one rendered ad, from its report.json.

    python radio_ads/ci/summary.py radio_ads/out/<id>/report.json >> "$GITHUB_STEP_SUMMARY"
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def _fmt(v, unit=""):
    return "n/a" if v is None else f"{v}{unit}"


def summary(report: dict) -> str:
    t = report.get("timing", {})
    target = report.get("target", {})
    measured = report.get("loudness", {}).get("measured", {})
    asr = report.get("asr") or {}
    render = report.get("render", {})
    out = [
        f"### Radio ad `{report.get('id')}` ({report.get('client', '')})",
        "",
        "| | |",
        "|---|---|",
        f"| Duration | {_fmt(t.get('actual_duration_s'), ' s')} (target {_fmt(target.get('duration_s'), ' s')}, "
        f"{t.get('status', 'n/a')}) |",
        f"| Words | {_fmt(t.get('words'))} at {_fmt(t.get('words_per_minute'))} wpm, tempo x{_fmt(t.get('tempo_applied'))} |",
    ]
    for kind in ("mp3", "wav"):
        m = measured.get(kind)
        if m:
            out.append(f"| {kind.upper()} loudness | {_fmt(m.get('integrated_lufs'), ' LUFS')} "
                       f"(target {_fmt(target.get('loudness_lufs'))}), true peak {_fmt(m.get('true_peak_dbtp'), ' dBTP')} "
                       f"(ceiling {_fmt(target.get('true_peak_dbtp'))}) |")
    if asr:
        out.append(f"| Word check | WER {_fmt(asr.get('wer'))} ({asr.get('asr_model', '')}) |")
    else:
        out.append("| Word check | skipped |")
    out.append(f"| Render | {render.get('mode_used', 'n/a')}, {_fmt(render.get('lines_rendered'))} lines rendered, "
               f"{_fmt(render.get('lines_cached'))} cached, {_fmt(report.get('wall_time_s'), ' s')} wall |")
    worst = sorted((ln for ln in report.get("lines", []) if ln.get("wer") is not None),
                   key=lambda ln: ln["wer"], reverse=True)[:3]
    if worst:
        out += ["", "Lines with the highest word error rate:", ""]
        for ln in worst:
            out.append(f"* WER {ln['wer']}: `{ln.get('speaker')}` \"{ln.get('text')}\" heard as \"{ln.get('asr')}\"")
    warnings = report.get("warnings") or []
    if warnings:
        out += ["", "Warnings:", ""] + [f"* {w}" for w in warnings]
    return "\n".join(out) + "\n"


def main(argv: list[str]) -> int:
    print(summary(json.loads(Path(argv[1]).read_text(encoding="utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
