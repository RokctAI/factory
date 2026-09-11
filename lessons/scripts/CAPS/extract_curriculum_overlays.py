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

"""Derive per-curriculum overlays from a twin session tree (W1).

For every shared package under lessons/curriculum/CAPS/<subject>/session/...
that has a twin at the same relative path under the twin root (default
lessons/curriculum/<CURRICULUM>), write

    <package>/overlays/<CURRICULUM>/{mcq.json, comprehension_check.json,
        assistant_qa_transcript.md, break_qa.md, exam_weight.md, label.json}

from the twin's mcq.json, comprehension_check.json and
assistant_qa_transcript.md. NEVER copied: script.md, intro.md,
manim_scene.py, reel_clip.json, assistant_nervous_script.md and
subtopics.json — those carry the twin's swapped worked case and reel hook;
the shared lesson keeps the CAPS narration and the CAPS id/tag.

The twin tree is READ ONLY here: nothing under the twin root is written,
moved or deleted (its retirement is a separate decision).

CASE-BOUND CHECK. A twin is a re-narration around a different worked case
(a different principal and rate, different letters in the anchor
expression), and its questions quote THAT case. Lifted verbatim, an
overlay question would ask about numbers the shared audio never taught.
So every overlay question is checked: the value tokens it quotes
(numerals, currency amounts, percentages, algebraic terms such as `3mp`,
capitalised names) are looked up in both scripts, with spoken forms
("four thousand", "three m p", "seven percent") normalised to match the
written ones. A question quoting a token that the TWIN script teaches and
the SHARED script never mentions is case-bound: it is written into the
overlay with `needs_reauthor: true` and `case_bound_tokens: [...]`,
never dropped and never silently copied as trusted. Questions that quote
nothing twin-specific go in as-is. The same check runs over the break
asks (the questions the board shows during the break).

ALIGNMENT is asserted, not repaired: subtopic refs, per-ref question-id
layout, comprehension ids and subtopic structure are compared with the
shared files and every mismatch is listed in the report (the manifest
supplies `exercise_by_ref` for a differing layout at assembly time).

REPORT: lessons/overlay_extraction_report.json (machine) and
lessons/overlay_extraction_report.md (readable) — per-lesson counts, the
case-bound items, the alignment mismatches, and the list of shared files
whose copy names "CAPS" (the wording pass is a separate content job; this
script only lists them).

Deterministic and stdlib only: no timestamps, sorted scans, one JSON
serialisation, so a re-run on unchanged input produces no diff and
`--check` can prove the committed overlays still match their twins.

Usage:
  python3 lessons/scripts/CAPS/extract_curriculum_overlays.py              # write overlays + report
  python3 lessons/scripts/CAPS/extract_curriculum_overlays.py --check      # drift: exit 1 if any overlay differs
  python3 lessons/scripts/CAPS/extract_curriculum_overlays.py --filter maths/session/grade10
"""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import curriculum_overlay as co  # noqa: E402
import curriculum_target  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[3]
SHARED_ROOT = REPO_ROOT / "lessons" / "curriculum" / co.DEFAULT_CURRICULUM
CURRICULA_ROOT = REPO_ROOT / "lessons" / "curriculum"
REPORT_JSON = REPO_ROOT / "lessons" / "overlay_extraction_report.json"
REPORT_MD = REPO_ROOT / "lessons" / "overlay_extraction_report.md"
GENERATED_BY = "lessons/scripts/CAPS/extract_curriculum_overlays.py"

# The twin files an overlay is derived from, and the ones it must never take.
TWIN_SOURCES = ("mcq.json", "comprehension_check.json", "assistant_qa_transcript.md")
NEVER_COPIED = (
    "script.md",
    "intro.md",
    "manim_scene.py",
    "reel_clip.json",
    "assistant_nervous_script.md",
    "subtopics.json",
)
# Shared package files scanned for the curriculum-name wording list.
SHARED_COPY_FILES = (
    "script.md",
    "intro.md",
    "mcq.json",
    "comprehension_check.json",
    "assistant_qa_transcript.md",
    "assistant_nervous_script.md",
    "subtopics.json",
    "reel_clip.json",
)
CAPS_WORD_RE = re.compile(r"\bCAPS\b")


