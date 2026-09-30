# Media regression baseline (step 0)

Before any media code moves into rokct-media, `.github/workflows/baseline.yml`
renders one small, fixed fixture with each **current** engine and keeps what
it produced as Actions artifacts, with `baseline_manifest.json` describing
it. Every later migration step renders the same fixtures through the new
package and compares (`rokct-media compare old/ new/`, thresholds in the
spec's migration section).

Nothing here changes engine code: the guard job fails the run if this branch
differs from factory main at `FACTORY_BASE` anywhere outside `baseline/` and
the workflow file.

## Fixtures

| engine | fixture | source (pinned in the workflow `env`) |
|---|---|---|
| `tutor_voice` | `fixtures/tutor_voice.json`: tutor_001, Voice A, line `acknowledgements/02` (its committed render is on agent main, so the run also says whether it reproduces it) | factory `voice_batch/run.py`; agent main for scripts and reference |
| `radio_ad` | `radio_ads/examples/kasi_corner_30.json`, model revision pinned | factory `radio_ads/make_ad.py`; agent main for the persona references |
| `reel_voices` | `fixtures/reel_voices_batch.json`: the `open` line of PR #196's batch, Voice B, seed 44 first | factory PR #196 head `radio_ads/reel_voice.py` |
| `social_reel` | grant card `2027-03-05_Open_Call_for_Feasibility_Fund_New_Zealand`, date 2026-10-01 (fixes the seed) | factory `social/facebook` motion, music, preview; agent main renderer; opportunities pinned |
| `lesson6` | `fixtures/lesson6_card.md` pointing at the session lesson `cash-receipts-journal`, sapi backend | factory `lessons/scripts/CAPS/lesson_manifest.py` |
| `tiktok_post` | `tutor_001/w01/d1_mon/s03` (brief + still; no voice file exists yet, the post is `silent_ok`) | agent PR #202 head `tiktok_render.py` |
| `still_tutor_images` | tutor_001 card and avatars from its source portrait | agent main `tutor_images.py`; portrait from the last commit that has it |
| `still_tour` | supacharge screenshot `06-schedule`, pinned | agent main `tour_still.py` |
| `still_typed_pr202` | `tutor_001/w01/d1_mon/s03/still.webp` | not baselined: its generator is not committed; the file's hash is recorded as the reference |
| `guided_tour` | minilauncher's committed `marketing/tour/screenshots` (no emulator) | shared-workflows `scripts/tour` (merge_fragments + assemble) |

Private inputs (agent repo) are referenced by repo@sha and path, never copied
here.

## Publishing and pushing are off

- The workflow token is read-only (`contents: read`).
- The only secret a job sees is `MONOREPO_PAT`, used as a checkout token with
  `persist-credentials: false` (no checkout keeps it, so no checkout can be
  pushed from; each source's `credentials_in_git_config` is recorded) and by
  the tour fragment fetch. No platform credential exists in any job, and
  `record.py` refuses to run a step if one does.
- Each engine is driven below the entry point that publishes:
  - tutor voice: `run.py` only; the agent-branch commit and PR scripts are
    separate workflow steps that this workflow never runs.
  - radio ad, reel voices: they only write files; outputs go to artifacts.
  - social Reel: `drivers/social_reel.py` calls `make_brief`, `make_motion`,
    `render` and `preview.one`; never `main`, so the ledger and the three
    platform posters are unreachable (their modules are not imported), and
    every HTTP entry point in the process raises.
  - Lesson 6: `lesson_manifest.py` only; the card state machine, release
    upload and ledger commit of `lesson6_production.yml` are not run.
  - TikTok and stills: renderers only write files; `tour_still.fetch` is
    replaced by a pinned checkout.
  - guided tour: `assemble.py` only; the caller workflow's commit-back and
    store upload are not run.
- `tools/forbidden.txt` lists publish and push commands; the guard job fails
  if any appears in `baseline/` or the workflow.
- No cache is saved (restore only), so production cache entries are never
  evicted.

## Cloned voices

This repository is public, so its Actions artifacts are public. Audio in
Voice A or Voice B is measured (sha256, duration, loudness, F0) and then
withheld from the artifact. Renders are deterministic, so the hashes are the
baseline; a compare job re-renders the old engine beside the new one. To keep
the audio itself, set the repository secret `BASELINE_ARTIFACT_KEY`: withheld
files are then uploaded as `withheld.tar.gz.enc`
(`openssl enc -d -aes-256-cbc -pbkdf2 -pass env:BASELINE_ARTIFACT_KEY`).

## Files

- `tools/record.py`: runs a step, then lists outputs with sha256 and metrics
  into `baseline_fragments/<engine>.json`.
- `tools/merge.py`: folds fragments into `baseline_manifest.json`.
- `drivers/`: the small callers for engines driven as functions.
- `actions/voice-engine`: shared setup for the three voice jobs.
