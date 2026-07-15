# Past-Paper Sources — Terms-of-Use Audit

Same diligence standard as the Musina tender scraper: each source's actual
terms were checked before fetching anything. Checked 2026-07-15.

| Source | Status | Terms / robots findings | Verdict |
|---|---|---|---|
| **DBE** (education.gov.za) | **USED** | Official NSC/Grade 11 papers are published for public download. [terms.aspx](https://www.education.gov.za/terms.aspx): DBE retains copyright ("Copyright: Department of Basic Education"); prohibits obtaining material "through any means not intentionally made available" — the exam-paper download links ARE intentionally provided. No robots rule against `/LinkClick.aspx` document downloads; no scraping prohibition in the terms. | OK to fetch the intentionally-published papers, with attribution + copyright notice. |
| **WCED ePortal** (wcedeportal.co.za) | **NOT USED** | robots.txt explicitly disallows `ClaudeBot` (and GPTBot, CCBot, Google-Extended, etc.), and carries a content signal `ai-train=no`. | Excluded — respect the block. |
| **Testpapers** (testpapers.co.za) | **NOT USED** | Aggregator/redistributor of DBE papers; no visible terms/licence page. Since the DBE is the primary rights holder and publishes the same papers directly, there is no need to scrape a third-party redistributor. | Excluded — go to the primary source instead. |
| **SA Exam Papers** (saexampapers.co.za) | **NOT USED** | Same reasoning as Testpapers — third-party aggregator; primary source available. | Excluded. |

## What was fetched

- `maths/grade11/2018/paper1.pdf` — DBE, Grade 11 Mathematics P1, November 2018,
  English (`fileticket=1KiiLnULnVY`). 16 pp, scanned (image-only, no text layer).
- `maths/grade11/2018/memo1.pdf` — the matching Marking Guidelines
  (`fileticket=_uRPiTTn5y4`). 19 pp, scanned.

Both are © Department of Basic Education, 2018, reproduced for educational
worked-example use with attribution. The scanned PDFs have no text layer;
question and memo text was extracted by reading the rendered pages (recorded
in `maths/grade11/2018/paper.json`), not by OCR, so every field is
human/vision-verified against the official document.
