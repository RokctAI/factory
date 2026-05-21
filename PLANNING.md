# RokctAI Factory — Planning Document
> For: AI Agent tasked with building this system
> Based on: RokctAI/opportunities repo patterns
> Author: System Architect

---

## 1. Vision

An autonomous publishing factory that generates, evaluates, improves, and publishes books across multiple genres. The human owner makes four decisions per book: approve idea, approve concept, approve rules, accept final draft. Everything else is automated.

---

## 2. Core Philosophy

### The Poetry Foundation
Every design decision in this system flows from a poetry philosophy:

- **Line = Tree** — stands alone, hits alone, needs nothing else to survive
- **Stanza = Forest** — trees together create something larger without losing individual strength
- **Poem = Region** — forests together with their own climate and rules
- **Book = Country** — regions forming a complete world
- **Universe = Collection of books** — each book a different planet, same author, different gravity

Every piece of content generated must pass a **backwards audit**:
Does this line serve the stanza? Does this stanza serve the poem? Does this poem serve the book? Does the book honor the world rules?

**Creation is singular. Evaluation is plural.**

---

## 3. Supported Input Types

The system accepts a single input card with three fields:

```
theme: [any theme]
type: [book.poetry | book.fiction | book.short_story | book.children]
age: [optional — number]
```

Age drives automatic rule injection. No other configuration needed from the human.

### Age Rules
- **Age < 6** → inject static child protection prompt (hardcoded, never changes)
- **Age 6–12** → inject middle grade static prompt
- **Age 13–17** → inject young adult static prompt
- **Age blank or adult** → no injection, full creative freedom

Same theme + different age = completely different book. The pipeline is identical. Only the injected guardrail changes.

### Static Child Protection Prompt (Age < 6)
```
This content is for a {age} year old child.
You MUST: use simple words, create wonder and safety, warm emotional world, nurturing tone.
You MUST NEVER: introduce darkness, fear, complex trauma, adult themes, ambiguous morality, violence, or loss without resolution.
```

This prompt is a template. `{age}` is replaced with the actual age. The protection rules never change. Only the age variable is dynamic.

---

## 4. Pipeline Levels

### Level 0 — Theme Generation (Fully Automated)
- Runs only when Level 1 has fewer than 5 pending themes
- Generates themes autonomously — no human approval needed
- Feeds directly into Level 1
- Agent: **Groq** (fast, chat-based)
- CI writes to ledger on completion

### Level 1 — Idea Generation (First Human Gate)
- Takes each theme and generates 5 one-line book ideas
- Human reads and approves one idea, requests more, or declines the theme
- Declined theme is gone
- Approved idea moves to Level 2
- Agent: **Groq**
- CI writes to ledger on human decision

### Level 2 — Concept Expansion (Second Human Gate)
- Approved idea expands into full concept using metarules if they exist
- Includes: angle, emotional world, target feeling, structural approach
- Human approves or sends back
- Agent: **Groq**
- CI writes to ledger

### Level 3 — Rule Generation (Third and Final Human Gate)
- Approved concept triggers full rule generation
- World rules → book rules → poem/chapter rules → stanza/scene rules → line rules
- Rules reference the metarules file for that type
- Human approves once. This is the last human touch before full automation.
- Agent: **Jules** (complex, file-writing task)
- CI writes to ledger

### Level 4 — Generation Loop (Fully Automated)
- Writer agent generates full content top-down
- Evaluator agent audits every element bottom-up
- Each element receives a score and optional suggested replacement
- Comparator agent evaluates original vs suggestion — improvement or regression?
- Best version survives
- Loop continues until quality thresholds are met
- Agent: **Jules**
- CI writes to ledger at each loop iteration

### Level 5 — Draft (Fourth Human Gate)
- Completed book lands in `books/drafts/{book_name}/`
- Human pulls and reads at their leisure
- Approve → moves to Level 6
- Reject → returns to Level 4 improvement loop with notes
- CI writes to ledger

