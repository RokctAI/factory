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
        # --- Band 0 (subtopic_1): Changing Units of Length
        self.write_rows(0, "Changing Units of Length", [
            "1 cm = 10 mm, 1 m = 100 cm",
            "1 km = 1 000 m",
            "1 m 35 cm = 135 cm",
            "1 m 5 cm = 105 cm",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Fractions of Units
        self.next_band(1)
        self.write_rows(1, "Fractions of Units", [
            "Half a metre: 50 cm",
            "Quarter of a metre: 25 cm",
            "Half a km: 500 m",
            "Half a cm: 5 mm",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Length Problems
        self.next_band(2)
        self.write_rows(2, "Length Problems", [
            "1 200 m + 1 200 m = 2 km 400 m",
            "200 cm - 45 cm = 155 cm",
            "5 laps of 400 m = 2 km",
            "300 cm shared by 4: 75 cm",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``4 m = 4 cm''",
            "``1 m 5 cm = 150 cm''",
            "``A quarter metre is 4 cm''",
            "``2 m minus 45 cm is impossible''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Tens, Hundreds, Thousands
        self.next_band(4)
        self.write_rows(4, "Tens, Hundreds, Thousands", [
            "10, 100, 1 000",
            "Smaller: multiply",
            "Bigger: group",
            "Watch the zeros",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Halves and Quarters of Lengths
        self.next_band(5)
        self.write_rows(5, "Halves and Quarters of Lengths", [
            "Half m: 50 cm",
            "Quarter m: 25 cm",
            "Half km: 500 m",
            "Half cm: 5 mm",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Length Stories
        self.next_band(6)
        self.write_rows(6, "Length Stories", [
            "Smaller unit first",
            "200 - 45 = 155 cm",
            "5 times 400 m = 2 km",
            "300 cm into 4: 75 cm",
        ], scale=0.9, box=2)

        last = Tex("10 mm, 100 cm, 1 000 m: multiply to go smaller, group to go bigger, and always write the unit.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
