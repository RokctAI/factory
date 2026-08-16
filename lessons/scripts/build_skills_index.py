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

"""Build lessons/skills_index.json — the machine-readable skill_ref lookup
behind the Supacharge NON-FORCING skill suggestions (pre-session
assessment, attendance hand-out) and the Library's skills shelf.

Scans the per-skill CAPS files — the source of truth for skill content:

    lessons/curriculum/CAPS/{subject}/skills/{grade}/{skill}.json

and collapses them into one lookup keyed by `skill_ref`. Each entry carries
the CAPS file's fields verbatim (name, importance, covered_by, diagnostic,
recap, exit_check, ...) so the authored review sets ride the index — the
app's BackendSkillReviewSource reads them straight off the published entry,
no second endpoint. On top of the verbatim fields each entry adds the
lookup keys lms_sdk's SkillLessonInfo.fromJson pins:

    card_id      — the stable skill_ref itself (the fromCapsJson precedent;
                   never a hash-suffixed pipeline card id)
    status       — "evaluated": per-skill CAPS files ARE the servable
                   authored form (only evaluated entries are servable
                   client-side)
    lesson_name  — the skill's proper `name`, so backend-served entries
                   display it (fromJson does not read `name` directly)
    subtopic     — the first covered_by subtopic, "" for
                   authored-review-only skills

Output shape (the contract pinned by rlms's `LMS Skills Index` doctype and
lms_sdk's SkillLessonIndex.parse):

    {
      "version": 1,
      "generated_at": "...Z",
      "skills": {
        "<skill_ref>": {"card_id": ..., "subject": ..., "grade": ...,
                        "topic": ..., "subtopic": ..., "lesson_name": ...,
                        "status": ..., ...verbatim CAPS fields...},
        ...
      }
    }

Publishing: POST the file to the rlms backend's System-Manager-only
`publish_skills_index` endpoint (the app fetches it from there,
backend-first; a copy shipped inside downloaded assets is the offline
fallback). `--publish` does that POST using the RLMS_SITE_URL /
RLMS_API_KEY / RLMS_API_SECRET environment variables (GitHub Actions
secrets in CI — never hardcoded here); without the flag the script is
fully offline.

Output is deterministic (skill refs sorted); the file is only rewritten
when content other than generated_at actually changed, so re-runs on
unchanged input produce no diff. Stdlib only — no third-party dependencies
(same rule as build_knowledge_bites_index.py, the pattern this script
mirrors).
"""

from __future__ import annotations

import json
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CAPS_ROOT = REPO_ROOT / "lessons" / "curriculum" / "CAPS"
OUTPUT_PATH = REPO_ROOT / "lessons" / "skills_index.json"

# The rlms whitelisted-method alias for api.skills.publish_skills_index
# (see agent lms/frappe/manifest.json; app_name is `paas` in production —
# the same base BackendSkillLessonSource uses client-side).
PUBLISH_METHOD = "/api/method/paas.api.lms.publish_skills_index"


def index_entry(skill: dict) -> dict:
    """One published entry: the CAPS file verbatim (minus the skill_ref the
    entry is keyed by) plus the pinned lookup keys, lookup keys first."""
    covered_by = skill.get("covered_by")
    first_covered = (
        covered_by[0]
        if isinstance(covered_by, list) and covered_by and isinstance(covered_by[0], dict)
        else {}
    )
    entry = {
        "card_id": skill["skill_ref"],
        "subject": skill.get("subject", ""),
        "grade": skill.get("grade"),
        "topic": skill.get("topic", ""),
        "subtopic": first_covered.get("subtopic", ""),
        "lesson_name": skill.get("name", ""),
        "status": "evaluated",
    }
    for key, value in skill.items():
        if key != "skill_ref" and key not in entry:
            entry[key] = value
    return entry


def scan_skills() -> dict:
    """skill_ref -> entry, from every subject's skills tree."""
    skills: dict[str, dict] = {}
    if not CAPS_ROOT.is_dir():
        return skills
    for subject_dir in sorted(CAPS_ROOT.iterdir()):
        skills_root = subject_dir / "skills"
        if not skills_root.is_dir():
            continue
        for skill_path in sorted(skills_root.glob("grade*/*.json")):
            try:
                skill = json.loads(skill_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                print(
                    f"warning: could not read {skill_path}: {exc}",
                    file=sys.stderr,
                )
                continue
            skill_ref = skill.get("skill_ref") if isinstance(skill, dict) else None
            if not isinstance(skill_ref, str) or not skill_ref:
                print(
                    f"warning: {skill_path} has no skill_ref; skipping",
                    file=sys.stderr,
                )
                continue
            if skill_ref in skills:
                print(
                    f"warning: duplicate skill_ref {skill_ref} "
                    f"({skill_path}); keeping the first",
                    file=sys.stderr,
                )
                continue
            skills[skill_ref] = index_entry(skill)
    return dict(sorted(skills.items()))


def build_index() -> dict:
    return {
        "version": 1,
        "generated_at": datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z"),
        "skills": scan_skills(),
    }


def content_signature(index: dict) -> str:
    """Serialization of everything except the volatile generated_at stamp."""
    stable = {key: value for key, value in index.items() if key != "generated_at"}
    return json.dumps(stable, ensure_ascii=False, sort_keys=True)


def publish(index: dict) -> int:
    """POST the index to publish_skills_index. Site URL and token come from
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
    payload = json.dumps(
        {"index_json": json.dumps(index, ensure_ascii=False), "source": source}
    ).encode("utf-8")
    req = urllib.request.Request(
        site_url + PUBLISH_METHOD,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"token {api_key}:{api_secret}",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as response:
        body = response.read().decode("utf-8", "replace")
    print(f"published skills index ({source}): {body[:200]}")
    return 0


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    index = build_index()
    skill_count = len(index["skills"])

    unchanged = False
    if OUTPUT_PATH.is_file():
        try:
            existing = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
            unchanged = content_signature(existing) == content_signature(index)
        except (json.JSONDecodeError, OSError):
            pass  # unreadable/invalid existing file — rewrite it

    if unchanged:
        print(f"skills_index.json unchanged ({skill_count} skills); not rewriting")
    else:
        OUTPUT_PATH.write_text(
            json.dumps(index, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"wrote {OUTPUT_PATH.relative_to(REPO_ROOT)} ({skill_count} skills)")

    if "--publish" in argv:
        return publish(index)
    return 0


if __name__ == "__main__":
    sys.exit(main())
