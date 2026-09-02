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

# BAND LAYOUT: sequential vertical bands, one frame-height each; the camera
# moves down between teaching steps and nothing is ever removed. Only
# exporter-supported mobjects (Tex/MathTex, Line, Rectangle/
# SurroundingRectangle) with write-only reveals — no sub-part transforms.
# The payslip is recreated as a rect + Tex cells; every calculation is built
# line by line in SA currency format.
#
# Mirrors script.md across the seven subtopics of the duo (Part 1 — Expert:
# subtopics 1-4; Part 2 — Simplifier: 5-7); band time proportional to
# subtopics.json.

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k."""
    return DOWN * BAND * k


class IncomeExpenditureBudgetsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the payslip ---
        title = Tex("Income, Expenditure and Personal Budgets").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        slip = Rectangle(width=7.4, height=4.2).shift(DOWN * 0.8)
        slip_t = Tex("PAYSLIP").scale(1.0).shift(UP * 0.9)
        self.play(Create(slip), Write(slip_t))
        self.wait(1.5)
        rule = Line(LEFT * 3.7, RIGHT * 3.7).shift(UP * 0.5)
        self.play(Create(rule))
        rows = [
            ("Gross salary", "R10 500,00", 0.0),
            ("PAYE (tax)", "R840,00", -0.7),
            ("UIF (1\\%)", "R105,00", -1.4),
            ("Pension (5\\%)", "R525,00", -2.1),
        ]
        for name, amt, y in rows:
            c1 = Tex(name).scale(0.9).shift(UP * y + LEFT * 2.1)
            c2 = Tex(amt).scale(0.9).shift(UP * y + RIGHT * 2.2)
            self.play(Write(c1), Write(c2))
            self.wait(1.3)
        chk = MathTex(r"\text{Check: } 0{,}05 \times 10\,500 = 525").scale(1.0).shift(DOWN * 3.3)
        self.play(Write(chk))
        self.wait(3)

        # --- Band 1 (subtopic_1): net income and all the streams ---
        self.next_band(1)
        b1_t = Tex("Net income: what actually arrives").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = MathTex(r"\text{Deductions: } 840 + 105 + 525 = 1\,470").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"\text{Net: } 10\,500 - 1\,470 = 9\,030").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Add rent R1 100 and hair work R1 070:").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = MathTex(r"9\,030 + 1\,100 + 1\,070 = 11\,200").scale(1.05).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        b1_l5 = Tex("Deductions are NOT expenditure; budget on net").scale(0.9).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): fixed expenses ---
        self.next_band(2)
        b2_t = Tex("Fixed expenses: same size every month").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex("Rent R3 400,00; funeral policy R210,00").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("School fees R520,00; phone R229,00").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"3\,400 + 210 + 520 + 229 = 4\,359").scale(1.05).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_l4 = Tex("Contracts and commitments —").scale(1.0).shift(band_shift(2) + DOWN * 1.8)
        b2_l5 = Tex("they cannot be reduced by using less").scale(1.0).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): variable, occasional, total ---
        self.next_band(3)
        b3_t = Tex("Variable and occasional expenses").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex("Groceries 2 750 + electricity 820 + taxi 940").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"+\, 260 + 330 = 5\,100").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("Provisioning: uniforms R350 + December R450").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        b3_l4 = MathTex(r"= 800 \text{ set aside monthly}").scale(1.0).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = MathTex(r"\text{Total: } 4\,359 + 5\,100 + 800 = 10\,259").scale(1.0).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        b3_l6 = Tex("Test: does the amount change with use?").scale(0.95).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): the bottom line ---
        self.next_band(4)
        b4_t = Tex("The budget and its bottom line").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"11\,200 - 10\,259 = 941").scale(1.15).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex("Surplus of R941,00").scale(1.1).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = MathTex(r"\text{Rent: } \frac{3\,400}{11\,200} = 30{,}4\%").scale(1.0).shift(band_shift(4) + DOWN * 1.0)
        b4_l4 = MathTex(r"\text{Groceries: } \frac{2\,750}{11\,200} = 24{,}6\%").scale(1.0).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex("Housing + food: over half of income").scale(1.0).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): stress test and the fix ---
        self.next_band(5)
        b5_t = Tex("Stress test: the hair work stops").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"10\,130 - 10\,259 = -129 \;\; \text{(deficit)}").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex("Fixed can't move — cut variables:").scale(1.0).shift(band_shift(5) + UP * 0.2)
        b5_l3 = Tex("data $-$R80, groceries $-$R100, Dec $-$R50").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = MathTex(r"10\,259 - 230 = 10\,029").scale(1.05).shift(band_shift(5) + DOWN * 1.5)
        b5_l5 = MathTex(r"10\,130 - 10\,029 = 101 \;\; \text{surplus}").scale(1.05).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): break-even for the stall ---
        self.next_band(6)
        b6_t = Tex("Break-even: the koeksister stall").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex("Fixed R720; cost R2,80 each; sells at R6,50").scale(0.95).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"\text{Each contributes: } 6{,}50 - 2{,}80 = 3{,}70").scale(1.0).shift(band_shift(6) + UP * 0.3)
        b6_l3 = MathTex(r"720 \div 3{,}70 = 194{,}59\ldots").scale(1.05).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("At 194: loss of R2,20. At 195: profit R1,50.").scale(0.95).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("Break-even = 195 — always round UP").scale(1.05).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the real month's profit ---
        self.next_band(7)
        b7_t = Tex("The real month: 24 days $\\times$ 15 = 360 sold").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = MathTex(r"\text{Income: } 360 \times 6{,}50 = 2\,340").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"\text{Cost: } 720 + 360 \times 2{,}80 = 1\,728").scale(1.05).shift(band_shift(7) + UP * 0.1)
        b7_l3 = MathTex(r"\text{Profit: } 2\,340 - 1\,728 = 612").scale(1.1).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        b7_l4 = Tex("``Breaks even at 195 and, selling 360,").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        b7_l5 = Tex("makes a profit of R612,00.''").scale(0.95).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): two envelopes on the table ---
        self.next_band(8)
        b8_t = Tex("Money that walks in, money that walks out").scale(1.05).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Two envelopes: IN and OUT — that is a budget").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("Payslip says R10 500 — three pieces carved off:").scale(1.0).shift(band_shift(8) + UP * 0.3)
        b8_l3 = MathTex(r"10\,500 - 1\,470 = 9\,030 \text{ in the bank}").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex("Never write tax on the OUT envelope too").scale(1.0).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("With rent and hair work: R11 200 walked in").scale(1.0).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): three kinds of bills ---
        self.next_band(9)
        b9_t = Tex("Bills that don't care how your month went").scale(1.05).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Don't care: rent, policy, fees — R4 359").scale(1.0).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("Listen to you: groceries, lights — R5 100").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("Ambush bills: pay them in slices — R800").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("Ask: does it change when I change").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        b9_l5 = Tex("what I do? Electricity yes; rent no.").scale(1.0).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the koeksisters that pay for the table ---
        self.next_band(10)
        b10_t = Tex("The koeksisters that pay for the table").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = MathTex(r"11\,200 - 10\,259 = 941 \;\; \text{surplus}").scale(1.0).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = Tex("Roof + food swallow over half the money").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = MathTex(r"\text{Stall: } 720 \div 3{,}70 = 194{,}6 \to 195").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = MathTex(r"360 \text{ sold: } 2\,340 - 1\,728 = 612").scale(1.0).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex("A bottom line needs a decision sentence").scale(1.0).shift(band_shift(10) + DOWN * 2.4)
        self.play(Write(b10_l5))
        self.wait(4)
