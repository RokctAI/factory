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

# Band-layout whiteboard scene for percentages-and-fraction-percentage-equivalence (Part 1 Expert
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


class PercentagesAndFractionPercentageEquivalenceSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What a Percentage Is
        self.write_rows(0, "What a Percentage Is", [
            "Percent: out of 100",
            "25 percent = 25/100 = 1/4",
            "50 percent = 1/2",
            "The whole is 100 percent",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Changing Between Fractions and Percentages
        self.next_band(1)
        self.write_rows(1, "Changing Between Fractions and Percentages", [
            "Fraction to percent: make the bottom 100",
            "17/20 = 85/100 = 85 percent",
            "Percent to fraction: over 100, simplify",
            "40 percent = 40/100 = 2/5",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Finding Percentages of Whole Numbers
        self.next_band(2)
        self.write_rows(2, "Finding Percentages of Whole Numbers", [
            "10 percent: divide by 10",
            "10 percent of R350 = R35",
            "15 percent of R360 = R36 + R18 = R54",
            "VAT on R200 = R30",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``17 out of 20 is 17 percent''",
            "``40 percent = 4/10 and stop''",
            "``10 percent of 350 = 3,5''",
            "``15 percent of R360 = R36 + R15''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Out of a Hundred
        self.next_band(4)
        self.write_rows(4, "Out of a Hundred", [
            "Out of a hundred",
            "25 percent is a quarter",
            "50 percent is a half",
            "100 percent is the whole",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Same Amount, Two Names
        self.next_band(5)
        self.write_rows(5, "Same Amount, Two Names", [
            "Same amount, two names",
            "17/20 is 85 percent",
            "40 percent is 2/5",
            "Make the bottom 100",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Ten Percent First
        self.next_band(6)
        self.write_rows(6, "Ten Percent First", [
            "Ten percent first",
            "Divide by 10",
            "Half of it is 5 percent",
            "Add for 15 percent",
        ], scale=0.9, box=1)

        last = Tex("Percent means out of a hundred: make the bottom 100 to get a percentage, and find 10 percent first to work out percentages of amounts.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
