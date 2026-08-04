# Cambridge Sources — Terms-of-Use Audit

Same diligence standard as `../CAPS/past_papers/SOURCES.md`, `../IEB/SOURCES.md`
and `../US/SOURCES.md`: read each source's actual terms before fetching
anything. Checked **2026-08-04**.

> **Read this first.** Every finding below was established from
> **search-indexed copies** of Cambridge's own pages — titles, indexed URLs and
> snippet extracts. This build environment's egress policy blocks
> `cambridgeinternational.org`, `cambridge.org` and
> `help.cambridgeinternational.org` (proxy answered 403 to CONNECT), and no
> page fetch of any host succeeded, so **nothing here was read first-hand**.
> The *substance* of each rule below was corroborated across three or four
> independent searches; the *exact wording* was not, so nothing is presented as
> a verbatim quotation. Run `scripts/fetch_cambridge_sources.py probe` from a
> network-enabled machine to read `robots.txt` and the terms pages directly,
> then update this file and flip `verification_method` in `RIGHTS.json`.
>
> **A gate may only ever be loosened on first-hand evidence.** The conservative
> reading stands until then.

## The headline

**Access is open; reproduction is not.** Cambridge publishes question papers,
mark schemes, examiner reports and specimen materials as open PDFs on its own
website — no login — and *separately and explicitly* refuses permission for
electronic publication of that material in any format. The ease of obtaining a
Cambridge paper says nothing about the right to reuse it, and the two facts
must not be collapsed.

This corrects an assumption made early in building this tree — that Cambridge
papers were login-gated behind the School Support Hub. They are not. The Hub is
a *superset* for registered schools, not the only route to papers. The
correction does not soften the conclusion; it sharpens it, because the binding
constraint turns out to be rights rather than access.

## Source-by-source

| Source | Status | Terms / findings | Verdict |
|---|---|---|---|
| **Cambridge International** (cambridgeinternational.org) | **PRIMARY — recorded, not yet fetched** | Syllabuses, question papers, mark schemes, examiner reports, specimen materials and grade-threshold tables are published openly. Syllabus PDFs carry their own copyright block: UCLES retains copyright, and **registered centres may copy material from the booklet for their own internal use**, with third-party-acknowledged material excluded even internally. Past papers carry no such grant. | Fetch the **syllabuses** for internal curriculum mapping — the ordinary use of a published syllabus. **Do not ingest assessment materials** (see the row below). |
| **Cambridge help centre** (help.cambridgeinternational.org) | **PRIMARY — the operative rules** | Three rules, each corroborated across multiple independent searches: (1) teachers **at Cambridge schools** may download and print past papers for use with their own students — a print-and-use permission, not a re-hosting one, and it does not extend to non-Cambridge schools, tutors, individuals or third-party organisations; (2) Cambridge is **unable to give permission to publish past papers on any website or school intranet**, citing loss of control once material is online including incidents of its material being sold — note this reaches a school's *own* intranet, so there is no internal-network carve-out; (3) the permissions process itself states Cambridge **does not grant permission for complete examination papers, nor for electronic publication in any format of past-paper questions, nor for reproduction of mark schemes, examiners' reports or multiple-choice questions**. | **Assessment materials are gated `blocked_pending_written_permission`.** The prohibition is **not** conditioned on commercial use, so no reading of this repository's use clears it. |
| **Cambridge University Press & Assessment** (cambridge.org/legal/copyright) | **PRIMARY — recorded** | General terms: content may be downloaded and printed for personal reference but not otherwise copied, distributed, adapted or transmitted without written permission. Carries an explicit **text-and-data-mining clause**: non-commercial TDM is permitted over content you have **lawful access** to, subject to linking to the source, with local copies deleted at project end — and Cambridge **expressly reserves and opts out of granting commercial TDM rights**. | **The most product-relevant clause in this audit.** See "The AI question" below. |
| **School Support Hub** (schoolsupporthub.cambridge.org) | **NOT USED** | Login-gated superset for registered Cambridge schools; teacher accounts are created by the school's Support Hub coordinator, and access is explicitly **not** open to individuals or third-party organisations. Materials older than about five years are withdrawn, partly because third-party permissions inside papers are cleared for five years only. | Excluded. This project is not a registered centre, and everything it legitimately needs (syllabuses) is on the public site anyway. |
| **Aggregators** (papacambridge, gceguide, dynamicpapers, xtremepapers, savemyexams, physicsandmathstutor, cienotes, exam-mate, rovepapers, Studocu, Scribd, …) | **NOT USED** | Unauthorised redistributors. None claims Cambridge authorisation; at least two affirmatively disclaim any affiliation; and the licence such a site would need is one Cambridge's own permissions policy says it does not issue. Cambridge names misuse of its material online, *including resale*, as its reason for refusing web publication. Aggregators were also observed re-scraping each other — papers served by one carrying another's watermark — so provenance through them is unreliable even setting rights aside. | Excluded, and `audit_tree.py` fails the build if any aggregator URL appears in the tree. Cambridge publishes the same documents itself; there is no scenario where an aggregator is the right source. |
| **British Council syllabus-list PDFs** (britishcouncil.lk) | **USED — corroboration only** | A public body's copies of Cambridge's own subject lists, used as an independent second source when confirming syllabus codes. | Acceptable as *corroboration for a code*. Never a document source to fetch, and never a source of syllabus content. |
| **web.archive.org** | **NOT USED** | Considered for reading blocked pages; also unreachable from here. Even where reachable, first-hand fetches are preferred for anything feeding provenance hashes. | Excluded for provenance. |

