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

# Band-layout whiteboard scene for "Demand, Supply and Equilibrium"
# (grade 10, term 2). One band per teaching beat; camera moves down, earlier
# work stays. All market diagrams are hand-built: axes = two Arrows, curves =
# chained Line segments, equilibria = Dot + DashedLine + Tex labels
# (exporter-safe primitives only; write-only reveals).
#
# Subtopic shares (subtopics.json, total 1470 s):
# 195/225/210/270/190/190/190 — subtopic_4 (the drought diagram) is the
# heavyweight and gets two bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


def chain(points, color, width=5):
    return VGroup(*[Line(points[i], points[i + 1], color=color,
                         stroke_width=width) for i in range(len(points) - 1)])


class DemandSupplyEquilibriumSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def axes(self, origin):
        x_axis = Arrow(origin, origin + RIGHT * 8.6, buff=0, stroke_width=4)
        y_axis = Arrow(origin, origin + UP * 4.6, buff=0, stroke_width=4)
        p_lab = Tex("P").scale(0.9).next_to(y_axis.get_end(), LEFT, buff=0.15)
        q_lab = Tex("Q").scale(0.9).next_to(x_axis.get_end(), DOWN, buff=0.15)
        return x_axis, y_axis, p_lab, q_lab

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the law of demand + demand curve ---
        title = Tex("Demand, Supply and Equilibrium").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d0a = Tex(r"Demand: willing AND able to buy").scale(1.05).shift(UP * 1.6)
        self.play(Write(d0a))
        self.wait(2)
        d0b = Tex(r"Price up $\Rightarrow$ quantity demanded down").scale(1.0).shift(UP * 0.8)
        self.play(Write(d0b))
        self.wait(2)
        o0 = LEFT * 4.6 + DOWN * 3.0
        xa, ya, pl, ql = self.axes(o0)
        self.play(Create(xa), Create(ya), Write(pl), Write(ql))
        d_pts = [o0 + RIGHT * 0.6 + UP * 3.6, o0 + RIGHT * 2.4 + UP * 2.4,
                 o0 + RIGHT * 4.4 + UP * 1.4, o0 + RIGHT * 6.6 + UP * 0.7]
        d_curve = chain(d_pts, BLUE)
        for seg in d_curve:
            self.play(Create(seg), run_time=0.6)
        d_lab = Tex("D", color=BLUE).scale(1.0).next_to(d_pts[-1], RIGHT, buff=0.15)
        self.play(Write(d_lab))
        self.wait(3)

        # --- Band 1 (subtopic_1): movement along vs shift ---
        self.next_band(1)
        b1t = Tex("Along the curve, or the whole curve?").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        b1w = Tex(r"``A maize price change shifts D''").scale(1.05).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1w))
        self.play(Create(strike(b1w)))
        self.wait(2)
        b1a = Tex(r"Own price: slide ALONG the same curve").scale(1.05).shift(band_shift(1) + UP * 0.2)
        b1b = Tex(r"(a change in quantity demanded)").scale(0.95).shift(band_shift(1) + DOWN * 0.5)
        self.play(Write(b1a))
        self.play(Write(b1b))
        self.wait(2.5)
        b1c = Tex(r"Income, substitutes, tastes, population:").scale(1.0).shift(band_shift(1) + DOWN * 1.3)
        b1d = Tex(r"the WHOLE curve shifts — right or left").scale(1.0).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1c))
        self.play(Write(b1d))
        self.wait(2)
        b1e = Tex(r"Own price moves you along; anything").scale(1.0).shift(band_shift(1) + DOWN * 2.8)
        b1f = Tex(r"else shifts it").scale(1.0).shift(band_shift(1) + DOWN * 3.4)
        self.play(Write(b1e))
        self.play(Write(b1f))
        self.play(Create(SurroundingRectangle(VGroup(b1e, b1f), color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the law of supply + supply curve ---
        self.next_band(2)
        b2t = Tex("The law of supply").scale(1.2).shift(band_shift(2) + UP * 2.8)
        self.play(Write(b2t))
        self.wait(1.5)
        b2a = Tex(r"Price up $\Rightarrow$ quantity supplied up —").scale(1.0).shift(band_shift(2) + UP * 2.0)
        b2b = Tex(r"price is the producer's reward").scale(1.0).shift(band_shift(2) + UP * 1.3)
        self.play(Write(b2a))
        self.play(Write(b2b))
        self.wait(2.5)
        o2 = band_shift(2) + LEFT * 4.6 + DOWN * 3.0
        xa2, ya2, pl2, ql2 = self.axes(o2)
        self.play(Create(xa2), Create(ya2), Write(pl2), Write(ql2))
        s_pts = [o2 + RIGHT * 0.6 + UP * 0.6, o2 + RIGHT * 2.4 + UP * 1.3,
                 o2 + RIGHT * 4.4 + UP * 2.4, o2 + RIGHT * 6.6 + UP * 3.8]
        s_curve = chain(s_pts, YELLOW)
        for seg in s_curve:
            self.play(Create(seg), run_time=0.6)
        s_lab = Tex("S", color=YELLOW).scale(1.0).next_to(s_pts[-1], RIGHT, buff=0.15)
        self.play(Write(s_lab))
        self.wait(2)
        b2c = Tex(r"Shifters: costs, technology, taxes,").scale(0.9).shift(band_shift(2) + RIGHT * 2.6 + UP * 0.2)
        b2d = Tex(r"producers, weather").scale(0.9).shift(band_shift(2) + RIGHT * 2.6 + DOWN * 0.5)
        self.play(Write(b2c))
        self.play(Write(b2d))
        self.wait(3)

        # --- Band 3 (subtopic_2): diagnosing the drought ---
        self.next_band(3)
        b3t = Tex("Diagnosing the drought").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        b3a = Tex(r"Q1: which side was hit? The farms —").scale(1.05).shift(band_shift(3) + UP * 1.2)
        b3b = Tex(r"SUPPLY").scale(1.1).shift(band_shift(3) + UP * 0.5)
        self.play(Write(b3a))
        self.play(Write(b3b))
        self.wait(2)
        b3c = Tex(r"Q2: did the own price cause it?").scale(1.05).shift(band_shift(3) + DOWN * 0.3)
        b3d = Tex(r"No — the weather did $\Rightarrow$ SHIFT").scale(1.05).shift(band_shift(3) + DOWN * 1.0)
        self.play(Write(b3c))
        self.play(Write(b3d))
        self.wait(2.5)
        b3e = Tex(r"Less offered at every price:").scale(1.05).shift(band_shift(3) + DOWN * 1.9)
        b3f = Tex(r"S shifts LEFT to S1; D stays put").scale(1.05).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3e))
        self.play(Write(b3f))
        self.play(Create(SurroundingRectangle(b3f, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): equilibrium on the diagram ---
        self.next_band(4)
        b4t = Tex("Equilibrium — where the market settles").scale(1.1).shift(band_shift(4) + UP * 2.8)
        self.play(Write(b4t))
        self.wait(1.5)
        o4 = band_shift(4) + LEFT * 4.6 + DOWN * 3.0
        xa4, ya4, pl4, ql4 = self.axes(o4)
        self.play(Create(xa4), Create(ya4), Write(pl4), Write(ql4))
        d4_pts = [o4 + RIGHT * 0.6 + UP * 3.7, o4 + RIGHT * 2.2 + UP * 2.7,
                  o4 + RIGHT * 3.9 + UP * 1.8, o4 + RIGHT * 5.8 + UP * 1.1,
                  o4 + RIGHT * 7.4 + UP * 0.7]
        s4_pts = [o4 + RIGHT * 0.6 + UP * 0.6, o4 + RIGHT * 2.2 + UP * 1.1,
                  o4 + RIGHT * 3.9 + UP * 1.8, o4 + RIGHT * 5.8 + UP * 2.8,
                  o4 + RIGHT * 7.4 + UP * 3.8]
        d4 = chain(d4_pts, BLUE)
        s4 = chain(s4_pts, YELLOW)
        self.play(Create(d4), run_time=1.5)
        self.play(Create(s4), run_time=1.5)
        d4_lab = Tex("D", color=BLUE).scale(0.95).next_to(d4_pts[-1], RIGHT, buff=0.12)
        s4_lab = Tex("S", color=YELLOW).scale(0.95).next_to(s4_pts[-1], RIGHT, buff=0.12)
        self.play(Write(d4_lab), Write(s4_lab))
        self.wait(1.5)
        e4 = o4 + RIGHT * 3.9 + UP * 1.8
        e4_dot = Dot(e4, color=GREEN)
        dash_p = DashedLine(e4, o4 + UP * 1.8, color=GREEN, stroke_width=3)
        dash_q = DashedLine(e4, o4 + RIGHT * 3.9, color=GREEN, stroke_width=3)
        self.play(Create(e4_dot))
        self.play(Create(dash_p), Create(dash_q))
        p_e = Tex("P").scale(0.85).next_to(o4 + UP * 1.8, LEFT, buff=0.15)
        q_e = Tex("Q").scale(0.85).next_to(o4 + RIGHT * 3.9, DOWN, buff=0.15)
        self.play(Write(p_e), Write(q_e))
        self.wait(2)
        b4a = Tex(r"buyers' plans $=$ sellers' plans:").scale(0.9).shift(band_shift(4) + RIGHT * 3.0 + UP * 1.4)
        b4b = Tex(r"the market clears").scale(0.9).shift(band_shift(4) + RIGHT * 3.0 + UP * 0.7)
        self.play(Write(b4a))
        self.play(Write(b4b))
        self.wait(3)

        # --- Band 5 (subtopic_3): surplus above, shortage below ---
        self.next_band(5)
        b5t = Tex("Why settle there and nowhere else?").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        b5a = Tex(r"Price ABOVE: supplied $>$ demanded —").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5b = Tex(r"SURPLUS: stock piles up, price falls").scale(1.0).shift(band_shift(5) + UP * 0.5)
        self.play(Write(b5a))
        self.play(Write(b5b))
        self.wait(2.5)
        b5c = Tex(r"Price BELOW: demanded $>$ supplied —").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        b5d = Tex(r"SHORTAGE: queues form, price rises").scale(1.0).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5c))
        self.play(Write(b5d))
        self.wait(2.5)
        b5e = Tex(r"Equilibrium: the only resting place —").scale(1.0).shift(band_shift(5) + DOWN * 2.0)
        b5f = Tex(r"a marble at the bottom of a bowl").scale(1.0).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5e))
        self.play(Write(b5f))
        self.play(Create(SurroundingRectangle(VGroup(b5e, b5f), color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the drought diagram, full construction ---
        self.next_band(6)
        b6t = Tex("The drought diagram").scale(1.15).shift(band_shift(6) + UP * 2.8)
        self.play(Write(b6t))
        self.wait(1.5)
        o6 = band_shift(6) + LEFT * 4.6 + DOWN * 3.0
        xa6, ya6, pl6, ql6 = self.axes(o6)
        self.play(Create(xa6), Create(ya6), Write(pl6), Write(ql6))
        d6_pts = [o6 + RIGHT * 0.6 + UP * 3.7, o6 + RIGHT * 2.2 + UP * 2.7,
                  o6 + RIGHT * 3.9 + UP * 1.8, o6 + RIGHT * 5.8 + UP * 1.1,
                  o6 + RIGHT * 7.4 + UP * 0.7]
        s6_pts = [o6 + RIGHT * 0.6 + UP * 0.6, o6 + RIGHT * 2.2 + UP * 1.1,
                  o6 + RIGHT * 3.9 + UP * 1.8, o6 + RIGHT * 5.8 + UP * 2.8,
                  o6 + RIGHT * 7.4 + UP * 3.8]
        d6 = chain(d6_pts, BLUE)
        s6 = chain(s6_pts, YELLOW)
        self.play(Create(d6), run_time=1.2)
        self.play(Create(s6), run_time=1.2)
        d6_lab = Tex("D", color=BLUE).scale(0.95).next_to(d6_pts[-1], RIGHT, buff=0.12)
        s6_lab = Tex("S", color=YELLOW).scale(0.95).next_to(s6_pts[-1], RIGHT, buff=0.12)
        self.play(Write(d6_lab), Write(s6_lab))
        e6 = o6 + RIGHT * 3.9 + UP * 1.8
        e6_dot = Dot(e6, color=GREEN)
        self.play(Create(e6_dot))
        self.wait(1.5)
        # The shock: S shifts left to S1.
        s1_pts = [o6 + RIGHT * 0.4 + UP * 1.6, o6 + RIGHT * 2.2 + UP * 2.7,
                  o6 + RIGHT * 3.9 + UP * 3.9]
        s1 = chain(s1_pts, RED)
        self.play(Create(s1), run_time=1.2)
        s1_lab = Tex("S1", color=RED).scale(0.95).next_to(s1_pts[-1], UP, buff=0.12)
        self.play(Write(s1_lab))
        shift_arrow = Arrow(o6 + RIGHT * 5.0 + UP * 3.0, o6 + RIGHT * 3.4 + UP * 3.4,
                            buff=0, color=RED, stroke_width=4)
        self.play(Create(shift_arrow))
        self.wait(1.5)
        e1 = o6 + RIGHT * 2.2 + UP * 2.7
        e1_dot = Dot(e1, color=RED)
        dash_p1 = DashedLine(e1, o6 + UP * 2.7, color=RED, stroke_width=3)
        dash_q1 = DashedLine(e1, o6 + RIGHT * 2.2, color=RED, stroke_width=3)
        self.play(Create(e1_dot))
        self.play(Create(dash_p1), Create(dash_q1))
        p1_lab = Tex("P1").scale(0.8).next_to(o6 + UP * 2.7, LEFT, buff=0.12)
        q1_lab = Tex("Q1").scale(0.8).next_to(o6 + RIGHT * 2.2, DOWN, buff=0.12)
        self.play(Write(p1_lab), Write(q1_lab))
        self.wait(2)
        b6a = Tex(r"P1 higher, Q1 smaller").scale(0.95).shift(band_shift(6) + RIGHT * 3.2 + UP * 1.0)
        self.play(Write(b6a))
        self.play(Create(SurroundingRectangle(b6a, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the story in words ---
        self.next_band(7)
        b7t = Tex("The diagram's story, in words").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(1.5)
        b7a = Tex(r"Old price: halved harvest leaves a").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7b = Tex(r"SHORTAGE — buyers bid the price up").scale(1.0).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7a))
        self.play(Write(b7b))
        self.wait(2.5)
        b7c = Tex(r"As it rises: buyers cut back (along D),").scale(1.0).shift(band_shift(7) + DOWN * 0.4)
        b7d = Tex(r"farmers stretch (along S1)").scale(1.0).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7c))
        self.play(Write(b7d))
        self.wait(2.5)
        b7e = Tex(r"Income unchanged $\Rightarrow$ D never moved —").scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        b7f = Tex(r"say so: reasoning earns marks").scale(1.0).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7e))
        self.play(Write(b7f))
        self.play(Create(SurroundingRectangle(b7f, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the cooler box of cold drinks ---
        self.next_band(8)
        b8t = Tex("The cooler box of cold drinks").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex(r"R20: a few buy. R15: more hands.").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8b = Tex(r"R10: half the queue — that's demand").scale(1.0).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8a))
        self.play(Write(b8b))
        self.wait(2.5)
        b8c = Tex(r"Empty pockets want too — the market").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        b8d = Tex(r"can't hear them: willing AND able").scale(1.0).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(b8c))
        self.play(Write(b8d))
        self.play(Create(SurroundingRectangle(b8d, color=GREEN)))
        self.wait(2.5)
        b8e = Tex(r"Seller: R10, one cooler; R20, phone the").scale(1.0).shift(band_shift(8) + DOWN * 2.0)
        b8f = Tex(r"cousin — price is the reward").scale(1.0).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8e))
        self.play(Write(b8f))
        self.wait(3)

        # --- Band 9 (subtopic_6): where the argument ends ---
        self.next_band(9)
        b9t = Tex("Where the argument ends").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex(r"R20: cans swim in melted ice —").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9b = Tex(r"the pile pushes the price DOWN").scale(1.0).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9a))
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = Tex(r"R8: cooler empty, queue waiting —").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        b9d = Tex(r"the queue pulls the price UP").scale(1.0).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9c))
        self.play(Write(b9d))
        self.wait(2.5)
        b9e = Tex(r"Between pile and queue: the last can to").scale(1.0).shift(band_shift(9) + DOWN * 2.0)
        b9f = Tex(r"the last buyer — and NOBODY set it").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9e))
        self.play(Write(b9f))
        self.play(Create(SurroundingRectangle(b9f, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the drought at the rank ---
        self.next_band(10)
        b10t = Tex("The drought at the rank").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex(r"Whose side got hit? The farms.").scale(1.05).shift(band_shift(10) + UP * 1.2)
        b10b = Tex(r"Did the own price do it? No — the sky.").scale(1.05).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10a))
        self.wait(2)
        self.play(Write(b10b))
        self.play(Create(SurroundingRectangle(VGroup(b10a, b10b), color=GREEN)))
        self.wait(2.5)
        b10c = Tex(r"Bags run out, buyers bid, families").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        b10d = Tex(r"switch to bread, farmers scrape hectares").scale(1.0).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10c))
        self.play(Write(b10d))
        self.wait(2.5)
        b10e = Tex(r"New resting place: higher price,").scale(1.0).shift(band_shift(10) + DOWN * 2.2)
        b10f = Tex(r"less maize traded").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10e))
        self.play(Write(b10f))
        self.wait(4)
