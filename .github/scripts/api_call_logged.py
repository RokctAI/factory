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

"""Rate-limit-aware wrapper around the pin-fetched Groq/Jules delegate.

Implements the logging half of docs/lesson-pipeline-scale-hardening-brief.md
section 3: the shared delegate (fetched from The-Rokct-Protocol at CI start
by .rokct/initiate.py, SHA-pinned via call_groq.py) already logs token usage
to .rokct/agent/log/api_usage.jsonl, but has no 429 handling — a rate-limit
lockout surfaces as a generic failed step with no trace in the log. This
factory-side wrapper adds that visibility WITHOUT touching the Protocol repo:

  - it invokes the same scaffold the call sites already use
    (.rokct/skills/agent_delegation/scripts/call_groq.py / call_jules.py),
    passing all remaining arguments through and echoing stdout/stderr, so
    `RESPONSE=$(python .rokct/skills/.../call_groq.py groq --prompt ...)`
    becomes
    `RESPONSE=$(python lessons/scripts/CAPS/api_call_logged.py --api groq
                --job-id "$ID" groq --prompt ...)`;
  - on failure that looks like HTTP 429 / rate limiting it appends a
    {"kind": "rate_limit", "status": 429, "retry_after": ..., "attempt": N,
     "run_id": ..., "job_id": ..., "ts": ...} event to the SAME
    api_usage.jsonl, then retries with bounded exponential backoff
    (honouring a Retry-After value when one is present in the error text);
  - when retries are exhausted it appends a {"kind": "call_failed"} event
    and exits with the delegate's exit code (existing failure handling in
    the workflows is preserved);
  - on success it annotates the record(s) the delegate just appended with
    "run_id" (GITHUB_RUN_ID), "job_id" (when given) and "retries": N, so
    usage is attributable per workflow run / job card. Legacy records are
    untouched.

Non-rate-limit failures are passed straight through with no retry — the
wrapper never changes what a genuine error looks like to the caller.

Environment knobs (all optional):
  API_USAGE_LOG          log path (default .rokct/agent/log/api_usage.jsonl)
  API_DELEGATE_SCRIPT    override the delegate script path (used by tests)
  API_CALL_MAX_RETRIES   max retries after a 429 (default 3)
  API_CALL_BACKOFF_BASE  backoff base seconds (default 2; delays are
                         base*2^attempt, capped at 60s)
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_USAGE_LOG = ".rokct/agent/log/api_usage.jsonl"
DELEGATE_BY_API = {
    "groq": ".rokct/skills/agent_delegation/scripts/call_groq.py",
    "jules": ".rokct/skills/agent_delegation/scripts/call_jules.py",
}
RATE_LIMIT_RE = re.compile(r"(?i)\b429\b|too many requests|rate.?limit")
RETRY_AFTER_RE = re.compile(r"(?i)retry.after[\s:=\"']+([0-9]+(?:\.[0-9]+)?)")
MAX_BACKOFF_S = 60.0


def _now_ts():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _usage_log():
    return Path(os.environ.get("API_USAGE_LOG", DEFAULT_USAGE_LOG))


def append_event(record):
    """Best-effort JSONL append (same contract as the delegate's logger)."""
    try:
        path = _usage_log()
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record) + "\n")
    except OSError:
        pass


def _count_lines(path):
    try:
        return len(path.read_text(encoding="utf-8").splitlines())
    except OSError:
        return 0


def annotate_new_records(before_count, retries, run_id, job_id):
    """Add run/job identity to records appended during this invocation and
    a retries count to the final (delegate-written) call record.

    Best-effort: unparseable lines are left untouched; wrapper-written
    rate_limit events already carry identity and are skipped for the
    retries annotation."""
    path = _usage_log()
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return
    if len(lines) <= before_count:
        return
    changed = False
    last_call_idx = None
    for idx in range(before_count, len(lines)):
        try:
            rec = json.loads(lines[idx])
        except ValueError:
            continue
        if not isinstance(rec, dict):
            continue
        if run_id and "run_id" not in rec:
            rec["run_id"] = run_id
            changed = True
        if job_id and "job_id" not in rec:
            rec["job_id"] = job_id
            changed = True
        if rec.get("kind") not in ("rate_limit", "call_failed"):
            last_call_idx = idx
        lines[idx] = json.dumps(rec)
    if last_call_idx is not None:
        try:
            rec = json.loads(lines[last_call_idx])
            if "retries" not in rec:
                rec["retries"] = retries
                lines[last_call_idx] = json.dumps(rec)
                changed = True
        except ValueError:
            pass
    if changed:
        try:
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        except OSError:
            pass


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Run the pin-fetched Groq/Jules delegate with 429 "
                    "retry + rate-limit event logging.")
    ap.add_argument("--api", choices=sorted(DELEGATE_BY_API), default="groq",
                    help="Which delegate scaffold to run (default: groq)")
    ap.add_argument("--job-id", default="",
                    help="Job-card id to stamp on this call's log records")
    ap.add_argument("--max-retries", type=int,
                    default=int(os.environ.get("API_CALL_MAX_RETRIES", "3")),
                    help="Retries after a rate-limited attempt (default 3)")
    ap.add_argument("rest", nargs=argparse.REMAINDER,
                    help="Arguments passed through to the delegate script")
    args = ap.parse_args(argv)

    delegate = os.environ.get("API_DELEGATE_SCRIPT") or DELEGATE_BY_API[args.api]
    backoff_base = float(os.environ.get("API_CALL_BACKOFF_BASE", "2"))
    run_id = os.environ.get("GITHUB_RUN_ID", "")
    log_path = _usage_log()
    before_count = _count_lines(log_path)

    retries = 0
    for attempt in range(args.max_retries + 1):
        proc = subprocess.run(
            [sys.executable, delegate] + args.rest,
            capture_output=True, text=True, encoding="utf-8",
            errors="replace",
        )
        if proc.returncode == 0:
            sys.stdout.write(proc.stdout)
            sys.stderr.write(proc.stderr)
            annotate_new_records(before_count, retries, run_id, args.job_id)
            return 0

        error_text = (proc.stderr or "") + "\n" + (proc.stdout or "")
        if not RATE_LIMIT_RE.search(error_text):
            # Genuine (non-rate-limit) failure: pass through untouched.
            sys.stdout.write(proc.stdout)
            sys.stderr.write(proc.stderr)
            return proc.returncode

        m = RETRY_AFTER_RE.search(error_text)
        retry_after = float(m.group(1)) if m else None
        append_event({
            "api": args.api, "kind": "rate_limit", "status": 429,
            "retry_after": retry_after, "attempt": attempt + 1,
            "ts": _now_ts(), "run_id": run_id or None,
            "job_id": args.job_id or None,
        })
        if attempt >= args.max_retries:
            append_event({
                "api": args.api, "kind": "call_failed", "status": 429,
                "retries": retries + 1, "ts": _now_ts(),
                "run_id": run_id or None, "job_id": args.job_id or None,
            })
            sys.stdout.write(proc.stdout)
            sys.stderr.write(proc.stderr)
            print(f"api_call_logged: giving up after "
                  f"{attempt + 1} rate-limited attempt(s).", file=sys.stderr)
            return proc.returncode
        retries += 1
        delay = retry_after if retry_after is not None else backoff_base * (2 ** attempt)
        delay = max(0.0, min(delay, MAX_BACKOFF_S))
        print(f"api_call_logged: rate limited (attempt {attempt + 1}); "
              f"retrying in {delay:.1f}s.", file=sys.stderr)
        time.sleep(delay)
    return 1  # unreachable, defensive


if __name__ == "__main__":
    sys.exit(main())