## The AI question — read this before building on the tree

The College Board's terms (audited in `../US/SOURCES.md`) expressly refuse
permission for content to be used with generative AI or to train AI systems.
Cambridge has no clause in exactly those words, but it has the closest
equivalent, and it points the same way:

- Commercial text-and-data-mining rights are **expressly reserved and opted
  out of**. Non-commercial TDM is permitted, conditioned on lawful access,
  source linking, and deletion of local copies when the project ends.
- Cambridge University Press & Assessment has separately adopted an **opt-in**
  posture for licensing author content to generative-AI companies, and
  publicly opposed a copyright exception with opt-out.

This repository is a pipeline that feeds curriculum material to a model. So:
**a generic reproduction permission would not cover what this project does.**
If permission is ever sought from Cambridge, it has to name the AI use
explicitly. This is recorded as an `owner_decision_required` gate on
text-and-data-mining in `RIGHTS.json`, not as a blocker on the tree itself —
indexing and internal analysis are unaffected.

## Third-party material inside papers — a second, separate exposure

Published Cambridge past papers are **already partially redacted**. Where
Cambridge could not clear third-party copyright — poems, prose passages — the
material is removed from the published paper, leaving only the first and last
lines plus a reference, with acknowledgements published separately in
per-series Copyright Acknowledgement Booklets. Third-party permissions are
typically cleared for five years, which is part of why older materials are
withdrawn.

The consequence matters for anyone tempted by an aggregator: a "complete" paper
that still contains the unredacted passage is, by construction, carrying
material **Cambridge itself could not license**. Using such a copy creates
infringement exposure against the third-party rights holder that is separate
from, and additional to, Cambridge's own copyright.

## What was fetched

**Nothing.** `sources_manifest.json` does not exist until the first
`fetch-syllabuses` or `register` run. Every syllabus document in
`scripts/subject_registry.json` carries `status: pending_fetch` and a
`url_status` recording that the URL was observed in a search result rather
than fetched. No Cambridge document content, assessment structure or paper
metadata in this tree is presented as verified.

## Open questions — the gaps that need a network-enabled machine

Tracked in `scripts/subject_registry.json` under `_open_questions` and mirrored
into `RIGHTS.json`:

1. **`robots.txt` and AI-crawler directives** for cambridgeinternational.org —
   completely unknown, and the single largest evidentiary gap. Resolve with
   `fetch_cambridge_sources.py probe` **before any bulk fetching**.
2. **Site-terms scope** — `cambridge.org/legal/copyright` scopes itself to
   "Cambridge.org website pages"; Cambridge International maintains its own
   terms page that could not be read. Whether the TDM clause governs
   cambridgeinternational.org is unresolved.
3. **Public past-paper retention window** — the five-year limit is documented
   for the School Support Hub specifically; whether it governs the public pages
   is unstated.
4. **Quote fidelity** — every passage here is snippet-reconstructed. Re-pull
   from the live pages before quoting any of it where it matters.

## Standing flag for the owner

Two decisions are needed, and they are different in kind:

1. **Assessment materials are blocked, not merely gated.** The
   CAPS/DBE past-paper worked-example pipeline
   (`lessons/scripts/past_papers.py`) has **no Cambridge equivalent** and must
   not be pointed at Cambridge material. Only a written permission grant from
   Cambridge can change that — and the same Cambridge document that describes
   the permission process also states the blanket refusal, so assume refusal
   until a grant exists. If one is ever obtained, record it here (scope, date,
   signatory, expiry) **before** narrowing `RIGHTS.json`.
2. **Syllabus content carries a shipping gate.** Ingesting public syllabuses to
   derive curriculum structure is ordinary use and needs no decision.
   Reproducing substantial syllabus prose in a commercial product does — the
   copying permission on the face of a syllabus runs to *registered centres for
   internal use*, which is not this repository.

Relative to its siblings: **stricter than the IEB**, which bars reproduction
for commercial gain but permits personal study use, and in the same bracket as
the College Board's AP/SAT gate in `../US/RIGHTS.json`.
