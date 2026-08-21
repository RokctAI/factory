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

# Band-layout whiteboard scene for the session duo "The Sine Rule and the
# Area Rule" (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier:
# subtopics 5-7). One band per teaching beat, add-only lifecycle, camera
# moves down between bands. Only exporter-supported mobjects; write-only
# reveals. Band dwell times follow subtopics.json
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
        # Intro beat: player holds the topic full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the labelling convention + area rule ---
        title = Tex("The Sine Rule and the Area Rule").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Small $a$ faces capital $A$; $b$ faces $B$; $c$ faces $C$").scale(1.0).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.play(Create(SurroundingRectangle(b0_l1, color=GREEN)))
        self.wait(2.5)
        b0_l2 = MathTex(r"\text{Area} = \tfrac{1}{2}ab\sin C").scale(1.15).shift(UP * 0.0)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Two sides, times sine of the angle BETWEEN them").scale(0.95).shift(DOWN * 1.0)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("Also $\\tfrac{1}{2}bc\\sin A$ and $\\tfrac{1}{2}ac\\sin B$").scale(0.95).shift(DOWN * 1.9)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): where it comes from + worked example ---
        self.next_band(1)
        b1_title = Tex("Manufacture the height: $h = a\\sin C$").scale(1.1).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        tc = band_shift(1) + DOWN * 0.4
        A = tc + LEFT * 3.0 + DOWN * 1.2
        C = tc + RIGHT * 3.0 + DOWN * 1.2
        B = tc + RIGHT * 0.8 + UP * 1.6
        F = tc + RIGHT * 0.8 + DOWN * 1.2
        sAC = Line(A, C); sAB = Line(A, B); sBC = Line(B, C); sBF = Line(B, F)
        lA = Tex("A").scale(0.9).move_to(A + LEFT * 0.35)
        lB = Tex("B").scale(0.9).move_to(B + UP * 0.35)
        lC = Tex("C").scale(0.9).move_to(C + RIGHT * 0.35)
        self.play(Create(sAC), Create(sAB), Create(sBC))
        self.play(Write(lA), Write(lB), Write(lC))
        self.wait(2)
        self.play(Create(sBF))
        self.wait(2)
        b1_l1 = MathTex(r"\text{Area} = \tfrac{1}{2} b (a\sin C) = \tfrac{1}{2}ab\sin C").scale(0.95).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"\tfrac{1}{2}(6)(11)\sin 40^\circ = 33 \times 0{,}6428 \approx 21{,}21 \text{ cm}^2").scale(0.9).shift(band_shift(1) + DOWN * 3.4)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): proving the sine rule ---
        self.next_band(2)
        b2_title = Tex("Three area formulae, one triangle").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\tfrac{1}{2}bc\sin A = \tfrac{1}{2}ac\sin B = \tfrac{1}{2}ab\sin C").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = Tex("Divide every part by $\\tfrac{1}{2}abc$:").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"\frac{\sin A}{a} = \frac{\sin B}{b} = \frac{\sin C}{c}").scale(1.1).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex("Flipped for sides: $\\tfrac{a}{\\sin A} = \\tfrac{b}{\\sin B} = \\tfrac{c}{\\sin C}$").scale(0.95).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): using it for a side ---
        self.next_band(3)
        b3_title = Tex(r"$A = 35^\circ$, $B = 70^\circ$, $b = 14$: find $a$").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = Tex("Complete pair: $b$ with $B$. Unknown on top:").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"\frac{a}{\sin 35^\circ} = \frac{14}{\sin 70^\circ}").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"a = \frac{14 \times 0{,}5736}{0{,}9397} = 8{,}55 \text{ cm}").scale(1.05).shift(band_shift(3) + DOWN * 1.0)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("Round only at the final line").scale(0.95).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): finding an angle, the second suspect ---
        self.next_band(4)
        b4_title = Tex(r"$a = 12$, $b = 8$, $A = 48^\circ$: find $B$").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"\sin B = \frac{8\sin 48^\circ}{12} = 0{,}4954").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"B = 29{,}7^\circ \quad \text{or} \quad 180^\circ - 29{,}7^\circ = 150{,}3^\circ?").scale(0.95).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"150{,}3^\circ + 48^\circ > 180^\circ \;\Rightarrow\; \text{rejected}").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = MathTex(r"C = 180^\circ - 48^\circ - 29{,}7^\circ = 102{,}3^\circ").scale(0.95).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_4): chaining — plan the route ---
        self.next_band(5)
        b5_title = Tex(r"$A = 44^\circ$, $B = 58^\circ$, $c = 20$: find the AREA").scale(1.0).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("Area rule needs two sides — build one first").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"C = 180^\circ - 44^\circ - 58^\circ = 78^\circ \;\text{(free)}").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"a = \frac{20\sin 44^\circ}{\sin 78^\circ} = 14{,}20 \text{ cm}").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the two disciplines ---
        self.next_band(6)
        b6_title = Tex("Close with the area rule").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("$a$ and $c$ meet at vertex $B$: $B$ is included").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"\text{Area} = \tfrac{1}{2}(14{,}20)(20)\sin 58^\circ").scale(1.0).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"= 142{,}04 \times 0{,}8480 \approx 120{,}45 \text{ cm}^2").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = Tex("Angle sum completes pairs for free; sketch picks the angle").scale(0.9).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the squashed gate ---
        self.next_band(7)
        b7_title = Tex("The squashed gate").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Two arms, hinged: sine of the corner is the squash factor").scale(0.95).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"90^\circ: \sin = 1, \text{ max area} \quad 0^\circ/180^\circ: \sin = 0, \text{ none}").scale(0.9).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"\text{Area} = \tfrac{1}{2} \times \text{arm} \times \text{arm} \times \text{squash}").scale(1.0).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex("Fingers on the two sides: take the angle where they meet").scale(0.9).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4))
        self.wait(3)

        # --- Band 8 (subtopic_6): fair trade at the triangle market ---
        self.next_band(8)
        b8_title = Tex("Fair trade at the triangle market").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("One fixed rate: side over sine of its facing angle").scale(0.95).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"\text{Rate} = \frac{14}{\sin 70^\circ}; \quad a = \sin 35^\circ \times \text{rate} = 8{,}55").scale(0.95).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex("Hunting a side? Sides on top. An angle? Flip.").scale(0.95).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("Second suspect at $180^\\circ$ minus — interrogate it").scale(0.95).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_7): planning the route before you drive ---
        self.next_band(9)
        b9_title = Tex("Plan the route before you drive").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Stocktake: sides, angles, complete pairs, destination").scale(0.95).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("Backwards: area needs a side; sine rule builds it;").scale(0.95).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex("the free angle completes the pair first").scale(0.95).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = MathTex(r"78^\circ \to 14{,}20 \text{ cm} \to 120{,}45 \text{ cm}^2").scale(1.0).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex("Label your own triangle; state each rule and its reason").scale(0.9).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l5))
        self.wait(4)
