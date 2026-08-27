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
        title = Tex("Wages, Salaries and the Scale").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("WAGE: pay per HOUR worked,").scale(1.05).shift(UP * 1.2)
        b0_l2 = Tex("paid weekly or fortnightly").scale(1.05).shift(UP * 0.4)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("SALARY: fixed amount per YEAR,").scale(1.05).shift(DOWN * 0.5)
        b0_l4 = Tex("paid in twelve equal slices").scale(1.05).shift(DOWN * 1.3)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(2.5)
        b0_l5 = Tex("The difference is the UNIT sold:").scale(1.0).shift(DOWN * 2.2)
        b0_l6 = Tex("the hour or the year").scale(1.05).shift(DOWN * 3.0)
        self.play(Write(b0_l5))
        self.play(Write(b0_l6))
        self.play(Create(SurroundingRectangle(b0_l6, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): reading the scale ---
        self.next_band(1)
        b1_title = Tex(r"R120 000 $\times$ R12 000 -- R180 000").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = Tex("Start: R120 000 a year").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("Notch: +R12 000 per completed year").scale(1.0).shift(band_shift(1) + UP * 0.3)
        b1_l3 = Tex("Ceiling: R180 000 -- the climb stops").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        self.play(Write(b1_l1))
        self.wait(1.5)
        self.play(Write(b1_l2))
        self.wait(1.5)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_m1 = MathTex(r"\frac{180\,000 - 120\,000}{12\,000} = 5 \text{ increments}").scale(0.95).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(b1_m1))
        self.wait(2)
        b1_l4 = Tex("Ceiling reached at the START of year six").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): overtime multipliers, rate first ---
        self.next_band(2)
        b2_title = Tex("The overtime multipliers").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"Evenings, Saturdays: $1{,}5\times$ normal").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex(r"Sundays, public holidays: $2\times$ normal").scale(1.0).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_m1 = MathTex(r"R50 \Rightarrow R75 \text{ and } R100").scale(1.05).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_m1))
        self.wait(2)
        b2_w = Tex("Hours times the NORMAL rate?").scale(1.0).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(b2_w))
        self.play(Create(strike(b2_w)))
        self.wait(1.5)
        b2_ok = Tex("Derive the RATE first, its own line").scale(1.0).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_ok))
        self.play(Create(SurroundingRectangle(b2_ok, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): Ndlovu's week ---
        self.next_band(3)
        b3_title = Tex("Ndlovu's week: R50 an hour").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{Normal: } 40 \times 50 = 2\,000").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"\text{OT rate: } 50 \times 1{,}5 = 75").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"\text{OT: } 3 \times 75 = 225").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"\text{Gross: } 2\,000 + 225 = \text{R2 225}").scale(1.05).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex("Every line labelled: normal, rate,").scale(0.95).shift(band_shift(3) + DOWN * 2.6)
        b3_l6 = Tex("overtime, gross").scale(0.95).shift(band_shift(3) + DOWN * 3.3)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): Adams's week and the wage bill ---
        self.next_band(4)
        b4_title = Tex("Adams's week: R44 an hour").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{Normal: } 40 \times 44 = 1\,760").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"\text{Sunday rate: } 44 \times 2 = 88").scale(1.0).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"\text{Sunday: } 2 \times 88 = 176").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"\text{Gross: } 1\,760 + 176 = \text{R1 936}").scale(1.05).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = MathTex(r"\text{Wage bill: } 2\,225 + 1\,936 = \text{R4 161}").scale(1.0).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_4): the administrator on the scale ---
        self.next_band(5)
        b5_title = Tex("The administrator, year two").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Appointed on R120 000").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("One completed year = one notch").scale(1.05).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2)
        b5_m1 = MathTex(r"120\,000 + 12\,000 = 132\,000").scale(1.05).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_m1))
        self.wait(2)
        b5_m2 = MathTex(r"132\,000 \div 12 = \text{R11 000 monthly}").scale(1.05).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_m2))
        self.play(Create(SurroundingRectangle(b5_m2, color=GREEN)))
        self.wait(2)
        b5_l3 = Tex("The same figure every month,").scale(1.0).shift(band_shift(5) + DOWN * 2.5)
        b5_l4 = Tex("however busy the shop was").scale(1.0).shift(band_shift(5) + DOWN * 3.2)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): technique, and the two designs ---
        self.next_band(6)
        b6_title = Tex("Scale technique, in order").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("1. Write start, notch, ceiling in words").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("2. Count COMPLETED years of service").scale(0.95).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("3. Divide by twelve only at the end").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        b6_l4 = Tex("4. Distance over notch counts increments").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        b6_l5 = Tex("5. Label every line").scale(0.95).shift(band_shift(6) + DOWN * 2.0)
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
        b6_l6 = Tex("Wage responds to the week;").scale(1.0).shift(band_shift(6) + DOWN * 2.8)
        b6_l7 = Tex("salary is stable, growing by notch").scale(1.0).shift(band_shift(6) + DOWN * 3.5)
        self.play(Write(b6_l6))
        self.play(Write(b6_l7))
        self.play(Create(SurroundingRectangle(b6_l7, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): two ways of getting paid ---
        self.next_band(7)
        b7_title = Tex("Two ways of getting paid").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("``I sell my HOURS'' -- the clock deal:").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("busy week, big pay; lands Friday").scale(1.0).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("``I sell my YEAR'' -- the year deal:").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        b7_l4 = Tex("one number, twelve equal slices").scale(1.0).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("Both deals build a number called GROSS").scale(1.0).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): the price list and the trap ---
        self.next_band(8)
        b8_title = Tex("The price list of hours").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Ordinary hour: R50 -- the plain price").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("Evening / Saturday: R75 -- the apology").scale(1.0).shift(band_shift(8) + UP * 0.3)
        b8_l3 = Tex("Sunday / holiday: R100 -- the double").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_w = Tex("Extra hours at the plain price?").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_w))
        self.play(Create(strike(b8_w)))
        self.wait(1.5)
        b8_ok = Tex("The row first -- then multiply").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_ok))
        self.play(Create(SurroundingRectangle(b8_ok, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): climbing the ladder ---
        self.next_band(9)
        b9_title = Tex("Climbing the ladder").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Start R120 000; each rung +R12 000;").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("top of the ladder R180 000").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2)
        b9_m1 = MathTex(r"60\,000 \div 12\,000 = 5 \text{ climbs}").scale(1.05).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_m1))
        self.wait(2)
        b9_l3 = Tex("Find the rung: count completed years").scale(0.95).shift(band_shift(9) + DOWN * 1.5)
        b9_l4 = Tex("Year to month: divide by twelve").scale(0.95).shift(band_shift(9) + DOWN * 2.2)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("The ladder makes tomorrow visible").scale(1.05).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(4)
