# Project Context Map

**Purpose**: A high-level map of the codebase to help the Agent understand where things are without searching deeply every time.

**Rule**: Update this map when you explore a new part of the codebase.

## Key Directories
*   `The-Rokct-Protocol/core`: Mandates (Authority, Communication).
*   `The-Rokct-Protocol/coding`: Tech stack and Design systems.
*   `The-Rokct-Protocol/templates`: Templates (Memory, Logs).
*   `The-Rokct-Protocol/`: (Submodule: **Do Not Touch**).

## Critical Files
*   `README.md`: Entry point.
*   `system/memory.md`: User preferences and lessons.

## Audio (one-engine move, 2026-11-20)
*   `voice_batch/`: today's lesson renderer (split, respell, render takes, QC gate, stitch).
*   `voice_batch/ci/media_parity.py` + `.github/workflows/media_parity.yml`: proves rokct-media gives byte-identical takes, verdicts and clips to `voice_batch`.
*   `radio_ads/adfactory/`: radio ads (own model loader, bed, ducking, loudness). Moves to rokct-media level 2 later.
*   `social/facebook/music.py`: Reel audio mixing. Moves later.
*   rokct-media itself: The-Rokct-Protocol `core/utils/rokct_media` (level 1 speech).
