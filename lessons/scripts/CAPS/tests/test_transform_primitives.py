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

# Licensed under the MIT License.
# Copyright 2026 RokctAI
"""Unit tests for the transform emit path — manim_exporter.py's morph
export and the R1 vocabulary gate that admits it (stdlib unittest).

Covers decision #51's exporter half: a Transform-family animation is
exported as the pair the player consumes — a `clear` of the element being
replaced, then a `transform` primitive carrying the morph's END STATE
inline under `to`. The schema asserted here is the one the painter reads
(lms_sdk whiteboard_canvas.dart `case 'transform':`): `to` is a nested
DRAWABLE primitive, never another transform, and a near-miss renders a grey
marker dot instead of the new line — which is why lesson_compliance R1
checks the nested type too, and is exercised here against the exporter's
own output rather than a hand-written fixture.

manim is a heavy third-party dependency and this suite runs with none (see
.github/workflows/unit_tests.yml), so a stand-in module carrying the mobject
classes the serializer type-checks against is installed before import. The
serializer itself is the real one — only manim is faked, never the exporter.

Run from the repo root:
    python3 -m unittest discover -s lessons/scripts/CAPS/tests -v
"""

import json
import sys
import tempfile
import types
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def _install_fake_manim():
    """The manim surface _primitive_of actually uses: the mobject classes it
    isinstance-checks and the UL corner constant."""
    manim = types.ModuleType("manim")

    class Mobject:
        pass

    for name in ("Text", "Dot", "Circle", "Line", "Rectangle", "VGroup"):
        setattr(manim, name, type(name, (Mobject,), {}))
    manim.Arrow = type("Arrow", (manim.Line,), {})
    manim.Mobject = Mobject
    manim.UL = "UL"
    sys.modules["manim"] = manim
    return manim


MANIM = _install_fake_manim()

import lesson_compliance  # noqa: E402
import manim_exporter  # noqa: E402

# Only the ratio matters; a square frame keeps the expected numbers readable
# (world x=0 is normalized 0.5, y=0 is 0.5, y up becomes y down).
SCALER = {"fw": 10.0, "fh": 10.0}

# The painter's drawable vocabulary, transcribed from the player's single
# source of truth (whiteboard_primitive_types.dart kDrawablePrimitiveTypes).
# A `to` outside this set falls through to the marker dot.
PAINTER_DRAWS = {"dot", "circle", "rect", "line", "text", "transform"}


class Tex(MANIM.Text):
    """A lesson equation as the exporter's Tex shim leaves it: a Text that
    remembers its latex string."""

    def __init__(self, tex, x=0.0, y=0.0):
        self.tex_string = tex
        self.original_text = tex.replace("$", "")
        self._point = (x, y)

    def get_center(self):
        return self._point

    def get_corner(self, _direction):
        return self._point


class Dot(MANIM.Dot):
    def get_center(self):
        return (0.0, 0.0)


class Group(MANIM.VGroup):
    """A morph target that is several mobjects, not one primitive."""

    def __init__(self, *submobjects):
        self.submobjects = list(submobjects)

    def get_center(self):
        return (0.0, 0.0)

    def get_family(self):
        return [self] + self.submobjects


class Sticker(MANIM.Mobject):
    """Real geometry the serializer does not recognize — it ships as an
    unknown type the painter renders as a marker dot."""

    def get_center(self):
        return (0.0, 0.0)

    def get_num_points(self):
        return 4


class Transform:
    def __init__(self, mobject, target_mobject):
        self.mobject = mobject
        self.target_mobject = target_mobject


class ReplacementTransform(Transform):
    pass


class TransformFromCopy(Transform):
    pass


class TransformMatchingTex:
    """The matching family exactly as manim 0.21.0 leaves it
    (transform_matching_parts.py:139-142).

    It is an AnimationGroup, so `mobject` is NOT the source: AnimationGroup
    hands its synthetic `self.group` up to Animation (composition.py:75-79),
    a Group built from the SUB-animations' mobjects — the matched and faded
    part groups — which the exporter has never emitted. The source being
    replaced is `to_remove[0]`; `to_remove[1]` is the fade_target copy. The
    target is `to_add`.

    Faking `mobject = mobject` here would hide exactly the bug this class
    exists to catch, so it must stay a group that is neither mobject."""

    def __init__(self, mobject, target_mobject):
        self.mobject = Group(Group(), Group())
        self.to_remove = [mobject, Group()]
        self.to_add = target_mobject


class Write:
    def __init__(self, mobject):
        self.mobject = mobject


def emit(animation, ids, at_time=1.0):
    """One play() call's morph half: capture the anchor, then emit."""
    morph = manim_exporter._morph_of(animation, SCALER)
    if morph is None:
        return None
    return manim_exporter._emit_morph(morph, at_time, SCALER, ids)


