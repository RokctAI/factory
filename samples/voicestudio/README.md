# VoiceStudio samples — cloned voice at teaching pace

Four real outputs from a CPU test of **VoiceStudio** (previously OmniVoice-Studio), checked in so
anyone evaluating pace control can hear a **single cloned voice slowed down** without re-running
inference. The other engines in `samples/tts-bakeoff/` either clone or slow down — none did both.
This is the listening evidence that one engine can do both at once.

All four are the **same test passage**:

> Right, let's look at this together. When you factorise a quadratic, you're really asking: which
> two numbers multiply to give the constant term, and add to give the middle one? Let's try one.

File `01` is the model's default voice with no cloning. Files `02`, `03` and `04` are the **same
cloned voice** at three different speeds — that is the comparison worth listening to.

All files are mono 16-bit WAV at 24 kHz.

| File | Voice | `speed` | Duration | Words/min | RMS |
| :--- | :--- | ---: | ---: | ---: | ---: |
| `01-default-voice-172wpm.wav` | Default, no cloning | 1.00 | 11.48 s | 172.5 | -19.7 dBFS |
| `02-cloned-default-191wpm.wav` | Cloned, default speed | 1.00 | 10.35 s | 191.3 | -24.4 dBFS |
| `03-cloned-slowed-153wpm.wav` | Cloned, slowed | 0.68 | 12.93 s | 153.1 | -25.0 dBFS |
| `04-cloned-teaching-pace-130wpm.wav` | Cloned, teaching pace | 0.50 | 15.28 s | 129.6 | -24.6 dBFS |

**Not committed**: the reference audio the clone was made from. It is a **VibeVoice Realtime-0.5B
output in the Carter preset that we generated earlier in this project**, trimmed to a **9.60 s
transcript-aligned excerpt**. It is not a real person's voice. The full-length version of that same
Carter reference is already in this repo as `samples/tts-bakeoff/ref_vibevoice_0.5b_carter_27s.wav`
if you want to A/B against it. The VibeVoice **demo voice assets** under Microsoft's repo are not
ours to redistribute and are **not** here.

## The engine

- **VoiceStudio** (previously OmniVoice-Studio) — <https://github.com/debpalash/OmniVoice-Studio>,
  cloned at commit **`afa3619`**.
- **Weights** — `k2-fsa/OmniVoice` from Hugging Face. **3.27 GB** on disk, **612M** parameters, on a
  **Qwen3-0.6B** base.

## How they were generated

**CPU only** — 4-core Intel Xeon, **no GPU**. torch **2.8.0+cpu**, **float32**, `num_step=32`,
`OMP_NUM_THREADS=4`.

| File | `speed` | Gen s | Audio s | RTF | Words/min |
| :--- | ---: | ---: | ---: | ---: | ---: |
| `01` default voice, no cloning | 1.00 | 79.18 | 11.48 | 6.90x | 172.5 |
| `02` cloned, default speed | 1.00 | 144.74 | 10.35 | 13.98x | 191.3 |
| `03` cloned, speed 0.68 | 0.68 | 175.57 | 12.93 | 13.58x | 153.1 |
| `04` cloned, speed 0.50 | 0.50 | 200.44 | 15.28 | 13.12x | 129.6 |

**RTF here is generation wall-clock divided by audio duration, so lower is faster** — the same
direction as `samples/vibevoice/README.md`, the inverse of the ×realtime column in
`samples/tts-bakeoff/README.md`. Peak RSS ranged **2.97 GB to 3.83 GB**.

This is slow. Cloning roughly **doubles** generation time against the default voice, and slowing the
speech adds more on top, because a lower `speed` means more audio tokens to fill. Treat these as
offline-render numbers, not interactive ones.

## Why this engine was tested

It is the **only candidate whose speed control operates on the voice-cloning path** rather than
time-stretching the output afterwards. Every other engine we slowed down either could not clone, or
produced its normal-speed audio and then resampled or phase-vocoded it — which drags artefacts and a
stretched-tape quality along with the slower pace.

