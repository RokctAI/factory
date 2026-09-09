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

"""Curriculum-root resolution shared by the four index builders.

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
from pathlib import Path

# The curriculum whose indexes live at the flat, historical output paths.
DEFAULT_CURRICULUM = "CAPS"


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
