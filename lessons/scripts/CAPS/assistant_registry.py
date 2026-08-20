#!/usr/bin/env python3
# Copyright (c) 2026 RokctAI
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Assistant identity registry — the single name<->opaque-id mapping for the
session assistants (the per-grade hosts), mirroring the tutor_001..tutor_012
precedent.

Canonical ids are permanent and opaque (^assistant_\\d+$):

    assistant_001 = Thandi (grade 10, slug "thandi")
    assistant_002 = Bianca (grade 11, slug "bianca")
    assistant_003 = Mandy  (grade 12, slug "mandy")

Source of truth is roster.json under $TEAM_ROOT/assistants/CAPS (the
RokctAI/agent checkout). Because the factory and agent migrations can land
in either order, BOTH roster layouts are understood:

  v1 (name-keyed, legacy): "assistants" keyed by slug directory name
     ("thandi": {"display_name": "Thandi", "grade": 10}), "by_grade" values
     are slugs. Ids are assigned from the fixed scheme above.
  v2 (id-keyed): {"version": 2, "assistants": {"assistant_001":
     {"display_name", "slug", "grade"}, ...}, "by_grade" values are ids,
     "aliases" maps legacy keys (slugs, assistant_gNN) to ids.

When no roster is reachable (TEAM_ROOT unset and no legacy in-repo copy)
an embedded fallback of the three known assistants applies, so callers
degrade gracefully instead of losing the mapping.

Accepted aliases everywhere an identity is looked up: the canonical id
itself, the slug, the display name (case-insensitive), and the retired
grade-keyed assistant_g10/g11/g12 ids.

Dependency-free (stdlib only), like the other lessons/scripts/CAPS modules.
"""
import json
import os
import re
from pathlib import Path

ASSISTANT_ID_RE = re.compile(r"^assistant_\d+$")

# The fixed id scheme — also the fallback roster when TEAM_ROOT is absent,
# and the id assignment for a v1 (name-keyed) roster that predates ids.
FALLBACK_ASSISTANTS = {
    "assistant_001": {"display_name": "Thandi", "slug": "thandi", "grade": 10},
    "assistant_002": {"display_name": "Bianca", "slug": "bianca", "grade": 11},
    "assistant_003": {"display_name": "Mandy", "slug": "mandy", "grade": 12},
}
_SLUG_TO_ID = {v["slug"]: k for k, v in FALLBACK_ASSISTANTS.items()}


class AssistantRegistry:
    """Immutable view over one roster (either layout) or the fallback."""

    def __init__(self, assistants, extra_aliases=None):
        # assistants: {canonical_id: {"display_name", "slug", "grade"}}
        self.assistants = dict(assistants)
        self._aliases = {}  # lowercased alias -> canonical id
        for aid, info in self.assistants.items():
            self._aliases[aid.lower()] = aid
            if info.get("slug"):
                self._aliases[str(info["slug"]).lower()] = aid
            if info.get("display_name"):
                self._aliases[str(info["display_name"]).lower()] = aid
            if info.get("grade") is not None:
                self._aliases[f"assistant_g{info['grade']}"] = aid
        for alias, aid in (extra_aliases or {}).items():
            if aid in self.assistants:
                self._aliases[str(alias).lower()] = aid
        self._by_grade = {info["grade"]: aid
                          for aid, info in self.assistants.items()
                          if info.get("grade") is not None}

    def canonical_id(self, id_or_alias):
        """Canonical opaque id for an id or any accepted alias; None when
        the value names no known assistant."""
        if not id_or_alias:
            return None
        return self._aliases.get(str(id_or_alias).strip().lower())

    def display_name(self, id_or_alias):
        aid = self.canonical_id(id_or_alias)
        return self.assistants[aid]["display_name"] if aid else None

    def slug(self, id_or_alias):
        aid = self.canonical_id(id_or_alias)
        return self.assistants[aid].get("slug") if aid else None

    def assistant_for_grade(self, grade):
        """Canonical id of the grade's host; None for a grade with no host."""
        try:
            return self._by_grade.get(int(grade))
        except (TypeError, ValueError):
            return None

    def all_display_names(self):
        """Every assistant display name — the on-air host names."""
        return {info["display_name"] for info in self.assistants.values()
                if info.get("display_name")}

    def aliases(self):
        """Copy of the full alias map (lowercased alias -> canonical id)."""
        return dict(self._aliases)


def _registry_from_roster(roster):
    """AssistantRegistry from a parsed roster.json of either layout."""
    entries = roster.get("assistants") or {}
    version = roster.get("version")
    id_keyed = (str(version) == "2"
                or (entries and all(ASSISTANT_ID_RE.match(k) for k in entries)))
    assistants = {}
    if id_keyed:
        for aid, info in entries.items():
            assistants[aid] = {
                "display_name": info.get("display_name", ""),
                "slug": info.get("slug", ""),
                "grade": info.get("grade"),
            }
        return AssistantRegistry(assistants, roster.get("aliases") or {})
    # v1: keys are slug directory names; ids come from the fixed scheme.
    for slug_key, info in entries.items():
        aid = _SLUG_TO_ID.get(slug_key)
        if not aid:  # a host added before its id existed: no id to invent
            continue
        assistants[aid] = {
            "display_name": info.get("display_name", slug_key.capitalize()),
            "slug": slug_key,
            "grade": info.get("grade"),
        }
    return AssistantRegistry(assistants or FALLBACK_ASSISTANTS)


def load_registry(team_root=None):
    """Registry for a team root (defaults to $TEAM_ROOT, matching the other
    scripts). Falls back to the legacy in-repo lessons/assistants path, then
    to the embedded mapping, so it always answers."""
    if team_root is None:
        team_root = os.environ.get("TEAM_ROOT", "").strip()
    candidates = []
    if team_root:
        candidates.append(Path(team_root) / "assistants" / "CAPS" / "roster.json")
    else:
        candidates.append(Path("lessons/assistants/roster.json"))
    for path in candidates:
        try:
            return _registry_from_roster(
                json.loads(path.read_text(encoding="utf-8")))
        except (OSError, ValueError):
            continue
    return AssistantRegistry(FALLBACK_ASSISTANTS)


_DEFAULT = None


def _default():
    global _DEFAULT
    if _DEFAULT is None:
        _DEFAULT = load_registry()
    return _DEFAULT


# Module-level convenience API over the $TEAM_ROOT-resolved registry.

def canonical_id(id_or_alias):
    return _default().canonical_id(id_or_alias)


def display_name(id_or_alias):
    return _default().display_name(id_or_alias)


def slug(id_or_alias):
    return _default().slug(id_or_alias)


def assistant_for_grade(grade):
    return _default().assistant_for_grade(grade)


def all_display_names():
    return _default().all_display_names()
