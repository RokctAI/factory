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

# BAND LAYOUT (see lessons/scripts/CAPS/manim_exporter.py): content is laid out in
# sequential vertical bands along a long virtual canvas — one band per teaching
# step, each one frame-height tall. Nothing is ever faded out or overwritten;
# at each step the camera moves down to clean space and earlier work stays on
# the canvas. Every mobject serializes to the whiteboard vocabulary
# (text/line/rect via Tex/MathTex/Line/SurroundingRectangle) — no sub-part
# Transform tricks, which leak raw glyph primitives through the exporter's
# Tex shim.
#
# The scene mirrors script.md's teaching beats across all seven subtopics of
# the session duo (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier:
# subtopics 5-7), with band dwell times proportional to subtopics.json
# (250/240/240/250/180/180/180 of 1520 s). Level 6 rescales primitive times
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


class Paper1EssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Opening intro beat: the player shows the TOPIC full-screen while the
        # tutor speaks intro.md; board work must not start until it lands.
        self.wait(16)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the opening solve — quadratic formula
        title = Tex("Paper 1 Essentials").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_q = Tex(r"Solve $3x^2 - 5x - 1 = 0$ (two decimals)").scale(1.0).shift(UP * 1.2)
        self.play(Write(b0_q))
        self.wait(2)
        b0_f = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").scale(1.1).shift(UP * 0.1)
        self.play(Write(b0_f))
        self.wait(2)
        b0_s = MathTex(r"x = \frac{5 \pm \sqrt{25 + 12}}{6} = \frac{5 \pm \sqrt{37}}{6}").scale(0.95).shift(DOWN * 1.1)
        self.play(Write(b0_s))
        self.wait(2.5)
        b0_a = MathTex(r"x \approx 1{,}85 \; \text{ or } \; x \approx -0{,}18").scale(1.0).shift(DOWN * 2.2)
        self.play(Write(b0_a))
        self.play(Create(SurroundingRectangle(b0_a, color=GREEN)))
        b0_w = Tex("Round once, at the end").scale(1.0).shift(DOWN * 3.0)
        self.play(Write(b0_w))
        self.wait(3)

        # --- Band 1 (subtopic_1): the k-method
        self.next_band(1)
        b1_t = Tex(r"Solve $3^{2x} - 10 \cdot 3^x + 9 = 0$").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_l1 = MathTex(r"\text{Let } k = 3^x: \quad k^2 - 10k + 9 = 0").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = MathTex(r"(k - 1)(k - 9) = 0").scale(1.1).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"3^x = 1 \;\Rightarrow\; x = 0").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = MathTex(r"3^x = 9 \;\Rightarrow\; x = 2").scale(1.05).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = MathTex(r"x = 0 \quad \text{or} \quad x = 2").scale(1.1).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_1): surd equations demand a check
        self.next_band(2)
        b2_t = Tex(r"Solve $\sqrt{x+5} = x - 1$").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"x + 5 = x^2 - 2x + 1").scale(1.1).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"x^2 - 3x - 4 = 0 \Rightarrow (x-4)(x+1) = 0").scale(0.9).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"x = 4: \; \sqrt{9} = 3 = 4 - 1 \;\checkmark").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"x = -1: \; \sqrt{4} = 2 \neq -2").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l4))
        self.play(Create(strike(b2_l4)))
        self.wait(2)
        b2_l5 = MathTex(r"x = 4 \text{ only}").scale(1.1).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_1): inequality picture + simultaneous pairs
        self.next_band(3)
        b3_t = Tex(r"Solve $(x-4)(x+2) > 0$").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex("Upward parabola: positive outside roots").scale(0.95).shift(band_shift(3) + UP * 1.3)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"x < -2 \; \text{ or } \; x > 4").scale(1.05).shift(band_shift(3) + UP * 0.5)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex(r"Simultaneous: $y = x + 2$, $x^2 + y^2 = 10$").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"x^2 + (x+2)^2 = 10 \Rightarrow x^2 + 2x - 3 = 0").scale(0.85).shift(band_shift(3) + DOWN * 1.4)
        self.play(Write(b3_l4))
        self.wait(2.5)
        b3_l5 = MathTex(r"(x+3)(x-1) = 0").scale(1.05).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l5))
        self.wait(2)
        b3_l6 = MathTex(r"(1; 3) \; \text{ or } \; (-3; -1)").scale(1.05).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(b3_l6, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_2): quadratic pattern by differences
        self.next_band(4)
        b4_t = Tex(r"Pattern $3;\,8;\,15;\,24$ — diagnose by differences").scale(0.95).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_l1 = MathTex(r"\text{1st: } 5,\,7,\,9 \qquad \text{2nd: } 2,\,2").scale(1.0).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"2a = 2 \Rightarrow a = 1, \quad T_n = n^2 + 2n").scale(0.95).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"\text{Check: } 1 + 2 = 3, \;\; 4 + 4 = 8 \;\checkmark").scale(0.95).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"n^2 + 2n - 168 = 0 \Rightarrow (n+14)(n-12) = 0").scale(0.85).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = MathTex(r"n = 12 \;\; (\text{reject } n = -14)").scale(1.05).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_2): geometric series and the smallest n
        self.next_band(5)
        b5_t = Tex(r"$128 + 64 + 32 + \ldots$ with $r = \tfrac{1}{2}$").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"-1 < r < 1 \;\Rightarrow\; S_\infty \text{ exists}").scale(1.0).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"S_\infty = \frac{a}{1 - r} = \frac{128}{\tfrac{1}{2}} = 256").scale(1.0).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = MathTex(r"S_n > 255: \; (\tfrac{1}{2})^n < \tfrac{1}{256} = (\tfrac{1}{2})^8").scale(0.85).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = MathTex(r"n > 8 \;\Rightarrow\; \text{smallest } n = 9").scale(1.0).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex(r"Sigma count: $k = 3$ to $20$ gives $18$ terms").scale(0.9).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_3): the graph checklist on a hyperbola
        self.next_band(6)
        b6_t = Tex(r"$f(x) = \dfrac{2}{x-1} + 3$ — the checklist").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = MathTex(r"\text{VA: } x = 1 \qquad \text{HA: } y = 3").scale(1.05).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"y\text{-int: } \frac{2}{-1} + 3 = 1").scale(1.05).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"x\text{-int: } \frac{2}{x-1} = -3 \Rightarrow x = \tfrac{1}{3}").scale(0.95).shift(band_shift(6) + DOWN * 1.0)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex("Four facts, four marks, before sketching").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_3): inverses — reflect across y = x
        self.next_band(7)
        b7_t = Tex(r"Inverses: reflect across $y = x$").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = MathTex(r"g(x) = 3^x \;\Rightarrow\; g^{-1}(x) = \log_3 x").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"(2; 9) \text{ on } g \;\Rightarrow\; (9; 2) \text{ on } g^{-1}").scale(0.95).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Domain and range swap wholesale").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex(r"$y = x^2$: restrict to $x \ge 0$ or $x \le 0$").scale(0.95).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("else the reflection fails the line test").scale(0.95).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_3): finance — effective rate and the annuity
        self.next_band(8)
        b8_t = Tex("Finance: two skills").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(1.5)
        b8_l1 = MathTex(r"\text{effective} = (1{,}02)^4 - 1 = 8{,}24\%").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex(r"Loan R900\,000 at 10,5\% monthly, $n = 240$").scale(0.9).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = MathTex(r"x = \frac{P \cdot i}{1 - (1+i)^{-n}}, \quad i = 0{,}00875").scale(0.9).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = MathTex(r"x = \text{R}8\,985{,}42").scale(1.05).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2)
        b8_l5 = Tex(r"Total $\approx$ R2,16 million — over double").scale(0.9).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_4): first principles, limit kept visible
        self.next_band(9)
        b9_t = Tex(r"First principles: $f(x) = 3x^2 - 2$").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(1.5)
        b9_l1 = MathTex(r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}").scale(0.95).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"f(x+h) = 3x^2 + 6xh + 3h^2 - 2").scale(0.95).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"\frac{6xh + 3h^2}{h} = 6x + 3h").scale(1.0).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = MathTex(r"f'(x) = \lim_{h \to 0}(6x + 3h) = 6x").scale(1.0).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        b9_l5 = Tex("Keep the limit symbol until it is used").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_4): the rules, after rewriting
        self.next_band(10)
        b10_t = Tex(r"Rewrite first: $y = 4x^3 - \sqrt{x} + \dfrac{2}{x}$").scale(1.0).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = MathTex(r"y = 4x^3 - x^{\frac{1}{2}} + 2x^{-1}").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"\frac{dy}{dx} = 12x^2 - \tfrac{1}{2}x^{-\frac{1}{2}} - 2x^{-2}").scale(0.95).shift(band_shift(10) + UP * 0.0)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = Tex(r"The rule only sees powers of $x$").scale(1.0).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l3))
        self.wait(3)

        # --- Band 11 (subtopic_4): the cubic anatomised
        self.next_band(11)
        b11_t = Tex(r"Cubic: $f(x) = x^3 - 6x^2 + 9x = x(x-3)^2$").scale(0.95).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(2)
        b11_l1 = MathTex(r"x\text{-ints: } 0 \text{ and } 3 \; (\text{double root: touch})").scale(0.85).shift(band_shift(11) + UP * 1.2)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = MathTex(r"f'(x) = 3x^2 - 12x + 9 = 0").scale(1.0).shift(band_shift(11) + UP * 0.3)
        self.play(Write(b11_l2))
        self.wait(2)
        b11_l3 = MathTex(r"x = 1 \; \text{ or } \; x = 3").scale(1.0).shift(band_shift(11) + DOWN * 0.5)
        self.play(Write(b11_l3))
        self.wait(2)
        b11_l4 = MathTex(r"\text{max } (1; 4), \quad \text{min } (3; 0)").scale(1.0).shift(band_shift(11) + DOWN * 1.4)
        self.play(Write(b11_l4))
        self.play(Create(SurroundingRectangle(b11_l4, color=GREEN)))
        self.wait(2)
        b11_l5 = MathTex(r"\text{inflection } (2; 2)").scale(1.0).shift(band_shift(11) + DOWN * 2.4)
        self.play(Write(b11_l5))
        self.wait(3)

        # --- Band 12 (subtopic_4): probability closes the paper
        self.next_band(12)
        b12_t = Tex(r"Probability: independent $A$ and $B$").scale(1.1).shift(band_shift(12) + UP * 2.2)
        self.play(Write(b12_t))
        self.wait(1.5)
        b12_l1 = MathTex(r"P(A \text{ and } B) = 0{,}4 \times 0{,}5 = 0{,}2").scale(0.95).shift(band_shift(12) + UP * 1.1)
        self.play(Write(b12_l1))
        self.wait(2.5)
        b12_l2 = MathTex(r"P(A \text{ or } B) = 0{,}4 + 0{,}5 - 0{,}2 = 0{,}7").scale(0.95).shift(band_shift(12) + UP * 0.1)
        self.play(Write(b12_l2))
        self.play(Create(SurroundingRectangle(b12_l2, color=GREEN)))
        self.wait(2.5)
        b12_l3 = Tex("REVISION: 8 letters, I appearing twice").scale(0.95).shift(band_shift(12) + DOWN * 1.0)
        self.play(Write(b12_l3))
        self.wait(2)
        b12_l4 = MathTex(r"\frac{8!}{2!} = 20\,160").scale(1.1).shift(band_shift(12) + DOWN * 2.0)
        self.play(Write(b12_l4))
        self.play(Create(SurroundingRectangle(b12_l4, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 13 (subtopic_5): the map of Paper One
        self.next_band(13)
        b13_t = Tex("The map of Paper One").scale(1.2).shift(band_shift(13) + UP * 2.2)
        self.play(Write(b13_t))
        self.wait(2)
        b13_l1 = MathTex(r"\text{Functions } 35 \quad \text{Calculus } 35").scale(1.0).shift(band_shift(13) + UP * 1.2)
        self.play(Write(b13_l1))
        self.wait(2.5)
        b13_l2 = MathTex(r"\text{Algebra } 25 \quad \text{Patterns } 25").scale(1.0).shift(band_shift(13) + UP * 0.3)
        self.play(Write(b13_l2))
        self.wait(2.5)
        b13_l3 = MathTex(r"\text{Finance } 15 \; \text{Probability } 15 \; = 150").scale(0.85).shift(band_shift(13) + DOWN * 0.6)
        self.play(Write(b13_l3))
        self.wait(2.5)
        b13_l4 = Tex("70 of 150 live in functions + calculus").scale(0.95).shift(band_shift(13) + DOWN * 1.6)
        self.play(Write(b13_l4))
        self.wait(2.5)
        b13_l5 = Tex("Never camp on a stalled question").scale(1.0).shift(band_shift(13) + DOWN * 2.6)
        self.play(Write(b13_l5))
        self.wait(3.5)

        # --- Band 14 (subtopic_6): five shapes that repeat every year
        self.next_band(14)
        b14_t = Tex("Five shapes that repeat every year").scale(1.1).shift(band_shift(14) + UP * 2.2)
        self.play(Write(b14_t))
        self.wait(2)
        b14_l1 = Tex(r"1. Two decimals $\Rightarrow$ quadratic formula").scale(0.9).shift(band_shift(14) + UP * 1.3)
        self.play(Write(b14_l1))
        self.wait(2.5)
        b14_l2 = Tex(r"2. $x$ in the exponent twice $\Rightarrow$ $k$-method").scale(0.9).shift(band_shift(14) + UP * 0.5)
        self.play(Write(b14_l2))
        self.wait(2.5)
        b14_l3 = Tex(r"3. Pattern $\Rightarrow$ differences, solve for $n$").scale(0.9).shift(band_shift(14) + DOWN * 0.3)
        self.play(Write(b14_l3))
        self.wait(2.5)
        b14_l4 = Tex("4. Graphs: shape, asymptotes, intercepts").scale(0.9).shift(band_shift(14) + DOWN * 1.1)
        self.play(Write(b14_l4))
        self.wait(2.5)
        b14_l5 = Tex("5. Cubic: factorise, differentiate, touch or cut").scale(0.85).shift(band_shift(14) + DOWN * 1.9)
        self.play(Write(b14_l5))
        self.wait(2)
        b14_l6 = Tex("Same shapes, new numbers").scale(1.05).shift(band_shift(14) + DOWN * 2.8)
        self.play(Write(b14_l6))
        self.play(Create(SurroundingRectangle(b14_l6, color=GREEN)))
        self.wait(3.5)

        # --- Band 15 (subtopic_7): the donation list
        self.next_band(15)
        b15_t = Tex("The donation list").scale(1.2).shift(band_shift(15) + UP * 2.2)
        self.play(Write(b15_t))
        self.wait(2)
        b15_l1 = Tex("1. Rounding too early — round once, at the end").scale(0.85).shift(band_shift(15) + UP * 1.3)
        self.play(Write(b15_l1))
        self.wait(2.5)
        b15_l2 = Tex("2. Surd answers unchecked — substitute back").scale(0.85).shift(band_shift(15) + UP * 0.5)
        self.play(Write(b15_l2))
        self.wait(2.5)
        b15_l3 = Tex("3. The missing second answer — find both").scale(0.85).shift(band_shift(15) + DOWN * 0.3)
        self.play(Write(b15_l3))
        self.wait(2.5)
        b15_l4 = Tex("4. Finance without a timeline — sketch it").scale(0.85).shift(band_shift(15) + DOWN * 1.1)
        self.play(Write(b15_l4))
        self.wait(2.5)
        b15_l5 = Tex("5. Calculus notation — keep the limit written").scale(0.85).shift(band_shift(15) + DOWN * 1.9)
        self.play(Write(b15_l5))
        self.wait(2.5)
        b15_l6 = Tex("After every answer: one check, one line").scale(0.9).shift(band_shift(15) + DOWN * 2.8)
        self.play(Write(b15_l6))
        self.play(Create(SurroundingRectangle(b15_l6, color=GREEN)))
        self.wait(4)
