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

# Band-layout whiteboard scene for the revision duo "Basic Concepts and
# Markets Essentials" (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier
# subtopics 5-7). Exporter-safe primitives only; add-only lifecycle.
# Subtopic durations: 235/235/230/240/195/190/195 of 1520 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BasicConceptsMarketsRevisionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===================== Part 1 — Expert =====================
        # --- Band 0 (subtopic_1): scarcity, choice, opportunity cost ---
        title = Tex("Revision Sweep One: Four Structures").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0a = Tex("Scarcity: permanent — limited means, unlimited wants").scale(0.95).shift(UP * 1.2)
        self.play(Write(b0a))
        self.wait(2)
        b0b = Tex("Choice follows; opportunity cost follows choice").scale(1.0).shift(UP * 0.4)
        self.play(Write(b0b))
        self.wait(2)
        b0c = Tex("Opportunity cost = the NEXT BEST alternative only").scale(1.0).shift(DOWN * 0.5)
        self.play(Write(b0c))
        self.play(Create(SurroundingRectangle(b0c, color=GREEN)))
        self.wait(2)
        b0d = Tex("WHAT $\\cdot$ HOW $\\cdot$ FOR WHOM").scale(1.05).shift(DOWN * 1.5)
        b0e = Tex("micro: one unit; macro: the totals").scale(0.95).shift(DOWN * 2.3)
        self.play(Write(b0d))
        self.wait(2)
        self.play(Write(b0e))
        self.wait(3)

        # --- Band 1 (subtopic_1): the production possibility curve ---
        self.next_band(1)
        b1t = Tex("The production possibility curve").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        ax_v = Line(band_shift(1) + DOWN * 1.8 + LEFT * 3.6, band_shift(1) + UP * 1.4 + LEFT * 3.6)
        ax_h = Line(band_shift(1) + DOWN * 1.8 + LEFT * 3.6, band_shift(1) + DOWN * 1.8 + RIGHT * 2.6)
        lab_v = Tex("fruit").scale(0.8).shift(band_shift(1) + UP * 1.6 + LEFT * 3.6)
        lab_h = Tex("furniture").scale(0.8).shift(band_shift(1) + DOWN * 2.2 + RIGHT * 2.4)
        self.play(Create(ax_v), Create(ax_h))
        self.play(Write(lab_v), Write(lab_h))
        curve = ArcBetweenPoints(band_shift(1) + UP * 1.2 + LEFT * 3.4,
                                 band_shift(1) + DOWN * 1.6 + RIGHT * 2.2, angle=-TAU / 5)
        self.play(Create(curve))
        self.wait(2)
        d_on = Dot(band_shift(1) + UP * 0.5 + LEFT * 0.6)
        t_on = Tex("on: efficient").scale(0.8).shift(band_shift(1) + UP * 0.9 + RIGHT * 1.2)
        self.play(Create(d_on), Write(t_on))
        self.wait(1.5)
        d_in = Dot(band_shift(1) + DOWN * 0.9 + LEFT * 2.2)
        t_in = Tex("inside: idle resources").scale(0.8).shift(band_shift(1) + DOWN * 0.5 + LEFT * 0.2)
        self.play(Create(d_in), Write(t_in))
        self.wait(1.5)
        d_out = Dot(band_shift(1) + UP * 1.1 + RIGHT * 1.9)
        t_out = Tex("beyond: unattainable today").scale(0.8).shift(band_shift(1) + UP * 1.7 + RIGHT * 1.9)
        self.play(Create(d_out), Write(t_out))
        self.wait(2)
        b1e = Tex("Outward shift of the whole curve = growth").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1e))
        self.play(Create(SurroundingRectangle(b1e, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the circular flow ---
        self.next_band(2)
        b2t = Tex("The circular flow").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        rh = Rectangle(width=3.2, height=1.1).shift(band_shift(2) + LEFT * 3.6)
        th = Tex("Households").scale(0.85).move_to(rh.get_center())
        rf = Rectangle(width=3.2, height=1.1).shift(band_shift(2) + RIGHT * 3.6)
        tf = Tex("Firms").scale(0.85).move_to(rf.get_center())
        self.play(Create(rh), Write(th))
        self.play(Create(rf), Write(tf))
        self.wait(1.5)
        a_top = Arrow(rh.get_top() + UP * 0.1, rf.get_top() + UP * 0.1, buff=0.2)
        t_top = Tex("factors sold; goods bought").scale(0.75).shift(band_shift(2) + UP * 1.3)
        a_bot = Arrow(rf.get_bottom() + DOWN * 0.1, rh.get_bottom() + DOWN * 0.1, buff=0.2)
        t_bot = Tex("income paid; spending returns").scale(0.75).shift(band_shift(2) + DOWN * 1.3)
        self.play(Create(a_top), Write(t_top))
        self.play(Create(a_bot), Write(t_bot))
        self.wait(2)
        b2e = Tex("Money one way; goods and factors the other").scale(0.95).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2e))
        self.play(Create(SurroundingRectangle(b2e, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): leakages, injections, GDP vs GNI ---
        self.next_band(3)
        b3t = Tex("Leaks, refills, and the national count").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = Tex("Leakages: saving $\\cdot$ taxes $\\cdot$ imports").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3b = Tex("Injections: investment $\\cdot$ government $\\cdot$ exports").scale(1.0).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3a))
        self.play(Write(b3b))
        self.wait(2.5)
        b3c = Tex("GDP: WHERE it was produced — inside the borders").scale(0.95).shift(band_shift(3) + DOWN * 0.7)
        b3d = Tex("GNI: WHO owns the factors — income follows home").scale(0.95).shift(band_shift(3) + DOWN * 1.4)
        self.play(Write(b3c))
        self.play(Write(b3d))
        self.wait(2.5)
        b3e = Tex("Final goods only — never count the flour twice").scale(0.95).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3e))
        self.play(Create(SurroundingRectangle(b3e, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): demand, supply and equilibrium ---
        self.next_band(4)
        b4t = Tex("Demand, supply, equilibrium").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        ax2v = Line(band_shift(4) + DOWN * 1.8 + LEFT * 3.2, band_shift(4) + UP * 1.4 + LEFT * 3.2)
        ax2h = Line(band_shift(4) + DOWN * 1.8 + LEFT * 3.2, band_shift(4) + DOWN * 1.8 + RIGHT * 2.8)
        self.play(Create(ax2v), Create(ax2h))
        dem = Line(band_shift(4) + UP * 1.2 + LEFT * 2.8, band_shift(4) + DOWN * 1.5 + RIGHT * 2.4)
        sup = Line(band_shift(4) + DOWN * 1.5 + LEFT * 2.8, band_shift(4) + UP * 1.2 + RIGHT * 2.4)
        t_d = Tex("D").scale(0.85).shift(band_shift(4) + DOWN * 1.2 + RIGHT * 2.7)
        t_s = Tex("S").scale(0.85).shift(band_shift(4) + UP * 1.4 + RIGHT * 2.7)
        self.play(Create(dem), Write(t_d))
        self.play(Create(sup), Write(t_s))
        self.wait(2)
        eq = Dot(band_shift(4) + DOWN * 0.15 + LEFT * 0.2)
        t_eq = Tex("equilibrium: plans agree").scale(0.85).shift(band_shift(4) + UP * 0.5 + RIGHT * 1.6)
        self.play(Create(eq), Write(t_eq))
        self.wait(2)
        b4e = Tex("No queue, no pile — the market cleared").scale(0.95).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4e))
        self.play(Create(SurroundingRectangle(b4e, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): movement vs shift, the egg shock ---
        self.next_band(5)
        b5t = Tex("Movement along, or shift of the whole curve?").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = Tex("Own price changes: movement ALONG").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5b = Tex("Anything else changes first: the CURVE shifts").scale(1.0).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5a))
        self.play(Write(b5b))
        self.wait(2)
        b5wrong = Tex("A product's own price shifts its own curve").scale(0.95).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5wrong))
        self.play(Create(strike(b5wrong)))
        self.wait(2)
        b5c = Tex("Egg shock: supply LEFT; shortage at old price;").scale(0.95).shift(band_shift(5) + DOWN * 1.5)
        b5c2 = Tex("price bid up; smaller quantity at new crossing").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5c))
        self.play(Write(b5c2))
        self.wait(2)
        b5d = Tex("Four steps: curve, direction, excess, new equilibrium").scale(0.9).shift(band_shift(5) + DOWN * 3.1)
        self.play(Write(b5d))
        self.play(Create(SurroundingRectangle(b5d, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): utility, value, price; market types ---
        self.next_band(6)
        b6t = Tex("Utility, value, price — and market structures").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = Tex("Utility: satisfaction $\\cdot$ Value: utility + scarcity").scale(0.95).shift(band_shift(6) + UP * 1.1)
        b6b = Tex("Price: value in money — water cheap, diamonds dear").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6a))
        self.play(Write(b6b))
        self.wait(2.5)
        b6c = Tex("Perfect: many buyers and sellers, same product,").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        b6c2 = Tex("full information, free entry — nobody sets the price").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6c))
        self.play(Write(b6c2))
        self.wait(2.5)
        b6d = Tex("Imperfect: monopoly (one), oligopoly (few),").scale(0.95).shift(band_shift(6) + DOWN * 2.0)
        b6d2 = Tex("monopolistic competition (many, differentiated)").scale(0.95).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6d))
        self.play(Write(b6d2))
        self.wait(3)

        # --- Band 7 (subtopic_4): the business cycle wave ---
        self.next_band(7)
        b7t = Tex("The business cycle and its instruments").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        w1 = ArcBetweenPoints(band_shift(7) + LEFT * 4.4 + DOWN * 0.6,
                              band_shift(7) + LEFT * 1.4 + UP * 0.9, angle=-TAU / 8)
        w2 = ArcBetweenPoints(band_shift(7) + LEFT * 1.4 + UP * 0.9,
                              band_shift(7) + RIGHT * 1.6 + DOWN * 0.9, angle=TAU / 8)
        w3 = ArcBetweenPoints(band_shift(7) + RIGHT * 1.6 + DOWN * 0.9,
                              band_shift(7) + RIGHT * 4.4 + UP * 0.6, angle=-TAU / 8)
        self.play(Create(w1))
        self.play(Create(w2))
        self.play(Create(w3))
        self.wait(1.5)
        p1 = Tex("recovery").scale(0.75).shift(band_shift(7) + LEFT * 3.6 + UP * 0.6)
        p2 = Tex("prosperity").scale(0.75).shift(band_shift(7) + LEFT * 1.4 + UP * 1.5)
        p3 = Tex("recession").scale(0.75).shift(band_shift(7) + RIGHT * 0.4 + DOWN * 0.9)
        p4 = Tex("depression").scale(0.75).shift(band_shift(7) + RIGHT * 1.8 + DOWN * 1.6)
        self.play(Write(p1), Write(p2))
        self.play(Write(p3), Write(p4))
        self.wait(2)
        b7a = Tex("Leading: headlights $\\cdot$ coincident: speedometer").scale(0.9).shift(band_shift(7) + DOWN * 2.5)
        b7b = Tex("lagging: rearview mirror").scale(0.9).shift(band_shift(7) + DOWN * 3.2)
        self.play(Write(b7a))
        self.play(Write(b7b))
        self.wait(3)

        # ===================== Part 2 — Simplifier =====================
        # --- Band 8 (subtopic_5): one wallet, three questions ---
        self.next_band(8)
        b8t = Tex("One wallet, three questions").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("R350 in the wallet; R580 on the fridge list").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8b = Tex("— the gap is permanent, and it has a name").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8a))
        self.play(Write(b8b))
        self.wait(2.5)
        b8c = Tex("True cost of the boots: the data and taxi fare").scale(0.95).shift(band_shift(8) + DOWN * 0.5)
        b8c2 = Tex("— the best thing walked away from").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8c))
        self.play(Write(b8c2))
        self.wait(2.5)
        b8d = Tex("Sewing room: all machines on = the curve;").scale(0.95).shift(band_shift(8) + DOWN * 2.0)
        b8d2 = Tex("idle machines = inside; more machines = growth").scale(0.95).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8d))
        self.play(Write(b8d2))
        self.wait(3)

        # --- Band 9 (subtopic_6): the circle of money on one street ---
        self.next_band(9)
        b9t = Tex("The circle of money on one street").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Fish shop pays wages; wages cross the counters;").scale(0.95).shift(band_shift(9) + UP * 1.1)
        b9a2 = Tex("takings pay wages again — a relay in a circle").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9a))
        self.play(Write(b9a2))
        self.wait(2.5)
        b9b = Tex("Leaks: bank savings, taxes, imported phones").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9b))
        self.wait(2)
        b9c = Tex("Refills: the second fryer, the repainted clinic,").scale(0.95).shift(band_shift(9) + DOWN * 1.2)
        b9c2 = Tex("rooibos sold abroad").scale(0.95).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9c))
        self.play(Write(b9c2))
        self.wait(2)
        b9d = Tex("Count finished things only — GDP by WHERE, GNI by WHO").scale(0.85).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9d))
        self.play(Create(SurroundingRectangle(b9d, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the vetkoek stand and the breathing economy ---
        self.next_band(10)
        b10t = Tex("The argument that sets the price").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("R15: full tray at ten o'clock — price drifts down").scale(0.95).shift(band_shift(10) + UP * 1.1)
        b10b = Tex("R3: empty before assembly — price drifts up").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10a))
        self.play(Write(b10b))
        self.wait(2.5)
        b10c = Tex("Near R7: last vetkoek meets last buyer — equilibrium").scale(0.9).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b10c))
        self.play(Create(SurroundingRectangle(b10c, color=GREEN)))
        self.wait(2)
        b10d = Tex("Own price: along the curve; oil price doubling:").scale(0.95).shift(band_shift(10) + DOWN * 1.5)
        b10d2 = Tex("the whole curve moves").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10d))
        self.play(Write(b10d2))
        self.wait(2)
        b10e = Tex("The economy breathes: four phases, three instruments").scale(0.9).shift(band_shift(10) + DOWN * 3.1)
        self.play(Write(b10e))
        self.play(Create(SurroundingRectangle(b10e, color=GREEN)))
        self.wait(4)
