# Manual Fetch Queue — NSC Grade 12 Papers

These URLs are catalogued in the per-subject `../<subject>/past_papers/index.json`
files but are **blocked from automated fetch** by this execution environment's
egress policy (education.gov.za returns CONNECT 403 at the proxy; verified
2026-08-06). Per the standing rule, the exact links are recorded here for a
human to fetch manually rather than discarding the task.

**How to use this queue:** download each PDF in a browser and supply the files
to a work session. Policy change 2026-08-06 (owner decision): supplied PDFs
are now tracked in this repo at `<subject>/grade12/<year>/paperN[_memo].pdf`
alongside the extracted `paperN.json` (the old `*.pdf` ignore rule is retired).

## NEXT BATCH — needs manual fetch

### 1. Mathematical Literacy P1 November 2024 ADDENDUM PDF

The addendum (Annexures A–C) is a separate DBE file, not part of the
question-paper PDF already supplied. Several transcribed P1 answers depend on
its tables/graphs (income-tax table, retailer price graphs, budget pie
charts). Annexure-dependent values in
`mathematical_literacy/grade12/2024/paper1.json` were reconstructed from
memo working and flagged `[ANNEXURE ... - not in repo]`; supplying the
addendum allows verbatim verification.

| Done | File | Where to fetch |
|:---:|---|---|
| [ ] | Mathematical Literacy P1 Addendum (Eng) | DBE session page [webpage — click the link labelled "Mathematical Literacy P1 Nov 2024 Addendum Eng"]: <https://www.education.gov.za/2024NSCNovemberpastpapers.aspx> |
| [x] | Mathematical Literacy P2 Addendum (Eng) — supplied by owner upload 2026-08-06 batch 2 (see Done) | — |

Known mirror (for cross-checking, prefer the DBE original)
[direct PDF — click and save]:
<https://www.theanswer.co.za/wp-content/uploads/2024/11/NSC-2024-Gr-12-Maths-Lit-P1-Addendum.pdf>,
and WCED ePortal (search "Mathematical Literacy addendum Nov 2024").

Heads-up for the download (the mirror naming is misleading, not your fault):
the batch-2 file named `NSC-2024-Gr-12-Maths-Lit-P2-Addendum.pdf` turned out
to be the FULL P2 question paper (13 pp) with the 4-page addendum appended —
17 pages total. That was perfectly usable (we split off pages 14–17), so if
the P1 "addendum" download is also ~18 pages instead of ~5, don't worry:
send it anyway and we'll extract the addendum pages. The true DBE addendum
is a short standalone file whose cover reads "MATHEMATICAL LITERACY P1 /
ADDENDUM / NOVEMBER 2024".

### 2. November 2025 session

The owner upload of 2026-08-06 contained November 2024 papers only — no
November 2025 (or May/June 2025) papers. The DBE has published the November
2025 NSC papers here — **[webpage — see shopping list below]**:

- <https://www.education.gov.za/Curriculum/NationalSeniorCertificate(NSC)Examinations/2025NovemberExamPapers.aspx>

Once fetched, the papers get added to the per-subject `index.json` files and
mirrored as rows here.

#### Shopping list — exactly what to click on that page

The DBE session pages list one link per document, labelled like the 2024
page did: "Mathematics P1 Nov 2024 Eng", "Mathematics P1 Nov 2024 MG
Afr & Eng", etc. On the 2025 page the labels should read the same with
"Nov 2025". Click and save each of these 26 links (tick as you go):

- [ ] Mathematics P1 Nov 2025 Eng
- [ ] Mathematics P1 Nov 2025 MG (memo — may say "MG Afr & Eng"; that
  bilingual file is fine)
- [ ] Mathematics P2 Nov 2025 Eng
- [ ] Mathematics P2 Nov 2025 MG
- [ ] Mathematical Literacy P1 Nov 2025 Eng
- [ ] Mathematical Literacy P1 Nov 2025 MG
- [ ] Mathematical Literacy P2 Nov 2025 Eng
- [ ] Mathematical Literacy P2 Nov 2025 MG
- [ ] Mathematical Literacy P1 Nov 2025 Addendum (Eng) — if listed; it may
  be bundled inside the P1 paper PDF instead, send whatever you get
