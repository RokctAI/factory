# IEB curriculum tree — sources-first, same contract as CAPS

The IEB (Independent Examinations Board) is South Africa's independent, Umalusi-accredited
assessment body. It is **not a curriculum author**: IEB NSC examinations assess the same
national CAPS FET (Grades 10–12) curriculum as the DBE stream. What is IEB-specific is the
**assessment layer** — the per-subject Subject Assessment Guidelines (SAGs), which fix the
NSC examination structure and the Grades 10–12 school-based assessment requirements for IEB
member schools, and the IEB's own NSC examination papers.

That single fact drives every design decision in this tree: curriculum *content* is
referenced from the CAPS tree (one source of truth, zero duplication), while everything the
IEB itself publishes (SAGs, past papers) is indexed here with real sources and an honest
verification trail, exactly like `../CAPS`.

## Layout (mirrors `../CAPS` per subject)

```
IEB/
  README.md                       <- this file
  .gitignore                      <- fetched PDFs are never committed (same rule as CAPS past_papers)
  scripts/
    ieb_sources.py                <- IEB-owned sourcing tool: list / audit / verify / fetch
    README.md                     <- how to capture ieb.co.za URLs + run the fetch pass
  {subject}/
    curriculum/index.json         <- content authority: points at the ingested CAPS policy text
    syllabus/grade{10,11,12}.json <- CAPS content universe + IEB pacing model + scope-delta ledger
    exam_guidelines/sag_index.json<- SAG document index (the IEB counterpart of DBE exam guidelines)
    skills/{grade}/manifest.json  <- CAPS skills that transfer, by reference, with the exam-weight caveat
    past_papers/index.json        <- IEB NSC past-paper portal index (sessions[] populated on fetch)
```

Subjects: `accounting`, `economics`, `geography`, `mathematical_literacy`, `maths`,
`physical_sciences` — the same six as CAPS, same folder names, so tooling that walks
`curriculum/{CAPS,IEB}/{subject}/...` needs no per-tree special cases.

## What each layer means here

| Layer | IEB reality | What the file does |
|---|---|---|
| **Curriculum** | IEB assesses CAPS; there is no separate IEB policy statement. | `curriculum/index.json` points at `../CAPS/{subject}/curriculum/caps_gr10-12.{md,json}` (already ingested, page-anchored) and at the SAG overlay. |
| **Syllabus** | The IEB publishes **no ATP equivalent** — pacing is school-determined within CAPS scope. | `syllabus/grade{N}.json` references the curated CAPS syllabus file as the content universe, records the school-determined pacing model, and carries a `scope_deltas` ledger to be filled **only** from the official SAG (empty = not yet transcribed, never "no differences"). |
| **Exam guidelines** | The SAG replaces the DBE Grade 12 Examination Guidelines *and* the ATP's programme-of-assessment prescriptions. | `exam_guidelines/sag_index.json` indexes the SAG (2026-examination-year edition current as of 2026-08) with fetch targets `grade12_2026.{json,md}` mirroring the CAPS ingestion format. |
| **Skills** | Same CAPS content ⇒ the prerequisite skills transfer as-is. | `skills/{grade}/manifest.json` lists the transferring CAPS skills **by reference** (validated by `ieb_sources.py audit`). Caveat carried in every manifest: CAPS `importance.exam_weight` blocks are DBE-ATP-derived and do **not** transfer — IEB weights await SAG ingestion. |
| **Past papers** | Grade 12 externally-examined papers only; roughly the 5 most recent years free on ieb.co.za; older via NSCexampapers@ieb.co.za; **most marking guidelines are not published publicly**. | `past_papers/index.json` records the portal, coverage policy and grade scope; `sessions[]` is honestly empty until per-paper URLs are captured (see verification status below). |

## Source & terms audit (same diligence standard as `../CAPS/past_papers/SOURCES.md`)

Checked 2026-08-03.

