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

# Band-layout whiteboard scene for the session duo "Cyclic Quadrilaterals and
# Tangents" (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics
# 5-7). One band per teaching beat, add-only lifecycle, camera moves down.
# Only exporter-supported mobjects; write-only reveals, no sub-part
# transforms. Band dwell times follow subtopics.json
# (235/225/240/265/190/195/205 of 1555 s); Level 6 rescales to real audio.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CyclicQuadrilateralsTangentsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: player holds the topic full-screen while intro.md plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the theorem and its proof
        title = Tex("Cyclic Quadrilaterals and Tangents").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        d1 = Tex("Cyclic quad: all four vertices on one circle").scale(1.05).shift(UP * 1.0)
        self.play(Write(d1))
        self.wait(2)
        d2 = MathTex(r"\hat{B} + \hat{D} = 180^\circ, \; \hat{A} + \hat{C} = 180^\circ").scale(1.0).shift(UP * 0.1)
        self.play(Write(d2))
        self.play(Create(SurroundingRectangle(d2, color=GREEN)))
        self.wait(2.5)
        d3 = Tex(r"Proof: $\hat{B}$ stands on arc $ADC$, $\hat{D}$ on arc $ABC$").scale(0.95).shift(DOWN * 1.0)
        d4 = MathTex(r"2\hat{B} + 2\hat{D} = 360^\circ; \; \hat{B} + \hat{D} = 180^\circ").scale(0.9).shift(DOWN * 1.9)
        self.play(Write(d3))
        self.wait(2.5)
        self.play(Write(d4))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): using it, and the exterior angle
        self.next_band(1)
        b1_title = Tex("Supplementary pairs, and the exterior angle").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\hat{A} = 95^\circ \Rightarrow \hat{C} = 85^\circ").scale(1.05).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2.5)
        b1_l2 = Tex(r"Extend $DC$ to $E$: $\hat{BCE} = 180^\circ - \hat{BCD}$").scale(1.0).shift(band_shift(1) + UP * 0.1)
        b1_l3 = MathTex(r"\hat{BCE} = \hat{A} \;\text{(ext. angle of cyclic quad)}").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l2))
        self.wait(2.5)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_l4 = Tex("Check all four corners sit ON the circle, in order").scale(0.95).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l4))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the three converse tests
        self.next_band(2)
        b2_title = Tex("Proving a quadrilateral is cyclic").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"Test 1: one opposite pair adds to $180^\circ$").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("(one pair suffices — the other follows from $360^\\circ$)").scale(0.9).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("Test 2: exterior angle $=$ interior opposite angle").scale(1.0).shift(band_shift(2) + DOWN * 0.5)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("Test 3: equal angles from the same side of a segment").scale(1.0).shift(band_shift(2) + DOWN * 1.4)
        b2_l5 = Tex("(converse of angles in the same segment)").scale(0.9).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2_l4))
        self.wait(2)
        self.play(Write(b2_l5))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): choosing the test
        self.next_band(3)
        b3_title = Tex("Match the test to the given information").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Angles adding towards $180^\circ$ $\to$ test 1").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex(r"An extended side $\to$ test 2").scale(1.0).shift(band_shift(3) + UP * 0.2)
        b3_l3 = Tex(r"Same base, equal apex angles, same side $\to$ test 3").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex(r"Write it: ``$ABCD$ cyclic (conv. opp. angles suppl.)''").scale(0.95).shift(band_shift(3) + DOWN * 1.7)
        b3_l5 = Tex("Part (a) proves the circle; part (b) spends it").scale(1.0).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l4))
        self.wait(2.5)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): tangent perpendicular to radius
        self.next_band(4)
        b4_title = Tex("Tangent $\\perp$ radius at the point of contact").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Axiom in CAPS — no proof, but always quote it").scale(1.0).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex(r"$P$ is 13 from centre $O$, radius 5, tangent $PT$:").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"\triangle OTP \text{ right-angled at } T").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = MathTex(r"PT^2 = 13^2 - 5^2 = 144 \;\Rightarrow\; PT = 12").scale(1.05).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = Tex("Tangent $+$ distance to centre $=$ this triangle, always").scale(0.95).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): the two equal tangents
        self.next_band(5)
        b5_title = Tex("Two tangents from one point are equal").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"\triangle OAP, \triangle OBP: OA = OB, \; OP \text{ common}").scale(0.9).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"\hat{A} = \hat{B} = 90^\circ \;\text{(tangent} \perp \text{radius)}").scale(0.95).shift(band_shift(5) + UP * 0.2)
        b5_l3 = MathTex(r"\text{RHS} \Rightarrow PA = PB \text{ (tangents)}").scale(0.95).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = MathTex(r"\hat{P} = 40^\circ: \hat{PAB} = \hat{PBA} = 70^\circ").scale(0.95).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("File that seventy — the next theorem catches it").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l5))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the tangent-chord theorem
        self.next_band(6)
        b6_title = Tex("Tangent-chord: the angle echoes across").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Tangent-chord angle $=$ angle in the alternate segment").scale(0.95).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2.5)
        b6_l2 = Tex(r"Proof sketch: diameter $AC$; tangent $\perp$ radius gives $90^\circ$").scale(0.9).shift(band_shift(6) + UP * 0.2)
        b6_l3 = MathTex(r"\hat{BAC} = 90^\circ - x, \; \hat{ABC} = 90^\circ").scale(0.95).shift(band_shift(6) + DOWN * 0.7)
        b6_l4 = MathTex(r"\text{Angle sum: } \hat{ACB} = x \;\text{ — the echo, proved}").scale(0.95).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l2))
        self.wait(2.5)
        self.play(Write(b6_l3))
        self.wait(2.5)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = MathTex(r"\text{Tan-chord } 65^\circ \Rightarrow 65^\circ \text{ far arc}").scale(0.95).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_l5))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): the full rider, plus cross-check
        self.next_band(7)
        b7_title = Tex(r"Rider: tangents $PA$, $PB$; $\hat{APB} = 40^\circ$; find $\hat{ACB}$").scale(0.95).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"PA = PB \;\text{(tangents from same point)}").scale(0.95).shift(band_shift(7) + UP * 1.2)
        b7_l2 = MathTex(r"\hat{PAB} = \hat{PBA} = 70^\circ \text{ (isosceles)}").scale(0.95).shift(band_shift(7) + UP * 0.3)
        b7_l3 = MathTex(r"\hat{ACB} = 70^\circ \;\text{(tangent-chord)}").scale(1.05).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = MathTex(r"\hat{AOB} = 360^\circ - 2(90^\circ) - 40^\circ = 140^\circ").scale(0.9).shift(band_shift(7) + DOWN * 1.7)
        b7_l5 = MathTex(r"\hat{ACB} = 140^\circ \div 2 = 70^\circ \text{ again}").scale(0.9).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l4))
        self.wait(2.5)
        self.play(Write(b7_l5))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): two arcs share the whole circle
        self.next_band(8)
        b8_title = Tex("Two arcs that share the whole circle").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Corner $B$ faces one arc, corner $D$ faces the rest").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("Between them they sweep the entire kraal wall").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"2\hat{B} + 2\hat{D} = 360^\circ; \; \hat{B} + \hat{D} = 180^\circ").scale(0.9).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("Walk past corner $C$: the outside angle is a").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        b8_l5 = Tex("photocopy of $\\hat{A}$, sent across the diagonal").scale(1.0).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3.5)

        # --- Band 9 (subtopic_6): the kerb and the two ropes
        self.next_band(9)
        b9_title = Tex("The kerb and the two ropes").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Wheel against a kerb: spoke to the touch point").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("stands dead square — tangent $\\perp$ radius, always").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(3)
        b9_l3 = MathTex(r"\text{Rope to a tank: } \sqrt{13^2 - 5^2} = 12").scale(1.05).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("Goat on two ropes to the kraal wall: the ropes are twins").scale(0.95).shift(band_shift(9) + DOWN * 1.7)
        b9_l5 = MathTex(r"\text{Peg } 40^\circ: \text{ base angles } 70^\circ").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l4))
        self.wait(2.5)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the echo across the chord
        self.next_band(10)
        b10_title = Tex("The echo across the chord").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Shout $65^\circ$ at the wall — it echoes, exact,").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("from every seat in the OTHER segment").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(3)
        b10_l3 = Tex("The echo crosses the chord; it starts at the touch point").scale(0.95).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex(r"Rider as a story: twin ropes, isosceles payout $70^\circ$,").scale(0.95).shift(band_shift(10) + DOWN * 1.5)
        b10_l5 = MathTex(r"\text{echo across: } \hat{ACB} = 70^\circ").scale(1.05).shift(band_shift(10) + DOWN * 2.4)
        self.play(Write(b10_l4))
        self.wait(2.5)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        b10_l6 = Tex("Two theorems, same number — the number is safe").scale(0.95).shift(band_shift(10) + DOWN * 3.1)
        self.play(Write(b10_l6))
        self.wait(4)
