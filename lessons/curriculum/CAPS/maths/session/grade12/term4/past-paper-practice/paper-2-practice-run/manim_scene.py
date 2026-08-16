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
# (text/line/rect/dot/circle via Tex/MathTex/Line/Dot/Circle/
# SurroundingRectangle) — no sub-part Transform tricks, which leak raw glyph
# primitives through the exporter's Tex shim.
#
# The scene mirrors script.md's seven exam questions (subtopics 1-7 of the
# practice run), with band dwell times proportional to subtopics.json
# (235/210/245/245/255/220/270 of 1680 s). Level 6 rescales primitive times
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


class Paper2PracticeRunSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Opening intro beat: the player shows the TOPIC full-screen while the
        # tutor speaks intro.md; board work must not start until it lands.
        self.wait(16)

        # --- Band 0 (subtopic_1): Q1 — mean and standard deviation
        title = Tex("Paper 2 Practice Run").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_q = Tex("Q1 — ten marks:").scale(1.1).shift(UP * 1.2)
        self.play(Write(b0_q))
        b0_data = MathTex(r"12;\,45;\,52;\,58;\,61;\,64;\,68;\,72;\,75;\,94").scale(1.0).shift(UP * 0.4)
        self.play(Write(b0_data))
        self.wait(2)
        b0_mean = MathTex(r"\bar{x} = \frac{601}{10} = 60{,}1").scale(1.15).shift(DOWN * 0.7)
        self.play(Write(b0_mean))
        self.wait(2.5)
        b0_sd = MathTex(r"\sigma = 20{,}5 \;\; \text{(calculator stats mode)}").scale(1.1).shift(DOWN * 1.9)
        self.play(Write(b0_sd))
        self.wait(3)

        # --- Band 1 (subtopic_1): five-number summary + box and whisker
        self.next_band(1)
        b1_title = Tex("Five-number summary and the box").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_sum = MathTex(r"12; \; Q_1 = 52; \; 62{,}5; \; Q_3 = 72; \; 94").scale(0.9).shift(band_shift(1) + UP * 1.3)
        self.play(Write(b1_sum))
        self.wait(2.5)
        # Box-and-whisker drawn from primitives: values 12..94 mapped onto
        # x in [-3, 3] locally (x = (v - 12) / 82 * 6 - 3).
        cy = 0.1

        def bx(v):
            return (v - 12.0) / 82.0 * 6.0 - 3.0

        axis = Line(band_shift(1) + RIGHT * -3.3 + UP * (cy - 0.8),
                    band_shift(1) + RIGHT * 3.3 + UP * (cy - 0.8))
        box = Rectangle(width=bx(72) - bx(52), height=0.8).move_to(
            band_shift(1) + RIGHT * ((bx(52) + bx(72)) / 2) + UP * cy)
        med = Line(band_shift(1) + RIGHT * bx(62.5) + UP * (cy - 0.4),
                   band_shift(1) + RIGHT * bx(62.5) + UP * (cy + 0.4))
        wl = Line(band_shift(1) + RIGHT * bx(12) + UP * cy,
                  band_shift(1) + RIGHT * bx(52) + UP * cy)
        wr = Line(band_shift(1) + RIGHT * bx(72) + UP * cy,
                  band_shift(1) + RIGHT * bx(94) + UP * cy)
        lab_min = MathTex(r"12").scale(0.8).move_to(band_shift(1) + RIGHT * bx(12) + UP * (cy - 1.2))
        lab_q1 = MathTex(r"52").scale(0.8).move_to(band_shift(1) + RIGHT * bx(52) + UP * (cy - 1.2))
        lab_q3 = MathTex(r"72").scale(0.8).move_to(band_shift(1) + RIGHT * bx(72) + UP * (cy - 1.2))
        lab_max = MathTex(r"94").scale(0.8).move_to(band_shift(1) + RIGHT * bx(94) + UP * (cy - 1.2))
        self.play(Create(axis))
        self.play(Create(box), Create(med))
        self.play(Create(wl), Create(wr))
        self.play(Write(lab_min), Write(lab_q1), Write(lab_q3), Write(lab_max))
        self.wait(3)

        # --- Band 2 (subtopic_1): the outlier fence and the 1-sigma count
        self.next_band(2)
        b2_title = Tex("Outlier? The fence decides, not the eye").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"IQR = 72 - 52 = 20").scale(1.1).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"\text{fence} = 52 - 1{,}5 \times 20 = 22").scale(1.1).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"12 < 22 \;\Rightarrow\; 12 \text{ is an outlier}").scale(1.1).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = MathTex(r"\bar{x} \pm \sigma: \; 39{,}6 \text{ to } 80{,}6").scale(1.1).shift(band_shift(2) + DOWN * 1.8)
        b2_l5 = Tex(r"Count the ordered list: 8 of the 10 marks").scale(1.05).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l4))
        self.wait(2)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): Q2 — regression and the fenced prediction
        self.next_band(3)
        b3_title = Tex("Q2 — temperature vs cans sold (6 pairs)").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"\hat{y} = -5{,}43 + 1{,}15x").scale(1.15).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"r = 0{,}999: \text{ very strong, positive}").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"x = 25: \;\; -5{,}43 + 1{,}15(25) \approx 23 \text{ cans}").scale(1.05).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex(r"$x = 40$? Outside 15--30: extrapolation").scale(1.05).shift(band_shift(3) + DOWN * 1.8)
        b3_l5 = Tex(r"and no straight line survives extreme heat").scale(1.0).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): Q3 — the right angle at B
        self.next_band(4)
        b4_title = Tex(r"Q3 — $A(-2;5)$, $B(6;1)$, $C(4;-3)$").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"m_{AB} = \frac{1 - 5}{6 - (-2)} = \frac{-4}{8} = -\tfrac{1}{2}").scale(1.05).shift(band_shift(4) + UP * 1.0)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"m_{BC} = \frac{-3 - 1}{4 - 6} = \frac{-4}{-2} = 2").scale(1.05).shift(band_shift(4) + DOWN * 0.3)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"m_{AB} \times m_{BC} = -\tfrac{1}{2} \times 2 = -1").scale(1.05).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"AB \perp BC \;\Rightarrow\; \hat{B} = 90^\circ").scale(1.1).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): length, midpoint, inclination
        self.next_band(5)
        b5_l1 = MathTex(r"AB = \sqrt{8^2 + 4^2} = \sqrt{80} = 4\sqrt{5}").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"M \text{ of } AC = (1; 1)").scale(1.1).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex(r"$\hat{B} = 90^\circ$, so $AC$ is a diameter").scale(1.05).shift(band_shift(5) + UP * 0.3)
        b5_l4 = Tex(r"$M$ is the centre: equidistant from $A$, $B$, $C$").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = MathTex(r"\tan\theta = -\tfrac{1}{2}: \;\; -26{,}57^\circ + 180^\circ").scale(1.05).shift(band_shift(5) + DOWN * 1.6)
        b5_l6 = MathTex(r"\theta = 153{,}43^\circ").scale(1.1).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l5))
        self.wait(2.5)
        self.play(Write(b5_l6))
        self.play(Create(SurroundingRectangle(b5_l6, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): Q4 — centre and radius, point on circle
        self.next_band(6)
        b6_title = Tex(r"Q4 — $x^2 + y^2 - 6x + 4y - 12 = 0$").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"x^2 - 6x + 9 + y^2 + 4y + 4 = 12 + 9 + 4").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"(x - 3)^2 + (y + 2)^2 = 25").scale(1.1).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"\text{centre } (3; -2), \quad r = 5").scale(1.1).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = MathTex(r"(7;1): \; 4^2 + 3^2 = 25 \;\checkmark \text{ on circle}").scale(1.05).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): the tangent and the external point
        self.next_band(7)
        b7_title = Tex(r"Tangent at $(7;1)$ — perpendicular to radius").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"m_{r} = \frac{1 - (-2)}{7 - 3} = \tfrac{3}{4} \;\Rightarrow\; m_{t} = -\tfrac{4}{3}").scale(0.85).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"y - 1 = -\tfrac{4}{3}(x - 7)").scale(1.1).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = MathTex(r"y = -\tfrac{4}{3}x + \tfrac{31}{3}").scale(1.1).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = MathTex(r"(9;8): \; d^2 = 6^2 + 10^2 = 136").scale(1.05).shift(band_shift(7) + DOWN * 1.7)
        b7_l5 = MathTex(r"\ell = \sqrt{136 - 25} = \sqrt{111} \approx 10{,}54").scale(1.05).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l4))
        self.wait(2.5)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_5): Q5 — cos 75 degrees, exactly
        self.next_band(8)
        b8_title = Tex(r"Q5 — $\cos 75^\circ$ without a calculator").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = MathTex(r"\cos(45^\circ + 30^\circ)").scale(1.1).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"= \cos 45^\circ \cos 30^\circ - \sin 45^\circ \sin 30^\circ").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"= \frac{\sqrt{2}}{2} \cdot \frac{\sqrt{3}}{2} - \frac{\sqrt{2}}{2} \cdot \frac{1}{2}").scale(0.88).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = MathTex(r"= \frac{\sqrt{6} - \sqrt{2}}{4}").scale(1.15).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_5): the identity — choose the right face
        self.next_band(9)
        b9_title = Tex(r"Prove: $\dfrac{\sin 2x}{1 - \cos 2x} = \dfrac{\cos x}{\sin x}$").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"\sin 2x = 2\sin x \cos x").scale(1.05).shift(band_shift(9) + UP * 1.0)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = MathTex(r"\cos 2x = 1 - 2\sin^2 x \text{ (kills the 1)}").scale(1.05).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"1 - \cos 2x = 2\sin^2 x").scale(1.05).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = MathTex(r"\frac{2\sin x \cos x}{2\sin^2 x} = \frac{\cos x}{\sin x} \;\checkmark").scale(0.88).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_5): general solution and the 3-4-5 doubles
        self.next_band(10)
        b10_title = Tex(r"$\cos x = -\tfrac{1}{2}$: reference angle $60^\circ$").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"cosine negative in quadrants II and III").scale(1.05).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = MathTex(r"x = \pm 120^\circ + k \cdot 360^\circ, \; k \in \mathbb{Z}").scale(0.92).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = MathTex(r"\sin x = \tfrac{3}{5}, \; x \text{ acute} \Rightarrow \cos x = \tfrac{4}{5}").scale(0.85).shift(band_shift(10) + DOWN * 0.9)
        b10_l4 = MathTex(r"\sin 2x = 2 \cdot \tfrac{3}{5} \cdot \tfrac{4}{5} = \tfrac{24}{25}").scale(1.05).shift(band_shift(10) + DOWN * 1.8)
        b10_l5 = MathTex(r"\cos 2x = \tfrac{16}{25} - \tfrac{9}{25} = \tfrac{7}{25}").scale(1.05).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l3))
        self.wait(2.5)
        self.play(Write(b10_l4))
        self.wait(2)
        self.play(Write(b10_l5))
        self.wait(3)

        # --- Band 11 (subtopic_6): Q6 — sine rule, cosine rule, area rule
        self.next_band(11)
        b11_title = Tex(r"Q6 — $p = 12$, $\hat{P} = 64^\circ$, $\hat{Q} = 52^\circ$").scale(1.1).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = MathTex(r"\frac{q}{\sin Q} = \frac{p}{\sin P}").scale(1.05).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11_l1))
        self.wait(2)
        b11_l2 = MathTex(r"q = \frac{12\sin 52^\circ}{\sin 64^\circ} \approx 10{,}52").scale(1.05).shift(band_shift(11) + UP * 0.0)
        self.play(Write(b11_l2))
        self.play(Create(SurroundingRectangle(b11_l2, color=GREEN)))
        self.wait(2.5)
        b11_l3 = MathTex(r"x^2 = 49 + 81 - 2(7)(9)\cos 60^\circ = 67").scale(1.0).shift(band_shift(11) + DOWN * 1.1)
        b11_l4 = MathTex(r"x = \sqrt{67} \approx 8{,}19").scale(1.05).shift(band_shift(11) + DOWN * 2.0)
        self.play(Write(b11_l3))
        self.wait(2.5)
        self.play(Write(b11_l4))
        self.wait(3)

        # --- Band 12 (subtopic_6): area rule and the tower
        self.next_band(12)
        b12_l1 = MathTex(r"\text{Area} = \tfrac{1}{2}(7)(9)\sin 60^\circ \approx 27{,}28").scale(1.05).shift(band_shift(12) + UP * 2.2)
        self.play(Write(b12_l1))
        self.wait(2.5)
        b12_title = Tex(r"The tower: one right triangle with tan").scale(1.1).shift(band_shift(12) + UP * 1.1)
        self.play(Write(b12_title))
        self.wait(1.5)
        # Right-triangle sketch: ground, tower, line of sight
        base_l = band_shift(12) + LEFT * 2.5 + DOWN * 1.0
        base_r = band_shift(12) + RIGHT * 1.5 + DOWN * 1.0
        top = band_shift(12) + RIGHT * 1.5 + UP * 0.4
        ground = Line(base_l, base_r)
        tower = Line(base_r, top)
        sight = Line(base_l, top)
        lab_45 = MathTex(r"45\text{ m}").scale(0.85).move_to(band_shift(12) + LEFT * 0.5 + DOWN * 1.4)
        lab_38 = MathTex(r"38^\circ").scale(0.85).move_to(band_shift(12) + LEFT * 1.5 + DOWN * 0.65)
        lab_h = MathTex(r"h").scale(0.9).move_to(band_shift(12) + RIGHT * 1.9 + DOWN * 0.3)
        self.play(Create(ground))
        self.play(Create(tower))
        self.play(Create(sight))
        self.play(Write(lab_45), Write(lab_38), Write(lab_h))
        self.wait(2.5)
        b12_l2 = MathTex(r"h = 45\tan 38^\circ \approx 35{,}16 \text{ m}").scale(1.1).shift(band_shift(12) + DOWN * 2.4)
        self.play(Write(b12_l2))
        self.play(Create(SurroundingRectangle(b12_l2, color=GREEN)))
        self.wait(3)

        # --- Band 13 (subtopic_7): Q7 — the tan-chord rider
        self.next_band(13)
        b13_title = Tex(r"Q7 — tangent $SAT$, $T\hat{A}B = 40^\circ$, $S\hat{A}C = 65^\circ$").scale(0.88).shift(band_shift(13) + UP * 2.2)
        self.play(Write(b13_title))
        self.wait(2)
        # Rider sketch: circle, tangent at A (bottom), chords AB and AC
        cc = band_shift(13) + UP * 0.5 + LEFT * 1.8
        circ = Circle(radius=1.1).move_to(cc)
        a_pt = cc + DOWN * 1.1
        b_pt = cc + UP * 1.1 * 0.64 + LEFT * 1.1 * 0.77
        c_pt = cc + UP * 1.1 * 0.77 + RIGHT * 1.1 * 0.64
        tangent = Line(a_pt + LEFT * 1.6, a_pt + RIGHT * 1.6)
        chord_ab = Line(a_pt, b_pt)
        chord_ac = Line(a_pt, c_pt)
        d_a = Dot(a_pt, radius=0.06)
        d_b = Dot(b_pt, radius=0.06)
        d_c = Dot(c_pt, radius=0.06)
        lab_a = MathTex(r"A").scale(0.8).move_to(a_pt + DOWN * 0.35)
        lab_b = MathTex(r"B").scale(0.8).move_to(b_pt + UP * 0.25 + LEFT * 0.25)
        lab_c = MathTex(r"C").scale(0.8).move_to(c_pt + UP * 0.25 + RIGHT * 0.25)
        self.play(Create(circ))
        self.play(Create(tangent))
        self.play(Create(chord_ab), Create(chord_ac))
        self.play(Create(d_a), Create(d_b), Create(d_c))
        self.play(Write(lab_a), Write(lab_b), Write(lab_c))
        self.wait(2.5)
        b13_l1 = MathTex(r"A\hat{C}B = 40^\circ \; \text{(tan chord)}").scale(1.0).shift(band_shift(13) + RIGHT * 2.3 + UP * 1.0)
        b13_l2 = MathTex(r"A\hat{B}C = 65^\circ \; \text{(tan chord)}").scale(1.0).shift(band_shift(13) + RIGHT * 2.3 + UP * 0.0)
        self.play(Write(b13_l1))
        self.wait(2.5)
        self.play(Write(b13_l2))
        self.wait(2.5)
        b13_l3 = MathTex(r"B\hat{A}C = 180^\circ - 40^\circ - 65^\circ = 75^\circ").scale(1.05).shift(band_shift(13) + DOWN * 1.6)
        self.play(Write(b13_l3))
        self.play(Create(SurroundingRectangle(b13_l3, color=GREEN)))
        b13_l4 = Tex(r"Check: $75 + 40 + 65 = 180$ exactly").scale(1.0).shift(band_shift(13) + DOWN * 2.6)
        self.play(Write(b13_l4))
        self.wait(3)

        # --- Band 14 (subtopic_7): the examinable tan-chord proof
        self.next_band(14)
        b14_title = Tex("The proof — a rehearsed performance").scale(1.15).shift(band_shift(14) + UP * 2.2)
        self.play(Write(b14_title))
        self.wait(1.5)
        b14_l1 = Tex(r"Construction: diameter $AOD$; join $DB$").scale(1.05).shift(band_shift(14) + UP * 1.2)
        self.play(Write(b14_l1))
        self.wait(2.5)
        b14_l2 = MathTex(r"D\hat{A}T = 90^\circ \; \text{(tangent} \perp \text{radius)}").scale(1.0).shift(band_shift(14) + UP * 0.3)
        self.play(Write(b14_l2))
        self.wait(2.5)
        b14_l3 = MathTex(r"A\hat{B}D = 90^\circ \; \text{(angle in semicircle)}").scale(1.0).shift(band_shift(14) + DOWN * 0.6)
        self.play(Write(b14_l3))
        self.wait(2.5)
        b14_l4 = MathTex(r"T\hat{A}B = 90^\circ - D\hat{A}B = A\hat{D}B").scale(1.0).shift(band_shift(14) + DOWN * 1.5)
        self.play(Write(b14_l4))
        self.wait(2.5)
        b14_l5 = MathTex(r"A\hat{D}B = A\hat{C}B \; \text{(same segment)} \;\checkmark").scale(1.0).shift(band_shift(14) + DOWN * 2.5)
        self.play(Write(b14_l5))
        self.play(Create(SurroundingRectangle(b14_l5, color=GREEN)))
        self.wait(4)
