# CAMBRIDGE scripts — registry, generator, audit, fetch

Self-contained on purpose: `../CAPS/` is the CAPS/DBE pipeline and stays
that way, exactly as `../IEB/` and `../US/` do.
All run from the repository root.

## The architecture in one line

```
subject_registry.json --build_cambridge_tree.py--> the tree
        ^
        +-- fetch_cambridge_sources.py writes fetch status + sha256 back here
```

The registry is the **single writer-owned source of truth**; the tree is a pure
function of it. Facts are edited in the registry, never in the tree. That is
what lets the drift check be *total*: every JSON file in the tree is generated,
so any hand edit anywhere in it is caught.

## `subject_registry.json`

The verified-facts store — qualifications, syllabus codes, editions, stage
alignment and the content-use policy. **The only file where a Cambridge fact
may be introduced by hand.** Every entry carries `source_urls` and a
`verification` status, and URLs carry a `url_status` recording whether they were
observed or fetched.

Two rules the audit enforces, both there to stop plausible-looking invention:
nothing may claim `corroborated` without at least two independent
`source_urls`, and a URL that was never observed stays `null` rather than being
constructed from a known pattern.

## `build_cambridge_tree.py`

Materialises the tree. Deterministic — same registry gives a byte-identical
tree, so any diff traces to a registry change or a generator change.
`--check` is the drift gate.

## `audit_tree.py`

Offline, CI-able, exit 1 on failure. Five checks:

1. **Structure** — five layers per subject; divergence from the CAPS subject
   set must be *recorded* (a subject with no Cambridge equivalent needs a
   `consumer_rule` saying what to do instead), not silent.
2. **Total drift** — the tree matches regeneration *and* contains no file the
   generator does not own.
3. **Registry provenance** — the corroboration and `url_status` rules above.
4. **Rights** — `RIGHTS.json` is well-formed, every document class declares a
   gate defined in `gate_levels`, every closed gate carries a rationale, and
   the assessment-material gates are **still closed**.
5. **Content guard** — the legal one, and the reason this script exists rather
   than relying on `--check`. It fails the build if past-paper pipeline fields
   (`memo_answer`, `solution_method`, `paper_id`, …) appear anywhere in the
   tree, if any URL points at an unauthorised redistributor or a non-Cambridge
   host, if a source PDF is committed, or if a Cambridge syllabus topic list
   turns out to be a subset of the CAPS topics for the same subject and grade.

All five are negative-tested — each defect class was injected and confirmed to
fail the build before this tree was committed.

## `fetch_cambridge_sources.py`

The fetch-and-record half of the CAPS ingestion method. Honest User-Agent,
`robots.txt` respected, >=2s spacing, retries with backoff. Stdlib only.

```
probe             read robots.txt + the terms pages FIRST and print them
discover          harvest syllabus PDF URLs from a subject landing page
                  (--url, or --html for a browser-saved copy) into the registry
fetch-syllabuses  download recorded syllabus PDFs, hash, update manifest+registry
register          record a file downloaded out of band, keeping URL + sha256
verify            re-hash manifest entries; --refetch detects a new edition
past-papers       REFUSES, and explains why
```

**It fetches syllabuses only.** `past-papers` exists purely to refuse, because
someone will eventually try and a refusal that explains itself beats a missing
feature. `fetch-syllabuses --force` re-downloads an existing *permitted* file —
it is not a rights override, and there is deliberately no flag that is.

Run `probe` before anything else: `robots.txt` for cambridgeinternational.org
is the largest open evidentiary gap in `../../curriculum/CAMBRIDGE/SOURCES.md`.

## Later steps that belong here

Syllabus ingestion (decoded text + structured extraction into
`{subject}/exam_guidelines/`) and any Cambridge question-linking work follow the
CAPS pattern but are implemented **here**, not in the CAPS scripts in
`lessons/scripts/CAPS/`. Note that
for Cambridge the past-paper half of that pattern is blocked outright — see
`../../curriculum/CAMBRIDGE/RIGHTS.json` before writing a line of it.
