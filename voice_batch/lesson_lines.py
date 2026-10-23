"""Lesson audio: who speaks which part of a session package, as render items.

A session package (lessons repo, school/curriculum/CAPS/<subject>/session/
grade<N>/term<N>/<topic>/<lesson>) has three speakers:

  first tutor (expert)   intro.md, script.md up to "# Part 2" (all of it in a
                         single-voice lesson), the Tutor turns of
                         assistant_qa_transcript.md
  second tutor           script.md from "# Part 2" on
  host (grade assistant) the asking turns of assistant_qa_transcript.md and
                         assistant_nervous_script.md

Each part renders as soon as ITS speaker has an approved voice
(lesson_voices.json), whatever the other speakers have (owner, 2026-10-16).
The duo, split and host come from the lessons repo's own release code
(release_on_complete.resolve_tutors, assistant_registry), so the parts line
up exactly with what the lesson release later assembles: script segments
are lesson_manifest.split_script_into_segments, one item per subtopic.

Records are committed in the lesson folder, <lesson>/voice/<persona>/:
manifest.json (passed lines, each with its release asset; failed lines;
what is left), qc_failed.json and the owner's redo.json. The MP3 stems are
never committed: they render to <stems root>/<same path>/<key>.mp3 and are
uploaded to a lessons pre-release (ci/lesson_stems.py), which keeps the
repo small. Line ids are "<lesson rel>#<persona>/<key>".
Nothing here prints line text.
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from lines import pronounced_fields, spoken_text  # noqa: E402

VOICES_FILE = HERE / "lesson_voices.json"
STEM_DIR = "voice"
# Bumped when the lesson QC gate changes so that lines failed under the old
# gate get one more try (pending_items). 2: near-miss sentences (2026-10-22).
# 3: the ASR check folds -ize/-ise, % and run-together compounds (2026-10-23).
LESSON_QC = 3
MANIFEST = "manifest.json"
CATEGORY = "lesson"
TURN_RE = re.compile(r"^\*\*([A-Za-z][\w ]*):\*\*\s*(.*)$")
R3_GRADES = {0, 1, 2, 3}


class LessonError(Exception):
    """A package whose parts cannot be planned (reported, scan continues)."""


def lessons_scripts(lessons_root: Path) -> Path:
    return lessons_root / "school" / "scripts" / "CAPS"


def _import_release(lessons_root: Path):
    """The lessons repo's release helpers (needs TEAM_ROOT = agent lms/team)."""
    p = str(lessons_scripts(lessons_root))
    if p not in sys.path:
        sys.path.insert(0, p)
    import assistant_registry  # noqa: F401
    import lesson_manifest
    import release_on_complete
    return release_on_complete, lesson_manifest, assistant_registry


def load_voices(path: Path = VOICES_FILE) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))["voices"]


def voice_family(agent: Path, persona: str) -> str | None:
    p = agent / "lms/team/voices" / f"{persona}.voice.json"
    try:
        return json.loads(p.read_text(encoding="utf-8")).get("voice_family")
    except (OSError, ValueError):
        return None


def curriculum_root(lessons_root: Path) -> Path:
    return lessons_root / "school" / "curriculum" / "CAPS"


def discover(lessons_root: Path) -> list[Path]:
    rel, _lm, _ar = _import_release(lessons_root)
    return [f for f in rel.discover_folders(curriculum_root(lessons_root)) if (f / "script.md").is_file()]


