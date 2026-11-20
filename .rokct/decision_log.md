# Architectural Decision Log (ADR)

**Purpose**: Record clear "Subject Closed" decisions to prevent re-debating them.

| ID | Date | Topic | Decision | Status |
| :--- | :--- | :--- | :--- | :--- |
| ADR-TT-1 | 2026-11-20 | Talking tutors: delivery | Pictures + a timing file, not video. Reason (Ray): saves data, nothing baked into the app, same idea as Manim board data. | **DECIDED** |
| ADR-TT-2 | 2026-11-20 | Talking tutors: storage | Face pictures live in the lessons repo and download via the backend. Reason (Ray): the app must not carry per-tutor content. | **DECIDED** |
| ADR-TT-3 | 2026-11-20 | Talking tutors: scope | Tutors on screen for intros, sign-offs and the sample lesson only; hosts whenever they talk; no faces during break questions. Reason (Ray): hosts talk little; keep it small and polished. | **DECIDED** |
| ADR-TT-4 | 2026-11-20 | Talking tutors: look | LivePortrait jaw/eyes + MuseTalk lips. Reason: best lips and keeps blinks; Wav2Lip blurry, JoyVASA off-identity. | **DECIDED** |
| ADR-TT-5 | 2026-11-20 | Talking tutors: mouth area | Mouth pictures start below the nostrils. Reason: starting higher made the nose move oddly (Ray's feedback). | **DECIDED** |
| ADR-TT-6 | 2026-11-20 | PR flow | One draft report-only PR per session, never ready; code in separate PRs; gatekeeper before any PR goes ready. Reason: Ray's standing rules. | **DECIDED** |
| ADR-TT-7 | 2026-11-20 | Talking tutors: format | App gets pictures plus timing files, not video; one shared mouth-picture set per member and style. Reason (Ray): 12 tutors per learner must stay small; greetings can share pictures. | **DECIDED** |
| ADR-TT-8 | 2026-11-20 | Talking tutors: styles | Separate 'clear' (Grade R-3) and 'normal' packs. Reason (Ray): R-3 needs a wider mouth. | **DECIDED** |
| ADR-TT-9 | 2026-11-20 | Talking tutors: no-voice members | Draw pictures from a stand-in voice sample; time real lines later. Reason (Ray): get every member's pack ready now. | **DECIDED** |
