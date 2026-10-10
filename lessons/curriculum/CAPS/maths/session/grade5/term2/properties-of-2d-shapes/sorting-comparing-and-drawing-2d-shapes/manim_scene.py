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

# Band-layout whiteboard scene for sorting-comparing-and-drawing-2d-shapes (Part 1 Expert
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


class SortingComparingAndDrawing2dShapesSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Straight Sides and Curved Sides
        self.write_rows(0, "Straight Sides and Curved Sides", [
            "Only straight: triangle, hexagon",
            "Only curved: circle, oval",
            "Both: semicircle, door shape",
            "Door: 3 straight, 1 curved",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Sorting and Comparing by Number of Sides
        self.next_band(1)
        self.write_rows(1, "Sorting and Comparing by Number of Sides", [
            "3 sides: all triangles",
            "4 sides: square, rectangle, kite",
            "Size and colour do not matter",
            "Hexagon: 3 more sides than triangle",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Drawing Shapes on Grid Paper
        self.next_band(2)
        self.write_rows(2, "Drawing Shapes on Grid Paper", [
            "Rectangle: 5 right, 3 up",
            "Then 5 left, 3 down",
            "Count squares, not lines",
            "House pentagon: 5 sides",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Semicircle with the polygons''",
            "``Big and small triangles apart''",
            "``Counting lines: a side of 4''",
            "``The square top kept inside''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Straight or Curved
        self.next_band(4)
        self.write_rows(4, "Straight or Curved", [
            "Straight or curved",
            "Triangle: straight",
            "Circle: curved",
            "Semicircle: both",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Count and Sort
        self.next_band(5)
        self.write_rows(5, "Count and Sort", [
            "Count and sort",
            "3 sides, 4 sides, 5, 6",
            "Ignore size and colour",
            "Hexagon 6, triangle 3",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Draw on the Grid
        self.next_band(6)
        self.write_rows(6, "Draw on the Grid", [
            "Draw on the grid",
            "5 right, 3 up, 5 left, 3 down",
            "Count the squares",
            "Check it is closed",
        ], scale=0.9, box=2)

        last = Tex("Sort by one property at a time, count only the sides, and on grid paper count the squares and check that every shape is closed.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