def lesson_disabled(lessons_root: Path, folder: Path) -> str | None:
    """Why the lesson's grade or topic is switched off ("lessons_enabled":
    false in its syllabus, as render_voices.py reads it), else None."""
    caps = curriculum_root(lessons_root)
    subject, _s, grade_part, _t, topic_slug, _l = folder.relative_to(caps).parts
    f = caps / subject / "syllabus" / f"{grade_part}.json"
    try:
        data = json.loads(f.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    if data.get("lessons_enabled") is False:
        return f"{subject} {grade_part} is disabled"
    slug = lambda s: re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")  # noqa: E731
    matches = [t for term in data.get("terms", []) for t in term.get("topics", [])
               if slug(t.get("name", "")) == topic_slug]
    if matches and all(t.get("lessons_enabled") is False for t in matches):
        return f"{subject} {grade_part} topic {topic_slug} is disabled"
    return None


def roles(lessons_root: Path, folder: Path) -> dict:
    """{"rel", "lesson_id", "grade", "first", "second", "host", "split"}:
    persona ids per speaker and the index of the first Part 2 segment."""
    rel, lm, ar = _import_release(lessons_root)
    caps = curriculum_root(lessons_root)
    ident = rel.lesson_identity(folder, caps)
    subtopics = json.loads((folder / "subtopics.json").read_text(encoding="utf-8"))
    script_md = (folder / "script.md").read_text(encoding="utf-8")
    try:
        first, second, split_ref = rel.resolve_tutors(ident, subtopics, script_md)
    except rel.ReleaseError as exc:
        raise LessonError(str(exc)) from None
    refs = [s.get("ref") for s in subtopics.get("subtopics", [])]
    split = refs.index(split_ref) if second and split_ref in refs else None
    return {"rel": str(folder.relative_to(caps)), "lesson_id": ident["id"], "grade": ident["grade"],
            "first": first["id"], "second": second["id"] if second else None,
            "host": ar.assistant_for_grade(ident["grade"]) or None, "split": split}


def qa_turns(md: str) -> list[tuple[str, str]]:
    """[(speaker label lowercased, spoken text)] from a Q&A transcript; a line
    without a label continues the turn above it."""
    turns: list[list[str]] = []
    for line in md.replace("\r\n", "\n").split("\n"):
        s = line.strip()
        if not s or set(s) <= {"*", "-", "_"}:
            continue
        m = TURN_RE.match(s)
        if m:
            turns.append([m.group(1).strip().lower(), m.group(2)])
        elif turns:
            turns[-1][1] += " " + s
    return [(who, spoken_text(text)) for who, text in turns if spoken_text(text)]


def part_texts(lessons_root: Path, folder: Path, r: dict, persona: str) -> list[tuple[str, str, str]]:
    """[(key, source, text)] this persona speaks in the lesson, in play order."""
    _rel, lm, _ar = _import_release(lessons_root)
    out: list[tuple[str, str, str]] = []
    if persona == r["first"]:
        intro = folder / "intro.md"
        if intro.is_file() and spoken_text(intro.read_text(encoding="utf-8")):
            out.append(("intro", "intro.md", spoken_text(intro.read_text(encoding="utf-8"))))
    if persona in (r["first"], r["second"]):
        for idx, text in lm.split_script_into_segments((folder / "script.md").read_text(encoding="utf-8")):
            mine = (r["split"] is None or idx < r["split"]) if persona == r["first"] else \
                (r["split"] is not None and idx >= r["split"])
            if mine and text:
                out.append((f"seg{idx:02d}", f"script.md#{idx}", text))
    qa = folder / "assistant_qa_transcript.md"
    if qa.is_file() and persona in (r["first"], r["host"]):
        n = 0
        for who, text in qa_turns(qa.read_text(encoding="utf-8")):
            if who != "tutor":
                n += 1
                if persona == r["host"]:
                    out.append((f"qa{n:02d}_ask", f"assistant_qa_transcript.md#{n}", text))
            elif persona == r["first"] and n:
                out.append((f"qa{n:02d}_answer", f"assistant_qa_transcript.md#{n}", text))
    nervous = folder / "assistant_nervous_script.md"
    if persona == r["host"] and nervous.is_file():
        text = spoken_text(nervous.read_text(encoding="utf-8"))
        if text:
            out.append(("nervous", "assistant_nervous_script.md", text))
    return out


def blocked(agent: Path, r: dict, persona: str) -> str | None:
    """Why this persona must not voice this lesson, else None."""
    fam = voice_family(agent, persona)
    if fam == "voice_a" and r["grade"] in R3_GRADES:
        return "Voice A never renders Grade R-3"
    if fam:
        for other in (r["first"], r["second"], r["host"]):
            if other and other != persona and voice_family(agent, other) == fam:
                return f"same voice family as {other} in this lesson"
    return None


def stem_rel(r: dict, persona: str, key: str = "") -> str:
    base = f"{r['rel']}/{STEM_DIR}/{persona}"
    return f"{base}/{key}.mp3" if key else base


def build_items(lessons_root: Path, folder: Path, r: dict, persona: str, pron: dict | None,
                names: list[str]) -> list[dict]:
    items = []
    for key, source, text in part_texts(lessons_root, folder, r, persona):
        id_ = f"{r['rel']}#{persona}/{key}"
        items.append({"id": id_, "category": CATEGORY, "key": key, "lesson": r["rel"], "persona": persona,
                      **pronounced_fields(id_, text, pron, names),
                      "file": stem_rel(r, persona, key), "final_wav": stem_rel(r, persona, key)[:-4] + ".wav",
                      "script": f"{r['rel']}/{source}"})
    return items


def persona_names(agent: Path) -> list[str]:
    """Every persona's own name, wildcarded in the ASR check (a host or tutor
    named in a line may be spelled differently by the ASR)."""
    out = []
    for p in sorted((agent / "lms/team/voices").glob("*.voice.json")):
        try:
            n = json.loads(p.read_text(encoding="utf-8")).get("name")
        except (OSError, ValueError):
            continue
        if isinstance(n, str) and n.strip():
            out.append(n.strip())
    return out


def manifest_path(records_root: Path, r: dict, persona: str) -> Path:
    return records_root / stem_rel(r, persona) / MANIFEST


REDO = "redo.json"


def load_redo(records_root: Path, r: dict, persona: str) -> list[dict]:
    """The owner's listening rejections for this lesson part:
    voice/<persona>/redo.json = {"redo": [{"key": "seg03", "sha256": "<mp3
    sha256 that sounded wrong>", "note": "..."}]}. Entries stay as history."""
    p = records_root / stem_rel(r, persona) / REDO
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []
    return [e for e in d.get("redo", []) if isinstance(e, dict) and e.get("key")]


def redo_shift(redo: list[dict], key: str) -> int:
    """Seed shift for a key: 100 per rejection, so a redo never repeats a take."""
    return 100 * sum(1 for e in redo if e["key"] == key)


def retry_failed(entry: dict) -> bool:
    """A failed line whose last round failed only the ASR check, under a QC
    older than LESSON_QC. Seeds are fixed, so a line that failed on voice
    match or pitch would fail the same way again: only ASR misses retry."""
    rounds = entry.get("rounds") or [{}]
    failing = set((rounds[-1].get("failing") or {}).keys())
    return entry.get("qc", 1) < LESSON_QC and bool(failing) and failing <= {"asr"}


def pending_items(items: list[dict], manifest: dict, ref_sha: str, redo: list[dict] = ()) -> list[dict]:
    """Items not yet rendered for this text and reference, plus passed lines
    the owner rejected on listening (redo.json names the rejected MP3 by its
    sha256; a fresh take has another hash). A line that failed every seed
    round for the same text and reference is settled: it needs a script or
    voice change, not another run, unless it failed only the ASR check
    under an older QC (LESSON_QC), which gets it one more try."""
    from textnorm import TAIL_PAD
    done = {e["id"]: e for e in manifest.get("lines", [])}
    failed = {e["id"]: e for e in manifest.get("failed", []) if not retry_failed(e)}
    rejected = {(e["key"], e.get("sha256")) for e in redo}
    out = []
    for it in items:
        prev = done.get(it["id"]) or failed.get(it["id"])
        if prev and prev.get("render_sha256") == it["render_sha256"] and prev.get("ref_sha256") == ref_sha \
                and prev.get("tail_pad", TAIL_PAD) == TAIL_PAD \
                and (it["key"], prev.get("sha256")) not in rejected:
            continue
        out.append(it)
    return out


def words(items: list[dict]) -> int:
    return sum(len(s.split()) for it in items for s in it["render_text"])


def plan(lessons_root: Path, agent: Path, records_root: Path, voices: dict, pron: dict | None = None,
         only: set[str] | None = None) -> tuple[list[dict], dict]:
    """[(lesson rel, persona, words pending)] for every voiced part still to
    render, plus counts. `only` limits the scan to lesson rels."""
    import pronunciations
    pron = pronunciations.load() if pron is None else pron
    names = persona_names(agent)
    todo, stats = [], {"lessons": 0, "disabled": 0, "blocked": 0, "errors": 0, "done": 0, "pending": 0,
                       "unvoiced": 0}
    for folder in discover(lessons_root):
        rel = str(folder.relative_to(curriculum_root(lessons_root)))
        if only and rel not in only:
            continue
        stats["lessons"] += 1
        if lesson_disabled(lessons_root, folder):
            stats["disabled"] += 1
            continue
        try:
            r = roles(lessons_root, folder)
        except LessonError as exc:
            stats["errors"] += 1
            print(f"skip {rel}: {exc}", file=sys.stderr)
            continue
        for persona in dict.fromkeys(p for p in (r["first"], r["second"], r["host"]) if p):
            if persona not in voices:
                stats["unvoiced"] += 1
                continue
            why = blocked(agent, r, persona)
            if why:
                stats["blocked"] += 1
                print(f"skip {rel} {persona}: {why}", file=sys.stderr)
                continue
            items = build_items(lessons_root, folder, r, persona, pron, names)
            mp = manifest_path(records_root, r, persona)
            manifest = json.loads(mp.read_text(encoding="utf-8")) if mp.is_file() else {}
            left = pending_items(items, manifest, voices[persona]["ref_sha256"],
                                 load_redo(records_root, r, persona))
            if left:
                stats["pending"] += 1
                todo.append({"lesson": rel, "persona": persona, "words": words(left), "grade": r["grade"]})
            else:
                stats["done"] += 1
    return todo, stats


def pack(todo: list[dict], max_jobs: int, job_words: int) -> list[dict]:
    """Matrix rows {persona, lessons: "a,b,..."}: one persona per job, lessons
    packed up to job_words pending words, personas taken in turn so every
    voice moves forward each run."""
    by_persona: dict[str, list[dict]] = {}
    for t in todo:
        by_persona.setdefault(t["persona"], []).append(t)
    queues = {p: list(v) for p, v in sorted(by_persona.items())}
    jobs: list[dict] = []
    while len(jobs) < max_jobs and any(queues.values()):
        for p in list(queues):
            q = queues[p]
            if not q or len(jobs) >= max_jobs:
                continue
            batch, total = [], 0
            while q and (not batch or total + q[0]["words"] <= job_words):
                t = q.pop(0)
                batch.append(t["lesson"])
                total += t["words"]
            jobs.append({"persona": p, "lessons": ",".join(batch), "words": total})
    return jobs


def env_int(name: str, default: int) -> int:
    try:
        return int(os.environ.get(name, "") or default)
    except ValueError:
        return default
