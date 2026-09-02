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

# Band layout: one frame-height band per teaching beat; the camera moves down
# to fresh space and earlier work stays on the canvas. Only exporter-supported
# mobjects; every line of working is a single-string MathTex revealed with
# Write — no sub-part transforms.
#
# Mirrors script.md across all seven subtopics (Part 1 — Expert: 1-4;
# Part 2 — Simplifier: 5-7), band time roughly proportional to subtopics.json
# (225/215/240/255/190/185/195 of 1505 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class IdentitiesAndReductionFormulaeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): x, y, r definitions and both identities
        title = Tex("Identities and Reduction Formulae").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"\sin\theta = \tfrac{y}{r}, \quad \cos\theta = \tfrac{x}{r}, \quad \tan\theta = \tfrac{y}{x}").scale(1.0).shift(UP * 0.9)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = MathTex(r"\frac{\sin\theta}{\cos\theta} = \frac{y/r}{x/r} = \frac{y}{x} = \tan\theta").scale(0.95).shift(DOWN * 0.2)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = MathTex(r"x^2 + y^2 = r^2 \;\xrightarrow{\div r^2}\; \sin^2\theta + \cos^2\theta = 1").scale(0.95).shift(DOWN * 1.3)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2.5)
        b0_l4 = MathTex(r"\frac{1 - \cos^2\theta}{\sin\theta\cos\theta} = \frac{\sin^2\theta}{\sin\theta\cos\theta} = \tan\theta").scale(0.9).shift(DOWN * 2.5)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_2): the CAST wheel
        self.next_band(1)
        b1_title = Tex("Signs in the four quadrants").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        ax_h = Line(LEFT * 3, RIGHT * 3).shift(band_shift(1) + DOWN * 0.4)
        ax_v = Line(DOWN * 2.2, UP * 1.4).shift(band_shift(1) + DOWN * 0.4)
        self.play(Create(ax_h), Create(ax_v))
        self.wait(1)
        q_a = Tex("A").scale(1.1).shift(band_shift(1) + RIGHT * 1.6 + UP * 0.4)
        q_s = Tex("S").scale(1.1).shift(band_shift(1) + LEFT * 1.6 + UP * 0.4)
        q_t = Tex("T").scale(1.1).shift(band_shift(1) + LEFT * 1.6 + DOWN * 1.3)
        q_c = Tex("C").scale(1.1).shift(band_shift(1) + RIGHT * 1.6 + DOWN * 1.3)
        self.play(Write(q_c))
        self.play(Write(q_a))
        self.play(Write(q_s))
        self.play(Write(q_t))
        self.wait(2)
        b1_l1 = Tex(r"Each letter: the ONLY positive ratio there").scale(0.9).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l1))
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the sketch method
        self.next_band(2)
        b2_title = Tex(r"$\cos\theta = -\tfrac{5}{13}$, \; $180^\circ < \theta < 270^\circ$").scale(1.0).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"\text{Third quadrant: } x = -5, \; r = 13").scale(0.95).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"y^2 = 169 - 25 = 144 \;\Rightarrow\; y = -12 \;\text{(south)}").scale(0.95).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"\sin\theta = -\tfrac{12}{13}, \quad \tan\theta = \tfrac{-12}{-5} = \tfrac{12}{5}").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_l4 = Tex(r"Mark the quadrant BEFORE writing any number").scale(0.9).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_3): the three families
        self.next_band(3)
        b3_title = Tex("Reduction formulae: size from the acute, sign from the quadrant").scale(0.85).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"180^\circ - \theta: \; \sin \to +\sin\theta, \; \cos \to -\cos\theta").scale(0.9).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"180^\circ + \theta: \; \tan \to +\tan\theta, \; \sin,\cos \to -").scale(0.9).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"360^\circ - \theta \text{ and } -\theta: \; \cos \to +\cos\theta, \; \sin,\tan \to -").scale(0.9).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex(r"Full turns of $360^\circ$ change nothing").scale(0.9).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): evaluations without a calculator
        self.next_band(4)
        b4_l1 = MathTex(r"\cos 150^\circ = -\cos 30^\circ = -\tfrac{\sqrt{3}}{2}").scale(1.0).shift(band_shift(4) + UP * 1.9)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"\sin 240^\circ = -\sin 60^\circ = -\tfrac{\sqrt{3}}{2}").scale(1.0).shift(band_shift(4) + UP * 0.9)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"\tan 315^\circ = -\tan 45^\circ = -1").scale(1.0).shift(band_shift(4) + DOWN * 0.1)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = MathTex(r"\cos 120^\circ \times \tan 210^\circ = -\tfrac{1}{2} \times \tfrac{\sqrt{3}}{3} = -\tfrac{\sqrt{3}}{6}").scale(0.95).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): co-functions and the chain
        self.next_band(5)
        b5_l1 = MathTex(r"\sin(90^\circ - \theta) = \cos\theta, \quad \cos(90^\circ - \theta) = \sin\theta").scale(0.9).shift(band_shift(5) + UP * 2.0)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"\sin(90^\circ + \theta) = \cos\theta, \quad \cos(90^\circ + \theta) = -\sin\theta").scale(0.9).shift(band_shift(5) + UP * 1.0)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"\frac{\cos(90^\circ - x)\sin(180^\circ - x)\tan(360^\circ - x)}{\sin(90^\circ + x)\sin(180^\circ + x)}").scale(0.9).shift(band_shift(5) + DOWN * 0.2)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = MathTex(r"= \frac{-\sin^2 x \tan x}{-\sin x \cos x} = \frac{\sin x \tan x}{\cos x} = \tan^2 x").scale(0.9).shift(band_shift(5) + DOWN * 1.5)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the proof with validity
        self.next_band(6)
        b6_title = Tex(r"Prove: $\dfrac{1}{1 - \cos x} + \dfrac{1}{1 + \cos x} = \dfrac{2}{\sin^2 x}$").scale(0.9).shift(band_shift(6) + UP * 2.1)
        self.play(Write(b6_title))
        self.wait(2.5)
        b6_l1 = MathTex(r"\text{LHS} = \frac{(1 + \cos x) + (1 - \cos x)}{(1 - \cos x)(1 + \cos x)}").scale(0.9).shift(band_shift(6) + UP * 0.9)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"= \frac{2}{1 - \cos^2 x} = \frac{2}{\sin^2 x}").scale(0.95).shift(band_shift(6) + DOWN * 0.2)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = Tex(r"Valid for all $x$ except multiples of $180^\circ$").scale(0.9).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l3))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the spoke and the shadow
        self.next_band(7)
        b7_title = Tex("The spoke and the shadow").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        circ = Circle(radius=1.5).shift(band_shift(7) + LEFT * 2.2 + DOWN * 0.4)
        arm = Line(band_shift(7) + LEFT * 2.2 + DOWN * 0.4,
                   band_shift(7) + LEFT * 2.2 + DOWN * 0.4 + 1.5 * (LEFT * 0.87 + DOWN * 0.5),
                   color=YELLOW)
        self.play(Create(circ))
        self.play(Create(arm))
        self.wait(2)
        b7_l1 = Tex(r"At $210^\circ$: both shadows negative").scale(0.9).shift(band_shift(7) + RIGHT * 2.0 + UP * 0.6)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex(r"Sine: north-south. Cosine: east-west.").scale(0.9).shift(band_shift(7) + RIGHT * 2.0 + DOWN * 0.4)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"\text{Arm of length 1: } \sin^2\theta + \cos^2\theta = 1").scale(0.9).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): four neighbourhoods, one rule
        self.next_band(8)
        b8_title = Tex("Four neighbourhoods, one rule").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"C — A — S — T, starting in the fourth").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"\cos\theta = -\tfrac{5}{13}, \; \text{third: } 13^2 - 5^2 = 144").scale(0.9).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"\sin\theta = -\tfrac{12}{13}, \quad \tan\theta = +\tfrac{12}{5}").scale(0.95).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex(r"The sketch IS the calculator — exact, no rounding").scale(0.9).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_7): folding the angle back home
        self.next_band(9)
        b9_title = Tex("Folding the angle back home").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Step 1: home angle. Step 2: neighbourhood sign. Step 3: sign, then size.").scale(0.8).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"\cos 150^\circ = -\cos 30^\circ, \quad \sin 240^\circ = -\sin 60^\circ").scale(0.9).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"\tan 315^\circ = -\tan 45^\circ = -1").scale(0.9).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex(r"$90^\circ$ swaps sine and cosine — swap first, then sign").scale(0.85).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(4)
