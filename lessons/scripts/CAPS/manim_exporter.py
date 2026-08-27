#!/usr/bin/env python3
# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
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

"""ManimExporter — runs a lesson's manim_scene.py and exports JSON primitives.

Implements supacharge-tech.md §4's "ManimExporter outputs JSON primitives"
step: the app never receives video — ReplaySDK's ManimPlayer renders these
primitives on-device (lms_sdk ManimPrimitive.fromJson expects a `primitive`
type string plus a normalized `position`/`from`; the whiteboard painter
draws dot/circle/rect/line/text plus the entry-51 `transform` event and
falls back to a marker dot for anything else, so unknown types stay
visible rather than vanishing).

How it works:
- Loads the scene module with `manim.Tex`/`manim.MathTex` shimmed onto a
  Pango-backed Text subclass that remembers the original LaTeX string. This
  removes the LaTeX-distribution requirement entirely (a full texlive is the
  single heaviest dependency a CI runner would otherwise need) at the cost of
  approximate glyph extents — acceptable because the app renders equations
  from the latex string via KaTeX, not from our metrics.
- Runs the scene through Manim's real update loop in dry_run mode (no ffmpeg,
  no frames), with Scene.play/Scene.wait wrapped to record, after each play
  call, the primitives newly present on screen stamped with the scene clock
  at the moment that animation began.
- Normalizes Manim world coordinates (frame is config.frame_width x
  config.frame_height, origin centre, y up) to the 0..1 top-left space
  CoordinateScaler expects.

BAND LAYOUT MODEL: lesson scenes lay content out in sequential vertical
BANDS along a long virtual canvas (band k = one frame-height, shifted
k * frame_height DOWN), one band per step/worked example. Content never
overwrites a previous band's space and there is no FadeOut lifecycle — the
camera simply moves to clean space (scenes subclass MovingCameraScene and
animate self.camera.frame down at each transition; earlier work stays on
the canvas, partially visible at the frame edge by design). Positions are
exported in frame units, so band-k content has y in [k, k+1] — the player
offsets its viewport by the camera track. Each camera.frame movement is
exported as a camera event {"time", "target": {x, y}} in a separate
top-level "camera" array (NOT a primitive: the ManimPlayer painter renders
unknown primitive types as marker dots, and a camera event must never
paint).

TRANSFORM EVENTS (entry 51): a Transform / ReplacementTransform /
TransformMatching* play call is exported as ONE `transform` primitive
carrying the morph's END STATE inline under "to" — a nested drawable
primitive object (dot/circle/rect/line/text, with its own
`position`/`from`) — while the event's own top-level "position" is the
source's anchor. The player renders that resolved target rather than
re-simulating the morph. The source element leaves the board through the
existing removal vocabulary: if it was exported earlier it is retro-stamped
with an "id" and a paired {"primitive": "clear", "target": <id>,
"animation": "fade_out"} removal is emitted at the same timestamp,
ordered before the transform event. A morph whose target does not
serialize to a plainly drawable primitive (e.g. a group) skips the
transform path entirely and falls back to the add-only model, so nothing
is half-emitted. TransformFromCopy is excluded on purpose: it reverses
its constructor arguments and morphs a COPY, leaving the original on the
board — nothing is replaced, so the add-only pass already exports its
outcome correctly.

Output: {"version": "1", "scene": <name>, "duration_seconds": float,
         "primitives": [{"time": s, "primitive": type, "position": {x, y},
                         ...type fields...}
                        — including "transform" events ({"to": <nested
                        drawable primitive>, "id": ..., ...}) and their
                        paired "clear" removals],
         "camera": [{"time": s, "target": {x, y}}, ...]}
"""
import argparse
import importlib.util
import itertools
import json
import sys
from pathlib import Path

