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

# BAND LAYOUT (see lessons/scripts/manim_exporter.py): content is laid out in
# sequential vertical bands along a long virtual canvas — one band per teaching
# step, each one frame-height tall. Nothing is ever faded out or overwritten;
# at each step the camera moves down to clean space and earlier work stays on
# the canvas. Every mobject used here serializes to the real whiteboard
# vocabulary (text/line/rect via Tex/MathTex/Line/SurroundingRectangle) — no
# sub-part Transform tricks, which leak raw glyph primitives through the
# exporter's Tex shim.
#
# The scene mirrors script.md's teaching beats across all seven subtopics of
# the session duo (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier:
# subtopics 5-7), with band dwell times proportional to subtopics.json
# (220/220/240/235/185/185/190 of 1475 s). Level 6 rescales primitive times
# to the real audio duration, so proportion — not absolute seconds — is what
# must match.

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k (k=0 is the default
    frame; each band is one frame-height further down)."""
    return DOWN * BAND * k


def strike(m):
    """Diagonal cancellation stroke through a term, teacher-style."""
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class QuadraticsByFactorisationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Opening intro beat: the player shows the TOPIC full-screen while the
        # tutor speaks intro.md; board work must not start until it lands. The
        # exporter measures the first primitive's time and the manifest
        # publishes it as the topic_display duration (~4-5% of the scene).
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): standard form and the zero-product principle
        title = Tex("Solving Quadratics by Factorisation").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        std_form = MathTex(r"ax^2 + bx + c = 0, \quad a \neq 0").scale(1.3).shift(UP * 0.8)
        self.play(Write(std_form))
        self.wait(2)
        zpp_name = Tex("Zero-product principle:").scale(1.1).shift(DOWN * 0.5)
        zpp = MathTex(r"A \times B = 0 \;\Rightarrow\; A = 0 \text{ or } B = 0").scale(1.2).shift(DOWN * 1.5)
        self.play(Write(zpp_name))
        self.play(Write(zpp))
        self.wait(3)
        only_zero = Tex(r"$A \times B = 8$ tells you nothing about $A$").scale(1.1).shift(DOWN * 2.7)
        self.play(Write(only_zero))
        self.wait(3)

        # --- Band 1 (subtopic_1): the =8 trap, worked in full
        self.next_band(1)
        b1_title = Tex(r"Solve: $(x-2)(x+5) = 8$").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_wrong = MathTex(r"x - 2 = 8 \quad \text{(no zero — not allowed!)}").scale(1.1).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2)
        b1_l1 = MathTex(r"x^2 + 3x - 10 = 8").scale(1.15).shift(band_shift(1))
        b1_l2 = MathTex(r"x^2 + 3x - 18 = 0").scale(1.15).shift(band_shift(1) + DOWN * 0.9)
        b1_l3 = MathTex(r"(x+6)(x-3) = 0").scale(1.15).shift(band_shift(1) + DOWN * 1.8)
        b1_l4 = MathTex(r"x = -6 \quad \text{or} \quad x = 3").scale(1.15).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_1): never divide by a variable
        self.next_band(2)
        b2_title = Tex(r"Solve: $x^2 = 3x$").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_wrong = MathTex(r"\div x: \;\; x = 3 \quad (x = 0 \text{ vanished})").scale(1.1).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2.5)
        b2_l1 = MathTex(r"x^2 - 3x = 0").scale(1.15).shift(band_shift(2))
        b2_l2 = MathTex(r"x(x - 3) = 0").scale(1.15).shift(band_shift(2) + DOWN * 0.9)
        b2_l3 = MathTex(r"x = 0 \quad \text{or} \quad x = 3").scale(1.15).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        b2_rule = Tex("Never divide by a variable — factorise it out").scale(1.1).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_rule))
        self.wait(3)

        # --- Band 3 (subtopic_2): shapes 1 and 2 — common factor, simple trinomial
        self.next_band(3)
        b3_title = Tex("The shapes a quadratic takes").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_s1 = Tex("1. Common factor:").scale(1.1).shift(band_shift(3) + UP * 1.2 + LEFT * 3.5)
        b3_l1 = MathTex(r"2x^2 - 8x = 0 \;\Rightarrow\; 2x(x-4) = 0").scale(1.1).shift(band_shift(3) + UP * 0.4)
        b3_l2 = MathTex(r"x = 0 \quad \text{or} \quad x = 4").scale(1.1).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3_s1))
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_s2 = Tex(r"2. Trinomial, $a = 1$:").scale(1.1).shift(band_shift(3) + DOWN * 1.3 + LEFT * 3.3)
        b3_l3 = MathTex(r"x^2 - 7x + 12 = (x-3)(x-4) = 0").scale(1.1).shift(band_shift(3) + DOWN * 2.1)
        b3_l4 = MathTex(r"(-3) \times (-4) = 12, \quad (-3) + (-4) = -7").scale(1.0).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_s2))
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_2): shape 3 — leading coefficient not one
        self.next_band(4)
        b4_title = Tex(r"3. Trinomial, $a \neq 1$: solve $3x^2 - 5x - 2 = 0$").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"a \times c = -6: \quad -6 \times 1 = -6, \;\; -6 + 1 = -5").scale(1.05).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"3x^2 - 6x + x - 2 = 0").scale(1.1).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"3x(x - 2) + 1(x - 2) = 0").scale(1.1).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"(3x + 1)(x - 2) = 0").scale(1.1).shift(band_shift(4) + DOWN * 1.6)
        b4_l5 = MathTex(r"x = -\tfrac{1}{3} \quad \text{or} \quad x = 2").scale(1.1).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_2): shape 4 — difference of squares, both roots
        self.next_band(5)
        b5_title = Tex(r"4. Difference of squares: $4x^2 - 25 = 0$").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"(2x - 5)(2x + 5) = 0").scale(1.15).shift(band_shift(5) + UP * 1.0)
        b5_l2 = MathTex(r"x = \tfrac{5}{2} \quad \text{or} \quad x = -\tfrac{5}{2}").scale(1.15).shift(band_shift(5))
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_warn = Tex(r"$9x^2 = 16$ gives $x = \tfrac{4}{3}$ AND $x = -\tfrac{4}{3}$").scale(1.1).shift(band_shift(5) + DOWN * 1.2)
        b5_rule = Tex("Never drop the negative square root").scale(1.1).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5_warn))
        self.wait(2)
        self.play(Write(b5_rule))
        self.wait(3)

        # --- Band 6 (subtopic_3): fractions — restrictions first
        self.next_band(6)
        b6_title = Tex(r"Fractions: solve $\dfrac{x+6}{x} = 5$").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Step 1 — restriction: $x \neq 0$").scale(1.1).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"\times x: \quad x^2 + 6 = 5x").scale(1.1).shift(band_shift(6) + UP * 0.2)
        b6_l3 = MathTex(r"x^2 - 5x + 6 = 0").scale(1.1).shift(band_shift(6) + DOWN * 0.7)
        b6_l4 = MathTex(r"(x - 2)(x - 3) = 0").scale(1.1).shift(band_shift(6) + DOWN * 1.6)
        b6_l5 = MathTex(r"x = 2 \;\text{ or }\; x = 3 \;\; \text{(not banned)}").scale(1.1).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(1.5)
        self.play(Write(b6_l4))
        self.wait(1.5)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_3): two denominators
        self.next_band(7)
        b7_title = Tex(r"Solve $\dfrac{4}{x} + \dfrac{4}{x+2} = 3$").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"Restrictions: $x \neq 0$ and $x \neq -2$; LCD $= x(x+2)$").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"4(x+2) + 4x = 3x(x+2)").scale(1.1).shift(band_shift(7) + UP * 0.2)
        b7_l3 = MathTex(r"3x^2 - 2x - 8 = 0").scale(1.1).shift(band_shift(7) + DOWN * 0.7)
        b7_l4 = MathTex(r"(3x + 4)(x - 2) = 0").scale(1.1).shift(band_shift(7) + DOWN * 1.6)
        b7_l5 = MathTex(r"x = -\tfrac{4}{3} \quad \text{or} \quad x = 2").scale(1.1).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(2)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_4): substitution — the repeated expression
        self.next_band(8)
        b8_title = Tex(r"Solve $(x^2-3x)^2 - 2(x^2-3x) - 8 = 0$").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"\text{Let } k = x^2 - 3x: \quad k^2 - 2k - 8 = 0").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = MathTex(r"(k - 4)(k + 2) = 0 \;\Rightarrow\; k = 4 \text{ or } k = -2").scale(1.05).shift(band_shift(8) + UP * 0.2)
        b8_l3 = MathTex(r"x^2 - 3x - 4 = 0 \;\Rightarrow\; x = 4 \text{ or } x = -1").scale(1.05).shift(band_shift(8) + DOWN * 0.8)
        b8_l4 = MathTex(r"x^2 - 3x + 2 = 0 \;\Rightarrow\; x = 1 \text{ or } x = 2").scale(1.05).shift(band_shift(8) + DOWN * 1.7)
        b8_l5 = MathTex(r"x \in \{-1,\; 1,\; 2,\; 4\}").scale(1.1).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(2)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_4): one linear with one quadratic
        self.next_band(9)
        b9_title = Tex(r"Solve $x + y = 5$ and $x^2 + y^2 = 17$").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"\text{Rearrange the LINEAR one: } y = 5 - x").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"x^2 + (5 - x)^2 = 17 \;\Rightarrow\; 2x^2 - 10x + 8 = 0").scale(1.0).shift(band_shift(9) + UP * 0.2)
        b9_l3 = MathTex(r"x^2 - 5x + 4 = (x-1)(x-4) = 0").scale(1.05).shift(band_shift(9) + DOWN * 0.8)
        b9_l4 = MathTex(r"(x; y) = (1; 4) \quad \text{or} \quad (4; 1)").scale(1.1).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2.5)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        b9_rule = Tex("Answers come as ordered pairs").scale(1.1).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_rule))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 10 (subtopic_5): zero is the only number that talks
        self.next_band(10)
        b10_title = Tex("Zero is the only number that talks").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Takings $\times$ takings $= 0$: someone sold nothing").scale(1.05).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex(r"Takings $\times$ takings $= 800$: you know nothing").scale(1.05).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"x^2 = 3x: \;\; x^2 - 3x = 0, \;\; x(x-3) = 0").scale(1.0).shift(band_shift(10) + DOWN * 0.9)
        b10_l4 = MathTex(r"x = 0 \quad \text{or} \quad x = 3").scale(1.1).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l3))
        self.wait(2.5)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_6): clear the fractions before you fight
        self.next_band(11)
        b11_title = Tex("Clear the fractions before you fight").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex(r"Banned values first: bottom is $x$, so $x \neq 0$").scale(1.05).shift(band_shift(11) + UP * 1.1)
        b11_l2 = MathTex(r"\frac{x+6}{x} = 5 \;\xrightarrow{\times x}\; x^2 + 6 = 5x").scale(1.05).shift(band_shift(11) + UP * 0.1)
        b11_l3 = MathTex(r"x^2 - 5x + 6 = (x-2)(x-3) = 0").scale(1.05).shift(band_shift(11) + DOWN * 1.0)
        b11_l4 = MathTex(r"x = 2 \quad \text{or} \quad x = 3").scale(1.1).shift(band_shift(11) + DOWN * 2.0)
        self.play(Write(b11_l1))
        self.wait(2.5)
        self.play(Write(b11_l2))
        self.wait(2.5)
        self.play(Write(b11_l3))
        self.wait(2)
        self.play(Write(b11_l4))
        self.play(Create(SurroundingRectangle(b11_l4, color=GREEN)))
        self.wait(3)

        # --- Band 12 (subtopic_7): nicknames, and keeping the pairs together
        self.next_band(12)
        b12_title = Tex("Nicknames, and keeping the pairs together").scale(1.15).shift(band_shift(12) + UP * 2.2)
        self.play(Write(b12_title))
        self.wait(2)
        b12_l1 = MathTex(r"\text{Nickname the chunk: } k = x^2 - 3x").scale(1.05).shift(band_shift(12) + UP * 1.1)
        b12_l2 = MathTex(r"k^2 - 2k - 8 = (k-4)(k+2) = 0").scale(1.05).shift(band_shift(12) + UP * 0.2)
        b12_l3 = Tex(r"Swap the chunk back in — $k$ was never the question").scale(1.0).shift(band_shift(12) + DOWN * 0.7)
        self.play(Write(b12_l1))
        self.wait(2.5)
        self.play(Write(b12_l2))
        self.wait(2.5)
        self.play(Write(b12_l3))
        self.wait(2.5)
        b12_l4 = Tex(r"Pairs hold hands: $(1; 4)$ or $(4; 1)$ — never two loose lists").scale(1.0).shift(band_shift(12) + DOWN * 1.7)
        self.play(Write(b12_l4))
        self.play(Create(SurroundingRectangle(b12_l4, color=GREEN)))
        self.wait(4)
