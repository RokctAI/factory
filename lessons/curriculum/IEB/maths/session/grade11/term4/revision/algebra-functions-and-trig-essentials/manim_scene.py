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

# Band-layout whiteboard scene (reference: quadratics-by-factorisation).
# One band per teaching beat, add-only lifecycle, camera moves down between
# bands. Covers all seven subtopics: Part 1 Expert (quadratic equations and
# the discriminant, the three function families, trig identities and general
# solutions, trig graphs and triangle rules) then Part 2 Simplifier (delta
# as the warning light, graphs as machines with dials, one circle and the
# final sweep). Band dwell proportional to subtopics.json
# (250/240/235/245/185/185/180 of 1520 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AlgebraFunctionsTrigRevisionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(16)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the three weapons ---
        title = Tex("Algebra, Functions and Trig Essentials").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"x^2 - 7x + 10 = 0 \Rightarrow (x-2)(x-5) = 0").scale(1.05).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = MathTex(r"x = 2 \text{ or } x = 5 \quad \text{(factors visible)}").scale(1.05).shift(UP * 0.1)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = MathTex(r"x^2 - 6x + 1 = 0 \Rightarrow x = \frac{6 \pm \sqrt{32}}{2} = 3 \pm 2\sqrt{2}").scale(1.0).shift(DOWN * 1.0)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2.5)
        b0_l4 = MathTex(r"\text{Same pair by completing: } (x-3)^2 = 8").scale(1.0).shift(DOWN * 2.1)
        self.play(Write(b0_l4))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): delta and the inequality ---
        self.next_band(1)
        b1_title = MathTex(r"\Delta = b^2 - 4ac \text{ runs the show}").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\Delta > 0: \text{two real};\;\; \Delta = 0: \text{one};\;\; \Delta < 0: \text{none}").scale(0.95).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"\Delta = 32 \text{ — positive, not a perfect square: irrational}").scale(0.95).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = MathTex(r"x^2 - 2x - 8 < 0 \Rightarrow (x-4)(x+2) < 0").scale(1.0).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = MathTex(r"-2 < x < 4 \text{ — below the axis, between the roots}").scale(1.0).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 2 (subtopic_1): the surd equation's ghost ---
        self.next_band(2)
        b2_title = MathTex(r"\sqrt{x+3} = x - 3").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"x + 3 = x^2 - 6x + 9 \Rightarrow x^2 - 7x + 6 = 0").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"x = 6 \text{ or } x = 1").scale(1.05).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"\text{Check } x = 6: \sqrt{9} = 3 = 6 - 3 \;\checkmark").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"\text{Check } x = 1: \sqrt{4} = 2 \neq -2 \;\text{— ghost!}").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4))
        self.play(Create(strike(b2_l4)))
        self.wait(2.5)
        b2_l5 = Tex("The check is part of the method").scale(1.0).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l5))
        self.wait(2)

        # --- Band 3 (subtopic_2): the parabola's anatomy ---
        self.next_band(3)
        b3_title = MathTex(r"y = 2(x+1)^2 - 18").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{Turning point } (-1; -18) \text{ — } p \text{ flips, } q \text{ does not}").scale(0.95).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"y\text{-int: } 2(1) - 18 = -16").scale(1.0).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"x\text{-ints: } (x+1)^2 = 9 \Rightarrow x = 2 \text{ or } x = -4").scale(1.0).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("Four anchors, one parabola, full marks").scale(1.0).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_2): hyperbola, exponential, the grammar ---
        self.next_band(4)
        b4_title = Tex("Hyperbola and exponential").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"y = \frac{4}{x+1} - 2: \; x = -1, \; y = -2").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex("The asymptotes ARE the domain and range").scale(0.95).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"y = 4 \cdot 2^x + 2: \; \text{floor } y = 2, \; \text{range } y > 2").scale(1.0).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = MathTex(r"\text{One grammar: } p \text{ flips, } q \text{ honest, } a \text{ stretches}").scale(0.95).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): identities and reduction ---
        self.next_band(5)
        b5_title = Tex("Two identities power everything").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"\tan x = \frac{\sin x}{\cos x}, \quad \sin^2 x + \cos^2 x = 1").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(2.5)
        b5_l2 = MathTex(r"\cos(180^\circ - x) = -\cos x, \;\; \sin(180^\circ + x) = -\sin x").scale(0.9).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"\cos 120^\circ: \text{quadrant 2, ref } 60^\circ \Rightarrow -\tfrac{1}{2}").scale(0.95).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex("Quadrant, sign from CAST, keep the reference").scale(0.95).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.wait(2)

        # --- Band 6 (subtopic_3): general solutions ---
        self.next_band(6)
        b6_title = Tex("General solutions — the circle never stops").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"\cos x = \tfrac{1}{2} \Rightarrow x = \pm 60^\circ + k \cdot 360^\circ").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2.5)
        b6_l2 = MathTex(r"\sin x = \tfrac{\sqrt{3}}{2} \Rightarrow x = 60^\circ \text{ or } 120^\circ, \; + k \cdot 360^\circ").scale(0.95).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"\tan: \text{one family, every } 180^\circ").scale(1.0).shift(band_shift(6) + DOWN * 1.0)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("Restricted interval? Let $k$ run, keep what lands inside").scale(0.9).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l4))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): trig graphs and the sine rule ---
        self.next_band(7)
        b7_title = Tex("Waves and the sine rule").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"y = \cos 3x: \text{ period } \tfrac{360^\circ}{3} = 120^\circ").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"\frac{a}{\sin A} = \frac{b}{\sin B} \text{ — needs a matching pair}").scale(1.0).shift(band_shift(7) + UP * 0.0)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"b = \frac{10 \sin 75^\circ}{\sin 35^\circ} \approx 16{,}84").scale(1.0).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)

        # --- Band 8 (subtopic_4): cosine rule, area rule, the museum ---
        self.next_band(8)
        b8_title = Tex("Cosine rule and area rule").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = MathTex(r"a^2 = 36 + 100 - 120\cos 40^\circ \approx 44{,}07 \Rightarrow a \approx 6{,}64").scale(0.9).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"\text{Area} = \tfrac{1}{2}(6)(10)\sin 40^\circ \approx 19{,}28").scale(0.95).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex("The included angle sits BETWEEN the two sides").scale(0.95).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("Museum: ghost root, unflipped $p$, lost family, wrong angle").scale(0.85).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): delta as the warning light ---
        self.next_band(9)
        b9_title = Tex("Delta as the warning light").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"\Delta > 0: \text{green — two crossings}").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = MathTex(r"\Delta = 0: \text{one dot — the kiss}").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"\Delta < 0: \text{red — floats clear}").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("Attachments: factorise, formula, complete the square").scale(0.95).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("Surd job: check in the ORIGINAL, reject the ghost").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.wait(2.5)

        # --- Band 10 (subtopic_6): machines with dials ---
        self.next_band(10)
        b10_title = Tex("Machines with dials").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"a: \text{stretch/flip} \quad p: \text{slides, label flipped} \quad q: \text{honest}").scale(0.9).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"y = 2(x+1)^2 - 18: \text{ left 1, down 18, doubled}").scale(0.95).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = Tex("Hyperbola: dials move the CROSS; branches follow").scale(0.95).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex("Exponential: $q$ moves the floor; range reads off it").scale(0.95).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("Anchor first, dials second — every family").scale(0.95).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l5))
        self.wait(2.5)

        # --- Band 11 (subtopic_7): one circle, and the final sweep ---
        self.next_band(11)
        b11_title = Tex("One circle, every triangle").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex("Sine is height, cosine is shadow, CAST keeps score").scale(0.95).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = MathTex(r"\cos x = \tfrac{1}{2}: \pm 60^\circ + k \cdot 360^\circ \text{ — the family}").scale(0.95).shift(band_shift(11) + UP * 0.1)
        self.play(Write(b11_l2))
        self.wait(2.5)
        b11_l3 = Tex("Matching pair: sine rule. Gripped angle: cosine rule").scale(0.95).shift(band_shift(11) + DOWN * 0.9)
        self.play(Write(b11_l3))
        self.play(Create(SurroundingRectangle(b11_l3, color=GREEN)))
        self.wait(2.5)
        b11_l4 = Tex("Sweep: check roots, flip $p$, both families, included angle").scale(0.85).shift(band_shift(11) + DOWN * 1.9)
        self.play(Write(b11_l4))
        self.wait(2)
        b11_l5 = Tex("Longer side faces bigger angle — collect the free proof").scale(0.9).shift(band_shift(11) + DOWN * 2.9)
        self.play(Write(b11_l5))
        self.wait(4)
