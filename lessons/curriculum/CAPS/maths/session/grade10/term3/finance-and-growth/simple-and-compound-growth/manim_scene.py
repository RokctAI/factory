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

# Band-layout whiteboard scene (see the quadratics-by-factorisation worked
# example). One band per teaching beat; the camera moves down to clean space
# and nothing is ever removed. Covers all seven subtopics of the duo
# (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7), dwell times roughly
# proportional to subtopics.json (150/150/180/190/150/170/140 of 1130 s).

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k."""
    return DOWN * BAND * k


def strike(m):
    """Diagonal cancellation stroke through a term, teacher-style."""
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SimpleCompoundGrowthSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(13)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the two formulae and the cast
        title = Tex("Simple and Compound Growth").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        f_simple = MathTex(r"A = P(1 + in)").scale(1.25).shift(UP * 1.1 + LEFT * 3.0)
        f_comp = MathTex(r"A = P(1 + i)^n").scale(1.25).shift(UP * 1.1 + RIGHT * 3.0)
        self.play(Write(f_simple))
        self.play(Create(SurroundingRectangle(f_simple, color=GREEN)))
        self.wait(1.5)
        self.play(Write(f_comp))
        self.play(Create(SurroundingRectangle(f_comp, color=GREEN)))
        self.wait(2)
        b0_l1 = Tex(r"$P$: principal; \; $A$: accumulated amount; \; $n$: periods").scale(1.0).shift(DOWN * 0.1)
        b0_l2 = Tex(r"$i$: rate per period as a DECIMAL: $8\% \to 0{,}08$, never $8$").scale(1.0).shift(DOWN * 1.0)
        self.play(Write(b0_l1))
        self.wait(2.5)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex(r"Simple: interest on the principal only").scale(1.0).shift(DOWN * 1.9)
        b0_l4 = Tex(r"Compound: interest on principal AND on interest").scale(0.95).shift(DOWN * 2.8)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): simple growth executed
        self.next_band(1)
        b1_title = Tex(r"R5\,000 at 8\% simple interest for 3 years").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"A = P(1 + in)").scale(1.1).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"P = 5\,000, \quad i = \tfrac{8}{100} = 0{,}08, \quad n = 3").scale(1.05).shift(band_shift(1) + UP * 0.3)
        b1_l3 = MathTex(r"A = 5\,000(1 + 0{,}08 \times 3) = 5\,000 \times 1{,}24").scale(1.05).shift(band_shift(1) + DOWN * 0.6)
        b1_l4 = Tex(r"$A = $ R6\,200 — units are part of the answer").scale(1.1).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2.5)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)
        b1_l5 = Tex(r"Verify: R1\,200 interest $=$ R400 per year $= 8\%$ of $P$").scale(0.95).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l5))
        self.wait(2.5)

        # --- Band 2 (subtopic_3): compound growth executed
        self.next_band(2)
        b2_title = Tex(r"Same data, compounded annually").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"A = P(1 + i)^n = 5\,000 \times 1{,}08^3").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_wrong = MathTex(r"5\,000(1 + 0{,}08 \times 3) \;\text{under a compound heading}").scale(0.95).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2)
        b2_l2 = MathTex(r"1{,}08^2 = 1{,}1664; \quad 1{,}1664 \times 1{,}08 = 1{,}259712").scale(1.0).shift(band_shift(2) + DOWN * 0.6)
        b2_l3 = MathTex(r"A = 5\,000 \times 1{,}259712 = 6\,298{,}56").scale(1.05).shift(band_shift(2) + DOWN * 1.5)
        b2_l4 = Tex(r"$A = $ R6\,298,56 — round money at the END only").scale(1.0).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l2))
        self.wait(2.5)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): the gap, quantified
        self.next_band(3)
        b3_title = Tex(r"Where the R98,56 gap comes from").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Year 1: both pay $8\%$ of $5\,000 = $ R400").scale(1.05).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"Year 2: compound pays $8\%$ of $5\,400 = $ R432 ($+$R32)").scale(1.0).shift(band_shift(3) + UP * 0.3)
        b3_l3 = Tex(r"Year 3: $8\%$ of $5\,832 = $ R466,56 ($+$R66,56)").scale(1.0).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.wait(2.5)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = MathTex(r"32 + 66{,}56 = 98{,}56").scale(1.1).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex(r"Interest on interest — quantified, not just named").scale(1.0).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_4): choosing the formula
        self.next_band(4)
        b4_title = Tex("The scenario decides the formula").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Hire purchase $\to$ SIMPLE (CAPS convention)").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex(r"Inflation, investments, population $\to$ COMPOUND").scale(1.0).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"\text{TV: } 8\,000(1 + 0{,}12 \times 2) = 8\,000 \times 1{,}24 = 9\,920").scale(0.95).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = MathTex(r"\text{Instalment: } 9\,920 \div 24 = \text{R}413{,}33").scale(1.0).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l3))
        self.wait(2.5)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = MathTex(r"\text{Bread: } 20 \times 1{,}06^5 = 20 \times 1{,}338226 = \text{R}26{,}76").scale(0.95).shift(band_shift(4) + DOWN * 2.4)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): working backwards
        self.next_band(5)
        b5_title = Tex(r"Reverse gear: find $P$ for R10\,000 in 4 years at 6\%").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"10\,000 = P \times 1{,}06^4").scale(1.1).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"1{,}06^4 = 1{,}262477").scale(1.1).shift(band_shift(5) + UP * 0.2)
        b5_l3 = MathTex(r"P = \frac{10\,000}{1{,}262477} = 7\,920{,}94").scale(1.1).shift(band_shift(5) + DOWN * 0.9)
        b5_l4 = Tex(r"$P = $ R7\,920,94").scale(1.15).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2.5)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex(r"Verify forwards: $7\,920{,}94 \times 1{,}262477 = 10\,000$").scale(0.95).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): the wage and the taxi
        self.next_band(6)
        b6_title = Tex("Two pictures: the wage and the taxi").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"Weekend job: R400 every Saturday, fixed").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex(r"3 Saturdays $= 3 \times$ R400 $=$ R1\,200 — steady").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex(r"The taxi owner saves the earnings — they buy a 2nd taxi").scale(0.95).shift(band_shift(6) + DOWN * 0.7)
        b6_l4 = Tex(r"Both taxis earn: the taxis are buying taxis").scale(1.05).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l3))
        self.wait(2.5)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex(r"Wage $=$ simple; \; taxi fleet $=$ compound").scale(1.05).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_6): the wage way, year by year
        self.next_band(7)
        b7_title = Tex(r"R5\,000 the wage way — year by year").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"$8\%$ of R5\,000 $=$ R400: this deal's weekend wage").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex(r"Year 1: R400. \; Year 2: R400. \; Year 3: R400").scale(1.05).shift(band_shift(7) + UP * 0.2)
        b7_l3 = Tex(r"Always on the ORIGINAL R5\,000").scale(1.05).shift(band_shift(7) + DOWN * 0.7)
        b7_l4 = MathTex(r"5\,000 + 3 \times 400 = 6\,200").scale(1.1).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 8 (subtopic_6): the taxi way, year by year
        self.next_band(8)
        b8_title = Tex(r"R5\,000 the taxi way — the interest gets a job").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Year 1: $+$R400, balance R5\,400 — it JOINS the account").scale(0.95).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex(r"Year 2: $8\%$ of $5\,400 = $ R432 — R32 from last year's R400").scale(0.95).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex(r"Year 3: $8\%$ of $5\,832 = $ R466,56 — balance R6\,298,56").scale(0.95).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex(r"The formulas are just this arithmetic in a hurry:").scale(1.0).shift(band_shift(8) + DOWN * 1.6)
        b8_l5 = MathTex(r"A = P(1 + in) \quad\text{and}\quad A = P(1 + i)^n").scale(1.05).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l4))
        self.wait(2)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): which deal is in front of you?
        self.next_band(9)
        b9_title = Tex("Which deal is in front of you?").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Hire purchase ``on terms'': WAGE deal — simple").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex(r"Savings ``compounded annually'': TAXI deal").scale(1.0).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex(r"Inflation and population: rises stand on rises — taxi").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2.5)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex(r"Warning: debts can compound too — both directions").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(4)
