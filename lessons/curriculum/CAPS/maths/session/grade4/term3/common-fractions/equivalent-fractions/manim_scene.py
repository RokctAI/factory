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

# Band-layout whiteboard scene for equivalent-fractions (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/160/160/110/110/110 of 830 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class EquivalentFractionsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Seeing Equivalent Fractions
        self.write_rows(0, "Seeing Equivalent Fractions", [
            "Half the pizza is 2/4 and 4/8",
            "Same amount, new names",
            "1/3 = 2/6",
            "3/4 = 6/8",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Making Equivalent Fractions
        self.next_band(1)
        self.write_rows(1, "Making Equivalent Fractions", [
            "Multiply top and bottom by the same number",
            "3/4: 4 times 2 is 8, 3 times 2 is 6",
            "3/4 = 6/8",
            "2/3 = 4/6",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Using Equivalent Fractions
        self.next_band(2)
        self.write_rows(2, "Using Equivalent Fractions", [
            "3/4 = 6/8, so 3/4 beats 5/8",
            "1/2 = 4/8, so 1/2 beats 3/8",
            "6/8 = 3/4",
            "Check with two strips",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``1/2 = 2/3''",
            "``3/4 = 3/8''",
            "``4/8 is more than 1/2''",
            "``3/4 is less than 5/8 because 3 is less than 5''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Same Size Pieces
        self.next_band(4)
        self.write_rows(4, "Same Size Pieces", [
            "1/2 = 2/4 = 4/8",
            "Same amount, different names",
            "1/3 = 2/6",
            "Wall: same end point",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Times Top and Bottom
        self.next_band(5)
        self.write_rows(5, "Times Top and Bottom", [
            "Times top and bottom by the same",
            "3/4 = 6/8",
            "1/2 = 3/6",
            "Never add to both",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Put Them to Work
        self.next_band(6)
        self.write_rows(6, "Put Them to Work", [
            "3/4 = 6/8, more than 5/8",
            "1/2 = 4/8, more than 3/8",
            "6/8 is 3/4",
            "Check with two strips",
        ], scale=0.9, box=0)

        last = Tex("Multiply top and bottom by the same number: new name, same amount.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
