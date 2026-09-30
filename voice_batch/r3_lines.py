"""Build the render list for Grades R-3 activity packs.

Every line a child hears in an R-3 session is prepared in a pack
(lessons/curriculum/CAPS/{subject}/r3_packs/grade*/term*/*.json). The app
(agent lms/dart/lib/src/common/application/r3/r3_session_engine.dart,
R3SessionEngine.lines) keys each line so pre-rendered audio can be matched:

  <pack.id>.show
  <pack.id>.hints_0 / hints_1                 (the engine only uses two hints)
  <pack.id>.rounds_<i>_prompt / _praise / _story (story: story_tap rounds only;
                                              praise: only when non-blank)
  <pack.id>.beat_the_tutor_{setup,tutor_try,win_line,gentle_line}
  r3.<tr key>                                 (the 4 default praise lines)

<i> counts the rounds the app actually parses (R3Round.tryParse skips an
unknown type or a round missing a required field), so it equals the pack's
round index for every pack that passes r3_pack_check.py.

AssetTutorVoice (agent lms/dart/templates/routes/lms_route_pages.dart)
plays assets/r3_packs/audio/<key>.mp3, which the SDK installs from
lms/dart/templates/assets/r3_packs/audio/ in the agent repo.

Phonics: voice_batch/r3_respellings.json maps a line key (or an exact line
text) to a TTS-only text, e.g. "a as in ant" -> "ah, as in ant", so the
voice says the sound and not the letter name. The display text never
changes; the respelled text is what is rendered and what the ASR gate
checks, and the line is flagged needs_listen for a human ear.

Word pronunciations (pronunciations.json, inline {{word|respelling}}) then
apply to that text, as for every batch kind; they flag needs_listen too.
"""
from __future__ import annotations

import fnmatch
import hashlib
import json
import re
import sys
from pathlib import Path

import pronunciations
from lines import pronounced_fields

FACTORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FACTORY / "lessons" / "scripts" / "CAPS"))
from r3_pack_check import ROUND_TYPES  # noqa: E402  (same table as the app's R3Round.requiredFields)

PACK_GLOB = "lessons/curriculum/CAPS/*/r3_packs/grade*/term*/*.json"
AUDIO_DIR = "lms/dart/templates/assets/r3_packs/audio"
RESPELLINGS = Path(__file__).resolve().parent / "r3_respellings.json"
ENGINE_DART = "lms/dart/lib/src/common/application/r3/r3_session_engine.dart"
TRANSLATIONS_DART = "lms/dart/lib/src/translations/lms_{locale}_translations.dart"

# The <where> part of every pack line key, as R3SessionEngine.lines builds
# it ({i} = round index). tests/test_r3.py checks this against the Dart.
WHERE_TEMPLATES = (
    "show", "hints_0", "hints_1",
    "rounds_{i}_prompt", "rounds_{i}_praise", "rounds_{i}_story",
    "beat_the_tutor_setup", "beat_the_tutor_tutor_try",
    "beat_the_tutor_win_line", "beat_the_tutor_gentle_line",
)
ENGINE_HINTS = 2

# Fallback for the 4 default praise lines when the agent checkout (and so
# the app's translation source) is not reachable, e.g. in the plan job.
# TODO: keep in step with kR3DefaultPraise and lms_{en,af}_translations.dart
# in the agent repo; the real renders read those files, and the AGENT_ROOT
# test fails if this table drifts.
DEFAULT_PRAISE_FALLBACK = {
    "keys": ("r3_praise_yes", "r3_praise_great", "r3_praise_clever", "r3_praise_right"),
    "en": ("Yes! Well done.", "Great job!", "Clever you!", "That's right!"),
    "af": ("Ja! Mooi so.", "Uitstekend!", "Slim van jou!", "Dis reg!"),
}
LOCALES = ("en", "af")


class R3Error(ValueError):
    pass


# ---------------------------------------------------------------------------
# Packs -> keyed lines (mirrors R3Pack.tryParse + R3SessionEngine.lines)
# ---------------------------------------------------------------------------

def _dart_str(v) -> str:
    """'${v ?? ''}' in Dart."""
    if v is None:
        return ""
    if isinstance(v, bool):
        return "true" if v else "false"
    return str(v)


