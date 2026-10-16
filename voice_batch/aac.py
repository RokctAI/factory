"""Encode a gated 24 kHz mono PCM_16 WAV to AAC (.m4a) for the app's tutor
and host clips.

AAC-LC at 48 kbps mono: about 7x smaller than the WAV and, for speech,
as good as MP3 at 64 kbps (Ray, 2026-10-16: no audible difference, AAC
chosen). Every Android and iOS device decodes it natively. ffmpeg's
built-in encoder, bit-exact flags and no metadata, so the same WAV always
gives the same bytes and re-runs stay idempotent.
"""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

SAMPLE_RATE = 24_000
BITRATE_KBPS = 48
EXT = ".m4a"


def encode(wav: str | Path, m4a: str | Path, bitrate_kbps: int = BITRATE_KBPS) -> str:
    """Write `m4a` from `wav`; returns the encoder used ('ffmpeg')."""
    wav, m4a = Path(wav), Path(m4a)
    m4a.parent.mkdir(parents=True, exist_ok=True)
    ff = shutil.which("ffmpeg")
    if not ff:
        raise RuntimeError("no AAC encoder: install ffmpeg")
    tmp = m4a.with_name(m4a.name + ".part")
    try:
        subprocess.run([ff, "-nostdin", "-loglevel", "error", "-y", "-i", str(wav), "-map_metadata", "-1",
                        "-fflags", "+bitexact", "-flags:a", "+bitexact", "-ac", "1", "-ar", str(SAMPLE_RATE),
                        "-c:a", "aac", "-b:a", f"{bitrate_kbps}k", "-movflags", "+faststart",
                        "-f", "ipod", str(tmp)], check=True)
        tmp.replace(m4a)
    finally:
        tmp.unlink(missing_ok=True)
    return "ffmpeg"
