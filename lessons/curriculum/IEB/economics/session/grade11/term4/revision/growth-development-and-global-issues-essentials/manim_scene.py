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

# Band-layout whiteboard scene for the revision session duo "Growth,
# Development and Global Issues Essentials" (Grade 11, Term 4, IEB
# catalogue). One band per teaching step; the camera moves down and nothing
# is removed. Exporter-safe mobjects only; the Lorenz sketch is hand-built
# from Lines and Arcs. Band time apportioned to subtopics.json
# (245/250/250/245/200/205/205 of 1600 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class GrowthDevelopmentGlobalRevisionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): growth and the Lorenz/Gini instruments ---
        title = Tex("Growth, Inequality and Redistribution").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        g1 = Tex("Growth = REAL GDP up: strip inflation,").scale(0.85).shift(UP * 1.5)
        g1b = Tex("divide by population").scale(0.85).shift(UP * 0.8)
        self.play(Write(g1))
        self.play(Write(g1b))
        self.wait(2)
        ax_v = Line(LEFT * 5 + DOWN * 2.6, LEFT * 5 + UP * 0.2)
        ax_h = Line(LEFT * 5 + DOWN * 2.6, RIGHT * 0.5 + DOWN * 2.6)
        diag = Line(LEFT * 5 + DOWN * 2.6, RIGHT * 0.5 + UP * 0.2, color=GREEN)
        self.play(Create(ax_v), Create(ax_h))
        self.play(Create(diag))
        lor = ArcBetweenPoints(LEFT * 5 + DOWN * 2.6, RIGHT * 0.5 + UP * 0.2,
                               angle=PI / 2.6, color=RED)
        self.play(Create(lor))
        self.wait(2)
        l1 = Tex("Lorenz: the deeper the sag, the worse the sharing").scale(0.8).shift(RIGHT * 3.4 + DOWN * 0.8)
        self.play(Write(l1))
        self.wait(2)
        l2 = Tex("Gini 0 to 1 — SA near 0,65: the deepest sag recorded").scale(0.8).shift(DOWN * 3.2)
        self.play(Write(l2))
        self.play(Create(SurroundingRectangle(l2, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): redistribution instruments + constraints ---
        self.next_band(1)
        b1_title = Tex("Five instruments, five evaluations").scale(1.1).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        r1 = Tex("Progressive tax; grants; free basic services;").scale(0.85).shift(band_shift(1) + UP * 1.4)
        r1b = Tex("minimum wage; land and asset reform").scale(0.85).shift(band_shift(1) + UP * 0.65)
        self.play(Write(r1))
        self.play(Write(r1b))
        self.wait(2.5)
        r2 = Tex("Grants need a tax base; the floor reaches only").scale(0.85).shift(band_shift(1) + DOWN * 0.25)
        r2b = Tex("the employed; assets need skills and finance").scale(0.85).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(r2))
        self.play(Write(r2b))
        self.wait(2.5)
        r3 = Tex("Constraints: electricity, skills, savings, crime, debt").scale(0.8).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(r3))
        self.wait(2)
        r4 = Tex("The pot must grow while the shares move").scale(0.9).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(r4))
        self.play(Create(SurroundingRectangle(r4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): development, HDI, the portrait ---
        self.next_band(2)
        b2_title = Tex("Development: the audit of lives").scale(1.1).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        d1 = Tex("HDI = health + education + income per person").scale(0.9).shift(band_shift(2) + UP * 1.4)
        self.play(Write(d1))
        self.play(Create(SurroundingRectangle(d1, color=GREEN)))
        self.wait(2.5)
        d2 = Tex("Portrait: low income, young populations, joblessness,").scale(0.8).shift(band_shift(2) + UP * 0.45)
        d2b = Tex("raw exports, dualism, thin infrastructure").scale(0.8).shift(band_shift(2) + DOWN * 0.3)
        self.play(Write(d2))
        self.play(Write(d2b))
        self.wait(2.5)
        d3 = Tex("SA matches: dualism, unemployment, raw exports").scale(0.8).shift(band_shift(2) + DOWN * 1.2)
        d4 = Tex("SA breaks: deep markets, banks, universities").scale(0.8).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(d3))
        self.wait(2)
        self.play(Write(d4))
        self.wait(2)
        d5 = Tex("Arguing BOTH sides is the evaluation skill").scale(0.85).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(d5))
        self.wait(3)

        # --- Band 3 (subtopic_2): strategies, the plans, IKS ---
        self.next_band(3)
        b3_title = Tex("Strategies, plans and inside knowledge").scale(1.1).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        s1 = Tex("Families: growth-first; redistribute-with-growth;").scale(0.85).shift(band_shift(3) + UP * 1.4)
        s1b = Tex("basic needs first; export-led").scale(0.85).shift(band_shift(3) + UP * 0.65)
        self.play(Write(s1))
        self.play(Write(s1b))
        self.wait(2.5)
        s2 = Tex(r"RDP $\to$ GEAR $\to$ AsgiSA $\to$ NDP").scale(0.95).shift(band_shift(3) + DOWN * 0.25)
        self.play(Write(s2))
        self.play(Create(SurroundingRectangle(s2, color=GREEN)))
        self.wait(2.5)
        s3 = Tex("Verdict: strong diagnosis, weak delivery").scale(0.9).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(s3))
        self.wait(2)
        s4 = Tex("IKS: cheap, fitted, owned — development").scale(0.85).shift(band_shift(3) + DOWN * 2.1)
        s4b = Tex("done WITH people compounds").scale(0.85).shift(band_shift(3) + DOWN * 2.85)
        self.play(Write(s4))
        self.play(Write(s4b))
        self.wait(3)

        # --- Band 4 (subtopic_3): globalisation causes + scorecard ---
        self.next_band(4)
        b4_title = Tex("Globalisation: causes and scorecard").scale(1.1).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        c1 = Tex("Possible: containers, cables, computing —").scale(0.85).shift(band_shift(4) + UP * 1.4)
        c1b = Tex("the global value chain").scale(0.85).shift(band_shift(4) + UP * 0.65)
        self.play(Write(c1))
        self.play(Write(c1b))
        self.wait(2.5)
        c2 = Tex("Permitted: tariffs down, WTO, finance freed,").scale(0.85).shift(band_shift(4) + DOWN * 0.25)
        c2b = Tex("closed economies rejoining").scale(0.85).shift(band_shift(4) + DOWN * 1.0)
        self.play(Write(c2))
        self.play(Write(c2b))
        self.wait(2.5)
        c3 = Tex("Gains: cheap goods, vehicle-plant jobs, poverty falling").scale(0.75).shift(band_shift(4) + DOWN * 1.9)
        c4 = Tex("Losses: clothing towns, 2008 contagion, uneven shares").scale(0.75).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(c3))
        self.wait(2)
        self.play(Write(c4))
        self.wait(3)

        # --- Band 5 (subtopic_3): the North/South divide ---
        self.next_band(5)
        b5_title = Tex("The divide: three mechanisms, three counterforces").scale(1.0).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(1.5)
        n1 = Tex("1. Terms-of-trade treadmill: raw out, made in").scale(0.85).shift(band_shift(5) + UP * 1.4)
        n2 = Tex("2. Debt in foreign currency squeezes budgets").scale(0.85).shift(band_shift(5) + UP * 0.55)
        n3 = Tex("3. Voice: rules written where votes tilt North").scale(0.85).shift(band_shift(5) + DOWN * 0.3)
        for m in (n1, n2, n3):
            self.play(Write(m))
            self.wait(1.8)
        n4 = Tex("Counterforces: Asia's rise, BRICS, AfCFTA").scale(0.85).shift(band_shift(5) + DOWN * 1.25)
        self.play(Write(n4))
        self.play(Create(SurroundingRectangle(n4, color=GREEN)))
        self.wait(2)
        n5 = Tex("SA straddles: Johannesburg finance, raw-export accounts").scale(0.75).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(n5))
        self.wait(3)

        # --- Band 6 (subtopic_4): market failure and the toolbox ---
        self.next_band(6)
        b6_title = Tex("Where market bookkeeping breaks").scale(1.1).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(1.5)
        f1 = Tex("Externality: cost priced at zero, product too cheap,").scale(0.8).shift(band_shift(6) + UP * 1.4)
        f1b = Tex("society makes too much of it").scale(0.8).shift(band_shift(6) + UP * 0.65)
        self.play(Write(f1))
        self.play(Write(f1b))
        self.wait(2.5)
        f2 = Tex("Commons: whole gain private, loss shared —").scale(0.8).shift(band_shift(6) + DOWN * 0.25)
        f2b = Tex("what belongs to everyone is protected by no one").scale(0.8).shift(band_shift(6) + DOWN * 1.0)
        self.play(Write(f2))
        self.play(Write(f2b))
        self.play(Create(SurroundingRectangle(f2b, color=GREEN)))
        self.wait(2.5)
        f3 = Tex("Toolbox: rules and EIAs; carbon tax and permits;").scale(0.8).shift(band_shift(6) + DOWN * 1.9)
        f3b = Tex("owners for the commons; treaties across borders").scale(0.8).shift(band_shift(6) + DOWN * 2.65)
        self.play(Write(f3))
        self.play(Write(f3b))
        self.wait(3)

        # --- Band 7 (subtopic_4): sustainability and South Africa's stake ---
        self.next_band(7)
        b7_title = Tex("Sustainability, and our stake in it").scale(1.1).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(1.5)
        u1 = Tex("Live off nature's INTEREST; leave the CAPITAL intact").scale(0.85).shift(band_shift(7) + UP * 1.4)
        self.play(Write(u1))
        self.play(Create(SurroundingRectangle(u1, color=GREEN)))
        self.wait(2.5)
        u2 = Tex("Three pillars: economic, social, environmental —").scale(0.85).shift(band_shift(7) + UP * 0.45)
        u2b = Tex("abandon one and lose all three").scale(0.85).shift(band_shift(7) + DOWN * 0.3)
        self.play(Write(u2))
        self.play(Write(u2b))
        self.wait(2.5)
        u3 = Tex("SA stake: water-scarce and warming, drought that").scale(0.8).shift(band_shift(7) + DOWN * 1.2)
        u3b = Tex("forced maize imports, KZN floods, coal-fired exports").scale(0.8).shift(band_shift(7) + DOWN * 1.95)
        self.play(Write(u3))
        self.play(Write(u3b))
        self.wait(2.5)
        u4 = Tex("Green transition = the entry fee for the future").scale(0.85).shift(band_shift(7) + DOWN * 2.85)
        self.play(Write(u4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the loaf and the queue ---
        self.next_band(8)
        b8_title = Tex("The loaf, and the queue of one hundred").scale(1.1).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        q1 = Tex("Two tricks: scrape the price froth, count the eaters").scale(0.85).shift(band_shift(8) + UP * 1.4)
        self.play(Write(q1))
        self.wait(2)
        q2 = Tex("Stroll the queue: past sixty people,").scale(0.85).shift(band_shift(8) + UP * 0.5)
        q2b = Tex("barely a tenth of the loaf counted").scale(0.85).shift(band_shift(8) + DOWN * 0.25)
        self.play(Write(q2))
        self.play(Write(q2b))
        self.wait(2.5)
        q3 = Tex("The sag scored 0 to 1: ours near 0,65").scale(0.9).shift(band_shift(8) + DOWN * 1.15)
        self.play(Write(q3))
        self.play(Create(SurroundingRectangle(q3, color=GREEN)))
        self.wait(2)
        q4 = Tex("Five hands move bread back; every hand has a blister").scale(0.8).shift(band_shift(8) + DOWN * 2.05)
        self.play(Write(q4))
        self.wait(2)
        q5 = Tex("Grow it AND share it — one arm is half an essay").scale(0.8).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(q5))
        self.wait(3)

        # --- Band 9 (subtopic_6): taller or better, and the one-world shop ---
        self.next_band(9)
        b9_title = Tex("Taller or better — and the one-world shop").scale(1.05).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        h1 = Tex("Height is not health: growth is the height,").scale(0.85).shift(band_shift(9) + UP * 1.4)
        h1b = Tex("development is the full medical (HDI: 3 vitals)").scale(0.85).shift(band_shift(9) + UP * 0.65)
        self.play(Write(h1))
        self.play(Write(h1b))
        self.wait(2.5)
        h2 = Tex("Six symptoms on one drive; SA shows some, defies others").scale(0.75).shift(band_shift(9) + DOWN * 0.25)
        self.play(Write(h2))
        self.wait(2)
        h3 = Tex(r"RDP $\to$ GEAR $\to$ AsgiSA $\to$ NDP: thin delivery").scale(0.85).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(h3))
        self.wait(2)
        h4 = Tex("The shop gives gifts and bills; the profitable").scale(0.8).shift(band_shift(9) + DOWN * 2.0)
        h4b = Tex("counters stand up north — so finish what we dig").scale(0.8).shift(band_shift(9) + DOWN * 2.75)
        self.play(Write(h4))
        self.play(Write(h4b))
        self.play(Create(SurroundingRectangle(h4b, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the smoke, the river, the seed ---
        self.next_band(10)
        b10_title = Tex("The smoke, the river and the seed mealies").scale(1.1).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        z1 = Tex("Smoke: fumes on no invoice — bill the polluter").scale(0.85).shift(band_shift(10) + UP * 1.4)
        self.play(Write(z1))
        self.wait(2)
        z2 = Tex("River: private gain, shared loss — install a guardian").scale(0.85).shift(band_shift(10) + UP * 0.5)
        self.play(Write(z2))
        self.wait(2)
        z3 = Tex("Seed: never eat the regenerating stock").scale(0.85).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(z3))
        self.wait(2)
        z4 = Tex("Bill the smoke, guard the river, save the seed").scale(0.9).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(z4))
        self.play(Create(SurroundingRectangle(z4, color=GREEN)))
        self.wait(2.5)
        z5 = Tex("Mechanism, evidence, evaluation —").scale(0.9).shift(band_shift(10) + DOWN * 2.2)
        z5b = Tex("by now it is simply how you think").scale(0.9).shift(band_shift(10) + DOWN * 2.95)
        self.play(Write(z5))
        self.play(Write(z5b))
        self.wait(4)
