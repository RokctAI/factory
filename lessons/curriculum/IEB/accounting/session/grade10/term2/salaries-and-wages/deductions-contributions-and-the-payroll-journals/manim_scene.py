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
        title = Tex("From Gross to Net").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("PAYE: SARS tables, to SARS monthly").scale(1.0).shift(UP * 1.2)
        b0_l2 = Tex("Pension: 7,5\\% of gross, own saving").scale(1.0).shift(UP * 0.4)
        b0_l3 = Tex("UIF: 1\\% of gross, job-loss cover").scale(1.0).shift(DOWN * 0.4)
        b0_l4 = Tex("Medical: fixed share of membership").scale(1.0).shift(DOWN * 1.2)
        b0_l5 = Tex("Union: fixed subscription").scale(1.0).shift(DOWN * 2.0)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(1.5)
        self.play(Write(b0_l5))
        self.wait(2)
        b0_l6 = Tex("Each one: the EMPLOYEE'S money, redirected").scale(0.95).shift(DOWN * 2.9)
        self.play(Write(b0_l6))
        self.play(Create(SurroundingRectangle(b0_l6, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the administrator's run, gross to net ---
        self.next_band(1)
        b1_title = Tex("The administrator's month").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Gross: R11 000").scale(1.05).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(1.5)
        b1_l2 = Tex("PAYE 1 430; pension 825; UIF 110;").scale(1.0).shift(band_shift(1) + UP * 0.4)
        b1_l3 = Tex("medical 520; union 75").scale(1.0).shift(band_shift(1) + DOWN * 0.3)
        self.play(Write(b1_l2))
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_m1 = MathTex(r"\text{Deductions: } 2\,960").scale(1.05).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_m1))
        self.wait(2)
        b1_m2 = MathTex(r"11\,000 - 2\,960 = \text{R8 040 net}").scale(1.1).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1_m2))
        self.play(Create(SurroundingRectangle(b1_m2, color=GREEN)))
        self.wait(2)
        b1_l4 = Tex("Gross is earned; net is received").scale(1.0).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the employer's contributions ---
        self.next_band(2)
        b2_title = Tex("What the employer adds").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Pension: rand-for-rand -- another 825").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("UIF: matches the 1\\% -- another 110").scale(1.0).shift(band_shift(2) + UP * 0.3)
        b2_l3 = Tex("Medical: rand-for-rand -- another 520").scale(1.0).shift(band_shift(2) + DOWN * 0.5)
        b2_l4 = Tex("SDL: 1\\% of gross -- 110, no employee half").scale(1.0).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_w = Tex("Contributions shrink net pay?").scale(1.0).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2_w))
        self.play(Create(strike(b2_w)))
        self.wait(1.5)
        b2_ok = Tex("On top of gross -- never off the payslip").scale(0.95).shift(band_shift(2) + DOWN * 3.1)
        self.play(Write(b2_ok))
        self.play(Create(SurroundingRectangle(b2_ok, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): total cost of employment ---
        self.next_band(3)
        b3_title = Tex("The total cost of employing").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_m1 = MathTex(r"825 + 110 + 520 + 110 = 1\,565").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_m1))
        self.wait(2)
        b3_m2 = MathTex(r"11\,000 + 1\,565 = \text{R12 565}").scale(1.15).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_m2))
        self.play(Create(SurroundingRectangle(b3_m2, color=GREEN)))
        self.wait(2.5)
        b3_l1 = Tex("Worker receives 8 040;").scale(1.05).shift(band_shift(3) + DOWN * 1.0)
        b3_l2 = Tex("business pays out 12 565").scale(1.05).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("Every rand between them: tax, retirement,").scale(0.95).shift(band_shift(3) + DOWN * 2.7)
        b3_l4 = Tex("insurance, medicine, training").scale(0.95).shift(band_shift(3) + DOWN * 3.4)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): the Salaries Journal row ---
        self.next_band(4)
        b4_title = Tex("The Salaries Journal row").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_frame = Rectangle(width=7.4, height=2.2).shift(band_shift(4) + UP * 0.6)
        self.play(Create(b4_frame))
        b4_l1 = Tex("Gross 11 000 | PAYE 1 430 | Pens 825").scale(0.9).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex("UIF 110 | Med 520 | Union 75").scale(0.9).shift(band_shift(4) + UP * 0.4)
        b4_l3 = Tex("NET 8 040").scale(1.0).shift(band_shift(4) + DOWN * 0.2)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex("Employer columns: pens 825, UIF 110,").scale(0.95).shift(band_shift(4) + DOWN * 1.2)
        b4_l5 = Tex("med 520, SDL 110").scale(0.95).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(2)
        b4_l6 = Tex("WJ: Ndlovu 2 225 - 222,50 - 22,25 = 1 980,25").scale(0.85).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_3): the double entry and the settlements ---
        self.next_band(5)
        b5_title = Tex("The double entry, reasoned").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Debit Salaries: the full gross 11 000").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("Credit Bank (CPJ): only the net 8 040").scale(1.0).shift(band_shift(5) + UP * 0.3)
        b5_l3 = Tex("Credit each fund as a CREDITOR: owed").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex("Then the settlements: SARS 1 430 + 110;").scale(0.95).shift(band_shift(5) + DOWN * 1.4)
        b5_l5 = Tex("pension 825 + 825 = 1 650; UIF 220").scale(0.95).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(2)
        b5_l6 = Tex("Each payment: debit creditor, credit Bank").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l6))
        self.play(Create(SurroundingRectangle(b5_l6, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): ethics on the payroll ---
        self.next_band(6)
        b6_title = Tex("Ethics on the payroll").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("The CONTRACT authorises every figure").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("NEPOTISM: a name earning outside the scale").scale(0.95).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("Pay IN LINE WITH RESPONSIBILITIES:").scale(1.0).shift(band_shift(6) + DOWN * 0.4)
        b6_l4 = Tex("equal work, equal pay, on the scale").scale(1.0).shift(band_shift(6) + DOWN * 1.1)
        b6_l5 = Tex("The UNION: the workers' collective voice").scale(1.0).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2)
        self.play(Write(b6_l5))
        self.wait(2)
        b6_l6 = Tex("Books can balance while conduct cannot").scale(1.0).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the envelope that shrinks ---
        self.next_band(7)
        b7_title = Tex("The envelope that shrinks").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Leaves the safe with R11 000").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("Five stops: tax 1 430; retirement 825;").scale(0.95).shift(band_shift(7) + UP * 0.3)
        b7_l3 = Tex("insurance 110; doctor 520; union 75").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(b7_l2))
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_m1 = MathTex(r"\text{Arrives holding } \text{R8 040}").scale(1.1).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(b7_m1))
        self.play(Create(SurroundingRectangle(b7_m1, color=GREEN)))
        self.wait(2)
        b7_l4 = Tex("Nothing taken FROM you -- your money,").scale(1.0).shift(band_shift(7) + DOWN * 2.3)
        b7_l5 = Tex("sent ahead to agreed places").scale(1.0).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): the boss's second envelope ---
        self.next_band(8)
        b8_title = Tex("The boss's second envelope").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Retirement match 825; insurance match 110;").scale(0.9).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("medical match 520; skills levy 110").scale(0.95).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_m1 = MathTex(r"\text{Second envelope: } 1\,565").scale(1.05).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_m1))
        self.wait(2)
        b8_m2 = MathTex(r"11\,000 + 1\,565 = \text{R12 565}").scale(1.1).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_m2))
        self.play(Create(SurroundingRectangle(b8_m2, color=GREEN)))
        self.wait(2)
        b8_l3 = Tex("Your envelope shrinks by DEDUCTIONS;").scale(0.95).shift(band_shift(8) + DOWN * 2.4)
        b8_l4 = Tex("the second one is CONTRIBUTIONS, on top").scale(0.95).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_7): fair deals on payday ---
        self.next_band(9)
        b9_title = Tex("Fair deals on payday").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("The written deal: paper does not negotiate").scale(0.95).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("The nephew problem: nepotism poisons").scale(0.95).shift(band_shift(9) + UP * 0.3)
        b9_l3 = Tex("the ladder for everyone").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("Same work, same scale; heavier job, higher").scale(0.9).shift(band_shift(9) + DOWN * 1.2)
        b9_l5 = Tex("The union: one voice for all together").scale(0.95).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l4))
        self.wait(2)
        self.play(Write(b9_l5))
        self.wait(2)
        b9_l6 = Tex("Arithmetic wrapped around people").scale(1.05).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(4)
