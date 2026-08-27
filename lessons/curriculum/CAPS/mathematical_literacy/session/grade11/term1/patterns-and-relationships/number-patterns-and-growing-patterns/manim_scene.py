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

# Band layout: one frame-height band per teaching beat; the camera moves down,
# nothing is removed. Exporter-supported mobjects only (Tex/MathTex/Line/
# Rectangle/SurroundingRectangle); single-string Write reveals throughout.
#
# Covers all seven subtopics (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7),
# band time roughly proportional to subtopics.json
# (230/235/225/240/195/185/190 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class NumberPatternsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the three families ---
        title = Tex("Number Patterns and Growing Patterns").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        f1 = Tex(r"1. Constant difference: $13;\ 20;\ 27;\ 34$ (add 7)").scale(1.05).shift(UP * 1.1)
        f2 = Tex(r"2. Constant ratio: $5;\ 10;\ 20;\ 40$ ($\times$ 2)").scale(1.05).shift(UP * 0.2)
        f3 = Tex(r"3. Growing step: $1;\ 3;\ 6;\ 10$ (steps 2, 3, 4)").scale(1.05).shift(DOWN * 0.7)
        self.play(Write(f1)); self.wait(2.5)
        self.play(Write(f2)); self.wait(2.5)
        self.play(Write(f3)); self.wait(2.5)
        rule = Tex("Naming the family is half the marks").scale(1.05).shift(DOWN * 1.7)
        self.play(Write(rule))
        self.play(Create(SurroundingRectangle(rule, color=GREEN)))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the vocabulary ---
        self.next_band(1)
        b1_title = Tex("The words the paper expects").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("TERMS: the numbers in the list").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("POSITION: first term, second term, ...").scale(1.05).shift(band_shift(1) + UP * 0.2)
        b1_l3 = Tex("CONSECUTIVE: terms standing next to each other").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l1)); self.wait(2.5)
        self.play(Write(b1_l2)); self.wait(2.5)
        self.play(Write(b1_l3)); self.wait(2.5)
        b1_l4 = Tex(r"Describe in words: ``add 7 to each term''").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l4)); self.wait(2.5)

        # --- Band 2 (subtopic_2): the difference row ---
        self.next_band(2)
        b2_title = Tex("The difference row — your first test").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"13 \qquad 20 \qquad 27 \qquad 34").scale(1.2).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"+7 \qquad +7 \qquad +7").scale(1.05).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l1)); self.wait(2)
        self.play(Write(b2_l2)); self.wait(2.5)
        b2_l3 = MathTex(r"34 + 7 = 41; \quad 41 + 7 = 48").scale(1.1).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l3)); self.wait(2.5)
        b2_l4 = Tex(r"Missing term: $20 + 7 = 27$ and $34 - 7 = 27$").scale(1.0).shift(band_shift(2) + DOWN * 1.7)
        b2_l5 = Tex("Check from BOTH sides — both walks must agree").scale(1.0).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l4)); self.wait(2.5)
        self.play(Write(b2_l5)); self.wait(2.5)

        # --- Band 3 (subtopic_2): the tariff wrapper ---
        self.next_band(3)
        b3_title = Tex("The courier tariff: R13, then R7 per km").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"13;\ 20;\ 27;\ 34 = \text{cost of }1, 2, 3, 4\text{ km}").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1)); self.wait(2.5)
        b3_l2 = MathTex(r"41;\ 48;\ 55 \quad \text{(5, 6, 7 km)}").scale(1.1).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2)); self.wait(2.5)
        b3_l3 = MathTex(r"\text{Seven kilometres costs } R55").scale(1.15).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("Answer inside the story: R55, never a naked 55").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        b3_l5 = Tex("Count positions on your fingers as you extend").scale(1.0).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l4)); self.wait(2)
        self.play(Write(b3_l5)); self.wait(2.5)

        # --- Band 4 (subtopic_3): the ratio test ---
        self.next_band(4)
        b4_title = Tex("When the difference row refuses").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"5 \qquad 10 \qquad 20 \qquad 40").scale(1.2).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex(r"Differences 5, 10, 20 — not constant, doubling!").scale(1.0).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l1)); self.wait(2)
        self.play(Write(b4_l2)); self.wait(2.5)
        b4_l3 = MathTex(r"10 \div 5 = 2; \;\; 20 \div 10 = 2; \;\; 40 \div 20 = 2").scale(1.05).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3)); self.wait(2.5)
        b4_l4 = MathTex(r"40 \times 2 = 80; \quad 80 \times 2 = 160").scale(1.1).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): same amount vs same factor ---
        self.next_band(5)
        b5_title = Tex("Same amount vs same factor").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Adding R7 per km will never explode").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex(r"Doubling will never stay polite").scale(1.05).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1)); self.wait(2.5)
        self.play(Write(b5_l2)); self.wait(2.5)
        b5_l3 = MathTex(r"5 \to 80 \text{ in four doublings}; \; \to 1\,280 \text{ in four more}").scale(0.91).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3)); self.wait(2.5)
        b5_l4 = Tex(r"The ratio pattern wins EVENTUALLY — say ``eventually''").scale(0.95).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l4)); self.wait(3)

        # --- Band 6 (subtopic_4): the stacked-rows table ---
        self.next_band(6)
        b6_title = Tex("Stacked rows: 7 rows, one more each row").scale(1.1).shift(band_shift(6) + UP * 2.6)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Per row: $1;\ 2;\ 3;\ 4;\ 5;\ 6;\ 7$").scale(1.0).shift(band_shift(6) + UP * 1.8)
        b6_l2 = Tex(r"Totals: $1;\ 3;\ 6;\ 10;\ 15;\ 21;\ 28$ — steps grow by one").scale(0.95).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6_l1)); self.wait(2)
        self.play(Write(b6_l2)); self.wait(2.5)
        tbl = Rectangle(width=7.2, height=3.0).shift(band_shift(6) + DOWN * 0.9)
        self.play(Create(tbl))
        b6_r1 = Tex(r"Row: 1 \; 2 \; 3 \; 4 \; 5 \; 6 \; 7").scale(1.0).shift(band_shift(6) + DOWN * 0.3)
        b6_r2 = Tex(r"Total: 1 \; 3 \; 6 \; 10 \; 15 \; 21 \; 28").scale(1.0).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(b6_r1)); self.wait(2)
        self.play(Write(b6_r2)); self.wait(2.5)
        b6_ans = MathTex(r"\text{The decoration uses } 28 \text{ circles}").scale(1.1).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_ans))
        self.play(Create(SurroundingRectangle(b6_ans, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the pairing check and the trap ---
        self.next_band(7)
        b7_title = Tex("The pairing check").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"1 + 7 = 8; \;\; 2 + 6 = 8; \;\; 3 + 5 = 8").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"3 \times 8 + 4 = 28 \quad \text{— same answer, another road}").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1)); self.wait(2.5)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_wrong = Tex(r"Total asked, row answered: 7").scale(1.05).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_wrong))
        self.play(Create(strike(b7_wrong)))
        self.wait(2)
        b7_l3 = Tex(r"Seventh row $= 7$; all seven rows $= 28$").scale(1.05).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l3)); self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the steady staircase ---
        self.next_band(8)
        b8_title = Tex("A staircase with equal steps").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2.5)
        b8_l1 = Tex(r"Minibus zones: $13;\ 20;\ 27;\ 34$ — subtract neighbours").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1)); self.wait(3)
        b8_l2 = MathTex(r"20 - 13 = 7; \;\; 27 - 20 = 7 \quad \text{— the step is } 7").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2)); self.wait(3)
        b8_l3 = MathTex(r"34 + 7 = 41; \;\; 48; \;\; 55 \;\Rightarrow\; R55").scale(1.05).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(3)
        b8_l4 = Tex("Missing term: walk to it from both sides").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        b8_l5 = Tex("Keep the units — R55, not a naked 55").scale(1.0).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l4)); self.wait(2.5)
        self.play(Write(b8_l5)); self.wait(3)

        # --- Band 9 (subtopic_6): the rumour that doubles ---
        self.next_band(9)
        b9_title = Tex("The rumour that doubles").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = MathTex(r"5 \to 10 \to 20 \to 40 \quad \text{(nobody is adding)}").scale(1.05).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1)); self.wait(3)
        b9_l2 = Tex(r"Divide any hour by the hour before: always 2").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2)); self.wait(3)
        b9_l3 = Tex(r"Staircase trudges 55, 62, 69; rumour hits 320").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3)); self.wait(3)
        b9_l4 = Tex("Test order: subtract first; gaps unequal? divide").scale(1.0).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(3.5)

        # --- Band 10 (subtopic_7): cans at the shop ---
        self.next_band(10)
        b10_title = Tex("The pyramid of cans").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2.5)
        b10_l1 = Tex(r"Rows 1 to 7; totals $1;\ 3;\ 6;\ 10;\ 15;\ 21;\ 28$").scale(0.95).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1)); self.wait(3)
        b10_l2 = Tex(r"Gaps 2, 3, 4, 5 — the step itself grows by one").scale(1.0).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2)); self.wait(3)
        b10_l3 = MathTex(r"1 + 2 + 3 + 4 + 5 + 6 + 7 = 28 \text{ cans}").scale(1.05).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(3)
        b10_l4 = MathTex(r"\text{Check: } 3 \times 8 + 4 = 28").scale(1.0).shift(band_shift(10) + DOWN * 1.8)
        b10_l5 = Tex("A row, or the whole stack? Read the last line slowly").scale(0.95).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l4)); self.wait(3)
        self.play(Write(b10_l5)); self.wait(4)