# --- value tokens (the case-bound vocabulary) ---

UNITS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
}
TENS = {
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
}
SCALES = {"hundred": 100, "thousand": 1000, "million": 1000000}
DECIMAL_WORDS = ("point", "comma")
NUMBER_WORDS = set(UNITS) | set(TENS) | set(SCALES)
# Function names that look like algebraic letter clusters but are not values.
NOT_TERMS = {
    "sin",
    "cos",
    "tan",
    "log",
    "ln",
    "exp",
    "sec",
    "csc",
    "cot",
    "and",
    "or",
    "of",
    "the",
    "for",
    "per",
    "to",
    "in",
    "on",
    "at",
    "is",
    "if",
    "so",
    "as",
    "by",
    "be",
    "it",
    "an",
    "no",
    "up",
    "km",
    "cm",
    "mm",
    "kg",
    "ml",
    "hr",
    "am",
    "pm",
    "one",
    "two",
    "six",
    "ten",
}
# Capitalised words that are never a case name.
NOT_NAMES = {
    "Grade",
    "CAPS",
    "IEB",
    "Rand",
    "Paper",
    "Term",
    "Part",
    "Subtopic",
    "Tutor",
    "Student",
    "Question",
    "Questions",
    "Answer",
    "Section",
    "Step",
    "Table",
    "Figure",
}

# Numerals: SA style thousands (`4 000`), comma or point decimals (`0,07`),
# an optional glued algebraic suffix (`3mp`); a currency `R` is split off
# by _normalise_text first so the lookbehind sees a word boundary.
NUMBER_RE = re.compile(
    r"(?<![\w.])(\d{1,3}(?: \d{3})+|\d+)(?:[.,](\d+))?"
    r"(?:([a-zA-Z]{1,3})\b)?"
)
# Letter clusters that sit against a maths operator (`− np`, `nq =`); the
# ASCII hyphen only counts when spaced like an operator (see
# _normalise_text), so `one-sentence` and `hen-coop` are not terms.
OPERATORS = "+−=×÷/^"
TERM_AFTER_OP_RE = re.compile(rf"[{OPERATORS}(]\s*([a-z]{{2,3}})\b")
TERM_BEFORE_OP_RE = re.compile(rf"\b([a-z]{{2,3}})\s*(?=[{OPERATORS})])")
NAME_RE = re.compile(r"\b([A-Z][a-z]{2,})\b")
WORD_RE = re.compile(r"[a-z]+|\d+")


def _normalise_text(text: str) -> str:
    """One spelling for the characters the token regexes key on: NBSP ->
    space, dashes -> punctuation, a spaced ASCII hyphen -> true minus,
    a currency R split from its digits."""
    text = (
        text.replace("\u00a0", " ")
        .replace("\u202f", " ")
        .replace("—", " ; ")
        .replace("–", " ; ")
        .replace(" - ", " − ")
    )
    return re.sub(r"\bR(?=\d)", "R ", text)


def _number(int_part: str, frac_part: str = "") -> str:
    """Canonical numeric string: no thousands separators, `.` decimal,
    no leading/trailing zero padding (4 000 -> 4000, 0,070 -> 0.07)."""
    ip = int_part.replace(" ", "").replace(" ", "").lstrip("0") or "0"
    fp = (frac_part or "").rstrip("0")
    return f"{ip}.{fp}" if fp else ip


