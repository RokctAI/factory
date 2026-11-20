# Architectural Decision Log (ADR)

**Purpose**: Record clear "Subject Closed" decisions to prevent re-debating them.

| ID | Date | Topic | Decision | Status |
| :--- | :--- | :--- | :--- | :--- |
| ADR-001 | 2026-11-20 | Audio engine | One audio engine, rokct-media, used for lessons, radio ads and Reels. Reason (Ray): "a radio ad is a tutor lesson voice"; one copy stops the copies drifting apart. | **DECIDED** |
| ADR-002 | 2026-11-20 | Move order | Catch rokct-media up first, then prove parity, then switch lessons behind a switch, then radio ads, Reels, retire old copies, and video last. Reason: lesson rendering must keep working at every step. | **DECIDED** |
| ADR-003 | 2026-11-20 | Parity bar | Lessons switch only when both engines give byte-identical takes, verdicts and clips on the same seeds. Reason: approved voices must sound exactly the same after the move. | **DECIDED** |
| ADR-004 | 2026-11-20 | PR flow | A gatekeeper check runs before any PR becomes ready, and each session keeps one draft report-only PR. Reason: Ray's standing rules. | **DECIDED** |
| ADR-005 | 2026-11-20 | Rollback window | Lessons default to rokct-media, with MEDIA_ENGINE=voice_batch as a no-code rollback. The old renderer (render_takes.py, qc.py, agent render_voices.py) is deleted only after lesson renders have run cleanly on rokct-media. Reason: keep lesson rendering safe while switching. | **DECIDED** |
| ADR-006 | 2026-11-20 | Engine layout | rokct-media levels: 1 speech, 2 audio composition (radio ads, Reel music), 3 video (vertical assembly first). Product rules (which line plays where, the one-voice rule, briefs) stay with the callers. | **DECIDED** |
