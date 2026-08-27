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

# Band-layout whiteboard scene for "Taxes, Subsidies and Price Controls"
# (grade 10, term 2 — IEB catalogue). One band per teaching beat; camera moves
# down, earlier work stays. Market diagrams are hand-built: axes = two Arrows,
# curves = chained Line segments, ceilings/floors = horizontal Lines,
# gaps = thick Lines between curve intersections (exporter-safe primitives
# only; write-only reveals).
#
# Subtopic shares (subtopics.json, total 1450 s):
# 220/220/210/230/190/190/190 — subtopics 2-4 each split across two bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def chain(points, color, width=5):
    return VGroup(*[Line(points[i], points[i + 1], color=color,
                         stroke_width=width) for i in range(len(points) - 1)])


class TaxesSubsidiesPriceControlsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def axes(self, origin):
        x_axis = Arrow(origin, origin + RIGHT * 8.2, buff=0, stroke_width=4)
        y_axis = Arrow(origin, origin + UP * 4.6, buff=0, stroke_width=4)
        p_lab = Tex("P").scale(0.9).next_to(y_axis.get_end(), LEFT, buff=0.15)
        q_lab = Tex("Q").scale(0.9).next_to(x_axis.get_end(), DOWN, buff=0.15)
        return x_axis, y_axis, p_lab, q_lab

    def market(self, origin):
        d_pts = [origin + RIGHT * 0.6 + UP * 3.7, origin + RIGHT * 2.2 + UP * 2.7,
                 origin + RIGHT * 3.9 + UP * 1.8, origin + RIGHT * 5.8 + UP * 1.1,
                 origin + RIGHT * 7.2 + UP * 0.7]
        s_pts = [origin + RIGHT * 0.6 + UP * 0.6, origin + RIGHT * 2.2 + UP * 1.1,
                 origin + RIGHT * 3.9 + UP * 1.8, origin + RIGHT * 5.8 + UP * 2.8,
                 origin + RIGHT * 7.2 + UP * 3.7]
        return chain(d_pts, BLUE), chain(s_pts, YELLOW), d_pts, s_pts

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): why the state steps in, and with what ---
        title = Tex("Taxes, Subsidies and Price Controls").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0a = Tex(r"Markets misfire: smoke uncharged, harmful").scale(0.9).shift(UP * 1.6)
        b0b = Tex(r"goods overused, needs without income").scale(0.9).shift(UP * 0.9)
        self.play(Write(b0a))
        self.play(Write(b0b))
        self.wait(2.5)
        fams = [
            r"1. Indirect taxes: VAT, excise, levies",
            r"2. Subsidies: transport, farming, water",
            r"3. Welfare: grants, clinics, no-fee schools",
            r"4. Price controls: ceilings, floors, wages",
        ]
        for i, f in enumerate(fams):
            m = Tex(f).scale(0.85).shift(DOWN * (0.1 + i * 0.7))
            self.play(Write(m), run_time=0.8)
            self.wait(0.8)
        b0c = Tex(r"Each overrules the market on purpose").scale(0.9).shift(DOWN * 3.2)
        self.play(Write(b0c))
        self.play(Create(SurroundingRectangle(b0c, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_2): the tax on the diagram ---
        self.next_band(1)
        b1t = Tex("An indirect tax, drawn").scale(1.1).shift(band_shift(1) + UP * 3.2)
        self.play(Write(b1t))
        self.wait(1.5)
        o1 = band_shift(1) + LEFT * 4.2 + DOWN * 3.2
        xa1, ya1, pl1, ql1 = self.axes(o1)
        self.play(Create(xa1), Create(ya1), Write(pl1), Write(ql1))
        d1, s1, d1_pts, s1_pts = self.market(o1)
        self.play(Create(d1), run_time=1.2)
        self.play(Create(s1), run_time=1.2)
        e1_dot = Dot(o1 + RIGHT * 3.9 + UP * 1.8, color=GREEN)
        self.play(Create(e1_dot))
        self.wait(1.5)
        # Tax shifts S left/up.
        s1b_pts = [o1 + RIGHT * 0.4 + UP * 1.7, o1 + RIGHT * 2.2 + UP * 2.7,
                   o1 + RIGHT * 3.9 + UP * 3.9]
        s1b = chain(s1b_pts, RED)
        self.play(Create(s1b), run_time=1.2)
        s1b_lab = Tex("S1", color=RED).scale(0.9).next_to(s1b_pts[-1], UP, buff=0.12)
        self.play(Write(s1b_lab))
        e1b_dot = Dot(o1 + RIGHT * 2.2 + UP * 2.7, color=RED)
        self.play(Create(e1b_dot))
        dash_p1 = DashedLine(o1 + RIGHT * 2.2 + UP * 2.7, o1 + UP * 2.7,
                             color=RED, stroke_width=3)
        self.play(Create(dash_p1))
        self.wait(1.5)
        b1a = Tex(r"Price up (by less than the tax),").scale(0.85).shift(band_shift(1) + RIGHT * 3.4 + UP * 1.6)
        b1b = Tex(r"quantity down — burden shared").scale(0.85).shift(band_shift(1) + RIGHT * 3.4 + UP * 0.9)
        self.play(Write(b1a))
        self.play(Write(b1b))
        self.play(Create(SurroundingRectangle(b1b, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the subsidy mirror + discipline ---
        self.next_band(2)
        b2t = Tex("The subsidy: the exact mirror").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        b2a = Tex(r"State pays part of the cost per unit —").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2b = Tex(r"supply shifts RIGHT: price down, quantity up").scale(1.0).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2a))
        self.play(Write(b2b))
        self.wait(2.5)
        b2c = Tex(r"Honest costs: funded by taxes elsewhere;").scale(0.95).shift(band_shift(2) + DOWN * 0.4)
        b2d = Tex(r"margins can be pocketed; taxes breed smuggling").scale(0.95).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2c))
        self.play(Write(b2d))
        self.wait(2.5)
        b2e = Tex(r"Discipline: taxes and subsidies SHIFT S —").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        b2f = Tex(r"draw the shift, mark both equilibria").scale(0.95).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2e))
        self.play(Write(b2f))
        self.play(Create(SurroundingRectangle(VGroup(b2e, b2f), color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): the ceiling on the diagram ---
        self.next_band(3)
        b3t = Tex("The ceiling, drawn").scale(1.15).shift(band_shift(3) + UP * 3.2)
        self.play(Write(b3t))
        self.wait(1.5)
        o3 = band_shift(3) + LEFT * 4.2 + DOWN * 3.2
        xa3, ya3, pl3, ql3 = self.axes(o3)
        self.play(Create(xa3), Create(ya3), Write(pl3), Write(ql3))
        d3, s3, d3_pts, s3_pts = self.market(o3)
        self.play(Create(d3), run_time=1.2)
        self.play(Create(s3), run_time=1.2)
        e3_dot = Dot(o3 + RIGHT * 3.9 + UP * 1.8, color=GREEN)
        self.play(Create(e3_dot))
        self.wait(1)
        # Ceiling below equilibrium at height 1.1: S at x=2.2, D at x=5.8.
        ceil = Line(o3 + UP * 1.1, o3 + RIGHT * 7.4 + UP * 1.1,
                    color=RED, stroke_width=4)
        self.play(Create(ceil))
        c_lab = Tex("ceiling", color=RED).scale(0.75).next_to(o3 + UP * 1.1, LEFT, buff=0.12)
        self.play(Write(c_lab))
        self.wait(1.5)
        gap3 = Line(o3 + RIGHT * 2.2 + UP * 1.1, o3 + RIGHT * 5.8 + UP * 1.1,
                    color=ORANGE, stroke_width=8)
        self.play(Create(gap3))
        b3a = Tex(r"Demanded $\gg$ supplied: SHORTAGE —").scale(0.85).shift(band_shift(3) + RIGHT * 3.4 + UP * 1.8)
        b3b = Tex(r"and the clearing price is illegal").scale(0.85).shift(band_shift(3) + RIGHT * 3.4 + UP * 1.1)
        self.play(Write(b3a))
        self.play(Write(b3b))
        self.play(Create(SurroundingRectangle(b3b, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the honest verdict ---
        self.next_band(4)
        b4t = Tex("The ceiling's honest verdict").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        b4a = Tex(r"Rationing switched off $\Rightarrow$ queues,").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4b = Tex(r"favourites, per-family limits").scale(1.0).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4a))
        self.play(Write(b4b))
        self.wait(2.5)
        b4c = Tex(r"Pressure leaks: BLACK MARKET above the").scale(0.95).shift(band_shift(4) + DOWN * 0.4)
        b4d = Tex(r"cap; quality quietly sags").scale(0.95).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4c))
        self.play(Write(b4d))
        self.wait(2.5)
        b4e = Tex(r"Succeeds on price, fails on quantity —").scale(0.95).shift(band_shift(4) + DOWN * 2.0)
        b4f = Tex(r"why states often prefer subsidies or grants").scale(0.95).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4e))
        self.play(Write(b4f))
        self.play(Create(SurroundingRectangle(b4e, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): the floor on the diagram ---
        self.next_band(5)
        b5t = Tex("The floor, drawn").scale(1.15).shift(band_shift(5) + UP * 3.2)
        self.play(Write(b5t))
        self.wait(1.5)
        o5 = band_shift(5) + LEFT * 4.2 + DOWN * 3.2
        xa5, ya5, pl5, ql5 = self.axes(o5)
        self.play(Create(xa5), Create(ya5), Write(pl5), Write(ql5))
        d5, s5, d5_pts, s5_pts = self.market(o5)
        self.play(Create(d5), run_time=1.2)
        self.play(Create(s5), run_time=1.2)
        e5_dot = Dot(o5 + RIGHT * 3.9 + UP * 1.8, color=GREEN)
        self.play(Create(e5_dot))
        self.wait(1)
        # Floor above equilibrium at height 2.7: D at x=2.2, S at x=5.7.
        floor = Line(o5 + UP * 2.7, o5 + RIGHT * 7.4 + UP * 2.7,
                     color=RED, stroke_width=4)
        self.play(Create(floor))
        f_lab = Tex("floor", color=RED).scale(0.75).next_to(o5 + UP * 2.7, LEFT, buff=0.12)
        self.play(Write(f_lab))
        self.wait(1.5)
        gap5 = Line(o5 + RIGHT * 2.2 + UP * 2.7, o5 + RIGHT * 5.7 + UP * 2.7,
                    color=ORANGE, stroke_width=8)
        self.play(Create(gap5))
        b5a = Tex(r"Supplied $\gg$ demanded: SURPLUS —").scale(0.85).shift(band_shift(5) + RIGHT * 3.4 + UP * 1.2)
        b5b = Tex(r"the state buys, stores, exports").scale(0.85).shift(band_shift(5) + RIGHT * 3.4 + UP * 0.5)
        self.play(Write(b5a))
        self.play(Write(b5b))
        self.play(Create(SurroundingRectangle(b5a, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the minimum wage, both ways ---
        self.next_band(6)
        b6t = Tex("The minimum wage — both truths").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        b6a = Tex(r"Mechanics: more labour offered, less").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6b = Tex(r"hired — surplus of labour predicted").scale(0.95).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6a))
        self.play(Write(b6b))
        self.wait(2.5)
        b6c = Tex(r"FOR: dignity, less working poverty,").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        b6d = Tex(r"wages feed the circular flow").scale(0.95).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6c))
        self.play(Write(b6d))
        self.wait(2)
        b6e = Tex(r"AGAINST: youngest and least skilled").scale(0.95).shift(band_shift(6) + DOWN * 2.0)
        b6f = Tex(r"priced out first; work goes informal").scale(0.95).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6e))
        self.play(Write(b6f))
        self.wait(2)
        b6g = Tex(r"Size of the trade-off: measured, not assumed").scale(0.9).shift(band_shift(6) + DOWN * 3.6)
        self.play(Write(b6g))
        self.play(Create(SurroundingRectangle(b6g, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the referee's four calls ---
        self.next_band(7)
        b7t = Tex("The referee enters the game").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        calls = [
            r"Call 1: make it DEARER — the levy",
            r"Call 2: make it CHEAPER — the subsidy",
            r"Call 3: freeze the SCORE — ceiling or floor",
            r"Call 4: hand the ball over — grants, clinics",
        ]
        for i, c in enumerate(calls):
            m = Tex(c).scale(0.9).shift(band_shift(7) + UP * (1.2 - i * 0.75))
            self.play(Write(m), run_time=0.8)
            self.wait(1)
        b7a = Tex(r"Because ``whoever can pay, plays''").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        b7b = Tex(r"is sometimes a rule society refuses").scale(0.95).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(b7a))
        self.play(Write(b7b))
        self.play(Create(SurroundingRectangle(VGroup(b7a, b7b), color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): queues under ceilings, piles on floors ---
        self.next_band(8)
        b8t = Tex("Queues under ceilings, piles on floors").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex(r"Oil capped cheap: shoppers pour in,").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8b = Tex(r"producers pull back — shelves go bare").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8a))
        self.play(Write(b8b))
        self.wait(2.5)
        b8c = Tex(r"Price may not rise: dawn queues, favourites,").scale(0.9).shift(band_shift(8) + DOWN * 0.4)
        b8d = Tex(r"and double-priced bottles out the back").scale(0.9).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(b8c))
        self.play(Write(b8d))
        self.wait(2.5)
        b8e = Tex(r"Potatoes propped dear: fields planted,").scale(0.9).shift(band_shift(8) + DOWN * 2.0)
        b8f = Tex(r"buyers retreat — the state buys the mountain").scale(0.9).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8e))
        self.play(Write(b8f))
        self.wait(2)
        b8g = Tex(r"Queues under ceilings; piles on floors").scale(0.95).shift(band_shift(8) + DOWN * 3.6)
        self.play(Write(b8g))
        self.play(Create(SurroundingRectangle(b8g, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): the wage floor at the factory gate ---
        self.next_band(9)
        b9t = Tex("The wage floor at the factory gate").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex(r"Truth one: employed lives change —").scale(0.95).shift(band_shift(9) + UP * 1.2)
        b9b = Tex(r"wages spent at the spaza and the rank").scale(0.95).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9a))
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = Tex(r"Truth two: fewer hired, gate crowd grows —").scale(0.9).shift(band_shift(9) + DOWN * 0.4)
        b9d = Tex(r"the youngest squeezed out first").scale(0.9).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9c))
        self.play(Write(b9d))
        self.wait(2.5)
        b9e = Tex(r"Three questions for EVERY intervention:").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        b9f = Tex(r"what FOR, what predicted, what ELSE follows").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9e))
        self.play(Write(b9f))
        self.play(Create(SurroundingRectangle(VGroup(b9e, b9f), color=GREEN)))
        self.wait(4)
