#!/usr/bin/env python3
# Copyright (c) 2026 RokctAI
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Records Level 6 production outputs on a lesson job card.

After the asset triple is uploaded, this writes the download URLs plus
sha256 + byte size for each asset onto the card. The field names match
replay_sdk's UpcomingSession.fromJson (manifest_url/audio_url/animation_url,
*_checksum, *_size_bytes) so the backend's get_upcoming_sessions endpoint can
lift them straight onto the payload the app verifies downloads against.
"""
import argparse
import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def set_field(content, field, value):
    if re.search(rf"^{field}:", content, re.MULTILINE):
        return re.sub(rf"^{field}:.*", f"{field}: {value}", content, flags=re.MULTILINE)
    parts = content.rsplit("---", 1)
    return f"{parts[0]}{field}: {value}\n---{parts[1]}"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--card", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--base-url", required=True,
                    help="release download base, no trailing slash")
    args = ap.parse_args()

    out = Path(args.out_dir)
    assets = {
        "manifest": "manifest.json",
        "audio": "audio.mp3",
        "animation": "animations.json",
    }
    content = Path(args.card).read_text(encoding="utf-8")
    for key, name in assets.items():
        path = out / name
        content = set_field(content, f"{key}_url", f"{args.base_url}/{name}")
        content = set_field(content, f"{key}_checksum", sha256_of(path))
        content = set_field(content, f"{key}_size_bytes", str(path.stat().st_size))
    content = set_field(content, "produced_at",
                        datetime.now(timezone.utc).replace(microsecond=0).isoformat())
    Path(args.card).write_text(content, encoding="utf-8")
    print(f"Recorded production metadata on {args.card}")


if __name__ == "__main__":
    main()