### Level 6 — Final Publishing (Fully Automated)
- On human acceptance: cover brief triggered, credits generated, copyright statement generated, opening letter generated
- PDF assembled from all markdown files in the folder
- Entire `{book_name}/` folder moved from `books/drafts/` to `books/published/`
- Agent: **Jules**
- CI writes to ledger

---

## 5. Repository Structure

```
RokctAI/factory/                         # New repo, separate from opportunities

.rokct/
  agent/
    prompts/
      in_progress/                       # Recurring prompts — run forever, never complete
      queue/                             # One-time prompts waiting to run
      completed/                         # One-time prompts that have finished

    jobs/
      pending/                           # Jobs waiting for Jules to pick up
      running/                           # Jules currently working on this
      done/                              # Jules finished, PR opened and merged

    log/
      ledger.md                          # Single source of truth — CI writes only, agents read only

    guardrails/
      age_under_6.md                     # Static child protection prompt template
      age_6_12.md                        # Middle grade static prompt
      age_13_17.md                       # Young adult static prompt

  types/
    poetry/
      metarules/
        world_rules.md
        book_rules.md
        poem_rules.md
        stanza_rules.md
        line_rules.md
        impact_metrics.md
        audit_rules.md
    fiction/
      metarules/
        world_rules.md
        book_rules.md
        chapter_rules.md
        scene_rules.md
        line_rules.md
        impact_metrics.md
        audit_rules.md
    short_story/
      metarules/
        [same structure]
    children/
      metarules/
        [same structure]

.github/
  workflows/
    level0_theme_generation.yml          # Scheduled — triggers Groq if Level 1 queue < 5
    level1_idea_generation.yml           # Triggers on new theme card
    level2_concept_expansion.yml         # Triggers on approved idea
    level3_rule_generation.yml           # Triggers on approved concept — opens Jules session
    level4_generation_loop.yml           # Daily 08:00 — Jules writing session
    level4_evaluation_loop.yml           # Weekend — Jules evaluation session
    level6_publish.yml                   # Triggers on human acceptance
    ledger_update.yml                    # Called by all other workflows to update ledger
    session_scheduler.yml                # Manages Jules session slots and conflicts

books/
  drafts/
    {book_name_hash}/
      metadata.md                        # Theme, type, age, status, metarules link, rules
      opening_letter.md
      credits.md
      copyright.md
      cover_brief.md
      01_{title}.md                      # Each poem or chapter as own file
      02_{title}.md
      ...

  published/
    {book_name_hash}/
      [same files as drafts]
      book.pdf                           # Assembled on publish
      cover.jpg                          # Generated on publish
```

---

## 6. Card Structure

### Idea Card (lives in `.rokct/agent/jobs/`)
Filename: `{theme}_{type}_{hash}.md`
Example: `loneliness_poetry_a3f7b2.md`

```markdown
---
id: loneliness_poetry_a3f7b2
theme: loneliness
type: poetry
age:
metarules: .rokct/types/poetry/metarules/
guardrail:
idea: Blank spaces between people who share a bed
idea_status: pending_approval
concept:
concept_status:
rules_status:
book_name:
book_path:
status: idea_generated
created: 2026-04-29
last_updated: 2026-04-29
---
```

Status progression:
`idea_generated` → `pending_approval` → `concept_expanding` → `concept_generated` → `pending_concept_approval` → `rules_generating` → `rules_generated` → `pending_rules_approval` → `writing` → `evaluating` → `draft_ready` → `pending_acceptance` → `publishing` → `published`

---

## 7. Ledger Structure

File: `.rokct/agent/log/ledger.md`

**Only CI writes to this file. Agents read only.**

