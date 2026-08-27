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

# Band-layout whiteboard scene for "The Production Possibility Curve"
# (grade 10, term 2). One band per teaching beat; camera moves down, earlier
# work stays. The PPC is hand-built: axes = two Arrows, the curve = a chain
# of Line segments through the schedule's points, zones marked with Dots —
# exporter-safe primitives only, write-only reveals.
#
# Subtopic shares (subtopics.json, total 1460 s):
# 220/230/220/220/190/190/190.
#
# PPC scale: maize (x) 0.09 units per tonne, vegetables (y) 0.07 per tonne.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


SCHEDULE = [(0, 50), (10, 45), (20, 38), (30, 28), (40, 15), (50, 0)]


def ppc_points(origin):
    return [origin + RIGHT * (0.09 * m) + UP * (0.07 * v) for m, v in SCHEDULE]


def ppc_chain(origin, color=BLUE):
    pts = ppc_points(origin)
    return VGroup(*[Line(pts[i], pts[i + 1], color=color, stroke_width=5)
                    for i in range(len(pts) - 1)])


class ProductionPossibilityCurveSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def ppc_axes(self, origin):
        x_axis = Arrow(origin, origin + RIGHT * 6.4, buff=0, stroke_width=4)
        y_axis = Arrow(origin, origin + UP * 4.6, buff=0, stroke_width=4)
        xl = Tex("Maize (t)").scale(0.75).next_to(x_axis.get_end(), DOWN, buff=0.15)
        yl = Tex("Vegetables (t)").scale(0.75).next_to(y_axis.get_end(), RIGHT, buff=0.15)
        return x_axis, y_axis, xl, yl

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the assumptions ---
        title = Tex("The Production Possibility Curve").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d0 = Tex(r"Scarcity, choice and cost — drawn").scale(1.05).shift(UP * 1.3)
        self.play(Write(d0))
        self.wait(2)
        a1 = Tex(r"1. Only TWO goods produced").scale(1.0).shift(UP * 0.4)
        a2 = Tex(r"2. Resources fixed in quantity, quality").scale(1.0).shift(DOWN * 0.3)
        a3 = Tex(r"3. Technology fixed").scale(1.0).shift(DOWN * 1.0)
        a4 = Tex(r"4. All resources fully employed").scale(1.0).shift(DOWN * 1.7)
        self.play(Write(a1))
        self.play(Write(a2))
        self.play(Write(a3))
        self.play(Write(a4))
        box0 = SurroundingRectangle(VGroup(a1, a2, a3, a4), color=GREEN)
        self.play(Create(box0))
        self.wait(2)
        d1 = Tex(r"State the assumptions — examiners ask").scale(0.95).shift(DOWN * 2.8)
        self.play(Write(d1))
        self.wait(3)

        # --- Band 1 (subtopic_1): plotting the schedule ---
        self.next_band(1)
        b1t = Tex("Maize against vegetables — the schedule").scale(1.05).shift(band_shift(1) + UP * 2.9)
        self.play(Write(b1t))
        self.wait(1.5)
        sched = Tex(r"A(0; 50) B(10; 45) C(20; 38)").scale(0.85).shift(band_shift(1) + UP * 2.2)
        sched2 = Tex(r"D(30; 28) E(40; 15) F(50; 0)").scale(0.85).shift(band_shift(1) + UP * 1.6)
        self.play(Write(sched))
        self.play(Write(sched2))
        self.wait(2)
        o1 = band_shift(1) + LEFT * 3.2 + DOWN * 3.1
        xa, ya, xl, yl = self.ppc_axes(o1)
        self.play(Create(xa), Create(ya), Write(xl), Write(yl))
        pts = ppc_points(o1)
        labels = ["A", "B", "C", "D", "E", "F"]
        for p, lab in zip(pts, labels):
            self.play(Create(Dot(p, color=BLUE)),
                      Write(Tex(lab).scale(0.65).next_to(p, UR, buff=0.08)),
                      run_time=0.5)
        curve = ppc_chain(o1)
        self.play(Create(curve), run_time=1.5)
        clab = Tex("PPC", color=BLUE).scale(0.85).move_to(o1 + RIGHT * 4.6 + UP * 1.8)
        self.play(Write(clab))
        self.wait(2)
        b1a = Tex(r"Every point ON it is a maximum;").scale(0.85).shift(band_shift(1) + RIGHT * 3.4 + UP * 0.4)
        b1b = Tex(r"nothing beyond is reachable").scale(0.85).shift(band_shift(1) + RIGHT * 3.4 + DOWN * 0.3)
        self.play(Write(b1a))
        self.play(Write(b1b))
        self.wait(3)

        # --- Band 2 (subtopic_2): on, inside, beyond ---
        self.next_band(2)
        b2t = Tex("Three zones, three meanings").scale(1.15).shift(band_shift(2) + UP * 2.9)
        self.play(Write(b2t))
        self.wait(1.5)
        o2 = band_shift(2) + LEFT * 3.2 + DOWN * 3.1
        xa2, ya2, xl2, yl2 = self.ppc_axes(o2)
        self.play(Create(xa2), Create(ya2), Write(xl2), Write(yl2))
        curve2 = ppc_chain(o2)
        self.play(Create(curve2), run_time=1.2)
        on_dot = Dot(o2 + RIGHT * (0.09 * 20) + UP * (0.07 * 38), color=GREEN)
        on_lab = Tex("on: efficient", color=GREEN).scale(0.8).next_to(on_dot, UR, buff=0.1)
        self.play(Create(on_dot), Write(on_lab))
        self.wait(2)
        in_dot = Dot(o2 + RIGHT * (0.09 * 20) + UP * (0.07 * 28), color=YELLOW)
        in_lab = Tex("inside: idle resources", color=YELLOW).scale(0.8).next_to(in_dot, DR, buff=0.1)
        self.play(Create(in_dot), Write(in_lab))
        self.wait(2)
        out_dot = Dot(o2 + RIGHT * (0.09 * 40) + UP * (0.07 * 40), color=RED)
        out_lab = Tex("beyond: unattainable", color=RED).scale(0.8).next_to(out_dot, UR, buff=0.1)
        self.play(Create(out_dot), Write(out_lab))
        self.wait(2)
        b2a = Tex(r"Inside is where recessions and").scale(0.85).shift(band_shift(2) + RIGHT * 3.6 + UP * 1.6)
        b2b = Tex(r"unemployment live").scale(0.85).shift(band_shift(2) + RIGHT * 3.6 + UP * 0.9)
        self.play(Write(b2a))
        self.play(Write(b2b))
        self.wait(3)

        # --- Band 3 (subtopic_2): increasing opportunity cost ---
        self.next_band(3)
        b3t = Tex("Why the curve bows outward").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        b3a = Tex(r"Each 10 maize costs, in vegetables:").scale(1.0).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3a))
        b3b = MathTex(r"5, \; 7, \; 10, \; 13, \; 15").scale(1.15).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3b))
        self.wait(2)
        b3c = Tex(r"INCREASING opportunity cost —").scale(1.0).shift(band_shift(3) + DOWN * 0.6)
        b3d = Tex(r"resources are not equally suited").scale(1.0).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3c))
        self.play(Write(b3d))
        self.play(Create(SurroundingRectangle(VGroup(b3c, b3d), color=GREEN)))
        self.wait(2.5)
        b3e = Tex(r"First fields switched suit maize best;").scale(0.95).shift(band_shift(3) + DOWN * 2.2)
        b3f = Tex(r"push further, each tonne costs more").scale(0.95).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3e))
        self.play(Write(b3f))
        self.wait(3)

        # --- Band 4 (subtopic_3): what moves the curve ---
        self.next_band(4)
        b4t = Tex("What moves the curve").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        b4a = Tex(r"INTERNAL: more resources, better").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4b = Tex(r"quality (education), technology,").scale(1.0).shift(band_shift(4) + UP * 0.5)
        b4c = Tex(r"efficiency reforms").scale(1.0).shift(band_shift(4) + DOWN * 0.2)
        self.play(Write(b4a))
        self.play(Write(b4b))
        self.play(Write(b4c))
        self.wait(2.5)
        b4d = Tex(r"EXTERNAL: weather, world markets,").scale(1.0).shift(band_shift(4) + DOWN * 1.1)
        b4e = Tex(r"shocks that destroy resources").scale(1.0).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4d))
        self.play(Write(b4e))
        self.wait(2)
        b4f = Tex(r"Outward shift IS economic growth;").scale(1.0).shift(band_shift(4) + DOWN * 2.7)
        b4g = Tex(r"destruction drags the curve inward").scale(1.0).shift(band_shift(4) + DOWN * 3.4)
        self.play(Write(b4f))
        self.play(Write(b4g))
        self.play(Create(SurroundingRectangle(b4f, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): along vs toward vs shift ---
        self.next_band(5)
        b5t = Tex("Three movements — keep them apart").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        b5w = Tex(r"``Unemployment falling $=$ growth''").scale(1.05).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5w))
        self.play(Create(strike(b5w)))
        self.wait(2)
        b5a = Tex(r"ALONG the curve: reallocation —").scale(1.0).shift(band_shift(5) + UP * 0.2)
        b5b = Tex(r"more maize, fewer vegetables").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(b5a))
        self.play(Write(b5b))
        self.wait(2)
        b5c = Tex(r"Inside TOWARD the curve: recovery").scale(1.0).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5c))
        self.wait(2)
        b5d = Tex(r"The curve ADVANCING: growth").scale(1.0).shift(band_shift(5) + DOWN * 2.3)
        self.play(Write(b5d))
        self.play(Create(SurroundingRectangle(b5d, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): consequences of inefficiency ---
        self.next_band(6)
        b6t = Tex("The cost of the inside point").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        b6a = Tex(r"The gap to the curve $=$ output that").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6b = Tex(r"could exist and does not").scale(1.0).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6a))
        self.play(Write(b6b))
        self.wait(2)
        b6c = Tex(r"Lost output $\rightarrow$ lost incomes $\rightarrow$ lost").scale(1.0).shift(band_shift(6) + DOWN * 0.4)
        b6d = Tex(r"spending $\rightarrow$ lost tax revenue").scale(1.0).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6c))
        self.play(Write(b6d))
        self.wait(2.5)
        b6e = Tex(r"Idleness erodes: skills decay, machines").scale(0.95).shift(band_shift(6) + DOWN * 2.0)
        b6f = Tex(r"rust — tomorrow's curve pulled inward").scale(0.95).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6e))
        self.play(Write(b6f))
        self.wait(2)
        b6g = Tex(r"Two tasks: get TO the curve, then MOVE it").scale(0.95).shift(band_shift(6) + DOWN * 3.4)
        self.play(Write(b6g))
        self.play(Create(SurroundingRectangle(b6g, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): one oven, two breads ---
        self.next_band(7)
        b7t = Tex("One oven, two breads").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex(r"The day's menu: 50W+0B, 45W+10B,").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7b = Tex(r"38W+20B, 28W+30B, 15W+40B, 0W+50B").scale(1.0).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7a))
        self.play(Write(b7b))
        self.wait(2.5)
        b7c = Tex(r"Every extra brown is PAID FOR in").scale(1.0).shift(band_shift(7) + DOWN * 0.4)
        b7d = Tex(r"whites — the oven's day is fixed").scale(1.0).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7c))
        self.play(Write(b7d))
        self.play(Create(SurroundingRectangle(b7d, color=GREEN)))
        self.wait(2.5)
        b7e = Tex(r"Join the dots: the edge of the possible").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        b7f = Tex(r"day — a country's PPC is the same idea").scale(0.95).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7e))
        self.play(Write(b7f))
        self.wait(3)

        # --- Band 8 (subtopic_6): lazy days and dream days ---
        self.next_band(8)
        b8t = Tex("Lazy days and dream days").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex(r"FULL day: everything humming — ON").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8b = Tex(r"the line, a maximum in your chosen mix").scale(1.0).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8a))
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex(r"LAZY day: baker off, oven idle —").scale(1.0).shift(band_shift(8) + DOWN * 0.3)
        b8d = Tex(r"INSIDE the line, waste's address").scale(1.0).shift(band_shift(8) + DOWN * 1.0)
        self.play(Write(b8c))
        self.play(Write(b8d))
        self.wait(2)
        b8e = Tex(r"DREAM day: 50W AND 40B — BEYOND,").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        b8f = Tex(r"tomorrow's target, not today's option").scale(1.0).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8e))
        self.play(Write(b8f))
        self.wait(2)
        b8g = Tex(r"First browns cost 5 whites; the last 15 —").scale(0.9).shift(band_shift(8) + DOWN * 3.2)
        self.play(Write(b8g))
        self.wait(3)

        # --- Band 9 (subtopic_7): growing the oven ---
        self.next_band(9)
        b9t = Tex("Growing the oven").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex(r"Second oven bought: every mix improves —").scale(0.95).shift(band_shift(9) + UP * 1.2)
        b9b = Tex(r"the boundary steps OUTWARD: growth").scale(0.95).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9a))
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = Tex(r"New mix: walk ALONG. Fix a lazy day:").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        b9d = Tex(r"walk back TO. Line advances: GROWTH.").scale(0.95).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9c))
        self.play(Write(b9d))
        self.play(Create(SurroundingRectangle(VGroup(b9c, b9d), color=GREEN)))
        self.wait(2.5)
        b9e = Tex(r"SA's unemployment: millions of hands").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        b9f = Tex(r"inside the line — the cheapest growth").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        b9g = Tex(r"is walking back to the boundary").scale(0.95).shift(band_shift(9) + DOWN * 3.4)
        self.play(Write(b9e))
        self.play(Write(b9f))
        self.play(Write(b9g))
        self.wait(4)
