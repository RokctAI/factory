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
# "Final Accounts and the Appropriation Account" (partnerships).
# One band per teaching beat; camera moves down, nothing removed.
# Exporter-safe primitives only; appropriation and current accounts are
# posted line by line in script order, totals last.
# Subtopic shares: 220/245/230/225/195/195/195 of 1505 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FinalAccountsAppropriationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the trading account ---
        title = Tex("Final Accounts and Appropriation").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Trading account — home of gross profit").scale(1.05).shift(UP * 1.1)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("Sales R2 856 000 (credit side)").scale(1.05).shift(UP * 0.3)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex(r"Cost of sales R1 904 000 (debit side)").scale(1.05).shift(DOWN * 0.5)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("Gross profit R952 000, carried down").scale(1.05).shift(DOWN * 1.4)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2)
        b0_l5 = Tex(r"Check: 952 000 on cost 1 904 000 = 50\% mark-up").scale(0.95).shift(DOWN * 2.3)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): profit and loss, and where it goes ---
        self.next_band(1)
        b1_title = Tex("Profit and loss — home of net profit").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Cr: gross profit 952 000 + rent 49 200").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("+ commission 26 800 = R1 028 000").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Dr: operating expenses 526 000").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        b1_l4 = Tex("+ interest on loan 22 000 = R548 000").scale(1.0).shift(band_shift(1) + DOWN * 1.1)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex(r"Net profit: 1 028 000 $-$ 548 000 = R480 000").scale(1.05).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(2)
        b1_l6 = Tex("Two owners — so it goes to APPROPRIATION").scale(1.0).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): the appropriation account, top down ---
        self.next_band(2)
        b2_title = Tex("Appropriation: the agreement, in order").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"1. Interest on capital 8\%:").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("40 000 + 20 000 = R60 000").scale(1.0).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("2. Salaries: 132 000 + 156 000 = R288 000").scale(1.0).shift(band_shift(2) + DOWN * 0.3)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("3. Bonus to Smit: R12 000").scale(1.0).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex(r"Spoken for: R360 000; remains R120 000").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l5))
        self.wait(2)
        b2_l6 = MathTex(r"\tfrac{2}{3} = R80\,000; \quad \tfrac{1}{3} = R40\,000").scale(1.05).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): proof, and the expense trap ---
        self.next_band(3)
        b3_title = Tex("Prove the split, watch the trap").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Khumalo: 40 000 + 132 000 + 80 000").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("= R252 000").scale(1.05).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex("Smit: 20 000 + 156 000 + 12 000").scale(1.0).shift(band_shift(3) + DOWN * 0.4)
        b3_l4 = Tex("+ 40 000 = R228 000").scale(1.05).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(2.5)
        b3_l5 = Tex("252 000 + 228 000 = R480 000 — all shared").scale(1.0).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(2)
        b3_wrong = Tex("Partner's salary in operating expenses?").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(3)

        # --- Band 4 (subtopic_3): current account of Khumalo ---
        self.next_band(4)
        b4_title = Tex("Current account: Khumalo").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1)
        t_top = Line(band_shift(4) + UP * 2.0 + LEFT * 3.4,
                     band_shift(4) + UP * 2.0 + RIGHT * 3.4, stroke_width=4)
        t_mid = Line(band_shift(4) + UP * 2.0,
                     band_shift(4) + DOWN * 1.4, stroke_width=4)
        self.play(Create(t_top))
        self.play(Create(t_mid))
        self.wait(1)
        b4_cr1 = Tex("b/d 9 600").scale(0.9).shift(band_shift(4) + UP * 1.5 + RIGHT * 1.8)
        self.play(Write(b4_cr1))
        self.wait(1.5)
        b4_cr2 = Tex("Interest 40 000").scale(0.9).shift(band_shift(4) + UP * 0.9 + RIGHT * 1.8)
        self.play(Write(b4_cr2))
        self.wait(1.5)
        b4_cr3 = Tex("Salary 132 000").scale(0.9).shift(band_shift(4) + UP * 0.3 + RIGHT * 1.8)
        self.play(Write(b4_cr3))
        self.wait(1.5)
        b4_cr4 = Tex("Share 80 000").scale(0.9).shift(band_shift(4) + DOWN * 0.3 + RIGHT * 1.8)
        self.play(Write(b4_cr4))
        self.wait(1.5)
        b4_dr1 = Tex("Drawings 214 000").scale(0.9).shift(band_shift(4) + UP * 1.5 + LEFT * 1.8)
        self.play(Write(b4_dr1))
        self.wait(2)
        b4_bal = Tex(r"261 600 $-$ 214 000 = R47 600 credit").scale(1.0).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_bal))
        self.play(Create(SurroundingRectangle(b4_bal, color=GREEN)))
        self.wait(2)
        b4_l5 = Tex("The business owes Khumalo R47 600").scale(1.0).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): current account of Smit ---
        self.next_band(5)
        b5_title = Tex("Current account: Smit").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Opens R6 300 in DEBIT — drew too much").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex("Credits: 20 000 + 156 000 + 12 000").scale(1.0).shift(band_shift(5) + UP * 0.3)
        b5_l3 = Tex("+ 40 000 = R228 000").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l2))
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex("Debits: 6 300 + drawings 195 500 = 201 800").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("Closing balance: R26 200 credit").scale(1.05).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(2)
        b5_l6 = Tex("Together R73 800 joins capital R750 000").scale(0.95).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): the equation, three columns ---
        self.next_band(6)
        b6_title = Tex("The accounting equation, partnership edition").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Capital EFT R60 000: A +60 000, E +60 000").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = Tex("Stock taken R4 200: A $-$4 200,").scale(1.0).shift(band_shift(6) + UP * 0.3)
        b6_l3 = Tex("E $-$4 200 via drawings, at cost").scale(1.0).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6_l2))
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex("Interest on capital allowed R40 000:").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        b6_l5 = Tex("no effect on totals — a REDISTRIBUTION").scale(1.0).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(2.5)
        b6_l6 = Tex("Appropriations never create or destroy equity").scale(0.95).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): two more events, and the method ---
        self.next_band(7)
        b7_title = Tex("Two more events, one method").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Interest capitalised R22 000:").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("L +22 000, E $-$22 000 — still level").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Pay creditor R16 500: A $-$16 500,").scale(1.0).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex("L $-$16 500 — equity untouched").scale(1.0).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("Method: write the double entry first,").scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        b7_l6 = Tex("classify accounts, read effects off it").scale(1.0).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): one pot, three ladles ---
        self.next_band(8)
        b8_title = Tex("One pot, three ladles").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("The pot: net profit R480 000").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Ladle 1 — money waiting: 40 000 + 20 000").scale(1.0).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Ladle 2 — hands working: 132 000 +").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        b8_l4 = Tex("156 000 + bonus 12 000").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex("Ladle 3 — leftovers R120 000 split 2 : 1:").scale(1.0).shift(band_shift(8) + DOWN * 2.0)
        b8_l6 = Tex("R80 000 and R40 000 — pot empty").scale(1.0).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l5))
        self.wait(2)
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(3.5)

        # --- Band 9 (subtopic_6): each friend's tab ---
        self.next_band(9)
        b9_title = Tex("Each friend's tab").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Khumalo: owed 9 600, earns 252 000,").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("side reaches 261 600; draws 214 000").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(3)
        b9_l3 = Tex("Tab: shop owes him R47 600").scale(1.05).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("Smit: opens R6 300 in the red,").scale(1.0).shift(band_shift(9) + DOWN * 1.4)
        b9_l5 = Tex("earns 228 000, draws 195 500 + 6 300").scale(1.0).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(3)
        b9_l6 = Tex("Ends: shop owes HER R26 200").scale(1.05).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3.5)

        # --- Band 10 (subtopic_7): the scale never lies ---
        self.next_band(10)
        b10_title = Tex("The scale never lies").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("EFT in 60 000: both sides up sixty — level").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex("Stock home 4 200: both sides down — level").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Loan grows 22 000, owners down 22 000").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex("Interest on capital: no totals move —").scale(1.0).shift(band_shift(10) + DOWN * 1.3)
        b10_l5 = Tex("it just writes a name on the serving").scale(1.0).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(3)
        b10_l6 = Tex("Never guess: write the entry, read the signs").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