```markdown
| ID              | Type    | Theme      | Status                  | Agent | Session  | PR    | Timestamp           |
|-----------------|---------|------------|-------------------------|-------|----------|-------|---------------------|
| loneliness_a3f7 | poetry  | loneliness | idea_generated          | groq  | GS-0001  | —     | 2026-04-29 08:00    |
| loneliness_a3f7 | poetry  | loneliness | pending_approval        | —     | —        | —     | 2026-04-29 08:01    |
| loneliness_a3f7 | poetry  | loneliness | concept_expanding       | groq  | GS-0002  | —     | 2026-04-29 09:00    |
| loneliness_a3f7 | poetry  | loneliness | rules_generating        | jules | JS-0001  | #12   | 2026-04-29 20:00    |
| loneliness_a3f7 | poetry  | loneliness | writing                 | jules | JS-0002  | #15   | 2026-04-30 08:00    |
| loneliness_a3f7 | poetry  | loneliness | draft_ready             | jules | JS-0003  | #18   | 2026-05-03 20:00    |
| loneliness_a3f7 | poetry  | loneliness | published               | human | —        | #22   | 2026-05-04 10:00    |
```

Session naming:
- Groq sessions: `GS-XXXX`
- Jules sessions: `JS-XXXX`
- Human actions: `human`

---

## 8. Jules Session Management

### Daily Sessions
- **08:00 weekdays** — Writing session. One book at a time. Full focus. Deep work.
- **20:00 weekdays** — Rule generation or concept expansion. One card at a time.

### Weekend Sessions
- **Saturday + Sunday** — Evaluation session. All books in draft or in_progress swept in one session.
- Jules has a **session availability file**: `.rokct/agent/session_state.md`

```markdown
---
weekend_block: open          # open | running | done
weekend_session_id:
weekend_started:
weekend_finished:
---
```

- When Jules starts weekend evaluation: sets `weekend_block: running`
- When Jules finishes early: sets `weekend_block: open` — block is freed for other jobs
- Scheduler reads this before opening any new session
- If `running`: wait
- If `open` on weekend: available for evaluation or overflow writing

### Session Rules
- Maximum 2 active Jules sessions at any time
- No two sessions writing the same book simultaneously
- Evaluation sessions can touch multiple books — read heavy, no write conflicts
- All Jules PRs are auto-merged (Jules is trusted as owner)

---

## 9. Groq Integration Pattern

Groq is chat-based. It cannot write to the repo directly. It produces output that CI picks up.

Pattern (same as existing opportunities repo):
1. Groq receives prompt + card content
2. Groq generates output as structured markdown
3. CI receives output, writes file to repo, opens PR
4. PR auto-merges
5. CI updates ledger

Groq prompt cards follow the same JSON structure as `grants_hunt_corporate.json`:

```json
{
  "repo": "RokctAI/factory",
  "prompt": "[TASK INSTRUCTIONS]",
  "branch": "main",
  "title": "[Session Title]",
  "automation_mode": "AUTO_CREATE_PR",
  "recurrence": "[Weekly | Daily | Once]",
  "immediate": false,
  "scheduled_at": "[ISO timestamp]"
}
```

---

## 10. Metarules Behavior

- If metarules exist for a type: agents reference them during rule generation and evaluation
- If metarules do not exist: system proceeds without them, logs a warning in the ledger, does not fail
- Metarules are linked in every `metadata.md` card so agents always know where to find the constitution behind the book's specific rules

---

## 11. Evaluation Logic

Every generated element receives:
- A **score** (0–10) against its level rules
- A **pass/fail** against world rules (non-negotiable)
- An **optional suggested replacement** if score < threshold

Suggested replacements are shown alongside originals. A third comparator agent evaluates:
- Is the suggestion an improvement or regression?
- What is the delta score?
- Which version survives?

The writer agent and evaluator agent are always different sessions. The agent that creates never evaluates its own work.

---

## 12. Publishing Automation

On human acceptance of a draft, the publish workflow:
1. Generates `cover_brief.md` if not already present
2. Triggers cover image generation
3. Assembles all poem/chapter `.md` files into single `book.pdf` in order
4. Generates `copyright.md` with correct year, author, rights statement
5. Generates `opening_letter.md` from theme and rules
6. Generates `credits.md`
7. Moves entire `{book_name}/` folder from `books/drafts/` to `books/published/`
8. Updates ledger to `published`

