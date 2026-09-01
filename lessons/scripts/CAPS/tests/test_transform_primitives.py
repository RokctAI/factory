#!/usr/bin/env python3
# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""Unit tests for the entry-51 transform emit path — manim_exporter.py's
morph export and the R1 vocabulary gate that admits it (stdlib unittest;
suite adopted from PR #158, adapted to this branch's isinstance-based
detection and lazy retro-stamped ids).

A Transform-family animation is exported as the pair the player consumes —
a `clear` of the element being replaced, then a `transform` primitive
carrying the morph's END STATE inline under `to`. The schema asserted here
is the one the merged painter reads (lms_sdk whiteboard_canvas.dart
`case 'transform':`): `to` is a nested DRAWABLE primitive, never another
transform, and a near-miss renders a grey marker dot instead of the new
line — which is why lesson_compliance R1 checks the nested type too, and
is exercised here against the exporter's own output rather than a
hand-written fixture.

manim is a heavy third-party dependency and this suite runs with none (see
.github/workflows/unit_tests.yml), so a stand-in manim package carrying the
classes the exporter isinstance-checks against — including the
`manim.animation.transform_matching_parts` submodule — is installed before
import. The exporter code under test is the real one; only manim is faked.

Run from the repo root:
    python3 -m unittest discover -s lessons/scripts/CAPS/tests -v
"""

import itertools
import json
import sys
import tempfile
import types
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def _install_fake_manim():
    """The manim surface the exporter actually touches: the mobject classes
    _primitive_of isinstance-checks, the UL corner constant, and the
    animation classes _transform_parts isinstance-checks (including the
    transform_matching_parts submodule it imports from)."""
    manim = types.ModuleType("manim")

    class Mobject:
        pass

    for name in ("Text", "Dot", "Circle", "Line", "Rectangle", "VGroup"):
        setattr(manim, name, type(name, (Mobject,), {}))
    manim.Arrow = type("Arrow", (manim.Line,), {})
    manim.Mobject = Mobject
    manim.UL = "UL"

    class Transform:
        """manim.Transform as _transform_parts reads it."""

        def __init__(self, mobject, target_mobject):
            self.mobject = mobject
            self.target_mobject = target_mobject

    class ReplacementTransform(Transform):
        pass

    class TransformFromCopy(Transform):
        """Exactly as real manim builds it (animation/transform.py): the
        constructor REVERSES its arguments — Transform(target, source) —
        and interpolation runs backwards, so a COPY morphs into place and
        the original stays on the board. Faking it un-reversed would hide
        the mis-handling the exclusion exists to prevent."""

        def __init__(self, mobject, target_mobject):
            super().__init__(target_mobject, mobject)

    manim.Transform = Transform
    manim.ReplacementTransform = ReplacementTransform
    manim.TransformFromCopy = TransformFromCopy

    animation_pkg = types.ModuleType("manim.animation")
    matching = types.ModuleType("manim.animation.transform_matching_parts")

    class TransformMatchingAbstractBase:
        """Base of the TransformMatching* family — an AnimationGroup, not a
        Transform, recording its pair as to_remove/to_add."""

    matching.TransformMatchingAbstractBase = TransformMatchingAbstractBase
    animation_pkg.transform_matching_parts = matching
    manim.animation = animation_pkg
    sys.modules["manim"] = manim
    sys.modules["manim.animation"] = animation_pkg
    sys.modules["manim.animation.transform_matching_parts"] = matching
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


class Sticker(MANIM.Mobject):
    """Real geometry the serializer does not recognize — it ships as an
    unknown type the painter renders as a marker dot."""

    def get_center(self):
        return (0.0, 0.0)

    def get_num_points(self):
        return 4


class TransformMatchingTex(
        MANIM.animation.transform_matching_parts.TransformMatchingAbstractBase):
    """The matching family exactly as manim 0.21.0 leaves it
    (transform_matching_parts.py).

    It is an AnimationGroup, so `mobject` is NOT the source: AnimationGroup
    hands its synthetic group up to Animation — a Group built from the
    SUB-animations' matched and faded part groups, which the exporter has
    never emitted. The source being replaced is `to_remove[0]`
    (`to_remove = [mobject, fade_target_copy]`); the target is `to_add`.
    Faking `mobject` as the source would hide exactly the mis-read this
    shape exists to catch, so it stays a group that is neither mobject."""

    def __init__(self, mobject, target_mobject):
        self.mobject = Group(Group(), Group())
        self.to_remove = [mobject, Group()]
        self.to_add = target_mobject


class Write:
    """A plain (non-replacing) animation."""

    def __init__(self, mobject):
        self.mobject = mobject


class Board:
    """The per-scene export state _emit_morph_events works against,
    mirroring export_scene's closure (primitives/seen/emitted/id counter)."""

    def __init__(self):
        self.primitives = []
        self.seen = set()
        self.emitted = {}
        self._ids = itertools.count(1)

    def new_id(self):
        return f"el{next(self._ids)}"

    def write(self, mobject, at_time=0.0):
        """Add-only emit, as Recorder._record does."""
        prim = manim_exporter._primitive_of(mobject, SCALER)
        prim["time"] = round(at_time, 2)
        self.primitives.append(prim)
        self.seen.add(id(mobject))
        self.emitted[id(mobject)] = prim
        return prim

    def play(self, animation, at_time=1.0):
        """One play() call's morph half: identify the parts and snapshot
        the source BEFORE the update loop, as Recorder.play does. Returns
        the events emitted, or None for a non-morph."""
        parts = manim_exporter._transform_parts(animation)
        if parts is None:
            return None
        source, target = parts
        source_prim = manim_exporter._primitive_of(source, SCALER)
        return manim_exporter._emit_morph_events(
            source, target, source_prim, at_time, SCALER,
            self.primitives, self.seen, self.emitted, self.new_id)


