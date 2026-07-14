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
| 0 | `lesson0_topic_selection.yml` | hourly / seed push | Creates job cards from `lessons/curriculum/caps_seed.json` when pending count per type is low | `theme_generated` |
| 1 | `lesson1_plan_generation.yml` | hourly / card push | Groq captures tutor persona, example problem, prior knowledge, lesson angle | `pending_approval` |
| — | **human gate 1** | edit card | Set `idea_status: approved` | — |
| 2 | `lesson2_concept_expansion.yml` | card push | Jules generates all §4 content items into `lessons/drafts/<id>/` and opens a PR | `concept_expanding` |
| — | **human gate 2** | review + merge the Jules PR | Content lands; Jules' card update sets `concept_generated` | `concept_generated` |
| 3 | `lesson3_rules_check.yml` | merge push | Structural/pedagogy checks (`lesson_pipeline.py check`): MCQ answer keys, subtopic timestamps, all files present | `pending_concept_approval` |
| — | **human gate 3** | edit card | Review content accuracy (§4 step 3), set `concept_status: approved` | — |
| 4 | `lesson4_evaluation.yml` | card push | Final evaluation gate (`lesson_pipeline.py evaluate`), then terminal transition | `evaluated` |

## Layout

- `curriculum/caps_seed.json` — hand-written CAPS-aligned topic list (interim
  source of truth until a real CAPS pacing source exists). Every entry
  carries a `term` (CAPS school term 1–4, verified against the DBE 2023/24
  Annual Teaching Plans; `all` = skills integrated across terms, e.g.
  Geography mapwork; `unknown` = no verifiable ATP placement — never guess).
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
- `<subject>/<grade>/<term>/<card_id>/` (e.g.
  `maths/grade11/term1/..._31d165/`) — one directory per lesson: `script.md`,
  `manim_scene.py`, `subtopics.json`, `mcq.json`,
  `comprehension_check.json`, `mandy_nervous_script.md` (optional — but
  when produced it must be referenced by the card's
  `mandy_nervous_script_path` field; Level 3 fails untracked content),
  `reel_clip.json`, `mandy_qa_transcript.md`.
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
