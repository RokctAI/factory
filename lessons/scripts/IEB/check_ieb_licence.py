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

"""IEB licence gate: refuse a non-empty IEB knowledge-bites index until the
IEB's written permission for commercial reproduction is on record.

WHY THIS EXISTS
---------------
`lessons/curriculum/IEB/SOURCES.md` records the one material difference
between the IEB's terms and the DBE's: the IEB publishes its NSC past papers
and marking guidelines "as a study aid for learners", but its terms of use
state that **"©IEB material may not be reproduced for commercial gain"**.
The DBE's terms carry no such clause. Indexing, linking and internal
analysis of IEB material are unaffected; reproducing IEB *question content*
inside a commercial product is not covered and needs the IEB's written
permission first.

Knowledge bites are exactly that reproduction. A bite is a past-paper worked
example: the CAPS bite slugs look like
`dbe-physical-sciences-g12-p2-2024-nov-q7-1`, and each `question.md` carries
the full question text, the method, the memo working and the answer under an
attribution line. `build_knowledge_bites_index.py` inlines that whole
payload into the index — deliberately, because an accepted bite must stay
readable offline forever — and the index is then POSTed to the rlms
backend's `publish_knowledge_bites_index` endpoint and shipped to students.
So the index is the point where paper content actually leaves the repo. That
makes it the right place to stand a gate: upstream of it there is curation,
downstream of it there is publication.

WHY NOW, WHILE IT IS STILL EMPTY
--------------------------------
Today the IEB tree holds zero `knowledge_bites/` directories (CAPS holds
1429), so building this index over it yields `{"bites": {}}` and nothing is
shipped. That safety is an accident of absence, not a control. Since the
index builders were generalised to take `--curriculum NAME`
(`curriculum_target.py`), an IEB bites index is one flag away — it lands at
`lessons/IEB/knowledge_bites_index.json`. The moment someone fetches IEB
papers and runs the builder, restricted material would flow into a published
index with nothing to stop it. This gate is that stop, written while the
answer is still trivially "nothing to see".

WHAT IS *NOT* GATED, AND WHY
----------------------------
Only the bites index. The other three IEB indexes carry no past-paper
material:

  * practice bank — `build_practice_bank.py` reads the session tree's
    `mcq.json` files. The IEB tree's 366 `mcq.json` files hold ~9.7k
    authored multiple-choice questions written alongside the IEB lessons:
    conceptual teaching items with invented worked figures, carrying no
    paper reference, no question number, no memo transcription and no
    copyright attribution line. Not one of them is byte-identical to its
    CAPS counterpart. They are authored content, not reproduced content, so
    they are not restricted and are deliberately not gated here.
  * skills index — skill_ref metadata, inherited from the curriculum-neutral
    CAPS skill files.
  * review index — lesson package metadata.

LIFTING THE GATE
----------------
Deliberately, in one reviewable commit: obtain the IEB's written permission,
record it in `lessons/curriculum/IEB/SOURCES.md`, and add the permission
marker file this script looks for (see PERMISSION_PATH / PERMISSION_TOKEN).
The marker has to carry an explicit token so that a placeholder or a
half-finished template cannot open the gate by merely existing.

Two layers, same as the mojibake guard:
  - locally:  python3 lessons/scripts/IEB/check_ieb_licence.py
  - in CI:    .github/workflows/ieb_licence_gate.yml

Exit 0 = clear; exit 1 = blocked.
"""
import argparse
import json
import sys
from pathlib import Path

# The published payload this gate protects: an IEB bites index, at the path
# curriculum_target.output_path() gives a non-default curriculum.
INDEX_PATH = Path("lessons") / "IEB" / "knowledge_bites_index.json"

# Where the IEB terms audit and the standing owner flag live. Referenced, not
# parsed — prose is not a machine-readable licence grant.
SOURCES_PATH = Path("lessons") / "curriculum" / "IEB" / "SOURCES.md"

# The marker that lifts the gate, and the exact line it must contain.
PERMISSION_PATH = Path("lessons") / "curriculum" / "IEB" / "IEB_WRITTEN_PERMISSION.md"
PERMISSION_TOKEN = "IEB_COMMERCIAL_REPRODUCTION_PERMISSION: GRANTED"


def repo_root_from_here() -> Path:
    """lessons/scripts/IEB/check_ieb_licence.py -> the repository root."""
    return Path(__file__).resolve().parents[3]


def permission_recorded(repo_root: Path) -> bool:
    """True only when the marker file exists and carries the exact token."""
    path = Path(repo_root) / PERMISSION_PATH
    if not path.is_file():
        return False
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return False
    return PERMISSION_TOKEN in text


