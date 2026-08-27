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

# Band-layout whiteboard scene for "Unique Transactions" (grade 12, term 1,
# companies). One band per teaching beat; the camera moves down and nothing
# is removed. Part 1 (Expert) = subtopics 1-4, Part 2 (Simplifier) =
# subtopics 5-7 in fresh bands. Exporter-safe primitives only; write-only
# reveals. Subtopic durations 225/250/240/220/195/200/200 of 1530 s guide
# the apportioning. Worked figures follow Naledi Limited.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class UniqueTransactionsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the company form ---
        title = Tex("Companies: Unique Transactions").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Register the MOI with the CIPC:").scale(1.0).shift(UP * 1.3)
        b0_l2 = Tex("Companies Act 71 of 2008 — a legal person").scale(0.95).shift(UP * 0.6)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Limited liability: lose only the price").scale(1.0).shift(DOWN * 0.3)
        b0_l4 = Tex("paid for the shares; continuity: owners").scale(1.0).shift(DOWN * 1.0)
        b0_l5 = Tex("change, the company carries on").scale(1.0).shift(DOWN * 1.7)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.play(Write(b0_l5))
        self.wait(2.5)
        b0_l6 = Tex("Public (Ltd): public offers, JSE listing").scale(0.95).shift(DOWN * 2.6)
        b0_l7 = Tex("Private (Pty Ltd): no offers to the public").scale(0.95).shift(DOWN * 3.3)
        self.play(Write(b0_l6))
        self.play(Write(b0_l7))
        self.wait(3)

        # --- Band 1 (subtopic_1): ownership split from control ---
        self.next_band(1)
        b1_t = Tex("Owning is not managing").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_l1 = Tex("Shareholders own and vote at the AGM;").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex("elected directors run the business").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Spending other people's money $\\Rightarrow$").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        b1_l4 = Tex("independent auditor reports to shareholders").scale(0.9).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(2.5)
        b1_l5 = Tex("AUTHORISED: the ceiling in the MOI").scale(0.95).shift(band_shift(1) + DOWN * 2.1)
        b1_l6 = Tex("ISSUED: actually sold — never above it").scale(0.95).shift(band_shift(1) + DOWN * 2.8)
        b1_l7 = Tex("No par value: recorded at the price raised").scale(0.95).shift(band_shift(1) + DOWN * 3.5)
        self.play(Write(b1_l5))
        self.wait(2)
        self.play(Write(b1_l6))
        self.play(Write(b1_l7))
        self.wait(3)

        # --- Band 2 (subtopic_2): the share issue ---
        self.next_band(2)
        b2_t = Tex("Naledi Ltd issues shares").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = Tex("Start: 600 000 shares, R3 000 000").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("(average R5,00 per share)").scale(0.95).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("Issue 200 000 at R8,00 $=$ R1 600 000:").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        b2_l4 = Tex("Dr Bank, Cr Ordinary Share Capital").scale(1.0).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Now 800 000 shares, R4 600 000").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
        b2_l6 = Tex("New average: R4 600 000 $\\div$ 800 000 $=$ R5,75").scale(1.0).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l5))
        self.wait(2)
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the buy-back ---
        self.next_band(3)
        b3_t = Tex("The buy-back: 40 000 at R9,00").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_trap = Tex("Take R9,00 a share out of capital?").scale(1.0).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_trap))
        self.play(Create(strike(b3_trap)))
        self.wait(2)
        b3_l1 = Tex("Capital surrenders only its AVERAGE:").scale(1.0).shift(band_shift(3) + UP * 0.3)
        b3_l2 = Tex("Dr Share Capital 40 000 $\\times$ R5,75 $=$ R230 000").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        b3_l3 = Tex("Dr Retained Income (excess) R130 000").scale(0.95).shift(band_shift(3) + DOWN * 1.3)
        b3_l4 = Tex("Cr Bank R360 000").scale(1.0).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex("After: 760 000 shares, R4 370 000 —").scale(0.95).shift(band_shift(3) + DOWN * 2.9)
        b3_l6 = Tex("repurchased shares are CANCELLED").scale(0.95).shift(band_shift(3) + DOWN * 3.6)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): income tax and the SARS score ---
        self.next_band(4)
        b4_t = Tex("Income tax: the SARS score").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_l1 = Tex("Provisional: R160 000 $+$ R200 000").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex("$=$ R360 000 paid in advance").scale(1.0).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("Charge: 27\\% of R1 500 000 $=$ R405 000").scale(1.0).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex("Score: R405 000 owed $-$ R360 000 paid").scale(1.0).shift(band_shift(4) + DOWN * 1.4)
        b4_l5 = Tex("$=$ R45 000 current liability").scale(1.05).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        b4_l6 = Tex("overpay and it flips to a current asset").scale(0.95).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_3): dividends on the shares in issue ---
        self.next_band(5)
        b5_t = Tex("Dividends: count the shares each date").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_l1 = Tex("Interim (Oct, 800 000 shares):").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("30c $\\times$ 800 000 $=$ R240 000 paid").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_trap = Tex("Final on 800 000 shares?").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(b5_trap))
        self.play(Create(strike(b5_trap)))
        self.wait(2)
        b5_l3 = Tex("After the buy-back: 50c $\\times$ 760 000").scale(1.0).shift(band_shift(5) + DOWN * 1.4)
        b5_l4 = Tex("$=$ R380 000 declared, unpaid:").scale(1.0).shift(band_shift(5) + DOWN * 2.2)
        b5_l5 = Tex("Shareholders for Dividends (liability)").scale(0.95).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        b5_l6 = Tex("Total dividends for the year: R620 000").scale(0.95).shift(band_shift(5) + DOWN * 3.6)
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): the loan with capitalised interest ---
        self.next_band(6)
        b6_t = Tex("Loan with capitalised interest").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = Tex("Kopano Bank: R800 000 at 10\\%").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("Interest ADDED to the loan: $+$R80 000").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("Instalments paid: $-$R180 000").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex("R800 000 $+$ R80 000 $-$ R180 000 $=$ R700 000").scale(1.0).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_l5 = Tex("The loan grows before payments shrink it;").scale(0.95).shift(band_shift(6) + DOWN * 2.3)
        b6_l6 = Tex("the interest is still a full expense").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): fees, audit fees, retained income ---
        self.next_band(7)
        b7_t = Tex("Fees are not dividends").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("Directors' fees: pay for the work —").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("operating expense, before net profit").scale(1.0).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Audit fees: the check on management —").scale(1.0).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex("appointed by and reporting to shareholders").scale(0.95).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("Dividends: reward of ownership, after tax —").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        b7_l6 = Tex("two separate doors for the same person").scale(0.95).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(2.5)
        b7_l7 = Tex("Retained income: profit kept after both").scale(0.95).shift(band_shift(7) + DOWN * 3.4)
        self.play(Write(b7_l7))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the spaza that became a company ---
        self.next_band(8)
        b8_t = Tex("The spaza that became a company").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Three new towns need more money than").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("one owner's savings: sell SLICES").scale(1.0).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("If it fails, you lose the slice price —").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex("nobody comes for your furniture").scale(1.0).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex("Authorised $=$ the most slices the loaf").scale(1.0).shift(band_shift(8) + DOWN * 2.0)
        b8_l6 = Tex("may ever hold; issued $=$ already cut").scale(1.0).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.wait(2.5)
        b8_l7 = Tex("The spenders are not the owners —").scale(0.95).shift(band_shift(8) + DOWN * 3.4)
        self.play(Write(b8_l7))
        self.wait(3)

        # --- Band 9 (subtopic_6): selling slices ---
        self.next_band(9)
        b9_t = Tex("Selling slices of the business").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Old slices: 600 000 for R3 000 000 (R5,00)").scale(0.95).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("Fresh: 200 000 at R8,00 — a stronger").scale(0.95).shift(band_shift(9) + UP * 0.4)
        b9_l3 = Tex("business costs more; average now R5,75").scale(0.95).shift(band_shift(9) + DOWN * 0.3)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("Buy-back at R9,00: one cheque, two sources —").scale(0.9).shift(band_shift(9) + DOWN * 1.2)
        b9_l5 = Tex("refund the R5,75 average from capital,").scale(0.95).shift(band_shift(9) + DOWN * 1.9)
        b9_l6 = Tex("farewell R3,25 from saved-up profits").scale(0.95).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l4))
        self.wait(2)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.wait(2.5)
        b9_l7 = Tex("Returned slices are shredded: 760 000 left").scale(0.9).shift(band_shift(9) + DOWN * 3.4)
        self.play(Write(b9_l7))
        self.wait(3)

        # --- Band 10 (subtopic_7): the company's own bills ---
        self.next_band(10)
        b10_t = Tex("The company's own bills").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Tax: guessed R360 000, counted R405 000 —").scale(0.9).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("still owes SARS R45 000 (or it flips)").scale(0.95).shift(band_shift(10) + UP * 0.5)
        self.play(Write(b10_l1))
        self.wait(2)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = Tex("Dividends: 30c on 800 000 in October;").scale(0.95).shift(band_shift(10) + DOWN * 0.4)
        b10_l4 = Tex("50c on 760 000 at year-end — count").scale(0.95).shift(band_shift(10) + DOWN * 1.1)
        b10_l5 = Tex("the slices on the day. Every time.").scale(0.95).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_l3))
        self.wait(2)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(2.5)
        b10_l6 = Tex("Fees for the managing, dividends for").scale(0.95).shift(band_shift(10) + DOWN * 2.7)
        b10_l7 = Tex("the owning — keep the doors apart").scale(0.95).shift(band_shift(10) + DOWN * 3.4)
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.wait(4)