# Mirror of the player's kDrawablePrimitiveTypes
# (lms_sdk whiteboard_primitive_types.dart) MINUS 'transform' itself: a
# transform's morph target must be a plainly drawable primitive — the
# painter refuses a nested 'transform' and anything it cannot draw.
DRAWABLE_PRIMITIVE_TYPES = frozenset({"dot", "circle", "rect", "line", "text"})


def _install_tex_shim():
    """Replace Tex/MathTex with a Text stand-in that keeps the tex string."""
    import manim

    class _TexShim(manim.Text):
        def __init__(self, *tex_strings, **kwargs):
            tex = " ".join(str(s) for s in tex_strings)
            self.tex_string = tex
            # Rough plain-text form for painters without KaTeX.
            plain = (tex.replace("$", "").replace(r"\rightarrow", "->")
                        .replace(r"\times", "x").replace("{", "").replace("}", ""))
            kwargs.pop("arg_separator", None)
            kwargs.pop("tex_environment", None)
            kwargs.pop("tex_template", None)
            super().__init__(plain or " ", font_size=36)

    manim.Tex = _TexShim
    manim.MathTex = _TexShim
    return _TexShim


def _primitive_of(mobject, scaler):
    """Serialize one mobject to a ManimPlayer primitive dict (or None)."""
    import manim

    def norm(point):
        x, y = float(point[0]), float(point[1])
        return {
            "x": round((x + scaler["fw"] / 2) / scaler["fw"], 4),
            "y": round((scaler["fh"] / 2 - y) / scaler["fh"], 4),
        }

    center = mobject.get_center()
    name = type(mobject).__name__

    if hasattr(mobject, "tex_string"):
        return {"primitive": "text", "position": norm(mobject.get_corner(manim.UL)),
                "text": getattr(mobject, "original_text", "") or mobject.tex_string,
                "latex": mobject.tex_string}
    if isinstance(mobject, manim.Text):
        return {"primitive": "text", "position": norm(mobject.get_corner(manim.UL)),
                "text": mobject.original_text}
    if isinstance(mobject, manim.Dot):
        return {"primitive": "dot", "position": norm(center)}
    if isinstance(mobject, manim.Circle):
        return {"primitive": "circle", "position": norm(center),
                "radius": round(float(mobject.width) / 2 / scaler["fw"], 4)}
    if isinstance(mobject, (manim.Arrow, manim.Line)):
        return {"primitive": "line", "from": norm(mobject.get_start()),
                "to": norm(mobject.get_end()),
                "arrow": isinstance(mobject, manim.Arrow)}
    if isinstance(mobject, manim.Rectangle):
        return {"primitive": "rect", "position": norm(center),
                "width": round(float(mobject.width) / scaler["fw"], 4),
                "height": round(float(mobject.height) / scaler["fh"], 4)}
    if isinstance(mobject, manim.VGroup) or name in ("VDict", "Group"):
        return None  # children serialize individually
    # Unknown types still ship (painter renders a visible marker dot) — but
    # only if they carry real geometry. Manim leaves empty base Mobject
    # containers behind after FadeOut etc.; those have no points and must
    # not become phantom centre-screen dots. Returning None lets visit()
    # recurse in case an unrecognized group holds real submobjects.
    try:
        has_geometry = mobject.get_num_points() > 0
    except Exception:
        has_geometry = False
    if has_geometry:
        return {"primitive": name.lower(), "position": norm(center)}
    return None


