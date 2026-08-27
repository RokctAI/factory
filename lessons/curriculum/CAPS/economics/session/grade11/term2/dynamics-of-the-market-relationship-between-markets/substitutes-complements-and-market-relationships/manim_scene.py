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

# Band-layout whiteboard scene for the session duo "Substitutes, Complements
# and Market Relationships" (Grade 11, Term 2). One band per teaching step;
# the camera moves down and nothing is removed. Exporter-safe mobjects only;
# the demand-shift diagram is hand-built from Arrows and chained Lines. Band
# time apportioned to subtopics.json (220/240/230/240/200/190/200 of 1520 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MarketRelationshipsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): price vs relative price ---
        title = Tex("Markets Talk to Each Other").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        r1 = Tex(r"Chicken R70/kg — seventy compared to WHAT?").scale(1.05).shift(UP * 1.1)
        self.play(Write(r1))
        self.wait(2)
        r2 = MathTex(r"\text{Relative price: } \frac{70}{140} = \text{half the price of beef}").scale(0.91).shift(UP * 0.1)
        self.play(Write(r2))
        self.wait(2.5)
        r3 = Tex("The signal that steers spending is the RELATIVE price").scale(1.0).shift(DOWN * 0.9)
        self.play(Write(r3))
        self.play(Create(SurroundingRectangle(r3, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the doubling experiment + along vs shift ---
        self.next_band(1)
        b1_title = Tex("The doubling thought experiment").scale(1.15).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        d1 = Tex(r"ALL prices double, income doubles: choices unchanged").scale(0.95).shift(band_shift(1) + UP * 1.3)
        self.play(Write(d1))
        self.wait(2.5)
        d2 = Tex(r"Only beef doubles: chicken is relatively cheaper").scale(0.95).shift(band_shift(1) + UP * 0.4)
        d3 = Tex("Shoppers swing to chicken — its tag never moved").scale(0.95).shift(band_shift(1) + DOWN * 0.5)
        self.play(Write(d2))
        self.wait(2)
        self.play(Write(d3))
        self.wait(2.5)
        d4 = Tex(r"Own price changes: move ALONG the demand curve").scale(0.95).shift(band_shift(1) + DOWN * 1.5)
        d5 = Tex(r"Anything else changes: the WHOLE curve SHIFTS").scale(0.95).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(d4))
        self.wait(2)
        self.play(Write(d5))
        self.play(Create(SurroundingRectangle(VGroup(d4, d5), color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): substitutes — beef demand shifts right ---
        self.next_band(2)
        b2_title = Tex(r"Substitutes: chicken R70 $\to$ R95, watch BEEF").scale(1.05).shift(band_shift(2) + UP * 2.5)
        self.play(Write(b2_title))
        self.wait(2)
        org = band_shift(2) + LEFT * 4.6 + DOWN * 2.5
        ax_y = Arrow(org, org + UP * 4.2, buff=0)
        ax_x = Arrow(org, org + RIGHT * 7.6, buff=0)
        ylab = Tex("P (beef)").scale(0.8).move_to(org + UP * 4.2 + RIGHT * 1.1)
        xlab = Tex("Q (beef)").scale(0.8).move_to(org + RIGHT * 7.6 + UP * 0.4)
        self.play(Create(ax_y), Create(ax_x), Write(ylab), Write(xlab))
        self.wait(1.5)
        d_old_1 = Line(org + RIGHT * 0.8 + UP * 3.4, org + RIGHT * 2.6 + UP * 1.8, stroke_width=5)
        d_old_2 = Line(org + RIGHT * 2.6 + UP * 1.8, org + RIGHT * 4.4 + UP * 0.6, stroke_width=5)
        d_old_lab = Tex(r"$D_1$").scale(0.8).move_to(org + RIGHT * 4.8 + UP * 0.4)
        self.play(Create(d_old_1), Create(d_old_2), Write(d_old_lab))
        self.wait(2)
        d_new_1 = Line(org + RIGHT * 2.4 + UP * 3.4, org + RIGHT * 4.2 + UP * 1.8, stroke_width=5, color=BLUE)
        d_new_2 = Line(org + RIGHT * 4.2 + UP * 1.8, org + RIGHT * 6.0 + UP * 0.6, stroke_width=5, color=BLUE)
        d_new_lab = Tex(r"$D_2$").scale(0.8).move_to(org + RIGHT * 6.4 + UP * 0.4)
        shift_arrow = Arrow(org + RIGHT * 2.7 + UP * 2.4, org + RIGHT * 4.3 + UP * 2.4, buff=0, color=BLUE)
        self.play(Create(d_new_1), Create(d_new_2), Write(d_new_lab))
        self.play(Create(shift_arrow))
        self.wait(2)
        note = Tex("Whole curve steps RIGHT — beef's own price unchanged").scale(0.85).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(note))
        self.wait(2)
        rule = Tex("Substitute's price up: my demand shifts right").scale(0.9).shift(band_shift(2) + RIGHT * 2.4 + UP * 1.6)
        self.play(Write(rule))
        self.play(Create(SurroundingRectangle(rule, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): complements + the symmetry rule ---
        self.next_band(3)
        b3_title = Tex("Complements: consumed together").scale(1.15).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        c1 = Tex(r"Phones cheaper $\Rightarrow$ data demand shifts RIGHT").scale(0.95).shift(band_shift(3) + UP * 1.3)
        self.play(Write(c1))
        self.wait(2.5)
        c2 = Tex(r"Cars pricier $\Rightarrow$ petrol demand shifts LEFT").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(c2))
        self.wait(2.5)
        c3 = Tex("Substitutes: related price and my demand move TOGETHER").scale(0.9).shift(band_shift(3) + DOWN * 0.6)
        c4 = Tex("Complements: they move in OPPOSITE directions").scale(0.9).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(c3))
        self.wait(2)
        self.play(Write(c4))
        self.play(Create(SurroundingRectangle(VGroup(c3, c4), color=GREEN)))
        self.wait(2)
        c5 = Tex("Pairs: chicken/beef, butter/margarine; phone/data, car/petrol").scale(0.85).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(c5))
        self.wait(3)

        # --- Band 4 (subtopic_3): derived demand — the forward loop ---
        self.next_band(4)
        b4_title = Tex("Product markets, factor markets, derived demand").scale(1.05).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        e1 = Tex("Demand for bricklayers is DERIVED from houses").scale(0.95).shift(band_shift(4) + UP * 1.5)
        self.play(Write(e1))
        self.play(Create(SurroundingRectangle(e1, color=GREEN)))
        self.wait(2.5)
        pm = Rectangle(width=4.6, height=1.1).shift(band_shift(4) + LEFT * 3.2 + UP * 0.2)
        pm_lab = Tex("Product market: houses").scale(0.75).move_to(pm.get_center())
        fm = Rectangle(width=4.6, height=1.1).shift(band_shift(4) + RIGHT * 3.2 + UP * 0.2)
        fm_lab = Tex("Factor markets: labour, cement").scale(0.7).move_to(fm.get_center())
        self.play(Create(pm), Write(pm_lab))
        self.play(Create(fm), Write(fm_lab))
        self.wait(1.5)
        fwd = Arrow(pm.get_right() + UP * 0.15, fm.get_left() + UP * 0.15, buff=0.1)
        fwd_lab = Tex("derived demand").scale(0.7).shift(band_shift(4) + UP * 1.0)
        self.play(Create(fwd), Write(fwd_lab))
        self.wait(2)
        f1 = Tex("Gauteng housing surges: wages bid up, cement climbs").scale(0.9).shift(band_shift(4) + DOWN * 1.0)
        self.play(Write(f1))
        self.wait(2)
        back = Arrow(fm.get_left() + DOWN * 0.15, pm.get_right() + DOWN * 0.15, buff=0.1, color=RED)
        back_lab = Tex("higher costs push back").scale(0.7).shift(band_shift(4) + DOWN * 0.55)
        self.play(Create(back), Write(back_lab))
        self.wait(2)
        f2 = Tex("Higher factor prices: product supply LEFT, prices up").scale(0.9).shift(band_shift(4) + DOWN * 1.9)
        f3 = Tex("Wages become income, income becomes spending").scale(0.9).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(f2))
        self.wait(2)
        self.play(Write(f3))
        self.wait(3)

        # --- Band 5 (subtopic_4): the four market structures ---
        self.next_band(5)
        b5_title = Tex("The four market structures: a first map").scale(1.1).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(1.5)
        s1 = Tex("1. Perfect competition: many sellers, identical, free entry").scale(0.85).shift(band_shift(5) + UP * 1.4)
        s2 = Tex("2. Monopolistic competition: many, differentiated").scale(0.9).shift(band_shift(5) + UP * 0.55)
        s3 = Tex("3. Oligopoly: few large sellers, hard entry, interdependent").scale(0.85).shift(band_shift(5) + DOWN * 0.3)
        s4 = Tex("4. Monopoly: one seller, no close substitute, blocked entry").scale(0.85).shift(band_shift(5) + DOWN * 1.15)
        for m in (s1, s2, s3, s4):
            self.play(Write(m))
            self.wait(2)
        s5 = Tex("Tomato farmer; salon; banks and networks; Eskom grid").scale(0.85).shift(band_shift(5) + DOWN * 2.05)
        self.play(Write(s5))
        self.wait(2)
        s6 = Tex("Collusion is illegal: Competition Commission, bread case").scale(0.85).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(s6))
        self.wait(3)

        # --- Band 6 (subtopic_4): perfect vs imperfect, the two questions ---
        self.next_band(6)
        b6_title = Tex("Perfect or imperfect?").scale(1.15).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(1.5)
        g1 = Tex("Perfect competition: price TAKERS — the only perfect market").scale(0.85).shift(band_shift(6) + UP * 1.3)
        self.play(Write(g1))
        self.wait(2)
        g2 = Tex("The other three are IMPERFECT: some power over price").scale(0.9).shift(band_shift(6) + UP * 0.4)
        self.play(Write(g2))
        self.wait(2)
        g3 = Tex("Monopolist: a price MAKER, disciplined only by buyers").scale(0.9).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(g3))
        self.wait(2)
        g4 = Tex("Sort any market: how many sellers? how hard is entry?").scale(0.9).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(g4))
        self.play(Create(SurroundingRectangle(g4, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the fridge decides ---
        self.next_band(7)
        b7_title = Tex("The fridge decides: the compared price").scale(1.1).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(2)
        h1 = Tex(r"``Is chicken expensive?'' — asked in mid-air").scale(0.95).shift(band_shift(7) + UP * 1.4)
        self.play(Write(h1))
        self.play(Create(strike(h1)))
        self.wait(1.5)
        h2 = Tex(r"``Is chicken expensive COMPARED TO beef?''").scale(0.95).shift(band_shift(7) + UP * 0.5)
        self.play(Write(h2))
        self.wait(2)
        h3 = Tex("Same job: substitutes. Job done together: complements.").scale(0.9).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(h3))
        self.wait(2.5)
        h4 = Tex(r"Bird flu: chicken to R95 — beef's whole curve steps RIGHT").scale(0.85).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(h4))
        self.wait(2)
        h5 = Tex("Rivals move together; partners move apart").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(h5))
        self.play(Create(SurroundingRectangle(h5, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): every job hides inside a purchase ---
        self.next_band(8)
        b8_title = Tex("Every job hides inside something somebody buys").scale(1.0).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        j1 = Tex("The want for the house comes FIRST;").scale(0.95).shift(band_shift(8) + UP * 1.4)
        j2 = Tex("the want for the bricklayer is borrowed from it").scale(0.95).shift(band_shift(8) + UP * 0.6)
        self.play(Write(j1))
        self.play(Write(j2))
        self.wait(2.5)
        j3 = Tex(r"Building spree $\Rightarrow$ wages bid up, cement surges, loans").scale(0.85).shift(band_shift(8) + DOWN * 0.3)
        self.play(Write(j3))
        self.wait(2)
        j4 = Tex(r"Hands pull back: costs rise $\Rightarrow$ house prices nudge up").scale(0.85).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(j4))
        self.wait(2)
        j5 = Tex("Fatter pay packets become spending at the shops").scale(0.9).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(j5))
        self.wait(2)
        j6 = Tex("Shops and jobs: two halves of one loop").scale(0.95).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(j6))
        self.play(Create(SurroundingRectangle(j6, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): count the sellers — the ladder ---
        self.next_band(9)
        b9_title = Tex("Count the sellers, test the entry door").scale(1.1).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        l1 = Tex("50 tomato sellers, same tomatoes: price TAKERS").scale(0.9).shift(band_shift(9) + UP * 1.4)
        l2 = Tex("Takeaways on one route: a rand or two of power").scale(0.9).shift(band_shift(9) + UP * 0.55)
        l3 = Tex("A handful of networks, billions to enter: oligopoly").scale(0.9).shift(band_shift(9) + DOWN * 0.3)
        l4 = Tex("One grid past your house: monopoly, price MAKER").scale(0.9).shift(band_shift(9) + DOWN * 1.15)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2)
        l5 = Tex("Fewer sellers $+$ harder entry $=$ more price power").scale(0.95).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(l5))
        self.play(Create(SurroundingRectangle(l5, color=GREEN)))
        self.wait(2)
        l6 = Tex("Colluding instead of competing — illegal (bread case)").scale(0.85).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(l6))
        self.wait(4)
