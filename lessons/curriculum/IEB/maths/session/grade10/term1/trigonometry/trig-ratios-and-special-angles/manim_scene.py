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

# Band-layout whiteboard scene: one band per teaching beat, camera moves down
# to fresh space, nothing removed. Write-only reveals on single-string
# Tex/MathTex keep the export clean. Bands cover all seven subtopics
# (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7), dwell time proportional
# to subtopics.json (220/250/230/260/170/170/170 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TrigRatiosAndSpecialAnglesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the three ratios
        title = Tex("Trig Ratios and Special Angles").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        tri = Polygon([-3, -2.2, 0], [2.5, -2.2, 0], [2.5, 0.8, 0], color=WHITE)
        self.play(Create(tri))
        self.wait(1.5)
        l01 = MathTex(r"\sin\theta = \frac{O}{H}, \quad \cos\theta = \frac{A}{H}, \quad \tan\theta = \frac{O}{A}").scale(0.95).shift(UP * 1.4)
        self.play(Write(l01))
        self.play(Create(SurroundingRectangle(l01, color=YELLOW)))
        self.wait(2)
        l02 = Tex(r"SOH CAH TOA — and the ratio belongs to the ANGLE").scale(0.9).shift(DOWN * 3.0)
        self.play(Write(l02))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): the two special triangles
        self.next_band(1)
        b1_title = Tex("Two triangles, six values").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Equilateral side 2, halved: height $\sqrt{3}$").scale(0.95).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"\sin 60^\circ = \tfrac{\sqrt{3}}{2}, \; \cos 60^\circ = \tfrac{1}{2}, \; \tan 60^\circ = \sqrt{3}").scale(0.9).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"\sin 30^\circ = \tfrac{1}{2}, \; \cos 30^\circ = \tfrac{\sqrt{3}}{2}, \; \tan 30^\circ = \tfrac{1}{\sqrt{3}}").scale(0.9).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex(r"Square side 1, diagonal $\sqrt{2}$: \; $\sin 45^\circ = \cos 45^\circ = \tfrac{1}{\sqrt{2}}$, $\tan 45^\circ = 1$").scale(0.8).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l4))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the evaluation
        self.next_band(2)
        b2_title = Tex(r"Evaluate: $\sin 45^\circ \cos 45^\circ + \tan 60^\circ \tan 30^\circ$").scale(0.95).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\tfrac{1}{\sqrt{2}} \times \tfrac{1}{\sqrt{2}} = \tfrac{1}{2}").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"\sqrt{3} \times \tfrac{1}{\sqrt{3}} = 1").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"\tfrac{1}{2} + 1 = \tfrac{3}{2}").scale(1.1).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_l4 = Tex(r"Exact surds, exact fraction — no decimals anywhere").scale(0.9).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l4))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): the inverse move
        self.next_band(3)
        b3_title = Tex(r"Find $x$: hypotenuse 25, opposite 7").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\sin x = \frac{7}{25}").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"x = \sin^{-1}\!\left(\frac{7}{25}\right) = 16{,}3^\circ").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = Tex(r"Check 1: $0{,}28 < 0{,}5 = \sin 30^\circ$, so $x < 30^\circ$").scale(0.85).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex(r"Check 2: 7-24-25 triple; $16{,}3^\circ + 73{,}7^\circ = 90^\circ$").scale(0.85).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): where you stand
        self.next_band(4)
        b4_title = Tex("Where you stand decides the names").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex(r"Slide = hypotenuse: loyal to the square corner").scale(0.95).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex(r"Move seats and opposite/adjacent trade places").scale(0.95).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex(r"Angle first, names second").scale(1.05).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=YELLOW)))
        self.wait(2.5)

        # --- Band 5 (subtopic_6): rebuild anywhere
        self.next_band(5)
        b5_title = Tex("Two triangles you can rebuild anywhere").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex(r"Road sign cut in half; serviette folded corner to corner").scale(0.85).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"\tfrac{1}{\sqrt{2}} \cdot \tfrac{1}{\sqrt{2}} + \sqrt{3} \cdot \tfrac{1}{\sqrt{3}} = \tfrac{1}{2} + 1 = \tfrac{3}{2}").scale(0.95).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2)
        b5_l3 = Tex(r"Exact fraction = finished answer").scale(0.95).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(2.5)

        # --- Band 6 (subtopic_7): forward gear, reverse gear
        self.next_band(6)
        b6_title = Tex("Forward gear, reverse gear").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"Forward: angle in, ratio out. Reverse: ratio in, angle out.").scale(0.85).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"\sin x = \frac{7}{25} \;\Rightarrow\; x = \sin^{-1}\!\left(\frac{7}{25}\right) = 16{,}3^\circ").scale(0.95).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2)
        b6_wrong = MathTex(r"\sin 30^\circ = -0{,}988").scale(0.95).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_wrong))
        self.play(Create(strike(b6_wrong)))
        b6_l3 = Tex(r"Wrong mode — find the D, reset, retest with $\sin 30^\circ = 0{,}5$").scale(0.8).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l3))
        self.wait(4)
