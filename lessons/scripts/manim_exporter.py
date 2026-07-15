#!/usr/bin/env python3
"""ManimExporter — runs a lesson's manim_scene.py and exports JSON primitives.

Implements supacharge-tech.md §4's "ManimExporter outputs JSON primitives"
step: the app never receives video — ReplaySDK's ManimPlayer renders these
primitives on-device (lms_sdk ManimPrimitive.fromJson expects a `primitive`
type string plus a normalized `position`/`from`; the whiteboard painter
currently draws dot/circle/line/text and falls back to a marker dot for
anything else, so unknown types stay visible rather than vanishing).

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

Output: {"version": "1", "scene": <name>, "duration_seconds": float,
         "primitives": [{"time": s, "primitive": type, "position": {x, y},
                         ...type fields...}]}
"""
import argparse
import importlib.util
import json
import sys
from pathlib import Path


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
    import numpy as np

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
    seen = set()

    class Recorder(scene_cls):
        def play(self, *args, **kwargs):
            started_at = float(self.renderer.time)
            super().play(*args, **kwargs)
            self._record(started_at)

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
          f"scene duration {payload['duration_seconds']}s -> {args.out}")


if __name__ == "__main__":
    main()