def item_tokens(text: str) -> set[str]:
    """Value tokens quoted by one question (question + options / answer)."""
    text = _normalise_text(text)
    tokens: set[str] = set()
    for m in NUMBER_RE.finditer(text):
        int_part, frac_part, suffix = m.group(1), m.group(2), m.group(3)
        number = _number(int_part, frac_part)
        tokens.add(number)
        if suffix and not frac_part and suffix.lower() not in NOT_TERMS:
            tokens.add(number + suffix.lower())
    for rx in (TERM_AFTER_OP_RE, TERM_BEFORE_OP_RE):
        for m in rx.finditer(text):
            term = m.group(1)
            if term not in NOT_TERMS:
                tokens.add(term)
    for name in capitalised_names(text):
        tokens.add(name)
    return tokens


def capitalised_names(text: str) -> set[str]:
    """Capitalised words that are not at a sentence start (a name inside a
    sentence, e.g. "when Thabo invests"), minus the never-a-name list."""
    names = set()
    for m in NAME_RE.finditer(text):
        before = text[: m.start()].rstrip(" \t")
        if not before or before[-1] in ".?!:\n\"'(":
            continue
        if m.group(1) not in NOT_NAMES:
            names.add(m.group(1))
    return names


def _words_value(words: list[str]) -> int:
    total, current = 0, 0
    for w in words:
        if w in UNITS:
            current += UNITS[w]
        elif w in TENS:
            current += TENS[w]
        elif w == "hundred":
            current = max(current, 1) * 100
        elif w in SCALES:
            total += max(current, 1) * SCALES[w]
            current = 0
    return total + current


def _fraction_words(words: list[str]) -> str:
    if words and all(w in UNITS and UNITS[w] < 10 for w in words):
        return "".join(str(UNITS[w]) for w in words)
    return str(_words_value(words)) if words else ""


def script_vocabulary(script_md: str) -> set[str]:
    """Every value token a script teaches, written or spoken: literal
    numerals (`R4 000`, `7%`), spelled numbers (`four thousand`,
    `seven percent`, `zero comma zero seven`), spoken algebraic terms
    (`three m p` -> `3mp`, `n p` -> `np`) and capitalised words."""
    text = _normalise_text(script_md)
    vocab = item_tokens(text)
    # A script teaches a name wherever it says it, sentence-initial or not
    # (the item side keeps the sentence-start guard).
    vocab.update(n for n in NAME_RE.findall(text) if n not in NOT_NAMES)
    words = WORD_RE.findall(text.lower().replace("-", " "))
    i, n = 0, len(words)
    while i < n:
        w = words[i]
        if w in NUMBER_WORDS:
            j = i
            run = []
            while j < n and (
                words[j] in NUMBER_WORDS
                or (
                    words[j] == "and"
                    and run
                    and j + 1 < n
                    and words[j + 1] in NUMBER_WORDS
                )
            ):
                if words[j] != "and":
                    run.append(words[j])
                j += 1
            int_part = str(_words_value(run))
            frac = ""
            if j < n and words[j] in DECIMAL_WORDS:
                k = j + 1
                frac_words = []
                while k < n and words[k] in NUMBER_WORDS:
                    frac_words.append(words[k])
                    k += 1
                if frac_words:
                    frac = _fraction_words(frac_words)
                    j = k
            number = _number(int_part, frac)
            vocab.add(number)
            letters = []
            k = j
            while (
                k < n and len(words[k]) == 1 and words[k].isalpha() and len(letters) < 3
            ):
                letters.append(words[k])
                k += 1
            if letters and not frac:
                vocab.add(number + "".join(letters))
            i = max(j, i + 1)
            continue
        if len(w) == 1 and w.isalpha():
            letters = []
            k = i
            while (
                k < n and len(words[k]) == 1 and words[k].isalpha() and len(letters) < 3
            ):
                letters.append(words[k])
                k += 1
            if 2 <= len(letters) <= 3:
                vocab.add("".join(letters))
            i = k
            continue
        i += 1
    return vocab


