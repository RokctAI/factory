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

"""Curriculum-root resolution shared by the four index builders, and the
factory-owned curriculum registry (lessons/curriculum/curricula.json).

The builders (build_skills_index, build_practice_bank,
build_knowledge_bites_index, build_review_index) were each pinned to
`lessons/curriculum/CAPS` by a module-level constant. This module lets one
implementation serve any curriculum tree under `lessons/curriculum/` via a
`--curriculum NAME` flag, so a second curriculum is a second INVOCATION
rather than a forked copy of the builder — the same "parameterize, don't
fork" rule `lessons/scripts/IEB/release_on_complete.py` already applies to
the release path.

CAPS is the default and its behaviour is unchanged in every respect,
including the output path: `--curriculum CAPS`, and passing no flag at all,
both write the same flat `lessons/<index>.json` the workflows commit today.

SEPARATE OUTPUT FILES ARE DELIBERATE, NOT A CONVENIENCE. Index identities do
not carry a curriculum:

  * skills entries are keyed by `skill_ref` and the IEB tree keeps those
    byte-identical to CAPS on purpose, so the syllabus `requires_skills`
    links resolve against the same skill;
  * practice-bank item ids are derived from (subject, grade, lesson,
    subtopic) with no curriculum segment;
  * review-index lesson ids are derived from the package path below the
    curriculum root.

So a second curriculum written into the SAME file would collide on every
key. build_practice_bank's own duplicate guard would drop the coloniser
silently ("keeping the first"). Merging curricula into one index therefore
needs a curriculum dimension in the published schema and in every consumer
that reads it — a separate, larger change. Until that exists, each
curriculum gets its own file and nothing that reads today's files changes.
"""
import json
from pathlib import Path

# The curriculum whose indexes live at the flat, historical output paths.
DEFAULT_CURRICULUM = "CAPS"

# THE CURRICULUM REGISTRY (Ray, 2026-09-10/11: the factory repo decides the
# curriculum set; Cambridge is the third curriculum and carries a "soon"
# label). lessons/curriculum/curricula.json is the one factory-owned list:
# id (the directory name under lessons/curriculum/ and under a package's
# overlays/), display name, badge text, status ("live" | "soon") and how
# the content is delivered ("package" = the shared top-level package,
# "overlay" = overlays/<id>/ inside it, null = declared, no content yet).
# Overlay labels, the manifest `curricula` list and every badge derive
# from here — never from a second hard-coded list. lms_sdk's landing
# `curricula` list should read the same file (follow-up).
REPO_ROOT = Path(__file__).resolve().parents[3]
REGISTRY_PATH = Path("lessons") / "curriculum" / "curricula.json"
STATUS_LIVE = "live"
STATUS_SOON = "soon"
CONTENT_ALLOWED = "allowed"


def load_registry(repo_root: Path | None = None) -> dict:
    """The parsed registry file (raises if it is missing or malformed —
    there is no fallback list by design)."""
    path = Path(repo_root or REPO_ROOT) / REGISTRY_PATH
    data = json.loads(path.read_text(encoding="utf-8"))
    entries = data.get("curricula")
    if not isinstance(entries, list) or not entries:
        raise ValueError(f"{path}: `curricula` must be a non-empty list")
    for entry in entries:
        for key in ("id", "name", "badge", "status"):
            if not isinstance(entry.get(key), str) or not entry[key]:
                raise ValueError(f"{path}: every curriculum needs `{key}`")
    return data


def registry_entries(repo_root: Path | None = None) -> list[dict]:
    """Registry entries in registry order (the display / manifest order)."""
    return list(load_registry(repo_root)["curricula"])


def curriculum_ids(repo_root: Path | None = None) -> list[str]:
    return [e["id"] for e in registry_entries(repo_root)]


def curriculum_entry(curriculum: str, repo_root: Path | None = None) -> dict:
    for entry in registry_entries(repo_root):
        if entry["id"] == curriculum:
            return entry
    raise KeyError(f"{curriculum!r} is not a registered curriculum "
                   f"({REGISTRY_PATH} lists {curriculum_ids(repo_root)})")


