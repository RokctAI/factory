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

"""Per-curriculum overlays inside a shared session package (W1 of the
shared-lesson design, ruling of 2026-09-11).

CAPS and IEB learners attend the SAME class and see different things. The
lesson folder stays the contract (release_on_complete's nine content files
are the shared lesson and the CAPS variant), and the parts that differ per
curriculum live in an overlay directory INSIDE that folder:

    <lesson>/overlays/<CURRICULUM>/
        mcq.json                  # same subtopic refs + question ids as the shared file
        comprehension_check.json  # same ids as the shared file
        assistant_qa_transcript.md
        break_qa.md               # the spoken script for the per-curriculum break clip
        exam_weight.md            # the exam-weight note shown to this curriculum
        label.json                # {"curriculum", "badge", "content_basis", ...}

Never overlaid: script.md, intro.md, manim_scene.py, reel_clip.json,
assistant_nervous_script.md and subtopics.json — those carry the shared
worked case, the reel hook and the board's single title set.

Nothing that exists today can see an overlay: release_on_complete's
discover_folders globs exactly six path parts for subtopics.json, and
build_practice_bank globs `grade*/*/*/*/mcq.json`, so `overlays/**` is
invisible to both until a caller asks this module. The manifest contract
built here is ADDITIVE — see build_variants: the top-level `questions`,
`comprehension_check` and `break_start.questions` stay the CAPS variant
byte-for-byte and old players never read the new keys.

Overlay questions may carry `needs_reauthor: true` (set by
extract_curriculum_overlays' case-bound check when a question quotes the
twin package's worked case rather than the shared one). They are carried,
flagged, never silently dropped; the label counts them so a rollout can be
gated per lesson.

The curriculum set comes from the factory-owned registry
(lessons/curriculum/curricula.json via curriculum_target): overlay paths
are generic `overlays/<CURRICULUM>/`, a label's badge, the manifest's
`curricula` order and the R7 membership check all derive from it, so a
curriculum declared "soon" (Cambridge) needs no code change when its
content arrives.

Stdlib only; deterministic output (sorted keys where order is not part of
the contract, two-space JSON, trailing newline).
"""

from __future__ import annotations

import json
from pathlib import Path

import curriculum_target

OVERLAY_DIR = "overlays"
DEFAULT_CURRICULUM = curriculum_target.DEFAULT_CURRICULUM
CURRICULUM_NAME_RE_TEXT = r"^[A-Z][A-Z0-9_]{1,15}$"

OVERLAY_MCQ = "mcq.json"
OVERLAY_COMPREHENSION = "comprehension_check.json"
OVERLAY_TRANSCRIPT = "assistant_qa_transcript.md"
OVERLAY_BREAK_QA = "break_qa.md"
OVERLAY_EXAM_WEIGHT = "exam_weight.md"
OVERLAY_LABEL = "label.json"
OVERLAY_FILES = (
    OVERLAY_MCQ,
    OVERLAY_COMPREHENSION,
    OVERLAY_TRANSCRIPT,
    OVERLAY_BREAK_QA,
    OVERLAY_EXAM_WEIGHT,
    OVERLAY_LABEL,
)

# label.json contract: the keys every overlay label must carry, and the
# value each one is allowed to take when constrained.
LABEL_REQUIRED_KEYS = ("curriculum", "badge", "content_basis")
LABEL_CONTENT_BASIS = DEFAULT_CURRICULUM
BREAK_AUDIO_PENDING = "pending_recording"

# Question flag written by the case-bound check. Carried verbatim through
# the practice bank and the manifest so consumers can gate on it.
NEEDS_REAUTHOR = "needs_reauthor"
CASE_BOUND_TOKENS = "case_bound_tokens"


class OverlayError(ValueError):
    """An overlay directory that does not honour the contract."""


# --- paths ---


def overlay_root(folder) -> Path:
    return Path(folder) / OVERLAY_DIR


def overlay_dir(folder, curriculum: str) -> Path:
    return overlay_root(folder) / curriculum


def list_overlays(folder) -> list[str]:
    """Curricula with an overlay directory carrying a label.json under
    `folder`, sorted so every consumer walks them in the same order."""
    root = overlay_root(folder)
    if not root.is_dir():
        return []
    return sorted(
        p.name for p in root.iterdir() if p.is_dir() and (p / OVERLAY_LABEL).is_file()
    )


