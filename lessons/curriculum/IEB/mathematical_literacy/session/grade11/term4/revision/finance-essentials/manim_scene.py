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

# Band-layout whiteboard scene for the Finance Essentials revision session duo.
# Part 1 — Expert: subtopics 1-4 (documents & deductions, VAT both gears,
# tariffs & exchange rates, profit/break-even/interest/inflation). Part 2 —
# Simplifier: subtopics 5-7 retell the same maths from the stand and kitchen
# table. Durations 235/235/245/250/190/190/195 of 1540 s — simplifier bands
# carry longer waits. Exporter-safe mobjects only; add-only lifecycle.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FinanceEssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(15)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): Naledi's payslip, gross to net ---
        title = Tex("Finance Essentials").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        slip = Rectangle(width=7.6, height=4.4).shift(DOWN * 0.7)
        self.play(Create(slip))
        p_l1 = MathTex(r"\text{Gross salary: R11 200}").scale(1.05).shift(UP * 0.9)
        p_l2 = MathTex(r"\text{UIF } 1\%: \; 0,01 \times 11\;200 = \text{R}112").scale(1.0).shift(UP * 0.1)
        p_l3 = MathTex(r"\text{Pension } 7,5\%: \; 0,075 \times 11\;200 = \text{R}840").scale(1.0).shift(DOWN * 0.7)
        p_l4 = MathTex(r"\text{Income tax: R1 498}").scale(1.0).shift(DOWN * 1.5)
        p_l5 = MathTex(r"\text{Net: } 11\;200 - 112 - 840 - 1\;498 = \text{R8 750}").scale(0.95).shift(DOWN * 2.4)
        self.play(Write(p_l1)); self.wait(2)
        self.play(Write(p_l2)); self.wait(2)
        self.play(Write(p_l3)); self.wait(2)
        self.play(Write(p_l4)); self.wait(2)
        self.play(Write(p_l5))
        self.play(Create(SurroundingRectangle(p_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): sorting vocabulary and document habits ---
        self.next_band(1)
        b1_title = Tex("Gross $-$ deductions $=$ net").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = Tex("Fixed income: salary; variable: overtime").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("Fixed expense: rent; variable: electricity").scale(1.05).shift(band_shift(1) + UP * 0.2)
        b1_l3 = Tex("Sort into columns, total, compare").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = Tex("Opening balance: still owed from last month").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        b1_l5 = Tex("Label what each number IS before using it").scale(1.0).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        self.play(Write(b1_l3)); self.wait(2)
        self.play(Write(b1_l4)); self.wait(2)
        self.play(Write(b1_l5)); self.wait(3)

        # --- Band 2 (subtopic_2): VAT in both gears ---
        self.next_band(2)
        b2_title = Tex("VAT at 15\\%: forward and reverse").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"0,15 \times 1\;240 = 186 \;\Rightarrow\; \text{R1 426}").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"\text{One move: } 1\;240 \times 1,15 = 1\;426").scale(1.05).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1)); self.wait(2)
        self.play(Write(b2_l2)); self.wait(2)
        b2_wrong = MathTex(r"1\;426 - 15\% \text{ of } 1\;426").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2)
        b2_l3 = MathTex(r"1\;426 \div 1,15 = \text{R1 240}").scale(1.1).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        b2_note = Tex("The tag is 115\\% — division is the only way back").scale(0.95).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_note))
        self.wait(3)

        # --- Band 3 (subtopic_2): mixed trolleys and payslip percentages ---
        self.next_band(3)
        b3_title = Tex("Sort the trolley, then the percentages").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Zero-rated: brown bread, maize meal, rice").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("VAT only on the standard-rated subtotal").scale(1.05).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"1\% \text{ of } 11\;200 = 112 \;\text{(slide the decimal)}").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = MathTex(r"5\% \text{ raise: } \times 1,05 \text{, then rerun lines}").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        b3_l5 = Tex("`Including' warns: reverse gear — divide").scale(1.0).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l1)); self.wait(2)
        self.play(Write(b3_l2)); self.wait(2.5)
        self.play(Write(b3_l3)); self.wait(2)
        self.play(Write(b3_l4)); self.wait(2.5)
        self.play(Write(b3_l5)); self.wait(3)

        # --- Band 4 (subtopic_3): the stepped tariff ladder ---
        self.next_band(4)
        b4_title = Tex("Stepped tariff: walk the ladder").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("First 150 units R1,95; after that R2,85").scale(1.05).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"150 \times 1,95 = \text{R}292,50").scale(1.05).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"260 - 150 = 110 \text{ units left}").scale(1.05).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"110 \times 2,85 = \text{R}313,50").scale(1.05).shift(band_shift(4) + DOWN * 1.6)
        b4_l5 = MathTex(r"292,50 + 313,50 = \text{R}606").scale(1.1).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l1)); self.wait(2)
        self.play(Write(b4_l2)); self.wait(2)
        self.play(Write(b4_l3)); self.wait(2)
        self.play(Write(b4_l4)); self.wait(2)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): exchange rates, both directions ---
        self.next_band(5)
        b5_title = Tex("Exchange rate: R20,25 per euro").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"80 \times 20,25 = \text{R1 620}").scale(1.1).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"1\;215 \div 20,25 = 60 \text{ euros}").scale(1.1).shift(band_shift(5) + UP * 0.2)
        b5_l3 = Tex("Multiply into rand; divide back to euros").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
        b5_l4 = MathTex(r"20,25 \to 19,60: \text{ the rand STRENGTHENED}").scale(1.0).shift(band_shift(5) + DOWN * 1.8)
        b5_l5 = Tex("Each euro costs fewer rand — imports cheaper").scale(1.0).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l1)); self.wait(2)
        self.play(Write(b5_l2)); self.wait(2)
        self.play(Write(b5_l3)); self.wait(2.5)
        self.play(Write(b5_l4)); self.wait(2)
        self.play(Write(b5_l5)); self.wait(3)

        # --- Band 6 (subtopic_4): Sipho's break-even ---
        self.next_band(6)
        b6_title = Tex("Break-even at the boerewors stand").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Contribution: } 31 - 16 = \text{R}15").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"1\;800 \div 15 = 120 \text{ rolls}").scale(1.1).shift(band_shift(6) + UP * 0.2)
        b6_l3 = MathTex(r"\text{Check: } 120 \times 31 = 3\;720").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        b6_l4 = MathTex(r"1\;800 + 120 \times 16 = 3\;720").scale(1.0).shift(band_shift(6) + DOWN * 1.6)
        b6_l5 = Tex("Above 120 profit; below 120 loss").scale(1.05).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_l1)); self.wait(2)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2)
        self.play(Write(b6_l3)); self.wait(2)
        self.play(Write(b6_l4)); self.wait(2)
        self.play(Write(b6_l5)); self.wait(3)

        # --- Band 7 (subtopic_4): interest twice, inflation once ---
        self.next_band(7)
        b7_title = Tex("R8 000 at 10\\% for 3 years").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"\text{Simple: } 3 \times 800 = 2\;400 \to \text{R10 400}").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"\text{Compound: } 8\;800 \to 9\;680 \to 10\;648").scale(1.0).shift(band_shift(7) + UP * 0.2)
        b7_l3 = MathTex(r"\text{Gap: } 10\;648 - 10\;400 = \text{R}248").scale(1.05).shift(band_shift(7) + DOWN * 0.8)
        b7_l4 = MathTex(r"\text{Inflation } 5\%: \; 320 \times 1,05 = \text{R}336").scale(1.0).shift(band_shift(7) + DOWN * 1.8)
        b7_l5 = Tex("Prices compound; money buys less").scale(1.05).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l1)); self.wait(2.5)
        self.play(Write(b7_l2)); self.wait(2.5)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        self.play(Write(b7_l4)); self.wait(2)
        self.play(Write(b7_l5)); self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the payslip as a story ---
        self.next_band(8)
        b8_title = Tex("The payslip is a story of subtraction").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2.5)
        b8_l1 = Tex("UIF R112: insurance. Pension R840: future you").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("Tax R1 498: schools, roads, clinics").scale(1.05).shift(band_shift(8) + UP * 0.2)
        b8_l3 = MathTex(r"11\;200 \text{ in}, \; 2\;450 \text{ named}, \; 8\;750 \text{ out}").scale(1.0).shift(band_shift(8) + DOWN * 0.8)
        b8_l4 = Tex("Askables: calculate, explain, recalculate").scale(1.05).shift(band_shift(8) + DOWN * 1.8)
        b8_l5 = Tex("Raise? Change the gross FIRST, then rerun").scale(1.0).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l1)); self.wait(3)
        self.play(Write(b8_l2)); self.wait(3)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(3)
        self.play(Write(b8_l4)); self.wait(3)
        self.play(Write(b8_l5)); self.wait(3)

        # --- Band 9 (subtopic_6): the hole and the shovel ---
        self.next_band(9)
        b9_title = Tex("The stall that teaches break-even").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = Tex("The hole: R1 800 rent, sales or not").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"\text{The shovel: } 31 - 16 = \text{R}15 \text{ a sale}").scale(1.05).shift(band_shift(9) + UP * 0.2)
        b9_l3 = MathTex(r"1\;800 \div 15 = 120 \text{: hole filled}").scale(1.05).shift(band_shift(9) + DOWN * 0.8)
        b9_l4 = MathTex(r"\text{R19 costs? shovel R12} \to 150 \text{ sales}").scale(1.0).shift(band_shift(9) + DOWN * 1.8)
        b9_l5 = Tex("Price R34? shovel R18, 100 — but will they buy?").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l1)); self.wait(3)
        self.play(Write(b9_l2)); self.wait(3)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(3)
        self.play(Write(b9_l4)); self.wait(3)
        self.play(Write(b9_l5)); self.wait(3)

        # --- Band 10 (subtopic_7): slow money ---
        self.next_band(10)
        b10_title = Tex("Slow money: the long game").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2.5)
        b10_l1 = Tex("Simple: R800 a year, a raise-less salary").scale(1.05).shift(band_shift(10) + UP * 1.1)
        b10_l2 = MathTex(r"\text{Compound: } 8\;800,\; 9\;680,\; 10\;648").scale(1.05).shift(band_shift(10) + UP * 0.2)
        b10_l3 = Tex("A snowball — and the hill is time").scale(1.05).shift(band_shift(10) + DOWN * 0.7)
        b10_l4 = MathTex(r"\text{Jersey: } 320 \times 1,05 = 336 \text{, then again}").scale(1.0).shift(band_shift(10) + DOWN * 1.7)
        b10_l5 = Tex("Build the table; end with the comparison").scale(1.05).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10_l1)); self.wait(3)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(3)
        self.play(Write(b10_l3)); self.wait(3)
        self.play(Write(b10_l4)); self.wait(3)
        self.play(Write(b10_l5)); self.wait(4)
