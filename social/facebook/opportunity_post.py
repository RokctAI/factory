#!/usr/bin/env python3
# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""Daily opportunity Reel for the RokctAI Facebook Page, TikTok and YouTube.

One run = one opportunity, posted to every platform whose keys are set:

  1. pick   - one open, VERIFIED opportunity from RokctAI/opportunities that
              has not been posted before (grant cards first, then tenders
              with a readable title), soonest-closing first but never one
              closing inside MIN_DAYS_LEFT - a viewer must have time to apply.
  2. brief  - write a brief.json in the TikTok post-folder contract
              (duration_seconds, silent_ok) plus the post description,
              every fact copied verbatim from the card (reel_rules.md rule 5:
              no invented terms).
  3. motion - animate the 1080x1920 clip (motion.py): brand mark, count-up
              figure from frame one, title, live days-left counter, "link in
              the comments" close, all on the beat of a track synthesised by
              music.py (royalty-free by construction). Brand name only; the
              link and domain go in the post's first comment.
  4. render - hand the folder to RokctAI/agent's tiktok_render.py, the one
              renderer the fleet already uses, which conforms the clip and
              mixes the music in, writing render/<id>.mp4.
  5. post   - publish the MP4 to the Page as a Reel (Graph API video_reels),
              add the apply link as the first comment, read back the
              permalink. TikTok and YouTube Shorts get a second cut that
              closes on "Link in bio" (neither makes links in comments
              clickable) with the apply link in the caption (tiktok.py,
              youtube.py). Every post is recorded in posted.json.

A platform whose keys are missing is skipped; with none set the run is a
dry run: steps 1-4 happen, nothing is published and the ledger is
untouched, so the pipeline can be proven before the accounts exist. One
platform failing does not stop the others.

    python social/facebook/opportunity_post.py \
        --opportunities ../opportunities --agent ../agent --out build/fb

Environment (from Occultation .env/production.env, never printed):
    FACEBOOK_PAGE_ID, FACEBOOK_PAGE_ACCESS_TOKEN
    TIKTOK_CLIENT_KEY, TIKTOK_CLIENT_SECRET, TIKTOK_REFRESH_TOKEN
    YOUTUBE_CLIENT_ID, YOUTUBE_CLIENT_SECRET, YOUTUBE_REFRESH_TOKEN
