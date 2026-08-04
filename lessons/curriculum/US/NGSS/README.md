# Next Generation Science Standards — open to non-profits *by name*

K-12 science content standards, adopted or adapted state by state. Developed
by the NGSS Lead States via Achieve; the trademarks transferred to **WestEd**
in May 2020; the published volume is copyright National Academies Press.

## The licence finding — and the subtlety that matters

The brief asked for NGSS's actual licence rather than an assumption. It is
open, and the grant is genuinely generous:

> The K-12 academic standards may be copied, reproduced, altered, adapted,
> edited, deleted and rearranged by states, districts, schools, teachers and
> non-profit education entities as they see fit and without permission.

Read that list of **verbs** — copy, reproduce, alter, adapt, edit, delete,
rearrange — and it looks like one of the most permissive licences in
education. Read the list of **subjects** and something narrower appears:
*states, districts, schools, teachers and non-profit education entities.* The
grant is written as an enumeration of actors, and **a for-profit product is
not among them.**

That is not a prohibition. It is *silence about our case* — which is
precisely why it is recorded as an **owner decision** rather than either a
green light or a gate:

- It is **not** the IEB's situation (an explicit "not for commercial gain").
- It is **not** the College Board's situation (an explicit refusal plus an
  anti-AI clause).
- It is a licence that simply does not address commercial reuse, leaving the
  default position of copyright underneath it.

**Action for the owner:** before NGSS-derived content ships inside a paid
product, either confirm the non-profit/educational framing or obtain written
confirmation from WestEd. Ingesting, indexing and aligning are fine now.

## The trademark rule — binding immediately, decision or not

Separate from the copyright question and not subject to it:

- "Next Generation Science Standards" and the NGSS logo are **registered
  trademarks of WestEd**.
- The logo may not be used without WestEd's express written consent.
- The marks may not appear **in the main title** of any product, service or
  publication, may not be combined with another mark or design, and may not be
  used in a way suggesting third-party ownership or endorsement.
- WestEd may request samples of material using the marks and require
  non-conforming material to be altered.

So: never an "NGSS Science" product or feature name, never the logo.
"Aligned to the NGSS" in body text is nominative use and is the intended
pattern.

Required citation, carried in every generated file:

> NGSS Lead States. 2013. Next Generation Science Standards: For States, By
> States. Washington, DC: The National Academies Press.

Full audit: `../SOURCES.md`. Machine-readable policy: `../RIGHTS.json`.

## Why this framework needs different handling from CAPS

An NGSS **performance expectation is not a content statement.** It braids
three dimensions into one assessable expectation:

- a **science and engineering practice** (8 of them, SEP1–SEP8),
- a **disciplinary core idea** (domains PS, LS, ESS, ETS),
- a **crosscutting concept** (7 of them, CCC1–CCC7).

Any lesson generator targeting NGSS has to carry all three dimensions rather
than flattening to a topic list — that is the structural difference from both
CAPS and Common Core, and the reason the practices and crosscutting concepts
are modelled as first-class skill files rather than buried in prose.

PE codes read `<grade or band>-<DCI domain+number>-<sequence>`: `K-PS2-1`,
`3-LS1-1`, `MS-PS1-1`, `HS-LS1-1`. Engineering expectations are banded across
grades, e.g. `K-2-ETS1-1`.

## Layout

```
NGSS/science/
  curriculum/ngss_k-12.json     the three dimensions, all SEPs/CCCs/DCI domains
  exam_guidelines/index.json    "no examining body" + downstream assessment
  syllabus/gradeK … grade5, grade6-8, grade9-12
  skills/practices/sep1 … sep8
  skills/crosscutting/ccc1 … ccc7
  skills/grade*/index.json
```

**No `past_papers/`** — NGSS sets no papers. The audit fails the build if the
folder appears. `exam_guidelines/` records that NGSS-aligned state science
assessments exist, are built state by state, are **not** covered by the NGSS
reuse grant, and have not been audited.

Grade axis is the framework's own: K–5 grade by grade, then the middle school
(6-8) and high school (9-12) bands. Within a band NGSS does not assign
expectations to a specific grade — states choose the course sequence.

## What is real here today

Recorded: the three-dimensional architecture, all eight practices and seven
crosscutting concepts by name, the four DCI domains, the code grammar, and the
grade/band organisation.

Not recorded: the performance expectations themselves. `nextgenscience.org` is
blocked by this environment's egress policy, so nothing has been fetched.
Every syllabus file carries an empty `performance_expectations[]` and
`parse_status: architecture_recorded_pending_source_ingest`. The
`dci_domains_available` list is the set NGSS draws from — **not** a claim
about which DCIs a given grade actually carries. That comes from the fetched
standards, not from memory and not from a third-party re-host.

When ingesting, note the PE contract: `clarification_statement` and
`assessment_boundary` must be reproduced **verbatim**. An assessment boundary
changes what may legitimately be taught and assessed at that grade, and
paraphrasing one silently changes the curriculum.
