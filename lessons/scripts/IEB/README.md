# IEB scripts — self-contained sourcing + generation + audit

These scripts are deliberately separate from the CAPS pipeline scripts in
`lessons/scripts/CAPS/` (owner instruction: the CAPS pipeline scripts are
read-only reference for the method; IEB sourcing lives here). All run from the repository root.

Ownership map (enforced across the three scripts):

- `build_from_caps.py` owns the CAPS-derived layers: `curriculum/`,
  `syllabus/grade*.json`, `skills/`.
- The assessment-layer indexes (`exam_guidelines/index.json`,
  `past_papers/index.json`) and `syllabus/scope_deltas.json` are
  **hand-owned** — seeded once, then mutated by `fetch_ieb_sources.py` and
  curation passes. The generator never touches them, so regeneration can
  never clobber recorded provenance.
- `audit_tree.py` validates both halves.

## `build_from_caps.py`

Generates every derivable IEB layer from the CAPS tree — curriculum
pointers, syllabus files (CAPS content scope minus DBE-assessment fields),
skills inheritance pointers. Deterministic; `--check` verifies committed
files against regeneration (run it after editing the CAPS tree). It only
ever writes the files it owns — ingested SAG text/curation lives in
separate files it never touches.

## `audit_tree.py`

Offline, CI-able, exit 1 on failure — the contract keeper. One command runs
the generated-layer drift check (plus orphan detection the drift check
can't see: a committed generated file whose CAPS source was deleted or
renamed), then validates the hand-owned contracts: required keys on both
indexes, `documents[]` entry shapes, `sessions[]` in the CAPS shape with
primary-source (ieb.co.za) URLs only, scope-delta items citing the SAG
passage they came from, exact two-way skills sync with the CAPS tree, and
that every cross-tree pointer resolves. Run it after any hand edit.

## `fetch_ieb_sources.py`

The fetch-and-record step of the CAPS ingestion method, pointed at
ieb.co.za: `probe` (robots + terms first — see `../../curriculum/IEB/SOURCES.md`),
`fetch-sags`, `fetch-papers`, `register` (for browser-downloaded files when
bot protection blocks scripted fetches; keeps real URL + sha256 provenance),
`verify` (re-hash, and `--refetch` to detect upstream edition changes).
Needs a network-enabled machine — the usual build environment blocks
ieb.co.za (details in `../../curriculum/IEB/README.md`). Stdlib only; polite (honest UA,
robots respected, 2s spacing, backoff). The client identifies itself and
gives a contact route; it does not spoof a browser — if the IEB's front end
refuses it, the answer is a manual browser session, not evasion.

`fetch-papers` records raw portal links into each index's
`captured_links[]`; `sessions[]` keeps the CAPS shape and is hand-filled
from those links per the index's `sessions_contract`. Both `fetch-*`
subcommands accept `--html <file>` to parse a browser-saved copy of the
page (records URLs, downloads nothing) when scripted fetching is blocked.

## Capturing document URLs (the current gap)

The index files ship with `documents[].url = null` and `sessions[]` empty
because per-document URLs could not be captured from the authoring
environment (bot-blocked front end + no egress). To close the gap, from a
normal browser:

1. Open the SAG portal (each subject's `exam_guidelines/index.json`
   `source_page`) and either copy each subject's current-edition SAG
   download URL into `documents[].url`, or save the page and run
   `fetch-sags --html <saved.html>`, or download the PDFs and `register`
   them.
2. Open the past-papers portal (each subject's `past_papers/index.json`
   `portal`) and record each available session into `sessions[]` per the
   `sessions_contract`; the docs.ieb.co.za guest library (guest credentials
   published on the IEB FAQ) needs an interactive login — harvest there and
   `register` the files. When a marking guideline isn't downloadable, omit
   `memo_url` rather than pointing at a third-party re-upload.
3. Run `verify`, then `audit_tree.py`, and commit the index changes (never
   the PDFs — `../../curriculum/IEB/.gitignore` blocks them; IEB terms: attributed,
   non-commercial internal use, no redistribution).

## Curation after fetching

A human/agent pass, exactly as for the 18 CAPS ATPs: full-text
`grade12_{year}.md` + structured `grade12_{year}.json` next to each
subject's `exam_guidelines/index.json` (manual verification against the
rendered pages before trusting any mechanical extraction), then fill
`syllabus/scope_deltas.json` and derive IEB exam-weight overlays for the
skills layer. No numbers from third-party re-uploads — only from the
fetched official PDF.

## Later pipeline steps that belong here

IEB past-paper extraction (`paper.json`) and question-to-lesson linking —
follow `docs/past-papers-linking-brief.md` and `lessons/scripts/CAPS/
past_papers.py` as the pattern, but implement here (`lessons/scripts/CAPS/`
stays CAPS/DBE-only). Plan for the memo gap recorded in each past-papers
index: marking-guideline availability is unresolved on secondary evidence,
and memo-method matching needs the marking guideline — order it via
NSCexampapers@ieb.co.za or record that paper index-only. Before any IEB
question ships inside the product, clear the commercial-use flag in
`../../curriculum/IEB/SOURCES.md`.
