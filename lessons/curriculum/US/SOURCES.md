# US Sources — Terms-of-Use Audit

Same diligence standard as `../CAPS/past_papers/SOURCES.md` and
`../IEB/SOURCES.md`: check each source's actual terms before fetching
anything.

Checked **2026-08-04 — via web search only.** This build environment's egress
policy blocks all four rights holders' sites (`corestandards.org`,
`nextgenscience.org`, `collegeboard.org`, `apcentral.collegeboard.org` — the
proxy answered 403 to CONNECT for every one), and the server-side fetch tool
was refused with HTTP 403 by every host tried, *including a neutral control*,
so this is a session-wide limitation rather than a per-site block. The
excerpts below therefore come from search-indexed copies of each rights
holder's own pages.

Re-run `scripts/fetch_us_sources.py probe` from a network-enabled machine to
read robots.txt and each terms page first-hand before the first real fetch,
and update this file and `RIGHTS.json` with what it says. **The gates below
are the conservative reading; a gate may only be loosened on first-hand
evidence, never tightened-then-forgotten.**

## Primary sources

| Source | Status | Terms / findings | Verdict |
|---|---|---|---|
| **Common Core** (corestandards.org, CCSSO) | **RECORDED, not yet fetched** | Not public domain. NGA Center/CCSSO hold copyright and publish their own public licence: a *"limited, non-exclusive, royalty-free license to copy, publish, distribute, and display the Common Core State Standards for purposes that support the Common Core State Standards Initiative"*, whole or in excerpts. Conditions: NGA Center/CCSSO must be acknowledged as sole owners and developers, no contrary claims; any publication or public display must carry *"© Copyright 2010. National Governors Association Center for Best Practices and Council of Chief State School Officers. All rights reserved."*; states that adopted the CCSS in whole are exempt from the attribution provision; **the licence covers the standards only, NOT the embedded examples** — some are public-domain material and others were used under third-party permission. | **OK to ingest and use.** No non-commercial clause, unlike the IEB. The limitation is on *purpose* ("support the Initiative"), which teaching CCSS-aligned lessons satisfies on any ordinary reading. **Attribution is a hard obligation, not a courtesy.** Do not reproduce the embedded examples. |
| **NGSS** (nextgenscience.org; steward WestEd) | **RECORDED, not yet fetched** | *"The K-12 academic standards may be copied, reproduced, altered, adapted, edited, deleted and rearranged by states, districts, schools, teachers and non-profit education entities as they see fit and without permission."* Trademarks (`NGSS`, the name, the logo) transferred from Achieve to WestEd in May 2020; the published volume is copyright National Academies Press. Third parties may not use the logo without WestEd's express written consent, may not put the marks in the main title of a product/service/publication, may not combine them with another mark, and WestEd may request samples and require non-conforming material be altered. Citation: *NGSS Lead States. 2013. Next Generation Science Standards: For States, By States.* | **OK to ingest; one open question for the owner.** The reuse grant is broad in verbs but **narrow in subjects — it enumerates non-profit actors, and a for-profit product is not among them.** That is silence about our case, not a prohibition, so it needs a decision rather than an assumption in either direction. Trademark rules bind immediately: never "NGSS" in a product/feature title, never the logo, "aligned to the NGSS" in body text only. |
| **College Board — AP** (apcentral.collegeboard.org) | **RECORDED, not fetched — GATED** | *"No copyrighted material or College Board content may be performed, distributed, downloaded, uploaded, modified, reused, reproduced, reposted, retransmitted, disseminated, sold, published, broadcast or circulated without express written permission from the College Board."* Services are *"provided solely for non-commercial use"* — not to make money and not as part of any test prep or other business. Released past exams: teachers may download and copy for their own students **in a classroom setting only**; they *"may not be posted on school or personal websites, nor electronically redistributed for any reason."* **AI: College Board *"does not grant permission for its copyrighted content, including practice test questions, to be used in conjunction with generative AI or similar technologies"*, and does not permit training any AI system on its content.** | **GATED — the IEB/Cambridge-equivalent gate, and stricter.** Indexing links and metadata: fine. Ingesting, transcribing or feeding any AP content to a model: **not permitted.** Permission must explicitly cover (a) reproduction, (b) commercial use if the product is paid, and (c) generative-AI use — a generic reproduction permission does not reach (c). Request via the [permission form](https://privacy.collegeboard.org/copyright-trademark/request-form). |
| **College Board — SAT Suite** (satsuite.collegeboard.org) | **RECORDED, not fetched — GATED (same policy, confirmed)** | **Same rights holder, same policy — confirmed, not assumed.** The AP audit was run against College Board's *organisation-level* Terms of Use (`collegeboard.org/terms/terms-of-use`) and its single Copyright and Trademark policy (`privacy.collegeboard.org/copyright-trademark/`); neither is scoped to a programme. The same pass surfaced SAT-specific applications of that one policy: reproduction from *The Official SAT Study Guide* and *Teacher's Guide* is not allowed in any manner; *The Official SAT Practice Test* may be used by a student in a non-commercial educational setting **but not in a test prep course**; the SAT Suite Question Bank and released questions are licensed *"non-exclusive, limited and revocable … for the purpose of classroom teaching and internal reporting only"*, with no uploading, posting online, caching, reproducing, modifying, displaying, editing, altering or enhancing without express written permission. The generative-AI refusal is written against *"College Board's copyrighted content, including practice test questions"* — not AP-scoped either. | **GATED — identical gate to AP, under one policy.** Deliberately not re-audited from scratch: one rights holder, one policy, one gate, and this row records that explicitly rather than leaving SAT looking separately unverified. A single permission request should cover both programmes; do **not** treat an AP permission as covering SAT (or vice versa) unless the granted permission says so. |

## Excluded sources

`audit_tree.py` fails the build if any file in the tree cites one of these.

| Source | Why excluded |
|---|---|
| **thecorestandards.org** | **Not the Common Core site.** An unofficial mirror, created without CCSSO/NGA permission or knowledge; CCSSO has publicly demanded it be taken offline citing copyright infringement. It reproduces the real licence text *accurately* and ranks well in search — which is exactly what makes it dangerous. Cite `corestandards.org` (CCSSO) or CCSSO's own `learning.ccsso.org`. |
| **uworld.com, edisonos.com, research.com, sparkl.me** and similar CED summarisers | Third-party reproductions of College Board content. Same exclusion as Studocu/Scribd in the IEB audit. Transcribing an AP unit list from one of these would launder a prohibited reproduction into the tree — the tempting shortcut, and the one that must not be taken. Useful only to locate official documents. |
| **studocu, scribd, coursehero, clacenter** and similar | Unauthorised re-uploads of exam papers and standards PDFs; unverifiable fidelity. **No data may be transcribed from these — not even exam-structure numbers.** |
| **Test-prep vendor blogs** (galvanizetestprep, testprepkart, oneprep, catalysttestprep, makon.ai, ttprep, testprepscout) | Used **only** to corroborate the digital SAT's published *format* — a fact College Board itself publishes — and recorded with that provenance and an explicit confidence caveat. Never a source of question content, never for provenance hashes. |
| **web.archive.org** | Considered as a mirror for the blocked pages. Prefer first-hand fetches for anything feeding provenance hashes. Fine for manual reading. |

## What was fetched

**Nothing.** No `sources_manifest.json` exists for any framework until the
first `fetch` / `register` run. Every layer carries an explicit
`pending_source_ingest`, `urls_recorded_not_verified` or
`blocked_pending_written_permission` status until then. No standard text,
performance expectation, AP unit or SAT testing point in this tree is
presented as verified — because none is present at all.

One item is recorded as **fact rather than reproduction**: the digital SAT's
published format (98 questions / 134 minutes; Reading and Writing 54 in 64
min, Math 44 in 70 min; two adaptive modules per section). Reporting how long
a test is and how many questions it has is factual reporting about the test,
not reproduction of its content. It is corroborated across multiple secondary
sources but **not** confirmed against College Board's own specification, and
the file says so in its `confidence` field. Resolve before any student-facing
use.

## Standing flags for the owner

1. **AP and SAT are blocked.** This is the answer to "which of the four need
   the same permission gate as IEB/Cambridge": **both College Board
   programmes, and they are stricter than the IEB.** The IEB bars commercial
   reproduction; the College Board additionally bars generative-AI use of its
   content and AI training on it — the specific thing this repository's
   pipeline does. Nothing may be ingested until written permission covering
   reproduction, commercial use and AI use is obtained and recorded in
   `RIGHTS.json`.

2. **NGSS needs a decision, not a gate.** If this product is commercial, we
   are outside the enumerated list of actors the reuse grant names. Either
   confirm the non-profit/educational framing or get written confirmation
   from WestEd. Trademark rules apply now regardless of that decision.

3. **Common Core needs a mechanism, not a decision.** The copyright notice
   must ride along with any CCSS-derived material that reaches a student.
   It is carried in every generated file's `rights.attribution_notice` and
   verified by `audit_tree.py`, but nothing yet propagates it into rendered
   lesson output — wire that up before CCSS content ships.

4. **The verification gap is real.** Every finding above is search-sourced.
   Run `probe` from a network-enabled machine before acting on any of it in a
   way that matters.
