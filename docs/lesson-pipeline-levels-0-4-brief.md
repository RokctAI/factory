# Task Brief: Add a `lesson.*` Job Type to the Factory (Levels 0–4 Only)

> Self-contained brief for a fresh session. Read in full; should not require the conversation that
> produced it. This is the first of two phases — this brief covers content generation + human review
> only (Levels 0–4). Level 6 (the Manim/VibeVoice production runner) is deliberately out of scope here
> and will be its own separate brief once this phase is proven, since it requires real new VPS
> infrastructure, not just CI/template work.

## Future enhancement (noted, not yet scoped) — ground content in real past papers

Free CAPS/NSC-aligned South African past exam papers are available (Testpapers, SA Exam Papers, WCED
ePortal, the DBE's own site) and could feed two things once this pipeline is further along: (1) real
ground-truth example problems/answers for Level 0/1 topic and example-problem selection instead of
purely LLM-invented ones, and (2) a concrete reference Level 3 could check generated MCQs/example
problems against, rather than relying only on structural validation. Not scoped into this brief — a
later addition once Levels 0–4 are proven across all subjects.

## Context — what `factory` already is (confirmed, don't re-derive)

`factory` (`C:\Users\sinya\Desktop\RokctAI\factory`) is a working, CI-driven autonomous content pipeline —
currently used only for books (`book.poetry`, `book.fiction`, `book.short_story`, `book.children`) and one
film type (`film.documentary`). It was recently unblocked (missing `Initiate Protocol` steps across its
workflows were fixed, plus a stale `delegate_to_agent.py` reference and a `GROQ_API_KEY` secret gap — see
git log for `The-Rokct-Protocol`, `shared-workflows`, and `factory` around 2026-07-13 for the fix commits).
It should now actually be able to run end-to-end for existing book types — verify that's true before
building on top of it (check `.rokct/agent/log/ledger.md` and job cards in `.rokct/agent/jobs/pending/`
for real forward progress on a scheduled run, not just that CI goes green).

**Mechanism**: job cards (`.rokct/agent/jobs/pending/*.md`, YAML frontmatter + a `status:` field) advance
through a state machine via `.rokct/skills/agent_delegation/scripts/update_status.py` and friends
(`lock_job.py`, `call_jules.py`, `call_groq.py`, `manage_sessions.py`) — these scripts are fetched fresh
each CI run by `.rokct/initiate.py` (gitignored `.rokct/skills/`, regenerated every run, don't assume
anything under it is committed). Each level is its own GitHub Actions workflow
(`.github/workflows/level*.yml`) with 4 human-approval gates in the full book pipeline. Content generation
is delegated to an AI agent called "Jules" via `call_jules.py` (creates a GitHub-hosted agent session,
opens a PR with the generated content). `factory_genres.txt`
(`.rokct/config/classifications/factory_genres.txt`) lists top-level content genres — currently
`children`, `fiction`, `poetry`, `short_story`. The job card template is at
`.rokct/agent/jobs/template.md` — read it, its fields are book-shaped (`book_name`, `book_path`, `age`,
etc.) and will need lesson-shaped equivalents, not a forced reuse of the same field names for different
meaning.

## Goal

Add a new job type family, `lesson.*` (e.g. `lesson.maths`, `lesson.science` — mirror the existing
`book.<genre>` convention, don't invent a different shape), that produces Supacharge lesson content
through Levels 0–4 of the same pipeline mechanism, stopping before the Level 6 production step (which
needs real Manim/VibeVoice VPS infrastructure that doesn't exist yet — a separate, later brief).

## What a lesson job must actually produce, per subtopic/lesson (grounded in the existing product spec)

Read `agent/replay/docs/supacharge-tech.md` section "4. Content Production Pipeline" in full — it defines
exactly what one lesson-creation pass must produce:
1. Lesson script (in the chosen tutor's voice — "Grandmaster" formal, or "Big John" simplistic/lower-grade)
2. Manim Python file (whiteboard-style animations, step by step)
3. Subtopic markers with timestamps
4. MCQ questions per subtopic (3–5, predefined answers)
5. Comprehension check questions
6. TikTok/reel clip script (60 seconds, best moment) — this already has a close analogue in the existing
   `level6c_reel_brief.yml` pattern, worth reusing that convention rather than inventing a new one
7. Mandy (post-session assistant) Q&A transcript

The "Prompt Template" subsection of the same doc section gives the exact input fields a lesson-generation
request needs: Subject, Grade, Topic, Subtopic, Example problem, Tutor (Grandmaster/Big John), Prior
knowledge. Use this as the lesson job card's input schema — don't invent different field names.

## Downstream consumption contract — what Level 4's output must be structurally compatible with

The MCQ output (item 4 above) must eventually populate `LMS Lesson Quiz Result`-style data consumed by
`agent/lms/dart/lib/src/domain/models/lesson_models.dart`'s `McqResult` type and the manifest event
vocabulary already implemented in `agent/replay/dart/lib/src/controllers/manifest_parser.dart` /
`audio_sync.dart` (`TrackEvent`, `subtopic_end` events carrying an MCQ batch — see
`agent/lms/dart/templates/routes/lms_route_pages.dart`'s `ReplayLessonEngine` for the reference mapping).
Read these files to understand the *shape* Level 4's approved output needs to already be in, even though
actually assembling the real manifest JSON is Level 6's job (out of scope here) — getting the MCQ/subtopic
data shape right now avoids a rework later.

## What to actually build

1. **Job card schema**: extend or parallel `template.md` with lesson-appropriate fields (subject, grade,
   topic, subtopic, tutor persona, example_problem, prior_knowledge, script_path, manim_path,
   mcq_data_path, comprehension_check_path, reel_brief_path, mandy_transcript_path — adjust names to match
   existing conventions you find, don't just invent from scratch without checking how book cards reference
   their content paths).
2. **Level 0 (Theme → Topic/Subtopic selection)**: mirror `level0_theme_generation.yml`'s structure
   (hourly check, `PENDING_COUNT` per type threshold) but selecting subject/grade/topic/subtopic
   combinations instead of book themes. Source of truth for what topics exist: check if a CAPS curriculum
   pacing data source already exists anywhere in the workspace (the product docs reference "CAPS Pacing"
   as a still-unbuilt feature — confirm whether any topic list exists yet, or whether this level needs a
   seed list written by hand first, don't assume the data already exists).
3. **Level 1 (Idea)**: capture tutor-persona choice + example problem + prior-knowledge assumptions per
   the Prompt Template fields above.
4. **Level 2 (Concept expansion)**: the big one — delegate to Jules (via `call_jules.py`, same as existing
   book levels) to produce all 7 content items listed above from the Prompt Template. Write the actual
   Jules prompt closely from the doc's "Prompt Template" section, don't paraphrase it.
5. **Level 3 (Rules)**: pedagogical/CAPS-alignment consistency checks in place of book structural rules —
   scope this modestly (e.g. reading-level/grade-appropriateness checks, MCQ answer-key sanity checks)
   rather than inventing an elaborate new rules engine; it's fine if this level is thin for v1.
6. **Level 4 (Evaluation + human review)**: human approves content accuracy before anything proceeds —
   mirror the existing human-gate pattern exactly (same PR-based approval flow already used for books).
7. Update `factory_genres.txt` or its lesson-equivalent config, and `entity_groups.json`/`reel_rules.md`
   equivalents if lesson content needs its own smart-tool/security-profile entries (check
   `rcore_private/rcore/platform/entity_groups.json` if a similar "which security profile applies to
   which content type" pattern is relevant here — probably not needed for a content-generation pipeline
   with no live financial/medical data, but confirm rather than assume).

## Explicitly out of scope for this brief

- Level 6 production (Manim → JSON export, VibeVoice audio generation, manifest assembly, upload/schedule)
  — needs a VPS runner that doesn't exist yet. Stop the lesson pipeline's job-card progression at
  "Level 4 approved" for now; don't attempt to fake or stub Level 6.
- Any change to `lms_sdk`'s Dart code, `replay_sdk`'s manifest parser, or the manifest JSON format itself —
  this brief produces the raw content Level 6 will eventually assemble into that format, it doesn't touch
  the consuming side.
- Any change to the existing `book.*`/`film.*` pipeline behavior — `lesson.*` should be additive, sharing
  the state-machine mechanism without altering how existing book types behave.

## Deliverable

Working `lesson.*` job type flowing through Levels 0–4 with at least one real end-to-end test job card
(e.g. `lesson.maths` — Grade 11, Quadratic Equations, Factoring method, matching the doc's own worked
example) reaching a human-approval-gated `concept_generated`/`evaluated` state, verified against the
ledger (not just "CI went green" — confirm the job card's `status:` field actually advanced and content
was actually produced by Jules, matching the level of verification rigor already established in this
project's other work). Report back before starting the Level 6 brief.
