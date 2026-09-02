# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from manim import *

# Band-layout whiteboard scene. One band per teaching beat, camera moves down,
# nothing is ever removed. Covers all seven subtopics of the session duo:
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
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the warning shot and the four identities
        title = Tex("Compound and Double Angles").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = MathTex(r"\sin(45^\circ + 45^\circ) \neq \sin 45^\circ + \sin 45^\circ").scale(1.0).shift(UP * 0.9)
        self.play(Write(d1))
        self.play(Create(strike(d1)))
        self.wait(2)
        d2 = MathTex(r"1 \neq 1{,}41").scale(1.05).shift(DOWN * 0.0)
        self.play(Write(d2))
        self.wait(2)
        d3 = MathTex(r"\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta").scale(1.0).shift(DOWN * 1.0)
        self.play(Write(d3))
        self.wait(2)
        d4 = MathTex(r"\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta").scale(1.0).shift(DOWN * 2.0)
        self.play(Write(d4))
        self.play(Create(SurroundingRectangle(d4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_2): exact values
        self.next_band(1)
        b1_title = Tex("Exact values without a calculator").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\sin 15^\circ = \sin(45^\circ - 30^\circ)").scale(1.05).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"= \sin 45^\circ \cos 30^\circ - \cos 45^\circ \sin 30^\circ").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"= \tfrac{\sqrt{6}}{4} - \tfrac{\sqrt{2}}{4} = \frac{\sqrt{6} - \sqrt{2}}{4}").scale(1.05).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_l4 = MathTex(r"\cos 75^\circ \text{ gives the same surd (co-functions)}").scale(0.95).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = MathTex(r"\cos 50^\circ \cos 20^\circ + \sin 50^\circ \sin 20^\circ = \cos 30^\circ = \tfrac{\sqrt{3}}{2}").scale(0.9).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_3): the double angles
        self.next_band(2)
        b2_title = Tex("Fold the compounds: the double angles").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\sin 2\alpha = 2\sin\alpha\cos\alpha").scale(1.1).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"\cos 2\alpha = \cos^2\alpha - \sin^2\alpha").scale(1.05).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"= 2\cos^2\alpha - 1 = 1 - 2\sin^2\alpha").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex("Three faces, one identity — choose by scene").scale(1.0).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_3): the worked quadrant case
        self.next_band(3)
        b3_title = Tex(r"Given $\cos\alpha = -\tfrac{5}{13}$, $90^\circ < \alpha < 180^\circ$").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"\sin^2\alpha = 1 - \tfrac{25}{169} = \tfrac{144}{169}").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"\text{Quadrant 2: } \sin\alpha = +\tfrac{12}{13}").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = MathTex(r"\sin 2\alpha = 2 \cdot \tfrac{12}{13} \cdot \left(-\tfrac{5}{13}\right) = -\tfrac{120}{169}").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"\cos 2\alpha = 2 \cdot \tfrac{25}{169} - 1 = -\tfrac{119}{169}").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("Both negative: $2\\alpha$ in quadrant 3 — consistent").scale(0.95).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_4): proof and equation
        self.next_band(4)
        b4_title = Tex(r"Prove: $\dfrac{\sin 2\alpha}{1 + \cos 2\alpha} = \tan\alpha$").scale(1.0).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"\frac{2\sin\alpha\cos\alpha}{1 + 2\cos^2\alpha - 1} = \frac{2\sin\alpha\cos\alpha}{2\cos^2\alpha} = \tan\alpha").scale(0.95).shift(band_shift(4) + UP * 1.0)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(2.5)
        b4_l2 = MathTex(r"\cos 2x + 3\sin x - 2 = 0").scale(1.05).shift(band_shift(4) + DOWN * 0.1)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"1 - 2\sin^2 x + 3\sin x - 2 = 0 \;\Rightarrow\; 2\sin^2 x - 3\sin x + 1 = 0").scale(0.9).shift(band_shift(4) + DOWN * 1.0)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"(2\sin x - 1)(\sin x - 1) = 0").scale(1.0).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = MathTex(r"x = 30^\circ, \; 90^\circ, \; 150^\circ").scale(1.05).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): why the shortcut fails
        self.next_band(5)
        b5_title = Tex("Why the shortcut fails").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("Tilting a ramp twice does not double the height").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"\sin 90^\circ = 1 \;\text{ but }\; \sin 45^\circ + \sin 45^\circ \approx 1{,}41").scale(0.95).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.play(Create(strike(b5_l2)))
        self.wait(2.5)
        b5_l3 = Tex("Sine MIXES the functions and copies the sign").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex("Cosine PAIRS the functions and flips the sign").scale(1.0).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_6): making 15 degrees from scratch
        self.next_band(6)
        b6_title = Tex("Making 15 degrees from scratch").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("No 15-degree tin — mix 45 and 30").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"\sin 15^\circ = \frac{\sqrt{6} - \sqrt{2}}{4}").scale(1.1).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = Tex("Exact surd earns the marks; 0,26 earns none").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = MathTex(r"\cos 50^\circ \cos 20^\circ + \sin 50^\circ \sin 20^\circ = \cos 30^\circ").scale(0.9).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("Read the recipe backwards too").scale(1.0).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_7): one angle, folded double
        self.next_band(7)
        b7_title = Tex("One angle, folded double").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"\beta = \alpha: \;\; \sin 2\alpha = 2\sin\alpha\cos\alpha").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex("Three costumes for $\\cos 2\\alpha$ — match the scene").scale(1.0).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"\text{Only } \cos\alpha \text{ known: wear } 2\cos^2\alpha - 1").scale(0.95).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = MathTex(r"\text{Sine on stage: wear } 1 - 2\sin^2 x").scale(0.95).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        b7_l5 = Tex("The double never argues — it changes costume").scale(0.95).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l5))
        self.wait(4)
