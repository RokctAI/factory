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

# Band-layout whiteboard scene for measuring-perimeter (Part 1 Expert
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


class MeasuringPerimeterSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What Perimeter Is
        self.write_rows(0, "What Perimeter Is", [
            "Perimeter: distance around the edge",
            "Measure every side",
            "30 + 20 + 30 + 20 = 100 cm",
            "Same unit before adding",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Perimeter of Rectangles and Squares
        self.next_band(1)
        self.write_rows(1, "Perimeter of Rectangles and Squares", [
            "6 + 4 + 6 + 4 = 20 m",
            "Square side 5 m: 4 times 5 = 20 m",
            "Grid 5 by 3: 16 units",
            "Perimeter 30 m, length 10 m: width 5 m",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Other Shapes and Perimeter Problems
        self.next_band(2)
        self.write_rows(2, "Other Shapes and Perimeter Problems", [
            "Triangle 3, 4, 5: 12 cm",
            "Hexagon side 6: 36 cm",
            "20 m at R25 per metre: R500",
            "Gate of 1 m: 19 m of fence",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Rectangle 6 by 4: 10 m''",
            "``Count the squares inside''",
            "``4 m + 250 cm = 254''",
            "``Fence the gate too''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Walk Around the Edge
        self.next_band(4)
        self.write_rows(4, "Walk Around the Edge", [
            "All the way round",
            "Measure every side",
            "Add them up",
            "Same unit",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Add the Sides
        self.next_band(5)
        self.write_rows(5, "Add the Sides", [
            "Rectangle: add, then double",
            "6 + 4 = 10, doubled 20",
            "Square: 4 times the side",
            "Count edges, not squares",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Fences and Frames
        self.next_band(6)
        self.write_rows(6, "Fences and Frames", [
            "Add all the sides",
            "Fence: 20 m",
            "R25 a metre: R500",
            "Photo ribbon: 50 cm",
        ], scale=0.9, box=2)

        last = Tex("Perimeter: every side, all the way round, in one unit.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
