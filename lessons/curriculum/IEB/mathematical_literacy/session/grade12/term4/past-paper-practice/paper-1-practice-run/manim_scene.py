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

# Band-layout whiteboard scene for the Finance and Data practice-run session
# (an original 150-mark practice paper walked question by question). One band
# per teaching beat; the camera moves down and earlier work stays on the
# canvas. Exporter-supported mobjects only; every working line is its own
# single-string Tex/MathTex revealed with Write. No transforms, no FadeOut.
#
# Subtopic time shares (subtopics.json, total 900 s):
# 150/105/110/120/135/160/120 -> bands 0-1 / 2 / 3 / 4-5 / 6-7 / 8-9 / 10.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FinancePracticeRunSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(13)

        # --- Band 0 (subtopic_1): how the practice paper is built
        title = Tex("Finance Practice Run: 150 Marks").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Q1: 30 marks of single-step warm-ups").scale(1.05).shift(UP * 1.2)
        b0_l2 = Tex("Q2 Finance; Q3 Data Handling").scale(1.05).shift(UP * 0.4)
        b0_l3 = Tex("Q4--5 mix the two families").scale(1.05).shift(DOWN * 0.4)
        b0_l4 = Tex("Probability's few marks hide anywhere").scale(1.05).shift(DOWN * 1.2)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex("A third recall, a third routine, the rest reasoning").scale(0.95).shift(DOWN * 2.2)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): the mark allocation is the instruction
        self.next_band(1)
        b1_t = Tex("Read the mark allocation as an instruction").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("2 marks: one method mark, one answer mark").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("3 marks: a hidden middle step (a conversion)").scale(1.05).shift(band_shift(1) + UP * 0.2)
        b1_l3 = Tex("5 marks and up: a staged journey — each stage pays").scale(1.0).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("Follow-through: wrong numbers carried").scale(1.05).shift(band_shift(1) + DOWN * 1.7)
        b1_l5 = Tex("forward correctly KEEP paying — never stop").scale(1.05).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(VGroup(b1_l4, b1_l5), color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): Question One warm-ups, four specimens
        self.next_band(2)
        b2_t = Tex("Question One: the confidence deposit").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{VAT: } 180 \times 0{,}15 = \text{R}27{,}00; \;\text{total R}207{,}00").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"\text{Net pay: } 14\;650 - 2\;980 = \text{R}11\;670{,}00").scale(1.0).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"\text{Mode of } 9, 13, 13, 17, 20: \;\; 13").scale(1.05).shift(band_shift(2) + DOWN * 0.8)
        b2_l4 = MathTex(r"P(\text{green}) = \tfrac{1}{5}").scale(1.1).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Show the one line even for two marks").scale(1.05).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_3): the electricity block tariff, six marks
        self.next_band(3)
        b3_t = Tex("Q2.1 The tariff: a staircase, not a switch").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{First 100: } 100 \times 1{,}80 = \text{R}180{,}00").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"\text{101 to 400: } 300 \times 2{,}40 = \text{R}720{,}00").scale(1.0).shift(band_shift(3) + UP * 0.4)
        b3_l3 = MathTex(r"\text{401 to 460: } 60 \times 3{,}10 = \text{R}186{,}00").scale(1.0).shift(band_shift(3) + DOWN * 0.4)
        b3_l4 = MathTex(r"180 + 720 + 186 = \text{R}1\;086{,}00").scale(1.0).shift(band_shift(3) + DOWN * 1.2)
        b3_l5 = MathTex(r"\text{VAT: } 1\;086 \times 1{,}15 = \text{R}1\;248{,}90").scale(1.05).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(1.5)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(2)
        b3_l6 = MathTex(r"460 \times 3{,}10 \; \text{ — all at the top rate: never}").scale(0.95).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_l6))
        self.play(Create(strike(b3_l6)))
        self.wait(3)

        # --- Band 4 (subtopic_4): compound interest year by year
        self.next_band(4)
        b4_t = Tex("Q2.2 Compound interest: show the compounding").scale(1.0).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex(r"R9 500 at 7,2\% a year, three years").scale(1.05).shift(band_shift(4) + UP * 1.2)
        b4_l2 = MathTex(r"\text{Year 1: } 9\;500 \times 1{,}072 = \text{R}10\;184{,}00").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"\text{Year 2: } 10\;184 \times 1{,}072 = \text{R}10\;917{,}25").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = MathTex(r"\text{Year 3: full balance} \times 1{,}072 = \text{R}11\;703{,}29").scale(1.0).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2.5)
        b4_l5 = Tex("Each year's interest lands on the NEW balance").scale(1.0).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_4): interest earned, and compound vs simple
        self.next_band(5)
        b5_t = Tex("The follow-ups the paper loves").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"\text{Interest: } 11\;703{,}29 - 9\;500 = \text{R}2\;203{,}29").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"\text{Simple: } 9\;500 \times 0{,}072 = \text{R}684 \text{ per year}").scale(0.97).shift(band_shift(5) + UP * 0.2)
        b5_l3 = MathTex(r"3 \times 684 = \text{R}2\;052{,}00").scale(1.05).shift(band_shift(5) + DOWN * 0.7)
        b5_l4 = MathTex(r"\text{Compound wins by R}151{,}29").scale(1.05).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex("...because later interest grows on interest —").scale(1.0).shift(band_shift(5) + DOWN * 2.5)
        b5_l6 = Tex("the explanation mark needs that clause").scale(1.0).shift(band_shift(5) + DOWN * 3.2)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_5): summarising the test marks
        self.next_band(6)
        b6_t = Tex("Q3 Data: ten learners' percentages").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"41, 44, 49, 53, 57, 61, 64, 68, 74, 79").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = MathTex(r"\text{Range: } 79 - 41 = 38").scale(1.05).shift(band_shift(6) + UP * 0.3)
        b6_l3 = MathTex(r"\text{Mean: } 590 \div 10 = 59{,}0").scale(1.05).shift(band_shift(6) + DOWN * 0.6)
        b6_l4 = MathTex(r"\text{Median (even count): } \tfrac{57 + 61}{2} = 59{,}0").scale(1.05).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_l5 = Tex("Picking one middle value forfeits the marks").scale(1.0).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_5): quartiles, IQR and the honest comment
        self.next_band(7)
        b7_t = Tex("Quartiles and the reasoning marks").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = MathTex(r"Q_1 = 49 \text{ (3rd of lower five)} \qquad Q_3 = 68 \text{ (8th)}").scale(0.88).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"IQR = 68 - 49 = 19").scale(1.1).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex("Comment WITH calculations:").scale(1.05).shift(band_shift(7) + DOWN * 0.9)
        b7_l4 = Tex("mean 59,0 and median 59,0 agree — no outlier pull —").scale(0.95).shift(band_shift(7) + DOWN * 1.7)
        b7_l5 = Tex("but a quarter of the group scored below 49").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l3))
        self.wait(1.5)
        self.play(Write(b7_l4))
        self.wait(2)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): integrated question — chance and budget
        self.next_band(8)
        b8_t = Tex("Q4 Integrated: data, money, chance").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(1.5)
        b8_l1 = MathTex(r"P(\text{below } 50) = \tfrac{3}{10} = 0{,}3").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"\text{Costs: } 150 \times 7{,}20 = \text{R}1\;080{,}00").scale(1.0).shift(band_shift(8) + UP * 0.2)
        b8_l3 = MathTex(r"\text{Income: } 150 \times 12 = \text{R}1\;800; \; \text{profit R}720{,}00").scale(0.95).shift(band_shift(8) + DOWN * 0.7)
        b8_l4 = MathTex(r"\text{Only } 80\% \text{ sell: } 120 \times 12 = \text{R}1\;440{,}00").scale(1.0).shift(band_shift(8) + DOWN * 1.6)
        b8_l5 = MathTex(r"\text{Profit falls to } 1\;440 - 1\;080 = \text{R}360{,}00").scale(1.0).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(2)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the advice close
        self.next_band(9)
        b9_t = Tex("Advise with the number, not opinion").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(1.5)
        b9_l1 = MathTex(r"\text{Target R}950: \; 360 \text{ falls R}590 \text{ short}").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"120p - 1\;080 = 950").scale(1.1).shift(band_shift(9) + UP * 0.1)
        b9_l3 = MathTex(r"p = 2\;030 \div 120 = 16{,}9166").scale(1.05).shift(band_shift(9) + DOWN * 0.9)
        b9_l4 = MathTex(r"\text{Round UP: R}16{,}92").scale(1.1).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex("R16,91 banks R2 029,20 — eighty cents short").scale(1.0).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the five memo habits
        self.next_band(10)
        b10_t = Tex("Five memo habits that harvest marks").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(1.5)
        b10_l1 = Tex("1. Show substitution — structure banks the mark").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("2. Follow-through — finish every chain").scale(1.0).shift(band_shift(10) + UP * 0.4)
        b10_l3 = Tex("3. Units and form — R, two decimals, comma").scale(1.0).shift(band_shift(10) + DOWN * 0.4)
        b10_l4 = Tex("4. Round for the context, only at the end").scale(1.0).shift(band_shift(10) + DOWN * 1.2)
        b10_l5 = Tex("5. Answer the verb — advise needs a number").scale(1.0).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.wait(2.5)
        self.play(Write(b10_l3))
        self.wait(2.5)
        self.play(Write(b10_l4))
        self.wait(2.5)
        self.play(Write(b10_l5))
        self.wait(2)
        b10_l6 = Tex("The cheapest ten marks any paper offers").scale(1.05).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
