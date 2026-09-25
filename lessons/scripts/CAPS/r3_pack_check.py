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

"""Checker for Foundation Phase (Grades R-3) activity packs.

R-3 learners do not get the secondary lesson package. The tutor is the
lesson: an engine in the app runs short game rounds from prepared packs, and
the AI only checks a spoken answer against the round's accept list. Every
line a child hears is written here and reviewed; nothing is generated live.

Packs live at lessons/curriculum/CAPS/{subject}/r3_packs/grade{R,1,2,3}/
term{N}/{slug}.json. Rules (exit 1 on any violation):

  P1 SHAPE        required keys present, id matches the file path
  P2 SOURCE       source.file/term/topic/subtopic names a real syllabus row
                  that is switched on (lessons_enabled not false at file,
                  topic or subtopic level)
  P3 ROUNDS       4-8 rounds, every type in ROUND_TYPES with its own fields
  P4 ANSWERS      a tap round's answer is one of 2-4 distinct options; a say
                  round has a non-empty accept list; a count round's answer
                  equals its count
  P5 CHILD LINES  every spoken line is short (<= MAX_LINE_WORDS words), with
                  no brackets (TTS reads them aloud) and no URLs
  P6 IMAGES       every image key is a lowercase slug listed in the pack's
                  images list, so the illustration job knows what to draw.
                  listen_tap/story_tap/blend options are pictures; count_tap
                  and what_next options are drawn as numerals or text
  P7 UNIQUE IDS   pack ids are unique across the tree
"""
import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
CAPS_DIR = REPO / "lessons" / "curriculum" / "CAPS"
PACK_GLOB = "*/r3_packs/grade*/term*/*.json"

MAX_LINE_WORDS = 20
SLUG_RE = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+)*$")
BRACKET_RE = re.compile(r"[\[\]{}<>]|\([^)]*\)")
REQUIRED = ("id", "subject", "grade", "term", "weeks", "source", "skill",
            "prereq_skills", "images", "show", "rounds", "hints",
            "beat_the_tutor", "parent_line")

# Round type -> the fields that type needs beyond "type" and "prompt".
ROUND_TYPES = {
    "listen_tap": ("options", "answer"),
    "say_it": ("accept",),
    "trace": ("glyph",),
    "count_tap": ("image", "count", "options", "answer"),
    "match_sort": ("groups", "items"),
    "what_next": ("sequence", "options", "answer"),
    "story_tap": ("story", "options", "answer"),
    "blend": ("sounds", "options", "answer"),
    "read_to_me": ("text", "accept"),
}
TAP_TYPES = {"listen_tap", "count_tap", "what_next", "story_tap", "blend"}


def _sub_name(sub):
    return sub["name"] if isinstance(sub, dict) else sub


def _source_ok(source):
    """Return an error string, or None when source names a live syllabus row."""
    path = REPO / source.get("file", "")
    if not path.is_file():
        return f"source.file {source.get('file')!r} not found"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("lessons_enabled") is False:
        return f"{source['file']} has lessons_enabled false"
    for term in data.get("terms", []):
        if term.get("term") != source.get("term"):
            continue
        for topic in term.get("topics", []):
            if topic["name"] != source.get("topic"):
                continue
            if topic.get("lessons_enabled") is False:
                return f"topic {topic['name']!r} has lessons_enabled false"
            for sub in topic.get("subtopics", []):
                if _sub_name(sub) == source.get("subtopic"):
                    if isinstance(sub, dict) and sub.get("lessons_enabled") is False:
                        return "subtopic has lessons_enabled false"
                    return None
            return f"subtopic {source.get('subtopic')!r} not in topic {topic['name']!r}"
    return f"term {source.get('term')} topic {source.get('topic')!r} not found in {source['file']}"


def _spoken_lines(pack):
    yield "show.line", pack["show"].get("line", "")
    for i, h in enumerate(pack["hints"]):
        yield f"hints[{i}]", h
    for i, r in enumerate(pack["rounds"]):
        yield f"rounds[{i}].prompt", r.get("prompt", "")
        if r.get("praise"):
            yield f"rounds[{i}].praise", r["praise"]
        if r.get("story"):
            yield f"rounds[{i}].story", r["story"]
    btt = pack["beat_the_tutor"]
    for key in ("setup", "tutor_try", "win_line", "gentle_line"):
        if btt.get(key):
            yield f"beat_the_tutor.{key}", btt[key]


