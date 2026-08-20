#!/usr/bin/env python3
# Copyright (c) 2026 RokctAI
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Licensed under the MIT License.
# Copyright 2026 RokctAI
"""Cost / rate-limit reporting over .rokct/agent/log/api_usage.jsonl.

Implements the reporting half of docs/lesson-pipeline-scale-hardening-brief.md
section 3 ("Cost / rate-limit visibility"): aggregate the per-call usage
records the shared delegate already writes — plus the rate-limit / retry
events written by lessons/scripts/CAPS/api_call_logged.py — into a queryable
markdown section for lessons/DASHBOARD.md.

Record shapes handled (all JSONL, one object per line; unknown or malformed
lines are skipped, legacy records missing new fields aggregate fine):

  - call records (anything whose "kind" is not an event kind below), e.g.
      {"api": "groq", "kind": "chat", "model": ..., "prompt_tokens": N,
       "completion_tokens": N, "total_tokens": N, "ts": ...}
      {"api": "jules", "kind": "create_session", ...}
    New optional fields written by the logged wrapper: "run_id" (GitHub
    Actions run id), "job_id" (job-card id), "retries" (int — how many
    rate-limited attempts preceded this successful call).
  - rate-limit events: {"api": ..., "kind": "rate_limit", "status": 429,
      "retry_after": <seconds or null>, "attempt": N, "ts": ...,
      "run_id": ..., "job_id": ...}
  - exhausted-retry events: {"api": ..., "kind": "call_failed", ...}

Pricing is CONFIG-ONLY — this module ships with no prices and never invents
one. Set the environment variable API_PRICE_TABLE to the path of a JSON file:

    {
      "currency": "USD",
      "prices": {
        "groq":  {"<model-id>": {"prompt_per_1m": 0.0,
                                 "completion_per_1m": 0.0}},
        "jules": {"*": {"per_call": 0.0}}
      }
    }

  - prices are per 1 million tokens (prompt_per_1m / completion_per_1m)
    and/or a flat per_call amount; all three keys are optional per entry;
  - "*" is a per-api fallback used when the record's model has no entry;
  - "currency" is a display label only (defaults to blank).

When API_PRICE_TABLE is unset (or unreadable) the report shows raw token
quantities with an explicit "pricing not configured" note and NO cost
numbers.

CLI: python3 lessons/scripts/CAPS/api_cost_report.py [--log PATH]
prints the markdown section to stdout.
"""

import argparse
import json
import os
import sys
from pathlib import Path

DEFAULT_USAGE_LOG = Path(".rokct/agent/log/api_usage.jsonl")
PRICE_TABLE_ENV = "API_PRICE_TABLE"
EVENT_KINDS = ("rate_limit", "call_failed")
MAX_RUN_ROWS = 20  # most recent runs shown in the per-run table
UNTAGGED = "untagged"


def parse_usage(path):
    """Read the JSONL log tolerantly.

    Returns (records, malformed_count). Lines that are not JSON objects are
    counted and skipped, never fatal.
    """
    records, malformed = [], 0
    path = Path(path)
    if not path.exists():
        return records, malformed
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        try:
            rec = json.loads(raw)
        except ValueError:
            malformed += 1
            continue
        if not isinstance(rec, dict):
            malformed += 1
            continue
        records.append(rec)
    return records, malformed


def _int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def _new_bucket():
    return {"calls": 0, "prompt_tokens": 0, "completion_tokens": 0,
            "total_tokens": 0, "retries": 0, "rate_limit_hits": 0,
            "failed": 0}


def _add_record(bucket, rec):
    kind = rec.get("kind")
    if kind == "rate_limit":
        bucket["rate_limit_hits"] += 1
    elif kind == "call_failed":
        bucket["failed"] += 1
    else:
        bucket["calls"] += 1
        bucket["prompt_tokens"] += _int(rec.get("prompt_tokens"))
        bucket["completion_tokens"] += _int(rec.get("completion_tokens"))
        bucket["total_tokens"] += _int(rec.get("total_tokens"))
        bucket["retries"] += _int(rec.get("retries"))


def aggregate(records):
    """Aggregate records into by-(api, model) and by-run buckets.

    Returns {"by_model": {(api, model): bucket}, "by_run": {run_id: bucket},
             "run_last_ts": {run_id: ts}}. Records without a run_id group
    under "untagged"; event records (rate_limit / call_failed) carry no
    model and group under (api, "-").
    """
    by_model, by_run, run_last_ts = {}, {}, {}
    for rec in records:
        api = str(rec.get("api") or "unknown")
        if rec.get("kind") in EVENT_KINDS:
            model = "-"
        else:
            model = str(rec.get("model") or "-")
        mkey = (api, model)
        by_model.setdefault(mkey, _new_bucket())
        _add_record(by_model[mkey], rec)

        run = str(rec.get("run_id") or UNTAGGED)
        by_run.setdefault(run, _new_bucket())
        _add_record(by_run[run], rec)
        ts = str(rec.get("ts") or "")
        if ts > run_last_ts.get(run, ""):
            run_last_ts[run] = ts
    return {"by_model": by_model, "by_run": by_run,
            "run_last_ts": run_last_ts}


