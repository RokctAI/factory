# Cambridge curriculum tree — a curriculum author, not an assessor of someone else's

`lessons/curriculum/CAMBRIDGE/` covers **Cambridge International Education**
(Cambridge Assessment International Education, part of Cambridge University
Press & Assessment) — a **global** qualification provider whose syllabuses are
taught in schools worldwide and are not tied to any one country's national
curriculum.

That last point drives the single most important structural decision here:

> **Cambridge authors its own curriculum.** The IEB tree next door assesses the
> DBE's CAPS curriculum, so its content layer legitimately *references* CAPS.
> Cambridge does not. Its content authority is the per-subject **Cambridge
> syllabus document**, and no file in this tree may derive content from, or
> fall back to, the CAPS or IEB trees. `lessons/scripts/CAMBRIDGE/audit_tree.py`
enforces this:
> it fails the build if a Cambridge syllabus file's topic list turns out to be
> a subset of the CAPS topic list for the same subject and grade.

## The headline for the owner

**Access is open; reproduction is not.** Cambridge publishes question papers,
mark schemes, examiner reports and specimen materials openly on its own website
— and separately, explicitly, refuses permission for electronic publication of
that material in any format, commercial or not. The two facts are independent
and must not be collapsed.

| Document class | Access | Gate |
|---|---|---|
| **Syllabuses** | public, no login | `owner_decision_required` — only for *shipping* substantial prose, not for the mapping work |
| **Past papers** | public, no login | **`blocked_pending_written_permission`** |
| **Mark schemes, examiner reports** | public, no login | **`blocked_pending_written_permission`** |
| **Specimen materials** | public, no login | **`blocked_pending_written_permission`** (conservative inference — see `SOURCES.md`) |
| **Text & data mining / AI use** | — | `owner_decision_required` — commercial TDM rights are expressly reserved |

Consequences worth stating plainly:

- **The CAPS/DBE past-paper worked-example pipeline has no Cambridge
  equivalent.** `lessons/scripts/past_papers.py` works by embedding real
  question text, memo working and answers into lesson content. For Cambridge
  that is exactly the electronic reproduction Cambridge refuses. It must not be
  pointed at Cambridge material without a written grant on file.
- **A generic reproduction permission would not be enough.** This repository
  feeds curriculum material to a model, and Cambridge expressly reserves
  commercial text-and-data-mining rights. Any permission sought must name the
  AI use — the same conclusion the US tree reached about the College Board.
- Stricter than the **IEB** (which bars reproduction *for commercial gain* but
  permits personal study use); same bracket as **AP/SAT** in `../US/RIGHTS.json`.

`RIGHTS.json` is the machine-readable policy of record — same filename and same
`gate_levels` vocabulary as `../US/RIGHTS.json`, so a consumer can walk
`curriculum/*/RIGHTS.json` and compare postures across every tree. The keyed
unit differs (`document_classes` rather than `frameworks`) because Cambridge is
a single rights holder whose permissions vary by document class rather than by
framework. Full evidence and the terms audit are in `SOURCES.md`.

## Layout (mirrors `../CAPS` and `../IEB`, one folder per subject)

```
CAMBRIDGE/
  RIGHTS.json           policy of record (machine-readable, CI-enforced)
  SOURCES.md            terms-of-use audit + evidence trail
  stage_alignment.json  Cambridge stage <-> repo grade convention
  scripts -> lessons/scripts/CAMBRIDGE/   (this tree's scripts)
    subject_registry.json      the verified-facts store — the ONLY place a
                               Cambridge fact is introduced by hand
    build_cambridge_tree.py    materialises the tree from the registry
    audit_tree.py              structure + drift + rights + content guard
    fetch_cambridge_sources.py fetch & provenance (syllabuses only)
  {subject}/
    curriculum/cambridge_curriculum.json  qualifications + content authority
    syllabus/grade{10,11,12}.json         stage-resolved; content pending ingestion
    exam_guidelines/index.json            assessment-document index
    skills/{grade}/candidates.json        prerequisite-skill transfer work-list
    past_papers/index.json                access + policy record (NOT a link index)
```

Subjects are the same six as CAPS and IEB — `accounting`, `economics`,
`geography`, `mathematical_literacy`, `maths`, `physical_sciences` — so tooling
walking `curriculum/{CAPS,IEB,CAMBRIDGE}/{subject}/…` needs no per-tree special
cases. **Two of them do not map cleanly, and that is recorded rather than
smoothed over.**

## Where the six subjects don't fit Cambridge

| Repo subject | Cambridge mapping | Note |
|---|---|---|
| `maths` | IGCSE **0580**, AS & A Level **9709** | Clean. But IGCSE has a Core/Extended **tier split** and A Level is assembled from **chosen components** — neither has a CAPS analogue. |
| `geography` | IGCSE **0460**, AS & A Level **9696** | Clean by name; different themes, plus a coursework-or-written-alternative choice CAPS lacks. |
| `accounting` | IGCSE **0452**, AS & A Level **9706** | Clean by name; Cambridge uses international/IAS-style terminology where CAPS uses South African conventions. |
| `economics` | IGCSE **0455**, AS & A Level **9708** | Clean. New 0455 syllabus began teaching in 2025-26, so edition selection matters. |
| `physical_sciences` | **composite** — the pair 0625 Physics + 0620 Chemistry (IGCSE), 9702 + 9701 (AS & A Level) | SA Physical Sciences is physics+chemistry in one subject. Cambridge **had** exactly that — IGCSE Physical Science **0652** — but it is **withdrawn, final exams November 2026**. Every surviving combined option (0653, 0654) adds Biology, and at AS/A Level there is no combined science at all. So one repo subject maps to **two Cambridge subjects**. |
| `mathematical_literacy` | **none** | Cambridge publishes no equivalent. Its whole maths suite is academic; the Core tiers of 0580/0607 are grade-capped tiers of academic maths, not numeracy-in-context. The folder exists so the layout stays uniform, and records the absence explicitly. **A Cambridge stream must not substitute 0580 Core, and must not fall back to CAPS or IEB.** |

