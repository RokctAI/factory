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

# Band-layout whiteboard scene for the growth-and-development session duo.
# Part 1 (Expert): subtopics 1-4; Part 2 (Simplifier): subtopics 5-7.
# Subtopic durations 235/235/240/265/195/200/210 of 1580 s — band dwell
# times are apportioned to match. All diagrams are hand-built from
# exporter-safe primitives (Arrow/Line/Dot/Rectangle/Tex only).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def axes(origin, w, h, xlab, ylab):
    """Two arrows + labels; the exporter has no Axes support."""
    xa = Arrow(origin, origin + RIGHT * w, buff=0, stroke_width=3)
    ya = Arrow(origin, origin + UP * h, buff=0, stroke_width=3)
    xl = Tex(xlab).scale(0.9).next_to(origin + RIGHT * w, DOWN, buff=0.2)
    yl = Tex(ylab).scale(0.9).next_to(origin + UP * h, LEFT, buff=0.2)
    return VGroup(xa, ya, xl, yl)


def chain(origin, pts, color=WHITE, sw=5):
    """Polyline curve: short Line segments, exporter-safe."""
    g = VGroup()
    for a, b in zip(pts[:-1], pts[1:]):
        g.add(Line(origin + RIGHT * a[0] + UP * a[1],
                   origin + RIGHT * b[0] + UP * b[1],
                   color=color, stroke_width=sw))
    return g


class GrowthDevelopmentNorthSouthSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): two different questions ---
        title = Tex("Growth, Development, the North-South Divide").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        g1 = Tex("GROWTH: producing more —").scale(1.05).shift(UP * 1.4)
        g2 = MathTex(r"\%\ \Delta\ \text{real GDP, read against population}").scale(1.0).shift(UP * 0.6)
        self.play(Write(g1))
        self.play(Write(g2))
        self.wait(2)
        d1 = Tex("DEVELOPMENT: living better —").scale(1.05).shift(DOWN * 0.4)
        d2 = Tex("health, learning, standard of living").scale(1.0).shift(DOWN * 1.2)
        self.play(Write(d1))
        self.play(Write(d2))
        self.wait(2)
        rule = Tex("Growth below population growth = poorer average person").scale(0.95).shift(DOWN * 2.2)
        self.play(Write(rule))
        self.play(Create(SurroundingRectangle(rule, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): HDI and the partings ---
        self.next_band(1)
        b1_title = Tex("The HDI — and when the two part company").scale(1.1).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        h1 = Tex("HDI averages three dimensions:").scale(1.0).shift(band_shift(1) + UP * 1.4)
        h2 = Tex("long healthy life $\\cdot$ knowledge $\\cdot$ decent living").scale(1.0).shift(band_shift(1) + UP * 0.6)
        self.play(Write(h1))
        self.play(Write(h2))
        self.play(Create(SurroundingRectangle(h2, color=GREEN)))
        self.wait(2)
        p1 = Tex("Growth without development: the mineral enclave").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        p2 = Tex("Development without growth: grants, housing,").scale(1.0).shift(band_shift(1) + DOWN * 1.2)
        p3 = Tex("treatment lifting indicators in weak-growth years").scale(1.0).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(p1))
        self.wait(2)
        self.play(Write(p2))
        self.play(Write(p3))
        self.wait(2)
        ask = Tex("Ask BOTH questions of every data set").scale(1.0).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(ask))
        self.wait(3)

        # --- Band 2 (subtopic_2): demand-side instruments ---
        self.next_band(2)
        b2_title = Tex("Demand side: raise the spending").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        i1 = MathTex(r"C + I + G + (X - M)").scale(1.1).shift(band_shift(2) + UP * 1.4)
        self.play(Write(i1))
        self.play(Create(SurroundingRectangle(i1, color=GREEN)))
        self.wait(2)
        i2 = Tex("Fiscal: infrastructure, public works, grants").scale(1.0).shift(band_shift(2) + UP * 0.4)
        i3 = Tex("Monetary: lower rates, easier credit").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        i4 = Tex("Export demand: agreements, competitive rand").scale(1.0).shift(band_shift(2) + DOWN * 1.2)
        for m in (i2, i3, i4):
            self.play(Write(m))
            self.wait(1.8)
        i5 = Tex("Case for: spare capacity — spending calls out jobs").scale(1.0).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(i5))
        self.wait(3)

        # --- Band 3 (subtopic_2): the four walls ---
        self.next_band(3)
        b3_title = Tex("Four walls in front of the stimulus").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        w1 = Tex("INFLATION: supply-bound spending lifts prices").scale(1.0).shift(band_shift(3) + UP * 1.4)
        w2 = Tex("IMPORTS: the stimulus leaks abroad").scale(1.0).shift(band_shift(3) + UP * 0.6)
        w3 = Tex("DEBT: interest eats the next budget").scale(1.0).shift(band_shift(3) + DOWN * 0.2)
        w4 = Tex("STRUCTURE: demand cannot train the electrician").scale(1.0).shift(band_shift(3) + DOWN * 1.0)
        for m in (w1, w2, w3, w4):
            self.play(Write(m))
            self.wait(2)
        s1 = Tex("Verdict: relief, not transformation").scale(1.05).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(s1))
        self.play(Create(SurroundingRectangle(s1, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): supply side shifts the PPC ---
        self.next_band(4)
        b4_title = Tex("Supply side: build the capacity").scale(1.15).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        o4 = band_shift(4) + LEFT * 5.4 + DOWN * 2.6
        ax4 = axes(o4, 4.8, 4.2, "Good A", "Good B")
        self.play(Create(ax4))
        self.wait(1)
        ppc1 = chain(o4, [(0.3, 3.2), (1.6, 2.9), (2.8, 2.1), (3.5, 0.9)], color=BLUE)
        self.play(Create(ppc1))
        self.wait(1.5)
        ppc2 = chain(o4, [(0.3, 4.0), (2.0, 3.6), (3.5, 2.6), (4.4, 1.1)], color=GREEN)
        arrow_out = Arrow(o4 + RIGHT * 2.4 + UP * 2.4, o4 + RIGHT * 3.2 + UP * 3.1, buff=0, stroke_width=4, color=GREEN)
        self.play(Create(ppc2), Create(arrow_out))
        self.wait(2)
        m1 = Tex("Costs: power, ports, less red tape").scale(0.95).shift(band_shift(4) + RIGHT * 3.0 + UP * 1.6)
        m2 = Tex("Human capital: schools, colleges, health").scale(0.95).shift(band_shift(4) + RIGHT * 3.0 + UP * 0.8)
        m3 = Tex("Capital and technology; efficient markets").scale(0.95).shift(band_shift(4) + RIGHT * 3.0 + UP * 0.0)
        m4 = Tex("Incentives — and policy certainty").scale(0.95).shift(band_shift(4) + RIGHT * 3.0 + DOWN * 0.8)
        for m in (m1, m2, m3, m4):
            self.play(Write(m))
            self.wait(1.8)
        self.wait(2)

        # --- Band 5 (subtopic_3): evaluation and sequencing ---
        self.next_band(5)
        b5_title = Tex("Evaluating the two approaches").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        e1 = Tex("Supply side: durable — but SLOW,").scale(1.0).shift(band_shift(5) + UP * 1.4)
        e2 = Tex("regressive at first, and needs state capacity").scale(1.0).shift(band_shift(5) + UP * 0.6)
        self.play(Write(e1))
        self.play(Write(e2))
        self.wait(2)
        e3 = Tex("Demand only: today bought at tomorrow's expense").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        e4 = Tex("Supply only: the poor sacrificed to a distant future").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(e3))
        self.wait(2)
        self.play(Write(e4))
        self.wait(2)
        e5 = Tex("Answer: sequencing and proportion —").scale(1.05).shift(band_shift(5) + DOWN * 2.2)
        e6 = Tex("soften the swings, raise the trend").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(e5))
        self.play(Write(e6))
        self.play(Create(SurroundingRectangle(e6, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): South Africa's endeavours ---
        self.next_band(6)
        b6_title = Tex("South Africa's procession of plans").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        s_1 = Tex("RDP 1994: basic needs first").scale(1.0).shift(band_shift(6) + UP * 1.4)
        s_2 = Tex("GEAR 1996: discipline and opening").scale(1.0).shift(band_shift(6) + UP * 0.6)
        s_3 = Tex("ASGISA 2006: name the constraints").scale(1.0).shift(band_shift(6) + DOWN * 0.2)
        s_4 = Tex("NDP 2012: the 2030 destination").scale(1.0).shift(band_shift(6) + DOWN * 1.0)
        for m in (s_1, s_2, s_3, s_4):
            self.play(Write(m))
            self.wait(1.9)
        v1 = Tex("Verdict: stability + social wage achieved;").scale(0.95).shift(band_shift(6) + DOWN * 2.0)
        v2 = Tex("growth trailed population; constraints remain").scale(0.95).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(v1))
        self.play(Write(v2))
        self.play(Create(SurroundingRectangle(v2, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the north-south divide ---
        self.next_band(7)
        b7_title = Tex("The north-south divide").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        n1 = Tex("North: manufactures, capital, rule-writing votes").scale(1.0).shift(band_shift(7) + UP * 1.4)
        n2 = Tex("South: commodities, foreign-currency debt,").scale(1.0).shift(band_shift(7) + UP * 0.6)
        n3 = Tex("conditional aid, emigrating skills").scale(1.0).shift(band_shift(7) + DOWN * 0.1)
        for m in (n1, n2, n3):
            self.play(Write(m))
            self.wait(1.8)
        n4 = Tex("Gap-keepers: terms of trade, debt service,").scale(1.0).shift(band_shift(7) + DOWN * 1.0)
        n5 = Tex("tariff escalation, brain drain").scale(1.0).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(n4))
        self.play(Write(n5))
        self.play(Create(SurroundingRectangle(n5, color=GREEN)))
        self.wait(2)
        n6 = Tex("Counter-currents: east Asia, BRICS, AfCFTA, remittances").scale(0.95).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(n6))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the payslip and the report card ---
        self.next_band(8)
        b8_title = Tex("The payslip and the report card").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        r1 = Rectangle(width=5.6, height=2.6).shift(band_shift(8) + LEFT * 3.2 + UP * 0.7)
        r1_a = Tex("House one").scale(0.95).shift(band_shift(8) + LEFT * 3.2 + UP * 1.5)
        r1_b = Tex("income climbing —").scale(0.8).shift(band_shift(8) + LEFT * 3.2 + UP * 0.7)
        r1_c = Tex("school lost, clinic missed").scale(0.8).shift(band_shift(8) + LEFT * 3.2 + UP * 0.1)
        self.play(Create(r1), Write(r1_a))
        self.play(Write(r1_b), Write(r1_c))
        self.wait(2)
        r2 = Rectangle(width=5.6, height=2.6).shift(band_shift(8) + RIGHT * 3.2 + UP * 0.7)
        r2_a = Tex("House two").scale(0.95).shift(band_shift(8) + RIGHT * 3.2 + UP * 1.5)
        r2_b = Tex("income flat —").scale(0.8).shift(band_shift(8) + RIGHT * 3.2 + UP * 0.7)
        r2_c = Tex("children schooled, medicine collected").scale(0.8).shift(band_shift(8) + RIGHT * 3.2 + UP * 0.1)
        self.play(Create(r2), Write(r2_a))
        self.play(Write(r2_b), Write(r2_c))
        self.wait(2)
        b8_l1 = Tex("Payslip = growth; report card = development").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l1))
        self.play(Create(SurroundingRectangle(b8_l1, color=GREEN)))
        self.wait(2)
        b8_l2 = Tex("Strip inflation, divide by people, then judge").scale(1.0).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l2))
        self.wait(3)

        # --- Band 9 (subtopic_6): feed the fire or build the stove ---
        self.next_band(9)
        b9_title = Tex("Feed the fire or build the stove").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2)
        f1 = Tex("Fire: money in pockets, spent at the spaza,").scale(1.0).shift(band_shift(9) + UP * 1.4)
        f2 = Tex("warmth spreading — the multiplier at home").scale(1.0).shift(band_shift(9) + UP * 0.7)
        self.play(Write(f1))
        self.play(Write(f2))
        self.wait(2)
        f3 = Tex("Four limits: full pots, far-away shops,").scale(1.0).shift(band_shift(9) + DOWN * 0.2)
        f4 = Tex("the lender at the door, the unwired stove").scale(1.0).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(f3))
        self.play(Write(f4))
        self.wait(2)
        f5 = Tex("Stove: wiring, the bakkie, matric and college,").scale(1.0).shift(band_shift(9) + DOWN * 1.8)
        f6 = Tex("a safe street — slow, then permanent").scale(1.0).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(f5))
        self.play(Write(f6))
        self.wait(2)
        f7 = Tex("Two clocks: fire for this winter, stove for all winters").scale(0.95).shift(band_shift(9) + DOWN * 3.3)
        self.play(Write(f7))
        self.play(Create(SurroundingRectangle(f7, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the street and the suburb ---
        self.next_band(10)
        b10_title = Tex("The street and the suburb").scale(1.2).shift(band_shift(10) + UP * 2.6)
        self.play(Write(b10_title))
        self.wait(2)
        g_1 = Tex("Suburb inherits working systems; street supplies it").scale(1.0).shift(band_shift(10) + UP * 1.7)
        self.play(Write(g_1))
        self.wait(2)
        g_2 = Tex("Gap-keepers: raw in cheap, made goods taxed,").scale(1.0).shift(band_shift(10) + UP * 0.9)
        g_3 = Tex("suburb-currency debt, boardroom votes, brain drain").scale(1.0).shift(band_shift(10) + UP * 0.2)
        self.play(Write(g_2))
        self.play(Write(g_3))
        self.play(Create(SurroundingRectangle(g_3, color=GREEN)))
        self.wait(2)
        g_4 = Tex("Redrawn map: east Asia's stoves, the street").scale(1.0).shift(band_shift(10) + DOWN * 0.8)
        g_5 = Tex("trading with itself, remittances rivalling aid").scale(1.0).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(g_4))
        self.play(Write(g_5))
        self.wait(2)
        g_6 = Tex("The corner house: growth to afford the future,").scale(1.0).shift(band_shift(10) + DOWN * 2.4)
        g_7 = Tex("development so everyone arrives there").scale(1.0).shift(band_shift(10) + DOWN * 3.1)
        self.play(Write(g_6))
        self.play(Write(g_7))
        self.play(Create(SurroundingRectangle(g_7, color=GREEN)))
        self.wait(4)
