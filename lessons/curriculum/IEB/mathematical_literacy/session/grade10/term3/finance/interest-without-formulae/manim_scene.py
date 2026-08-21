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

# Band-layout whiteboard scene for the Interest Without Formulae session duo.
# One band per teaching beat, camera moves down between bands, add-only
# lifecycle. Exporter-supported mobjects only; every working line is a
# single-string Tex/MathTex revealed with Write. Band time apportioned to
# subtopics.json (200/230/230/260/180/190/190 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class InterestWithoutFormulaeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): a percentage is not money ---
        title = Tex("Interest Without Formulae").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Rate: a percentage per time period — a speed").scale(1.05).shift(UP * 1.1)
        b0_l2 = Tex("Interest: the actual rand amount produced").scale(1.05).shift(UP * 0.2)
        self.play(Write(b0_l1))
        self.wait(2.5)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = MathTex(r"6\% \text{ of R4 000} = 0{,}06 \times 4\;000 = \text{R}240").scale(1.1).shift(DOWN * 0.8)
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_rule = Tex("Rate acts on PRINCIPAL to produce interest").scale(1.0).shift(DOWN * 1.9)
        self.play(Write(b0_rule))
        self.play(Create(SurroundingRectangle(b0_rule, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): direction of the flow ---
        self.next_band(1)
        b1_t = Tex("Who pays whom?").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("Saver: the bank uses YOUR money — bank pays you").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("Borrower: you use the BANK'S money — you pay").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Units: rate wears \\%, interest wears R").scale(1.05).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): year one of the saving ---
        self.next_band(2)
        b2_t = Tex("Growing R4 000 at 6\\% per year").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Year 1: } 6\% \text{ of } 4\;000 = \text{R}240").scale(1.1).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"4\;000 + 240 = \text{R}4\;240").scale(1.1).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("Mental path: 10\\% is 400, 1\\% is 40, 6\\% is 240").scale(0.95).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l3))
        self.wait(3)

        # --- Band 3 (subtopic_2): year two grows from the NEW balance ---
        self.next_band(3)
        b3_t = Tex("Year two: the balance moved").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_wrong = MathTex(r"6\% \text{ of } 4\;000 \text{ again} = \text{R}240").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_l1 = MathTex(r"\text{Year 2: } 6\% \text{ of } 4\;240 = \text{R}254{,}40").scale(1.05).shift(band_shift(3) + UP * 0.1)
        b3_l2 = MathTex(r"4\;240 + 254{,}40 = \text{R}4\;494{,}40").scale(1.05).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = Tex("R14,40 more — interest earning interest").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l3))
        self.wait(3)

        # --- Band 4 (subtopic_3): the bank loan ---
        self.next_band(4)
        b4_t = Tex("Borrowing R4 000 at 15\\% per year").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{Interest: } 0{,}15 \times 4\;000 = \text{R}600").scale(1.1).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"\text{Repay: } 4\;000 + 600 = \text{R}4\;600").scale(1.1).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the mashonisa ---
        self.next_band(5)
        b5_t = Tex("The mashonisa: 25\\% PER MONTH").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"25\% \text{ of } 4\;000 = \text{R}1\;000 \text{ each month}").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex("Three months: R3 000 paid, R4 000 still owed").scale(1.0).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"25\% \times 12 = 300\% \text{ per year vs } 15\%").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_ans = Tex("Twenty times more expensive").scale(1.05).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_ans))
        self.play(Create(SurroundingRectangle(b5_ans, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): finding the rate backwards ---
        self.next_band(6)
        b6_t = Tex("Backwards: find the rate").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex("R480 interest on a R4 000 loan, one year").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"\frac{480}{4\;000} \times 100 = 12\% \text{ per year}").scale(1.05).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_wrong = MathTex(r"\frac{480}{4\;480} \times 100 \approx 10{,}7\%").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_wrong))
        self.play(Create(strike(b6_wrong)))
        self.wait(2)
        b6_l3 = Tex("Divide by the PRINCIPAL, never the repayment").scale(1.0).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_l3))
        self.wait(3)

        # --- Band 7 (subtopic_4): the five-step method ---
        self.next_band(7)
        b7_t = Tex("Method for any interest question").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex("1. Principal, rate, and the rate's time period").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("2. Direction: earned by saver or paid by borrower?").scale(1.0).shift(band_shift(7) + UP * 0.2)
        b7_l3 = Tex("3. One period's interest = \\% of current balance").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        b7_l4 = Tex("4. Multiple periods: one at a time, track the balance").scale(1.0).shift(band_shift(7) + DOWN * 1.6)
        b7_l5 = Tex("5. Answer what was asked — interest, balance, or rate").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(2)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l1, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): renting money ---
        self.next_band(8)
        b8_t = Tex("Interest is rent for money").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Borrow R4 000: pay R600 rent, return R4 600").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("Save R4 000: the bank rents YOURS — pays R240").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Rate = the price on the to-let sign (\\%)").scale(1.0).shift(band_shift(8) + DOWN * 0.8)
        b8_l4 = Tex("Interest = the rent money that changes hands (R)").scale(1.0).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the snowball ---
        self.next_band(9)
        b9_t = Tex("The snowball in the savings account").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = MathTex(r"\text{Year 1: } 4\;000 \to 4\;240").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"\text{Year 2: } 6\% \text{ of } 4\;240 = 254{,}40 \to 4\;494{,}40").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Withdraw yearly: R480. Leave it in: R494,40").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_ans = Tex("Measure the ball as it is NOW").scale(1.05).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_ans))
        self.play(Create(SurroundingRectangle(b9_ans, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): which loan hurts less ---
        self.next_band(10)
        b10_t = Tex("Which loan hurts less?").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Bank: 15\\% PER YEAR — R600 for twelve months").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("Mashonisa: 25\\% PER MONTH — R1 000 every month").scale(1.0).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"25 \times 12 = 300\% \text{ per year} \gg 15\%").scale(1.05).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_ans = Tex("Same time period first, then compare").scale(1.05).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_ans))
        self.play(Create(SurroundingRectangle(b10_ans, color=GREEN)))
        b10_l4 = Tex("Interest-only payments never shrink the debt").scale(0.95).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10_l4))
        self.wait(4)
