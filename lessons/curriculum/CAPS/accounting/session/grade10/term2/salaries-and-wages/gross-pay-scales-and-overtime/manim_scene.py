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

# Band-layout whiteboard scene for "Gross Pay, Scales and Overtime"
# (grade10 term2, salaries-and-wages). One band per teaching beat, add-only
# lifecycle, camera moves down between bands. Exporter-safe mobjects only
# (Tex/MathTex/Line/Rectangle/SurroundingRectangle/VGroup).
#
# Subtopic time shares (subtopics.json, total 1380 s):
# 210/200/220/200/180/190/180 -> bands 0-1 / 2 / 3-4 / 5-6 / 7 / 8 / 9.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class GrossPayScalesOvertimeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): wage vs salary ---
        title = Tex("Gross Pay, Scales and Overtime").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("WAGE: pay per time worked -- the hour;").scale(1.05).shift(UP * 1.1)
        b0_l2 = Tex("paid weekly, varies with the week").scale(1.05).shift(UP * 0.3)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("SALARY: fixed annual amount -- the year;").scale(1.05).shift(DOWN * 0.6)
        b0_l4 = Tex("twelve equal monthly instalments").scale(1.05).shift(DOWN * 1.4)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(2.5)
        b0_l5 = Tex("The UNIT decides the journal:").scale(1.0).shift(DOWN * 2.3)
        b0_l6 = Tex("Wages Journal or Salaries Journal").scale(1.0).shift(DOWN * 3.0)
        self.play(Write(b0_l5))
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_1): reading the scale ---
        self.next_band(1)
        b1_title = Tex("Reading the scale").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\text{R96 000} \times \text{R9 600} - \text{R144 000}").scale(1.15).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Start R96 000; notch R9 600 per year;").scale(1.0).shift(band_shift(1) + UP * 0.3)
        b1_l3 = Tex("ceiling R144 000").scale(1.05).shift(band_shift(1) + DOWN * 0.5)
        self.play(Write(b1_l2))
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = Tex("Year 1: 96 000; year 2: 105 600;").scale(1.0).shift(band_shift(1) + DOWN * 1.4)
        b1_l5 = Tex("year 3: 115 200 -- one notch a year").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(2)
        b1_m = MathTex(r"\frac{144\,000 - 96\,000}{9\,600} = 5 \text{ increments}").scale(1.0).shift(band_shift(1) + DOWN * 3.2)
        self.play(Write(b1_m))
        self.play(Create(SurroundingRectangle(b1_m, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): overtime multipliers, rate first ---
        self.next_band(2)
        b2_title = Tex("Normal time and the multipliers").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Inside 45 normal hours: the basic rate").scale(1.05).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"\text{Time and a half: } 40 \times 1{,}5 = \text{R60/h}").scale(1.05).shift(band_shift(2) + UP * 0.3)
        b2_l3 = MathTex(r"\text{Double time: } 40 \times 2 = \text{R80/h}").scale(1.05).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("Evenings, Saturdays: 1,5; Sundays,").scale(1.0).shift(band_shift(2) + DOWN * 1.5)
        b2_l5 = Tex("public holidays: 2").scale(1.0).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.wait(2)
        b2_l6 = Tex("Write the RATE as its own line first --").scale(1.0).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): Dlamini's week ---
        self.next_band(3)
        b3_title = Tex("S. Dlamini: R40/h, 45 h + 4 h evenings").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"\text{Normal: } 45 \times 40 = \text{R1 800}").scale(1.1).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"\text{Overtime rate: } 40 \times 1{,}5 = \text{R60}").scale(1.1).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"\text{Overtime: } 4 \times 60 = \text{R240}").scale(1.1).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"\text{Gross} = 1\,800 + 240 = \text{R2 040}").scale(1.1).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2.5)
        b3_l5 = Tex("Public holiday instead? Rate R80:").scale(1.0).shift(band_shift(3) + DOWN * 2.5)
        b3_l6 = MathTex(r"4 \times 80 = 320; \;\; \text{gross R2 120}").scale(1.0).shift(band_shift(3) + DOWN * 3.3)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): Mokoena's week and the wage bill ---
        self.next_band(4)
        b4_title = Tex("B. Mokoena: R36/h, 45 h + 2 h Sunday").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"\text{Normal: } 45 \times 36 = \text{R1 620}").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"\text{Sunday rate: } 36 \times 2 = \text{R72}").scale(1.1).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"\text{Sunday: } 2 \times 72 = \text{R144}").scale(1.1).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"\text{Gross} = 1\,620 + 144 = \text{R1 764}").scale(1.1).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2.5)
        b4_l5 = MathTex(r"\text{Week's bill: } 2\,040 + 1\,764 = \text{R3 804}").scale(1.0).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_4): the administrator on the scale ---
        self.next_band(5)
        b5_title = Tex("The salaried administrator, year two").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Appointed at the R96 000 notch;").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("one completed year = one notch up").scale(1.05).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_m1 = MathTex(r"96\,000 + 9\,600 = \text{R105 600 per year}").scale(1.05).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_m1))
        self.wait(2)
        b5_m2 = MathTex(r"105\,600 \div 12 = \text{R8 800 per month}").scale(1.05).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_m2))
        self.play(Create(SurroundingRectangle(b5_m2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex("Same figure every month, however busy").scale(1.0).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l3))
        self.wait(3)

        # --- Band 6 (subtopic_4): technique, and the two designs ---
        self.next_band(6)
        b6_title = Tex("Scale technique, in order").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("1. Write start, notch, ceiling in words").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("2. Count COMPLETED years for the notch").scale(1.0).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("3. Divide by twelve only at the end").scale(1.0).shift(band_shift(6) + DOWN * 0.4)
        b6_l4 = Tex("4. Top: distance $\\div$ notch = increments").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        b6_l5 = Tex("5. Label every line -- marks ride the route").scale(1.0).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l1))
        self.wait(1.5)
        self.play(Write(b6_l2))
        self.wait(1.5)
        self.play(Write(b6_l3))
        self.wait(1.5)
        self.play(Write(b6_l4))
        self.wait(1.5)
        self.play(Write(b6_l5))
        self.wait(2)
        b6_l6 = Tex("Wages respond to the week; salaries").scale(1.0).shift(band_shift(6) + DOWN * 2.8)
        b6_l7 = Tex("are stable, growing by the notch").scale(1.0).shift(band_shift(6) + DOWN * 3.5)
        self.play(Write(b6_l6))
        self.play(Write(b6_l7))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): two ways of getting paid ---
        self.next_band(7)
        b7_title = Tex("Two ways of getting paid").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("``I sell my HOURS'': R40 each,").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("counted by the clock, lands Friday").scale(1.05).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("``I sell my YEAR'': one number,").scale(1.05).shift(band_shift(7) + DOWN * 0.6)
        b7_l4 = Tex("sliced into twelve equal months").scale(1.05).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("Different deals for different jobs --").scale(1.0).shift(band_shift(7) + DOWN * 2.3)
        b7_l6 = Tex("both build a number called GROSS").scale(1.05).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): the price list and the trap ---
        self.next_band(8)
        b8_title = Tex("The three-row price list").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Ordinary hour: R40 -- the plain price").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("Evening/Saturday: R60 -- a small apology").scale(1.0).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex("Sunday/holiday: R80 -- costs you the most").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_w = MathTex(r"\text{Overtime: } 4 \times 40 = 160").scale(1.05).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(b8_w))
        self.play(Create(strike(b8_w)))
        self.wait(1.5)
        b8_ok = MathTex(r"\text{Row first: } 4 \times 60 = \text{R240}").scale(1.05).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8_ok))
        self.play(Create(SurroundingRectangle(b8_ok, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex("Which row am I on? Price, then hours").scale(1.0).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_7): climbing the ladder ---
        self.next_band(9)
        b9_title = Tex("Climbing the ladder").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Start R96 000; climb R9 600 a rung;").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("top out at R144 000").scale(1.05).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Rung 1: R8 000/month; rung 2: R8 800").scale(1.05).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_m = MathTex(r"48\,000 \div 9\,600 = 5 \text{ steps to the top}").scale(1.0).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_m))
        self.play(Create(SurroundingRectangle(b9_m, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("The ladder makes tomorrow visible --").scale(1.0).shift(band_shift(9) + DOWN * 2.4)
        b9_l5 = Tex("staying is worth a rung a year").scale(1.0).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(4)
