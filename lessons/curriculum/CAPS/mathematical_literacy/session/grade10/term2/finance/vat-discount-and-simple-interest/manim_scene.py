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
# exporter-supported mobjects (Tex/MathTex, Line, SurroundingRectangle) with
# write-only reveals — no sub-part transforms. The till-slip basket is built
# as text rows; all money in SA format (decimal comma).
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


class VatDiscountSimpleInterestSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): VAT forwards ---
        title = Tex("VAT, Discount and Simple Interest").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("VAT: 15\\%. Shelf prices are INCLUSIVE.").scale(1.05).shift(UP * 1.2)
        self.play(Write(l01))
        self.wait(2)
        l02 = Tex("Forwards: cooler box R690,00 excl.").scale(1.0).shift(UP * 0.3)
        l03 = MathTex(r"690 \times 0{,}15 = 103{,}50").scale(1.05).shift(DOWN * 0.6)
        l04 = MathTex(r"690 \times 1{,}15 = 793{,}50").scale(1.05).shift(DOWN * 1.6)
        self.play(Write(l02))
        self.wait(1.5)
        self.play(Write(l03))
        self.wait(2)
        self.play(Write(l04))
        self.play(Create(SurroundingRectangle(l04, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): VAT backwards ---
        self.next_band(1)
        b1_t = Tex("Backwards: R1 288,00 including VAT").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("Subtracting 15\\% is WRONG —").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex("the 15\\% was worked on the smaller price").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = MathTex(r"1\,288 \div 1{,}15 = 1\,120").scale(1.1).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        b1_l4 = MathTex(r"\text{VAT: } 1\,288 - 1\,120 = 168").scale(1.05).shift(band_shift(1) + DOWN * 1.6)
        b1_l5 = MathTex(r"\text{Check: } 1\,120 \times 0{,}15 = 168").scale(1.0).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l4))
        self.wait(2)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_1): the basket and the zero-rated list ---
        self.next_band(2)
        b2_t = Tex("The basket: separate zero-rated first").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex("Zero-rated: maize meal, milk, bread = R202,00").scale(0.95).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex("Standard: powder, cooldrink, chips = R172,50").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"172{,}50 \div 1{,}15 = 150 \;\Rightarrow\; \text{VAT} = 22{,}50").scale(1.0).shift(band_shift(2) + DOWN * 0.5)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex("Total R374,50, of which R22,50 is VAT").scale(1.0).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = MathTex(r"0{,}15 \times 374{,}50 = 56{,}18").scale(1.0).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l5))
        self.play(Create(strike(b2_l5)))
        self.wait(3)

        # --- Band 3 (subtopic_2): discount, and discounts that chain ---
        self.next_band(3)
        b3_t = Tex("Discount: 30\\% off a R640,00 tracksuit").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"640 \times 0{,}70 = 448").scale(1.05).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2)
        b3_l2 = Tex("20\\% off then a further 10\\% is NOT 30\\%:").scale(0.95).shift(band_shift(3) + UP * 0.3)
        b3_l3 = MathTex(r"640 \times 0{,}80 = 512; \quad 512 \times 0{,}90 = 460{,}80").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"0{,}80 \times 0{,}90 = 0{,}72 \;\Rightarrow\; 28\% \text{ off}").scale(1.0).shift(band_shift(3) + DOWN * 1.4)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("Reverse: 460,80 $\\div$ 0,72 = R640,00").scale(0.95).shift(band_shift(3) + DOWN * 2.3)
        b3_l6 = Tex("``Buy 2 get 1 free'' = 33,3\\% off, not 50\\%").scale(0.95).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(b3_l5))
        self.wait(2)
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): simple interest forwards ---
        self.next_band(4)
        b4_t = Tex("Simple interest: growth in a straight line").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"I = P \times r \times t \;\; (t \text{ in YEARS})").scale(1.05).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"I = 4\,500 \times 0{,}075 \times 3").scale(1.05).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"= 337{,}50 \times 3 = 1\,012{,}50").scale(1.05).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"\text{Closing balance: } 4\,500 + 1\,012{,}50 = 5\,512{,}50").scale(0.95).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = MathTex(r"8 \text{ months} = \tfrac{8}{12} = 0{,}667 \text{ yr}; \;\; 6 \text{ mo} = 0{,}5").scale(0.9).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): simple interest backwards ---
        self.next_band(5)
        b5_t = Tex("Backwards: find the rate").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("R4 500,00 grows to R5 062,50 in 2 years").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = MathTex(r"I = 5\,062{,}50 - 4\,500 = 562{,}50").scale(1.0).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"562{,}50 = 4\,500 \times r \times 2 = 9\,000\,r").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        b5_l4 = MathTex(r"r = 562{,}50 \div 9\,000 = 0{,}0625").scale(1.0).shift(band_shift(5) + DOWN * 1.5)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("Rate = 6,25\\% per year — say the unit").scale(1.05).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the fridge decision ---
        self.next_band(6)
        b6_t = Tex("The fridge decision: buy now or wait?").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Sale: } 7\,200 \times 0{,}85 = 6\,120 \;\; (\text{save } 1\,080)").scale(0.95).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"\text{Waiting: } 6\,500 \times 0{,}06 \times 0{,}5 = 195").scale(1.0).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Wait: savings R6 695 vs fridge R7 200").scale(1.0).shift(band_shift(6) + DOWN * 0.6)
        b6_l4 = Tex("— R505 short of buying at all").scale(1.0).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = MathTex(r"195 - 1\,080 = -885: \text{ buy now}").scale(1.05).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the habits that earn marks ---
        self.next_band(7)
        b7_t = Tex("Habits that convert working into marks").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        habits = [
            "Write the formula, then substitute",
            "Divide to undo VAT or a discount",
            "Months $\\div$ 12 before anything else",
            "Round once, at the end, to cents",
            "Close with a sentence that answers",
        ]
        for i, h in enumerate(habits):
            m = Tex(h).scale(1.0).shift(band_shift(7) + UP * (1.2 - 0.85 * i))
            self.play(Write(m))
            self.wait(1.7)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the till slip at the corner shop ---
        self.next_band(8)
        b8_t = Tex("The tax is already in the price").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Like squash: concentrate already stirred in —").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("you cannot take 15\\% of the full glass").scale(0.95).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"172{,}50 \div 1{,}15 = 150; \;\; \text{tax} = 22{,}50").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("Maize meal, milk, bread: no tax at all").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Basket R374,50 — only R22,50 is tax").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): the sale sign that says more ---
        self.next_band(9)
        b9_t = Tex("The sale sign that says more than it gives").scale(1.0).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("30\\% off R640: keep 70\\%").scale(1.05).shift(band_shift(9) + UP * 1.2)
        b9_l2 = MathTex(r"640 \times 0{,}70 = 448").scale(1.05).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("20\\% then 10\\%: R512, then R460,80").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("R12,80 more than ``30\\% off'' feels").scale(1.0).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex("The second percentage eats what the first left").scale(0.95).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): same growth every year, and the fridge ---
        self.next_band(10)
        b10_t = Tex("Money that grows the same every year").scale(1.05).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = MathTex(r"4\,500 \times 0{,}075 = 337{,}50 \text{ each year}").scale(1.0).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = Tex("Three years: R1 012,50 — ends R5 512,50").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("Six months is 0,5 — never 6").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex("Fridge: save R1 080 now vs earn R195 waiting").scale(0.95).shift(band_shift(10) + DOWN * 1.5)
        b10_l5 = Tex("Buy now — ahead by R885,00").scale(1.05).shift(band_shift(10) + DOWN * 2.4)
        self.play(Write(b10_l4))
        self.wait(2)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(4)
