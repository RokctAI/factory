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

# Band-layout whiteboard scene for budget-growth-and-redressing-inequality (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (300/160/180/180/170/170/160 of 1320 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class BudgetGrowthAndRedressingInequalitySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.78, box=None):
        t = Tex(title).scale(1.1).shift(band_shift(k) + UP * 2.4)
        self.play(Write(t))
        self.wait(1.5)
        made = []
        for i, r in enumerate(rows):
            m = Tex(r).scale(scale).shift(band_shift(k) + UP * (1.3 - 0.95 * i))
            self.play(Write(m))
            self.wait(2.3)
            made.append(m)
        if box is not None:
            self.play(Create(SurroundingRectangle(made[box], color=YELLOW)))
            self.wait(2)
        return made

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1)
        self.write_rows(0, "Economic growth", [
            "Growth: more goods and services over time",
            "GDP: value of final goods and services",
            "GDP per capita = GDP / population",
            "3\\% a year doubles in about 24 years",
        ], box=3)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "How the budget promotes growth", [
            "Infrastructure: roads, rail, ports, power",
            "Human capital: education and health",
            "Fiscal policy and the multiplier effect",
            "Tax incentives; stable debt",
        ], box=2)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Inequality", [
            "Income: a flow; wealth: a stock",
            "Gini: 0 equal, 1 unequal",
            "South Africa: about 0,63",
            "Main driver: unemployment",
        ], box=2)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Redressing inequality", [
            "Revenue: progressive tax, wealth taxes",
            "Spending: grants and the social wage",
            "Causes: education, NSFAS, land reform",
            "NDP 2030 goals",
        ], box=1)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Growth versus redistribution", [
            "Partners: skills, stability, revenue",
            "Rivals: the same limited money",
            "Borrowing adds interest",
            "A job is the most lasting redistribution",
        ], box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "Two learners, one birthday", [
            "Suburb and village: unequal start",
            "Tax more from the top",
            "Spend more at the bottom",
            "Education helps for a lifetime",
        ], box=3)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "Grow the pie, share the pie", [
            "Grow: build, educate, invest",
            "Share: progressive tax, grants",
            "1\\% growth: about 70 years to double",
            "The best slice is a job",
        ], box=3)

        self.wait(4)