class MorphDetectionTests(unittest.TestCase):
    def test_the_transform_family_is_a_morph(self):
        for animation in (Transform(Tex("a"), Tex("b")),
                          ReplacementTransform(Tex("a"), Tex("b")),
                          TransformMatchingTex(Tex("a"), Tex("b"))):
            self.assertIsNotNone(
                manim_exporter._morph_of(animation, SCALER),
                f"{type(animation).__name__} should export as a morph")

    def test_a_plain_animation_is_not_a_morph(self):
        self.assertIsNone(manim_exporter._morph_of(Write(Tex("a")), SCALER))

    def test_transform_from_copy_stays_on_the_add_only_path(self):
        # It reverses its arguments and leaves the original on the board, so
        # nothing is replaced and nothing may be cleared.
        self.assertIsNone(
            manim_exporter._morph_of(TransformFromCopy(Tex("a"), Tex("b")),
                                     SCALER))


class EmittedPairTests(unittest.TestCase):
    def setUp(self):
        self.ids = manim_exporter._ElementIds()
        self.source = Tex("$2x = 8$", x=-2.0, y=1.0)
        self.written = self.ids.new(self.source)  # already on the board

    def test_clear_precedes_the_transform_and_names_the_old_element(self):
        emitted = emit(Transform(self.source, Tex("$x = 4$", x=-2.0, y=1.0)),
                       self.ids, at_time=3.25)
        self.assertEqual([p["primitive"] for p in emitted],
                         ["clear", "transform"])
        self.assertEqual(emitted[0]["target"], self.written)
        self.assertEqual(emitted[0]["time"], 3.25)
        self.assertEqual(emitted[1]["time"], 3.25)

    def test_the_transform_carries_the_end_state_as_a_nested_primitive(self):
        emitted = emit(Transform(self.source, Tex("$x = 4$", x=2.0, y=-1.0)),
                       self.ids)
        morph = emitted[1]
        self.assertEqual(morph["to"], {"primitive": "text",
                                       "position": {"x": 0.7, "y": 0.6},
                                       "text": "x = 4",
                                       "latex": "$x = 4$"})
        self.assertIn(morph["to"]["primitive"], PAINTER_DRAWS)

    def test_a_transform_never_nests_another_transform(self):
        self.assertNotIn("transform", manim_exporter.MORPH_TARGET_PRIMITIVES)

    def test_the_anchor_is_the_position_before_the_morph(self):
        # The source is mutated in place by a real Transform, so the anchor
        # has to be read from its pre-morph state.
        emitted = emit(Transform(self.source, Tex("$x = 4$", x=2.0, y=-1.0)),
                       self.ids)
        self.assertEqual(emitted[1]["position"], {"x": 0.3, "y": 0.4})

    def test_the_emitted_keys_are_exactly_what_the_painter_reads(self):
        emitted = emit(Transform(self.source, Tex("$x = 4$")), self.ids)
        self.assertEqual(set(emitted[0]), {"time", "primitive", "target"})
        self.assertEqual(set(emitted[1]),
                         {"time", "primitive", "id", "position", "to"})

    def test_an_unrecorded_source_clears_nothing(self):
        # Nothing of the source is on the board, so there is no id to erase
        # and a clear would be a lie.
        emitted = emit(Transform(Tex("$2x = 8$"), Tex("$x = 4$")), self.ids)
        self.assertEqual([p["primitive"] for p in emitted], ["transform"])

    def test_the_matching_family_target_is_read_from_to_add(self):
        emitted = emit(TransformMatchingTex(self.source, Tex("$x = 4$")),
                       self.ids)
        self.assertEqual(emitted[-1]["to"]["latex"], "$x = 4$")

    def test_the_matching_family_source_is_read_from_to_remove(self):
        # TransformMatchingTex is the idiomatic live-solve animation, and it
        # is an AnimationGroup: its `mobject` is a synthetic Group that was
        # never emitted, so reading the source from there erases nothing and
        # the new equation paints on top of the old one. The source is
        # to_remove[0].
        emitted = emit(TransformMatchingTex(self.source,
                                            Tex("$x = 4$", x=-2.0, y=1.0)),
                       self.ids, at_time=3.25)
        self.assertEqual([p["primitive"] for p in emitted],
                         ["clear", "transform"])
        self.assertEqual(emitted[0]["target"], self.written)
        # The anchor comes off the source too, not off the synthetic group
        # (which serializes to nothing at all).
        self.assertEqual(emitted[1]["position"], {"x": 0.3, "y": 0.4})


