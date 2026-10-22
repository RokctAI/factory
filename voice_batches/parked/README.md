# voice_batches/parked/

Batches taken out of `voice_batches/inbox/` so that no voice batch run picks
them up: the daily scan and push runs only read the inbox, and a
continuation of a parked batch no longer finds its file.
To restart one, move it back into the inbox (a push that adds one batch
renders it; several are picked up one per day by the scan).

- `r3_packs_*.json`, `r3_phonics_probe.json` (Grades R-3 pack audio,
  assistant_005 / voice_b_sister): parked 2026-10-22 on the owner's call
  ("stop grade r-3, im not feeling the voice for kids"). Passed audio stays
  in RokctAI/lessons `voices/r3/`; the in-flight chain (run 39857583124) was
  cancelled.