def _parsed_rounds(pack: dict) -> list[dict]:
    """The rounds the app keeps: known type with every required field."""
    out = []
    for r in pack.get("rounds") or []:
        if not isinstance(r, dict):
            continue
        need = ROUND_TYPES.get(r.get("type"))
        if need is None or any(k not in r for k in ("prompt",) + tuple(need)):
            continue
        out.append(r)
    return out


def pack_lines(pack: dict) -> list[tuple[str, str]]:
    """(key, text) for every line the engine can say for this pack, in
    session order. Blank lines are left out (nothing to render)."""
    pid = _dart_str(pack.get("id"))
    out: list[tuple[str, str]] = []

    def add(where: str, text) -> None:
        text = _dart_str(text)
        if text.strip():
            out.append((f"{pid}.{where}", text))

    add("show", (pack.get("show") or {}).get("line"))
    for i, h in enumerate((pack.get("hints") or [])[:ENGINE_HINTS]):
        add(f"hints_{i}", h)
    for i, r in enumerate(_parsed_rounds(pack)):
        add(f"rounds_{i}_prompt", r.get("prompt"))
        if r.get("type") == "story_tap":
            add(f"rounds_{i}_story", r.get("story"))
        if r.get("praise") is not None:
            add(f"rounds_{i}_praise", r.get("praise"))
    btt = pack.get("beat_the_tutor") or {}
    for k in ("setup", "tutor_try", "win_line", "gentle_line"):
        add(f"beat_the_tutor_{k}", btt.get(k))
    return out


def pack_paths(factory_root: str | Path = FACTORY) -> list[Path]:
    return sorted(Path(factory_root).glob(PACK_GLOB))


def load_packs(factory_root: str | Path = FACTORY) -> list[dict]:
    return [json.loads(p.read_text(encoding="utf-8")) for p in pack_paths(factory_root)]


def select_packs(packs: list[dict], patterns: list[str] | None) -> list[dict]:
    if not patterns:
        return packs
    return [p for p in packs if any(fnmatch.fnmatchcase(str(p.get("id")), pat) for pat in patterns)]


# ---------------------------------------------------------------------------
# Default praise (kR3DefaultPraise + the app's translations)
# ---------------------------------------------------------------------------

_DART_STR = r"'((?:[^'\\]|\\.)*)'|\"((?:[^\"\\]|\\.)*)\""


def _unescape_dart(s: str) -> str:
    return re.sub(r"\\(.)", lambda m: {"n": "\n", "t": "\t"}.get(m.group(1), m.group(1)), s)


def dart_praise_keys(engine_src: str) -> list[str]:
    m = re.search(r"kR3DefaultPraise\s*=\s*\[(.*?)\];", engine_src, re.S)
    if not m:
        raise R3Error("kR3DefaultPraise not found in the engine source")
    return re.findall(r"\(\s*'([a-z0-9_]+)'\s*,", m.group(1))


def dart_translations(src: str) -> dict[str, str]:
    out = {}
    for m in re.finditer(rf"^\s*'([a-z0-9_]+)'\s*:\s*(?:{_DART_STR})\s*,", src, re.M):
        out[m.group(1)] = _unescape_dart(m.group(2) if m.group(2) is not None else m.group(3))
    return out


def default_praise(locale: str = "en", agent_root: str | Path | None = None) -> tuple[list[tuple[str, str]], str]:
    """([(key 'r3.<tr key>', text)], source). Reads the app's key list and
    translation for `locale` from the agent checkout when it is there,
    otherwise the checked-in fallback table."""
    if locale not in LOCALES:
        raise R3Error(f"locale {locale!r} not one of {LOCALES}")
    if agent_root:
        eng = Path(agent_root) / ENGINE_DART
        tr = Path(agent_root) / TRANSLATIONS_DART.format(locale=locale)
        if eng.is_file() and tr.is_file():
            keys = dart_praise_keys(eng.read_text(encoding="utf-8"))
            table = dart_translations(tr.read_text(encoding="utf-8"))
            missing = [k for k in keys if not table.get(k, "").strip()]
            if missing:
                raise R3Error(f"no {locale} translation for {missing}")
            return [(f"r3.{k}", table[k]) for k in keys], "agent"
    fb = DEFAULT_PRAISE_FALLBACK
    return [(f"r3.{k}", t) for k, t in zip(fb["keys"], fb[locale])], "fallback"


