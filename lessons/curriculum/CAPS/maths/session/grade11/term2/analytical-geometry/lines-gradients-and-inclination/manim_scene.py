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

# Band-layout whiteboard scene for the session duo "Lines, Gradients and
# Inclination" (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier:
# subtopics 5-7). One band per teaching beat, add-only lifecycle, camera
# moves down. Only exporter-supported mobjects; write-only reveals.
# Band dwell times follow subtopics.json (230/220/250/240/190/190/210 of
# 1530 s); Level 6 rescales to real audio, so proportion is what matters.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class LinesGradientsInclinationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: player holds the topic full-screen while intro.md plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the working pair, and distance
        title = Tex("Lines, Gradients and Inclination").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        d1 = MathTex(r"A(-2; 3) \quad \text{and} \quad B(4; -5)").scale(1.15).shift(UP * 0.9)
        self.play(Write(d1))
        self.wait(2)
        d2 = MathTex(r"\text{Gaps: } 4 - (-2) = 6, \quad -5 - 3 = -8").scale(1.05).shift(DOWN * 0.1)
        d3 = MathTex(r"AB^2 = 6^2 + 8^2 = 100 \;\Rightarrow\; AB = 10").scale(1.1).shift(DOWN * 1.1)
        self.play(Write(d2))
        self.wait(2.5)
        self.play(Write(d3))
        self.play(Create(SurroundingRectangle(d3, color=GREEN)))
        self.wait(2)
        d4 = Tex("The distance formula is Pythagoras in coordinates").scale(1.0).shift(DOWN * 2.2)
        self.play(Write(d4))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): midpoint and gradient
        self.next_band(1)
        b1_title = Tex("Midpoint and gradient of $AB$").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"M = \left( \frac{-2 + 4}{2}; \; \frac{3 + (-5)}{2} \right) = (1; -1)").scale(1.05).shift(band_shift(1) + UP * 1.0)
        self.play(Write(b1_l1))
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2.5)
        b1_l2 = MathTex(r"m_{AB} = \frac{-5 - 3}{4 - (-2)} = \frac{-8}{6} = -\frac{4}{3}").scale(1.05).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("Subtract in the same order, top and bottom").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        b1_l4 = Tex("Horizontal: $m = 0$; vertical: no gradient at all").scale(1.0).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): parallel and perpendicular
        self.next_band(2)
        b2_title = Tex("Parallel and perpendicular").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Parallel: } m_1 = m_2").scale(1.1).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"\text{Perpendicular: } m_1 \times m_2 = -1").scale(1.1).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"\text{Flip and switch: } -\tfrac{4}{3} \;\to\; +\tfrac{3}{4}").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = MathTex(r"\text{Check: } -\tfrac{4}{3} \times \tfrac{3}{4} = -1").scale(1.05).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)
        b2_l5 = Tex("Exception: horizontal $\\perp$ vertical — quote the geometry").scale(0.95).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l5))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): collinear points
        self.next_band(3)
        b3_title = Tex(r"Collinear: is $C(7; -9)$ on line $AB$?").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"m_{AB} = -\frac{4}{3}").scale(1.1).shift(band_shift(3) + UP * 1.0)
        b3_l2 = MathTex(r"m_{BC} = \frac{-9 - (-5)}{7 - 4} = \frac{-4}{3}").scale(1.05).shift(band_shift(3) + UP * 0.0)
        b3_l3 = MathTex(r"m_{AB} = m_{BC}, \text{ shared } B \Rightarrow \text{collinear}").scale(1.0).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2.5)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = Tex("Parallelogram $=$ two gradient pairs; right angle $=$ product $-1$").scale(0.9).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): equation from two points
        self.next_band(4)
        b4_title = Tex(r"Equation through $A(-2; 3)$ and $B(4; -5)$").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"y = mx + c, \quad m = -\tfrac{4}{3}").scale(1.1).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"\text{Sub } B: \; -5 = -\tfrac{4}{3}(4) + c").scale(1.05).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"c = \tfrac{16}{3} - 5 = \tfrac{1}{3}").scale(1.05).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"y = -\tfrac{4}{3}x + \tfrac{1}{3}").scale(1.15).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = MathTex(r"\text{Check } A: \; -\tfrac{4}{3}(-2) + \tfrac{1}{3} = \tfrac{9}{3} = 3").scale(1.0).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): parallel, perpendicular, special cases
        self.next_band(5)
        b5_title = Tex("Inherit or flip the gradient").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Through $(1; 2)$, parallel to $y = 3x - 4$: $m = 3$").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"2 = 3(1) + c \;\Rightarrow\; c = -1: \quad y = 3x - 1").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex(r"Through $(2; -1)$, perp. to $y = 2x + 3$: $m = -\tfrac{1}{2}$").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        b5_l4 = MathTex(r"-1 = -\tfrac{1}{2}(2) + c \Rightarrow c = 0: \; y = -\tfrac{1}{2}x").scale(1.0).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l3))
        self.wait(2.5)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex(r"Vertical: $x = $ constant; horizontal: $y = $ constant").scale(1.0).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l5))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): inclination — the angle in the gradient
        self.next_band(6)
        b6_title = Tex("Inclination: the angle inside the gradient").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"m = \tan\theta, \; 0^\circ \leq \theta < 180^\circ").scale(1.1).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2.5)
        b6_l2 = Tex("Rise over run is opposite over adjacent").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"m = 1: \theta = 45^\circ \quad m = 2: \theta = 63{,}43^\circ").scale(0.95).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex("Rising line: acute angle, calculator answers directly").scale(0.95).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): falling lines and boundaries
        self.next_band(7)
        b7_title = Tex(r"Falling line: $m = -\tfrac{4}{3}$").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_wrong = MathTex(r"\tan^{-1}(-\tfrac{4}{3}) = -53{,}13^\circ \text{ (not inclination)}").scale(0.95).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_wrong))
        self.play(Create(strike(b7_wrong)))
        self.wait(2)
        b7_l1 = MathTex(r"\text{Size first: } \tan^{-1}\left(\tfrac{4}{3}\right) = 53{,}13^\circ").scale(1.0).shift(band_shift(7) + UP * 0.3)
        b7_l2 = MathTex(r"\text{Tan negative in Q2: } \theta = 180^\circ - 53{,}13^\circ").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        b7_l3 = MathTex(r"\theta = 126{,}87^\circ").scale(1.15).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        b7_l4 = MathTex(r"\theta = 135^\circ \Rightarrow m = \tan 135^\circ = -1").scale(1.0).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex(r"Horizontal: $0^\circ$; vertical: $90^\circ$, $\tan$ undefined").scale(0.9).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l5))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the town grid
        self.next_band(8)
        b8_title = Tex("The town grid").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"$(-2; 3)$ is an address: 2 blocks west, 3 north").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex(r"Walk 6 east, 8 south — the crow cuts the diagonal:").scale(1.0).shift(band_shift(8) + UP * 0.2)
        b8_l3 = MathTex(r"6^2 + 8^2 = 100 \;\Rightarrow\; 10 \text{ blocks direct}").scale(1.05).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex(r"Meet halfway: average both parts — $(1; -1)$").scale(1.0).shift(band_shift(8) + DOWN * 1.7)
        b8_l5 = Tex(r"Steepness: lose 8 north per 6 east $= -\tfrac{4}{3}$").scale(1.0).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l4))
        self.wait(2.5)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): ramps, twins and corners
        self.next_band(9)
        b9_title = Tex("Ramps, twins and corners").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Twins: same steepness, run side by side — parallel").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex(r"Perfect corner: flip and switch — $-\tfrac{4}{3} \to +\tfrac{3}{4}$").scale(1.0).shift(band_shift(9) + UP * 0.2)
        b9_l3 = MathTex(r"m_1 \times m_2 = -1 \;\text{ — the corner test}").scale(1.05).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l2))
        self.wait(2.5)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("Queue test: same gradient $A$ to $B$ as $B$ to $C$").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        b9_l5 = Tex("Every show-that question is twins, corners or queues").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l4))
        self.wait(2.5)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): directions from a landmark
        self.next_band(10)
        b10_title = Tex("Directions from a landmark").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"$y = mx + c$: start $c$ up, climb $m$ per block east").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex("Steal a twin's steepness, or flip a corner's").scale(1.0).shift(band_shift(10) + UP * 0.2)
        b10_l3 = MathTex(r"(2; -1), m = -\tfrac{1}{2}: c = 0 \Rightarrow y = -\tfrac{1}{2}x").scale(1.0).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10_l2))
        self.wait(2.5)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2.5)
        b10_l4 = Tex(r"Bearing: steepness $= \tan(\text{angle})$; falling $=$ obtuse").scale(0.95).shift(band_shift(10) + DOWN * 1.7)
        b10_l5 = MathTex(r"m = -\tfrac{4}{3}: \; 180^\circ - 53{,}13^\circ = 126{,}87^\circ").scale(1.0).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l4))
        self.wait(2.5)
        self.play(Write(b10_l5))
        self.wait(4)
