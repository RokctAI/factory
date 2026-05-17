#!/usr/bin/env python3
"""
call_jules — factory repo entry point.

Environment details describe this repo:
  Name  : RokctAI / factory
  Type  : Book-factory automation pipeline (socket-based)
  Scope : Generates books, briefs, overlays, and publisher assets.
          All output flows through the .rokct/ agent pipeline.
  CI    : Runs via GitHub Actions (ubuntu-latest)
  Env    : Requires MONOREPO_PAT, JULES_API_KEY (or AGENT_API_KEY),
          GROQ_API_KEY. docker/podman and ffmpeg also needed for rendering.
  Fallback: The-Rokct-Protocol is at ../../The-Rokct-Protocol/ relative to
           .rokct/skills/agent_delegation/scripts/
"""
import os
import sys

_here = os.path.dirname(os.path.abspath(__file__))

_THENR_NAME = "call_jules.py"

# Try local parent dir first (sibling to this script), then The-Rokct-Protocol
_candidates = [
    os.path.join(_here, _THENR_NAME),                         # same dir
    os.path.join(os.path.dirname(_here), _THENR_NAME),        # scripts/ dir
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(_here))),
        "The-Rokct-Protocol", "core", "skills",
        "agent_delegation", _THENR_NAME,
    ),  # workspace_parent / The-Rokct-Protocol / …
]

_thenr = next((c for c in _candidates if os.path.exists(c)), None)

if not _thenr:
    # Last resort: search upward
    _search = os.path.dirname(_here)
    for _ in range(5):
        _candidate = os.path.join(_search, "The-Rokct-Protocol", "core",
                                  "skills", "agent_delegation", _THENR_NAME)
        if os.path.exists(_candidate):
            _thenr = _candidate
            break
        _parent = os.path.dirname(_search)
        if _parent == _search:
            break
        _search = _parent

if not _thenr:
    print("Error: call_jules.py not found", file=sys.stderr)
    sys.exit(1)

# Pre-fill environment details for this repo
ENVIRONMENT_DETAILS = """
Repository: RokctAI/factory
Type: Book-factory automation pipeline (socket-based)
Scope: Generates books, briefs, overlays, and publisher assets.
All output flows through the .rokct/ agent pipeline.
CI: Runs via GitHub Actions (ubuntu-latest).
Dependencies: MONOREPO_PAT, JULES_API_KEY (or AGENT_API_KEY),
  GROQ_API_KEY, docker/podman, ffmpeg.
"""

_shared_dir = os.path.dirname(_thenr)
if _shared_dir not in sys.path:
    sys.path.insert(0, _shared_dir)

import call_jules  # noqa: E402

# If delegate_to_agent supports --environment-details, inject it
if hasattr(call_jules, "main"):
    orig_argv = sys.argv[:]
    # Only inject if the caller didn't supply it explicitly
    if "--environment-details" not in sys.argv:
        sys.argv = (
            [sys.argv[0], "--environment-details", ENVIRONMENT_DETAILS.strip(),
             "--extra-context",
             "Repo: RokctAI/factory. All .rokct/ skills and scripts are available."]
            + sys.argv[1:]
        )

    rc = call_jules.main()
else:
    print("Error: call_jules.main() not found", file=sys.stderr)
    sys.exit(1)

sys.exit(rc or 0)
