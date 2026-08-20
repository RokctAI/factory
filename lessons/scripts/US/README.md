# US scripts — spec-driven generation, enforced rights, honest sourcing

Deliberately separate from the CAPS pipeline scripts in
`lessons/scripts/CAPS/` (owner instruction: the CAPS pipeline scripts are
read-only reference for the method; US sourcing lives here). All run from the repository root. Stdlib only, no dependencies.

Ownership map, enforced across the four files:

- `us_spec.py` — the structural spec. What subjects exist, what the grade axis
  is for each framework and *why*, the CCSS domain table, the NGSS dimensions,
  the AP course registry, the SAT suite bands. Both other scripts import it, so
  the tree and its audit can never disagree about what is supposed to exist.
- `build_us_tree.py` owns the generated layers: `curriculum/`, `syllabus/`,
  `skills/`, `AP/courses.json`. Overwrites them freely.
- The assessment-layer indexes (`exam_guidelines/index.json`,
  `past_papers/index.json`) are **hand-owned** — seeded once when absent, then
  never touched. That is where fetch provenance and rights decisions get
  recorded, so a regenerate must not be able to clobber them.
- `audit_tree.py` validates both halves and enforces the rights gates.
- `fetch_us_sources.py` is the only script that touches the network.

## `build_us_tree.py`

Generates every derivable layer from `us_spec.py` + `../../curriculum/US/RIGHTS.json`.
Deterministic — `--check` verifies committed files against a regeneration and
exits 1 on drift. Run it after editing the spec or the rights policy (the
rights block is embedded in every generated file, so a gate change propagates
through a rebuild).

```
python3 lessons/scripts/US/build_us_tree.py
python3 lessons/scripts/US/build_us_tree.py --check
```

## `audit_tree.py`

Offline, CI-able, exit 1 on failure — the contract keeper. Nine checks:

1. `RIGHTS.json` well-formed; every framework declares a known gate, and a
   closed gate actually declares `gated_paths` (a gate that enforces nothing
   is a bug, not a policy).
2. Generated-layer drift.
3. Orphans — a committed file that is neither generator-owned nor a declared
   hand-owned file (catches renames the drift check cannot see).
4. **The rights gate.** For any framework gated
   `blocked_pending_written_permission`, every content array anywhere under
   its `gated_paths` must be empty, and no `sources_manifest.json` may exist.
   This is the check that matters: it turns a rights decision into something
   CI enforces rather than something a future contributor has to remember.
5. **Excluded sources** — fails if any file cites a domain `../../curriculum/US/SOURCES.md`
   excluded (the unofficial Common Core mirror, CED summarisers, question
   re-uploads). `RIGHTS.json`, `SOURCES.md` and `README.md` are exempt,
   because naming an excluded source is what those files are *for*.
6. Attribution — every generated file carries its framework's rights block
   with the notice matching `RIGHTS.json` verbatim.
7. Layout contract — required folders present, and `past_papers/` present
   exactly where it belongs and **absent** where it does not. An empty
   `past_papers/` under a standards framework is a failure, not a no-op: it
   would imply papers exist and are merely un-indexed.
8. Hand-owned index contracts — required keys present.
9. No copyrighted PDFs committed.

```
python3 lessons/scripts/US/audit_tree.py --verbose
```

Verified to actually fire: populating `sessions[]` in an AP past-papers index
makes it exit 1 with a `RIGHTS GATE VIOLATION`.

## `fetch_us_sources.py`

The fetch-and-record step of the CAPS ingestion method, pointed at the four US
rights holders. Polite by construction: honest User-Agent with a contact
route, robots.txt respected, 2 s spacing, exponential backoff. It does not
spoof a browser — if a front end refuses this client, the answer is a manual
browser session and `register`, not evasion.

**The important behaviour is the refusal.** Every subcommand reads
`../../curriculum/US/RIGHTS.json` first, and a framework gated
`blocked_pending_written_permission` is refused outright with an explanation
and the permission-request URL. There is deliberately **no `--force`**:
clearing a gate is an edit to `RIGHTS.json` by the owner, backed by a recorded
permission, not a command-line flag.

```
probe                        robots.txt + terms pages for all four, first-hand
fetch <framework>            download recorded primary sources (refuses if gated)
register <fw> <file> --url   record a browser download with real URL + sha256
verify [fw] [--refetch]      re-hash; --refetch detects upstream edition changes
```

`probe` is the missing piece of the audit: `../../curriculum/US/SOURCES.md` is currently
search-sourced because this environment cannot reach any of the four sites.
Run `probe` from a network-enabled machine, fold the findings in, and set
`RIGHTS.json.verification_method` to `first_hand` with the date.

## Curation after fetching

A human/agent pass, exactly as for the 18 CAPS ATPs: full decoded text as
`.md` beside the curriculum index, structured extraction as `.json`, and a
manual pass against the rendered pages before trusting any mechanical
extraction. Then fill the syllabus `domains[].clusters/standards` (Common
Core) or `performance_expectations[]` (NGSS), and author the skills layer so
each skill anchors to real standard codes.

No numbers or text from third-party re-uploads — only from the fetched
official document. For NGSS, `clarification_statement` and
`assessment_boundary` must be reproduced verbatim: an assessment boundary
changes what may be taught and must never be paraphrased.

## Adding an AP course

Edit `AP_SCAFFOLDED_COURSES` in `us_spec.py`, rerun `build_us_tree.py`. No new
code. There is little value in scaffolding all forty while the rights gate
blocks content ingestion for every one of them.
