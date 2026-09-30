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
from textnorm import speak_text, split_sentences

CLIP_CATEGORIES = ("acknowledgements", "greetings", "signoffs")


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


def build_lines(agent_root: str | Path, tutor: str, categories: list[str], pron: dict | None = None) -> list[dict]:
    pron = pronunciations.load() if pron is None else pron
    root = Path(agent_root)
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
