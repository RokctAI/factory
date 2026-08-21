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

# Band-layout whiteboard scene for "The Production Possibility Curve"
# (grade 10, term 2 — IEB catalogue). One band per teaching beat; camera moves
# down, earlier work stays. The PPC is hand-built: axes = two Arrows, the
# boundary = chained Line segments through the wheat/wool schedule, zone
# points = Dots (exporter-safe primitives only; write-only reveals).
#
# Subtopic shares (subtopics.json, total 1460 s):
# 220/230/220/220/190/190/190 — subtopics 1-3 each split across two bands
# where the argument divides naturally.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def chain(points, color, width=5):
    return VGroup(*[Line(points[i], points[i + 1], color=color,
                         stroke_width=width) for i in range(len(points) - 1)])


# Wheat/wool schedule mapped to band-local offsets:
# wheat 0-50 -> x 0-7.5 (0.15 per tonne); wool 0-40 -> y 0-4.2 (0.105 per bale).
PPC_OFFSETS = [(0.0, 4.2), (1.5, 4.0), (3.0, 3.6), (4.5, 2.8),
               (6.0, 1.7), (7.5, 0.0)]


class ProductionPossibilityCurveSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def axes(self, origin):
        x_axis = Arrow(origin, origin + RIGHT * 8.4, buff=0, stroke_width=4)
        y_axis = Arrow(origin, origin + UP * 4.8, buff=0, stroke_width=4)
        y_lab = Tex("Wool (bales)").scale(0.6).next_to(y_axis.get_end(), UP, buff=0.12)
        x_lab = Tex("Wheat (tonnes)").scale(0.6).next_to(x_axis.get_end(), DOWN, buff=0.12)
        return x_axis, y_axis, y_lab, x_lab

    def ppc_pts(self, origin):
        return [origin + RIGHT * dx + UP * dy for dx, dy in PPC_OFFSETS]

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the assumptions ---
        title = Tex("The Production Possibility Curve").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        assumptions = [
            r"1. Two goods only",
            r"2. Resources fixed (quantity and quality)",
            r"3. Technology fixed",
            r"4. Full, efficient employment",
        ]
        for i, a in enumerate(assumptions):
            m = Tex(a).scale(0.95).shift(UP * (1.4 - i * 0.75))
            self.play(Write(m), run_time=0.8)
            self.wait(1)
        b0a = Tex(r"Under these, every division of effort").scale(0.95).shift(DOWN * 1.9)
        b0b = Tex(r"between the goods can be listed").scale(0.95).shift(DOWN * 2.6)
        self.play(Write(b0a))
        self.play(Write(b0b))
        self.wait(3)

        # --- Band 1 (subtopic_1): plotting the schedule ---
        self.next_band(1)
        b1t = Tex("Wheat and wool: the schedule drawn").scale(1.05).shift(band_shift(1) + UP * 3.2)
        self.play(Write(b1t))
        self.wait(1.5)
        o1 = band_shift(1) + LEFT * 4.4 + DOWN * 3.2
        xa1, ya1, yl1, xl1 = self.axes(o1)
        self.play(Create(xa1), Create(ya1), Write(yl1), Write(xl1))
        pts1 = self.ppc_pts(o1)
        labels = ["A", "B", "C", "D", "E", "F"]
        for p, lab in zip(pts1, labels):
            self.play(Create(Dot(p, color=BLUE)), run_time=0.4)
            self.play(Write(Tex(lab).scale(0.7).next_to(p, UR, buff=0.08)), run_time=0.3)
        curve1 = chain(pts1, BLUE)
        self.play(Create(curve1), run_time=2)
        self.wait(1.5)
        b1a = Tex(r"A boundary bowing outward —").scale(0.9).shift(band_shift(1) + RIGHT * 3.6 + UP * 1.6)
        b1b = Tex(r"scarcity, drawn").scale(0.9).shift(band_shift(1) + RIGHT * 3.6 + UP * 0.9)
        self.play(Write(b1a))
        self.play(Write(b1b))
        self.play(Create(SurroundingRectangle(b1b, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): on, inside, beyond ---
        self.next_band(2)
        b2t = Tex("Three zones, three verdicts").scale(1.1).shift(band_shift(2) + UP * 3.2)
        self.play(Write(b2t))
        self.wait(1.5)
        o2 = band_shift(2) + LEFT * 4.4 + DOWN * 3.2
        xa2, ya2, yl2, xl2 = self.axes(o2)
        self.play(Create(xa2), Create(ya2), Write(yl2), Write(xl2))
        curve2 = chain(self.ppc_pts(o2), BLUE)
        self.play(Create(curve2), run_time=1.5)
        on_dot = Dot(o2 + RIGHT * 3.0 + UP * 3.6, color=GREEN)
        self.play(Create(on_dot))
        on_lab = Tex(r"ON: efficient", color=GREEN).scale(0.75).next_to(on_dot, UR, buff=0.1)
        self.play(Write(on_lab))
        self.wait(1.5)
        in_dot = Dot(o2 + RIGHT * 2.2 + UP * 1.6, color=YELLOW)
        self.play(Create(in_dot))
        in_lab = Tex(r"INSIDE: idle resources", color=YELLOW).scale(0.75).next_to(in_dot, DOWN, buff=0.12)
        self.play(Write(in_lab))
        self.wait(1.5)
        out_dot = Dot(o2 + RIGHT * 6.4 + UP * 3.6, color=RED)
        self.play(Create(out_dot))
        out_lab = Tex(r"BEYOND: unattainable today", color=RED).scale(0.75).next_to(out_dot, UP, buff=0.12)
        self.play(Write(out_lab))
        self.wait(3)

        # --- Band 3 (subtopic_2): increasing opportunity cost ---
        self.next_band(3)
        b3t = Tex("The rising price of wheat, in wool").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        b3a = Tex(r"Each 10 tonnes of wheat costs:").scale(1.0).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3a))
        b3b = Tex(r"2, then 4, then 7, then 11, then 16 bales").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3b))
        self.wait(2.5)
        b3c = Tex(r"INCREASING opportunity cost —").scale(1.0).shift(band_shift(3) + DOWN * 0.5)
        b3d = Tex(r"the reason for the outward bow").scale(1.0).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(b3c))
        self.play(Write(b3d))
        self.wait(2.5)
        b3e = Tex(r"Best grain paddocks plough first; later").scale(0.95).shift(band_shift(3) + DOWN * 2.1)
        b3f = Tex(r"switches surrender brilliant wool land").scale(0.95).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3e))
        self.play(Write(b3f))
        self.play(Create(SurroundingRectangle(VGroup(b3e, b3f), color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): what moves the curve ---
        self.next_band(4)
        b4t = Tex("What moves the boundary").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        b4a = Tex(r"INTERNAL: more resources, better skills,").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4b = Tex(r"new technology, efficiency reforms").scale(0.95).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4a))
        self.play(Write(b4b))
        self.wait(2.5)
        b4c = Tex(r"EXTERNAL: rains and drought, world").scale(0.95).shift(band_shift(4) + DOWN * 0.4)
        b4d = Tex(r"markets, imported capital, shocks").scale(0.95).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4c))
        self.play(Write(b4d))
        self.wait(2.5)
        b4e = Tex(r"Improvement $\Rightarrow$ OUTWARD (growth);").scale(0.95).shift(band_shift(4) + DOWN * 2.0)
        b4f = Tex(r"destruction $\Rightarrow$ INWARD (capacity lost)").scale(0.95).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4e))
        self.play(Write(b4f))
        self.play(Create(SurroundingRectangle(VGroup(b4e, b4f), color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): along vs toward vs shift ---
        self.next_band(5)
        b5t = Tex("Three moves that look alike").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        b5a = Tex(r"ALONG the curve: reallocation —").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5b = Tex(r"more wheat, less wool, same capacity").scale(1.0).shift(band_shift(5) + UP * 0.5)
        self.play(Write(b5a))
        self.play(Write(b5b))
        self.wait(2)
        b5c = Tex(r"Inside TOWARD the curve: recovery —").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        b5d = Tex(r"idle hands returning to work").scale(1.0).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5c))
        self.play(Write(b5d))
        self.wait(2)
        b5e = Tex(r"The curve ADVANCING: growth —").scale(1.0).shift(band_shift(5) + DOWN * 2.0)
        b5f = Tex(r"and only that is growth").scale(1.0).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5e))
        self.play(Write(b5f))
        self.play(Create(SurroundingRectangle(b5f, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): consequences of inefficiency ---
        self.next_band(6)
        b6t = Tex("The cost of the inside point").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6t))
        self.wait(1.5)
        chain_items = [
            r"Gap to the curve $=$ output lost",
            r"$\Rightarrow$ incomes never earned",
            r"$\Rightarrow$ spending shrinks (circular flow)",
            r"$\Rightarrow$ tax revenue lost",
            r"$\Rightarrow$ skills fade, machines rust",
        ]
        for i, c in enumerate(chain_items):
            m = Tex(c).scale(0.9).shift(band_shift(6) + UP * (1.4 - i * 0.7))
            self.play(Write(m), run_time=0.8)
            self.wait(0.8)
        b6a = Tex(r"First reach the curve; then move it").scale(0.95).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6a))
        self.play(Create(SurroundingRectangle(b6a, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): one workshop, two uniforms ---
        self.next_band(7)
        b7t = Tex("One workshop, two uniforms").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex(r"One day: 60 shirts, or 60 jerseys,").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7b = Tex(r"or a mix from the menu").scale(1.0).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7a))
        self.play(Write(b7b))
        self.wait(2.5)
        b7c = Tex(r"Iron rule: every dozen jerseys is").scale(1.0).shift(band_shift(7) + DOWN * 0.4)
        b7d = Tex(r"PAID FOR in shirts").scale(1.0).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7c))
        self.play(Write(b7d))
        self.play(Create(SurroundingRectangle(b7d, color=GREEN)))
        self.wait(2.5)
        b7e = Tex(r"Dots joined $=$ the edge of the possible").scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        b7f = Tex(r"day — a country is a bigger room").scale(1.0).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7e))
        self.play(Write(b7f))
        self.wait(3)

        # --- Band 8 (subtopic_6): lazy days and dream days ---
        self.next_band(8)
        b8t = Tex("Lazy days and dream days").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex(r"FULL day: machines humming — ON the line").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8a))
        self.wait(2)
        b8b = Tex(r"LAZY day: sick machinist, jammed machine —").scale(0.95).shift(band_shift(8) + UP * 0.4)
        b8c = Tex(r"INSIDE the line: waste's address").scale(0.95).shift(band_shift(8) + DOWN * 0.3)
        self.play(Write(b8b))
        self.play(Write(b8c))
        self.wait(2.5)
        b8d = Tex(r"DREAM day: 60 AND 48 — BEYOND the line,").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        b8e = Tex(r"tomorrow's target").scale(0.95).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8d))
        self.play(Write(b8e))
        self.wait(2.5)
        b8f = Tex(r"Jerseys grow dearer: 6 shirts, then 18 —").scale(0.95).shift(band_shift(8) + DOWN * 2.8)
        b8g = Tex(r"hands are not all-purpose: the bow").scale(0.95).shift(band_shift(8) + DOWN * 3.5)
        self.play(Write(b8f))
        self.play(Write(b8g))
        self.play(Create(SurroundingRectangle(b8g, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): buying the second machine ---
        self.next_band(9)
        b9t = Tex("Buying the second machine").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex(r"New machines + training: every mix").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9b = Tex(r"improves — the boundary steps OUT").scale(1.0).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9a))
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = Tex(r"Mix change: along. Lazy day fixed:").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        b9d = Tex(r"back TO the line. Growth: the line moves").scale(1.0).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9c))
        self.play(Write(b9d))
        self.play(Create(SurroundingRectangle(VGroup(b9c, b9d), color=GREEN)))
        self.wait(2.5)
        b9e = Tex(r"Millions of hands inside the line:").scale(1.0).shift(band_shift(9) + DOWN * 2.0)
        b9f = Tex(r"cheapest growth is walking back first").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9e))
        self.play(Write(b9f))
        self.wait(4)
