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
            "Perimeter: all the way around",
            "30 + 20 + 30 + 20 = 100 cm",
            "Triangle 5, 6, 7 cm: 18 cm",
            "Square, 25 cm sides: 100 cm",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Measuring Perimeter with Rulers and Tapes
        self.next_band(1)
        self.write_rows(1, "Measuring Perimeter with Rulers and Tapes", [
            "Measure each side and tick it",
            "Ruler, tape, or string for curves",
            "Hexagon: 6 times 8 is 48 cm",
            "Same unit before adding",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Perimeter Problems and Checks
        self.next_band(2)
        self.write_rows(2, "Perimeter Problems and Checks", [
            "L shape: 6 sides",
            "8 + 4 + 3 + 2 + 5 + 6 = 28 m",
            "Perimeter 100, length 30",
            "Width: 40 divided by 2 is 20 cm",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Only length plus width: 50 cm''",
            "``Missing a side: 22 m''",
            "``1 m plus 45 cm is 46''",
            "``Counting squares inside''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): All the Way Around
        self.next_band(4)
        self.write_rows(4, "All the Way Around", [
            "All the way around",
            "Painting: 100 cm",
            "Square: 4 times the side",
            "Start at a corner",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Measure Every Side
        self.next_band(5)
        self.write_rows(5, "Measure Every Side", [
            "Measure every side",
            "Ruler or tape",
            "Hexagon: 48 cm",
            "Tick each side",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Count the Sides
        self.next_band(6)
        self.write_rows(6, "Count the Sides", [
            "Count the sides",
            "L shape: 6 sides",
            "28 m of fence",
            "No gaps",
        ], scale=0.9, box=2)

        last = Tex("Walk around the edge, measure and tick every side, use one unit, and add them all to find the perimeter.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
