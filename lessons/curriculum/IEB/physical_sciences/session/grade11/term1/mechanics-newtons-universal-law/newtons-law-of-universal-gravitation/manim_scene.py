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

# Band-layout whiteboard scene for the Universal Gravitation duo.
# Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7.
# Band dwell proportional to subtopics.json (225/215/240/230/180/180/195
# of 1465 s). Exporter-safe mobjects only; add-only lifecycle; camera bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class GravitationUniversalSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the law ---
        title = Tex("Newton's Law of Universal Gravitation").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"F = \frac{G m_1 m_2}{d^2}").scale(1.3).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.play(Create(SurroundingRectangle(b0_l1, color=BLUE)))
        self.wait(2.5)
        b0_l2 = MathTex(r"G = 6{,}67 \times 10^{-11}\ \text{N}\cdot\text{m}^2\cdot\text{kg}^{-2}").scale(0.9).shift(DOWN * 0.3)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("Always attractive; equal and opposite pair;").scale(0.9).shift(DOWN * 1.2)
        b0_l4 = Tex("d runs CENTRE to CENTRE").scale(0.9).shift(DOWN * 1.9)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): the scale of it ---
        self.next_band(1)
        b1_title = Tex("Two learners, 50 kg and 70 kg, 2 m apart").scale(1.0).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"F = \frac{6{,}67 \times 10^{-11} \times 50 \times 70}{2^2}").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = MathTex(r"F \approx 5{,}8 \times 10^{-8}\ \text{N}").scale(1.05).shift(band_shift(1) + UP * 0.0)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("Utterly unfeelable — everyday gravity is tiny").scale(0.95).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("Swap in the Earth: the force becomes 588 N $= mg$").scale(0.95).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l4))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): ratio rules ---
        self.next_band(2)
        b2_title = Tex("Inverse-square ratio questions").scale(1.1).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Double one mass: force $\\times$ 2").scale(0.95).shift(band_shift(2) + UP * 1.3)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex("Double the distance: force $\\div$ 4").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=BLUE)))
        self.wait(2.5)
        b2_l3 = Tex("Quadruple a mass AND double the distance:").scale(0.95).shift(band_shift(2) + DOWN * 0.6)
        b2_l4 = MathTex(r"\times 4 \div 4 = \text{unchanged}").scale(1.0).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.wait(2.5)
        b2_l5 = Tex("Distance changes are ALWAYS squared").scale(0.95).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): the numeric ratio ---
        self.next_band(3)
        b3_l1 = MathTex(r"F = 8 \times 10^{-7}\ \text{N, distance halved}").scale(1.0).shift(band_shift(3) + UP * 1.6)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"F_{new} = 8 \times 10^{-7} \times 4 = 3{,}2 \times 10^{-6}\ \text{N}").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex("Halve the distance: multiply by four, not two").scale(0.95).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): deriving g ---
        self.next_band(4)
        b4_title = Tex("Deriving the surface gravity").scale(1.1).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"mg = \frac{GMm}{r^2} \Rightarrow g = \frac{GM}{r^2}").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=BLUE)))
        self.wait(2.5)
        b4_l2 = Tex("The object's mass cancels:").scale(0.95).shift(band_shift(4) + UP * 0.0)
        b4_l3 = Tex("everything falls alike at a given place").scale(0.95).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l2))
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = MathTex(r"\text{Earth: } g = \frac{6{,}67 \times 10^{-11} \times 5{,}98 \times 10^{24}}{(6{,}38 \times 10^6)^2} = 9{,}8").scale(0.85).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): Venus and altitude ---
        self.next_band(5)
        b5_l1 = MathTex(r"\text{Venus: } g = \frac{6{,}67 \times 10^{-11} \times 4{,}87 \times 10^{24}}{(6{,}05 \times 10^6)^2} = 8{,}87").scale(0.85).shift(band_shift(5) + UP * 1.7)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex("Two Earth radii up = three from the centre:").scale(0.95).shift(band_shift(5) + UP * 0.5)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"g = \frac{9{,}8}{3^2} = 1{,}09\ \text{m}\cdot\text{s}^{-2}").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex("At orbital height g is still almost 9 — remember this").scale(0.9).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l4))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): mass vs weight ---
        self.next_band(6)
        b6_title = Tex("Mass vs weight").scale(1.15).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Mass: kilograms, identical everywhere").scale(0.95).shift(band_shift(6) + UP * 1.3)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex("Weight: $w = mg$, newtons, changes with g").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(VGroup(b6_l1, b6_l2), color=BLUE)))
        self.wait(2.5)
        b6_l3 = MathTex(r"60\ \text{kg: Earth } 588\ \text{N}, \text{ Moon } 97{,}2\ \text{N}, \text{ Venus } 532\ \text{N}").scale(0.85).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex("Three planets, three weights, one mass").scale(0.95).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): true weightlessness ---
        self.next_band(7)
        b7w_title = Tex("True weightlessness").scale(1.15).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7w_title))
        self.wait(2)
        b7w_l1 = Tex("In orbit, gravity is still nearly full strength").scale(0.95).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7w_l1))
        self.wait(2.5)
        b7w_l2 = Tex("The station FALLS around the Earth continuously").scale(0.95).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7w_l2))
        self.wait(2.5)
        b7w_l3 = Tex("Weightlessness: free fall, support gone, gravity on").scale(0.95).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7w_l3))
        self.play(Create(SurroundingRectangle(b7w_l3, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): everything pulls ---
        self.next_band(8)
        b7_title = Tex("Everything pulls on everything").scale(1.15).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(2)
        d1 = Dot(color=YELLOW).shift(band_shift(8) + LEFT * 2.5 + UP * 0.8)
        d2 = Dot(color=YELLOW).shift(band_shift(8) + RIGHT * 2.0 + UP * 1.0)
        d3 = Dot(color=YELLOW).shift(band_shift(8) + LEFT * 0.5 + DOWN * 0.3)
        t12 = DashedLine(d1.get_center(), d2.get_center(), color=BLUE)
        t13 = DashedLine(d1.get_center(), d3.get_center(), color=BLUE)
        t23 = DashedLine(d2.get_center(), d3.get_center(), color=BLUE)
        self.play(Create(d1), Create(d2), Create(d3))
        self.play(Create(t12), Create(t13), Create(t23))
        self.wait(2.5)
        b7_l1 = Tex("A quiet thread between every pair of masses").scale(0.9).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("Noticeable only when a planet joins in").scale(0.9).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b7_l2))
        self.wait(3)

        # --- Band 9 (subtopic_6): torchlight fading ---
        self.next_band(9)
        b8_title = Tex("Double the distance, quarter the pull").scale(1.1).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Torch at double distance: same light, four times the wall").scale(0.85).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Gravity spreads exactly like torchlight").scale(0.95).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = MathTex(r"\times 2\ \text{distance} \Rightarrow \div 4, \quad \times 3 \Rightarrow \div 9").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("Masses are simple: no squaring there").scale(0.95).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 10 (subtopic_7): same you, different weight ---
        self.next_band(10)
        b9_title = Tex("Same you, different weight").scale(1.15).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("A scale is a pull-meter in a mass costume").scale(0.95).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"\text{Earth: } 9{,}8\ \text{N/kg}, \; \text{Moon: } 1{,}62, \; \text{Venus: } 8{,}87").scale(0.9).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Astronauts fall around the planet, floor and all —").scale(0.9).shift(band_shift(10) + DOWN * 0.8)
        b9_l4 = Tex("no push on the feet is the whole floating feeling").scale(0.9).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(VGroup(b9_l3, b9_l4), color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex("Kilograms for what you are; newtons for the pull").scale(0.9).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b9_l5))
        self.wait(4)
