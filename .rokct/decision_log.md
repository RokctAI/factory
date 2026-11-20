# Technical Decision Log

Engineering decisions for the factory engine that aren't inferable from the code alone. Newest first.

## 2026-11-20: LTX-Video, not Wan 2.2 5B, for CPU drama shots
- **Decision:** For no-GPU microdrama/TV-ad shots, use LTX-Video 2B distilled (v0.9.8) in bf16 via diffusers.
- **Reason:** On the 4-core sandbox LTX makes a 4 s 480x832 shot in about 6-7 min. Wan 2.2 TI2V 5B (ComfyUI, GGUF Q8) took 61 min for 2 s, even with bf16.
- **Note:** Seedance 2.0 has no open weights (API only), so it cannot run on our machines.

