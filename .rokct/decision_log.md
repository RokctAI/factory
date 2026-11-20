# Architectural Decision Log (ADR)

**Purpose**: Record clear "Subject Closed" decisions to prevent re-debating them.

| ID | Date | Topic | Decision | Status |
| :--- | :--- | :--- | :--- | :--- |
| ADR-001 | 2026-11-20 | Audio engine | One audio engine, rokct-media, used for lessons, radio ads and Reels. Reason (Ray): "a radio ad is a tutor lesson voice"; one copy stops the copies drifting apart. | **DECIDED** |
| ADR-002 | 2026-11-20 | Move order | Catch rokct-media up first, then prove parity, then switch lessons behind a switch, then radio ads, Reels, retire old copies, and video last. Reason: lesson rendering must keep working at every step. | **DECIDED** |
| ADR-003 | 2026-11-20 | Parity bar | Lessons switch only when both engines give byte-identical takes, verdicts and clips on the same seeds. Reason: approved voices must sound exactly the same after the move. | **DECIDED** |
| ADR-004 | 2026-11-20 | PR flow | A gatekeeper check runs before any PR becomes ready, and each session keeps one draft report-only PR. Reason: Ray's standing rules. | **DECIDED** |
