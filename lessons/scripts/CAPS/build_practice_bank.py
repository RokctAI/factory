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

"""Build lessons/practice_bank.json — the pre-authored practice item bank
behind the Supacharge adaptive practice queue (product log #42 item 2).

Scans the session lesson tree:

    lessons/curriculum/CAPS/{subject}/session/{grade}/{term}/{topic}/{lesson-slug}/mcq.json

and collapses every subtopic-boundary MCQ into one flat item map. Each item
keeps the lesson's own `subtopic_ref` VERBATIM — the same ref the app
attaches to `LMS Lesson Quiz Result` rows during playback — so the server's
need-weighting (`practice_rules.subtopic_needs`) joins practice items to a
student's quiz history with no translation layer. `comprehension_check.json`
is deliberately NOT included: its questions are open-ended (question +
expected answer, no options), and a practice item must be a self-marking MCQ.

Output shape (the contract pinned by rlms's `LMS Practice Item Bank` doctype
and lms_sdk's PracticeItem.fromJson):

    {
      "version": 1,
      "generated_at": "...Z",
      "items": {
        "<subject>.<grade>.<lesson-slug>.<question-id>": {
          "subject": ..., "grade": ..., "lesson": ..., "subtopic_ref": ...,
          "question": ..., "options": [...], "correct_index": ...,
          "skill_ref": ...   (only when the MCQ carries one)
        },
        ...
      }
    }

Item ids are namespaced with subject/grade/lesson because MCQ question ids
(`<subtopic_ref>_q<n>` per the metarules) are only unique within one lesson.

Publishing: POST the file to the rlms backend's System-Manager-only
`publish_practice_bank` endpoint (the app's practice queue is selected
server-side from this bank plus the member's own history). `--publish` does
that POST using the RLMS_SITE_URL / RLMS_API_KEY / RLMS_API_SECRET
environment variables (GitHub Actions secrets in CI — never hardcoded
here); without the flag the script is fully offline. Same split as the
knowledge bites index (built here, published to
publish_knowledge_bites_index).

Output is deterministic (item ids sorted); the file is only rewritten when
content other than generated_at actually changed, so re-runs on unchanged
input produce no diff. Stdlib only — no third-party dependencies (same rule
as build_knowledge_bites_index.py, the pattern this script mirrors).
"""

from __future__ import annotations

import json
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
CAPS_ROOT = REPO_ROOT / "lessons" / "curriculum" / "CAPS"
OUTPUT_PATH = REPO_ROOT / "lessons" / "practice_bank.json"

# All calls ride the single gateway endpoint; the prefix-free `cmd` below
# addresses the rlms whitelisted-method alias
# `{app_name}.api.lms.publish_practice_bank` (see agent
# lms/frappe/manifest.json) whatever the composed app is named.
GATEWAY_PATH = "/api/v1/method/rokct.platform.api"
PUBLISH_CMD = "api.lms.publish_practice_bank"


def parse_int(value, default=None):
    try:
        return int(str(value))
    except (TypeError, ValueError):
        return default


def valid_question(question: dict) -> bool:
    """Mirrors lms_sdk PracticeItem.isValid: an id, a prompt, at least two
    options, and a correct index inside them. Anything else is unservable
    and is skipped (with a warning) rather than published broken."""
    options = question.get("options")
    correct = question.get("correct_index")
    return bool(
        isinstance(question.get("id"), str)
        and question.get("id")
        and isinstance(question.get("question"), str)
        and question.get("question")
        and isinstance(options, list)
        and len(options) >= 2
        and isinstance(correct, int)
        and not isinstance(correct, bool)
        and 0 <= correct < len(options)
    )


