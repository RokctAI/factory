"""Build the render list for one tutor from the agent repo's team layout.

Audio sits beside its script (the app convention the factory clip table
uses: ref 'tutor_001/greetings/02' -> script tutors/CAPS/tutor_001/greetings/02.md):

  <cat>/NN.md                       -> <cat>/NN.wav   (acknowledgements, greetings, signoffs)
  samples.json  samples[].id        -> samples/<id>.wav
  voices/<tutor>.voice.json sample_line -> samples/sample_line.wav

Pronunciations (pronunciations.py) apply to every line: "text" is the
display text (inline {{word|respelling}} resolved to the word), the TTS gets
render_text, and the QC wildcards the respelled words (sentence_wild).
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import pronunciations
import sys
from textnorm import speak_text, split_sentences

CLIP_CATEGORIES = ("acknowledgements", "greetings", "signoffs")
ASSISTANT_CATEGORIES = ("intro", "handover", "signoff", "timekeeping")


def team_rel(target: str) -> str:
    """The agent-repo team folder of a tutor_NNN or assistant_NNN."""
    if re.fullmatch(r"assistant_\d{3}", target):
        return f"lms/team/assistants/CAPS/{target}"
    if re.fullmatch(r"tutor_\d{3}", target):
        return f"lms/team/tutors/CAPS/{target}"
    raise ValueError(f"not a tutor or assistant id: {target}")


def spoken_text(md: str) -> str:
    """The spoken text of a clip script: YAML front matter, headings, HTML
    comments and emphasis markers are metadata/markdown, never spoken."""
    md = md.replace("\r\n", "\n").lstrip("﻿")
    if md.startswith("---\n"):
        end = md.find("\n---", 4)
        if end != -1:
            md = md[end + 4:]
    md = re.sub(r"<!--.*?-->", " ", md, flags=re.S)
    keep = [ln for ln in md.split("\n") if not ln.lstrip().startswith(("#", ">", "|"))]
    text = " ".join(" ".join(keep).split())
    text = re.sub(r"(\*\*|`)(.+?)\1", r"\2", text)
    return text


def pronounced_fields(id_: str, text: str, pron: dict | None) -> dict:
    """The text fields every render item carries, with pronunciations
    applied sentence by sentence (shared with r3_lines.item).

    text        display text: inline markup resolved to the display word
    sentences   display sentences (the per-take ASR reference)
    render_text what the TTS is given, one per sentence
    sentence_wild / asr_wild  the respelled words the ASR check wildcards
    tts_text    only when a pronunciation changed the spoken text"""
    try:
        parts = [pronunciations.apply(s, pron) for s in split_sentences(text)]
    except pronunciations.PronunciationError as exc:
        raise pronunciations.PronunciationError(f"line {id_}: {exc}") from None
    display = " ".join(p[0] for p in parts)
    render = [speak_text(p[1]) for p in parts]
    out = {
        "text": display, "source_text": text,
        "text_sha256": hashlib.sha256(display.encode("utf-8")).hexdigest(),
        "render_sha256": hashlib.sha256("\n".join(render).encode("utf-8")).hexdigest(),
        "sentences": [p[0] for p in parts], "render_text": render,
        "sentence_wild": [p[2] for p in parts], "asr_text": display,
        "asr_wild": [w for p in parts for w in p[2]],
        "pronounced": [w[0] for p in parts for w in p[2]],
    }
    tts = " ".join(p[1] for p in parts)
    if tts != display:
        out["tts_text"] = tts
    return out


def _item(id_: str, category: str, text: str, team_rel: str, wav: str, script: str, pron: dict | None) -> dict:
    return {"id": id_, "category": category, **pronounced_fields(id_, text, pron),
            "file": f"{team_rel}/{wav}", "script": script}

ASSISTANT_ROSTER = "lms/team/assistants/CAPS/roster.json"
TUTOR_ROSTER = "lms/team/tutors/CAPS/roster.json"
# Host-line placeholders naming the session's tutor duo. A single-brace
# {name}, never the {{word|respelling}} pronunciation markup.
PLACEHOLDER_RE = re.compile(r"(?<!\{)\{([a-z_]+)\}(?!\})")
DUO_PLACEHOLDERS = ("first_tutor", "second_tutor")  # expert, simplifier
DUO_SUFFIX_RE = r"@tutor_\d{3}\+tutor_\d{3}"


def _json(path: Path) -> dict:
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return d if isinstance(d, dict) else {}


def assistant_grades(root: Path, assistant: str) -> list[str]:
    """The grade(s) an assistant hosts live (assistants roster by_grade)."""
    by_grade = _json(root / ASSISTANT_ROSTER).get("by_grade") or {}
    return [str(g) for g, a in by_grade.items() if a == assistant]


def grade_duos(root: Path, grade: str) -> list[tuple[str, str]]:
    """(expert, simplifier) duos teaching a grade, in roster subject order,
    deduplicated. Phases: `subjects` for fet_grades, then senior_phase,
    intermediate_phase and grade_7 ({grades, subjects}); a subject may carry
    per-grade `grade_duos`."""
    t = _json(root / TUTOR_ROSTER)
    phases = [(t.get("fet_grades") or [], t.get("subjects") or {})]
    for key in ("senior_phase", "intermediate_phase", "grade_7"):
        ph = t.get(key) or {}
        phases.append((ph.get("grades") or [], ph.get("subjects") or {}))
    duos: list[tuple[str, str]] = []
    for grades, subjects in phases:
        if grade not in {str(g) for g in grades}:
            continue
        for subj in subjects.values():
            if not isinstance(subj, dict):
                continue
            d = (subj.get("grade_duos") or {}).get(grade) if "grade_duos" in subj else subj
            if isinstance(d, dict) and all(re.fullmatch(r"tutor_\d{3}", str(d.get(k, ""))) for k in ("expert", "simplifier")):
                pair = (d["expert"], d["simplifier"])
                if pair not in duos:
                    duos.append(pair)
    return duos


def tutor_display_name(root: Path, tutor: str) -> str:
    """A tutor's display name: tutors roster or appearance/still.json
    `display_name` if present, else tutor.md's `display_name:` line (where
    the agent repo keeps it today)."""
    tdir = root / "lms/team/tutors/CAPS" / tutor
    for d in ((_json(root / TUTOR_ROSTER).get("tutors") or {}).get(tutor), _json(tdir / "appearance/still.json")):
        if isinstance(d, dict) and isinstance(d.get("display_name"), str) and d["display_name"].strip():
            return d["display_name"].strip()
    try:
        m = re.search(r"^display_name:\s*(.+?)\s*$", (tdir / "tutor.md").read_text(encoding="utf-8"), re.M)
    except OSError:
        m = None
    if not m:
        raise ValueError(f"no display name for {tutor}")
    return m.group(1)


def host_duos(root: Path, assistant: str) -> list[tuple[str, str]]:
    duos: list[tuple[str, str]] = []
    for g in assistant_grades(root, assistant):
        duos += [d for d in grade_duos(root, g) if d not in duos]
    return duos


def fill_placeholders(text: str, names: dict[str, str]) -> str:
    def sub(m: re.Match) -> str:
        if m.group(1) not in names:
            raise ValueError(f"unknown placeholder {{{m.group(1)}}}")
        return names[m.group(1)]
    return PLACEHOLDER_RE.sub(sub, text)


def build_assistant_lines(root: Path, assistant: str, categories: list[str], pron: dict | None) -> list[dict]:
    """An assistant's named scripts: <cat>/<stem>.md -> <cat>/<stem>.wav, id
    '<assistant>/<cat>/<stem>'. A script naming the session's tutors
    ({first_tutor} = expert, {second_tutor} = simplifier) becomes one line per
    duo of the grade(s) the assistant hosts, id and wav suffixed
    '@<expert>+<simplifier>'; with no duo (no live grade) it is skipped. The voice spec's optional sample_line goes in
    the first category as samples/sample_line.wav."""
    rel = team_rel(assistant)
    adir = root / rel
    items: list[dict] = []
    duos: list[tuple[str, str]] | None = None
    for cat in categories:
        if cat not in ASSISTANT_CATEGORIES:
            raise ValueError(f"unknown category {cat}")
        for md in sorted((adir / cat).glob("*.md")):
            if not re.fullmatch(r"[a-z0-9_]{1,40}", md.stem):
                continue
            text = spoken_text(md.read_text(encoding="utf-8"))
            if not text:
                continue
            script = f"{rel}/{cat}/{md.name}"
            used = set(PLACEHOLDER_RE.findall(text))
            if not used:
                items.append(_item(f"{assistant}/{cat}/{md.stem}", cat, text, rel,
                                   f"{cat}/{md.stem}.wav", script, pron))
                continue
            unknown = used - set(DUO_PLACEHOLDERS)
            if unknown:
                raise ValueError(f"line {assistant}/{cat}/{md.stem}: unknown placeholder(s) "
                                 + ", ".join("{%s}" % u for u in sorted(unknown)))
            if duos is None:
                duos = host_duos(root, assistant)
            if not duos:
                print(f"skip {assistant}/{cat}/{md.stem}: names the session tutors but {assistant} "
                      "hosts no grade with a live tutor duo", file=sys.stderr)
                continue
            for e, s in duos:
                names = dict(zip(DUO_PLACEHOLDERS, (tutor_display_name(root, e), tutor_display_name(root, s))))
                sfx = f"@{e}+{s}"
                items.append(_item(f"{assistant}/{cat}/{md.stem}{sfx}", cat, fill_placeholders(text, names), rel,
                                   f"{cat}/{md.stem}{sfx}.wav", script, pron))
    if categories and categories[0] == ASSISTANT_CATEGORIES[0]:
        vj = root / "lms/team/voices" / f"{assistant}.voice.json"
        if vj.is_file():
            line = json.loads(vj.read_text(encoding="utf-8")).get("sample_line")
            if isinstance(line, str) and line.strip():
                items.append(_item(f"{assistant}_sample_line", categories[0], " ".join(line.split()), rel,
                                   "samples/sample_line.wav", f"lms/team/voices/{assistant}.voice.json#sample_line", pron))
    return items


def build_lines(agent_root: str | Path, tutor: str, categories: list[str], pron: dict | None = None,
                kind: str = "tutor") -> list[dict]:
    pron = pronunciations.load() if pron is None else pron
    root = Path(agent_root)
    if kind == "assistant":
        return build_assistant_lines(root, tutor, categories, pron)
    team_rel = f"lms/team/tutors/CAPS/{tutor}"
    tdir = root / team_rel
    items: list[dict] = []
    for cat in categories:
        if cat in CLIP_CATEGORIES:
            for md in sorted((tdir / cat).glob("[0-9][0-9].md")):
                text = spoken_text(md.read_text(encoding="utf-8"))
                if text:
                    items.append(_item(f"{tutor}/{cat}/{md.stem}", cat, text, team_rel,
                                       f"{cat}/{md.stem}.wav", f"{team_rel}/{cat}/{md.name}", pron))
        elif cat == "teaching":
            sj = tdir / "samples.json"
            if sj.is_file():
                for s in json.loads(sj.read_text(encoding="utf-8")).get("samples", []):
                    sid, script = s.get("id"), s.get("script")
                    if isinstance(sid, str) and re.fullmatch(r"[A-Za-z0-9_]+", sid) and script:
                        items.append(_item(sid, cat, " ".join(script.split()), team_rel,
                                           f"samples/{sid}.wav", f"{team_rel}/samples.json#{sid}", pron))
            vj = root / "lms/team/voices" / f"{tutor}.voice.json"
            if vj.is_file():
                line = json.loads(vj.read_text(encoding="utf-8")).get("sample_line")
                if line:
                    items.append(_item(f"{tutor}_sample_line", cat, " ".join(line.split()), team_rel,
                                       "samples/sample_line.wav", f"lms/team/voices/{tutor}.voice.json#sample_line", pron))
        else:
            raise ValueError(f"unknown category {cat}")
    return items
