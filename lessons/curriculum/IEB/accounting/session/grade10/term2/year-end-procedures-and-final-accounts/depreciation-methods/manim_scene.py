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

# Band-layout whiteboard scene for "Depreciation Methods" (grade10 term2,
# year-end-procedures-and-final-accounts). One band per teaching beat,
# add-only lifecycle, camera moves down between bands. Exporter-safe
# mobjects only (Tex/MathTex/Line/Rectangle/SurroundingRectangle/VGroup).
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
        title = Tex("Why Assets Lose Value in the Books").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Bakkie: R150 000 on 1 March").scale(1.05).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("MATCHING: spread the cost across").scale(1.0).shift(UP * 0.3)
        b0_l3 = Tex("the years the asset earns").scale(1.0).shift(DOWN * 0.4)
        self.play(Write(b0_l2))
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_l4 = Tex("PRUDENCE: never carry an ageing").scale(1.0).shift(DOWN * 1.3)
        b0_l5 = Tex("asset at its showroom price").scale(1.0).shift(DOWN * 2.0)
        self.play(Write(b0_l4))
        self.play(Write(b0_l5))
        self.wait(2.5)
        b0_l6 = Tex("The books must record the wearing").scale(1.0).shift(DOWN * 2.9)
        self.play(Write(b0_l6))
        self.play(Create(SurroundingRectangle(b0_l6, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): three figures and the double entry ---
        self.next_band(1)
        b1_title = Tex("Three figures, kept apart").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("COST: R150 000 -- anchored forever").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("ACCUMULATED: all wear to date,").scale(1.0).shift(band_shift(1) + UP * 0.3)
        b1_l3 = Tex("a negative asset, growing yearly").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        b1_l4 = Tex("CARRYING VALUE: cost minus accumulated").scale(1.0).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("Debit Depreciation;").scale(1.0).shift(band_shift(1) + DOWN * 2.1)
        b1_l6 = Tex("credit Accumulated -- never Vehicles").scale(1.0).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.play(Create(SurroundingRectangle(b1_l6, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): straight-line, the level slice ---
        self.next_band(2)
        b2_title = Tex("Straight-line: 20\\% on COST").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_m1 = MathTex(r"20\% \times 150\,000 = 30\,000").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_m1))
        self.wait(2)
        b2_l1 = Tex("Year one: 30 000. Year two: 30 000.").scale(1.0).shift(band_shift(2) + UP * 0.2)
        b2_l2 = Tex("Year three: 30 000. The slice never").scale(1.0).shift(band_shift(2) + DOWN * 0.5)
        b2_l3 = Tex("changes -- its base never changes").scale(1.0).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex("Five level slices consume the cost;").scale(0.95).shift(band_shift(2) + DOWN * 2.1)
        b2_l5 = Tex("often R1 is left standing").scale(0.95).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): the three figures down the years ---
        self.next_band(3)
        b3_title = Tex("The three figures, year by year").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("End Y1: cost 150 000; acc 30 000;").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("carrying value 120 000").scale(0.95).shift(band_shift(3) + UP * 0.5)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("End Y2: acc 60 000; carrying 90 000").scale(0.95).shift(band_shift(3) + DOWN * 0.3)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("End Y3: acc 90 000; carrying 60 000").scale(0.95).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("A straight line down the graph --").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        b3_l6 = Tex("the method's name is its picture").scale(1.0).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(b3_l6, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): diminishing balance, and the base trap ---
        self.next_band(4)
        b4_title = Tex("Diminishing balance: 20\\% of what's LEFT").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_m1 = MathTex(r"\text{Y1: } 20\% \times 150\,000 = 30\,000").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_m2 = MathTex(r"\text{Y2: } 20\% \times 120\,000 = 24\,000").scale(0.95).shift(band_shift(4) + UP * 0.4)
        b4_m3 = MathTex(r"\text{Y3: } 20\% \times 96\,000 = 19\,200").scale(0.95).shift(band_shift(4) + DOWN * 0.4)
        self.play(Write(b4_m1))
        self.wait(2)
        self.play(Write(b4_m2))
        self.wait(2)
        self.play(Write(b4_m3))
        self.wait(2)
        b4_w = Tex("Year two: 20\\% of 150 000?").scale(1.0).shift(band_shift(4) + DOWN * 1.4)
        self.play(Write(b4_w))
        self.play(Create(strike(b4_w)))
        self.wait(1.5)
        b4_ok = Tex("The base is the CARRYING VALUE: 120 000").scale(0.95).shift(band_shift(4) + DOWN * 2.3)
        self.play(Write(b4_ok))
        self.play(Create(SurroundingRectangle(b4_ok, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the mid-year addition ---
        self.next_band(5)
        b5_title = Tex("Bought partway through the year").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Computer: R24 000 on 1 November,").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("straight-line at 15\\%").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2)
        b5_m1 = MathTex(r"\text{Full year: } 15\% \times 24\,000 = 3\,600").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_m1))
        self.wait(2)
        b5_m2 = MathTex(r"3\,600 \times \tfrac{4}{12} = \text{R1 200}").scale(1.05).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_m2))
        self.play(Create(SurroundingRectangle(b5_m2, color=GREEN)))
        self.wait(2)
        b5_l3 = Tex("Four months served: Nov to Feb --").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        b5_l4 = Tex("carrying value ends at 22 800").scale(0.95).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): the asset register ---
        self.next_band(6)
        b6_title = Tex("The asset register").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("One page per asset: description,").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("date, cost, method, rate -- then").scale(1.0).shift(band_shift(6) + UP * 0.3)
        b6_l3 = Tex("yearly: wear, accumulated, carrying").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("Register totals must equal ledger").scale(1.0).shift(band_shift(6) + DOWN * 1.4)
        b6_l5 = Tex("balances -- summary meets detail").scale(1.0).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(2)
        b6_l6 = Tex("An unproducible asset has a question").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): exam technique, five habits ---
        self.next_band(7)
        b7_title = Tex("Five habits").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("1. Name the method: on cost / on carrying").scale(0.9).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("2. Write the base figure first").scale(0.95).shift(band_shift(7) + UP * 0.4)
        b7_l3 = Tex("3. Count the months; write the fraction").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex("4. Label: year's / accumulated / carrying").scale(0.9).shift(band_shift(7) + DOWN * 1.2)
        b7_l5 = Tex("5. Expense debited, accumulated credited").scale(0.9).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l1))
        self.wait(1.5)
        self.play(Write(b7_l2))
        self.wait(1.5)
        self.play(Write(b7_l3))
        self.wait(1.5)
        self.play(Write(b7_l4))
        self.wait(1.5)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): receipt, wear, worth ---
        self.next_band(8)
        b8_title = Tex("The bakkie that quietly gets cheaper").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Nothing broke -- it just got older,").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("and the world marked it down").scale(1.0).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("RECEIPT: what it cost -- in ink").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        b8_l4 = Tex("WEAR: what it has lost so far").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        b8_l5 = Tex("WORTH: the honest answer today").scale(1.0).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(2)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): two ways to slice the loaf ---
        self.next_band(9)
        b9_title = Tex("Two ways to slice the loaf").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Same slice: 30 000 every year,").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("gone in five -- straight-line").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("A fifth of what's left: 30 000,").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        b9_l4 = Tex("24 000, 19 200 -- diminishing balance").scale(1.0).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("Say the base out loud before you cut").scale(1.0).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): every asset gets its own page ---
        self.next_band(10)
        b10_title = Tex("Every asset gets its own page").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Totals upstairs in the ledger;").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("faces downstairs in the register").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("November computer: four months served,").scale(0.95).shift(band_shift(10) + DOWN * 0.6)
        b10_l4 = Tex("so 1 200, not 3 600").scale(1.0).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex("The page holds the facts behind").scale(1.0).shift(band_shift(10) + DOWN * 2.2)
        b10_l6 = Tex("replace-or-repair").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
