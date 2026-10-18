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


"""Results loop rules - decide pause / scale / keep per ad from insights.

Input: a list of per-ad insight rows as Meta's /insights endpoint returns
them (spend, impressions, clicks, actions). Output: one decision per ad.
Pure function, no network: a later live step feeds it real insights and
applies the decisions; today it runs on saved or sample rows.

    python social/meta_ads/optimise.py examples/sample_insights.json --target-cpa 2500
"""

import argparse
import json
import sys
from pathlib import Path

MIN_IMPRESSIONS = 1000      # no verdict before this much data
MIN_CTR = 0.005             # 0.5% link CTR floor
SCALE_STEP = 0.2            # +20% budget per scale, Meta's own guidance on gentle changes


def _results(row, event):
    for a in row.get("actions", []):
        if a.get("action_type") == event:
            return float(a.get("value", 0))
    return 0.0


def decide(row, target_cpa_minor, event="link_click"):
    imps = float(row.get("impressions", 0))
    spend_minor = round(float(row.get("spend", 0)) * 100)
    clicks = float(row.get("inline_link_clicks", row.get("clicks", 0)))
    results = _results(row, event)
    ad = row.get("ad_id", "?")
    if imps < MIN_IMPRESSIONS:
        return {"ad_id": ad, "action": "keep", "reason": "learning: under 1000 impressions"}
    ctr = clicks / imps if imps else 0
    if results == 0 and spend_minor >= 2 * target_cpa_minor:
        return {"ad_id": ad, "action": "pause", "reason": "spent 2x target CPA with no results"}
    if ctr < MIN_CTR:
        return {"ad_id": ad, "action": "pause", "reason": f"CTR {ctr:.2%} under {MIN_CTR:.1%}"}
    if results:
        cpa = spend_minor / results
        if cpa <= 0.8 * target_cpa_minor:
            return {"ad_id": ad, "action": "scale", "budget_factor": 1 + SCALE_STEP,
                    "reason": f"CPA {cpa:.0f} under 80% of target"}
        if cpa > 1.5 * target_cpa_minor:
            return {"ad_id": ad, "action": "pause", "reason": f"CPA {cpa:.0f} over 150% of target"}
    return {"ad_id": ad, "action": "keep", "reason": "within target"}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("insights", type=Path)
    ap.add_argument("--target-cpa", type=int, required=True, help="target cost per result, minor units")
    ap.add_argument("--event", default="link_click")
    args = ap.parse_args(argv)
    rows = json.loads(args.insights.read_text(encoding="utf-8"))
    print(json.dumps([decide(r, args.target_cpa, args.event) for r in rows], indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
