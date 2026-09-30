# voice_batch

Renders a tutor's standing lines (acknowledgements, greetings, sign-offs,
teaching snippets) in the tutor's consented cloned voice (kind `tutor`), or
the Grades R–3 activity-pack lines (kind `r3`), gates every line, and
commits the passing audio on a `rokct/` branch of the private
`RokctAI/agent` repo, then opens (or notes the run on) a PR from that
branch into `main`. Workflow: [`.github/workflows/voice_batch.yml`](../.github/workflows/voice_batch.yml).

**Nothing identifying and no audio ever lands in this public repo.** The
reference clip, the line scripts and the rendered audio live only in the
private agent repo; this repo holds code plus a small batch JSON naming ids,
paths and a hash. The job has no artifact upload, caches only public model
weights, and logs/summaries show line ids and scores only.

## Trigger a batch

Commit one JSON to `voice_batches/inbox/` on `main` (one batch per push), or
run the workflow by hand ("Run workflow", `batch_path`):

```json
{
  "tutor": "tutor_001",
  "voice": "voice_a",
  "ref_path": "lms/team/voice_refs/voice_a_ref.wav",
  "ref_sha256": "<sha256 of the reference in the agent branch>",
  "agent_branch": "rokct/<branch>",
  "categories": ["acknowledgements", "greetings", "signoffs", "teaching"],
  "lines": ["tutor_001/greetings/01", "tutor_001_sample_line"]
}
```

`lines` is optional: a subset of ids for a quick smoke batch. Only the
categories it touches get a job. `agent_branch` must start with `rokct/`
(CI-written branches only; never `main`).

Optional for both kinds: `f0_target_hz` and `f0_tolerance_hz`, the median-F0
gate (default 102 ± 8 Hz = 94–110 Hz, tuned to Voice A, so existing batches
behave exactly as before). Set them for any other voice.

### R–3 batches

```json
{
  "kind": "r3",
  "voice": "<voice>",
  "ref_path": "lms/team/voice_refs/<voice>_ref.wav",
  "ref_sha256": "<sha256>",
  "agent_branch": "rokct/<branch>",
  "packs": "english_home_language.gradeR.term1.*",
  "lines": ["english_home_language.gradeR.term1.w01_sound_a.show"],
  "locale": "en",
  "f0_target_hz": 210,
  "f0_tolerance_hz": 25
}
```

`packs` (a pack-id glob or a list of globs), `lines` (app line keys) and
`locale` are optional. Without filters a batch renders all 310 pack lines of
the 20 Grade R Term 1 packs plus the 4 default praise lines (314), split
into 8 shard jobs of about 40 lines. A `packs` filter leaves out the shared
praise lines. `locale` only changes the praise lines (packs are English):
`af` renders the 4 Afrikaans praise lines as `<key>.af.mp3` with the
multilingual ASR model, which the app does not play yet.

Line keys match the app exactly (`r3_lines.py`, checked against
`r3_session_engine.dart` by `tests/test_r3.py` with `AGENT_ROOT`):
`<pack id>.show`, `.hints_0`/`.hints_1`, `.rounds_<i>_prompt|_praise|_story`,
`.beat_the_tutor_setup|_tutor_try|_win_line|_gentle_line`, and
`r3.r3_praise_{yes,great,clever,right}` (text read from the app's
translations, with a checked-in fallback).

**Phonics.** `r3_respellings.json` maps a line key (or an exact line text)
to a TTS-only text so the voice says the letter *sound*, not its name
("a as in ant" → "Ah, as in ant"). The pack text shown on screen never
changes. A respelled line is rendered from, and ASR-checked against, the
respelling, and is marked `needs_listen: true` in the manifest: a person
should listen before merging. `voice_batches/examples/r3_phonics_probe.json`
is a 6-line probe for this; it runs only if moved into `inbox/`.

Output: `lms/dart/templates/assets/r3_packs/audio/<key>.mp3` (mono, 24 kHz,
64 kbps CBR, via lameenc or ffmpeg), which the app's `AssetTutorVoice` plays
as `assets/r3_packs/audio/<key>.mp3`, plus `r3_manifest.<voice>.json`
beside it (shards write `r3_manifest.<voice>.partNN.json`; the merge job
folds and removes them).
Re-running a batch is idempotent: lines whose text and reference are
unchanged are skipped; changed ones are re-rendered and overwrite the same
files.

## Pronunciations

`pronunciations.json` fixes how the voice says a word, for every batch kind
(tutor and r3). It ships empty; add entries as needed:

```json
{
  "words": {"Mahikeng": "mah-hee-KENG"},
  "ambiguous": {"<Name>": ["<variant 1>", "<variant 2>"]}
}
```

- `words`: every whole-word use of the word (any case) is spoken as the
  respelling.
- `ambiguous`: words, usually names, with more than one right pronunciation
  for the same spelling, with the known variants. The global list never
  touches them. A line that uses one must say which it means inline, or the
  batch fails with, e.g., `line tutor_009/greetings/01 uses '<Name>': write
  {{<Name>|<variant 1>}} or {{<Name>|<variant 2>}}`.
