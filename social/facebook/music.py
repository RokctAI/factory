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

"""Soundtrack for the daily Reel: rokct-media's royalty-free music synth
(rokct_media.compose.reel_music, moved there from this file 2026-11-20)
plus the Reel's own voice lines, laid in by rokct-media.

render_music, tempo_for and RATE are re-exported for opportunity_post.py and
preview.py; which line plays where (add_voiceover) stays here.
"""

from pathlib import Path

from rokct_media.compose.reel_music import RATE, render_music, tempo_for  # noqa: F401
from rokct_media.compose.reel_music import lay as _lay

ASSETS = Path(__file__).resolve().parent / "assets"
# Shared voice lines, rendered by the radio-ads factory from
# radio_ads/inbox/facebook_reel_brand_15.json, facebook_reel_open_15.json and
# facebook_reel_follow_15.json; tender Reels add radio_ads/reel_jobs/
# facebook_reel_tenderassist_15.json, rendered at build time by the Reel
# workflow (gated by REEL_SPONSOR_VOICE) and never committed.
VOICE_BRAND = ASSETS / "voice_brand.wav"
VOICE_OPEN = ASSETS / "voice_open.wav"
VOICE_CLOSE = ASSETS / "voice_close.wav"
VOICE_SPONSOR = ASSETS / "voice_tenderassist.wav"
SPONSOR_PAUSE = 0.3  # seconds between the sponsor line and the follow line
OPEN_PAUSE = 0.7  # seconds between "ROKCT" and the opening line


def add_voiceover(music: Path, duration, opener=True, sponsor=False):
    """ROKCT (a man's voice) on the first beat, the opening line straight
    after it (unless opener is False), the follow line over the close. With
    sponsor, "Brought to you by TenderAssist" ends just before the follow
    line; until its asset is rendered it is skipped."""
    brand_end = _lay(music, VOICE_BRAND, lambda length: 0.15)
    if opener:
        _lay(music, VOICE_OPEN, lambda length: (brand_end or 0) + OPEN_PAUSE)
    close = {}

    def close_at(length):
        close["at"] = max(0.5, duration - length - 0.35)
        return close["at"]

    _lay(music, VOICE_CLOSE, close_at)
    if sponsor and "at" in close:
        _lay(music, VOICE_SPONSOR, lambda length: max(0.5, close["at"] - length - SPONSOR_PAUSE))
