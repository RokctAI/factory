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

# Band-layout whiteboard scene for the Paper 2 revision-essentials duo.
# Part 1 (Expert): subtopics 1-4; Part 2 (Simplifier): subtopics 5-7.
# Subtopic durations 250/250/245/250/195/200/195 of 1585 s — bands
# 0-1 / 2-3 / 4-5 / 6-7 / 8 / 9 / 10 apportioned to match.
# Kinked-demand and externality sketches hand-built from
# Arrow/Line/Dot/Tex primitives only.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


def axes(origin, w, h, xlab, ylab):
    xa = Arrow(origin, origin + RIGHT * w, buff=0, stroke_width=3)
    ya = Arrow(origin, origin + UP * h, buff=0, stroke_width=3)
    xl = Tex(xlab).scale(0.9).next_to(origin + RIGHT * w, DOWN, buff=0.2)
    yl = Tex(ylab).scale(0.9).next_to(origin + UP * h, RIGHT, buff=0.15)
    return VGroup(xa, ya, xl, yl)


def chain(origin, pts, color=WHITE, sw=5):
    g = VGroup()
    for a, b in zip(pts[:-1], pts[1:]):
        g.add(Line(origin + RIGHT * a[0] + UP * a[1],
                   origin + RIGHT * b[0] + UP * b[1],
                   color=color, stroke_width=sw))
    return g


class PaperTwoMicroEssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(14)

        # --- Band 0 (subtopic_1): perfect markets, three positions ---
        title = Tex("Paper 2 Essentials: Micro and Issues").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        p0 = Tex("Perfect competition: many sellers, homogeneous").scale(1.0).shift(UP * 1.5)
        p0b = Tex("product, free entry, perfect information").scale(1.0).shift(UP * 0.8)
        self.play(Write(p0))
        self.play(Write(p0b))
        self.wait(2)
        p1 = MathTex(r"\text{Price taker: } D = P = AR = MR \text{ (flat line)}").scale(1.0).shift(DOWN * 0.1)
        self.play(Write(p1))
        self.play(Create(SurroundingRectangle(p1, color=GREEN)))
        self.wait(2.5)
        p2 = MathTex(r"P > AC: \text{ economic profit}").scale(1.0).shift(DOWN * 1.1)
        p3 = MathTex(r"P < AC: \text{ economic loss}").scale(1.0).shift(DOWN * 1.9)
        p4 = MathTex(r"P = \text{min } AC: \text{ normal profit — the long run}").scale(1.0).shift(DOWN * 2.7)
        self.play(Write(p2))
        self.wait(1.8)
        self.play(Write(p3))
        self.wait(1.8)
        self.play(Write(p4))
        self.wait(3)

        # --- Band 1 (subtopic_1): shutdown and competition policy ---
        self.next_band(1)
        b1_title = Tex("Shutdown, and the referees").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"P \geq AVC: \text{ produce — units help pay fixed costs}").scale(1.0).shift(band_shift(1) + UP * 1.4)
        b1_l2 = MathTex(r"P < \text{min } AVC: \text{ shut down}").scale(1.05).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("Competition Act 1998: Commission investigates,").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        b1_l4 = Tex("Tribunal adjudicates, Appeal Court hears appeals").scale(1.0).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(2.5)
        b1_l5 = Tex("Scoreboard: the bread cartel; construction").scale(1.0).shift(band_shift(1) + DOWN * 2.1)
        b1_l6 = Tex("collusion around the 2010 stadiums").scale(1.0).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): monopoly ---
        self.next_band(2)
        b2_title = Tex("Monopoly: the industry in one firm").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("One seller, no close substitutes, high barriers —").scale(1.0).shift(band_shift(2) + UP * 1.4)
        b2_l2 = Tex("natural (the grid) or artificial (licences, patents)").scale(1.0).shift(band_shift(2) + UP * 0.7)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("D slopes down; MR lies BELOW D — one more").scale(1.0).shift(band_shift(2) + DOWN * 0.2)
        b2_l4 = Tex("unit sold lowers the price on all units").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.wait(2.5)
        b2_l5 = MathTex(r"Q \text{ at } MC = MR; \; P \text{ read UP on } D").scale(1.05).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(2)
        b2_l6 = Tex("Long-run economic profit possible behind barriers —").scale(0.95).shift(band_shift(2) + DOWN * 2.7)
        b2_l7 = Tex("but never guaranteed: weak demand still means losses").scale(0.95).shift(band_shift(2) + DOWN * 3.3)
        self.play(Write(b2_l6))
        self.play(Write(b2_l7))
        self.wait(3)

        # --- Band 3 (subtopic_2): oligopoly's kink, and the many ---
        self.next_band(3)
        b3_title = Tex("Oligopoly: the kinked demand curve").scale(1.1).shift(band_shift(3) + UP * 2.6)
        self.play(Write(b3_title))
        self.wait(1.5)
        o = band_shift(3) + LEFT * 4.8 + DOWN * 2.2
        ax = axes(o, 5.4, 4.2, "Q", "P")
        self.play(Create(ax))
        upper = chain(o, [(0.5, 3.6), (2.5, 2.4)], color=BLUE)
        lower = chain(o, [(2.5, 2.4), (3.9, 0.5)], color=BLUE)
        kink = Dot(o + RIGHT * 2.5 + UP * 2.4, color=YELLOW)
        k_guide = DashedLine(o + UP * 2.4, o + RIGHT * 2.5 + UP * 2.4, stroke_width=2)
        k_lab = Tex("current P").scale(0.8).next_to(o + UP * 2.4, LEFT, buff=0.1)
        self.play(Create(upper))
        self.play(Create(kink), Create(k_guide), Write(k_lab))
        self.play(Create(lower))
        self.wait(2)
        e_lab = Tex("elastic above: raisers lose").scale(0.85).shift(band_shift(3) + RIGHT * 3.4 + UP * 1.4)
        i_lab = Tex("inelastic below: cuts matched").scale(0.85).shift(band_shift(3) + RIGHT * 3.4 + UP * 0.6)
        s_lab = Tex("so prices stick; rivalry moves").scale(0.85).shift(band_shift(3) + RIGHT * 3.4 + DOWN * 0.3)
        s_lab2 = Tex("to brands and loyalty points").scale(0.85).shift(band_shift(3) + RIGHT * 3.4 + DOWN * 1.0)
        self.play(Write(e_lab))
        self.play(Write(i_lab))
        self.play(Write(s_lab))
        self.play(Write(s_lab2))
        self.wait(2.5)
        b3_l1 = Tex("Collusion — cartels, price leadership — is illegal;").scale(0.95).shift(band_shift(3) + DOWN * 2.7)
        b3_l2 = Tex("monopolistic competition: many, differentiated, easy in").scale(0.9).shift(band_shift(3) + DOWN * 3.3)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(3)

        # --- Band 4 (subtopic_3): market failure and externalities ---
        self.next_band(4)
        b4_title = Tex("Market failure: the externality graph").scale(1.1).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        o2 = band_shift(4) + LEFT * 5.4 + DOWN * 2.2
        ax2 = axes(o2, 5.4, 4.0, "Q", "P")
        self.play(Create(ax2))
        dd = chain(o2, [(0.5, 3.3), (2.4, 1.9), (4.2, 0.8)], color=BLUE)
        d_lab = Tex("D").scale(0.85).next_to(o2 + RIGHT * 4.2 + UP * 0.8, RIGHT, buff=0.1)
        sp = chain(o2, [(0.6, 0.7), (2.4, 1.9), (4.2, 3.1)], color=YELLOW)
        sp_lab = Tex("S private").scale(0.8).next_to(o2 + RIGHT * 4.2 + UP * 3.1, RIGHT, buff=0.1)
        self.play(Create(dd), Write(d_lab))
        self.play(Create(sp), Write(sp_lab))
        self.wait(1.5)
        ss = chain(o2, [(0.2, 1.4), (1.8, 2.6), (3.3, 3.7)], color=RED)
        ss_lab = Tex("S social").scale(0.8).next_to(o2 + RIGHT * 3.3 + UP * 3.7, RIGHT, buff=0.1)
        self.play(Create(ss), Write(ss_lab))
        self.wait(2)
        b4_l1 = Tex("Market counts private cost only:").scale(0.9).shift(band_shift(4) + RIGHT * 3.5 + UP * 1.2)
        b4_l2 = Tex("too much, too cheap — efficient").scale(0.9).shift(band_shift(4) + RIGHT * 3.5 + UP * 0.4)
        b4_l3 = Tex("point: social cost meets demand").scale(0.9).shift(band_shift(4) + RIGHT * 3.5 + DOWN * 0.4)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex("Positive externality (education): market buys too little;").scale(0.9).shift(band_shift(4) + DOWN * 2.7)
        b4_l5 = Tex("public goods: free riding kills private supply").scale(0.9).shift(band_shift(4) + DOWN * 3.3)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): intervention and CBA ---
        self.next_band(5)
        b5_title = Tex("State tools, each with its verbal graph").scale(1.1).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Maximum price BELOW equilibrium $\\rightarrow$ shortage,").scale(1.0).shift(band_shift(5) + UP * 1.4)
        b5_l2 = Tex("queues, black markets").scale(1.0).shift(band_shift(5) + UP * 0.7)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Minimum price ABOVE equilibrium $\\rightarrow$ surplus;").scale(1.0).shift(band_shift(5) + DOWN * 0.2)
        b5_l4 = Tex("minimum wage is the labour-market version").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex("Tax harm (sugar, fuel levies); subsidise good;").scale(1.0).shift(band_shift(5) + DOWN * 1.8)
        b5_l6 = Tex("provide public goods; redistribute").scale(1.0).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(2)
        b5_l7 = Tex("CBA: count ALL costs and benefits, then decide").scale(1.0).shift(band_shift(5) + DOWN * 3.2)
        self.play(Write(b5_l7))
        self.play(Create(SurroundingRectangle(b5_l7, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): inflation in one band ---
        self.next_band(6)
        b6_title = Tex("Contemporary issues I: inflation").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Rate} = \frac{\text{new} - \text{old}}{\text{OLD}} \times 100").scale(1.1).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2.5)
        b6_l2 = Tex("Demand-pull: credit booms, G, export surges").scale(1.0).shift(band_shift(6) + DOWN * 0.1)
        b6_l3 = Tex("Cost-push: wages over productivity, weak rand,").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        b6_l4 = Tex("fuel and electricity, droughts").scale(1.0).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("Targeting: 3–6\\% via the repo — powerful against").scale(1.0).shift(band_shift(6) + DOWN * 2.5)
        b6_l6 = Tex("demand-pull, blunt against cost-push").scale(1.0).shift(band_shift(6) + DOWN * 3.2)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): tourism and sustainability ---
        self.next_band(7)
        b7_title = Tex("Contemporary issues II: tourism, planet").scale(1.1).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Tourism: labour-intensive, skills-light at entry —").scale(1.0).shift(band_shift(7) + UP * 1.4)
        b7_l2 = Tex("absorbs job seekers fast; benefits households,").scale(1.0).shift(band_shift(7) + UP * 0.7)
        b7_l3 = Tex("businesses, the state and infrastructure").scale(1.0).shift(band_shift(7))
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.play(Write(b7_l3))
        self.wait(3)
        b7_l4 = Tex("Sustainability: meet present needs without").scale(1.0).shift(band_shift(7) + DOWN * 0.9)
        b7_l5 = Tex("robbing future generations").scale(1.0).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(2.5)
        b7_l6 = Tex("Tools: property rights, charges, green taxes,").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        b7_l7 = Tex("permits, command; Rio, Kyoto, Paris, the SDGs").scale(1.0).shift(band_shift(7) + DOWN * 3.2)
        self.play(Write(b7_l6))
        self.play(Write(b7_l7))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the spaza and the giant ---
        self.next_band(8)
        b8_title = Tex("The spaza and the giant: one street").scale(1.15).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Tomato stalls: near-perfect competition — the").scale(1.0).shift(band_shift(8) + UP * 1.5)
        b8_l2 = Tex("price is given; Friday's new stalls melt profits").scale(1.0).shift(band_shift(8) + UP * 0.8)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("The electricity giant: monopoly — output at").scale(1.0).shift(band_shift(8))
        b8_l4 = Tex("MC $=$ MR, price what demand will bear").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex("Banks and networks: the FEW, watching rivals —").scale(1.0).shift(band_shift(8) + DOWN * 1.6)
        b8_l6 = Tex("fighting with adverts, not prices").scale(1.0).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.wait(2)
        b8_l7 = Tex("Hair salons: the MANY with a difference").scale(1.0).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(b8_l7))
        self.play(Create(SurroundingRectangle(b8_l7, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): when the market drops the ball ---
        self.next_band(9)
        b9_title = Tex("When the market drops the ball").scale(1.15).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Scrapyard smoke over the school: costs dumped").scale(1.0).shift(band_shift(9) + UP * 1.5)
        b9_l2 = Tex("on others — too much burning, too cheap").scale(1.0).shift(band_shift(9) + UP * 0.8)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Education's benefits leak to everyone —").scale(1.0).shift(band_shift(9))
        b9_l4 = Tex("the town buys too little of the best things").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("The streetlight: no one can charge — the").scale(1.0).shift(band_shift(9) + DOWN * 1.4)
        b9_l6 = Tex("municipality builds it or nobody does").scale(1.0).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.wait(2.5)
        b9_l7 = Tex("Cap bread price $\\rightarrow$ empty shelves; wage floor").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        b9_l8 = Tex("$\\rightarrow$ surplus — in labour, that means unemployment").scale(0.95).shift(band_shift(9) + DOWN * 3.2)
        self.play(Write(b9_l7))
        self.play(Write(b9_l8))
        self.play(Create(SurroundingRectangle(b9_l8, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): prices, tourists, planet ---
        self.next_band(10)
        b10_title = Tex("Prices, tourists and the planet").scale(1.15).shift(band_shift(10) + UP * 2.6)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Grant-day markups: demand-pull; diesel and").scale(1.0).shift(band_shift(10) + UP * 1.8)
        b10_l2 = Tex("Eskom markups: cost-push").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("The repo cools spenders but cannot cheapen").scale(1.0).shift(band_shift(10) + UP * 0.2)
        b10_l4 = Tex("diesel — the cure must match the cause").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2.5)
        b10_l5 = Tex("The tourist's rand: shisa nyama, beadwork, guest").scale(1.0).shift(band_shift(10) + DOWN * 1.3)
        b10_l6 = Tex("house — exporting without shipping a box").scale(1.0).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.wait(2.5)
        b10_l7 = Tex("Free dumping dirties the river: make the polluter").scale(1.0).shift(band_shift(10) + DOWN * 2.6)
        b10_l8 = Tex("pay — promises are easier than delivery").scale(1.0).shift(band_shift(10) + DOWN * 3.1)
        self.play(Write(b10_l7))
        self.play(Write(b10_l8))
        self.wait(4)
