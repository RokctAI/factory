# Real DBE syllabus (ATP) data — THE source of truth (caps_seed.json is retired)

`lessons/curriculum/caps_seed.json` was an interim, hand-written stand-in and has been deleted. The
pipeline now reads this folder directly: `lesson_pipeline.py load_seed_entries()` flattens these files
(plus the hand-curated skill definitions in `{subject}/skills/{grade}/{skillname}.json`, which aren't derivable from ATPs) into the
topic rows Level 0 and the dashboard consume. Data here is sourced directly from the Department of
Basic Education's real 2023/24 Annual Teaching Plans (ATPs) — the actual government syllabus
documents, not a hand-picked subset.

## Layout

One file per subject **per grade** — `CAPS/{subject}/syllabus/{gradeN}.json` — because each grade has
its own official ATP document (18 PDFs total, not 6): a subject's grades share topic families (CAPS is
a spiral curriculum) but each grade's term-by-term content and placement genuinely differ. Each file
maps 1:1 to a single source PDF via its `source_url`, so one grade can be reviewed/regenerated without
touching its siblings. The subject folder is the top split so other per-subject curriculum data (past
papers, exam guidelines, ...) can live alongside `syllabus/` later.

Skills — editorial prerequisite-knowledge units (`skill_ref`, name, example problem, prior
knowledge) — live at `{subject}/skills/{grade}/{skillname}.json`; syllabus topics link them with an
optional `requires_skills: [<skill_ref>]` field, and `lesson_pipeline.py skills-index` validates
that every link resolves. **A skill is not taught like a lesson** (owner decision, 2026-07-27): a
lesson teaches for the first time (15-minute arc, seven content items); a skill *refreshes* — its
content is the review format (1-2 diagnostic questions to skip ahead, a 250-700-word method recap,
a 2-5-question exit check, optionally one Manim scene; no reel/Mandy/subtopic segmentation), which
Level 3 enforces per `category: skill`. Where a syllabus subtopic already teaches the content, the
skill's `covered_by` (list of `{grade, topic, subtopic}`, validated) records it — deep review
defers to that lesson in the Library instead of duplicating it, and cross-grade rewatching (a Gr 12
student reopening the Gr 11 lesson) resolves through the same pointer. Extra depth is a *later
skill in the requires_skills chain*, not a per-grade variant. 21 of the 24 skills are covered by a
real lesson subtopic; 3 (gradient calculation, graphing from tables, substitution in formulae) are
authored-review-only because no syllabus lesson teaches them. Each skill also carries an `importance` block telling the student why it
matters: `summary` (authored, grounded in the transcribed exam structures), `required_by` /
`required_by_topics` (computed from the requires_skills links — regenerate when links change), and
`exam_weight` (hard section marks, present only where the ATP prints per-section marks: Maths, PS
gr12, Geography mapwork/Q1; qualitative-only for Accounting/Economics/ML whose ATPs give paper
structure without per-topic marks — no invented numbers).

```
CAPS/
  maths/syllabus/grade10.json
  maths/syllabus/grade11.json
  maths/syllabus/grade12.json
  ...
  accounting/syllabus/grade12.json
```

Each file: `{subject, grade, curriculum, atp_edition, source_verified, source_url, parse_status,
terms: [...], exam_structure, ...}`. Each term is `{term, topics: [{name, subtopics?,
prior_knowledge?}], sba?, theme?, control_test_scope?}` — `name` is the ordered CAPS topic,
`subtopics` the topic's content breakdown from the ATP's concepts/skills rows, `prior_knowledge`
the ATP's requisite-pre-knowledge note where the source gives one per topic. `sba` lists the term's
formal assessment tasks (with marks/timing where stated). `theme` appears where the ATP names the
term (Geography gr11/12). Physical Sciences additionally carries `control_test_scope` per term and
grade-level `sba_guidelines`. `exam_structure` captures the final-exam paper composition
(marks/hours and section weights or question formats) as printed in each ATP. Mathematical
Literacy files carry `notes` (e.g. the CAPS teach-in-context rule; gr12's deliberate double-FINANCE
term). Revision/exam topics carry no subtopics.

## Source documents (real, verified 2026-07-26)

Each file's `source_url` points at the actual PDF fetched from `education.gov.za`. All 18
subject/grade PDFs (6 subjects × grades 10-12) were live and fetched successfully.