def overlay_files(folder) -> list[Path]:
    """Every file under every overlay of `folder`, sorted (for the mojibake
    and compliance gates, which check files, not directories)."""
    root = overlay_root(folder)
    if not root.is_dir():
        return []
    return sorted(p for p in root.rglob("*") if p.is_file())


def break_audio_asset(curriculum: str) -> str:
    """Release asset name of the per-curriculum break clip. The clip is not
    recorded yet for any curriculum; the manifest names the slot and marks
    it pending so W2/W3 can wire playback without a second contract change."""
    return f"break_qa.{curriculum}.mp3"


# --- JSON helpers (one serialisation everywhere the overlay is written) ---


def dumps(data) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def _read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


# --- shape helpers ---


def mcq_ids_by_ref(mcq: dict) -> dict[str, list[str]]:
    """{subtopic_ref: [question id, ...]} in file order."""
    out: dict[str, list[str]] = {}
    for block in (mcq or {}).get("subtopics", []) or []:
        if not isinstance(block, dict) or not block.get("ref"):
            continue
        out[block["ref"]] = [
            q["id"]
            for q in block.get("questions", []) or []
            if isinstance(q, dict) and q.get("id")
        ]
    return out


def mcq_questions(mcq: dict) -> list[dict]:
    return [
        q
        for block in (mcq or {}).get("subtopics", []) or []
        if isinstance(block, dict)
        for q in block.get("questions", []) or []
        if isinstance(q, dict)
    ]


def comprehension_ids(cc: dict) -> list[str]:
    return [
        q["id"]
        for q in (cc or {}).get("questions", []) or []
        if isinstance(q, dict) and q.get("id")
    ]


def comprehension_questions(cc: dict) -> list[dict]:
    return [q for q in (cc or {}).get("questions", []) or [] if isinstance(q, dict)]


def needs_reauthor_count(mcq: dict, cc: dict) -> int:
    return sum(
        1
        for q in mcq_questions(mcq) + comprehension_questions(cc)
        if q.get(NEEDS_REAUTHOR) is True
    )


# --- label ---


def make_label(curriculum: str, source_twin: str = "", **extra) -> dict:
    """The label.json payload. `extra` keys (counts, statuses) are sorted
    into place so the file is deterministic whatever the caller passes.
    Refuses a curriculum the registry does not allow content for."""
    if not curriculum_target.content_allowed(curriculum):
        raise OverlayError(curriculum_target.refusal(curriculum))
    label = {
        "curriculum": curriculum,
        "badge": curriculum_target.badge(curriculum),
        "content_basis": LABEL_CONTENT_BASIS,
        "source_twin": source_twin,
        "break_audio": {
            "asset": break_audio_asset(curriculum),
            "status": BREAK_AUDIO_PENDING,
            "script": f"{OVERLAY_DIR}/{curriculum}/{OVERLAY_BREAK_QA}",
        },
    }
    for key in sorted(extra):
        label[key] = extra[key]
    return label


def validate_label(label, curriculum: str | None = None) -> list[str]:
    """Shape problems in a parsed label.json (empty list = valid)."""
    problems = []
    if not isinstance(label, dict):
        return ["label.json is not a JSON object"]
    for key in LABEL_REQUIRED_KEYS:
        if not isinstance(label.get(key), str) or not label.get(key):
            problems.append(f"label.json: `{key}` must be a non-empty string")
    if curriculum and label.get("curriculum") not in (None, curriculum):
        problems.append(
            f"label.json: curriculum {label.get('curriculum')!r} "
            f"does not match its directory {curriculum!r}"
        )
    declared = label.get("curriculum") or curriculum
    if isinstance(declared, str) and declared:
        if not curriculum_target.content_allowed(declared):
            problems.append(f"label.json: {curriculum_target.refusal(declared)}")
        elif isinstance(label.get("badge"), str) and label["badge"] != (
            curriculum_target.badge(declared)
        ):
            problems.append(
                f"label.json: badge {label['badge']!r} is not the registry "
                f"badge {curriculum_target.badge(declared)!r}"
            )
    if label.get("content_basis") not in (None, LABEL_CONTENT_BASIS):
        problems.append(
            f"label.json: content_basis must be "
            f"{LABEL_CONTENT_BASIS!r} (the shared lesson is the "
            f"{LABEL_CONTENT_BASIS} narration)"
        )
    ba = label.get("break_audio")
    if ba is not None and not (
        isinstance(ba, dict)
        and isinstance(ba.get("asset"), str)
        and isinstance(ba.get("status"), str)
    ):
        problems.append("label.json: break_audio must be {asset, status, ...}")
    return problems


