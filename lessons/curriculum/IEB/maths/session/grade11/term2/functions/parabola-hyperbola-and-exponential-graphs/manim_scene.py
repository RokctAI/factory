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
# moves down. Only exporter-supported mobjects; write-only reveals. Band
# dwell times follow subtopics.json (235/235/235/245/195/195/205 of 1545 s);
# Level 6 rescales to real audio, so proportion is what matters.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ParabolaHyperbolaExponentialSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: player holds the topic full-screen while intro.md plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): turning-point form
        title = Tex("Parabola, Hyperbola and Exponential Graphs").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        d1 = MathTex(r"y = a(x + p)^2 + q: \; \text{turning point } (-p; q)").scale(1.05).shift(UP * 0.9)
        self.play(Write(d1))
        self.play(Create(SurroundingRectangle(d1, color=GREEN)))
        self.wait(2.5)
        d2 = MathTex(r"y = 2(x + 3)^2 - 8: \; \text{TP } (-3; -8), \text{ axis } x = -3").scale(1.0).shift(DOWN * 0.2)
        d3 = MathTex(r"y\text{-int: } 2(9) - 8 = 10").scale(1.0).shift(DOWN * 1.1)
        self.play(Write(d2))
        self.wait(2.5)
        self.play(Write(d3))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): x-intercepts and the balance check
        self.next_band(1)
        b1_title = Tex("Intercepts balance about the axis").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"2(x+3)^2 = 8 \Rightarrow (x+3)^2 = 4").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"x + 3 = \pm 2 \Rightarrow x = -1 \text{ or } x = -5").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = MathTex(r"\text{Audit: } \tfrac{-1 + (-5)}{2} = -3 = \text{axis} \; \checkmark").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = Tex(r"Domain: all real $x$; range: $y \geq -8$").scale(1.0).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l3))
        self.wait(2.5)
        self.play(Write(b1_l4))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the hyperbola's cross
        self.next_band(2)
        b2_title = MathTex(r"y = \frac{4}{x+1} - 2").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_va = Line(band_shift(2) + UP * 1.4 + LEFT * 1.0, band_shift(2) + DOWN * 2.6 + LEFT * 1.0, color=RED)
        b2_ha = Line(band_shift(2) + DOWN * 1.2 + LEFT * 5.0, band_shift(2) + DOWN * 1.2 + RIGHT * 3.0, color=RED)
        self.play(Create(b2_va), Create(b2_ha))
        self.wait(2)
        b2_l1 = Tex(r"Asymptotes: $x = -1$, $y = -2$; centre $(-1; -2)$").scale(0.95).shift(band_shift(2) + UP * 1.1 + RIGHT * 1.5)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"y\text{-int: } \tfrac{4}{1} - 2 = 2; \quad x\text{-int: } \tfrac{4}{x+1} = 2 \Rightarrow x = 1").scale(0.9).shift(band_shift(2) + UP * 0.2 + RIGHT * 1.2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = Tex(r"Domain: $x \neq -1$; range: $y \neq -2$ — write the exceptions").scale(0.85).shift(band_shift(2) + DOWN * 2.9 + RIGHT * 0.5)
        self.play(Write(b2_l3))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): the exponential
        self.next_band(3)
        b3_title = MathTex(r"y = 4 \cdot 2^{x-1} - 8").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Floor: $y = -8$ — $2^{\text{anything}}$ is strictly positive").scale(0.95).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"y\text{-int: } 4 \cdot 2^{-1} - 8 = 2 - 8 = -6").scale(1.0).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"x\text{-int: } 2^{x-1} = 2 \Rightarrow x - 1 = 1 \Rightarrow x = 2").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l2))
        self.wait(2.5)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex(r"Range: $y > -8$ STRICTLY — approach, never touch").scale(0.95).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_4): average gradient
        self.next_band(4)
        b4_title = Tex("Average gradient on $y = x^2$").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"x = 2 \to 4: \; \frac{16 - 4}{4 - 2} = 6").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(2.5)
        b4_l2 = MathTex(r"2 \to 3: 5 \quad 2 \to 2{,}5: 4{,}5 \quad 2 \to 2{,}1: 4{,}1").scale(0.95).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex(r"The averages converge on 4 — the curve's own steepness at $x = 2$").scale(0.85).shift(band_shift(4) + DOWN * 0.9)
        b4_l4 = Tex(r"'between' $=$ string; 'at' $=$ limit").scale(0.95).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l3))
        self.wait(2.5)
        self.play(Write(b4_l4))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): sliding the tent
        self.next_band(5)
        b5_title = Tex("Sliding the tent").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex(r"$q$: the crane. $p$: sideways push (against the sign). $a$: canvas tension").scale(0.85).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex(r"$y = 2(x+3)^2 - 8$: push 3 left, lower 8, double tension").scale(0.9).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex(r"Ask: what $x$ zeroes the bracket? That is the pole").scale(0.95).shift(band_shift(5) + DOWN * 0.8)
        b5_l4 = Tex(r"Intercepts $-5$ and $-1$ average to the pole at $-3$").scale(0.95).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l3))
        self.wait(2.5)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_6): the fences
        self.next_band(6)
        b6_title = Tex("The fences you never touch").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"Hyperbola: two fences crossing at the centre — branches in opposite corners").scale(0.8).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = Tex(r"Exponential: one fence — a floor at $y = q$").scale(0.95).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex(r"Domain and range are the fences written as sentences").scale(0.9).shift(band_shift(6) + DOWN * 0.7)
        b6_l4 = Tex(r"Tent touches ($\geq$); fences are only approached ($>$)").scale(0.9).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l3))
        self.wait(2.5)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_7): tollgates
        self.next_band(7)
        b7_title = Tex("Average speed between two tollgates").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"240 \text{ km in } 3 \text{ h} \Rightarrow 80 \text{ km/h average}").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex(r"Average gradient $=$ the taut string between two points").scale(0.9).shift(band_shift(7) + UP * 0.2)
        b7_l3 = MathTex(r"\text{Strings: } 5, \; 4{,}5, \; 4{,}1 \; \to \; 4").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l2))
        self.wait(2.5)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex(r"4 $=$ the speedometer at the instant $x = 2$").scale(0.95).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l4))
        self.wait(4)
