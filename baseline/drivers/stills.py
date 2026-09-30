#!/usr/bin/env python3
"""Baseline renders of the agent's still-image scripts, called as functions.

    stills.py tutor-images AGENT_ROOT SOURCE_APPEARANCE_DIR SUBJECT_REL OUT_DIR
    stills.py tour-still   AGENT_ROOT SCREENSHOT_PNG OUT_DIR

tutor-images: the subject's source portrait was pruned from agent main a
week after its renders were verified (the script's own policy), so the
source comes from the last agent commit that still had it; it is copied
into this runner's checkout only and tutor_images.process() re-renders the
card and both avatars from it. out/committed.json records the committed
renders' sha256 and whether the source matches the hash the committed
render manifest names.

tour-still: tour_still.fetch() reads the app repo's moving main branch, so
the screenshot is checked out at a pinned commit instead and
tour_still.downscale() is applied to it. Its two production outputs are the
same bytes, so one file is written.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import sys
from pathlib import Path

RASTER = (".png", ".jpg", ".jpeg", ".webp")


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def tutor_images(agent: Path, src_appearance: Path, subject_rel: str, out: Path) -> int:
    appearance = agent / subject_rel
    renders = appearance / "renders"
    committed = {p.name: sha256(p) for p in sorted(renders.glob("*")) if p.is_file()}
    manifest = json.loads((renders / "manifest.json").read_text(encoding="utf-8"))
    sources = [p for p in sorted(src_appearance.iterdir()) if p.is_file() and p.suffix.lower() in RASTER]
    if len(sources) != 1:
        sys.exit(f"expected one source portrait in the pinned source commit, found {len(sources)}")
    src = appearance / sources[0].name
    shutil.copyfile(sources[0], src)
    source_sha1 = hashlib.sha1(src.read_bytes()).hexdigest()

    os.chdir(agent)
    sys.path.insert(0, str(agent / "lms/team/scripts"))
    import tutor_images as ti

    row = ti.process(Path(subject_rel), check_only=False, force=True)
    out.mkdir(parents=True, exist_ok=True)
    for name in ti.RENDITIONS:
        f = renders / f"{name}{ti.APP_RENDER_EXT}"
        shutil.copyfile(f, out / f.name)
    shutil.copyfile(renders / "manifest.json", out / "render_manifest.json")
    fresh = {p.name: sha256(out / p.name) for p in sorted(out.glob(f"*{ti.APP_RENDER_EXT}"))}
    info = {
        "result": row,
        "source": {"sha256": sha256(src), "sha1_12": source_sha1[:12],
                   "matches_committed_manifest": source_sha1[:12] == manifest.get("source_sha1")},
        "committed_renders_sha256": committed,
        "baseline_renders_sha256": fresh,
        "byte_identical_to_committed": {k: committed.get(k) == v for k, v in fresh.items()},
    }
    (out / "committed.json").write_text(json.dumps(info, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(info, indent=1))
    return 0


def tour_still(agent: Path, screenshot: Path, out: Path) -> int:
    sys.path.insert(0, str(agent / "lms/team/scripts"))
    import tour_still as ts

    still, size = ts.downscale(screenshot.read_bytes())
    out.mkdir(parents=True, exist_ok=True)
    (out / "social-still.png").write_bytes(still)
    info = {"chapter": screenshot.stem, "source_sha256": sha256(screenshot), "size": list(size),
            "still_width": ts.STILL_WIDTH,
            "production_outputs": ["lms/team/marketing/tour/renders/social-still.png",
                                   "lms/nextjs/templates/public/brand/social-still.png"]}
    (out / "still_info.json").write_text(json.dumps(info, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(info, indent=1))
    return 0


def main() -> int:
    cmd, *args = sys.argv[1:]
    if cmd == "tutor-images":
        agent, src, rel, out = args
        return tutor_images(Path(agent).resolve(), Path(src).resolve(), rel, Path(out).resolve())
    if cmd == "tour-still":
        agent, shot, out = args
        return tour_still(Path(agent).resolve(), Path(shot).resolve(), Path(out).resolve())
    sys.exit(f"unknown command {cmd}")


if __name__ == "__main__":
    sys.exit(main())
