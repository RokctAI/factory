# AP — GATED. Nothing may be ingested without written permission.

The College Board's Advanced Placement programme. A commercial examination
board, structurally much closer to Cambridge or the IEB than to Common Core
or NGSS — and its terms are **stricter than the IEB's**.

> **Status: `blocked_pending_written_permission`.**
> This subtree contains structure, links and rights metadata **only**. No AP
> content — no question text, no scoring guidelines, no Course and Exam
> Description prose, no unit or topic lists — is present, and none may be
> added until permission is obtained and recorded in `../RIGHTS.json`.

## Why the gate is closed, and why it is tighter than IEB/Cambridge

Four separate restrictions, each sufficient on its own:

1. **Express written permission for any reproduction.** *"No copyrighted
   material or College Board content may be performed, distributed,
   downloaded, uploaded, modified, reused, reproduced, reposted,
   retransmitted, disseminated, sold, published, broadcast or circulated
   without express written permission from the College Board."*
2. **Non-commercial only.** Services are *"provided solely for non-commercial
   use"* — not to make money, and not as part of any test prep or other
   business.
3. **Released exams are classroom-copy-only.** Teachers may download released
   questions and copy them for their own students in a classroom setting; the
   materials *"may not be posted on school or personal websites, nor
   electronically redistributed for any reason."*
4. **The AI clause — the decisive one for this repository.** College Board
   *"does not grant permission for its copyrighted content, including practice
   test questions, to be used in conjunction with generative AI or similar
   technologies"*, and does not permit training any AI system on its content.

Point 4 is what makes this different in kind from the IEB. The IEB bars
reproduction *for commercial gain* and says nothing about AI; an internal
non-commercial build would arguably have been fine there. This repository is a
pipeline that feeds curriculum material to a model — so feeding it an AP
question, a scoring guideline or a CED is squarely the prohibited act **even
for a non-commercial internal build**.

**Therefore permission must explicitly cover three things**, and a generic
reproduction permission does not reach the third:

- (a) reproduction,
- (b) commercial use, if the product is paid,
- (c) use in conjunction with generative AI.

Request via the [College Board permission
form](https://privacy.collegeboard.org/copyright-trademark/request-form).
One request should cover AP and SAT together — same rights holder, same
policy — but do not treat an AP permission as covering SAT unless the granted
permission says so.

## The shortcut that must not be taken

AP unit lists, topic breakdowns and exam weightings are widely republished by
test-prep sites and CED summarisers. Transcribing from one of those would
**launder a prohibited reproduction** into this tree while looking like
original research. It is the exact analogue of the Studocu/Scribd exclusion in
the IEB audit, and `../scripts/audit_tree.py` fails the build if any file
cites one of those domains.

The same rule is why `exam_guidelines/index.json` has `exam_structure: null`
rather than a format summary lifted from a blog — unlike SAT, where the
published test format is recorded as reported fact with its provenance and
confidence stated.

## How the gate is enforced

Not by convention — by CI:

- `audit_tree.py` fails the build if **any** content array under
  `AP/**/{curriculum,exam_guidelines,syllabus,past_papers}/**` is non-empty,
  or if a `sources_manifest.json` appears (which would mean documents were
  fetched).
- `fetch_us_sources.py fetch AP` **refuses**, prints why, prints the
  permission URL, and exits 2. There is deliberately no `--force` — clearing
  the gate is an edit to `RIGHTS.json` by the owner, backed by a recorded
  permission.

Verified: populating `sessions[]` in a past-papers index makes the audit exit
1 with a `RIGHTS GATE VIOLATION`.

## Layout, and the one deviation

```
AP/
  courses.json                 registry: 16 scaffolded, 24 more listed
  {course}/
    curriculum/ced.json        what a CED is; content gated
    exam_guidelines/index.json exam_structure: null, gated
    syllabus/course.json       units: [], gated
    skills/course/index.json   gated (but see below)
    past_papers/index.json     sessions: [], gated
```

**`syllabus/course.json`, not `syllabus/{grade}.json`.** AP has no grade axis
at all — the College Board prescribes no grade for a course; schools place
them where their sequence allows. Emitting `grade11.json`/`grade12.json` would
manufacture curriculum structure that does not exist. This is the same
reasoning that omits `past_papers/` from Common Core and NGSS: never fabricate
a distinction the framework does not make. `skills/course/` follows for
consistency.

## What *can* be worked on while the gate is closed

Prerequisite skills that are **not** College Board content. The algebra a
student needs before Calculus AB, the stoichiometry before AP Chemistry —
written from general subject knowledge, these are ours to author, and
`skills/course/index.json` says so explicitly. What may **not** happen is
transcribing the CED's named course skills, or deriving them by working
backwards from released questions.

## Course registry

16 courses are scaffolded, chosen to line up with the subject spine this
repository already teaches (mathematics, physical sciences, economics,
geography) plus the English pair matching Common Core ELA. The remaining ~24
official courses are listed in `courses.json` as `not_yet_scaffolded`.

Scaffolding another is a one-line edit to `AP_SCAFFOLDED_COURSES` in
`../scripts/us_spec.py` plus a regenerate — no new code. There is little value
in scaffolding all forty while the gate blocks content for every one of them.

Verify the course list against `apcentral.collegeboard.org` before relying on
it: the College Board adds and retires courses, and this list was recorded
from search results on 2026-08-04, not read first-hand.
