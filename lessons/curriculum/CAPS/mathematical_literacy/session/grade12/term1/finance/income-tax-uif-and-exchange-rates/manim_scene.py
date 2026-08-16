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

# Band-layout whiteboard scene for the Income Tax, UIF and Exchange Rates
# session duo. Part 1 — Expert: subtopics 1-4 (gross to taxable, tax table
# and rebate, UIF and the payslip, exchange rates). Part 2 — Simplifier:
# subtopics 5-7 retell the ladder, the rainy-day percent and the price tag.
# Durations 215/215/225/230/195/195/195 of 1470 s. Exporter-safe mobjects
# only; add-only lifecycle; camera moves down one band per teaching beat.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class IncomeTaxUifExchangeRatesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): gross to taxable income ---
        title = Tex("Income Tax, UIF and Exchange Rates").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Gross income: everything before subtraction").scale(1.0).shift(UP * 1.1)
        b0_l2 = MathTex(r"28\;500 \times 12 = \text{R342 000 a year}").scale(1.05).shift(UP * 0.2)
        b0_l3 = Tex("No deductions: taxable income R342 000").scale(1.05).shift(DOWN * 0.7)
        b0_l4 = Tex("The IRP5 records income and tax deducted").scale(1.0).shift(DOWN * 1.7)
        self.play(Write(b0_l1)); self.wait(2)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(2)
        self.play(Write(b0_l3)); self.wait(2)
        self.play(Write(b0_l4)); self.wait(3)

        # --- Band 1 (subtopic_1): the vocabulary that carries marks ---
        self.next_band(1)
        b1_title = Tex("Vocabulary that carries marks").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Tax year: 1 March to end February").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("PAYE: monthly tax sent ahead to SARS").scale(1.05).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"\text{Threshold: R95 750 } \Rightarrow \text{ no tax below}").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = Tex("Non-taxable: inheritances, most bursaries").scale(1.0).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        self.play(Write(b1_l3)); self.wait(2.5)
        self.play(Write(b1_l4)); self.wait(3)

        # --- Band 2 (subtopic_2): reading the tax table ---
        self.next_band(2)
        b2_title = Tex("The tax table: a staircase of rates").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{To } 237\;100: 18\%").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"\text{Then: } 42\;678 + 26\% \text{ above } 237\;100").scale(1.0).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"342\;000 - 237\;100 = 104\;900").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = MathTex(r"104\;900 \times 0,26 = 27\;274").scale(1.05).shift(band_shift(2) + DOWN * 1.6)
        b2_l5 = MathTex(r"42\;678 + 27\;274 = \text{R69 952}").scale(1.05).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l1)); self.wait(2)
        self.play(Write(b2_l2)); self.wait(2.5)
        self.play(Write(b2_l3)); self.wait(2)
        self.play(Write(b2_l4)); self.wait(2)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the rebate, and the classic error ---
        self.next_band(3)
        b3_title = Tex("Subtract the rebate, dodge the trap").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_wrong = MathTex(r"26\% \text{ of ALL } 342\;000 = 88\;920").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_l1 = MathTex(r"69\;952 - 17\;235 = \text{R52 717}").scale(1.1).shift(band_shift(3) + UP * 0.1)
        b3_l2 = MathTex(r"52\;717 \div 12 = \text{R4 393,08 PAYE}").scale(1.1).shift(band_shift(3) + DOWN * 0.9)
        b3_l3 = Tex("Tax only starts once tax exceeds the rebate").scale(1.0).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l1)); self.wait(2.5)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        self.play(Write(b3_l3)); self.wait(3)

        # --- Band 4 (subtopic_3): UIF and its ceiling ---
        self.next_band(4)
        b4_title = Tex("UIF: 1\\% with a ceiling").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Employee 1\\%, employer another 1\\% on top").scale(1.05).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"\text{Ceiling: R17 712} \Rightarrow \text{max R177,12}").scale(1.05).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"\text{R28 500 salary: capped at R177,12}").scale(1.05).shift(band_shift(4) + DOWN * 0.8)
        b4_l4 = MathTex(r"\text{R12 000 salary: } 1\% = \text{R120,00}").scale(1.05).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l1)); self.wait(2)
        self.play(Write(b4_l2)); self.wait(2.5)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        self.play(Write(b4_l4)); self.wait(3)

        # --- Band 5 (subtopic_3): assembling the payslip ---
        self.next_band(5)
        b5_title = Tex("The payslip, assembled").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        slip = Rectangle(width=8.2, height=3.4).shift(band_shift(5) + DOWN * 0.3)
        self.play(Create(slip))
        b5_l1 = MathTex(r"\text{Gross: R28 500,00}").scale(1.0).shift(band_shift(5) + UP * 0.9)
        b5_l2 = MathTex(r"\text{PAYE R4 393,08} \quad \text{UIF R177,12}").scale(1.0).shift(band_shift(5) + UP * 0.1)
        b5_l3 = MathTex(r"28\;500 - 4\;393,08 - 177,12 = \text{R23 929,80}").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l1)); self.wait(2)
        self.play(Write(b5_l2)); self.wait(2)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_l4 = MathTex(r"4\;570,20 \div 28\;500 \times 100 = 16,04\%").scale(1.0).shift(band_shift(5) + DOWN * 2.2)
        b5_l5 = Tex("About one rand in six leaves first").scale(1.0).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l4)); self.wait(2)
        self.play(Write(b5_l5)); self.wait(3)

        # --- Band 6 (subtopic_4): exchange rates, both directions ---
        self.next_band(6)
        b6_title = Tex("R18,50 per dollar: the price of money").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"450 \times 18,50 = \text{R8 325,00}").scale(1.1).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"5\;000 \div 18,50 = 270,27 \text{ dollars}").scale(1.1).shift(band_shift(6) + UP * 0.1)
        b6_l3 = Tex("Rand numbers grow; dollar numbers shrink").scale(1.05).shift(band_shift(6) + DOWN * 0.9)
        b6_l4 = Tex("Smaller rand answer? Wrong operation").scale(1.05).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l1)); self.wait(2.5)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        self.play(Write(b6_l3)); self.wait(2)
        self.play(Write(b6_l4)); self.wait(3)

        # --- Band 7 (subtopic_4): movement and buying power ---
        self.next_band(7)
        b7_title = Tex("When the rate moves").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"18,50 \to 19,20: \text{ rand WEAKENED}").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"899 \times 18,50 = \text{R16 631,50}").scale(1.05).shift(band_shift(7) + UP * 0.2)
        b7_l3 = MathTex(r"899 \times 19,20 = \text{R17 260,80}").scale(1.05).shift(band_shift(7) + DOWN * 0.7)
        b7_l4 = Tex("Weaker rand: imports, fuel, travel cost more").scale(1.0).shift(band_shift(7) + DOWN * 1.7)
        b7_l5 = Tex("Stronger rand: imports cheapen, exporters earn less").scale(0.95).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l1)); self.wait(2.5)
        self.play(Write(b7_l2)); self.wait(2)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        self.play(Write(b7_l4)); self.wait(2.5)
        self.play(Write(b7_l5)); self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the ladder of tax brackets ---
        self.next_band(8)
        b8_title = Tex("The ladder of tax brackets").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2.5)
        b8_l1 = Tex("A raise never re-taxes the lower rungs").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = MathTex(r"\text{Rung 1 done for you: R42 678}").scale(1.05).shift(band_shift(8) + UP * 0.2)
        b8_l3 = MathTex(r"\text{Only the slice: } 104\;900 \times 26\% = 27\;274").scale(1.0).shift(band_shift(8) + DOWN * 0.8)
        b8_l4 = MathTex(r"69\;952 - 17\;235 = \text{R52 717 owed}").scale(1.05).shift(band_shift(8) + DOWN * 1.8)
        b8_l5 = Tex("26\\% on everything overtaxes by R19 000").scale(1.0).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l1)); self.wait(3)
        self.play(Write(b8_l2)); self.wait(3)
        self.play(Write(b8_l3)); self.wait(3)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(3)
        self.play(Write(b8_l5)); self.wait(3)

        # --- Band 9 (subtopic_6): one percent for the rainy day ---
        self.next_band(9)
        b9_title = Tex("One percent for the rainy day").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = Tex("UIF: insurance at one cent in the rand").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"\text{Counting stops at R17 712: pay R177,12}").scale(1.0).shift(band_shift(9) + UP * 0.2)
        b9_l3 = MathTex(r"\text{Net: } 28\;500 - 4\;393,08 - 177,12").scale(1.05).shift(band_shift(9) + DOWN * 0.8)
        b9_l4 = MathTex(r"= \text{R23 929,80 in the bank}").scale(1.1).shift(band_shift(9) + DOWN * 1.7)
        b9_l5 = Tex("Of every R100 earned, about R16 leaves first").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l1)); self.wait(3)
        self.play(Write(b9_l2)); self.wait(3)
        self.play(Write(b9_l3)); self.wait(3)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(3)
        self.play(Write(b9_l5)); self.wait(3)

        # --- Band 10 (subtopic_7): rands per dollar, which way to divide ---
        self.next_band(10)
        b10_title = Tex("The rate is a price tag").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2.5)
        b10_l1 = Tex("One dollar COSTS R18,50 — like bananas").scale(1.05).shift(band_shift(10) + UP * 1.1)
        b10_l2 = MathTex(r"\text{Buy 450: } 450 \times 18,50 = \text{R8 325}").scale(1.05).shift(band_shift(10) + UP * 0.2)
        b10_l3 = MathTex(r"\text{How many tags? } 5\;000 \div 18,50 = 270").scale(1.05).shift(band_shift(10) + DOWN * 0.8)
        b10_l4 = Tex("Nobody gets rich at a bureau de change").scale(1.05).shift(band_shift(10) + DOWN * 1.8)
        b10_l5 = Tex("Weaker rand, dearer imports — say it with numbers").scale(0.95).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l1)); self.wait(3)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(3)
        self.play(Write(b10_l3)); self.wait(3)
        self.play(Write(b10_l4)); self.wait(3)
        self.play(Write(b10_l5)); self.wait(4)
