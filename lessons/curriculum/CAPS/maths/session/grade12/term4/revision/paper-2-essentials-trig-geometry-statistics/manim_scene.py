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

# BAND LAYOUT (see lessons/scripts/manim_exporter.py): content is laid out in
# sequential vertical bands along a long virtual canvas — one band per teaching
# step, each one frame-height tall. Nothing is ever faded out or overwritten;
# at each step the camera moves down to clean space and earlier work stays on
# the canvas. Every mobject serializes to the whiteboard vocabulary
# (text/line/rect via Tex/MathTex/Line/SurroundingRectangle) — no sub-part
# Transform tricks, which leak raw glyph primitives through the exporter's
# Tex shim.
#
# The scene mirrors script.md's teaching beats across all seven subtopics of
# the session duo (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier:
# subtopics 5-7), with band dwell times proportional to subtopics.json
# (245/245/255/240/180/180/185 of 1530 s). Level 6 rescales primitive times
# to the real audio duration, so proportion — not absolute seconds — is what
# must match.

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k (k=0 is the default
    frame; each band is one frame-height further down)."""
    return DOWN * BAND * k


def strike(m):
    """Diagonal cancellation stroke through a term, teacher-style."""
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class Paper2EssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Opening intro beat: the player shows the TOPIC full-screen while the
        # tutor speaks intro.md; board work must not start until it lands.
        self.wait(16)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): calculator statistics on ten marks
        title = Tex("Paper 2 Essentials").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_data = MathTex(r"12;\,45;\,52;\,58;\,61;\,64;\,68;\,72;\,75;\,94").scale(0.9).shift(UP * 1.1)
        self.play(Write(b0_data))
        self.wait(2)
        b0_mean = MathTex(r"\bar{x} = \frac{601}{10} = 60{,}1").scale(1.1).shift(UP * 0.1)
        self.play(Write(b0_mean))
        self.wait(2.5)
        b0_sd = MathTex(r"\sigma = 20{,}5 \;\; \text{(calculator stats mode)}").scale(1.0).shift(DOWN * 1.0)
        self.play(Write(b0_sd))
        self.wait(2.5)
        b0_five = MathTex(r"12; \; Q_1 = 52; \; 62{,}5; \; Q_3 = 72; \; 94").scale(0.9).shift(DOWN * 2.0)
        self.play(Write(b0_five))
        self.wait(3)

        # --- Band 1 (subtopic_1): the fence rule and the 1-sigma count
        self.next_band(1)
        b1_t = Tex("The fence rule polices outliers").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = MathTex(r"IQR = 72 - 52 = 20").scale(1.1).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"\text{fence} = 52 - 1{,}5 \times 20 = 22").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = MathTex(r"12 < 22 \;\Rightarrow\; 12 \text{ is an outlier}").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_l4 = MathTex(r"\bar{x} \pm \sigma: \; 39{,}6 \text{ to } 80{,}6").scale(1.0).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("Counting the list: 8 of the 10 marks").scale(0.95).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_1): regression and the fenced prediction
        self.next_band(2)
        b2_t = Tex("Regression: temperature vs cans sold").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"\hat{y} = -5{,}43 + 1{,}15x").scale(1.15).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"r = 0{,}999: \text{ very strong positive}").scale(0.95).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("Gradient: one more can per degree warmer").scale(0.9).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = MathTex(r"x = 25 \Rightarrow \approx 23 \text{ cans (inside range)}").scale(0.9).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2.5)
        b2_l5 = Tex(r"$x = 40$: extrapolation — decline to trust").scale(0.9).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): the four formulas on A and B
        self.next_band(3)
        b3_t = Tex(r"$A(-3;2)$, $B(5;6)$: four formulas").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_l1 = MathTex(r"m = \frac{6 - 2}{5 - (-3)} = \frac{4}{8} = \tfrac{1}{2}").scale(1.0).shift(band_shift(3) + UP * 1.0)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"M = (1; 4)").scale(1.1).shift(band_shift(3) + DOWN * 0.1)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"AB = \sqrt{8^2 + 4^2} = \sqrt{80} = 4\sqrt{5}").scale(0.95).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("Surds stay surds unless decimals asked").scale(0.95).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_2): the inclination compass
        self.next_band(4)
        b4_t = Tex("The inclination compass").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"\tan\theta = m = \tfrac{1}{2} \Rightarrow \theta \approx 26{,}57^\circ").scale(0.82).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex(r"Negative gradient: add $180^\circ$").scale(1.0).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"\text{parallel: equal } m; \quad \perp: \; m_1 m_2 = -1").scale(0.9).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = MathTex(r"y - y_1 = m(x - x_1)").scale(1.1).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_2): the circle's corridor
        self.next_band(5)
        b5_t = Tex(r"Circle: $x^2 + y^2 - 6x + 4y - 12 = 0$").scale(0.95).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_l1 = MathTex(r"(x - 3)^2 + (y + 2)^2 = 25").scale(1.1).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"\text{centre } (3; -2), \quad r = 5").scale(1.05).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = MathTex(r"\text{at } (7;1): \; m_r = \tfrac{3}{4} \Rightarrow m_t = -\tfrac{4}{3}").scale(0.9).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex(r"tangent $\perp$ radius, then point-gradient").scale(0.9).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_3): cos 75 degrees, exactly
        self.next_band(6)
        b6_t = Tex(r"$\cos 75^\circ$ exactly: split $45^\circ + 30^\circ$").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = MathTex(r"\cos(A + B) = \cos A \cos B - \sin A \sin B").scale(0.9).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"= \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} - \frac{\sqrt{2}}{2} \cdot \frac{1}{2}").scale(0.88).shift(band_shift(6) + DOWN * 0.1)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"= \frac{\sqrt{6} - \sqrt{2}}{4}").scale(1.15).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        b6_l4 = Tex("Exact — no calculator decimal earns marks").scale(0.9).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_3): the three faces of cos 2x
        self.next_band(7)
        b7_t = Tex(r"$\cos 2x$ wears three faces").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = MathTex(r"\cos^2 x - \sin^2 x, \; 2\cos^2 x - 1, \; 1 - 2\sin^2 x").scale(0.8).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"\sin x = \tfrac{3}{5}, \; x \text{ acute}: \; \cos x = \tfrac{4}{5}").scale(0.85).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"\sin 2x = 2 \cdot \tfrac{3}{5} \cdot \tfrac{4}{5} = \tfrac{24}{25}").scale(1.0).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = MathTex(r"\cos 2x = \tfrac{16}{25} - \tfrac{9}{25} = \tfrac{7}{25}").scale(1.0).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_3): the identity — choose the killing face
        self.next_band(8)
        b8_t = Tex(r"Prove: $\dfrac{\sin 2x}{1 - \cos 2x} = \dfrac{\cos x}{\sin x}$").scale(1.05).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = MathTex(r"\sin 2x = 2\sin x \cos x").scale(1.05).shift(band_shift(8) + UP * 1.0)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"1 - \cos 2x = 2\sin^2 x \text{ (the face that kills the 1)}").scale(0.8).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"\frac{2\sin x \cos x}{2\sin^2 x} = \frac{\cos x}{\sin x} \;\checkmark").scale(0.88).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("One side only — never multiply across").scale(0.95).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_3): general solution, then triangle rules
        self.next_band(9)
        b9_t = Tex(r"$\cos x = -\tfrac{1}{2}$: family first").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = MathTex(r"x = \pm 120^\circ + k \cdot 360^\circ, \; k \in \mathbb{Z}").scale(0.92).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.play(Create(SurroundingRectangle(b9_l1, color=GREEN)))
        self.wait(2.5)
        b9_l2 = MathTex(r"x^2 = 49 + 81 - 2(7)(9)\cos 60^\circ = 67").scale(0.9).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"x = \sqrt{67} \approx 8{,}19").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = MathTex(r"\text{Area} = \tfrac{1}{2}(7)(9)\sin 60^\circ \approx 27{,}28").scale(0.95).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = MathTex(r"h = 45\tan 38^\circ \approx 35{,}16 \text{ m}").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_4): the theorems in memo wording
        self.next_band(10)
        b10_t = Tex("Theorems in memo wording").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex(r"Angle at centre $= 2\times$ circumference").scale(0.9).shift(band_shift(10) + UP * 1.3)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex(r"Same segment equal; semicircle $90^\circ$").scale(0.9).shift(band_shift(10) + UP * 0.5)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Cyclic quad: opposite angles supplementary").scale(0.85).shift(band_shift(10) + DOWN * 0.3)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex("Tan-chord: angle in alternate segment").scale(0.9).shift(band_shift(10) + DOWN * 1.1)
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex("Tangents from a common point are equal").scale(0.9).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l5))
        self.wait(2)
        b10_l6 = Tex("Parallel line divides sides proportionally").scale(0.85).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l6))
        self.wait(3)

        # --- Band 11 (subtopic_4): riders — givens are invitations
        self.next_band(11)
        b11_t = Tex("Riders: givens are invitations").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(2)
        b11_l1 = Tex(r"diameter $\Rightarrow$ $90^\circ$ whispered").scale(0.95).shift(band_shift(11) + UP * 1.2)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = Tex(r"tangent $\Rightarrow$ tan-chord").scale(0.95).shift(band_shift(11) + UP * 0.4)
        self.play(Write(b11_l2))
        self.wait(2)
        b11_l3 = Tex(r"cyclic quad $\Rightarrow$ supplementary").scale(0.95).shift(band_shift(11) + DOWN * 0.4)
        self.play(Write(b11_l3))
        self.wait(2.5)
        b11_l4 = Tex("Similarity: letters in matching order").scale(0.9).shift(band_shift(11) + DOWN * 1.3)
        self.play(Write(b11_l4))
        self.wait(2.5)
        b11_l5 = Tex("Every statement carries its reason").scale(0.95).shift(band_shift(11) + DOWN * 2.3)
        self.play(Write(b11_l5))
        self.play(Create(SurroundingRectangle(b11_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 12 (subtopic_5): the map of Paper Two
        self.next_band(12)
        b12_t = Tex("The map of Paper Two").scale(1.2).shift(band_shift(12) + UP * 2.2)
        self.play(Write(b12_t))
        self.wait(2)
        b12_l1 = MathTex(r"\text{Trig } 50 \quad \text{Analytical } 40").scale(1.0).shift(band_shift(12) + UP * 1.2)
        self.play(Write(b12_l1))
        self.wait(2.5)
        b12_l2 = MathTex(r"\text{Euclidean } 40 \quad \text{Stats } 20 \; = 150").scale(0.9).shift(band_shift(12) + UP * 0.3)
        self.play(Write(b12_l2))
        self.wait(2.5)
        b12_l3 = Tex("Statistics first: the gentlest opening").scale(0.95).shift(band_shift(12) + DOWN * 0.6)
        self.play(Write(b12_l3))
        self.wait(2.5)
        b12_l4 = Tex("No camping on a stubborn proof").scale(0.95).shift(band_shift(12) + DOWN * 1.5)
        self.play(Write(b12_l4))
        self.wait(2.5)
        b12_l5 = Tex("The diagram is the working, not decoration").scale(0.85).shift(band_shift(12) + DOWN * 2.4)
        self.play(Write(b12_l5))
        self.play(Create(SurroundingRectangle(b12_l5, color=GREEN)))
        self.wait(3.5)

        # --- Band 13 (subtopic_6): the formula sheet is half the paper
        self.next_band(13)
        b13_t = Tex("The formula sheet is half the paper").scale(1.1).shift(band_shift(13) + UP * 2.2)
        self.play(Write(b13_t))
        self.wait(2)
        b13_l1 = Tex("Printed: distance, midpoint, gradient, line").scale(0.85).shift(band_shift(13) + UP * 1.3)
        self.play(Write(b13_l1))
        self.wait(2.5)
        b13_l2 = Tex("sine, cosine, area rules; compound angles").scale(0.85).shift(band_shift(13) + UP * 0.5)
        self.play(Write(b13_l2))
        self.wait(2.5)
        b13_l3 = Tex("Memorise: reductions, quadrants, specials").scale(0.85).shift(band_shift(13) + DOWN * 0.3)
        self.play(Write(b13_l3))
        self.wait(2.5)
        b13_l4 = Tex(r"reasons, $\tan\theta = m$, $m_1 m_2 = -1$").scale(0.9).shift(band_shift(13) + DOWN * 1.2)
        self.play(Write(b13_l4))
        self.wait(2.5)
        b13_l5 = Tex("Rehearse the route your eyes will travel").scale(0.9).shift(band_shift(13) + DOWN * 2.2)
        self.play(Write(b13_l5))
        self.wait(3.5)

        # --- Band 14 (subtopic_7): five habits, all of them marks
        self.next_band(14)
        b14_t = Tex("Five habits, all of them marks").scale(1.15).shift(band_shift(14) + UP * 2.2)
        self.play(Write(b14_t))
        self.wait(2)
        b14_l1 = Tex("1. Reason column in memo wording").scale(0.9).shift(band_shift(14) + UP * 1.3)
        self.play(Write(b14_l1))
        self.wait(2.5)
        b14_l2 = Tex("2. Degrees mode checked first").scale(0.9).shift(band_shift(14) + UP * 0.5)
        self.play(Write(b14_l2))
        self.wait(2.5)
        b14_l3 = Tex("3. Exact surds; round only when named").scale(0.9).shift(band_shift(14) + DOWN * 0.3)
        self.play(Write(b14_l3))
        self.wait(2.5)
        b14_l4 = Tex("4. The diagram is a ledger — write on it").scale(0.9).shift(band_shift(14) + DOWN * 1.1)
        self.play(Write(b14_l4))
        self.wait(2.5)
        b14_l5 = Tex("5. General solution first, harvest second").scale(0.9).shift(band_shift(14) + DOWN * 1.9)
        self.play(Write(b14_l5))
        self.wait(2.5)
        b14_l6 = Tex("One check after every answer").scale(0.95).shift(band_shift(14) + DOWN * 2.8)
        self.play(Write(b14_l6))
        self.play(Create(SurroundingRectangle(b14_l6, color=GREEN)))
        self.wait(4)
