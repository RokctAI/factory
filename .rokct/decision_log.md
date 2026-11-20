# Decision Log

| Date | Decision | Reason | By |
|---|---|---|---|
| 2026-11-20 | Talking tutors use pictures + a timing file, not video | Saves data; nothing baked into the app; same approach as Manim board animations | Ray |
| 2026-11-20 | Face pictures live in the lessons repo and download via the backend | The app must not carry per-tutor content | Ray |
| 2026-11-20 | Tutors on screen only for intros, sign-offs and the sample lesson; hosts whenever they talk; no faces during break questions | Hosts talk little; keeps scope small and polished | Ray |
| 2026-11-20 | Look = LivePortrait jaw/eyes + MuseTalk lips ("combo") | Best lip shape and keeps blinks; Wav2Lip blurry, JoyVASA off-identity | Ray |
| 2026-11-20 | Mouth pictures start below the nostrils | Starting higher made the nose move oddly | Ray (feedback), Claude (fix) |
| 2026-11-20 | Each session opens one draft, report-only PR that is never marked ready; code goes in separate PRs | Ray's reporting rule | Ray |
| 2026-11-20 | Run the protocol's gatekeeper skill before marking any code PR ready | Ray's PR rule | Ray |
