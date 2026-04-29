# RokctAI Factory

An autonomous publishing factory that generates, evaluates, improves, and publishes books across multiple genres.

## 🚀 Factory Status Dashboard
*Last Updated: 2026-04-29 12:00*

| Genre | Total Jobs | New (7d) | Published | Health |
| :--- | :--- | :--- | :--- | :--- |
| 🎭 **Poetry** | 0 | 0 | 0 | 🟡 |
| 📚 **Fiction** | 0 | 0 | 0 | 🟡 |
| 📖 **Short Story** | 0 | 0 | 0 | 🟡 |
| 👶 **Children** | 0 | 0 | 0 | 🟡 |

**Overall Progress**: `0.0%` Published | `+0` New Jobs This Week

## 🏗 Pipeline Levels

- **Level 0: Theme Generation** (Fully Automated) - Discovers new themes.
- **Level 1: Idea Generation** (Human Gate 1) - Expands themes into book ideas for approval.
- **Level 2: Concept Expansion** (Human Gate 2) - Develops approved ideas into full concepts.
- **Level 3: Rule Generation** (Human Gate 3) - Generates world, book, and chapter rules.
- **Level 4: Generation Loop** (Fully Automated) - Continuous writing and evaluation loop.
- **Level 5: Draft** (Human Gate 4) - Final human review of the completed book.
- **Level 6: Publishing** (Fully Automated) - Assembles PDF, generates cover, and publishes.

## 👥 Human Decision Points

1. **Approve Idea** (Level 1): Change `idea_status` to `approved` in the job card.
2. **Approve Concept** (Level 2): Change `concept_status` to `approved` in the job card.
3. **Approve Rules** (Level 3): Change `rules_status` to `approved` in the job card.
4. **Accept Final Draft** (Level 5): Change `status` to `accepted` in `metadata.md`.

## 📁 Repository Structure

- `.rokct/agent/`: AI agent configurations, prompts, and job tracking.
- `.rokct/skills/`: Reusable agent capabilities and automation scripts.
- `.rokct/types/`: Metarules for different book types (poetry, fiction, etc.).
- `.github/workflows/`: Functional automation pipelines for each level.
- `books/drafts/`: In-progress book projects.
- `books/published/`: Completed and published books.

## 🤖 Jules Sessions

Jules (the primary AI agent) runs in scheduled sessions:
- **Daily Writing Sessions**: Weekdays at 08:00 UTC.
- **Weekend Evaluation Sessions**: Deep audit of all active drafts.

## 📖 Ledger

The `.rokct/agent/log/ledger.md` is the single source of truth for the system state. **Only CI workflows are permitted to write to the ledger.**

## ✍️ How to Add a Book Idea Manually

Create a new card in `.rokct/agent/jobs/pending/` using the `template.md` and set the status to `idea_generated`.
