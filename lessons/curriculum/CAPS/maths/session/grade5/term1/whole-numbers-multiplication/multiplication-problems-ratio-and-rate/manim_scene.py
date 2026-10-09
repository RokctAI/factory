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
            "Equal groups: multiply",
            "36 bags at R95: 3 600 minus 180",
            "R3 420",
            "24 panels of 175 cm is 4 200 cm",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Ratio: Comparing the Same Kind
        self.next_band(1)
        self.write_rows(1, "Ratio: Comparing the Same Kind", [
            "Ratio: same kind, cement to sand",
            "1 to 3 becomes 12 to 36",
            "Multiply both parts by the same number",
            "2 boys to 3 girls: 14 and 21 in 35",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Rate: Comparing Different Kinds
        self.next_band(2)
        self.write_rows(2, "Rate: Comparing Different Kinds", [
            "Rate: different kinds, rand per kg",
            "R45 per kg times 12 kg is R540",
            "80 km per hour for 3 hours: 240 km",
            "6 for R66 is R11 a can",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``1 to 3 becomes 12 to 14''",
            "``2 to 3 means 2 out of 3 are boys''",
            "``R45 per kg for 12 kg is 540 kg''",
            "``4 for R48 is cheaper: 48 is less''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): How Much Altogether
        self.next_band(4)
        self.write_rows(4, "How Much Altogether", [
            "Each, every, per: multiply",
            "36 times 95",
            "3 600 minus 180 is 3 420",
            "125 books at R148 is R18 500",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Parts of a Mix
        self.next_band(5)
        self.write_rows(5, "Parts of a Mix", [
            "1 cement to 3 sand",
            "Times 12: 12 cement to 36 sand",
            "48 buckets altogether",
            "Multiply both parts",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Per Means For Each
        self.next_band(6)
        self.write_rows(6, "Per Means For Each", [
            "Per means for each",
            "R18 per trip, 26 trips: R468",
            "15 ml per minute: 900 ml an hour",
            "Compare the price of one can",
        ], scale=0.9, box=0)

        last = Tex("Multiply equal groups, scale both parts of a ratio, and read per as for each.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
