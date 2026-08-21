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

# Band-layout whiteboard scene for the cash-receipts-journal session duo.
# Exporter-safe primitives only (Tex/MathTex/Line/Arrow/Rectangle/VGroup);
# write-only reveals. Band time follows subtopics.json
# (180/200/180/200/170/180/170 of 1280 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CashReceiptsJournalSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the job of the CRJ ---
        title = Tex("The Cash Receipts Journal").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("ALL money received, in date order,").scale(1.0).shift(UP * 1.1)
        l02 = Tex("for one month — money out stays out").scale(1.0).shift(UP * 0.3)
        self.play(Write(l01)); self.play(Write(l02)); self.wait(2.5)
        l03 = Tex("Proof: register roll, duplicate receipt,").scale(0.95).shift(DOWN * 0.8)
        l04 = Tex("duplicate deposit slip — numbered").scale(0.95).shift(DOWN * 1.6)
        self.play(Write(l03)); self.wait(2)
        self.play(Write(l04))
        l05 = Tex("No entry without evidence").scale(1.05).shift(DOWN * 2.6)
        self.play(Write(l05))
        self.play(Create(SurroundingRectangle(l05, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): columns + the analysis column ---
        self.next_band(1)
        b1_t = Tex("Analysis vs Bank").scale(1.2).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_t)); self.wait(2)
        b1_l1 = Tex("Analysis: what arrived, item by item").scale(1.0).shift(band_shift(1) + UP * 1.4)
        b1_l2 = Tex("Bank: what was deposited, and when").scale(1.0).shift(band_shift(1) + UP * 0.6)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        b1_l3 = Tex("Busy Saturday: five analysis amounts,").scale(0.95).shift(band_shift(1) + DOWN * 0.4)
        b1_l4 = Tex("one Bank figure").scale(1.0).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_l3)); self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("Takings banked daily, intact").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): the cash sale, two truths ---
        self.next_band(2)
        b2_t = Tex("Cash sales: two truths per sale").scale(1.15).shift(band_shift(2) + UP * 2.5)
        self.play(Write(b2_t)); self.wait(2)
        b2_l1 = Tex("Register roll: R1 800 — analysis, Bank, Sales").scale(0.95).shift(band_shift(2) + UP * 1.4)
        self.play(Write(b2_l1)); self.wait(2)
        b2_l2 = Tex("Mark-up 50\\% on cost:").scale(1.0).shift(band_shift(2) + UP * 0.5)
        b2_l3 = MathTex(r"1\,800 \div 1{,}5 = 1\,200").scale(1.1).shift(band_shift(2) + DOWN * 0.3)
        self.play(Write(b2_l2)); self.play(Write(b2_l3)); self.wait(2.5)
        b2_l4 = Tex("R1 200 into COST OF SALES, same line").scale(1.0).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2_l4)); self.wait(2)
        b2_l5 = MathTex(r"1\,200 \times 1{,}5 = 1\,800\ \checkmark").scale(1.0).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the two pitfalls ---
        self.next_band(3)
        b3_t = Tex("Two pitfalls, buried today").scale(1.15).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_t)); self.wait(2)
        b3_wrong1 = Tex("Take 50\\% off the price: R900").scale(1.0).shift(band_shift(3) + UP * 1.3)
        self.play(Write(b3_wrong1))
        self.play(Create(strike(b3_wrong1)))
        b3_l1 = Tex("The mark-up was ON COST — divide by 1,5").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1)); self.wait(2.5)
        b3_wrong2 = Tex("Leave cost of sales blank: no cash moved").scale(0.95).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_wrong2))
        self.play(Create(strike(b3_wrong2)))
        b3_l2 = Tex("The column exists for the non-cash truth").scale(0.95).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l2))
        self.wait(3)

        # --- Band 4 (subtopic_3): receipts that are not sales ---
        self.next_band(4)
        b4_t = Tex("Receipts that are not sales").scale(1.15).shift(band_shift(4) + UP * 2.5)
        self.play(Write(b4_t)); self.wait(2)
        b4_l1 = Tex("Capital R60 000 — receipt 71:").scale(1.0).shift(band_shift(4) + UP * 1.4)
        b4_l2 = Tex("analysis, Bank, Sundries: `Capital'").scale(1.0).shift(band_shift(4) + UP * 0.6)
        self.play(Write(b4_l1)); self.play(Write(b4_l2)); self.wait(2.5)
        b4_l3 = Tex("Rent income R3 200 — receipt 72: same road").scale(0.95).shift(band_shift(4) + DOWN * 0.3)
        self.play(Write(b4_l3)); self.wait(2)
        b4_l4 = Tex("Daily regulars get lanes;").scale(1.0).shift(band_shift(4) + DOWN * 1.2)
        b4_l5 = Tex("rare visitors get NAMED in Sundries").scale(1.0).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l4)); self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_4): totals ---
        self.next_band(5)
        b5_t = Tex("Month end: rule off and total").scale(1.15).shift(band_shift(5) + UP * 2.5)
        self.play(Write(b5_t)); self.wait(2)
        b5_l1 = Tex("Bank: 1 800 + 60 000 + 3 200 + 2 700").scale(0.95).shift(band_shift(5) + UP * 1.4)
        b5_l2 = Tex("= R67 700").scale(1.1).shift(band_shift(5) + UP * 0.6)
        self.play(Write(b5_l1)); self.wait(2)
        self.play(Write(b5_l2)); self.wait(2)
        b5_l3 = Tex("Sales R4 500; Cost of Sales R3 000;").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex("Sundries R63 200").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l3)); self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): the cross-cast proof ---
        self.next_band(6)
        b6_t = Tex("The cross-cast").scale(1.2).shift(band_shift(6) + UP * 2.5)
        self.play(Write(b6_t)); self.wait(2)
        b6_l1 = MathTex(r"4\,500 + 63\,200 = 67\,700").scale(1.1).shift(band_shift(6) + UP * 1.3)
        self.play(Write(b6_l1)); self.wait(2)
        b6_l2 = Tex("= the Bank column total: proven").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2)
        b6_l3 = Tex("Cost of Sales stays OUTSIDE:").scale(1.0).shift(band_shift(6) + DOWN * 0.6)
        b6_l4 = Tex("not money — the parallel stock record").scale(0.95).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(b6_l3)); self.play(Write(b6_l4)); self.wait(2)
        b6_l5 = Tex("Cross-cast BEFORE posting, every month").scale(0.95).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l5))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): the money-in diary ---
        self.next_band(7)
        b7_t = Tex("The money-in diary").scale(1.2).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7_t)); self.wait(2)
        b7_l1 = Tex("One line: date, proof, who, how much").scale(1.0).shift(band_shift(7) + UP * 1.4)
        self.play(Write(b7_l1)); self.wait(2)
        b7_l2 = Tex("Sales, Sales, Sales... give it a column").scale(1.0).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l2)); self.wait(2)
        b7_l3 = Tex("Regulars get lanes;").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex("visitors get named — Capital, Rent income").scale(0.95).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(b7_l3)); self.play(Write(b7_l4)); self.wait(2)
        b7_l5 = Tex("Laziness, organised brilliantly").scale(1.0).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): the double line ---
        self.next_band(8)
        b8_t = Tex("What the customer pays, what the shelf loses").scale(1.0).shift(band_shift(8) + UP * 2.5)
        self.play(Write(b8_t)); self.wait(2)
        b8_l1 = Tex("Till: R1 800 in — the money truth").scale(1.0).shift(band_shift(8) + UP * 1.4)
        self.play(Write(b8_l1)); self.wait(2)
        b8_l2 = MathTex(r"1\,800 \div 1{,}5 = 1\,200").scale(1.1).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex("— the shelf's number, cost of sales").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l2)); self.play(Write(b8_l3)); self.wait(2.5)
        b8_l4 = Tex("R600 gross profit, known TODAY").scale(1.05).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2)
        b8_l5 = Tex("The perpetual system in one line").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_7): the month-end handshake ---
        self.next_band(9)
        b9_t = Tex("The month-end handshake").scale(1.2).shift(band_shift(9) + UP * 2.5)
        self.play(Write(b9_t)); self.wait(2)
        b9_l1 = MathTex(r"\text{Sales} + \text{Sundries} = \text{Bank}").scale(1.05).shift(band_shift(9) + UP * 1.4)
        self.play(Write(b9_l1)); self.wait(2)
        b9_l2 = MathTex(r"4\,500 + 63\,200 = 67\,700\ \checkmark").scale(1.0).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2)
        b9_l3 = Tex("Fails? Hunt the difference —").scale(1.0).shift(band_shift(9) + DOWN * 0.5)
        b9_l4 = Tex("a number on one side, a blank on the other").scale(0.95).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l3)); self.play(Write(b9_l4)); self.wait(2)
        b9_l5 = Tex("The journal catches its own errors first").scale(1.0).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9_l5))
        self.wait(4)
