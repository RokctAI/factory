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

# Band-layout whiteboard scene for the grade 12 accounting session duo
# "Interpreting Reconciliations and Age Analysis". One band per teaching
# beat; camera moves down, earlier work stays. Exporter-safe mobjects only;
# write-only reveals — no Transform/FadeOut/sub-part indexing on MathTex.
#
# Subtopic time shares (subtopics.json, total 1565 s):
# 240/240/245/225 expert, 200/205/210 simplifier.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class InterpretingReconciliationsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the bank reconciliation bridge ---
        title = Tex("Reconciliations and Age Analysis").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Bank statement: R21\,400 \quad Books: R26\,900").scale(1.05).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex(r"$+$ Outstanding deposit \quad R12\,700").scale(1.05).shift(UP * 0.3)
        b0_l3 = Tex(r"$-$ Outstanding payments \quad R7\,200").scale(1.05).shift(DOWN * 0.5)
        b0_l4 = MathTex(r"21\,400 + 12\,700 - 7\,200 = 26\,900").scale(1.1).shift(DOWN * 1.4)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2)
        b0_l5 = Tex("Deposit outstanding for WEEKS: rolling of cash").scale(1.0).shift(DOWN * 2.3)
        b0_l6 = Tex("Charges on statement only: update the books first").scale(0.95).shift(DOWN * 3.0)
        self.play(Write(b0_l5))
        self.wait(2)
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_2): creditors' reconciliation, five items ---
        self.next_band(1)
        b1_title = Tex(r"Siyakha statement R52\,900 vs ledger R33\,400").scale(1.05).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Missing invoice: ledger $+$ R5\,800 $=$ R39\,200").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex(r"EFT of 29th: statement $-$ R7\,600 $=$ R45\,300").scale(1.0).shift(band_shift(1) + UP * 0.4)
        b1_l3 = Tex(r"Discount not processed: $-$ R850 $=$ R44\,450").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        b1_l4 = Tex(r"Returns not credited: $-$ R1\,750 $=$ R42\,700").scale(1.0).shift(band_shift(1) + DOWN * 1.2)
        b1_l5 = Tex(r"Not our invoice: $-$ R3\,500 $=$ R39\,200").scale(1.0).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2)
        self.play(Write(b1_l5))
        self.wait(2)
        b1_l6 = Tex(r"Both sides agree: true debt R39\,200").scale(1.05).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l6))
        self.play(Create(SurroundingRectangle(b1_l6, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the discipline and the cost of skipping ---
        self.next_band(2)
        b2_title = Tex("Each difference belongs to ONE side").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Your errors: fix your books").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("Their errors and timing: the statement side").scale(1.05).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_wrong = Tex(r"Paying the raw statement total of R52\,900").scale(1.05).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2)
        b2_l3 = Tex(r"That pays R3\,500 of another customer's goods").scale(1.0).shift(band_shift(2) + DOWN * 1.5)
        b2_l4 = Tex(r"Trade payables carries the corrected R39\,200").scale(1.0).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_3): control account vs list ---
        self.next_band(3)
        b3_title = Tex("Debtors' control vs debtors' list").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Control account: R96\,000 \quad List: R94\,200").scale(1.05).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"Found: invoice R1\,800 never posted to the customer").scale(1.0).shift(band_shift(3) + UP * 0.4)
        b3_l3 = Tex(r"Correct the LIST: R96\,000 both sides").scale(1.05).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = Tex(r"Journal-total errors $\rightarrow$ control account").scale(1.0).shift(band_shift(3) + DOWN * 1.4)
        b3_l5 = Tex(r"Posting errors $\rightarrow$ the list").scale(1.0).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the age analysis table ---
        self.next_band(4)
        b4_title = Tex(r"Age analysis: R96\,000 on 30-day terms").scale(1.1).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        h1 = Tex("Age").scale(0.9).shift(band_shift(4) + UP * 1.5 + LEFT * 3.0)
        h2 = Tex("Amount").scale(0.9).shift(band_shift(4) + UP * 1.5 + RIGHT * 0.3)
        h3 = Tex(r"\%").scale(0.9).shift(band_shift(4) + UP * 1.5 + RIGHT * 3.0)
        self.play(Write(h1), Write(h2), Write(h3))
        self.wait(1.5)
        r1a = Tex("Current").scale(0.85).shift(band_shift(4) + UP * 0.7 + LEFT * 3.0)
        r1b = Tex(r"R48\,000").scale(0.85).shift(band_shift(4) + UP * 0.7 + RIGHT * 0.3)
        r1c = Tex("50").scale(0.85).shift(band_shift(4) + UP * 0.7 + RIGHT * 3.0)
        self.play(Write(r1a), Write(r1b), Write(r1c))
        self.wait(1.5)
        r2a = Tex("30 days").scale(0.85).shift(band_shift(4) + UP * 0.0 + LEFT * 3.0)
        r2b = Tex(r"R24\,000").scale(0.85).shift(band_shift(4) + UP * 0.0 + RIGHT * 0.3)
        r2c = Tex("25").scale(0.85).shift(band_shift(4) + UP * 0.0 + RIGHT * 3.0)
        self.play(Write(r2a), Write(r2b), Write(r2c))
        self.wait(1.5)
        r3a = Tex("60 days").scale(0.85).shift(band_shift(4) + DOWN * 0.7 + LEFT * 3.0)
        r3b = Tex(r"R14\,400").scale(0.85).shift(band_shift(4) + DOWN * 0.7 + RIGHT * 0.3)
        r3c = Tex("15").scale(0.85).shift(band_shift(4) + DOWN * 0.7 + RIGHT * 3.0)
        self.play(Write(r3a), Write(r3b), Write(r3c))
        self.wait(1.5)
        r4a = Tex("90+ days").scale(0.85).shift(band_shift(4) + DOWN * 1.4 + LEFT * 3.0)
        r4b = Tex(r"R9\,600").scale(0.85).shift(band_shift(4) + DOWN * 1.4 + RIGHT * 0.3)
        r4c = Tex("10").scale(0.85).shift(band_shift(4) + DOWN * 1.4 + RIGHT * 3.0)
        self.play(Write(r4a), Write(r4b), Write(r4c))
        self.wait(2)
        b4_l1 = Tex("25\\% overdue; 90-day column breeds bad debts").scale(1.0).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex("Remind, charge interest, suspend credit, collect").scale(0.95).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4_l2))
        self.wait(3)

        # --- Band 5 (subtopic_4): ethics, fraud, paper trail ---
        self.next_band(5)
        b5_title = Tex("Four frauds the reconciliation exposes").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Rolling cash — deposits always one beat late").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("Invoice fraud — beaten by the three-way match").scale(1.0).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex("Friendly write-offs — need independent authorisation").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex("Kiting — month-end items that always reverse").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex(r"Principle: segregation $+$ an independent eye").scale(1.05).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(2)
        b5_l6 = Tex("Pay on the last day WITHIN terms — treasury discipline").scale(0.9).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l6))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): phone vs notebook ---
        self.next_band(6)
        b6_title = Tex("Why your phone and notebook disagree").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"Notebook: R26\,900 \quad Banking app: R21\,400").scale(1.05).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex(r"App has not seen the R12\,700 deposit").scale(1.0).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex(r"nor felt the R7\,200 of payments sent tonight").scale(1.0).shift(band_shift(6) + DOWN * 0.3)
        b6_l4 = MathTex(r"21\,400 + 12\,700 - 7\,200 = 26\,900").scale(1.05).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_l5 = Tex("A deposit on the bridge three weeks: hand in the till").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        b6_l6 = Tex("The banker must never build the bridge").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l5))
        self.wait(2)
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_6): the supplier's statement, re-walked ---
        self.next_band(7)
        b7_title = Tex("The statement says you owe more").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"Your book $33\,400 + 5\,800$ (real goods) $=$ R39\,200").scale(0.95).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"52\,900 - 7\,600 - 850 - 1\,750 - 3\,500").scale(1.0).shift(band_shift(7) + UP * 0.3)
        b7_l3 = Tex(r"$=$ R39\,200 — both records agree").scale(1.05).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        b7_l4 = Tex(r"Pay unchecked: R52\,900 — R13\,700 too much").scale(1.0).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("Never pay a statement; pay a RECONCILED statement").scale(0.95).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_7): the lunch book, aged ---
        self.next_band(8)
        b8_title = Tex(r"Who owes you R9\,000 — and for how long?").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Current R4\,500; 30 days R2\,250").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex(r"60 days R1\,350; 90$+$ days R900").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("The older the debt, the sicker it is").scale(1.05).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex("Remind, then interest, then close the tap,").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        b8_l5 = Tex("then collect — but credit checks come first").scale(0.95).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2.5)
        b8_l6 = Tex("Somewhere YOU are a line in a supplier's age analysis").scale(0.9).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l6))
        self.wait(4)