- [ ] Mathematical Literacy P2 Nov 2025 Addendum (Eng) — same note as P1
- [ ] Physical Sciences P1 Nov 2025 Eng
- [ ] Physical Sciences P1 Nov 2025 MG
- [ ] Physical Sciences P2 Nov 2025 Eng
- [ ] Physical Sciences P2 Nov 2025 MG
- [ ] Accounting P1 Nov 2025 Eng
- [ ] Accounting P1 Nov 2025 MG
- [ ] Accounting P2 Nov 2025 Eng
- [ ] Accounting P2 Nov 2025 MG
- [ ] Economics P1 Nov 2025 Eng
- [ ] Economics P1 Nov 2025 MG
- [ ] Economics P2 Nov 2025 Eng
- [ ] Economics P2 Nov 2025 MG
- [ ] Geography P1 Nov 2025 Eng
- [ ] Geography P1 Nov 2025 MG
- [ ] Geography P2 Nov 2025 Eng
- [ ] Geography P2 Nov 2025 MG

What to SKIP on that page:

- Skip Afrikaans-only question papers (labels ending "Afr" with no "Eng") —
  we only need the English QPs. Bilingual memos ("MG Afr & Eng") are fine.
- Skip every other subject (Life Sciences, Business Studies, languages,
  etc.) — only the six subjects above.

Direct 2025 links already surfaced by web search 2026-08-06 (these download
straight away — no page navigation needed):