def _transform_parts(animation):
    """(source, target) mobjects for a transform-family animation, else None.

    Covers manim.Transform and its replacing subclasses
    (ReplacementTransform, ...) plus the TransformMatching* family, which is
    an AnimationGroup rather than a Transform and records its pair as
    to_remove/to_add (its `mobject` is a synthetic Group built from the
    sub-animations, never the lesson's own mobject). Anything else —
    including Transforms whose parts can't be identified — returns None and
    stays on the add-only path.

    TransformFromCopy is excluded on purpose: its constructor reverses its
    arguments (Transform(target, source)) and it interpolates backwards, so
    it morphs a COPY into place and leaves the original on the board.
    Nothing is replaced — the add-only pass already exports its outcome
    correctly, and a clear here would erase an element still visible.
    """
    import manim
    from manim.animation.transform_matching_parts import (
        TransformMatchingAbstractBase,
    )

    if isinstance(animation, TransformMatchingAbstractBase):
        to_remove = animation.to_remove
        source = (to_remove[0]
                  if isinstance(to_remove, (list, tuple)) and to_remove
                  else to_remove)
        target = animation.to_add
        if source is None or target is None:
            return None
        return source, target
    if isinstance(animation, manim.TransformFromCopy):
        return None  # morphs a copy; replaces nothing (see docstring)
    if isinstance(animation, manim.Transform):
        source = getattr(animation, "mobject", None)
        target = getattr(animation, "target_mobject", None)
        if source is None or target is None or source is target:
            return None
        return source, target
    return None


def _emit_morph_events(source, target, source_prim, at_time, scaler,
                       primitives, seen, emitted, new_element_id):
    """Append the events one morph contributes, in the order the player
    reads them: the `clear` of the element being replaced (omitted when
    that element was never emitted — a clear would be a lie), then the
    `transform` carrying the END STATE inline under `to`. `source_prim` is
    the source's serialization captured BEFORE the animation ran (an
    in-place Transform mutates the source into the target), and supplies
    the event's anchor.

    A morph whose target does not serialize to a plainly drawable
    primitive (a VGroup of several mobjects, an unrecognized type) appends
    nothing and stays on the add-only path, which exports the pieces
    individually, exactly as before. Returns the events appended.
    """
    target_prim = _primitive_of(target, scaler)
    if (target_prim is None or
            target_prim.get("primitive") not in DRAWABLE_PRIMITIVE_TYPES):
        # Unsupported morph target (group, unknown geometry):
        # fall back to the add-only model untouched.
        return []
    anchor = None
    if source_prim is not None:
        anchor = source_prim.get("position") or source_prim.get("from")
    if anchor is None:
        anchor = (target_prim.get("position")
                  or target_prim.get("from")
                  or {"x": 0.5, "y": 0.5})
    prior = emitted.get(id(source))
    events = []
    if prior is not None:
        # The source is on the board: retro-stamp it with an id
        # (dicts stay mutable until the payload is written) and
        # fade it out at the moment the morph begins. Appended
        # before the transform event and sorted stably, so the
        # player sees clear-then-draw.
        prior_id = prior.setdefault("id", new_element_id())
        events.append({
            "time": round(at_time, 2),
            "primitive": "clear",
            "target": prior_id,
            "animation": "fade_out",
        })
    event = {
        "time": round(at_time, 2),
        "primitive": "transform",
        "id": new_element_id(),
        "position": dict(anchor),
        "to": target_prim,
    }
    events.append(event)
    primitives.extend(events)
    # Neither side of the morph may re-emit as a plain
    # primitive: the transform event already carries the end
    # state, and ReplacementTransform/TransformMatching* put
    # the target into scene.mobjects. Both sides map to the
    # transform event, so a later morph of either one clears the
    # step actually on the board.
    seen.add(id(source))
    seen.add(id(target))
    emitted[id(source)] = event
    emitted[id(target)] = event
    return events


