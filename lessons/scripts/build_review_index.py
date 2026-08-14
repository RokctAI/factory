#!/usr/bin/env python3
"""Build lessons/review_index.json — the machine-readable lesson index for the
Supacharge in-app lesson review flow.

Scans one lesson population:

1. Session packages:
   lessons/curriculum/CAPS/{subject}/session/grade{g}/term{t}/{topic-slug}/{subtopic-slug}/
   id: session_{subject}_g{grade}_t{term}_{topic-slug}_{subtopic-slug}

Pipeline lessons (the junior tree at lessons/{subject}/grade{g}/..., driven by
job cards in .rokct/agent/jobs/) are deliberately NOT indexed: every pipeline
lesson has a senior CAPS session equivalent that is already indexed, so listing
both would put duplicate lessons in front of reviewers.

Review state is merged from lessons/reviews/<id>.json (absent file means
status "pending"). Output is deterministic (lessons sorted by id); the file
is only rewritten when content other than generated_at actually changed, so
CI re-runs on unchanged input produce no diff.

Stdlib only — no third-party dependencies.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CAPS_ROOT = REPO_ROOT / "lessons" / "curriculum" / "CAPS"
REVIEWS_DIR = REPO_ROOT / "lessons" / "reviews"
OUTPUT_PATH = REPO_ROOT / "lessons" / "review_index.json"


def slug_to_display(slug: str) -> str:
    """'finance-and-growth' -> 'Finance and growth' (sentence case)."""
    words = slug.replace("-", " ").replace("_", " ").strip()
    return words[:1].upper() + words[1:] if words else words


def parse_int(value, default=None):
    try:
        return int(str(value))
    except (TypeError, ValueError):
        return default


def load_review(lesson_id: str) -> dict:
    """Merge review state from lessons/reviews/<id>.json; absent -> pending."""
    review_path = REVIEWS_DIR / f"{lesson_id}.json"
    if review_path.is_file():
        try:
            data = json.loads(review_path.read_text(encoding="utf-8"))
            status = data.get("status")
            if status in ("approved", "denied"):
                return {
                    "status": status,
                    "reason": data.get("reason"),
                    "reviewed_at": data.get("reviewed_at"),
                }
            print(
                f"warning: {review_path} has invalid status {status!r}; "
                "treating as pending",
                file=sys.stderr,
            )
        except (json.JSONDecodeError, OSError) as exc:
            print(f"warning: could not read {review_path}: {exc}", file=sys.stderr)
    return {"status": "pending", "reason": None, "reviewed_at": None}


def scan_session_lessons() -> list:
    """Scan CAPS session packages:
    lessons/curriculum/CAPS/{subject}/session/grade{g}/term{t}/{topic}/{subtopic}/
    """
    lessons = []
    if not CAPS_ROOT.is_dir():
        return lessons
    for subject_dir in sorted(CAPS_ROOT.iterdir()):
        session_root = subject_dir / "session"
        if not session_root.is_dir():
            continue
        subject = subject_dir.name
        for grade_dir in sorted(session_root.glob("grade*")):
            grade = parse_int(grade_dir.name.removeprefix("grade"))
            if grade is None or not grade_dir.is_dir():
                continue
            for term_dir in sorted(grade_dir.glob("term*")):
                term = parse_int(term_dir.name.removeprefix("term"))
                if term is None or not term_dir.is_dir():
                    continue
                for topic_dir in sorted(term_dir.iterdir()):
                    if not topic_dir.is_dir():
                        continue
                    for subtopic_dir in sorted(topic_dir.iterdir()):
                        if not subtopic_dir.is_dir():
                            continue
                        lesson_id = (
                            f"session_{subject}_g{grade}_t{term}_"
                            f"{topic_dir.name}_{subtopic_dir.name}"
                        )
                        lessons.append(
                            {
                                "id": lesson_id,
                                "source": "session",
                                "subject": subject,
                                "grade": grade,
                                "term": term,
                                "topic": slug_to_display(topic_dir.name),
                                "subtopic": slug_to_display(subtopic_dir.name),
                                "package_path": subtopic_dir.relative_to(
                                    REPO_ROOT
                                ).as_posix(),
                                "produced": False,
                                "assets": None,
                                "review": load_review(lesson_id),
                            }
                        )
    return lessons


def build_index() -> dict:
    lessons = scan_session_lessons()
    lessons.sort(key=lambda lesson: lesson["id"])
    return {
        "version": 1,
        "generated_at": datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z"),
        "lessons": lessons,
    }


def content_signature(index: dict) -> str:
    """Serialization of everything except the volatile generated_at stamp."""
    stable = {key: value for key, value in index.items() if key != "generated_at"}
    return json.dumps(stable, ensure_ascii=False, sort_keys=True)


def main() -> int:
    index = build_index()

    if OUTPUT_PATH.is_file():
        try:
            existing = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
            if content_signature(existing) == content_signature(index):
                print(
                    f"review_index.json unchanged "
                    f"({len(index['lessons'])} lessons); not rewriting"
                )
                return 0
        except (json.JSONDecodeError, OSError):
            pass  # unreadable/invalid existing file — rewrite it

    OUTPUT_PATH.write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    by_source: dict = {}
    produced = 0
    for lesson in index["lessons"]:
        by_source[lesson["source"]] = by_source.get(lesson["source"], 0) + 1
        produced += lesson["produced"]
    print(
        f"wrote {OUTPUT_PATH.relative_to(REPO_ROOT)}: "
        f"{len(index['lessons'])} lessons "
        f"({by_source.get('session', 0)} session, "
        f"{by_source.get('pipeline', 0)} pipeline, {produced} produced)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
