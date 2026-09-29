# Facebook — daily opportunity Reel

`.github/workflows/facebook_daily_post.yml` runs every day at 07:00 SAST and
posts one Reel to the RokctAI Facebook Page:

1. **Pick** — one open, `VERIFIED` grant from `RokctAI/opportunities`
   (`02_grants/*.md`) that has not been posted yet, soonest-closing first
   but at least 7 days before its deadline. When grants run out it falls
   back to active tenders with a readable title (`published/api/tenders.json`).
2. **Brief + motion** — a `brief.json` in the TikTok post-folder contract and
   an animated 15 s clip (`motion.py`): the brand drops in, the amount counts
   up to its exact value, the title rises, a live days-left counter lands,
   and it closes on "Link in the description". Every fact is copied verbatim
   from the card (`.rokct/types/opportunity.*/metarules/reel_rules.md`). The
   video shows the brand name only; the link and domain go in the post
   description. Palette and background motif rotate by day so the feed does
   not read as one repeated template.
3. **Render** — `RokctAI/agent` `lms/team/scripts/tiktok_render.py` conforms
   and encodes it to a silent 1080x1920 MP4.
4. **Post** — the Graph API `video_reels` upload; the permalink and a
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
