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

# Band-layout whiteboard scene for the Loans, Hire Purchase and Insurance
# session duo. Part 1 — Expert: subtopics 1-4 (hire purchase, balloon car
# finance, personal loans, insurance). Part 2 — Simplifier: subtopics 5-7
# retell the fridge, the bubble and the worst-day policies. Durations
# 215/215/225/230/195/195/195 of 1470 s. Exporter-safe mobjects only;
# add-only lifecycle; camera moves down one band per teaching beat.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class LoansHirePurchaseInsuranceSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): hire purchase ---
        title = Tex("Loans, Hire Purchase and Insurance").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"\text{Cash price: R9 499}").scale(1.05).shift(UP * 1.1)
        b0_l2 = MathTex(r"\text{Deposit } 15\%: 1\;424,85").scale(1.0).shift(UP * 0.2)
        b0_l3 = MathTex(r"30 \times 379,90 = 11\;397,00").scale(1.0).shift(DOWN * 0.7)
        b0_l4 = MathTex(r"\text{Total HP: } 12\;821,85").scale(1.05).shift(DOWN * 1.6)
        b0_l5 = MathTex(r"\text{Extra: } 12\;821,85 - 9\;499 = 3\;322,85").scale(1.0).shift(DOWN * 2.6)
        self.play(Write(b0_l1)); self.wait(2)
        self.play(Write(b0_l2)); self.wait(2)
        self.play(Write(b0_l3)); self.wait(2)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2)
        self.play(Write(b0_l5)); self.wait(3)

        # --- Band 1 (subtopic_2): the balloon deal ---
        self.next_band(1)
        b1_title = Tex("Bakkie: R215 000 with a balloon").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\text{Deposit } 10\%: 21\;500").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"72 \times 3\;285 = 236\;520").scale(1.0).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"\text{Balloon } 35\%: 75\;250").scale(1.0).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = MathTex(r"21\;500 + 236\;520 + 75\;250 = 333\;270").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        b1_l5 = MathTex(r"\text{R118 270 above the windscreen price}").scale(1.0).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        self.play(Write(b1_l3)); self.wait(2)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)
        self.play(Write(b1_l5)); self.wait(3)

        # --- Band 2 (subtopic_3): personal loan cost of credit ---
        self.next_band(2)
        b2_title = Tex("R18 000 loan: what credit costs").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Outflow: } 939 + 60 = 999").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"1\;050 + 24 \times 999 = 25\;026").scale(1.0).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"\text{Cost of credit: } 25\;026 - 18\;000 = 7\;026").scale(1.0).shift(band_shift(2) + DOWN * 0.8)
        b2_l4 = MathTex(r"\text{Surplus } 8\;600 - 7\;300 = 1\;300").scale(1.0).shift(band_shift(2) + DOWN * 1.8)
        b2_l5 = Tex("Instalment fits with R301 to spare").scale(1.0).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l1)); self.wait(2)
        self.play(Write(b2_l2)); self.wait(2)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        self.play(Write(b2_l4)); self.wait(2)
        self.play(Write(b2_l5)); self.wait(3)

        # --- Band 3 (subtopic_4): insurance ---
        self.next_band(3)
        b3_title = Tex("Premium, cover, excess").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{Funeral: R95 a month for R25 000}").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"\text{Saving alone: } 25\;000 \div 95 \approx 263 \text{ months}").scale(0.95).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"\text{Vehicle: R920 a month, excess } 5\;200").scale(0.95).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = MathTex(r"\text{Claim: } 31\;400 - 5\;200 = 26\;200").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        b3_l5 = Tex("Financed with a balloon? Insurance required").scale(0.95).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l1)); self.wait(2)
        self.play(Write(b3_l2)); self.wait(2)
        self.play(Write(b3_l3)); self.wait(2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        self.play(Write(b3_l5)); self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 4 (subtopic_5): the fridge that cost a third more ---
        self.next_band(4)
        b4_title = Tex("The fridge that cost a third more").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2.5)
        b4_l1 = MathTex(r"\text{Window: } 9\;499 \quad \text{Signed for: } 12\;821,85").scale(0.95).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"379,90 \times 30 = 11\;397 \;\; +\; 1\;424,85").scale(0.95).shift(band_shift(4) + UP * 0.2)
        b4_l3 = Tex("Store owns it until the last payment").scale(1.0).shift(band_shift(4) + DOWN * 0.8)
        b4_l4 = MathTex(r"\text{Lay-by: } 5 \times 1\;899,80 = 9\;499").scale(1.0).shift(band_shift(4) + DOWN * 1.8)
        b4_l5 = Tex("Total everything, then compare with cash").scale(1.0).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l1)); self.wait(3)
        self.play(Write(b4_l2)); self.wait(3)
        self.play(Write(b4_l3)); self.wait(3)
        self.play(Write(b4_l4)); self.wait(3)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_6): the bubble at the end ---
        self.next_band(5)
        b5_title = Tex("The bubble at the end of the loan").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2.5)
        b5_l1 = Tex("The instalment was built to be looked at").scale(1.0).shift(band_shift(5) + UP * 1.1)
        bubble = Circle(radius=0.9, color=RED).shift(band_shift(5) + UP * 0.0 + RIGHT * 3.4)
        bub_lab = MathTex(r"75\;250").scale(0.8).shift(band_shift(5) + RIGHT * 3.4)
        b5_l2 = MathTex(r"21\;500 + 236\;520 + 75\;250").scale(1.0).shift(band_shift(5) + UP * 0.1 + LEFT * 1.2)
        b5_l3 = MathTex(r"= 333\;270 \text{ for a R215 000 bakkie}").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        b5_l4 = Tex("Pay it, refinance it, or sell to settle it").scale(1.0).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l1)); self.wait(3)
        self.play(Create(bubble), Write(bub_lab)); self.wait(2.5)
        self.play(Write(b5_l2)); self.wait(3)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(3)
        self.play(Write(b5_l4)); self.wait(3.5)

        # --- Band 6 (subtopic_7): paying for the worst day ---
        self.next_band(6)
        b6_title = Tex("Paying for the worst day before it comes").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2.5)
        b6_l1 = MathTex(r"\text{R95 a month buys a R25 000 promise}").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("A tin takes nearly twenty-two years").scale(1.0).shift(band_shift(6) + UP * 0.2)
        b6_l3 = MathTex(r"\text{Crash: } 31\;400 - 5\;200 = 26\;200 \text{ paid}").scale(1.0).shift(band_shift(6) + DOWN * 0.8)
        b6_l4 = Tex("Excess: bring disasters, not scratches").scale(1.0).shift(band_shift(6) + DOWN * 1.8)
        b6_l5 = Tex("Name premium, cover, excess — then weigh").scale(1.0).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l1)); self.wait(3)
        self.play(Write(b6_l2)); self.wait(3)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(3)
        self.play(Write(b6_l4)); self.wait(3)
        self.play(Write(b6_l5)); self.wait(4)
