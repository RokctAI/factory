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

# Band-layout whiteboard scene for fractions-of-whole-numbers-and-sharing-problems (Part 1 Expert
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


class FractionsOfWholeNumbersAndSharingProblemsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Finding a Fraction of a Whole Number
        self.write_rows(0, "Finding a Fraction of a Whole Number", [
            "Divide by the bottom",
            "Multiply by the top",
            "1/4 of 240 = 60",
            "3/4 of 240 = 180",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Fractions in Sharing and Grouping Problems
        self.next_band(1)
        self.write_rows(1, "Fractions in Sharing and Grouping Problems", [
            "7 pizzas for 4 friends",
            "7/4 = 1 and 3/4 each",
            "5 litres for 8: 5/8 of a litre",
            "3 cups hold 12 quarter cups",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Fraction Problems with Money and Measurement
        self.next_band(2)
        self.write_rows(2, "Fraction Problems with Money and Measurement", [
            "1/5 of R450 = R90 off",
            "Sale price: R360",
            "3/4 of 2 000 m = 1 500 m",
            "2/3 of 60 minutes = 40 minutes",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``3/4 of 240 = 320''",
            "``7 pizzas for 4 friends: 4/7 each''",
            "``The sale price is R90''",
            "``3/4 of 2 km = 750 m''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Divide, Then Multiply
        self.next_band(4)
        self.write_rows(4, "Divide, Then Multiply", [
            "Divide, then multiply",
            "240 divided by 4 = 60",
            "3 times 60 = 180",
            "2/5 of 350 = 140",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Share It Fairly
        self.next_band(5)
        self.write_rows(5, "Share It Fairly", [
            "Share it fairly",
            "Things on top",
            "People underneath",
            "1 and 3/4 pizzas",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Fractions in Real Life
        self.next_band(6)
        self.write_rows(6, "Fractions in Real Life", [
            "Fractions in real life",
            "R90 off, R360 to pay",
            "1 500 m walked",
            "40 minutes",
        ], scale=0.9, box=1)

        last = Tex("To find a fraction of an amount, divide by the bottom and multiply by the top, and when sharing, the things go on top.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
