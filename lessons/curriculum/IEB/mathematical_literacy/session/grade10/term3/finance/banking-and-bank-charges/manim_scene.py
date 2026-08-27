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

# Band-layout whiteboard scene for the Banking and Bank Charges session duo.
# One band per teaching beat, camera moves down between bands, nothing is ever
# removed. Only exporter-supported mobjects (Tex/MathTex/Line/Arrow/Dot/
# Rectangle/SurroundingRectangle); every line of working is its own
# single-string Tex/MathTex revealed with Write. Band time is apportioned to
# subtopics.json (210/220/230/270/180/185/185 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BankingAndBankChargesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the language of banking — accounts ---
        title = Tex("Banking and Bank Charges").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_h = Tex("Types of account").scale(1.1).shift(UP * 1.4)
        self.play(Write(b0_h))
        self.wait(1.5)
        b0_l1 = Tex("Savings: safe keeping, small interest").scale(1.1).shift(UP * 0.5)
        b0_l2 = Tex("Current (cheque): constant flow, higher fees").scale(1.1).shift(DOWN * 0.4)
        b0_l3 = Tex("Fixed deposit: locked lump sum, better rate").scale(1.1).shift(DOWN * 1.3)
        b0_l4 = Tex("Credit: spend the bank's money, repay later").scale(1.1).shift(DOWN * 2.2)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): movements of money, debit vs credit ---
        self.next_band(1)
        b1_t = Tex("Movements of money").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("Deposit: money IN \\quad Withdrawal: money OUT").scale(1.1).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("EFT: money moves without cash").scale(1.1).shift(band_shift(1) + UP * 0.2)
        b1_l3 = Tex("Debit order: a company collects a regular payment").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_rule = Tex("On the statement: debit = out, credit = in").scale(1.1).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_rule))
        self.play(Create(SurroundingRectangle(b1_rule, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the PayPerUse fee table ---
        self.next_band(2)
        b2_t = Tex("PayPerUse fee table").scale(1.2).shift(band_shift(2) + UP * 2.6)
        self.play(Write(b2_t))
        self.wait(1.5)
        table = Rectangle(width=10.6, height=3.6).shift(band_shift(2) + UP * 0.1)
        self.play(Create(table))
        r1 = Line(LEFT * 5.3, RIGHT * 5.3).shift(band_shift(2) + UP * 1.0)
        r2 = Line(LEFT * 5.3, RIGHT * 5.3).shift(band_shift(2) + UP * 0.1)
        r3 = Line(LEFT * 5.3, RIGHT * 5.3).shift(band_shift(2) + DOWN * 0.8)
        vline = Line(UP * 1.9, DOWN * 1.7).shift(band_shift(2) + RIGHT * 2.2)
        self.play(Create(r1), Create(r2), Create(r3), Create(vline))
        self.wait(1)
        c1 = Tex("Monthly admin fee").scale(0.95).shift(band_shift(2) + UP * 1.45 + LEFT * 2.6)
        p1 = Tex("R5,00").scale(0.95).shift(band_shift(2) + UP * 1.45 + RIGHT * 3.6)
        self.play(Write(c1), Write(p1))
        self.wait(1.5)
        c2 = Tex("ATM withdrawal").scale(0.95).shift(band_shift(2) + UP * 0.55 + LEFT * 2.8)
        p2 = Tex("R2,50 + R1,20/R100").scale(0.85).shift(band_shift(2) + UP * 0.55 + RIGHT * 3.6)
        self.play(Write(c2), Write(p2))
        self.wait(1.5)
        c3 = Tex("Cashback at the till").scale(0.95).shift(band_shift(2) + DOWN * 0.35 + LEFT * 2.55)
        p3 = Tex("R2,00").scale(0.95).shift(band_shift(2) + DOWN * 0.35 + RIGHT * 3.6)
        self.play(Write(c3), Write(p3))
        self.wait(1.5)
        c4 = Tex("Branch counter").scale(0.95).shift(band_shift(2) + DOWN * 1.25 + LEFT * 2.85)
        p4 = Tex("R60,00").scale(0.95).shift(band_shift(2) + DOWN * 1.25 + RIGHT * 3.6)
        self.play(Write(c4), Write(p4))
        self.wait(2)
        b2_note = Tex("ATM rate: per R100 OR PART THEREOF").scale(1.0).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_note))
        self.wait(3)

        # --- Band 3 (subtopic_2): ATM fee worked, part-thereof trap ---
        self.next_band(3)
        b3_t = Tex("What a withdrawal really costs").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{R400: } \text{R}2{,}50 + 4 \times \text{R}1{,}20 = \text{R}7{,}30").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"\text{R1 000: } \text{R}2{,}50 + 10 \times \text{R}1{,}20 = \text{R}14{,}50").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_wrong = MathTex(r"\text{R350: } \text{R}2{,}50 + 3{,}5 \times \text{R}1{,}20 = \text{R}6{,}70").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_l3 = Tex("A part counts as a WHOLE: R350 = 4 hundreds").scale(1.05).shift(band_shift(3) + DOWN * 1.7)
        b3_l4 = MathTex(r"\text{R}2{,}50 + 4 \times \text{R}1{,}20 = \text{R}7{,}30").scale(1.1).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_2): same R400, three channels ---
        self.next_band(4)
        b4_t = Tex("Same R400 — three different prices").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("Cashback at the till: R2,00").scale(1.1).shift(band_shift(4) + UP * 1.0)
        b4_l2 = Tex("Own ATM: R7,30").scale(1.1).shift(band_shift(4) + UP * 0.1)
        b4_l3 = Tex("Branch counter: R60,00").scale(1.1).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_rule = Tex("Choosing the cheap channel saves thousands a year").scale(1.0).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_rule))
        self.wait(3)

        # --- Band 5 (subtopic_3): quiet month head to head ---
        self.next_band(5)
        b5_t = Tex("Quiet month: 5 withdrawals of R400").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"\text{PayPerUse: } 5 \times \text{R}7{,}30 = \text{R}36{,}50").scale(1.1).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"\text{R}36{,}50 + \text{R}5{,}00 = \text{R}41{,}50").scale(1.1).shift(band_shift(5) + UP * 0.2)
        b5_l3 = Tex("AllInOne: R48,00 flat").scale(1.1).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2.5)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_ans = Tex("PayPerUse wins by R6,50 this month").scale(1.1).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_ans))
        self.play(Create(SurroundingRectangle(b5_ans, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_3): busy month and break-even ---
        self.next_band(6)
        b6_t = Tex("Busy month: 10 withdrawals of R1 000").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"10 \times \text{R}14{,}50 + \text{R}5{,}00 = \text{R}150{,}00").scale(1.1).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("AllInOne still R48,00 — wins by R102").scale(1.05).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"5 \text{ withdrawals: } \text{R}5 + \text{R}36{,}50 = \text{R}41{,}50").scale(0.95).shift(band_shift(6) + DOWN * 0.8)
        b6_l4 = MathTex(r"6 \text{ withdrawals: } \text{R}5 + \text{R}43{,}80 = \text{R}48{,}80").scale(0.95).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_ans = Tex("5 or fewer: PayPerUse; 6 or more: AllInOne").scale(1.05).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_ans))
        self.play(Create(SurroundingRectangle(b6_ans, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the fee graph ---
        self.next_band(7)
        b7_t = Tex("The fee graph").scale(1.2).shift(band_shift(7) + UP * 2.6)
        self.play(Write(b7_t))
        self.wait(1.5)
        origin = band_shift(7) + DOWN * 2.2 + LEFT * 4.5
        x_ax = Arrow(origin, origin + RIGHT * 8.6, buff=0, stroke_width=4)
        y_ax = Arrow(origin, origin + UP * 4.4, buff=0, stroke_width=4)
        self.play(Create(x_ax), Create(y_ax))
        x_lab = Tex("withdrawals").scale(0.8).shift(origin + RIGHT * 7.3 + DOWN * 0.5)
        y_lab = Tex("cost (R)").scale(0.8).shift(origin + UP * 4.1 + RIGHT * 1.2)
        self.play(Write(x_lab), Write(y_lab))
        self.wait(1.5)
        allin_line = Line(origin + UP * 2.6, origin + UP * 2.6 + RIGHT * 7.8, color=BLUE, stroke_width=5)
        allin_lab = Tex("AllInOne: flat R48").scale(0.85).shift(origin + UP * 3.1 + RIGHT * 6.0)
        self.play(Create(allin_line), Write(allin_lab))
        self.wait(2)
        ppu_line = Line(origin + UP * 0.3, origin + UP * 3.9 + RIGHT * 7.2, color=YELLOW, stroke_width=5)
        ppu_lab = Tex("PayPerUse: starts at R5,00, +R7,30 each").scale(0.85).shift(origin + UP * 1.4 + RIGHT * 4.9)
        self.play(Create(ppu_line), Write(ppu_lab))
        self.wait(2)
        cross = Dot(origin + UP * 2.6 + RIGHT * 4.6, color=RED)
        cross_lab = Tex("break-even").scale(0.85).shift(origin + UP * 2.2 + RIGHT * 4.6)
        self.play(Create(cross), Write(cross_lab))
        self.wait(3)

        # --- Band 8 (subtopic_4): the five-step method ---
        self.next_band(8)
        b8_t = Tex("Method for any charges question").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(1.5)
        b8_l1 = Tex("1. Classify each fee: flat, fixed + rate, \\%").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("2. Count the R100s — round parts UP").scale(1.0).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex("3. Total the month; never forget the admin fee").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        b8_l4 = Tex("4. Compare accounts on the SAME month of use").scale(1.0).shift(band_shift(8) + DOWN * 1.6)
        b8_l5 = Tex("5. Step transactions up to find the crossing").scale(1.0).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(2)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): the bank is a shop ---
        self.next_band(9)
        b9_t = Tex("The bank is a shop that sells services").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Locker rental (admin fee): R5,00").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("Cash from the machine: R2,50 + R1,20 per R100").scale(1.05).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex("Cash from a human (deluxe): R60,00").scale(1.05).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("The prices are on the menu — read it").scale(1.05).shift(band_shift(9) + DOWN * 1.7)
        b9_l5 = Tex("Debit column: out \\quad Credit column: in").scale(1.05).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l4))
        self.wait(2)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_6): small fees eat big money ---
        self.next_band(10)
        b10_t = Tex("One R400 note, three doors").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Till: R2,00 \\quad ATM: R7,30 \\quad Counter: R60,00").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"\text{Year at the till: } 52 \times \text{R}2{,}00 = \text{R}104").scale(1.05).shift(band_shift(10) + UP * 0.1)
        b10_l3 = MathTex(r"\text{Year at the counter: } 52 \times \text{R}60 = \text{R}3\;120").scale(1.01).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l2))
        self.wait(2.5)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_ans = Tex("Same cash, same year — only the door changed").scale(1.0).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_ans))
        self.play(Create(SurroundingRectangle(b10_ans, color=GREEN)))
        b10_l4 = Tex("R350? The machine sees 4 hundreds, fee R7,30").scale(0.95).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l4))
        self.wait(3)

        # --- Band 11 (subtopic_7): flat rate or pay-as-you-go ---
        self.next_band(11)
        b11_t = Tex("Flat rate or pay-as-you-go?").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(2)
        b11_l1 = Tex("Like airtime: bundles suit heavy users only").scale(1.05).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = MathTex(r"\text{Quiet: R41,50} < \text{R48} \to \text{pay-as-you-go}").scale(0.9).shift(band_shift(11) + UP * 0.1)
        b11_l3 = MathTex(r"\text{Busy: R150,00} > \text{R48} \to \text{bundle}").scale(0.9).shift(band_shift(11) + DOWN * 0.9)
        self.play(Write(b11_l2))
        self.wait(2.5)
        self.play(Write(b11_l3))
        self.wait(2.5)
        b11_ans = Tex("Count up until the totals swap: the flip is at 6").scale(1.0).shift(band_shift(11) + DOWN * 1.9)
        self.play(Write(b11_ans))
        self.play(Create(SurroundingRectangle(b11_ans, color=GREEN)))
        b11_l4 = Tex("Re-check the pattern once a year").scale(1.0).shift(band_shift(11) + DOWN * 2.9)
        self.play(Write(b11_l4))
        self.wait(4)
