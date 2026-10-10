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

from manim import *

# Band-layout whiteboard scene for giving-directions-from-place-to-place (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/140/210/110/110/110 of 860 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class GivingDirectionsFromPlaceToPlaceSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.8, box=None, box_color=YELLOW):
        t = Tex(title).scale(1.15).shift(band_shift(k) + UP * 2.4)
        self.play(Write(t))
        self.wait(1.5)
        made = []
        for i, r in enumerate(rows):
            m = Tex(r).scale(scale).shift(band_shift(k) + UP * (1.3 - 0.95 * i))
            self.play(Write(m))
            self.wait(2.3)
            made.append(m)
        if box is not None:
            self.play(Create(SurroundingRectangle(made[box], color=box_color)))
            self.wait(2)
        return made

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(42)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Left, Right and Straight On
        self.write_rows(0, "Left, Right and Straight On", [
            "Left, right, straight on",
            "Left hand: the L shape",
            "They swap when you turn around",
            "Opposite, next to, corner",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Using Landmarks and Road Names
        self.next_band(1)
        self.write_rows(1, "Using Landmarks and Road Names", [
            "Turn at a landmark you can see",
            "Read road names on signs",
            "Go two blocks",
            "Count: the third building",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Giving Clear Directions
        self.next_band(2)
        self.write_rows(2, "Giving Clear Directions", [
            "Start point and direction",
            "One step at a time, in order",
            "Landmarks and road names",
            "Lost: ask a trusted adult",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Left and right never change''",
            "``Turn left, but where''",
            "``Use a parked taxi as a landmark''",
            "``Steps in any order''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Which Way
        self.next_band(4)
        self.write_rows(4, "Which Way", [
            "Left",
            "Right",
            "Straight on",
            "Face a clear way",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Where to Turn
        self.next_band(5)
        self.write_rows(5, "Where to Turn", [
            "Turn at a landmark",
            "Water tower",
            "Road names",
            "Street signs",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Step by Step
        self.next_band(6)
        self.write_rows(6, "Step by Step", [
            "Start point",
            "One step at a time",
            "Landmarks and roads",
            "End point",
        ], scale=0.9, box=1)

        last = Tex("Clear directions use left, right and straight on, with landmarks and road names, one step at a time.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
