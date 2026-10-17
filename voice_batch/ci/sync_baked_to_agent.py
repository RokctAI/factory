#!/usr/bin/env python3
"""Copy the audio the app bakes in from the voice repo (lessons voices/) into
an agent checkout, at the app's paths.

    python voice_batch/ci/sync_baked_to_agent.py --voices ../lessons --agent ../agent [--check]

Ray (2026-10-16/17): the app bakes only the tutor-card samples of the first
three tutors (BAKED_TUTORS) plus images. Everything else (host and tutor
standing lines, lesson audio, R-3 packs) stays in lessons and is downloaded
on demand through the backend, so it is never copied here.

  voices/team/tutors/CAPS/<tutor>/samples/*.{m4a,mp3,wav} and *.timings.json
      -> lms/team/tutors/CAPS/<tutor>/samples/  (agent's sync_team_assets
         workflow then copies them into the app's assets/team trees)

A baked sample that no longer exists in lessons is removed from agent;
nothing outside those sample folders is touched. Paths and counts only,
never contents. Prints `changed=<n>` for the workflow.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import voice_paths as vp  # noqa: E402

BAKED_TUTORS = ("tutor_001", "tutor_002", "tutor_003")
AUDIO_RE = re.compile(r".+\.(mp3|m4a|wav)|.+\.timings\.json")


def _sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def _samples(base: Path) -> dict[str, Path]:
    """{tutor/samples/name: file} for the baked tutors' samples under base."""
    out = {}
    for t in BAKED_TUTORS:
        d = base / t / "samples"
        if d.is_dir():
            for f in sorted(d.iterdir()):
                if f.is_file() and AUDIO_RE.fullmatch(f.name):
                    out[f"{t}/samples/{f.name}"] = f
    return out


def sync(voices: Path, agent: Path, check: bool = False, root: str | None = None) -> dict[str, list[str]]:
    want = _samples(voices / vp.team_base(root) / "tutors" / "CAPS")
    if not want:
        # An empty or missing voices/ tree would otherwise delete every
        # baked sample in agent.
        raise SystemExit("::error::no baked samples found in the voice repo checkout; refusing to sync")
    dest = agent / vp.AGENT_TEAM / "tutors" / "CAPS"
    have = _samples(dest)
    added, updated, removed = [], [], []
    for rel, src in want.items():
        dst = dest / rel
        if not dst.exists():
            added.append(rel)
        elif _sha(dst) != _sha(src):
            updated.append(rel)
        else:
            continue
        if not check:
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(src.read_bytes())
    for rel in sorted(set(have) - set(want)):
        removed.append(rel)
        if not check:
            have[rel].unlink()
    return {"added": added, "updated": updated, "removed": removed}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--voices", required=True, help="checkout of the voice repo (lessons)")
    ap.add_argument("--agent", required=True, help="checkout of RokctAI/agent")
    ap.add_argument("--check", action="store_true", help="report only")
    a = ap.parse_args()
    r = sync(Path(a.voices), Path(a.agent), a.check)
    for k, v in r.items():
        print(f"{k}: {len(v)}")
    changed = sum(len(v) for v in r.values())
    print(f"changed={changed}")
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a", encoding="utf-8") as fh:
            fh.write(f"changed={changed}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