def _image_refs(pack):
    if pack["show"].get("image"):
        yield "show.image", pack["show"]["image"]
    for i, r in enumerate(pack["rounds"]):
        if r.get("image"):
            yield f"rounds[{i}].image", r["image"]
        if r["type"] in {"listen_tap", "story_tap", "blend"}:  # picture options
            for opt in r.get("options", []):
                yield f"rounds[{i}].options", opt
        if r["type"] == "match_sort":
            for item in r.get("items", []):
                yield f"rounds[{i}].items", item["image"]
    if pack["beat_the_tutor"].get("image"):
        yield "beat_the_tutor.image", pack["beat_the_tutor"]["image"]


def check_pack(path, pack):
    errs = []
    missing = [k for k in REQUIRED if k not in pack]
    if missing:
        return [f"P1 missing keys {missing}"]
    rel = path.relative_to(CAPS_DIR)
    subject, _, grade_dir, term_dir, fname = rel.parts
    want_id = f"{subject}.{grade_dir}.{term_dir}.{path.stem}"
    if pack["id"] != want_id:
        errs.append(f"P1 id {pack['id']!r} should be {want_id!r}")
    if f"term{pack['term']}" != term_dir or f"grade{pack['grade']}" != grade_dir:
        errs.append("P1 grade/term fields disagree with the path")

    err = _source_ok(pack["source"])
    if err:
        errs.append(f"P2 {err}")

    rounds = pack["rounds"]
    if not 4 <= len(rounds) <= 8:
        errs.append(f"P3 {len(rounds)} rounds (want 4-8)")
    for i, r in enumerate(rounds):
        rtype = r.get("type")
        if rtype not in ROUND_TYPES:
            errs.append(f"P3 rounds[{i}] unknown type {rtype!r}")
            continue
        need = [k for k in ("prompt",) + ROUND_TYPES[rtype] if k not in r]
        if need:
            errs.append(f"P3 rounds[{i}] {rtype} missing {need}")
            continue
        if rtype in TAP_TYPES:
            opts = r["options"]
            if not 2 <= len(opts) <= 4 or len(set(opts)) != len(opts):
                errs.append(f"P4 rounds[{i}] needs 2-4 distinct options")
            if r["answer"] not in opts:
                errs.append(f"P4 rounds[{i}] answer {r['answer']!r} not in options")
        if rtype in ("say_it", "read_to_me") and not r["accept"]:
            errs.append(f"P4 rounds[{i}] empty accept list")
        if rtype == "count_tap" and str(r["count"]) != str(r["answer"]):
            errs.append(f"P4 rounds[{i}] count {r['count']} != answer {r['answer']}")
        if rtype == "match_sort":
            groups = set(r["groups"])
            for item in r["items"]:
                if item.get("group") not in groups:
                    errs.append(f"P4 rounds[{i}] item {item} has no valid group")

    for where, line in _spoken_lines(pack):
        if len(line.split()) > MAX_LINE_WORDS:
            errs.append(f"P5 {where} has {len(line.split())} words (max {MAX_LINE_WORDS})")
        if BRACKET_RE.search(line) or "http" in line:
            errs.append(f"P5 {where} has brackets or a URL: {line!r}")

    images = set(pack["images"])
    for img in images:
        if not SLUG_RE.match(img):
            errs.append(f"P6 image key {img!r} is not a lowercase slug")
    for where, img in _image_refs(pack):
        if img not in images:
            errs.append(f"P6 {where} uses {img!r}, not listed in images")
    return errs


def pack_paths(root=CAPS_DIR):
    return sorted(root.glob(PACK_GLOB))


def run(paths):
    failures, seen = [], {}
    for path in paths:
        try:
            pack = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            failures.append(f"{path}: unreadable: {exc}")
            continue
        for err in check_pack(path, pack):
            failures.append(f"{path.relative_to(REPO)}: {err}")
        pid = pack.get("id")
        if pid in seen:
            failures.append(f"{path.relative_to(REPO)}: P7 id {pid!r} also in {seen[pid]}")
        seen[pid] = path.relative_to(REPO)
    return failures


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("files", nargs="*", help="pack files (default: every pack)")
    args = ap.parse_args(argv)
    paths = [Path(f).resolve() for f in args.files] or pack_paths()
    failures = run(paths)
    for f in failures:
        print(f"FAIL {f}")
    print(f"{len(paths)} pack(s) checked, {len(failures)} problem(s).")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
