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

# Band-layout whiteboard scene for the micro revision-essentials duo.
# Part 1 (Expert): subtopics 1-4; Part 2 (Simplifier): subtopics 5-7.
# Subtopic durations 250/250/245/250/195/200/195 of 1585 s — bands
# 0-1 / 2-3 / 4-5 / 6-7 / 8 / 9 / 10 apportioned to match.
# Kinked-demand and externality sketches hand-built from
# Arrow/Line/Dot/Tex primitives only.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


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


class MicroEssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # --- Band 0 (subtopic_1): the price taker's flat line ---
        title = Tex("Micro Essentials — one sweep").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        o = LEFT * 5.2 + DOWN * 2.6
        ax = axes(o, 9.6, 4.2, "quantity", "price, cost")
        self.play(Create(ax))
        flat = Line(o + RIGHT * 0.6 + UP * 2.6, o + RIGHT * 9.0 + UP * 2.6,
                    color=BLUE, stroke_width=4)
        flat_lab = Tex("P $=$ AR $=$ MR").scale(0.85).next_to(o + RIGHT * 9.0 + UP * 2.6, UP, buff=0.15)
        self.play(Create(flat), Write(flat_lab))
        self.wait(1.5)
        ac = chain(o, [(1.6, 3.6), (3.2, 2.2), (4.6, 1.9), (6.2, 2.3), (8.0, 3.4)],
                   color=YELLOW)
        ac_lab = Tex("AC").scale(0.85).next_to(o + RIGHT * 8.0 + UP * 3.4, UP, buff=0.15)
        self.play(Create(ac), Write(ac_lab))
        self.wait(1.5)
        s1 = Tex("Price taker: flat demand at the market price").scale(0.95).shift(UP * 1.4 + RIGHT * 0.6)
        self.play(Write(s1))
        self.wait(2)
        s2 = Tex("Compare price with AC at equilibrium:").scale(0.95).shift(DOWN * 3.3 + LEFT * 2.4)
        s3 = Tex("above $=$ profit, below $=$ loss, touch $=$ normal").scale(0.95).shift(DOWN * 3.9 + LEFT * 2.0)
        self.play(Write(s2))
        self.play(Write(s3))
        self.wait(3)

        # --- Band 1 (subtopic_1): shutdown and the authorities ---
        self.next_band(1)
        b1_title = Tex("Shutdown, and the competition authorities").scale(1.1).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Keep producing at a loss while price covers").scale(1.0).shift(band_shift(1) + UP * 1.4)
        b1_l2 = Tex("average VARIABLE cost — units still help fix costs").scale(0.95).shift(band_shift(1) + UP * 0.7)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Shutdown point: price at the minimum of AVC").scale(1.0).shift(band_shift(1) + DOWN * 0.2)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        b1_l4 = Tex("Competition Act 1998:").scale(1.0).shift(band_shift(1) + DOWN * 1.2)
        b1_l5 = Tex("Commission investigates $\\rightarrow$ Tribunal").scale(0.95).shift(band_shift(1) + DOWN * 1.9)
        b1_l6 = Tex("adjudicates $\\rightarrow$ Appeal Court above").scale(0.95).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): monopoly's two curves ---
        self.next_band(2)
        b2_title = Tex("Monopoly: two curves, one reading").scale(1.15).shift(band_shift(2) + UP * 2.6)
        self.play(Write(b2_title))
        self.wait(1.5)
        o2 = band_shift(2) + LEFT * 5.4 + DOWN * 2.4
        ax2 = axes(o2, 9.6, 4.4, "quantity", "price, cost")
        self.play(Create(ax2))
        dem = Line(o2 + RIGHT * 0.6 + UP * 4.0, o2 + RIGHT * 8.8 + UP * 0.8, color=BLUE, stroke_width=4)
        dem_lab = Tex("D $=$ AR").scale(0.85).next_to(o2 + RIGHT * 8.8 + UP * 0.8, RIGHT, buff=0.15)
        mr = Line(o2 + RIGHT * 0.6 + UP * 3.8, o2 + RIGHT * 5.6 + UP * 0.4, color=GREEN, stroke_width=4)
        mr_lab = Tex("MR below").scale(0.85).next_to(o2 + RIGHT * 5.6 + UP * 0.4, DOWN, buff=0.15)
        self.play(Create(dem), Write(dem_lab))
        self.play(Create(mr), Write(mr_lab))
        self.wait(1.5)
        mc = chain(o2, [(1.6, 1.0), (3.4, 1.6), (4.8, 2.8), (5.8, 4.2)], color=RED)
        mc_lab = Tex("MC").scale(0.85).next_to(o2 + RIGHT * 5.8 + UP * 4.2, UP, buff=0.15)
        self.play(Create(mc), Write(mc_lab))
        self.wait(1.5)
        eq = Dot(o2 + RIGHT * 4.35 + UP * 2.25, color=WHITE)
        up_line = DashedLine(o2 + RIGHT * 4.35 + UP * 2.25, o2 + RIGHT * 4.35 + UP * 2.65,
                             color=WHITE, stroke_width=3)
        pr = Dot(o2 + RIGHT * 4.35 + UP * 2.65, color=BLUE)
        pr_lab = Tex("price read UP on demand").scale(0.8).next_to(o2 + RIGHT * 4.35 + UP * 2.65, UR, buff=0.15)
        self.play(Create(eq))
        self.play(Create(up_line), Create(pr), Write(pr_lab))
        self.wait(2)
        b2_l1 = Tex("Less output, higher price — profit can persist").scale(0.95).shift(band_shift(2) + DOWN * 3.2)
        self.play(Write(b2_l1))
        self.wait(3)

        # --- Band 3 (subtopic_2): the kink, and the blends ---
        self.next_band(3)
        b3_title = Tex("Oligopoly's kink, and the blends").scale(1.15).shift(band_shift(3) + UP * 2.6)
        self.play(Write(b3_title))
        self.wait(1.5)
        o3 = band_shift(3) + LEFT * 5.4 + DOWN * 2.2
        ax3 = axes(o3, 8.6, 4.2, "quantity", "price")
        self.play(Create(ax3))
        kink_top = Line(o3 + RIGHT * 0.8 + UP * 3.8, o3 + RIGHT * 4.2 + UP * 2.4,
                        color=YELLOW, stroke_width=4)
        kink_bot = Line(o3 + RIGHT * 4.2 + UP * 2.4, o3 + RIGHT * 7.6 + UP * 0.4,
                        color=YELLOW, stroke_width=4)
        kdot = Dot(o3 + RIGHT * 4.2 + UP * 2.4, color=RED)
        k_lab = Tex("current price").scale(0.8).next_to(o3 + RIGHT * 4.2 + UP * 2.4, UR, buff=0.15)
        self.play(Create(kink_top))
        self.play(Create(kink_bot))
        self.play(Create(kdot), Write(k_lab))
        self.wait(2)
        b3_l1 = Tex("Above: elastic — a lone rise loses customers").scale(0.9).shift(band_shift(3) + RIGHT * 2.8 + UP * 1.6)
        b3_l2 = Tex("Below: inelastic — a cut is matched at once").scale(0.9).shift(band_shift(3) + RIGHT * 2.8 + UP * 0.9)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("Sticky price $\\Rightarrow$ non-price competition;").scale(0.9).shift(band_shift(3) + DOWN * 3.0 + LEFT * 2.2)
        b3_l4 = Tex("collusion overt or tacit — both illegal").scale(0.9).shift(band_shift(3) + DOWN * 3.6 + LEFT * 2.2)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): the externality graphs ---
        self.next_band(4)
        b4_title = Tex("Market failure: the externality graphs").scale(1.1).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        o4 = band_shift(4) + LEFT * 5.6 + DOWN * 2.2
        ax4 = axes(o4, 5.0, 4.0, "quantity", "price")
        self.play(Create(ax4))
        d4 = Line(o4 + RIGHT * 0.5 + UP * 3.4, o4 + RIGHT * 4.6 + UP * 0.6, color=BLUE, stroke_width=4)
        sp = Line(o4 + RIGHT * 0.5 + UP * 0.5, o4 + RIGHT * 4.6 + UP * 3.2, color=YELLOW, stroke_width=4)
        sp_lab = Tex("S private").scale(0.75).next_to(o4 + RIGHT * 4.6 + UP * 3.2, RIGHT, buff=0.1)
        ss = Line(o4 + RIGHT * 0.5 + UP * 1.5, o4 + RIGHT * 4.2 + UP * 3.9, color=RED, stroke_width=4)
        ss_lab = Tex("S social").scale(0.75).next_to(o4 + RIGHT * 4.2 + UP * 3.9, UP, buff=0.1)
        self.play(Create(d4), Create(sp), Write(sp_lab))
        self.play(Create(ss), Write(ss_lab))
        self.wait(2)
        b4_l1 = Tex("Negative: market makes too much,").scale(0.9).shift(band_shift(4) + RIGHT * 3.2 + UP * 1.4)
        b4_l2 = Tex("too cheap — efficient point sits left").scale(0.9).shift(band_shift(4) + RIGHT * 3.2 + UP * 0.7)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex("Positive: social benefit right of demand —").scale(0.9).shift(band_shift(4) + DOWN * 2.9 + LEFT * 1.6)
        b4_l4 = Tex("market makes too little; public goods: none").scale(0.9).shift(band_shift(4) + DOWN * 3.5 + LEFT * 1.6)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): price controls and CBA ---
        self.next_band(5)
        b5_title = Tex("Price controls, and cost-benefit analysis").scale(1.1).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Max price BELOW equilibrium $\\Rightarrow$ SHORTAGE,").scale(0.95).shift(band_shift(5) + UP * 1.4)
        b5_l2 = Tex("queues and black markets in its shadow").scale(0.95).shift(band_shift(5) + UP * 0.7)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("Min price ABOVE equilibrium $\\Rightarrow$ SURPLUS —").scale(0.95).shift(band_shift(5) + DOWN * 0.2)
        b5_l4 = Tex("the minimum wage is its labour-market form").scale(0.95).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("Tax harm, subsidise benefit, provide public goods").scale(0.95).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l5))
        self.wait(2)
        b5_l6 = Tex("CBA: count ALL costs and benefits, discount,").scale(0.95).shift(band_shift(5) + DOWN * 2.6)
        b5_l7 = Tex("proceed only when social benefit wins").scale(0.95).shift(band_shift(5) + DOWN * 3.3)
        self.play(Write(b5_l6))
        self.play(Write(b5_l7))
        self.play(Create(SurroundingRectangle(b5_l7, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): inflation ---
        self.next_band(6)
        b6_title = Tex("Inflation: one formula, two engines").scale(1.1).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_f1 = MathTex(r"\text{rate} = \frac{\text{new} - \text{old}}{\text{OLD}} \times 100").scale(1.1).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_f1))
        self.play(Create(SurroundingRectangle(b6_f1, color=GREEN)))
        self.wait(2.5)
        b6_l1 = Tex("Demand-pull: credit booms, state spending,").scale(0.95).shift(band_shift(6) + UP * 0.1)
        b6_l2 = Tex("export surges — spending outruns capacity").scale(0.95).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("Cost-push: wages above productivity, weak rand,").scale(0.95).shift(band_shift(6) + DOWN * 1.5)
        b6_l4 = Tex("fuel, electricity, drought").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("Target band 3--6\\%: repo strong on pull, blunt on push").scale(0.9).shift(band_shift(6) + DOWN * 3.1)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): tourism and sustainability ---
        self.next_band(7)
        b7_title = Tex("Tourism, and the planet's prices").scale(1.1).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Tourism: labour-intensive, open at entry —").scale(0.95).shift(band_shift(7) + UP * 1.4)
        b7_l2 = Tex("jobs fast; gains for households, firms, state").scale(0.95).shift(band_shift(7) + UP * 0.7)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("Policy: market, spread beyond icons, build").scale(0.95).shift(band_shift(7) + DOWN * 0.2)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("Sustainability: price the unpriced — rights,").scale(0.95).shift(band_shift(7) + DOWN * 1.1)
        b7_l5 = Tex("charges, green taxes, subsidies, permits").scale(0.95).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(2)
        b7_l6 = Tex("Rio, Kyoto, Paris, the development goals —").scale(0.95).shift(band_shift(7) + DOWN * 2.6)
        b7_l7 = Tex("judge by delivery, not signatures").scale(0.95).shift(band_shift(7) + DOWN * 3.3)
        self.play(Write(b7_l6))
        self.play(Write(b7_l7))
        self.play(Create(SurroundingRectangle(b7_l7, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_5): the street's four markets ---
        self.next_band(8)
        b8_title = Tex("The spaza and the giant").scale(1.15).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = Tex("Fruit sellers: same bananas, given price —").scale(0.95).shift(band_shift(8) + UP * 1.4)
        b8_l2 = Tex("flat demand line, profits melt by Friday").scale(0.95).shift(band_shift(8) + UP * 0.7)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("Water utility: one set of pipes, price made,").scale(0.95).shift(band_shift(8) + DOWN * 0.2)
        b8_l4 = Tex("regulator watching").scale(0.95).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Fuel stations and banks: the watchful few —").scale(0.95).shift(band_shift(8) + DOWN * 1.8)
        b8_l6 = Tex("loyalty cards, not price wars").scale(0.95).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.wait(2)
        b8_l7 = Tex("Spazas: each slightly its own thing — until copied").scale(0.9).shift(band_shift(8) + DOWN * 3.3)
        self.play(Write(b8_l7))
        self.play(Create(SurroundingRectangle(b8_l7, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the blind spots and the fixes ---
        self.next_band(9)
        b9_title = Tex("When the market drops the ball").scale(1.15).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(1.5)
        b9_l1 = Tex("Soapy runoff in the stream $\\rightarrow$ negative").scale(0.95).shift(band_shift(9) + UP * 1.4)
        b9_l2 = Tex("externality: harm priced at zero, too much of it").scale(0.95).shift(band_shift(9) + UP * 0.7)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("Study centre $\\rightarrow$ positive externality:").scale(0.95).shift(band_shift(9) + DOWN * 0.2)
        b9_l4 = Tex("neighbours gain, street buys too little").scale(0.95).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("Streetlight $\\rightarrow$ public good: free riders,").scale(0.95).shift(band_shift(9) + DOWN * 1.8)
        b9_l6 = Tex("municipality builds or nobody does").scale(0.95).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.wait(2)
        b9_l7 = Tex("Tax the harm, subsidise the spillover, build the light").scale(0.9).shift(band_shift(9) + DOWN * 3.3)
        self.play(Write(b9_l7))
        self.play(Create(SurroundingRectangle(b9_l7, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): prices, tourists, the planet ---
        self.next_band(10)
        b10_title = Tex("Prices, tourists and the planet").scale(1.15).shift(band_shift(10) + UP * 2.4)
        self.play(Write(b10_title))
        self.wait(1.5)
        b10_l1 = Tex("Pull: flush month-end tills; push: diesel,").scale(0.95).shift(band_shift(10) + UP * 1.4)
        b10_l2 = Tex("rand, electricity — the cure must match the cause").scale(0.95).shift(band_shift(10) + UP * 0.7)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("Repo cools spenders; it cannot cheapen diesel").scale(0.95).shift(band_shift(10) + DOWN * 0.2)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2)
        b10_l4 = Tex("Tourism: the export that never leaves home —").scale(0.95).shift(band_shift(10) + DOWN * 1.1)
        b10_l5 = Tex("cook, crafter, cleaner, driver all paid").scale(0.95).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(2)
        b10_l6 = Tex("Free dump grows — make the polluter pay;").scale(0.95).shift(band_shift(10) + DOWN * 2.6)
        b10_l7 = Tex("promises are easier than delivery").scale(0.95).shift(band_shift(10) + DOWN * 3.3)
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.play(Create(SurroundingRectangle(b10_l7, color=GREEN)))
        self.wait(4)