---

## 13. Scalability

The same pipeline with zero structural changes supports:
- Poetry collections
- Fiction novels
- Short story collections
- Children's books (any age, guardrail injected automatically)
- Children's poetry books
- Any future genre — add metarules folder, system works immediately

Same theme across types produces different books:
```
theme: loneliness  type: poetry     age: —   → Adult poetry collection
theme: loneliness  type: short_story age: —  → Adult short stories
theme: loneliness  type: poetry     age: 5   → Children's poetry book
theme: loneliness  type: book.fiction    age: 14  → YA novel
```

One input file. Four different planets.

---

## 14. What Does Not Exist Yet (Build Order)

1. Repo scaffold — folders, README, placeholder files
2. Ledger system — structure, CI writer workflow
3. Guardrails — static prompt templates for each age group
4. Metarules — poetry first, other types can be empty stubs
5. Groq prompt cards — Level 0 and Level 1 scheduled prompts
6. Jules job templates — writing, evaluation, publishing
7. Session scheduler — reads ledger, manages slots
8. GitHub Actions workflows — one per pipeline level
9. Session state file — Jules weekend availability
10. Book folder templates — metadata, credits, copyright stubs
## Reliability Layer (Added post-audit)

Six fixes implemented after external audit:
1. Job locking — lock_job.py prevents race conditions
2. Single state authority — card is truth, ledger is log
3. State machine enforcement — update_status.py validates all transitions
4. Generation loop exit — max_iterations prevents infinite loops
5. Failure states — stalled status and retry logic with 3 attempt limit
6. Deduplication — similarity check before Level 0 creates theme cards

## Visual Layer (Added post-infrastructure)

Triggered after human accepts a draft and sets visual preferences in metadata.md.

Three fields control visual generation:
  visuals_cover: true|false
  visuals_illustrations: true|false
  visuals_illustration_scope: none|per_poem|per_chapter

Four stage pipeline:
  Stage 6a: Jules summarizes full book into visuals/book_summary.md
  Stage 6b: Groq generates cover.json from summary
  Stage 6c: Groq generates illustration JSON files one at a time
  Stage 6d: Image rendering from JSON files (external system, not yet implemented)

All visual briefs are JSON. No images are generated in the repo.
Rendered images land in visuals/rendered/ when external system processes the JSONs.
Age guardrail is injected into every Groq visual brief call if age is set on the book.

## Social Media Reel Pipeline (Added post-visual layer)

Triggered automatically after visuals_status reaches done, if visuals_reel is true in metadata.

Groq reads book_summary.md and scans all content for highest impact lines.
Selects hook based on impact_metrics philosophy — punch, delay, or accumulation.
Generates reel.json inside books/published/{book_name}/visuals/

The reel brief is consumed by an external video generation system (not yet implemented).
The hook_text is the line or lines extracted from the book that will appear on screen.
The hook must work in under 5 seconds. It is one tree from the forest, shown to the world.

## Bible Series Stream (Added alongside book factory)

The factory supports a second content stream for long-form research series.
Content lives in bible/ not books/.
Same pipeline and agent infrastructure.
Different metarules under .rokct/types/bible.series/

First series: Forbidden Questions
Location: bible/forbidden_questions/
Status: 15 episodes complete, characters and deep-dives to build.

To generate a new episode:
  theme: [topic]
  type: bible.series
  series: forbidden_questions

The factory reads the series metarules, the master thread, and the existing episodes as style reference before generating.

## Bible Series Stream (Added alongside book factory)

The factory supports a second content stream for long-form research series.
Content lives in bible/ not books/.
Same pipeline and agent infrastructure.
Different metarules under .rokct/types/bible.series/

First series: Forbidden Questions
Location: bible/forbidden_questions/
Status: 15 episodes complete, characters and deep-dives to build.

To generate a new episode:
  theme: [topic]
  type: bible.series
  series: forbidden_questions

The factory reads the series metarules, the master thread, and the existing episodes as style reference before generating.
