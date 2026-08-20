# IEB curriculum tree — same CAPS content, IEB assessment

The IEB (Independent Examinations Board, ieb.co.za) administers the National
Senior Certificate for independent schools **on the same DBE CAPS
curriculum** the CAPS tree transcribes. What differs is not the content
policy but:

- **Assessment** — specified per subject by the IEB **Subject Assessment
  Guidelines (SAGs)**, reissued for each examination year: SBA composition,
  exam paper structure, cognitive-level weightings, and any IEB-specific
  content emphases. The SAG is the IEB counterpart of *both* the DBE Grade 12
  Examination Guidelines and the DBE SBA programme.
- **Pacing** — the IEB publishes no ATP equivalent; each school sets its own
  term-by-term plan.
- **Papers** — the IEB sets its own NSC papers (Grade 12 only; Grades 10–11
  are school-assessed per the SAGs, so no national Gr 10/11 IEB papers exist).

## Layout (mirrors `../CAPS`, one folder per subject)

| Layer | Path | Status |
|---|---|---|
| **Curriculum** (policy statement) | `{subject}/curriculum/ieb_gr10-12.json` | Generated pointer at the shared CAPS statement (`../CAPS/{subject}/curriculum/`) — the IEB teaches the same CAPS content, so the full text is maintained once, there. SAG overlay pending fetch. |
| **Syllabus** (content scope + default pacing) | `{subject}/syllabus/grade{10,11,12}.json` | Generated from the CAPS ATP files: topics, subtopics, prior knowledge, week spans and `requires_skills` links carry over; every DBE-assessment field (`sba`, `sba_weighting`, `sba_guidelines`, `control_test_scope`, `exam_structure`) is deliberately stripped because IEB assessment is SAG territory. Weeks are advisory (DBE pacing as a default — IEB schools self-pace). |
| **Skills** (prerequisite units) | `{subject}/skills/{grade}/{skill}.json` | Generated inheritance pointers at the CAPS skill files, same `skill_ref`s so syllabus links resolve. Skill teaching content is curriculum-neutral; only `importance.exam_weight` (DBE paper marks) does not carry — re-derive from SAG exam structures once ingested. |
| **Scope deltas** (SAG-stated content differences) | `{subject}/syllabus/scope_deltas.json` | Hand-owned ledger, seeded empty with `status: pending_sag_transcription`. Filled ONLY from the fetched official SAG; every item must cite the SAG passage it came from. An empty ledger means "not yet transcribed", never "no differences". |
| **Exam guidelines** (SAGs) | `{subject}/exam_guidelines/index.json` | Hand-owned index (seeded once, then mutated by `fetch_ieb_sources.py` — deliberately NOT generator-owned so a regenerate can't clobber recorded provenance). Source + 2026-edition document slot recorded, **pending fetch** (see below). Ingested SAGs will land next to the index as `.md` + `.json`, per the CAPS method. |
| **Past papers** | `{subject}/past_papers/index.json` | Hand-owned index (same ownership rule). Portal + guest-library recorded, **pending verification/fetch**; `sessions[]` (CAPS shape, per the index's `sessions_contract`) empty until URLs are captured; note the index's `marking_guidelines_note` — memo availability is genuinely unresolved on secondary evidence and the linking pipeline must plan for unavailable marking guidelines (request via NSCexampapers@ieb.co.za or record index-only). |
| **School calendar** | — | Deliberately absent: IEB schools follow independent-school calendars (ISASA), not the state calendar in `../CAPS/school_calendar/`. Add if a scheduler ever serves IEB students. |

`sources_manifest.json` (created on first fetch/register) is the provenance
record: URL, sha256, byte size and date for every source document.

## Honest sourcing status (2026-08-03)

The build environment that created this tree has an egress policy that
blocks ieb.co.za (proxy CONNECT 403), and ieb.co.za additionally answers
HTTP 403 to automated fetchers. So, unlike the CAPS tree, **no IEB PDF has
been fetched or hash-verified yet**. What is real here today:

- the structural derivation from CAPS (deterministic, drift-checked);
- source *locations* (SAG page, past-papers page, docs.ieb.co.za guest
  library) found via web search and recorded in every index with an explicit
  `pending_fetch` / `urls_recorded_not_verified` status — never presented as
  verified;
- the terms-of-use audit in `SOURCES.md`, including a **commercial-use flag
  that needs an owner decision before any IEB paper content is embedded**.

Nothing in this tree fabricates SAG content, IEB exam structures or paper
metadata. Consumers must treat `pending_fetch` layers as absent.

## Regenerating / completing

```
python3 lessons/scripts/IEB/build_from_caps.py          # regenerate derived layers
python3 lessons/scripts/IEB/build_from_caps.py --check  # drift check after CAPS edits
python3 lessons/scripts/IEB/audit_tree.py               # full structural audit (offline, CI-able):
                                                                   #   drift + orphans + hand-owned contracts
                                                                   #   + skills two-way sync + pointer resolution
python3 lessons/scripts/IEB/fetch_ieb_sources.py probe  # from a network-enabled machine
python3 lessons/scripts/IEB/fetch_ieb_sources.py fetch-sags
python3 lessons/scripts/IEB/fetch_ieb_sources.py fetch-papers
```

Ownership rule the scripts enforce between them: `build_from_caps.py` owns
only the CAPS-derived layers (curriculum pointer, syllabus grade files,
skills pointers); the assessment-layer indexes and scope-delta ledgers are
hand-owned and mutated by `fetch_ieb_sources.py`/curation, so regeneration
never clobbers recorded provenance. `audit_tree.py` is the contract keeper
for the hand-owned half (and catches orphaned generated files the drift
check can't see).

Then curate each fetched SAG the way the 18 CAPS ATPs were curated: full
decoded text as `exam_guidelines/grade12_{year}.md`, structured extraction
(SBA composition, paper structure, weightings) as `grade12_{year}.json`, a
manual pass against the source text before trusting any mechanical
extraction, then fill each subject's `syllabus/scope_deltas.json` and add
IEB exam-weight overlays for the skills layer. No numbers may be
transcribed from third-party SAG re-uploads (Studocu/Scribd) — only from
the fetched official PDF.
The scripts live in `lessons/scripts/IEB/` (separate from the CAPS
pipeline scripts in `lessons/scripts/CAPS/`, which are read-only
reference for the method).
