# Agent Memory & Lessons Learned

**Rule**: Before asking a question or starting a task, the Agent **MUST** read this file to check for past lessons or user preferences.

## User Profiles
*   **[Name]**:
    *   **Safe ID**: [ray.dev.9ac2b1] (Used for filenames)
    *   **Role/Preferences**: [Details]
*   *(Agent: Add new users here as they appear)*

## Global Preferences
*   **Session Retention**: [Forever] (Options: Forever, 1 Month, 1 Week)
*   **Checkpoint Policy**: [Value] (Options: Frequent, Manual) -> *Set 'Frequent' for Cloud Agents*
*   [Active] Prefer "Frappe" for backend.
*   [Active] Prefer "Next.js + AI SDK" for frontend.
*   [Active] Prefer "Flutter" for mobile.
*   [Active] "Premium" design aesthetic is non-negotiable.

## Standing Rules (Ray, 2026-11-20)
*   **Report PR**: every session opens ONE draft PR that holds only its report and is never flipped to ready. The task goes first in the PR description, and the description is kept current until the session ends. All code goes in separate PRs. The report lists every PR the session opened, with its state and what it does. Keep `memory.md`, `decision_log.md`, `project_map.md` and `active_session.txt` current, and put the session report in `.rokct/sessions/`. Never delete or move old sessions: **Session Retention** above prunes them.
*   **Gatekeeper before ready**: run The-Rokct-Protocol `core/skills/.rok/pr-gatekeeper-check/gatekeeper_check.py` on a PR before turning it to ready. State its NOT RUN lines in the PR in plain words.
*   **One audio engine**: lessons, radio ads and Reels move onto rokct-media (The-Rokct-Protocol `core/utils/rokct_media`) step by step. Approved voice settings never change in the move. Lessons switch only after `media_parity.yml` passes and Ray gives the go-ahead.

## Lessons Learned
*(Agent to append new lessons here when a mistake is made or a correction is received)*

*   **[Date]** - [Lesson]


## Safe ID
sinyage.f74d39
