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

# Band-layout whiteboard scene for drawing-the-rescue-device (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (260/150/150/110/110/110 of 890 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DrawingTheRescueDeviceSession(MovingCameraScene):
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
        self.wait(48)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Developing the idea into sizes
        self.write_rows(0, "Developing the idea into sizes", [
            "Measure the syringe first: 110 long, 70 travel",
            "Base 300 by 120, arms 200 by 25, doubled",
            "Pivot 60 from tip: grip; 80: wider opening",
            "Split pins, straw rod, card saddles",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): The oblique drawing
        self.next_band(1)
        self.write_rows(1, "The oblique drawing", [
            "Side view as the front face",
            "Feint: base, syringe, arms, rod, saddles",
            "Depth at 45 on the grid, half width",
            "Dark outlines, labels, title, scale",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): The working drawing
        self.next_band(2)
        self.write_rows(2, "The working drawing", [
            "One view at 1:2, every real size once",
            "Holes: diameter and position",
            "Hidden edges dashed",
            "Parts list: part, number, material, size",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Arm length chosen by looks alone''",
            "``Pivot placed without a reason''",
            "``Sizes written on the oblique drawing''",
            "``Working drawing with no parts list''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): From sketch to sizes
        self.next_band(4)
        self.write_rows(4, "From sketch to sizes", [
            "You cannot change the syringe",
            "Base holds syringe plus arms",
            "Pivot near tip grips, further back opens",
            "Joints with no slack",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Drawing it solid
        self.next_band(5)
        self.write_rows(5, "Drawing it solid", [
            "Side as front face",
            "Feint first, check, then 45 degree lines",
            "Dark over visible edges",
            "Label from plunger to jaw",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Drawing it to cut
        self.next_band(6)
        self.write_rows(6, "Drawing it to cut", [
            "Every size in millimetres",
            "Each size once, arrows and thin lines",
            "Parts list beside it",
            "A friend could build it",
        ], scale=0.9, box=3)

        last = Tex("Measure, decide with reasons, draw it to show and draw it to make: the design is complete.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
