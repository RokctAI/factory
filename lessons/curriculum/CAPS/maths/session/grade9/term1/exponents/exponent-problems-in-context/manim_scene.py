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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex/MathTex keep the export to
# the allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (220/230/230/230/190/190/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ExponentContextsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): growth
        title = Tex("Exponents in Context").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"500 \to 1\,000 \to 2\,000 \to 4\,000 \to \dots").scale(1.0).shift(UP * 1.3)
        l2 = MathTex(r"500 \times 2^6 = 500 \times 64 = 32\,000 \quad (\text{not } 500 \times 2 \times 6)").scale(0.95).shift(UP * 0.3)
        l3 = MathTex(r"3^5 = 243 \qquad 100 \times 3^4 = 8\,100 \qquad 5\,000 \times 1{,}08^3 = 6\,298{,}56").scale(0.85).shift(DOWN * 0.7)
        l4 = MathTex(r"\text{Backwards: } 32\,000 \div 2^6 = 500").scale(1.0).shift(DOWN * 1.7)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l2, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): area, volume, scaling
        self.next_band(1)
        b1_title = Tex("Area, volume and powers").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"15^2 = 225 \text{ m}^2 \qquad (2 \times 10^2)^3 = 8 \times 10^6 \text{ cm}^3").scale(0.95).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"1 \text{ km}^2 = (10^3)^2 = 10^6 \text{ m}^2 \qquad 1 \text{ m}^3 = 10^6 \text{ cm}^3").scale(0.95).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"(2s)^2 = 4s^2 \qquad (2s)^3 = 8s^3 \qquad k \to k^2,\; k^3").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = MathTex(r"2^3 \times 2 \times 10^4 = 16 \times 10^4 = 1{,}6 \times 10^5 \text{ cm}^3").scale(0.95).shift(band_shift(1) + DOWN * 1.8)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): scientific notation problems
        self.next_band(2)
        b2_title = Tex("Fronts and powers separately").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"(3 \times 10^5)(5 \times 10^2) = 15 \times 10^7 = 1{,}5 \times 10^8 \text{ km}").scale(0.95).shift(band_shift(2) + UP * 1.2)
        b2_l2 = MathTex(r"(2{,}5 \times 10^9) \div (5 \times 10^6) = 0{,}5 \times 10^3 = 500 \text{ photos}").scale(0.95).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"(2 \times 10^{12})(1 \times 10^{-12}) = 2 \times 10^0 = 2 \text{ g}").scale(0.95).shift(band_shift(2) + DOWN * 0.8)
        b2_l4 = MathTex(r"(5 \times 10^6)(5 \times 10^6) = 25 \times 10^{12} = 2{,}5 \times 10^{13} \text{ cells}").scale(0.95).shift(band_shift(2) + DOWN * 1.8)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): checks
        self.next_band(3)
        b3_title = Tex("Size, units, small case").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Size: $10^5 \times 10^{2\text{ or }3} \Rightarrow$ exponent 7 or 8").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"3{,}5 \text{ km} = 3{,}5 \times 10^5 \text{ cm} \qquad 0{,}0025 \text{ m} = 2{,}5 \text{ mm}").scale(0.95).shift(band_shift(3) + UP * 0.2)
        b3_l3 = Tex(r"Small case: $500 \times 2n$ at $n=3$ gives 3 000; truth is 4 000").scale(0.95).shift(band_shift(3) + DOWN * 0.8)
        for m in (b3_l1, b3_l2, b3_l3):
            self.play(Write(m))
            self.wait(2.4)
        self.wait(1.5)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"500 \times 2 \times 6 \;\text{for six doublings}").scale(1.0).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"1 \text{ km}^2 = 10^3 \text{ m}^2").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"15 \times 10^7 \;\text{left as the final answer}").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = Tex("Counting hours when the period is 20 minutes").scale(0.95).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.play(Write(b4_l4))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): doubling runs away
        self.next_band(5)
        b5_title = Tex("Doubling is faster than you think").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex(r"R1 000 a day for 30 days: R30 000").scale(1.0).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex(r"1 cent doubled daily: $2^{10} \approx 1\,000$, so $2^{30} \approx$ a billion cents").scale(0.9).shift(band_shift(5) + UP * 0.4)
        b5_l3 = MathTex(r"500,\; 1\,000,\; 2\,000,\; 4\,000,\; 8\,000,\; 16\,000,\; 32\,000").scale(0.9).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex(r"Every, each, per $\Rightarrow$ a power. Backwards $\Rightarrow$ divide.").scale(0.95).shift(band_shift(5) + DOWN * 1.5)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): pizza and boxes
        self.next_band(6)
        b6_title = Tex("Squares, cubes and scaling up").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        small = Square(side_length=0.8, color=BLUE).shift(band_shift(6) + UP * 0.9 + LEFT * 3.0)
        big = Square(side_length=1.6, color=BLUE).shift(band_shift(6) + UP * 0.9 + LEFT * 0.8)
        lab = Tex(r"Twice as wide: 4 times the area").scale(0.9).shift(band_shift(6) + UP * 0.9 + RIGHT * 2.3)
        self.play(Create(small))
        self.play(Create(big))
        self.play(Write(lab))
        self.wait(2)
        b6_l3 = Tex(r"Box with every edge doubled: $2 \times 2 \times 2 = 8$ times the volume").scale(0.9).shift(band_shift(6) + DOWN * 0.6)
        b6_l4 = MathTex(r"1 \text{ km}^2 = 10^6 \text{ m}^2 \qquad 0{,}1 \times 2^{10} \approx 102 \text{ mm}").scale(0.95).shift(band_shift(6) + DOWN * 1.6)
        for m in (b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(1.5)

        # --- Band 7 (subtopic_7): the recipe
        self.next_band(7)
        b7_title = Tex("Four steps for any huge or tiny number").scale(1.1).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        rows = [
            r"\text{1. Standard form with units}",
            r"\text{2. Write the expression}",
            r"\text{3. Fronts and powers on separate lines}",
            r"\text{4. Tidy, then check the size}",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.95).shift(band_shift(7) + UP * (1.3 - 0.75 * i))
            self.play(Write(m))
            self.wait(1.8)
        b7_l5 = MathTex(r"(3 \times 10^5)(5 \times 10^2) = 15 \times 10^7 = 1{,}5 \times 10^8 \text{ km}").scale(0.9).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=YELLOW)))
        self.wait(4)
