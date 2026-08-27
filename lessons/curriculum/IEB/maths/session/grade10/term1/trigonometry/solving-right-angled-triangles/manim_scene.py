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
# to subtopics.json (230/200/230/270/190/185/195 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SolvingRightAngledTrianglesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the ladder, unknown on top
        title = Tex("Solving Right-Angled Triangles").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        tri = Polygon([-3, -2.5, 0], [2, -2.5, 0], [2, 0.6, 0], color=WHITE)
        self.play(Create(tri))
        l01 = Tex(r"Ladder 15 m at $50^\circ$: how high?").scale(0.95).shift(UP * 1.2)
        self.play(Write(l01))
        self.wait(2)
        l02 = MathTex(r"\sin 50^\circ = \frac{h}{15} \;\Rightarrow\; h = 15\sin 50^\circ = 11{,}49 \text{ m}").scale(0.9).shift(DOWN * 3.2)
        self.play(Write(l02))
        self.play(Create(SurroundingRectangle(l02, color=GREEN)))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): unknown underneath
        self.next_band(1)
        b1_title = Tex(r"Guy wire: $\cos 55^\circ = \dfrac{20}{w}$").scale(1.05).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"w = \frac{20}{\cos 55^\circ} = 34{,}87 \text{ m}").scale(1.05).shift(band_shift(1) + UP * 1.0)
        self.play(Write(b1_l1))
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2)
        b1_wrong = MathTex(r"w = 20 \times \cos 55^\circ = 11{,}47 \text{ m}").scale(0.95).shift(band_shift(1) + UP * 0.0)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2)
        b1_l2 = Tex(r"Hypotenuse must beat 20 m — 11,47 is impossible").scale(0.9).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex(r"Unknown on top: multiply. Underneath: divide.").scale(0.95).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=YELLOW)))
        self.wait(2.5)

        # --- Band 2 (subtopic_3): angle + whole triangle
        self.next_band(2)
        b2_title = Tex(r"Ramp: rise 1,2 m, run 4 m").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\tan\theta = \frac{1{,}2}{4} = 0{,}3 \;\Rightarrow\; \theta = \tan^{-1}(0{,}3) = 16{,}70^\circ").scale(0.9).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"\text{Third angle: } 90^\circ - 16{,}70^\circ = 73{,}30^\circ").scale(0.95).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"\text{Pythagoras: } \sqrt{1{,}44 + 16} = 4{,}18 \text{ m}").scale(0.95).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_l4 = Tex(r"Round only at the end — never mid-stream").scale(0.9).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4))
        self.wait(2.5)

        # --- Band 3 (subtopic_4): elevation and depression
        self.next_band(3)
        b3_title = Tex("Elevation and depression — from the horizontal").scale(1.0).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Depression from the top = elevation from the bottom").scale(0.9).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.play(Create(SurroundingRectangle(b3_l1, color=YELLOW)))
        self.wait(2)
        b3_l2 = MathTex(r"\text{Tower: } 30\tan 58^\circ = 48{,}01; \;\; +1{,}5 = 49{,}51 \text{ m}").scale(0.9).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = MathTex(r"\text{Ship: } \frac{60}{\tan 20^\circ} = 164{,}85 \text{ m}").scale(0.95).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = Tex(r"Check the D on the screen; add the eye height back").scale(0.85).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): naming from where you stand
        self.next_band(4)
        b4_title = Tex("Naming the sides from where you stand").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex(r"Hypotenuse: faces the square corner, never renamed").scale(0.9).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex(r"Opposite: faces YOU. Adjacent: runs beside you.").scale(0.9).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex(r"O+H: sine \quad A+H: cosine \quad O+A: tangent").scale(0.95).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=YELLOW)))
        self.wait(2.5)

        # --- Band 5 (subtopic_6): upstairs multiply, downstairs divide
        self.next_band(5)
        b5_title = Tex("Upstairs you multiply, downstairs you divide").scale(1.0).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex(r"One voucher R30 $\to$ twelve: multiply").scale(0.9).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex(r"Twelve cost R360 $\to$ one: divide").scale(0.9).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l1))
        self.wait(1.5)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"h = 15\sin 50^\circ \qquad w = \frac{20}{\cos 55^\circ}").scale(0.95).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_l4 = Tex(r"Then: is the hypotenuse the biggest number here?").scale(0.9).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l4))
        self.wait(2.5)

        # --- Band 6 (subtopic_7): looking up and down
        self.next_band(6)
        b6_title = Tex("Looking up and looking down").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"The level line from your eyes is the reference").scale(0.9).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex(r"Confused by depression? Walk to the bottom, look up").scale(0.9).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=YELLOW)))
        self.wait(2)
        b6_l3 = MathTex(r"49{,}51 \text{ m tower}; \quad 164{,}85 \text{ m to the ship}").scale(0.95).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex(r"Add back the height you stand on — every time").scale(0.9).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4))
        self.wait(4)
