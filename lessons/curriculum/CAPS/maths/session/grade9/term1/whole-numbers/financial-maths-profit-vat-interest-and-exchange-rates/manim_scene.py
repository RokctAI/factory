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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex/MathTex keep the export to
# the allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (230/230/210/250/190/190/180 of
# 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FinancialMathsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): profit, loss, discount
        title = Tex("Financial Mathematics").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"\%\text{ profit} = \frac{320 - 250}{250} \times 100 = 28\%").scale(1.05).shift(UP * 1.1)
        l2 = MathTex(r"\%\text{ loss} = \frac{800 - 680}{800} \times 100 = 15\%").scale(1.05).shift(UP * 0.1)
        l3 = MathTex(r"\text{Mark-up } 40\%: 250 \times 1{,}4 = 350").scale(1.05).shift(DOWN * 0.9)
        l4 = MathTex(r"\text{Discount } 20\%: 450 \times 0{,}8 = 360").scale(1.05).shift(DOWN * 1.9)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_1): VAT on and off
        self.next_band(1)
        b1_title = Tex("VAT at 15\\%: on is $\\times 1{,}15$, off is $\\div 1{,}15$").scale(1.1).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"200 \times 1{,}15 = 230 \text{ incl. VAT}").scale(1.1).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"460 \div 1{,}15 = 400 \text{ excl. VAT}, \quad \text{VAT} = 60").scale(1.05).shift(band_shift(1) + UP * 0.2)
        b1_wrong = MathTex(r"460 - 15\% \text{ of } 460 = 391").scale(1.05).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l1))
        self.wait(2.3)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.3)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        b1_note = Tex("The inclusive price is already 115\\%").scale(1.0).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_note))
        self.wait(3)

        # --- Band 2 (subtopic_2): simple interest and hire purchase
        self.next_band(2)
        b2_title = Tex(r"Simple interest: $I = P \times i \times n$").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"5\,000 \times 0{,}08 \times 3 = 1\,200 \;\Rightarrow\; A = 6\,200").scale(1.05).shift(band_shift(2) + UP * 1.3)
        b2_l2 = Tex(r"TV R6 000: deposit $10\% = 600$, balance $5\,400$").scale(1.0).shift(band_shift(2) + UP * 0.4)
        b2_l3 = MathTex(r"5\,400 \times 0{,}12 \times 2 = 1\,296 \;\Rightarrow\; 6\,696 \text{ owed}").scale(1.0).shift(band_shift(2) + DOWN * 0.5)
        b2_l4 = MathTex(r"6\,696 \div 24 = 279 \text{ per month}").scale(1.05).shift(band_shift(2) + DOWN * 1.4)
        b2_l5 = MathTex(r"\text{Total } 600 + 6\,696 = 7\,296 \;(1\,296 \text{ more than cash})").scale(1.0).shift(band_shift(2) + DOWN * 2.3)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4, b2_l5):
            self.play(Write(m))
            self.wait(2.2)
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_3): compound interest
        self.next_band(3)
        b3_title = Tex(r"Compound interest: $A = P(1 + i)^n$").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"5\,000 \to 5\,400 \to 5\,832 \to 6\,298{,}56").scale(1.1).shift(band_shift(3) + UP * 1.3)
        b3_l2 = MathTex(r"A = 5\,000 \times 1{,}08^3 = 5\,000 \times 1{,}259712 = 6\,298{,}56").scale(1.0).shift(band_shift(3) + UP * 0.3)
        b3_l3 = MathTex(r"\text{Interest} = 6\,298{,}56 - 5\,000 = 1\,298{,}56").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = Tex(r"Simple R6 200 vs compound R6 298,56: R98,56 more").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): exchange rates and commission
        self.next_band(4)
        b4_title = Tex("Exchange rates and commission").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\$1 = \text{R}18{,}50: \quad \$200 \times 18{,}50 = \text{R}3\,700").scale(1.05).shift(band_shift(4) + UP * 1.2)
        b4_l2 = MathTex(r"\text{R}5\,550 \div 18{,}50 = \$300").scale(1.05).shift(band_shift(4) + UP * 0.3)
        b4_l3 = Tex("Towards rands: multiply. Towards dollars: divide.").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = MathTex(r"\text{Commission } 5\% \times 48\,000 = 2\,400; \; 4\,000 + 2\,400 = 6\,400").scale(1.0).shift(band_shift(4) + DOWN * 1.6)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(2)

        # --- Band 5 (subtopic_4): budget and account
        self.next_band(5)
        b5_title = Tex("A budget and an account statement").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Income R6 400").scale(1.05).shift(band_shift(5) + UP * 1.3)
        b5_l2 = MathTex(r"\text{Expenses } 2\,500 + 1\,800 + 900 + 300 = 5\,500").scale(1.0).shift(band_shift(5) + UP * 0.4)
        b5_l3 = MathTex(r"\text{Surplus } 6\,400 - 5\,500 = 900").scale(1.05).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = MathTex(r"\text{Closing} = 1\,250 + 860 - 1\,000 = 1\,110").scale(1.05).shift(band_shift(5) + DOWN * 1.5)
        b5_l5 = Tex("opening + charges $-$ payments = closing").scale(1.0).shift(band_shift(5) + DOWN * 2.4)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4, b5_l5):
            self.play(Write(m))
            self.wait(2.2)
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): the spaza counter
        self.next_band(6)
        b6_title = Tex("Buying low, selling high at the spaza").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"Paid R250, sold R320: R70 up $= \tfrac{70}{250} \times 100 = 28\%$").scale(1.0).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex(r"Paid R800, sold R680: R120 down $= 15\%$ loss").scale(1.0).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex(r"20\% off R450: keep 80\%, $450 \times 0{,}8 = 360$").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex(r"VAT on: $200 \times 1{,}15 = 230$ \quad VAT off: $460 \div 1{,}15 = 400$").scale(1.0).shift(band_shift(6) + DOWN * 1.5)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        b6_l5 = Tex("Compare with what you PAID").scale(1.05).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_6): rent on money
        self.next_band(7)
        b7_title = Tex("Interest: rent you pay on money").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"Simple: R400, R400, R400 $\to$ R6 200").scale(1.05).shift(band_shift(7) + UP * 1.3)
        b7_l2 = Tex(r"Compound: R400, R432, R466,56 $\to$ R6 298,56").scale(1.05).shift(band_shift(7) + UP * 0.4)
        b7_l3 = Tex("Rent on the same pile vs rent on the growing pile").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex(r"TV on terms: $600 + 5\,400 + 1\,296 = 7\,296$, i.e. R279 $\times$ 24").scale(0.95).shift(band_shift(7) + DOWN * 1.5)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2)

        # --- Band 8 (subtopic_7): rands to dollars and a budget
        self.next_band(8)
        b8_title = Tex("Rands to dollars, and a budget").scale(1.15).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"\$200 $\to$ R: $200 \times 18{,}50 = 3\,700$ (bigger number)").scale(1.0).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex(r"R5 550 $\to$ \$: $5\,550 \div 18{,}50 = 300$ (smaller number)").scale(1.0).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex(r"Basic R4 000 + 5\% of R48 000 = R6 400").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        b8_l4 = Tex(r"In R6 400, out R5 500 $\to$ R900 left to save").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        b8_l5 = Tex(r"Owed 1 250 + 860 $-$ 1 000 paid = R1 110").scale(1.0).shift(band_shift(8) + DOWN * 2.3)
        for m in (b8_l1, b8_l2, b8_l3, b8_l4, b8_l5):
            self.play(Write(m))
            self.wait(2.2)
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(4)
