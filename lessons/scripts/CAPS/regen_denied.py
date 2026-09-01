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

"""Queue regeneration for lessons whose review landed as "denied".

Scans lessons/reviews/*.json (the review-state files written by the
Supacharge admin review endpoint) and, for each denial, re-enters the lesson
into generation with the reviewer's feedback attached.

All indexed lessons are session lessons (source "session" —
folder-is-the-contract packages authored by direct in-context sessions; no
automated generator exists): a regeneration brief is written to
lessons/reviews/regen/<lesson_id>.md with the denial reason, the package
path, and the authoring contract. That directory is the work queue an
authoring session consumes; the brief is deleted by the commit that rewrites
the package (or cleared here on approval).

(The former pipeline branch — re-queueing a job card for source "pipeline"
lessons — was removed in 2026-08 with the retirement and deletion of the
junior lesson tree; review_index.json has been session-only since the
index stopped listing pipeline lessons.)

Idempotency and bounded retries via lessons/reviews/regen_state.json:
a given denial (lesson_id + reviewed_at) queues exactly once — re-running
on unchanged reviews is a no-op. Max 2 regeneration attempts per lesson;
a third denial sets parked=true (human intervention required, nothing is
queued) until an approved review clears the lesson's state. An approval
also removes any pending regen brief.

Stdlib only — no third-party dependencies.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
REVIEWS_DIR = REPO_ROOT / "lessons" / "reviews"
REGEN_DIR = REVIEWS_DIR / "regen"
STATE_PATH = REVIEWS_DIR / "regen_state.json"
INDEX_PATH = REPO_ROOT / "lessons" / "review_index.json"

MAX_ATTEMPTS = 2

BRIEF_TEMPLATE = """\
# Regeneration brief — {lesson_id}

- **Denied by:** {reviewed_by} on {reviewed_at} (regeneration attempt {attempt} of {max_attempts})
- **Package:** `{package_path}`
- **Lesson:** {subject} grade {grade} term {term} — {topic} / {subtopic}
- **Reason:**

> {reason}

## Authoring contract

Rewrite the package in place to address the reason above. The folder is the
contract — all 9 required files must remain present and consistent:
`script.md`, `intro.md`, `mcq.json`, `subtopics.json`, `manim_scene.py`,
`assistant_qa_transcript.md`, `assistant_nervous_script.md`,
`comprehension_check.json`, `reel_clip.json` (plus `audio.mp3` under the
audio root for release).

- Duo format: the subject's expert tutor leads Part 1; a `# Part 2` heading
  in `script.md` marks the simplifier's takeover.
- Compliance: no greetings/self-intros/sign-offs (R2) and no bracketed stage
  directions (R3) in script text. Validate before committing:

      python3 lessons/scripts/CAPS/lesson_compliance.py <changed files>

Delete this brief in the same commit that rewrites the package.
"""


def now_utc() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def load_state() -> dict:
    if STATE_PATH.is_file():
        try:
            data = json.loads(STATE_PATH.read_text(encoding="utf-8"))
            if isinstance(data, dict) and isinstance(data.get("lessons"), dict):
                return data
        except (json.JSONDecodeError, OSError) as exc:
            print(f"warning: could not read {STATE_PATH}: {exc}", file=sys.stderr)
    return {"version": 1, "lessons": {}}


def load_index_lessons() -> dict:
    """id -> index entry, for resolving a lesson's source and package."""
    try:
        index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
        return {lesson["id"]: lesson for lesson in index.get("lessons", [])}
    except (json.JSONDecodeError, OSError, KeyError, TypeError) as exc:
        print(f"error: could not read {INDEX_PATH}: {exc}", file=sys.stderr)
        return {}


def load_reviews() -> list:
    """All valid review files, sorted by lesson id. Skips the state file."""
    reviews = []
    for path in sorted(REVIEWS_DIR.glob("*.json")):
        if path == STATE_PATH:
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            print(f"warning: could not read {path}: {exc}", file=sys.stderr)
            continue
        lesson_id = path.stem
        if data.get("lesson_id") not in (None, lesson_id):
            print(
                f"warning: {path} lesson_id {data.get('lesson_id')!r} does not "
                f"match filename; skipping",
                file=sys.stderr,
            )
            continue
        if data.get("status") not in ("approved", "denied"):
            continue  # pending/invalid — the index build already warns
        reviews.append((lesson_id, data))
    return reviews


