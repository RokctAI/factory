# inbox/

Commit an ad JSON here and push: the "Radio ads" GitHub Actions workflow
validates it, renders it and attaches `radio-ad-<id>` (MP3, WAV,
report.json) to the run. See "Render in CI" in [`../README.md`](../README.md).

Locally, `python make_ad.py --watch inbox/` renders whatever lands here.