def case_bound_tokens(
    item_text: str, twin_vocab: set[str], shared_vocab: set[str]
) -> list[str]:
    """Tokens the item quotes that the twin script teaches and the shared
    script never mentions — sorted, empty when the item is safe."""
    return sorted(
        t for t in item_tokens(item_text) if t in twin_vocab and t not in shared_vocab
    )


def mcq_item_text(q: dict) -> str:
    parts = [str(q.get("question", ""))]
    parts += [str(o) for o in q.get("options", []) or []]
    return "\n".join(parts)


def comprehension_item_text(q: dict) -> str:
    return f"{q.get('question', '')}\n{q.get('expected_answer', '')}"


# --- derivation ---


def _read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def flag_questions(questions: list[dict], text_of, twin_vocab, shared_vocab):
    """Mutates each question in place: sets needs_reauthor/case_bound_tokens
    when case-bound, clears stale flags otherwise. Returns the flagged
    [(id, tokens)]."""
    flagged = []
    for q in questions:
        tokens = case_bound_tokens(text_of(q), twin_vocab, shared_vocab)
        q.pop(co.NEEDS_REAUTHOR, None)
        q.pop(co.CASE_BOUND_TOKENS, None)
        if tokens:
            q[co.NEEDS_REAUTHOR] = True
            q[co.CASE_BOUND_TOKENS] = tokens
            flagged.append((q.get("id"), tokens))
    return flagged


def break_qa_text(curriculum: str, ident: str, transcript: str) -> str:
    """The spoken script for the per-curriculum break clip: the twin's
    Q&A transcript verbatim under a header naming the clip it becomes."""
    return (
        f"# Break Q&A — {curriculum} variant\n\n"
        f"lesson: {ident}\n"
        f"clip: {co.break_audio_asset(curriculum)}\n"
        f"status: {co.BREAK_AUDIO_PENDING}\n\n"
        "This is the recording script for the break segment played to "
        f"{curriculum} learners in place of the shared break. The asks "
        "are the break-board questions; the Tutor turns are spoken.\n\n"
        "***\n\n" + transcript.rstrip("\n") + "\n"
    )


def exam_weight_text(curriculum: str) -> str:
    return (
        f"{curriculum} exam weighting: pending SAG ingestion. The shared "
        "lesson's exam-weight figures describe DBE papers and must not "
        f"be shown in a {curriculum} context (see the skills layer's "
        "overrides_pending).\n"
    )


def alignment(
    shared_folder: Path, twin_folder: Path, twin_mcq: dict, twin_cc: dict
) -> dict:
    shared_mcq = _read_json(shared_folder / "mcq.json")
    shared_cc = _read_json(shared_folder / "comprehension_check.json")
    shared_layout = co.mcq_ids_by_ref(shared_mcq)
    twin_layout = co.mcq_ids_by_ref(twin_mcq)
    subtopics_match = None
    shared_subs, twin_subs = (
        shared_folder / "subtopics.json",
        twin_folder / "subtopics.json",
    )
    if shared_subs.is_file() and twin_subs.is_file():
        s_refs = [s.get("ref") for s in _read_json(shared_subs).get("subtopics", [])]
        t_refs = [s.get("ref") for s in _read_json(twin_subs).get("subtopics", [])]
        subtopics_match = s_refs == t_refs
    return {
        "mcq_refs_match": list(shared_layout) == list(twin_layout),
        "mcq_refs_subset": set(twin_layout) <= set(shared_layout),
        "mcq_layout_match": shared_layout == twin_layout,
        "comprehension_ids_match": (
            co.comprehension_ids(shared_cc) == co.comprehension_ids(twin_cc)
        ),
        "subtopic_refs_match": subtopics_match,
    }


