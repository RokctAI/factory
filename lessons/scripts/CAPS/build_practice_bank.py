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

CURRICULUM LABELS (shared-lesson overlays, W1): every item carries
`"curriculum": "<name>"` — the tree it was scanned from (CAPS on the
default path). A lesson's `overlays/<CURRICULUM>/mcq.json` (see
curriculum_overlay.py) can contribute that curriculum's items under the id
`<subject>.<grade>.<lesson-slug>.<question-id>~<curriculum lower>` so the
existing ids — and every LMS Practice Attempt row keyed by them — are
untouched. Overlay questions flagged `needs_reauthor: true` (they quote a
worked case the shared lesson never taught) are never published until
re-authored; they stay in the overlay file and are counted on stderr.

OVERLAY ITEMS ARE OFF BY DEFAULT. The backend's practice_queue has no
curriculum filter until W2, so overlay items in the published bank would be
served to every learner. They enter the bank only when asked for
explicitly — `--include-overlay-curricula IEB[,...]` or the environment
variable ROKCT_PRACTICE_OVERLAY_CURRICULA=IEB[,...] — and W2 flips the
workflow on once the filter exists. With neither set, a lesson's overlay
changes nothing about this file.

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

import curriculum_overlay
import curriculum_target

REPO_ROOT = Path(__file__).resolve().parents[3]
# Defaults for a no-flag run. main() re-points both at the tree named by
# --curriculum (see curriculum_target); CAPS keeps these exact paths.
CAPS_ROOT = REPO_ROOT / "lessons" / "curriculum" / "CAPS"
OUTPUT_PATH = REPO_ROOT / "lessons" / "practice_bank.json"
CURRICULUM = curriculum_target.DEFAULT_CURRICULUM
# Overlay curricula whose items join the bank; empty = none (the default).
OVERLAY_CURRICULA_ENV = "ROKCT_PRACTICE_OVERLAY_CURRICULA"
OVERLAY_CURRICULA_FLAG = "--include-overlay-curricula"
OVERLAY_CURRICULA: tuple[str, ...] = ()

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


def lesson_items(mcq_path: Path, subject: str, grade: int,
                 curriculum: str | None = None, lesson_slug: str | None = None,
                 id_suffix: str = ""):
    """Yields (item_id, item) for every servable MCQ in one lesson's
    mcq.json; unreadable files and malformed questions warn and are
    skipped rather than published broken. `curriculum` labels the items
    (default: the tree being built); an overlay passes its lesson slug and
    the `~<curriculum>` id suffix explicitly."""
    lesson_slug = lesson_slug or mcq_path.parent.name
    curriculum = curriculum or CURRICULUM
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
            if question.get(curriculum_overlay.NEEDS_REAUTHOR) is True:
                print(
                    f"note: {mcq_path}: {question['id']} needs re-authoring "
                    "against the shared lesson; not published",
                    file=sys.stderr,
                )
                continue
            item_id = (f"{subject}.grade{grade}.{lesson_slug}.{question['id']}"
                       f"{id_suffix}")
            item = {
                "subject": subject,
                "grade": grade,
                "lesson": lesson_slug,
                "curriculum": curriculum,
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
                for item_id, item in overlay_items(
                    mcq_path.parent, subject_dir.name, grade
                ):
                    if item_id in items:
                        print(
                            f"warning: duplicate item id {item_id} "
                            f"({mcq_path.parent}); keeping the first",
                            file=sys.stderr,
                        )
                        continue
                    items[item_id] = item
    return dict(sorted(items.items()))


def parse_overlay_curricula(argv, environ=None) -> tuple[str, ...]:
    """Overlay curricula to include, from `--include-overlay-curricula
    A[,B]` / `--include-overlay-curricula=A` or the environment variable;
    () when neither is set. Names must be registered curricula."""
    environ = os.environ if environ is None else environ
    argv = list(argv or [])
    raw = environ.get(OVERLAY_CURRICULA_ENV, "")
    for i, arg in enumerate(argv):
        if arg == OVERLAY_CURRICULA_FLAG and i + 1 < len(argv):
            raw = argv[i + 1]
        elif arg.startswith(OVERLAY_CURRICULA_FLAG + "="):
            raw = arg.split("=", 1)[1]
    names = tuple(n.strip() for n in raw.split(",") if n.strip())
    for name in names:
        if not curriculum_target.content_allowed(name):
            raise ValueError(curriculum_target.refusal(name))
    return names


def overlay_items(lesson_dir: Path, subject: str, grade: int):
    """(item_id, item) for every INCLUDED overlay curriculum of one lesson
    (see OVERLAY_CURRICULA — empty by default): the overlay's mcq.json under
    the `~<curriculum>` id suffix, labelled with that curriculum, the lesson
    slug shared with the CAPS items."""
    if not OVERLAY_CURRICULA:
        return
    for curriculum in curriculum_overlay.list_overlays(lesson_dir):
        if curriculum not in OVERLAY_CURRICULA:
            continue
        mcq_path = (curriculum_overlay.overlay_dir(lesson_dir, curriculum)
                    / curriculum_overlay.OVERLAY_MCQ)
        if not mcq_path.is_file():
            continue
        yield from lesson_items(
            mcq_path, subject, grade, curriculum=curriculum,
            lesson_slug=lesson_dir.name, id_suffix=f"~{curriculum.lower()}")


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
    global CAPS_ROOT, OUTPUT_PATH, CURRICULUM, OVERLAY_CURRICULA
    curriculum, CAPS_ROOT, OUTPUT_PATH = curriculum_target.resolve(
        REPO_ROOT, argv, "practice_bank.json")
    CURRICULUM = curriculum
    OVERLAY_CURRICULA = parse_overlay_curricula(argv)
    if OVERLAY_CURRICULA:
        print(f"including overlay curricula: {', '.join(OVERLAY_CURRICULA)}")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    if curriculum != curriculum_target.DEFAULT_CURRICULUM:
        print(
            f"building {curriculum} from "
            f"{CAPS_ROOT.relative_to(REPO_ROOT)} -> "
            f"{OUTPUT_PATH.relative_to(REPO_ROOT)}"
        )
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