# ---------------------------------------------------------------------------
# Respellings
# ---------------------------------------------------------------------------

def load_respellings(path: str | Path = RESPELLINGS) -> dict:
    p = Path(path)
    if not p.is_file():
        return {"by_key": {}, "by_text": {}}
    raw = json.loads(p.read_text(encoding="utf-8"))
    return {"by_key": dict(raw.get("by_key", {})), "by_text": dict(raw.get("by_text", {}))}


def respelled(key: str, text: str, resp: dict) -> str | None:
    t = resp["by_key"].get(key)
    if t is None:
        t = resp["by_text"].get(text)
    return t if t and t != text else None


# ---------------------------------------------------------------------------
# Render items
# ---------------------------------------------------------------------------

def file_id(key: str, locale: str) -> str:
    """Audio file stem. English (the packs' language) is the bare key the
    app looks up; another locale's praise gets a .<locale> suffix so it
    never overwrites the English file."""
    return key if locale == "en" else f"{key}.{locale}"


def item(key: str, text: str, locale: str, source: str, resp: dict, pron: dict | None = None) -> dict:
    display = pronunciations.display_text(text) if pronunciations.has_markup(text) else text
    tts = respelled(key, display, resp)
    f = pronounced_fields(file_id(key, locale), tts or text, pron)
    fid = file_id(key, locale)
    it = {
        "id": fid, "key": key, "locale": locale, "category": "r3", "text": display,
        "text_sha256": hashlib.sha256(display.encode("utf-8")).hexdigest(),
        "render_sha256": f["render_sha256"],
        "file": f"{AUDIO_DIR}/{fid}.mp3", "final_wav": f"r3/{fid}.wav", "script": source,
        # sentences = what the ASR gate checks per take (display words);
        # render_text = what is rendered (respelling + pronunciations).
        "sentences": f["sentences"], "render_text": f["render_text"], "asr_text": f["asr_text"],
        "sentence_wild": f["sentence_wild"], "asr_wild": f["asr_wild"], "pronounced": f["pronounced"],
        "source_text": text, "needs_listen": tts is not None or bool(f["pronounced"]),
    }
    if tts is not None or "tts_text" in f:
        it["tts_text"] = f.get("tts_text", f["asr_text"])
    return it


def all_keyed_lines(factory_root: str | Path = FACTORY, packs: list[str] | None = None,
                    locale: str = "en", agent_root: str | Path | None = None) -> list[tuple[str, str, str]]:
    """(key, text, source) in render order: packs (path order), then the
    default praise. A `packs` filter drops the shared praise lines. Pack
    text is English, so a non-English locale renders the praise lines only."""
    out = []
    if locale == "en":
        for p in select_packs(load_packs(factory_root), packs):
            src = f"r3_pack:{p.get('id')}"
            out += [(k, t, src) for k, t in pack_lines(p)]
    if not packs:
        praise, psrc = default_praise(locale, agent_root)
        out += [(k, t, f"praise:{psrc}") for k, t in praise]
    return out


def build_r3_lines(factory_root: str | Path = FACTORY, packs: list[str] | None = None,
                   only: list[str] | None = None, locale: str = "en",
                   agent_root: str | Path | None = None, respellings: dict | None = None,
                   pron: dict | None = None) -> list[dict]:
    resp = load_respellings() if respellings is None else respellings
    pron = pronunciations.load() if pron is None else pron
    rows = all_keyed_lines(factory_root, packs, locale, agent_root)
    if only:
        want = set(only)
        rows = [r for r in rows if r[0] in want]
    return [item(k, t, locale, s, resp, pron) for k, t, s in rows]


def shard(items: list, k: int, n: int) -> list:
    """Contiguous shard k (1-based) of n."""
    if not 1 <= k <= n:
        raise R3Error(f"shard {k}/{n} out of range")
    size = len(items)
    return items[(k - 1) * size // n: k * size // n]


def shard_count(n_lines: int, per_shard: int = 40, max_shards: int = 8) -> int:
    return max(1, min(max_shards, -(-n_lines // per_shard)))