def derive_overlay(
    shared_folder: Path, twin_folder: Path, curriculum: str, ident: str, break_extractor
) -> dict:
    """Overlay content + per-lesson report entry for one package. Reads
    the twin, never writes it."""
    twin_mcq = copy.deepcopy(_read_json(twin_folder / "mcq.json"))
    twin_cc = copy.deepcopy(_read_json(twin_folder / "comprehension_check.json"))
    transcript = (twin_folder / "assistant_qa_transcript.md").read_text("utf-8")
    twin_vocab = script_vocabulary((twin_folder / "script.md").read_text("utf-8"))
    shared_vocab = script_vocabulary((shared_folder / "script.md").read_text("utf-8"))

    mcq_flagged = flag_questions(
        co.mcq_questions(twin_mcq), mcq_item_text, twin_vocab, shared_vocab
    )
    cc_flagged = flag_questions(
        co.comprehension_questions(twin_cc),
        comprehension_item_text,
        twin_vocab,
        shared_vocab,
    )
    asks = break_extractor(transcript)
    ask_flagged = [
        (i + 1, tokens)
        for i, a in enumerate(asks)
        if (
            tokens := case_bound_tokens(a.get("question", ""), twin_vocab, shared_vocab)
        )
    ]
    align = alignment(shared_folder, twin_folder, twin_mcq, twin_cc)
    needs = len(mcq_flagged) + len(cc_flagged)
    label = co.make_label(
        curriculum,
        source_twin=str(twin_folder.relative_to(REPO_ROOT)).replace("\\", "/")
        if twin_folder.is_relative_to(REPO_ROOT)
        else str(twin_folder),
        sag_status="pending_fetch",
        needs_reauthor=needs,
        break_asks_case_bound=len(ask_flagged),
        alignment={
            k: v
            for k, v in align.items()
            if k in ("mcq_layout_match", "comprehension_ids_match")
        },
        generated_by=GENERATED_BY,
    )
    content = {
        "mcq": twin_mcq,
        "comprehension": twin_cc,
        "transcript": transcript,
        "break_qa": break_qa_text(curriculum, ident, transcript),
        "exam_weight": exam_weight_text(curriculum),
        "label": label,
    }
    entry = {
        "id": ident,
        "mcq": {
            "total": len(co.mcq_questions(twin_mcq)),
            "case_bound": [{"id": i, "tokens": t} for i, t in mcq_flagged],
        },
        "comprehension": {
            "total": len(co.comprehension_questions(twin_cc)),
            "case_bound": [{"id": i, "tokens": t} for i, t in cc_flagged],
        },
        "break_asks": {
            "total": len(asks),
            "case_bound": [{"ask": i, "tokens": t} for i, t in ask_flagged],
        },
        "alignment": align,
    }
    return {"content": content, "report": entry}


def rendered_files(content: dict) -> dict[str, str]:
    """The exact bytes write_overlay produces, keyed by file name (for
    --check without touching disk)."""
    return {
        co.OVERLAY_MCQ: co.dumps(content["mcq"]),
        co.OVERLAY_COMPREHENSION: co.dumps(content["comprehension"]),
        co.OVERLAY_TRANSCRIPT: content["transcript"],
        co.OVERLAY_BREAK_QA: content["break_qa"],
        co.OVERLAY_EXAM_WEIGHT: content["exam_weight"],
        co.OVERLAY_LABEL: co.dumps(content["label"]),
    }


# --- scan ---


def discover_packages(root: Path) -> list[Path]:
    return sorted(p.parent for p in root.glob("*/session/*/*/*/*/subtopics.json"))


def lesson_id(folder: Path, root: Path) -> str:
    subject, _s, grade, _term, topic, sub = folder.relative_to(root).parts
    return f"{subject}_g{re.sub(r'[^0-9]', '', grade)}_{topic}_{sub}"


