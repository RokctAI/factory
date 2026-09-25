# Ray voice samples — a real human reference, cloned

Four real outputs from a CPU test of cloning **Ray's own voice**, checked in so anyone evaluating
the clone can hear it without re-running inference. Every earlier sample set in this repo cloned
either a library corpus voice or an **earlier synthetic sample we generated ourselves** — see
`samples/tts-bakeoff/` and `samples/voicestudio/`. This is the first set cloned from a **real
person who recorded the reference himself and sent it for this purpose**.

All four are the **same test passage**:

> Right, let's look at this together. When you factorise a quadratic, you're really asking: which
> two numbers multiply to give the constant term, and add to give the middle one? Let's try one.

File `01` is **VibeVoice-1.5B**, whose weights are MIT and therefore usable commercially. Files
`02`, `03` and `04` are **VoiceStudio** at three speeds — comparison only, see **Licensing**.

All files are mono 16-bit WAV at 24 kHz.

| File | Engine | `speed` | Audio s | RTF | Words/min | Notes |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| `01-vibevoice-150wpm.wav` | VibeVoice-1.5B | n/a | 13.20 | 6.59x | 150.0 | 211 s wall, peak RSS 11.34 GB, `cfg_scale` 1.3, seed 42 |
| `02-voicestudio-129wpm.wav` | VoiceStudio | 0.68 | 15.33 | 10.3x | 129.2 | teaching pace |
| `03-voicestudio-195wpm.wav` | VoiceStudio | 1.00 | 10.14 | 17.1x | 195.3 | too fast, pitch unstable |
| `04-voicestudio-98wpm.wav` | VoiceStudio | 0.50 | 20.21 | 10.1x | 98.0 | overshoots |

**RTF here is generation wall-clock divided by audio duration, so lower is faster** — the same
direction as `samples/voicestudio/README.md`. Files `02`-`04` are **normalised to -20 dBFS** for
listening; `01` is as generated.

Of the four, **`02` at 129 wpm is the usable teaching pace.** `03` runs too fast and the pitch is
unstable; `04` overshoots into something slower than a person would actually teach at.

## Not committed — the reference recordings

**These files are synthesised renders of Ray's voice, not recordings of him.** They were cloned
from a reference he recorded himself and sent for exactly this purpose.

**The reference audio is deliberately not committed** — not the WhatsApp `.ogg` uploads, not the
converted WAVs, none of the three takes. Those are Ray's **actual voice** rather than a synthesised
render, and they stay off the repo unless he asks for them to be added. Everything below describes
that reference; nothing here reproduces it.

## The source reference

A **WhatsApp voice note** — Ogg Opus, **16 kHz mono, ~18 kbps, 8.53 s**. It is the **best of three
takes by signal-to-noise**: **22.9 dB** SNR, noise floor **-44.8 dBFS**, and **zero clipped
samples**. Converted to **24 kHz mono PCM_16** before cloning.

## The hard limit — a brick wall at 7.8 kHz

**The 16 kHz source has no content above about 7.8 kHz.** The spectrum is flat to **7.6 kHz**, then
collapses about **60 dB** into the 16-bit dither floor by **7.9 kHz**.

**That is the anti-alias filter of the 16 kHz sample rate itself, not a WhatsApp lowpass.** A
16 kHz sample rate cannot represent anything above 8 kHz, so the wall is arithmetic, not a codec
choice — and no amount of WhatsApp tuning would move it.

**The clones inherit it exactly** — measured **-92 dB above 8 kHz** in the output. The models
reproduce the band they were given and invent nothing above it.

**What that costs is brightness and sibilant air, not speaker identity.** F0 and formants F1 to F4
all sit **below 4 kHz** and survive the wall intact, which is why the similarity figures below hold
up. The top octave is what is missing, and **re-recording without WhatsApp in the path is what
recovers it** — the fix is the capture chain, not post-processing.

## WhatsApp's own processing was milder than expected

Measured on the reference rather than assumed:

- **No gating** — no evidence of noise gate action on the quiet passages.
- **Noise-suppression pumping of only +3.3 dB** — present, but small.
- **No aggressive AGC** — the voiced-frame **p10 to p90 dynamic range of 19-21 dB survives**
  intact. A hard AGC would have crushed that.

So the 8 kHz wall above is the real constraint. WhatsApp's DSP is a footnote next to it.

## Similarity

Log-mel cosine — **40 bands, 50 Hz to 8 kHz, 1024-sample Hann window, 256 hop, 40th-percentile
energy gate.** All figures are for **file `01`** against the reference.

| Comparison | Cosine |
| :--- | ---: |
| Clone vs reference | **0.9772** |
| Same speaker, second take | 0.9503 |
| Same speaker, third take | 0.9249 |
| Different man's voice (best of 4 demo voices) | 0.9013 |
| Different woman's voice | 0.6077 |

**Median F0 matched exactly — 145.5 Hz in, 145.5 Hz out.**

**The honest caveat: part of that 0.9772 is channel match, not voice match.** The clone was
generated from that exact recording, so it inherits its 8 kHz wall and its coding noise, and the
metric rewards that alongside the speaker similarity. **Do not read 0.9772 as a pure identity
score.**

**The margin that matters is 0.9772 against the 0.9013 wrong-speaker figure.** A different man's
voice — the closest of four demo voices — scores 0.9013, so the clone clears the nearest wrong
answer by a real margin, and clears it by more than the reference's own second and third takes do
in the other direction. That gap is the result, not the absolute number.

Calibration from earlier work in this project, for scale: **0.98** cloning from **VCTK studio
audio**, **0.79** cloning from **NCHLT outdoor smartphone prompts**. A WhatsApp voice note lands
much nearer the studio end than the field-recording end.

## How they were generated

**CPU only** — 4-core Intel Xeon, **no GPU**. File `01` took **211 s of wall clock** at a peak RSS
of **11.34 GB**, with `cfg_scale` 1.3 and seed 42.

## Licensing

**File `01` is the one that can ship. Files `02`-`04` cannot.**

- **VibeVoice-1.5B — weights are MIT.** File `01`'s engine is **usable commercially**, with no
  non-commercial term and no third-party tokenizer licence riding along.
- **VoiceStudio — `k2-fsa/OmniVoice` weights are CC-BY-NC**, with a separate **Boson Higgs Audio 2
  Community License** on the bundled audio tokenizer. Files `02`-`04` are here **for comparison
  only**, and **that engine cannot ship.**

The full licence analysis, including why an automated licence scan reports these weights as clean
when they are not, is in **`samples/voicestudio/README.md`** — read it before considering
VoiceStudio for anything shipping.
