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

# Band-layout whiteboard scene for the CAPS Grade 10 Accounting session duo
# "Notes to the Financial Statements". Add-only lifecycle, one band per
# teaching beat, camera moves down between bands. Covers all seven subtopics:
# Part 1 Expert (subtopics 1-4), Part 2 Simplifier (subtopics 5-7) in fresh
# bands. subtopics.json durations 200/220/210/230/180/190/190 of 1420 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class NotesToStatementsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): why notes exist, the cross-reference rule
        title = Tex("Notes to the Financial Statements").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("A statement line compresses a family:").scale(1.05).shift(UP * 1.2)
        b0_l2 = Tex("Trade and other receivables: R4 950 — but WHO?").scale(1.0).shift(UP * 0.4)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("The note behind the line opens the figure up").scale(1.0).shift(DOWN * 0.5)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("Line and note must agree TO THE RAND").scale(1.05).shift(DOWN * 1.4)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2.5)
        b0_l5 = Tex("Seven Grade 10 notes: interest, fixed assets,").scale(0.95).shift(DOWN * 2.3)
        b0_l6 = Tex("inventories, receivables, cash, equity, payables").scale(0.95).shift(DOWN * 3.0)
        self.play(Write(b0_l5))
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_2): the fixed assets note, built as its format
        self.next_band(1)
        b1_title = Tex("The fixed assets note").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        panel = Rectangle(width=10.5, height=4.2).shift(band_shift(1) + DOWN * 0.4)
        self.play(Create(panel))
        b1_r1 = Tex("Carrying value at beginning of year: nil").scale(0.95).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_r1))
        self.wait(2)
        b1_r2 = Tex("Additions at cost: R18 000").scale(0.95).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_r2))
        self.wait(2)
        b1_r3 = Tex("Depreciation for the year: (R1 800)").scale(0.95).shift(band_shift(1) + DOWN * 0.5)
        self.play(Write(b1_r3))
        self.wait(2)
        tot_line = Line(LEFT * 5.25, RIGHT * 5.25).shift(band_shift(1) + DOWN * 1.0)
        self.play(Create(tot_line))
        b1_r4 = Tex("Carrying value at end: R16 200").scale(0.95).shift(band_shift(1) + DOWN * 1.5)
        b1_r5 = Tex("(cost R18 000 less acc. depreciation R1 800)").scale(0.9).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1_r4))
        self.play(Create(SurroundingRectangle(b1_r4, color=GREEN)))
        self.wait(2)
        self.play(Write(b1_r5))
        self.wait(2)
        b1_l1 = Tex("One note, two statements, three agreements").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l1))
        self.wait(3)

        # --- Band 2 (subtopic_2): the interest notes and the growing loan
        self.next_band(2)
        b2_title = Tex("The interest notes").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = Tex("Interest income: none this year").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex("Interest expense: R1 200 on the loan").scale(1.05).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"10\,000 + 1\,200 = 11\,200").scale(1.15).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex("The debt grew without a payment —").scale(1.0).shift(band_shift(2) + DOWN * 1.8)
        b2_l5 = Tex("interest capitalised onto the loan").scale(1.0).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_3): inventories and receivables registers
        self.next_band(3)
        b3_title = Tex("Working-capital notes I").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = Tex("Inventories: stock R2 250 + consumables R200").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"= \text{R}2\,450").scale(1.1).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex("Receivables: debtors R3 850").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = Tex("+ accrued income R500 + prepaid R600").scale(1.0).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = MathTex(r"= \text{R}4\,950").scale(1.1).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): cash and payables registers
        self.next_band(4)
        b4_title = Tex("Working-capital notes II").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex("Cash: bank R15 000 + petty cash R300").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"= \text{R}15\,300").scale(1.1).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex("Payables: creditors R3 200 + accrued R100").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = Tex("+ income received in advance R500").scale(1.0).shift(band_shift(4) + DOWN * 1.5)
        b4_l5 = MathTex(r"= \text{R}3\,800").scale(1.1).shift(band_shift(4) + DOWN * 2.3)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(2)
        b4_l6 = Tex("Every total lands on its statement line").scale(0.95).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_4): the owner's equity note
        self.next_band(5)
        b5_title = Tex("The owner's equity note").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("Balance at beginning: R20 000").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex("+ net profit for the year: R7 900").scale(1.0).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("$-$ drawings: (R4 000)").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex("Balance at end: R23 900").scale(1.05).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_wrong = Tex("Owner's capital contribution booked as income").scale(0.95).shift(band_shift(5) + DOWN * 2.3)
        self.play(Write(b5_wrong))
        self.play(Create(strike(b5_wrong)))
        b5_l5 = Tex("A contribution is never income").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the GAAP thread, gathered
        self.next_band(6)
        b6_title = Tex("The GAAP thread, gathered").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Historical cost: equipment anchored at R18 000").scale(0.95).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex("Going concern: carrying values, not forced sale").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("Matching: shaped every adjusted figure").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("Prudence: the deficit and the loan, without delay").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("Entity: drawings out of expenses, home out of books").scale(0.9).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l5))
        self.wait(2)
        b6_l6 = Tex("Disclosure: material detail, organised into notes").scale(0.95).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): the indigenous bookkeeping thread
        self.next_band(7)
        b7_title = Tex("Indigenous bookkeeping").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Stokvels, burial societies, savings clubs:").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("member books, contribution registers, rosters").scale(1.0).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Member detail agreeing with a running total —").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        b7_l4 = Tex("a control account and its list, in another dress").scale(1.0).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("Money held for others must be accounted to them").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the front page and its backpages
        self.next_band(8)
        b8_title = Tex("The page and its backpages").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Statements are headlines: PROFIT R7 900").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Notes are the inside pages — same total, faces:").scale(1.0).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex("customers R3 850, tenant's month, insurer's cover").scale(0.95).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_wrong = Tex("Front page R4 950, inside page adds to R4 850").scale(0.95).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_wrong))
        self.play(Create(strike(b8_wrong)))
        self.wait(2)
        b8_l4 = Tex("Headline and story must say the same thing").scale(1.0).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): unpacking the suitcases
        self.next_band(9)
        b9_title = Tex("Unpacking the suitcases").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Inventories: R2 250 + R200, tag R2 450").scale(1.0).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("Receivables: R3 850 + R500 + R600, tag R4 950").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("Cash: R15 000 + R300, tag R15 300").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("Payables: R3 200 + R100 + R500, tag R3 800").scale(0.95).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("Fixed assets: cost 18 000, worn 1 800, left 16 200").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9_l5))
        self.wait(2)
        b9_l6 = Tex("The tag outside must equal the contents inside").scale(1.0).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): trust, in any language
        self.next_band(10)
        b10_title = Tex("Trust, in any language").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("The stokvel book: every member, every").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("contribution, every payout, every date").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Any member may check her page, any meeting").scale(1.0).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex("GAAP and the stokvel book: two grammars").scale(1.0).shift(band_shift(10) + DOWN * 1.6)
        b10_l5 = Tex("of the same honesty").scale(1.0).shift(band_shift(10) + DOWN * 2.4)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(4)
