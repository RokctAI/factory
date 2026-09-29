# Facebook — daily opportunity Reel

`.github/workflows/facebook_daily_post.yml` runs every day at 07:00 SAST and
posts one Reel to the RokctAI Facebook Page:

1. **Pick** — one open, `VERIFIED` grant from `RokctAI/opportunities`
   (`02_grants/*.md`) that has not been posted yet, soonest-closing first
   but at least 7 days before its deadline, whose Funding Amount leads with
   a real currency figure (a percentage, "Unspecified" or "Varies" is skipped). When grants run out it falls
   back to active tenders with a readable title (`published/api/tenders.json`).
2. **Brief + motion** — a `brief.json` in the TikTok post-folder contract and
   an animated 15 s clip (`motion.py`): the brand drops in, the amount counts
   up to its exact value, the title rises, a live days-left counter lands,
   and it closes on "Link in the comments". Every fact is copied verbatim
   from the card (`.rokct/types/opportunity.*/metarules/reel_rules.md`). The
   video shows the ROKCT brand mark only; the link and domain go in the
   first comment. The background motif rotates by day so the feed does not
   read as one repeated template.
3. **Sound** — `music.py` synthesises a royalty-free track (rotating key,
   tempo and progression) and lays three shared voice lines over it with the
   music ducked: `assets/voice_brand.wav` (a man's voice saying "ROKCT", from
   `radio_ads/inbox/facebook_reel_brand_15.json`) on the first beat,
   `assets/voice_open.wav` ("Need funding? Here's one you can
   apply for right now.", from `radio_ads/inbox/facebook_reel_open_15.json`)
   straight after it, and `assets/voice_close.wav` ("Follow Rocket for more
   funding opportunities every day.", from
   `radio_ads/inbox/facebook_reel_follow_15.json`) over the close.
4. **Render** — `RokctAI/agent` `lms/team/scripts/tiktok_render.py` conforms
   the clip and mixes the audio into a 12 s 1080x1920 MP4.
5. **Post** — the Graph API `video_reels` upload, the apply link as the
   first comment; the permalink and a
   one-tap share link land in the run summary, and the post is recorded in
   `posted.json` so it is never repeated.

The rendered MP4 is kept as the run's `facebook-reel` artifact.

## Setup (once)

Until both keys are set every run is a **dry run**: it renders the video and
publishes nothing.

1. Create the Facebook Page.
2. At developers.facebook.com create a Business app, add **Facebook Login for
   Business**, and request `pages_show_list`, `pages_read_engagement` and
   `pages_manage_posts` (App Review + business verification to go live).
3. Generate a long-lived **Page** access token for the Page.
4. Add both keys to Occultation `.env/production.env`, **below** the
   `##########END_FLUTTER##########` marker:

   ```text
   FACEBOOK_PAGE_ID=
   FACEBOOK_PAGE_ACCESS_TOKEN=
   ```

## Run locally

```bash
pip install pillow requests   # plus ffmpeg and DejaVu fonts
python social/facebook/opportunity_post.py \
    --opportunities ../opportunities --agent ../agent --out build/facebook --dry-run
```
