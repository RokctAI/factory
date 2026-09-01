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
# "Accrued and Prepaid Incomes and Expenses". Add-only lifecycle, one band per
# teaching beat, camera moves down between bands. Covers all seven subtopics:
# Part 1 Expert (subtopics 1-4), Part 2 Simplifier (subtopics 5-7) in fresh
# bands. subtopics.json durations 210/220/230/200/180/190/190 of 1420 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AccruedPrepaidSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the timing problem as a two-by-two grid
        title = Tex("Accrued and Prepaid Items").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("This year's statement carries THIS year's").scale(1.0).shift(UP * 1.6)
        b0_l2 = Tex("incomes and expenses — whenever cash moved").scale(1.0).shift(UP * 0.9)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        vline = Line(UP * 0.4, DOWN * 2.9)
        hline = Line(LEFT * 5.6, RIGHT * 5.6).shift(DOWN * 1.25)
        self.play(Create(vline), Create(hline))
        g1 = Tex("Used, not paid:").scale(0.9).shift(DOWN * 0.1 + LEFT * 2.9)
        g1b = Tex("ACCRUED EXPENSE").scale(0.9).shift(DOWN * 0.75 + LEFT * 2.9)
        self.play(Write(g1), Write(g1b))
        self.wait(2)
        g2 = Tex("Paid, not used:").scale(0.9).shift(DOWN * 0.1 + RIGHT * 2.9)
        g2b = Tex("PREPAID EXPENSE").scale(0.9).shift(DOWN * 0.75 + RIGHT * 2.9)
        self.play(Write(g2), Write(g2b))
        self.wait(2)
        g3 = Tex("Earned, not received:").scale(0.9).shift(DOWN * 1.7 + LEFT * 2.9)
        g3b = Tex("ACCRUED INCOME").scale(0.9).shift(DOWN * 2.35 + LEFT * 2.9)
        self.play(Write(g3), Write(g3b))
        self.wait(2)
        g4 = Tex("Received, not earned:").scale(0.9).shift(DOWN * 1.7 + RIGHT * 2.9)
        g4b = Tex("IN ADVANCE").scale(0.9).shift(DOWN * 2.35 + RIGHT * 2.9)
        self.play(Write(g4), Write(g4b))
        self.wait(3)

        # --- Band 1 (subtopic_1): the two questions, and always the pair
        self.next_band(1)
        b1_title = Tex("Two questions sort every straddler").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = Tex("1. Whose year is it — this one or next?").scale(1.05).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = Tex("2. Has the cash moved yet?").scale(1.05).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("This year, cash not moved: accrue it in").scale(1.0).shift(band_shift(1) + DOWN * 0.6)
        b1_l4 = Tex("Next year, cash already moved: push it out").scale(1.0).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2.5)
        b1_l5 = Tex("Always a PAIR: statement correction").scale(1.0).shift(band_shift(1) + DOWN * 2.3)
        b1_l6 = Tex("+ balance-sheet creation").scale(1.0).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): the accrued expense, worked in full
        self.next_band(2)
        b2_title = Tex("Accrued expense: June's electricity").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = Tex("Ledger: 11 months paid, R2 640").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex("The year USED twelve months").scale(1.0).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"\text{Debit Water and electricity: } 2\,640 + 300 = 2\,940").scale(0.95).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex("Credit Accrued expenses R300").scale(1.0).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)
        b2_l5 = Tex("— a CURRENT LIABILITY: the business owes it").scale(1.0).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): the prepaid expense, worked in full
        self.next_band(3)
        b3_title = Tex("Prepaid expense: insurance paid ahead").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = Tex("Paid 1 March: R1 800 for twelve months").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"\text{Used Mar--Jun: } \tfrac{4}{12} \times 1\,800 = 600").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex("Credit Insurance R1 200 — expense stays at R600").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex("Debit Prepaid expenses R1 200 — a CURRENT ASSET").scale(0.95).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2.5)
        b3_l5 = Tex("Paid-for does not mean used-up").scale(1.0).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the income mirror, both corners
        self.next_band(4)
        b4_title = Tex("The income side — the mirror").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex("Tenant a month behind: rent earned = 12 months").scale(0.95).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"\text{Credit Rent income: } 6\,600 + 600 = 7\,200").scale(1.0).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("Debit Accrued income R600 — current ASSET").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = MathTex(r"\text{Paid ahead? } 7\,800 - 600 = 7\,200 \text{ earned}").scale(1.0).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = Tex("Credit Income received in advance — LIABILITY").scale(0.95).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): interest capitalised — the growing loan
        self.next_band(5)
        b5_title = Tex("Interest capitalised").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"\text{Loan R}15\,000 \text{ at } 10\%: \; 1\,500 \text{ interest}").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_wrong = Tex("No cash moved, so no entry needed").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_wrong))
        self.play(Create(strike(b5_wrong)))
        self.wait(2)
        b5_l2 = Tex("Debit Interest on loan R1 500 — this year's cost").scale(0.95).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"\text{Credit Loan: } 15\,000 + 1\,500 = 16\,500").scale(1.0).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex("Miss it: expense AND liability understated").scale(1.0).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): the five afterlives and the symmetry check
        self.next_band(6)
        b6_title = Tex("Balance-sheet afterlives").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Accrued expenses — current liability").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("Prepaid expenses, accrued income — current assets").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("Income in advance — current liability").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        b6_l4 = Tex("Interest capitalised — the loan grows").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("Check: profit and the equation move together —").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        b6_l6 = Tex("one without the other means half an entry").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the chalk line and the four corners
        self.next_band(7)
        b7_title = Tex("The year line and the four latecomers").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        yline = Line(LEFT * 4.5, RIGHT * 4.5).shift(band_shift(7) + UP * 1.2)
        b7_lab = Tex("midnight, last day of June").scale(0.9).shift(band_shift(7) + UP * 0.7)
        self.play(Create(yline))
        self.play(Write(b7_lab))
        self.wait(2.5)
        b7_l1 = Tex("Money refuses to respect the line").scale(1.0).shift(band_shift(7) + DOWN * 0.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("Ask: paying or collecting? Money before").scale(1.0).shift(band_shift(7) + DOWN * 1.0)
        b7_l3 = Tex("or after the work it belongs to?").scale(1.0).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l2))
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex("Report card takes the year; loose ends to the").scale(0.95).shift(band_shift(7) + DOWN * 2.6)
        b7_l5 = Tex("balance sheet").scale(0.95).shift(band_shift(7) + DOWN * 3.2)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): the sticky note and the parcel
        self.next_band(8)
        b8_title = Tex("Bills still coming, cover paid ahead").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("June's heaters ran in June —").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("charge the year R2 940; sticky note: owe R300").scale(0.95).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Insurance: only four months used by the line").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("Charge R600; parcel on the shelf: R1 200 stored").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2.5)
        b8_l5 = Tex("One corner leaves a debt, the other a parcel").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_7): rent behind, rent ahead, the quiet loan
        self.next_band(9)
        b9_title = Tex("Rent owed, rent ahead, the quiet loan").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"\text{Month behind: earned } 6\,600 + 600 = 7\,200").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("The missing R600: an IOU in the shop's favour").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Month ahead: money in hand, still a liability —").scale(0.95).shift(band_shift(9) + DOWN * 0.5)
        b9_l4 = Tex("the tenant holds the claim").scale(0.95).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = MathTex(r"\text{Lay-by loan: } 15\,000 + 1\,500 = 16\,500").scale(1.0).shift(band_shift(9) + DOWN * 2.2)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(2)
        b9_l6 = Tex("No cash, no slip — only the loan statement, larger").scale(0.9).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l6))
        self.wait(4)
