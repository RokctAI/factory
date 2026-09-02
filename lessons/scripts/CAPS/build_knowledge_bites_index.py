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

"""Build lessons/knowledge_bites_index.json — the machine-readable bites
index behind the Supacharge in-app knowledge-bite offer (decision #52).

Scans the rehoused bite tree:

    lessons/curriculum/CAPS/{subject}/knowledge_bites/{grade}/{lesson-slug}/{bite-slug}/question.md

and collapses it into one lookup keyed by lesson-slug — the slug of the
session-tree lesson (`session/{grade}/{term}/{topic}/{lesson-slug}`) the
bite is tied to — so the app resolves "what bites exist for this lesson"
directly. Each entry carries the full question.md content inline: an
accepted bite must stay readable offline forever, so the index is the
complete payload, not a pointer.

Output shape (the contract pinned by rlms's bite_rules + lms_sdk's
KnowledgeBiteIndex.parse):

    {
      "version": 1,
      "generated_at": "...Z",
      "bites": {
        "<lesson-slug>": [
          {"bite_slug": ..., "subject": ..., "grade": ..., "title": ...,
           "question_md": ...},
          ...
        ]
      }
    }

Publishing: POST the file to the rlms backend's System-Manager-only
`publish_knowledge_bites_index` endpoint (the app fetches it from there,
backend-first; a copy shipped inside downloaded assets is the offline
fallback). Same split as the skills index.

Output is deterministic (lesson slugs sorted; bites sorted by subject,
grade, bite_slug); the file is only rewritten when content other than
generated_at actually changed, so re-runs on unchanged input produce no
diff. Stdlib only — no third-party dependencies (same rule as
build_review_index.py, the pattern this script mirrors).
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
CAPS_ROOT = REPO_ROOT / "lessons" / "curriculum" / "CAPS"
OUTPUT_PATH = REPO_ROOT / "lessons" / "knowledge_bites_index.json"


def parse_int(value, default=None):
    try:
        return int(str(value))
    except (TypeError, ValueError):
        return default


def bite_title(question_md: str, bite_slug: str) -> str:
    """The first `# ` heading (the attributed worked-example title), falling
    back to the bite slug so a heading-less file still gets a label."""
    for line in question_md.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return bite_slug


def scan_bites() -> dict:
    """lesson-slug -> [bite, ...], from every subject's knowledge_bites tree.

    The same lesson-slug appearing under several subjects/grades merges into
    one list (each bite carries its own subject/grade); the app offers one
    bite per lesson deterministically, so ordering here is part of the
    contract.
    """
    bites: dict[str, list] = {}
    if not CAPS_ROOT.is_dir():
        return bites
    for subject_dir in sorted(CAPS_ROOT.iterdir()):
        bites_root = subject_dir / "knowledge_bites"
        if not bites_root.is_dir():
            continue
        subject = subject_dir.name
        for grade_dir in sorted(bites_root.glob("grade*")):
            grade = parse_int(grade_dir.name.removeprefix("grade"))
            if grade is None or not grade_dir.is_dir():
                continue
            for lesson_dir in sorted(grade_dir.iterdir()):
                if not lesson_dir.is_dir():
                    continue
                for bite_dir in sorted(lesson_dir.iterdir()):
                    question_path = bite_dir / "question.md"
                    if not bite_dir.is_dir() or not question_path.is_file():
                        continue
                    try:
                        question_md = question_path.read_text(encoding="utf-8")
                    except OSError as exc:
                        print(
                            f"warning: could not read {question_path}: {exc}",
                            file=sys.stderr,
                        )
                        continue
                    bites.setdefault(lesson_dir.name, []).append(
                        {
                            "bite_slug": bite_dir.name,
                            "subject": subject,
                            "grade": grade,
                            "title": bite_title(question_md, bite_dir.name),
                            "question_md": question_md,
                        }
                    )
    for entries in bites.values():
        entries.sort(
            key=lambda b: (b["subject"], b["grade"], b["bite_slug"])
        )
    return dict(sorted(bites.items()))


def build_index() -> dict:
    return {
        "version": 1,
        "generated_at": datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z"),
        "bites": scan_bites(),
    }


def content_signature(index: dict) -> str:
    """Serialization of everything except the volatile generated_at stamp."""
    stable = {key: value for key, value in index.items() if key != "generated_at"}
    return json.dumps(stable, ensure_ascii=False, sort_keys=True)


def main() -> int:
    index = build_index()
    bite_count = sum(len(entries) for entries in index["bites"].values())

    if OUTPUT_PATH.is_file():
        try:
            existing = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
            if content_signature(existing) == content_signature(index):
                print(
                    f"knowledge_bites_index.json unchanged "
                    f"({len(index['bites'])} lessons, {bite_count} bites); "
                    "not rewriting"
                )
                return 0
        except (json.JSONDecodeError, OSError):
            pass  # unreadable/invalid existing file — rewrite it

    OUTPUT_PATH.write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"wrote {OUTPUT_PATH.relative_to(REPO_ROOT)} "
        f"({len(index['bites'])} lessons, {bite_count} bites)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
