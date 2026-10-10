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
| [x] | Mathematical Literacy P1 Addendum (Eng) — supplied by owner upload 2026-08-06 batch 3 (see Done) | — |
| [x] | Mathematical Literacy P2 Addendum (Eng) — supplied by owner upload 2026-08-06 batch 2 (see Done) | — |

Known mirror (for cross-checking, prefer the DBE original)
[direct PDF — click and save]:
<https://www.theanswer.co.za/wp-content/uploads/2024/11/NSC-2024-Gr-12-Maths-Lit-P1-Addendum.pdf>,
and WCED ePortal (search "Mathematical Literacy addendum Nov 2024").

Resolution 2026-08-06 batch 3: exactly as predicted, the supplied
`NSC-2024-Gr-12-Maths-Lit-P1-Addendum.pdf` (theanswer.co.za mirror, 18 pp)
was the full P1 question paper (pp 1–13) + answer sheet (p 14) + the true
4-page addendum (pp 15–18; cover "MATHEMATICAL LITERACY P1 / ADDENDUM /
NOVEMBER 2024", Annexure A income-tax tables, Annexure B retailer
stores/employees graphs, Annexure C Indian Union budget pie charts — all
page-verified). Pages 15–18 were extracted verbatim to
`mathematical_literacy/grade12/2024/paper1_addendum.pdf`, enabling verbatim
verification of the `[ANNEXURE ...]`-flagged values in `paper1.json`
(verification DONE 2026-08-06: all reconstructed values matched the printed
annexures — no corrections needed; `[ANNEXURE ... - not in repo]` flags
replaced with verbatim annexure descriptions and Q3.1.1 flipped back to
checkable). Batch 4 (2026-08-06) re-supplied the same 18-pp mirror file
(`NSC-2024-Gr-12-Maths-Lit-P1-Addendum (1).pdf`, browser re-download,
md5 `b03a0c0…`, pp 1/15 re-verified) — duplicate, no action needed.

### 2. November 2025 session

Session page (source of every URL below):
<https://www.education.gov.za/Curriculum/NationalSeniorCertificate(NSC)Examinations/2025NovemberExamPapers.aspx>

