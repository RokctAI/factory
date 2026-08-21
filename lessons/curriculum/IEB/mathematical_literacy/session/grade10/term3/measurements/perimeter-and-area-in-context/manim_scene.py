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

# Band-layout whiteboard scene for the Perimeter and Area in Context session
# duo. One band per teaching beat, camera moves down between bands, add-only
# lifecycle. Exporter-supported mobjects only; every working line is a
# single-string Tex/MathTex revealed with Write. Band time apportioned to
# subtopics.json (210/220/240/260/180/190/180 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PerimeterAndAreaInContextSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the plot, perimeter and area ---
        title = Tex("Perimeter and Area in Context").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        plot = Rectangle(width=6.0, height=4.0).shift(DOWN * 0.6 + LEFT * 2.9)
        self.play(Create(plot))
        self.wait(1)
        p_lab = Tex("15 m $\\times$ 10 m").scale(0.9).shift(DOWN * 0.6 + LEFT * 2.9)
        self.play(Write(p_lab))
        self.wait(1.5)
        b0_l1 = MathTex(r"P = 2(15 + 10) = 50 \text{ m}").scale(0.95).shift(UP * 0.6 + RIGHT * 3.4)
        b0_l2 = MathTex(r"A = 15 \times 10 = 150 \text{ m}^2").scale(0.95).shift(DOWN * 0.3 + RIGHT * 3.4)
        self.play(Write(b0_l1))
        self.wait(2.5)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = MathTex(r"\text{Fence: } 50 - 2 \text{ (gate)} = 48 \text{ m}").scale(0.95).shift(DOWN * 1.4 + RIGHT * 3.4)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): edge or inside ---
        self.next_band(1)
        b1_t = Tex("Edge or inside?").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("Fencing, edging, framing: PERIMETER — metres").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("Paving, planting, painting: AREA — square metres").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Say the unit with the number, every time").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the triangle ---
        self.next_band(2)
        b2_t = Tex("The triangular sandpit").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        tri_a = band_shift(2) + DOWN * 1.6 + LEFT * 5.0
        tri_b = band_shift(2) + DOWN * 1.6 + LEFT * 1.0
        tri_c = band_shift(2) + UP * 0.6 + LEFT * 3.6
        t1 = Line(tri_a, tri_b)
        t2 = Line(tri_b, tri_c)
        t3 = Line(tri_c, tri_a)
        h = Line(tri_c, band_shift(2) + DOWN * 1.6 + LEFT * 3.6, color=YELLOW)
        self.play(Create(t1), Create(t2), Create(t3))
        self.play(Create(h))
        self.wait(1.5)
        b2_l1 = MathTex(r"A = \tfrac{1}{2} \times 5 \times 4 = 10 \text{ m}^2").scale(1.0).shift(band_shift(2) + UP * 0.6 + RIGHT * 3.2)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2.5)
        b2_l2 = Tex("Height = the PERPENDICULAR height, not the slant").scale(0.9).shift(band_shift(2) + DOWN * 0.6 + RIGHT * 2.9)
        self.play(Write(b2_l2))
        self.wait(3)

        # --- Band 3 (subtopic_2): the circle formulae ---
        self.next_band(3)
        b3_t = Tex("The round pond, radius 4,5 m").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        pond = Circle(radius=1.5).shift(band_shift(3) + DOWN * 1.4 + LEFT * 4.2)
        self.play(Create(pond))
        self.wait(1)
        b3_l1 = MathTex(r"C = 2 \times 3{,}142 \times 4{,}5 = 28{,}28 \text{ m}").scale(0.95).shift(band_shift(3) + UP * 0.9 + RIGHT * 2.6)
        b3_l2 = MathTex(r"A = 3{,}142 \times 4{,}5^2 = 3{,}142 \times 20{,}25").scale(0.95).shift(band_shift(3) + UP * 0.0 + RIGHT * 2.6)
        b3_l3 = MathTex(r"= 63{,}63 \text{ m}^2").scale(0.95).shift(band_shift(3) + DOWN * 0.9 + RIGHT * 2.6)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.wait(2.5)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = Tex("Square the radius FIRST; halve any diameter").scale(0.9).shift(band_shift(3) + DOWN * 2.0 + RIGHT * 2.6)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): the semicircle trap ---
        self.next_band(4)
        b4_t = Tex("The semicircle trap, radius 3 m").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{Area: } \tfrac{1}{2} \times 3{,}142 \times 3^2 = 14{,}14 \text{ m}^2").scale(0.95).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_wrong = MathTex(r"\text{Perimeter} = \tfrac{1}{2} \times 18{,}852 = 9{,}43 \text{ m}").scale(0.95).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_wrong))
        self.play(Create(strike(b4_wrong)))
        self.wait(2)
        b4_l2 = MathTex(r"\text{Curve } 9{,}426 + \text{diameter } 6 = 15{,}43 \text{ m}").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2)
        b4_l3 = Tex("Quarter: 4,713 + two radii = 10,71 m").scale(0.95).shift(band_shift(4) + DOWN * 1.9)
        b4_l4 = Tex("Area takes the fraction; perimeter adds the cuts").scale(0.95).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_4): pricing the fence ---
        self.next_band(5)
        b5_t = Tex("From metres to money: the fence").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"48 \div 15 = 3{,}2 \text{ rolls}").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("Materials round UP: buy 4 rolls").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"4 \times \text{R}520 = \text{R}2\;080").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_l4 = Tex("3 rolls = 45 m: a hole guarded by hope").scale(0.95).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): pricing the lawn ---
        self.next_band(6)
        b6_t = Tex("Pricing the lawn").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"150 - 10 - 14{,}14 = 125{,}86 \text{ m}^2").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"125{,}86 \div 25 = 5{,}03 \to 6 \text{ bags}").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"6 \times \text{R}150 = \text{R}900").scale(1.05).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_ans = MathTex(r"\text{Project so far: } 2\;080 + 900 = \text{R}2\;980").scale(1.0).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_ans))
        self.play(Create(SurroundingRectangle(b6_ans, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): walking and painting ---
        self.next_band(7)
        b7_t = Tex("Walk the edge, paint the floor").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("The walk: 15 + 10 + 15 + 10 = 50 m").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("The paint: 15 rows of 10 tiles = 150 m$^2$").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("The gate: 2 m of walk with no fence — 48 m to buy").scale(0.95).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): the pizza rule ---
        self.next_band(8)
        b8_t = Tex("Half a pizza still has a straight side").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = MathTex(r"\text{Whole crust: } 2 \times 3{,}142 \times 3 = 18{,}852 \text{ m}").scale(0.95).shift(band_shift(8) + UP * 1.1)
        b8_l2 = MathTex(r"\text{Half crust } 9{,}426 + \text{cut } 6 = 15{,}43 \text{ m}").scale(0.95).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex("Quarter: two cuts — 4,713 + 3 + 3 = 10,71 m").scale(0.95).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("Topping (area) just takes the fraction").scale(0.95).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_7): rolls, not metres ---
        self.next_band(9)
        b9_t = Tex("The shop sells rolls, not metres").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = MathTex(r"48 \div 15 = 3{,}2 \to 4 \text{ rolls} \to \text{R}2\;080").scale(0.95).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"125{,}86 \div 25 = 5{,}03 \to 6 \text{ bags} \to \text{R}900").scale(0.95).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Buy the smallest amount that FINISHES the job").scale(0.95).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex("Measure, divide, round up, price: R2 980").scale(0.95).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4))
        self.wait(4)
