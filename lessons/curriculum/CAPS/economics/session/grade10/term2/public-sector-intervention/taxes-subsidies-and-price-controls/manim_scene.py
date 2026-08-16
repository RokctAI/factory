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

# Band-layout whiteboard scene for "Taxes, Subsidies and Price Controls"
# (grade 10, term 2). One band per teaching beat; camera moves down, earlier
# work stays. Market diagrams are hand-built (Arrow axes, straight Line
# curves, DashedLine ceilings/floors, Dot equilibria) — exporter-safe
# primitives only, write-only reveals.
#
# Subtopic shares (subtopics.json, total 1450 s):
# 220/220/210/230/190/190/190.
#
# Diagram geometry (origin-relative): D runs (0.6,4.0)->(7.0,0.8),
# S runs (0.6,0.8)->(7.0,4.0), equilibrium E = (3.8,2.4).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TaxesSubsidiesPriceControlsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def market(self, origin):
        """Axes + D + S + labels; returns nothing extra (positions are fixed)."""
        x_axis = Arrow(origin, origin + RIGHT * 8.2, buff=0, stroke_width=4)
        y_axis = Arrow(origin, origin + UP * 5.0, buff=0, stroke_width=4)
        p_lab = Tex("P").scale(0.85).next_to(y_axis.get_end(), LEFT, buff=0.12)
        q_lab = Tex("Q").scale(0.85).next_to(x_axis.get_end(), DOWN, buff=0.12)
        self.play(Create(x_axis), Create(y_axis), Write(p_lab), Write(q_lab))
        d_line = Line(origin + RIGHT * 0.6 + UP * 4.0, origin + RIGHT * 7.0 + UP * 0.8,
                      color=BLUE, stroke_width=5)
        s_line = Line(origin + RIGHT * 0.6 + UP * 0.8, origin + RIGHT * 7.0 + UP * 4.0,
                      color=YELLOW, stroke_width=5)
        self.play(Create(d_line), Create(s_line))
        d_lab = Tex("D", color=BLUE).scale(0.9).next_to(origin + RIGHT * 7.0 + UP * 0.8, RIGHT, buff=0.12)
        s_lab = Tex("S", color=YELLOW).scale(0.9).next_to(origin + RIGHT * 7.0 + UP * 4.0, RIGHT, buff=0.12)
        self.play(Write(d_lab), Write(s_lab))
        e_dot = Dot(origin + RIGHT * 3.8 + UP * 2.4, color=GREEN)
        self.play(Create(e_dot))

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): why the state steps in, and with what ---
        title = Tex("Taxes, Subsidies and Price Controls").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex(r"The market's rationing — those able to").scale(1.0).shift(UP * 1.2)
        d2 = Tex(r"pay — is sometimes intolerable").scale(1.0).shift(UP * 0.5)
        self.play(Write(d1))
        self.play(Write(d2))
        self.wait(2.5)
        f1 = Tex(r"1. Indirect taxes: VAT, excise, fuel levy").scale(0.95).shift(DOWN * 0.4)
        f2 = Tex(r"2. Subsidies: transport, agriculture").scale(0.95).shift(DOWN * 1.1)
        f3 = Tex(r"3. Welfare: grants, clinics, schools").scale(0.95).shift(DOWN * 1.8)
        f4 = Tex(r"4. Price controls: ceilings, floors, wage").scale(0.95).shift(DOWN * 2.5)
        self.play(Write(f1))
        self.play(Write(f2))
        self.play(Write(f3))
        self.play(Write(f4))
        box0 = SurroundingRectangle(VGroup(f1, f2, f3, f4), color=GREEN)
        self.play(Create(box0))
        self.wait(3)

        # --- Band 1 (subtopic_2): the tax on the diagram ---
        self.next_band(1)
        b1t = Tex("An indirect tax shifts supply left").scale(1.1).shift(band_shift(1) + UP * 2.9)
        self.play(Write(b1t))
        self.wait(1.5)
        o1 = band_shift(1) + LEFT * 4.4 + DOWN * 3.1
        self.market(o1)
        self.wait(1.5)
        s1_line = Line(o1 + RIGHT * 0.6 + UP * 1.8, o1 + RIGHT * 7.0 + UP * 5.0,
                       color=RED, stroke_width=5)
        self.play(Create(s1_line))
        s1_lab = Tex("S1", color=RED).scale(0.9).next_to(o1 + RIGHT * 7.0 + UP * 5.0, RIGHT, buff=0.12)
        self.play(Write(s1_lab))
        e1_dot = Dot(o1 + RIGHT * 2.8 + UP * 2.9, color=RED)
        self.play(Create(e1_dot))
        dash_p1 = DashedLine(o1 + RIGHT * 2.8 + UP * 2.9, o1 + UP * 2.9, color=RED, stroke_width=3)
        dash_q1 = DashedLine(o1 + RIGHT * 2.8 + UP * 2.9, o1 + RIGHT * 2.8, color=RED, stroke_width=3)
        self.play(Create(dash_p1), Create(dash_q1))
        self.wait(2)
        b1a = Tex(r"Price HIGHER, quantity LOWER;").scale(0.9).shift(band_shift(1) + RIGHT * 3.4 + UP * 1.6)
        b1b = Tex(r"burden splits: buyers and").scale(0.9).shift(band_shift(1) + RIGHT * 3.4 + UP * 0.9)
        b1c = Tex(r"sellers share the tax").scale(0.9).shift(band_shift(1) + RIGHT * 3.4 + UP * 0.2)
        self.play(Write(b1a))
        self.play(Write(b1b))
        self.play(Write(b1c))
        self.wait(3)

        # --- Band 2 (subtopic_2): the subsidy mirror + discipline ---
        self.next_band(2)
        b2t = Tex("The subsidy — the tax in reverse").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        b2a = Tex(r"State pays per unit: supply shifts RIGHT —").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2b = Tex(r"price LOWER, quantity HIGHER").scale(1.0).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2a))
        self.play(Write(b2b))
        self.wait(2.5)
        b2c = Tex(r"Honest costs: funded by taxes elsewhere;").scale(0.95).shift(band_shift(2) + DOWN * 0.4)
        b2d = Tex(r"high taxes breed smuggling; subsidies").scale(0.95).shift(band_shift(2) + DOWN * 1.1)
        b2e = Tex(r"can fatten margins, not cut prices").scale(0.95).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2c))
        self.play(Write(b2d))
        self.play(Write(b2e))
        self.wait(2)
        b2w = Tex(r"``The tax just moves the price''").scale(1.0).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2w))
        self.play(Create(strike(b2w)))
        self.wait(1.5)
        b2f = Tex(r"It SHIFTS the supply curve — draw it").scale(1.0).shift(band_shift(2) + DOWN * 3.4)
        self.play(Write(b2f))
        self.play(Create(SurroundingRectangle(b2f, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): the ceiling on the diagram ---
        self.next_band(3)
        b3t = Tex("Maximum price — the ceiling").scale(1.1).shift(band_shift(3) + UP * 2.9)
        self.play(Write(b3t))
        self.wait(1.5)
        o3 = band_shift(3) + LEFT * 4.4 + DOWN * 3.1
        self.market(o3)
        self.wait(1.5)
        ceil = DashedLine(o3 + UP * 1.6, o3 + UP * 1.6 + RIGHT * 6.4,
                          color=RED, stroke_width=4)
        ceil_lab = Tex("ceiling", color=RED).scale(0.8).next_to(o3 + UP * 1.6, LEFT, buff=0.12)
        self.play(Create(ceil), Write(ceil_lab))
        self.wait(1.5)
        qs_dot = Dot(o3 + RIGHT * 2.2 + UP * 1.6, color=YELLOW)
        qd_dot = Dot(o3 + RIGHT * 5.4 + UP * 1.6, color=BLUE)
        self.play(Create(qs_dot), Create(qd_dot))
        qs_lab = Tex("Qs").scale(0.75).next_to(o3 + RIGHT * 2.2, DOWN, buff=0.12)
        qd_lab = Tex("Qd").scale(0.75).next_to(o3 + RIGHT * 5.4, DOWN, buff=0.12)
        drop_s = DashedLine(o3 + RIGHT * 2.2 + UP * 1.6, o3 + RIGHT * 2.2, color=RED, stroke_width=3)
        drop_d = DashedLine(o3 + RIGHT * 5.4 + UP * 1.6, o3 + RIGHT * 5.4, color=RED, stroke_width=3)
        self.play(Create(drop_s), Create(drop_d), Write(qs_lab), Write(qd_lab))
        self.wait(2)
        b3a = Tex(r"Set BELOW equilibrium:").scale(0.9).shift(band_shift(3) + RIGHT * 3.4 + UP * 1.9)
        b3b = Tex(r"Qd $>$ Qs — a SHORTAGE").scale(0.9).shift(band_shift(3) + RIGHT * 3.4 + UP * 1.2)
        self.play(Write(b3a))
        self.play(Write(b3b))
        self.play(Create(SurroundingRectangle(b3b, color=GREEN)))
        self.wait(2)
        b3c = Tex(r"Queues, favoured customers,").scale(0.85).shift(band_shift(3) + RIGHT * 3.4 + UP * 0.3)
        b3d = Tex(r"black market above the ceiling").scale(0.85).shift(band_shift(3) + RIGHT * 3.4 + DOWN * 0.4)
        self.play(Write(b3c))
        self.play(Write(b3d))
        self.wait(3)

        # --- Band 4 (subtopic_3): the honest verdict ---
        self.next_band(4)
        b4t = Tex("The ceiling's honest verdict").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        b4a = Tex(r"Cheap bread for those who GET bread —").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4b = Tex(r"and a shortage deciding who, by luck,").scale(1.0).shift(band_shift(4) + UP * 0.4)
        b4c = Tex(r"queueing or connection").scale(1.0).shift(band_shift(4) + DOWN * 0.3)
        self.play(Write(b4a))
        self.play(Write(b4b))
        self.play(Write(b4c))
        self.wait(2.5)
        b4d = Tex(r"Succeeds at its price goal,").scale(1.0).shift(band_shift(4) + DOWN * 1.2)
        b4e = Tex(r"fails at its quantity goal").scale(1.0).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4d))
        self.play(Write(b4e))
        self.play(Create(SurroundingRectangle(VGroup(b4d, b4e), color=GREEN)))
        self.wait(2)
        b4f = Tex(r"Hence states often prefer subsidies or").scale(0.95).shift(band_shift(4) + DOWN * 2.8)
        b4g = Tex(r"grants to fighting the crossing point").scale(0.95).shift(band_shift(4) + DOWN * 3.5)
        self.play(Write(b4f))
        self.play(Write(b4g))
        self.wait(3)

        # --- Band 5 (subtopic_4): the floor on the diagram ---
        self.next_band(5)
        b5t = Tex("Minimum price — the floor").scale(1.1).shift(band_shift(5) + UP * 2.9)
        self.play(Write(b5t))
        self.wait(1.5)
        o5 = band_shift(5) + LEFT * 4.4 + DOWN * 3.1
        self.market(o5)
        self.wait(1.5)
        floor = DashedLine(o5 + UP * 3.2, o5 + UP * 3.2 + RIGHT * 6.4,
                           color=RED, stroke_width=4)
        floor_lab = Tex("floor", color=RED).scale(0.8).next_to(o5 + UP * 3.2, LEFT, buff=0.12)
        self.play(Create(floor), Write(floor_lab))
        self.wait(1.5)
        qd5 = Dot(o5 + RIGHT * 2.2 + UP * 3.2, color=BLUE)
        qs5 = Dot(o5 + RIGHT * 5.4 + UP * 3.2, color=YELLOW)
        self.play(Create(qd5), Create(qs5))
        b5a = Tex(r"Set ABOVE equilibrium:").scale(0.9).shift(band_shift(5) + RIGHT * 3.4 + UP * 1.6)
        b5b = Tex(r"Qs $>$ Qd — a SURPLUS").scale(0.9).shift(band_shift(5) + RIGHT * 3.4 + UP * 0.9)
        self.play(Write(b5a))
        self.play(Write(b5b))
        self.play(Create(SurroundingRectangle(b5b, color=GREEN)))
        self.wait(2)
        b5c = Tex(r"Silos fill; the state buys, stores,").scale(0.85).shift(band_shift(5) + RIGHT * 3.4)
        b5d = Tex(r"exports — the budget pays").scale(0.85).shift(band_shift(5) + RIGHT * 3.4 + DOWN * 0.7)
        self.play(Write(b5c))
        self.play(Write(b5d))
        self.wait(3)

        # --- Band 6 (subtopic_4): the minimum wage, both ways ---
        self.next_band(6)
        b6t = Tex("The minimum wage — a labour floor").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        b6a = Tex(r"Mechanics: more labour offered, less").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6b = Tex(r"demanded — unemployment pressure").scale(1.0).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6a))
        self.play(Write(b6b))
        self.wait(2.5)
        b6c = Tex(r"FOR: dignity, less working poverty,").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        b6d = Tex(r"wages spent back into the flow").scale(0.95).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6c))
        self.play(Write(b6d))
        self.wait(2)
        b6e = Tex(r"AGAINST: the least skilled priced out,").scale(0.95).shift(band_shift(6) + DOWN * 2.0)
        b6f = Tex(r"some work pushed informal").scale(0.95).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6e))
        self.play(Write(b6f))
        self.wait(2)
        b6g = Tex(r"A trade-off — its size is empirical").scale(1.0).shift(band_shift(6) + DOWN * 3.4)
        self.play(Write(b6g))
        self.play(Create(SurroundingRectangle(b6g, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the referee's four whistles ---
        self.next_band(7)
        b7t = Tex("The referee enters the game").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex(r"Whistle 1: make it DEARER — tax it").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7b = Tex(r"Whistle 2: make it CHEAPER — subsidise").scale(1.0).shift(band_shift(7) + UP * 0.5)
        b7c = Tex(r"Whistle 3: fix the SCORE — ceiling, floor").scale(1.0).shift(band_shift(7) + DOWN * 0.2)
        b7d = Tex(r"Whistle 4: skip the game — grants,").scale(1.0).shift(band_shift(7) + DOWN * 0.9)
        b7e = Tex(r"clinics, no-fee schools").scale(1.0).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7a))
        self.wait(1.5)
        self.play(Write(b7b))
        self.wait(1.5)
        self.play(Write(b7c))
        self.wait(1.5)
        self.play(Write(b7d))
        self.play(Write(b7e))
        self.wait(2)
        b7f = Tex(r"Because ``whoever can pay, plays'' is a").scale(0.95).shift(band_shift(7) + DOWN * 2.5)
        b7g = Tex(r"rule society won't accept for bread").scale(0.95).shift(band_shift(7) + DOWN * 3.2)
        self.play(Write(b7f))
        self.play(Write(b7g))
        self.wait(3)

        # --- Band 8 (subtopic_6): queues under ceilings, piles on floors ---
        self.next_band(8)
        b8t = Tex("Ceilings make queues, floors make piles").scale(1.05).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex(r"Bread capped cheap: buyers crowd in,").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8b = Tex(r"bakers bake less — shelves empty,").scale(1.0).shift(band_shift(8) + UP * 0.5)
        b8c = Tex(r"5 a.m. queues, hidden loaves at double").scale(1.0).shift(band_shift(8) + DOWN * 0.2)
        self.play(Write(b8a))
        self.play(Write(b8b))
        self.play(Write(b8c))
        self.wait(2.5)
        b8d = Tex(r"Maize propped dear: farmers plant all,").scale(1.0).shift(band_shift(8) + DOWN * 1.1)
        b8e = Tex(r"buyers shrink — silos overflow and the").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        b8f = Tex(r"state buys the mountain").scale(1.0).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8d))
        self.play(Write(b8e))
        self.play(Write(b8f))
        self.wait(2)
        b8g = Tex(r"Queues under ceilings; piles on floors").scale(1.0).shift(band_shift(8) + DOWN * 3.3)
        self.play(Write(b8g))
        self.play(Create(SurroundingRectangle(b8g, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): the wage floor at the factory gate ---
        self.next_band(9)
        b9t = Tex("The wage floor at the factory gate").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex(r"Truth one: the employed at the floor —").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9b = Tex(r"rent paid, children fed, spaza fed too").scale(1.0).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9a))
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = Tex(r"Truth two: fewer hands hired — the").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        b9d = Tex(r"youngest and least skilled squeezed out").scale(1.0).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9c))
        self.play(Write(b9d))
        self.wait(2.5)
        b9e = Tex(r"Both can be right — about different").scale(1.0).shift(band_shift(9) + DOWN * 2.0)
        b9f = Tex(r"people; the balance is measured").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9e))
        self.play(Write(b9f))
        self.wait(2)
        b9g = Tex(r"Ask: what FOR, what predicted, what ELSE?").scale(0.95).shift(band_shift(9) + DOWN * 3.4)
        self.play(Write(b9g))
        self.play(Create(SurroundingRectangle(b9g, color=GREEN)))
        self.wait(4)
