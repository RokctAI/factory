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

# Band-layout whiteboard scene for area-by-counting-squares (Part 1 Expert
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


class AreaByCountingSquaresSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Area and Square Units
        self.write_rows(0, "Area and Square Units", [
            "Area: flat surface inside",
            "Each grid square: 1 square unit",
            "5 by 3: 3 rows of 5 is 15",
            "No gaps, no overlaps",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Counting Squares in Irregular Shapes
        self.next_band(1)
        self.write_rows(1, "Counting Squares in Irregular Shapes", [
            "L shape: 8 + 4 = 12 squares",
            "Count row by row and mark",
            "Triangle: 6 whole, 4 halves",
            "4 halves make 2: area 8",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Comparing Areas and Estimating
        self.next_band(2)
        self.write_rows(2, "Comparing Areas and Estimating", [
            "4 by 3 and 6 by 2: area 12",
            "Perimeters: 14 and 16 units",
            "Curved: half or more counts 1",
            "Round rug: about 29",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Counting the dots: 24''",
            "``Halves as wholes: 10''",
            "``Area of 4 by 3 is 14''",
            "``15 with no square unit''",
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
            "3 rows of 5",
            "15 square units",
            "Mark each one",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Halves Make Wholes
        self.next_band(5)
        self.write_rows(5, "Halves Make Wholes", [
            "Halves make wholes",
            "L shape: 12",
            "Triangle: 6 + 2 = 8",
            "Two halves make one",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Same Area, Different Shape
        self.next_band(6)
        self.write_rows(6, "Same Area, Different Shape", [
            "Same area, new shape",
            "4 by 3 and 6 by 2",
            "Both 12 square units",
            "Different perimeters",
        ], scale=0.9, box=1)

        last = Tex("Count the squares row by row, pair up the halves, write square units, and remember that area is the inside and perimeter is the edge.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