def export_scene(scene_file, out_path):
    _install_tex_shim()
    import manim
    from manim import config

    config.dry_run = True
    config.disable_caching = True
    config.verbosity = "ERROR"

    spec = importlib.util.spec_from_file_location("lesson_scene", scene_file)
    module = importlib.util.module_from_spec(spec)
    sys.modules["lesson_scene"] = module
    spec.loader.exec_module(module)

    # `from manim import *` pulls manim's own Scene subclasses into the
    # module namespace — only classes defined IN the lesson file count.
    scene_classes = [v for v in vars(module).values()
                     if isinstance(v, type) and issubclass(v, manim.Scene)
                     and v.__module__ == module.__name__]
    if not scene_classes:
        raise SystemExit(f"No Scene subclass found in {scene_file}")
    scene_cls = scene_classes[0]

    scaler = {"fw": float(config.frame_width), "fh": float(config.frame_height)}
    primitives = []
    camera_events = []
    seen = set()
    # id(mobject) -> the dict last emitted for it, so a transform can
    # retro-stamp its source with an "id" and clear it by that id.
    emitted = {}
    id_counter = itertools.count(1)

    def new_element_id():
        return f"el{next(id_counter)}"

    def norm_point(point):
        return {"x": round((float(point[0]) + scaler["fw"] / 2) / scaler["fw"], 4),
                "y": round((scaler["fh"] / 2 - float(point[1])) / scaler["fh"], 4)}

    class Recorder(scene_cls):
        def play(self, *args, **kwargs):
            started_at = float(self.renderer.time)
            # Snapshot transform SOURCES before the update loop runs:
            # Transform mutates the source mobject's geometry in place, so
            # its pre-morph serialization only exists now.
            pending_transforms = []
            for animation in args:
                parts = _transform_parts(animation)
                if parts is not None:
                    source, target = parts
                    pending_transforms.append(
                        (source, target, _primitive_of(source, scaler)))
            super().play(*args, **kwargs)
            self._record_transforms(pending_transforms, started_at)
            self._record(started_at)
            self._record_camera(started_at)

        def _record_transforms(self, pending, at_time):
            # Entry 51 transform events (contract shape defined by the
            # player's whiteboard_canvas.dart 'transform' case): one event
            # per morph, END STATE nested under "to", source cleared via
            # the removal vocabulary. See TRANSFORM EVENTS in the module
            # docstring and _emit_morph_events (module level, so the unit
            # suite exercises the real emit path without a scene run).
            for source, target, source_prim in pending:
                _emit_morph_events(source, target, source_prim, at_time,
                                   scaler, primitives, seen, emitted,
                                   new_element_id)

        def _record_camera(self, at_time):
            # Band transitions: a MovingCameraScene animating camera.frame
            # becomes a camera event with the new viewport centre (frame
            # units — band k's centre has y = k + 0.5). Static Scenes have
            # no frame mobject and emit nothing.
            frame = getattr(self.camera, "frame", None)
            if frame is None:
                return
            target = norm_point(frame.get_center())
            last = camera_events[-1]["target"] if camera_events else {"x": 0.5, "y": 0.5}
            if abs(target["x"] - last["x"]) > 0.01 or abs(target["y"] - last["y"]) > 0.01:
                camera_events.append({"time": round(at_time, 2), "target": target})

        def _record(self, at_time):
            # Whole-mobject granularity: a Text/Tex is ONE primitive, never
            # its Pango glyph leaves. Only unrecognized containers recurse.
            # Add-only model: each mobject is emitted once, at the scene time
            # it first appears — matching today's ManimPlayer, which only
            # accumulates primitives (no move/remove events yet).
            def visit(m):
                if id(m) in seen:
                    return
                seen.add(id(m))
                prim = _primitive_of(m, scaler)
                if prim is not None:
                    prim["time"] = round(at_time, 2)
                    primitives.append(prim)
                    emitted[id(m)] = prim
                else:
                    for sub in getattr(m, "submobjects", []):
                        visit(sub)

            for m in self.mobjects:
                visit(m)

    scene = Recorder()
    scene.render()
    duration = float(scene.renderer.time)

    payload = {
        "version": "1",
        "scene": scene_cls.__name__,
        "duration_seconds": round(duration, 2),
        "primitives": sorted(primitives, key=lambda p: p["time"]),
        "camera": camera_events,
    }
    Path(out_path).write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return payload


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--scene-file", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    payload = export_scene(args.scene_file, args.out)
    print(f"Exported {len(payload['primitives'])} primitives, "
          f"{len(payload['camera'])} camera event(s), "
          f"scene duration {payload['duration_seconds']}s -> {args.out}")


if __name__ == "__main__":
    main()