class FallThroughTests(unittest.TestCase):
    """Morphs the player cannot render stay on the add-only path, which
    exports them exactly as it did before — no clear, no transform."""

    def setUp(self):
        self.ids = manim_exporter._ElementIds()

    def test_a_group_target_falls_through(self):
        source = Tex("$2x = 8$")
        self.ids.new(source)
        self.assertEqual(
            emit(Transform(source, Group(Tex("$x = 4$"), Dot())), self.ids),
            [])

    def test_an_unknown_target_type_falls_through(self):
        # It would serialize as {"primitive": "sticker"}, which the painter
        # renders as a marker dot — worse than the pre-morph line.
        source = Tex("$2x = 8$")
        self.ids.new(source)
        self.assertEqual(emit(Transform(source, Sticker()), self.ids), [])


class ChainedMorphTests(unittest.TestCase):
    """The live-solve style morphs the same line again and again; each step
    has to erase the step actually on the board."""

    def setUp(self):
        self.ids = manim_exporter._ElementIds()

    def test_in_place_chain_clears_the_previous_morph(self):
        line = Tex("$2x + 3 = 11$")
        first = self.ids.new(line)
        step_two = emit(Transform(line, Tex("$2x = 8$")), self.ids)
        step_three = emit(Transform(line, Tex("$x = 4$")), self.ids)
        self.assertEqual(step_two[0]["target"], first)
        self.assertEqual(step_three[0]["target"], step_two[1]["id"])
        self.assertNotEqual(step_three[1]["id"], step_two[1]["id"])

    def test_a_replacement_chain_follows_the_new_mobject(self):
        line = Tex("$2x + 3 = 11$")
        self.ids.new(line)
        replacement = Tex("$2x = 8$")
        step_two = emit(ReplacementTransform(line, replacement), self.ids)
        # The replacement is the element on the board now, so morphing IT
        # next must erase the transform, not the line it replaced.
        step_three = emit(Transform(replacement, Tex("$x = 4$")), self.ids)
        self.assertEqual(step_three[0]["target"], step_two[1]["id"])


class RecordedMarkingTests(unittest.TestCase):
    """The add-only pass must not emit a morph target a second time beside
    the transform already carrying it."""

    def test_the_target_and_its_family_are_marked_recorded(self):
        child = Tex("$x = 4$")
        target = Group(child)
        seen = set()
        manim_exporter._mark_recorded(target, seen)
        self.assertIn(id(target), seen)
        self.assertIn(id(child), seen)

    def test_a_target_without_a_family_is_still_marked(self):
        target = Tex("$x = 4$")
        seen = set()
        manim_exporter._mark_recorded(target, seen)
        self.assertIn(id(target), seen)


class ElementIdTests(unittest.TestCase):
    def test_ids_are_unique_and_stable_per_mobject(self):
        ids = manim_exporter._ElementIds()
        first, second = Tex("a"), Tex("b")
        self.assertNotEqual(ids.new(first), ids.new(second))
        self.assertEqual(ids.of(first), "e1")
        self.assertIsNone(ids.of(Tex("c")))

    def test_one_id_can_name_both_of_a_morph_s_mobjects(self):
        ids = manim_exporter._ElementIds()
        source, target = Tex("a"), Tex("b")
        element_id = ids.new(source, target)
        self.assertEqual(ids.of(source), element_id)
        self.assertEqual(ids.of(target), element_id)


class ComplianceGateTests(unittest.TestCase):
    """R1 admits the morph the exporter emits, and still catches the
    near-misses that would render as grey dots."""

    def check(self, *primitives):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "animations.json"
            path.write_text(json.dumps({"version": "1", "duration_seconds": 4.0,
                                        "primitives": list(primitives)}),
                            encoding="utf-8")
            return lesson_compliance.check_animations(str(path))

    def test_an_exported_morph_passes_the_gate(self):
        ids = manim_exporter._ElementIds()
        source = Tex("$2x = 8$", x=-2.0, y=1.0)
        written = manim_exporter._primitive_of(source, SCALER)
        written["time"] = 1.0
        written["id"] = ids.new(source)
        emitted = emit(Transform(source, Tex("$x = 4$", x=-2.0, y=1.0)), ids)
        self.assertEqual(self.check(written, *emitted), [])

    def test_a_transform_that_morphs_into_nothing_fails(self):
        errs = self.check({"time": 1.0, "primitive": "transform",
                           "position": {"x": 0.3, "y": 0.4}})
        self.assertEqual([rule for rule, _ in errs], ["R1"])
        self.assertIn("marker dot", errs[0][1])

    def test_a_transform_nesting_a_transform_fails(self):
        errs = self.check({"time": 1.0, "primitive": "transform",
                           "to": {"primitive": "transform"}})
        self.assertEqual([rule for rule, _ in errs], ["R1"])
        self.assertIn("morphs into", errs[0][1])

    def test_the_top_level_text_shorthand_passes(self):
        self.assertEqual(self.check({"time": 1.0, "primitive": "transform",
                                     "position": {"x": 0.3, "y": 0.4},
                                     "text": "x = 4"}), [])


if __name__ == "__main__":
    unittest.main()
