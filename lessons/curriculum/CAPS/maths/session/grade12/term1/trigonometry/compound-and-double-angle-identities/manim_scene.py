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

# Band-layout whiteboard scene (see AUTHORING-SPEC / quadratics-by-factorisation
# worked example). One band per teaching beat, camera moves down, nothing is
# ever removed. Covers all seven subtopics of the session duo:
# Part 1 — Expert (subtopics 1-4), Part 2 — Simplifier (subtopics 5-7),
# band time apportioned to subtopics.json (230/240/250/260/190/200/220 of 1590 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CompoundAndDoubleAngleIdentitiesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(16)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the warning shot
        title = Tex("Compound and Double Angle Identities").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = MathTex(r"\sin(60^\circ + 30^\circ) = \sin 60^\circ + \sin 30^\circ").scale(0.95).shift(UP * 0.9)
        self.play(Write(d1))
        self.play(Create(strike(d1)))
        self.wait(2)
        d2 = MathTex(r"\sin 90^\circ = 1").scale(1.1).shift(DOWN * 0.2)
        self.play(Write(d2))
        self.wait(1.5)
        d3 = MathTex(r"\sin 60^\circ + \sin 30^\circ \approx 0{,}87 + 0{,}5 = 1{,}37").scale(1.0).shift(DOWN * 1.2)
        self.play(Write(d3))
        self.wait(2)
        d4 = Tex("Never distribute a trig function over $+$").scale(1.05).shift(DOWN * 2.3)
        self.play(Write(d4))
        self.wait(3)

        # --- Band 1 (subtopic_1): the four identities
        self.next_band(1)
        b1_title = Tex("The four compound-angle identities").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta").scale(0.85).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"\sin(\alpha - \beta) = \sin\alpha\cos\beta - \cos\alpha\sin\beta").scale(0.85).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta").scale(0.85).shift(band_shift(1) + DOWN * 0.4)
        b1_l4 = MathTex(r"\cos(\alpha - \beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta").scale(0.85).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("Sine mixes and keeps the sign;").scale(1.0).shift(band_shift(1) + DOWN * 2.1)
        b1_l6 = Tex("cosine pairs up and flips it").scale(1.0).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): exact value of cos 15
        self.next_band(2)
        b2_title = Tex(r"Exact value: $\cos 15^\circ = \cos(45^\circ - 30^\circ)$").scale(1.0).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"= \cos 45^\circ \cos 30^\circ + \sin 45^\circ \sin 30^\circ").scale(0.9).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"= \frac{\sqrt{2}}{2} \times \frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2} \times \frac{1}{2}").scale(1.0).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"= \frac{\sqrt{6}}{4} + \frac{\sqrt{2}}{4}").scale(1.05).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"\cos 15^\circ = \frac{\sqrt{6} + \sqrt{2}}{4}").scale(1.1).shift(band_shift(2) + DOWN * 2.3)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): 75 degrees, and running it in reverse
        self.next_band(3)
        b3_title = Tex(r"$\sin 75^\circ$, and reading in reverse").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"= \sin 45^\circ\cos 30^\circ + \cos 45^\circ\sin 30^\circ").scale(0.9).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"= \frac{\sqrt{6} + \sqrt{2}}{4} = \cos 15^\circ").scale(1.0).shift(band_shift(3) + UP * 0.0)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"\sin 40^\circ \cos 10^\circ - \cos 40^\circ \sin 10^\circ").scale(1.0).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"= \sin(40^\circ - 10^\circ) = \sin 30^\circ = \tfrac{1}{2}").scale(1.05).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the double angles, three faces
        self.next_band(4)
        b4_title = Tex(r"Set $\beta = \alpha$: the double angles").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\sin 2\alpha = 2\sin\alpha\cos\alpha").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(2.5)
        b4_l2 = MathTex(r"\cos 2\alpha = \cos^2\alpha - \sin^2\alpha").scale(1.1).shift(band_shift(4) + UP * 0.0)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"= 2\cos^2\alpha - 1").scale(1.1).shift(band_shift(4) + DOWN * 0.9)
        b4_l4 = MathTex(r"= 1 - 2\sin^2\alpha").scale(1.1).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex("Three faces — choosing the right one is the skill").scale(1.0).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): worked case with quadrants
        self.next_band(5)
        b5_title = Tex(r"$\sin\alpha = \tfrac{3}{5}$, $90^\circ < \alpha < 180^\circ$").scale(1.0).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"\cos^2\alpha = 1 - \tfrac{9}{25} = \tfrac{16}{25}").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"\text{Quadrant II: } \cos\alpha = -\tfrac{4}{5}").scale(1.05).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"\sin 2\alpha = 2 \times \tfrac{3}{5} \times (-\tfrac{4}{5}) = -\tfrac{24}{25}").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = MathTex(r"\cos 2\alpha = 1 - 2 \times \tfrac{9}{25} = \tfrac{7}{25}").scale(1.05).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex(r"Check: $2\alpha$ lands in quadrant IV — consistent").scale(1.0).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): proving an identity
        self.next_band(6)
        b6_title = Tex(r"Prove: $\dfrac{1 - \cos 2\alpha}{\sin 2\alpha} = \tan\alpha$").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"\text{Choose the face } \cos 2\alpha = 1 - 2\sin^2\alpha").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"\text{Numerator: } 1 - (1 - 2\sin^2\alpha) = 2\sin^2\alpha").scale(1.0).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l2b = MathTex(r"\text{Denominator: } 2\sin\alpha\cos\alpha").scale(1.0).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l2b))
        self.wait(2)
        b6_l3 = MathTex(r"\text{Divide: } \frac{\sin\alpha}{\cos\alpha} = \tan\alpha").scale(1.05).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = Tex("Pick the face that kills the constant").scale(1.05).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): the equation
        self.next_band(7)
        b7_title = Tex(r"Solve $\cos 2x + \sin x = 0$, $x \in [0^\circ; 360^\circ]$").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"1 - 2\sin^2 x + \sin x = 0").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"2\sin^2 x - \sin x - 1 = 0").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = MathTex(r"(2\sin x + 1)(\sin x - 1) = 0").scale(1.05).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = MathTex(r"\sin x = -\tfrac{1}{2} \quad \text{or} \quad \sin x = 1").scale(1.05).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = MathTex(r"x = 90^\circ;\; 210^\circ;\; 330^\circ").scale(1.1).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): why the shortcut fails
        self.next_band(8)
        b8_title = Tex("Why the shortcut fails").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Angles combine by rotation, not stacked rulers").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("The second tilt starts already tilted —").scale(1.0).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex("part of its effort goes sideways").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = MathTex(r"\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta").scale(0.85).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex("Blend for sine; pair and flip for cosine").scale(1.05).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): making 15 degrees from scratch
        self.next_band(9)
        b9_title = Tex("Making $15^\\circ$ from scratch").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("No fifteen-degree paint in the shop —").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("mix $45^\\circ$ and $30^\\circ$ with the recipe").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"\cos 15^\circ = \frac{\sqrt{6} + \sqrt{2}}{4}").scale(1.1).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("Read recipes backwards too:").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        b9_l5 = MathTex(r"\sin 40^\circ\cos 10^\circ - \cos 40^\circ\sin 10^\circ = \tfrac{1}{2}").scale(0.85).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l4))
        self.wait(1.5)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): one actor, three costumes
        self.next_band(10)
        b10_title = Tex("One angle, folded double").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"\sin 2\alpha = 2\sin\alpha\cos\alpha").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = Tex(r"$\cos 2\alpha$: one actor, three costumes").scale(1.05).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = MathTex(r"\text{Hold } \sin\alpha = \tfrac{3}{5}? \text{ Wear } 1 - 2\sin^2\alpha").scale(0.9).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = MathTex(r"\cos 2\alpha = 1 - \tfrac{18}{25} = \tfrac{7}{25}").scale(1.05).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex("Sign of $\\cos\\alpha$ chosen by quadrant: $-\\tfrac{4}{5}$").scale(1.0).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10_l5))
        self.wait(3)

        # --- Band 11 (subtopic_7): the costume matches the scene
        self.next_band(11)
        b11_title = Tex("Dress the double to match the single").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = MathTex(r"\cos 2x + \sin x = 0: \text{ the other term is sine}").scale(1.0).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = MathTex(r"(2\sin x + 1)(\sin x - 1) = 0").scale(1.05).shift(band_shift(11) + UP * 0.1)
        self.play(Write(b11_l2))
        self.wait(2.5)
        b11_l3 = MathTex(r"x = 90^\circ;\; 210^\circ;\; 330^\circ").scale(1.1).shift(band_shift(11) + DOWN * 0.9)
        self.play(Write(b11_l3))
        self.play(Create(SurroundingRectangle(b11_l3, color=GREEN)))
        self.wait(2.5)
        b11_l4 = Tex("The double never fights the single —").scale(1.0).shift(band_shift(11) + DOWN * 1.9)
        b11_l5 = Tex("it changes costume to join it").scale(1.0).shift(band_shift(11) + DOWN * 2.7)
        self.play(Write(b11_l4))
        self.play(Write(b11_l5))
        self.wait(4)
