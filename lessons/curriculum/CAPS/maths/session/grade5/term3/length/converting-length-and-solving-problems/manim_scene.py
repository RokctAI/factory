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

# Band-layout whiteboard scene for converting-length-and-solving-problems (Part 1 Expert
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


class ConvertingLengthAndSolvingProblemsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Changing Bigger Units to Smaller
        self.write_rows(0, "Changing Bigger Units to Smaller", [
            "10 mm is 1 cm, 100 cm is 1 m",
            "1 000 m is 1 km",
            "5 km is 5 000 m",
            "4 m 5 cm is 405 cm",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Changing Smaller Units to Bigger, and Fractions
        self.next_band(1)
        self.write_rows(1, "Changing Smaller Units to Bigger, and Fractions", [
            "600 cm is 6 m",
            "2 500 m is 2 and 1/2 km",
            "Half a kilometre is 500 m",
            "Three quarters of a metre: 75 cm",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Solving Length Problems
        self.next_band(2)
        self.write_rows(2, "Solving Length Problems", [
            "1 750 m + 2 500 m = 4 250 m",
            "5 000 minus 4 250 is 750 m",
            "6 m is 600 cm: 24 medals",
            "Water every 500 m: 9 stations",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``5 km is 500 m''",
            "``4 m 5 cm is 45 cm''",
            "``Half a kilometre is 50 m''",
            "``Adding without converting''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Big to Small: Multiply
        self.next_band(4)
        self.write_rows(4, "Big to Small: Multiply", [
            "Big to small: multiply",
            "5 km is 5 000 m",
            "3 m is 300 cm",
            "7 cm is 70 mm",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Small to Big: Divide
        self.next_band(5)
        self.write_rows(5, "Small to Big: Divide", [
            "Small to big: divide",
            "600 cm is 6 m",
            "Half a kilometre: 500 m",
            "Quarter of a metre: 25 cm",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Same Unit, Then Solve
        self.next_band(6)
        self.write_rows(6, "Same Unit, Then Solve", [
            "Same unit, then solve",
            "6 m is 600 cm",
            "600 divided by 25 is 24",
            "Write the unit",
        ], scale=0.9, box=2)

        last = Tex("Multiply to go to a smaller unit, divide to go to a bigger unit, and change every length to the same unit before you calculate.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