def load_price_table(env=None):
    """Load the price table named by API_PRICE_TABLE.

    Returns (table_or_None, note). table is {"currency": str,
    "prices": {api: {model: {...}}}} or None when pricing is not
    configured / unreadable — callers must render no cost in that case.
    """
    env = os.environ if env is None else env
    location = env.get(PRICE_TABLE_ENV, "").strip()
    if not location:
        return None, ("Pricing not configured — set the " + PRICE_TABLE_ENV +
                      " environment variable to the path of a JSON price "
                      "table to enable cost estimates. Token quantities "
                      "only; no cost numbers are shown.")
    try:
        data = json.loads(Path(location).read_text(encoding="utf-8"))
        prices = data["prices"]
        if not isinstance(prices, dict):
            raise ValueError("'prices' must be an object")
    except Exception as exc:  # unreadable config == unconfigured (no cost)
        return None, (f"Price table at {location!r} could not be read "
                      f"({exc}) — token quantities only; no cost numbers "
                      "are shown.")
    return {"currency": str(data.get("currency", "")).strip(),
            "prices": prices}, ""


def price_entry(table, api, model):
    """Look up the price entry for api/model, honouring the '*' fallback."""
    if not table:
        return None
    per_api = table["prices"].get(api)
    if not isinstance(per_api, dict):
        return None
    entry = per_api.get(model)
    if not isinstance(entry, dict):
        entry = per_api.get("*")
    return entry if isinstance(entry, dict) else None


def bucket_cost(bucket, entry):
    """Cost of one aggregate bucket under one price entry, or None."""
    if not entry:
        return None
    try:
        cost = 0.0
        cost += bucket["prompt_tokens"] * float(entry.get("prompt_per_1m", 0)) / 1e6
        cost += bucket["completion_tokens"] * float(entry.get("completion_per_1m", 0)) / 1e6
        cost += bucket["calls"] * float(entry.get("per_call", 0))
    except (TypeError, ValueError):
        return None
    return cost


def _fmt_cost(amount, currency):
    text = f"{amount:.4f}"
    return f"{currency} {text}".strip()


def render_dashboard_section(usage_path=None, env=None):
    """Return the 'Cost / rate-limits' dashboard section as a list of lines
    (markdown, ending with a blank line)."""
    usage_path = Path(usage_path or DEFAULT_USAGE_LOG)
    records, malformed = parse_usage(usage_path)
    table, pricing_note = load_price_table(env=env)
    priced = table is not None
    currency = table["currency"] if priced else ""

    lines = ["## Cost / rate-limits", ""]
    if not records:
        lines += ["No API usage recorded yet.", ""]
        if not priced:
            lines += [pricing_note, ""]
        return lines

    agg = aggregate(records)

    # --- by api/model ---
    header = "| API | Model | Calls | Prompt tok | Completion tok | Total tok | Retries | 429 hits | Failed |"
    rule = "|---|---|---|---|---|---|---|---|---|"
    if priced:
        header += " Est. cost |"
        rule += "---|"
    lines += ["### By API / model", "", header, rule]
    grand_cost, cost_gaps = 0.0, 0
    for (api, model) in sorted(agg["by_model"]):
        b = agg["by_model"][(api, model)]
        row = (f"| {api} | `{model}` | {b['calls']} | {b['prompt_tokens']} "
               f"| {b['completion_tokens']} | {b['total_tokens']} "
               f"| {b['retries']} | {b['rate_limit_hits']} | {b['failed']} |")
        if priced:
            cost = bucket_cost(b, price_entry(table, api, model))
            if cost is None:
                if b["calls"]:
                    cost_gaps += 1
                row += " no price |"
            else:
                grand_cost += cost
                row += f" {_fmt_cost(cost, currency)} |"
        lines.append(row)
    lines.append("")
    if priced:
        note = f"Estimated total spend (priced rows): **{_fmt_cost(grand_cost, currency)}**."
        if cost_gaps:
            note += (f" {cost_gaps} api/model group(s) have no entry in the "
                     "configured price table.")
        lines += [note, ""]
    else:
        lines += [pricing_note, ""]

    # --- by run ---
    by_run = agg["by_run"]
    runs = [r for r in by_run if r != UNTAGGED]
    runs.sort(key=lambda r: agg["run_last_ts"].get(r, ""), reverse=True)
    shown = runs[:MAX_RUN_ROWS]
    lines += [f"### By run (last {len(shown)} of {len(runs)} tagged runs)", ""]
    if shown or UNTAGGED in by_run:
        lines += ["| Run | Calls | Total tok | Retries | 429 hits | Failed |",
                  "|---|---|---|---|---|---|"]
        for run in shown:
            b = by_run[run]
            lines.append(f"| {run} | {b['calls']} | {b['total_tokens']} "
                         f"| {b['retries']} | {b['rate_limit_hits']} "
                         f"| {b['failed']} |")
        if UNTAGGED in by_run:
            b = by_run[UNTAGGED]
            lines.append(f"| _{UNTAGGED} (legacy records)_ | {b['calls']} "
                         f"| {b['total_tokens']} | {b['retries']} "
                         f"| {b['rate_limit_hits']} | {b['failed']} |")
        lines.append("")
    else:
        lines += ["No run-tagged records yet.", ""]
    if malformed:
        lines += [f"({malformed} malformed log line(s) skipped.)", ""]
    return lines


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Render the Cost / rate-limits dashboard section from "
                    "the API usage JSONL log.")
    ap.add_argument("--log", default=str(DEFAULT_USAGE_LOG),
                    help="Path to api_usage.jsonl "
                         f"(default: {DEFAULT_USAGE_LOG})")
    args = ap.parse_args(argv)
    print("\n".join(render_dashboard_section(args.log)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
