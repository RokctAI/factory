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

# Band-layout whiteboard scene for the session duo "Cyclic Quadrilaterals and
# Tangents" (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics
# 5-7). One band per teaching beat, add-only lifecycle, camera moves down.
# Only exporter-supported mobjects; write-only reveals. Band dwell times
# follow subtopics.json (235/225/240/265/190/195/205 of 1555 s); Level 6
# rescales to real audio, so proportion is what matters.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CyclicQuadsTangentsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: player holds the topic full-screen while intro.md plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): opposite angles supplementary
        title = Tex("Cyclic Quadrilaterals and Tangents").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        d1 = MathTex(r"\hat{A} + \hat{C} = 180^\circ, \quad \hat{B} + \hat{D} = 180^\circ").scale(1.1).shift(UP * 0.9)
        self.play(Write(d1))
        self.play(Create(SurroundingRectangle(d1, color=GREEN)))
        self.wait(2.5)
        d2 = MathTex(r"\hat{A} = 105^\circ \;\Rightarrow\; \hat{C} = 75^\circ").scale(1.05).shift(DOWN * 0.2)
        self.play(Write(d2))
        self.wait(2.5)
        d3 = Tex(r"Proof: $2\hat{B} + 2\hat{D} = 360^\circ$ about the centre").scale(1.0).shift(DOWN * 1.2)
        d4 = Tex("Exterior angle $=$ interior opposite angle").scale(1.0).shift(DOWN * 2.1)
        self.play(Write(d3))
        self.wait(2.5)
        self.play(Write(d4))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): the three converse tests
        self.next_band(1)
        b1_title = Tex("Proving four points share a circle").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Test 1: one pair of opposite angles supplementary").scale(0.95).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("Test 2: exterior angle $=$ interior opposite").scale(0.95).shift(band_shift(1) + UP * 0.2)
        b1_l3 = Tex("Test 3: equal angles on the same side of a segment").scale(0.95).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.wait(2.5)
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = Tex("One test settles it; part (a) earns the circle, part (b) spends it").scale(0.85).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 2 (subtopic_3): tangent perpendicular to radius
        self.next_band(2)
        b2_title = Tex("Tangent $\\perp$ radius at the point of contact").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_c = Circle(radius=1.5, color=BLUE).shift(band_shift(2) + DOWN * 1.6 + LEFT * 3)
        b2_t = Line(band_shift(2) + DOWN * 0.1 + LEFT * 5.2, band_shift(2) + DOWN * 0.1 + LEFT * 0.8, color=YELLOW)
        self.play(Create(b2_c))
        self.play(Create(b2_t))
        self.wait(2)
        b2_l1 = MathTex(r"OP = 17, \; r = 8: \; PT^2 = 17^2 - 8^2 = 225").scale(1.0).shift(band_shift(2) + UP * 1.0 + RIGHT * 1.2)
        b2_l2 = MathTex(r"PT = 15").scale(1.15).shift(band_shift(2) + UP * 0.1 + RIGHT * 1.2)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): two equal tangents
        self.next_band(3)
        b3_title = Tex("Two tangents from one point are equal").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"$OA = OB$ (radii); $OP$ common hypotenuse; $90^\circ$ at $A, B$").scale(0.9).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"\text{RHS} \Rightarrow PA = PB \;\; \text{(tangents from same point)}").scale(0.95).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = MathTex(r"\hat{APB} = 52^\circ: \; \hat{PAB} = \hat{PBA} = \tfrac{180 - 52}{2} = 64^\circ").scale(0.95).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex("Equal tangents plant an isosceles triangle — find it first").scale(0.9).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_4): tangent-chord and the full rider
        self.next_band(4)
        b4_title = Tex("Tangent-chord: the angle in the alternate segment").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{Tangent-chord angle } 58^\circ \Rightarrow 58^\circ \text{ on the far arc}").scale(0.95).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"1.\; PA = PB \;\; \text{(tangents from same point)}").scale(0.9).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"2.\; \hat{PAB} = \hat{PBA} = 64^\circ \;\; \text{(isosceles, angle sum)}").scale(0.9).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"3.\; \hat{ACB} = 64^\circ \;\; \text{(tangent-chord)}").scale(0.95).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2.5)
        b4_l5 = MathTex(r"\text{Check: } \hat{AOB} = 360 - 90 - 90 - 52 = 128^\circ \Rightarrow \tfrac{128}{2} = 64^\circ").scale(0.85).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): two arcs, one wall
        self.next_band(5)
        b5_title = Tex("Two arcs that share the whole circle").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("Opposite posts $B$ and $D$ watch complementary arcs").scale(0.95).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("Together their arcs cover the entire kraal wall").scale(0.95).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"2\hat{B} + 2\hat{D} = 360^\circ \;\Rightarrow\; \hat{B} + \hat{D} = 180^\circ").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex("Outside angle at $C$ $=$ photocopy of the angle at $A$").scale(0.95).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_6): the kerb and the ropes
        self.next_band(6)
        b6_title = Tex("The kerb and the two ropes").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Spoke to the touching point: dead square to the kerb").scale(0.95).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"17 \text{ paces, radius } 8: \text{ rope} = \sqrt{289 - 64} = 15").scale(0.95).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = Tex("Two ropes from one peg: always twins (mirror symmetry)").scale(0.95).shift(band_shift(6) + DOWN * 0.8)
        b6_l4 = MathTex(r"52^\circ \text{ at the peg} \Rightarrow 64^\circ \text{ and } 64^\circ \text{ at the wall}").scale(0.95).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l3))
        self.wait(2.5)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_7): the echo across the chord
        self.next_band(7)
        b7_title = Tex("The echo across the chord").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Shout $58^\\circ$ against the wall — it echoes across the chord").scale(0.95).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("The echo lands in the ALTERNATE segment, never the same side").scale(0.9).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Story rider: twins, isosceles $64^\\circ$, echo $\\Rightarrow$ $64^\\circ$ far arc").scale(0.9).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex("Second road: greedy centre $128^\\circ$, half $= 64^\\circ$ — confirmed").scale(0.9).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l4))
        self.wait(4)