Batch 3 (owner upload 2026-08-06) supplied THREE of the 2025 documents
(ticked below) plus a saved copy of the session page itself
(`2025NovemberExamPapers.aspx` HTML). Every remaining document's direct
fileticket URL was harvested from that saved page, so the old
click-the-page shopping list is retired: every row below is now
[direct PDF — click and save] with a full absolute URL — just click the
link. Labels on the page are per-subject
modules ("Paper 1 (English)", "Memo 1 (Afrikaans and English)", etc.).
Note: the 2025 page lists NO separate Mathematical Literacy addenda — if
the annexures turn out to be bundled in the QPs, nothing else to fetch.
RESOLVED batch 5 (2026-08-06): the annexures are NOT in the QPs — both 2025
ML QPs reference their annexures inside a 17-page SPECIAL ANSWER BOOK
(P1 p 13 'ANNEXURE B in the ANSWER BOOK'; P2 p 14 'ANNEXURE D in the ANSWER
BOOK'), so the two ML answer books DO still need fetching — new rows at the
bottom of the table below.

Already supplied (owner upload 2026-08-06 batch 3), tracked in this tree
and indexed in the subject `index.json` files:

| Done | Document | Where it lives |
|:---:|---|---|
| [x] | Mathematics P1 Nov 2025 MG (bilingual Afr & Eng, 21 pp; cover verified "MATHEMATICS P1 ... NOVEMBER 2025 MARKING GUIDELINES") | `maths/grade12/2025/paper1_memo.pdf` (fileticket=lMX4KlIrUCs — page label "Memo 1 (Afrikaans and English)") |
| [x] | Mathematics P2 Nov 2025 MG (bilingual Afr & Eng, 26 pp; cover verified — settles the previously unverified fileticket=0Hh6qly8lfU, which the session page labels "Memo 2 (Afrikaans & English)") | `maths/grade12/2025/paper2_memo.pdf` |
| [x] | Physical Sciences P1 Nov 2025 Eng QP (16 pp + 3 data sheets = 19 pp; cover/mid/data-sheet pages verified; stanmorephysics.com mirror watermark — replace with the DBE original `fileticket=oWZB83JVXE0` when convenient) | `physical_sciences/grade12/2025/paper1.pdf` |

Batch 4 (owner upload 2026-08-06, `FETCH_QUEUE4.zip`) contained NONE of
the November 2025 documents — it carried the Mathematical Literacy CAPS
policy (now ticked in the REFERENCE section below), re-downloads of four
legacy QPs (byte-identical to the already-tracked files; the memos those
rows need did not arrive) and a re-download of the 2024 ML P1 addendum
mirror file already processed in batch 3. Every row below stays open.

Batch 5 (owner upload 2026-08-06, `FETCH_QUEUE5.zip`, 25 PDFs) supplied
ALL 24 open November 2025 rows below — every file verified on cover +
middle + late pages (the four scanned QPs — Maths P1/P2, Maths Lit P1/P2 —
by rendered-page reading), no md5 collisions with tracked files except the
deliberate Physical Sciences P1 QP replacement and the one duplicate noted
in the REFERENCE section (Maths Lit CAPS policy, byte-identical
re-supply). All 24 are now tracked in `<subject>/grade12/2025/` and
indexed in the six subject `index.json` files.

Still to fetch — English QPs and bilingual memos (skip Afrikaans-only QPs
and answerbooks; all URLs harvested 2026-08-06 from the owner-supplied
session-page HTML):

| Done | Document | Direct URL |
|:---:|---|---|
| [x] | Mathematics P1 Eng QP — supplied by owner upload 2026-08-06 batch 5 (scanned, 12 pp = 11 QP pages + information sheet; cover/mid/info-sheet render-verified), tracked at `maths/grade12/2025/paper1.pdf`; transcribed to `paper1.json` 2026-08-06 (49 questions, 150 marks reconciled, links.json extended) | <https://www.education.gov.za/LinkClick.aspx?fileticket=JM4biRg1OIk%3d&tabid=5742&portalid=0&mid=14845> |
| [x] | Mathematics P2 Eng QP — supplied by owner upload 2026-08-06 batch 5 (scanned, 15 pp = 14 QP pages + information sheet; render-verified), tracked at `maths/grade12/2025/paper2.pdf`; transcribed to `paper2.json` 2026-08-06 (54 questions, 150 marks reconciled, links.json extended) | <https://www.education.gov.za/LinkClick.aspx?fileticket=8t-92qfBEV0%3d&tabid=5742&portalid=0&mid=14845> |
| [x] | Mathematical Literacy P1 Eng QP — supplied by owner upload 2026-08-06 batch 5 (scanned, 13 pp, TOTAL 150, render-verified; annexures NOT included — they sit in the un-supplied 17-pp Special Answer Book, see new rows below), tracked at `mathematical_literacy/grade12/2025/paper1.pdf`; transcribed to `paper1.json` 2026-08-06 (51 questions, 150 marks reconciled, links.json extended; annexure-dependent items reconstructed from memo and flagged pending the Special Answer Book) | <https://www.education.gov.za/LinkClick.aspx?fileticket=0fZnlOqdEo0%3d&tabid=5742&portalid=0&mid=14844> |
| [x] | Mathematical Literacy P1 Memo (Afr & Eng) — supplied by owner upload 2026-08-06 batch 5 (bilingual, 23 pp, cover/mid/late verified), tracked at `mathematical_literacy/grade12/2025/paper1_memo.pdf` | <https://www.education.gov.za/LinkClick.aspx?fileticket=yfBLrkeMk2o%3d&tabid=5742&portalid=0&mid=14844> |
| [x] | Mathematical Literacy P2 Eng QP — supplied by owner upload 2026-08-06 batch 5 (scanned, 15 pp, TOTAL 150, render-verified; same answer-book annexure caveat as P1), tracked at `mathematical_literacy/grade12/2025/paper2.pdf`; transcribed to `paper2.json` 2026-08-06 (49 questions, 150 marks reconciled, links.json extended; annexure-dependent items reconstructed from memo and flagged pending the Special Answer Book) | <https://www.education.gov.za/LinkClick.aspx?fileticket=SlY1pYy3GT4%3d&tabid=5742&portalid=0&mid=14844> |
| [x] | Mathematical Literacy P2 Memo (Afr & Eng) — supplied by owner upload 2026-08-06 batch 5 (bilingual, 15 pp, cover/mid/late verified), tracked at `mathematical_literacy/grade12/2025/paper2_memo.pdf` | <https://www.education.gov.za/LinkClick.aspx?fileticket=anKb8eamj_M%3d&tabid=5742&portalid=0&mid=14844> |
| [x] | Physical Sciences P1 Eng QP (DBE original of the mirror above) — supplied by owner upload 2026-08-06 batch 5 (19 pp = 16 pages + 3 data sheets, real text layer, no watermark; p 8 content matches the mirror page-for-page). REPLACED the batch-3 stanmorephysics mirror (old md5 `69a101e…`, new md5 `27a7d9c…`) at `physical_sciences/grade12/2025/paper1.pdf`; transcribed to `paper1.json` 2026-08-06 (55 questions, 150 marks reconciled, links.json extended) | <https://www.education.gov.za/LinkClick.aspx?fileticket=oWZB83JVXE0%3d&tabid=5742&portalid=0&mid=14848> |
| [x] | Physical Sciences P1 Memo (Eng & Afr) — supplied by owner upload 2026-08-06 batch 5 (bilingual, 20 pp, cover/mid/late verified), tracked at `physical_sciences/grade12/2025/paper1_memo.pdf` | <https://www.education.gov.za/LinkClick.aspx?fileticket=OpuzjBocaqw%3d&tabid=5742&portalid=0&mid=14848> |
| [x] | Physical Sciences P2 Eng QP — supplied by owner upload 2026-08-06 batch 5 (20 pp = 16 pages + 4 data sheets, cover/mid/data-sheet verified), tracked at `physical_sciences/grade12/2025/paper2.pdf`; transcribed to `paper2.json` 2026-08-06 (68 questions, 150 marks reconciled, links.json extended; memo Kc inconsistency at Q6.2.3 flagged in-file) | <https://www.education.gov.za/LinkClick.aspx?fileticket=hF7ax9AbzOw%3d&tabid=5742&portalid=0&mid=14848> |
| [x] | Physical Sciences P2 Memo (Eng & Afr) — supplied by owner upload 2026-08-06 batch 5 (bilingual, 22 pp, cover/mid/late verified), tracked at `physical_sciences/grade12/2025/paper2_memo.pdf` | <https://www.education.gov.za/LinkClick.aspx?fileticket=xvxkhSquue4%3d&tabid=5742&portalid=0&mid=14848> |
| [x] | Accounting P1 Eng QP — supplied by owner upload 2026-08-06 batch 5 (16 pp = 15 pages + formula sheet, cover/mid/late verified), tracked at `accounting/grade12/2025/paper1.pdf`; transcribed to `paper1.json` 2026-08-06 (28 questions, 150 marks reconciled, links.json extended) | <https://www.education.gov.za/LinkClick.aspx?fileticket=fjsgFDpa8wg%3d&tabid=5742&portalid=0&mid=14825> |
| [x] | Accounting P1 Memo (Eng) — supplied by owner upload 2026-08-06 batch 5 (13 pp, cover/mid/late verified), tracked at `accounting/grade12/2025/paper1_memo.pdf` | <https://www.education.gov.za/LinkClick.aspx?fileticket=oZyi7eQjyEo%3d&tabid=5742&portalid=0&mid=14825> |
| [x] | Accounting P1 Answer Book (Eng) — supplied by owner upload 2026-08-06 batch 5 (11 pp Special Answer Book, cover/mid/late verified), tracked at `accounting/grade12/2025/paper1_answer_book.pdf` | <https://www.education.gov.za/LinkClick.aspx?fileticket=1WvL2tbx12Y%3d&tabid=5742&portalid=0&mid=14825> |
| [x] | Accounting P2 Eng QP — supplied by owner upload 2026-08-06 batch 5 (16 pp = 15 pages + formula sheet, cover/mid/late verified), tracked at `accounting/grade12/2025/paper2.pdf`; transcribed to `paper2.json` 2026-08-06 (35 questions, 150 marks reconciled, links.json extended; paper-vs-memo bonus-date conflict and stockholding anomaly flagged in-file) | <https://www.education.gov.za/LinkClick.aspx?fileticket=3BYl4uHjIyA%3d&tabid=5742&portalid=0&mid=14825> |
| [x] | Accounting P2 Memo (Eng) — supplied by owner upload 2026-08-06 batch 5 (13 pp, cover/mid/late verified), tracked at `accounting/grade12/2025/paper2_memo.pdf` | <https://www.education.gov.za/LinkClick.aspx?fileticket=xBkE4RhcBtc%3d&tabid=5742&portalid=0&mid=14825> |
| [x] | Accounting P2 Answerbook (Eng) — supplied by owner upload 2026-08-06 batch 5 (11 pp Special Answer Book, cover/mid/late verified), tracked at `accounting/grade12/2025/paper2_answer_book.pdf` | <https://www.education.gov.za/LinkClick.aspx?fileticket=t08Pta3AYdE%3d&tabid=5742&portalid=0&mid=14825> |
| [x] | Economics P1 Eng QP — supplied by owner upload 2026-08-06 batch 5 (12 pp, cover/mid/late verified), tracked at `economics/grade12/2025/paper1.pdf`; transcribed to `paper1.json` 2026-08-06 (66 entries, 230 transcribed marks answered out of 150 reconciled, links.json extended; misprints flagged in-file) | <https://www.education.gov.za/LinkClick.aspx?fileticket=ctIxKzDjX7o%3d&tabid=5742&portalid=0&mid=14836> |
| [x] | Economics P1 Memo (Eng) — supplied by owner upload 2026-08-06 batch 5 (22 pp, cover/mid/late verified), tracked at `economics/grade12/2025/paper1_memo.pdf` | <https://www.education.gov.za/LinkClick.aspx?fileticket=0Nt-PqRAEpI%3d&tabid=5742&portalid=0&mid=14836> |
| [x] | Economics P2 Eng QP — supplied by owner upload 2026-08-06 batch 5 (12 pp, cover/mid/late verified), tracked at `economics/grade12/2025/paper2.pdf`; transcribed to `paper2.json` 2026-08-06 (66 entries, 230 transcribed marks answered out of 150 reconciled, links.json extended; misprints flagged in-file) | <https://www.education.gov.za/LinkClick.aspx?fileticket=Bi6CsZZVPzo%3d&tabid=5742&portalid=0&mid=14836> |
| [x] | Economics P2 Memo (Eng) — supplied by owner upload 2026-08-06 batch 5 (23 pp, cover/mid/late verified), tracked at `economics/grade12/2025/paper2_memo.pdf` | <https://www.education.gov.za/LinkClick.aspx?fileticket=iIiF0mlTUsU%3d&tabid=5742&portalid=0&mid=14836> |
| [x] | Geography P1 Eng QP — supplied by owner upload 2026-08-06 batch 5 (18 pp, cover/mid/late verified), tracked at `geography/grade12/2025/paper1.pdf`; transcribed to `paper1.json` 2026-08-06 (81 questions, 150 marks reconciled, STELLENBOSCH mapwork, links.json extended) | <https://www.education.gov.za/LinkClick.aspx?fileticket=-yt9PT3ew3w%3d&tabid=5742&portalid=0&mid=14839> |
| [x] | Geography P1 Memo (Eng) — supplied by owner upload 2026-08-06 batch 5 (12 pp, cover/mid/late verified), tracked at `geography/grade12/2025/paper1_memo.pdf` | <https://www.education.gov.za/LinkClick.aspx?fileticket=3m3EI20-OFE%3d&tabid=5742&portalid=0&mid=14839> |
| [x] | Geography P2 Eng QP — supplied by owner upload 2026-08-06 batch 5 (20 pp: Economic Geography + Map Interpretation/GIS, cover/mid/late verified), tracked at `geography/grade12/2025/paper2.pdf`; transcribed to `paper2.json` 2026-08-06 (80 questions, 150 marks reconciled, eMALAHLENI (WITBANK) mapwork, links.json extended) | <https://www.education.gov.za/LinkClick.aspx?fileticket=q-0mpNmbw9Q%3d&tabid=5742&portalid=0&mid=14839> |
| [x] | Geography P2 Memo (Eng) — supplied by owner upload 2026-08-06 batch 5 (13 pp, cover/mid/late verified), tracked at `geography/grade12/2025/paper2_memo.pdf` | <https://www.education.gov.za/LinkClick.aspx?fileticket=V40npxGuaQY%3d&tabid=5742&portalid=0&mid=14839> |
| [ ] | Mathematical Literacy P1 Answer Book (Eng) — NEW ROW batch 5: the 2025 ML annexures live in this 17-pp Special Answer Book (QP p 13 references 'ANNEXURE B in the ANSWER BOOK'), needed for annexure-dependent transcription; direct fileticket not yet harvested — fetch from the session page (label "Answer Book 1 (English)" in the Mathematical Literacy module). Direct-PDF search 2026-08-07 (Ray reports the link at right is an htm landing page, not a PDF — correct, it is the session page): NO direct-PDF alternative found — no Nov 2025 ML Answer Book file was sighted verbatim on any sanctioned mirror (theanswer.co.za, stanmorephysics.com, ecexams.co.za; all three egress-blocked here, searched via web-result snippets only; WCED hosts answer books but stays excluded per SOURCES.md). The htm session page remains the path — on it, click "Answer Book 1 (English)" under Mathematical Literacy; the click itself yields the direct LinkClick.aspx PDF download | <https://www.education.gov.za/Curriculum/NationalSeniorCertificate(NSC)Examinations/2025NovemberExamPapers.aspx> |
| [ ] | Mathematical Literacy P2 Answer Book (Eng) — NEW ROW batch 5: same as above for P2 (17-pp Special Answer Book holding Annexures A–D; QP p 14 references 'ANNEXURE D in the ANSWER BOOK'). Direct-PDF search 2026-08-07: same result as the P1 row — NO direct-PDF alternative sighted on sanctioned mirrors; the htm session page remains the path (click "Answer Book 2 (English)" under Mathematical Literacy) | <https://www.education.gov.za/Curriculum/NationalSeniorCertificate(NSC)Examinations/2025NovemberExamPapers.aspx> |

## GRADE 10 AND 11 PAPERS (batch of 2026-10-10)

Scope: official DBE or provincial common papers only, the two most recent
November sessions per grade, each with its official marking guidelines.
education.gov.za and ecexams.co.za (no-www host) were reachable from the work
environment on 2026-10-10, so every paper and memo below was fetched
directly, tracked beside its `paperN.json`, transcribed and linked to the
existing Grade 10/11 lessons (`links.json`). URLs are also recorded in each
subject's `index.json`.

- **Grade 11**: Eastern Cape Department of Education provincial common
  examinations, November 2025 and November 2024.
- **Grade 10**: November 2019 and November 2018 are the most recent real
  Grade 10 exam sessions. The EC archive's "November 2020 Gr. 10
  Examinations" page (<https://ecexams.co.za/2020_November_Gr_10_Exemplars.htm>)
  holds exemplars only, and no later Grade 10 session is published there;
  the DBE Grade 10 page
  (<https://www.education.gov.za/Curriculum/NationalSeniorCertificate(NSC)Examinations/Grade10Exams.aspx>)
  carries Mathematics and Physical Sciences only, latest year 2018. The
  2019 Mathematics and Physical Sciences papers are national DBE papers
  (page headers read DBE/November 2019) distributed through the EC archive.
- **June**: no official Grade 10 or 11 June common papers are published on
  the reachable portals (the EC archive lists November sessions and
  exemplars only), so none are included.

### Grade 11 — November 2025

Session page: <https://ecexams.co.za/2025_November_Gr_11_Exams.htm>

| Done | Paper (tracked at `past_papers/...`) | Question paper URL | Memo URL |
|:---:|---|---|---|
| [x] | Mathematics P1 — `maths/grade11/2025/paper1.json` | <https://ecexams.co.za/2025_November_Gr_11_Exams/Question%20Papers%20Gr%2011/MATHS%20P1%20QP%20GR11%20NOV%202025_watermark.zip> | <https://ecexams.co.za/2025_November_Gr_11_Exams/MATHS%20P1%20MEMO%20GR11%20NOV%202025%20E+A_watermark.pdf> |
| [x] | Mathematics P2 — `maths/grade11/2025/paper2.json` | <https://ecexams.co.za/2025_November_Gr_11_Exams/Question%20Papers%20Gr%2011/MATHS%20P2%20GR%2011%202025_watermark.zip> | <https://ecexams.co.za/2025_November_Gr_11_Exams/MATHS%20P2%20MEMO%20GR%2011%20%20NOVEMBER%202025%20(ENG%20&%20AFR)_watermark.pdf> |
| [x] | Mathematical Literacy P1 — `mathematical_literacy/grade11/2025/paper1.json` | <https://ecexams.co.za/2025_November_Gr_11_Exams/Question%20Papers%20Gr%2011/MATHS%20LITERACY%20P1%20GR11%20QP%20NOV2025_watermark.zip> | <https://ecexams.co.za/2025_November_Gr_11_Exams/MATHS%20LITERACY%20P1%20GR11%20MEMO%20NOV2025_watermark.zip> |
| [x] | Mathematical Literacy P2 — `mathematical_literacy/grade11/2025/paper2.json` | <https://ecexams.co.za/2025_November_Gr_11_Exams/Question%20Papers%20Gr%2011/MATHS%20LIT%20P2%20GRADE%2011%20NOV%202025%20QPAPER_watermark.zip> | <https://ecexams.co.za/2025_November_Gr_11_Exams/MATHS%20LIT%20%20P2%20GRADE%2011%20NOV%202025%20MEMO_watermark.zip> |
| [x] | Physical Sciences P1 — `physical_sciences/grade11/2025/paper1.json` | <https://ecexams.co.za/2025_November_Gr_11_Exams/Question%20Papers%20Gr%2011/PHYSICAL%20SC%20P1%20QP%20GR11%20NOV%202025watermark.zip> | <https://ecexams.co.za/2025_November_Gr_11_Exams/PHYSICAL%20SC%20P1%20MEMO%20NOV%202025%20E+A_watermark.pdf> |
| [x] | Physical Sciences P2 — `physical_sciences/grade11/2025/paper2.json` | <https://ecexams.co.za/2025_November_Gr_11_Exams/Question%20Papers%20Gr%2011/PHYSICAL%20SC%20P2%20QP%20GR11%20NOVEMBER%202025_watermark.zip> | <https://ecexams.co.za/2025_November_Gr_11_Exams/PHYSICAL%20SCIENCES%20P2%20GRADE%2011%20MEMO%20NOVEMBER%202025%20ENG%20&%20AFR_watermark.pdf> |
| [x] | Accounting P1 — `accounting/grade11/2025/paper1.json` | <https://ecexams.co.za/2025_November_Gr_11_Exams/Question%20Papers%20Gr%2011/ACCOUNTING%20P1%20GR11%20QP%20NOV2025watermark.zip> | <https://ecexams.co.za/2025_November_Gr_11_Exams/ACCOUNTING%20P1%20GR11%20MEMO%20NOV2025_watermark.zip> |
| [x] | Accounting P2 — `accounting/grade11/2025/paper2.json` | <https://ecexams.co.za/2025_November_Gr_11_Exams/Question%20Papers%20Gr%2011/ACCOUNTING%20P2%20GR11%20NOV%202025_watermark.zip> | <https://ecexams.co.za/2025_November_Gr_11_Exams/ACCOUNTING%20P2%20%20MEMO%20GR11%20NOV%202025watermark.zip> |
| [x] | Economics P1 — `economics/grade11/2025/paper1.json` | <https://ecexams.co.za/2025_November_Gr_11_Exams/Question%20Papers%20Gr%2011/ECONOMICS%20P1%20GR11%20QP%20NOVEMBER%202025_watermark.zip> | <https://ecexams.co.za/2025_November_Gr_11_Exams/ECONOMICS%20P1%20GR11%20QP%20NOVEMBER%202025%20MARKING%20GUIDELINE_watermark.zip> |
| [x] | Economics P2 — `economics/grade11/2025/paper2.json` | <https://ecexams.co.za/2025_November_Gr_11_Exams/Question%20Papers%20Gr%2011/ECONOMICS%20P2%20GR11%20QP%20NOV2025_watermark.zip> | <https://ecexams.co.za/2025_November_Gr_11_Exams/ECONOMICS%20P2%20GR11%20MEMO%20NOV2025_watermark.zip> |
| [x] | Geography P1 — `geography/grade11/2025/paper1.json` | <https://ecexams.co.za/2025_November_Gr_11_Exams/Question%20Papers%20Gr%2011/GEOGRAPHY%20P1%20QP.zip> | <https://ecexams.co.za/2025_November_Gr_11_Exams/GEOGAPHY%20P1%20MEMO%20GR11%20NOV%202025watermark.zip> |
| [x] | Geography P2 — `geography/grade11/2025/paper2.json` | <https://ecexams.co.za/2025_November_Gr_11_Exams/Question%20Papers%20Gr%2011/GEOGRAPHY%20P2%20GR11%20QP%20NOV2025_watermark.zip> | <https://ecexams.co.za/2025_November_Gr_11_Exams/GEOGRAPHY%20P2%20GR11%20%20NOV2025%20MARKING%20GUIDELINE_watermark.zip> |

### Grade 11 — November 2024

Session page: <https://ecexams.co.za/2024_November_Gr_11_Exams.htm>

| Done | Paper (tracked at `past_papers/...`) | Question paper URL | Memo URL |
|:---:|---|---|---|
| [x] | Mathematics P1 — `maths/grade11/2024/paper1.json` | <https://ecexams.co.za/2024_November_Gr_11_Exams/Question%20Papers/MATHS%20P1%20QP%20GR11%20NOV2024_watermark.zip> | <https://ecexams.co.za/2024_November_Gr_11_Exams/MATHS%20P1%20MEMO%20GR11%20NOV2024_ENG_AFR_watermark.pdf> |
| [x] | Mathematics P2 — `maths/grade11/2024/paper2.json` | <https://ecexams.co.za/2024_November_Gr_11_Exams/Question%20Papers/MATHS%20P2%20QP%20GR11%202024_watermark.zip> | <https://ecexams.co.za/2024_November_Gr_11_Exams/MATHS%20P2%20GRADE%2011%20NOV%202024%20ENG_AFR%20MARKING%20GUIDELINE_watermark.pdf> |
| [x] | Mathematical Literacy P1 — `mathematical_literacy/grade11/2024/paper1.json` | <https://ecexams.co.za/2024_November_Gr_11_Exams/Question%20Papers/MATHS%20LIT%20P1%20GR11%20QP%20NOV%202024_watermark.zip> | <https://ecexams.co.za/2024_November_Gr_11_Exams/MATHS%20LIT%20P1%20MEMO%20GR%2011%20NOV2024_watermark.zip> |
| [x] | Mathematical Literacy P2 — `mathematical_literacy/grade11/2024/paper2.json` | <https://ecexams.co.za/2024_November_Gr_11_Exams/Question%20Papers/MATHS%20LIT%20P2%20GRADE%2011%20NOV%202024_watermark.zip> | <https://ecexams.co.za/2024_November_Gr_11_Exams/MATHS%20LIT%20P2%20GRADE%2011%20NOV%202024%20MARKING%20GUIDELINE_watermark.zip> |
| [x] | Physical Sciences P1 — `physical_sciences/grade11/2024/paper1.json` | <https://ecexams.co.za/2024_November_Gr_11_Exams/Question%20Papers/PHYS%20SCIENCES%20%20P1%20QP%20GR11%20NOV%202024_watermark.zip> | <https://ecexams.co.za/2024_November_Gr_11_Exams/PHYS%20SCIENCES%20P1%20GR11%20MEMO%20NOV%202024%20ENG%20+%20AFR_watermark.pdf> |
| [x] | Physical Sciences P2 — `physical_sciences/grade11/2024/paper2.json` | <https://ecexams.co.za/2024_November_Gr_11_Exams/Question%20Papers/PHYSICAL%20Sc.%20P2%20QP%20GR11%20NOV%202024_watermark.zip> | <https://ecexams.co.za/2024_November_Gr_11_Exams/PHYSICAL%20SCIENCES%20P2%20GR11%20MEMO%202024%20ENG_AFR_watermark.pdf> |
| [x] | Accounting P1 — `accounting/grade11/2024/paper1.json` | <https://ecexams.co.za/2024_November_Gr_11_Exams/Question%20Papers/ACCOUNTING%20%20P1%20GR11%20NOV%202024watermark.zip> | <https://ecexams.co.za/2024_November_Gr_11_Exams/EC%20ACCOUNTING%20P1%20GR11%20%20MG%20NOV%202024_watermark.zip> |
| [x] | Accounting P2 — `accounting/grade11/2024/paper2.json` | <https://ecexams.co.za/2024_November_Gr_11_Exams/Question%20Papers/Accounting%20P2%20QP%20GR11%20NOV%202024watermark.zip> | <https://ecexams.co.za/2024_November_Gr_11_Exams/ACCOUNTING%20P2%20MEMO%20GR11%20NOV%202024_watermark.zip> |
| [x] | Economics P1 — `economics/grade11/2024/paper1.json` | <https://ecexams.co.za/2024_November_Gr_11_Exams/Question%20Papers/ECONOMICS%20P1%20GR11%20QP%20NOV%202024_watermark.zip> | <https://ecexams.co.za/2024_November_Gr_11_Exams/ECONOMICS%20P1%20GR11%20MEMO%20NOV%202024_watermark.zip> |
| [x] | Economics P2 — `economics/grade11/2024/paper2.json` | <https://ecexams.co.za/2024_November_Gr_11_Exams/Question%20Papers/ECONOMICS%20GRADE%2011%20P2%20QP%20NOV%202024_watermark.zip> | <https://ecexams.co.za/2024_November_Gr_11_Exams/ECONOMICS%20GRADE%2011%20P2%20MG%20NOV%202024_watermark.zip> |
| [x] | Geography P1 — `geography/grade11/2024/paper1.json` | <https://ecexams.co.za/2024_November_Gr_11_Exams/Question%20Papers/GEOGRAPHY%20P1%20QP%20GR11%20NOV%202024_watermark.zip> | <https://ecexams.co.za/2024_November_Gr_11_Exams/GEOGRAPHY%20P1%20MEMO%20GR11%20NOV%202024_watermark.zip> |
| [x] | Geography P2 — `geography/grade11/2024/paper2.json` | <https://ecexams.co.za/2024_November_Gr_11_Exams/Question%20Papers/GEOGRAPHY%20P2%20GR11%20QP%20NOV2024_watermark.zip> | <https://ecexams.co.za/2024_November_Gr_11_Exams/GEOGRAPHY%20P2%20GR11%20MEMO%20NOV2024_watermark.zip> |

### Grade 10 — November 2019

Session page: <https://ecexams.co.za/2019_November_Gr_10_Exams.htm>

| Done | Paper (tracked at `past_papers/...`) | Question paper URL | Memo URL |
|:---:|---|---|---|
| [x] | Mathematics P1 — `maths/grade10/2019/paper1.json` | <https://ecexams.co.za/2019_November_Gr_10_Exams/Maths%20Gr%2010%20P1%20QP.zip> | <https://ecexams.co.za/2019_November_Gr_10_Exams/Mathematics%20P1%20Grade%2010%20Nov%202019%20Memo%20Afr%20&%20Eng.pdf> |
| [x] | Mathematics P2 — `maths/grade10/2019/paper2.json` | <https://ecexams.co.za/2019_November_Gr_10_Exams/MATHS%20P2%20GRADE%2010%20NOV%202019.zip> | <https://ecexams.co.za/2019_November_Gr_10_Exams/Mathematics%20P2%20Grade%2010%20Nov%202019%20Memo%20Afr%20&%20Eng.pdf> |
| [x] | Mathematical Literacy P1 — `mathematical_literacy/grade10/2019/paper1.json` | <https://ecexams.co.za/2019_November_Gr_10_Exams/MATHS%20LIT%20P1%20GR10%20QP%20FINAL%20NOV2019.zip> | <https://ecexams.co.za/2019_November_Gr_10_Exams/MATHS%20LIT%20P1%20GR10%20MEMO%20FINAL%20NOV2019.zip> |
| [x] | Mathematical Literacy P2 — `mathematical_literacy/grade10/2019/paper2.json` | <https://ecexams.co.za/2019_November_Gr_10_Exams/Maths%20Lit%20QP%20P2.zip> | <https://ecexams.co.za/2019_November_Gr_10_Exams/MATHS%20LIT%20P2%20GR10%20MEMO%20NOV2019.zip> |
| [x] | Physical Sciences P1 — `physical_sciences/grade10/2019/paper1.json` | <https://ecexams.co.za/2019_November_Gr_10_Exams/Physical%20Sciences%20P1%20Gr%2010%20Nov%202019.zip> | <https://ecexams.co.za/2019_November_Gr_10_Exams/Physical%20Sciences%20P1%20Gr%2010%20Nov%202019%20Memo%20Afr%20&%20Eng.pdf> |
| [x] | Physical Sciences P2 — `physical_sciences/grade10/2019/paper2.json` | <https://ecexams.co.za/2019_November_Gr_10_Exams/Physical%20Sciences%20P2%20Gr%2010%20Nov%202019.zip> | <https://ecexams.co.za/2019_November_Gr_10_Exams/Physical%20Sciences%20P2%20Gr%2010%20Nov%202019%20Memo%20Afr%20&%20Eng.pdf> |
| [x] | Accounting P1 — `accounting/grade10/2019/paper1.json` | <https://ecexams.co.za/2019_November_Gr_10_Exams/ACCOUNTING%20P1%20GR10%20QP%20NOV2019.zip> | <https://ecexams.co.za/2019_November_Gr_10_Exams/ACCOUNTING%20P1%20GR10%20MEMO%20NOV2019.zip> |
| [x] | Accounting P2 — `accounting/grade10/2019/paper2.json` | <https://ecexams.co.za/2019_November_Gr_10_Exams/ACCOUNTING%20P2%20GR10%20QP%20NOV%202019.zip> | <https://ecexams.co.za/2019_November_Gr_10_Exams/ACCOUNTING%20P2%20MEMO%20GR10%20NOV%202019.zip> |
| [x] | Economics P1 — `economics/grade10/2019/paper1.json` | <https://ecexams.co.za/2019_November_Gr_10_Exams/ECONOMICS%20P1%20QP%20GR10%20NOV%202019.zip> | <https://ecexams.co.za/2019_November_Gr_10_Exams/ECONOMICS%20P1%20MEMO%20GR10%20NOV%202019.zip> |
| [x] | Economics P2 — `economics/grade10/2019/paper2.json` | <https://ecexams.co.za/2019_November_Gr_10_Exams/ECONOMICS%20P2%20GR11%20QP%20NOV2019.zip> | <https://ecexams.co.za/2019_November_Gr_10_Exams/ECONOMICS%20P2%20GR10%20MEMO%20NOV2019.zip> |
| [x] | Geography P1 — `geography/grade10/2019/paper1.json` | <https://ecexams.co.za/2019_November_Gr_10_Exams/GEOGRAPHY%20P1%20GR10%20QP%20NOV2019.zip> | <https://ecexams.co.za/2019_November_Gr_10_Exams/GEO%20P1%20GR10%20MEMO%20NOV2019.zip> |
| [x] | Geography P2 — `geography/grade10/2019/paper2.json` | <https://ecexams.co.za/2019_November_Gr_10_Exams/GEOGRAPHY%20P2%20QP%20GR10%20NOV%202019.zip> | <https://ecexams.co.za/2019_November_Gr_10_Exams/GEOGRAPHY%20P2%20GR10%20MEMO%20NOV2019.zip> |

### Grade 10 — November 2018

Session page: <https://ecexams.co.za/2018_November_Gr_10_Exams.htm>, <https://www.education.gov.za/Curriculum/NationalSeniorCertificate(NSC)Examinations/Grade10Exams.aspx>

| Done | Paper (tracked at `past_papers/...`) | Question paper URL | Memo URL |
|:---:|---|---|---|
| [x] | Mathematics P1 — `maths/grade10/2018/paper1.json` | <https://www.education.gov.za/LinkClick.aspx?fileticket=xB_6NSmf6m8%3d&tabid=1853&portalid=0&mid=8657> | <https://www.education.gov.za/LinkClick.aspx?fileticket=odfn3DagL_E%3d&tabid=1853&portalid=0&mid=8657> |
| [x] | Mathematics P2 — `maths/grade10/2018/paper2.json` | <https://www.education.gov.za/LinkClick.aspx?fileticket=RZ22JJ5tljc%3d&tabid=1853&portalid=0&mid=8657> | <https://www.education.gov.za/LinkClick.aspx?fileticket=_QJV3vhD7tw%3d&tabid=1853&portalid=0&mid=8657> |
| [x] | Mathematical Literacy P1 — `mathematical_literacy/grade10/2018/paper1.json` | <https://ecexams.co.za/2018_November_Gr_10_Exams/Maths%20Lit%20P1%20QP.zip> | <https://ecexams.co.za/2018_November_Gr_10_Exams/Maths%20Lit%20P1%20Memo.zip> |
| [x] | Mathematical Literacy P2 — `mathematical_literacy/grade10/2018/paper2.json` | <https://ecexams.co.za/2018_November_Gr_10_Exams/Maths%20Lit%20P2%20QP.zip> | <https://ecexams.co.za/2018_November_Gr_10_Exams/Maths%20Lit%20P2%20Memo.zip> |
| [x] | Physical Sciences P1 — `physical_sciences/grade10/2018/paper1.json` | <https://www.education.gov.za/LinkClick.aspx?fileticket=NbdCRLTzv7E%3d&tabid=1853&portalid=0&mid=8656> | <https://www.education.gov.za/LinkClick.aspx?fileticket=St4cmfQVTdM%3d&tabid=1853&portalid=0&mid=8656> |
| [x] | Physical Sciences P2 — `physical_sciences/grade10/2018/paper2.json` | <https://www.education.gov.za/LinkClick.aspx?fileticket=e-67gT6qA1I%3d&tabid=1853&portalid=0&mid=8656> | <https://www.education.gov.za/LinkClick.aspx?fileticket=Ni2da6SmL6E%3d&tabid=1853&portalid=0&mid=8656> |
| [x] | Accounting P1 — `accounting/grade10/2018/paper1.json` | <https://ecexams.co.za/2018_November_Gr_10_Exams/Accounting%20P1%20QP.zip> | <https://ecexams.co.za/2018_November_Gr_10_Exams/Accounting%20P1%20Memo.zip> |
| [x] | Accounting P2 — `accounting/grade10/2018/paper2.json` | <https://ecexams.co.za/2018_November_Gr_10_Exams/Accounting%20P2%20QP.zip> | <https://ecexams.co.za/2018_November_Gr_10_Exams/Accounting%20P2%20Memo.zip> |
| [x] | Economics P1 — `economics/grade10/2018/paper1.json` | <https://ecexams.co.za/2018_November_Gr_10_Exams/Economics%20P1%20QP.zip> | <https://ecexams.co.za/2018_November_Gr_10_Exams/Economics%20P1%20Memo.zip> |
| [x] | Economics P2 — `economics/grade10/2018/paper2.json` | <https://ecexams.co.za/2018_November_Gr_10_Exams/Economics%20P2%20QP.zip> | <https://ecexams.co.za/2018_November_Gr_10_Exams/Economics%20P2%20Memo.zip> |
| [x] | Geography P1 — `geography/grade10/2018/paper1.json` | <https://ecexams.co.za/2018_November_Gr_10_Exams/Geography%20P1%20QP.zip> | <https://ecexams.co.za/2018_November_Gr_10_Exams/Geography%20P1%20Memo.zip> |
| [x] | Geography P2 — `geography/grade10/2018/paper2.json` | <https://ecexams.co.za/2018_November_Gr_10_Exams/Geography%20P2%20QP.zip> | <https://ecexams.co.za/2018_November_Gr_10_Exams/Geography%20P2%20Memo.zip> |

### Still outstanding (Grade 10/11)

Every paper above has its official memo; nothing in scope is missing a memo.
The items below are supporting material that is blocked or was never published.

| Done | Item | URL |
|:---:|---|---|
| [ ] | Mathematics Gr 11 P2 Nov 2024 answer book (25 pp, referred to on the question paper). It is not in the question-paper zip and the session page has no separate link; `maths/grade11/2024/paper2.json` is complete without it. Fetch it if the EC archive adds it. | <https://ecexams.co.za/2024_November_Gr_11_Exams.htm> (zip: <https://ecexams.co.za/2024_November_Gr_11_Exams/Question%20Papers/MATHS%20P2%20QP%20GR11%202024_watermark.zip>) |
| [ ] | Geography Gr 11 P2 Nov 2024 Mbombela topographic and orthophoto map sheets: not published with the paper (the mapwork questions are transcribed from the paper and memo). | <https://ecexams.co.za/2024_November_Gr_11_Exams.htm> |
| [ ] | Geography Gr 10 P2 Nov 2019 and Nov 2018 topographic and orthophoto map sheets: resource material collected by schools, never published online. | <https://ecexams.co.za/2019_November_Gr_10_Exams.htm>, <https://ecexams.co.za/2018_November_Gr_10_Exams.htm> |
| [ ] | Geography Gr 11 Nov 2025 P1 (Howick) and P2 (2529CC EMALAHLENI, about 50 MB) map sheets: published inside the question-paper zips but deliberately not tracked (size). Fetch from the zip URLs in `geography/past_papers/index.json` if needed. | <https://ecexams.co.za/2025_November_Gr_11_Exams.htm> |
| [ ] | Other provincial portals, not reachable from the work environment on 2026-10-10 (CONNECT 502 or connection reset), so no papers from them are included: Gauteng <https://www.education.gpg.gov.za/>, KwaZulu-Natal <https://www.kzneducation.gov.za/>, Free State <https://www.education.fs.gov.za/>, Limpopo <https://www.limpopo-education.gov.za/>, Mpumalanga <https://www.mpuedu.gov.za/>, Northern Cape <https://www.ncedu.ncpg.gov.za/>, North West <https://nwdesd.nwpg.gov.za/>. The WCED ePortal stays excluded (robots block, see SOURCES.md). | (see item) |

The earlier Grade 10 November 2017 rows were dropped: 2017 is outside the
"two most recent years" scope. If wanted, the official papers are on
<https://ecexams.co.za/2017_November_Gr_10_Exams.htm>.

## Done

All November 2024 papers below were supplied by owner upload 2026-08-06 and
transcribed to `paperN.json` on 2026-08-06 (Geography P2 was supplied by
owner upload 2026-08-06 batch 2 and transcribed the same day). All are
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
| [x] | Mathematical Literacy P1 Addendum — supplied by owner upload 2026-08-06 batch 3. The supplied file (`NSC-2024-Gr-12-Maths-Lit-P1-Addendum.pdf`, theanswer.co.za mirror, 18 pp) was the full QP (pp 1–13) + answer sheet (p 14) + addendum (pp 15–18: Annexures A tax tables, B retailer graphs, C budget pie charts); the 4-page addendum was extracted verbatim to `mathematical_literacy/grade12/2024/paper1_addendum.pdf`. Verbatim re-verification of the `[ANNEXURE ...]`-flagged values in `paper1.json` completed 2026-08-06 — all values matched, no corrections needed. | (mirror, see NEXT BATCH) | — |
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
| [x] | Geography P2 — supplied by owner upload 2026-08-06 batch 2; verified across multiple pages (QP 18 pp: Economic Geography + Map Interpretation; marking guidelines 15 pp). Tracked at `geography/grade12/2024/paper2.pdf` + `paper2_memo.pdf`; transcribed to `paper2.json` 2026-08-06 (81 entries, 150 marks reconciled, links.json extended). | <https://www.education.gov.za/LinkClick.aspx?fileticket=LrQ39-VlNh4%3d> | <https://www.education.gov.za/LinkClick.aspx?fileticket=2qulvYkBv6k%3d> |

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

Batch 3 (owner upload 2026-08-06) supplied 33 of the 34 documents (all
verified by multi-page reading — covers, middle and late pages match the
claimed identities). Committed placement: each reference PDF now sits NEXT
TO its extraction artefact rather than in a separate `reference_docs/`
tree, mirroring the paperN.pdf-beside-paperN.json convention — CAPS
policies at `../<subject>/curriculum/caps_gr10-12.pdf`, ATPs at
`../<subject>/syllabus/<grade>_atp_2023-24.pdf`, exam guidelines at
`../<subject>/exam_guidelines/grade12_2021.pdf`, legacy past-paper QPs in
their existing `<subject>/<grade>/<year>/` dirs below. The one gap: the
Mathematical Literacy CAPS policy PDF was not in the batch. The four
legacy MEMO PDFs were also not in the batch (only the QPs were) — their
rows stay open for the memos.

### CAPS policy statements, FET Grades 10-12

One PDF per subject ("Curriculum and Assessment Policy Statement, FET
Grades 10-12"), extracted to `<subject>/curriculum/caps_gr10-12.json`.

| Done | Subject | Source URL |
|:---:|---|---|
| [x] | Accounting — supplied by owner upload 2026-08-06 batch 3, tracked at `../accounting/curriculum/caps_gr10-12.pdf` (multi-page verified) | <https://www.education.gov.za/LinkClick.aspx?fileticket=IIU4LUlZBFM%3d&tabid=570&portalid=0&mid=1558> |
| [x] | Economics — supplied by owner upload 2026-08-06 batch 3, tracked at `../economics/curriculum/caps_gr10-12.pdf` (multi-page verified) | <https://www.education.gov.za/LinkClick.aspx?fileticket=Lv-97xKN0eM%3d&tabid=570&portalid=0&mid=1558> |
| [x] | Geography — supplied by owner upload 2026-08-06 batch 3, tracked at `../geography/curriculum/caps_gr10-12.pdf` (multi-page verified) | <https://www.education.gov.za/LinkClick.aspx?fileticket=sdwEoyM0nY0%3d&tabid=570&portalid=0&mid=1558> |
| [x] | Mathematical Literacy — supplied by owner upload 2026-08-06 batch 4, tracked at `../mathematical_literacy/curriculum/caps_gr10-12.pdf` (134 pp; cover "MATHEMATICAL LITERACY ... Curriculum and Assessment Policy Statement, Further Education and Training Phase Grades 10-12", pp 3/60/130 verified — DBE contact page, banking/loans content, models taxonomy). Batch 5 (2026-08-06) re-supplied the same file (`CAPS FET _ MATHEMATICAL LITERACY _ GR 10-12 _ Web_DDA9.pdf`, byte-identical md5 `a492e3f…` to the tracked copy) — duplicate, no action needed | <https://www.education.gov.za/LinkClick.aspx?fileticket=q8-SkGy43rw%3d&tabid=570&portalid=0&mid=1558> |
| [x] | Mathematics — supplied by owner upload 2026-08-06 batch 3, tracked at `../maths/curriculum/caps_gr10-12.pdf` (multi-page verified) | <https://www.education.gov.za/LinkClick.aspx?fileticket=uXLZcIa67rE%3d&tabid=570&portalid=0&mid=1558> |
| [x] | Physical Sciences — supplied by owner upload 2026-08-06 batch 3, tracked at `../physical_sciences/curriculum/caps_gr10-12.pdf` (multi-page verified) | <https://www.education.gov.za/LinkClick.aspx?fileticket=uVcOcx728Y8%3d&tabid=570&portalid=0&mid=1558> |

### Annual Teaching Plans, 2023/24 edition

One PDF per subject per grade, extracted to `<subject>/syllabus/<grade>.json`
(all `source_verified: 2026-07-26`, `atp_edition: 2023/24`).

| Done | Subject / grade | Source URL |
|:---:|---|---|
| [x] | Accounting Gr 10 — supplied by owner upload 2026-08-06 batch 3, tracked at `../accounting/syllabus/grade10_atp_2023-24.pdf` (multi-page verified) | <https://www.education.gov.za/LinkClick.aspx?fileticket=xMiwoYjt1vw%3D&tabid=3205&portalid=0&mid=10736> |
| [x] | Accounting Gr 11 — supplied by owner upload 2026-08-06 batch 3, tracked at `../accounting/syllabus/grade11_atp_2023-24.pdf` (multi-page verified) | <https://www.education.gov.za/LinkClick.aspx?fileticket=qxPOjU7FXcA%3D&tabid=3205&portalid=0&mid=10752> |
| [x] | Accounting Gr 12 — supplied by owner upload 2026-08-06 batch 3, tracked at `../accounting/syllabus/grade12_atp_2023-24.pdf` (multi-page verified) | <https://www.education.gov.za/Portals/0/Documents/Recovery%20plan%20page/2023%20ATPs/FET%20Content%20Subjects/Grade%2012/1.150%20ATP%202023-24%20Gr%2012%20Acc%20final.pdf> |
| [x] | Economics Gr 10 — supplied by owner upload 2026-08-06 batch 3, tracked at `../economics/syllabus/grade10_atp_2023-24.pdf` (multi-page verified) | <https://www.education.gov.za/Portals/0/Documents/Recovery%20plan%20page/2023%20ATPs/FET%20Content%20Subjects/Grade%2010/1.210%20ATP%202023-24%20Gr%2010%20Eco%20final.pdf> |
| [x] | Economics Gr 11 — supplied by owner upload 2026-08-06 batch 3, tracked at `../economics/syllabus/grade11_atp_2023-24.pdf` (multi-page verified) | <https://www.education.gov.za/LinkClick.aspx?fileticket=BjrxUz7iUNo%3D&tabid=3205&portalid=0&mid=10752> |
| [x] | Economics Gr 12 — supplied by owner upload 2026-08-06 batch 3, tracked at `../economics/syllabus/grade12_atp_2023-24.pdf` (multi-page verified) | <https://www.education.gov.za/Portals/0/Documents/Recovery%20plan%20page/2023%20ATPs/FET%20Content%20Subjects/Grade%2012/1.230%20ATP%202023-24%20Gr%2012%20Eco%20final.pdf> |
| [x] | Geography Gr 10 — supplied by owner upload 2026-08-06 batch 3, tracked at `../geography/syllabus/grade10_atp_2023-24.pdf` (multi-page verified) | <https://www.education.gov.za/Portals/0/Documents/Recovery%20plan%20page/2023%20ATPs/FET%20Content%20Subjects/Grade%2010/1.380%20ATP%202023-24%20Gr%2010%20Geo%20final.pdf> |
| [x] | Geography Gr 11 — supplied by owner upload 2026-08-06 batch 3, tracked at `../geography/syllabus/grade11_atp_2023-24.pdf` (multi-page verified) | <https://www.education.gov.za/Portals/0/Documents/Recovery%20plan%20page/2023%20ATPs/FET%20Content%20Subjects/Grade%2011/1.390%20ATP%202023-24%20Gr%2011%20Geo%20final.pdf> |
| [x] | Geography Gr 12 — supplied by owner upload 2026-08-06 batch 3, tracked at `../geography/syllabus/grade12_atp_2023-24.pdf` (multi-page verified) | <https://www.education.gov.za/Portals/0/Documents/Recovery%20plan%20page/2023%20ATPs/FET%20Content%20Subjects/Grade%2012/1.400%20ATP%202023-24%20Gr%2012%20Geo%20final.pdf> |
| [x] | Mathematical Literacy Gr 10 — supplied by owner upload 2026-08-06 batch 3, tracked at `../mathematical_literacy/syllabus/grade10_atp_2023-24.pdf` (multi-page verified) | <https://www.education.gov.za/Portals/0/Documents/Recovery%20plan%20page/2023%20ATPs/FET%20Content%20Subjects/Grade%2010/1.020%20ATP%202023-24%20Gr%2010%20Maths%20Lit%20final.pdf> |
| [x] | Mathematical Literacy Gr 11 — supplied by owner upload 2026-08-06 batch 3, tracked at `../mathematical_literacy/syllabus/grade11_atp_2023-24.pdf` (multi-page verified) | <https://www.education.gov.za/LinkClick.aspx?fileticket=EqZ41-tXhWA%3D&tabid=3205&portalid=0&mid=10752> |
| [x] | Mathematical Literacy Gr 12 — supplied by owner upload 2026-08-06 batch 3, tracked at `../mathematical_literacy/syllabus/grade12_atp_2023-24.pdf` (multi-page verified) | <https://www.education.gov.za/LinkClick.aspx?fileticket=X4ZvlGUQ0vY%3D&tabid=3205&portalid=0&mid=10755> |
| [x] | Mathematics Gr 10 — supplied by owner upload 2026-08-06 batch 3, tracked at `../maths/syllabus/grade10_atp_2023-24.pdf` (multi-page verified) | <https://www.education.gov.za/Portals/0/Documents/Recovery%20plan%20page/2023%20ATPs/FET%20Content%20Subjects/Grade%2010/1.580%20ATP%202023-24%20Gr%2010%20Maths%20final.pdf> |
| [x] | Mathematics Gr 11 — supplied by owner upload 2026-08-06 batch 3, tracked at `../maths/syllabus/grade11_atp_2023-24.pdf` (multi-page verified) | <https://www.education.gov.za/Portals/0/Documents/Recovery%20plan%20page/2023%20ATPs/FET%20Content%20Subjects/Grade%2011/1.590%20ATP%202023-24%20Gr%2011%20Maths%20final.pdf> |
| [x] | Mathematics Gr 12 — supplied by owner upload 2026-08-06 batch 3, tracked at `../maths/syllabus/grade12_atp_2023-24.pdf` (multi-page verified) | <https://www.education.gov.za/LinkClick.aspx?fileticket=_kS5tgxXQ0I%3D&tabid=3205&portalid=0&mid=10755> |
| [x] | Physical Sciences Gr 10 — supplied by owner upload 2026-08-06 batch 3, tracked at `../physical_sciences/syllabus/grade10_atp_2023-24.pdf` (multi-page verified) | <https://www.education.gov.za/Portals/0/Documents/Recovery%20plan%20page/2023%20ATPs/FET%20Content%20Subjects/Grade%2010/1.520%20ATP%202023-24%20Gr%2010%20Phys%20Sci%20final.pdf> |
| [x] | Physical Sciences Gr 11 — supplied by owner upload 2026-08-06 batch 3, tracked at `../physical_sciences/syllabus/grade11_atp_2023-24.pdf` (multi-page verified) | <https://www.education.gov.za/LinkClick.aspx?fileticket=6y_u-yjj97c%3D&tabid=3205&portalid=0&mid=10755> |
| [x] | Physical Sciences Gr 12 — supplied by owner upload 2026-08-06 batch 3, tracked at `../physical_sciences/syllabus/grade12_atp_2023-24.pdf` (multi-page verified) | <https://www.education.gov.za/LinkClick.aspx?fileticket=HofhdeKXMCM%3D&tabid=3205&portalid=0&mid=10752> |

### Grade 12 Examination Guidelines, 2021 edition

One PDF per subject, extracted to
`<subject>/exam_guidelines/grade12_2021.json` + `grade12_2021.md`
(all fetched 2026-07-27).

| Done | Subject | Source URL |
|:---:|---|---|
| [x] | Accounting — supplied by owner upload 2026-08-06 batch 3, tracked at `../accounting/exam_guidelines/grade12_2021.pdf` (multi-page verified) | <https://www.education.gov.za/LinkClick.aspx?fileticket=Wrz2RY6cOEY%3d&tabid=2720&portalid=0&mid=9677> |
| [x] | Economics — supplied by owner upload 2026-08-06 batch 3, tracked at `../economics/exam_guidelines/grade12_2021.pdf` (multi-page verified) | <https://www.education.gov.za/LinkClick.aspx?fileticket=4EZMm9gdCdA%3d&tabid=2720&portalid=0&mid=9690> |
| [x] | Geography — supplied by owner upload 2026-08-06 batch 3, tracked at `../geography/exam_guidelines/grade12_2021.pdf` (multi-page verified) | <https://www.education.gov.za/LinkClick.aspx?fileticket=ZL0-Tn1aRmA%3d&tabid=2720&portalid=0&mid=9693> |
| [x] | Mathematical Literacy — supplied by owner upload 2026-08-06 batch 3, tracked at `../mathematical_literacy/exam_guidelines/grade12_2021.pdf` (multi-page verified) | <https://www.education.gov.za/LinkClick.aspx?fileticket=eW-HTUSjqck%3d&tabid=2720&portalid=0&mid=9705> |
| [x] | Mathematics — supplied by owner upload 2026-08-06 batch 3, tracked at `../maths/exam_guidelines/grade12_2021.pdf` (multi-page verified) | <https://www.education.gov.za/LinkClick.aspx?fileticket=gtM--fFe--Q%3d&tabid=2720&portalid=0&mid=9706> |
| [x] | Physical Sciences — supplied by owner upload 2026-08-06 batch 3, tracked at `../physical_sciences/exam_guidelines/grade12_2021.pdf` (multi-page verified) | <https://www.education.gov.za/LinkClick.aspx?fileticket=7rRU21y6sgg%3d&tabid=2720&portalid=0&mid=9709> |

### Past papers transcribed before the PDF-tracking policy

These were fetched, extracted to the listed `paper.json`, and discarded under
the old ignore rule; the PDFs are absent from the repo. (The November 2024
papers are NOT listed here — their PDFs are already tracked next to their
`paperN.json` files, no refetch needed.)

| Done | Paper (extracted to) | Question paper URL | Memo URL |
|:---:|---|---|---|
| [x] | Mathematics Gr 11 P1 Nov 2017 — DONE 2026-10-10: the official DBE marking guidelines were fetched from the memo URL at right (education.gov.za now reachable) and are tracked at `maths/grade11/2017/paper1_memo.pdf`; `paper.json` `memo_file` updated. History: QP supplied by owner upload 2026-08-06 batch 3, tracked at `maths/grade11/2017/paper1.pdf` (7 pp scan, cover/mid/late pages verified; matches the paper.json). MEMO still missing: batch 4 (2026-08-06) re-supplied the QP again (`Mathematics P1 Grade 11 Nov 2017 Eng.pdf`, byte-identical md5 `80f35be…` to the tracked QP) — the memo URL at right, labelled "Memo 1 (Afrikaans and English)" on Grade11Exams.aspx, is what still needs downloading [direct PDF — click and save]. Mirror search 2026-08-06: no direct link found on acceptable hosts (WCED ePortal excluded per SOURCES.md robots block; Scribd/Studypool are viewer pages, not PDFs). Direct-link search 2026-08-07: two ecexams.co.za leads (host still egress-blocked here — CONNECT 403 re-verified 2026-08-07, so neither could be fetched): (a) the 2017 Gr 11 directory exists — index page <https://www.ecexams.co.za/2017_November_Gr_11_Exams.htm>, sibling file sighted VERBATIM in search results: <https://www.ecexams.co.za/2017_November_Gr_11_Exams/Maths%20P2%20Memo.pdf> — the P1 analogue <https://www.ecexams.co.za/2017_November_Gr_11_Exams/Maths%20P1%20Memo.pdf> was pattern-guessed from that sibling and is now DEAD: 404/not-found confirmed by Ray's manual fetch 2026-08-08 — do not retry it. URL needed — manual fetch via the ecexams index page <https://www.ecexams.co.za/2017_November_Gr_11_Exams.htm> (this index page WAS sighted verbatim): open it and click the Maths P1 memo link if one is listed. SIBLING-PATTERN CAUTION (2026-08-08): the sighted P2 URL above shares the same short-name `Maths PN Memo.pdf` pattern as the dead P1 guess — treat it as suspect until actually opened; the ecexams URLs that ARE corroborated elsewhere in this file (2018 Gr 11 and 2019 Gr 11 directories, rows below) all use the long DBE filenames (e.g. `Mathematics P2 Grade 11 Nov 2018 Memo Eng & Afr.pdf`), so the 2017 short names may simply not be what the index links. No replacement URL is recorded because no 2017 Gr 11 filename pattern is confirmed working anywhere in this repo — derive the real one from the .htm index. No other row in this file uses the `2017_November_Gr_11_Exams/` pattern. (b) sighted VERBATIM but UNVERIFIED (host blocked): stanmorephysics combined QP+memo <https://stanmorephysics.com/wp-content/uploads/2020/07/Mathematics-P1-Nov-2017-and-memo.pdf> — CAUTION: grade not confirmable from snippets (may be the Gr 12 NSC Nov 2017 paper, not Gr 11) — check the cover on open before trusting it | <https://www.education.gov.za/LinkClick.aspx?fileticket=b5H9lDVw-o4%3d&tabid=1869&portalid=0&mid=8659> | <https://www.education.gov.za/LinkClick.aspx?fileticket=DDENSGJw7eo%3d&tabid=1869&portalid=0&mid=8659> |
| [x] | Mathematics Gr 11 P1 Nov 2018 — DONE 2026-10-10: the official DBE marking guidelines were fetched from the memo URL at right (education.gov.za now reachable) and are tracked at `maths/grade11/2018/paper1_memo.pdf`; `paper.json` `memo_file` updated. History: QP supplied by owner upload 2026-08-06 batch 3, tracked at `maths/grade11/2018/paper1.pdf` (16 pp scan: Eng pp 1-8 + Afr pp 9-16, verified). MEMO still missing: batch 4 (2026-08-06) re-supplied the QP again (`Mathematics P1 Grade 11 Nov 2018 Eng.pdf`, byte-identical md5 `5d85abb…` to the tracked QP). ALTERNATIVE direct memo PDF found by web search 2026-08-06 on the Eastern Cape DoE exam site (URL observed verbatim in search results; ecexams.co.za is egress-blocked here so unfetched-but-real) [direct PDF — click and save]: <https://www.ecexams.co.za/2018_November_Gr_11_Exams/Mathematics%20P1%20Grade%2011%20Nov%202018%20Memo%20Eng%20&%20Afr.pdf> — or use the DBE memo URL at right. Link-type check 2026-08-07 (Ray reports the remaining links resolve to htm): the ecexams URL above IS a direct `.pdf` static-file path — the site's `.htm` pages are only its directory indexes; the host is still egress-blocked here (CONNECT 403 re-verified 2026-08-07) so it could not be fetched, but the sibling P2 memo in the same directory was sighted VERBATIM in search results 2026-08-07 (<https://www.ecexams.co.za/2018_November_Gr_11_Exams/Mathematics%20P2%20Grade%2011%20Nov%202018%20Memo%20Eng%20&%20Afr.pdf>), corroborating directory and filename pattern. If the P1 link misbehaves in a browser (the raw `&` in the filename can trip some link handlers), open the index <https://www.ecexams.co.za/2018_November_Gr_11_Exams.htm> and click "Mathematics P1 Grade 11 Nov 2018 Memo Eng & Afr" | <https://www.education.gov.za/LinkClick.aspx?fileticket=1KiiLnULnVY%3d&tabid=1869&portalid=0&mid=8659> | <https://www.education.gov.za/LinkClick.aspx?fileticket=_uRPiTTn5y4%3d&tabid=1869&portalid=0&mid=8659> |
| [x] | Physical Sciences Gr 11 P1 Nov 2018 — DONE 2026-10-10: the official DBE marking guidelines were fetched from the memo URL at right (education.gov.za now reachable) and are tracked at `physical_sciences/grade11/2018/paper1_memo.pdf`; `paper.json` `memo_file` updated. History: QP supplied by owner upload 2026-08-06 batch 3, tracked at `physical_sciences/grade11/2018/paper1.pdf` (15 pp + 2 data sheets, verified). MEMO still missing: batch 4 (2026-08-06) re-supplied the QP again (`Physical Sciences P1 Grade 11 Nov 2018 Eng.pdf`, byte-identical md5 `84a2fb6…` to the tracked QP). Mirror search 2026-08-06: no direct link found — the same ecexams.co.za directory that holds the Maths Gr 11 Nov 2018 memo (`https://www.ecexams.co.za/2018_November_Gr_11_Exams/`) very likely holds it too, link label best guess "Physical Sciences P1 Grade 11 Nov 2018 Memo Eng & Afr.pdf" (NOT verified — site egress-blocked here); otherwise use the DBE memo URL at right [direct PDF — click and save]. Direct-link search 2026-08-07: still no verbatim sighting of the 2018 P1 file itself, but the filename pattern is now corroborated by a VERBATIM-sighted 2019 sibling (<https://ecexams.co.za/2019_November_Gr_11_Exams/Physical%20Sciences%20P2%20Grade%2011%20Nov%202019%20Memo%20Eng%20&%20Afr.pdf>), upgrading the best-guess URL to candidate — verify on open: <https://www.ecexams.co.za/2018_November_Gr_11_Exams/Physical%20Sciences%20P1%20Grade%2011%20Nov%202018%20Memo%20Eng%20&%20Afr.pdf> (pattern-guess, NOT sighted; ecexams still CONNECT 403 here 2026-08-07). If it 404s, open the index <https://www.ecexams.co.za/2018_November_Gr_11_Exams.htm> and click the Physical Sciences P1 memo link | <https://www.education.gov.za/LinkClick.aspx?fileticket=_BnHGkPLTbs%3d&tabid=1869&portalid=0&mid=8659> | <https://www.education.gov.za/LinkClick.aspx?fileticket=ip1nUg1Suw0%3d&tabid=1869&portalid=0&mid=8658> |
| [ ] | Geography Gr 12 P2 Nov 2018 — QP supplied by owner upload 2026-08-06 batch 3, tracked at `geography/grade12/2018/paper2.pdf` (15 pp mapwork paper, 75 marks, verified). MEMO still missing: batch 4 (2026-08-06) re-supplied the QP again (`Geography P2 Nov 2018 Eng.pdf`, byte-identical md5 `553fb16…` to the tracked QP). Mirror search 2026-08-06: no direct link found on acceptable hosts — the DBE file is named "Geography P2 Nov 2018 FINAL Memo Eng.pdf" (per Yumpu/Scribd viewer copies); WCED ePortal hosts it at page <https://wcedeportal.co.za/eresource/115736> (link label "NSC NOV 2018 Geography Paper 2 MEMO") but WCED is excluded per SOURCES.md robots block, so use the DBE memo URL at right [direct PDF — click and save]. Direct-link search 2026-08-07: still no direct PDF sighted verbatim on sanctioned hosts (stanmorephysics's Geography Gr 12 mirror files only go back to Nov 2022). ecexams.co.za's Gr 12 NSC Nov 2018 index page DOES exist (sighted verbatim: <https://www.ecexams.co.za/2018_November_NSC_Exams.htm>) and by the site's convention (directory named after the index page + DBE original filename) would hold the memo at candidate — verify on open: <https://www.ecexams.co.za/2018_November_NSC_Exams/Geography%20P2%20Nov%202018%20FINAL%20Memo%20Eng.pdf> (pattern-guess, NOT sighted; ecexams egress-blocked here, CONNECT 403 re-verified 2026-08-07); if it 404s, open the .htm index and click the Geography P2 memo link — otherwise the DBE memo URL at right remains primary | <https://www.education.gov.za/LinkClick.aspx?fileticket=SyVEO7Woybo%3d&tabid=2268&portalid=0&mid=8393&forcedownload=true> | <https://www.education.gov.za/LinkClick.aspx?fileticket=uMTatGRjfvI%3d&tabid=2268&portalid=0&mid=8393&forcedownload=true> |

### School calendars

`school_calendar/2026.json` records its source as the web page
<https://www.gov.za/about-sa/school-calendar> — an HTML source, not a
discarded PDF, so it was excluded from the original refetch list. Batch 3
(owner upload 2026-08-06) nevertheless supplied the underlying Government
Gazette notices, now tracked:

- `school_calendar/2026.pdf` — Gazette GoN 5901, 25 Feb 2025, "2026
  Calendar for Public Schools" (final; gazette page header prints
  No. 52177 although the gov.za filename says 52178gon5901.pdf).
- `school_calendar/2027.pdf` — Gazette No. 51400, GoN 5429, 15 Oct 2024,
  "Proposed 2027 Calendar for Public Schools" (call-for-comments notice;
  the gov.za school-calendar page confirms the 2027 calendar was published
  26 Feb 2025 with identical dates). Extracted to
  `school_calendar/2027.json` matching the 2026.json schema; all per-term
  day counts recomputed from dates+holidays and reconciled with the
  gazette summary (199 learner days / 203 incl. educator days). The
  gov.za page's "Term 3: 46 school days" line contradicts its own dates
  and the gazette (52) and was treated as a typo.

The batch also included three saved gov.za HTML pages (school-calendar.htm
and the 2026/2027 calendar call-for-comments notice pages) — inventoried
as provenance but not committed (the tracked gazette PDFs + JSON carry the
data).
