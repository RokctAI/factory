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

# Band-layout whiteboard scene for "Charge and Coulomb's Law" (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). Exporter-safe mobjects
# only; write-only reveals; camera moves down band by band. Band time
# apportioned to subtopics.json (225/235/235/245/180/185/185 of 1490 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ChargeAndCoulombsLawSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): charge, unit, quantisation ---
        title = Tex("Charge and Coulomb's Law").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("two kinds: positive and negative").scale(1.0).shift(UP * 1.3)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("unit: the coulomb, C").scale(1.0).shift(UP * 0.5)
        self.play(Write(b0_l2))
        b0_l3 = MathTex(r"\mu\text{C} = 10^{-6}\;\text{C}, \quad \text{nC} = 10^{-9}\;\text{C}").scale(0.95).shift(DOWN * 0.4)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("quantised: whole multiples of").scale(0.95).shift(DOWN * 1.4)
        b0_l5 = MathTex(r"e = 1{,}6 \times 10^{-19}\;\text{C}").scale(1.0).shift(DOWN * 2.2)
        self.play(Write(b0_l4))
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): Q = nq both ways ---
        self.next_band(1)
        b1_t = MathTex(r"Q = nq").scale(1.4).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.play(Create(SurroundingRectangle(b1_t, color=GREEN)))
        self.wait(2)
        b1_l1 = MathTex(r"n = \frac{8 \times 10^{-18}}{1{,}6 \times 10^{-19}} = 50\ \text{electrons}").scale(0.95).shift(band_shift(1) + UP * 0.9)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("negative charge: EXCESS electrons — a count, no unit").scale(0.85).shift(band_shift(1) + UP * 0.0)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"Q = (2{,}5 \times 10^{11})(1{,}6 \times 10^{-19}) = 4 \times 10^{-8}\;\text{C}").scale(0.9).shift(band_shift(1) + DOWN * 1.1)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        b1_l4 = Tex("lost electrons: sign is POSITIVE").scale(0.95).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the three charging methods ---
        self.next_band(2)
        b2_t = Tex("Only electrons ever move").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.play(Create(SurroundingRectangle(b2_t, color=GREEN)))
        self.wait(2)
        b2_l1 = Tex("friction (insulators): opposite signs —").scale(0.9).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("stronger gripper strips the weaker").scale(0.9).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("contact (conductors): SAME sign — electrons spread").scale(0.85).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("induction (conductors): OPPOSITE sign,").scale(0.9).shift(band_shift(2) + DOWN * 1.6)
        b2_l5 = Tex("no touch at all").scale(0.9).shift(band_shift(2) + DOWN * 2.3)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): induction, drawn step by step ---
        self.next_band(3)
        b3_t = Tex("Induction, step by step").scale(1.15).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_t))
        self.wait(1.5)
        rod = Line(band_shift(3) + LEFT * 4.0 + UP * 1.0, band_shift(3) + LEFT * 2.6 + UP * 1.0, color=BLUE)
        rod_lab = Tex("negative rod").scale(0.75).shift(band_shift(3) + LEFT * 3.3 + UP * 1.6)
        ball = Circle(radius=0.9, color=WHITE).shift(band_shift(3) + RIGHT * 0.4 + UP * 1.0)
        self.play(Create(rod), Write(rod_lab), Create(ball))
        near = Tex("+").scale(1.1).shift(band_shift(3) + LEFT * 0.3 + UP * 1.0)
        far = Tex("--").scale(1.1).shift(band_shift(3) + RIGHT * 1.1 + UP * 1.0)
        self.play(Write(near), Write(far))
        self.wait(2)
        b3_l1 = Tex("1. electrons flee to the far side").scale(0.9).shift(band_shift(3) + DOWN * 0.4)
        b3_l2 = Tex("2. earth the far side: they drain away").scale(0.9).shift(band_shift(3) + DOWN * 1.1)
        b3_l3 = Tex("3. finger away FIRST, rod away second").scale(0.9).shift(band_shift(3) + DOWN * 1.8)
        b3_l4 = Tex("4. sphere left POSITIVE — opposite the rod").scale(0.9).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): conservation and the sharing rule ---
        self.next_band(4)
        b4_t = Tex("Conservation, and the equal split").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("charge is never created or destroyed —").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex("only transferred").scale(0.95).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(VGroup(b4_l1, b4_l2), color=GREEN)))
        self.wait(2)
        b4_l3 = MathTex(r"Q = \frac{Q_1 + Q_2}{2}\ \text{(identical spheres, signs in)}").scale(0.95).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"\frac{(-5) + (+1)}{2} = \frac{-4}{2} = -2\;\text{nC each}").scale(0.95).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): electrons transferred + the sign trap ---
        self.next_band(5)
        b5_t = Tex("Counting the moved electrons").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("P: from $-5$ nC to $-2$ nC — gave up 3 nC").scale(0.95).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"n = \frac{3 \times 10^{-9}}{1{,}6 \times 10^{-19}} = 1{,}875 \times 10^{10}").scale(1.0).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2)
        b5_l3 = Tex("add sizes, ignore signs: 3 nC each").scale(0.95).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5_l3))
        self.play(Create(strike(b5_l3)))
        self.wait(2)
        b5_l4 = Tex("and the halving is for IDENTICAL spheres only").scale(0.9).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): Coulomb's law worked ---
        self.next_band(6)
        b6_t = MathTex(r"F = \frac{kQ_1Q_2}{r^2}, \quad k = 9 \times 10^{9}").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.play(Create(SurroundingRectangle(b6_t, color=GREEN)))
        self.wait(2)
        b6_l1 = MathTex(r"F = \frac{(9 \times 10^{9})(2 \times 10^{-6})(6 \times 10^{-6})}{(0{,}20)^2}").scale(0.95).shift(band_shift(6) + UP * 0.7)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"= \frac{0{,}108}{0{,}04} = 2{,}7\;\text{N}").scale(1.05).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2)
        b6_l3 = Tex("unlike charges: ATTRACTION — said in words").scale(0.95).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l3))
        self.wait(3)

        # --- Band 7 (subtopic_4): inverse square + the named traps ---
        self.next_band(7)
        b7_t = Tex("The inverse square, and the traps").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = MathTex(r"r: 0{,}20 \to 0{,}40\;\text{m}: \quad F = \frac{0{,}108}{0{,}16} = 0{,}675\;\text{N}").scale(0.9).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("double the gap: QUARTER the force").scale(0.95).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2)
        b7_l3 = Tex("forgetting to square r").scale(0.9).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3))
        self.play(Create(strike(b7_l3)))
        b7_l4 = Tex("centimetres left in — a slip of ten thousand").scale(0.9).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l4))
        b7_l5 = Tex("magnitudes in the formula, direction in words").scale(0.9).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the balloon and the jersey ---
        self.next_band(8)
        b8_t = Tex("The balloon and the school jersey").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("rubbing scrapes electrons off wool onto rubber").scale(0.9).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("balloon negative, jersey positive —").scale(0.95).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex("nothing made, only moved").scale(0.95).shift(band_shift(8) + DOWN * 0.3)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex("wall's electrons pushed back: face turns").scale(0.9).shift(band_shift(8) + DOWN * 1.3)
        b8_l5 = Tex("slightly positive — the balloon hangs on").scale(0.9).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2)
        b8_l6 = Tex("whole electrons only: charge counts like marbles").scale(0.85).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_6): three pictures + the pocket-money split ---
        self.next_band(9)
        b9_t = Tex("Three ways in, one fair split").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("rub: opposites — shock season on dry carpets").scale(0.9).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("touch: same sign — electrons spread out").scale(0.9).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("bring near + earth: OPPOSITE sign, no touch").scale(0.9).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = MathTex(r"-5\ \text{and}\ +1: \ \frac{-4}{2} = -2\ \text{each}").scale(0.95).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex("pool WITH signs, then split — like pocket money").scale(0.85).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): close is strong ---
        self.next_band(10)
        b10_t = Tex("Close is strong").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("bigger charges: bigger force").scale(0.95).shift(band_shift(10) + UP * 1.3)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = Tex("double the distance: quarter the force —").scale(0.95).shift(band_shift(10) + UP * 0.5)
        b10_l3 = Tex("like stepping back from the braai fire").scale(0.95).shift(band_shift(10) + DOWN * 0.2)
        self.play(Write(b10_l2))
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = MathTex(r"\frac{0{,}108}{0{,}04} = 2{,}7\;\text{N}; \quad \frac{0{,}108}{0{,}16} = 0{,}675\;\text{N}").scale(0.9).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex("metres before you square; signs out, words in").scale(0.9).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(4)