The mechanism, in the bundled `omnivoice` package:

- `omnivoice/models/omnivoice.py:1193` passes the per-item `speed` into `_estimate_target_tokens`
  (`:1233`),
- which divides the estimated duration by it — `est = est / speed` (`:1244`),
- and the result becomes `target_lens` (`:1224`),
- which sizes the audio-token canvas the decoder fills (`:1418`).

So the model **generates into a longer budget** rather than stretching audio after the fact. The
slower delivery is synthesized, not post-processed.

## What a listener needs to know

**`speed` maps non-linearly to words per minute.** It is a budget multiplier, not a rate dial —
the model spends the extra room partly on slower articulation and partly on longer pauses, and it
does not spend all of it. `speed` **0.68 gave 153 wpm** and **0.50 gave 130 wpm**, against 191 wpm
at 1.00. Halving `speed` did **not** halve the rate. Pick a target wpm by measuring, not by
arithmetic.

**The cloned output is about 5 dB quieter than the default voice** — roughly **-24.5 dBFS** across
`02`-`04` versus **-19.7 dBFS** for `01`. This is inherited from the reference, whose loudness the
model tracks. **Normalise before use**, and level-match before any A/B, or you will hear the
loudness difference as a quality difference.

## Licensing

**These weights cannot be used in a commercial product as they stand.** That is the headline; the
detail follows. All of it is read from primary sources — the local model snapshot and the upstream
terms — not assumed from tooling.

**Do not trust an automated licence scan here.** The Hugging Face YAML frontmatter and API metadata
for `k2-fsa/OmniVoice` carry **no `license` field at all**, so a scanner reports the model as
"unspecified" — which reads as clean and is not. The real terms are in prose and in a bundled
`LICENSE` file, where no scanner will look.

- **VoiceStudio repo code — AGPL-3.0-only.** `LICENSE-NOTICE.md` in the repo states AGPL-3.0-only
  and is explicit that this *does* include commercial and internal business use, with the usual
  Affero obligation to publish your source if you modify it and expose it over a network. A
  **commercial licence is offered** by the author for embedding it in a closed-source product.
- **`k2-fsa/OmniVoice` pre-trained weights — CC-BY-NC, non-commercial.** The model card says it
  directly, under `## License`: *"Our code is released under the Apache 2.0 License. The
  pre-trained model is licensed under the CC-BY-NC due to constraints from its training data
  (e.g., Emilia)."* Note the split — the upstream *code* is Apache-2.0, the *weights* are not.
- **The training-data constraint is real, not boilerplate.** Upstream **Emilia**'s gated terms put
  the core corpus under **CC-BY-NC**; only the **Emilia-YODAS** subset is CC-BY. The dataset's
  `cc-by-4.0` tag on Hugging Face is misleading on this point, so the non-commercial term genuinely
  propagates into these weights.
- **The bundled audio tokenizer is a second, independent restriction.** The snapshot ships a full
  `audio_tokenizer/LICENSE` containing the **Boson Higgs Audio 2 Community License Agreement**
  (Boson AI USA, Inc.), itself based on the Meta Llama 3 Community License. It requires **prominent
  attribution** — *"Built with Higgs Materials licensed from Boson AI USA, Inc."* — and its §2
  requires a **separate expanded licence from Boson above 100,000 annual active users**. Clearing
  the CC-BY-NC problem would still leave this one.
- **No commercially-usable checkpoint exists today.** The sibling `k2-fsa/OmniVoice-Emilia` is
  research-only, and the open requests for either a commercial licence or a YODAS-only retrain
  (Hugging Face discussions **#29** and **#31**) are **unanswered**.

So the AGPL on the application code is the *easy* part, and the commercial licence on offer does
not solve the real problem. **The weights are the blocker**, and no licence from the VoiceStudio
author can lift it — the constraint comes from the upstream training data and from a third party's
tokenizer. Using this engine in a commercial product would require retrained or differently
licensed weights, which nobody is currently offering.
