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
        # --- Band 0 (subtopic_1): Money and Measurement Problems
        self.write_rows(0, "Money and Measurement Problems", [
            "24 boxes at R35: 24 times 35",
            "Grid: 600, 100, 120, 20 gives 840",
            "8 rolls of 75 cm is 600 cm",
            "14 cars at R15 is R210",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Ratio: Comparing the Same Kind
        self.next_band(1)
        self.write_rows(1, "Ratio: Comparing the Same Kind", [
            "Ratio compares the same kind",
            "2 cups to 3 vetkoek",
            "Multiply both parts by the same number",
            "10 cups for 15 vetkoek",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Rate: Comparing Different Kinds
        self.next_band(2)
        self.write_rows(2, "Rate: Comparing Different Kinds", [
            "Rate compares different kinds",
            "60 kilometres per hour",
            "3 hours: 3 times 60 is 180 km",
            "Per means for each one",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Each means add''",
            "``2 to 3 scales to 10 to 3''",
            "``3 to 2 means 3 out of 2''",
            "``Drop the units from a rate''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Equal Groups of Money and Measure
        self.next_band(4)
        self.write_rows(4, "Equal Groups of Money and Measure", [
            "Each box R35, 24 boxes: multiply",
            "24 times 35 is 840",
            "8 times 75 is 600 cm",
            "Does it fit the story?",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Two of the Same Kind
        self.next_band(5)
        self.write_rows(5, "Two of the Same Kind", [
            "Same kind: ratio",
            "2 to 3",
            "Times both by 5: 10 to 15",
            "Order matters",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Per Means For Each One
        self.next_band(6)
        self.write_rows(6, "Per Means For Each One", [
            "Different kinds: rate",
            "60 km per hour",
            "3 hours: 180 km",
            "Can you say per? Rate",
        ], scale=0.9, box=3)

        last = Tex("Each means multiply, a ratio scales both parts together, and a rate is an amount per one.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
