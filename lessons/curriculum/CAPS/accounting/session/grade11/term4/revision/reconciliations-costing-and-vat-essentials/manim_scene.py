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

# Band-layout whiteboard scene for "Reconciliations, Costing and VAT
# Essentials" (grade 11, term 4, revision). One band per teaching beat;
# the camera moves down and nothing is removed. Part 1 (Expert) =
# subtopics 1-4, Part 2 (Simplifier) = subtopics 5-7 in fresh bands.
# Exporter-safe primitives only; write-only reveals. Subtopic durations
# 220/220/230/230/190/200/200 of 1490 s guide the apportioning.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ToolkitRevisionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): update your own books first ---
        title = Tex("Reconciliations, Costing and VAT").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Bank rec, step 1: update YOUR books").scale(1.05).shift(UP * 1.3)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("Ledger bank account \\quad R10 940").scale(1.05).shift(UP * 0.5)
        b0_l3 = Tex("$-$ charges R150 $-$ debit order R450").scale(1.0).shift(DOWN * 0.3)
        b0_l4 = Tex("$+$ interest earned R60").scale(1.0).shift(DOWN * 1.1)
        b0_l5 = Tex("True book balance \\quad R10 400").scale(1.1).shift(DOWN * 2.0)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): both statements meet ---
        self.next_band(1)
        b1_t = Tex("Step 2: the reconciliation statements").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_l1 = Tex("Bank statement R9 800 $+$ deposit R3 200").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex("$-$ payments not through R2 600 $=$ R10 400").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("Creditors: our R6 600 $+$ invoice R950").scale(1.0).shift(band_shift(1) + DOWN * 0.6)
        b1_l4 = Tex("$=$ R7 550; their R8 750 $-$ payment R1 200").scale(1.0).shift(band_shift(1) + DOWN * 1.4)
        b1_l5 = Tex("$=$ R7 550 — both records meet").scale(1.05).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        b1_l6 = Tex("Timing reconciles; errors get corrected").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): contribution and break-even ---
        self.next_band(2)
        b2_t = Tex("Costing: sort costs by behaviour").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = Tex("Variable travels with the unit: R10").scale(1.05).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("Fixed stands still: R7 500 a month").scale(1.05).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("Sells at R25: contribution R25 $-$ R10 $=$ R15").scale(1.0).shift(band_shift(2) + DOWN * 0.5)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("Break-even: R7 500 $\\div$ R15 $=$ 500 units").scale(1.05).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)
        b2_l5 = Tex("499: loss. 500: level. Beyond:").scale(1.0).shift(band_shift(2) + DOWN * 2.3)
        b2_l6 = Tex("each unit carries its full R15 home").scale(1.0).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): profit at 620, proved both ways ---
        self.next_band(3)
        b3_t = Tex("Sell 620: profit proved both ways").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_l1 = Tex("Short way: 120 past the line $\\times$ R15").scale(1.05).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("$=$ R1 800").scale(1.1).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = Tex("Long way: sales R15 500 $-$ variable R6 200").scale(1.0).shift(band_shift(3) + DOWN * 0.5)
        b3_l4 = Tex("$=$ contribution R9 300 $-$ fixed R7 500").scale(1.0).shift(band_shift(3) + DOWN * 1.3)
        b3_l5 = Tex("$=$ R1 800 — same answer").scale(1.05).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.wait(2)
        b3_l6 = Tex("Price drops to R22: contribution R12,").scale(0.95).shift(band_shift(3) + DOWN * 2.9)
        b3_l7 = Tex("break-even jumps to 625").scale(0.95).shift(band_shift(3) + DOWN * 3.6)
        self.play(Write(b3_l6))
        self.play(Write(b3_l7))
        self.wait(3)

        # --- Band 4 (subtopic_3): stock systems and periodic cost of sales ---
        self.next_band(4)
        b4_t = Tex("Two ways to know cost of sales").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_l1 = Tex("Perpetual: recorded with every sale;").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex("theft visible as account vs count gap").scale(1.0).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("Periodic, by calculation:").scale(1.0).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex("R12 000 $+$ R40 000 $+$ R3 000 carriage").scale(1.0).shift(band_shift(4) + DOWN * 1.2)
        b4_l5 = Tex("$-$ closing R15 000 $=$ R40 000").scale(1.05).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l3))
        self.wait(1.5)
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        b4_l6 = Tex("cheaper, but cannot tell sold from stolen").scale(0.95).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_3): the debtors collection schedule ---
        self.next_band(5)
        b5_t = Tex("Debtors collection schedule").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_l1 = Tex("Pattern: 40\\% same month, 55\\% next,").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("5\\% never — written off").scale(1.0).shift(band_shift(5) + UP * 0.5)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("September: 40\\% $\\times$ R30 000 $=$ R12 000").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex("$+$ 55\\% $\\times$ R28 000 (August) $=$ R15 400").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        b5_l5 = Tex("Total collected: R27 400").scale(1.05).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(2)
        b5_trap = Tex("Budget on 100\\% of credit sales?").scale(1.0).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_trap))
        self.play(Create(strike(b5_trap)))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): VAT skeleton and categories ---
        self.next_band(6)
        b6_t = Tex("VAT: the collector's arithmetic").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = Tex("Charge output tax, reclaim input tax,").scale(1.05).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("pay over the difference — never yours").scale(1.05).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Standard-rated: 15\\%").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex("Zero-rated: 0\\%, inputs STILL reclaimed").scale(1.0).shift(band_shift(6) + DOWN * 1.3)
        b6_l5 = Tex("Exempt: outside — no output, no reclaim").scale(1.0).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6_l3))
        self.wait(1.5)
        self.play(Write(b6_l4))
        self.wait(2)
        self.play(Write(b6_l5))
        self.wait(2)
        b6_l6 = Tex("The separating question: may the seller").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        b6_l7 = Tex("reclaim its own VAT?").scale(0.95).shift(band_shift(6) + DOWN * 3.6)
        self.play(Write(b6_l6))
        self.play(Write(b6_l7))
        self.wait(3)

        # --- Band 7 (subtopic_4): both directions, and the return ---
        self.next_band(7)
        b7_t = Tex("Both directions, and the return").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("Up from exclusive: $\\times$ 1,15").scale(1.05).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_trap = Tex("VAT in R4 600 $=$ 15\\% of R4 600?").scale(1.0).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_trap))
        self.play(Create(strike(b7_trap)))
        self.wait(2)
        b7_l2 = MathTex(r"4\,600 \times \tfrac{15}{115} = \text{R}600").scale(1.1).shift(band_shift(7) + DOWN * 0.7)
        b7_l3 = Tex("on an exclusive R4 000").scale(1.0).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("Return: output R9 000 $-$ input R6 300").scale(1.0).shift(band_shift(7) + DOWN * 2.3)
        b7_l5 = Tex("$=$ R2 700 to SARS — TRUST money").scale(1.0).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(b7_l4))
        self.wait(2)
        self.play(Write(b7_l5))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): when two notebooks disagree ---
        self.next_band(8)
        b8_t = Tex("When two notebooks disagree").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("The bank knew: fee R150, debit order").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("R450, interest R60 — write them in first").scale(1.0).shift(band_shift(8) + UP * 0.5)
        b8_l3 = Tex("Your notebook now says R10 400").scale(1.05).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("You knew: travelling deposit, unlanded").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        b8_l5 = Tex("payments — the bank's side meets R10 400").scale(1.0).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2.5)
        b8_l6 = Tex("Wholesaler: both corrected to R7 550 —").scale(1.0).shift(band_shift(8) + DOWN * 2.9)
        b8_l7 = Tex("pay the meeting point, not the shout").scale(1.0).shift(band_shift(8) + DOWN * 3.6)
        self.play(Write(b8_l6))
        self.play(Write(b8_l7))
        self.wait(3)

        # --- Band 9 (subtopic_6): the vetkoek line that pays the rent ---
        self.next_band(9)
        b9_t = Tex("The vetkoek line that pays the rent").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Sells R25; flour, oil, filling R10:").scale(1.05).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("each vetkoek walks R15 to the rent").scale(1.05).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("R7 500 $\\div$ R15 $=$ 500 vetkoek").scale(1.1).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex("1 to 499: working for the landlord").scale(1.0).shift(band_shift(9) + DOWN * 1.4)
        b9_l5 = Tex("501: the first one working for YOU").scale(1.0).shift(band_shift(9) + DOWN * 2.2)
        self.play(Write(b9_l4))
        self.wait(2)
        self.play(Write(b9_l5))
        self.wait(2)
        b9_l6 = Tex("620 sold: 120 $\\times$ R15 $=$ R1 800 profit").scale(1.0).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l6))
        self.wait(3)

        # --- Band 10 (subtopic_7): the slip, the shelf, the month ahead ---
        self.next_band(10)
        b10_t = Tex("The slip, the shelf, the month ahead").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Slip R4 600 incl.: VAT $=$ 15 of 115").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("$=$ R600 — passing through, never resting").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.wait(2)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = Tex("Shelf: 12 $+$ 40 $+$ 3 $-$ 15 (thousands)").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        b10_l4 = Tex("$=$ R40 000 went out — blind to theft").scale(1.0).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l3))
        self.wait(2)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("Month ahead: plan on 40 now, 55 later,").scale(1.0).shift(band_shift(10) + DOWN * 2.2)
        b10_l6 = Tex("let the 5 go before it lies to you").scale(1.0).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.wait(4)
