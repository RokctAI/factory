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

# Band-layout whiteboard scene for "Depreciation Methods" (grade10 term2,
# year-end-procedures-and-final-accounts). One band per teaching beat,
# add-only lifecycle, camera moves down between bands. Exporter-safe mobjects
# only (Tex/MathTex/Line/Rectangle/SurroundingRectangle/VGroup).
#
# Subtopic time shares (subtopics.json, total 1420 s):
# 210/210/230/210/180/200/180 -> bands 0-1 / 2-3 / 4-5 / 6-7 / 8 / 9 / 10.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DepreciationMethodsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): why the books must record the wearing ---
        title = Tex("Depreciation Methods").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Bakkie: R120 000, bought 1 March --").scale(1.05).shift(UP * 1.2)
        b0_l2 = Tex("worth steadily less from day one").scale(1.05).shift(UP * 0.4)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("MATCHING: spread the cost across the").scale(1.0).shift(DOWN * 0.5)
        b0_l4 = Tex("years the bakkie earns").scale(1.0).shift(DOWN * 1.3)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex("PRUDENCE: never carry an ageing asset").scale(1.0).shift(DOWN * 2.2)
        b0_l6 = Tex("at its shiny purchase price").scale(1.0).shift(DOWN * 3.0)
        self.play(Write(b0_l5))
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_1): three figures and the double entry ---
        self.next_band(1)
        b1_title = Tex("Three figures, kept strictly apart").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("COST: R120 000 -- anchored forever").scale(1.05).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex("ACCUMULATED: total written off so far,").scale(1.0).shift(band_shift(1) + UP * 0.4)
        b1_l3 = Tex("a negative asset, growing yearly").scale(1.0).shift(band_shift(1) + DOWN * 0.3)
        b1_l4 = MathTex(r"\text{CARRYING} = \text{cost} - \text{accumulated}").scale(1.05).shift(band_shift(1) + DOWN * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)
        b1_l5 = Tex("Entry: debit Depreciation (expense);").scale(1.0).shift(band_shift(1) + DOWN * 2.1)
        b1_l6 = Tex("credit Accumulated Depreciation --").scale(1.0).shift(band_shift(1) + DOWN * 2.8)
        b1_l7 = Tex("never credit Vehicles itself").scale(1.0).shift(band_shift(1) + DOWN * 3.5)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.play(Write(b1_l7))
        self.wait(3)

        # --- Band 2 (subtopic_2): straight-line, the level slice ---
        self.next_band(2)
        b2_title = Tex("Straight-line: 20\\% on COST").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Year 1: } 20\% \times 120\,000 = \text{R24 000}").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"\text{Year 2: } 20\% \times 120\,000 = \text{R24 000}").scale(1.05).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"\text{Year 3: R24 000 again}").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("The slice never changes, because its").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        b2_l5 = Tex("base -- cost -- never changes").scale(1.0).shift(band_shift(2) + DOWN * 2.3)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.wait(2)
        b2_l6 = Tex("Even service, even slices: furniture,").scale(0.95).shift(band_shift(2) + DOWN * 3.0)
        b2_l7 = Tex("fittings, office equipment").scale(0.95).shift(band_shift(2) + DOWN * 3.6)
        self.play(Write(b2_l6))
        self.play(Write(b2_l7))
        self.wait(3)

        # --- Band 3 (subtopic_2): the three figures down the years ---
        self.next_band(3)
        b3_title = Tex("Tracking the three figures").scale(1.2).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_h1 = Tex("Year").scale(0.9).shift(band_shift(3) + UP * 1.4 + LEFT * 2.8)
        b3_h2 = Tex("Accumulated").scale(0.9).shift(band_shift(3) + UP * 1.4)
        b3_h3 = Tex("Carrying").scale(0.9).shift(band_shift(3) + UP * 1.4 + RIGHT * 2.8)
        self.play(Write(b3_h1), Write(b3_h2), Write(b3_h3))
        b3_hl = Line(LEFT * 3.5, RIGHT * 3.5).shift(band_shift(3) + UP * 1.0)
        self.play(Create(b3_hl))
        self.wait(1.5)
        b3_r1a = Tex("1").scale(0.95).shift(band_shift(3) + UP * 0.4 + LEFT * 2.8)
        b3_r1b = Tex("24 000").scale(0.95).shift(band_shift(3) + UP * 0.4)
        b3_r1c = Tex("96 000").scale(0.95).shift(band_shift(3) + UP * 0.4 + RIGHT * 2.8)
        self.play(Write(b3_r1a), Write(b3_r1b), Write(b3_r1c))
        self.wait(2)
        b3_r2a = Tex("2").scale(0.95).shift(band_shift(3) + DOWN * 0.4 + LEFT * 2.8)
        b3_r2b = Tex("48 000").scale(0.95).shift(band_shift(3) + DOWN * 0.4)
        b3_r2c = Tex("72 000").scale(0.95).shift(band_shift(3) + DOWN * 0.4 + RIGHT * 2.8)
        self.play(Write(b3_r2a), Write(b3_r2b), Write(b3_r2c))
        self.wait(2)
        b3_r3a = Tex("3").scale(0.95).shift(band_shift(3) + DOWN * 1.2 + LEFT * 2.8)
        b3_r3b = Tex("72 000").scale(0.95).shift(band_shift(3) + DOWN * 1.2)
        b3_r3c = Tex("48 000").scale(0.95).shift(band_shift(3) + DOWN * 1.2 + RIGHT * 2.8)
        self.play(Write(b3_r3a), Write(b3_r3b), Write(b3_r3c))
        self.wait(2)
        b3_l1 = Tex("Same R24 000 step down -- a straight").scale(1.0).shift(band_shift(3) + DOWN * 2.2)
        b3_l2 = Tex("line; gone in five years at 20\\%").scale(1.0).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(3)

        # --- Band 4 (subtopic_3): diminishing balance, and the base trap ---
        self.next_band(4)
        b4_title = Tex("Diminishing balance: 20\\% on").scale(1.15).shift(band_shift(4) + UP * 2.3)
        b4_title2 = Tex("CARRYING VALUE").scale(1.15).shift(band_shift(4) + UP * 1.6)
        self.play(Write(b4_title))
        self.play(Write(b4_title2))
        self.wait(2)
        b4_l1 = MathTex(r"\text{Yr 1: } 20\% \times 120\,000 = 24\,000 \;\; (96\,000)").scale(0.95).shift(band_shift(4) + UP * 0.7)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_w = MathTex(r"\text{Yr 2: } 20\% \times 120\,000?").scale(1.0).shift(band_shift(4) + DOWN * 0.1)
        self.play(Write(b4_w))
        self.play(Create(strike(b4_w)))
        self.wait(1.5)
        b4_l2 = MathTex(r"\text{Yr 2: } 20\% \times 96\,000 = 19\,200 \;\; (76\,800)").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2)
        b4_l3 = MathTex(r"\text{Yr 3: } 20\% \times 76\,800 = 15\,360 \;\; (61\,440)").scale(0.95).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex("Shrinking base, shrinking charge --").scale(1.0).shift(band_shift(4) + DOWN * 2.7)
        b4_l5 = Tex("big work years carry big slices").scale(1.0).shift(band_shift(4) + DOWN * 3.4)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): the mid-year addition ---
        self.next_band(5)
        b5_title = Tex("Bought partway through the year").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Machine R18 000, 1 September;").scale(1.05).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("straight-line at 10\\% -- but it worked").scale(1.05).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex("only SIX months of this year").scale(1.05).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.play(Write(b5_l3))
        self.wait(2)
        b5_m1 = MathTex(r"1\,800 \times \tfrac{6}{12} = \text{R900}").scale(1.15).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5_m1))
        self.play(Create(SurroundingRectangle(b5_m1, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex("Pro rata from the month of purchase,").scale(1.0).shift(band_shift(5) + DOWN * 2.4)
        b5_l5 = Tex("on either method; carrying value R17 100").scale(1.0).shift(band_shift(5) + DOWN * 3.1)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the asset register ---
        self.next_band(6)
        b6_title = Tex("The asset register").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("One page per asset: description,").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("registration, date, cost, method, rate,").scale(1.0).shift(band_shift(6) + UP * 0.3)
        b6_l3 = Tex("then year by year: charge, accumulated,").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex("carrying value -- the whole life story").scale(1.0).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("Register totals must agree with the").scale(1.0).shift(band_shift(6) + DOWN * 2.2)
        b6_l6 = Tex("ledger -- summary and detail, like").scale(1.0).shift(band_shift(6) + DOWN * 2.9)
        b6_l7 = Tex("debtors control and its list").scale(1.0).shift(band_shift(6) + DOWN * 3.6)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.play(Write(b6_l7))
        self.wait(3)

        # --- Band 7 (subtopic_4): exam technique, five habits ---
        self.next_band(7)
        b7_title = Tex("Five habits for the exam").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("1. Name the method: ``on cost'' vs").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("``on carrying value''").scale(1.0).shift(band_shift(7) + UP * 0.5)
        b7_l3 = Tex("2. Write the base figure down first").scale(1.0).shift(band_shift(7) + DOWN * 0.3)
        b7_l4 = Tex("3. Count the months, write the fraction").scale(1.0).shift(band_shift(7) + DOWN * 1.1)
        b7_l5 = Tex("4. Label: year's charge / accumulated /").scale(1.0).shift(band_shift(7) + DOWN * 1.9)
        b7_l6 = Tex("carrying value").scale(1.0).shift(band_shift(7) + DOWN * 2.6)
        b7_l7 = Tex("5. Expense debited, accumulated credited").scale(1.0).shift(band_shift(7) + DOWN * 3.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.wait(1.5)
        self.play(Write(b7_l4))
        self.wait(1.5)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(1.5)
        self.play(Write(b7_l7))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): receipt, wear, worth ---
        self.next_band(8)
        b8_title = Tex("The bakkie that quietly gets cheaper").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Like last year's phone: nothing broke,").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("the world just marked it down").scale(1.0).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("RECEIPT: R120 000 -- written in ink").scale(1.05).shift(band_shift(8) + DOWN * 0.6)
        b8_l4 = Tex("WEAR: the running total of loss").scale(1.05).shift(band_shift(8) + DOWN * 1.4)
        b8_l5 = Tex("WORTH: receipt minus wear, today").scale(1.05).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(2)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(2)
        b8_l6 = Tex("Every question asks for ONE of the three").scale(0.95).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_6): two ways to slice the loaf ---
        self.next_band(9)
        b9_title = Tex("Two ways to slice the loss").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Same slice of the ORIGINAL loaf:").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("24 000, 24 000, 24 000 -- straight-line").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("A fifth of WHAT'S LEFT: 24 000, then").scale(1.0).shift(band_shift(9) + DOWN * 0.5)
        b9_l4 = Tex("19 200, then 15 360 -- diminishing").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("Year two: which number do you slice?").scale(1.0).shift(band_shift(9) + DOWN * 2.2)
        b9_l6 = Tex("Say the base out loud before you cut").scale(1.0).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l5))
        self.wait(2)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): every asset gets its own page ---
        self.next_band(10)
        b10_title = Tex("Every asset gets its own page").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Totals upstairs (the ledger); faces").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("downstairs (the register) -- must agree").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("A page nobody can produce on inspection").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        b10_l4 = Tex("starts a very serious conversation").scale(1.0).shift(band_shift(10) + DOWN * 1.4)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex("September machine: charged for the six").scale(1.0).shift(band_shift(10) + DOWN * 2.3)
        b10_l6 = Tex("months it served -- R900, not R1 800").scale(1.0).shift(band_shift(10) + DOWN * 3.1)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