## Grades are a repository convention, not a Cambridge fact

Cambridge uses its own stages (Upper Secondary = IGCSE/O Level, Advanced =
AS & A Level), not national grade numbers — and **disclaims a mapping**: it
states its age ranges are for guidance only, that there are no formal age
regulations for IGCSE entry, that centres set their own entry policy, and that
IGCSE runs one year rather than two in some countries. Cambridge assigns
internal stage numbers only to Primary and Lower Secondary.

So `stage_alignment.json` records a **repository convention**, repeated as a
caveat inside every syllabus file:

- `grade10` + `grade11` → Cambridge IGCSE (the two-year course, exams at the end)
- `grade12` → Cambridge International **AS Level**

with alternative pathways recorded alongside. **Unresolved and deliberately not
invented:** a full A Level is a two-year course of which AS is year one, so a
school on the default pathway sits A2 in a thirteenth year that has no
grade12-keyed slot in this contract. A Level must not be silently folded into
`grade12`.

## Honest status (2026-08-04)

Cambridge hosts are blocked by this build environment's egress policy (proxy
CONNECT 403), and no page fetch of any host succeeded. So:

- **No Cambridge document has been fetched or hash-verified.** Every syllabus
  entry carries `status: pending_fetch`, and every URL a `url_status` recording
  that it was *observed in a search result*, not fetched.
- URLs are recorded **only** where the URL itself appeared in a search result
  with its subject attribution. The landing-page and document URL patterns are
  documented but **deliberately not used to construct URLs** — the document id
  is opaque and a plausible-but-wrong URL is worse than a null.
- Assessment structures (paper counts, durations, marks, weightings) are
  **deliberately absent**. Research surfaced candidate figures and also
  surfaced live traps — 0580 was restructured for 2025 and revision sites still
  publish the pre-2025 marks as current; 0452's figures conflict between
  sources. Those traps are recorded as `research_notes` in the registry so the
  curation pass knows what to check, but no number enters the tree except from
  a fetched official syllabus.
- Nothing here is fabricated. An empty topic list means *not yet ingested*,
  never *this grade has no content*.

## How the pieces fit

```
subject_registry.json  --build_cambridge_tree.py-->  the whole tree
         ^
         |
fetch_cambridge_sources.py writes fetch status + sha256 back HERE
```

The registry is the single writer-owned source of truth and the tree is a pure
function of it. This is deliberately different from the IEB tree, where a
generator and a fetch script both wrote to the same index files (fixed there by
making those indexes hand-owned). Here the conflict cannot arise: the fetch
script updates facts in the registry and the tree is regenerated. That is what
lets `--check` be a **total** drift gate — every JSON file in the tree is
generated, so any hand edit anywhere in it is caught.

```
python3 lessons/scripts/CAMBRIDGE/build_cambridge_tree.py          # regenerate
python3 lessons/scripts/CAMBRIDGE/build_cambridge_tree.py --check  # drift gate
python3 lessons/scripts/CAMBRIDGE/audit_tree.py                    # full audit (CI-able)
python3 lessons/scripts/CAMBRIDGE/fetch_cambridge_sources.py probe # network-enabled machine
```

Run `probe` **first**: `robots.txt` for cambridgeinternational.org is the
largest open evidentiary gap and must be read before any bulk fetching.

## Completing the tree

1. **Probe** — read `robots.txt` and the terms pages first-hand; reconcile
   against `RIGHTS.json` and update `SOURCES.md`. A gate may only be loosened
   on first-hand evidence.
2. **Discover + fetch syllabuses** — harvest real document URLs from each
   subject's landing page (`discover`), then `fetch-syllabuses`. Provenance
   (URL, sha256, size, date) lands in `sources_manifest.json`; the PDFs
   themselves are gitignored and never committed.
3. **Curate** — the same hand pass the 18 CAPS ATPs received: full decoded text
   plus a structured extraction of topics, learning objectives and the
   assessment specification, verified against the rendered pages. Then the
   syllabus `topics` and the exam-guidelines `assessment_structure` stop being
   empty.
4. **Skills** — the `skills/{grade}/candidates.json` registers list CAPS
   prerequisite skills as **candidates** with `transfers: null`. After syllabus
   ingestion, confirm each against the Cambridge syllabus and author
   Cambridge-specific skills that CAPS never defined. `exam_weight` and
   `covered_by` from CAPS never transfer — they describe a different
   qualification's papers and a different curriculum's lessons.
5. **Past papers** — nothing to do, and that is the finding. Revisit only if a
   written permission grant is obtained and recorded in `SOURCES.md`.

Deliberately absent: a **school calendar**. Cambridge is global and sits
alongside many national calendars; its own fixed points are examination series
(June, November, and March in India), not term dates. `../CAPS/school_calendar/`
has no Cambridge analogue and inventing one would be wrong.
