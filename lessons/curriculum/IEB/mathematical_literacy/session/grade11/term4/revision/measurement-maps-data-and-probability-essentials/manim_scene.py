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

# Band-layout whiteboard scene for the Measurement, Maps, Data and Probability
# Essentials revision duo. Part 1 — Expert: subtopics 1-4 (conversions &
# costing, scales & plans, data summaries, probability). Part 2 — Simplifier:
# subtopics 5-7 walk the same fix-up with a shopping list. Durations
# 240/245/240/250/190/195/200 of 1560 s. Exporter-safe mobjects only;
# add-only lifecycle; camera moves down one band per teaching beat.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MeasurementMapsDataProbabilityEssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(16)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the metric ladder ---
        title = Tex("Measurement, Maps, Data, Probability").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"4,7\text{ km} = 4\;700\text{ m}").scale(1.1).shift(UP * 1.1)
        b0_l2 = MathTex(r"60\text{ mm} = 6\text{ cm}").scale(1.1).shift(UP * 0.2)
        b0_l3 = MathTex(r"1\text{ m}^3 = 1\;000 \text{ litres}").scale(1.1).shift(DOWN * 0.7)
        b0_l4 = Tex("Same unit before multiplying — price's unit").scale(1.05).shift(DOWN * 1.7)
        self.play(Write(b0_l1)); self.wait(2)
        self.play(Write(b0_l2)); self.wait(2)
        self.play(Write(b0_l3)); self.wait(2)
        self.play(Write(b0_l4)); self.wait(3)

        # --- Band 1 (subtopic_1): tiles and paint, costed ---
        self.next_band(1)
        b1_title = Tex("Convert, calculate, round UP, price").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"5,2 \times 3,6 = 18,72\text{ m}^2").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"18,72 \div 1,6 = 11,7 \to 12 \text{ boxes}").scale(1.05).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"12 \times \text{R}210 = \text{R2 520}").scale(1.1).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        b1_l4 = MathTex(r"\text{Paint: } 13,5 \times 2 = 27; \; 27 \div 9 = 3 \text{ litres}").scale(0.95).shift(band_shift(1) + DOWN * 1.8)
        b1_l5 = Tex("One 5-litre tin — reasoning shown").scale(1.0).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l4)); self.wait(2)
        self.play(Write(b1_l5)); self.wait(3)

        # --- Band 2 (subtopic_2): the street map at 1 : 25 000 ---
        self.next_band(2)
        b2_title = Tex("Street map: scale 1 : 25 000").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"6,4 \times 25\;000 = 160\;000\text{ cm}").scale(1.1).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"160\;000\text{ cm} = 1,6\text{ km}").scale(1.1).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1)); self.wait(2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2)
        b2_l3 = Tex("Store sits SOUTH-EAST of the flat").scale(1.05).shift(band_shift(2) + DOWN * 0.8)
        b2_l4 = Tex("Routes: turns and landmarks, in order").scale(1.05).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l3)); self.wait(2.5)
        self.play(Write(b2_l4)); self.wait(3)

        # --- Band 3 (subtopic_2): the builder's plan at 1 : 50 ---
        self.next_band(3)
        b3_title = Tex("Builder's plan: 1 mm = 50 mm").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"84 \times 50 = 4\;200\text{ mm} = 4,2\text{ m}").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"\text{Reverse: } 1\;600 \div 50 = 32\text{ mm}").scale(1.05).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"50 \times 64\text{ mm} \to 2,5 \times 3,2\text{ m} = 8\text{ m}^2").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = Tex("Plan feeds the materials bill").scale(1.05).shift(band_shift(3) + DOWN * 1.7)
        b3_l5 = Tex("Photocopies lie; the bar scale doesn't").scale(1.05).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l1)); self.wait(2)
        self.play(Write(b3_l2)); self.wait(2)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        self.play(Write(b3_l4)); self.wait(2)
        self.play(Write(b3_l5)); self.wait(3)

        # --- Band 4 (subtopic_3): seven quotes, four summaries ---
        self.next_band(4)
        b4_title = Tex("Seven waterproofing quotes (R hundreds)").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_data = MathTex(r"13,\;17,\;17,\;20,\;23,\;24,\;26").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_data)); self.wait(2)
        b4_l1 = MathTex(r"\text{Mean: } 140 \div 7 = 20").scale(1.05).shift(band_shift(4) + UP * 0.2)
        b4_l2 = MathTex(r"\text{Median: 4th value} = 20").scale(1.05).shift(band_shift(4) + DOWN * 0.7)
        b4_l3 = MathTex(r"\text{Mode: } 17 \quad \text{Range: } 26 - 13 = 13").scale(1.05).shift(band_shift(4) + DOWN * 1.6)
        b4_l4 = Tex("Mean = median: balanced data").scale(1.05).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l1)); self.wait(2)
        self.play(Write(b4_l2)); self.wait(2)
        self.play(Write(b4_l3)); self.wait(2)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): comparing centre AND spread ---
        self.next_band(5)
        b5_title = Tex("Two contractors, one verdict").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"\text{A: mean } 20, \text{ range } 13").scale(1.1).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"\text{B: mean } 20, \text{ range } 5").scale(1.1).shift(band_shift(5) + UP * 0.2)
        b5_l3 = Tex("Same centre, different spread — B is reliable").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        b5_l4 = Tex("Categorical data takes a mode, never a mean").scale(1.0).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l1)); self.wait(2)
        self.play(Write(b5_l2)); self.wait(2)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        self.play(Write(b5_l4)); self.wait(3)

        # --- Band 6 (subtopic_4): the two-way table ---
        self.next_band(6)
        b6_title = Tex("Two-way table: 50 learners").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        # Table: rows girls/boys margin, columns minibus/walk
        tbl = Rectangle(width=6.4, height=2.4).shift(band_shift(6) + UP * 0.4)
        hline = Line(tbl.get_left(), tbl.get_right(), stroke_width=2)
        self.play(Create(tbl), Create(hline))
        c1 = Tex("Minibus: 30 (girls 15)").scale(0.95).shift(band_shift(6) + UP * 0.95)
        c2 = Tex("Walk: 20 (girls 10)").scale(0.95).shift(band_shift(6) + DOWN * 0.15)
        self.play(Write(c1)); self.wait(1.5)
        self.play(Write(c2)); self.wait(2)
        b6_l1 = MathTex(r"P(\text{minibus}) = \tfrac{30}{50} = 0,6").scale(1.05).shift(band_shift(6) + DOWN * 1.2)
        b6_l2 = MathTex(r"P(\text{girl and minibus}) = \tfrac{15}{50} = \tfrac{3}{10}").scale(1.0).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_l1)); self.wait(2)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): tree diagrams and fairness ---
        self.next_band(7)
        b7_title = Tex("Trees: multiply along, add across").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"P(\text{power off}) = 0,4; \;\; P(\text{late} \mid \text{off}) = 0,5").scale(0.95).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"0,4 \times 0,5 = 0,2").scale(1.15).shift(band_shift(7) + UP * 0.2)
        b7_l3 = MathTex(r"P(\text{power on}) = 1 - 0,4 = 0,6").scale(1.05).shift(band_shift(7) + DOWN * 0.8)
        b7_l4 = MathTex(r"\text{Spinner: red} = \tfrac{1}{4} = 0,25").scale(1.05).shift(band_shift(7) + DOWN * 1.8)
        b7_l5 = Tex("0,2 means about 20 in 100 — no promise").scale(1.0).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l1)); self.wait(2.5)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2)
        self.play(Write(b7_l3)); self.wait(2)
        self.play(Write(b7_l4)); self.wait(2)
        self.play(Write(b7_l5)); self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): buy enough, not too much ---
        self.next_band(8)
        b8_title = Tex("Buy enough, not too much").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2.5)
        b8_l1 = MathTex(r"11,7 \text{ boxes: } 11 \text{ leaves bare screed}").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = MathTex(r"12 \times \text{R}210 = \text{R2 520}").scale(1.1).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex("Two coats: the roller travels 27, not 13,5").scale(1.05).shift(band_shift(8) + DOWN * 0.8)
        b8_l4 = Tex("Estimate first: about 5 by 3,5, call it 18").scale(1.05).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l1)); self.wait(3)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(3)
        self.play(Write(b8_l3)); self.wait(3)
        self.play(Write(b8_l4)); self.wait(3.5)

        # --- Band 9 (subtopic_6): the plan is the house, folded small ---
        self.next_band(9)
        b9_title = Tex("The plan is the house, folded small").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = MathTex(r"\text{Un-fold: } 84 \times 50 = 4\;200\text{ mm}").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"\text{Fold: } 1\;600 \div 50 = 32\text{ mm}").scale(1.05).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex("Reality is always the big number").scale(1.05).shift(band_shift(9) + DOWN * 0.7)
        b9_l4 = MathTex(r"\text{Map: } 6,4\text{ cm} \to 1,6\text{ km}").scale(1.05).shift(band_shift(9) + DOWN * 1.6)
        b9_l5 = Tex("Trust the bar scale, not the photocopy").scale(1.05).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l1)); self.wait(3)
        self.play(Write(b9_l2)); self.wait(3)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(3)
        self.play(Write(b9_l4)); self.wait(3)
        self.play(Write(b9_l5)); self.wait(3)

        # --- Band 10 (subtopic_7): quotes, chances and promises ---
        self.next_band(10)
        b10_title = Tex("Deciding with numbers").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2.5)
        b10_l1 = Tex("A wild 52 joins: mean jumps, median holds").scale(1.05).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("Spread is trust: the huddled contractor wins").scale(1.05).shift(band_shift(10) + UP * 0.2)
        b10_l3 = MathTex(r"0,4 \times 0,5 = 0,2 \;\text{(20 evenings in 100)}").scale(1.0).shift(band_shift(10) + DOWN * 0.8)
        b10_l4 = MathTex(r"\text{Scratch cards: } \tfrac{1}{4} = 0,25 \text{ promised}").scale(1.0).shift(band_shift(10) + DOWN * 1.8)
        b10_l5 = Tex("If winners are rarer, the data votes no").scale(1.05).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l1)); self.wait(3)
        self.play(Write(b10_l2)); self.wait(3)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(3)
        self.play(Write(b10_l4)); self.wait(3)
        self.play(Write(b10_l5)); self.wait(4)
