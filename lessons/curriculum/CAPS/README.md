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
that every link resolves. Each skill also carries an `importance` block telling the student why it
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
tasks and exam structure (see Layout above for the schema). Deliberately NOT transcribed:
week-level spans/hours (the ATP grids carry them, but column boundaries are ambiguous in
extraction — re-derive from the source PDFs if pacing-by-week is ever needed), Physical Sciences'
requisite-pre-knowledge rows (week-granular and repetitive in that ATP; other subjects' per-topic
rows ARE transcribed), and resources/informal-assessment rows (teaching aids, not syllabus).

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

## Re-verifying / re-generating

The DBE reissues ATPs yearly and term placement can shift between editions. To regenerate against a new
edition: refetch each `source_url` (check `education.gov.za`'s ATP index page if a link goes stale),
then re-run the same pdfplumber-based extraction (row matching `TOPIC(S)` / `CAPS TOPIC(S)` label,
paired with the `TERM N` header row in the same table — this pattern held across all 6 subjects once the
singular-vs-plural "TOPIC"/"TOPICS" label variance was accounted for). A mechanical re-parse alone will
reintroduce the noise catalogued above (Term 4 exam tables, merged cells, truncations) — budget a
manual verification pass against the extracted text before trusting a regenerated edition.
