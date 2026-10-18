# Meta ads pipeline (dry run)

Our own Zeely-style pipeline: creative in, paused Meta campaign out, results loop decides what to keep.

- `campaign.py` - ad job JSON -> the Marketing API requests (campaign, ad set, creative, ad), written to `plan.json`. **No network code; everything PAUSED.**
- `optimise.py` - per-ad insights -> keep / pause / scale (+20%) decisions.
- Creative comes from existing pieces: posters from RokctAI/designer Template mode, reels from `radio_ads` + `social/facebook/motion.py`.

Not here yet (needs Ray's word): live sending, ad account, Pixel, Meta app review. Keys will live in Occultation (`META_AD_ACCOUNT_ID`, `META_ADS_ACCESS_TOKEN`, `META_PIXEL_ID`), never in this public repo.

```
python social/meta_ads/campaign.py social/meta_ads/examples/juvo_merchant_promo.json --out build/ads
python social/meta_ads/optimise.py social/meta_ads/examples/sample_insights.json --target-cpa 2500
```
