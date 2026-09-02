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

# Band-layout whiteboard scene: sequential vertical bands, one per teaching
# beat, camera moves down between bands, add-only lifecycle. Exporter-safe
# mobjects only. Two-part revision sweep: subtopics 1-4 (Expert) rebuild the
# territory methods on fresh examples; subtopics 5-7 (Simplifier) give the
# map, the toolkit page, and the five habits. Band dwell times proportional
# to subtopics.json (245/245/255/240/180/180/185 of 1530 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class Paper2EssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(16)

        # --- Band 0 (subtopic_1): mean, sd, five-number summary
        title = Tex("Paper Two Essentials — the revision sweep").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_data = MathTex(r"15;\,42;\,47;\,53;\,57;\,60;\,64;\,69;\,74;\,89").scale(0.95).shift(UP * 1.0)
        self.play(Write(b0_data))
        self.wait(2)
        b0_l1 = MathTex(r"\bar{x} = \frac{570}{10} = 57, \qquad \sigma = 19{,}03").scale(1.05).shift(UP * 0.0)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = MathTex(r"15; \; Q_1 = 47; \; \text{med} = 58{,}5; \; Q_3 = 69; \; 89").scale(0.95).shift(DOWN * 1.1)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the fence acquits 15; regression line
        self.next_band(1)
        b1_t = Tex("The fence rule decides — not the eye").scale(1.05).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_l1 = MathTex(r"\text{IQR} = 22: \; 47 - 1{,}5(22) = 14 < 15").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex(r"$\Rightarrow$ no outlier — 15 is acquitted").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = MathTex(r"\text{Rain vs umbrellas: } \hat{y} = 2{,}07 + 1{,}18x, \; r = 0{,}996").scale(0.85).shift(band_shift(1) + DOWN * 0.9)
        b1_l4 = MathTex(r"x = 22: \hat{y} \approx 28 \; \checkmark \quad x = 60: \text{ extrapolation}").scale(0.85).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l3))
        self.wait(2.5)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the four formulas on AB
        self.next_band(2)
        b2_t = MathTex(r"A(-2;\,7), \; B(4;\,-1)").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = MathTex(r"m = \frac{-1-7}{4+2} = -\frac{4}{3}, \quad M(1;\,3)").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"AB = \sqrt{6^2 + 8^2} = 10").scale(1.05).shift(band_shift(2) + UP * 0.1)
        b2_l3 = MathTex(r"\tan\theta = -\tfrac{4}{3}: \; \theta = 180^\circ - 53{,}13^\circ = 126{,}87^\circ").scale(0.9).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        b2_l4 = Tex("Perpendicular gradient: $\\tfrac{3}{4}$ (product $-1$)").scale(0.9).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): the circle's corridor
        self.next_band(3)
        b3_t = MathTex(r"x^2 + y^2 - 4x + 10y + 4 = 0").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_l1 = MathTex(r"(x-2)^2 + (y+5)^2 = 25").scale(1.1).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"\text{Centre } (2;\,-5), \; r = 5").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = MathTex(r"\text{At } (5;\,-1): \; m_{\text{rad}} = \tfrac{4}{3} \Rightarrow m_{\text{tan}} = -\tfrac{3}{4}").scale(0.95).shift(band_shift(3) + DOWN * 1.0)
        b3_l4 = Tex("Complete the square, read the centre, use $\\perp$").scale(0.9).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_l3))
        self.wait(2.5)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): exact values and double angles
        self.next_band(4)
        b4_t = MathTex(r"\cos 105^\circ = \cos(60^\circ + 45^\circ)").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_l1 = MathTex(r"= \tfrac{1}{2}\cdot\tfrac{\sqrt{2}}{2} - \tfrac{\sqrt{3}}{2}\cdot\tfrac{\sqrt{2}}{2} = \frac{\sqrt{2} - \sqrt{6}}{4}").scale(0.95).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(2.5)
        b4_l2 = Tex("Negative — quadrant two demands it: free check").scale(0.9).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"\cos x = \tfrac{3}{5}: \; \sin 2x = \tfrac{24}{25}, \; \cos 2x = -\tfrac{7}{25}").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the identity and the general solution
        self.next_band(5)
        b5_t = MathTex(r"\frac{\sin 2x}{1 + \cos 2x} = \tan x").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_l1 = MathTex(r"\frac{2\sin x \cos x}{2\cos^2 x} = \frac{\sin x}{\cos x} = \tan x").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        b5_l2 = Tex("Face chosen: $2\\cos^2 x - 1$ — it kills the one").scale(0.9).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"\sin x = \tfrac{1}{2}: \; x = 30^\circ + k\,360^\circ \text{ or } 150^\circ + k\,360^\circ").scale(0.85).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        b5_l4 = Tex("Family first — harvest the interval second").scale(0.9).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_3): triangle rules
        self.next_band(6)
        b6_t = Tex("Triangle rules: match the data to the rule").scale(1.0).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = MathTex(r"\text{Sine rule: } \frac{14 \sin 48^\circ}{\sin 75^\circ} \approx 10{,}77").scale(0.95).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"\text{Cosine rule: } c^2 = 136 - 120\cos 120^\circ = 196 \Rightarrow c = 14").scale(0.9).shift(band_shift(6) + UP * 0.1)
        b6_l3 = MathTex(r"\text{Area} = \tfrac{1}{2}(6)(10)\sin 120^\circ = 15\sqrt{3} \approx 25{,}98").scale(0.9).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("3D: one triangle at a time, carry the shared side").scale(0.9).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): the theorem catalogue with reasons
        self.next_band(7)
        b7_t = Tex("Theorems earn with their reasons").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        o7 = band_shift(7) + UP * 0.3
        circ = Circle(radius=1.5, color=BLUE).move_to(o7)
        centre = Dot(o7, radius=0.05, color=WHITE)
        # central angle 140 degrees vs 70 at circumference
        ra = Line(o7, o7 + RIGHT * 1.5, color=YELLOW, stroke_width=3)
        rb = Line(o7, o7 + LEFT * 1.15 + UP * 0.96, color=YELLOW, stroke_width=3)
        pc = Dot(o7 + DOWN * 1.5, radius=0.06, color=RED)
        ca = Line(o7 + DOWN * 1.5, o7 + RIGHT * 1.5, color=GREEN, stroke_width=2)
        cb = Line(o7 + DOWN * 1.5, o7 + LEFT * 1.15 + UP * 0.96, color=GREEN, stroke_width=2)
        self.play(Create(circ), Create(centre))
        self.play(Create(ra), Create(rb))
        self.play(Create(pc), Create(ca), Create(cb))
        self.wait(2)
        b7_l1 = MathTex(r"140^\circ \text{ at centre} \Rightarrow 70^\circ \text{ at circumference}").scale(0.9).shift(band_shift(7) + DOWN * 1.7)
        b7_l2 = Tex(r"Reason: $\angle$ at centre $= 2 \times \angle$ at circumference").scale(0.85).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_4): rider strategy — the pincer
        self.next_band(8)
        b8_t = Tex("Riders: the pincer, not the lightning bolt").scale(1.0).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Forwards: every given is a theorem invitation").scale(0.9).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("Diameter $\\to 90^\\circ$; tangent $\\to$ tan-chord; cyclic $\\to$ supplementary").scale(0.8).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex("Backwards: list what would prove the target").scale(0.9).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex("The proof is the corridor where the searches meet").scale(0.9).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        b8_l5 = Tex("Similarity: letter order IS the mapping").scale(0.85).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_5): the map — four territories
        self.next_band(9)
        b9_t = Tex("The map: four territories").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        r1 = Rectangle(width=3.4, height=1.2, color=YELLOW).shift(band_shift(9) + LEFT * 1.7 + UP * 0.8)
        r2 = Rectangle(width=2.6, height=1.2, color=BLUE).shift(band_shift(9) + RIGHT * 1.9 + UP * 0.8)
        r3 = Rectangle(width=2.6, height=1.2, color=BLUE).shift(band_shift(9) + LEFT * 1.7 + DOWN * 0.8)
        r4 = Rectangle(width=2.2, height=1.2, color=GREEN).shift(band_shift(9) + RIGHT * 1.9 + DOWN * 0.8)
        t1 = Tex("Trigonometry").scale(0.7).move_to(r1)
        t2 = Tex("Analytical").scale(0.65).move_to(r2)
        t3 = Tex("Euclidean").scale(0.65).move_to(r3)
        t4 = Tex("Statistics").scale(0.6).move_to(r4)
        self.play(Create(r1), Write(t1))
        self.play(Create(r2), Create(r3), Create(r4), Write(t2), Write(t3), Write(t4))
        self.wait(2.5)
        b9_l1 = Tex("Bank statistics early; never camp on a rider").scale(0.85).shift(band_shift(9) + DOWN * 2.0)
        b9_l2 = Tex("Every territory starts with the diagram").scale(0.85).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(3)

        # --- Band 10 (subtopic_6): the toolkit page
        self.next_band(10)
        b10_t = Tex("One page, from memory, every second day").scale(1.0).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        page = Rectangle(width=4.2, height=3.4, color=WHITE).shift(band_shift(10) + DOWN * 0.4)
        self.play(Create(page))
        b10_l1 = Tex("Distance, midpoint, gradient, line, circle").scale(0.7).shift(band_shift(10) + UP * 0.7)
        b10_l2 = Tex("Sine, cosine, area rules").scale(0.7).shift(band_shift(10) + UP * 0.1)
        b10_l3 = Tex("Compound angles; three faces of $\\cos 2A$").scale(0.7).shift(band_shift(10) + DOWN * 0.5)
        b10_l4 = Tex("Reductions, quadrants, special angles, reasons").scale(0.7).shift(band_shift(10) + DOWN * 1.1)
        for m in (b10_l1, b10_l2, b10_l3, b10_l4):
            self.play(Write(m))
            self.wait(1.5)
        b10_l5 = Tex("Retrieval, not recognition").scale(0.9).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_7): the five habits
        self.next_band(11)
        b11_t = Tex("Five habits, none of them mathematics").scale(1.0).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(2)
        b11_l1 = Tex("1. The reason column — accepted wording only").scale(0.8).shift(band_shift(11) + UP * 1.2)
        b11_l2 = Tex("2. Degree mode — check before the trigonometry").scale(0.8).shift(band_shift(11) + UP * 0.5)
        b11_l3 = Tex("3. Exact vs decimal — surds stay surds").scale(0.8).shift(band_shift(11) + DOWN * 0.2)
        b11_l4 = Tex("4. The diagram as ledger — write every find on it").scale(0.8).shift(band_shift(11) + DOWN * 0.9)
        b11_l5 = Tex("5. General solution reflex — family, then harvest").scale(0.8).shift(band_shift(11) + DOWN * 1.6)
        for m in (b11_l1, b11_l2, b11_l3, b11_l4, b11_l5):
            self.play(Write(m))
            self.wait(1.5)
        b11_l6 = Tex("All of them marks").scale(0.95).shift(band_shift(11) + DOWN * 2.6)
        self.play(Write(b11_l6))
        self.play(Create(SurroundingRectangle(b11_l6, color=GREEN)))
        self.wait(4)
