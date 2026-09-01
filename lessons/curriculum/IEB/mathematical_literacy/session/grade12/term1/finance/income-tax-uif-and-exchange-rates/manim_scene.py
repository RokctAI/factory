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

# Band-layout whiteboard scene for the Income Tax, UIF and Exchange Rates
# session duo. Part 1 — Expert: subtopics 1-4 (gross to taxable, tax table
# and rebate, UIF and the payslip, exchange rates against the euro). Part 2 —
# Simplifier: subtopics 5-7 retell the ladder, the rainy-day percent and the
# price tag. Durations 215/215/225/230/195/195/195 of 1470 s. Exporter-safe
# mobjects only; add-only lifecycle; camera moves down one band per beat.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class IncomeTaxUifExchangeRatesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): gross to taxable income ---
        title = Tex("Income Tax, UIF and Exchange Rates").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Gross income: everything before subtraction").scale(1.0).shift(UP * 1.1)
        b0_l2 = MathTex(r"27\;000 \times 12 = \text{R324 000 a year}").scale(1.05).shift(UP * 0.2)
        b0_l3 = Tex("No deductions: taxable income R324 000").scale(1.05).shift(DOWN * 0.7)
        b0_l4 = Tex("The IRP5 records income and tax deducted").scale(1.0).shift(DOWN * 1.7)
        b0_l5 = Tex("Threshold R95 750: below it, no tax at all").scale(1.0).shift(DOWN * 2.6)
        self.play(Write(b0_l1)); self.wait(2)
        self.play(Write(b0_l2)); self.wait(2)
        self.play(Write(b0_l3)); self.wait(2)
        self.play(Write(b0_l4)); self.wait(2)
        self.play(Write(b0_l5)); self.wait(3)

        # --- Band 1 (subtopic_2): the tax table and the rebate ---
        self.next_band(1)
        b1_title = Tex("Band 2: R42 678 + 26\\% of the slice").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"324\;000 - 237\;100 = 86\;900").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"86\;900 \times 0,26 = 22\;594").scale(1.05).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"42\;678 + 22\;594 = 65\;272").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = MathTex(r"65\;272 - 17\;235 = 48\;037 \text{ a year}").scale(1.05).shift(band_shift(1) + DOWN * 1.6)
        b1_l5 = MathTex(r"48\;037 \div 12 = \text{R4 003,08 PAYE}").scale(1.05).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        self.play(Write(b1_l3)); self.wait(2)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)
        self.play(Write(b1_l5)); self.wait(3)

        # --- Band 2 (subtopic_2): the classic error ---
        self.next_band(2)
        b2_title = Tex("The classic error").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"324\;000 \times 0,26 = 84\;240").scale(1.1).shift(band_shift(2) + UP * 0.9)
        self.play(Write(b2_l1)); self.wait(2)
        self.play(Create(strike(b2_l1)))
        self.wait(1.5)
        b2_l2 = Tex("Only the slice above R237 100 pays 26\\%").scale(1.05).shift(band_shift(2) + DOWN * 0.3)
        b2_l3 = Tex("The R42 678 already holds the 18\\% band").scale(1.05).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(b2_l2)); self.wait(2.5)
        self.play(Write(b2_l3)); self.wait(3)

        # --- Band 3 (subtopic_3): UIF and the payslip ---
        self.next_band(3)
        b3_title = Tex("UIF: 1\\% up to the ceiling").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{Ceiling } 17\;712: \; 17\;712 \times 0,01 = 177,12").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"\text{R9 800 earner: } 9\;800 \times 0,01 = 98,00").scale(1.0).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"27\;000 - 4\;003,08 - 177,12").scale(1.05).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = MathTex(r"\text{Net pay} = \text{R22 819,80}").scale(1.1).shift(band_shift(3) + DOWN * 1.7)
        b3_l5 = MathTex(r"\text{Deductions: } 4\;180,20 \div 27\;000 = 15,48\%").scale(0.95).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l1)); self.wait(2)
        self.play(Write(b3_l2)); self.wait(2)
        self.play(Write(b3_l3)); self.wait(2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        self.play(Write(b3_l5)); self.wait(3)

        # --- Band 4 (subtopic_4): exchange rates ---
        self.next_band(4)
        b4_title = Tex("R20,40 per euro: a price tag").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"380 \text{ euros} \to 380 \times 20,40 = \text{R7 752}").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"\text{R6 500} \to 6\;500 \div 20,40 = 318,63 \text{ euros}").scale(1.0).shift(band_shift(4) + UP * 0.2)
        b4_l3 = Tex("Rands grow, euros shrink — check the sizes").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"20,40 \to 21,10: \text{ rand WEAKENED}").scale(1.05).shift(band_shift(4) + DOWN * 1.7)
        b4_l5 = MathTex(r"\text{Camera: } 15\;279,60 \to 15\;803,90").scale(1.0).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l1)); self.wait(2.5)
        self.play(Write(b4_l2)); self.wait(2.5)
        self.play(Write(b4_l3)); self.wait(2)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        self.play(Write(b4_l5)); self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 5 (subtopic_5): the ladder of brackets ---
        self.next_band(5)
        b5_title = Tex("The ladder of tax brackets").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2.5)
        rung1 = Rectangle(width=5.6, height=0.8).shift(band_shift(5) + DOWN * 1.6)
        rung2 = Rectangle(width=5.6, height=0.8).shift(band_shift(5) + DOWN * 0.8 + UP * 0.0 + UP * 0.8)
        self.play(Create(rung1))
        r1_lab = MathTex(r"\text{to } 237\;100: 18\%").scale(0.9).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(r1_lab)); self.wait(2)
        self.play(Create(rung2))
        r2_lab = MathTex(r"\text{slice above: } 26\%").scale(0.9).shift(band_shift(5) + UP * 0.0)
        self.play(Write(r2_lab)); self.wait(2)
        b5_l1 = Tex("Lower rungs are never re-taxed").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"42\;678 + 22\;594 - 17\;235 = 48\;037").scale(1.0).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(3)
        self.play(Write(b5_l2)); self.wait(3)

        # --- Band 6 (subtopic_6): one percent for the rainy day ---
        self.next_band(6)
        b6_title = Tex("One percent for the rainy day").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2.5)
        b6_l1 = Tex("Below the ceiling: a clean 1\\%").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"\text{R9 800} \to \text{R98,00}").scale(1.05).shift(band_shift(6) + UP * 0.2)
        b6_l3 = MathTex(r"\text{Above it, everyone: R177,12}").scale(1.05).shift(band_shift(6) + DOWN * 0.7)
        b6_l4 = MathTex(r"27\;000 - 4\;003,08 - 177,12 = 22\;819,80").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        b6_l5 = Tex("About fifteen rand in a hundred leave first").scale(1.0).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_l1)); self.wait(3)
        self.play(Write(b6_l2)); self.wait(2.5)
        self.play(Write(b6_l3)); self.wait(3)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)
        self.play(Write(b6_l5)); self.wait(3)

        # --- Band 7 (subtopic_7): rands per euro, which way to divide ---
        self.next_band(7)
        b7_title = Tex("Rands per euro: which way to divide").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2.5)
        b7_l1 = Tex("R20,40 per euro = a price tag on one euro").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"\text{Buy 380 euros: } 380 \times 20,40").scale(1.05).shift(band_shift(7) + UP * 0.2)
        b7_l3 = MathTex(r"\text{Spend R6 500: } 6\;500 \div 20,40").scale(1.05).shift(band_shift(7) + DOWN * 0.7)
        b7_l4 = Tex("Rand number bigger, euro number smaller").scale(1.0).shift(band_shift(7) + DOWN * 1.7)
        b7_l5 = Tex("Tag up: rand weak, imports dear").scale(1.05).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l1)); self.wait(3)
        self.play(Write(b7_l2)); self.wait(3)
        self.play(Write(b7_l3)); self.wait(3)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)
        self.play(Write(b7_l5)); self.wait(4)
