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

# Band-layout whiteboard scene for the Paper 2 practice-run session.
# This practice script runs all seven subtopics as one exam walk-through
# (Section A, short items, two data responses, paragraphs, two essays).
# Subtopic durations 240/220/250/250/250/280/250 of 1740 s — bands
# 0-1 / 2 / 3-4 / 5 / 6-7 / 8-9 / 10 apportioned to match.
# Monopoly and kinked-demand sketches hand-built from Arrow/Line/Dot/Tex.

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


class PaperTwoPracticeRunSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # --- Band 0 (subtopic_1): Section A, the MCQ items ---
        title = Tex("Paper 2 Practice Run — 150 marks").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        m1 = Tex("Formal, written collusion? $\\rightarrow$ CARTELS").scale(1.05).shift(UP * 1.4)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex("Many sellers, differentiated products, easy entry?").scale(1.0).shift(UP * 0.5)
        m2a = Tex("$\\rightarrow$ MONOPOLISTIC COMPETITION").scale(1.05).shift(DOWN * 0.2)
        self.play(Write(m2))
        self.play(Write(m2a))
        self.wait(2.5)
        m3 = Tex("Sustained rise in the general price level?").scale(1.0).shift(DOWN * 1.1)
        m3a = Tex("$\\rightarrow$ INFLATION").scale(1.05).shift(DOWN * 1.8)
        self.play(Write(m3))
        self.play(Write(m3a))
        self.wait(2)
        m4 = Tex("Objective items recycle EXACT definition wording").scale(1.0).shift(DOWN * 2.8)
        self.play(Write(m4))
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): matching and give-the-term ---
        self.next_band(1)
        b1_title = Tex("Matching, and give-the-term").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("One seller, no close substitutes $\\rightarrow$ monopoly").scale(1.0).shift(band_shift(1) + UP * 1.4)
        b1_l2 = Tex("Prices up, output down, jobs down $\\rightarrow$ stagflation").scale(0.95).shift(band_shift(1) + UP * 0.7)
        b1_l3 = Tex("Waste into new products $\\rightarrow$ recycling").scale(1.0).shift(band_shift(1))
        for m in (b1_l1, b1_l2, b1_l3):
            self.play(Write(m))
            self.wait(1.8)
        b1_l4 = Tex("P $=$ min AVC, below it production stops").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        b1_l5 = Tex("$\\rightarrow$ the shutdown point").scale(1.0).shift(band_shift(1) + DOWN * 1.6)
        b1_l6 = Tex("Factory-gate index $\\rightarrow$ producer price index,").scale(1.0).shift(band_shift(1) + DOWN * 2.4)
        b1_l7 = Tex("written in full — the guideline refuses acronyms").scale(1.0).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(2)
        self.play(Write(b1_l6))
        self.play(Write(b1_l7))
        self.play(Create(SurroundingRectangle(b1_l7, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): short items ---
        self.next_band(2)
        b2_title = Tex("Short items: quick micro marks").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("TWO traits of perfect competition $\\rightarrow$ many").scale(1.0).shift(band_shift(2) + UP * 1.4)
        b2_l2 = Tex("buyers and sellers; homogeneous products").scale(1.0).shift(band_shift(2) + UP * 0.7)
        b2_l3 = Tex("TWO non-price weapons $\\rightarrow$ advertising, branding").scale(0.95).shift(band_shift(2))
        b2_l4 = Tex("TWO market failure causes $\\rightarrow$ externalities,").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        b2_l5 = Tex("missing markets").scale(1.0).shift(band_shift(2) + DOWN * 1.4)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4, b2_l5):
            self.play(Write(m))
            self.wait(1.6)
        b2_l6 = Tex("Why can't a monopolist charge anything? The").scale(1.0).shift(band_shift(2) + DOWN * 2.3)
        b2_l7 = Tex("demand curve still rules — pick a pair ON it").scale(1.0).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l6))
        self.play(Write(b2_l7))
        self.play(Create(SurroundingRectangle(b2_l7, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): the monopolist's graph ---
        self.next_band(3)
        b3_title = Tex("Data response: the monopolist's graph").scale(1.1).shift(band_shift(3) + UP * 2.6)
        self.play(Write(b3_title))
        self.wait(1.5)
        o = band_shift(3) + LEFT * 5.2 + DOWN * 2.6
        ax = axes(o, 9.8, 4.6, "Q", "R")
        self.play(Create(ax))
        self.wait(1)
        ar = chain(o, [(0.6, 4.2), (4.0, 2.6), (7.6, 1.0)], color=BLUE)
        ar_lab = Tex("D $=$ AR").scale(0.85).next_to(o + RIGHT * 7.6 + UP * 1.0, RIGHT, buff=0.1)
        self.play(Create(ar), Write(ar_lab))
        self.wait(1.5)
        mr = chain(o, [(0.6, 3.8), (2.6, 2.0), (4.6, 0.3)], color=TEAL)
        mr_lab = Tex("MR").scale(0.85).next_to(o + RIGHT * 4.6 + UP * 0.3, RIGHT, buff=0.1)
        self.play(Create(mr), Write(mr_lab))
        self.wait(1.5)
        ac = chain(o, [(1.2, 3.4), (2.6, 2.3), (3.8, 2.1), (5.6, 2.8), (6.8, 3.5)], color=YELLOW)
        ac_lab = Tex("AC").scale(0.85).next_to(o + RIGHT * 6.8 + UP * 3.5, RIGHT, buff=0.1)
        self.play(Create(ac), Write(ac_lab))
        mc = chain(o, [(1.6, 2.8), (2.6, 1.6), (3.8, 2.1), (4.8, 3.4), (5.4, 4.3)], color=RED)
        mc_lab = Tex("MC").scale(0.85).next_to(o + RIGHT * 5.4 + UP * 4.3, RIGHT, buff=0.1)
        self.play(Create(mc), Write(mc_lab))
        self.wait(1.5)
        eq = Dot(o + RIGHT * 3.1 + UP * 1.55, color=GREEN)
        eq_guide = DashedLine(o + RIGHT * 3.1 + UP * 3.05, o + RIGHT * 3.1, stroke_width=2)
        q_lab = Tex("100").scale(0.85).next_to(o + RIGHT * 3.1, DOWN, buff=0.15)
        self.play(Create(eq), Create(eq_guide), Write(q_lab))
        p_dot = Dot(o + RIGHT * 3.1 + UP * 3.05, color=GREEN)
        p_guide = DashedLine(o + UP * 3.05, o + RIGHT * 3.1 + UP * 3.05, stroke_width=2)
        p_lab = Tex("R150").scale(0.85).next_to(o + UP * 3.05, LEFT, buff=0.15)
        self.play(Create(p_dot), Create(p_guide), Write(p_lab))
        ac_guide = DashedLine(o + UP * 2.25, o + RIGHT * 3.1 + UP * 2.25, stroke_width=2)
        ac_val = Tex("R125").scale(0.85).next_to(o + UP * 2.25, LEFT, buff=0.15)
        self.play(Create(ac_guide), Write(ac_val))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): reading and calculating ---
        self.next_band(4)
        b4_title = Tex("Reading the monopoly graph for marks").scale(1.1).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Price R150, quantity 100 — read straight off").scale(1.0).shift(band_shift(4) + UP * 1.4)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex("Why MR below D: selling one more unit lowers").scale(1.0).shift(band_shift(4) + UP * 0.6)
        b4_l3 = Tex("the price on ALL units, so the extra revenue").scale(1.0).shift(band_shift(4) + DOWN * 0.1)
        b4_l4 = Tex("is less than the price (4 marks)").scale(1.0).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l2))
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = MathTex(r"\text{Profit/unit} = 150 - 125 = \text{R}25").scale(1.05).shift(band_shift(4) + DOWN * 1.7)
        b4_l6 = MathTex(r"\text{Total} = 25 \times 100 = \text{R}2\,500").scale(1.1).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l5))
        self.wait(2)
        self.play(Write(b4_l6))
        self.play(Create(SurroundingRectangle(b4_l6, color=GREEN)))
        b4_l7 = Tex("Reversed gap $\\Rightarrow$ same chain, a R2 500 loss").scale(1.0).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4_l7))
        self.wait(3)

        # --- Band 5 (subtopic_4): inflation figures and weights ---
        self.next_band(5)
        b5_title = Tex("Data response: inflation and the basket").scale(1.1).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("CPI 120,0 last year; 127,2 this year (Stats SA)").scale(1.0).shift(band_shift(5) + UP * 1.5)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"\frac{127{,}2 - 120{,}0}{120{,}0} \times 100 = 6{,}0\%").scale(1.1).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex("Trap: dividing by the NEW index").scale(1.0).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l3))
        self.play(Create(strike(b5_l3)))
        self.wait(2)
        b5_l4 = MathTex(r"0{,}4(8) + 0{,}35(6) + 0{,}25(4)").scale(1.05).shift(band_shift(5) + DOWN * 1.5)
        b5_l5 = MathTex(r"= 3{,}2 + 2{,}1 + 1{,}0 = 6{,}3\%").scale(1.05).shift(band_shift(5) + DOWN * 2.3)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(2)
        b5_l6 = Tex("Fuel and power leading? Cost-push — the repo").scale(1.0).shift(band_shift(5) + DOWN * 3.1)
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_5): the kinked demand curve ---
        self.next_band(6)
        b6_title = Tex("Paragraph: the kinked demand curve").scale(1.1).shift(band_shift(6) + UP * 2.6)
        self.play(Write(b6_title))
        self.wait(1.5)
        o2 = band_shift(6) + LEFT * 4.8 + DOWN * 2.2
        ax2 = axes(o2, 5.6, 4.2, "Q", "P")
        self.play(Create(ax2))
        upper = chain(o2, [(0.5, 3.6), (2.6, 2.4)], color=BLUE)
        lower = chain(o2, [(2.6, 2.4), (4.0, 0.5)], color=BLUE)
        kink = Dot(o2 + RIGHT * 2.6 + UP * 2.4, color=YELLOW)
        k_guide = DashedLine(o2 + UP * 2.4, o2 + RIGHT * 2.6 + UP * 2.4, stroke_width=2)
        k_lab = Tex("current P").scale(0.8).next_to(o2 + UP * 2.4, LEFT, buff=0.1)
        self.play(Create(upper))
        self.play(Create(kink), Create(k_guide), Write(k_lab))
        self.play(Create(lower))
        self.wait(2)
        e_lab = Tex("elastic above").scale(0.85).next_to(o2 + RIGHT * 1.4 + UP * 3.2, RIGHT, buff=0.1)
        i_lab = Tex("inelastic below").scale(0.85).next_to(o2 + RIGHT * 3.6 + UP * 1.3, RIGHT, buff=0.1)
        self.play(Write(e_lab))
        self.play(Write(i_lab))
        self.wait(2)
        b6_l1 = Tex("Raise alone: customers flee to rivals").scale(0.95).shift(band_shift(6) + RIGHT * 3.4 + UP * 1.0)
        b6_l2 = Tex("Cut: matched at once, little gained").scale(0.95).shift(band_shift(6) + RIGHT * 3.4 + UP * 0.2)
        b6_l3 = Tex("Revenue falls BOTH ways, so price").scale(0.95).shift(band_shift(6) + RIGHT * 3.4 + DOWN * 0.6)
        b6_l4 = Tex("stays; rivalry moves to branding").scale(0.95).shift(band_shift(6) + RIGHT * 3.4 + DOWN * 1.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_5): judgements in context ---
        self.next_band(7)
        b7_title = Tex("Higher order: weigh, then judge").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Minimum wage FOR: lifts the working poor,").scale(1.0).shift(band_shift(7) + UP * 1.4)
        b7_l2 = Tex("curbs exploitation, feeds local spending").scale(1.0).shift(band_shift(7) + UP * 0.7)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("AGAINST: set too high it prices unskilled").scale(1.0).shift(band_shift(7) + DOWN * 0.2)
        b7_l4 = Tex("workers out — a labour surplus is unemployment").scale(1.0).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("Judgement: a modest, well-enforced floor helps;").scale(1.0).shift(band_shift(7) + DOWN * 1.8)
        b7_l6 = Tex("an aggressive one bills the unemployed").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(2)
        b7_l7 = Tex("River fix: charge, fine, permit, educate —").scale(1.0).shift(band_shift(7) + DOWN * 3.2)
        self.play(Write(b7_l7))
        self.wait(3)

        # --- Band 8 (subtopic_6): the comparison essay body ---
        self.next_band(8)
        b8_title = Tex("Essay: perfect competition vs monopoly").scale(1.1).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = Tex("Intro (2): structure $=$ sellers, product, entry").scale(1.0).shift(band_shift(8) + UP * 1.5)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("Body (26), paired contrasts: many vs one;").scale(1.0).shift(band_shift(8) + UP * 0.7)
        b8_l3 = Tex("homogeneous vs unique; free entry vs barriers;").scale(1.0).shift(band_shift(8))
        b8_l4 = Tex("price taker vs price maker (demand still rules);").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        b8_l5 = Tex("horizontal D vs downward D with MR below;").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        b8_l6 = Tex("normal profit vs persistent economic profit").scale(1.0).shift(band_shift(8) + DOWN * 2.1)
        for m in (b8_l2, b8_l3, b8_l4, b8_l5, b8_l6):
            self.play(Write(m))
            self.wait(1.8)
        b8_l7 = Tex("Long run: Q at MC $=$ MR, P above on D, barriers").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l7))
        self.wait(3)

        # --- Band 9 (subtopic_6): the weighing and the close ---
        self.next_band(9)
        b9_title = Tex("The additional part: weigh monopoly").scale(1.15).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(1.5)
        b9_l1 = Tex("Not automatically evil: economies of scale;").scale(1.0).shift(band_shift(9) + UP * 1.4)
        b9_l2 = Tex("regulated natural monopolies exploit them").scale(1.0).shift(band_shift(9) + UP * 0.7)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("But unregulated: welfare shifts from consumers,").scale(1.0).shift(band_shift(9) + DOWN * 0.2)
        b9_l4 = Tex("innovation dulls — hence the Competition Act").scale(1.0).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("Conclusion (2): structure shapes conduct,").scale(1.0).shift(band_shift(9) + DOWN * 1.8)
        b9_l6 = Tex("so policy watches structure").scale(1.0).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): combating inflation, planned ---
        self.next_band(10)
        b10_title = Tex("Second option: combating inflation").scale(1.15).shift(band_shift(10) + UP * 2.6)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Monetary: repo up, credit dearer, open market").scale(1.0).shift(band_shift(10) + UP * 1.7)
        b10_l2 = Tex("sales, reserve requirements, moral suasion").scale(1.0).shift(band_shift(10) + UP * 1.0)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Fiscal: spending restraint, taxation, discipline").scale(1.0).shift(band_shift(10) + UP * 0.1)
        b10_l4 = Tex("over administered prices; plus competition,").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        b10_l5 = Tex("productivity, negotiated wage moderation").scale(1.0).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(2.5)
        b10_l6 = Tex("Verdict: targeting anchors expectations, but the").scale(1.0).shift(band_shift(10) + DOWN * 2.1)
        b10_l7 = Tex("repo is a demand weapon — cure must match cause").scale(1.0).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.play(Create(SurroundingRectangle(b10_l7, color=GREEN)))
        self.wait(2)
        b10_l8 = Tex("Checklist: verbs, mark counts, formulas, units").scale(1.0).shift(band_shift(10) + DOWN * 3.4)
        self.play(Write(b10_l8))
        self.wait(4)