- Inline, in the line's script: `{{Thendo|TEN-doh}}`. The voice gets the
  part after the bar; the display text (manifest `text`) and the word check
  get the part before it. Inline always wins over the file, and any
  respelling is allowed, not only a listed variant.

Only the spoken text changes. The word check stays word-exact except for
the respelled words, which match 1 to N transcript words (N = the larger of
the word's and the respelling's word counts, plus one). A line with a
pronunciation records `tts_text` and `pronounced` in the manifest and is
marked `needs_listen`. Changing a pronunciation changes `render_sha256`, so
the next batch re-renders that line.

The r3 check runs in the plan job (the packs are here). Tutor scripts live
in the agent repo, so each render job checks them after checkout
(`batch.py --agent-root .agent`). The app shows the `samples.json` teaching
`script` on the tutor card, today through a hand-copied demo constant
(`kDemoTutorSnippets`); avoid inline markup in `samples.json`, or strip it
when that constant is re-copied. Greetings, acknowledgements and sign-offs
are never displayed.

R–3 phonics respellings stay in `r3_respellings.json` (whole-line); word
pronunciations apply after them.

**Audition.** A push to `main` that changes `pronunciations.json` (or a
manual run of `pronunciation_audition.yml` with a comma-separated `words`
list) renders one short clip per changed word and voice (every variant of
a changed ambiguous entry), so someone can listen and adjust. The clips go
to the agent repo's `rokct/pronunciation-audition` branch, never to this
repo: `lms/team/voices/samples/pronunciation/<voice>/<word>--<respelling>.mp3`,
with `audition.json` beside them. `voices/samples/` is excluded from the app
bundle by `sync_team_assets.dart`. No agent PR is opened. The carrier is
`<respelling>. <respelling>.`, one take, seeds 11/22/33 until a light QC
passes (0.4–8 s, not silent, similarity ≥ 0.75, and the tail check once
`qc.py` has it); no ASR check, since these are unusual words. Otherwise the
best take is kept and marked `passed: false`.

## What a run does

1. **plan** lists the changed batch, validates it (`batch.py`) and emits one
   matrix entry per category (tutor) or per shard (r3, at most 8).
2. **render** (one runner per category, in parallel): checks out the agent
   branch, verifies the reference sha256 (fails on mismatch), installs CPU
   torch + the pinned VibeVoice fork, restores the model weights, then
   `run.py`:
   - splits each line into sentences (`textnorm.py`, `lines.py`: spoken
     text only, never markdown or metadata);
   - renders every sentence with seeds 11/22/33, one take at a time
     (`render_takes.py`, reusing the agent repo's `render_voices.py`);
   - measures each take (`qc.py`): word-exact ASR, median F0, upward
     swings, speaker similarity to the reference;
   - picks per sentence: median F0 closest to the target (default 102 Hz), then fewest swings,
     then higher similarity; stitches with 280–320 ms pauses and 12 ms
     fades; normalises to -20 dBFS, 24 kHz mono PCM_16;
   - gates the final file: median F0 in the batch's gate (default 94–110 Hz), similarity ≥ 0.88
     (≥ 5 s) or ≥ 0.83 (< 5 s), word-exact ASR;
   - lines not yet passing get seed 44, then 55; still failing = recorded
     as failed, audio not committed;
   - writes `<voice>_manifest.<category>.json` and commits the passing
     WAVs + that manifest to the agent branch (`ci/push_agent.sh`, with
     rebase-and-retry because category jobs push concurrently).
3. **merge** folds the category manifests into `<voice>_manifest.json`
   (r3: the shard parts into `r3_manifest.<voice>.json`), then
   `ci/open_agent_pr.py` opens a ready-for-review PR from the agent branch
   into `main` if none is open, or leaves one comment on the open one with
   this run's pass/fail counts (counts and run URL only). Merging that PR
   ships the audio into the app bundle.

Output layout in the agent repo (audio beside its script):
`lms/team/tutors/CAPS/<tutor>/<category>/NN.wav`,
`.../samples/<sample id>.wav`, `.../samples/sample_line.wav`.

## Caches

The model weights entry is shared with `radio_ads.yml` (same path and key
format), so the two workflows reuse one ~5.6 GB entry instead of evicting
each other under the 10 GB repository limit. The word-check ASR model has its
own small cache. Takes, references and audio are never cached.

## Expected wall time (first run, per category job)

Setup ~8–12 min (install, cache restore or first download), then roughly
acknowledgements ~10 min, sign-offs ~20 min, teaching ~35 min, greetings
~45 min of rendering and QC for seeds 11/22/33; each extra seed round for
failing lines adds ~30%. Categories run in parallel, so a full tutor batch
takes about as long as the greetings job (~1 h). A 3-line smoke batch takes
~20 min.

## Local tests

```bash
python -m pytest voice_batch/tests                         # model-free
AGENT_ROOT=/path/to/agent python -m pytest voice_batch/tests   # + real line scripts and the app's Dart
```