"""

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))

HERE = Path(__file__).resolve().parent
LEDGER = HERE / "posted.json"

GRAPH = "https://graph.facebook.com/v21.0"
RUPLOAD = "https://rupload.facebook.com/video-upload/v21.0"
MIN_DAYS_LEFT = 7
DURATION_SECONDS = 12
SITE = "https://rokct.ai"
HASHTAGS = "#funding #grants #tenders #business #ROKCT"
FACEBOOK_KEYS = ("FACEBOOK_PAGE_ID", "FACEBOOK_PAGE_ACCESS_TOKEN")
TIPS = HERE / "tips.json"
STREAMS = ("grant", "tender", "spotlight")
KIND_SEED = {"Grant": 0, "Tender": 1, "Investor": 2, "Funding tip": 2}



# --------------------------------------------------------------------- pick


def _field(text, name):
    m = re.search(rf"\*\*{re.escape(name)}\*\*:\s*(.+)", text)
    return m.group(1).strip() if m else ""


def _date(value):
    try:
        return dt.date.fromisoformat(str(value).strip()[:10])
    except ValueError:
        return None


def _clip(text, limit):
    return text if len(text) <= limit else text[: limit - 3].rstrip(" ,-") + "..."


def _short_amount(amount):
    """The headline figure: first clause of the card's Funding Amount,
    verbatim - '(…)' asides and '; …' tails are dropped, nothing reworded."""
    return _clip(re.split(r"[;(]", amount)[0].strip().rstrip(","), 60)


_FIRST_NUMBER = re.compile(r"\d[\d,.\s]*\d|\d")
_CURRENCY_BEFORE = re.compile(r"([$€£₹¥]|\b(?:USD|EUR|GBP|AUD|CAD|NZD|CHF|HUF|ZAR|INR|TL|R|Rs\.?|CA\$|US\$|A\$))\s?$")
_CURRENCY_AFTER = re.compile(r"^\s?(?:million|billion|m|bn|k)?\s?(?:USD|EUR|GBP|AUD|CAD|CHF|HUF|ZAR|INR|TL|euros?|dollars?|pounds?|rand|lakhs?|crores?)\b", re.I)


def money_headline(amount):
    """The headline figure, or None when the card's Funding Amount does not
    lead with real money. The first number in the headline clause must be a
    currency amount - '$25,000', 'CHF 25,000', '€12 million', '₹10 lakhs' -
    because that is the number the video counts up and shouts; a percentage
    ('up to 50% of approved project budget'), 'Unspecified' or 'Varies' is
    not a hook, so that grant is skipped rather than posted weakly."""
    head = _short_amount(amount)
    m = _FIRST_NUMBER.search(head)
    if not m:
        return None
    after = head[m.end():]
    if after.lstrip().startswith("%"):
        return None
    if _CURRENCY_BEFORE.search(head[: m.start()]) or _CURRENCY_AFTER.match(after):
        return head
    return None


# ISO codes -> the symbol a viewer reads. Codes with no symbol of their own
# (CHF, HUF) stay as written. A$ / CA$ / NZ$ keep other dollars apart from USD.
_SYMBOLS = [
    (r"\b(?:USD|US\$)\s?\$?\s?", "$"),
    (r"\b(?:AUD|A\$)\s?\$?\s?", "A$"),
    (r"\b(?:CAD|CA\$)\s?\$?\s?", "CA$"),
    (r"\b(?:NZD|NZ\$)\s?\$?\s?", "NZ$"),
    (r"\bEUR\s?", "€"),
    (r"\bGBP\s?", "£"),
    (r"\bZAR\s?", "R"),
    (r"\b(?:INR|Rs\.?)\s?", "₹"),
    (r"\bJPY\s?", "¥"),
]
_AMOUNT_WORD_AFTER = re.compile(
    r"(\d[\d,.]*(?:\s?(?:million|billion|m|bn|k))?)\s?(?:euros?)\b", re.I
)
_TL_AFTER = re.compile(r"(\d[\d,.]*(?:\s?(?:million|billion))?)\s?TL\b")


def pretty_money(text):
    """'USD 50,000 to USD 200,000' -> '$50,000 to $200,000'."""
    for code, sym in _SYMBOLS:
        text = re.sub(code + r"(?=\d)", sym, text)
    text = _AMOUNT_WORD_AFTER.sub(lambda m: "€" + m.group(1), text)
    text = _TL_AFTER.sub(lambda m: "₺" + m.group(1), text)
    text = re.sub(r"(\d)\.00\b", r"\1", text)  # "€2,000,000.00" -> "€2,000,000"
    # "AUD $1 million to $5 million": the second dollar is Australian too.
    m = re.search(r"\b(A|CA|NZ)\$", text)
    if m:
        text = re.sub(r"(?<![A-Z])\$", m.group(1) + "$", text)
    return text


def grant_candidates(repo: Path):
    for path in sorted((repo / "02_grants").glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        if _field(text, "Verification Status") != "VERIFIED":
            continue
        deadline = _date(_field(text, "Deadline"))
        amount = _field(text, "Funding Amount")
        link = _field(text, "Applying Link")
        title = re.sub(r"^#\s*Grant Opportunity:\s*", "", text.splitlines()[0]).strip()
        if not (deadline and amount and link and title) or "[" in amount:
            continue
        if not money_headline(amount):
            continue
        yield {
            "key": f"grant:{path.stem}",
            "kind": "Grant",
            "title": title,
            "organization": _field(text, "Organization"),
            "amount": amount,
            "deadline": deadline,
            "link": link,
        }


_CODEY = re.compile(r"^(Opportunity Nr \d+|[A-Z0-9/\-]+)$")


def tender_candidates(repo: Path):
    api = repo / "published" / "api" / "tenders.json"
    if not api.exists():
        return
    for row in json.loads(api.read_text(encoding="utf-8")):
        title = re.sub(r"^Tender Opportunity:\s*", "", row.get("title") or "")
        title = re.sub(r"\s*\(pdf\)\s*$", "", title).strip()
        # A tender number is not a hook - only post tenders a person can read.
        if _CODEY.match(title) or len(title.split()) < 4:
            continue
        deadline = _date(row.get("closing_date"))
        link = row.get("direct_link") or row.get("tender_documents") or ""
        if row.get("status") != "ACTIVE" or not deadline or not link.startswith("http"):
            continue
        yield {
            "key": f"tender:{row.get('slug') or row.get('tender_number')}",
            "kind": "Tender",
            "title": title,
            "organization": row.get("institution") or "",
            "amount": "",
            "region": ", ".join(x for x in (row.get("province"), "South Africa") if x),
            "deadline": deadline,
            "link": link,
        }


def equity_candidates(repo: Path):
    """Investors never close, so they are the evergreen stream."""
    for path in sorted((repo / "01_equity").glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        if _field(text, "Status") != "ACTIVE" or _field(text, "Verification Status") != "VERIFIED":
            continue
        org = _field(text, "Organization")
        stage = _field(text, "Funding Type")
        industry = _field(text, "Industry")
        site = _field(text, "Website")
        if not (org and stage and industry and site.startswith("http")):
            continue
        territory = _field(text, "Territory") or _field(text, "Country")
        yield {
            "key": f"equity:{path.stem}",
            "kind": "Investor",
            "title": f"Invests in {industry}",
            "organization": org,
            "stage": stage,
            "industry": industry,
            "territory": territory,
            "funder_type": _field(text, "Funder Type"),
            "deadline": None,
            "link": site,
        }


def tip_candidates():
    for tip in json.loads(TIPS.read_text(encoding="utf-8")):
        yield {
            "key": f"tip:{tip['id']}",
            "kind": "Funding tip",
            "title": tip["body"],
            "heading": tip["heading"],
            "organization": "",
            "deadline": None,
            "link": SITE,
        }


def pick(repo: Path, posted: set, today: dt.date, stream="grant", ledger=()):
    """One post for the stream:
    grant     - soonest-closing open grant; investors once grants run out
    tender    - soonest-closing open tender
    spotlight - an investor on odd days, a funding tip on even days
    """
    floor = today + dt.timedelta(days=MIN_DAYS_LEFT)

    def dated(source):
        fresh = [c for c in source(repo) if c["deadline"] >= floor and c["key"] not in posted]
        return min(fresh, key=lambda c: (c["deadline"], c["key"])) if fresh else None

    def investor():
        return next((c for c in equity_candidates(repo) if c["key"] not in posted), None)

    def tip():
        tips = list(tip_candidates())
        fresh = [c for c in tips if c["key"] not in posted]
        if fresh:
            return fresh[0]
        # All used: start the round again from the one posted longest ago.
        last = {row["source_key"]: row["date"] for row in ledger}
        return min(tips, key=lambda c: last.get(c["key"], ""))

    if stream == "grant":
        return dated(grant_candidates) or investor()
    if stream == "tender":
        return dated(tender_candidates)
    if stream == "spotlight":
        return (investor() or tip()) if today.toordinal() % 2 else tip()
    raise ValueError(f"unknown stream {stream!r}")


# -------------------------------------------------------------------- brief


def _nice_date(d: dt.date):
    return f"{d.day} {d.strftime('%B %Y')}"


def headline_for(opp):
    if opp["kind"] == "Grant":
        return pretty_money(money_headline(opp["amount"]))
    if opp["kind"] == "Investor":
        return opp["organization"]
    if opp["kind"] == "Funding tip":
        return opp["heading"]
    return f"{opp['organization']} is taking bids"


# Viewers land on the opportunity's own rokct.ai page, never straight on the
# funder's apply link (Ray, 2026-09-29). The path is the one rokctai_frontend's
# opportunity search links to: /opportunities/<tenders|grants|equity>/<slug>,
# where the slug is the card's file stem (grants, equity) or the tender slug.
PAGE_SECTION = {"grant": "grants", "tender": "tenders", "equity": "equity"}


def page_url(opp):
    kind, _, slug = opp["key"].partition(":")
    section = PAGE_SECTION.get(kind)
    if not section:
        return SITE
    return f"{SITE}/opportunities/{section}/{urllib.parse.quote(slug, safe='')}"


def _post_text(opp):
    """(caption lead, closing line, first comment, caption link line) per kind."""
    more = f"More funding, grants and tenders every day: {SITE}"
    page = page_url(opp)
    if opp["kind"] == "Investor":
        lead = f"{opp['organization']} invests in {opp['industry']} ({opp['stage']}), {opp['territory']}."
        return lead, "No deadline: pitch any time.", f"Details: {page}\n{more}", f"Details: {page}"
    if opp["kind"] == "Funding tip":
        lead = f"Funding tip: {opp['heading']}\n\n{opp['title']}"
        return lead, "Follow ROKCT for more funding opportunities every day.", more, ""
    closes = f"Closes {_nice_date(opp['deadline'])}."
    lead = f"{headline_for(opp)} - {opp['title']}"
    return lead, closes, f"How to apply: {page}\n{more}", f"How to apply: {page}"


def make_brief(opp, today: dt.date, stream="grant"):
    """The post spec. All on-screen text is drawn by motion.py, so the
    brief carries no hook or overlay lines for the renderer to burn in."""
    stamp = today.strftime("%Y%m%d")
    lead, closing, comment, bio_link = _post_text(opp)
    link_line = "Link in the comments." if opp["kind"] != "Funding tip" else "More in the comments."
    caption = "\n".join([lead, "", closing, link_line])
    # TikTok / YouTube: no clickable links in comments, so the link rides in
    # the caption (copyable) and the video points at the profile link.
    bio_caption = "\n".join(
        [lead, "", closing] + ([bio_link] if bio_link else []) + ["Link in bio for more every day.", "", HASHTAGS]
    )
    return {
        "id": f"{stream}_{stamp}",
        "format": "text-on-screen",
        "hook": "",
        "on_screen_text": [],
        "caption": caption,
        "first_comment": comment,
        "bio_caption": bio_caption,
        "short_title": f"{_clip(headline_for(opp) + ' - ' + opp['title'], 88)} #Shorts",
        "duration_seconds": DURATION_SECONDS,
        "source_key": opp["key"],
        "_pipeline_only": {"silent_ok": True},
    }


# ------------------------------------------------------------------- motion


def scene_facts(opp, today: dt.date):
    """What the clip shows beyond the headline: deadline or panel, and who."""
    shown = dict(opp)
    days_left = 0
    if opp["deadline"]:
        shown["deadline_text"] = _nice_date(opp["deadline"])
        days_left = (opp["deadline"] - today).days
    if opp["kind"] == "Grant":
        shown["who"] = f"From {opp['organization']}"
    elif opp["kind"] == "Investor":
        shown["panel"] = (opp["stage"], f"{opp['territory']} - no deadline, pitch any time")
        shown["who"] = opp.get("funder_type") or ""
    elif opp["kind"] == "Funding tip":
        shown["panel"] = ("Save this", "for your next application")
        shown["who"] = ""
    else:
        shown["who"] = opp.get("region") or "South Africa"
    return shown, days_left


def make_motion(opp, today: dt.date, folder: Path, close_line=None):
    """The visual (motion.mp4) and its soundtrack (music.wav), side by side
    in the post folder - the renderer takes them as the visual and audio."""
    from motion import CLOSE_LINE, render_motion
    from music import add_voiceover, render_music, tempo_for

    # Each of the day's slots gets its own track and motif.
    seed = today.toordinal() + 1000 * KIND_SEED.get(opp["kind"], 0)
    shown, days_left = scene_facts(opp, today)
    render_music(seed, DURATION_SECONDS, folder / "music.wav")
    # "Here's one you can apply for" does not fit a tip.
    add_voiceover(folder / "music.wav", DURATION_SECONDS, opener=opp["kind"] != "Funding tip")
    render_motion(
        shown, headline_for(opp), days_left, seed, DURATION_SECONDS, tempo_for(seed), folder / "motion.mp4",
        close_line or CLOSE_LINE,
    )


# ------------------------------------------------------------------- render


def render(folder: Path, agent: Path):
    script = agent / "lms" / "team" / "scripts" / "tiktok_render.py"
    subprocess.run(
        [sys.executable, str(script), str(folder.resolve()), "--force"],
        cwd=agent,
        check=True,
    )
    brief = json.loads((folder / "brief.json").read_text(encoding="utf-8"))
    mp4 = folder / "render" / f"{brief['id']}.mp4"
    if not mp4.exists():
        sys.exit(f"render finished but {mp4} is missing")
    return mp4


# --------------------------------------------------------------------- post


def _check(resp, what):
    try:
        body = resp.json()
    except ValueError:
        body = {"raw": resp.text[:300]}
    if resp.status_code >= 400 or "error" in body:
        err = body.get("error", body)
        msg = err.get("message") if isinstance(err, dict) else err
        sys.exit(f"Facebook {what} failed ({resp.status_code}): {msg}")
    return body


def publish_reel(page_id, token, mp4: Path, description):
    start = _check(
        requests.post(
            f"{GRAPH}/{page_id}/video_reels",
            data={"upload_phase": "start", "access_token": token},
            timeout=60,
        ),
        "reel start",
    )
    video_id = start["video_id"]
    data = mp4.read_bytes()
    _check(
        requests.post(
            f"{RUPLOAD}/{video_id}",
            headers={
                "Authorization": f"OAuth {token}",
                "offset": "0",
                "file_size": str(len(data)),
            },
            data=data,
            timeout=300,
        ),
        "reel upload",
    )
    _check(
        requests.post(
            f"{GRAPH}/{page_id}/video_reels",
            data={
                "upload_phase": "finish",
                "video_id": video_id,
                "video_state": "PUBLISHED",
                "description": description,
                "access_token": token,
            },
            timeout=60,
        ),
        "reel publish",
    )
    permalink = ""
    for _ in range(30):  # processing takes a little while before a link exists
        info = _check(
            requests.get(
                f"{GRAPH}/{video_id}",
                params={"fields": "permalink_url,status", "access_token": token},
                timeout=60,
            ),
            "reel status",
        )
        phase = (info.get("status") or {}).get("video_status")
        if phase == "error":
            sys.exit(f"Facebook rejected the reel while processing: {info.get('status')}")
        permalink = info.get("permalink_url") or ""
        if permalink and phase in (None, "ready", "published"):
            break
        time.sleep(10)
    if permalink.startswith("/"):
        permalink = "https://www.facebook.com" + permalink
    return video_id, permalink or f"https://www.facebook.com/reel/{video_id}"


def post_comment(object_id, token, message):
    """The apply link rides in the first comment, not in the video."""
    return _check(
        requests.post(
            f"{GRAPH}/{object_id}/comments",
            data={"message": message, "access_token": token},
            timeout=60,
        ),
        "first comment",
    ).get("id")


def _keys(names):
    """The named env values, or None when any is missing."""
    env = {n: os.environ.get(n, "").strip() for n in names}
    return env if all(env.values()) else None


def share_link(url):
    return "https://www.facebook.com/sharer/sharer.php?u=" + urllib.parse.quote(url, safe="")


# --------------------------------------------------------------------- main


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--opportunities", type=Path, required=True, help="RokctAI/opportunities checkout")
    ap.add_argument("--agent", type=Path, required=True, help="RokctAI/agent checkout (renderer)")
    ap.add_argument("--out", type=Path, default=Path("build/facebook"))
    ap.add_argument("--today", type=dt.date.fromisoformat, default=dt.date.today())
    ap.add_argument("--dry-run", action="store_true", help="render only, never publish")
    ap.add_argument("--stream", choices=STREAMS, default="grant", help="which daily slot this run fills")
    args = ap.parse_args(argv)

    ledger = json.loads(LEDGER.read_text(encoding="utf-8")) if LEDGER.exists() else []
    opp = pick(args.opportunities, {row["source_key"] for row in ledger}, args.today, args.stream, ledger)
    if not opp:
        print(f"No unposted {args.stream} with enough time left - nothing to post in this slot.")
        return 0

    brief = make_brief(opp, args.today, args.stream)
    folder = args.out / brief["id"]
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "brief.json").write_text(json.dumps(brief, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    make_motion(opp, args.today, folder)
    mp4 = render(folder, args.agent.resolve())
    print(f"Picked {opp['key']} (closes {opp['deadline'] or 'never'}); rendered {mp4}")

    import tiktok
    import youtube
    from motion import CLOSE_LINE_BIO

    # The TikTok / YouTube cut: same clip and track, closing on "Link in bio".
    bio_brief = dict(brief, id=brief["id"] + "_bio")
    bio_folder = args.out / bio_brief["id"]
    bio_folder.mkdir(parents=True, exist_ok=True)
    (bio_folder / "brief.json").write_text(json.dumps(bio_brief, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    make_motion(opp, args.today, bio_folder, CLOSE_LINE_BIO)
    bio_mp4 = render(bio_folder, args.agent.resolve())

    summary = [f"### Daily {args.stream} post {args.today}", f"- Post: {headline_for(opp)} ({opp['key']})"]
    platforms = {
        "facebook": _keys(FACEBOOK_KEYS),
        "tiktok": _keys(tiktok.KEYS),
        "youtube": _keys(youtube.KEYS),
    }
    row = {"date": args.today.isoformat(), "stream": args.stream, "source_key": opp["key"]}
    failed = []
    for name, env in platforms.items():
        if args.dry_run or not env:
            why = "--dry-run" if args.dry_run else "keys not set"
            print(f"{name}: skipped ({why}).")
            summary.append(f"- {name}: skipped ({why}).")
            continue
        try:
            if name == "facebook":
                video_id, permalink = publish_reel(
                    env["FACEBOOK_PAGE_ID"], env["FACEBOOK_PAGE_ACCESS_TOKEN"], mp4, brief["caption"]
                )
                # Recorded before the comment so a failed comment never re-posts.
                row.update(video_id=video_id, permalink=permalink)
                summary += [f"- facebook: {permalink}", f"- Share to your profile: {share_link(permalink)}"]
                post_comment(video_id, env["FACEBOOK_PAGE_ACCESS_TOKEN"], brief["first_comment"])
            elif name == "tiktok":
                publish_id, post_id, privacy = tiktok.publish(env, bio_mp4, brief["bio_caption"])
                row.update(tiktok_publish_id=publish_id, tiktok_post_id=post_id)
                summary.append(f"- tiktok: published ({privacy}) {post_id or publish_id}")
            else:
                video_id, url, privacy = youtube.publish(env, bio_mp4, brief["short_title"], brief["bio_caption"])
                row.update(youtube_id=video_id, youtube_url=url)
                summary.append(f"- youtube: {url} ({privacy})")
            print(f"{name}: published.")
        except (SystemExit, requests.RequestException) as exc:  # one platform down must not stop the rest
            failed.append(name)
            print(f"::error::{name}: {exc}")
            summary.append(f"- {name}: FAILED - {exc}")

    if len(row) > 3:
        ledger.append(row)
        LEDGER.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if step_summary:
        with open(step_summary, "a", encoding="utf-8") as fh:
            fh.write("\n".join(summary) + "\n")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
