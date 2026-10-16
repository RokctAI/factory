# Implementation Plan — Bible Series Audit & Alignment

This plan addresses the broken cross-references and table numbering shifts discovered in the `forbidden_questions` bible series (`factory/bible/forbidden_questions/`).

## User Review Required

> [!IMPORTANT]
> The audit of the 15 bible series episodes revealed a systematic numbering mismatch between the file index in [00_series_index.md](file:///c:/Users/sinya/Desktop/RokctAI/factory/bible/forbidden_questions/00_series_index.md) and the actual files in [episodes/](file:///c:/Users/sinya/Desktop/RokctAI/factory/bible/forbidden_questions/episodes).
>
> We will correct the index table, the core thread references in the index file, and all broken references inside the individual episode markdown files. No theological content will be modified.

## Open Questions
No open questions. The correction is a precise, mechanical fix of the file numbering mismatches and cross-references.

## Proposed Changes

### Index and Episode Reference Corrections

We will write a python script [fix_bible_refs.py](file:///C:/Users/sinya/.gemini/antigravity/brain/194cee78-737a-4a34-850a-cfb3fe3576a1/scratch/fix_bible_refs.py) to automatically perform the following replacements across all files in [forbidden_questions/](file:///c:/Users/sinya/Desktop/RokctAI/factory/bible/forbidden_questions):

1. **In `00_series_index.md`**:
   - Update table rows 13, 14, 15 filenames to match actual filenames:
     - `12_palestinians_canaanites.md` -> `13_palestinians_canaanites.md`
     - `13_third_temple.md` -> `14_third_temple.md`
     - `14_milk_and_honey.md` -> `15_milk_and_honey.md`
   - Update thread diagram references:
     - `God promises milk and honey — conditional on curse removal (14)` -> `(15)`
     - `Promise still pending — Dead Sea still dying (14)` -> `(15)`
     - Add `(14)` to the Third Temple reference: `Third Temple site blocked by their holy structures (14)`

2. **In the individual episode markdown files (`episodes/*.md`)**:
   - Replace shifted/incorrect file references:
     - `06_naamah_and_the_ark.md` -> `07_naamah_and_the_ark.md`
     - `07_canaan_curse.md` -> `08_canaan_curse.md`
     - `08_gods_glory_departs.md` -> `09_gods_glory_departs.md`
     - `09_israel_interbreeds.md` -> `10_israel_interbreeds.md`
     - `10_lost_ten_tribes.md` -> `11_lost_ten_tribes.md`
     - `11_abrahams_eastern_sons.md` -> `12_abrahams_eastern_sons.md`
     - `12_palestinians_and_canaanites.md` -> `13_palestinians_canaanites.md`
     - `12_palestinians_canaanites.md` -> `13_palestinians_canaanites.md`
     - `13_third_temple.md` -> `14_third_temple.md`
     - `14_milk_and_honey.md` -> `15_milk_and_honey.md`

## Verification Plan

### Automated Verification
- Re-run our python audit script to verify that:
  - All filenames listed in `00_series_index.md` exist.
  - No broken links exist in the cross-reference sections or content.
