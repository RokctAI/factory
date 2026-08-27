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

# Band-layout whiteboard scene for "Free Market, Planned and Mixed Economies"
# (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier subtopics 5-7).
# Exporter-safe primitives only; add-only lifecycle.
# Subtopic durations: 200/240/230/260/180/180/180 of 1470 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class EconomicSystemsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===================== Part 1 — Expert =====================
        # --- Band 0 (subtopic_1): the three questions and the root variable ---
        title = Tex("Free Market, Planned and Mixed Economies").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2.5)
        b0a = Tex("Every system answers three questions:").scale(1.05).shift(UP * 1.2)
        b0b = Tex("WHAT to produce $\\cdot$ HOW $\\cdot$ FOR WHOM").scale(1.1).shift(UP * 0.4)
        self.play(Write(b0a))
        self.play(Write(b0b))
        self.play(Create(SurroundingRectangle(b0b, color=GREEN)))
        self.wait(3)
        b0c = Tex("The separating variable: who OWNS the").scale(1.05).shift(DOWN * 0.6)
        b0c2 = Tex("means of production — private, or the state?").scale(1.05).shift(DOWN * 1.3)
        self.play(Write(b0c))
        self.play(Write(b0c2))
        self.wait(3)
        b0w = Tex("An economic system $=$ a political system").scale(1.0).shift(DOWN * 2.3)
        self.play(Write(b0w))
        self.play(Create(strike(b0w)))
        b0d = Tex("Separate axes: ownership vs how power is held").scale(0.95).shift(DOWN * 3.1)
        self.play(Write(b0d))
        self.wait(3)

        # --- Band 1 (subtopic_2): the free market and the price mechanism ---
        self.next_band(1)
        b1t = Tex("The free market: the price mechanism").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = Tex("Private property, enterprise, profit motive,").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1a2 = Tex("competition, umpire state").scale(1.0).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1a))
        self.play(Write(b1a2))
        self.wait(2.5)
        c1 = Tex("demand rises").scale(0.85).shift(band_shift(1) + DOWN * 0.5 + LEFT * 4.8)
        c2 = Tex("price rises").scale(0.85).shift(band_shift(1) + DOWN * 0.5 + LEFT * 1.4)
        c3 = Tex("profit rises").scale(0.85).shift(band_shift(1) + DOWN * 0.5 + RIGHT * 1.8)
        c4 = Tex("supply expands").scale(0.85).shift(band_shift(1) + DOWN * 0.5 + RIGHT * 5.0)
        ar1 = Arrow(c1.get_right(), c2.get_left(), buff=0.1)
        ar2 = Arrow(c2.get_right(), c3.get_left(), buff=0.1)
        ar3 = Arrow(c3.get_right(), c4.get_left(), buff=0.1)
        self.play(Write(c1))
        self.play(Create(ar1), Write(c2))
        self.play(Create(ar2), Write(c3))
        self.play(Create(ar3), Write(c4))
        self.wait(2.5)
        b1b = Tex("Prices carry information AND incentive —").scale(1.0).shift(band_shift(1) + DOWN * 1.6)
        b1b2 = Tex("the invisible hand, no instructions needed").scale(1.0).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(b1b))
        self.play(Write(b1b2))
        self.play(Create(SurroundingRectangle(b1b2, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): market answers, strengths, weaknesses ---
        self.next_band(2)
        b2t = Tex("Market answers — and market failures").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = Tex("WHAT: consumers vote with rands $\\cdot$ HOW: least").scale(0.95).shift(band_shift(2) + UP * 1.1)
        b2a2 = Tex("cost $\\cdot$ FOR WHOM: ability to pay").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2a))
        self.play(Write(b2a2))
        self.wait(2.5)
        b2b = Tex("Strengths: efficiency, innovation, choice, speed").scale(0.95).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2b))
        self.wait(2)
        b2c = Tex("Weaknesses as mechanisms: inequality;").scale(0.95).shift(band_shift(2) + DOWN * 1.2)
        b2c2 = Tex("public goods under-supplied; externalities").scale(0.95).shift(band_shift(2) + DOWN * 1.9)
        b2c3 = Tex("unpriced; market power; instability").scale(0.95).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2c))
        self.play(Write(b2c2))
        self.play(Write(b2c3))
        self.wait(2)
        b2d = Tex("Efficient and unjust can be true at once").scale(1.0).shift(band_shift(2) + DOWN * 3.4)
        self.play(Write(b2d))
        self.wait(3)

        # --- Band 3 (subtopic_3): the centrally planned economy ---
        self.next_band(3)
        b3t = Tex("The centrally planned economy").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = Tex("State owns the means of production;").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3a2 = Tex("planners set targets; prices administered").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3a))
        self.play(Write(b3a2))
        self.wait(2.5)
        b3b = Tex("WHAT: the plan $\\cdot$ HOW: the plan $\\cdot$").scale(1.0).shift(band_shift(3) + DOWN * 0.5)
        b3b2 = Tex("FOR WHOM: the state, in principle by need").scale(1.0).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(b3b))
        self.play(Write(b3b2))
        self.wait(2.5)
        b3c = Tex("Strengths: equality, guaranteed basics,").scale(1.0).shift(band_shift(3) + DOWN * 2.1)
        b3c2 = Tex("rapid mobilisation, no unemployment in principle").scale(0.95).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3c))
        self.play(Write(b3c2))
        self.wait(3)

        # --- Band 4 (subtopic_3): the planned economy's mechanisms of failure ---
        self.next_band(4)
        b4t = Tex("Why plans go wrong — mechanisms").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        b4a = Tex("INFORMATION: no office can know the millions").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4a2 = Tex("of local facts that prices summarise free").scale(1.0).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4a))
        self.play(Write(b4a2))
        self.play(Create(SurroundingRectangle(b4a2, color=GREEN)))
        self.wait(2.5)
        b4b = Tex("INCENTIVE: no profit, no risk — little reward").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        b4b2 = Tex("for effort, quality or invention").scale(1.0).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4b))
        self.play(Write(b4b2))
        self.wait(2.5)
        b4c = Tex("Administered prices cannot adjust: queues for").scale(0.95).shift(band_shift(4) + DOWN * 2.2)
        b4c2 = Tex("some goods, warehouses of unwanted others").scale(0.95).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4c))
        self.play(Write(b4c2))
        self.wait(3)

        # --- Band 5 (subtopic_4): the mixed economy — South Africa ---
        self.next_band(5)
        b5t = Tex("The mixed economy: divided answers").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = Tex("WHAT: markets, plus public and merit goods").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5b = Tex("HOW: least cost, within rules — labour,").scale(0.95).shift(band_shift(5) + UP * 0.5)
        b5b2 = Tex("environment, competition law").scale(0.95).shift(band_shift(5) + DOWN * 0.2)
        b5c = Tex("FOR WHOM: market income, then redistribution —").scale(0.95).shift(band_shift(5) + DOWN * 0.9)
        b5c2 = Tex("progressive tax, grants, no-fee schools").scale(0.95).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5a))
        self.wait(2)
        self.play(Write(b5b))
        self.play(Write(b5b2))
        self.wait(2)
        self.play(Write(b5c))
        self.play(Write(b5c2))
        self.wait(2)
        b5d = Tex("SA: private firms $+$ SOEs $+$ regulators $+$ grants").scale(0.95).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5d))
        self.play(Create(SurroundingRectangle(b5d, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): dualism explained by its causes ---
        self.next_band(6)
        b6t = Tex("And DUALISTIC: two economies in one").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        r6a = Rectangle(width=5.6, height=1.8).shift(band_shift(6) + UP * 0.7 + LEFT * 3.4)
        t6a = Tex("First: formal, capital-").scale(0.8).move_to(r6a.get_center() + UP * 0.4)
        t6a2 = Tex("intensive, global").scale(0.8).move_to(r6a.get_center() + DOWN * 0.4)
        self.play(Create(r6a), Write(t6a), Write(t6a2))
        self.wait(1.5)
        r6b = Rectangle(width=5.6, height=1.8).shift(band_shift(6) + UP * 0.7 + RIGHT * 3.4)
        t6b = Tex("Second: informal,").scale(0.8).move_to(r6b.get_center() + UP * 0.4)
        t6b2 = Tex("survivalist, no credit").scale(0.8).move_to(r6b.get_center() + DOWN * 0.4)
        self.play(Create(r6b), Write(t6b), Write(t6b2))
        self.wait(2)
        b6a = Tex("Explain, don't just describe — structural roots:").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6a))
        b6b = Tex("dispossession, migrant labour, apartheid").scale(0.95).shift(band_shift(6) + DOWN * 1.7)
        b6b2 = Tex("spatial planning, unequal education").scale(0.95).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6b))
        self.play(Write(b6b2))
        self.wait(2.5)
        b6c = Tex("Sophisticated and impoverished at once").scale(1.0).shift(band_shift(6) + DOWN * 3.2)
        self.play(Write(b6c))
        self.play(Create(SurroundingRectangle(b6c, color=GREEN)))
        self.wait(3)

        # ===================== Part 2 — Simplifier =====================
        # --- Band 7 (subtopic_5): three ways to run the kitchen ---
        self.next_band(7)
        b7t = Tex("Three ways to run the kitchen").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex("Tuckshop: the till does the talking; your").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7a2 = Tex("wallet decides your plate — free market").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7a))
        self.play(Write(b7a2))
        self.wait(2.5)
        b7b = Tex("Feeding scheme: one menu, every learner fed —").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        b7b2 = Tex("but samp all term if the official chose samp").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7b))
        self.play(Write(b7b2))
        self.wait(2.5)
        b7c = Tex("Real schools run BOTH — the mixed economy,").scale(1.0).shift(band_shift(7) + DOWN * 2.1)
        b7c2 = Tex("and South Africa is one").scale(1.0).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7c))
        self.play(Write(b7c2))
        self.play(Create(SurroundingRectangle(b7c2, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): what the till knows ---
        self.next_band(8)
        b8t = Tex("What the till knows and the memo doesn't").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("A price is a message: sold-out vetkoek says").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8a2 = Tex("`more of this' — free, daily, millions of times").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8a))
        self.play(Write(b8a2))
        self.wait(2.5)
        b8b = Tex("The planning office has no till: wrong guesses").scale(0.95).shift(band_shift(8) + DOWN * 0.5)
        b8b2 = Tex("mean queues here, full warehouses there").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8b))
        self.play(Write(b8b2))
        self.wait(2.5)
        b8c = Tex("But the till only hears money: a hungry learner").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        b8c2 = Tex("with no coins sends no message at all").scale(0.95).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8c))
        self.play(Write(b8c2))
        self.play(Create(SurroundingRectangle(b8c2, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): two economies in one country ---
        self.next_band(9)
        b9t = Tex("Two economies in one country").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("The Sandton tower: contracts, pensions, credit").scale(0.95).shift(band_shift(9) + UP * 1.1)
        b9b = Tex("An hour away: airtime table, R400 of stock,").scale(0.95).shift(band_shift(9) + UP * 0.3)
        b9b2 = Tex("no contract, no loan at any price").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9a))
        self.wait(2)
        self.play(Write(b9b))
        self.play(Write(b9b2))
        self.wait(2.5)
        b9w = Tex("What separates them is effort").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9w))
        self.play(Create(strike(b9w)))
        self.wait(1.5)
        b9c = Tex("Four structural walls: ownership taken, distance").scale(0.95).shift(band_shift(9) + DOWN * 2.2)
        b9c2 = Tex("imposed, unequal schools, no collateral").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9c))
        self.play(Write(b9c2))
        self.play(Create(SurroundingRectangle(VGroup(b9c, b9c2), color=GREEN)))
        self.wait(2)
        b9d = Tex("The mixed system is the attempted door between them").scale(0.9).shift(band_shift(9) + DOWN * 3.6)
        self.play(Write(b9d))
        self.wait(4)