# --- write / read ---


def write_overlay(
    folder,
    curriculum: str,
    *,
    mcq: dict,
    comprehension: dict,
    transcript: str,
    break_qa: str,
    exam_weight: str,
    label: dict,
) -> Path:
    """Write the six overlay files deterministically; returns the overlay
    directory. The caller owns the content (see extract_curriculum_overlays
    for how the twin package is turned into it)."""
    target = overlay_dir(folder, curriculum)
    target.mkdir(parents=True, exist_ok=True)
    (target / OVERLAY_MCQ).write_text(dumps(mcq), encoding="utf-8")
    (target / OVERLAY_COMPREHENSION).write_text(dumps(comprehension), encoding="utf-8")
    (target / OVERLAY_TRANSCRIPT).write_text(transcript, encoding="utf-8")
    (target / OVERLAY_BREAK_QA).write_text(break_qa, encoding="utf-8")
    (target / OVERLAY_EXAM_WEIGHT).write_text(exam_weight, encoding="utf-8")
    (target / OVERLAY_LABEL).write_text(dumps(label), encoding="utf-8")
    return target


def read_overlay(folder, curriculum: str) -> dict:
    """Parsed overlay: {"curriculum", "dir", "mcq", "comprehension",
    "transcript", "break_qa", "exam_weight", "label"}. Missing optional
    files read as empty; a missing label.json is an OverlayError because
    the label is what makes a directory an overlay."""
    target = overlay_dir(folder, curriculum)
    label_path = target / OVERLAY_LABEL
    if not label_path.is_file():
        raise OverlayError(f"{target}: no {OVERLAY_LABEL}")

    def text(name):
        p = target / name
        return p.read_text(encoding="utf-8") if p.is_file() else ""

    def data(name, default):
        p = target / name
        return _read_json(p) if p.is_file() else default

    return {
        "curriculum": curriculum,
        "dir": target,
        "mcq": data(OVERLAY_MCQ, {"subtopics": []}),
        "comprehension": data(OVERLAY_COMPREHENSION, {"questions": []}),
        "transcript": text(OVERLAY_TRANSCRIPT),
        "break_qa": text(OVERLAY_BREAK_QA),
        "exam_weight": text(OVERLAY_EXAM_WEIGHT),
        "label": _read_json(label_path),
    }


def read_all_overlays(folder) -> list[dict]:
    return [read_overlay(folder, c) for c in list_overlays(folder)]


# --- validation (R7: overlay ids ⊆ shared ids, label shape) ---


def validate_overlay(
    overlay: dict, shared_mcq: dict, shared_comprehension: dict
) -> list[str]:
    """R7 problems for one parsed overlay against the shared package files
    (empty list = compliant):

      * every overlay subtopic ref exists in the shared mcq.json (a ref the
        board never reaches would be a question nobody is asked);
      * every overlay comprehension id exists in the shared file;
      * question ids inside a ref may differ (the manifest then supplies
        `exercise_by_ref`), but must be unique within the overlay;
      * label.json has the contract shape; `needs_reauthor`, when present,
        is a boolean.
    """
    curriculum = overlay["curriculum"]
    problems = [
        f"{curriculum}: {p}" for p in validate_label(overlay["label"], curriculum)
    ]
    shared_refs = set(mcq_ids_by_ref(shared_mcq))
    overlay_refs = mcq_ids_by_ref(overlay["mcq"])
    for ref in overlay_refs:
        if ref not in shared_refs:
            problems.append(
                f"{curriculum}: {OVERLAY_MCQ} ref {ref!r} is not "
                "a subtopic of the shared mcq.json"
            )
    seen: set[str] = set()
    for ref, ids in overlay_refs.items():
        for qid in ids:
            if qid in seen:
                problems.append(
                    f"{curriculum}: {OVERLAY_MCQ} duplicate question id {qid!r}"
                )
            seen.add(qid)
    shared_cc = set(comprehension_ids(shared_comprehension))
    for cid in comprehension_ids(overlay["comprehension"]):
        if cid not in shared_cc:
            problems.append(
                f"{curriculum}: {OVERLAY_COMPREHENSION} id "
                f"{cid!r} is not in the shared file"
            )
    for q in mcq_questions(overlay["mcq"]) + comprehension_questions(
        overlay["comprehension"]
    ):
        flag = q.get(NEEDS_REAUTHOR)
        if flag is not None and not isinstance(flag, bool):
            problems.append(
                f"{curriculum}: question {q.get('id')!r} "
                f"{NEEDS_REAUTHOR} must be a boolean"
            )
    return problems


