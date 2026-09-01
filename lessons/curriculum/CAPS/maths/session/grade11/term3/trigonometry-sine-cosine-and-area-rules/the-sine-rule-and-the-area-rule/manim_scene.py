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
# bands. Covers all seven subtopics: Part 1 Expert (labelling and the area
# rule, proving and using the sine rule, finding angles, chaining the rules)
# then Part 2 Simplifier (the squashed gate, fair trade at the triangle
# market, planning the route). Band dwell proportional to subtopics.json
# (225/225/225/230/185/195/185 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SineRuleAreaRuleSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the labelling convention + area rule ---
        title = Tex("The Sine Rule and the Area Rule").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        tc = UP * 0.2
        A = tc + LEFT * 2.6 + DOWN * 1.1
        B = tc + RIGHT * 2.6 + DOWN * 1.1
        C = tc + RIGHT * 0.4 + UP * 1.3
        self.play(Create(Line(A, B)), Create(Line(A, C)), Create(Line(B, C)))
        lA = MathTex("A").scale(0.9).move_to(A + LEFT * 0.35)
        lB = MathTex("B").scale(0.9).move_to(B + RIGHT * 0.35)
        lC = MathTex("C").scale(0.9).move_to(C + UP * 0.35)
        la = MathTex("a").scale(0.85).move_to((B + C) / 2 + RIGHT * 0.4)
        lb = MathTex("b").scale(0.85).move_to((A + C) / 2 + LEFT * 0.4)
        lc = MathTex("c").scale(0.85).move_to((A + B) / 2 + DOWN * 0.35)
        self.play(Write(lA), Write(lB), Write(lC))
        self.play(Write(la), Write(lb), Write(lc))
        self.wait(2)
        b0_l1 = Tex("Small $a$ always OPPOSITE capital $A$").scale(1.05).shift(DOWN * 1.8)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = MathTex(r"\text{Area} = \tfrac{1}{2}ab\sin C \;\; (C \text{ included})").scale(1.1).shift(DOWN * 2.8)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): where it comes from + worked example ---
        self.next_band(1)
        b1_title = Tex("Height manufactured: $h = a\\sin C$").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\text{Area} = \tfrac{1}{2} b h = \tfrac{1}{2} a b \sin C").scale(1.1).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = Tex(r"$PQR$: $PQ = 7$, $QR = 9$, $\hat{Q} = 50^\circ$").scale(1.05).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"\text{Area} = \tfrac{1}{2}(7)(9)\sin 50^\circ").scale(1.1).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = MathTex(r"= 31{,}5 \times 0{,}7660 = 24{,}13 \text{ cm}^2").scale(1.1).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)
        b1_l5 = Tex("Square units, always — area lives there").scale(1.0).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l5))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): proving the sine rule ---
        self.next_band(2)
        b2_title = Tex("The sine rule falls out of the area rule").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\tfrac{1}{2}bc\sin A = \tfrac{1}{2}ac\sin B = \tfrac{1}{2}ab\sin C").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"\div \tfrac{1}{2}abc:").scale(1.05).shift(band_shift(2) + UP * 0.2 + LEFT * 3.2)
        self.play(Write(b2_l2))
        self.wait(1.5)
        b2_l3 = MathTex(r"\frac{\sin A}{a} = \frac{\sin B}{b} = \frac{\sin C}{c}").scale(1.15).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex("Upside-down version when a SIDE is unknown").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Needs one complete opposite pair, plus one piece").scale(1.0).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l5))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): using it for a side ---
        self.next_band(3)
        b3_title = Tex(r"$A = 40^\circ$, $B = 65^\circ$, $b = 12$: find $a$").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Complete pair: $b$ with $B$ — unknown on top").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"\frac{a}{\sin A} = \frac{b}{\sin B}").scale(1.1).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"a = \frac{12\sin 40^\circ}{\sin 65^\circ}").scale(1.05).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = MathTex(r"a = 8{,}51 \text{ cm}").scale(1.15).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex("Round only at the final line").scale(1.0).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): finding an angle, the second suspect ---
        self.next_band(4)
        b4_title = Tex(r"$a = 10$, $b = 7$, $A = 42^\circ$: find $B$").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\sin B = \frac{7\sin 42^\circ}{10} = 0{,}4684").scale(1.1).shift(band_shift(4) + UP * 1.0)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"B = 27{,}9^\circ, \text{ then } C = 110{,}1^\circ").scale(1.1).shift(band_shift(4) + UP * 0.0)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex(r"Second suspect: $180^\circ - 27{,}93^\circ = 152{,}07^\circ$").scale(1.0).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = MathTex(r"152{,}07^\circ + 42^\circ > 180^\circ: \text{ rejected}").scale(1.0).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex("Always test the $180^\\circ$-minus partner, in writing").scale(1.0).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): chaining — plan the route ---
        self.next_band(5)
        b5_title = Tex(r"$A = 52^\circ$, $B = 63^\circ$, $c = 15$: find area").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Area rule needs two sides — build one first").scale(1.0).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"C = 180^\circ - 52^\circ - 63^\circ = 65^\circ").scale(1.05).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"a = \frac{15\sin 52^\circ}{\sin 65^\circ} = 13{,}04 \text{ cm}").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = MathTex(r"\text{Area} = \tfrac{1}{2}(13{,}04)(15)\sin 63^\circ").scale(1.05).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = MathTex(r"= 87{,}15 \text{ cm}^2").scale(1.1).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the two disciplines ---
        self.next_band(6)
        b6_title = Tex("The disciplines that carried it").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"The angle sum is a TOOL — pairs for free").scale(1.05).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = Tex(r"$a$ and $c$ meet at $B$ — so $B$ is included").scale(1.05).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Choose the included angle from the SKETCH").scale(1.05).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = Tex("Draw, label fully, and the route announces itself").scale(1.0).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the squashed gate ---
        self.next_band(7)
        b7_title = Tex("The squashed gate").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Two arms, same length — the angle traps the space").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"\sin C \text{ is the squash factor: } \tfrac{1}{2}ab\sin C").scale(1.05).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"90^\circ: \text{max area.} \; 0^\circ, 180^\circ: \text{flat}").scale(0.95).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex("Touch the two sides — take the angle at your fingers").scale(1.0).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): fair trade at the triangle market ---
        self.next_band(8)
        b8_title = Tex("Fair trade at the triangle market").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Bigger angle faces bigger side — one exchange rate").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"\text{Rate fixed by the pair: } \frac{12}{\sin 65^\circ}").scale(1.05).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"a = \sin 40^\circ \times \frac{12}{\sin 65^\circ} = 8{,}51").scale(1.05).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("Hunting a side? Sides on top. An angle? Flip it").scale(1.0).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex(r"Interrogate the $180^\circ$-minus suspect every time").scale(1.0).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_7): planning the route before you drive ---
        self.next_band(9)
        b9_title = Tex("Plan the route before you drive").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Take stock: sides, angles, complete pairs").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("Area rule's ticket: two sides + included angle").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"180^\circ \text{ gave } 65^\circ \to \text{sine rule } 13{,}04").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = MathTex(r"\to \text{area rule closed it: } 87{,}15 \text{ cm}^2").scale(1.05).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex("Say which rule and why — markers pay for the reason").scale(0.95).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l5))
        self.wait(4)
