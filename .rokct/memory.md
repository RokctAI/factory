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
*   **2026-11-20** - Report rule (Ray): every session opens ONE draft PR that holds only its report and is never marked ready. Task first in the PR description; the report lists every PR the session opened with state and purpose; keep it updated until the session ends. Code goes in separate PRs. Keep memory.md, decision_log.md, project_map.md and active_session.txt current; session reports go in `.rokct/agent/sessions/`.
*   **2026-11-20** - Before marking any PR ready, run the protocol's "gatekeeper" skill (Ray).
*   **2026-11-20** - ComfyUI forces fp32 on CPU; on AMX/bf16 CPUs patch `should_use_bf16` for about 2.3x speed.


## Safe ID
sinyage.f74d39