def count_bites(index_path: Path):
    """(lesson_count, bite_count) for an index file, or None if unreadable.

    None means "cannot prove this index is empty", which the gate treats as
    a failure: a licence guard fails closed.
    """
    try:
        index = json.loads(Path(index_path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(index, dict):
        return None
    bites = index.get("bites")
    if bites is None:
        return (0, 0)
    if not isinstance(bites, dict):
        return None
    total = 0
    for entries in bites.values():
        total += len(entries) if isinstance(entries, (list, tuple)) else 1
    return (len(bites), total)


def blocked_message(lesson_count, bite_count) -> str:
    """The whole value of this gate is that this message explains itself to
    someone who has never read the conversation that produced it."""
    if lesson_count is None:
        found = (
            f"{INDEX_PATH.as_posix()} exists but could not be parsed as a bites "
            "index, so this gate cannot prove it is empty. A licence guard "
            "fails closed."
        )
    else:
        found = (
            f"{INDEX_PATH.as_posix()} carries {bite_count} knowledge bite(s) "
            f"across {lesson_count} lesson(s). It must be empty."
        )
    return f"""
================================================================================
BLOCKED: IEB knowledge bites are licence-restricted. This is deliberate.
================================================================================

{found}

THIS IS NOT A BUG IN THE BUILD. It is a licence gate, added on purpose while
the index was still empty, precisely so that nobody would have to discover
this problem after the material had already shipped.

WHY
  Knowledge bites are past-paper worked examples. Each one reproduces a full
  exam question, its method, its memo working and its answer, and the
  knowledge-bites index inlines that entire payload before it is POSTed to
  the rlms backend and shipped to students.

  The IEB's terms of use state:

    "IEB material may not be reproduced for commercial gain"

  The IEB publishes its NSC past papers as a study aid for learners;
  reproducing IEB question content inside a commercial product is NOT
  covered by that permission. This is the one material difference from the
  DBE, whose terms carry no commercial clause -- which is why the CAPS
  bites index is free to ship and this one is not.

  The full terms audit and the standing owner flag are recorded in:
    {SOURCES_PATH.as_posix()}

WHAT TO DO
  Do not delete this check, and do not edit the index by hand. Either:

  (a) The bites should not be there. Remove the IEB bite content, rebuild,
      and commit the empty index -- or delete the index file.

  (b) The bites should be there, because permission now exists. Then:
        1. Obtain WRITTEN permission from the IEB for commercial
           reproduction of its past-paper material (or written confirmation
           that the intended use is non-commercial).
        2. Record it in {SOURCES_PATH.as_posix()}
           -- who granted it, when, and what it covers.
        3. Create {PERMISSION_PATH.as_posix()}
           containing this exact line:

             {PERMISSION_TOKEN}

           plus a summary of the grant and a pointer to the written record.

      Step 3 is the switch. It is a separate, reviewable commit on purpose:
      lifting this gate should be a decision somebody signs, not a side
      effect of a green build.

  If you are tempted to skip to (b) without step 1, the answer is no. The
  owner decision this gate is waiting for has not been made.
================================================================================
""".rstrip()


def check(repo_root: Path):
    """(exit_code, report). Pure enough to unit-test against a fixture tree."""
    repo_root = Path(repo_root)
    index_path = repo_root / INDEX_PATH

    if not index_path.exists():
        return 0, (
            f"IEB licence gate clear: {INDEX_PATH.as_posix()} does not exist "
            "(no IEB knowledge bites have been indexed)."
        )

    counts = count_bites(index_path)
    if counts is not None and counts[1] == 0:
        return 0, (
            f"IEB licence gate clear: {INDEX_PATH.as_posix()} is empty "
            "(0 knowledge bites)."
        )

    lesson_count, bite_count = counts if counts is not None else (None, None)

    if permission_recorded(repo_root):
        return 0, (
            f"IEB licence gate lifted: {PERMISSION_PATH.as_posix()} records "
            "written IEB permission for commercial reproduction "
            f"({bite_count if bite_count is not None else 'unknown'} bite(s) "
            "allowed through). Verify the grant still covers this content."
        )

    return 1, blocked_message(lesson_count, bite_count)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Fail if lessons/IEB/knowledge_bites_index.json is non-empty "
            "while the IEB's written permission for commercial reproduction "
            "is not on record."
        )
    )
    parser.add_argument(
        "--repo-root",
        default=None,
        help="Repository root to check (default: the root containing this script).",
    )
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)

    repo_root = Path(args.repo_root) if args.repo_root else repo_root_from_here()
    code, report = check(repo_root)
    print(report, file=sys.stderr if code else sys.stdout)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
