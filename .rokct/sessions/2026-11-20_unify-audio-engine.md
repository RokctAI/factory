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
| The-Rokct-Protocol #610 | merged | Catches rokct-media up with today's lesson renderer |
| factory #66 | merged | Parity check, voice_batch vs rokct-media |
| factory #71 | merged | Keeps `.rokct/sessions/` when a session ends |
| factory #73 | draft until parity passes | Step 3: lessons render with rokct-media (MEDIA_ENGINE switch, default rokct-media, rollback by variable) |
| The-Rokct-Protocol #611 | ready | Steps 4-5: radio ads (compose) and Reel music move into rokct-media |
| factory #74 | draft, needs #611 | Steps 4-6: radio ads and Reels call rokct-media; lesson6 vibevoice option gone |
| lessons #283 | ready | Step 6: dead vibevoice backend removed |
| The-Rokct-Protocol #612 | ready, stacks on #611 | Step 7: vertical video assembly (level 3 groundwork) |
| agent #640 | draft, needs #612 | Step 7: tiktok_render imports the assembly |
| factory #69 (this report) | draft, never ready | Session report |

## Ray's go-ahead
2026-11-20 15:21Z: "go till you finish" (steps 3-7).

## Next
*   Retire factory render_takes.py/qc.py and agent render_voices.py once lesson renders have run cleanly on rokct-media (they are the rollback until then).
*   Repin factory #74 to #611's merge commit, then ready it.
