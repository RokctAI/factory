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

# Band-layout whiteboard scene for the session duo "Price Elasticity of
# Demand" (Grade 11, Term 2). One band per teaching step; the camera moves
# down to fresh space and nothing is removed. Exporter-safe mobjects only;
# the steep/flat demand sketches are hand-built from Arrows and Lines. Band
# time apportioned to subtopics.json (235/235/230/240/195/195/210 of 1540 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PriceElasticityOfDemandSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the formula ---
        title = Tex("Price Elasticity of Demand").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        f1 = Tex(r"Elasticity $=$ \% change in quantity demanded").scale(1.0).shift(UP * 1.1)
        f2 = Tex(r"$\div$ \% change in price").scale(1.0).shift(UP * 0.3)
        self.play(Write(f1))
        self.wait(2)
        self.play(Write(f2))
        self.wait(2.5)
        f3 = MathTex(r"\%\ \text{change} = \frac{\text{change}}{\text{ORIGINAL value}} \times 100").scale(1.0).shift(DOWN * 0.9)
        self.play(Write(f3))
        self.play(Create(SurroundingRectangle(f3, color=GREEN)))
        self.wait(2)
        f4 = Tex("Original on the bottom — always").scale(1.0).shift(DOWN * 2.0)
        self.play(Write(f4))
        self.wait(3)

        # --- Band 1 (subtopic_1): bus pass worked example ---
        self.next_band(1)
        b1_title = Tex("Bus pass: R500 $\\rightarrow$ R575, riders 2 000 $\\rightarrow$ 1 880").scale(1.0).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(2)
        e1 = MathTex(r"\text{Price: } 75 \div 500 \times 100 = 15\%").scale(1.0).shift(band_shift(1) + UP * 1.2)
        e2 = MathTex(r"\text{Quantity: } 120 \div 2000 \times 100 = 6\%").scale(1.0).shift(band_shift(1) + UP * 0.3)
        e3 = MathTex(r"6\% \div 15\% = 0{,}4").scale(1.1).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(e1))
        self.wait(2.5)
        self.play(Write(e2))
        self.wait(2.5)
        self.play(Write(e3))
        self.play(Create(SurroundingRectangle(e3, color=GREEN)))
        self.wait(2)
        e4 = Tex(r"Strictly $-0{,}4$: state the sign, use the size").scale(0.95).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(e4))
        self.wait(3)

        # --- Band 2 (subtopic_1): car wash example for contrast ---
        self.next_band(2)
        b2_title = Tex("Car wash: R60 $\\rightarrow$ R75, washes 240 $\\rightarrow$ 144").scale(1.0).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(2)
        g1 = MathTex(r"\text{Price: } 15 \div 60 \times 100 = 25\%").scale(1.0).shift(band_shift(2) + UP * 1.2)
        g2 = MathTex(r"\text{Quantity: } 96 \div 240 \times 100 = 40\%").scale(1.0).shift(band_shift(2) + UP * 0.3)
        g3 = MathTex(r"40\% \div 25\% = 1{,}6").scale(1.1).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(g1))
        self.wait(2.5)
        self.play(Write(g2))
        self.wait(2.5)
        self.play(Write(g3))
        self.play(Create(SurroundingRectangle(g3, color=GREEN)))
        self.wait(2)
        g4 = Tex(r"Two services, one scale: $0{,}4$ vs $1{,}6$").scale(1.0).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(g4))
        self.wait(3)

        # --- Band 3 (subtopic_2): the five zones, steep vs flat sketch ---
        self.next_band(3)
        b3_title = Tex("The five zones of the elasticity scale").scale(1.1).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_title))
        self.wait(1.5)
        z1 = Tex(r"$>1$: elastic \quad $<1$: inelastic \quad $=1$: unitary").scale(0.95).shift(band_shift(3) + UP * 1.6)
        self.play(Write(z1))
        self.wait(2)
        org = band_shift(3) + LEFT * 5.2 + DOWN * 2.6
        ax_y = Arrow(org, org + UP * 3.6, buff=0)
        ax_x = Arrow(org, org + RIGHT * 9.6, buff=0)
        ylab = Tex("P").scale(0.8).move_to(org + UP * 3.6 + RIGHT * 0.5)
        xlab = Tex("Q").scale(0.8).move_to(org + RIGHT * 9.6 + UP * 0.4)
        self.play(Create(ax_y), Create(ax_x), Write(ylab), Write(xlab))
        self.wait(1.5)
        steep = Line(org + RIGHT * 2.0 + UP * 3.2, org + RIGHT * 3.4 + UP * 0.3, stroke_width=5)
        steep_lab = Tex("steep: relatively inelastic").scale(0.7).move_to(org + RIGHT * 2.6 + UP * 3.5)
        self.play(Create(steep), Write(steep_lab))
        self.wait(2)
        flat = Line(org + RIGHT * 4.6 + UP * 2.4, org + RIGHT * 9.0 + UP * 1.0, stroke_width=5, color=BLUE)
        flat_lab = Tex("flat: relatively elastic").scale(0.7).move_to(org + RIGHT * 7.6 + UP * 2.8)
        self.play(Create(flat), Write(flat_lab))
        self.wait(3)

        # --- Band 4 (subtopic_2): the two extremes + slope warning ---
        self.next_band(4)
        b4_title = Tex("The two textbook extremes").scale(1.1).shift(band_shift(4) + UP * 2.5)
        self.play(Write(b4_title))
        self.wait(1.5)
        org2 = band_shift(4) + LEFT * 5.2 + DOWN * 2.2
        ax2_y = Arrow(org2, org2 + UP * 3.4, buff=0)
        ax2_x = Arrow(org2, org2 + RIGHT * 9.6, buff=0)
        self.play(Create(ax2_y), Create(ax2_x))
        vert = Line(org2 + RIGHT * 2.6, org2 + RIGHT * 2.6 + UP * 3.0, stroke_width=5)
        vert_lab = Tex(r"$e = 0$: perfectly inelastic (insulin)").scale(0.7).move_to(org2 + RIGHT * 2.9 + UP * 3.3)
        self.play(Create(vert), Write(vert_lab))
        self.wait(2)
        horiz = Line(org2 + RIGHT * 4.4 + UP * 1.6, org2 + RIGHT * 9.2 + UP * 1.6, stroke_width=5, color=BLUE)
        horiz_lab = Tex(r"$e = \infty$: perfectly elastic (one maize farmer)").scale(0.7).move_to(org2 + RIGHT * 6.8 + UP * 2.1)
        self.play(Create(horiz), Write(horiz_lab))
        self.wait(2)
        warn1 = Tex(r"``This curve IS elastic'' — from shape alone").scale(0.9).shift(band_shift(4) + UP * 1.4)
        self.play(Write(warn1))
        self.play(Create(strike(warn1)))
        self.wait(1.5)
        warn2 = Tex("Elasticity changes along a straight curve: calculate").scale(0.9).shift(band_shift(4) + UP * 0.5)
        self.play(Write(warn2))
        self.play(Create(SurroundingRectangle(warn2, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the determinants ---
        self.next_band(5)
        b5_title = Tex("What decides the number: five determinants").scale(1.1).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(1.5)
        d1 = Tex("1. Substitutes available? (the big one)").scale(0.95).shift(band_shift(5) + UP * 1.4)
        d2 = Tex("2. Necessity or luxury?").scale(0.95).shift(band_shift(5) + UP * 0.6)
        d3 = Tex("3. Share of income claimed?").scale(0.95).shift(band_shift(5) + DOWN * 0.2)
        d4 = Tex("4. Time to adjust?").scale(0.95).shift(band_shift(5) + DOWN * 1.0)
        d5 = Tex("5. Habit and addiction?").scale(0.95).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(d1))
        self.wait(2)
        self.play(Write(d2))
        self.wait(1.5)
        self.play(Write(d3))
        self.wait(1.5)
        self.play(Write(d4))
        self.wait(1.5)
        self.play(Write(d5))
        self.wait(2)
        d6 = Tex("Essays: determinant $+$ good $+$ because-sentence").scale(0.9).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(d6))
        self.play(Create(SurroundingRectangle(d6, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): elasticity and total revenue — bus ---
        self.next_band(6)
        b6_title = Tex(r"Total revenue $=$ price $\times$ quantity").scale(1.1).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(1.5)
        t1 = MathTex(r"\text{Before: } 500 \times 2000 = \text{R}1\,000\,000").scale(1.0).shift(band_shift(6) + UP * 1.2)
        t2 = MathTex(r"\text{After: } 575 \times 1880 = \text{R}1\,081\,000").scale(1.0).shift(band_shift(6) + UP * 0.3)
        self.play(Write(t1))
        self.wait(2.5)
        self.play(Write(t2))
        self.wait(2.5)
        t3 = Tex(r"Inelastic ($0{,}4$): price up, revenue UP R81 000").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(t3))
        self.play(Create(SurroundingRectangle(t3, color=GREEN)))
        self.wait(2)
        t4 = Tex("The stayers pay more than the leavers take away").scale(0.95).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(t4))
        self.wait(3)

        # --- Band 7 (subtopic_4): car-wash revenue + the rulebook ---
        self.next_band(7)
        b7_title = Tex("The car wash tries the same trick").scale(1.1).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(1.5)
        u1 = MathTex(r"\text{Before: } 60 \times 240 = \text{R}14\,400").scale(1.0).shift(band_shift(7) + UP * 1.3)
        u2 = MathTex(r"\text{After: } 75 \times 144 = \text{R}10\,800").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(u1))
        self.wait(2.5)
        self.play(Write(u2))
        self.wait(2.5)
        u3 = Tex(r"Elastic ($1{,}6$): price up, revenue DOWN R3 600").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(u3))
        self.play(Create(strike(u3)))
        self.wait(2)
        u4 = Tex("Inelastic: raise. Elastic: cut. Unitary: revenue still.").scale(0.95).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(u4))
        self.play(Create(SurroundingRectangle(u4, color=GREEN)))
        self.wait(2)
        u5 = Tex("Caution: revenue is not profit").scale(0.9).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(u5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the shrug test — stones and feathers ---
        self.next_band(8)
        b8_title = Tex("The shrug test: watch what buyers DO").scale(1.1).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        s1 = Tex("Electricity up: loud ouch, everyone still loads units").scale(0.95).shift(band_shift(8) + UP * 1.3)
        s2 = Tex("Energy drinks up: quiet ouch, hands drift to rivals").scale(0.95).shift(band_shift(8) + UP * 0.4)
        self.play(Write(s1))
        self.wait(2)
        self.play(Write(s2))
        self.wait(2)
        s3 = Tex("STONE: push it, it sits. FEATHER: push it, it flies.").scale(0.95).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(s3))
        self.play(Create(SurroundingRectangle(s3, color=GREEN)))
        self.wait(2)
        s4 = MathTex(r"6 \div 15 = 0{,}4 \text{ (stone)} \quad 40 \div 25 = 1{,}6 \text{ (feather)}").scale(0.9).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(s4))
        self.wait(3)

        # --- Band 9 (subtopic_6): the four everyday questions ---
        self.next_band(9)
        b9_title = Tex("Four questions call it before the calculator").scale(1.05).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        k1 = Tex("1. Is there a way out? (substitutes)").scale(0.95).shift(band_shift(9) + UP * 1.4)
        k2 = Tex("2. Must-have or nice-to-have?").scale(0.95).shift(band_shift(9) + UP * 0.6)
        k3 = Tex("3. How big a bite of the budget?").scale(0.95).shift(band_shift(9) + DOWN * 0.2)
        k4 = Tex("4. How much time to adjust?").scale(0.95).shift(band_shift(9) + DOWN * 1.0)
        self.play(Write(k1))
        self.wait(2)
        self.play(Write(k2))
        self.wait(1.5)
        self.play(Write(k3))
        self.wait(1.5)
        self.play(Write(k4))
        self.wait(2)
        k5 = Tex("Maize meal: stone. Ice lollies: feathers.").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(k5))
        self.play(Create(SurroundingRectangle(k5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): Zanele's dilemma ---
        self.next_band(10)
        b10_title = Tex("One week at Zanele's spaza").scale(1.15).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        z1 = Tex(r"Monday: maize meal $+10\%$ — stone — tin fills faster").scale(0.95).shift(band_shift(10) + UP * 1.3)
        self.play(Write(z1))
        self.wait(2.5)
        z2 = MathTex(r"\text{Lollies before: } 10 \times 300 = \text{R}3\,000").scale(0.95).shift(band_shift(10) + UP * 0.4)
        z3 = MathTex(r"\text{Lollies after: } 12 \times 210 = \text{R}2\,520").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(z2))
        self.wait(2)
        self.play(Write(z3))
        self.play(Create(strike(z3)))
        self.wait(2)
        z4 = Tex(r"Feather: price up, R480 gone from the tin").scale(1.0).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(z4))
        self.wait(2)
        z5 = Tex("Stone: push price up. Feather: pull price down.").scale(1.0).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(z5))
        self.play(Create(SurroundingRectangle(z5, color=GREEN)))
        self.wait(4)
