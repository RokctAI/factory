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
# The payslip is recreated as a rect + Tex cells, per the maths_literacy
# metarules; every calculation is built line by line in SA currency format.
#
# Mirrors script.md across the seven subtopics of the duo (Part 1 — Expert:
# subtopics 1-4; Part 2 — Simplifier: 5-7); band time proportional to
# subtopics.json.

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k."""
    return DOWN * BAND * k


def strike(m):
    """Diagonal cancellation stroke through a wrong line, teacher-style."""
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


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
            ("Gross salary", "R9 500,00", 0.0),
            ("PAYE (tax)", "R760,00", -0.7),
            ("UIF (1\\%)", "R95,00", -1.4),
            ("Pension (5\\%)", "R475,00", -2.1),
        ]
        for name, amt, y in rows:
            c1 = Tex(name).scale(0.9).shift(UP * y + LEFT * 2.1)
            c2 = Tex(amt).scale(0.9).shift(UP * y + RIGHT * 2.2)
            self.play(Write(c1), Write(c2))
            self.wait(1.3)
        chk = MathTex(r"\text{Check: } 0{,}05 \times 9\,500 = 475").scale(1.0).shift(DOWN * 3.3)
        self.play(Write(chk))
        self.wait(3)

        # --- Band 1 (subtopic_1): net income and all the streams ---
        self.next_band(1)
        b1_t = Tex("Net income: what actually arrives").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = MathTex(r"\text{Deductions: } 760 + 95 + 475 = 1\,330").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"\text{Net: } 9\,500 - 1\,330 = 8\,170").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Add rent R900 and sewing R1 130:").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = MathTex(r"8\,170 + 900 + 1\,130 = 10\,200").scale(1.05).shift(band_shift(1) + DOWN * 1.7)
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
        b2_l1 = Tex("Rent R3 000,00; funeral policy R180,00").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("School fees R450,00; phone R199,00").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"3\,000 + 180 + 450 + 199 = 3\,829").scale(1.05).shift(band_shift(2) + DOWN * 0.8)
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
        b3_l1 = Tex("Groceries 2 600 + electricity 750 + taxi 880").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"+\, 240 + 320 = 4\,790").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("Provisioning: uniforms R400 + December R500").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        b3_l4 = MathTex(r"= 900 \text{ set aside monthly}").scale(1.0).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = MathTex(r"\text{Total: } 3\,829 + 4\,790 + 900 = 9\,519").scale(1.0).shift(band_shift(3) + DOWN * 2.2)
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
        b4_l1 = MathTex(r"10\,200 - 9\,519 = 681").scale(1.15).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex("Surplus of R681,00").scale(1.1).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = MathTex(r"\text{Rent: } \frac{3\,000}{10\,200} = 29{,}4\%").scale(1.0).shift(band_shift(4) + DOWN * 1.0)
        b4_l4 = MathTex(r"\text{Groceries: } \frac{2\,600}{10\,200} = 25{,}5\%").scale(1.0).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex("Housing + food: over half of income").scale(1.0).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): stress test and the fix ---
        self.next_band(5)
        b5_t = Tex("Stress test: the sewing dries up").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"9\,070 - 9\,519 = -449 \;\; \text{(deficit)}").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex("Fixed can't move — cut variables:").scale(1.0).shift(band_shift(5) + UP * 0.2)
        b5_l3 = Tex("data $-$R120, groceries $-$R200, Dec $-$R150").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = MathTex(r"9\,519 - 470 = 9\,049").scale(1.05).shift(band_shift(5) + DOWN * 1.5)
        b5_l5 = MathTex(r"9\,070 - 9\,049 = 21 \;\; \text{surplus}").scale(1.05).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): break-even for the stall ---
        self.next_band(6)
        b6_t = Tex("Break-even: the vetkoek stall").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex("Fixed R600; cost R3,50 each; sells at R8,00").scale(0.95).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"\text{Each contributes: } 8 - 3{,}50 = 4{,}50").scale(1.0).shift(band_shift(6) + UP * 0.3)
        b6_l3 = MathTex(r"600 \div 4{,}50 = 133{,}33\ldots").scale(1.05).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("At 133: loss of R1,50. At 134: profit R3,00.").scale(0.95).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("Break-even = 134 — always round UP").scale(1.05).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the real month's profit ---
        self.next_band(7)
        b7_t = Tex("The real month: 26 days $\\times$ 12 = 312 sold").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = MathTex(r"\text{Income: } 312 \times 8 = 2\,496").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"\text{Cost: } 600 + 312 \times 3{,}50 = 1\,692").scale(1.05).shift(band_shift(7) + UP * 0.1)
        b7_l3 = MathTex(r"\text{Profit: } 2\,496 - 1\,692 = 804").scale(1.1).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        b7_l4 = Tex("``Breaks even at 134 and, selling 312,").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        b7_l5 = Tex("makes a profit of R804,00.''").scale(0.95).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): two bowls on the table ---
        self.next_band(8)
        b8_t = Tex("Money that walks in, money that walks out").scale(1.05).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Two bowls: IN and OUT — that is a budget").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("Payslip says R9 500 — three bites first:").scale(1.0).shift(band_shift(8) + UP * 0.3)
        b8_l3 = MathTex(r"9\,500 - 1\,330 = 8\,170 \text{ in the bank}").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex("Never write tax in the out-bowl too").scale(1.0).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("With rent and sewing: R10 200 walked in").scale(1.0).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): three kinds of bills ---
        self.next_band(9)
        b9_t = Tex("Bills that don't care how your month went").scale(1.05).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Don't care: rent, policy, fees — R3 829").scale(1.0).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("Listen to you: groceries, lights — R4 790").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("Sneaky ones: pay them in slices — R900").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("Ask: does it change when I change").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        b9_l5 = Tex("what I do? Electricity yes; rent no.").scale(1.0).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the vetkoek that pays for the table ---
        self.next_band(10)
        b10_t = Tex("The vetkoek that pays for the table").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = MathTex(r"10\,200 - 9\,519 = 681 \;\; \text{surplus}").scale(1.0).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = Tex("Roof + food swallow over half the money").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = MathTex(r"\text{Stall: } 600 \div 4{,}50 = 133{,}3 \to 134").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = MathTex(r"312 \text{ sold: } 2\,496 - 1\,692 = 804").scale(1.0).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex("A bottom line needs a decision sentence").scale(1.0).shift(band_shift(10) + DOWN * 2.4)
        self.play(Write(b10_l5))
        self.wait(4)
