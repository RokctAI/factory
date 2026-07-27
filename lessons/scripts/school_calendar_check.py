#!/usr/bin/env python3
# Licensed under the MIT License.
# Copyright 2026 RokctAI
"""Annual school-calendar refresh for lessons/curriculum/CAPS/school_calendar/.

The DBE gazettes a new national school calendar every year (term dates shift
annually). This tool keeps the repo's calendar files current so downstream
consumers - the app backend fetches the raw JSON from this repo and adjusts
schedules - never run a year on stale dates.

    python lessons/scripts/school_calendar_check.py            # check + report
    python lessons/scripts/school_calendar_check.py --write    # also write next
                                                               # year's file if
                                                               # extractable

Behaviour (fail-loud by design):
  - Determines the next calendar year missing from school_calendar/.
  - Fetches the government school-calendar page and looks for that year's
    term dates.
  - Extraction is best-effort: gazette wording/formatting shifts between
    years, so anything extracted is VALIDATED (exactly 4 terms, dates parse,
    ordered, inside the right year, term lengths sane). A file is only
    written when validation passes AND --write is given; the written file
    carries "verified": "PENDING-HUMAN" so a human confirms against the
    gazette before anything schedules off it.
  - Exit codes: 0 = calendar present/nothing to do, 1 = next year's calendar
    appears published but could not be extracted (go do it by hand),
    2 = fetch failed.

Run from CI once a month in Aug-Feb (the window when next year's calendar is
gazetted) - see school_calendar_refresh.yml.
"""

import argparse
import datetime as dt
import json
import re
import sys
import urllib.request
from pathlib import Path

CAL_DIR = Path("lessons/curriculum/CAPS/school_calendar")
SOURCE_URL = "https://www.gov.za/about-sa/school-calendar"

MONTHS = {m.lower(): i + 1 for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"])}


def fetch_page(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", errors="replace")


def _strip_tags(html):
    html = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.DOTALL | re.I)
    text = re.sub(r"<[^>]+>", " ", html)
    return re.sub(r"[ \t ]+", " ", text)


def _parse_day_month(fragment, year):
    m = re.search(r"(\d{1,2})\s+([A-Za-z]+)", fragment)
    if not m or m.group(2).lower() not in MONTHS:
        return None
    try:
        return dt.date(year, MONTHS[m.group(2).lower()], int(m.group(1)))
    except ValueError:
        return None


def extract_terms(text, year):
    """Best-effort: find 'Term N ... <start day month> ... <end day month>'
    rows for the given year in the page text. Returns [] when the page does
    not (yet) carry that year's table in a recognisable shape."""
    terms = []
    # Bound the search to the section mentioning the target year, if any.
    for m in re.finditer(
            r"[Tt]erm\s*([1-4])\D{0,40}?(\d{1,2}\s+[A-Za-z]+)(?:\s*(\d{4}))?"
            r"\D{0,40}?(\d{1,2}\s+[A-Za-z]+)(?:\s*(\d{4}))?", text):
        n = int(m.group(1))
        y_start = int(m.group(3)) if m.group(3) else year
        y_end = int(m.group(5)) if m.group(5) else year
        if y_start != year and y_end != year:
            continue
        start = _parse_day_month(m.group(2), y_start)
        end = _parse_day_month(m.group(4), y_end)
        if start and end and not any(t["term"] == n for t in terms):
            terms.append({"term": n, "start": start.isoformat(), "end": end.isoformat()})
    return sorted(terms, key=lambda t: t["term"])


def validate(terms, year):
    errors = []
    if [t["term"] for t in terms] != [1, 2, 3, 4]:
        errors.append(f"expected terms 1-4, got {[t['term'] for t in terms]}")
        return errors
    prev_end = None
    for t in terms:
        start = dt.date.fromisoformat(t["start"])
        end = dt.date.fromisoformat(t["end"])
        if not (start.year == year or (t["term"] == 1 and start.year == year)):
            errors.append(f"term {t['term']} start not in {year}")
        if end <= start:
            errors.append(f"term {t['term']} ends before it starts")
        length = (end - start).days
        if not 30 <= length <= 100:
            errors.append(f"term {t['term']} length {length} days is implausible")
        if prev_end and start <= prev_end:
            errors.append(f"term {t['term']} overlaps term {t['term'] - 1}")
        prev_end = end
    return errors


def main():
    parser = argparse.ArgumentParser(description="DBE school-calendar refresh check")
    parser.add_argument("--write", action="store_true",
                        help="write next year's file when extraction validates")
    parser.add_argument("--year", type=int, help="target year (default: first missing)")
    args = parser.parse_args()

    have = sorted(int(p.stem) for p in CAL_DIR.glob("*.json") if p.stem.isdigit())
    if not have:
        print(f"Error: no calendar files under {CAL_DIR}")
        return 2
    target = args.year or have[-1] + 1
    if target in have:
        print(f"calendar for {target} already present; nothing to do")
        return 0
    # Only start looking from August of the year before: the DBE gazettes
    # the next year's calendar in the second half of the current year.
    today = dt.date.today()
    if not args.year and (today.year, today.month) < (target - 1, 8):
        print(f"calendar for {target} not expected to be published yet "
              f"(checks begin Aug {target - 1}); latest on file: {have[-1]}")
        return 0

    try:
        text = _strip_tags(fetch_page(SOURCE_URL))
    except Exception as e:
        print(f"FETCH FAILED: {SOURCE_URL}: {e}")
        return 2

    if str(target) not in text:
        print(f"{SOURCE_URL} does not mention {target} yet; latest on file: {have[-1]}")
        return 0

    terms = extract_terms(text, target)
    errors = validate(terms, target) if terms else ["no term rows recognised"]
    if errors:
        print(f"CALENDAR FOR {target} APPEARS PUBLISHED but extraction failed validation:")
        for e in errors:
            print(f"  - {e}")
        print("Extract it by hand from the gazette and add "
              f"{CAL_DIR}/{target}.json (see {have[-1]}.json for the shape).")
        return 1

    print(f"extracted {target}: " + "; ".join(
        f"T{t['term']} {t['start']}..{t['end']}" for t in terms))
    if args.write:
        doc = {
            "year": target,
            "authority": "Department of Basic Education (single national calendar)",
            "source_url": SOURCE_URL,
            "verified": "PENDING-HUMAN",
            "terms": terms,
            "note": ("Auto-extracted by school_calendar_check.py - confirm every "
                     "date against the gazette, add public-holiday notes, then "
                     "set verified to the confirmation date. Maps ATP term "
                     "numbers to real dates for scheduling."),
        }
        out = CAL_DIR / f"{target}.json"
        out.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"written {out} (verified: PENDING-HUMAN - confirm before scheduling off it)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
