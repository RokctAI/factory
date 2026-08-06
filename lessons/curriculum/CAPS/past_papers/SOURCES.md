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

- `maths/grade11/2017/paper1.pdf` — DBE, Grade 11 Mathematics P1, November
  2017, English (`fileticket=b5H9lDVw-o4`, Grade11Exams.aspx "Mathematics:
  2017" module). 7 pp, scanned (no text layer) — question wording verified by
  reading the rendered pages.
- `maths/grade11/2017/memo1.pdf` — Memo 1 (Afrikaans and English)
  (`fileticket=DDENSGJw7eo`). 16 pp, real text layer (pdfplumber) —
  equations and answers cross-checked against the rendered paper.

- `geography/grade12/2018/paper2.pdf` — DBE, NSC Grade 12 Geography P2
  (mapwork, Pietermaritzburg 1:50 000 extract), November 2018, English
  (`fileticket=SyVEO7Woybo`, via the 2018NSCNovemberpastpapers.aspx page).
  15 pp, real text layer.
- `geography/grade12/2018/memo2.pdf` — the matching Marking Guidelines
  (`fileticket=uMTatGRjfvI`). 15 pp, real text layer. Both extracted with
  pdfplumber and cross-checked page-by-page; map-read inputs (trig height,
  measured distance) come from the memo's accepted values since the
  topographic map sheet itself is not part of the PDF.

- `maths/grade11/2018/paper1.pdf` — DBE, Grade 11 Mathematics P1, November 2018,
  English (`fileticket=1KiiLnULnVY`). 16 pp, scanned (image-only, no text layer).
- `maths/grade11/2018/memo1.pdf` — the matching Marking Guidelines
  (`fileticket=_uRPiTTn5y4`). 19 pp, scanned.

Both are © Department of Basic Education, 2018, reproduced for educational
worked-example use with attribution. The scanned PDFs have no text layer;
question and memo text was extracted by reading the rendered pages (recorded
in `maths/grade11/2018/paper.json`), not by OCR, so every field is
human/vision-verified against the official document.

Catalogued DBE papers not yet fetched (education.gov.za egress-blocked in the
work environment) are queued for manual browser download in `FETCH_QUEUE.md`.

## Batch 3 (owner upload 2026-08-06) — additional sources used

- **theanswer.co.za mirror** — `NSC-2024-Gr-12-Maths-Lit-P1-Addendum.pdf`
  (full Nov 2024 ML P1 QP + answer sheet + addendum; pp 15–18 extracted to
  `mathematical_literacy/grade12/2024/paper1_addendum.pdf`). Same mirror
  batch 2 used for the P2 addendum; owner-downloaded, not scraped.
- **stanmorephysics.com mirror** — Nov 2025 Physical Sciences P1 Eng QP
  (`physical_sciences/grade12/2025/paper1.pdf`, watermarked). Owner-
  downloaded; to be replaced with the DBE original
  (`fileticket=oWZB83JVXE0`) when fetched.
- **DBE (education.gov.za)** — Nov 2025 Mathematics P1/P2 marking
  guidelines (`maths/grade12/2025/paper1_memo.pdf`, `paper2_memo.pdf`);
  legacy QPs re-fetched for the archive (`maths/grade11/2017/paper1.pdf`,
  `maths/grade11/2018/paper1.pdf`,
  `physical_sciences/grade11/2018/paper1.pdf`,
  `geography/grade12/2018/paper2.pdf`); 2023/24 ATPs, 2021 Grade 12 exam
  guidelines and five CAPS FET policy statements (tracked next to their
  extractions — see FETCH_QUEUE.md REFERENCE section for exact paths).
- **gov.za / Government Gazette** — school-calendar gazettes tracked as
  `../school_calendar/2026.pdf` and `2027.pdf`; 2027 term dates extracted
  to `../school_calendar/2027.json`.

All documents © Department of Basic Education / Government Printing Works,
reproduced for educational use with attribution. Every batch-3 PDF was
identity-verified by reading multiple pages (cover + middle + late), never
trusted by filename.

## Batch 4 (owner upload 2026-08-06)

- **DBE (education.gov.za)** — CAPS FET policy statement, Mathematical
  Literacy Grades 10-12 (134 pp, multi-page verified), tracked at
  `../mathematical_literacy/curriculum/caps_gr10-12.pdf` next to its
  extraction. This closes the last open CAPS-policy row in
  `FETCH_QUEUE.md`.
- The batch's other five files were all duplicates of already-tracked
  material (four legacy QPs byte-identical to the batch-3 copies, plus a
  re-download of the 2024 ML P1 addendum mirror file) — inventoried in
  `FETCH_QUEUE.md`, nothing committed twice, nothing deleted from the
  upload.
- **ecexams.co.za** (Eastern Cape DoE) — identified by web search as an
  official provincial mirror hosting direct memo PDFs for the legacy
  Grade 11 Nov 2018 papers (URL recorded in `FETCH_QUEUE.md`); the site is
  egress-blocked from this environment (CONNECT 403), so nothing was
  fetched from it.
