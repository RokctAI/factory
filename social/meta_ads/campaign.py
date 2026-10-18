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


"""Meta (Facebook/Instagram) ad campaign builder - DRY RUN ONLY.

Turns an ad job JSON (examples/) into the exact Marketing API requests that
would create a campaign, ad set, creative and ad, and writes them to
<out>/<job id>/plan.json. Nothing is sent: this module has no network code.
Live sending is a later step that needs Ray's word, a verified Business,
an ad account and Meta app review (ads_management).

Every object is built with status PAUSED, so even a future live send
creates nothing that spends until a human switches it on.

    python social/meta_ads/campaign.py examples/juvo_merchant_promo.json --out build/ads
"""

import argparse
import json
import sys
from pathlib import Path

GRAPH_VERSION = "v21.0"
OBJECTIVES = {"traffic": "OUTCOME_TRAFFIC", "leads": "OUTCOME_LEADS",
              "sales": "OUTCOME_SALES", "awareness": "OUTCOME_AWARENESS"}
OPTIMISATION = {"traffic": "LINK_CLICKS", "leads": "LEAD_GENERATION",
                "sales": "OFFSITE_CONVERSIONS", "awareness": "REACH"}
CTAS = {"SHOP_NOW", "LEARN_MORE", "SIGN_UP", "ORDER_NOW", "CONTACT_US", "APPLY_NOW"}
REQUIRED = ("id", "objective", "daily_budget_minor", "currency", "link",
            "headline", "primary_text", "targeting")


class JobError(ValueError):
    pass


def validate(job):
    missing = [k for k in REQUIRED if not job.get(k)]
    if missing:
        raise JobError(f"missing: {', '.join(missing)}")
    if job["objective"] not in OBJECTIVES:
        raise JobError(f"objective must be one of {sorted(OBJECTIVES)}")
    if not isinstance(job["daily_budget_minor"], int) or job["daily_budget_minor"] <= 0:
        raise JobError("daily_budget_minor must be a positive integer (cents)")
    if not job["link"].startswith("https://"):
        raise JobError("link must be https")
    cta = job.get("cta", "LEARN_MORE")
    if cta not in CTAS:
        raise JobError(f"cta must be one of {sorted(CTAS)}")
    if not (job.get("image") or job.get("video")):
        raise JobError("need image (designer poster) or video (reel render)")
    t = job["targeting"]
    if not t.get("countries"):
        raise JobError("targeting.countries required")


def targeting_spec(t):
    spec = {"geo_locations": {"countries": t["countries"]},
            "age_min": t.get("age_min", 18), "age_max": t.get("age_max", 65)}
    if t.get("cities"):
        spec["geo_locations"]["cities"] = [
            {"key": c["key"], "radius": c.get("radius_km", 10), "distance_unit": "kilometer"}
            for c in t["cities"]]
    if t.get("interests"):
        spec["flexible_spec"] = [{"interests": [{"id": i} for i in t["interests"]]}]
    return spec


def build_plan(job, ad_account="act_<AD_ACCOUNT_ID>", page_id="<PAGE_ID>"):
    """Return the ordered list of Marketing API requests for one job."""
    validate(job)
    base = f"/{GRAPH_VERSION}/{ad_account}"
    name = job["id"]
    creative_media = ({"video_data": {"video_id": "<UPLOADED_VIDEO_ID>",
                                      "title": job["headline"], "message": job["primary_text"],
                                      "call_to_action": {"type": job.get("cta", "LEARN_MORE"),
                                                         "value": {"link": job["link"]}}}}
                      if job.get("video") else
                      {"link_data": {"image_hash": "<UPLOADED_IMAGE_HASH>", "link": job["link"],
                                     "name": job["headline"], "message": job["primary_text"],
                                     "call_to_action": {"type": job.get("cta", "LEARN_MORE")}}})
    adset = {"name": f"{name} adset", "campaign_id": "<CAMPAIGN_ID>",
             "daily_budget": job["daily_budget_minor"], "billing_event": "IMPRESSIONS",
             "optimization_goal": OPTIMISATION[job["objective"]],
             "bid_strategy": "LOWEST_COST_WITHOUT_CAP",
             "targeting": targeting_spec(job["targeting"]), "status": "PAUSED"}
    if job["objective"] == "sales":
        adset["promoted_object"] = {"pixel_id": "<PIXEL_ID>", "custom_event_type": "PURCHASE"}
    return [
        {"step": "upload_media", "method": "POST",
         "path": f"{base}/{'advideos' if job.get('video') else 'adimages'}",
         "local_file": job.get("video") or job.get("image")},
        {"step": "campaign", "method": "POST", "path": f"{base}/campaigns",
         "body": {"name": name, "objective": OBJECTIVES[job["objective"]],
                  "special_ad_categories": job.get("special_ad_categories", []),
                  "status": "PAUSED"}},
        {"step": "adset", "method": "POST", "path": f"{base}/adsets", "body": adset},
        {"step": "creative", "method": "POST", "path": f"{base}/adcreatives",
         "body": {"name": f"{name} creative",
                  "object_story_spec": {"page_id": page_id, **creative_media}}},
        {"step": "ad", "method": "POST", "path": f"{base}/ads",
         "body": {"name": f"{name} ad", "adset_id": "<ADSET_ID>",
                  "creative": {"creative_id": "<CREATIVE_ID>"}, "status": "PAUSED"}},
    ]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("job", type=Path)
    ap.add_argument("--out", type=Path, default=Path("build/ads"))
    args = ap.parse_args(argv)
    job = json.loads(args.job.read_text(encoding="utf-8"))
    try:
        plan = build_plan(job)
    except JobError as e:
        print(f"invalid job {args.job}: {e}", file=sys.stderr)
        return 1
    out = args.out / job["id"]
    out.mkdir(parents=True, exist_ok=True)
    (out / "plan.json").write_text(json.dumps({"dry_run": True, "job": job, "requests": plan},
                                              indent=2) + "\n", encoding="utf-8")
    print(f"dry run: {len(plan)} requests written to {out / 'plan.json'} (nothing sent)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
