# Speaking-rate samples — can these engines be slowed to a teaching pace?

Nine outputs of the **same 33-word passage** at different speaking rates, checked in so anyone
can hear the pace difference without re-running inference. This is the follow-up to
`samples/tts-bakeoff/`, which answered "which engine" but left the delivery too fast to teach with.

> Right, let's look at this together. When you factorise a quadratic, you're really asking: which
> two numbers multiply to give the constant term, and add to give the middle one? Let's try one.

**Why this matters.** Natural narration sits around **150 wpm**. A teaching pace for school
learners is **130-140 wpm** — slow enough that a learner can follow a new idea while it is being
said. The original bake-off samples all ran **170-203 wpm**, which is comfortable for an adult
skimming a podcast and too fast for a learner meeting quadratics for the first time. So the
question here is narrow: can each shortlisted engine actually be slowed, and does it still sound
right when it is?

All files are mono 16-bit WAV. Word rate is measured over the whole file, including leading and
trailing silence.

| File | Engine / voice | Rate control used | wpm | Duration |
| :--- | :--- | :--- | ---: | ---: |
| `kokoro_137wpm.wav` | Kokoro-82M, `af_heart` | `speed=0.80` | 136.8 | 14.48 s |
| `kokoro_128wpm.wav` | Kokoro-82M, `af_heart` | `speed=0.75` | 127.9 | 15.48 s |
| `kokoro_173wpm_baseline.wav` | Kokoro-82M, `af_heart` | `speed=1.00` (default) | 172.9 | 11.45 s |
| `piper_cori_140wpm.wav` | Piper 1.6.0, `en_GB-cori-high` | `length_scale=1.4405` | 139.7 | 14.18 s |
| `piper_cori_128wpm.wav` | Piper 1.6.0, `en_GB-cori-high` | `length_scale=1.6431` | 128.0 | 15.46 s |
| `piper_cori_191wpm_baseline.wav` | Piper 1.6.0, `en_GB-cori-high` | `length_scale=1.0` (default) | 190.6 | 10.39 s |
| `piper_vctk_p314_129wpm.wav` | Piper, `en_GB-vctk-medium` spk p314 | `length_scale=2.0246` | 129.1 | 15.34 s |
| `piper_vctk_p347_130wpm.wav` | Piper, `en_GB-vctk-medium` spk p347 | `length_scale=2.0246` | 130.4 | 15.19 s |
| `pocket_163wpm_no_rate_control.wav` | Pocket TTS 2.1.0, cloned from VCTK p347 | **none exists** | 162.8 | 12.16 s |

Kokoro and Piper files are the engine's own 24 kHz / 22.05 kHz output rates respectively; these
are **not level-matched**, same as the parent directory. Level-match before any A/B.

## Kokoro has genuine rate control

`KPipeline.__call__(..., speed=<float>)` reaches the model as a divisor on the **predicted phoneme
durations**, applied before the decoder runs (`kokoro/model.py`, around line 108). The model
therefore **re-synthesizes** at the new pace — it is not resampling or time-stretching the finished
waveform.

That distinction is verifiable, and we verified it. A resample would drag pitch down with the
tempo; a genuine duration change leaves pitch alone. Median F0 across the speed sweep:

| `speed` | 1.00 | 0.85 | 0.80 | 0.75 | 0.70 |
| :--- | ---: | ---: | ---: | ---: | ---: |
| Median F0 | 201.7 Hz | 200.0 Hz | 200.0 Hz | 200.0 Hz | 200.0 Hz |
| wpm | 172.9 | 153.5 | 136.8 | 127.9 | 119.6 |

Flat within 1.7 Hz across the whole range. A naive resample to 0.70x would have landed near
**141 Hz**. No pitch drift. `speed=0.80` gives **136.8 wpm**, squarely in the teaching band.

## Piper has genuine rate control

`SynthesisConfig(length_scale=...)`, where **higher is slower**. It scales the duration predictor's
output the same way, so it is also re-synthesis rather than post-processing.

Note the two voices have **different config defaults**, so a length_scale is only meaningful
against its own voice's baseline:

- `en_GB-cori-high` — config default **1.0**. At **1.4405** → 139.7 wpm; at **1.6431** → 128.0 wpm.
- `en_GB-vctk-medium` — config default **1.4**. At **2.0246** → ~130 wpm (129.1 for p314, 130.4 for
  p347).

**Caveat:** Piper's duration predictor is stochastic — `noise_w=0.8` by default — so the same
length_scale does not give the same duration twice. Expect pace to vary by roughly **±2% run to
run**. Calibrate against a target band, not an exact number.

## Pocket TTS has NO rate control

There is **no speed, rate, tempo or duration parameter anywhere in the package**. Not on the
synthesis call, not in the config, not on the model. This is not an oversight we could work around
with a hidden argument; the control surface does not exist.

**And time-stretching the cloning reference does not work.** The obvious workaround is to slow the
reference audio and hope the clone inherits the pace. We tried it properly: a pitch-preserving
**WSOLA** stretch of the p347 reference to **0.8x** speed, then eight clone runs from each
reference.

| Reference | Mean wpm | SD | n |
| :--- | ---: | ---: | ---: |
| Unstretched | 161.5 | ±7.1 | 8 |
| WSOLA-stretched to 0.8x | **179.7** | **±20.3** | 8 |

The clones from the *slowed* reference came out **faster**, with roughly **tripled variance**.
Pace does not transfer through post-processing — the model reads speaker identity from the
reference, not delivery, and destabilises when the reference is manipulated. `pocket_163wpm_no_rate_control.wav`
is the median run from the unstretched reference, committed here as the honest picture of what
Pocket gives you: about 163 wpm, take it or leave it.

## The consequence

**The engines with rate control cannot clone, and the engine that clones on CPU cannot be slowed.**
Kokoro and Piper both hit 128-140 wpm cleanly, and neither can produce a new voice. Pocket TTS
clones zero-shot on CPU and offers no way to slow it down. There is no engine in the shortlist that
does both.

**Untested route:** record the cloning reference with the speaker *genuinely speaking slowly*, so
the slow delivery is real speech rather than a stretched artifact. That is the one path the
stretching experiment does not rule out, and it has not been tried here.
