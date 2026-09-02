# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from manim import *

# Band-layout whiteboard scene for the IEB Grade 10 Accounting session duo
# "Error Corrections and Post-Closing". Add-only lifecycle, one band per
# teaching beat, camera moves down between bands. Covers all seven subtopics:
# Part 1 Expert (subtopics 1-4), Part 2 Simplifier (subtopics 5-7) in fresh
# bands. subtopics.json durations 200/230/220/210/190/190/190 of 1430 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ErrorCorrectionsPostClosingSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the full family, and the stock surplus
        title = Tex("Error Corrections and Post-Closing").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Eight adjustment tools — and one more:").scale(1.05).shift(UP * 1.2)
        b0_l2 = Tex("the trading stock SURPLUS").scale(1.05).shift(UP * 0.4)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Books say R10 700; shelves hold R10 745").scale(1.0).shift(DOWN * 0.5)
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_l4 = Tex("Debit Trading Stock R45; credit Surplus (income)").scale(0.95).shift(DOWN * 1.4)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2.5)
        b0_l5 = Tex("The count wins — but stock does not breed:").scale(0.95).shift(DOWN * 2.3)
        b0_l6 = Tex("book the surplus, then investigate").scale(0.95).shift(DOWN * 3.0)
        self.play(Write(b0_l5))
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_2): family one — wrong account
        self.next_band(1)
        b1_title = Tex("Error family 1: the wrong account").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = Tex("Advertising costs R320 posted to Stationery").scale(1.05).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = Tex("Trial balance never noticed — still level").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Debit Advertising R320; credit Stationery R320").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_l4 = Tex("Totals unchanged; the DETAIL now true").scale(1.0).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): family two — the omission
        self.next_band(2)
        b2_title = Tex("Error family 2: the omission").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = Tex("A credit sale of R600 never entered anywhere").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = Tex("Debit Debtors Control R600; credit Sales R600").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("And the cost pair at the mark-up:").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = Tex("Debit Cost of Sales R400; credit Stock R400").scale(1.0).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2.5)
        b2_l5 = Tex("An omission is corrected by DOING the entry").scale(1.0).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): family three — the wrong amount
        self.next_band(3)
        b3_title = Tex("Error family 3: the wrong amount").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"\text{Wages } 2\,700 \text{ entered as } 2\,070").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_wrong = Tex("Reverse everything and re-enter from scratch").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_l2 = MathTex(r"\text{Top up the DIFFERENCE: } 2\,700 - 2\,070 = 630").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex("Debit Wages R630; credit Bank R630").scale(1.05).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = Tex("The reconciliations caught it — not the TB").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): the post-adjustment trial balance format
        self.next_band(4)
        b4_title = Tex("Post-adjustment trial balance, in format").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        panel = Rectangle(width=11.0, height=4.2).shift(band_shift(4) + DOWN * 0.4)
        self.play(Create(panel))
        b4_r1 = Tex("Heading: business, document, date").scale(0.95).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_r1))
        self.wait(2)
        div = Line(LEFT * 5.5, RIGHT * 5.5).shift(band_shift(4) + UP * 0.6)
        self.play(Create(div))
        b4_r2 = Tex("Section 1 — balance sheet accounts:").scale(0.95).shift(band_shift(4) + UP * 0.1)
        b4_r3 = Tex("capital, assets, adjustment children, liabilities").scale(0.9).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4_r2))
        self.play(Write(b4_r3))
        self.wait(2.5)
        b4_r4 = Tex("Section 2 — nominal accounts, ADJUSTED:").scale(0.95).shift(band_shift(4) + DOWN * 1.3)
        b4_r5 = Tex("electricity at 12 months, insurance at 4").scale(0.9).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_r4))
        self.play(Write(b4_r5))
        self.wait(2.5)
        b4_l1 = Tex("Two columns; the totals must agree").scale(0.95).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l1))
        self.wait(3)

        # --- Band 5 (subtopic_3): the final accounts run, truer fuel
        self.next_band(5)
        b5_title = Tex("The final accounts, with adjusted inputs").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("Sales and Cost of Sales close to Trading:").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("gross profit").scale(1.05).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Incomes and adjusted expenses meet in").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        b5_l4 = Tex("Profit and Loss: net profit").scale(1.05).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex("Net profit transfers to Capital — same machine").scale(1.0).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): closing off; the post-closing trial balance
        self.next_band(6)
        b6_title = Tex("The post-closing trial balance").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Closing empties every nominal account to zero").scale(1.0).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = Tex("Drawings settles against Capital").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("What stands: assets, liabilities, updated Capital").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_wrong = Tex("Sales appearing on the post-closing list").scale(1.0).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(b6_wrong))
        self.play(Create(strike(b6_wrong)))
        self.wait(2)
        b6_l4 = Tex("Nominal on a post-closing TB = error by definition").scale(0.95).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("These balances open the new year").scale(1.0).shift(band_shift(6) + DOWN * 3.1)
        self.play(Write(b6_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the whole toolbox on one bench
        self.next_band(7)
        b7_title = Tex("The whole toolbox on one bench").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Counting tools: deficit (loss), surplus (gain —").scale(0.95).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("with the accountant's frown: shelves don't breed)").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Cupboard, wearing, four calendar tools,").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex("and the loan that grew by itself — nine tools").scale(0.95).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("One motion: report card takes the year's truth;").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        b7_l6 = Tex("the balance sheet holds the leftovers").scale(0.95).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(3)

        # --- Band 8 (subtopic_6): fixing the wrong-drawer mistakes
        self.next_band(8)
        b8_title = Tex("Fixing the wrong-drawer mistakes").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Wrong drawer: move R320, Stationery to Advertising").scale(0.92).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Still in the bag: unpack the R600 sale in full,").scale(0.95).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex("with its R400 cost pair").scale(0.95).shift(band_shift(8) + DOWN * 0.3)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("Folded wrong: add only the missing R630").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2.5)
        b8_l5 = Tex("Balance proves arithmetic;").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        b8_l6 = Tex("only checking proves truth").scale(0.95).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_7): the list that survives midnight
        self.next_band(9)
        b9_title = Tex("The list that survives midnight").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Story pages burn to zero — not lost, PROMOTED:").scale(0.95).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("the year compressed into Capital").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Owning continues; only earning starts fresh").scale(1.0).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("The surviving list, proven level: the").scale(1.0).shift(band_shift(9) + DOWN * 1.4)
        b9_l5 = Tex("post-closing trial balance — the equation itemised").scale(0.95).shift(band_shift(9) + DOWN * 2.2)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(2.5)
        b9_l6 = Tex("This ending position is next year's opening").scale(0.95).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l6))
        self.wait(4)
