#!/usr/bin/env python3
"""Fold the per-category manifests into one <voice>_manifest.json.

    python voice_batch/merge_manifest.py <agent>/lms/team/tutors/CAPS/<tutor> <voice>

Category jobs run in parallel and each writes <voice>_manifest.<category>.json,
so they never collide. This merges them (lines and failures in category
order; reference, engine and settings from the most recently updated one)
into the single manifest the app-side tooling reads. Prints counts only.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ORDER = ("acknowledgements", "greetings", "signoffs", "teaching")


def merge(tutor_dir: Path, voice: str) -> dict | None:
    parts = []
    for cat in ORDER:
        p = tutor_dir / f"{voice}_manifest.{cat}.json"
        if p.exists():
            parts.append(json.loads(p.read_text(encoding="utf-8")))
    if not parts:
        return None
    latest = max(parts, key=lambda m: m.get("updated_at", ""))
    out = {k: latest[k] for k in ("tutor", "voice", "reference", "engine", "settings", "updated_at", "ci_run") if k in latest}
    refs = {m.get("reference", {}).get("sha256") for m in parts}
    if len(refs) != 1:
        out["warning"] = "category manifests were rendered from different references"
    out["categories"] = {m["category"]: f"{voice}_manifest.{m['category']}.json" for m in parts if "category" in m}
    out["lines"] = [e for m in parts for e in m.get("lines", [])]
    out["failed"] = [e for m in parts for e in m.get("failed", [])]
    return out


if __name__ == "__main__":
    tdir, voice = Path(sys.argv[1]), sys.argv[2]
    m = merge(tdir, voice)
    if m is None:
        print("no category manifests found")
        sys.exit(0)
    (tdir / f"{voice}_manifest.json").write_text(json.dumps(m, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"merged manifest: {len(m['lines'])} passed, {len(m['failed'])} failed")
