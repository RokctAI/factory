#!/usr/bin/env python3
"""Radio ads factory: a JSON file in, a finished radio advert out.

    python make_ad.py examples/vuka_rides_30.json          # render one ad -> out/<id>/
    python make_ad.py --validate examples/*.json            # check files only, no rendering
    python make_ad.py --watch inbox/                        # render whatever lands in inbox/

See README.md for setup and SCHEMA.md for the ad format.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from adfactory.schema import AdError, load_ad  # noqa: E402


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ads", nargs="*", help="ad JSON file(s) to render")
    ap.add_argument("--watch", metavar="INBOX", help="poll INBOX for *.json and render each new/changed file")
    ap.add_argument("--validate", action="store_true", help="validate only; do not render")
    ap.add_argument("--out", default=str(HERE / "out"), help="output root (default radio_ads/out)")
    ap.add_argument("--failed", help="where failed inbox files go (default: <inbox>/../failed)")
    ap.add_argument("--voices", default=str(HERE / "voices"), help="folder with <voice_id>.wav references")
    ap.add_argument("--cache", default=str(HERE / "cache" / "tts"), help="rendered-line cache folder")
    ap.add_argument("--no-asr", action="store_true", help="skip the speech-recognition word check")
    ap.add_argument("--asr-model", default="base.en", help="faster-whisper model for the word check")
    ap.add_argument("--engine", choices=["vibevoice", "dummy"],
                    help="override render.engine (dummy = tones, for testing the mix)")
    ap.add_argument("--interval", type=float, default=3.0, help="watch poll interval, seconds")
    ap.add_argument("--once", action="store_true", help="with --watch: process the inbox once and exit")
    args = ap.parse_args(argv)

    if args.validate:
        ok = True
        for f in args.ads:
            try:
                ad, warnings = load_ad(f, Path(args.voices))
                print(f"OK   {f}  ({ad['format']}, {ad['duration_s']}s, ~{ad['estimate_speech_s']}s speech, "
                      f"mode {ad['render']['resolved_mode']})")
                for w in warnings:
                    print(f"     warning: {w}")
            except AdError as exc:
                ok = False
                print(f"FAIL {exc}")
        return 0 if ok else 1

    kwargs = dict(voices_dir=Path(args.voices), cache_dir=Path(args.cache), asr=not args.no_asr,
                  asr_model=args.asr_model, engine_override=args.engine)
    if args.watch:
        from adfactory.watch import watch
        try:
            watch(Path(args.watch), Path(args.out), Path(args.failed) if args.failed else None,
                  interval=args.interval, once=args.once, **kwargs)
        except KeyboardInterrupt:
            print("\nstopped")
        return 0

    if not args.ads:
        ap.error("give an ad JSON, --validate FILES, or --watch INBOX")
    from adfactory.pipeline import make_ad
    rc = 0
    for f in args.ads:
        try:
            make_ad(f, Path(args.out), **kwargs)
        except AdError as exc:
            print(f"invalid ad: {exc}", file=sys.stderr)
            rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
