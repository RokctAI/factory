# US curriculum tree — four frameworks, four different kinds of thing

`lessons/curriculum/US/` is not one curriculum. It is four subtrees that
happen to share a country, and the single most important structural decision
here is that they are kept apart:

| Subtree | What it actually is | Rights holder | Gate |
|---|---|---|---|
| `COMMON_CORE/` | Content standards (Maths, English Language Arts) | NGA Center + CCSSO | **attribution required** |
| `NGSS/` | Content standards (Science) | NGSS Lead States; trademark WestEd | **owner decision** for for-profit use |
| `AP/` | Examination programme (commercial exam board) | College Board | **BLOCKED pending written permission** |
| `SAT/` | Examination programme (same board, same policy) | College Board | **BLOCKED pending written permission** |

The first two publish statements of what a student should know by a grade.
They have no examining body, set no papers and award no certificate. The
second two are exam programmes run by a commercial board — much closer to
Cambridge or the IEB than to a standards document. Flattening them into a
single "US curriculum" would put an openly-licensed public standard and a
rights-gated commercial exam product under the same handling rules, which is
exactly the mistake this layout exists to prevent.

## The headline for the owner

**AP and SAT need the same commercial-reproduction permission gate as
IEB/Cambridge — and they are stricter.** The IEB bars reproduction *for
commercial gain*. The College Board bars commercial use, bars redistributing
released exams outside classroom copying, **and expressly refuses permission
for its content to be used with generative AI or to train AI systems.** That
last clause is aimed squarely at what this repository is: a pipeline that
feeds curriculum material to a model. A generic reproduction permission would
not cover it — permission has to name the AI use.

Common Core and NGSS do **not** need that gate. They carry obligations, not
gates:

- **Common Core** is *not* public domain (a common and reasonable assumption
  that turns out to be wrong — see `SOURCES.md`). It is copyrighted by NGA
  Center/CCSSO and released under their own written public licence, which is
  broad but purpose-limited, and which makes a specific copyright notice
  mandatory on any publication or public display.
- **NGSS** grants permission-free reuse to an *enumerated* list of actors —
  "states, districts, schools, teachers and non-profit education entities". A
  for-profit product is not on that list. That is silence about our case
  rather than a prohibition, which is why it is an owner decision rather than
  a gate. The trademark rules apply immediately regardless.

`RIGHTS.json` is the machine-readable version of all of this, and
`scripts/audit_tree.py` **enforces** it: the build fails if gated content is
ever ingested, and `scripts/fetch_us_sources.py` refuses to fetch from a
gated rights holder at all (there is deliberately no `--force`).

## Layout

Same convention as `../CAPS` and `../IEB` — one folder per subject, with
`curriculum/`, `exam_guidelines/`, `syllabus/`, `skills/` and, where it
applies, `past_papers/`.

```
US/
  RIGHTS.json          policy of record (machine-readable, CI-enforced)
  SOURCES.md           terms-of-use audit, one row per source
  scripts/             build + audit + fetch (this tree's own, per owner rule)
  COMMON_CORE/{math,ela}/
  NGSS/science/
  AP/{16 courses}/
  SAT/{math,reading_writing}/
```

### Where the convention bends, and why

Two deviations, both because forcing the convention would fabricate a
distinction the framework does not make:

- **No `past_papers/` under `COMMON_CORE/` or `NGSS/`.** Neither sets papers.
  An empty `past_papers/` folder would imply papers exist and are merely
  un-indexed. The audit *fails the build* if one appears. Their
  `exam_guidelines/index.json` is kept, though — it records that the
  assessment layer exists but belongs to somebody else (state assessment
  programmes), each with its own rights holder and its own un-run audit.
- **`AP/{course}/syllabus/course.json`, not `syllabus/{grade}.json`.** AP has
  no grade axis at all; the College Board prescribes no grade for a course.
  Inventing `grade11.json`/`grade12.json` would be manufacturing curriculum
  structure. Same reasoning, same rule.

The grade axis elsewhere is taken from each framework rather than from CAPS:

