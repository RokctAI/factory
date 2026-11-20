# Decision Log

Each decision with its reason. Newest last.

## 2026-11-20

- **Report rule adopted for every session.** Each session opens one draft PR that holds only its report, never marked ready, task first in the description, updated until the session ends; code goes in separate PRs. Reason: Ray asked for it (2026-11-20) so every session's work and PRs can be tracked in one place.
- **Session reports live in `.rokct/sessions/`, decision log at `.rokct/decision_log.md`.** Reason: this repo had neither; the agent repo keeps its decision log at `.rokct/decision_log.md`, so this matches it.
- **Microdrama engine approach (proposed, not yet approved): reuse `radio_ads/` for voices and sound, add episode script format, cast pictures, LTX drafts plus Seedance 2.0 finals, and a video assembler.** Reason: Story TV's Dolphin AI is an orchestrator over outside models, so an equivalent is mostly glue around tools we already tested. Waiting on Ray's go and a fal.ai key.
