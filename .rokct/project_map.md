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

## Factory engine (this repo)
*   `radio_ads/`: JSON script in, mastered radio ad out (VibeVoice voices, music bed, SFX, loudness).
*   `social/facebook/`: daily opportunity Reel (code-drawn motion graphics, music, voice lines) posted to Facebook/TikTok/YouTube.
*   `voice_batch/`, `.github/workflows/lesson_audio.yml`: lesson voice rendering.
*   Microdrama / TV-ad video: not built yet; tests and findings in `.rokct/sessions/2026-11-20_*`. Shared engine code belongs in rokct-media (The-Rokct-Protocol `core/utils/rokct_media/`).
