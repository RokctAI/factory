#!/usr/bin/env python3
"""Validate a voice batch JSON and print its fields as GitHub step outputs.

    python voice_batch/batch.py voice_batches/inbox/<batch>.json >> "$GITHUB_OUTPUT"

A batch names WHAT to render; the audio and the reference live only in the
private agent repo. Every field is pattern-checked because it flows into
paths, git refs and shell arguments.

Two kinds:

* "tutor" (the default when "kind" is absent): a tutor's standing lines,
  one render job per category.
* "r3": the Grades R-3 activity-pack lines (voice_batch/r3_lines.py), split
  into shards of about R3_LINES_PER_SHARD lines (at most R3_MAX_SHARDS jobs).
  Optional "packs" (a pack-id glob or a list of them), "lines" (R3Line
  keys) and "locale" (default "en").

* "assistant": an assistant's named scripts (lms/team/assistants/CAPS/<id>),
  one render job per category (intro, handover, signoff, timekeeping).
  Optional "lines" ids of the form '<id>/<category>/<stem>'.

All take an optional F0 gate: "f0_target_hz" and "f0_tolerance_hz"
(defaults: the Voice A values, 102 +/- 8 Hz, i.e. 94-110 Hz).

Pronunciations (voice_batch/pronunciations.json): the file must be valid,
and no line may use an "ambiguous" word outside an inline
{{word|respelling}}; the error names the line and the variants. R-3 lines
are in this repo, so an r3 batch is checked here. Tutor lines live in the
agent repo: pass --agent-root once it is checked out.

    python voice_batch/batch.py --agent-root .agent voice_batches/inbox/<batch>.json > /dev/null
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

CATEGORIES = ("acknowledgements", "greetings", "signoffs", "teaching")
ASSISTANT_CATEGORIES = ("intro", "handover", "signoff", "timekeeping")
DUO_SUFFIX_RE = r"@tutor_\d{3}\+tutor_\d{3}"  # per-duo host line variant (lines.py)
KINDS = ("tutor", "r3", "assistant")
COMMON = {
    "voice": r"[a-z][a-z0-9_]{0,31}",
    "ref_path": r"lms/team/voice_refs/[A-Za-z0-9_]+\.wav",
    "ref_sha256": r"[0-9a-f]{64}",
    "agent_branch": r"rokct/[A-Za-z0-9._-]+(/[A-Za-z0-9._-]+)*",
}
PATTERNS = {"tutor": r"tutor_\d{3}", **COMMON}   # the tutor kind's required fields
ASSISTANT_PATTERNS = {"assistant": r"assistant_\d{3}", **COMMON}
PACK_GLOB_RE = r"[A-Za-z0-9_.*?\[\]-]{1,120}"
R3_KEY_RE = r"[A-Za-z0-9_.]{1,160}"

# F0 gate defaults: Voice A (male), unchanged from before it was configurable.
F0_TARGET_HZ = 102.0
F0_TOLERANCE_HZ = 8.0
F0_TARGET_RANGE = (50.0, 400.0)
F0_TOLERANCE_RANGE = (1.0, 80.0)

R3_LINES_PER_SHARD = 40
R3_MAX_SHARDS = 8
ASR_MODEL_EN = "small.en"
ASR_MODEL_MULTI = "small"

SPARSE_TUTOR = ("lms/team/tutors/CAPS/{tutor}", "lms/team/voices", "lms/team/voice_refs", "lms/team/scripts")
# Non-cone patterns (the workflow turns cone mode off for assistants): the
# rosters and tutor cards name the session's tutor duo in host lines.
SPARSE_ASSISTANT = ("/lms/team/assistants/CAPS/{tutor}/", "/lms/team/voices/", "/lms/team/voice_refs/",
                    "/lms/team/scripts/", "/lms/team/assistants/CAPS/roster.json", "/lms/team/tutors/CAPS/roster.json",
                    "/lms/team/tutors/CAPS/*/tutor.md", "/lms/team/tutors/CAPS/*/appearance/still.json")
SPARSE_R3 = ("lms/dart/templates/assets/r3_packs/audio", "lms/team/voice_refs", "lms/team/scripts",
             "lms/dart/lib/src/common/application/r3", "lms/dart/lib/src/translations")


class BatchError(ValueError):
    pass


def category_of(line_id: str, tutor: str) -> str | None:
    """Category of a line id: '<tutor>/<category>/NN', '<tutor>_sample_NN'
    or '<tutor>_sample_line' (teaching). None if it is not one of those."""
    m = re.fullmatch(rf"{tutor}/(acknowledgements|greetings|signoffs)/\d{{2}}", line_id)
    if m:
        return m.group(1)
    if re.fullmatch(rf"{tutor}_sample_(\d{{2}}|line)", line_id):
        return "teaching"
    return None


def assistant_category_of(line_id: str, assistant: str) -> str | None:
    """Category of an assistant line id '<assistant>/<category>/<stem>'."""
    m = re.fullmatch(rf"{assistant}/({'|'.join(ASSISTANT_CATEGORIES)})/[a-z0-9_]{{1,40}}({DUO_SUFFIX_RE})?", line_id)
    return m.group(1) if m else None


def _num(raw: dict, key: str, default: float, lo_hi: tuple[float, float]) -> float:
    v = raw.get(key, default)
    if isinstance(v, bool) or not isinstance(v, (int, float)) or not lo_hi[0] <= v <= lo_hi[1]:
        raise BatchError(f"{key} must be a number in {lo_hi[0]:g}-{lo_hi[1]:g}")
    return float(v)


def _fields(raw: dict, patterns: dict) -> dict:
    out = {}
    for key, pat in patterns.items():
        val = raw.get(key)
        if not isinstance(val, str) or not re.fullmatch(pat, val):
            raise BatchError(f"field '{key}' missing or not matching {pat}")
        out[key] = val
    if ".." in out["agent_branch"] or out["agent_branch"].endswith((".", "/", ".lock")):
        raise BatchError("agent_branch is not a safe branch name")
    return out


def _unknown(raw: dict, allowed: set) -> None:
    unknown = set(raw) - allowed - {k for k in raw if k.startswith("_")}
    if unknown:
        raise BatchError(f"unknown field(s): {sorted(unknown)}")


def _load_tutor(raw: dict) -> dict:
    out = _fields(raw, PATTERNS)
    cats = raw.get("categories")
    if not isinstance(cats, list) or not cats or any(c not in CATEGORIES for c in cats):
        raise BatchError(f"categories must be a non-empty subset of {list(CATEGORIES)}")
    out["categories"] = [c for c in CATEGORIES if c in cats]
    lines = raw.get("lines")
    if lines is not None:
        if not isinstance(lines, list) or not lines or not all(isinstance(x, str) for x in lines):
            raise BatchError("lines, when given, must be a non-empty list of line ids")
        for x in lines:
            if category_of(x, out["tutor"]) not in out["categories"]:
                raise BatchError(f"line id {x!r} is not a {out['tutor']} line in the batch's categories")
        out["lines"] = sorted(set(lines))
        # Only run the categories the filter actually touches.
        out["categories"] = [c for c in out["categories"] if any(category_of(x, out["tutor"]) == c for x in lines)]
    _unknown(raw, set(PATTERNS) | {"kind", "categories", "lines", "f0_target_hz", "f0_tolerance_hz"})
    out["matrix"] = [{"category": c, "shard": ""} for c in out["categories"]]
    return out


def _load_assistant(raw: dict) -> dict:
    out = _fields(raw, ASSISTANT_PATTERNS)
    cats = raw.get("categories")
    if not isinstance(cats, list) or not cats or any(c not in ASSISTANT_CATEGORIES for c in cats):
        raise BatchError(f"categories must be a non-empty subset of {list(ASSISTANT_CATEGORIES)}")
    out["categories"] = [c for c in ASSISTANT_CATEGORIES if c in cats]
    lines = raw.get("lines")
    if lines is not None:
        if not isinstance(lines, list) or not lines or not all(isinstance(x, str) for x in lines):
            raise BatchError("lines, when given, must be a non-empty list of line ids")
        for x in lines:
            if assistant_category_of(x, out["assistant"]) not in out["categories"]:
                raise BatchError(f"line id {x!r} is not a {out['assistant']} line in the batch's categories")
        out["lines"] = sorted(set(lines))
        out["categories"] = [c for c in out["categories"]
                             if any(assistant_category_of(x, out["assistant"]) == c for x in lines)]
    _unknown(raw, set(ASSISTANT_PATTERNS) | {"kind", "categories", "lines", "f0_target_hz", "f0_tolerance_hz"})
    out["tutor"] = out["assistant"]   # the target id the CI steps pass around
    out["matrix"] = [{"category": c, "shard": ""} for c in out["categories"]]
    return out


def voice_spec(agent_root: str | Path | None, target: str) -> dict:
    """lms/team/voices/<target>.voice.json from the agent checkout, or {}."""
    if agent_root is None:
        return {}
    p = Path(agent_root) / "lms/team/voices" / f"{target}.voice.json"
    try:
        spec = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return spec if isinstance(spec, dict) else {}


def _load_r3(raw: dict, factory_root: Path | None) -> dict:
    import r3_lines
    out = _fields(raw, COMMON)
    locale = raw.get("locale", "en")
    if locale not in r3_lines.LOCALES:
        raise BatchError(f"locale must be one of {list(r3_lines.LOCALES)}")
    out["locale"] = locale
    packs = raw.get("packs")
    if packs is not None:
        if isinstance(packs, str):
            packs = [packs]
        if not isinstance(packs, list) or not packs or not all(
                isinstance(p, str) and re.fullmatch(PACK_GLOB_RE, p) for p in packs):
            raise BatchError("packs, when given, must be a pack-id glob or a non-empty list of them")
        if locale != "en":
            raise BatchError("packs are English; a non-English r3 batch renders the default praise only")
        out["packs"] = packs
    root = factory_root or r3_lines.FACTORY
    all_keys = [k for k, _, _ in r3_lines.all_keyed_lines(root, out.get("packs"), locale)]
    if not all_keys:
        raise BatchError("the packs filter matches no pack")
    lines = raw.get("lines")
    if lines is not None:
        if not isinstance(lines, list) or not lines or not all(
                isinstance(x, str) and re.fullmatch(R3_KEY_RE, x) for x in lines):
            raise BatchError("lines, when given, must be a non-empty list of R3Line keys")
        known = set(all_keys)
        bad = [x for x in lines if x not in known]
        if bad:
            raise BatchError(f"line key(s) not in the selected packs/locale: {bad[:5]}")
        out["lines"] = sorted(set(lines))
        n = len(out["lines"])
    else:
        n = len(all_keys)
    out["line_count"] = n
    shards = r3_lines.shard_count(n, R3_LINES_PER_SHARD, R3_MAX_SHARDS)
    out["matrix"] = [{"category": "r3", "shard": f"{k}/{shards}"} for k in range(1, shards + 1)]
    out["categories"] = ["r3"]
    _unknown(raw, set(COMMON) | {"kind", "packs", "lines", "locale", "f0_target_hz", "f0_tolerance_hz"})
    return out


def pronunciation_errors(b: dict, agent_root: str | Path | None = None, factory_root: Path | None = None,
                         pron: dict | None = None) -> list[str]:
    """Lines of the batch that use an ambiguous word without an inline
    respelling, or carry malformed inline markup. Tutor lines need the agent
    checkout (agent_root); without it only an r3 batch is checked."""
    import pronunciations
    try:
        pron = pronunciations.load() if pron is None else pron
        if b["kind"] == "r3":
            import r3_lines
            items = r3_lines.build_r3_lines(factory_root or r3_lines.FACTORY, b.get("packs"), b.get("lines"),
                                            b["locale"], agent_root, pron=pron)
        elif agent_root is None:
            return []
        else:
            from lines import build_lines
            items = build_lines(agent_root, b["tutor"], b["categories"], pron, kind=b["kind"])
            if b.get("lines"):
                items = [it for it in items if it["id"] in set(b["lines"])]
    except (pronunciations.PronunciationError, ValueError) as exc:
        return [str(exc)]
    return pronunciations.check_ambiguous(items, pron)


def load_batch(path: str | Path, factory_root: Path | None = None, agent_root: str | Path | None = None) -> dict:
    try:
        raw = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise BatchError(f"unreadable batch JSON ({type(exc).__name__})") from None
    if not isinstance(raw, dict):
        raise BatchError("batch must be a JSON object")
    kind = raw.get("kind", "tutor")
    if kind not in KINDS:
        raise BatchError(f"kind must be one of {list(KINDS)}")
    if kind == "tutor":
        out = _load_tutor(raw)
    elif kind == "assistant":
        out = _load_assistant(raw)
    else:
        out = _load_r3(raw, factory_root)
    out["kind"] = kind
    # F0 gate: the batch's values, else the voice spec's (assistants), else Voice A.
    spec = voice_spec(agent_root, out["tutor"]) if kind == "assistant" else {}
    out["f0_target_hz"] = _num(raw, "f0_target_hz", spec.get("f0_target_hz", F0_TARGET_HZ), F0_TARGET_RANGE)
    out["f0_tolerance_hz"] = _num(raw, "f0_tolerance_hz", spec.get("f0_tolerance_hz", F0_TOLERANCE_HZ),
                                  F0_TOLERANCE_RANGE)
    errs = pronunciation_errors(out, agent_root, factory_root)
    if errs:
        raise BatchError("; ".join(errs))
    return out


def sparse_paths(b: dict) -> list[str]:
    if b["kind"] == "r3":
        return list(SPARSE_R3)
    if b["kind"] == "assistant":
        return [p.format(tutor=b["tutor"]) for p in SPARSE_ASSISTANT]
    return [p.format(tutor=b["tutor"]) for p in SPARSE_TUTOR]


def outputs(b: dict) -> list[str]:
    """GitHub step output lines. Ids, paths and numbers only, never text."""
    from lines import team_rel
    out = [f"kind={b['kind']}", f"tutor={b.get('tutor', '')}",
           f"team_dir={team_rel(b['tutor']) if b.get('tutor') else ''}"]
    out += [f"{k}={b[k]}" for k in COMMON]
    out += [f"categories={' '.join(b['categories'])}",
            f"lines={','.join(b.get('lines', []))}",
            "categories_json=" + json.dumps(b["categories"]),
            "matrix_json=" + json.dumps(b["matrix"]),
            f"f0_target_hz={b['f0_target_hz']:g}", f"f0_tolerance_hz={b['f0_tolerance_hz']:g}",
            f"locale={b.get('locale', 'en')}",
            f"asr_model={ASR_MODEL_EN if b.get('locale', 'en') == 'en' else ASR_MODEL_MULTI}",
            f"line_count={b.get('line_count', '')}",
            "sparse<<SPARSE_EOF", *sparse_paths(b), "SPARSE_EOF"]
    return out


def main(argv: list[str]) -> int:
    agent_root = None
    if len(argv) == 4 and argv[1] == "--agent-root":
        agent_root, argv = argv[2], [argv[0], argv[3]]
    if len(argv) != 2:
        print("usage: batch.py [--agent-root AGENT_DIR] BATCH_JSON", file=sys.stderr)
        return 2
    try:
        b = load_batch(argv[1], agent_root=agent_root)
    except BatchError as exc:
        for e in str(exc).split("; "):
            print(f"::error::{argv[1]}: {e}", file=sys.stderr)
        return 1
    print("\n".join(outputs(b)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
