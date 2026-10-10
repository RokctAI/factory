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

# Band-layout whiteboard scene for ratio-and-rate-problems (Part 1 Expert
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


class RatioAndRateProblemsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Ratio
        self.write_rows(0, "Ratio", [
            "1 cup to 4 cups: ratio 1 : 4",
            "Order matters: water to concentrate is 4 : 1",
            "2 : 8 is the same as 1 : 4",
            "12 : 18 simplifies to 2 : 3",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Rate
        self.next_band(1)
        self.write_rows(1, "Rate", [
            "R18 for 6 rolls: R3 per roll",
            "240 km in 3 hours: 80 km per hour",
            "48 rolls in 20 minutes: 144 per hour",
            "A rate needs units and per",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Solving Ratio and Rate Problems
        self.next_band(2)
        self.write_rows(2, "Solving Ratio and Rate Problems", [
            "35 rolls in 3 : 4: 7 parts of 5",
            "Shares: 15 and 20",
            "R3 per roll against R2,50 per roll",
            "50 g per roll: 1 750 g for 35 rolls",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Concentrate to water as 4 : 1''",
            "``35 rolls shared equally in 3 : 4''",
            "``The bigger pack is always cheaper''",
            "``Speed as 240 times 3''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Same Kind
        self.next_band(4)
        self.write_rows(4, "Same Kind", [
            "Same kind",
            "Ratio with a colon",
            "No units",
            "Order matters",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Different Kinds
        self.next_band(5)
        self.write_rows(5, "Different Kinds", [
            "Different kinds",
            "Rate with per",
            "R3 per roll",
            "80 km per hour",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Best Buy
        self.next_band(6)
        self.write_rows(6, "Best Buy", [
            "Best buy",
            "Add the parts",
            "Find one part",
            "Compare the price for one",
        ], scale=0.9, box=3)

        last = Tex("Ratio compares the same kind, rate compares different kinds with per, and the price for one finds the better buy.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
