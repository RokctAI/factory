"""Where rendered voice audio and voice references live: ONE switch.

Phase 2 of the repo split moved every voice file out of RokctAI/agent into
RokctAI/lessons (private), under voices/:

  agent (old)                                         voice repo (VOICE_ROOT=voices)
  lms/team/voice_refs/<x>.wav                         voices/refs/<x>.wav
  lms/dart/templates/assets/r3_packs/audio/<f>        voices/r3/<f>
  lms/team/{tutors,assistants}/CAPS/<id>/<audio>      voices/team/{tutors,assistants}/CAPS/<id>/<audio>
  lms/team/voices/samples/<f>                         voices/samples/<f>

<audio> is a voice file or record only: *.m4a, *.mp3, *.wav, *.timings.json,
<voice>_manifest[.<cat>].json and qc_failed.json. Persona JSON, scripts,
images and the voice specs (lms/team/voices/*.voice.json) stay in agent and
are read from an agent checkout (read-only).

Two environment variables, read once at import:

  VOICE_REPO  the repo the voice pipeline reads and writes (default
              RokctAI/lessons); the workflows take it from the same env.
  VOICE_ROOT  the folder in it (default "voices"). Set it to "." or ""
              (and VOICE_REPO=RokctAI/agent) to go back to the old agent
              layout: every path below is then the agent path, unchanged.

The workflows set both from the repository variables of the same names
(vars.VOICE_REPO, vars.VOICE_ROOT; unset -> the defaults), so flipping the
target is one settings change, no code change.

Stdlib only; ids and paths, never text.
"""
from __future__ import annotations

import os
import re
import sys

DEFAULT_REPO = "RokctAI/lessons"
DEFAULT_ROOT = "voices"

VOICE_REPO = os.environ.get("VOICE_REPO") or DEFAULT_REPO
_root = os.environ.get("VOICE_ROOT", DEFAULT_ROOT).strip().strip("/")
VOICE_ROOT = "" if _root == "." else _root

# The old agent layout (and the layout with VOICE_ROOT="").
AGENT_REFS = "lms/team/voice_refs"
AGENT_R3 = "lms/dart/templates/assets/r3_packs/audio"
AGENT_TEAM = "lms/team"            # + {tutors,assistants}/CAPS/<id>
AGENT_SAMPLES = "lms/team/voices/samples"

TEAM_RE = re.compile(r"(tutors|assistants)/CAPS/((?:tutor|assistant)_\d{3})(/.*)?")
# Voice files and records inside a tutor's / assistant's team folder.
VOICE_RECORD_RE = re.compile(
    r"(.+\.(m4a|mp3|wav)|.+\.timings\.json|[a-z][a-z0-9_]{0,31}_manifest(\.[a-z]+)?\.json|qc_failed\.json)")


def _join(root: str, sub: str) -> str:
    return f"{root}/{sub}" if root else sub


def refs_dir(root: str | None = None) -> str:
    root = VOICE_ROOT if root is None else root
    return _join(root, "refs") if root else AGENT_REFS


def r3_dir(root: str | None = None) -> str:
    root = VOICE_ROOT if root is None else root
    return _join(root, "r3") if root else AGENT_R3


def samples_dir(root: str | None = None) -> str:
    root = VOICE_ROOT if root is None else root
    return _join(root, "samples") if root else AGENT_SAMPLES


def team_base(root: str | None = None) -> str:
    """Parent of tutors/ and assistants/ (voices/team, or agent lms/team)."""
    root = VOICE_ROOT if root is None else root
    return _join(root, "team") if root else AGENT_TEAM


def team_dir(target: str, root: str | None = None) -> str:
    """The voice-repo folder of a tutor_NNN's or assistant_NNN's audio."""
    if re.fullmatch(r"tutor_\d{3}", target):
        return f"{team_base(root)}/tutors/CAPS/{target}"
    if re.fullmatch(r"assistant_\d{3}", target):
        return f"{team_base(root)}/assistants/CAPS/{target}"
    raise ValueError(f"not a tutor or assistant id: {target}")


def ref_path_re(root: str | None = None) -> str:
    """Pattern a batch's ref_path must match."""
    return re.escape(refs_dir(root)) + r"/[A-Za-z0-9_]+\.wav"


def is_voice_record(name: str) -> bool:
    """A voice file or record (by its file name) that moves with the audio."""
    return bool(VOICE_RECORD_RE.fullmatch(name))


def map_agent_path(agent_rel: str, root: str | None = None) -> str | None:
    """The voice-repo path of an agent-repo path in the path map, or None
    when the file stays in agent (persona JSON, scripts, images, specs)."""
    p = agent_rel.strip("/")
    for old, new in ((AGENT_REFS, refs_dir(root)), (AGENT_R3, r3_dir(root)), (AGENT_SAMPLES, samples_dir(root))):
        if p == old or p.startswith(old + "/"):
            return new + p[len(old):]
    if p.startswith(AGENT_TEAM + "/"):
        m = TEAM_RE.fullmatch(p[len(AGENT_TEAM) + 1:])
        if m and m.group(3) and is_voice_record(p.rsplit("/", 1)[-1]):
            return f"{team_base(root)}/{m.group(1)}/CAPS/{m.group(2)}{m.group(3)}"
    return None


def voice_path(agent_rel: str, root: str | None = None) -> str:
    """map_agent_path, but a path outside the map is an error (render outputs)."""
    out = map_agent_path(agent_rel, root)
    if out is None:
        raise ValueError(f"not a voice path: {agent_rel}")
    return out


def target_dir(target: str, voice: str = "") -> str:
    """The folder a CI target writes: 'r3', 'pronunciation' (with voice) or
    a tutor_NNN / assistant_NNN."""
    if target == "r3":
        return r3_dir()
    if target == "pronunciation":
        if not re.fullmatch(r"[a-z][a-z0-9_]{0,31}", voice):
            raise ValueError("bad voice name")
        return f"{samples_dir()}/pronunciation/{voice}"
    return team_dir(target)


def manifest_patterns(root: str | None = None) -> list[str]:
    """Non-cone sparse-checkout patterns for every voice manifest (the
    scheduled scan reads only these from the voice repo's main)."""
    return [f"/{team_base(root)}/tutors/CAPS/*/*manifest*.json",
            f"/{team_base(root)}/assistants/CAPS/*/*manifest*.json",
            f"/{r3_dir(root)}/*manifest*.json"]


def main(argv: list[str]) -> int:
    """CLI for the shell steps (one source for the paths):

        voice_paths.py repo                  VOICE_REPO
        voice_paths.py dir TARGET [VOICE]    target_dir
        voice_paths.py refs|r3|samples       the folders
        voice_paths.py manifests             manifest_patterns, one per line
        voice_paths.py map AGENT_PATH        map_agent_path (exit 1 if none)
    """
    try:
        cmd = argv[1]
        if cmd == "repo":
            print(VOICE_REPO)
        elif cmd == "manifests":
            print("\n".join(manifest_patterns()))
        elif cmd == "dir":
            print(target_dir(argv[2], argv[3] if len(argv) > 3 else ""))
        elif cmd in ("refs", "r3", "samples"):
            print({"refs": refs_dir, "r3": r3_dir, "samples": samples_dir}[cmd]())
        elif cmd == "map":
            out = map_agent_path(argv[2])
            if out is None:
                return 1
            print(out)
        else:
            raise IndexError
    except IndexError:
        print(main.__doc__, file=sys.stderr)
        return 2
    except ValueError as exc:
        print(f"::error::{exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
