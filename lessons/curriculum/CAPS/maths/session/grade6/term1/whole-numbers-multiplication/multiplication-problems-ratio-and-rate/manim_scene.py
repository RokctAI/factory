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

# Band-layout whiteboard scene for multiplication-problems-ratio-and-rate (Part 1 Expert
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


class MultiplicationProblemsRatioAndRateSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Multiplication in Money and Measurement Problems
        self.write_rows(0, "Multiplication in Money and Measurement Problems", [
            "Equal groups: multiply",
            "145 tablets at R1 250",
            "= R181 250",
            "36 rolls of 125 m = 4 500 m",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Ratio: Comparing Quantities of the Same Kind
        self.next_band(1)
        self.write_rows(1, "Ratio: Comparing Quantities of the Same Kind", [
            "Ratio: for every",
            "Cement to sand 1 : 3",
            "15 bags of cement: 45 bags of sand",
            "Multiply both parts",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Rate: Comparing Different Kinds of Quantities
        self.next_band(2)
        self.write_rows(2, "Rate: Comparing Different Kinds of Quantities", [
            "Rate: per",
            "80 km per hour for 3 hours = 240 km",
            "R185 per hour for 8 hours = R1 480",
            "Total: multiply. Rate: divide.",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``6 cups of concentrate: 10 cups of water''",
            "``15 bags of cement: 5 bags of sand''",
            "``Speed is 80''",
            "``Multiplying to find a rate''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Groups of Equal Amounts
        self.next_band(4)
        self.write_rows(4, "Groups of Equal Amounts", [
            "Equal groups",
            "Multiply",
            "R181 250",
            "4 500 m of wire",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): For Every
        self.next_band(5)
        self.write_rows(5, "For Every", [
            "For every",
            "1 cup to 4 cups",
            "6 cups to 24 cups",
            "Same taste, more drink",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Per
        self.next_band(6)
        self.write_rows(6, "Per", [
            "Per means for each",
            "80 km per hour",
            "240 km in 3 hours",
            "R185 per hour",
        ], scale=0.9, box=0)

        last = Tex("Multiply equal groups, scale a ratio by multiplying both parts, and use per for a rate: multiply for a total, divide for the rate.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
