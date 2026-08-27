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

# Band layout: one frame-height band per teaching beat; the camera moves down,
# nothing is removed. Every mobject serializes to the exporter's
# text/line/rect/dot/circle vocabulary; every line of working is a
# single-string Tex/MathTex revealed with Write — no sub-part transforms.
#
# Covers all seven subtopics of the session duo (Part 1 — Expert: subtopics
# 1-4; Part 2 — Simplifier: subtopics 5-7), band time roughly proportional to
# subtopics.json (210/225/225/230/190/195/195 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PerimeterAreaCostsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): perimeter of the yard ---
        title = Tex("Perimeter, Area and Material Costs").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        yard = Rectangle(width=7.0, height=4.5).shift(DOWN * 0.6)
        self.play(Create(yard))
        y_l = Tex("14 m").scale(0.95).shift(UP * 1.9)
        y_b = Tex("9 m").scale(0.95).shift(LEFT * 4.1 + DOWN * 0.6)
        self.play(Write(y_l), Write(y_b))
        self.wait(2)
        p1 = MathTex(r"P = 2 \times (14 + 9) = 46 \text{ m}").scale(1.05).shift(DOWN * 3.2)
        self.play(Write(p1))
        self.play(Create(SurroundingRectangle(p1, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): circumference, and the gate ---
        self.next_band(1)
        b1_title = Tex("The circle, and the gate that is not fence").scale(1.1).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        bed = Circle(radius=1.0).shift(band_shift(1) + LEFT * 3.5 + UP * 0.6)
        self.play(Create(bed))
        b1_l1 = MathTex(r"C = 2 \times 3{,}14 \times 1{,}2 = 7{,}54 \text{ m}").scale(1.0).shift(band_shift(1) + RIGHT * 1.5 + UP * 0.6)
        self.play(Write(b1_l1)); self.wait(2.5)
        b1_l2 = MathTex(r"\text{Fence} = 46 - 2 = 44 \text{ m}").scale(1.05).shift(band_shift(1) + DOWN * 0.6)
        b1_l3 = MathTex(r"44 \times 315 = R13\,860").scale(1.05).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l2)); self.wait(2.5)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_l4 = Tex(r"Fencing all 46 m wastes $2 \times 315 = R630$").scale(0.95).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the three area formulae ---
        self.next_band(2)
        b2_title = Tex("Three area formulae carry the year").scale(1.1).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Rectangle: } 14 \times 9 = 126 \text{ m}^2").scale(1.0).shift(band_shift(2) + UP * 1.3)
        b2_l2 = MathTex(r"\text{Triangle: } \tfrac{1}{2} \times 3 \times 2 = 3 \text{ m}^2").scale(1.0).shift(band_shift(2) + UP * 0.4)
        b2_l3 = MathTex(r"\text{Circle: } 3{,}14 \times 1{,}2^2 = 4{,}52 \text{ m}^2").scale(1.0).shift(band_shift(2) + DOWN * 0.5)
        self.play(Write(b2_l1)); self.wait(2.5)
        self.play(Write(b2_l2)); self.wait(2.5)
        self.play(Write(b2_l3)); self.wait(2.5)
        b2_rule = Tex("Height of a triangle: PERPENDICULAR to the base").scale(0.95).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_rule))
        self.wait(3)

        # --- Band 3 (subtopic_2): composite areas and unit care ---
        self.next_band(3)
        b3_title = Tex("Composite shapes: add or subtract whole areas").scale(1.05).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{Paved} = 126 - 4{,}52 = 121{,}48 \text{ m}^2").scale(1.05).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2.5)
        b3_w = MathTex(r"1 \text{ m}^2 = 100 \text{ cm}^2 \quad \text{(wrong!)}").scale(1.0).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_w))
        self.play(Create(strike(b3_w)))
        self.wait(2)
        b3_l2 = MathTex(r"1 \text{ m}^2 = 100 \times 100 = 10\,000 \text{ cm}^2").scale(1.05).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the wall-area shortcut ---
        self.next_band(4)
        b4_title = Tex("Walls: floor perimeter $\\times$ height").scale(1.1).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        room = Rectangle(width=5.5, height=3.5).shift(band_shift(4) + LEFT * 2.8 + DOWN * 0.4)
        self.play(Create(room))
        b4_l1 = MathTex(r"2 \times (3{,}9 + 3{,}2) = 14{,}2 \text{ m}").scale(1.0).shift(band_shift(4) + RIGHT * 2.8 + UP * 0.4)
        b4_l2 = MathTex(r"14{,}2 \times 2{,}6 = 36{,}92 \text{ m}^2").scale(1.0).shift(band_shift(4) + RIGHT * 2.8 + DOWN * 0.6)
        self.play(Write(b4_l1)); self.wait(2.5)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex("Unroll the four walls: one long rectangle").scale(0.95).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(b4_l3))
        self.wait(3)

        # --- Band 5 (subtopic_3): subtract the openings, apply the coats ---
        self.next_band(5)
        b5_title = Tex("Doors and windows are never painted").scale(1.1).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"\text{Door: } 0{,}8 \times 2{,}0 = 1{,}6 \text{ m}^2; \; \text{window: } 1{,}4 \times 1{,}0 = 1{,}4 \text{ m}^2").scale(0.9).shift(band_shift(5) + UP * 1.3)
        b5_l2 = MathTex(r"36{,}92 - 3{,}0 = 33{,}92 \text{ m}^2").scale(1.05).shift(band_shift(5) + UP * 0.3)
        b5_l3 = MathTex(r"\text{Two coats: } 33{,}92 \times 2 = 67{,}84 \text{ m}^2").scale(1.05).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l1)); self.wait(2.5)
        self.play(Write(b5_l2)); self.wait(2.5)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): paint into tins ---
        self.next_band(6)
        b6_title = Tex("Coverage rate: 7 m$^2$ per litre").scale(1.1).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"67{,}84 \div 7 = 9{,}69 \ \ell").scale(1.05).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"Sold in 5 $\ell$ tins at R560 $\Rightarrow$ two tins").scale(1.0).shift(band_shift(6) + UP * 0.2)
        b6_l3 = MathTex(r"2 \times 560 = R1\,120").scale(1.05).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l1)); self.wait(2.5)
        self.play(Write(b6_l2)); self.wait(2.5)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): tiles with wastage ---
        self.next_band(7)
        b7_title = Tex("Tiles: add 10\\% wastage FIRST").scale(1.1).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"\text{Floor: } 3{,}9 \times 3{,}2 = 12{,}48 \text{ m}^2").scale(1.0).shift(band_shift(7) + UP * 1.3)
        b7_l2 = MathTex(r"12{,}48 \times 1{,}10 = 13{,}73 \text{ m}^2").scale(1.0).shift(band_shift(7) + UP * 0.4)
        b7_l3 = MathTex(r"13{,}73 \div 1{,}2 = 11{,}44 \Rightarrow 12 \text{ boxes}").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = MathTex(r"12 \times 265 = R3\,180").scale(1.05).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(b7_l1)); self.wait(2)
        self.play(Write(b7_l2)); self.wait(2)
        self.play(Write(b7_l3)); self.wait(2)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_4): paving and the honest total ---
        self.next_band(8)
        b8_title = Tex("Paving, and the honest total").scale(1.1).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = MathTex(r"121{,}48 \times 1{,}10 = 133{,}63 \Rightarrow \text{order } 134 \text{ m}^2").scale(0.95).shift(band_shift(8) + UP * 1.3)
        b8_l2 = MathTex(r"134 \times 130 = R17\,420").scale(1.05).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l1)); self.wait(2.5)
        self.play(Write(b8_l2)); self.wait(2.5)
        b8_l3 = Tex(r"Fence 13\,860 $+$ paving 17\,420 $+$ tiles 3\,180 $+$ paint 1\,120").scale(0.85).shift(band_shift(8) + DOWN * 0.7)
        b8_l4 = MathTex(r"\text{Materials total} = R35\,580").scale(1.1).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l3)); self.wait(2.5)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): walking the fence ---
        self.next_band(9)
        b9_title = Tex("Walking the fence").scale(1.15).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = MathTex(r"14 + 9 + 14 + 9 = 46 \text{ m}").scale(1.05).shift(band_shift(9) + UP * 1.3)
        self.play(Write(b9_l1)); self.wait(3)
        b9_l2 = Tex(r"The 2 m gate is NOT fence: $46 - 2 = 44$ m").scale(1.0).shift(band_shift(9) + UP * 0.3)
        b9_l3 = MathTex(r"44 \times 315 = R13\,860").scale(1.05).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l2)); self.wait(3)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(3)
        b9_l4 = Tex("Ask first: what on this line is not being bought?").scale(0.95).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l4))
        self.wait(3.5)

        # --- Band 10 (subtopic_6): covering floor and walls ---
        self.next_band(10)
        b10_title = Tex("Edge or covering?").scale(1.15).shift(band_shift(10) + UP * 2.4)
        self.play(Write(b10_title))
        self.wait(2.5)
        b10_l1 = Tex("Perimeter: the walk around. Area: the covering over.").scale(0.95).shift(band_shift(10) + UP * 1.3)
        self.play(Write(b10_l1)); self.wait(3)
        b10_l2 = MathTex(r"\text{Walls: } 14{,}2 \times 2{,}6 = 36{,}92 \text{ m}^2").scale(1.0).shift(band_shift(10) + UP * 0.3)
        b10_l3 = MathTex(r"36{,}92 - 1{,}6 - 1{,}4 = 33{,}92 \text{ m}^2").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        b10_l4 = MathTex(r"\text{Two coats: } 67{,}84 \text{ m}^2").scale(1.0).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10_l2)); self.wait(3)
        self.play(Write(b10_l3)); self.wait(3)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(3.5)

        # --- Band 11 (subtopic_7): the shop does not sell half a box ---
        self.next_band(11)
        b11_title = Tex("The shop does not sell half a box").scale(1.15).shift(band_shift(11) + UP * 2.4)
        self.play(Write(b11_title))
        self.wait(2.5)
        b11_l1 = MathTex(r"9{,}69 \ \ell \Rightarrow \text{two 5 } \ell \text{ tins} = R1\,120").scale(1.0).shift(band_shift(11) + UP * 1.3)
        self.play(Write(b11_l1)); self.wait(3)
        b11_l2 = MathTex(r"11{,}44 \Rightarrow 12 \text{ boxes} = R3\,180").scale(1.0).shift(band_shift(11) + UP * 0.3)
        self.play(Write(b11_l2)); self.wait(3)
        b11_l3 = MathTex(r"\text{Whole job: } R35\,580 \text{ in materials}").scale(1.05).shift(band_shift(11) + DOWN * 0.7)
        self.play(Write(b11_l3))
        self.play(Create(SurroundingRectangle(b11_l3, color=GREEN)))
        self.wait(3)
        b11_l4 = Tex("Round UP, give the reason, finish in a sentence").scale(0.95).shift(band_shift(11) + DOWN * 1.7)
        self.play(Write(b11_l4))
        self.wait(4)
