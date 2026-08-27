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

# Band-layout whiteboard scene for the session duo "Parabola, Hyperbola and
# Exponential Graphs" (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier:
# subtopics 5-7). One band per teaching beat, add-only lifecycle, camera
# moves down. Only exporter-supported mobjects; write-only reveals.
# Band dwell times follow subtopics.json (235/235/235/245/195/195/205 of
# 1545 s); Level 6 rescales to real audio, so proportion is what matters.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ParabolaHyperbolaExponentialSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: player holds the topic full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): turning-point form and the three controls
        title = Tex("Parabola, Hyperbola and Exponential Graphs").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        d1 = MathTex(r"y = a(x + p)^2 + q").scale(1.25).shift(UP * 0.9)
        self.play(Write(d1))
        self.play(Create(SurroundingRectangle(d1, color=GREEN)))
        self.wait(2)
        d2 = MathTex(r"\text{Turning point } (-p; q), \quad \text{axis } x = -p").scale(1.05).shift(DOWN * 0.2)
        self.play(Write(d2))
        self.wait(2.5)
        d3 = Tex(r"$a$: shape — up if positive, down if negative, big $=$ narrow").scale(0.9).shift(DOWN * 1.1)
        d4 = Tex(r"$p$: slides sideways, OPPOSITE to its sign; $q$: up or down").scale(0.9).shift(DOWN * 1.9)
        self.play(Write(d3))
        self.wait(2)
        self.play(Write(d4))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): full parabola example
        self.next_band(1)
        b1_title = Tex(r"Read $y = 2(x - 1)^2 - 8$ in full").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\text{TP } (1; -8) \text{ minimum}, \quad \text{axis } x = 1").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"y\text{-int } (x = 0): \; 2(1) - 8 = -6").scale(1.0).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"x\text{-ints: } 2(x-1)^2 = 8 \;\Rightarrow\; (x-1)^2 = 4").scale(1.0).shift(band_shift(1) + DOWN * 0.6)
        b1_l4 = MathTex(r"x - 1 = \pm 2 \;\Rightarrow\; x = 3 \text{ or } x = -1").scale(1.0).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l3))
        self.wait(2.5)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)
        b1_l5 = Tex(r"Check: $3$ and $-1$ average to $1$, the axis").scale(0.95).shift(band_shift(1) + DOWN * 2.4)
        b1_l6 = MathTex(r"\text{Domain } x \in \mathbb{R}; \quad \text{range } y \geq -8").scale(0.95).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(b1_l5))
        self.wait(2)
        self.play(Write(b1_l6))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the hyperbola's asymptote cross
        self.next_band(2)
        b2_title = Tex(r"Hyperbola: $y = \dfrac{3}{x - 2} + 1$").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"\text{Vertical asymptote: } x = 2 \;\text{(no division by 0)}").scale(0.95).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"\text{Horizontal asymptote: } y = 1 \;\text{(fraction never 0)}").scale(0.95).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2.5)
        vline = Line(UP * 0.6, DOWN * 2.6, stroke_width=3, color=BLUE).shift(band_shift(2) + LEFT * 2.8 + DOWN * 0.3)
        hline = Line(LEFT * 1.6, RIGHT * 1.6, stroke_width=3, color=BLUE).shift(band_shift(2) + LEFT * 2.8 + DOWN * 1.3)
        centre = Dot(band_shift(2) + LEFT * 2.8 + DOWN * 1.3, color=YELLOW)
        self.play(Create(vline), Create(hline))
        self.play(Create(centre))
        self.wait(1.5)
        b2_l3 = Tex(r"Centre $(2; 1)$ where the fences cross").scale(0.95).shift(band_shift(2) + DOWN * 0.9 + RIGHT * 2.4)
        b2_l4 = Tex(r"$a > 0$: branches top-right, bottom-left").scale(0.95).shift(band_shift(2) + DOWN * 1.8 + RIGHT * 2.4)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): hyperbola intercepts, domain, symmetry
        self.next_band(3)
        b3_title = Tex("Intercepts and the two exceptions").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"y\text{-int: } \frac{3}{-2} + 1 = -0{,}5").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"x\text{-int: } x - 2 = -3 \Rightarrow x = -1").scale(0.95).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = MathTex(r"\text{Domain: } x \neq 2; \; \text{range: } y \neq 1").scale(0.9).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex(r"Axes of symmetry through the centre:").scale(0.95).shift(band_shift(3) + DOWN * 1.8)
        b3_l5 = MathTex(r"y = x - 1 \quad \text{and} \quad y = -x + 3").scale(1.0).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l4))
        self.wait(1.5)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): the exponential raised and shifted
        self.next_band(4)
        b4_title = Tex(r"Exponential: $y = 2 \times 3^{x+1} - 6$").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"\text{Asymptote: } y = -6 \;\text{(the floor)}").scale(1.0).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"y\text{-int: } 2 \times 3^{1} - 6 = 0 \;\text{— through the origin}").scale(0.95).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"x\text{-int: } 2 \times 3^{x+1} = 6 \Rightarrow 3^{x+1} = 3^1").scale(0.95).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = MathTex(r"x + 1 = 1 \;\Rightarrow\; x = 0").scale(1.0).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l3))
        self.wait(2.5)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2.5)
        b4_l5 = MathTex(r"\text{Range: } y > -6 \;\text{STRICT — never lands on the floor}").scale(0.9).shift(band_shift(4) + DOWN * 2.4)
        b4_l6 = Tex("Parabola touches its extreme; exponential only approaches").scale(0.85).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4_l5))
        self.wait(2.5)
        self.play(Write(b4_l6))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): average gradient
        self.next_band(5)
        b5_title = Tex(r"Average gradient on $y = x^2$, from $x=1$ to $x=3$").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"y(1) = 1, \quad y(3) = 9").scale(1.1).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"m_{\text{avg}} = \frac{9 - 1}{3 - 1} = \frac{8}{2} = 4").scale(1.1).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex("The gradient of the straight line joining the points").scale(0.95).shift(band_shift(5) + DOWN * 1.1)
        b5_l4 = Tex("Curve starts shallower than 4, finishes steeper").scale(0.95).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the averages march to a limit
        self.next_band(6)
        b6_title = Tex(r"Drag the right point towards $x = 1$").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"[1; 2]: \; \frac{4 - 1}{1} = 3").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"[1; 1{,}5]: \; \frac{2{,}25 - 1}{0{,}5} = 2{,}5").scale(1.0).shift(band_shift(6) + UP * 0.2)
        b6_l3 = MathTex(r"[1; 1{,}1]: \; \frac{1{,}21 - 1}{0{,}1} = 2{,}1").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"3, \; 2{,}5, \; 2{,}1, \; \dots \;\to\; 2").scale(1.1).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_l5 = Tex("Between two points: a calculation; at a point: a limit").scale(0.95).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_l5))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): sliding the tent
        self.next_band(7)
        b7_title = Tex("Sliding the tent").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"$q$ is a crane: lift or lower, shape untouched").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex(r"$p$ pushes sideways — opposite to the sign you see").scale(1.0).shift(band_shift(7) + UP * 0.2)
        b7_l3 = Tex(r"$a$ is fabric tension; negative flips the tent over").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex(r"$y = 2(x-1)^2 - 8$: right 1, drop 8, tension 2").scale(1.0).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2.5)
        b7_l5 = Tex(r"Walls cross the ground at $-1$ and $3$ — averaging to the pole").scale(0.9).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): the fences you never touch
        self.next_band(8)
        b8_title = Tex("The fences you never touch").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Hyperbola: two fences crossing at the centre").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex(r"branches curl into opposite corners of the yard").scale(1.0).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(3)
        b8_l3 = Tex(r"Exponential: one fence — a floor (or ceiling) at $q$").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("Domain and range are just fences written as sentences").scale(0.95).shift(band_shift(8) + DOWN * 1.6)
        b8_l5 = Tex("Approach is not touch: strict $>$ for the exponential,").scale(0.95).shift(band_shift(8) + DOWN * 2.5)
        b8_l6 = Tex("but $\\geq$ for the tent, which really lands").scale(0.95).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(b8_l4))
        self.wait(2.5)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_7): average speed between tollgates
        self.next_band(9)
        b9_title = Tex("Average speed between two tollgates").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"180 \text{ km in 2 h} \;\Rightarrow\; 90 \text{ km/h average}").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex(r"A taut string between two curve points: gradient 4").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"\text{Gates closer: } 3, \; 2{,}5, \; 2{,}1 \;\to\; 2").scale(1.05).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex(r"2 is the speedometer reading at the instant $x = 1$").scale(1.0).shift(band_shift(9) + DOWN * 1.8)
        b9_l5 = Tex(r"``Between'' means the string; ``at'' means the speedometer").scale(0.95).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l4))
        self.wait(2.5)
        self.play(Write(b9_l5))
        self.wait(4)
