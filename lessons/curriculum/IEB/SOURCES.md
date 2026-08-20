# IEB Sources — Terms-of-Use Audit

Same diligence standard as `../CAPS/past_papers/SOURCES.md` (and the Musina
tender scraper before it): check each source's actual terms before fetching.
Checked 2026-08-03 — **via web search only**: this build environment's
egress policy blocks ieb.co.za outright (proxy CONNECT 403), and the site
also answered HTTP 403 to the available fetch tool, so the terms excerpts
below come from search-indexed copies of the site's own pages. Re-run
`scripts/fetch_ieb_sources.py probe` from a network-enabled machine to read
robots.txt and the terms page first-hand before the first real fetch, and
update this file with what it says.

| Source | Status | Terms / findings | Verdict |
|---|---|---|---|
| **IEB** (ieb.co.za) | **RECORDED, not yet fetched** | [terms-of-use](https://www.ieb.co.za/terms-of-use): copyright ©IEB on all site content; use "does not give you ownership of any intellectual property"; **"©IEB material may not be reproduced for commercial gain"**. NSC past papers + marking guidelines for the previous 5 years are published "as a study aid for learners"; SAGs are published for schools on the [SAG page](https://www.ieb.co.za/assessment/high-schools/national-senior-certificate/nsc-subject-assessment-guidelines). robots.txt not yet readable from this environment. | Indexing links/metadata: fine (facts, primary source). Fetching for internal curation: consistent with the published study-aid purpose. **Reproducing IEB questions inside a commercial product: NOT covered — needs IEB permission first. Owner decision required before any IEB paper content ships to students.** This is stricter than the DBE, whose terms carry no commercial clause. |
| **IEB document library** (docs.ieb.co.za) | **RECORDED, not yet fetched** | Guest credentials (guest@ieb.co.za / guest) are published by the IEB itself on its FAQ — intentionally provided public access, analogous to the DBE's public download links. Folders: NSC Public Resources → NSC Examination Papers / NSC Marking Guidelines. SharePoint-style login; not automated by our fetch script — harvest in a browser, then `register` files into the manifest. | OK to access with the published guest credentials; same commercial-reproduction caveat as above. |
| **DBE** (education.gov.za) | **USED (indirectly)** | Already audited in `../CAPS/past_papers/SOURCES.md`. The IEB tree's content layer derives from the CAPS files already fetched from the DBE. | OK — nothing new fetched. |
| **Aggregators** (sapapers.co.za, eduresourcza.com, myexampapers.co.za, saexampapers.co.za, …) | **NOT USED** | Third-party redistributors of IEB documents; the IEB is the primary rights holder and publishes the same material itself. Same reasoning that excluded Testpapers/SA Exam Papers from the CAPS audit. | Excluded — go to the primary source. |
| **Studocu / Scribd re-uploads of SAGs** | **NOT USED** | Third-party redistribution of IEB-copyrighted documents, unverifiable fidelity. | Excluded — **no data (not even exam-structure numbers) may be transcribed from these**; only from the fetched official PDF. Web-search snippets of them served solely to locate the official documents and editions, never as content. |
| **web.archive.org** | **NOT USED** | Considered as a mirror to read blocked IEB pages; also unreachable from this environment. Even where reachable, prefer first-hand fetches for anything that feeds provenance hashes. | Excluded for provenance; fine for manual reading. |

## What was fetched

Nothing yet. `sources_manifest.json` does not exist until the first
`fetch-sags` / `register` run; every per-subject index carries an explicit
`pending_fetch` / `urls_recorded_not_verified` status until then. No IEB
document content, exam structure or paper metadata in this tree is
presented as verified.

## Standing flag for the owner

The IEB's **non-commercial reproduction clause** is the one material
difference from the DBE audit. Before the past-papers pipeline
(`lessons/scripts/CAPS/past_papers.py`) is ever pointed at IEB papers — i.e.
before IEB questions are embedded as worked examples in a product —
obtain written permission from the IEB or confirm the intended use is
non-commercial. Indexing, internal analysis and linking are not affected.
