# Copyright (c) 2026 RokctAI
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
# session duo. Part 1 — Expert: subtopics 1-4 (hire purchase, car finance
# with a balloon, personal loans, insurance). Part 2 — Simplifier: subtopics
# 5-7 reopen the same contracts on the kitchen table. Durations 215/215/225/
# 230/195/195/195 of 1470 s. Exporter-safe mobjects only; add-only
# lifecycle; camera moves down one band per teaching beat.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class LoansHirePurchaseInsuranceSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the hire purchase deal ---
        title = Tex("Loans, Hire Purchase and Insurance").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"\text{Cash price: R11 999}").scale(1.05).shift(UP * 1.1)
        b0_l2 = MathTex(r"\text{Deposit } 10\%: \; 0,10 \times 11\;999 = \text{R1 199,90}").scale(1.0).shift(UP * 0.2)
        b0_l3 = MathTex(r"589,50 \times 24 = \text{R14 148,00}").scale(1.05).shift(DOWN * 0.7)
        b0_l4 = MathTex(r"1\;199,90 + 14\;148 = \text{R15 347,90}").scale(1.05).shift(DOWN * 1.7)
        self.play(Write(b0_l1)); self.wait(2)
        self.play(Write(b0_l2)); self.wait(2)
        self.play(Write(b0_l3)); self.wait(2)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        b0_note = Tex("Until the last instalment, it's the store's couch").scale(0.95).shift(DOWN * 2.8)
        self.play(Write(b0_note))
        self.wait(3)

        # --- Band 1 (subtopic_1): the extra, and lay-by ---
        self.next_band(1)
        b1_title = Tex("The price of paying later").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"15\;347,90 - 11\;999 = \text{R3 348,90}").scale(1.1).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("Nearly 28\\% more than the cash price").scale(1.05).shift(band_shift(1) + UP * 0.2)
        b1_l3 = Tex("Lay-by: R11 999 exactly, no interest").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = Tex("But the couch waits in the storeroom").scale(1.05).shift(band_shift(1) + DOWN * 1.6)
        b1_l5 = Tex("HP sells time; lay-by sells patience").scale(1.05).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l1))
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        self.play(Write(b1_l3)); self.wait(2)
        self.play(Write(b1_l4)); self.wait(2)
        self.play(Write(b1_l5)); self.wait(3)

        # --- Band 2 (subtopic_2): the balloon deal's three pieces ---
        self.next_band(2)
        b2_title = Tex("Car finance: three separate lines").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Price: R189 900}").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"\text{Deposit } 10\% = \text{R18 990}").scale(1.05).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"60 \times 3\;499 = \text{R209 940}").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = MathTex(r"\text{Balloon } 30\% = \text{R56 970, due month 60}").scale(1.0).shift(band_shift(2) + DOWN * 1.7)
        b2_l5 = Tex("The balloon makes the monthly look light").scale(1.0).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l1)); self.wait(2)
        self.play(Write(b2_l2)); self.wait(2)
        self.play(Write(b2_l3)); self.wait(2)
        self.play(Write(b2_l4)); self.wait(2.5)
        self.play(Write(b2_l5)); self.wait(3)

        # --- Band 3 (subtopic_2): totalling the deal honestly ---
        self.next_band(3)
        b3_title = Tex("Total the deal honestly").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"18\;990 + 209\;940 + 56\;970 = \text{R285 900}").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"285\;900 - 189\;900 = \text{R96 000 extra}").scale(1.05).shift(band_shift(3) + UP * 0.1)
        b3_l3 = Tex("Month 60: pay it, refinance it, or sell").scale(1.05).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l1))
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2.5)
        self.play(Write(b3_l2)); self.wait(2.5)
        self.play(Write(b3_l3)); self.wait(3)

        # --- Band 4 (subtopic_3): the total cost of credit ---
        self.next_band(4)
        b4_title = Tex("The personal loan: R25 000 over 36 months").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{Outflow: } 1\;095 + 69 = \text{R1 164 a month}").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"1\;207,50 + 36 \times 1\;164 = \text{R43 111,50}").scale(1.05).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"43\;111,50 - 25\;000 = \text{R18 111,50}").scale(1.05).shift(band_shift(4) + DOWN * 0.8)
        b4_l4 = Tex("The borrowing itself cost over 72\\%").scale(1.05).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l1)); self.wait(2.5)
        self.play(Write(b4_l2)); self.wait(2.5)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        self.play(Write(b4_l4)); self.wait(3)

        # --- Band 5 (subtopic_3): the affordability check ---
        self.next_band(5)
        b5_title = Tex("Affordability: income minus expenses").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"9\;800 - 8\;400 = \text{R1 400 surplus}").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"\text{Instalment R1 164 fits} \dots \text{just}").scale(1.05).shift(band_shift(5) + UP * 0.2)
        b5_l3 = MathTex(r"1\;400 - 1\;164 = \text{R236 breathing room}").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
        b5_l4 = Tex("One taxi-fare crisis from a missed payment").scale(1.0).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l1)); self.wait(2.5)
        self.play(Write(b5_l2)); self.wait(2)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        self.play(Write(b5_l4)); self.wait(3)

        # --- Band 6 (subtopic_4): funeral cover ---
        self.next_band(6)
        b6_title = Tex("Insurance: premium, cover, excess").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Funeral: R120 a month for R30 000 cover}").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"120 \times 12 = \text{R1 440 a year}").scale(1.05).shift(band_shift(6) + UP * 0.2)
        b6_l3 = MathTex(r"30\;000 \div 120 = 250 \text{ months to save}").scale(1.05).shift(band_shift(6) + DOWN * 0.8)
        b6_l4 = Tex("Yet full cover pays even at month three").scale(1.05).shift(band_shift(6) + DOWN * 1.8)
        b6_l5 = Tex("The many who don't claim carry the few who must").scale(0.95).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l1)); self.wait(2)
        self.play(Write(b6_l2)); self.wait(2)
        self.play(Write(b6_l3)); self.wait(2.5)
        self.play(Write(b6_l4)); self.wait(2)
        self.play(Write(b6_l5)); self.wait(3)

        # --- Band 7 (subtopic_4): the excess at claim time ---
        self.next_band(7)
        b7_title = Tex("The excess: your share of the claim").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"\text{Car cover: R850 a month, excess R4 500}").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"\text{Damage: R28 600}").scale(1.05).shift(band_shift(7) + UP * 0.2)
        b7_l3 = MathTex(r"28\;600 - 4\;500 = \text{R24 100 paid out}").scale(1.05).shift(band_shift(7) + DOWN * 0.8)
        b7_l4 = Tex("Excess keeps small claims out, premiums down").scale(1.0).shift(band_shift(7) + DOWN * 1.8)
        b7_l5 = Tex("A balloon-financed car MUST be insured").scale(1.0).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l1)); self.wait(2.5)
        self.play(Write(b7_l2)); self.wait(2)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        self.play(Write(b7_l4)); self.wait(2)
        self.play(Write(b7_l5)); self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the lounge suite that cost a third more ---
        self.next_band(8)
        b8_title = Tex("The lounge suite that cost a third more").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2.5)
        b8_l1 = Tex("Each R589,50 feels small — that's the design").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = MathTex(r"589,50 \times 24 + 1\;199,90 = \text{R15 347,90}").scale(1.05).shift(band_shift(8) + UP * 0.2)
        b8_l3 = MathTex(r"\text{The gap: R3 348,90 — price of impatience}").scale(1.0).shift(band_shift(8) + DOWN * 0.8)
        b8_l4 = Tex("Lay-by: R11 999 total, but wait six months").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l1)); self.wait(3)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(3)
        self.play(Write(b8_l3)); self.wait(3)
        self.play(Write(b8_l4)); self.wait(3.5)

        # --- Band 9 (subtopic_6): the bubble at the end ---
        self.next_band(9)
        b9_title = Tex("The bubble at the end of the car loan").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = Tex("R3 499 a month was built to be looked at").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"18\;990 + 209\;940 + 56\;970 = \text{R285 900}").scale(1.05).shift(band_shift(9) + UP * 0.2)
        b9_l3 = MathTex(r"\text{R96 000 more than the windscreen price}").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        b9_l4 = Tex("Judge a deal by its total, never its monthly").scale(1.05).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l1)); self.wait(3)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(3)
        self.play(Write(b9_l3)); self.wait(3)
        self.play(Write(b9_l4)); self.wait(3.5)

        # --- Band 10 (subtopic_7): paying for the worst day ---
        self.next_band(10)
        b10_title = Tex("Paying for the worst day before it comes").scale(1.05).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2.5)
        b10_l1 = Tex("A tin needs 250 months; the policy pays now").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("You buy certainty, not a payout").scale(1.05).shift(band_shift(10) + UP * 0.2)
        b10_l3 = MathTex(r"\text{Crash: insurer } 24\;100, \text{ you } 4\;500").scale(1.05).shift(band_shift(10) + DOWN * 0.8)
        b10_l4 = Tex("Bring the disasters, not the scratches").scale(1.05).shift(band_shift(10) + DOWN * 1.8)
        b10_l5 = Tex("Name premium, cover and excess — always").scale(1.05).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l1)); self.wait(3)
        self.play(Write(b10_l2)); self.wait(3)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(3)
        self.play(Write(b10_l4)); self.wait(3)
        self.play(Write(b10_l5)); self.wait(4)
