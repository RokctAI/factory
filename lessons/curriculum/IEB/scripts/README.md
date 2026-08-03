# IEB scripts — sourcing tooling for the IEB tree

IEB-owned on purpose: `lessons/scripts/` is the CAPS/DBE pipeline and stays that way.
Anything IEB-specific (sourcing now; SAG ingestion and past-paper extraction/linking later)
lives here.

## ieb_sources.py

```
python3 lessons/curriculum/IEB/scripts/ieb_sources.py list            # offline
python3 lessons/curriculum/IEB/scripts/ieb_sources.py audit           # offline, exit 1 on failure
python3 lessons/curriculum/IEB/scripts/ieb_sources.py verify [--stamp] [--timeout N]
python3 lessons/curriculum/IEB/scripts/ieb_sources.py fetch  [--allow-any-host] [--timeout N]
```

- **list** prints every URL-bearing entry across the six subjects' index files.
- **audit** is the contract keeper — run it after any hand edit to the tree. It validates the
  five-layer structure, required keys, that every `caps_reference`/`caps_syllabus`/`caps_path`
  resolves to a real file, that syllabus grades match the CAPS tree, that every skills
  manifest is in exact sync with `../CAPS/{subject}/skills/{grade}/` (both directions, names
  included), and that any `scope_deltas` item cites the SAG passage it came from.
- **verify** requests each indexed URL. A 403/429 is reported as BLOCKED, not dead:
  ieb.co.za fronts the site with bot blocking, so a URL this script can't reach may still be
  fine in a browser — confirm there before deleting anything. `--stamp` writes
  `last_verified: <today>` back into entries that answered 2xx/3xx.
- **fetch** downloads `documents[]` entries that carry both `url` and `fetch_path`. It
  refuses non-ieb.co.za hosts unless `--allow-any-host`, skips files already on disk, and
  flips the entry's `status` to `fetched`. Downloaded PDFs are ignored by `../.gitignore` and
  must never be committed (IEB terms: attributed, non-commercial internal use only — no
  redistribution).

The client identifies itself honestly (see `USER_AGENT` in the script) and gives a contact
route; it does not spoof a browser. That is deliberate — if the IEB's front end refuses the
tool, the answer is a manual browser session, not evasion.

## Capturing document URLs (the current gap)

The index files ship with `documents[]`/`sessions[]` unpopulated because per-document URLs
could not be captured mechanically (bot-blocked front end; the authoring sandbox also had no
egress to ieb.co.za). To close the gap, from a normal browser:

1. Open the SAG portal — https://www.ieb.co.za/assessment/high-schools/national-senior-certificate/nsc-subject-assessment-guidelines —
   and for each of the six subjects copy the current-edition SAG download URL into
   `{subject}/exam_guidelines/sag_index.json` `documents[0].url` (add entries per document if
   a subject splits its SAG).
2. Open the past-papers portal — https://www.ieb.co.za/assessment/high-schools/national-senior-certificate/nsc-past-papers —
   and per subject record each available session under `{subject}/past_papers/index.json`
   `sessions[]`, following the CAPS shape:
   `{"session": "November 2025 IEB NSC", "papers": [{"paper": 1, "question_paper_url": ...}]}`.
   Marking guidelines are mostly unpublished; when one isn't downloadable, omit `memo_url`
   rather than pointing at a third-party re-upload.
3. Run `verify --stamp`, then `fetch`, then `audit`, and commit the index changes (not the PDFs).

## Later pipeline steps that belong here

- `sag_ingest` — pdfplumber/pypdf extraction of each fetched SAG into
  `exam_guidelines/grade12_2026.{json,md}` (CAPS exam_guidelines format), followed by a
  manual verification pass against the rendered pages — same discipline as the CAPS ATP
  ingestion documented in `../../CAPS/README.md`.
- IEB past-paper extraction (`paper.json`) and question-to-lesson linking — follow
  `docs/past-papers-linking-brief.md` and `lessons/scripts/past_papers.py` as the pattern,
  but implement here. Plan for the memo gap: most IEB marking guidelines are unpublished, so
  method-level matching needs either a marking guideline ordered via NSCexampapers@ieb.co.za
  or an index-only entry for that paper.
