#!/usr/bin/env python3
"""Get finished lessons ready for release_on_complete.py: audio from the
stems pre-release, animations from the committed Manim export.

    LESSONS_PAT=... TEAM_ROOT=agent/lms/team python _engine/voice_batch/lesson_release_prep.py \
        --lessons-root . --audio-root agent/lms/lessons/CAPS [--filter maths] [--max 5]

A lesson is ready once EVERY speaker's part is in: each of its speakers
(first tutor, second tutor in a two-part lesson, the grade's host) has a
complete voice/<persona>/manifest.json, every line passed and uploaded
(owner, 2026-10-16: the release copies the parts once everything is there).
For a ready lesson without an audio.mp3 under the audio root this fetches
the tutors' script-segment stems, joins them into <audio root>/<rel>/audio.mp3
with timings.json (exact segment bounds, which release_on_complete reads),
and, when the folder has a good animations.export.json, writes the folder's
animations.json aligned to that audio (release_on_complete uses it as is).
Nothing here is committed: the release run uploads the results.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "ci"))
import lesson_lines as L  # noqa: E402


def part_complete(caps: Path, r: dict, persona: str) -> bool:
    mp = L.manifest_path(caps, r, persona)
    try:
        m = json.loads(mp.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False
    return bool(m.get("complete")) and not m.get("failed") and not m.get("remaining") \
        and all(e.get("asset") and e["asset"].get("sha256") == e.get("sha256") for e in m.get("lines", []))


def ready(lessons_root: Path, folder: Path) -> dict | None:
    try:
        r = L.roles(lessons_root, folder)
    except L.LessonError:
        return None
    speakers = [p for p in (r["first"], r["second"], r["host"]) if p]
    caps = L.curriculum_root(lessons_root)
    return r if speakers and all(part_complete(caps, r, p) for p in speakers) else None


def align_export(lessons_root: Path, folder: Path, audio_seconds: float) -> bool:
    exp = folder / "animations.export.json"
    try:
        anim = json.loads(exp.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False
    if anim.get("export_failed") or "primitives" not in anim:
        return False
    import lesson_animations
    if anim.get("source_sha256") != lesson_animations.scene_sha(folder):
        return False  # stale: the release exports the current scene itself
    anim.pop("source_sha256", None)
    _rel, lm, _ar = L._import_release(lessons_root)
    lm.align_animations(anim, folder / "animations.json", audio_seconds)
    return True


def main(argv: list[str] | None = None) -> int:
    import lesson_audio as LA
    import lesson_stems
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lessons-root", required=True)
    ap.add_argument("--audio-root", required=True)
    ap.add_argument("--filter", default="")
    ap.add_argument("--max", type=int, default=5)
    ap.add_argument("--repo", default=lesson_stems.REPO)
    args = ap.parse_args(argv)
    lessons_root = Path(args.lessons_root).resolve()
    audio_root = Path(args.audio_root).resolve()
    caps = L.curriculum_root(lessons_root)
    work = audio_root.parent / ".lesson_stems"
    made = 0
    for folder in L.discover(lessons_root):
        rel = str(folder.relative_to(caps))
        if args.filter and args.filter not in rel:
            continue
        if made >= args.max:
            break
        dst = audio_root / rel
        if (dst / "audio.mp3").is_file():
            continue
        r = ready(lessons_root, folder)
        if not r:
            continue
        if lesson_stems.main(["fetch", "--lessons-root", str(lessons_root), "--stems-root", str(work),
                              "--lesson", rel, "--repo", args.repo]) != 0:
            print(f"::warning::{rel}: stems incomplete on the pre-release; not releasing")
            continue
        if LA.main(["assemble", "--lessons-root", str(lessons_root), "--stems-root", str(work),
                    "--lesson", rel, "--out", str(dst)]) != 0:
            continue
        seconds = LA.probe_seconds(dst / "audio.mp3")
        anim = align_export(lessons_root, folder, seconds)
        print(f"{rel}: audio {seconds:.1f}s from stems, animations {'from export' if anim else 'exported at release'}")
        made += 1
    print(f"{made} lesson(s) prepared from stems")
    return 0


if __name__ == "__main__":
    sys.exit(main())
