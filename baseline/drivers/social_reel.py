#!/usr/bin/env python3
"""Baseline render of the daily opportunity Reel: one fixed card, one fixed
date (so one fixed seed), through the Reel's own render functions.

    social_reel.py --opportunities DIR --agent DIR --out DIR \
        --card-key grant:<stem> --today YYYY-MM-DD --stream grant

Calls opportunity_post.make_brief, make_motion (motion.py + music.py) and
render (the agent's tiktok_render.py) for the Facebook cut, then
preview.one for the same card at motif 0. It never calls
opportunity_post.main, so the ledger and the platform posters are never
reached; tiktok.py and youtube.py are not even imported. As a second lock,
every HTTP entry point in this process raises before the renders start.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve()
FACEBOOK = HERE.parents[2] / "social" / "facebook"


class NetworkBlocked(RuntimeError):
    pass


def block_network() -> None:
    def refuse(*_a, **_k):
        raise NetworkBlocked("network access is blocked in the baseline render")

    import socket
    import urllib.request

    import requests

    requests.sessions.Session.request = refuse
    urllib.request.urlopen = refuse
    socket.create_connection = refuse
    socket.socket.connect = refuse


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--opportunities", type=Path, required=True)
    ap.add_argument("--agent", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--card-key", required=True)
    ap.add_argument("--today", type=dt.date.fromisoformat, required=True)
    ap.add_argument("--stream", default="grant")
    a = ap.parse_args()

    sys.path.insert(0, str(FACEBOOK))
    import opportunity_post as op
    import preview

    block_network()
    timings = {}
    t = time.time()
    opp = next((c for c in op.grant_candidates(a.opportunities) if c["key"] == a.card_key), None)
    if opp is None:
        sys.exit(f"card {a.card_key} is not a postable grant at this opportunities commit")
    brief = op.make_brief(opp, a.today, a.stream)
    folder = a.out / "reel" / brief["id"]
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "brief.json").write_text(json.dumps(brief, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    op.make_motion(opp, a.today, folder)
    timings["motion_and_music_s"] = round(time.time() - t, 1)
    t = time.time()
    mp4 = op.render(folder, a.agent.resolve())
    timings["tiktok_render_s"] = round(time.time() - t, 1)
    t = time.time()
    row = preview.one(("grant", opp, 0, a.today, a.out / "preview"))
    timings["preview_s"] = round(time.time() - t, 1)
    seed = a.today.toordinal() + 1000 * op.KIND_SEED.get(opp["kind"], 0)
    info = {"card_key": a.card_key, "today": a.today.isoformat(), "stream": a.stream, "seed": seed,
            "headline": op.headline_for(opp), "reel": str(mp4.relative_to(a.out)), "preview": row,
            "timings": timings}
    (a.out / "render_info.json").write_text(json.dumps(info, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(info, indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
