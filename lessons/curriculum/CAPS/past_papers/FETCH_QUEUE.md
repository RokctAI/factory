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

### 1. Geography P2 November 2024 — re-download needed

The 2026-08-06 upload's Geography P2 files were duplicates of Accounting P2
(question paper and memo both) — supplied file was a duplicate of Accounting
P2 — re-download needed. The mis-supplied PDFs have been removed from
`geography/grade12/2024/`; the real Geography P2 (Rural & Urban Settlements /
Economic Geography) is still absent from the repo.

| Done | Paper | Question paper URL | Memo URL |
|:---:|---|---|---|
| [ ] | Geography P2 (Nov 2024) | <https://www.education.gov.za/LinkClick.aspx?fileticket=LrQ39-VlNh4%3d> | <https://www.education.gov.za/LinkClick.aspx?fileticket=2qulvYkBv6k%3d> |

Note: verify page 1 of both downloads reads "GEOGRAPHY P2" before supplying —
the previous upload delivered Accounting P2 content under these names.

### 2. Mathematical Literacy P1 + P2 November 2024 ADDENDUM PDFs

The addenda (Annexures A–C per paper) are separate DBE files, not part of the
question-paper PDFs already supplied. Several transcribed answers depend on
their tables/maps (P1: income-tax table, retailer price graphs, budget pie
charts; P2: campsite aerial view, trail-run map/elevation profile, Australia
trip map). Annexure-dependent values in
`mathematical_literacy/grade12/2024/paper[12].json` were reconstructed from
memo working and flagged `[ANNEXURE ... - not in repo]`; supplying the addenda
allows verbatim verification.

Web search (2026-08-06) exposes the official file names — "Mathematical
Literacy P1 Addendum Nov 2024 (Eng)" and "Mathematical Literacy P2 Addendum
Nov 2024 (Eng)" — but no direct education.gov.za fileticket URLs, so the
page-level link is recorded:

| Done | File | Where to fetch |
|:---:|---|---|
| [ ] | Mathematical Literacy P1 Addendum (Eng) | DBE session page: <https://www.education.gov.za/2024NSCNovemberpastpapers.aspx> |
| [ ] | Mathematical Literacy P2 Addendum (Eng) | DBE session page: <https://www.education.gov.za/2024NSCNovemberpastpapers.aspx> |

Known mirrors (for cross-checking, prefer the DBE originals):
<https://www.theanswer.co.za/wp-content/uploads/2024/11/NSC-2024-Gr-12-Maths-Lit-P1-Addendum.pdf>,
<https://www.theanswer.co.za/wp-content/uploads/2024/11/NSC-2024-Gr-12-Maths-Lit-P2-Addendum.pdf>,
and WCED ePortal (search "Mathematical Literacy addendum Nov 2024").

### 3. November 2025 session

The owner upload of 2026-08-06 contained November 2024 papers only — no
November 2025 (or May/June 2025) papers. The DBE has published the November
2025 NSC papers here (page-level link; direct fileticket URLs not yet
recorded):

- <https://www.education.gov.za/Curriculum/NationalSeniorCertificate(NSC)Examinations/2025NovemberExamPapers.aspx>

To pull: P1/P2 question papers + memos (English) for Mathematics,
Mathematical Literacy, Physical Sciences, Accounting, Economics and
Geography, then add the sessions to the per-subject `index.json` files and
mirror rows here.

## Done

All November 2024 papers below were supplied by owner upload 2026-08-06 and
transcribed to `paperN.json` on 2026-08-06 (except Geography P2 — see NEXT
BATCH above). All are English-language, November 2024 NSC, Grade 12, from the
session page <https://www.education.gov.za/2024NSCNovemberpastpapers.aspx>.

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

(Geography P2 rows moved to NEXT BATCH — the supplied files were Accounting
P2 duplicates.)

## How to extend this queue

Older sessions on the DBE portal (November + May/June, 2008 to present) are
not indexed yet. To extend this queue, add their sessions/papers to the
per-subject `index.json` files
(`lessons/curriculum/CAPS/<subject>/past_papers/index.json`) and mirror the
new entries here as additional table rows.
