# Common Core State Standards — open licence, hard attribution

Content standards for Mathematics and English Language Arts & Literacy,
adopted state by state. **Not a federal curriculum, and not public domain.**

## The licence finding

The brief for this tree asked whether Common Core is genuinely open, and
warned against assuming it is — correctly, as it turns out, though not in the
direction one might expect. It is *more* open than the IEB and *less* open
than public domain:

- The standards are **copyrighted** by the NGA Center for Best Practices and
  CCSSO. State adoption does not place them in the public domain; it only
  exempts adopting states from the licence's attribution provision.
- They are released under NGA Center/CCSSO's own **public licence**: a
  *"limited, non-exclusive, royalty-free license to copy, publish, distribute,
  and display"* the standards *"for purposes that support the Common Core
  State Standards Initiative"*.
- There is **no non-commercial clause** — the material difference from the
  IEB, whose terms say ©IEB material *"may not be reproduced for commercial
  gain"*. What Common Core has instead is a **purpose** limitation, which
  teaching CCSS-aligned lessons satisfies on any ordinary reading.
- Two conditions bind us. NGA Center/CCSSO must be acknowledged as sole owners
  and developers, with no contrary claims. And any publication or public
  display must carry, verbatim:

  > © Copyright 2010. National Governors Association Center for Best Practices
  > and Council of Chief State School Officers. All rights reserved.

- The licence covers the **standards only, not the examples embedded in
  them** — some are public-domain material, others were used under
  third-party permission. Do not reproduce the examples.

**No permission gate.** But the notice is an obligation, not a courtesy: it is
carried in every generated file's `rights.attribution_notice` and verified by
`../scripts/audit_tree.py`. Nothing yet propagates it into rendered lesson
output — wire that up before CCSS content reaches a student.

Full audit: `../SOURCES.md`. Machine-readable policy: `../RIGHTS.json`.

## Watch out for the wrong site

`thecorestandards.org` is **not** the Common Core site. It is an unofficial
mirror that CCSSO has publicly demanded be taken offline citing copyright
infringement. It reproduces the licence text accurately and ranks well in
search, which is exactly what makes it a trap. The audit excludes it and the
build **fails** if any file references it.

Primary source: `corestandards.org` (CCSSO). CCSSO's own `learning.ccsso.org`
hosts the standards PDFs; search results in August 2026 suggested
`corestandards.org` was serving a reduced site during technical work, so
confirm which host is live at fetch time and record the one actually used.

## Layout

```
COMMON_CORE/
  math/
    curriculum/ccss_math_k-12.json      architecture + the 8 practice standards
    exam_guidelines/index.json          "no examining body" + downstream assessment
    syllabus/gradeK … grade8, grade9-12
    skills/practices/mp1 … mp8          cross-grade practice standards
    skills/grade{K..8,9-12}/index.json  grade-scoped skills (pending)
  ela/
    curriculum/ccss_ela_k-12.json
    exam_guidelines/index.json
    syllabus/gradeK … grade8, grade9-10, grade11-12
    skills/practices/{reading,writing,speaking_listening,language}_anchors.json
    skills/grade*/index.json
```

**No `past_papers/`.** Common Core is a standards framework with no examining
body — it sets no papers and awards no certificate. An empty folder would
imply papers exist and are merely un-indexed, so the audit *fails the build*
if one appears.

`exam_guidelines/` is kept, though, and it is not empty of meaning: it records
that the assessment layer genuinely exists but belongs to somebody else — the
state assessment programmes built on the standards (Smarter Balanced, the
PARCC successors, state-specific tests). **Each has its own rights holder and
its own terms, none covered by the CCSS public licence, and none audited.**
Audit separately before ingesting any of them.

## Grade axis

Maths is `gradeK`–`grade8` then a single `grade9-12`: CCSS high school
mathematics is organised into conceptual categories (Number and Quantity,
Algebra, Functions, Geometry, Statistics and Probability, plus the Modeling
category that has no standards of its own) spanning 9–12 rather than assigned
to grades. Splitting it into `grade9`…`grade12` would invent a sequencing
decision the standards deliberately leave to states and districts.

ELA is `gradeK`–`grade8` then `grade9-10` and `grade11-12` — the bands the
standards themselves use.

## What is real here today

Recorded: the framework architecture — the domain set for each grade, the ELA
strand sets (RF is K-5 only; RH/RST/WHST are 6-12 only), the eight Standards
for Mathematical Practice by name, the CCR anchor counts, and the identifier
grammar (`CCSS.MATH.CONTENT.5.NF.A.1`, `CCSS.ELA-LITERACY.RST.6-8.3`).

Not recorded: cluster headings and standard text. The PDFs have not been
fetched — this environment's egress policy blocks `corestandards.org`. Every
syllabus file carries `parse_status:
architecture_recorded_pending_source_ingest` and empty `clusters`/`standards`
arrays. **An empty array means "not yet transcribed", never "the grade has
none".**

## Pacing

There is none, deliberately. Common Core prescribes no pacing — there is no
CCSS equivalent of a DBE Annual Teaching Plan, so no `terms` array is emitted.
Term and week placement is a state, district or school decision. A scheduler
wanting US pacing must source a district scope-and-sequence, which is a
different document with its own rights position.
