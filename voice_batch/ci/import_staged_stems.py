#!/usr/bin/env python3
"""Move lesson stems rendered outside CI (a sandbox box with no upload
route) from a staging branch of the lessons repo onto the stems
pre-releases, and their records onto lessons main.

    LESSONS_PAT=... import_staged_stems.py --stage _stage --lessons-root _lessons

The staging branch holds, at the paths a render job uses:
    school/curriculum/CAPS/<rel>/voice/<persona>/manifest.json (+ qc_failed.json)
    _sandbox_stems/<rel>/voice/<persona>/<key>.mp3
Each staged record is copied into the lessons main checkout and
lesson_stems.py push uploads the MP3s it lists and commits the records to
main with [skip ci], exactly as a lesson_audio.yml job's final push does.
A lesson part whose main manifest already has passed lines the staged one
lacks (a CI job rendered it too) is skipped, so CI's work is never
overwritten. Logs lesson paths, personas and counts only. The staging
branch is left as it is; whoever stages deletes or resets it.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import lesson_lines as L  # noqa: E402

STEMS_DIR = "_sandbox_stems"


def staged(stage: Path) -> dict[str, list[str]]:
    """{persona: [lesson rel]} for every staged manifest."""
    caps = L.curriculum_root(stage)
    out: dict[str, list[str]] = {}
    for m in sorted(caps.glob(f"*/session/*/*/*/*/{L.STEM_DIR}/*/{L.MANIFEST}")):
        persona = m.parent.name
        rel = str(m.parent.parent.parent.relative_to(caps))
        out.setdefault(persona, []).append(rel)
    return out


def keys_passed(p: Path) -> set[str]:
    if not p.is_file():
        return set()
    return {e["key"] for e in json.loads(p.read_text(encoding="utf-8")).get("lines", [])}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stage", required=True, help="checkout of the staging branch")
    ap.add_argument("--lessons-root", required=True, help="checkout of lessons main (records are pushed from here)")
    args = ap.parse_args(argv)
    stage, lessons_root = Path(args.stage).resolve(), Path(args.lessons_root).resolve()
    scaps, mcaps = L.curriculum_root(stage), L.curriculum_root(lessons_root)
    total = 0
    for persona, rels in staged(stage).items():
        take = []
        for rel in rels:
            src = scaps / rel / L.STEM_DIR / persona
            dst = mcaps / rel / L.STEM_DIR / persona
            if not (mcaps / rel).is_dir():
                print(f"::warning::skip {rel} {persona}: no such lesson on main")
                continue
            extra = keys_passed(dst / L.MANIFEST) - keys_passed(src / L.MANIFEST)
            if extra:
                print(f"::warning::skip {rel} {persona}: main has {len(extra)} passed line(s) the staged record lacks")
                continue
            dst.mkdir(parents=True, exist_ok=True)
            for n in (L.MANIFEST, "qc_failed.json"):
                if (src / n).is_file():
                    shutil.copyfile(src / n, dst / n)
            take.append(rel)
        if not take:
            continue
        print(f"{persona}: importing {len(take)} lesson part(s)")
        subprocess.run([sys.executable, str(HERE / "lesson_stems.py"), "push", "--lessons-root", str(lessons_root),
                        "--stems-root", str(stage / STEMS_DIR), "--persona", persona, "--lessons", ",".join(take)],
                       check=True)
        total += len(take)
    print(f"{total} lesson part(s) imported")
    return 0


if __name__ == "__main__":
    sys.exit(main())