def lesson_items(mcq_path: Path, subject: str, grade: int):
    """Yields (item_id, item) for every servable MCQ in one lesson's
    mcq.json; unreadable files and malformed questions warn and are
    skipped rather than published broken."""
    lesson_slug = mcq_path.parent.name
    try:
        mcq = json.loads(mcq_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"warning: could not read {mcq_path}: {exc}", file=sys.stderr)
        return
    subtopics = mcq.get("subtopics") if isinstance(mcq, dict) else None
    for subtopic in subtopics if isinstance(subtopics, list) else []:
        if not isinstance(subtopic, dict):
            continue
        for question in subtopic.get("questions") or []:
            if not isinstance(question, dict) or not valid_question(question):
                print(
                    f"warning: skipping malformed question in {mcq_path}",
                    file=sys.stderr,
                )
                continue
            item_id = f"{subject}.grade{grade}.{lesson_slug}.{question['id']}"
            item = {
                "subject": subject,
                "grade": grade,
                "lesson": lesson_slug,
                "subtopic_ref": subtopic.get("ref"),
                "question": question["question"],
                "options": list(question["options"]),
                "correct_index": question["correct_index"],
            }
            # Optional per the bank contract: present only when the MCQ is
            # a skill-check question.
            if question.get("skill_ref"):
                item["skill_ref"] = question["skill_ref"]
            yield item_id, item


def scan_items() -> dict:
    """item_id -> item, from every subject's session lesson tree."""
    items: dict[str, dict] = {}
    if not CAPS_ROOT.is_dir():
        return items
    for subject_dir in sorted(CAPS_ROOT.iterdir()):
        session_root = subject_dir / "session"
        if not session_root.is_dir():
            continue
        for grade_dir in sorted(session_root.glob("grade*")):
            grade = parse_int(grade_dir.name.removeprefix("grade"))
            if grade is None or not grade_dir.is_dir():
                continue
            for mcq_path in sorted(grade_dir.glob("*/*/*/mcq.json")):
                for item_id, item in lesson_items(
                    mcq_path, subject_dir.name, grade
                ):
                    if item_id in items:
                        print(
                            f"warning: duplicate item id {item_id} "
                            f"({mcq_path}); keeping the first",
                            file=sys.stderr,
                        )
                        continue
                    items[item_id] = item
    return dict(sorted(items.items()))


def build_bank() -> dict:
    return {
        "version": 1,
        "generated_at": datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z"),
        "items": scan_items(),
    }


def content_signature(bank: dict) -> str:
    """Serialization of everything except the volatile generated_at stamp."""
    stable = {key: value for key, value in bank.items() if key != "generated_at"}
    return json.dumps(stable, ensure_ascii=False, sort_keys=True)


def publish(bank: dict) -> int:
    """POST the bank to publish_practice_bank. Site URL and token come from
    the environment (CI secrets) — nothing sensitive lives in this public
    repo. Fails loudly on missing configuration or a non-200 answer."""
    site_url = os.environ.get("RLMS_SITE_URL", "").rstrip("/")
    api_key = os.environ.get("RLMS_API_KEY", "")
    api_secret = os.environ.get("RLMS_API_SECRET", "")
    if not (site_url and api_key and api_secret):
        print(
            "error: --publish needs RLMS_SITE_URL, RLMS_API_KEY and "
            "RLMS_API_SECRET in the environment",
            file=sys.stderr,
        )
        return 1
    source = f"factory@{os.environ.get('GITHUB_SHA', 'local')[:12]}"
    body = json.dumps(
        {
            "cmd": PUBLISH_CMD,
            "payload": {
                "bank_json": json.dumps(bank, ensure_ascii=False),
                "source": source,
            },
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        site_url + GATEWAY_PATH,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"token {api_key}:{api_secret}",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as response:
        body = response.read().decode("utf-8", "replace")
    print(f"published practice bank ({source}): {body[:200]}")
    return 0


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    bank = build_bank()
    item_count = len(bank["items"])

    unchanged = False
    if OUTPUT_PATH.is_file():
        try:
            existing = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
            unchanged = content_signature(existing) == content_signature(bank)
        except (json.JSONDecodeError, OSError):
            pass  # unreadable/invalid existing file — rewrite it

    if unchanged:
        print(f"practice_bank.json unchanged ({item_count} items); not rewriting")
    else:
        OUTPUT_PATH.write_text(
            json.dumps(bank, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"wrote {OUTPUT_PATH.relative_to(REPO_ROOT)} ({item_count} items)")

    if "--publish" in argv:
        return publish(bank)
    return 0


if __name__ == "__main__":
    sys.exit(main())
