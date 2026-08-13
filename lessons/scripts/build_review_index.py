#!/usr/bin/env python3
"""Build lessons/review_index.json — the machine-readable lesson index for the
Supacharge in-app lesson review flow.

Scans two lesson populations:

1. Session packages:
   lessons/curriculum/CAPS/{subject}/session/grade{g}/term{t}/{topic-slug}/{subtopic-slug}/
   id: session_{subject}_g{grade}_t{term}_{topic-slug}_{subtopic-slug}

2. Pipeline lessons:
   lessons/{subject}/grade{g}/{term}/{card_id}/ driven by job cards in
   .rokct/agent/jobs/{pending,running,done}/. Only lesson directories that
   exist on disk are indexed (a queued card with no generated content has
   nothing to review yet). id: the job-card id verbatim.
   Done cards whose frontmatter carries manifest_url / audio_url /
   animation_url (GitHub Release assets) are marked produced=true.

Review state is merged from lessons/reviews/<id>.json (absent file means
status "pending"). Output is deterministic (lessons sorted by id); the file
is only rewritten when content other than generated_at actually changed, so
CI re-runs on unchanged input produce no diff.

Stdlib only — no third-party dependencies.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CAPS_ROOT = REPO_ROOT / "lessons" / "curriculum" / "CAPS"
JOBS_ROOT = REPO_ROOT / ".rokct" / "agent" / "jobs"
REVIEWS_DIR = REPO_ROOT / "lessons" / "reviews"
OUTPUT_PATH = REPO_ROOT / "lessons" / "review_index.json"

JOB_QUEUES = ("pending", "running", "done")

FRONTMATTER_KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$")


def parse_frontmatter(path: Path) -> dict:
    """Parse simple scalar key: value pairs from a job card's YAML frontmatter.

    Tiny stdlib parser: reads the block between the first pair of '---' lines
    (ignoring any leading HTML comment), takes zero-indent 'key: value' lines,
    and skips block-scalar bodies (indented continuation lines).
    """
    fields: dict = {}
    in_frontmatter = False
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return fields
    for line in text.splitlines():
        if line.strip() == "---":
            if in_frontmatter:
                break
            in_frontmatter = True
            continue
        if not in_frontmatter:
            continue
        if line[:1] in (" ", "\t"):
            continue  # block-scalar continuation / nested value
        match = FRONTMATTER_KEY_RE.match(line)
        if match:
            value = match.group(2).strip()
            if value in ("|", ">", "|-", ">-"):
                value = ""  # block scalar marker; body not needed here
            fields[match.group(1)] = value
    return fields


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


def scan_pipeline_lessons() -> list:
    """Scan pipeline lessons via job cards in .rokct/agent/jobs/{pending,running,done}.

    A card is indexed when its lesson directory exists on disk. produced=true
    only when the card carries GitHub Release asset URLs.
    """
    lessons = []
    seen = set()
    for queue in JOB_QUEUES:
        queue_dir = JOBS_ROOT / queue
        if not queue_dir.is_dir():
            continue
        for card_path in sorted(queue_dir.glob("*.md")):
            card = parse_frontmatter(card_path)
            card_id = card.get("id")
            if not card_id or card_id in seen:
                continue
            lesson_path = card.get("lesson_path", "")
            if not lesson_path or not (REPO_ROOT / lesson_path).is_dir():
                continue  # no generated content on disk yet — nothing to review
            seen.add(card_id)

            manifest_url = card.get("manifest_url") or None
            audio_url = card.get("audio_url") or None
            animations_url = card.get("animation_url") or None
            produced = bool(manifest_url and audio_url and animations_url)
            assets = (
                {
                    "manifest_url": manifest_url,
                    "audio_url": audio_url,
                    "animations_url": animations_url,
                }
                if produced
                else None
            )

            # subject as slug (directory form), consistent with session lessons
            path_parts = Path(lesson_path).parts
            subject = path_parts[1] if len(path_parts) > 1 else (
                card.get("subject", "").lower().replace(" ", "_")
            )

            lessons.append(
                {
                    "id": card_id,
                    "source": "pipeline",
                    "subject": subject,
                    "grade": parse_int(card.get("grade")),
                    "term": parse_int(card.get("term")),
                    "topic": card.get("topic") or None,
                    "subtopic": card.get("subtopic") or None,
                    "package_path": lesson_path,
                    "produced": produced,
                    "assets": assets,
                    "review": load_review(card_id),
                }
            )
    return lessons


def build_index() -> dict:
    lessons = scan_session_lessons() + scan_pipeline_lessons()
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
