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

# Band-layout whiteboard scene for area-of-squares-and-rectangles (Part 1 Expert
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


class AreaOfSquaresAndRectanglesSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Counting Squares
        self.write_rows(0, "Counting Squares", [
            "Area: squares inside",
            "Unit: square centimetres, square metres",
            "Two halves make one whole",
            "12 whole + 4 halves = 14",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): The Rule for Rectangles and Squares
        self.next_band(1)
        self.write_rows(1, "The Rule for Rectangles and Squares", [
            "Area = length times width",
            "4 m by 3 m: 12 square metres",
            "Square 5 cm: 25 square centimetres",
            "24 divided by 6 = 4 m wide",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Using Area to Solve Problems
        self.next_band(2)
        self.write_rows(2, "Using Area to Solve Problems", [
            "L-shape: 30 + 20 = 50",
            "Or 80 minus 30 = 50",
            "4 tiles per square metre: 48 tiles",
            "30 times R25 = R750",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Area = 4 + 3 = 7''",
            "``Area: 12 m''",
            "``Half squares counted as whole''",
            "``L-shape: 10 times 8 = 80''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Count the Squares
        self.next_band(4)
        self.write_rows(4, "Count the Squares", [
            "Count the squares",
            "Space inside",
            "Halves join up",
            "Square units",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Rows Times Columns
        self.next_band(5)
        self.write_rows(5, "Rows Times Columns", [
            "Rows times columns",
            "3 rows of 5",
            "Length times width",
            "12 square metres",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Split and Add
        self.next_band(6)
        self.write_rows(6, "Split and Add", [
            "Split and add",
            "30 square metres",
            "20 square metres",
            "50 square metres",
        ], scale=0.9, box=3)

        last = Tex("Area is the number of unit squares inside a shape: for a rectangle, length times width.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