| Done | Document | Direct URL |
|:---:|---|---|
| [ ] | Mathematics P1 Nov 2025 MG (bilingual; title verified in search result) [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=lMX4KlIrUCs%3D&tabid=5742&portalid=0&mid=14845> |
| [ ] | Mathematics P2 Nov 2025 — exact label unverified (surfaced in a search for the Nov 2025 Maths P2; same DBE tab as the row above; likely the MG — check the cover page after download) [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=0Hh6qly8lfU%3D&tabid=5742&portalid=0&mid=14845> |
| [ ] | Physical Sciences P1 Nov 2025 Eng QP (stanmorephysics.com mirror — prefer the DBE original from the page above) [direct PDF — click and save] | <https://stanmorephysics.com/wp-content/uploads/2025/11/NSC-Physical-Sciences-Grade-12-November-2025-P1-only.pdf> |

No other direct 2025 fileticket URLs appeared in search results (checked
Mathematical Literacy, Physical Sciences, Accounting, Economics, Geography);
those must come from the session page via the shopping list.

## Done

All November 2024 papers below were supplied by owner upload 2026-08-06 and
transcribed to `paperN.json` on 2026-08-06, except Geography P2 (supplied by
owner upload 2026-08-06 batch 2; transcription pending). All are
English-language, November 2024 NSC, Grade 12, from the session page
<https://www.education.gov.za/2024NSCNovemberpastpapers.aspx>.

### Mathematics

| Done | Paper | Question paper URL | Memo URL |
|:---:|---|---|---|
| [x] | Mathematics P1 | <https://www.education.gov.za/LinkClick.aspx?fileticket=8W2dAxBUTQA%3d> | <https://www.education.gov.za/LinkClick.aspx?fileticket=D_T4clPBpkk%3d> |
| [x] | Mathematics P2 | <https://www.education.gov.za/LinkClick.aspx?fileticket=ycHWvBVvV2M%3d> | <https://www.education.gov.za/LinkClick.aspx?fileticket=0DIM92_2Vu8%3d> |

### Mathematical Literacy

| Done | Paper | Question paper URL | Memo URL |
|:---:|---|---|---|
| [x] | Mathematical Literacy P1 | <https://www.education.gov.za/LinkClick.aspx?fileticket=r3H6xWQUYXg%3d> | <https://www.education.gov.za/LinkClick.aspx?fileticket=AY2Qj8huxtE%3d> |
| [x] | Mathematical Literacy P2 | <https://www.education.gov.za/LinkClick.aspx?fileticket=1EZXhzf3-sI%3d> | <https://www.education.gov.za/LinkClick.aspx?fileticket=xrUiB59LW4E%3d> |
| [x] | Mathematical Literacy P2 Addendum — supplied by owner upload 2026-08-06 batch 2. The supplied file (`NSC-2024-Gr-12-Maths-Lit-P2-Addendum.pdf`, theanswer.co.za mirror) was the full QP (pp 1–13) + addendum (pp 14–17) combined; the 4-page addendum (Annexures A–C: campsite, trail-run map/elevation, Australia trip map) was extracted verbatim to `mathematical_literacy/grade12/2024/paper2_addendum.pdf`. | (mirror, see NEXT BATCH) | — |

### Physical Sciences

| Done | Paper | Question paper URL | Memo URL |
|:---:|---|---|---|
| [x] | Physical Sciences P1 | <https://www.education.gov.za/LinkClick.aspx?fileticket=jKqWYBbucS4%3d> | <https://www.education.gov.za/LinkClick.aspx?fileticket=4GvIWeAkK8U%3d> |
| [x] | Physical Sciences P2 | <https://www.education.gov.za/LinkClick.aspx?fileticket=ZxN41kEGHhI%3d> | <https://www.education.gov.za/LinkClick.aspx?fileticket=8rVrLl89rfM%3d> |

### Accounting

| Done | Paper | Question paper URL | Memo URL |
|:---:|---|---|---|
| [x] | Accounting P1 | <https://www.education.gov.za/LinkClick.aspx?fileticket=LPWTS_eR8NI%3d> | <https://www.education.gov.za/LinkClick.aspx?fileticket=3dYVxFZTk1o%3d> |
| [x] | Accounting P2 | <https://www.education.gov.za/LinkClick.aspx?fileticket=tJdE50Ec9zY%3d> | <https://www.education.gov.za/LinkClick.aspx?fileticket=ccWKxzmiifk%3d> |

### Economics

| Done | Paper | Question paper URL | Memo URL |
|:---:|---|---|---|
| [x] | Economics P1 | <https://www.education.gov.za/LinkClick.aspx?fileticket=gZ8YszYxrcI%3d> | <https://www.education.gov.za/LinkClick.aspx?fileticket=9HXtzh5TON8%3d> |
| [x] | Economics P2 | <https://www.education.gov.za/LinkClick.aspx?fileticket=bFm9Gw3zowg%3d> | <https://www.education.gov.za/LinkClick.aspx?fileticket=3sLdLOgS52I%3d> |

### Geography

| Done | Paper | Question paper URL | Memo URL |
|:---:|---|---|---|
| [x] | Geography P1 | <https://www.education.gov.za/LinkClick.aspx?fileticket=Hc8_CaQJpd4%3d> | <https://www.education.gov.za/LinkClick.aspx?fileticket=ZKd8Wo9VYr0%3d> |
| [x] | Geography P2 — supplied by owner upload 2026-08-06 batch 2; verified across multiple pages (QP 18 pp: Economic Geography + Map Interpretation; marking guidelines 15 pp). Tracked at `geography/grade12/2024/paper2.pdf` + `paper2_memo.pdf`; transcription to `paper2.json` pending. | <https://www.education.gov.za/LinkClick.aspx?fileticket=LrQ39-VlNh4%3d> | <https://www.education.gov.za/LinkClick.aspx?fileticket=2qulvYkBv6k%3d> |

(The first 2026-08-06 upload's Geography P2 files were Accounting P2
duplicates; the batch-2 re-download above fixed this.)

## How to extend this queue

Older sessions on the DBE portal (November + May/June, 2008 to present) are
not indexed yet. To extend this queue, add their sessions/papers to the
per-subject `index.json` files
(`lessons/curriculum/CAPS/<subject>/past_papers/index.json`) and mirror the
new entries here as additional table rows.

## REFERENCE DOCUMENTS — refetch for the archive

Audit 2026-08-06: earlier work sessions fetched the source PDFs below,
extracted them to the JSON/Markdown artefacts in this tree, and then discarded
the PDFs (the pre-2026-08-06 ignore rule), so the repo holds extractions with
no source of record. Every source document is listed here with its recorded
URL so the PDFs can be refetched into the tracked archive. URLs are copied
verbatim from each artefact's own metadata (`source_url` /
`paper_download_url` / `memo_download_url`); none are fabricated. All
documents are © Department of Basic Education.

Link-type audit 2026-08-06: every URL in this section was checked against
the two direct-download patterns (`LinkClick.aspx?fileticket=...` and plain
`.../*.pdf` paths — both download the file immediately, no page to navigate).
All 34 rows are direct downloads, so each row is tagged
"[direct PDF — click and save]": open the link, the PDF downloads, save it.
No webpage-only links in this section.

### CAPS policy statements, FET Grades 10-12

One PDF per subject ("Curriculum and Assessment Policy Statement, FET
Grades 10-12"), extracted to `<subject>/curriculum/caps_gr10-12.json`.

| Done | Subject | Source URL |
|:---:|---|---|
| [ ] | Accounting [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=IIU4LUlZBFM%3d&tabid=570&portalid=0&mid=1558> |
| [ ] | Economics [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=Lv-97xKN0eM%3d&tabid=570&portalid=0&mid=1558> |
| [ ] | Geography [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=sdwEoyM0nY0%3d&tabid=570&portalid=0&mid=1558> |
| [ ] | Mathematical Literacy [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=q8-SkGy43rw%3d&tabid=570&portalid=0&mid=1558> |
| [ ] | Mathematics [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=uXLZcIa67rE%3d&tabid=570&portalid=0&mid=1558> |
| [ ] | Physical Sciences [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=uVcOcx728Y8%3d&tabid=570&portalid=0&mid=1558> |

### Annual Teaching Plans, 2023/24 edition

One PDF per subject per grade, extracted to `<subject>/syllabus/<grade>.json`
(all `source_verified: 2026-07-26`, `atp_edition: 2023/24`).

| Done | Subject / grade | Source URL |
|:---:|---|---|
| [ ] | Accounting Gr 10 [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=xMiwoYjt1vw%3D&tabid=3205&portalid=0&mid=10736> |
| [ ] | Accounting Gr 11 [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=qxPOjU7FXcA%3D&tabid=3205&portalid=0&mid=10752> |
| [ ] | Accounting Gr 12 [direct PDF — click and save] | <https://www.education.gov.za/Portals/0/Documents/Recovery%20plan%20page/2023%20ATPs/FET%20Content%20Subjects/Grade%2012/1.150%20ATP%202023-24%20Gr%2012%20Acc%20final.pdf> |
| [ ] | Economics Gr 10 [direct PDF — click and save] | <https://www.education.gov.za/Portals/0/Documents/Recovery%20plan%20page/2023%20ATPs/FET%20Content%20Subjects/Grade%2010/1.210%20ATP%202023-24%20Gr%2010%20Eco%20final.pdf> |
| [ ] | Economics Gr 11 [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=BjrxUz7iUNo%3D&tabid=3205&portalid=0&mid=10752> |
| [ ] | Economics Gr 12 [direct PDF — click and save] | <https://www.education.gov.za/Portals/0/Documents/Recovery%20plan%20page/2023%20ATPs/FET%20Content%20Subjects/Grade%2012/1.230%20ATP%202023-24%20Gr%2012%20Eco%20final.pdf> |
| [ ] | Geography Gr 10 [direct PDF — click and save] | <https://www.education.gov.za/Portals/0/Documents/Recovery%20plan%20page/2023%20ATPs/FET%20Content%20Subjects/Grade%2010/1.380%20ATP%202023-24%20Gr%2010%20Geo%20final.pdf> |
| [ ] | Geography Gr 11 [direct PDF — click and save] | <https://www.education.gov.za/Portals/0/Documents/Recovery%20plan%20page/2023%20ATPs/FET%20Content%20Subjects/Grade%2011/1.390%20ATP%202023-24%20Gr%2011%20Geo%20final.pdf> |
| [ ] | Geography Gr 12 [direct PDF — click and save] | <https://www.education.gov.za/Portals/0/Documents/Recovery%20plan%20page/2023%20ATPs/FET%20Content%20Subjects/Grade%2012/1.400%20ATP%202023-24%20Gr%2012%20Geo%20final.pdf> |
| [ ] | Mathematical Literacy Gr 10 [direct PDF — click and save] | <https://www.education.gov.za/Portals/0/Documents/Recovery%20plan%20page/2023%20ATPs/FET%20Content%20Subjects/Grade%2010/1.020%20ATP%202023-24%20Gr%2010%20Maths%20Lit%20final.pdf> |
| [ ] | Mathematical Literacy Gr 11 [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=EqZ41-tXhWA%3D&tabid=3205&portalid=0&mid=10752> |
| [ ] | Mathematical Literacy Gr 12 [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=X4ZvlGUQ0vY%3D&tabid=3205&portalid=0&mid=10755> |
| [ ] | Mathematics Gr 10 [direct PDF — click and save] | <https://www.education.gov.za/Portals/0/Documents/Recovery%20plan%20page/2023%20ATPs/FET%20Content%20Subjects/Grade%2010/1.580%20ATP%202023-24%20Gr%2010%20Maths%20final.pdf> |
| [ ] | Mathematics Gr 11 [direct PDF — click and save] | <https://www.education.gov.za/Portals/0/Documents/Recovery%20plan%20page/2023%20ATPs/FET%20Content%20Subjects/Grade%2011/1.590%20ATP%202023-24%20Gr%2011%20Maths%20final.pdf> |
| [ ] | Mathematics Gr 12 [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=_kS5tgxXQ0I%3D&tabid=3205&portalid=0&mid=10755> |
| [ ] | Physical Sciences Gr 10 [direct PDF — click and save] | <https://www.education.gov.za/Portals/0/Documents/Recovery%20plan%20page/2023%20ATPs/FET%20Content%20Subjects/Grade%2010/1.520%20ATP%202023-24%20Gr%2010%20Phys%20Sci%20final.pdf> |
| [ ] | Physical Sciences Gr 11 [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=6y_u-yjj97c%3D&tabid=3205&portalid=0&mid=10755> |
| [ ] | Physical Sciences Gr 12 [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=HofhdeKXMCM%3D&tabid=3205&portalid=0&mid=10752> |

### Grade 12 Examination Guidelines, 2021 edition

One PDF per subject, extracted to
`<subject>/exam_guidelines/grade12_2021.json` + `grade12_2021.md`
(all fetched 2026-07-27).

| Done | Subject | Source URL |
|:---:|---|---|
| [ ] | Accounting [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=Wrz2RY6cOEY%3d&tabid=2720&portalid=0&mid=9677> |
| [ ] | Economics [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=4EZMm9gdCdA%3d&tabid=2720&portalid=0&mid=9690> |
| [ ] | Geography [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=ZL0-Tn1aRmA%3d&tabid=2720&portalid=0&mid=9693> |
| [ ] | Mathematical Literacy [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=eW-HTUSjqck%3d&tabid=2720&portalid=0&mid=9705> |
| [ ] | Mathematics [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=gtM--fFe--Q%3d&tabid=2720&portalid=0&mid=9706> |
| [ ] | Physical Sciences [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=7rRU21y6sgg%3d&tabid=2720&portalid=0&mid=9709> |

### Past papers transcribed before the PDF-tracking policy

These were fetched, extracted to the listed `paper.json`, and discarded under
the old ignore rule; the PDFs are absent from the repo. (The November 2024
papers are NOT listed here — their PDFs are already tracked next to their
`paperN.json` files, no refetch needed.)

| Done | Paper (extracted to) | Question paper URL | Memo URL |
|:---:|---|---|---|
| [ ] | Mathematics Gr 11 P1 Nov 2017 (`past_papers/maths/grade11/2017/paper.json`) [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=b5H9lDVw-o4%3d&tabid=1869&portalid=0&mid=8659> | <https://www.education.gov.za/LinkClick.aspx?fileticket=DDENSGJw7eo%3d&tabid=1869&portalid=0&mid=8659> |
| [ ] | Mathematics Gr 11 P1 Nov 2018 (`past_papers/maths/grade11/2018/paper.json`) [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=1KiiLnULnVY%3d&tabid=1869&portalid=0&mid=8659> | <https://www.education.gov.za/LinkClick.aspx?fileticket=_uRPiTTn5y4%3d&tabid=1869&portalid=0&mid=8659> |
| [ ] | Physical Sciences Gr 11 P1 Nov 2018 (`past_papers/physical_sciences/grade11/2018/paper.json`) [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=_BnHGkPLTbs%3d&tabid=1869&portalid=0&mid=8659> | <https://www.education.gov.za/LinkClick.aspx?fileticket=ip1nUg1Suw0%3d&tabid=1869&portalid=0&mid=8658> |
| [ ] | Geography Gr 12 P2 Nov 2018 (`past_papers/geography/grade12/2018/paper.json`) [direct PDF — click and save] | <https://www.education.gov.za/LinkClick.aspx?fileticket=SyVEO7Woybo%3d&tabid=2268&portalid=0&mid=8393&forcedownload=true> | <https://www.education.gov.za/LinkClick.aspx?fileticket=uMTatGRjfvI%3d&tabid=2268&portalid=0&mid=8393&forcedownload=true> |

### Not a PDF (no refetch)

`school_calendar/2026.json` records its source as the web page
<https://www.gov.za/about-sa/school-calendar> — an HTML source, not a
discarded PDF, so it is excluded from the refetch list.
