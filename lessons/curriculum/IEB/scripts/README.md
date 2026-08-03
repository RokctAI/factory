# IEB scripts — self-contained sourcing + generation

These scripts are deliberately separate from `lessons/scripts/` (owner
instruction: the CAPS pipeline scripts are read-only reference for the
method; IEB sourcing lives here). Both run from the repository root.

## `build_from_caps.py`

Generates every derivable IEB layer from the CAPS tree — curriculum
pointers, syllabus files (CAPS content scope minus DBE-assessment fields),
skills inheritance pointers, and the exam-guidelines / past-papers index
scaffolds. Deterministic; `--check` verifies committed files against
regeneration (run it after editing the CAPS tree, alongside
`atp_drift_check.py`-style checks). It only ever writes the files it owns —
ingested SAG text/curation lives in separate files it never touches.

## `fetch_ieb_sources.py`

The fetch-and-record step of the CAPS ingestion method, pointed at
ieb.co.za: `probe` (robots + terms first — see `../SOURCES.md`),
`fetch-sags`, `fetch-papers`, `register` (for browser-downloaded files when
bot protection blocks scripted fetches; keeps real URL + sha256 provenance),
`verify` (re-hash, and `--refetch` to detect upstream edition changes).
Needs a network-enabled machine — the usual build environment blocks
ieb.co.za (details in `../README.md`). Stdlib only; polite (honest UA,
robots respected, 2s spacing, backoff).

Curation after fetching is a human/agent pass, exactly as for the 18 CAPS
ATPs: full-text `.md` + structured `.json` next to each subject's
`exam_guidelines/index.json`, then replace the syllabus files'
deliberately-stripped assessment fields with SAG-derived ones.
