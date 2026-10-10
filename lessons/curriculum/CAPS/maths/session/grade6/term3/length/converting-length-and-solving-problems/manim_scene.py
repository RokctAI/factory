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
        # --- Band 0 (subtopic_1): Bigger Units to Smaller Units
        self.write_rows(0, "Bigger Units to Smaller Units", [
            "1 km = 1 000 m; 1 m = 100 cm",
            "12,5 km = 12 500 m",
            "3/4 km = 750 m",
            "1,75 m = 175 cm",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Smaller Units to Bigger Units
        self.next_band(1)
        self.write_rows(1, "Smaller Units to Bigger Units", [
            "8 750 m = 8,75 km",
            "175 cm = 1,75 m",
            "500 m = 1/2 km = 0,5 km",
            "35 mm = 3,5 cm",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Solving Length Problems
        self.next_band(2)
        self.write_rows(2, "Solving Length Problems", [
            "8 750 m = 8,75 km",
            "12,5 km + 8,75 km = 21,25 km",
            "50 km minus 36,5 km = 13,5 km",
            "5 m = 500 cm: 20 pieces of 25 cm",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``12,5 km = 125 m''",
            "``8 750 m = 87,5 km''",
            "``3/4 km = 75 m''",
            "``12,5 km + 8 750 m = 8 762,5''",
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
            "km to m: times 1 000",
            "m to cm: times 100",
            "3/4 km is 750 m",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Small to Big: Divide
        self.next_band(5)
        self.write_rows(5, "Small to Big: Divide", [
            "Small to big: divide",
            "m to km: divide by 1 000",
            "8 750 m is 8,75 km",
            "500 m is half a km",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Same Unit, Then Solve
        self.next_band(6)
        self.write_rows(6, "Same Unit, Then Solve", [
            "Same unit, then solve",
            "Make 8 750 m into 8,75 km",
            "12,5 + 8,75",
            "21,25 km",
        ], scale=0.9, box=3)

        last = Tex("Big unit to small unit: multiply; small unit to big unit: divide; same units before you add.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