class MorphDetectionTests(unittest.TestCase):
    def test_the_transform_family_is_a_morph(self):
        for animation in (MANIM.Transform(Tex("a"), Tex("b")),
                          MANIM.ReplacementTransform(Tex("a"), Tex("b")),
                          TransformMatchingTex(Tex("a"), Tex("b"))):
            self.assertIsNotNone(
                manim_exporter._transform_parts(animation),
                f"{type(animation).__name__} should export as a morph")

    def test_the_matching_family_pair_is_to_remove_and_to_add(self):
        source, target = Tex("a"), Tex("b")
        parts = manim_exporter._transform_parts(
            TransformMatchingTex(source, target))
        self.assertIs(parts[0], source)
        self.assertIs(parts[1], target)

    def test_a_plain_animation_is_not_a_morph(self):
        self.assertIsNone(manim_exporter._transform_parts(Write(Tex("a"))))

    def test_transform_from_copy_stays_on_the_add_only_path(self):
        # It reverses its constructor arguments and morphs a COPY, leaving
        # the original on the board — nothing is replaced and nothing may
        # be cleared.
        self.assertIsNone(manim_exporter._transform_parts(
            MANIM.TransformFromCopy(Tex("a"), Tex("b"))))

    def test_a_self_transform_is_not_a_morph(self):
        line = Tex("a")
        self.assertIsNone(
            manim_exporter._transform_parts(MANIM.Transform(line, line)))


