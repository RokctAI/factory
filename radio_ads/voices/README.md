# voices/ (local only, git-ignored)

The factory clones each cast member from a short reference WAV. Nothing in
this folder is committed except this README.

`"cast": {"driver": {"voice": "tutor_008"}}` resolves to `voices/tutor_008.wav`
(and reads `voices/tutor_008.voice.json` for metadata if present).

## Fill it from the private repos

The tutor/assistant persona reference WAVs live in `RokctAI/lessons` under
`voices/samples/` (moved from RokctAI/agent in phase 2 of the repo split);
their `.voice.json` specs stay in `RokctAI/agent`:

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/RokctAI/lessons.git /tmp/lessons
git -C /tmp/lessons sparse-checkout set voices/samples
cp /tmp/lessons/voices/samples/*.wav           radio_ads/voices/
git clone --depth 1 https://github.com/RokctAI/agent.git /tmp/agent
cp /tmp/agent/lms/team/voices/*.voice.json     radio_ads/voices/
```

That gives `tutor_001` .. `tutor_012` and `assistant_001` .. `assistant_003`
(24 kHz mono, 6-11 s each). The personas' names, ages, accents and
registers are in the `.voice.json` files, which helps when casting.

These are synthetic placeholder voices (Kokoro blends converted onto an SA
accent), not recordings of real people.

## Your own voice

Any WAV works: `"cast": {"host": {"ref": "voices/ray.wav"}}`. 10-30 s of clean
speech, no music behind it (music in the reference leaks into the output),
read at the pace you want the ad read. Only clone someone's voice with their
consent.
