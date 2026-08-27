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

# Band-layout whiteboard scene for "Deductions, Contributions and the Payroll
# Journals" (grade10 term2, salaries-and-wages). One band per teaching beat,
# add-only lifecycle, camera moves down between bands. Exporter-safe mobjects
# only (Tex/MathTex/Line/Rectangle/SurroundingRectangle/VGroup).
#
# Subtopic time shares (subtopics.json, total 1400 s):
# 220/210/220/200/180/190/180 -> bands 0-1 / 2-3 / 4-5 / 6 / 7 / 8 / 9.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PayrollJournalsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the five deductions ---
        title = Tex("Deductions and the Payroll Journals").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Deduction: taken OUT of gross --").scale(1.05).shift(UP * 1.2)
        b0_l2 = Tex("the employee's money, redirected").scale(1.05).shift(UP * 0.4)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("PAYE: tax, by SARS tables").scale(1.0).shift(DOWN * 0.5)
        b0_l4 = Tex("Pension 7,5\\% of gross; UIF 1\\%").scale(1.0).shift(DOWN * 1.3)
        b0_l5 = Tex("Medical aid: fixed rands; union: fixed fee").scale(1.0).shift(DOWN * 2.1)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2)
        self.play(Write(b0_l5))
        self.wait(2)
        b0_l6 = Tex("Percentage bases vs fixed amounts -- apart!").scale(0.95).shift(DOWN * 3.0)
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_1): the administrator's run, gross to net ---
        self.next_band(1)
        b1_title = Tex("The administrator's month").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Gross: R8 800").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("PAYE 1 100; pension 660; UIF 88").scale(1.05).shift(band_shift(1) + UP * 0.4)
        b1_l3 = Tex("medical 450; union 60").scale(1.05).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_m1 = MathTex(r"1\,100 + 660 + 88 + 450 + 60 = 2\,358").scale(1.05).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(b1_m1))
        self.wait(2)
        b1_m2 = MathTex(r"\text{Net} = 8\,800 - 2\,358 = \text{R6 442}").scale(1.1).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1_m2))
        self.play(Create(SurroundingRectangle(b1_m2, color=GREEN)))
        self.wait(2)
        b1_l4 = Tex("Earned, received, redirected -- three words").scale(0.95).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the employer's contributions ---
        self.next_band(2)
        b2_title = Tex("What the employer adds").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Contribution: the EMPLOYER pays, on top --").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("it never shrinks net pay").scale(1.05).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("Pension rand-for-rand: R660; UIF: R88").scale(1.0).shift(band_shift(2) + DOWN * 0.5)
        b2_l4 = Tex("Medical: R450; SDL 1\\%: R88 -- employer only").scale(0.95).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_m1 = MathTex(r"660 + 88 + 450 + 88 = \text{R1 286}").scale(1.1).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2_m1))
        self.play(Create(SurroundingRectangle(b2_m1, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): total cost of employment ---
        self.next_band(3)
        b3_title = Tex("The total cost of employing her").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_w = Tex("Total cost = the net R6 442?").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_w))
        self.play(Create(strike(b3_w)))
        self.wait(2)
        b3_m1 = MathTex(r"8\,800 + 1\,286 = \text{R10 086}").scale(1.15).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_m1))
        self.play(Create(SurroundingRectangle(b3_m1, color=GREEN)))
        self.wait(2.5)
        b3_l1 = Tex("She sees R6 442; the business pays").scale(1.05).shift(band_shift(3) + DOWN * 0.9)
        b3_l2 = Tex("R10 086 in her name").scale(1.05).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex("Test: reduces pay? Deduction.").scale(1.05).shift(band_shift(3) + DOWN * 2.5)
        b3_l4 = Tex("Employer's extra on top? Contribution.").scale(1.05).shift(band_shift(3) + DOWN * 3.2)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): the Salaries Journal row ---
        self.next_band(4)
        b4_title = Tex("The Salaries Journal row").scale(1.2).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_frame = Rectangle(width=7.2, height=2.0).shift(band_shift(4) + UP * 0.8)
        self.play(Create(b4_frame))
        b4_v1 = Line(UP * 1.8, DOWN * 0.2).shift(band_shift(4) + LEFT * 1.8)
        b4_v2 = Line(UP * 1.8, DOWN * 0.2).shift(band_shift(4))
        b4_v3 = Line(UP * 1.8, DOWN * 0.2).shift(band_shift(4) + RIGHT * 1.8)
        self.play(Create(b4_v1), Create(b4_v2), Create(b4_v3))
        b4_h1 = Tex("Gross").scale(0.85).shift(band_shift(4) + UP * 1.35 + LEFT * 2.7)
        b4_h2 = Tex("Deduct.").scale(0.85).shift(band_shift(4) + UP * 1.35 + LEFT * 0.9)
        b4_h3 = Tex("Net").scale(0.85).shift(band_shift(4) + UP * 1.35 + RIGHT * 0.9)
        b4_h4 = Tex("Contrib.").scale(0.85).shift(band_shift(4) + UP * 1.35 + RIGHT * 2.7)
        self.play(Write(b4_h1), Write(b4_h2), Write(b4_h3), Write(b4_h4))
        self.wait(1.5)
        b4_c1 = Tex("8 800").scale(0.9).shift(band_shift(4) + UP * 0.35 + LEFT * 2.7)
        b4_c2 = Tex("2 358").scale(0.9).shift(band_shift(4) + UP * 0.35 + LEFT * 0.9)
        b4_c3 = Tex("6 442").scale(0.9).shift(band_shift(4) + UP * 0.35 + RIGHT * 0.9)
        b4_c4 = Tex("1 286").scale(0.9).shift(band_shift(4) + UP * 0.35 + RIGHT * 2.7)
        self.play(Write(b4_c1))
        self.play(Write(b4_c2))
        self.play(Write(b4_c3))
        self.play(Write(b4_c4))
        self.wait(2)
        b4_l1 = Tex("Deduction columns: PAYE 1 100, pension 660,").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        b4_l2 = Tex("UIF 88, medical 450, union 60").scale(0.95).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex("Contribution columns: 660, 88, 450, SDL 88").scale(0.95).shift(band_shift(4) + DOWN * 2.4)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex("WJ, weekly: Dlamini 2 040; net 1 815,60").scale(0.95).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): the double entry and the settlements ---
        self.next_band(5)
        b5_title = Tex("The double entry, reasoned").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Debit Salaries with GROSS: 8 800").scale(1.05).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("Credit Bank with NET: 6 442 (CPJ)").scale(1.05).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("Credit each fund as a creditor: SARS,").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex("pension fund, UIF, medical, union").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("Contributions: debit expense, credit fund").scale(1.0).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l5))
        self.wait(2)
        b5_l6 = Tex("Settle by CPJ: SARS gets PAYE + SDL;").scale(1.0).shift(band_shift(5) + DOWN * 2.8)
        b5_l7 = Tex("pension carries both halves: 660 + 660").scale(1.0).shift(band_shift(5) + DOWN * 3.5)
        self.play(Write(b5_l6))
        self.play(Write(b5_l7))
        self.wait(3)

        # --- Band 6 (subtopic_4): ethics on the payroll ---
        self.next_band(6)
        b6_title = Tex("Ethics on the payroll").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("The CONTRACT: every figure authorised").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("on paper -- hours, rate, deductions").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("NEPOTISM: a name earning outside the").scale(1.0).shift(band_shift(6) + DOWN * 0.4)
        b6_l4 = Tex("scale -- competence and faith both lost").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("Pay must MATCH responsibility --").scale(1.0).shift(band_shift(6) + DOWN * 2.0)
        b6_l6 = Tex("books can balance while practice cannot").scale(1.0).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(2)
        b6_l7 = Tex("The UNION: deduct faithfully, pay promptly").scale(0.95).shift(band_shift(6) + DOWN * 3.5)
        self.play(Write(b6_l7))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the envelope that shrinks ---
        self.next_band(7)
        b7_title = Tex("The envelope that shrinks").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("In the envelope: R8 800 earned").scale(1.05).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("Tax man: 1 100. Retirement jar: 660.").scale(1.0).shift(band_shift(7) + UP * 0.4)
        b7_l3 = Tex("Just-in-case: 88. Doctor cover: 450.").scale(1.0).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex("The voice (union): 60.").scale(1.0).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_m = Tex("Arrives holding R6 442").scale(1.1).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_m))
        self.play(Create(SurroundingRectangle(b7_m, color=GREEN)))
        self.wait(2)
        b7_l5 = Tex("Nothing taken -- YOUR money, sent ahead").scale(1.0).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): the boss's second envelope ---
        self.next_band(8)
        b8_title = Tex("The boss's second envelope").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Not one rand of it comes out of yours:").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("660 retirement + 88 insurance").scale(1.0).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex("+ 450 medical + 88 skills levy").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.wait(2)
        b8_m1 = MathTex(r"\text{Second envelope} = \text{R1 286}").scale(1.05).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_m1))
        self.wait(2)
        b8_m2 = MathTex(r"\text{True cost} = 8\,800 + 1\,286 = \text{R10 086}").scale(1.05).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_m2))
        self.play(Create(SurroundingRectangle(b8_m2, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex("Deductions shrink yours; contributions").scale(1.0).shift(band_shift(8) + DOWN * 3.0)
        b8_l5 = Tex("are extra -- keep the envelopes apart").scale(1.0).shift(band_shift(8) + DOWN * 3.7)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_7): fair deals on payday ---
        self.next_band(9)
        b9_title = Tex("Fair deals on payday").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Paper remembers: the written deal is").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("your case when the envelope is light").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("The cousin problem poisons the ladder --").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        b9_l4 = Tex("the shop pays twice for nepotism").scale(1.0).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("Same work, same scale -- balancing is").scale(1.0).shift(band_shift(9) + DOWN * 2.2)
        b9_l6 = Tex("not the same as being right").scale(1.0).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(4)
