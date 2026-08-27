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

# Band layout: one frame-height band per teaching beat; the camera moves down,
# nothing is removed. Exporter-supported mobjects only (Tex/MathTex/Line/
# Rectangle/SurroundingRectangle); single-string Write reveals throughout.
#
# Covers all seven subtopics (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7),
# band time roughly proportional to subtopics.json
# (215/220/225/230/195/195/195 of 1475 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class VatUifTariffsExchangeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): adding VAT ---
        title = Tex("VAT, UIF, Tariffs and Exchange Rates").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l1 = Tex(r"VAT $= 15\%$ added to most goods and services").scale(1.05).shift(UP * 1.1)
        self.play(Write(l1)); self.wait(2)
        l2 = MathTex(r"\text{VAT: } 240 \times 0{,}15 = R36").scale(1.1).shift(UP * 0.2)
        l3 = MathTex(r"\text{Shelf price: } 240 \times 1{,}15 = R276").scale(1.1).shift(DOWN * 0.7)
        self.play(Write(l2)); self.wait(2)
        self.play(Write(l3))
        self.play(Create(SurroundingRectangle(l3, color=GREEN)))
        self.wait(2.5)
        l4 = Tex("Excluding $=$ before tax; including $=$ what you pay").scale(1.0).shift(DOWN * 1.8)
        self.play(Write(l4)); self.wait(2.5)

        # --- Band 1 (subtopic_1): removing VAT, zero-rated basket ---
        self.next_band(1)
        b1_title = Tex("Removing VAT is where marks die").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_wrong = MathTex(r"276 \times 0{,}85 = R234{,}60 \quad \text{(wrong by } R5{,}40)").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2.5)
        b1_l1 = Tex(r"R276 is 115\% of the original — divide by 1,15").scale(1.0).shift(band_shift(1) + UP * 0.1)
        b1_l2 = MathTex(r"276 \div 1{,}15 = R240").scale(1.15).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l1)); self.wait(2.5)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("Zero-rated: brown bread, maize meal, rice, milk, eggs").scale(0.95).shift(band_shift(1) + DOWN * 1.9)
        b1_l4 = Tex("Tax the taxable lines; leave the zero-rated alone").scale(0.95).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l3)); self.wait(2)
        self.play(Write(b1_l4)); self.wait(2.5)

        # --- Band 2 (subtopic_2): UIF, one percent from each side ---
        self.next_band(2)
        b2_title = Tex(r"UIF: 1\% taken twice").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Worker: } 8\,400 \times 0{,}01 = R84").scale(1.1).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"\text{Employer adds another } R84").scale(1.05).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"\text{Fund receives } 84 + 84 = R168").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l1)); self.wait(2.5)
        self.play(Write(b2_l2)); self.wait(2)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex("Only R84 comes off Sipho's pay — read what is asked").scale(0.95).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l4)); self.wait(2.5)

        # --- Band 3 (subtopic_2): the payslip, gross to net ---
        self.next_band(3)
        b3_title = Tex("The payslip: gross to net").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        slip = Rectangle(width=8.6, height=3.4).shift(band_shift(3) + UP * 0.2)
        self.play(Create(slip))
        b3_r1 = Tex(r"Gross pay \hfill R8\,400").scale(1.0).shift(band_shift(3) + UP * 1.3)
        b3_r2 = Tex(r"UIF (1\% of gross) \quad $-$R84").scale(1.0).shift(band_shift(3) + UP * 0.5)
        b3_r3 = Tex(r"Other deductions \quad $-$R516").scale(1.0).shift(band_shift(3) + DOWN * 0.3)
        b3_r4 = MathTex(r"\text{Net: } 8\,400 - 84 - 516 = R7\,800").scale(1.0).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_r1)); self.wait(2)
        self.play(Write(b3_r2)); self.wait(2)
        self.play(Write(b3_r3)); self.wait(2)
        self.play(Write(b3_r4))
        self.play(Create(SurroundingRectangle(b3_r4, color=GREEN)))
        self.wait(2.5)
        b3_l1 = Tex("UIF is worked on GROSS, before other deductions").scale(0.95).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3_l1)); self.wait(2.5)

        # --- Band 4 (subtopic_3): exchange rates, both directions ---
        self.next_band(4)
        b4_title = Tex(r"Exchange rate: one dollar costs R18,50").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{Buy } \$120: \; 120 \times 18{,}50 = R2\,220").scale(1.05).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"R5\,000 \text{ buys } 5\,000 \div 18{,}50 = \$270{,}27").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l1)); self.wait(2.5)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex("Toward rands: multiply. Toward the foreign unit: divide.").scale(0.95).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3)); self.wait(2.5)
        b4_l4 = Tex(r"R18,50 $\to$ R19,20 per dollar: the rand WEAKENED").scale(0.95).shift(band_shift(4) + DOWN * 1.8)
        b4_l5 = MathTex(r"\pounds 400: \; 400 \times 23{,}40 = R9\,360; \;\; \text{at } 24{,}10 = R9\,640").scale(0.87).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l4)); self.wait(2)
        self.play(Write(b4_l5)); self.wait(2.5)

        # --- Band 5 (subtopic_4): two phone deals, tested ---
        self.next_band(5)
        b5_title = Tex(r"Option A: R99 $+$ R0,75/min. \; B: R1,45/min.").scale(1.0).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"A = 99 + 0{,}75 \times m; \qquad B = 1{,}45 \times m").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1)); self.wait(2.5)
        b5_l2 = MathTex(r"100\text{ min: } A = R174, \; B = R145 \;\; (B \text{ wins})").scale(1.0).shift(band_shift(5) + UP * 0.2)
        b5_l3 = MathTex(r"200\text{ min: } A = R249, \; B = R290 \;\; (A \text{ wins})").scale(1.0).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l2)); self.wait(2.5)
        self.play(Write(b5_l3)); self.wait(2.5)

        # --- Band 6 (subtopic_4): the crossing point ---
        self.next_band(6)
        b6_title = Tex("Where the options trade places").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"99 + 0{,}75 \times m = 1{,}45 \times m").scale(1.1).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"99 = 0{,}70 \times m").scale(1.1).shift(band_shift(6) + UP * 0.2)
        b6_l3 = MathTex(r"m = 141{,}43 \text{ minutes}").scale(1.1).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l1)); self.wait(2.5)
        self.play(Write(b6_l2)); self.wait(2)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = Tex("Below 141 min: take B. Above: take A.").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        b6_l5 = Tex("Answer as advice in words — who chooses what, and why").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_l4)); self.wait(2.5)
        self.play(Write(b6_l5)); self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the passenger in the price ---
        self.next_band(7)
        b7_title = Tex("Fifteen percent riding inside the price").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2.5)
        b7_l1 = MathTex(r"\text{No tax yet? } 240 \times 1{,}15 = R276").scale(1.05).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1)); self.wait(3)
        b7_l2 = MathTex(r"\text{Tax inside? } 276 \div 1{,}15 = R240").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(3)
        b7_l3 = Tex(r"Taking 15\% off gives R234,60 — feels right, loses all").scale(0.95).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3)); self.wait(3)
        b7_l4 = Tex("The protected basket rides free: bread, maize, milk, eggs").scale(0.9).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l4)); self.wait(3.5)

        # --- Band 8 (subtopic_6): the two R84s ---
        self.next_band(8)
        b8_title = Tex("The two R84s on the payslip").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2.5)
        b8_l1 = Tex(r"One percent: slide the comma — R8\,400 $\to$ R84").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1)); self.wait(3)
        b8_l2 = Tex(r"Sipho contributes R84; the fund receives R168").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(3)
        b8_l3 = MathTex(r"8\,400 - 84 - 516 = R7\,800 \text{ net}").scale(1.05).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3)); self.wait(3)
        b8_l4 = Tex("Gross minus deductions equals net — always").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l4)); self.wait(3.5)

        # --- Band 9 (subtopic_7): rands abroad, and the phone shop ---
        self.next_band(9)
        b9_title = Tex("A dollar is an item priced at R18,50").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = MathTex(r"120 \text{ of them: } 120 \times 18{,}50 = R2\,220").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l2 = MathTex(r"R5\,000 \text{ buys: } 5\,000 \div 18{,}50 \approx \$270").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1)); self.wait(3)
        self.play(Write(b9_l2)); self.wait(3)
        b9_l3 = Tex(r"Weaker rand: petrol hurts, but London's £400 grows").scale(0.95).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3)); self.wait(3)
        b9_l4 = Tex(r"Phone deals: rent $+$ cheap minutes vs no rent, dear minutes").scale(0.9).shift(band_shift(9) + DOWN * 1.7)
        b9_l5 = Tex(r"``At 100 minutes, choose B and save R29''").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l4)); self.wait(3)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(4)
