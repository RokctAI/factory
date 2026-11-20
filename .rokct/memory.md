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
*   [Active] **Report rule (Ray, 2026-11-20):** every session opens ONE draft PR holding only its report and never marks it ready. Task first in the PR description; keep it updated until the session ends; list every PR opened with state and purpose. All code goes in separate PRs. Keep current: `.rokct/memory.md`, `.rokct/decision_log.md`, `.rokct/project_map.md`, `.rokct/active_session.txt`. Session reports go in `.rokct/sessions/`; never delete or move old ones (Session Retention above prunes them).

## Lessons Learned
*(Agent to append new lessons here when a mistake is made or a correction is received)*

*   **[Date]** - [Lesson]


## Safe ID
sinyage.f74d39