# --- manifest variants (additive) ---


def _bank(questions: list[dict]) -> dict:
    return {q["id"]: q for q in questions if q.get("id")}


def build_variants(
    folder,
    shared_mcq: dict,
    shared_comprehension: dict,
    break_questions: list[dict],
    *,
    break_question_extractor,
    default_curriculum: str = DEFAULT_CURRICULUM,
) -> dict:
    """The additive manifest block for a package, or {} when the package
    has no overlay (so a package without overlays assembles byte-identically
    to before this module existed).

    Returns {"curricula": [...], "default_curriculum": ..., "variants":
    {<curriculum>: {...}}}. The default variant is built from the shared
    files (the same banks the manifest already carries at top level); each
    overlay variant from its own files. `exercise_by_ref` is emitted only
    when an overlay's question ids under a ref differ from the shared
    layout, because `subtopic_end.exercise` keeps the shared id list.
    `break_question_extractor(transcript_md)` is the same extractor the
    caller used for the top-level break list, so both variants reduce a
    transcript identically; break questions are only emitted when the
    caller emitted them (two-part lessons)."""
    overlays = read_all_overlays(folder)
    if not overlays:
        return {}
    for ov in overlays:
        if not curriculum_target.content_allowed(ov["curriculum"]):
            raise OverlayError(
                f"{ov['dir']}: {curriculum_target.refusal(ov['curriculum'])}"
            )
    shared_layout = mcq_ids_by_ref(shared_mcq)
    variants = {
        default_curriculum: {
            "label": {
                "curriculum": default_curriculum,
                "badge": curriculum_target.badge(default_curriculum),
                "content_basis": LABEL_CONTENT_BASIS,
            },
            "questions": _bank(mcq_questions(shared_mcq)),
            "comprehension_check": _bank(comprehension_questions(shared_comprehension)),
            "break_questions": list(break_questions),
            "break_audio": None,
            "break_audio_status": {
                "asset": break_audio_asset(default_curriculum),
                "status": BREAK_AUDIO_PENDING,
                # Today the default break rides inside audio.mp3; the
                # separate clip is the target so both curricula play the
                # same way (spec §4.3 / Q3).
                "fallback": "inline in audio.mp3",
            },
            "exam_weight": None,
            "needs_reauthor": 0,
        }
    }
    for ov in overlays:
        curriculum = ov["curriculum"]
        label = dict(ov["label"])
        ba = label.get("break_audio") or {}
        variant = {
            "label": {
                k: label[k]
                for k in ("curriculum", "badge", "content_basis", "sag_status")
                if k in label
            },
            "questions": _bank(mcq_questions(ov["mcq"])),
            "comprehension_check": _bank(comprehension_questions(ov["comprehension"])),
            "break_questions": (
                break_question_extractor(ov["transcript"]) if break_questions else []
            ),
            "break_audio": None,
            "break_audio_status": {
                "asset": ba.get("asset") or break_audio_asset(curriculum),
                "status": ba.get("status") or BREAK_AUDIO_PENDING,
                "script": f"{OVERLAY_DIR}/{curriculum}/{OVERLAY_BREAK_QA}",
            },
            "exam_weight": ov["exam_weight"].strip() or None,
            "needs_reauthor": needs_reauthor_count(ov["mcq"], ov["comprehension"]),
        }
        layout = mcq_ids_by_ref(ov["mcq"])
        differing = {
            ref: ids for ref, ids in layout.items() if shared_layout.get(ref) != ids
        }
        if differing:
            variant["exercise_by_ref"] = differing
        variants[curriculum] = variant
    # Registry order (the display order), never a second hard-coded list;
    # only curricula this package actually carries are listed.
    curricula = curriculum_target.ordered(variants)
    return {
        "curricula": curricula,
        "default_curriculum": default_curriculum,
        "variants": {c: variants[c] for c in curricula},
    }
