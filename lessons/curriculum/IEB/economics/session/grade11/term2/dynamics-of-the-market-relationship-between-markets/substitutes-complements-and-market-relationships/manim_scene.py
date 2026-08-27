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
# the camera moves down to fresh space and nothing is removed. Exporter-safe
# mobjects only; the demand-shift diagram is hand-built from Arrows and
# Lines. Band time apportioned to subtopics.json
# (220/240/230/240/200/190/200 of 1520 s).

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
        title = Tex("Substitutes, Complements and Market Relationships").scale(1.0).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        p1 = Tex(r"Money price: rice R30/kg, maize meal R15/kg").scale(1.0).shift(UP * 1.1)
        self.play(Write(p1))
        self.wait(2)
        p2 = Tex(r"Relative price: rice costs TWO maize meals").scale(1.0).shift(UP * 0.2)
        self.play(Write(p2))
        self.play(Create(SurroundingRectangle(p2, color=GREEN)))
        self.wait(2)
        p3 = Tex("The compared price is the signal buyers read").scale(1.0).shift(DOWN * 0.8)
        self.play(Write(p3))
        self.wait(3)

        # --- Band 1 (subtopic_1): the doubling experiment + along vs shift ---
        self.next_band(1)
        b1_title = Tex("The doubling thought experiment").scale(1.1).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        d1 = Tex("ALL prices double, income doubles: choices unchanged").scale(0.95).shift(band_shift(1) + UP * 1.3)
        self.play(Write(d1))
        self.wait(2.5)
        d2 = Tex("Only rice doubles: maize meal is relatively cheaper").scale(0.95).shift(band_shift(1) + UP * 0.4)
        self.play(Write(d2))
        self.wait(2.5)
        d3 = Tex("Own price changes: move ALONG the demand curve").scale(0.95).shift(band_shift(1) + DOWN * 0.6)
        d4 = Tex("Anything else changes: the WHOLE curve SHIFTS").scale(0.95).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(d3))
        self.wait(2)
        self.play(Write(d4))
        self.play(Create(SurroundingRectangle(VGroup(d3, d4), color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): substitutes — margarine demand shifts right ---
        self.next_band(2)
        b2_title = Tex("Butter R60 $\\rightarrow$ R85: the margarine market").scale(1.05).shift(band_shift(2) + UP * 2.6)
        self.play(Write(b2_title))
        self.wait(1.5)
        org = band_shift(2) + LEFT * 4.8 + DOWN * 2.8
        ax_y = Arrow(org, org + UP * 4.6, buff=0)
        ax_x = Arrow(org, org + RIGHT * 9.0, buff=0)
        ylab = Tex("P").scale(0.8).move_to(org + UP * 4.6 + RIGHT * 0.5)
        xlab = Tex("Q").scale(0.8).move_to(org + RIGHT * 9.0 + UP * 0.4)
        self.play(Create(ax_y), Create(ax_x), Write(ylab), Write(xlab))
        self.wait(1.5)
        d_old = Line(org + RIGHT * 1.2 + UP * 3.8, org + RIGHT * 5.4 + UP * 0.6, stroke_width=5)
        d_old_lab = Tex(r"$D_1$").scale(0.8).move_to(org + RIGHT * 5.8 + UP * 0.5)
        self.play(Create(d_old), Write(d_old_lab))
        self.wait(2)
        d_new = Line(org + RIGHT * 3.0 + UP * 3.8, org + RIGHT * 7.2 + UP * 0.6, stroke_width=5, color=BLUE)
        d_new_lab = Tex(r"$D_2$").scale(0.8).move_to(org + RIGHT * 7.6 + UP * 0.5)
        arr = Arrow(org + RIGHT * 3.6 + UP * 2.4, org + RIGHT * 5.2 + UP * 2.4, buff=0, color=YELLOW)
        self.play(Create(d_new), Write(d_new_lab), Create(arr))
        self.wait(2)
        s_rule = Tex("Substitute's price UP: demand shifts RIGHT").scale(0.9).shift(band_shift(2) + DOWN * 3.2)
        self.play(Write(s_rule))
        self.play(Create(SurroundingRectangle(s_rule, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): complements + the symmetry rule ---
        self.next_band(3)
        b3_title = Tex("Complements: partners, not rivals").scale(1.1).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        c1 = Tex("Smart TVs cheaper: streaming demand shifts RIGHT").scale(0.95).shift(band_shift(3) + UP * 1.3)
        self.play(Write(c1))
        self.wait(2.5)
        c2 = Tex("Mobile data dearer: streaming demand shifts LEFT").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(c2))
        self.wait(2.5)
        c3 = Tex("Substitutes: related price and my demand move TOGETHER").scale(0.9).shift(band_shift(3) + DOWN * 0.6)
        c4 = Tex("Complements: they move APART").scale(0.9).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(c3))
        self.wait(2)
        self.play(Write(c4))
        self.play(Create(SurroundingRectangle(VGroup(c3, c4), color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): derived demand — the loop ---
        self.next_band(4)
        b4_title = Tex("Derived demand: the loop between markets").scale(1.05).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        l1 = Tex("Solar boom in the product market").scale(0.95).shift(band_shift(4) + UP * 1.4)
        self.play(Write(l1))
        self.wait(2)
        l2 = Tex(r"$\Rightarrow$ factor markets: electricians, panels, loans").scale(0.95).shift(band_shift(4) + UP * 0.5)
        self.play(Write(l2))
        self.wait(2)
        l3 = Tex("Forward: product demand lifts wages and factor prices").scale(0.9).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(l3))
        self.wait(2)
        l4 = Tex("Backward: higher costs shift product supply LEFT").scale(0.9).shift(band_shift(4) + DOWN * 1.4)
        self.play(Write(l4))
        self.wait(2)
        l5 = Tex("Circular flow: wages return as spending").scale(0.9).shift(band_shift(4) + DOWN * 2.3)
        self.play(Write(l5))
        self.play(Create(SurroundingRectangle(l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): the four market structures ---
        self.next_band(5)
        b5_title = Tex("The four market structures").scale(1.15).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(1.5)
        m1 = Tex("1. Perfect competition: very many, identical, free entry").scale(0.85).shift(band_shift(5) + UP * 1.4)
        m2 = Tex("2. Monopolistic competition: many, differentiated").scale(0.85).shift(band_shift(5) + UP * 0.6)
        m3 = Tex("3. Oligopoly: few, hard entry, interdependent").scale(0.85).shift(band_shift(5) + DOWN * 0.2)
        m4 = Tex("4. Monopoly: one seller, blocked entry, price maker").scale(0.85).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(m1))
        self.wait(2)
        self.play(Write(m2))
        self.wait(2)
        self.play(Write(m3))
        self.wait(2)
        self.play(Write(m4))
        self.wait(2)
        m5 = Tex("Collusion is illegal: the Competition Commission polices it").scale(0.8).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(m5))
        self.wait(3)

        # --- Band 6 (subtopic_4): perfect vs imperfect, the two questions ---
        self.next_band(6)
        b6_title = Tex("Perfect vs imperfect markets").scale(1.15).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(1.5)
        q1 = Tex("Only perfect competition is a PERFECT market").scale(1.0).shift(band_shift(6) + UP * 1.3)
        self.play(Write(q1))
        self.wait(2)
        q2 = Tex("The other three: sellers hold power over price").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(q2))
        self.wait(2)
        q3 = Tex("Sorting question 1: how many sellers?").scale(0.95).shift(band_shift(6) + DOWN * 0.6)
        q4 = Tex("Sorting question 2: how hard is the entry door?").scale(0.95).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(q3))
        self.wait(2)
        self.play(Write(q4))
        self.play(Create(SurroundingRectangle(VGroup(q3, q4), color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the shelf decides ---
        self.next_band(7)
        b7_title = Tex("The shelf decides: rice vs maize meal").scale(1.1).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(2)
        f1 = Tex(r"Rice R30, maize meal R15: the compared price steers").scale(0.95).shift(band_shift(7) + UP * 1.3)
        self.play(Write(f1))
        self.wait(2)
        f2 = Tex("Poor harvest: maize meal jumps to R25").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(f2))
        self.wait(2)
        f3 = Tex("Rice's tag unmoved, yet rice demand steps RIGHT").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(f3))
        self.play(Create(SurroundingRectangle(f3, color=GREEN)))
        self.wait(2)
        f4 = Tex("Bread pricey: polony demand steps LEFT").scale(0.95).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(f4))
        self.wait(2)
        f5 = Tex("Rivals move together; partners move apart").scale(1.0).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(f5))
        self.wait(3)

        # --- Band 8 (subtopic_6): every job hides inside a purchase ---
        self.next_band(8)
        b8_title = Tex("Every job hides inside something somebody buys").scale(1.0).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        j1 = Tex("The electrician inside the powered home").scale(0.95).shift(band_shift(8) + UP * 1.3)
        j2 = Tex("The driver inside the delivery; the miner inside the battery").scale(0.9).shift(band_shift(8) + UP * 0.4)
        self.play(Write(j1))
        self.wait(2)
        self.play(Write(j2))
        self.wait(2)
        j3 = Tex("Solar spree: wages bid up, imports surge, loans written").scale(0.9).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(j3))
        self.wait(2)
        j4 = Tex("Costs pull back: dearer factors, dearer installations").scale(0.9).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(j4))
        self.wait(2)
        j5 = Tex("Tills and jobs: two halves of one loop").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(j5))
        self.play(Create(SurroundingRectangle(j5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): count the sellers — the ladder ---
        self.next_band(9)
        b9_title = Tex("Count the sellers: the ladder of price power").scale(1.05).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        r1 = Tex("40 spinach stalls: price TAKER").scale(0.9).shift(band_shift(9) + UP * 1.4)
        r2 = Tex("Salons on the main road: price NUDGER").scale(0.9).shift(band_shift(9) + UP * 0.6)
        r3 = Tex("A handful of airlines: rival WATCHER").scale(0.9).shift(band_shift(9) + DOWN * 0.2)
        r4 = Tex("One set of water pipes: price MAKER").scale(0.9).shift(band_shift(9) + DOWN * 1.0)
        self.play(Write(r1))
        self.wait(2)
        self.play(Write(r2))
        self.wait(2)
        self.play(Write(r3))
        self.wait(2)
        self.play(Write(r4))
        self.wait(2)
        r5 = Tex("Fewer sellers $+$ harder entry $=$ more price power").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(r5))
        self.play(Create(SurroundingRectangle(r5, color=GREEN)))
        self.wait(4)
