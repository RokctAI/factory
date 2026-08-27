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

# Band-layout whiteboard scene for the revision session duo "Growth,
# Development and Global Issues Essentials" (Grade 11, Term 4). One band per
# teaching step; the camera moves down and nothing is removed. Exporter-safe
# mobjects only; the Lorenz sketch is hand-built from a Rectangle and Lines.
# Band time apportioned to subtopics.json (245/250/250/245/200/205/205 of
# 1600 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class GrowthDevelopmentGlobalRevisionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): growth and the Lorenz/Gini instruments ---
        title = Tex("Revision: Growth, Development, Global Issues").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        g1 = Tex("Growth: REAL GDP up — strip inflation, divide by people").scale(0.9).shift(UP * 1.4)
        self.play(Write(g1))
        self.wait(2)
        g2 = Tex("SA: a decade of growth below population growth").scale(0.9).shift(UP * 0.6)
        self.play(Write(g2))
        self.wait(2)
        org = LEFT * 5.2 + DOWN * 2.9
        sq = Rectangle(width=3.4, height=3.4).move_to(org + RIGHT * 1.7 + UP * 1.7)
        diag = Line(org, org + RIGHT * 3.4 + UP * 3.4, stroke_width=4, color=BLUE)
        lz1 = Line(org, org + RIGHT * 2.04 + UP * 0.34, stroke_width=5)
        lz2 = Line(org + RIGHT * 2.04 + UP * 0.34, org + RIGHT * 3.4 + UP * 3.4, stroke_width=5)
        self.play(Create(sq))
        self.play(Create(diag))
        self.play(Create(lz1), Create(lz2))
        self.wait(2)
        g3 = Tex("Lorenz: the deeper the sag,").scale(0.85).shift(RIGHT * 1.6 + DOWN * 0.9)
        g3b = Tex("the worse the inequality").scale(0.85).shift(RIGHT * 1.6 + DOWN * 1.6)
        self.play(Write(g3))
        self.play(Write(g3b))
        self.wait(2)
        g4 = Tex(r"Gini $\approx 0{,}65$: the world's deepest sag").scale(0.9).shift(RIGHT * 2.2 + DOWN * 2.6)
        self.play(Write(g4))
        self.play(Create(SurroundingRectangle(g4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): redistribution instruments + constraints ---
        self.next_band(1)
        b1_title = Tex("Redistribution instruments, growth constraints").scale(1.0).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        r1 = Tex("Progressive tax; social grants; free basic services;").scale(0.9).shift(band_shift(1) + UP * 1.4)
        r1b = Tex("minimum wage; land reform and empowerment").scale(0.9).shift(band_shift(1) + UP * 0.6)
        self.play(Write(r1))
        self.play(Write(r1b))
        self.wait(2.5)
        r2 = Tex("Each with its evaluation: grants need a growing tax base;").scale(0.8).shift(band_shift(1) + DOWN * 0.3)
        r2b = Tex("the wage floor reaches only the employed").scale(0.85).shift(band_shift(1) + DOWN * 1.1)
        self.play(Write(r2))
        self.play(Write(r2b))
        self.wait(2.5)
        r3 = Tex("Constraints: electricity, skills beside unemployment,").scale(0.85).shift(band_shift(1) + DOWN * 2.0)
        r3b = Tex("low savings, crime, policy doubt, debt interest").scale(0.85).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(r3))
        self.play(Write(r3b))
        self.wait(3)

        # --- Band 2 (subtopic_2): development, HDI, the portrait ---
        self.next_band(2)
        b2_title = Tex("Development: how the people live").scale(1.1).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        d1 = Tex("HDI: life expectancy $+$ education $+$ income —").scale(0.9).shift(band_shift(2) + UP * 1.4)
        d1b = Tex("a healthier country can outrank a richer one").scale(0.9).shift(band_shift(2) + UP * 0.6)
        self.play(Write(d1))
        self.play(Write(d1b))
        self.wait(2.5)
        d2 = Tex("Portrait: low income; young, fast-growing population;").scale(0.85).shift(band_shift(2) + DOWN * 0.3)
        d2b = Tex("unemployment; primary exports; DUALISM; thin services").scale(0.85).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(d2))
        self.play(Write(d2b))
        self.wait(2.5)
        d3 = Tex("SA fits in parts, breaks it in others —").scale(0.9).shift(band_shift(2) + DOWN * 2.0)
        d3b = Tex("both-ways evidence is what essays reward").scale(0.9).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(d3))
        self.play(Write(d3b))
        self.play(Create(SurroundingRectangle(d3b, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): strategies, the plans, IKS ---
        self.next_band(3)
        b3_title = Tex("Strategies and South Africa's plans").scale(1.1).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        s1 = Tex("Families: growth-first; redistribution-with-growth;").scale(0.85).shift(band_shift(3) + UP * 1.4)
        s1b = Tex("basic needs; export-led").scale(0.9).shift(band_shift(3) + UP * 0.6)
        self.play(Write(s1))
        self.play(Write(s1b))
        self.wait(2.5)
        s2 = Tex(r"RDP $\to$ GEAR $\to$ AsgiSA $\to$ NDP").scale(1.05).shift(band_shift(3) + DOWN * 0.3)
        self.play(Write(s2))
        self.play(Create(SurroundingRectangle(s2, color=GREEN)))
        self.wait(2.5)
        s3 = Tex("Verdict: strong on diagnosis, weak on implementation").scale(0.9).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(s3))
        self.wait(2)
        s4 = Tex("IKS: development from within — done WITH people,").scale(0.85).shift(band_shift(3) + DOWN * 2.2)
        s4b = Tex("not TO them; local knowledge carries ownership").scale(0.85).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(s4))
        self.play(Write(s4b))
        self.wait(3)

        # --- Band 4 (subtopic_3): globalisation causes + scorecard ---
        self.next_band(4)
        b4_title = Tex("Globalisation: causes and scorecard").scale(1.1).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        q1 = Tex("Technology made it possible: containers, cables,").scale(0.85).shift(band_shift(4) + UP * 1.4)
        q1b = Tex("computing — the global value chain").scale(0.9).shift(band_shift(4) + UP * 0.6)
        self.play(Write(q1))
        self.play(Write(q1b))
        self.wait(2.5)
        q2 = Tex("Policy made it permitted: WTO, free finance, reopeners").scale(0.85).shift(band_shift(4) + DOWN * 0.3)
        self.play(Write(q2))
        self.wait(2.5)
        q3 = Tex("Gains: cheap goods, motor-industry jobs, spreading tech").scale(0.8).shift(band_shift(4) + DOWN * 1.2)
        q4 = Tex("Losses: textile towns, 2008 contagion, mobile capital").scale(0.8).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(q3))
        self.wait(2)
        self.play(Write(q4))
        self.wait(2)
        q5 = Tex("Grows the total while moving the shares").scale(0.9).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(q5))
        self.play(Create(SurroundingRectangle(q5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the North/South divide ---
        self.next_band(5)
        b5_title = Tex("The North/South divide: three mechanisms").scale(1.05).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(1.5)
        n1 = Tex("1. Terms-of-trade treadmill: raw out, made in").scale(0.9).shift(band_shift(5) + UP * 1.4)
        n2 = Tex("2. Foreign-currency debt squeezing Southern budgets").scale(0.9).shift(band_shift(5) + UP * 0.55)
        n3 = Tex("3. Voice: rules written where votes tilt North").scale(0.9).shift(band_shift(5) + DOWN * 0.3)
        for m in (n1, n2, n3):
            self.play(Write(m))
            self.wait(2)
        n4 = Tex("Counterforces: Asia's rise, BRICS, AfCFTA").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(n4))
        self.play(Create(SurroundingRectangle(n4, color=GREEN)))
        self.wait(2)
        n5 = Tex("SA on both sides: Sandton finance, raw-export accounts").scale(0.85).shift(band_shift(5) + DOWN * 2.3)
        self.play(Write(n5))
        self.wait(3)

        # --- Band 6 (subtopic_4): market failure and the toolbox ---
        self.next_band(6)
        b6_title = Tex("The environment: where bookkeeping fails").scale(1.05).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(1.5)
        e1 = Tex("Externality: smoke lands outside the deal —").scale(0.9).shift(band_shift(6) + UP * 1.4)
        e1b = Tex("priced at zero, so too cheap, so too much").scale(0.9).shift(band_shift(6) + UP * 0.6)
        self.play(Write(e1))
        self.play(Write(e1b))
        self.wait(2.5)
        e2 = Tex("Commons: what belongs to everyone is cared for by no one").scale(0.8).shift(band_shift(6) + DOWN * 0.3)
        self.play(Write(e2))
        self.wait(2.5)
        e3 = Tex("Toolbox: command and control; carbon tax and permits;").scale(0.8).shift(band_shift(6) + DOWN * 1.2)
        e3b = Tex("subsidies; property rights; treaties across borders").scale(0.85).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(e3))
        self.play(Write(e3b))
        self.wait(2.5)
        e4 = Tex("Match each tool to the failure it fixes").scale(0.9).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(e4))
        self.play(Create(SurroundingRectangle(e4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): sustainability and South Africa's stake ---
        self.next_band(7)
        b7_title = Tex("Sustainability, and South Africa's stake").scale(1.1).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(1.5)
        u1 = Tex("Live off nature's INTEREST without eating the CAPITAL").scale(0.9).shift(band_shift(7) + UP * 1.4)
        self.play(Write(u1))
        self.play(Create(SurroundingRectangle(u1, color=GREEN)))
        self.wait(2.5)
        u2 = Tex("Three legs — economic, social, environmental —").scale(0.9).shift(band_shift(7) + UP * 0.4)
        u2b = Tex("sacrifice any one and the strategy falls").scale(0.9).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(u2))
        self.play(Write(u2b))
        self.wait(2.5)
        u3 = Tex("SA: water-scarce, warming fast, coal-powered exports").scale(0.85).shift(band_shift(7) + DOWN * 1.3)
        u3b = Tex("facing carbon border taxes; acid mine drainage lingers").scale(0.85).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(u3))
        self.play(Write(u3b))
        self.wait(2.5)
        u4 = Tex("Green transition is the condition for survival, not a luxury").scale(0.8).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(u4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the pot and the queue ---
        self.next_band(8)
        b8_title = Tex("The pot and the queue of one hundred").scale(1.1).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        p1 = Tex("Skim the froth of prices; count the family first —").scale(0.9).shift(band_shift(8) + UP * 1.4)
        p1b = Tex(r"pot up 2\%, family up 2\%: nobody's plate grew").scale(0.9).shift(band_shift(8) + UP * 0.6)
        self.play(Write(p1))
        self.play(Write(p1b))
        self.wait(2.5)
        p2 = Tex("Walk past sixty people: barely a tenth counted;").scale(0.9).shift(band_shift(8) + DOWN * 0.3)
        p2b = Tex(r"the last few hold half the pot — Gini $\approx 0{,}65$").scale(0.9).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(p2))
        self.play(Write(p2b))
        self.wait(2.5)
        p3 = Tex("Five spoons: taxes, grants, free basics, wage floor,").scale(0.85).shift(band_shift(8) + DOWN * 2.0)
        p3b = Tex("land reform — each spoon with its handle").scale(0.85).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(p3))
        self.play(Write(p3b))
        self.play(Create(SurroundingRectangle(p3b, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): taller or better, and the one-world shop ---
        self.next_band(9)
        b9_title = Tex("Taller or better — and the one-world shop").scale(1.05).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        t1 = Tex("Growth is the height; development is the report card —").scale(0.85).shift(band_shift(9) + UP * 1.4)
        t1b = Tex("HDI grades health, schooling, income").scale(0.9).shift(band_shift(9) + UP * 0.6)
        self.play(Write(t1))
        self.play(Write(t1b))
        self.wait(2.5)
        t2 = Tex("Six signs on one walk; SA shows some, breaks others").scale(0.85).shift(band_shift(9) + DOWN * 0.3)
        self.play(Write(t2))
        self.wait(2)
        t3 = Tex("The initials in order: RDP, GEAR, AsgiSA, NDP —").scale(0.9).shift(band_shift(9) + DOWN * 1.2)
        t3b = Tex("excellent diagnosis, thin delivery").scale(0.9).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(t3))
        self.play(Write(t3b))
        self.wait(2.5)
        t4 = Tex("The shop gives and takes; finish what we dig and grow").scale(0.85).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(t4))
        self.play(Create(SurroundingRectangle(t4, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the smoke, the river, the seed ---
        self.next_band(10)
        b10_title = Tex("The smoke, the river and the seed mealies").scale(1.1).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        z1 = Tex("Price the smoke: polluter pays, as the carbon tax does").scale(0.85).shift(band_shift(10) + UP * 1.4)
        self.play(Write(z1))
        self.wait(2)
        z2 = Tex("Guard the river: rules, community owners, capped permits").scale(0.85).shift(band_shift(10) + UP * 0.5)
        self.play(Write(z2))
        self.wait(2)
        z3 = Tex("Save the seed: live off what regrows, never the stock").scale(0.85).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(z3))
        self.wait(2)
        z4 = Tex("Price the smoke, guard the river, save the seed").scale(0.95).shift(band_shift(10) + DOWN * 1.4)
        self.play(Write(z4))
        self.play(Create(SurroundingRectangle(z4, color=GREEN)))
        self.wait(2.5)
        z5 = Tex("Argue with mechanisms, close with evaluation —").scale(0.9).shift(band_shift(10) + DOWN * 2.3)
        z5b = Tex("the whole examiner's wishlist").scale(0.9).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(z5))
        self.play(Write(z5b))
        self.wait(4)
