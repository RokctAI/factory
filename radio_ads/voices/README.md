# voices/ (local only, git-ignored)

The factory clones each cast member from a short reference WAV. Nothing in
this folder is committed except this README.

`"cast": {"driver": {"voice": "tutor_008"}}` resolves to `voices/tutor_008.wav`
(and reads `voices/tutor_008.voice.json` for metadata if present).

## Fill it from the agent repo

The tutor/assistant persona voices live in `RokctAI/agent` on branch
`claude/voice-render-pipeline-qk3n8v` (PR #319):

```bash
git clone --depth 1 -b claude/voice-render-pipeline-qk3n8v https://github.com/RokctAI/agent.git /tmp/agent
cp /tmp/agent/lms/team/voices/samples/*.wav   radio_ads/voices/
cp /tmp/agent/lms/team/voices/*.voice.json    radio_ads/voices/
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
