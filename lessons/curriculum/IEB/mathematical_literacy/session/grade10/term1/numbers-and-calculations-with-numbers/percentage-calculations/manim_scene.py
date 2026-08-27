# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from manim import *

# BAND LAYOUT: sequential vertical bands, one frame-height each; the camera
# moves down between teaching steps and nothing is ever removed. Only
# exporter-supported mobjects (Tex/MathTex, Line, Rectangle via
# SurroundingRectangle) with write-only reveals — no sub-part transforms.
#
# Mirrors script.md across the seven subtopics of the duo (Part 1 — Expert:
# subtopics 1-4; Part 2 — Simplifier: 5-7); band time proportional to
# subtopics.json. Every calculation of the sneaker chain (R800, -15%, +15%
# VAT) is built line by line with SA currency formatting.

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k."""
    return DOWN * BAND * k


def strike(m):
    """Diagonal cancellation stroke through a wrong line, teacher-style."""
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PercentageCalculationsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): percentage as a decimal ---
        title = Tex("Percentage Calculations").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = MathTex(r"15\% = \frac{15}{100} = 0{,}15").scale(1.2).shift(UP * 1.0)
        self.play(Write(l01))
        self.wait(2.5)
        l02 = Tex("15\\% of R800:").scale(1.1).shift(DOWN * 0.1)
        l03 = MathTex(r"0{,}15 \times 800 = 120").scale(1.15).shift(DOWN * 1.0)
        self.play(Write(l02))
        self.play(Write(l03))
        self.wait(2.5)
        l04 = Tex("The discount is R120,00").scale(1.1).shift(DOWN * 2.0)
        self.play(Write(l04))
        self.play(Create(SurroundingRectangle(l04, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the single multiplier ---
        self.next_band(1)
        b1_t = Tex("The multiplier method").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = MathTex(r"\text{15\% decrease: } \times \, 0{,}85 \;\; (100 - 15)").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"\text{15\% increase: } \times \, 1{,}15 \;\; (100 + 15)").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = MathTex(r"\text{Long way: } 800 - 120 = 680").scale(1.05).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = MathTex(r"\text{One step: } 800 \times 0{,}85 = 680").scale(1.05).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        b1_l5 = Tex("Same answer, half the steps").scale(1.0).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): the sneaker chain, worked in full ---
        self.next_band(2)
        b2_t = Tex("Discount, then VAT — each on the result").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Step 1: } 800 \times 0{,}85 = 680").scale(1.1).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"\text{Step 2 (VAT on } 680\text{):}").scale(1.05).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"680 \times 1{,}15 = 782").scale(1.1).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex("This chain lands exactly on the cent:").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        b2_l5 = Tex("Final price = R782,00").scale(1.15).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the classic cancel trap ---
        self.next_band(3)
        b3_t = Tex("The classic error").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex("``$-$R120 then $+$R120, so R800''").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.play(Create(strike(b3_l1)))
        self.wait(2.5)
        b3_l2 = Tex("The discount acted on R800,").scale(1.05).shift(band_shift(3) + UP * 0.1)
        b3_l3 = Tex("but VAT acted on the smaller R680").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("Same rate, different base =").scale(1.05).shift(band_shift(3) + DOWN * 1.7)
        b3_l5 = Tex("different amounts of money").scale(1.05).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): multiply the multipliers ---
        self.next_band(4)
        b4_t = Tex("One multiplier for the whole journey").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"0{,}85 \times 1{,}15 = 0{,}9775").scale(1.15).shift(band_shift(4) + UP * 1.0)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex("Final price is 97,75\\% of the original").scale(1.05).shift(band_shift(4) + UP * 0.0)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"100 - 97{,}75 = 2{,}25").scale(1.1).shift(band_shift(4) + DOWN * 1.0)
        b4_l4 = Tex("A 2,25\\% decrease overall").scale(1.1).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        b4_l5 = Tex("$-15\\%$ then $+15\\%$ is NOT zero").scale(1.0).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): confirm with the direct formula ---
        self.next_band(5)
        b5_t = Tex("Percentage change: the direct formula").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"\%\text{ change} = \frac{\text{change}}{\text{ORIGINAL}} \times 100").scale(0.97).shift(band_shift(5) + UP * 1.0)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"800 - 782 = 18").scale(1.05).shift(band_shift(5) + UP * 0.0)
        b5_l3 = MathTex(r"\frac{18}{800} = 0{,}0225").scale(1.1).shift(band_shift(5) + DOWN * 1.1)
        b5_l4 = MathTex(r"0{,}0225 \times 100 = 2{,}25\% \text{ decrease}").scale(1.05).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        b5_l5 = Tex("The original always sits in the denominator").scale(0.95).shift(band_shift(5) + DOWN * 3.1)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): reverse percentages ---
        self.next_band(6)
        b6_t = Tex("Reverse: R782 including 15\\% VAT").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"782 \times 0{,}85 = 664{,}70").scale(1.05).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.play(Create(strike(b6_l1)))
        b6_l2 = Tex("VAT was charged on the BEFORE-VAT price").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"\text{final} = \text{before-VAT} \times 1{,}15").scale(1.05).shift(band_shift(6) + DOWN * 0.7)
        b6_l4 = MathTex(r"782 \div 1{,}15 = 680").scale(1.1).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        b6_l5 = Tex("To undo a multiplier, divide by it").scale(1.05).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): the five-move toolkit ---
        self.next_band(7)
        b7_t = Tex("The five moves").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        moves = [
            "1. \\% of amount: decimal $\\times$ amount",
            "2. Up/down: one multiplier, $1 \\pm$ decimal",
            "3. Chained: multiply the multipliers",
            "4. \\% change: difference $\\div$ original $\\times$ 100",
            "5. Reverse: divide by the multiplier",
        ]
        for i, mv in enumerate(moves):
            m = Tex(mv).scale(1.0).shift(band_shift(7) + UP * (1.2 - 0.85 * i))
            self.play(Write(m))
            self.wait(1.8)
        b7_chk = Tex("Whole loop checks: 800 $\\to$ 680 $\\to$ 782").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_chk))
        self.play(Create(SurroundingRectangle(b7_chk, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the one-button way ---
        self.next_band(8)
        b8_t = Tex("Taking off and putting on — one button").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Slab of 100 blocks; 15 come off,").scale(1.05).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("85 stay: keep 85\\%").scale(1.05).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = MathTex(r"800 \times 0{,}85 = 680").scale(1.1).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = MathTex(r"\text{Airtime bonus: } 150 \times 1{,}20 = 180").scale(1.05).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Down: under 1. Up: over 1. The multiplier.").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): two fifteens that refuse to cancel ---
        self.next_band(9)
        b9_t = Tex("Two fifteens that refuse to cancel").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Discount: 15\\% of R800 = R120 off").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("VAT: 15\\% of R680 = only R102 on").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"680 + 102 = 782").scale(1.05).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = MathTex(r"0{,}85 \times 1{,}15 = 0{,}9775 \;\Rightarrow\; 2{,}25\% \text{ down}").scale(0.95).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("Same fraction of a smaller parcel is less").scale(1.0).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): winding the till backwards ---
        self.next_band(10)
        b10_t = Tex("Winding the till backwards").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Slip says R782 including VAT").scale(1.05).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = MathTex(r"782 \times 0{,}85 = 664{,}70").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.play(Create(strike(b10_l2)))
        self.wait(2)
        b10_l3 = MathTex(r"782 \div 1{,}15 = 680").scale(1.1).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2)
        b10_l4 = Tex("Multiply in, divide out — same gate").scale(1.05).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("Check: R680 + R102 VAT = R782,00").scale(1.0).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10_l5))
        self.wait(4)
