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

# Band-layout whiteboard scene (see lessons/scripts/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing removed.
# Write-only reveals on single-string Tex/MathTex keep the export clean. Bands
# cover all seven subtopics (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7),
# dwell time proportional to subtopics.json (220/250/250/260/160/160/160 of
# 1460 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SumAndDifferenceOfCubesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): recognising cubes
        title = Tex("Sum and Difference of Cubes").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l01 = MathTex(r"1,\; 8,\; 27,\; 64,\; 125,\; 216").scale(1.2).shift(UP * 0.9)
        l02 = MathTex(r"= 1^3,\; 2^3,\; 3^3,\; 4^3,\; 5^3,\; 6^3").scale(1.1).shift(UP * 0.0)
        self.play(Write(l01))
        self.wait(2)
        self.play(Write(l02))
        self.wait(2)
        l03 = MathTex(r"y^6 = (y^2)^3, \quad 8a^3b^3 = (2ab)^3").scale(1.05).shift(DOWN * 1.0)
        self.play(Write(l03))
        self.wait(2)
        l04 = MathTex(r"x^3 + 8 = a^3 + b^3: \;\; a = x, \; b = 2").scale(1.1).shift(DOWN * 2.0)
        self.play(Write(l04))
        self.play(Create(SurroundingRectangle(l04, color=GREEN)))
        l05 = Tex("No common factor, not squares, not a trinomial").scale(1.0).shift(DOWN * 3.0)
        self.play(Write(l05))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): the identities and SOAP
        self.next_band(1)
        b1_title = Tex("The identities").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"a^3 + b^3 = (a + b)(a^2 - ab + b^2)").scale(1.1).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"a^3 - b^3 = (a - b)(a^2 + ab + b^2)").scale(1.1).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex(r"SOAP: Same — Opposite — Always Positive").scale(1.1).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=YELLOW)))
        self.wait(2)
        b1_l4 = Tex(r"Second bracket: square, multiply, square").scale(1.05).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l4))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): where the identity comes from
        self.next_band(2)
        b2_title = Tex(r"Expand $(a+b)(a^2 - ab + b^2)$").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"a: \quad a^3 - a^2b + ab^2").scale(1.1).shift(band_shift(2) + UP * 1.0)
        b2_l2 = MathTex(r"b: \quad + a^2b - ab^2 + b^3").scale(1.1).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex(r"$-a^2b$ cancels $+a^2b$; $+ab^2$ cancels $-ab^2$").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        b2_l4 = MathTex(r"\text{Survivors: } a^3 + b^3").scale(1.15).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l3))
        self.wait(2.5)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): factorise x^3 + 8, step by step
        self.next_band(3)
        b3_title = Tex(r"Factorise fully: $x^3 + 8$").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"a = x, \quad b = 2").scale(1.1).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"\text{Same: } (x + 2)").scale(1.1).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"\text{Square, multiply, square: } x^2, \; 2x, \; 4").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = MathTex(r"x^3 + 8 = (x + 2)(x^2 - 2x + 4)").scale(1.1).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        b3_l5 = Tex(r"Middle is $-2x$ (a product), never $-4x$").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): verify, and know when to stop
        self.next_band(4)
        b4_title = Tex("Verify — and stop in the right place").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"x(x^2 - 2x + 4) = x^3 - 2x^2 + 4x").scale(1.05).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"2(x^2 - 2x + 4) = 2x^2 - 4x + 8").scale(1.05).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"\text{Middles cancel: } x^3 + 8 \;\checkmark").scale(1.1).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_wrong = MathTex(r"x^2 - 2x + 4 = (\;?\;)(\;?\;)").scale(1.05).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_wrong))
        self.play(Create(strike(b4_wrong)))
        b4_rule = Tex("The quadratic factor NEVER factorises here").scale(1.0).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_rule))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): the difference twin
        self.next_band(5)
        b5_title = Tex(r"The twin: $x^3 - 27$").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"a = x, \quad b = 3").scale(1.1).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"x^3 - 27 = (x - 3)(x^2 + 3x + 9)").scale(1.1).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex(r"Squares vs cubes: check the exponent first").scale(1.05).shift(band_shift(5) + DOWN * 1.0)
        b5_l4 = MathTex(r"x^2 - 9 = (x-3)(x+3) \;\text{ — both linear}").scale(1.0).shift(band_shift(5) + DOWN * 1.9)
        b5_l5 = Tex(r"Cubes: one short bracket, one long — long stays").scale(1.0).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): common factor first + full method
        self.next_band(6)
        b6_title = Tex(r"Factorise fully: $2x^3 - 54$").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"= 2(x^3 - 27)").scale(1.1).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"= 2(x - 3)(x^2 + 3x + 9)").scale(1.1).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2)
        b6_m1 = Tex(r"1. Common factor first \; 2. Name $a$ and $b$").scale(1.0).shift(band_shift(6) + DOWN * 0.8)
        b6_m2 = Tex(r"3. Short bracket: Same \; 4. Long: square, multiply, square").scale(0.95).shift(band_shift(6) + DOWN * 1.6)
        b6_m3 = Tex(r"5. Verify by expanding \; 6. Long bracket is final").scale(1.0).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_m1))
        self.wait(1.5)
        self.play(Write(b6_m2))
        self.wait(1.5)
        self.play(Write(b6_m3))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): cubes are boxes you can stack
        self.next_band(7)
        b7_title = Tex("Cubes are just boxes you can stack").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"$2 \times 2 \times 2 = 8$ stock cubes fill a perfect box").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"1,\; 8,\; 27,\; 64,\; 125,\; 216 \;\text{ — know them cold}").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = MathTex(r"x^3 + 8: \;\; x \text{ boxed, and } 2 \text{ boxed}").scale(1.05).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        b7_l4 = Tex(r"Old tools bounce off — the signpost reads ``cubes''").scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l4))
        self.wait(2.5)

        # --- Band 8 (subtopic_6): three signs, one bar of soap
        self.next_band(8)
        b8_title = Tex("Three signs, one bar of soap").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Skeleton first: square, times, square").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex(r"SOAP: Same, Opposite, Always Positive").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=YELLOW)))
        self.wait(2)
        b8_l3 = MathTex(r"x^3 + 8 = (x + 2)(x^2 - 2x + 4)").scale(1.1).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex(r"Middles cancel when you multiply back — paid out,").scale(0.95).shift(band_shift(8) + DOWN * 1.8)
        b8_l5 = Tex(r"paid straight back. And the middle is $2x$, not $4x$").scale(0.95).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2.5)

        # --- Band 9 (subtopic_7): curtain, twin, full stop
        self.next_band(9)
        b9_title = Tex("The curtain, the twin, the full stop").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"x^3 - 27 = (x - 3)(x^2 + 3x + 9)").scale(1.05).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = MathTex(r"2x^3 - 54 = 2(x^3 - 27)").scale(1.05).shift(band_shift(9) + UP * 0.3)
        b9_l3 = MathTex(r"= 2(x - 3)(x^2 + 3x + 9)").scale(1.05).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l2))
        self.wait(2)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex(r"Wrapper off first — common factor, then pattern").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        b9_l5 = Tex(r"And leave the long bracket alone — it never breaks").scale(1.0).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l4))
        self.wait(2)
        self.play(Write(b9_l5))
        self.wait(4)
