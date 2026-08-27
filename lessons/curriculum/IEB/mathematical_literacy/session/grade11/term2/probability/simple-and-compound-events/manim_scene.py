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
# (210/220/230/230/190/195/200 of 1475 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SimpleAndCompoundEventsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the 0-to-1 scale ---
        title = Tex("Simple and Compound Events").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        scale_line = Line(LEFT * 4.5 + UP * 0.9, RIGHT * 4.5 + UP * 0.9)
        self.play(Create(scale_line))
        s0 = Tex("0 impossible").scale(0.85).shift(LEFT * 4.3 + UP * 0.3)
        s5 = Tex("0,5 even chance").scale(0.85).shift(UP * 0.3)
        s1 = Tex("1 certain").scale(0.85).shift(RIGHT * 4.3 + UP * 0.3)
        self.play(Write(s0), Write(s5), Write(s1))
        self.wait(2.5)
        l1 = Tex("Outcome: one result. Event: the outcomes you care about.").scale(0.9).shift(DOWN * 0.7)
        l2 = Tex(r"Three outfits: $\tfrac{1}{2}$, \; 0,5, \; 50\% — same chance").scale(1.0).shift(DOWN * 1.6)
        self.play(Write(l1)); self.wait(2.5)
        self.play(Write(l2)); self.wait(2.5)

        # --- Band 1 (subtopic_1): theoretical probability ---
        self.next_band(1)
        b1_title = Tex("Counting the equally likely").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"P(\text{greater than 4}) = \tfrac{2}{6} = \tfrac{1}{3}").scale(1.1).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"P(\text{WIN on the wheel}) = \tfrac{1}{10} = 0{,}1 = 10\%").scale(1.0).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l1)); self.wait(2.5)
        self.play(Write(b1_l2)); self.wait(2.5)
        b1_l3 = MathTex(r"P(\text{lose}) = 1 - \tfrac{1}{10} = \tfrac{9}{10}").scale(1.1).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_wrong = MathTex(r"P = 1{,}3 \quad \text{(off the scale — always wrong)}").scale(1.0).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): relative frequency ---
        self.next_band(2)
        b2_title = Tex("Watching instead of calculating").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Minibuses own no symmetry — so watch").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1)); self.wait(2.5)
        b2_l2 = MathTex(r"\text{Full on 18 of 50 mornings: } \tfrac{18}{50} = 0{,}36").scale(1.05).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = Tex("Relative frequency $=$ times it happened $\\div$ trials").scale(0.95).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3)); self.wait(2.5)
        b2_l4 = Tex("Coins and dice: theory. Rain and breakdowns: data.").scale(0.95).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4)); self.wait(2.5)

        # --- Band 3 (subtopic_2): the wobble, and the fair-coin verdict ---
        self.next_band(3)
        b3_title = Tex("Relative frequency wobbles").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("8 heads in 10 flips: a small sample. 800 in 1\\,000: loaded.").scale(0.9).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1)); self.wait(2.5)
        b3_l2 = Tex("More trials $\\Rightarrow$ the estimate settles toward the truth").scale(0.9).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2)); self.wait(2.5)
        b3_l3 = MathTex(r"\text{250 flips, 110 heads: theory } 0{,}5, \text{ watched } \tfrac{110}{250} = 0{,}44").scale(0.76).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3)); self.wait(2.5)
        b3_l4 = Tex(r"``0,44 sits close to 0,5, so the coin looks fair''").scale(0.95).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): the tree diagram ---
        self.next_band(4)
        b4_title = Tex("Two tosses: the tree catches every journey").scale(1.05).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        root = band_shift(4) + LEFT * 4.6 + UP * 0.4
        n_h = band_shift(4) + LEFT * 1.6 + UP * 1.5
        n_t = band_shift(4) + LEFT * 1.6 + DOWN * 0.7
        e_hh = band_shift(4) + RIGHT * 1.4 + UP * 2.0
        e_ht = band_shift(4) + RIGHT * 1.4 + UP * 1.0
        e_th = band_shift(4) + RIGHT * 1.4 + DOWN * 0.2
        e_tt = band_shift(4) + RIGHT * 1.4 + DOWN * 1.2
        self.play(Create(Line(root, n_h)), Create(Line(root, n_t)))
        lab_h = Tex(r"H $\tfrac{1}{2}$").scale(0.9).shift(n_h + LEFT * 0.7)
        lab_t = Tex(r"T $\tfrac{1}{2}$").scale(0.9).shift(n_t + LEFT * 0.7)
        self.play(Write(lab_h), Write(lab_t))
        self.wait(2)
        self.play(Create(Line(n_h, e_hh)), Create(Line(n_h, e_ht)),
                  Create(Line(n_t, e_th)), Create(Line(n_t, e_tt)))
        lab_hh = Tex(r"HH $\tfrac{1}{4}$").scale(0.9).shift(e_hh + RIGHT * 0.9)
        lab_ht = Tex(r"HT $\tfrac{1}{4}$").scale(0.9).shift(e_ht + RIGHT * 0.9)
        lab_th = Tex(r"TH $\tfrac{1}{4}$").scale(0.9).shift(e_th + RIGHT * 0.9)
        lab_tt = Tex(r"TT $\tfrac{1}{4}$").scale(0.9).shift(e_tt + RIGHT * 0.9)
        self.play(Write(lab_hh), Write(lab_ht), Write(lab_th), Write(lab_tt))
        self.wait(2.5)
        b4_l1 = MathTex(r"P(2\text{ tails}) = \tfrac{1}{4}; \;\; P(\text{exactly one}) = \tfrac{2}{4} = \tfrac{1}{2}").scale(0.79).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4_l1)); self.wait(2.5)
        b4_l2 = MathTex(r"P(\text{at least one tail}) = 1 - \tfrac{1}{4} = \tfrac{3}{4}").scale(0.95).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): multiply along the branches ---
        self.next_band(5)
        b5_title = Tex(r"Unequal branches: rolls run out one day in ten").scale(1.0).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"\text{Rolls both days: } 0{,}9 \times 0{,}9 = 0{,}81").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"\text{Sold out both days: } 0{,}1 \times 0{,}1 = 0{,}01").scale(1.05).shift(band_shift(5) + UP * 0.2)
        b5_l3 = MathTex(r"\text{One yes, one no: } 1 - 0{,}81 - 0{,}01 = 0{,}18").scale(1.05).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l1)); self.wait(2.5)
        self.play(Write(b5_l2)); self.wait(2.5)
        self.play(Write(b5_l3)); self.wait(2.5)
        b5_l4 = MathTex(r"0{,}81 + 0{,}01 + 0{,}18 = 1 \;\checkmark").scale(1.05).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the two-way table ---
        self.next_band(6)
        b6_title = Tex("150 visitors, two facts each").scale(1.1).shift(band_shift(6) + UP * 2.7)
        self.play(Write(b6_title))
        self.wait(1.5)
        grid = Rectangle(width=9.6, height=3.6).shift(band_shift(6) + DOWN * 0.1)
        self.play(Create(grid))
        h_line = Line(band_shift(6) + LEFT * 4.8 + UP * 0.5, band_shift(6) + RIGHT * 4.8 + UP * 0.5)
        v_line = Line(band_shift(6) + LEFT * 0.4 + UP * 1.7, band_shift(6) + LEFT * 0.4 + DOWN * 1.9)
        self.play(Create(h_line), Create(v_line))
        head = Tex(r"\quad Minibus \quad Walk \quad Total").scale(0.95).shift(band_shift(6) + UP * 1.2 + RIGHT * 1.3)
        self.play(Write(head))
        r1 = Tex(r"Learners: \; 36 \quad 54 \quad 90").scale(0.95).shift(band_shift(6) + UP * 0.0)
        r2 = Tex(r"Adults: \; 24 \quad 36 \quad 60").scale(0.95).shift(band_shift(6) + DOWN * 0.8)
        r3 = Tex(r"Total: \; 60 \quad 90 \quad 150").scale(0.95).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(r1)); self.wait(2)
        self.play(Write(r2)); self.wait(2)
        self.play(Write(r3)); self.wait(2)
        b6_l1 = Tex("Every row and column must add to its total — check it").scale(0.9).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l1)); self.wait(2.5)

        # --- Band 7 (subtopic_4): reading the grid ---
        self.next_band(7)
        b7_title = Tex("The wording picks the denominator").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"P(\text{learner}) = \tfrac{90}{150} = \tfrac{3}{5} = 0{,}6").scale(1.03).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"P(\text{adult AND minibus}) = \tfrac{24}{150} = 0{,}16").scale(1.05).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l1)); self.wait(2.5)
        self.play(Write(b7_l2)); self.wait(2.5)
        b7_l3 = MathTex(r"\text{GIVEN a learner: } \tfrac{36}{90} = 0{,}4").scale(1.1).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex(r"``Given that'' shrinks the world to one row or column").scale(0.95).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4)); self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): how sure is sure ---
        self.next_band(8)
        b8_title = Tex("One short ruler, 0 to 1").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2.5)
        b8_l1 = Tex("Never at 0, definitely at 1, coin toss in the middle").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1)); self.wait(3)
        b8_l2 = MathTex(r"\text{Red sweet blind: } \tfrac{4}{20} = \tfrac{1}{5}").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(3)
        b8_l3 = Tex(r"WIN $\tfrac{1}{10}$ means LOSE $\tfrac{9}{10}$ — together exactly 1").scale(0.95).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3)); self.wait(3)
        b8_l4 = Tex("A probability of 1,3 is not a big chance — it is broken").scale(0.95).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l4)); self.wait(3.5)

        # --- Band 9 (subtopic_6): fifty mornings at the minibus ---
        self.next_band(9)
        b9_title = Tex("The minibus you watched for fifty mornings").scale(1.05).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = MathTex(r"\text{Full 18 of 50: } \tfrac{18}{50} = 0{,}36").scale(1.1).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.play(Create(SurroundingRectangle(b9_l1, color=GREEN)))
        self.wait(3)
        b9_l2 = Tex("Watch, count, divide — the real world's chances").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2)); self.wait(3)
        b9_l3 = Tex("Fifty mornings: a solid watch. Five: gossip.").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3)); self.wait(3)
        b9_l4 = Tex(r"Theory 0,5, watching 0,44 — close, so the coin is fair").scale(0.95).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4)); self.wait(3.5)

        # --- Band 10 (subtopic_7): branches and grids ---
        self.next_band(10)
        b10_title = Tex("Journeys for sequences, cells for crowds").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2.5)
        b10_l1 = Tex(r"Multiply along the journey: $\tfrac{1}{2} \times \tfrac{1}{2} = \tfrac{1}{4}$ each route").scale(0.85).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1)); self.wait(3)
        b10_l2 = Tex("Exactly one tail: TWO journeys — the tree shows the one you lost").scale(0.83).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2)); self.wait(3)
        b10_l3 = MathTex(r"\text{Grid: } P(\text{learner}) = \tfrac{90}{150}; \;\; \text{given a learner: } \tfrac{36}{90}").scale(0.73).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(3)
        b10_l4 = Tex("Draw the picture first; let it do the counting").scale(1.0).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_l4)); self.wait(4)
