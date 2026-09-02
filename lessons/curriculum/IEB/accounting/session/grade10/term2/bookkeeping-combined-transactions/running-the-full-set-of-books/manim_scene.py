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

# Band-layout whiteboard scene for "Running the Full Set of Books"
# (grade10 term2, bookkeeping-combined-transactions). One band per teaching
# beat, add-only lifecycle, camera moves down between bands. Exporter-safe
# mobjects only (Tex/MathTex/Line/Rectangle/SurroundingRectangle/VGroup).
#
# Subtopic time shares (subtopics.json, total 1380 s):
# 200/220/210/200/180/190/180 -> bands 0-1 / 2-3 / 4-5 / 6-7 / 8 / 9 / 10.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RunningTheFullSetOfBooksSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): six journals, one system ---
        title = Tex("Six Journals, One System").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Two questions route every transaction:").scale(1.05).shift(UP * 1.2)
        b0_l2 = Tex("did MONEY move, and which DIRECTION?").scale(1.05).shift(UP * 0.4)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex(r"Money in $\Rightarrow$ CRJ; money out $\Rightarrow$ CPJ").scale(0.98).shift(DOWN * 0.5)
        b0_l4 = Tex(r"Credit sale $\Rightarrow$ DJ; credit purchase $\Rightarrow$ CJ").scale(0.9).shift(DOWN * 1.4)
        b0_l5 = Tex(r"Returns $\Rightarrow$ DAJ / CAJ").scale(1.05).shift(DOWN * 2.2)
        b0_l6 = Tex(r"No money, no goods $\Rightarrow$ General Journal").scale(1.0).shift(DOWN * 3.0)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2)
        self.play(Write(b0_l5))
        self.wait(1.5)
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_1): the new columns, and the Sales trap ---
        self.next_band(1)
        b1_title = Tex("The new control columns").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"R2 400 from a debtor $\Rightarrow$ CRJ,").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("Debtors Control column + the debtor's page").scale(1.0).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_w = Tex("Receipt from a debtor touches Sales?").scale(1.0).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_w))
        self.play(Create(strike(b1_w)))
        self.wait(2)
        b1_l3 = Tex("The sale was recorded the day the goods").scale(1.0).shift(band_shift(1) + DOWN * 1.6)
        b1_l4 = Tex("left -- the receipt settles the DEBT").scale(1.0).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): Zanele's month, days 1-11 ---
        self.next_band(2)
        b2_title = Tex("Zanele's Traders -- the month begins").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"1st: capital R30 000 $\Rightarrow$ CRJ sundries").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex(r"3rd: stock on credit, Bayside R12 000 $\Rightarrow$ CJ").scale(0.9).shift(band_shift(2) + UP * 0.4)
        b2_l3 = Tex(r"6th: cash sales R9 000, CoS R6 000 $\Rightarrow$ CRJ").scale(0.95).shift(band_shift(2) + DOWN * 0.4)
        b2_l4 = Tex(r"9th: credit sale Mokoena R4 500, CoS R3 000 $\Rightarrow$ DJ").scale(0.85).shift(band_shift(2) + DOWN * 1.2)
        b2_l5 = Tex(r"11th: rent paid R4 000 $\Rightarrow$ CPJ sundries").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        self.play(Write(b2_l5))
        self.wait(2)
        b2_l6 = Tex("Mark-up 50\\% on cost: R6 000 sells for R9 000").scale(0.95).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): days 13-29 ---
        self.next_band(3)
        b3_title = Tex("The month, continued").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"13th: Mokoena returns R900, CoS R600 $\Rightarrow$ DAJ").scale(0.9).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"16th: Mokoena pays R2 400 $\Rightarrow$ CRJ Debtors col").scale(0.9).shift(band_shift(3) + UP * 0.4)
        b3_l3 = Tex(r"19th: paid Bayside R7 000 $\Rightarrow$ CPJ Creditors").scale(0.95).shift(band_shift(3) + DOWN * 0.4)
        b3_l4 = Tex(r"21st: return to Bayside R1 000 $\Rightarrow$ CAJ").scale(1.0).shift(band_shift(3) + DOWN * 1.2)
        b3_l5 = Tex(r"26th: wages R2 200 $\Rightarrow$ CPJ Wages column").scale(0.95).shift(band_shift(3) + DOWN * 2.0)
        b3_l6 = Tex(r"29th: Khumalo's R400 written off $\Rightarrow$ GJ").scale(0.95).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(1.5)
        self.play(Write(b3_l4))
        self.wait(1.5)
        self.play(Write(b3_l5))
        self.wait(1.5)
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): posting and the balances ---
        self.next_band(4)
        b4_title = Tex("Post the month, balance the accounts").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{Bank: } 41\,400 - 13\,200 = \text{R28 200 Dr}").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex("Trading Stock: R2 600 Dr").scale(1.0).shift(band_shift(4) + UP * 0.5)
        b4_l3 = Tex("Debtors Control: R1 200 Dr = Mokoena's page").scale(0.95).shift(band_shift(4) + DOWN * 0.2)
        b4_l4 = Tex("Creditors Control: R4 000 Cr = Bayside's page").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        b4_l5 = Tex("Capital R30 400 Cr; Sales R13 500 Cr").scale(1.0).shift(band_shift(4) + DOWN * 1.6)
        b4_l6 = Tex("CoS 8 400, Rent 4 000, Wages 2 200,").scale(1.0).shift(band_shift(4) + DOWN * 2.4)
        b4_l7 = Tex("Bad Debts 400 -- all debits").scale(1.0).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(1.5)
        self.play(Write(b4_l3))
        self.wait(1.5)
        self.play(Write(b4_l4))
        self.wait(1.5)
        self.play(Write(b4_l5))
        self.wait(1.5)
        self.play(Write(b4_l6))
        self.play(Write(b4_l7))
        self.wait(3)

        # --- Band 5 (subtopic_3): the trial balance grid ---
        self.next_band(5)
        b5_title = Tex("Trial balance").scale(1.2).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_frame = Rectangle(width=7.0, height=3.6).shift(band_shift(5) + UP * 0.1)
        b5_mid = Line(UP * 1.9, DOWN * 1.7).shift(band_shift(5))
        self.play(Create(b5_frame))
        self.play(Create(b5_mid))
        b5_hd = Tex("Debits").scale(1.05).shift(band_shift(5) + UP * 1.5 + LEFT * 1.8)
        b5_hc = Tex("Credits").scale(1.05).shift(band_shift(5) + UP * 1.5 + RIGHT * 1.8)
        self.play(Write(b5_hd))
        self.play(Write(b5_hc))
        self.wait(1.5)
        b5_d1 = Tex("28 200 + 2 600 + 1 200").scale(0.85).shift(band_shift(5) + UP * 0.7 + LEFT * 1.8)
        b5_d2 = Tex("+ 900 + 8 400 + 4 000").scale(0.85).shift(band_shift(5) + LEFT * 1.8)
        b5_d3 = Tex("+ 2 200 + 400").scale(0.85).shift(band_shift(5) + DOWN * 0.7 + LEFT * 1.8)
        self.play(Write(b5_d1))
        self.play(Write(b5_d2))
        self.play(Write(b5_d3))
        self.wait(2)
        b5_c1 = Tex("30 400 + 13 500").scale(0.9).shift(band_shift(5) + UP * 0.7 + RIGHT * 1.8)
        b5_c2 = Tex("+ 4 000").scale(0.9).shift(band_shift(5) + RIGHT * 1.8)
        self.play(Write(b5_c1))
        self.play(Write(b5_c2))
        self.wait(2)
        b5_rule = Line(LEFT * 3.5, RIGHT * 3.5).shift(band_shift(5) + DOWN * 1.1)
        self.play(Create(b5_rule))
        b5_td = Tex("R47 900").scale(1.0).shift(band_shift(5) + DOWN * 1.4 + LEFT * 1.8)
        b5_tc = Tex("R47 900").scale(1.0).shift(band_shift(5) + DOWN * 1.4 + RIGHT * 1.8)
        self.play(Write(b5_td))
        self.play(Write(b5_tc))
        self.wait(2)
        b5_ans = Tex("R47 900 = R47 900 -- level").scale(1.05).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_ans))
        self.play(Create(SurroundingRectangle(b5_ans, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the control web ---
        self.next_band(6)
        b6_title = Tex("The control web around the month").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Cash: banked daily, intact; reconciled").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("Stock: R2 600 is a claim a count can test").scale(1.0).shift(band_shift(6) + UP * 0.3)
        b6_l3 = Tex("Debtors: limits, statements, follow-up").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex("Creditors: invoice matched to order and").scale(1.0).shift(band_shift(6) + DOWN * 1.3)
        b6_l5 = Tex("delivery note; numbered debit note").scale(1.0).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(2)
        b6_l6 = Tex("Write-off only after documented follow-up").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): the ethics thread ---
        self.next_band(7)
        b7_title = Tex("The ethics thread").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Narrated write-off = accountability:").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("visible, dated, explained").scale(1.05).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Intact daily banking = transparency:").scale(1.05).shift(band_shift(7) + DOWN * 0.6)
        b7_l4 = Tex("records and cash agree for any reader").scale(1.05).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("Integrated answers: weakness, risk,").scale(1.05).shift(band_shift(7) + DOWN * 2.3)
        b7_l6 = Tex("recommendation, principle").scale(1.05).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(VGroup(b7_l5, b7_l6), color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): eleven slips, six doors ---
        self.next_band(8)
        b8_title = Tex("Eleven slips, six doors").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Money in? $\Rightarrow$ CRJ. Money out? $\Rightarrow$ CPJ").scale(0.95).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex(r"Trust out? $\Rightarrow$ DJ. Trust in? $\Rightarrow$ CJ").scale(1.0).shift(band_shift(8) + UP * 0.3)
        b8_l3 = Tex(r"Coming back? $\Rightarrow$ DAJ / CAJ. Else $\Rightarrow$ GJ").scale(0.95).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_w = Tex("Mokoena's R2 400 = a new sale?").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_w))
        self.play(Create(strike(b8_w)))
        self.wait(1.5)
        b8_ok = Tex("It settles his page -- never the Sales lane").scale(0.95).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_ok))
        self.play(Create(SurroundingRectangle(b8_ok, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): pages, big accounts, the weigh-in ---
        self.next_band(9)
        b9_title = Tex("The month that used everything").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"\text{Mokoena: } 4\,500 - 900 - 2\,400 = \text{R1 200}").scale(0.95).shift(band_shift(9) + UP * 1.2)
        b9_l2 = MathTex(r"\text{Bayside: } 12\,000 - 1\,000 - 7\,000 = \text{R4 000}").scale(0.95).shift(band_shift(9) + UP * 0.4)
        b9_l3 = MathTex(r"\text{Bank: } 41\,400 - 13\,200 = \text{R28 200}").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        b9_l4 = Tex("Shelf claim: R2 600 of goods, checkable").scale(1.0).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("Left 47 900 = Right 47 900 -- level:").scale(1.05).shift(band_shift(9) + DOWN * 2.1)
        b9_l6 = Tex("not one rand lost or invented").scale(1.05).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(VGroup(b9_l5, b9_l6), color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the owner's Friday walk ---
        self.next_band(10)
        b10_title = Tex("The owner's Friday walk").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("1. Till vs analysis column -- then bank it").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("2. Shelf vs the stock account's R2 600").scale(1.0).shift(band_shift(10) + UP * 0.3)
        b10_l3 = Tex("3. Debtors list: old debts, near limits").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        b10_l4 = Tex("4. Bayside's statement vs page: R4 000").scale(1.0).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l1))
        self.wait(2)
        self.play(Write(b10_l2))
        self.wait(2)
        self.play(Write(b10_l3))
        self.wait(2)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("Records first, control second,").scale(1.05).shift(band_shift(10) + DOWN * 2.2)
        b10_l6 = Tex("trust throughout").scale(1.05).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(VGroup(b10_l5, b10_l6), color=GREEN)))
        self.wait(4)