class EmittedPairTests(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.source = Tex("$2x = 8$", x=-2.0, y=1.0)
        self.written = self.board.write(self.source)  # already on the board

    def test_clear_precedes_the_transform_and_names_the_old_element(self):
        events = self.board.play(
            MANIM.Transform(self.source, Tex("$x = 4$", x=-2.0, y=1.0)),
            at_time=3.25)
        self.assertEqual([p["primitive"] for p in events],
                         ["clear", "transform"])
        self.assertEqual(events[0]["target"], self.written["id"])
        self.assertEqual(events[0]["time"], 3.25)
        self.assertEqual(events[1]["time"], 3.25)

    def test_the_source_is_retro_stamped_with_the_id_the_clear_targets(self):
        self.assertNotIn("id", self.written)  # lazy: no morph, no id
        events = self.board.play(
            MANIM.Transform(self.source, Tex("$x = 4$")))
        self.assertEqual(self.written["id"], events[0]["target"])

    def test_the_transform_carries_the_end_state_as_a_nested_primitive(self):
        events = self.board.play(
            MANIM.Transform(self.source, Tex("$x = 4$", x=2.0, y=-1.0)))
        morph = events[1]
        self.assertEqual(morph["to"], {"primitive": "text",
                                       "position": {"x": 0.7, "y": 0.6},
                                       "text": "x = 4",
                                       "latex": "$x = 4$"})
        self.assertIn(morph["to"]["primitive"], PAINTER_DRAWS)

    def test_a_transform_never_nests_another_transform(self):
        self.assertNotIn("transform",
                         manim_exporter.DRAWABLE_PRIMITIVE_TYPES)

    def test_the_anchor_is_the_position_before_the_morph(self):
        # A real in-place Transform mutates the source's geometry during
        # play, so the anchor must come from the snapshot taken before —
        # mutate the source between snapshot and emit to prove it.
        animation = MANIM.Transform(self.source,
                                    Tex("$x = 4$", x=2.0, y=-1.0))
        source, target = manim_exporter._transform_parts(animation)
        snapshot = manim_exporter._primitive_of(source, SCALER)
        self.source._point = (2.0, -1.0)  # the morph has run
        events = manim_exporter._emit_morph_events(
            source, target, snapshot, 1.0, SCALER, self.board.primitives,
            self.board.seen, self.board.emitted, self.board.new_id)
        self.assertEqual(events[-1]["position"], {"x": 0.3, "y": 0.4})

    def test_the_emitted_keys_are_exactly_what_the_player_reads(self):
        events = self.board.play(
            MANIM.Transform(self.source, Tex("$x = 4$")))
        self.assertEqual(set(events[0]),
                         {"time", "primitive", "target", "animation"})
        self.assertEqual(events[0]["animation"], "fade_out")
        self.assertEqual(set(events[1]),
                         {"time", "primitive", "id", "position", "to"})

    def test_an_unrecorded_source_clears_nothing(self):
        # Nothing of the source is on the board, so there is no id to erase
        # and a clear would be a lie.
        events = Board().play(MANIM.Transform(Tex("$2x = 8$"), Tex("$x = 4$")))
        self.assertEqual([p["primitive"] for p in events], ["transform"])

    def test_the_matching_family_target_is_read_from_to_add(self):
        events = self.board.play(
            TransformMatchingTex(self.source, Tex("$x = 4$")))
        self.assertEqual(events[-1]["to"]["latex"], "$x = 4$")

    def test_the_matching_family_source_is_read_from_to_remove(self):
        # TransformMatchingTex is the idiomatic live-solve animation, and
        # it is an AnimationGroup: its `mobject` is a synthetic group that
        # was never emitted, so reading the source from there would erase
        # nothing and paint the new equation on top of the old one. The
        # source is to_remove[0].
        events = self.board.play(
            TransformMatchingTex(self.source,
                                 Tex("$x = 4$", x=-2.0, y=1.0)),
            at_time=3.25)
        self.assertEqual([p["primitive"] for p in events],
                         ["clear", "transform"])
        self.assertEqual(events[0]["target"], self.written["id"])
        # The anchor comes off the source too, not off the synthetic group
        # (which serializes to nothing at all).
        self.assertEqual(events[1]["position"], {"x": 0.3, "y": 0.4})


class FallThroughTests(unittest.TestCase):
    """Morphs the player cannot render stay on the add-only path, which
    exports them exactly as it did before — no clear, no transform, and the
    mobjects stay unmarked so the add-only pass may still visit them."""

    def setUp(self):
        self.board = Board()
        self.source = Tex("$2x = 8$")
        self.board.write(self.source)

    def test_a_group_target_falls_through(self):
        target = Group(Tex("$x = 4$"), Dot())
        self.assertEqual(
            self.board.play(MANIM.Transform(self.source, target)), [])
        self.assertNotIn(id(target), self.board.seen)
        self.assertEqual(len(self.board.primitives), 1)  # just the write

    def test_an_unknown_target_type_falls_through(self):
        # It would serialize as {"primitive": "sticker"}, which the painter
        # renders as a marker dot — worse than the pre-morph line.
        self.assertEqual(
            self.board.play(MANIM.Transform(self.source, Sticker())), [])
        self.assertNotIn("id", self.board.primitives[0])


class TransformFromCopyTests(unittest.TestCase):
    """The exclusion in practice: the original survives and the new element
    reaches the board through the add-only pass, not a morph."""

    def test_nothing_is_cleared_and_nothing_marked_seen(self):
        board = Board()
        original = Tex("$2x = 8$", x=-2.0, y=1.0)
        board.write(original)
        new = Tex("$x = 4$", x=2.0, y=-1.0)
        self.assertIsNone(board.play(MANIM.TransformFromCopy(original, new)))
        self.assertEqual(len(board.primitives), 1)  # no clear, no transform
        # The new element is not marked seen, so the add-only pass emits it
        # at its own position — exactly the pre-transform behavior.
        self.assertNotIn(id(new), board.seen)
        board.write(new)
        self.assertEqual(board.primitives[1]["position"],
                         {"x": 0.7, "y": 0.6})


class ChainedMorphTests(unittest.TestCase):
    """The live-solve style morphs the same line again and again; each step
    has to erase the step actually on the board."""

    def setUp(self):
        self.board = Board()

    def test_in_place_chain_clears_the_previous_morph(self):
        line = Tex("$2x + 3 = 11$")
        first = self.board.write(line)
        step_two = self.board.play(MANIM.Transform(line, Tex("$2x = 8$")))
        step_three = self.board.play(MANIM.Transform(line, Tex("$x = 4$")))
        self.assertEqual(step_two[0]["target"], first["id"])
        self.assertEqual(step_three[0]["target"], step_two[1]["id"])
        self.assertNotEqual(step_three[1]["id"], step_two[1]["id"])

    def test_a_replacement_chain_follows_the_new_mobject(self):
        line = Tex("$2x + 3 = 11$")
        self.board.write(line)
        replacement = Tex("$2x = 8$")
        step_two = self.board.play(
            MANIM.ReplacementTransform(line, replacement))
        # The replacement is the element on the board now, so morphing IT
        # next must erase the transform, not the line it replaced.
        step_three = self.board.play(
            MANIM.Transform(replacement, Tex("$x = 4$")))
        self.assertEqual(step_three[0]["target"], step_two[1]["id"])

    def test_both_sides_of_a_morph_are_marked_recorded(self):
        line, target = Tex("$2x = 8$"), Tex("$x = 4$")
        self.board.write(line)
        self.board.play(MANIM.ReplacementTransform(line, target))
        # Neither may re-emit beside the transform already carrying the
        # end state.
        self.assertIn(id(line), self.board.seen)
        self.assertIn(id(target), self.board.seen)


class LazyIdTests(unittest.TestCase):
    """Ids are retro-stamped only when a morph needs them, so the export of
    the existing (transform-free) lesson library stays byte-identical."""

    def test_a_transform_free_scene_carries_no_ids_at_all(self):
        board = Board()
        board.write(Tex("$2x = 8$"))
        board.write(Dot())
        for prim in board.primitives:
            self.assertNotIn("id", prim)
        self.assertFalse(any(p["primitive"] in ("clear", "transform")
                             for p in board.primitives))

    def test_ids_are_unique_and_stable(self):
        board = Board()
        line = Tex("$2x + 3 = 11$")
        written = board.write(line)
        step_two = board.play(MANIM.Transform(line, Tex("$2x = 8$")))
        step_three = board.play(MANIM.Transform(line, Tex("$x = 4$")))
        ids = [written["id"], step_two[1]["id"], step_three[1]["id"]]
        self.assertEqual(len(ids), len(set(ids)))
        # A retro-stamped id is never reissued: the transform's own id is
        # reused as the clear target, not replaced.
        self.assertEqual(step_three[0]["target"], step_two[1]["id"])


class ComplianceGateTests(unittest.TestCase):
    """R1 admits the morph the exporter emits, and still catches the
    near-misses that would render as grey dots."""

    def check(self, *primitives):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "animations.json"
            path.write_text(json.dumps({"version": "1",
                                        "duration_seconds": 4.0,
                                        "primitives": list(primitives)}),
                            encoding="utf-8")
            return lesson_compliance.check_animations(str(path))

    def test_an_exported_morph_passes_the_gate(self):
        board = Board()
        source = Tex("$2x = 8$", x=-2.0, y=1.0)
        board.write(source, at_time=1.0)
        board.play(MANIM.Transform(source, Tex("$x = 4$", x=-2.0, y=1.0)))
        self.assertEqual(self.check(*board.primitives), [])

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
