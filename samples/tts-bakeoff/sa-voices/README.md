# South African English voice samples — references, clones and Piper renditions

Ten files probing the one gap the bake-off left open: **no engine tested has an en-ZA voice**, so a
South African accent has to come from a cloned reference. These are the clone experiments that
followed, using the only two openly-licensed corpora with labelled South African English speakers.

> ⚠️ **These are evaluation artifacts, not production voices.** Read the consent caveat at the
> bottom before reusing any of this. The corpus licences do not cover what a licence would need to
> cover here.

All files are mono 16-bit WAV. The synthesized passage is the same teaching passage used throughout
`samples/tts-bakeoff/`; the reference files are corpus speech, not the passage.

| File | Source | Speaker | What it demonstrates | Rate | Duration |
| :--- | :--- | :--- | :--- | ---: | ---: |
| `ref_vctk_p314.wav` | CSTR VCTK 0.92 (5 utts, mic1) | p314 — 26F, Cape Town | Real studio reference | 24 kHz | 29.33 s |
| `ref_vctk_p347.wav` | CSTR VCTK 0.92 (4 utts, mic1) | p347 — 26M, Johannesburg | Real studio reference | 24 kHz | 27.99 s |
| `pocket_clone_vctk_p314.wav` | Pocket TTS 2.1.0 | p314 | Clone of the p314 reference | 24 kHz | 12.40 s |
| `pocket_clone_vctk_p347.wav` | Pocket TTS 2.1.0 | p347 | Clone of the p347 reference | 24 kHz | 11.44 s |
| `vctk_sa_p314.wav` | Piper `en_GB-vctk-medium` (spk 35) | p314 | Piper's own rendition, not a clone | 22.05 kHz | 11.09 s |
| `vctk_sa_p323.wav` | Piper `en_GB-vctk-medium` (spk 31) | p323 — 19F, Pretoria | Piper's own rendition, not a clone | 22.05 kHz | 13.21 s |
| `vctk_sa_p336.wav` | Piper `en_GB-vctk-medium` (spk 51) | p336 — 18F, Johannesburg | Piper's own rendition, not a clone | 22.05 kHz | 10.03 s |
| `vctk_sa_p347.wav` | Piper `en_GB-vctk-medium` (spk 32) | p347 | Piper's own rendition, not a clone | 22.05 kHz | 11.03 s |
| `ref_sa_nchlt_eng.wav` | NCHLT English Speech Corpus | speaker 500 | Real smartphone reference | 16 kHz | 29.95 s |
| `pocket_clone_sa_nchlt_eng.wav` | Pocket TTS 2.1.0 | speaker 500 | Clone of the NCHLT reference | 24 kHz | 12.24 s |

The four `vctk_sa_*.wav` files are **all four South African speakers** the VCTK corpus contains,
rendered by Piper's multi-speaker `en_GB-vctk-medium` model. Piper is not cloning here — those
speakers are baked into that checkpoint as speaker IDs.

## Attribution — required by licence

**VCTK.** CSTR VCTK Corpus version 0.92, University of Edinburgh, licensed **CC BY 4.0**. Speakers
used: **p314** (26, female, Cape Town), **p323** (19, female, Pretoria), **p336** (18, female,
Johannesburg), **p347** (26, male, Johannesburg). These are the only **4 of 110** speakers in the
corpus labelled `SouthAfrican`.

**NCHLT.** NCHLT English Speech Corpus, licensed **CC BY 3.0**, attribution to the **Department of
Arts and Culture (DAC)**, the **CSIR** and **North-West University (NWU)**. Speaker used: **500**.

Both licences require attribution wherever this audio or anything derived from it travels. Carry
these credits with the files.

## Measured clone quality

Log-mel cosine similarity against each speaker's own reference. The **ceiling** is the reference's
own split-half self-similarity — the score a perfect clone could hope for, given the measure is
noisy against real speech. The **baseline** is Pocket's preset `alba` voice with no cloning at all.

| Reference | Clone | Ceiling (self-similarity) | Preset baseline |
| :--- | ---: | ---: | ---: |
| VCTK p347 (studio) | **0.9859** | 0.9324 | 0.8006 |
| VCTK p314 (studio) | **0.9790** | 0.9669 | 0.8551 |
| NCHLT spk 500 (smartphone) | **0.7887** | 0.9641 | 0.6829 |

Both VCTK clones scored **above their references' own self-similarity ceilings** — the clone is
more consistent with the reference than two halves of the reference are with each other, because
synthetic speech has less within-speaker variation than a human reading aloud. Against preset
baselines of 0.8006 and 0.8551, the cloning is doing real work.

The NCHLT clone managed only **0.7887** from the same engine and the same procedure. The difference
is the recording: NCHLT is **prompted speech captured on smartphones**, VCTK is studio.

**Lesson: reference recording quality dominates clone fidelity.** Not reference length, not the
engine, not the tuning — the microphone and the room. Budget for a good recording before anything
else. (The NCHLT number is also a cross-rate comparison, 16 kHz reference against 24 kHz output, so
it is not strictly comparable to the VCTK rows — but the gap is far too large to be an artifact of
that.)

## Caveat on accent labelling

The corpus metadata records **accent, age, gender and city** and nothing more. It does **not**
record which variety of South African English these speakers speak. "SouthAfrican" plus a city is
all there is. Do not read these four VCTK speakers as representative of South African English
generally, and do not infer a variety from a city name.

## ⚠️ Consent — why these are not production voices

**These are evaluation artifacts only.**

The corpus licences cover **copyright**. They do **not** cover the speakers' consent to synthetic
voice creation. Those people consented to contribute to speech-technology research; they did not
consent to having a synthetic replica of their voice built, and nothing in CC BY asked them to.

Concretely:

- **POPIA** treats a voiceprint as **biometric special personal information**, which requires
  **purpose-specific consent**. Consent to corpus research is not consent to voice cloning.
- **CC licences do not grant personality rights.** A copyright licence cannot hand over someone's
  voice, likeness or identity, because those were never the licensor's to give.

**Production voices must be commissioned** — a paid voice artist, recorded to brief, under a
contract with an **explicit synthetic-voice clause** covering training, cloning, retention and
scope of use. There is no shortcut through an open corpus, and this directory should not be read as
suggesting one.
