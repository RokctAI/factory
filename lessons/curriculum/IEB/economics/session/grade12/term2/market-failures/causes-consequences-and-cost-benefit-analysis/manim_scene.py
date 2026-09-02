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

# Band-layout whiteboard scene for the market-failures session duo.
# Part 1 (Expert): subtopics 1-4; Part 2 (Simplifier): subtopics 5-7.
# Subtopic durations 235/255/245/240/195/190/210 of 1570 s — band dwell
# times are apportioned to match. All diagrams are hand-built from
# exporter-safe primitives (Arrow/Line/Dot/Rectangle/Tex only).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


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


class MarketFailuresSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the definition, causes 1-3 ---
        title = Tex("Market Failure and Cost-Benefit Analysis").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Failure = the QUANTITIES are wrong,").scale(1.05).shift(UP * 1.5)
        d2 = Tex("judged against the social optimum").scale(1.05).shift(UP * 0.8)
        self.play(Write(d1), Write(d2))
        self.play(Create(SurroundingRectangle(VGroup(d1, d2), color=GREEN)))
        self.wait(2)
        c1 = Tex("1. Externalities — spillovers the price ignores").scale(1.0).shift(DOWN * 0.4)
        c2 = Tex("2. Missing markets — public and merit goods").scale(1.0).shift(DOWN * 1.2)
        c3 = Tex("3. Imperfect competition — price above MC").scale(1.0).shift(DOWN * 2.0)
        for m in (c1, c2, c3):
            self.play(Write(m))
            self.wait(1.8)
        self.wait(2)

        # --- Band 1 (subtopic_1): causes 4-6 ---
        self.next_band(1)
        b1_title = Tex("Three more causes").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        c4 = Tex("4. Imperfect information — wrong facts, wrong quantities").scale(1.0).shift(band_shift(1) + UP * 1.3)
        c5 = Tex("5. Immobile factors — skills and capital stuck").scale(1.0).shift(band_shift(1) + UP * 0.4)
        c6 = Tex("6. Inequality — rand votes, not need").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        for m in (c4, c5, c6):
            self.play(Write(m))
            self.wait(2)
        eq = Tex("Efficiency and equity are DIFFERENT tests").scale(1.05).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(eq))
        self.play(Create(SurroundingRectangle(eq, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): negative production externality ---
        self.next_band(2)
        b2_title = Tex("The brick kiln: external cost on top").scale(1.1).shift(band_shift(2) + UP * 2.6)
        self.play(Write(b2_title))
        self.wait(1.5)
        o2 = band_shift(2) + LEFT * 4.6 + DOWN * 2.8
        ax2 = axes(o2, 7.8, 4.6, "Q", "P")
        self.play(Create(ax2))
        self.wait(1)
        dem = chain(o2, [(0.6, 3.9), (3.4, 2.2), (6.2, 0.7)], color=BLUE)
        dem_lab = Tex("D").scale(0.9).next_to(o2 + RIGHT * 6.2 + UP * 0.7, RIGHT, buff=0.15)
        self.play(Create(dem), Write(dem_lab))
        self.wait(1)
        mpc = chain(o2, [(0.8, 0.7), (3.4, 2.2), (5.8, 3.5)], color=YELLOW)
        mpc_lab = Tex("MPC").scale(0.85).next_to(o2 + RIGHT * 5.8 + UP * 3.5, RIGHT, buff=0.15)
        self.play(Create(mpc), Write(mpc_lab))
        self.wait(1.5)
        msc = chain(o2, [(0.8, 1.7), (2.6, 2.75), (4.8, 4.0)], color=RED)
        msc_lab = Tex("MSC").scale(0.85).next_to(o2 + RIGHT * 4.8 + UP * 4.0, RIGHT, buff=0.15)
        self.play(Create(msc), Write(msc_lab))
        self.wait(1.5)
        mkt = Dot(o2 + RIGHT * 3.4 + UP * 2.2, color=YELLOW)
        soc = Dot(o2 + RIGHT * 2.6 + UP * 2.75, color=GREEN)
        self.play(Create(mkt), Create(soc))
        self.wait(1.5)
        verdict = Tex("Market over-produces and under-prices").scale(1.0).shift(band_shift(2) + RIGHT * 3.0 + UP * 1.2)
        self.play(Write(verdict))
        self.play(Create(SurroundingRectangle(verdict, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): positive consumption externality ---
        self.next_band(3)
        b3_title = Tex("Education: external benefit on top").scale(1.1).shift(band_shift(3) + UP * 2.6)
        self.play(Write(b3_title))
        self.wait(1.5)
        o3 = band_shift(3) + LEFT * 4.6 + DOWN * 2.8
        ax3 = axes(o3, 7.8, 4.6, "Q", "P")
        self.play(Create(ax3))
        self.wait(1)
        sup = chain(o3, [(0.8, 0.7), (3.2, 2.1), (5.8, 3.5)], color=YELLOW)
        sup_lab = Tex("S").scale(0.9).next_to(o3 + RIGHT * 5.8 + UP * 3.5, RIGHT, buff=0.15)
        self.play(Create(sup), Write(sup_lab))
        self.wait(1)
        mpb = chain(o3, [(0.6, 3.4), (3.2, 2.1), (5.6, 0.9)], color=BLUE)
        mpb_lab = Tex("MPB").scale(0.85).next_to(o3 + RIGHT * 5.6 + UP * 0.9, RIGHT, buff=0.15)
        self.play(Create(mpb), Write(mpb_lab))
        self.wait(1.5)
        msb = chain(o3, [(0.6, 4.4), (4.0, 2.55), (6.6, 1.2)], color=GREEN)
        msb_lab = Tex("MSB").scale(0.85).next_to(o3 + RIGHT * 6.6 + UP * 1.2, RIGHT, buff=0.15)
        self.play(Create(msb), Write(msb_lab))
        self.wait(1.5)
        mkt3 = Dot(o3 + RIGHT * 3.2 + UP * 2.1, color=BLUE)
        soc3 = Dot(o3 + RIGHT * 4.0 + UP * 2.55, color=GREEN)
        self.play(Create(mkt3), Create(soc3))
        self.wait(1.5)
        verdict3 = Tex("Market under-produces the spillover good").scale(1.0).shift(band_shift(3) + RIGHT * 3.0 + UP * 1.2)
        self.play(Write(verdict3))
        self.play(Create(SurroundingRectangle(verdict3, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): consequences, taxes and subsidies ---
        self.next_band(4)
        b4_title = Tex("Consequences — and the first two tools").scale(1.1).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Misallocation, degraded environment, missing").scale(1.0).shift(band_shift(4) + UP * 1.5)
        b4_l2 = Tex("public goods, deeper inequality, macro costs").scale(1.0).shift(band_shift(4) + UP * 0.8)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex("TAX the external cost: carbon tax, fuel levy,").scale(1.0).shift(band_shift(4) + DOWN * 0.2)
        b4_l4 = Tex("excise duties, sugary drinks levy").scale(1.0).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex("SUBSIDISE the external benefit: no-fee schools,").scale(1.0).shift(band_shift(4) + DOWN * 1.8)
        b4_l6 = Tex("free clinics, funded students").scale(1.0).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l5))
        self.play(Write(b4_l6))
        self.play(Create(SurroundingRectangle(b4_l6, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): provision, regulation, prices ---
        self.next_band(5)
        b5_title = Tex("The rest of the toolkit").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Direct provision: streetlights, courts, defence").scale(1.0).shift(band_shift(5) + UP * 1.5)
        b5_l2 = Tex("Regulation: emission limits, bans, labels").scale(1.0).shift(band_shift(5) + UP * 0.7)
        b5_l3 = Tex("Max price: affordable — but risks shortages").scale(1.0).shift(band_shift(5) + DOWN * 0.1)
        b5_l4 = Tex("Min price: protects sellers — risks surpluses").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        b5_l5 = Tex("Redistribution: progressive tax and grants").scale(1.0).shift(band_shift(5) + DOWN * 1.7)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4, b5_l5):
            self.play(Write(m))
            self.wait(1.8)
        b5_l6 = Tex("Every tool has a cost — argue each case").scale(1.0).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l6))
        self.play(Create(SurroundingRectangle(b5_l6, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): CBA in five steps ---
        self.next_band(6)
        b6_title = Tex("Cost-benefit analysis: five steps").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        s1 = Tex("1. List ALL costs — external ones included").scale(1.0).shift(band_shift(6) + UP * 1.5)
        s2 = Tex("2. List ALL benefits — spillovers included").scale(1.0).shift(band_shift(6) + UP * 0.7)
        s3 = Tex("3. Value everything in money — even the unpriced").scale(1.0).shift(band_shift(6) + DOWN * 0.1)
        s4 = Tex("4. DISCOUNT future flows to today's rand").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        s5 = Tex("5. Compare — and rank by benefit per rand").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        for m in (s1, s2, s3, s4, s5):
            self.play(Write(m))
            self.wait(1.8)
        rule = MathTex(r"\text{Build if social benefits} > \text{social costs}").scale(1.0).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(rule))
        self.play(Create(SurroundingRectangle(rule, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the four limits ---
        self.next_band(7)
        b7_title = Tex("Four honest limits of CBA").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        l1 = Tex("Valuing the unpriceable is contested").scale(1.0).shift(band_shift(7) + UP * 1.4)
        l2 = Tex("The discount rate is a moral dial").scale(1.0).shift(band_shift(7) + UP * 0.6)
        l3 = Tex("Optimism bias: champions round their own way").scale(1.0).shift(band_shift(7) + DOWN * 0.2)
        l4 = Tex("Totals never ask WHOSE rands").scale(1.0).shift(band_shift(7) + DOWN * 1.0)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2)
        close = Tex("Honest CBA disciplines politics; cynical CBA dresses it").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(close))
        self.play(Create(SurroundingRectangle(close, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the bill nobody sends ---
        self.next_band(8)
        b8_title = Tex("The bill nobody sends").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Coal: R90 at the gate + R7 in soap, paint,").scale(1.0).shift(band_shift(8) + UP * 1.4)
        b8_l2 = Tex("inhalers and taxi fare = R97 true cost").scale(1.0).shift(band_shift(8) + UP * 0.7)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2)
        b8_l3 = Tex("Looks R7 cheaper than it is — so people buy MORE").scale(1.0).shift(band_shift(8) + DOWN * 0.3)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("The gym: R60 buys fitness — and calmer streets").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        b8_l5 = Tex("nobody pays for — so too few join").scale(1.0).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2)
        b8_l6 = Tex("Unsent bill: too much. Unsent thank-you: too little.").scale(1.0).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): fixing the price ---
        self.next_band(9)
        b9_title = Tex("Fixing the price until it tells the truth").scale(1.15).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Deliver the bill: R7 levy per bag —").scale(1.0).shift(band_shift(9) + UP * 1.4)
        b9_l2 = Tex("coal at R97, fewer trucks, funded clinics").scale(1.0).shift(band_shift(9) + UP * 0.7)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("Deliver the thank-you: gym subsidised to R30 — full").scale(1.0).shift(band_shift(9) + DOWN * 0.2)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("No bill possible: state buys the streetlight outright").scale(1.0).shift(band_shift(9) + DOWN * 1.1)
        b9_l5 = Tex("Harm too grave to tax: cover the loads — a RULE").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l4))
        self.wait(2)
        self.play(Write(b9_l5))
        self.wait(2)
        b9_l6 = Tex("Markets fail; fixers fail too — pick the smaller failure").scale(0.95).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): should the toll road be built? ---
        self.next_band(10)
        b10_title = Tex("Should the toll road be built?").scale(1.2).shift(band_shift(10) + UP * 2.6)
        self.play(Write(b10_title))
        self.wait(2)
        cost_box = Rectangle(width=5.6, height=2.4).shift(band_shift(10) + LEFT * 3.2 + UP * 0.8)
        cost_h = Tex("Costs").scale(1.0).shift(band_shift(10) + LEFT * 3.2 + UP * 1.6)
        cost_1 = Tex("tar, 40 households moved,").scale(0.8).shift(band_shift(10) + LEFT * 3.2 + UP * 0.8)
        cost_2 = Tex("split farm, lost trade, noise").scale(0.8).shift(band_shift(10) + LEFT * 3.2 + UP * 0.2)
        self.play(Create(cost_box), Write(cost_h))
        self.play(Write(cost_1), Write(cost_2))
        self.wait(2)
        ben_box = Rectangle(width=5.6, height=2.4).shift(band_shift(10) + RIGHT * 3.2 + UP * 0.8)
        ben_h = Tex("Benefits").scale(1.0).shift(band_shift(10) + RIGHT * 3.2 + UP * 1.6)
        ben_1 = Tex("hours saved, crashes avoided,").scale(0.8).shift(band_shift(10) + RIGHT * 3.2 + UP * 0.8)
        ben_2 = Tex("trade to the port, jobs").scale(0.8).shift(band_shift(10) + RIGHT * 3.2 + UP * 0.2)
        self.play(Create(ben_box), Write(ben_h))
        self.play(Write(ben_1), Write(ben_2))
        self.wait(2)
        b10_l1 = Tex("Shrink future rands first — then compare").scale(1.0).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l1))
        self.play(Create(SurroundingRectangle(b10_l1, color=GREEN)))
        self.wait(2)
        b10_l2 = Tex("And always ask: WHO carries the cost,").scale(1.0).shift(band_shift(10) + DOWN * 1.8)
        b10_l3 = Tex("and are the losers compensated?").scale(1.0).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(b10_l2))
        self.play(Write(b10_l3))
        self.wait(4)
