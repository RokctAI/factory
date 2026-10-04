#!/usr/bin/env python3
"""Fold the per-category manifests into one <voice>_manifest.json.

    python voice_batch/merge_manifest.py <agent>/lms/team/tutors/CAPS/<tutor> <voice>
    python voice_batch/merge_manifest.py --r3 <agent>/lms/dart/templates/assets/r3_packs/audio <voice>

Category jobs run in parallel and each writes <voice>_manifest.<category>.json,
so they never collide. This merges them (lines and failures in category
order; reference, engine and settings from the most recently updated one)
into the single manifest the app-side tooling reads. Prints counts only.

--r3: R-3 shard jobs each write r3_manifest.<voice>.partNN.json. This folds
every part into r3_manifest.<voice>.json per line id (a part's entry
replaces the one already merged, newest part last) and deletes the parts,
so the audio folder keeps one manifest per voice.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ORDER = ("acknowledgements", "greetings", "signoffs", "teaching", "intro", "handover", "signoff", "timekeeping")


def merge(tutor_dir: Path, voice: str) -> dict | None:
    parts = []
    for cat in ORDER:
        p = tutor_dir / f"{voice}_manifest.{cat}.json"
        if p.exists():
            parts.append(json.loads(p.read_text(encoding="utf-8")))
    if not parts:
        return None
    latest = max(parts, key=lambda m: m.get("updated_at", ""))
    out = {k: latest[k] for k in ("tutor", "kind", "assistant", "agreement_in_place", "voice", "reference", "engine", "settings", "updated_at", "ci_run") if k in latest}
    refs = {m.get("reference", {}).get("sha256") for m in parts}
    if len(refs) != 1:
        out["warning"] = "category manifests were rendered from different references"
    out["categories"] = {m["category"]: f"{voice}_manifest.{m['category']}.json" for m in parts if "category" in m}
    out["lines"] = [e for m in parts for e in m.get("lines", [])]
    out["failed"] = [e for m in parts for e in m.get("failed", [])]
    return out


def merge_r3(audio_dir: Path, voice: str) -> tuple[dict | None, list[Path]]:
    """(merged manifest, part files folded in). None when there is nothing."""
    main_p = audio_dir / f"r3_manifest.{voice}.json"
    base = json.loads(main_p.read_text(encoding="utf-8")) if main_p.exists() else {}
    part_paths = sorted(audio_dir.glob(f"r3_manifest.{voice}.part[0-9][0-9].json"))
    parts = sorted((json.loads(p.read_text(encoding="utf-8")) for p in part_paths),
                   key=lambda m: m.get("updated_at", ""))
    if not parts:
        return (base or None), []
    lines = {e["id"]: e for e in base.get("lines", [])}
    failed = {e["id"]: e for e in base.get("failed", [])}
    for m in parts:
        for e in m.get("lines", []):
            lines[e["id"]] = e
            failed.pop(e["id"], None)
        for e in m.get("failed", []):
            # A failed re-render never hides audio that already passed.
            if e["id"] not in lines:
                failed[e["id"]] = e
    latest = parts[-1]
    out = {k: latest[k] for k in ("kind", "voice", "reference", "engine", "settings", "updated_at", "ci_run") if k in latest}
    refs = {e.get("ref_sha256") for e in lines.values()} - {None}
    if len(refs) > 1:
        out["warning"] = "lines were rendered from different references"
    out["lines"] = sorted(lines.values(), key=lambda e: e["id"])
    out["failed"] = sorted(failed.values(), key=lambda e: e["id"])
    out["needs_listen"] = sum(bool(e.get("needs_listen")) for e in out["lines"])
    return out, part_paths


def main_r3(audio_dir: Path, voice: str) -> None:
    m, parts = merge_r3(audio_dir, voice)
    if m is None:
        print("no r3 manifests found")
        return
    (audio_dir / f"r3_manifest.{voice}.json").write_text(json.dumps(m, indent=1, ensure_ascii=False) + "\n",
                                                          encoding="utf-8")
    for p in parts:
        p.unlink()
    print(f"merged r3 manifest: {len(m['lines'])} passed, {len(m['failed'])} failed, "
          f"{m['needs_listen']} need a listen, {len(parts)} part(s) folded")


if __name__ == "__main__":
    if sys.argv[1] == "--r3":
        main_r3(Path(sys.argv[2]), sys.argv[3])
        sys.exit(0)
    tdir, voice = Path(sys.argv[1]), sys.argv[2]
    m = merge(tdir, voice)
    if m is None:
        print("no category manifests found")
        sys.exit(0)
    (tdir / f"{voice}_manifest.json").write_text(json.dumps(m, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"merged manifest: {len(m['lines'])} passed, {len(m['failed'])} failed")