def caps_wording(root: Path, packages: list[Path]) -> list[dict]:
    out = []
    for folder in packages:
        for name in SHARED_COPY_FILES:
            p = folder / name
            if not p.is_file():
                continue
            hits = len(CAPS_WORD_RE.findall(p.read_text(encoding="utf-8")))
            if hits:
                out.append(
                    {
                        "file": str(p.relative_to(REPO_ROOT)).replace("\\", "/")
                        if p.is_relative_to(REPO_ROOT)
                        else str(p),
                        "mentions": hits,
                    }
                )
    return out


def render_report_md(report: dict) -> str:
    s = report["summary"]
    lines = [
        f"# Curriculum overlay extraction — {report['curriculum']}",
        "",
        f"Generated by `{GENERATED_BY}`; the JSON twin of this file is the "
        "machine-readable record. Deterministic: re-running on unchanged "
        "input produces no diff.",
        "",
        "## Headline",
        "",
        "| Measure | Count |",
        "| --- | ---: |",
        f"| Shared packages scanned | {s['packages_scanned']} |",
        f"| Packages with a twin under `{report['twin_root']}` | {s['packages_with_twin']} |",
        f"| Overlays written | {s['overlays_written']} |",
        f"| MCQ items copied | {s['mcq_items']} |",
        f"| MCQ items case-bound (`needs_reauthor`) | {s['mcq_case_bound']} |",
        f"| Comprehension items copied | {s['comprehension_items']} |",
        f"| Comprehension items case-bound (`needs_reauthor`) | {s['comprehension_case_bound']} |",
        f"| Break asks | {s['break_asks']} |",
        f"| Break asks case-bound | {s['break_asks_case_bound']} |",
        f"| Lessons with at least one case-bound item | {s['lessons_with_case_bound']} |",
        f"| Lessons with every item clean | {s['lessons_clean']} |",
        f"| MCQ id-layout mismatches (listed, not fixed) | {s['mcq_layout_mismatches']} |",
        f"| Comprehension id mismatches | {s['comprehension_id_mismatches']} |",
        f"| Subtopic-structure mismatches | {s['subtopic_mismatches']} |",
        f'| Shared files naming "CAPS" (wording follow-up) | {s["caps_wording_files"]} |',
        "",
        "## How case-bound is decided",
        "",
        "A question's value tokens (numerals, currency amounts, percentages, "
        "algebraic terms such as `3mp`, capitalised names) are looked up in "
        "both scripts with spoken forms normalised (`four thousand`, "
        "`three m p`, `seven percent`). A token the twin script teaches and "
        "the shared script never mentions marks the item `needs_reauthor: "
        "true` in the overlay JSON; it is carried, never dropped. Items that "
        "quote nothing twin-specific go in as-is.",
        "",
        "## Lessons with case-bound items or alignment mismatches",
        "",
        "| Lesson | MCQ case-bound / total | Comprehension case-bound / total "
        "| Break asks case-bound / total | MCQ layout | Comprehension ids | Subtopics |",
        "| --- | ---: | ---: | ---: | --- | --- | --- |",
    ]
    for entry in report["lessons"]:
        a = entry["alignment"]
        flagged = (
            entry["mcq"]["case_bound"]
            or entry["comprehension"]["case_bound"]
            or entry["break_asks"]["case_bound"]
        )
        mismatch = not (
            a["mcq_layout_match"]
            and a["comprehension_ids_match"]
            and a["subtopic_refs_match"] is not False
        )
        if not (flagged or mismatch):
            continue

        def yn(v):
            return "same" if v else ("differs" if v is False else "n/a")

        lines.append(
            f"| `{entry['id']}` "
            f"| {len(entry['mcq']['case_bound'])} / {entry['mcq']['total']} "
            f"| {len(entry['comprehension']['case_bound'])} / {entry['comprehension']['total']} "
            f"| {len(entry['break_asks']['case_bound'])} / {entry['break_asks']['total']} "
            f"| {yn(a['mcq_layout_match'])} | {yn(a['comprehension_ids_match'])} "
            f"| {yn(a['subtopic_refs_match'])} |"
        )
    lines += [
        "",
        '## Shared files that name "CAPS" (wording follow-up, not changed here)',
        "",
        "The shared lesson is heard by both curricula. These files say "
        '"CAPS" in copy; neutralising the wording is a follow-up content '
        "pass (spec Q2), listed here so it can be scoped.",
        "",
    ]
    for hit in report["caps_wording"]["files"]:
        lines.append(f"- `{hit['file']}` ({hit['mentions']})")
    lines.append("")
    return "\n".join(lines)


