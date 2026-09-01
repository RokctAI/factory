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

# Band-layout whiteboard scene. One band per teaching beat; the camera moves
# down to clean space and nothing is ever removed. Covers all seven subtopics
# of the duo (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7), dwell times
# roughly proportional to subtopics.json (150/150/180/190/150/170/140 of
# 1130 s).

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
        b0_l2 = Tex(r"$i$: rate per period as a DECIMAL: $7\% \to 0{,}07$, never $7$").scale(1.0).shift(DOWN * 1.0)
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
        b1_title = Tex(r"R4\,000 at 7\% simple interest for 3 years").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"A = P(1 + in)").scale(1.1).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"P = 4\,000, \quad i = \tfrac{7}{100} = 0{,}07, \quad n = 3").scale(1.05).shift(band_shift(1) + UP * 0.3)
        b1_l3 = MathTex(r"A = 4\,000(1 + 0{,}07 \times 3) = 4\,000 \times 1{,}21").scale(1.05).shift(band_shift(1) + DOWN * 0.6)
        b1_l4 = Tex(r"$A = $ R4\,840 — units are part of the answer").scale(1.1).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2.5)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)
        b1_l5 = Tex(r"Verify: R840 interest $=$ R280 per year $= 7\%$ of $P$").scale(0.95).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l5))
        self.wait(2.5)

        # --- Band 2 (subtopic_3): compound growth executed
        self.next_band(2)
        b2_title = Tex(r"Same data, compounded annually").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"A = P(1 + i)^n = 4\,000 \times 1{,}07^3").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_wrong = MathTex(r"4\,000(1 + 0{,}07 \times 3) \;\text{under a compound heading}").scale(0.95).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2)
        b2_l2 = MathTex(r"1{,}07^2 = 1{,}1449; \quad 1{,}1449 \times 1{,}07 = 1{,}225043").scale(1.0).shift(band_shift(2) + DOWN * 0.6)
        b2_l3 = MathTex(r"A = 4\,000 \times 1{,}225043 = 4\,900{,}17").scale(1.05).shift(band_shift(2) + DOWN * 1.5)
        b2_l4 = Tex(r"$A = $ R4\,900,17 — round money at the END only").scale(1.0).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l2))
        self.wait(2.5)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): the gap, quantified
        self.next_band(3)
        b3_title = Tex(r"Where the R60,17 gap comes from").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Year 1: both pay $7\%$ of $4\,000 = $ R280").scale(1.05).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"Year 2: compound pays $7\%$ of $4\,280 = $ R299,60 ($+$R19,60)").scale(0.95).shift(band_shift(3) + UP * 0.3)
        b3_l3 = Tex(r"Year 3: $7\%$ of $4\,579,60 = $ R320,57 ($+$R40,57)").scale(1.0).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.wait(2.5)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = MathTex(r"19{,}60 + 40{,}57 = 60{,}17").scale(1.1).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex(r"Interest on interest — traced coin by coin").scale(1.0).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_4): choosing the formula
        self.next_band(4)
        b4_title = Tex("The scenario decides the formula").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Hire purchase $\to$ SIMPLE (standing convention)").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex(r"Inflation, investments, population $\to$ COMPOUND").scale(1.0).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"\text{Laptop: } 12\,000(1 + 0{,}10 \times 3) = 12\,000 \times 1{,}30 = 15\,600").scale(0.9).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = MathTex(r"\text{Instalment: } 15\,600 \div 36 = \text{R}433{,}33").scale(1.0).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l3))
        self.wait(2.5)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = MathTex(r"\text{Taxi fare: } 15 \times 1{,}05^4 = 15 \times 1{,}215506 = \text{R}18{,}23").scale(0.95).shift(band_shift(4) + DOWN * 2.4)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): working backwards
        self.next_band(5)
        b5_title = Tex(r"Reverse gear: find $P$ for R8\,000 in 3 years at 5\%").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"8\,000 = P \times 1{,}05^3").scale(1.1).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"1{,}05^3 = 1{,}157625").scale(1.1).shift(band_shift(5) + UP * 0.2)
        b5_l3 = MathTex(r"P = \frac{8\,000}{1{,}157625} = 6\,910{,}70").scale(1.1).shift(band_shift(5) + DOWN * 0.9)
        b5_l4 = Tex(r"$P = $ R6\,910,70").scale(1.15).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2.5)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex(r"Verify forwards: $6\,910{,}70 \times 1{,}157625 = 8\,000$").scale(0.95).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): the bicycle and the hens
        self.next_band(6)
        b6_title = Tex("Two pictures: the bicycle and the hens").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"Bicycle rented out: R280 every month, fixed").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex(r"3 months $= 3 \times$ R280 $=$ R840 — steady").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex(r"The aunt lets eggs hatch — new hens start laying").scale(0.95).shift(band_shift(6) + DOWN * 0.7)
        b6_l4 = Tex(r"More hens, more eggs, more hens: hens raising hens").scale(1.0).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l3))
        self.wait(2.5)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex(r"Bicycle $=$ simple; \; hen coop $=$ compound").scale(1.05).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_6): the bicycle way, year by year
        self.next_band(7)
        b7_title = Tex(r"R4\,000 the bicycle way — year by year").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"$7\%$ of R4\,000 $=$ R280: this deal's flat rent").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex(r"Year 1: R280. \; Year 2: R280. \; Year 3: R280").scale(1.05).shift(band_shift(7) + UP * 0.2)
        b7_l3 = Tex(r"Always on the ORIGINAL R4\,000").scale(1.05).shift(band_shift(7) + DOWN * 0.7)
        b7_l4 = MathTex(r"4\,000 + 3 \times 280 = 4\,840").scale(1.1).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 8 (subtopic_6): the hen-coop way, year by year
        self.next_band(8)
        b8_title = Tex(r"R4\,000 the hen-coop way — the interest hatches").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Year 1: $+$R280, balance R4\,280 — it JOINS the balance").scale(0.95).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex(r"Year 2: $7\%$ of $4\,280 = $ R299,60 — R19,60 from last year's R280").scale(0.9).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex(r"Year 3: $7\%$ of $4\,579,60 = $ R320,57 — balance R4\,900,17").scale(0.9).shift(band_shift(8) + DOWN * 0.7)
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
        b9_l1 = Tex(r"Hire purchase ``on terms'': BICYCLE deal — simple").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex(r"Savings ``compounded annually'': HEN-COOP deal").scale(1.0).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex(r"Inflation and population: rises stand on rises — hen coop").scale(0.95).shift(band_shift(9) + DOWN * 0.7)
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