def is_registered(curriculum: str, repo_root: Path | None = None) -> bool:
    return curriculum in curriculum_ids(repo_root)


def badge(curriculum: str, repo_root: Path | None = None) -> str:
    """The badge text a learner sees for `curriculum`."""
    return curriculum_entry(curriculum, repo_root)["badge"]


def status(curriculum: str, repo_root: Path | None = None) -> str:
    return curriculum_entry(curriculum, repo_root)["status"]


def content_allowed(curriculum: str, repo_root: Path | None = None) -> bool:
    """May the tools generate or accept content (an overlay, bank items)
    for `curriculum`? Only a registered, live curriculum whose `content`
    is "allowed" — Cambridge is "soon" and blocked pending written
    permission, so every generator and validator refuses it."""
    if not is_registered(curriculum, repo_root):
        return False
    entry = curriculum_entry(curriculum, repo_root)
    return (entry["status"] == STATUS_LIVE
            and entry.get("content", CONTENT_ALLOWED) == CONTENT_ALLOWED)


def refusal(curriculum: str, repo_root: Path | None = None) -> str:
    """Why content for `curriculum` is refused (for error messages)."""
    if not is_registered(curriculum, repo_root):
        return (f"{curriculum!r} is not a registered curriculum "
                f"({REGISTRY_PATH} lists {curriculum_ids(repo_root)})")
    entry = curriculum_entry(curriculum, repo_root)
    return (f"{curriculum!r} is {entry['status']} with content "
            f"{entry.get('content', CONTENT_ALLOWED)!r}: no overlay or bank "
            "item may be generated or accepted for it")


def ordered(curricula, repo_root: Path | None = None) -> list[str]:
    """`curricula` (any iterable of ids) in registry order, dropping ids the
    registry does not know."""
    wanted = set(curricula)
    return [c for c in curriculum_ids(repo_root) if c in wanted]


def parse_curriculum(argv) -> str:
    """Read `--curriculum NAME` / `--curriculum=NAME` out of argv.

    Unknown flags are ignored, so the builders' existing `--publish`
    handling is untouched. Returns DEFAULT_CURRICULUM when absent.
    """
    argv = list(argv or [])
    for i, arg in enumerate(argv):
        if arg == "--curriculum" and i + 1 < len(argv):
            value = argv[i + 1]
            break
        if arg.startswith("--curriculum="):
            value = arg.split("=", 1)[1]
            break
    else:
        return DEFAULT_CURRICULUM
    value = value.strip()
    if not value:
        raise ValueError("--curriculum needs a non-empty curriculum name")
    if "/" in value or "\\" in value or value.startswith("."):
        raise ValueError(f"--curriculum must be a bare directory name, got {value!r}")
    return value


def curriculum_root(repo_root: Path, curriculum: str) -> Path:
    """The lesson tree for `curriculum`, e.g. lessons/curriculum/IEB."""
    return Path(repo_root) / "lessons" / "curriculum" / curriculum


def output_path(repo_root: Path, curriculum: str, filename: str) -> Path:
    """Where `curriculum`'s copy of `filename` is written.

    CAPS keeps the flat historical path (`lessons/skills_index.json`) that
    the workflows commit and the backend publishes. Every other curriculum
    is namespaced under its own directory (`lessons/IEB/skills_index.json`)
    so the two never overwrite each other and no existing consumer sees a
    changed file.
    """
    repo_root = Path(repo_root)
    if curriculum == DEFAULT_CURRICULUM:
        return repo_root / "lessons" / filename
    return repo_root / "lessons" / curriculum / filename


def resolve(repo_root: Path, argv, filename: str):
    """(curriculum, root, output_path) for this invocation."""
    curriculum = parse_curriculum(argv)
    return (
        curriculum,
        curriculum_root(repo_root, curriculum),
        output_path(repo_root, curriculum, filename),
    )
