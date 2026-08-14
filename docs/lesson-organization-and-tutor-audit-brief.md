# Task Brief: Lesson Grouping, Duplicate Safety, and Tutor Selection Fixes

> Self-contained brief for a fresh session. Read in full; should not require the conversation that
> produced it. Follow-on to `factory/docs/lesson-pipeline-levels-0-4-brief.md` (the `lesson.*` job type
> implementation) — that work is confirmed real and working (two Grade 11 maths lessons genuinely reached
> `status: evaluated` with correct content). This brief fixes four specific gaps found in a direct audit
> of the actual generated job cards and content, not guessed.

## Findings, each confirmed directly against real files

1. **Every generated lesson defaults to "Grandmaster" — Big John is never used.** Checked all 6 existing
   lesson job cards (2 `done/`, 4 `pending/`) — every single one has `tutor: Grandmaster — formal`, zero
   have `Big John — simplistic, lower grade logic`. `lessons/curriculum/caps_seed.json`'s own comment says
   "tutor is optional — when omitted, Level 1 recommends one (Grandmaster — formal | Big John — simplistic,
   lower grade logic)" — so the mechanism is supposed to vary, but in practice it never has. Find and fix
   whatever Level 1 logic is supposed to make this choice (check `lesson1_plan_generation.yml` and its
   underlying script/prompt) — it's either hardcoded to always pick Grandmaster, or the "recommend one"
   step isn't actually running/being respected.

2. **No structural duplicate-prevention on `(subject, grade, topic, subtopic)`.** The only dedup mechanism
   found (`is_duplicate_theme` in `lessons/scripts/lesson_pipeline.py` or wherever it now lives — confirm
   current location) does fuzzy string-matching against the human-readable `theme` field, not a direct
   check against the structural `subject`/`grade`/`topic`/`subtopic` fields. This happens to have avoided
   duplicates so far by luck of the seed list being manually curated, but isn't a real guarantee once more
   subjects/topics are added or if Level 0 ever generates topics rather than just pulling from
   `caps_seed.json`. Add an explicit check: before opening a new lesson job card, look for existing
   pending/running/done cards with the same `(subject, grade, topic, subtopic)` tuple and skip/flag instead
   of creating a duplicate.

3. **No `term` field anywhere — schema, seed data, or cards.** CAPS curriculum is organized by South
   African school term (Term 1–4), and this dimension doesn't exist anywhere in the pipeline right now —
   not `template_lesson.md`, not `caps_seed.json`'s entries, not any generated job card. Add a `term` field
   (1–4) to: the job card template (`template_lesson.md`), `caps_seed.json`'s entry schema (populate it for
   every existing entry — this requires knowing which CAPS term each topic actually falls in, don't guess;
   check a real CAPS pacing document/past-paper source per subject, or leave it explicitly marked
   `unknown` rather than a guessed value if you can't verify), and the Level 0/1/2 flow so it gets carried
   through to the finished lesson the same way `subject`/`grade` already are.

4. **Lessons are not grouped into folders — flat `lessons/drafts/<id>/` for everything.**
   *(Historical note, 2026-08: the grouped tree this item introduced — the "junior"
   pipeline-output layout — was later retired and deleted; lesson content now lives in the
   CAPS session tree under `lessons/curriculum/CAPS/<subject>/session/...`.)* Reorganize into
   `lessons/<subject>/<grade>/<term>/<id>/` (e.g. `lessons/maths/grade11/term2/quadratic_equations_factoring_method_31d165/`)
   instead of the current flat `lessons/drafts/<id>/`. This needs to happen consistently across: where
   Level 2 (Jules) writes new content, where the job card's `lesson_path`/`script_path`/etc. fields point,
   and the two already-`done` lessons' existing content (move it to match the new structure, update their
   cards' path fields accordingly — don't leave old-structure and new-structure lessons inconsistent).
   Confirm this doesn't break the `done/`-vs-`pending/` job-card archiving mechanism added in the previous
   session's queue-hygiene fix — that's about job *cards* (`.rokct/agent/jobs/{pending,done}/`), a separate
   thing from lesson *content* folders (`lessons/drafts/` → the new grouped path), don't conflate the two
   when making this change.

## Sequencing

Do #3 (add `term` field) before #4 (folder grouping), since the folder path depends on knowing the term.
#1 and #2 are independent of the other two and can be done in any order. Verify each fix against the real
existing data (the two `done` lessons, the 4 `pending` cards) rather than only against new test cards.

## Deliverable

All four fixes applied and verified: at least one new test lesson card that actually gets assigned Big
John (proving #1 works), a duplicate-attempt that gets correctly skipped/flagged (proving #2 works), every
card populated with a real or explicitly-`unknown` term (#3), and the two existing done lessons plus all
pending ones physically reorganized under `lessons/<subject>/<grade>/<term>/` with their cards' path fields
updated to match (#4). Report back with evidence for each, not just "done."
