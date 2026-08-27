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

# Band-layout whiteboard scene (reference: quadratics-by-factorisation).
# One band per teaching beat, add-only lifecycle, camera moves down between
# bands. Covers all seven subtopics: Part 1 Expert (first and second
# differences, building the general term, both directions, patterns in
# context) then Part 2 Simplifier (fingerprint at the second layer, three
# screws, driving the machine). Band dwell proportional to subtopics.json
# (230/235/225/230/195/195/190 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class QuadraticNumberPatternsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the difference table diagnosis ---
        title = Tex("Quadratic Number Patterns").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"4;\; 10;\; 18;\; 28;\; 40").scale(1.2).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = MathTex(r"\text{1st differences: } 6,\; 8,\; 10,\; 12").scale(1.1).shift(UP * 0.1)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = MathTex(r"\text{2nd differences: } 2,\; 2,\; 2 \text{ — constant!}").scale(1.1).shift(DOWN * 0.8)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = MathTex(r"\Rightarrow \text{quadratic: } T_n = an^2 + bn + c").scale(1.1).shift(DOWN * 1.8)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2.5)
        b0_l5 = Tex("Use at least four terms — three can look like anything").scale(0.95).shift(DOWN * 2.9)
        self.play(Write(b0_l5))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): why squares leave this fingerprint ---
        self.next_band(1)
        b1_title = Tex("Why? Squares climb by the odd numbers").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"1,\; 4,\; 9,\; 16,\; 25").scale(1.15).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"\text{jumps } 3, 5, 7, 9 \text{ — each } 2 \text{ more}").scale(1.05).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"\text{2nd difference} = 2a").scale(1.2).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_l4 = MathTex(r"2,\; 8,\; -6 \;\Rightarrow\; a = 1,\; 4,\; -3").scale(1.0).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1_l4))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): building T_n, first pattern ---
        self.next_band(2)
        b2_title = Tex("Three facts pin down $a$, $b$, $c$").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"2a = 2 \;\Rightarrow\; a = 1").scale(1.1).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"3a + b = 6 \;\Rightarrow\; b = 3").scale(1.1).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"a + b + c = 4 \;\Rightarrow\; c = 0").scale(1.1).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"T_n = n^2 + 3n").scale(1.2).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)
        b2_l5 = MathTex(r"\text{Test unseen: } T_4 = 16 + 12 = 28 \checkmark").scale(1.0).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l5))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): the dipping pattern ---
        self.next_band(3)
        b3_title = MathTex(r"12;\; 7;\; 4;\; 3;\; 4").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{1st: } -5, -3, -1, 1 \quad \text{2nd: } 2, 2, 2").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"a = 1, \quad 3 + b = -5 \Rightarrow b = -8").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"1 - 8 + c = 12 \Rightarrow c = 19").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"T_n = n^2 - 8n + 19 = (n-4)^2 + 3").scale(1.1).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2.5)
        b3_l5 = MathTex(r"\text{Minimum } T_4 = 3 \text{ — a parabola's mirror}").scale(1.0).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): forward and backward ---
        self.next_band(4)
        b4_title = Tex("The machine runs both ways").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{Forward: } T_{50} = 2500 + 150 = 2650").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"\text{Backward: } n^2 + 3n - 130 = 0").scale(1.1).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"(n + 13)(n - 10) = 0").scale(1.1).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"n = 10 \;\; (n = -13 \text{ rejected: positions} > 0)").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): membership and the discriminant ---
        self.next_band(5)
        b5_title = Tex("Is 150 a term? Ask the discriminant").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"n^2 + 3n - 150 = 0").scale(1.1).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"\Delta = 9 + 600 = 609 \text{ — not a perfect square}").scale(1.05).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("No natural-number $n$: 150 is not a term").scale(1.05).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex(r"$T_n$ is a parabola sampled at whole numbers").scale(1.0).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): brick pads — structure or table ---
        self.next_band(6)
        b6_title = Tex("Brick pads: 4, 10, 18, 28 bricks").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        r1 = Rectangle(width=1.4, height=0.4, color=BLUE).shift(band_shift(6) + UP * 1.4 + LEFT * 2.6)
        r2 = Rectangle(width=1.8, height=0.8, color=BLUE).shift(band_shift(6) + UP * 1.3)
        r3 = Rectangle(width=2.2, height=1.2, color=BLUE).shift(band_shift(6) + UP * 1.2 + RIGHT * 2.6)
        l1 = MathTex(r"1 \times 4").scale(0.8).move_to(r1.get_center() + DOWN * 0.7)
        l2 = MathTex(r"2 \times 5").scale(0.8).move_to(r2.get_center() + DOWN * 0.9)
        l3 = MathTex(r"3 \times 6").scale(0.8).move_to(r3.get_center() + DOWN * 1.1)
        self.play(Create(r1), Write(l1))
        self.play(Create(r2), Write(l2))
        self.play(Create(r3), Write(l3))
        self.wait(2)
        b6_l1 = MathTex(r"\text{Pad } n: \; n \times (n + 3) = n^2 + 3n").scale(1.1).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2.5)
        b6_l2 = Tex("Read the structure — the table is the fallback").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("Check: formula must reproduce pads 1 and 2").scale(1.0).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l3))
        self.wait(2)

        # --- Band 7 (subtopic_4): context answers, in context language ---
        self.next_band(7)
        b7_title = Tex("Answer in the language of the story").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"\text{Pad 20: } 400 + 60 = 460 \text{ bricks}").scale(1.1).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"154 \text{ bricks: } n^2 + 3n - 154 = 0").scale(1.05).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = MathTex(r"(n + 14)(n - 11) = 0 \Rightarrow \text{pad } 11").scale(1.05).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex("150 bricks? No — the discriminant says never").scale(1.05).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the fingerprint at the second layer ---
        self.next_band(8)
        b8_title = Tex("The fingerprint at the second layer").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Gaps: 6, 8, 10, 12 — growing").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("Gaps of gaps: 2, 2, 2 — steady").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("A staircase whose steps grow by the same extra 2").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = MathTex(r"\text{Steady number} = 2a:\; 8 \Rightarrow 4n^2").scale(1.0).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2.5)
        b8_l5 = Tex("Never fingerprint from three smudges").scale(1.0).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l5))
        self.wait(2.5)

        # --- Band 9 (subtopic_6): three screws fix the machine ---
        self.next_band(9)
        b9_title = Tex("Three screws fix the machine").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"\text{Screw 1: } a = \tfrac{\text{steady 2nd diff}}{2} = 1").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"\text{Screw 2: } 3a + b = \text{gap } 6 \Rightarrow b = 3").scale(1.0).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"\text{Screw 3: } a + b + c = T_1 = 4 \Rightarrow c = 0").scale(1.0).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = MathTex(r"T_n = n^2 + 3n, \;\; \text{test } T_4 = 28 \checkmark").scale(1.05).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex("Loose screw? Suspect $c$ first, then $b$, then $a$").scale(1.0).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l5))
        self.wait(2.5)

        # --- Band 10 (subtopic_7): forwards and in reverse ---
        self.next_band(10)
        b10_title = Tex("Drive it forwards and in reverse").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"\text{Forwards: feed } 50 \to 2500 + 150 = 2650").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"\text{Reverse: } 130 \Rightarrow (n+13)(n-10) = 0").scale(1.0).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Bay 10 exists; bay $-13$ does not — say so").scale(1.0).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2.5)
        b10_l4 = Tex(r"150? $\Delta = 609$ — the staircase never lands there").scale(1.0).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("154 bricks: pad 11 — finish in context").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l5))
        self.wait(4)
