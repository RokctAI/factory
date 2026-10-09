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

# Band-layout whiteboard scene for money-and-measurement-problems (Part 1 Expert
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


class MoneyAndMeasurementProblemsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Money Problems
        self.write_rows(0, "Money Problems", [
            "Profit is selling minus cost",
            "R15 230 minus R12 650 is R2 580",
            "R8 499 minus R5 750 is R2 749",
            "Change: count up from R367 to R500",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Measurement Problems
        self.next_band(1)
        self.write_rows(1, "Measurement Problems", [
            "Distance: end minus start",
            "47 123 minus 45 678 is 1 445 km",
            "8 450 kg + 4 975 kg = 13 425 kg",
            "Units must match",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Multi-Step Problems and Sensible Answers
        self.next_band(2)
        self.write_rows(2, "Multi-Step Problems and Sensible Answers", [
            "Step one: total spending R13 595",
            "Step two: R18 500 minus R13 595",
            "R4 905 is left each month",
            "Tank: 25 000 minus 18 113 is 6 887",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``How much is left: add''",
            "``The answer is 1 445''",
            "``3 km + 250 m = 253''",
            "``R13 595 is left''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Rands In, Rands Out
        self.next_band(4)
        self.write_rows(4, "Rands In, Rands Out", [
            "Profit: selling minus cost",
            "R2 580 profit",
            "Save: price minus what you have",
            "Change: count up",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Kilometres and Kilograms
        self.next_band(5)
        self.write_rows(5, "Kilometres and Kilograms", [
            "End reading minus start",
            "1 445 km",
            "Same units first",
            "Write the unit in the answer",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Step by Step
        self.next_band(6)
        self.write_rows(6, "Step by Step", [
            "First answer is a stepping stone",
            "R18 500 minus R13 595 is R4 905",
            "18 113 litres used",
            "6 887 litres left",
        ], scale=0.9, box=1)

        last = Tex("Understand, write the sentence, calculate, check, and answer in a sentence with units.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
