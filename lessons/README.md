# RokctAI Factory — Lessons Stream (`lesson.*`)

Produces Supacharge lesson content through pipeline Levels 0–4, sharing the
factory's job-card state machine (`.rokct/agent/jobs/`, `update_status.py`,
locks, ledger) without touching the `book.*` / `film.*` streams.

Content requirements come from `agent/replay/docs/supacharge-tech.md`
§4 "Content Production Pipeline". **The pipeline stops at `status: evaluated`
(Level 4: human-approved content).** Level 6 production — Manim JSON export,
VibeVoice audio, manifest assembly, upload — needs VPS infrastructure that
does not exist yet and is a separate future brief.

## Flow

| Level | Workflow | Trigger | What happens | Status after |
|---|---|---|---|---|
| 0 | `lesson0_topic_selection.yml` | hourly / syllabus push | Creates job cards from `lessons/curriculum/CAPS/{subject}/syllabus/{grade}.json` (+ `CAPS/{subject}/skills/`) when pending count per type is low | `theme_generated` |
| 1 | `lesson1_plan_generation.yml` | hourly / card push | Groq captures tutor persona, example problem, prior knowledge, lesson angle; card is born/planned with `idea_status: approved` | `pending_approval` |
| — | ~~human gate 1~~ | — | **Retired for lesson cards (owner decision, 2026-07-17)** — lesson ideas flow straight to Level 2. Book/film types keep their gate. | — |
| 2 | `lesson2_concept_expansion.yml` | card push | Jules generates all §4 content items into `lessons/drafts/<id>/` and opens a PR | `concept_expanding` |
| — | **human gate 2** | review + merge the Jules PR | Content lands; Jules' card update sets `concept_generated` | `concept_generated` |
| 3 | `lesson3_rules_check.yml` | merge push | Structural/pedagogy checks (`lesson_pipeline.py check`): MCQ answer keys, subtopic timestamps, all files present | `pending_concept_approval` |
| — | **human gate 3** | edit card | Review content accuracy (§4 step 3), set `concept_status: approved` | — |
| 4 | `lesson4_evaluation.yml` | card push | Final evaluation gate (`lesson_pipeline.py evaluate`), then terminal transition | `evaluated` |

## Layout

- `curriculum/CAPS/{subject}/syllabus/{grade}.json` — the source of truth:
  curated DBE ATP syllabus data (topics, subtopics, prior knowledge, SBA,
  exam structure) per subject and grade, each file recording the exact
  education.gov.za document it came from (`source_url`, `atp_edition`).
  `lesson_pipeline.py load_seed_entries()` flattens these into one row per
  teachable subtopic; revision/exam/assessment topics never become lesson
  rows. See `curriculum/CAPS/README.md` for the schema and curation notes.
  (Replaces the retired hand-written `curriculum/caps_seed.json`.)
- `curriculum/CAPS/{subject}/skills/{grade}/{skillname}.json` — hand-curated
  skill definitions (`skill_ref`, name, example problem, prior knowledge):
  term-independent prerequisite-knowledge units that are not derivable from
  the ATP documents; appended to the same load as `category: skill` rows.
  Syllabus topics link them via `requires_skills: [<skill_ref>]`;
  `lesson_pipeline.py skills-index` validates the graph (the generated
  `lessons/skills_index.json` artifact is retired).
- `scripts/atp_drift_check.py` — re-verifies every syllabus term against
  each CAPS file's recorded `source_url` (the DBE reissues ATPs yearly and
  placements can shift between editions). Run it when a new school year's
  ATPs publish: update `source_url`/`atp_edition` in the CAPS files, run
  the check, and fix any DRIFT rows by hand — the script reports, it never
  rewrites.
- `scripts/lesson_pipeline.py` — seeding, prompt construction (§4 Prompt
  Template verbatim), plan capture, Level 3/4 checks. Seeding refuses
  structural duplicates: an existing pending/running/done card with the same
  `(subject, grade, topic, subtopic)` tuple is skipped and flagged
  (`check-duplicate` runs the same test standalone).
- Tutor personas: both Grandmaster and Big John teach every FET grade — the
  Level 1 prompt selects on teaching-style fit (real-world-anchored
  subtopics → Big John; abstraction-heavy ones → Grandmaster) and records a
  `Tutor choice:` line in the idea block. Seed rows may pin `tutor`
  explicitly.
- Lesson content output — **retired layout deleted (2026-08)**: pipeline
  lessons used to land in `<subject>/<grade>/<term>/<card_id>/` (the
  "junior" tree). Every lesson it held has a senior equivalent in the CAPS
  session tree (`curriculum/CAPS/<subject>/session/...`), which is where
  lesson content is authored now (directly by in-context sessions), so the
  junior tree was deleted and `content_dir()` in
  `scripts/lesson_pipeline.py` hard-fails rather than mint a path in the
  retired layout.
- Level 3 also verifies content programmatically wherever it is computable
  — MCQ answer keys (quadratic roots/factoring/expansion/solution counts,
  pure-arithmetic values) and every fully-numeric worked-arithmetic
  identity in the script/MCQs/comprehension text across all six subjects
  (SA and US number formats, word operators, unit words) — failing the
  check on any recomputed mismatch. Non-computable statements are skipped,
  never guessed.
- **Level 3.5 — independent AI cross-check**: after structural and computed
  checks pass, a fresh Groq (llama) call — a different model and context
  from the Jules session that generated the content — reviews the lesson
  against subject-scoped criteria (units/formulas for sciences, market
  mechanisms for economics, hemisphere-correct processes for geography,
  CAPS rounding for maths literacy, double-entry/format discipline for
  accounting). The verdict lands on the card as `crosscheck_status`
  (passed/failed/error) with a `crosscheck_notes` report. The Level 4 human
  is no longer asked "is this correct" but "given this independent report,
  proceed?" — a `failed` verdict advances WITH its report for the human to
  weigh; an `error` (API failure, malformed response) blocks Level 4
  entirely until the check runs (fail-closed).
- Card template: `.rokct/agent/jobs/template_lesson.md`.
- Metarules: `.rokct/types/lesson.<subject>/metarules/` — one directory per
  lesson type (`lesson.maths`, `lesson.physical_sciences`,
  `lesson.economics`, `lesson.geography`, `lesson.maths_literacy`,
  `lesson.accounting`); `pedagogy_rules.md` and
  `mcq_rules.md` are shared conventions, `lesson_rules.md` carries the
  subject flavour. To onboard a new subject: add its type to
  `lesson0_topic_selection.yml`'s `TYPES` array, create its metarules
  directory, and add seed rows to `curriculum/caps_seed.json`.

MCQ and subtopic JSON shapes are contracts with the shipped app
(`McqQuestion.fromJson`, `ReplayLessonEngine` subtopic_end exercise batches)
so Level 6 can assemble manifests later without content rework.