def run(
    shared_root: Path,
    twin_root: Path,
    curriculum: str,
    *,
    check: bool,
    filter_text: str,
    break_extractor,
    report_json: Path | None,
    report_md: Path | None,
    out=print,
) -> tuple[int, dict]:
    packages = [
        p
        for p in discover_packages(shared_root)
        if not filter_text or filter_text in str(p)
    ]
    lessons, drift, written = [], [], 0
    mcq_items = mcq_cb = cc_items = cc_cb = asks = asks_cb = 0
    with_twin = 0
    for folder in packages:
        twin = twin_root / folder.relative_to(shared_root)
        if not all((twin / n).is_file() for n in TWIN_SOURCES):
            continue
        with_twin += 1
        ident = lesson_id(folder, shared_root)
        derived = derive_overlay(folder, twin, curriculum, ident, break_extractor)
        files = rendered_files(derived["content"])
        target = co.overlay_dir(folder, curriculum)
        if check:
            for name, text in files.items():
                p = target / name
                if not p.is_file():
                    drift.append(f"{p}: missing")
                elif p.read_text(encoding="utf-8") != text:
                    drift.append(f"{p}: differs from its twin-derived content")
        else:
            co.write_overlay(folder, curriculum, **derived["content"])
            written += 1
        entry = derived["report"]
        entry["lesson"] = str(folder.relative_to(shared_root)).replace("\\", "/")
        lessons.append(entry)
        mcq_items += entry["mcq"]["total"]
        mcq_cb += len(entry["mcq"]["case_bound"])
        cc_items += entry["comprehension"]["total"]
        cc_cb += len(entry["comprehension"]["case_bound"])
        asks += entry["break_asks"]["total"]
        asks_cb += len(entry["break_asks"]["case_bound"])
    wording = caps_wording(shared_root, packages)
    flagged_lessons = sum(
        1
        for e in lessons
        if e["mcq"]["case_bound"]
        or e["comprehension"]["case_bound"]
        or e["break_asks"]["case_bound"]
    )
    report = {
        "generated_by": GENERATED_BY,
        "curriculum": curriculum,
        "shared_root": str(shared_root.relative_to(REPO_ROOT)).replace("\\", "/")
        if shared_root.is_relative_to(REPO_ROOT)
        else str(shared_root),
        "twin_root": str(twin_root.relative_to(REPO_ROOT)).replace("\\", "/")
        if twin_root.is_relative_to(REPO_ROOT)
        else str(twin_root),
        "never_copied": list(NEVER_COPIED),
        "summary": {
            "packages_scanned": len(packages),
            "packages_with_twin": with_twin,
            "overlays_written": written,
            "mcq_items": mcq_items,
            "mcq_case_bound": mcq_cb,
            "comprehension_items": cc_items,
            "comprehension_case_bound": cc_cb,
            "break_asks": asks,
            "break_asks_case_bound": asks_cb,
            "items_total": mcq_items + cc_items,
            "items_case_bound": mcq_cb + cc_cb,
            "lessons_with_case_bound": flagged_lessons,
            "lessons_clean": len(lessons) - flagged_lessons,
            "mcq_layout_mismatches": sum(
                1 for e in lessons if not e["alignment"]["mcq_layout_match"]
            ),
            "comprehension_id_mismatches": sum(
                1 for e in lessons if not e["alignment"]["comprehension_ids_match"]
            ),
            "subtopic_mismatches": sum(
                1 for e in lessons if e["alignment"]["subtopic_refs_match"] is False
            ),
            "caps_wording_files": len(wording),
        },
        "lessons": lessons,
        "caps_wording": {"count": len(wording), "files": wording},
    }
    if not check:
        if report_json:
            report_json.parent.mkdir(parents=True, exist_ok=True)
            report_json.write_text(co.dumps(report), encoding="utf-8")
        if report_md:
            report_md.write_text(render_report_md(report), encoding="utf-8")
    s = report["summary"]
    out(
        f"[overlays] {curriculum}: {s['packages_scanned']} shared packages, "
        f"{s['packages_with_twin']} with a twin, "
        f"{'checked' if check else 'written'} "
        f"{s['packages_with_twin'] if check else written}"
    )
    out(
        f"[case-bound] MCQ {s['mcq_case_bound']}/{s['mcq_items']}, "
        f"comprehension {s['comprehension_case_bound']}/{s['comprehension_items']}, "
        f"break asks {s['break_asks_case_bound']}/{s['break_asks']}; "
        f"lessons flagged {s['lessons_with_case_bound']}, "
        f"clean {s['lessons_clean']}"
    )
    out(
        f"[alignment] mcq layout mismatches {s['mcq_layout_mismatches']}, "
        f"comprehension id mismatches {s['comprehension_id_mismatches']}, "
        f"subtopic mismatches {s['subtopic_mismatches']}"
    )
    out(
        f"[wording] {s['caps_wording_files']} shared file(s) name CAPS "
        "(follow-up, unchanged)"
    )
    if check:
        for d in drift[:40]:
            out(f"  [drift] {d}")
        if len(drift) > 40:
            out(f"  ... and {len(drift) - 40} more")
        out(
            f"[check] {'DRIFT: ' + str(len(drift)) + ' file(s)' if drift else 'overlays match their twins'}"
        )
        return (1 if drift else 0), report
    return 0, report


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument(
        "--curriculum",
        default="IEB",
        help="overlay curriculum (directory name under "
        "lessons/curriculum and overlays/)",
    )
    ap.add_argument(
        "--root", default=str(SHARED_ROOT), help="shared (CAPS) curriculum root"
    )
    ap.add_argument(
        "--twin-root",
        default="",
        help="twin tree root; default lessons/curriculum/<curriculum>",
    )
    ap.add_argument(
        "--filter", default="", help="only packages whose path contains this substring"
    )
    ap.add_argument(
        "--check",
        action="store_true",
        help="drift mode: derive in memory and compare with the "
        "committed overlays; exit 1 on any difference",
    )
    ap.add_argument("--report-json", default=str(REPORT_JSON))
    ap.add_argument("--report-md", default=str(REPORT_MD))
    ap.add_argument("--no-report", action="store_true")
    args = ap.parse_args(argv)
    if not re.match(co.CURRICULUM_NAME_RE_TEXT, args.curriculum):
        ap.error(f"--curriculum must match {co.CURRICULUM_NAME_RE_TEXT}")
    if not curriculum_target.content_allowed(args.curriculum):
        ap.error(f"--curriculum: {curriculum_target.refusal(args.curriculum)}")
    shared_root = Path(args.root)
    twin_root = (
        Path(args.twin_root) if args.twin_root else CURRICULA_ROOT / args.curriculum
    )
    if not twin_root.is_dir():
        print(f"[error] twin root {twin_root} does not exist")
        return 1
    import release_on_complete as roc  # noqa: E402  (sibling module)

    code, _report = run(
        shared_root,
        twin_root,
        args.curriculum,
        check=args.check,
        filter_text=args.filter,
        break_extractor=roc.extract_session_break_questions,
        report_json=None if args.no_report else Path(args.report_json),
        report_md=None if args.no_report else Path(args.report_md),
    )
    return code


if __name__ == "__main__":
    raise SystemExit(main())