| Source | Status | Findings | Verdict |
|---|---|---|---|
| **IEB** (ieb.co.za) | **PRIMARY — fetch pending** | Terms: IEB material may not be reproduced for commercial gain; must be acknowledged as IEB material; altering content may violate the Copyright Act 98 of 1978; IEB reserves the right to prosecute infringement. Past papers are published as a free study aid (last ~5 years); SAGs are published as guidance for schools writing IEB exams. | OK to fetch the intentionally-published documents for internal, attributed, non-commercial pipeline use. **Do not redistribute**; fetched PDFs stay uncommitted (`.gitignore`). |
| **Studocu / Scribd re-uploads of SAGs** | **NOT USED** | Third-party redistribution of IEB-copyrighted documents, unverifiable fidelity. | Excluded — no data (not even exam-structure numbers) may be transcribed from these; only from the fetched official PDF. |
| **SA Papers / MyExamPapers / ZA Info** (aggregators) | **NOT USED** | Redistributors; the IEB is the primary rights holder and publishes the same papers directly. | Excluded — go to the primary source. |

## Verification status — read this before trusting any URL

`ieb.co.za` fronts its site with bot blocking (403 to non-browser clients), and the sandbox
this tree was authored in additionally had **no network egress to ieb.co.za at all**. So,
honestly recorded in every index file:

- **Portal page URLs** (`nsc-subject-assessment-guidelines`, `nsc-past-papers`, the NSC page)
  were confirmed to exist via web search on 2026-08-03, not by direct fetch —
  `last_verified: null` everywhere until the verify pass runs.
- **Per-document URLs** (SAG PDFs, per-paper downloads) could not be captured mechanically.
  They must be captured in a normal browser session on the portal pages, written into
  `documents[]` / `sessions[]`, then verified and fetched with `scripts/ieb_sources.py`.
- **No content was transcribed** from any IEB document, because none could be fetched. Every
  file that would carry transcribed content says `pending_fetch` / `pending_sag_transcription`
  instead. Nothing in this tree is invented.

## Running the tooling

From the repo root (network only needed for `verify`/`fetch`):

```
python3 lessons/curriculum/IEB/scripts/ieb_sources.py list     # every indexed source, one line each
python3 lessons/curriculum/IEB/scripts/ieb_sources.py audit    # structural + cross-reference validation (CI-able, exit 1 on failure)
python3 lessons/curriculum/IEB/scripts/ieb_sources.py verify   # HEAD/GET each URL; --stamp writes last_verified back
python3 lessons/curriculum/IEB/scripts/ieb_sources.py fetch    # download pending documents to their fetch_path (never committed)
```

`audit` is the contract keeper: it fails if a subject is missing one of the five layers, an
index drops a required key, a `caps_reference`/`caps_path` points at a file that doesn't
exist, or a skills manifest drifts from the CAPS skills tree.

These scripts are IEB-owned on purpose — `lessons/scripts/` stays CAPS/DBE-only
(`past_papers.py` etc. are not IEB-aware and must not be bent into it). When IEB past-paper
ingestion starts, its `paper.json` extraction and question-linking variant belongs in
`scripts/` here, following the CAPS pipeline pattern (`docs/past-papers-linking-brief.md`),
with one structural difference to plan for: IEB marking guidelines are mostly unpublished, so
the memo-method matching step needs a per-paper decision (order the marking guideline via
NSCexampapers@ieb.co.za, or mark the paper index-only).

## Gap status (deliberate, in dependency order)

1. **Capture document URLs** — browser session on the two portal pages; fill `documents[]`
   (six SAG PDFs) and `sessions[]` (per subject, most recent five November sessions), then
   `verify --stamp`.
2. **Fetch + ingest SAGs** — produce `exam_guidelines/grade12_2026.{json,md}` per subject in
   the CAPS ingestion format; then fill each syllabus `scope_deltas` ledger and add
   IEB exam weights to the skills layer (as a manifest field, leaving CAPS skill files untouched).
3. **Past-paper ingestion** — after (1), fetch papers, build `paper.json` extractions and an
   IEB linking pipeline in `scripts/` (see above; blocked on lessons existing for IEB streams).
4. **School calendar** — IEB schools set their own calendars (no single official equivalent of
   `../CAPS/school_calendar/`); decide per-school or ISASA-guideline handling if IEB
   scheduling is ever needed.
5. **Sessions/lessons for IEB streams** — out of scope here by design; this tree provides the
   source layer those lessons will cite.
