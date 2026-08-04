# SAT Suite — GATED. Same rights holder as AP, same policy, same gate.

The College Board's SAT Suite of Assessments: SAT, PSAT/NMSQT, PSAT 10 and
PSAT 8/9.

> **Status: `blocked_pending_written_permission`** — identical to `../AP/`.

## Same policy — confirmed, not assumed

The brief asked whether College Board's terms cover AP and SAT under one
policy, and if so to confirm it explicitly rather than re-running the same
audit or leaving SAT looking separately unverified. They do, and here is the
basis:

- The AP audit was run against College Board's **organisation-level** Terms of
  Use (`collegeboard.org/terms/terms-of-use`) and its **single** Copyright and
  Trademark policy (`privacy.collegeboard.org/copyright-trademark/`). Neither
  is scoped to a programme — they are published for the organisation.
- The **generative-AI refusal** is written against *"College Board's
  copyrighted content, including practice test questions"*. Not AP-scoped
  either; "practice test questions" is if anything SAT-flavoured language.
- The same pass surfaced SAT-specific *applications* of that one policy,
  which confirm rather than complicate it:
  - reproduction from *The Official SAT Study Guide* and *The Official SAT
    Teacher's Guide* is **not allowed in any manner**;
  - *The Official SAT Practice Test* may be used by a student in a
    non-commercial educational setting **but not in a test prep course**;
  - the **SAT Suite Question Bank** and released questions are licensed
    *"non-exclusive, limited and revocable … for the purpose of classroom
    teaching and internal reporting only"*, with no uploading, posting online,
    caching, reproducing, modifying, displaying, editing, altering or
    enhancing without express written permission.

**One rights holder, one policy, one gate.** So the SAT gate is not an
inherited assumption — it is the same audit reaching the same document set.
Recorded explicitly in `../RIGHTS.json` under `same_policy_as: "AP"` with the
reasoning, so nobody later mistakes it for an un-audited copy-paste.

A single permission request should cover both programmes. Do **not** treat an
AP permission as covering SAT, or vice versa, unless the granted permission
says so. Request via the [College Board permission
form](https://privacy.collegeboard.org/copyright-trademark/request-form).

## The one thing recorded here — and why it is not a breach

`exam_guidelines/index.json` carries the digital SAT's **published format**:

- 98 questions / 134 minutes total
- Reading and Writing: 54 questions, 64 minutes, two 27-question modules
- Math: 44 questions, 70 minutes, two 22-question modules, calculator
  throughout
- section-adaptive: module 1 performance sets module 2's difficulty

This is **factual reporting about the test's shape**, which College Board
itself publishes — not reproduction of test content. How long a test is and
how many questions it has is a fact, not creative expression. Content
domains (Information and Ideas, Craft and Structure, Expression of Ideas,
Standard English Conventions; Algebra, Advanced Math, Problem-Solving and Data
Analysis, Geometry and Trigonometry) are recorded on the same basis: they are
the test's public score-reporting structure.

The **skill/knowledge testing points inside those domains are content** and
are gated, as are score scales and concordance tables.

**Caveat recorded in the file itself:** these figures were corroborated across
multiple secondary sources in August 2026 but **not** confirmed against
College Board's own specification, which this environment could not reach. The
`confidence` field says so. Resolve before any student-facing use.

## Layout

```
SAT/
  reading_writing/
    curriculum/sat_suite.json   content domains + suite structure
    exam_guidelines/index.json  published format (fact) + gated content
    syllabus/grade8-9, grade10, grade11-12
    skills/grade*/index.json
    past_papers/index.json      sessions: [], gated
  math/                         same shape
```

**Subjects are the two test sections**, because that is how the SAT is
structured and reported — there is no subject axis otherwise.

**The grade axis is the Suite's own band structure**, which unlike AP is
genuinely grade-scoped: `grade8-9` (PSAT 8/9), `grade10` (PSAT 10 and
PSAT/NMSQT, also taken in grade 11), `grade11-12` (SAT). The Suite is
vertically scaled — the same content domains run across all four assessments,
with difficulty rather than domain set changing by band.

## `past_papers/` here means something slightly different

College Board does not release live SAT forms the way the DBE releases NSC
papers. The analogue is the released full-length practice tests plus the SAT
Suite Question Bank — recorded in `past_papers/index.json` with that
distinction stated, and gated.

## What *can* be worked on while the gate is closed

Prerequisite skills authored from general subject knowledge — the algebra
fluency a student needs, the reading strategies. What may **not** happen is
transcribing College Board's skill/knowledge testing points, or deriving
skills by working backwards from released questions, which reaches the same
protected content by another route.

## Enforcement

Same as AP: `audit_tree.py` fails the build on any non-empty content array
under `SAT/**/{curriculum,exam_guidelines,syllabus,past_papers}/**` or any
`sources_manifest.json`; `fetch_us_sources.py fetch SAT` refuses and exits 2,
with no `--force`.