def write_brief(lesson_id: str, entry: dict, review: dict, attempt: int) -> None:
    REGEN_DIR.mkdir(parents=True, exist_ok=True)
    reason = (review.get("reason") or "no reason given").strip()
    brief = BRIEF_TEMPLATE.format(
        lesson_id=lesson_id,
        reviewed_by=review.get("reviewed_by") or "unknown",
        reviewed_at=review.get("reviewed_at") or "unknown",
        attempt=attempt,
        max_attempts=MAX_ATTEMPTS,
        package_path=entry.get("package_path") or "unknown",
        subject=entry.get("subject"),
        grade=entry.get("grade"),
        term=entry.get("term"),
        topic=entry.get("topic"),
        subtopic=entry.get("subtopic"),
        reason="\n> ".join(reason.splitlines()),
    )
    (REGEN_DIR / f"{lesson_id}.md").write_text(brief, encoding="utf-8")
    print(f"queued session regen: {lesson_id} (attempt {attempt}) -> lessons/reviews/regen/{lesson_id}.md")


def remove_brief(lesson_id: str) -> None:
    brief_path = REGEN_DIR / f"{lesson_id}.md"
    if brief_path.is_file():
        brief_path.unlink()
        print(f"removed regen brief: lessons/reviews/regen/{lesson_id}.md")


def main() -> int:
    state = load_state()
    original = json.dumps(state, sort_keys=True)
    index_lessons = load_index_lessons()
    tracked = state["lessons"]

    for lesson_id, review in load_reviews():
        if review["status"] == "approved":
            if lesson_id in tracked:
                del tracked[lesson_id]
                print(f"approved: cleared regen state for {lesson_id}")
            remove_brief(lesson_id)
            continue

        # status == "denied"
        entry = tracked.get(lesson_id)
        if entry and entry.get("parked"):
            print(f"parked: {lesson_id} needs human intervention; not queued")
            continue
        reviewed_at = review.get("reviewed_at") or ""
        if entry and (not reviewed_at or reviewed_at <= entry.get("last_reviewed_at", "")):
            continue  # this denial was already queued — no-op

        attempt = (entry.get("attempts", 0) if entry else 0) + 1
        if attempt > MAX_ATTEMPTS:
            tracked[lesson_id] = {
                "attempts": attempt,
                "last_reviewed_at": reviewed_at,
                "last_queued_at": (entry or {}).get("last_queued_at"),
                "parked": True,
            }
            remove_brief(lesson_id)
            print(
                f"parked: {lesson_id} denied again after {MAX_ATTEMPTS} regeneration "
                "attempts; human intervention required"
            )
            continue

        lesson = index_lessons.get(lesson_id)
        if lesson is None:
            print(f"warning: {lesson_id} not in review_index.json; not queued", file=sys.stderr)
            continue
        if lesson.get("source") == "pipeline":
            # Defensive: the index has been session-only since the junior
            # lesson tree was retired (2026-08); a pipeline entry here means
            # the index and this script have drifted apart.
            print(
                f"warning: {lesson_id} has source 'pipeline' — the pipeline "
                "regeneration path was retired with the junior lesson tree; "
                "not queued",
                file=sys.stderr,
            )
            continue
        write_brief(lesson_id, lesson, review, attempt)
        tracked[lesson_id] = {
            "attempts": attempt,
            "last_reviewed_at": reviewed_at,
            "last_queued_at": now_utc(),
            "parked": False,
        }

    if json.dumps(state, sort_keys=True) != original:
        STATE_PATH.write_text(
            json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(f"wrote {STATE_PATH.relative_to(REPO_ROOT)} ({len(tracked)} tracked lessons)")
    else:
        print("regen_state.json unchanged; nothing queued")
    return 0


if __name__ == "__main__":
    sys.exit(main())
