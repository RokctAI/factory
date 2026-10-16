#!/usr/bin/env python3
"""Export each lesson's Manim scene once and keep it in the lesson folder.

    TEAM_ROOT=.agent/lms/team python voice_batch/lesson_animations.py \
        --lessons-root _lessons [--max 200] [--only <rel>,...] [--commit]

For every session package whose manim_scene.py has no animations.export.json
beside it (or whose export was made from an older scene), runs the lessons
repo's manim_exporter.export_scene and writes animations.export.json: the
primitives on the scene's own clock, plus "source_sha256" of the scene. The
lesson release aligns it to the real audio (lesson_release_prep.py), so the
scene is run once per change instead of at every release. A scene that
fails to export gets a marker ({"export_failed": ..., "source_sha256"}) so
it is not retried until it changes. With --commit the
new exports go to lessons main ([skip ci]) via ci/lesson_stems.py.

Logs lesson paths and counts only; the exporter's own output is swallowed.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "ci"))
import lesson_lines as L  # noqa: E402

EXPORT = "animations.export.json"


def scene_sha(folder: Path) -> str:
    return hashlib.sha256((folder / "manim_scene.py").read_bytes()).hexdigest()


def stale(folder: Path) -> bool:
    if not (folder / "manim_scene.py").is_file():
        return False
    try:
        cur = json.loads((folder / EXPORT).read_text(encoding="utf-8")).get("source_sha256")
    except (OSError, ValueError):
        return True
    return cur != scene_sha(folder)


def export(lessons_root: Path, folder: Path) -> int:
    """Write the folder's export; returns the primitive count."""
    sys.path.insert(0, str(L.lessons_scripts(lessons_root)))
    from manim_exporter import export_scene
    out = folder / EXPORT
    sink = io.StringIO()
    with contextlib.redirect_stdout(sink), contextlib.redirect_stderr(sink):
        anim = export_scene(str(folder / "manim_scene.py"), str(out))
    anim["source_sha256"] = scene_sha(folder)
    out.write_text(json.dumps(anim, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return len(anim.get("primitives", []))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lessons-root", required=True)
    ap.add_argument("--max", type=int, default=200)
    ap.add_argument("--only", default="")
    ap.add_argument("--commit", action="store_true")
    args = ap.parse_args(argv)
    lessons_root = Path(args.lessons_root).resolve()
    caps = L.curriculum_root(lessons_root)
    only = {x for x in args.only.split(",") if x}
    todo = [f for f in L.discover(lessons_root)
            if (not only or str(f.relative_to(caps)) in only) and stale(f)]
    print(f"{len(todo)} lesson(s) need a Manim export; doing up to {args.max}")
    done, failed = [], 0
    for f in todo[:args.max]:
        rel = str(f.relative_to(caps))
        try:
            n = export(lessons_root, f)
        except Exception as exc:  # noqa: BLE001 - one bad scene must not stop the rest
            failed += 1
            print(f"::warning::{rel}: export failed ({type(exc).__name__})")
            # A marker, so a broken scene is not retried until it changes;
            # the release then runs the exporter itself, as before.
            (f / EXPORT).write_text(json.dumps({"export_failed": type(exc).__name__,
                                                "source_sha256": scene_sha(f)}, indent=1) + "\n",
                                    encoding="utf-8")
            done.append(rel)
            continue
        done.append(rel)
        print(f"{rel}: {n} primitive(s)")
    print(f"exported {len(done)}, failed {failed}, left {max(0, len(todo) - args.max)}")
    if args.commit and done:
        import lesson_stems
        paths = [f"school/curriculum/CAPS/{rel}/{EXPORT}" for rel in done]
        for i in range(0, len(paths), 100):
            lesson_stems.commit_push(lessons_root, paths[i:i + 100],
                                     f"Manim export for {len(paths[i:i + 100])} lesson(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
