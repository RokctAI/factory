# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""Render every look the daily Reel can take, for review before it posts.

One clip per post type (grant, tender, investor, tip) per background motif
(four per type, see motion.MOTIFS), each with its day's music and voice
lines, scaled to 540x960 for a light preview. The real posts are 1080x1920.

    python social/facebook/preview.py --opportunities ../opportunities --out build/preview
"""

import argparse
import datetime as dt
import json
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import opportunity_post as op  # noqa: E402

STILLS = (0.6, 2.4, 6.0, 10.6)  # seconds: count, climb/deadline, full card, end card


def samples(repo: Path, today: dt.date):
    grants = [c for c in op.grant_candidates(repo) if c["deadline"] >= today + dt.timedelta(days=op.MIN_DAYS_LEFT)]
    ranged = next((c for c in grants if " to " in op.headline_for(c)), None)
    single = next((c for c in grants if " to " not in op.headline_for(c)), None)
    floor = today + dt.timedelta(days=op.MIN_DAYS_LEFT)
    tender = next((c for c in op.tender_candidates(repo) if c["deadline"] >= floor), None)
    return [
        ("grant-range", ranged),
        ("grant", single),
        ("tender", tender),
        ("investor", next(op.equity_candidates(repo), None)),
        ("tip", next(op.tip_candidates())),
    ]


def one(job):
    name, opp, motif, today, out = job
    from motion import MOTIF_NAMES, MOTIFS, motif_for, render_motion
    from music import add_voiceover, render_music, tempo_for

    names = MOTIFS[opp["kind"]]
    # A seed whose motif is the one asked for, keeping the day's rotation.
    seed = today.toordinal() + 1000 * op.KIND_SEED.get(opp["kind"], 0)
    seed += (motif - seed % len(names)) % len(names)
    motif = motif_for(opp["kind"], seed)
    folder = out / f"{name}-{motif}"
    folder.mkdir(parents=True, exist_ok=True)
    shown, days_left = op.scene_facts(opp, today)
    render_music(seed, op.DURATION_SECONDS, folder / "music.wav")
    add_voiceover(folder / "music.wav", op.DURATION_SECONDS, opener=opp["kind"] != "Funding tip")
    render_motion(shown, op.headline_for(opp), days_left, seed, op.DURATION_SECONDS, tempo_for(seed), folder / "motion.mp4")
    clip = out / f"{name}-{motif}.mp4"
    subprocess.run(
        [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-i", str(folder / "motion.mp4"), "-i", str(folder / "music.wav"),
            "-vf", "scale=540:960", "-c:v", "libx264", "-crf", "30", "-preset", "veryfast",
            "-c:a", "aac", "-b:a", "96k", "-shortest", "-movflags", "+faststart", str(clip),
        ],
        check=True,
    )
    # A static strip of the beats: the count, the deadline landing, the
    # full card and the end card.
    strip = clip.with_suffix(".jpg")
    picks = "+".join(f"eq(n\\,{int(s * 30)})" for s in STILLS)
    subprocess.run(
        ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(folder / "motion.mp4"),
         "-vf", f"select='{picks}',scale=360:640,tile={len(STILLS)}x1:padding=12:color=0x09090b",
         "-frames:v", "1", "-vsync", "0", "-q:v", "3", str(strip)],
        check=True,
    )
    return {
        "type": name,
        "motif": motif,
        "motif_name": MOTIF_NAMES[motif],
        "headline": op.headline_for(opp),
        "title": opp["title"],
        "video": clip.name,
        "strip": strip.name,
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--opportunities", type=Path, required=True)
    ap.add_argument("--out", type=Path, default=Path("build/preview"))
    ap.add_argument("--today", type=dt.date.fromisoformat, default=dt.date.today())
    args = ap.parse_args(argv)
    args.out.mkdir(parents=True, exist_ok=True)
    jobs = [
        (name, opp, motif, args.today, args.out)
        for name, opp in samples(args.opportunities, args.today)
        if opp
        for motif in range(4)
    ]
    with ProcessPoolExecutor() as pool:
        rows = list(pool.map(one, jobs))
    (args.out / "manifest.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{len(rows)} clips in {args.out}")


if __name__ == "__main__":
    main()