| Subtree | Grade axis | Why |
|---|---|---|
| Common Core maths | `gradeK`–`grade8`, `grade9-12` | CCSS high school is organised by conceptual category across 9–12, not by grade |
| Common Core ELA | `gradeK`–`grade8`, `grade9-10`, `grade11-12` | the bands the standards themselves use |
| NGSS | `gradeK`–`grade5`, `grade6-8`, `grade9-12` | the bands the standards themselves use |
| SAT | `grade8-9`, `grade10`, `grade11-12` | the SAT Suite's own band structure (PSAT 8/9, PSAT 10 / NMSQT, SAT) |

## Honest sourcing status (2026-08-04)

Read this before trusting any layer.

**No source document has been fetched, and no terms page was read
first-hand.** This build environment's egress policy blocks
`corestandards.org`, `nextgenscience.org`, `collegeboard.org` and
`apcentral.collegeboard.org` — the proxy answered 403 to CONNECT for all four
— and the server-side fetch tool was refused (HTTP 403) by every host tried,
including a neutral control, so it was not a per-site block but a
session-wide one. Every licence quote in `SOURCES.md` and `RIGHTS.json` comes
from a **search-indexed copy of the rights holder's own page**.

That is the same position the IEB tree is in, and it is recorded the same
way. What is real here today:

- the **rights audit** and the gates derived from it — conservative readings,
  which may only be *loosened* on first-hand evidence;
- the **framework architecture** — CCSS domains per grade, ELA strands, the
  eight mathematical practices, the NGSS three dimensions, SAT content
  domains. These are stable, well-established structural facts, recorded with
  `parse_status: architecture_recorded_pending_source_ingest`;
- **source locations**, recorded with explicit `urls_recorded_not_verified`
  status and never presented as verified.

What is deliberately **not** here: standard text, cluster headings, NGSS
performance expectations, AP unit lists, SAT testing points. Every one of
those is `pending_source_ingest` or `blocked_pending_written_permission`.
**Consumers must treat a pending layer as absent, not as an empty
curriculum.** Nothing in this tree fabricates standard text.

One trap worth naming, because it is well-indexed and looks authoritative:
`thecorestandards.org` is **not** the Common Core site. It is an unofficial
mirror that CCSSO has publicly demanded be taken offline citing copyright
infringement. It reproduces the real licence text accurately, which is
precisely what makes it dangerous to cite. The audit excludes it and
`audit_tree.py` fails the build if any file in the tree references it. The
primary source is `corestandards.org`, with CCSSO's own `learning.ccsso.org`
hosting the documents.

## Running it

```
python3 lessons/curriculum/US/scripts/build_us_tree.py           # regenerate derived layers
python3 lessons/curriculum/US/scripts/build_us_tree.py --check   # drift check
python3 lessons/curriculum/US/scripts/audit_tree.py --verbose    # full audit (offline, CI-able, exit 1 on failure)
python3 lessons/curriculum/US/scripts/fetch_us_sources.py probe  # from a network-enabled machine
```

Ownership rule the scripts enforce between them, inherited from the IEB tree:
`build_us_tree.py` owns the generated layers (`curriculum/`, `syllabus/`,
`skills/`) and overwrites them freely; the assessment-layer indexes
(`exam_guidelines/index.json`, `past_papers/index.json`) are **hand-owned**,
seeded once and never regenerated, so a rebuild can never clobber recorded
provenance or a rights decision.

Scripts live here rather than in `lessons/scripts/` by owner instruction —
the CAPS pipeline scripts are read-only reference for the method.

## What happens next

1. Run `fetch_us_sources.py probe` from a network-enabled machine, fold the
   first-hand robots/terms findings into `SOURCES.md`, and set
   `RIGHTS.json.verification_method` to `first_hand` with the date.
2. `fetch COMMON_CORE` and `fetch NGSS`, then curate each PDF the way the 18
   CAPS ATPs were curated: full decoded text as `.md`, structured extraction
   as `.json`, and a manual pass against the rendered pages before trusting
   any mechanical extraction.
3. Author the skills layer once standards text exists, so each skill anchors
   to real standard codes.
4. **AP and SAT stay untouched** until written permission covering
   reproduction, commercial use and generative-AI use is obtained and
   recorded in `RIGHTS.json`. One request should cover both — same rights
   holder, same policy — but do not assume an AP permission covers SAT unless
   the granted permission says so.
