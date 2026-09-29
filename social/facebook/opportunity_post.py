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

"""Daily opportunity Reel for the RokctAI Facebook Page.

One run = one post:

  1. pick   - one open, VERIFIED opportunity from RokctAI/opportunities that
              has not been posted before (grant cards first, then tenders
              with a readable title), soonest-closing first but never one
              closing inside MIN_DAYS_LEFT - a viewer must have time to apply.
  2. brief  - write a brief.json in the TikTok post-folder contract
              (hook / on_screen_text / duration_seconds, silent_ok), with
              every fact copied verbatim from the card (reel_rules.md rule 5:
              no invented terms).
  3. card   - draw the 1080x1920 still the captions sit over (Pillow).
  4. render - hand the folder to RokctAI/agent's tiktok_render.py, the one
              renderer the fleet already uses, which burns the captions in
              and writes render/<id>.mp4.
  5. post   - publish the MP4 to the Page as a Reel (Graph API video_reels),
              read back its permalink, and record it in posted.json.

With no Page credentials in the environment the run is a dry run: steps
1-4 happen, nothing is published and the ledger is untouched, so the
pipeline can be proven before the Page exists.

    python social/facebook/opportunity_post.py \
        --opportunities ../opportunities --agent ../agent --out build/fb

Environment (from Occultation .env/production.env, never printed):
    FACEBOOK_PAGE_ID, FACEBOOK_PAGE_ACCESS_TOKEN
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

HERE = Path(__file__).resolve().parent
LEDGER = HERE / "posted.json"

GRAPH = "https://graph.facebook.com/v21.0"
RUPLOAD = "https://rupload.facebook.com/video-upload/v21.0"
MIN_DAYS_LEFT = 7
DURATION_SECONDS = 15
CTA = "Find more and apply at rokct.ai"
SITE = "https://rokct.ai"

W, H = 1080, 1920
INK = (14, 14, 16)
PANEL = (28, 28, 32)
YELLOW = (255, 196, 0)
WHITE = (245, 245, 245)
GREY = (160, 160, 168)


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


def pick(repo: Path, posted: set, today: dt.date):
    floor = today + dt.timedelta(days=MIN_DAYS_LEFT)
    for source in (grant_candidates, tender_candidates):
        fresh = [c for c in source(repo) if c["deadline"] >= floor and c["key"] not in posted]
        if fresh:
            return min(fresh, key=lambda c: (c["deadline"], c["key"]))
    return None


# -------------------------------------------------------------------- brief


def _nice_date(d: dt.date):
    return f"{d.day} {d.strftime('%B %Y')}"


def make_brief(opp, today: dt.date):
    stamp = today.strftime("%Y%m%d")
    closes = f"Closes {_nice_date(opp['deadline'])}"
    if opp["kind"] == "Grant":
        amount = _short_amount(opp["amount"])
        hook = amount if len(amount) <= 40 else _clip(opp["title"], 70)
        lines = [f"From {opp['organization']}", closes, CTA]
    else:
        hook = f"{opp['organization']} is taking bids"
        lines = [opp.get("region") or "South Africa", closes, CTA]
    caption = "\n".join(
        [
            hook,
            "",
            closes + ".",
            f"Apply: {opp['link']}",
            "",
            f"More funding, grants and tenders every day at {SITE}",
        ]
    )
    return {
        "id": f"fb_opportunity_{stamp}",
        "format": "text-on-screen",
        "hook": hook,
        "on_screen_text": lines,
        "caption": caption,
        "cta": CTA,
        "duration_seconds": DURATION_SECONDS,
        "source_key": opp["key"],
        # The card is drawn here, not generated, so it carries no AI
        # watermark strip for the renderer to trim away.
        "_pipeline_only": {"silent_ok": True, "watermark_trim": {"bottom": 0, "right": 0}},
    }


# --------------------------------------------------------------------- card


def _font(size, bold=True):
    from PIL import ImageFont

    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    for base in ("/usr/share/fonts/truetype/dejavu", "/usr/share/fonts/dejavu"):
        if Path(base, name).exists():
            return ImageFont.truetype(str(Path(base, name)), size)
    return ImageFont.load_default()


def _wrap(draw, text, font, width):
    words, lines, line = text.split(), [], ""
    for word in words:
        trial = f"{line} {word}".strip()
        if draw.textlength(trial, font=font) <= width or not line:
            line = trial
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def _wrap_max(draw, text, font, width, max_lines):
    """Wrap, and mark a cut with '...' so a clipped figure never reads whole."""
    lines = _wrap(draw, text, font, width)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1].rstrip(" ,-") + "..."
    return lines


def make_card(opp, path: Path):
    """The still behind the captions. The renderer burns the hook in at
    ~14% height (first 3s only) and the on-screen lines at ~66%, so the
    card keeps its facts in the band between them and its brand mark at
    the foot."""
    from PIL import Image, ImageDraw

    img = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(img)
    for y in range(H):  # soft vertical fade so the slow zoom has texture
        shade = int(8 * y / H)
        d.line([(0, y), (W, y)], fill=(INK[0] + shade, INK[1] + shade, INK[2] + shade + 2))

    margin, inner = 110, W - 2 * 110 - 20
    kind_f, head_f, title_f, date_f = _font(40), _font(72), _font(42, bold=False), _font(46)
    headline = _short_amount(opp["amount"]) if opp["amount"] else opp["organization"]
    head_lines = _wrap_max(d, headline, head_f, inner, 3)
    title_lines = _wrap_max(d, opp["title"], title_f, inner, 4)
    height = 50 + 70 + len(head_lines) * 88 + 24 + len(title_lines) * 56 + 30 + 60 + 40
    top = int(H * 0.26)
    bottom = top + height
    d.rounded_rectangle([margin - 30, top, W - margin + 30, bottom], radius=36, fill=PANEL)
    d.rectangle([margin - 30, top, margin - 18, bottom], fill=YELLOW)

    y = top + 50
    d.text((margin + 10, y), opp["kind"].upper(), font=kind_f, fill=YELLOW)
    y += 70
    for line in head_lines:
        d.text((margin + 10, y), line, font=head_f, fill=WHITE)
        y += 88
    y += 24
    for line in title_lines:
        d.text((margin + 10, y), line, font=title_f, fill=GREY)
        y += 56
    y += 30
    d.text((margin + 10, y), f"Closes {_nice_date(opp['deadline'])}", font=date_f, fill=YELLOW)

    mark = "rokct.ai"
    f = _font(64)
    d.text(((W - d.textlength(mark, font=f)) / 2, int(H * 0.86)), mark, font=f, fill=YELLOW)
    img.save(path)


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
    args = ap.parse_args(argv)

    ledger = json.loads(LEDGER.read_text(encoding="utf-8")) if LEDGER.exists() else []
    opp = pick(args.opportunities, {row["source_key"] for row in ledger}, args.today)
    if not opp:
        print("No unposted open opportunity with enough time left - nothing to post today.")
        return 0

    brief = make_brief(opp, args.today)
    folder = args.out / brief["id"]
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "brief.json").write_text(json.dumps(brief, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    make_card(opp, folder / "card.png")
    mp4 = render(folder, args.agent.resolve())
    print(f"Picked {opp['key']} (closes {opp['deadline']}); rendered {mp4}")

    page_id = os.environ.get("FACEBOOK_PAGE_ID", "").strip()
    token = os.environ.get("FACEBOOK_PAGE_ACCESS_TOKEN", "").strip()
    summary = [f"### Facebook opportunity post {args.today}", f"- Opportunity: {opp['title']} ({opp['key']})"]
    if args.dry_run or not (page_id and token):
        why = "--dry-run" if args.dry_run else "FACEBOOK_PAGE_ID / FACEBOOK_PAGE_ACCESS_TOKEN not set"
        print(f"Dry run ({why}): not published.")
        summary.append(f"- Dry run ({why}); the rendered MP4 is in the run artifacts.")
    else:
        video_id, permalink = publish_reel(page_id, token, mp4, brief["caption"])
        ledger.append(
            {
                "date": args.today.isoformat(),
                "source_key": opp["key"],
                "video_id": video_id,
                "permalink": permalink,
            }
        )
        LEDGER.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Published: {permalink}")
        summary += [f"- Post: {permalink}", f"- Share to your profile: {share_link(permalink)}"]

    step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if step_summary:
        with open(step_summary, "a", encoding="utf-8") as fh:
            fh.write("\n".join(summary) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
