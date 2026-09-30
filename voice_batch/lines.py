"""Build the render list for one tutor from the agent repo's team layout.

Audio sits beside its script (the app convention the factory clip table
uses: ref 'tutor_001/greetings/02' -> script tutors/CAPS/tutor_001/greetings/02.md):

  <cat>/NN.md                       -> <cat>/NN.wav   (acknowledgements, greetings, signoffs)
  samples.json  samples[].id        -> samples/<id>.wav
  voices/<tutor>.voice.json sample_line -> samples/sample_line.wav
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

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


def _item(tutor_dir: Path, team_rel: str, id_: str, category: str, text: str, wav: str, script: str) -> dict:
    sentences = split_sentences(text)
    return {
        "id": id_, "category": category, "text": text,
        "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "file": f"{team_rel}/{wav}", "script": script,
        "sentences": sentences, "render_text": [speak_text(s) for s in sentences],
    }


def build_lines(agent_root: str | Path, tutor: str, categories: list[str]) -> list[dict]:
    root = Path(agent_root)
    team_rel = f"lms/team/tutors/CAPS/{tutor}"
    tdir = root / team_rel
    items: list[dict] = []
    for cat in categories:
        if cat in CLIP_CATEGORIES:
            for md in sorted((tdir / cat).glob("[0-9][0-9].md")):
                text = spoken_text(md.read_text(encoding="utf-8"))
                if text:
                    items.append(_item(tdir, team_rel, f"{tutor}/{cat}/{md.stem}", cat, text,
                                       f"{cat}/{md.stem}.wav", f"{team_rel}/{cat}/{md.name}"))
        elif cat == "teaching":
            sj = tdir / "samples.json"
            if sj.is_file():
                for s in json.loads(sj.read_text(encoding="utf-8")).get("samples", []):
                    sid, script = s.get("id"), s.get("script")
                    if isinstance(sid, str) and re.fullmatch(r"[A-Za-z0-9_]+", sid) and script:
                        items.append(_item(tdir, team_rel, sid, cat, " ".join(script.split()),
                                           f"samples/{sid}.wav", f"{team_rel}/samples.json#{sid}"))
            vj = root / "lms/team/voices" / f"{tutor}.voice.json"
            if vj.is_file():
                line = json.loads(vj.read_text(encoding="utf-8")).get("sample_line")
                if line:
                    items.append(_item(tdir, team_rel, f"{tutor}_sample_line", cat, " ".join(line.split()),
                                       "samples/sample_line.wav", f"lms/team/voices/{tutor}.voice.json#sample_line"))
        else:
            raise ValueError(f"unknown category {cat}")
    return items
