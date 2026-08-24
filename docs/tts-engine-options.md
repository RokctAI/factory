# TTS Engine Options for Tutor/Mandy Voice Generation

> Reference doc, not a decision yet. You have no existing voice to clone (your own or anyone else's) — a
> picked/trained voice is fine. Constraint: CPU-only VPS available; API-based generation is acceptable too.

> **Update (Level 6 build, 2026-07)**: the general "single-speaker CPU inference is feasible" claim below
> turned out too optimistic for VibeVoice specifically once checked directly against the real model.
> **VibeVoice-1.5B genuinely requires a CUDA GPU — no practical CPU path exists** (confirmed against the
> model's actual requirements, not a summary). The table below is still accurate for the *other* engines
> (Piper/Kokoro's CPU speed claims are unaffected), but treat VibeVoice as GPU-only from here on. This
> doesn't break the "no persistent VPS" plan — an on-demand GPU runner for the weekly production batch
> (e.g. GitHub's `linux_4_core_gpu` runner, ~$0.052/min, NVIDIA T4) costs roughly **$13/month** at your
> volume, versus $200-720/month for an always-on GPU VPS. See `factory/docs/README-level6.md` for the
> real, built pipeline this now runs through.

## Open-source / self-hosted (CPU)

| Engine | License | CPU speed | Long-form quality | Custom voice ("Grandmaster") |
|---|---|---|---|---|
| **Piper** | **GPL-3.0-or-later** (code, since v1.3.0's move to `OHF-voice/piper1-gpl`; MIT covers v1.2.0 and earlier only). Voice models licensed separately and vary — e.g. `en_GB-cori-high` is public domain, but several popular `en_US` voices are CC BY-NC-SA (non-commercial); check per voice | Very fast — real-time on a Raspberry Pi 5, 10-30x real-time on desktop CPU | Clear/intelligible, can sound robotic on long passages — "functional," not narration-grade | ~100+ fixed voice presets, no real cloning — pick a preset, don't create a bespoke character |
| **Kokoro TTS** | Apache 2.0 (commercial-safe) | Real-time or faster on budget CPU (~150ms per 10s of text) | #1 on TTS Arena as of Jan 2026; many report it's indistinguishable from ElevenLabs casually; strong long-form quality | No built-in cloning; community add-on (KokoClone) does zero-shot cloning from a 3-10s reference sample — quality depends on the reference |
| **XTTS v2 (Coqui)** | **CPML — non-commercial only.** Coqui Inc. also shut down Jan 2024. | Needs GPU for real-time; CPU is slow | Best-in-class cloning quality among open models | Best cloning (6s sample, 17 languages) — **but licensing blocks commercial use**, reference/research only |
| **F5-TTS** | **CC-BY-NC-4.0 — non-commercial only** | GPU-oriented, CPU slow | Good quality, strong cloning | Cloning supported but same licensing block as XTTS v2 |
| **StyleTTS2** | Mostly MIT-derivative (varies by fork) | GPU-oriented; CPU path underdocumented/slower | Regarded as best prosody in open source, well suited to long-form | Fine-tuning possible, more engineering-heavy |

**Read**: Piper is fast (but GPL-3.0-or-later since v1.3.0, with per-voice model licenses to check) and sounds more "functional" than premium. Kokoro is the best fit if you
want quality and are okay with community-supported cloning — commercially usable, CPU-friendly, currently
top-rated. XTTS v2/F5-TTS have the best cloning tech but are legally off-limits for a commercial product.

## Commercial APIs

| Provider | Pricing | Voice cloning | Reputation |
|---|---|---|---|
| **ElevenLabs** | ~$0.10/1K chars (Multilingual v2) or $0.05/1K (Flash/Turbo); Creator plan $22/mo = 100K chars (~100 min) | Yes — Professional Voice Cloning, built for consistency across long scripts | Strong reputation specifically for audiobook/education narration |
| **OpenAI TTS** | tts-1 $15/1M chars, tts-1-hd $30/1M chars | **No real cloning** — 6 fixed voices only | Decent quality, can't lock a custom character voice |
| **Google Cloud TTS** | Standard/WaveNet $4/1M chars, Neural2 $16/1M, Chirp3 HD $30/1M, Instant Custom Voice $60/1M | Instant Custom Voice tier supports cloning at added cost | High quality, granular style/accent control |
| **Azure TTS** | Neural $16/1M, Neural HD $22/1M, Custom Neural $24-48/1M + training/hosting fees | Custom Neural Voice = durable trainable custom voice | Enterprise-grade, well suited to a consistent long-term character voice |

**Volume math** (3 tutor voices × ~20 min avg script × ~300 lessons): roughly 100-300+ hours of audio
total, once. At ElevenLabs rates, a 20-min lesson ≈ 20,000 chars ≈ $2; a full ~300-lesson catalog ≈ **$600
one-time**. Google/Azure land in a similar or cheaper range depending on tier.

## Pocket TTS (Kyutai Labs) — added 2026-07-17, CPU-only WITH cloning (strongest fit so far)

Released January 2026, 100M params. Code is MIT, but the **weights are CC-BY-4.0** and consent-gated — distributed on Hugging Face behind a term prohibiting voice impersonation or cloning without explicit and lawful consent. The one option found so far that combines
CPU-only inference (runs on the owner's own PC — Intel UHD, no GPU) with real zero-shot voice
cloning (20s reference sample) — Piper/Kokoro lack or only community-support cloning; VibeVoice/
Voxtral have cloning but need a GPU. Built on a new "Continuous Audio Language Models" architecture
(predicts continuous audio representations, not discrete tokens). ~200ms time-to-first-chunk, 6x
real-time — fast enough for CI batch production AND potentially fast enough for Mandy's live chat
voice later, not just pre-produced lesson narration. English-only for now (matches current need).

**If real-world quality holds up on actual tutor scripts, this could remove the GPU-tier question
entirely** — no CI GPU-runner cost, no VibeVoice/Voxtral bake-off needed, cloning works locally.
Test this FIRST, on the owner's own machine, before anything requiring a GPU runner.
Source: kyutai.org/pocket-tts-technical-report, github.com/kyutai-labs/pocket-tts.

## Voxtral TTS (Mistral AI) — added 2026-07-17, open-weight GPU option

Released March 2026, open-weight, 4B params, self-hostable (Hugging Face) or via Mistral Studio API.
Genuinely competitive with the commercial APIs above, not just the open-CPU tier:

- **Voice cloning from <5s of reference audio** — captures accent/inflection/quirks, comparable to or
  better than the self-hosted CPU options' cloning story (Piper has none, Kokoro's is community-only).
- Reported to beat ElevenLabs Flash v2.5 in human preference tests; 90ms time-to-first-audio, built for
  streaming/real-time.
- **Runs on a single 16GB VRAM GPU** — smaller footprint than expected, and importantly the SAME class
  of on-demand GitHub GPU runner already planned for VibeVoice (`linux_4_core_gpu`'s T4 has 16GB) fits
  it — no bigger/costlier instance needed, so it slots into the exact same "on-demand CI GPU, ~$13/mo at
  weekly-batch volume" architecture as VibeVoice, as an alternative model on the same infra.
- 9 languages (en/fr/de/es/nl/pt/it/hi/ar) — no confirmed en-ZA, same gap as every other option here.
- Self-hosted = no per-character cost (unlike ElevenLabs/Google/Azure); only the GPU-runner minutes.

**Worth a real bake-off** against VibeVoice on the same GPU-runner infra before committing — same
hosting cost class, but Voxtral's fast built-in cloning and reported quality edge make it a strong
contender, possibly the strongest self-hosted option once actually tested against real tutor scripts.

## Voicebox (jamiepine) — added 2026-07-20, an authoring tool, not a CI engine — untested

Not a TTS engine itself — a local-first desktop voice studio (Tauri/React/FastAPI, MIT, 43.7k
stars) that wraps and switches between 7 engines (Kokoro, LuxTTS, Qwen3-TTS, Chatterbox Turbo/
Multilingual, TADA/HumeAI, Qwen CustomVoice), plus full voice cloning from a sample or 50+ presets,
Whisper-based STT, and a timeline editor. Its own README frames it as bridging ElevenLabs (output)
and WisprFlow (input) locally, with a bundled LLM for refinement and per-profile personas.

**Real potential use, distinct from the CI question**: this doesn't need to run in production —
Level 6 is a batch CI job, Voicebox is an interactive desktop app, wrong shape for that role. But it
could be the tool a human uses ONCE to actually clone each tutor's voice (Grandmaster, Big John,
Mandy) from a reference sample, before any of the CI/production questions matter. That's a genuinely
different problem than "run this in GitHub Actions."

**The deciding question, not yet answered**: does Voicebox's cloning produce a portable voice
profile usable headlessly via the underlying engine's own CLI/API (e.g. clone in Voicebox, then run
that same Chatterbox/Qwen3-TTS voice profile in CI without the desktop app) — or is the cloned voice
locked inside the app's own UI, unusable outside it? If portable: Voicebox becomes the voice-creation
step, whichever underlying engine it wraps becomes the production engine. If locked-in: it's useful
only for prototyping/audition, not for the real pipeline. Needs a real test before either conclusion.

Also surfaces four engine names not otherwise in this doc, unresearched individually — LuxTTS,
Qwen3-TTS, Chatterbox (Turbo/Multilingual), TADA/HumeAI. Worth noting Voicebox's maintainer chose
Kokoro as one of only 7 supported engines, consistent with Kokoro already being a reasonable pick
above — not independent confirmation of the others' quality/license/CPU-GPU story, which remain
unchecked.

## Recommendation (not yet decided, for your review)

- **Near-term**: ElevenLabs Professional Voice Cloning — purpose-built for exactly this ("one consistent
  voice reading long scripts"), cheap at your actual volume, strong long-form narration reputation.
- **Later, if useful**: self-host Kokoro (Apache 2.0, free, near-top-tier quality) once cloning tooling
  matures, especially if per-lesson API cost becomes a concern at much larger scale or GPU access appears.
- **Avoid for production**: XTTS v2, F5-TTS — best cloning tech in open source, but licensing (and Coqui's
  shutdown) makes them a legal risk for a commercial ed-tech product.

## South African accent

en-ZA voices exist on Google Cloud and Azure (a handful of options, not deep/native quality). Open-source
options (Piper, Kokoro) ship mostly US/UK/generic-English voices, no confirmed SA accent model. An
authentically SA-accented tutor voice would likely need a commercial provider's custom-voice training on
real SA-accented reference audio.

## Ruled out (not a TTS tool)

**Colibri** (github.com/JustVugg/colibri) — checked directly, this is a CPU-inference engine for a large
text-generation LLM (GLM-5.2, 744B params), completely unrelated to voice synthesis. Doesn't apply here.

---
Sources: Piper TTS Setup Guide, Best Local TTS Models 2026, Kokoro TTS Complete Guide, Kokoro TTS Review
2026, Local TTS & Voice Cloning Licenses 2026, XTTS v2 Commercial License 2026, ElevenLabs Pricing 2026,
OpenAI TTS API Pricing, Azure Text-to-Speech Pricing 2026, Google Cloud Text-to-Speech Pricing, Narakeet
South African Accent TTS, ReadSpeaker South African English.
