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
        # --- Band 0 (subtopic_1): Same Amount, Different Names
        self.write_rows(0, "Same Amount, Different Names", [
            "1/2 = 2/4 = 4/8",
            "1/3 = 2/6 = 4/12",
            "1/5 = 2/10",
            "Same amount, different names",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Making and Simplifying Equivalent Fractions
        self.next_band(1)
        self.write_rows(1, "Making and Simplifying Equivalent Fractions", [
            "Times top and bottom by the same number",
            "3/4 = 6/8 = 9/12",
            "Divide top and bottom to simplify",
            "6/12 = 1/2 and 8/12 = 2/3",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Using Equivalent Fractions
        self.next_band(2)
        self.write_rows(2, "Using Equivalent Fractions", [
            "2/3 = 8/12 and 3/4 = 9/12",
            "So 3/4 is bigger",
            "6 of 12 eggs is 1/2 the box",
            "2 and 2/4 is 2 and 1/2",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``1/2 = 2/3: add 1 to top and bottom''",
            "``3/4 = 6/4''",
            "``4/8 is bigger than 1/2''",
            "``6/12 = 3/4''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Cut the Pieces Smaller
        self.next_band(4)
        self.write_rows(4, "Cut the Pieces Smaller", [
            "Cut the pieces smaller",
            "1/2 is 2 quarters",
            "1/2 is 4 eighths",
            "The amount stays the same",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Same Number Top and Bottom
        self.next_band(5)
        self.write_rows(5, "Same Number Top and Bottom", [
            "Same number top and bottom",
            "3/5 = 6/10",
            "Divide to make it simpler",
            "4/10 = 2/5",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Same Bottom, Then Compare
        self.next_band(6)
        self.write_rows(6, "Same Bottom, Then Compare", [
            "Change to the same bottom",
            "1/3 is 4/12, so 5/12 is bigger",
            "6/8 is 3/4 of the pizza",
            "9/12 is 3/4",
        ], scale=0.9, box=1)

        last = Tex("Multiply or divide the top and bottom by the same number: the pieces change, the amount stays the same.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