**Found and fixed one real bug while doing this**: `caps_seed.json`'s `_sources.documents` block had the
Physical Sciences Grade 11 and Grade 12 URLs swapped — the "Grade 11" link actually served the Grade 12
ATP and vice versa. Confirmed by reading each PDF's own header (`ANNUAL TEACHING PLANS: PHYSICAL
SCIENCES: GRADE N`), not by assumption. Fixed here (and moot for `caps_seed.json`, which has since
been retired and deleted).

## Curation status: every term list hand-verified against the source text

All 72 term lists (18 subject/grades × terms 1-4) carry `parse_status: "curated"` — a mechanical
pdfplumber extraction followed by a manual pass that read the source text for every term the parser
got wrong and fixed: a missing Accounting G10 Term 1, truncated cells ("Revision of", "Consolidation
of", "Subtropical anticyclones and" → full phrases), merged week cells split apart (Physical Sciences),
a leaked "CAPS TOPICS" row label removed, exam-paper mark-breakdown tables stripped out of Term 4
topic lists, and a "easurement" OCR artifact removed.

A second hand-transcription pass then enriched every file with subtopics, prior knowledge, SBA
tasks and exam structure (see Layout above for the schema). A third pass added **week spans**:
topics carry `weeks: [ints]` extracted from the ATP grids' WEEK-header columns (pdfplumber column
mapping + a hand-verified override for every case the mechanical pass got wrong — substring
collisions like "Tropical cyclones" inside "extra tropical cyclones", forward-fill bleed into
exam-table cells, the source's "ELECTRICTY" typo, duplicate topic names). 318 of 321 topics are
week-placed; 3 are genuinely ungridded in the source (Geography gr10 exam prep/final, gr12 final
NSC block) and carry no weeks. Overlapping spans are faithful: where the ATP merges a block of
weeks across consecutive topics without per-topic boundaries (Accounting gr10 T1 bookkeeping
phases), each topic carries the shared block. Combined with `school_calendar/{year}.json`, weeks
resolve to real dates for any future scheduler. Deliberately NOT transcribed: per-week HOURS
(Physical Sciences prints them; add if a scheduler ever needs sub-week resolution), Physical
Sciences' requisite-pre-knowledge rows (week-granular and repetitive in that ATP; other subjects'
per-topic rows ARE transcribed), and resources/informal-assessment rows (teaching aids, not
syllabus).

Semantics to know when consuming these lists:
- **Assessment/revision entries are kept deliberately** ("CONTROL TEST", "REVISION & ASSESSMENT",
  "FINAL EXAMINATION"...) — they're real ATP weeks and matter for pacing; filter them out if you only
  want teachable content topics.
- **Mathematical Literacy G12 Term 1 lists FINANCE twice** — that's genuine (the ATP teaches Finance,
  then Data Handling and Probability, then returns to Finance at the end of the term).
- **Physical Sciences topics are week-granular** ("MECHANICS: Momentum & impulse" style units, one per
  topic-block) because that's how its ATP is written — more granular than e.g. Economics' term-level
  CAPS topics. A topic reappearing across terms (e.g. "MECHANICS: Energy" in G10 T3 and T4) means the
  ATP genuinely continues it across the term boundary.
- Topic-name casing follows each source document (some ATPs write topics in ALL CAPS, some in sentence
  case) — normalized only where the source itself was inconsistent about the same word.

## Gap status (closed 2026-07-27; what remains is deliberate)

The full document hierarchy now lives here, per subject:

| Layer | Path | Status |
|---|---|---|
| **Curriculum** (CAPS policy statement, gr10-12) | `{subject}/curriculum/caps_gr10-12.md` + `.json` | Ingested: full decoded text with pdf/printed page markers + TOC metadata. The ATPs' "PAGE NO. IN CAPS" references resolve against printed pages (verified: ML p49 = topic Finance). Decoded from cid-only fonts via /MTnn glyph names; maths symbols beyond Latin-1 may be imperfect - source PDF is authoritative. |
| **Syllabus** (ATP pacing) | `{subject}/syllabus/{grade}.json` | Curated + enriched (subtopics, prior knowledge, SBA, exam structure, skills links). |
| **Skills** (prerequisite units) | `{subject}/skills/{grade}/{skillname}.json` | 24 defined, importance + covered_by, review-format convention enforced. |
| **Exam guidelines** (gr12) | `{subject}/exam_guidelines/grade12_2021.md` + `.json` | Ingested: full text of the 2021 national edition (latest on the DBE index) - the document the ATPs' exam notes defer to. |
| **Past papers** | `{subject}/past_papers/index.json` | Real DBE sources indexed (Nov 2024 NSC P1/P2 + memos per subject; portal covers 2008-present). PDF ingestion + question-to-subtopic linking is the past-papers pipeline task (`docs/past-papers-linking-brief.md`) - and the honest source for pre-filling `example_problem`. |
| **Ingested papers** (pipeline store) | `past_papers/{subject}/{grade}/{year}/paper.json` + `past_papers/links.json` | The working store `lessons/scripts/past_papers.py` operates on: per-paper `paper.json` extractions, the paper<->lesson bidirectional `links.json`, and the DBE terms audit (`past_papers/SOURCES.md`). Moved here from `lessons/past_papers/` 2026-08-03 so everything CAPS-sourced lives under `CAPS/` (the IEB tree keeps its own store). |
| **School calendar** | `school_calendar/2026.json` | Official 2026 term dates (gov.za, verified) - maps ATP term numbers to real dates. Reissued annually. |

Still open, deliberately:
- **Grades 8-9 / more subjects** - a product-scope decision, not a data task: Senior Phase has a
  different subject set (EMS, Natural Sciences, Social Sciences) that doesn't map 1:1 onto the six.
  Decide the product serves those grades first; then this same ingestion method applies.
- **Week-level ATP spans/hours** - transcription deliberately skipped (ambiguous column boundaries);
  re-derive from source PDFs if week-pacing is ever needed.
- **Edition freshness** (checked 2026-07-27): education.gov.za's national ATP index still serves the
  2023/24 edition these files were built from. Newer 2025/2026 ATPs circulate provincially (e.g. KZN)
  and via aggregators - if provincial alignment matters, ingest that province's edition and run
  `atp_drift_check.py`. Exam guidelines: 2021 is the latest national edition.

## Re-verifying / re-generating

The DBE reissues ATPs yearly and term placement can shift between editions. To regenerate against a new
edition: refetch each `source_url` (check `education.gov.za`'s ATP index page if a link goes stale),
then re-run the same pdfplumber-based extraction (row matching `TOPIC(S)` / `CAPS TOPIC(S)` label,
paired with the `TERM N` header row in the same table — this pattern held across all 6 subjects once the
singular-vs-plural "TOPIC"/"TOPICS" label variance was accounted for). A mechanical re-parse alone will
reintroduce the noise catalogued above (Term 4 exam tables, merged cells, truncations) — budget a
manual verification pass against the extracted text before trusting a regenerated edition.
