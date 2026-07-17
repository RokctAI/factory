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
| **Piper** | MIT (commercial-safe) | Very fast — real-time on a Raspberry Pi 5, 10-30x real-time on desktop CPU | Clear/intelligible, can sound robotic on long passages — "functional," not narration-grade | ~100+ fixed voice presets, no real cloning — pick a preset, don't create a bespoke character |
| **Kokoro TTS** | Apache 2.0 (commercial-safe) | Real-time or faster on budget CPU (~150ms per 10s of text) | #1 on TTS Arena as of Jan 2026; many report it's indistinguishable from ElevenLabs casually; strong long-form quality | No built-in cloning; community add-on (KokoClone) does zero-shot cloning from a 3-10s reference sample — quality depends on the reference |
| **XTTS v2 (Coqui)** | **CPML — non-commercial only.** Coqui Inc. also shut down Jan 2024. | Needs GPU for real-time; CPU is slow | Best-in-class cloning quality among open models | Best cloning (6s sample, 17 languages) — **but licensing blocks commercial use**, reference/research only |
| **F5-TTS** | **CC-BY-NC-4.0 — non-commercial only** | GPU-oriented, CPU slow | Good quality, strong cloning | Cloning supported but same licensing block as XTTS v2 |
| **StyleTTS2** | Mostly MIT-derivative (varies by fork) | GPU-oriented; CPU path underdocumented/slower | Regarded as best prosody in open source, well suited to long-form | Fine-tuning possible, more engineering-heavy |

**Read**: Piper is safe and fast but sounds more "functional" than premium. Kokoro is the best fit if you
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
