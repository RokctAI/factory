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
        # --- Band 0 (subtopic_1): What Area Is
        self.write_rows(0, "What Area Is", [
            "Area: the surface inside",
            "Cover with squares, no gaps",
            "Count them: square units",
            "Same size squares to compare",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Counting Squares in Rectangles
        self.next_band(1)
        self.write_rows(1, "Counting Squares in Rectangles", [
            "5 long, 3 wide: 15 squares",
            "4 rows of 6: 24 squares",
            "Kitchen 4 by 3: 12 square metres",
            "L shape: 10 + 4 = 14",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Irregular Shapes and Area versus Perimeter
        self.next_band(2)
        self.write_rows(2, "Irregular Shapes and Area versus Perimeter", [
            "Count full squares",
            "Two halves make one",
            "Leaf: 12 + 3 = 15 squares",
            "Same area, different perimeter",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Area: count the edges''",
            "``Gaps are fine''",
            "``Each half square is 1''",
            "``Same area, same perimeter''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): The Space Inside
        self.next_band(4)
        self.write_rows(4, "The Space Inside", [
            "Space inside",
            "Equal squares",
            "No gaps, no overlaps",
            "Square units",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Rows of Squares
        self.next_band(5)
        self.write_rows(5, "Rows of Squares", [
            "Count in rows",
            "3 rows of 5: 15",
            "Kitchen: 12",
            "Split L shapes",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Leaves, Puddles and the Difference
        self.next_band(6)
        self.write_rows(6, "Leaves, Puddles and the Difference", [
            "Full squares first",
            "Two halves make one",
            "About 15 squares",
            "Area is not perimeter",
        ], scale=0.9, box=1)

        last = Tex("Area counts the squares inside, in square units; perimeter walks the edge, in units of length.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
