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

# Band-layout whiteboard scene for the imperfect-markets session duo.
# Part 1 (Expert): subtopics 1-4; Part 2 (Simplifier): subtopics 5-7.
# Subtopic durations 250/250/230/240/195/195/210 of 1570 s — band dwell
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


class ImperfectMarketsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): monopoly and its barriers ---
        title = Tex("Monopoly, Oligopoly, Monopolistic Competition").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        m_head = Tex("Monopoly: ONE seller, no close substitutes,").scale(1.05).shift(UP * 1.6)
        m_head2 = Tex("BLOCKED entry").scale(1.05).shift(UP * 0.9)
        self.play(Write(m_head), Write(m_head2))
        self.wait(2)
        b1 = Tex("Barriers: patents, licences, franchises").scale(1.0).shift(UP * 0.0)
        b2 = Tex("Control of a key resource").scale(1.0).shift(DOWN * 0.8)
        b3 = Tex("Natural monopoly — one network is cheapest").scale(1.0).shift(DOWN * 1.6)
        b4 = Tex("Economies of scale no entrant can match").scale(1.0).shift(DOWN * 2.4)
        for m in (b1, b2, b3, b4):
            self.play(Write(m))
            self.wait(1.6)
        self.wait(2)

        # --- Band 1 (subtopic_1): MR below AR, and the diagram ---
        self.next_band(1)
        c1_title = Tex("Price maker: MR runs below the demand curve").scale(1.1).shift(band_shift(1) + UP * 2.6)
        self.play(Write(c1_title))
        self.wait(1.5)
        num1 = Tex("Sell 20 at R50 — or 21 at R49:").scale(1.0).shift(band_shift(1) + UP * 1.7)
        num2 = MathTex(r"MR = 49 - 20 = \text{R}29").scale(1.05).shift(band_shift(1) + UP * 0.9)
        self.play(Write(num1))
        self.wait(2)
        self.play(Write(num2))
        self.play(Create(SurroundingRectangle(num2, color=GREEN)))
        self.wait(2)
        o1 = band_shift(1) + LEFT * 4.8 + DOWN * 3.0
        ax1 = axes(o1, 8.0, 4.4, "Q", "P")
        self.play(Create(ax1))
        self.wait(1)
        d = chain(o1, [(0.5, 3.9), (3.5, 2.4), (6.5, 0.9)], color=BLUE)
        d_lab = MathTex(r"D = AR").scale(0.9).next_to(o1 + RIGHT * 6.5 + UP * 0.9, RIGHT, buff=0.15)
        self.play(Create(d), Write(d_lab))
        self.wait(1.5)
        mr = chain(o1, [(0.5, 3.7), (2.4, 2.0), (4.3, 0.3)], color=YELLOW)
        mr_lab = Tex("MR").scale(0.9).next_to(o1 + RIGHT * 4.3 + UP * 0.3, RIGHT, buff=0.15)
        self.play(Create(mr), Write(mr_lab))
        self.wait(1.5)
        mc = chain(o1, [(1.2, 1.6), (2.0, 1.1), (3.2, 1.6), (4.5, 3.2)], color=RED)
        mc_lab = Tex("MC").scale(0.9).next_to(o1 + RIGHT * 4.5 + UP * 3.2, RIGHT, buff=0.15)
        self.play(Create(mc), Write(mc_lab))
        self.wait(1.5)
        q_dot = Dot(o1 + RIGHT * 2.9 + UP * 1.45, color=GREEN)
        p_guide = DashedLine(o1 + RIGHT * 2.9 + UP * 1.45, o1 + RIGHT * 2.9 + UP * 2.7, stroke_width=2)
        p_dot = Dot(o1 + RIGHT * 2.9 + UP * 2.7, color=GREEN)
        read = Tex("Price read UP to D — never off MR").scale(0.95).shift(band_shift(1) + RIGHT * 3.4 + DOWN * 0.4)
        self.play(Create(q_dot), Create(p_guide), Create(p_dot))
        self.play(Write(read))
        self.play(Create(SurroundingRectangle(read, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): oligopoly and the kink ---
        self.next_band(2)
        c2_title = Tex("Oligopoly: the few, and the kink").scale(1.15).shift(band_shift(2) + UP * 2.6)
        self.play(Write(c2_title))
        self.wait(1.5)
        c2_l1 = Tex("Interdependence: each firm watches its rivals").scale(1.0).shift(band_shift(2) + UP * 1.7)
        self.play(Write(c2_l1))
        self.wait(2)
        o2 = band_shift(2) + LEFT * 4.6 + DOWN * 3.0
        ax2 = axes(o2, 7.8, 4.4, "Q", "P")
        self.play(Create(ax2))
        self.wait(1)
        upper = chain(o2, [(0.6, 3.6), (3.4, 2.6)], color=BLUE)
        lower = chain(o2, [(3.4, 2.6), (5.2, 0.6)], color=BLUE)
        kink = Dot(o2 + RIGHT * 3.4 + UP * 2.6, color=YELLOW)
        self.play(Create(upper))
        self.wait(1.5)
        self.play(Create(lower), Create(kink))
        self.wait(1.5)
        e_lab = Tex("Elastic above: raise alone, lose alone").scale(0.9).shift(band_shift(2) + RIGHT * 2.9 + UP * 1.0)
        i_lab = Tex("Inelastic below: cut, get matched, gain nothing").scale(0.9).shift(band_shift(2) + RIGHT * 2.9 + UP * 0.2)
        self.play(Write(e_lab))
        self.wait(2)
        self.play(Write(i_lab))
        self.wait(2)
        sticky = Tex("Result: STICKY prices").scale(1.05).shift(band_shift(2) + RIGHT * 2.9 + DOWN * 0.8)
        self.play(Write(sticky))
        self.play(Create(SurroundingRectangle(sticky, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): non-price war and collusion ---
        self.next_band(3)
        c3_title = Tex("Non-price war — or no war at all").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(c3_title))
        self.wait(1.5)
        c3_l1 = Tex("Branding, advertising, loyalty schemes,").scale(1.0).shift(band_shift(3) + UP * 1.5)
        c3_l2 = Tex("features, service, sponsorships").scale(1.0).shift(band_shift(3) + UP * 0.8)
        self.play(Write(c3_l1))
        self.play(Write(c3_l2))
        self.wait(2)
        c3_l3 = Tex("Overt collusion: CARTEL — agree prices, split markets").scale(1.0).shift(band_shift(3) + DOWN * 0.2)
        c3_l4 = Tex("Tacit collusion: price leadership — follow the leader").scale(1.0).shift(band_shift(3) + DOWN * 1.0)
        self.play(Write(c3_l3))
        self.wait(2)
        self.play(Write(c3_l4))
        self.wait(2)
        c3_l5 = Tex("Cartels cheat from inside and face the law outside").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(c3_l5))
        self.play(Create(SurroundingRectangle(c3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): monopolistic competition ---
        self.next_band(4)
        c4_title = Tex("Monopolistic competition: many, each special").scale(1.1).shift(band_shift(4) + UP * 2.4)
        self.play(Write(c4_title))
        self.wait(1.5)
        c4_l1 = Tex("Many sellers + free entry + differentiated products").scale(1.0).shift(band_shift(4) + UP * 1.5)
        c4_l2 = Tex("Loyalty tilts the demand curve — gently").scale(1.0).shift(band_shift(4) + UP * 0.7)
        c4_l3 = Tex("Short run: a pocket-sized monopoly diagram").scale(1.0).shift(band_shift(4) + DOWN * 0.1)
        c4_l4 = MathTex(r"MR = MC,\ \text{price off } D,\ \text{verdict from } AC").scale(1.0).shift(band_shift(4) + DOWN * 1.0)
        for m in (c4_l1, c4_l2, c4_l3, c4_l4):
            self.play(Write(m))
            self.wait(1.8)
        c4_l5 = Tex("Short-run economic profit: possible").scale(1.0).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(c4_l5))
        self.play(Create(SurroundingRectangle(c4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): entry until tangency ---
        self.next_band(5)
        c5_title = Tex("Free entry shaves profit to the tangency").scale(1.1).shift(band_shift(5) + UP * 2.6)
        self.play(Write(c5_title))
        self.wait(1.5)
        o5 = band_shift(5) + LEFT * 4.6 + DOWN * 2.8
        ax5 = axes(o5, 7.8, 4.4, "Q", "P")
        self.play(Create(ax5))
        self.wait(1)
        ac5 = chain(o5, [(0.8, 3.8), (2.4, 2.2), (3.6, 1.9), (5.2, 2.5), (6.2, 3.3)], color=BLUE)
        ac5_lab = Tex("AC").scale(0.9).next_to(o5 + RIGHT * 6.2 + UP * 3.3, RIGHT, buff=0.15)
        self.play(Create(ac5), Write(ac5_lab))
        self.wait(1.5)
        d5 = chain(o5, [(0.6, 3.6), (2.6, 2.45), (4.6, 1.3)], color=YELLOW)
        d5_lab = Tex("D after entry").scale(0.9).next_to(o5 + RIGHT * 4.6 + UP * 1.3, RIGHT, buff=0.15)
        self.play(Create(d5), Write(d5_lab))
        self.wait(1.5)
        tang = Dot(o5 + RIGHT * 2.6 + UP * 2.45, color=GREEN)
        tang_lab = Tex("Tangency: $P = AC$, normal profit only").scale(0.95).shift(band_shift(5) + RIGHT * 2.8 + UP * 1.4)
        self.play(Create(tang), Write(tang_lab))
        self.play(Create(SurroundingRectangle(tang_lab, color=GREEN)))
        self.wait(2)
        cap1 = Tex("Left of AC's minimum: EXCESS CAPACITY").scale(0.95).shift(band_shift(5) + RIGHT * 2.8 + UP * 0.5)
        cap2 = Tex("The payment for it: VARIETY").scale(0.95).shift(band_shift(5) + RIGHT * 2.8 + DOWN * 0.3)
        self.play(Write(cap1))
        self.wait(2)
        self.play(Write(cap2))
        self.wait(3)

        # --- Band 6 (subtopic_4): the comparison table ---
        self.next_band(6)
        c6_title = Tex("Four structures, five tests").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(c6_title))
        self.wait(1.5)
        t1 = Tex("Sellers: very many / many / few / one").scale(1.0).shift(band_shift(6) + UP * 1.5)
        t2 = Tex("Product: identical / differentiated / either / unique").scale(1.0).shift(band_shift(6) + UP * 0.7)
        t3 = Tex("Entry: free / free / difficult / blocked").scale(1.0).shift(band_shift(6) + DOWN * 0.1)
        t4 = Tex("Price power: none / slight / considerable / full").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        t5 = Tex("Demand curve: flat / gentle slope / kinked / market's own").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        for m in (t1, t2, t3, t4, t5):
            self.play(Write(m))
            self.wait(1.8)
        t6 = Tex("Long-run profit: normal / normal / possible / persistent").scale(1.0).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(t6))
        self.play(Create(SurroundingRectangle(t6, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the two dials ---
        self.next_band(7)
        c7_title = Tex("Two dials generate everything").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(c7_title))
        self.wait(1.5)
        d1 = Rectangle(width=5.4, height=1.6).shift(band_shift(7) + LEFT * 3.2 + UP * 0.8)
        d1_a = Tex("Dial 1: SLOPE").scale(1.0).shift(band_shift(7) + LEFT * 3.2 + UP * 1.1)
        d1_b = Tex("of the firm's demand curve").scale(0.85).shift(band_shift(7) + LEFT * 3.2 + UP * 0.5)
        self.play(Create(d1), Write(d1_a), Write(d1_b))
        self.wait(2)
        d2 = Rectangle(width=5.4, height=1.6).shift(band_shift(7) + RIGHT * 3.2 + UP * 0.8)
        d2_a = Tex("Dial 2: DOOR").scale(1.0).shift(band_shift(7) + RIGHT * 3.2 + UP * 1.1)
        d2_b = Tex("how easily entry happens").scale(0.85).shift(band_shift(7) + RIGHT * 3.2 + UP * 0.5)
        self.play(Create(d2), Write(d2_a), Write(d2_b))
        self.wait(2)
        c7_l1 = Tex("Same three questions every time:").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        c7_l2 = MathTex(r"\text{output at } MR = MC,\ \text{price off } D,\ \text{profit against } AC").scale(0.95).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(c7_l1))
        self.wait(1.5)
        self.play(Write(c7_l2))
        self.play(Create(SurroundingRectangle(c7_l2, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the only ferry across the lagoon ---
        self.next_band(8)
        c8_title = Tex("The only ferry across the lagoon").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(c8_title))
        self.wait(2)
        c8_l1 = Tex("No next crate: raise the fare, most still ride").scale(1.0).shift(band_shift(8) + UP * 1.4)
        c8_l2 = Tex("Price MAKER — leashed only by the demand slope").scale(1.0).shift(band_shift(8) + UP * 0.6)
        self.play(Write(c8_l1))
        self.wait(2)
        self.play(Write(c8_l2))
        self.wait(2)
        c8_l3 = Tex("Cut R30 to R28: EVERYONE pays R28").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        c8_l4 = Tex("— the discount quietly eats the gain (MR below P)").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(c8_l3))
        self.wait(2)
        self.play(Write(c8_l4))
        self.play(Create(SurroundingRectangle(c8_l4, color=GREEN)))
        self.wait(2)
        c8_l5 = Tex("One boat cheaper than two: natural monopoly —").scale(1.0).shift(band_shift(8) + DOWN * 2.2)
        c8_l6 = Tex("regulate the fare, don't force a rival").scale(1.0).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(c8_l5))
        self.play(Write(c8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_6): three bakeries ---
        self.next_band(9)
        c9_title = Tex("Three bakeries and a staring contest").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(c9_title))
        self.wait(2)
        c9_l1 = Tex("Raise a rand: rivals hold, customers leave — lose alone").scale(0.95).shift(band_shift(9) + UP * 1.4)
        self.play(Write(c9_l1))
        self.play(Create(strike(c9_l1)))
        self.wait(2)
        c9_l2 = Tex("Cut a rand: matched by Thursday — gain nothing").scale(0.95).shift(band_shift(9) + UP * 0.5)
        self.play(Write(c9_l2))
        self.play(Create(strike(c9_l2)))
        self.wait(2)
        c9_l3 = Tex("So the price freezes: the kink, wearing an apron").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(c9_l3))
        self.play(Create(SurroundingRectangle(c9_l3, color=GREEN)))
        self.wait(2)
        c9_l4 = Tex("War moves to freshness, vans, sponsor boards").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(c9_l4))
        self.wait(2)
        c9_l5 = Tex("The table at the show: two rand up, all three").scale(1.0).shift(band_shift(9) + DOWN * 2.2)
        self.play(Write(c9_l5))
        self.play(Create(strike(c9_l5)))
        self.wait(1.5)
        c9_l6 = Tex("Cheating inside, Competition Act outside").scale(1.0).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(c9_l6))
        self.wait(3)

        # --- Band 10 (subtopic_7): a street full of takeaways ---
        self.next_band(10)
        c10_title = Tex("A street full of takeaways").scale(1.2).shift(band_shift(10) + UP * 2.6)
        self.play(Write(c10_title))
        self.wait(2)
        c10_l1 = Tex("Fourteen shops, each slightly its own:").scale(1.0).shift(band_shift(10) + UP * 1.7)
        c10_l2 = Tex("crispest chips, halaal, late hours, extra atchar").scale(1.0).shift(band_shift(10) + UP * 0.9)
        self.play(Write(c10_l1))
        self.play(Write(c10_l2))
        self.wait(2)
        c10_l3 = Tex("Regulars pay R5 more — never R15 more").scale(1.0).shift(band_shift(10) + UP * 0.1)
        self.play(Write(c10_l3))
        self.wait(2)
        c10_l4 = Tex("Fat margins invite new shops: profit melts to normal").scale(1.0).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(c10_l4))
        self.play(Create(SurroundingRectangle(c10_l4, color=GREEN)))
        self.wait(2)
        c10_l5 = Tex("Half-idle fryers at 3pm: excess capacity").scale(1.0).shift(band_shift(10) + DOWN * 1.7)
        c10_l6 = Tex("What it buys: VARIETY").scale(1.0).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(c10_l5))
        self.wait(2)
        self.play(Write(c10_l6))
        self.wait(4)
