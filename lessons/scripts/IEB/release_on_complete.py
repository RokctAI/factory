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

"""Release-on-folder-complete for the IEB session tree.

The IEB counterpart of lessons/scripts/CAPS/release_on_complete.py: it scans
session packages under lessons/curriculum/IEB/<subject>/session/... and
publishes complete, compliant packages as GitHub Releases on the agent repo,
with exactly the CAPS script's contract (same 9 content files + audio.mp3
under the audio root, same compliance/mojibake gates, same asset triple,
same idempotent skip-if-tag-exists behaviour).

WHY A SEPARATE SCRIPT — release identity must not collide with CAPS. IEB
mirror packages deliberately reuse the SAME lesson_id values as their CAPS
twins (reel_clip.json lesson_ids are byte-identical by design), so running
the CAPS script over the IEB tree would derive identical `lesson-<lesson_id>`
tags and the idempotent skip would silently drop every IEB release. This
script prefixes the release identity with `ieb_` everywhere a lesson_id
becomes a tag/release name:

    id  = ieb_<lesson_id>            (e.g. ieb_maths_g11_quadratic-equations_factoring-method)
    tag = lesson-ieb_<lesson_id>

so IEB releases can never collide with CAPS tags on the release repo. The
prefix exists at release-tooling level ONLY: on-disk package lesson_ids
(reel_clip.json etc.) stay untouched, and the lesson_slug / knowledge-bite
join key carries through unprefixed exactly as on the CAPS path.

Everything else is the CAPS machinery, imported and parameterized rather than
forked (the CAPS scripts stay the single implementation; this file owns only
the IEB session root and the `ieb_` release identity). --audio-root follows
the same convention as CAPS: a checkout of the repo audio is dropped in (the
agent repo), holding audio.mp3 at each package's IEB-relative path — i.e. the
agent repo's IEB audio home, the CAPS audio layout with CAPS -> IEB.

Usage:
  python3 lessons/scripts/IEB/release_on_complete.py --dry-run       # scan only
  python3 lessons/scripts/IEB/release_on_complete.py --max-releases 5
Exit 0 = clean (including nothing to do); 1 = at least one attempted
release failed (compliance, assembly, or publish error).
"""
import importlib.util
import sys
from pathlib import Path

# Load the CAPS implementation by file path (the scripts directories are not
# packages). The CAPS dir goes on sys.path first so the module's own sibling
# imports (assistant_registry, lesson_manifest, ...) resolve, exactly as when
# it runs directly.
_CAPS_DIR = Path(__file__).resolve().parents[1] / "CAPS"
sys.path.insert(0, str(_CAPS_DIR))
_spec = importlib.util.spec_from_file_location(
    "caps_release_on_complete", _CAPS_DIR / "release_on_complete.py")
caps = importlib.util.module_from_spec(_spec)
sys.modules["caps_release_on_complete"] = caps
_spec.loader.exec_module(caps)

SESSION_ROOT = Path("lessons/curriculum/IEB")
RELEASE_ID_PREFIX = "ieb_"

_caps_lesson_identity = caps.lesson_identity


def lesson_identity(folder, root):
    """CAPS path-derived identity with the release identity prefixed:
    id becomes ieb_<lesson_id>, tag becomes lesson-ieb_<lesson_id>. All
    other fields (subject, grade, lesson_slug, ...) carry unchanged."""
    ident = _caps_lesson_identity(folder, root)
    ident["id"] = RELEASE_ID_PREFIX + ident["id"]
    ident["tag"] = f"lesson-{ident['id']}"
    return ident


def main():
    # Parameterize the CAPS machinery for the IEB tree, then run it
    # unchanged: same scan, gates, assembly, idempotent skip, and ledger.
    caps.SESSION_ROOT = SESSION_ROOT
    caps.lesson_identity = lesson_identity
    return caps.main()


if __name__ == "__main__":
    raise SystemExit(main())
