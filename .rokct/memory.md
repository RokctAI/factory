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

## Lessons Learned
*(Agent to append new lessons here when a mistake is made or a correction is received)*

*   **[Date]** - [Lesson]
*   **2026-11-20** - Report rule (Ray): every session opens one DRAFT PR holding only its report (task first, every PR opened with its state and what it does), keeps it updated until the session ends, and never marks it ready. All code goes in separate PRs. Keep memory.md, decision_log.md, project_map.md and active_session.txt current; session reports go in .rokct/sessions/ and are never deleted or moved (Session Retention prunes them).
*   **2026-11-20** - Run the protocol's gatekeeper skill before marking any code PR ready (Ray).


## Safe ID
sinyage.f74d39
