# How to Use the RokctAI Factory

This guide explains each level of the RokctAI Factory pipeline, highlighting where human intervention is required, what actions the human must take, and how subsequent levels depend on these actions.

## Pipeline Overview

The factory operates across 7 levels, from theme discovery to publishing. Certain levels operate fully autonomously, while others act as "Human Gates" requiring explicit approval before the system will proceed to the next level.

---

### Level 0: Theme Generation
- **Automation:** Fully Automated
- **Human Intervention:** Not required.
- **What happens:** The system autonomously monitors the job queue. If the queue falls below a certain threshold (e.g., 5 items), it delegates tasks to the AI agent to generate new themes. New job cards are created with the status `theme_generated`.

### Level 1: Idea Generation
- **Automation:** Fully Automated Execution, Human Approval Required at the end.
- **What happens:** The AI takes a `theme_generated` card and expands it into a concrete book idea. Once the idea is generated, the system automatically sets the status to `pending_approval`.
- **Human Gate 1:**
  - **Required Action:** A human must review the generated idea in the job card. To approve it and move it to the next level, the human must manually update the job card's status to `concept_expanding`.
  - **Dependency:** **Level 2 will not start** until this status is changed to `concept_expanding`.

### Level 2: Concept Expansion
- **Automation:** Fully Automated Execution, Human Approval Required at the end.
- **What happens:** The AI expands the approved idea into a full structural concept (angle, emotional world, etc.). Once complete, it sets the status to `pending_concept_approval`.
- **Human Gate 2:**
  - **Required Action:** A human must review the expanded concept. To approve it, manually update the job card's status to `rules_generating`.
  - **Dependency:** **Level 3 will not start** until this status is changed to `rules_generating`.

### Level 3: Rule Generation
- **Automation:** Fully Automated Execution, Human Approval Required at the end.
- **What happens:** The AI generates hierarchical rules (world rules, book rules, chapter rules, etc.) based on the approved concept. Once done, it sets the status to `pending_rules_approval`.
- **Human Gate 3:**
  - **Required Action:** A human must review the generated rules. To approve them, manually update the job card's status to `writing`.
  - **Dependency:** **Level 4 will not start** until this status is changed to `writing`.

### Level 4: Generation Loop (Writing & Evaluating)
- **Automation:** Fully Automated
- **Human Intervention:** Not required.
- **What happens:** The AI enters a continuous loop of writing and evaluating the text based on the established rules. The status transitions between `writing` and `evaluating`. Once the system determines the draft is complete and passes evaluation, it sets the status to `draft_ready`, which leads to `pending_acceptance`.

### Level 5: Draft Acceptance
- **Automation:** Human Gate 4
- **What happens:** The system pauses at `pending_acceptance` and waits for human review of the completed book draft.
- **Human Gate 4:**
  - **Required Action:** A human must review the final completed draft. To accept the draft and trigger publication, the human must update the status to `publishing` (often tracked in `metadata.md` or the main job card).
  - **Dependency:** **Level 6 will not start** until the draft status is set to `publishing`.

### Level 6: Publishing
- **Automation:** Fully Automated
- **Human Intervention:** Not required.
- **What happens:** The system automatically takes the accepted draft, assembles the PDF, generates cover and visual briefs, and completes the publication process. The final status becomes `published`.

---

**Summary for the Human in the Loop:**
If you want a book to proceed through the entire factory, you must periodically review jobs in the `.rokct/agent/jobs/pending/` directory and advance them through the "pending" statuses:
1. `pending_approval` -> change to `concept_expanding`
2. `pending_concept_approval` -> change to `rules_generating`
3. `pending_rules_approval` -> change to `writing`
4. `pending_acceptance` -> change to `publishing`
