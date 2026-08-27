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

# Band-layout whiteboard scene for the IEB Grade 11 Term 1 duo
# "Capital, Current Accounts and Year-End Adjustments" (partnerships).
# One band per teaching beat; camera moves down, nothing removed.
# Exporter-safe primitives only; every figure mirrors script.md.
# Subtopic shares: 225/235/235/220/190/200/190 of 1495 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CapitalCurrentAccountsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): capital fixed, current moving ---
        title = Tex("Capital, Current Accounts and Adjustments").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Capital: Khumalo R500 000, Smit R250 000").scale(1.05).shift(UP * 1.1)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("Capital stays FIXED — formal changes only").scale(1.05).shift(UP * 0.3)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("Current account = the running scorecard:").scale(1.05).shift(DOWN * 0.6)
        b0_l4 = Tex("earnings credited, drawings debited").scale(1.05).shift(DOWN * 1.4)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(2.5)
        b0_l5 = Tex("Credit balance: business owes the partner").scale(1.0).shift(DOWN * 2.3)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): what the agreement promises ---
        self.next_band(1)
        b1_title = Tex("The agreement promises, before any split").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Interest on capital 8\%:").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("R40 000 Khumalo, R20 000 Smit").scale(1.05).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Salaries: Khumalo R132 000, Smit R156 000").scale(1.0).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = Tex("Bonus R12 000 to Smit if target met").scale(1.0).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("Remainder shared 2 : 1 (capital ratio)").scale(1.05).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the four timing adjustments ---
        self.next_band(2)
        b2_title = Tex("Timing adjustments at 28 February").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Accrued expense: Dr Electricity R2 340,").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("Cr Accrued expenses (liability)").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("Prepaid: Dr Prepaid R3 300, Cr Insurance").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex("Advance rent: Dr Rent income R4 100 —").scale(1.0).shift(band_shift(2) + DOWN * 1.2)
        b2_l5 = Tex(r"rent 53 300 $\rightarrow$ R49 200 (12 months)").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.wait(2.5)
        b2_l6 = Tex("Accrued income: commission R1 750 earned").scale(1.0).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): depreciation twice, stock deficit ---
        self.next_band(3)
        b3_title = Tex("Depreciation twice, and the missing stock").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Vehicles: 20\% $\times$ 360 000 = R72 000").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = Tex(r"Equipment: 10\% $\times$ 55 000 = R5 500").scale(1.05).shift(band_shift(3) + UP * 0.2)
        b3_l3 = Tex("(diminishing balance)").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(b3_l2))
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex(r"Stock deficit: 214 600 $-$ 212 150 = R2 450").scale(1.0).shift(band_shift(3) + DOWN * 1.4)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex("Dr Trading stock deficit, Cr Trading stock").scale(0.95).shift(band_shift(3) + DOWN * 2.3)
        b3_l6 = Tex("— an expense AND a control alarm").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): provision for bad debts, created ---
        self.next_band(4)
        b4_title = Tex("New: provision for bad debts").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Debtors R64 000; provide 5\%:").scale(1.05).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"64\,000 \times 5\% = R3\,200").scale(1.1).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("Dr Provision adjustment, Cr Provision").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex(r"Statements: 64 000 $-$ 3 200 = R60 800").scale(1.05).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = Tex("Bad debts = a NAMED debtor;").scale(0.95).shift(band_shift(4) + DOWN * 2.5)
        b4_l6 = Tex("the provision = the UNKNOWN slice").scale(0.95).shift(band_shift(4) + DOWN * 3.2)
        self.play(Write(b4_l5))
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_3): adjusting it, and capitalised interest ---
        self.next_band(5)
        b5_title = Tex("Adjust the provision; capitalised interest").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Next year: 78 000 $\times$ 5\% = 3 900").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("Only the R700 movement hits profit").scale(1.05).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex(r"Loan R200 000 at 11\%: interest R22 000").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_wrong = Tex("Dr Interest on loan, Cr Bank?").scale(1.0).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5_wrong))
        self.play(Create(strike(b5_wrong)))
        self.wait(2)
        b5_l4 = Tex("Cr LOAN — no money left; the debt grew").scale(1.0).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex(r"200 000 + 22 000 $-$ 45 000 = R177 000").scale(1.05).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): reversals on 1 March ---
        self.next_band(6)
        b6_title = Tex("Reversals on the first of March").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Without a flip, the power bill counts twice").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = Tex("1 March: Dr Accrued expenses, Cr Electricity").scale(1.0).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("Electricity opens R2 340 in credit;").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex("March payment lands — nets to nil").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("Flip all four: R2 340, R3 300,").scale(1.0).shift(band_shift(6) + DOWN * 2.1)
        b6_l6 = Tex("R4 100, R1 750 — exactly reversed").scale(1.0).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): what is never reversed ---
        self.next_band(7)
        b7_title = Tex("Never reversed").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Depreciation, trading stock deficit,").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("bad debts, the provision — losses stay").scale(1.05).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("The test: did it move an amount ACROSS").scale(1.05).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex("the year-end boundary?").scale(1.05).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("Yes: reverse on day one. No: leave it").scale(1.05).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): two friends, one till, two scorecards ---
        self.next_band(8)
        b8_title = Tex("Two friends, one till, two scorecards").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("On the wall: Lwazi R60 000, Musa R30 000").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("The wall never moves — that is capital").scale(1.0).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("The scorecard moves every week: salary,").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        b8_l4 = Tex("interest earned, airtime and bread taken").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(3)
        b8_l5 = Tex("Wall = planted; scorecard = owed right now").scale(1.0).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3.5)

        # --- Band 9 (subtopic_6): making the photo honest ---
        self.next_band(9)
        b9_title = Tex("Making the photo honest").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Lights used, bill not here: write in R2 340").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("Next year's insurance R3 300: set aside").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("March rent R4 100 held; commission R1 750 in").scale(0.95).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex(r"Dimmer switch: 5\% of 64 000 = R3 200,").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        b9_l5 = Tex("debtors shown at R60 800").scale(1.0).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(3)
        b9_l6 = Tex(r"Loan: 200 000 + 22 000 $-$ 45 000 = R177 000").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3.5)

        # --- Band 10 (subtopic_7): flipping the switches ---
        self.next_band(10)
        b10_title = Tex("Flipping the switches on day one").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("The March bill would be written TWICE").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.play(Create(strike(b10_l1)))
        self.wait(2.5)
        b10_l2 = Tex("So flip the four shuffles exactly:").scale(1.0).shift(band_shift(10) + UP * 0.2)
        b10_l3 = Tex("power, insurance, early rent, commission").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b10_l2))
        self.play(Write(b10_l3))
        self.wait(3)
        b10_l4 = Tex("The bakkie's wear stays; missing stock").scale(1.0).shift(band_shift(10) + DOWN * 1.4)
        b10_l5 = Tex("stays missing; the dial stays set").scale(1.0).shift(band_shift(10) + DOWN * 2.1)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(3)
        b10_l6 = Tex("Shuffles get flipped; losses stay").scale(1.05).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
