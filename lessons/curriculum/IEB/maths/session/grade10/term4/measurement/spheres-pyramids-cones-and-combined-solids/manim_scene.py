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

# Band layout: one frame-height band per teaching beat; the camera moves down
# to fresh space and earlier work stays on the canvas. Only exporter-supported
# mobjects; every line of working is a single-string MathTex revealed with
# Write — no sub-part transforms.
#
# Mirrors script.md across all seven subtopics (Part 1 — Expert: 1-4;
# Part 2 — Simplifier: 5-7), band time roughly proportional to subtopics.json
# (230/240/230/250/185/185/180 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SpheresPyramidsConesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the one-third family
        title = Tex("Spheres, Pyramids, Cones and Combined Solids").scale(1.0).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"V = \tfrac{1}{3} \times \text{base area} \times h").scale(1.1).shift(UP * 0.9)
        self.play(Write(b0_l1))
        self.play(Create(SurroundingRectangle(b0_l1, color=GREEN)))
        self.wait(2.5)
        b0_l2 = MathTex(r"\text{Pyramid, edge } 12, h = 8: \; \tfrac{1}{3}(144)(8) = 384").scale(0.95).shift(DOWN * 0.1)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = MathTex(r"\text{Cone, } r=5, h=12: \; \tfrac{1}{3}(25\pi)(12) = 100\pi").scale(0.95).shift(DOWN * 1.1)
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_l4 = Tex(r"Three pours of the cone fill the cylinder — exactly").scale(0.9).shift(DOWN * 2.1)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_2): slant height via Pythagoras
        self.next_band(1)
        b1_title = Tex("Manufacture the slant height").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = MathTex(r"s^2 = h^2 + r^2 = 144 + 25 = 169 \Rightarrow s = 13").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2.5)
        b1_l2 = MathTex(r"\text{Cone SA} = \pi r^2 + \pi r s = 25\pi + 65\pi = 90\pi").scale(0.95).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = MathTex(r"\text{Pyramid: } s^2 = 8^2 + 6^2 = 100 \Rightarrow s = 10").scale(0.95).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = MathTex(r"SA = 144 + 4 \times \tfrac{1}{2}(12)(10) = 384").scale(1.0).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_3): the sphere
        self.next_band(2)
        b2_title = Tex("The sphere: cubed fills, squared wraps").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"V = \tfrac{4}{3}\pi r^3, \qquad SA = 4\pi r^2").scale(1.1).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2.5)
        b2_l2 = MathTex(r"r = 3: \; V = \tfrac{4}{3}\pi(27) = 36\pi, \; SA = 4\pi(9) = 36\pi").scale(0.9).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"\text{Closed hemisphere: } 18\pi + 9\pi = 27\pi").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex(r"The cut exposes a NEW circle — surface never halves").scale(0.9).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_4): combined solids
        self.next_band(3)
        b3_title = Tex("The spinning top: cone $+$ hemisphere").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"V = 12\pi + 18\pi = 30\pi \; \text{(volumes just add)}").scale(0.95).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2.5)
        b3_w1 = MathTex(r"SA = SA_{\text{cone}} + SA_{\text{hemi}} \text{ in full}").scale(0.95).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_w1))
        self.play(Create(strike(b3_w1)))
        self.wait(2)
        b3_l2 = Tex(r"The joined circles are buried — strike them out").scale(0.95).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"SA = \pi r s + 2\pi r^2 = 15\pi + 18\pi = 33\pi").scale(1.0).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): party hat, marquee, netball
        self.next_band(4)
        b4_title = Tex("A party hat, a marquee and a netball").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex(r"Pointy solids: base $\times$ height, divided by three").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"\text{Marquee: } \tfrac{1}{3}(144)(8) = 384, \; \text{hat: } \tfrac{1}{3}(25\pi)(12) = 100\pi").scale(0.85).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex(r"Netball: $\tfrac{4}{3}\pi r^3$ fills, $4\pi r^2$ wraps").scale(1.0).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex(r"Cubed fills, squared wraps").scale(1.0).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_6): the grain silo
        self.next_band(5)
        b5_title = Tex("Raising the grain silo").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"\text{Grain: } 12\pi + 2\pi = 14\pi \text{ m}^3").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(2.5)
        b5_l2 = MathTex(r"\text{Roof slant: } s = \sqrt{1{,}5^2 + 2^2} = 2{,}5").scale(1.0).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"\text{Paint } 2\pi(2)(3) = 12\pi, \; \text{sheeting } \pi(2)(2{,}5) = 5\pi").scale(0.9).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex(r"The ceiling circles are buried — never billed").scale(0.95).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_7): the four traps
        self.next_band(6)
        b6_title = Tex("Four traps to sidestep").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"1. Inside height fills; slope height wraps").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = Tex(r"2. A cut sphere grows a new flat circle").scale(1.0).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex(r"3. Buried faces leave the surface bill").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex(r"4. Never drop the one third").scale(1.0).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(4)
