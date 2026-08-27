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

# Band layout: one frame-height band per teaching beat; the camera moves down
# to fresh space and earlier work stays on the canvas. Only exporter-supported
# mobjects; every line of working is a single-string MathTex revealed with
# Write — no sub-part transforms.
#
# Mirrors script.md across all seven subtopics (Part 1 — Expert: 1-4;
# Part 2 — Simplifier: 5-7), band time roughly proportional to subtopics.json
# (225/240/225/250/180/180/180 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PrismsAndCylindersSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the single volume law
        title = Tex("Volume and Surface Area: Prisms and Cylinders").scale(1.05).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"V = \text{area of base} \times \text{perpendicular height}").scale(1.05).shift(UP * 0.9)
        self.play(Write(b0_l1))
        self.play(Create(SurroundingRectangle(b0_l1, color=GREEN)))
        self.wait(2.5)
        b0_l2 = MathTex(r"\text{Tea box } 9 \times 4 \times 10: \; V = 36 \times 10 = 360 \text{ cm}^3").scale(1.0).shift(DOWN * 0.1)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = MathTex(r"\text{Tin } r=4, h=15: \; V = \pi(4)^2 \times 15 = 240\pi").scale(1.0).shift(DOWN * 1.1)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = MathTex(r"240\pi = 753{,}98 \text{ cm}^3 \; \text{(exact first, round last)}").scale(0.95).shift(DOWN * 2.1)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_2): the box's net
        self.next_band(1)
        b1_title = Tex("Unfold the box: six faces, three pairs").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = MathTex(r"\text{Top/bottom: } 9 \times 4 = 36 \text{ each}").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"\text{Front/back: } 9 \times 10 = 90, \quad \text{ends: } 4 \times 10 = 40").scale(1.0).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = MathTex(r"SA = 2(36 + 90 + 40) = 2(166) = 332 \text{ cm}^2").scale(1.05).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_l4 = Tex(r"Cubic units fill; square units wrap").scale(1.0).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the tin's net
        self.next_band(2)
        b2_title = Tex("The tin's wall is a rectangle").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"\text{Two circles: } \pi r^2 = 16\pi \text{ each} \to 32\pi").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"\text{Wall: height } 15, \text{ width } 2\pi r = 8\pi").scale(1.0).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"2\pi r h = 8\pi \times 15 = 120\pi").scale(1.05).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"SA = 32\pi + 120\pi = 152\pi = 477{,}52 \text{ cm}^2").scale(1.05).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): triangular prism, volume
        self.next_band(3)
        b3_title = Tex("Triangular prism: legs 5 and 12, length 20").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"\text{Base area} = \tfrac{1}{2} \times 5 \times 12 = 30 \text{ cm}^2").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"V = 30 \times 20 = 600 \text{ cm}^3").scale(1.1).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_w1 = MathTex(r"\text{Base area} = 5 \times 12 = 60").scale(1.0).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_w1))
        self.play(Create(strike(b3_w1)))
        self.wait(1.5)
        b3_l3 = Tex(r"The half is not optional — 60 is the rectangle").scale(0.95).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l3))
        self.wait(3)

        # --- Band 4 (subtopic_3): triangular prism, surface area
        self.next_band(4)
        b4_title = Tex("Surface area by the net").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"\text{Two triangles: } 30 \times 2 = 60").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"\text{Rectangles: } 100 + 240 + 260 = 600").scale(1.0).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"\text{Shortcut: perimeter} \times \text{length} = 30 \times 20 = 600").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = MathTex(r"SA = 60 + 600 = 660 \text{ cm}^2").scale(1.1).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): units, litres, open solids
        self.next_band(5)
        b5_title = Tex("Housekeeping: units, litres, open solids").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"1000 \text{ cm}^3 = 1 \text{ litre}: \; 360 \text{ cm}^3 = 0{,}36 \, \ell").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"0{,}9 \text{ m} = 90 \text{ cm — convert BEFORE multiplying}").scale(0.95).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"\text{No lid: } SA = 16\pi + 120\pi = 136\pi").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex(r"Diameter 8 means $r = 4$ — halve before squaring").scale(0.95).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): the coin stack
        self.next_band(6)
        b6_title = Tex("A stack of identical coins").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"One layer's area $\times$ number of layers").scale(1.05).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"\text{Box: } 36 \times 10 = 360, \quad \text{tin: } 16\pi \times 15 = 240\pi").scale(0.95).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex(r"Strange prism? Find the layer, count the layers").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = Tex(r"The layer is the face that appears twice").scale(1.0).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_6): gift-wrap versus fill
        self.next_band(7)
        b7_title = Tex("Gift-wrap versus fill").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"Panels of the box: $36, 36, 90, 90, 40, 40 \to 332$").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex(r"The wrapper slides off flat: $8\pi \times 15 = 120\pi$").scale(1.0).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"\text{Full wrap: } 152\pi \text{ cm}^2 = 477{,}52 \text{ cm}^2").scale(1.0).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex(r"Did I fill (cm$^3$) or did I wrap (cm$^2$)?").scale(1.0).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4))
        self.wait(3)

        # --- Band 8 (subtopic_7): the five-step checklist
        self.next_band(8)
        b8_title = Tex("The checklist that solves every solid").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"1. Name the repeated face. \; 2. Base area.").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex(r"3. $V =$ base $\times$ height. \; 4. Net for SA.").scale(1.0).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"5. Exact, then rounded, then the right unit").scale(1.0).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = MathTex(r"360 / 332, \quad 240\pi / 152\pi, \quad 600 / 660").scale(1.0).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.wait(4)
