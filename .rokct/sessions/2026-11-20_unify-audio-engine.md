# 2026-11-20: Unify audio into one rokct-media engine

**Task (Ray)**: "one audio engine. a repo just use it for different things. a radio ad is a tutor lesson voice".

## Done
*   Inventoried every audio copy: factory `voice_batch`, `radio_ads/adfactory`, `social/facebook/music.py`, agent `tiktok_render.py` and `render_voices`, and a dead stub in lessons. All pin the same VibeVoice fork and model revision.
*   Step 1: brought rokct-media level with `voice_batch` (The-Rokct-Protocol #610). 117 tests pass.
*   Step 2: built the parity check (factory #66). Run 44741946544 passed. Text matched on 1,789 lessons (27,613 parts). Audio was byte-identical for Voice A, the Grade 9 host and Voice F.
*   Ran the gatekeeper on both PRs: no FAIL.

## PRs
| PR | State | What it does |
| :--- | :--- | :--- |
| The-Rokct-Protocol #610 | merged 2026-11-20 | Catches rokct-media up with today's lesson renderer |
| factory #66 | ready | Parity check, voice_batch vs rokct-media |
| factory #71 | ready | Keeps `.rokct/sessions/` when a session ends (end_protocol.py synced from the protocol) |
| factory #69 (this report) | draft, never ready | Session report |

## Next
*   Step 3: lessons render through rokct-media behind a `MEDIA_ENGINE` switch. Waits for Ray's go-ahead.
*   Then radio ads, Reels, retiring the old copies, and video as level 3.
