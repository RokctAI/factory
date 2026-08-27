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

# Band-layout whiteboard scene for the Analysing Graphs and Making Decisions
# session duo. One band per teaching beat, camera-only transitions, add-only
# lifecycle. Exporter-supported mobjects only: axes are Arrows, the
# electricity line is a chain of Lines, bars are Rectangles, points are Dots.
# Band time apportioned to subtopics.json (210/230/230/260/180/185/185 of
# 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AnalysingGraphsDecisionsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the electricity line graph, read ---
        title = Tex("Analysing Graphs, Making Decisions").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        origin = DOWN * 2.6 + LEFT * 5.4
        x_ax = Arrow(origin, origin + RIGHT * 9.6, buff=0, stroke_width=4)
        y_ax = Arrow(origin, origin + UP * 4.6, buff=0, stroke_width=4)
        self.play(Create(x_ax), Create(y_ax))
        y_lab = Tex("units").scale(0.8).shift(origin + UP * 4.3 + RIGHT * 1.0)
        x_lab = Tex("month").scale(0.8).shift(origin + RIGHT * 8.9 + DOWN * 0.4)
        self.play(Write(y_lab), Write(x_lab))
        self.wait(1.5)
        # Jan 320 -> May 500 -> Jun 575 -> Sep 400 (heights scaled /150)
        p_jan = origin + RIGHT * 1.0 + UP * 2.13
        p_may = origin + RIGHT * 4.4 + UP * 3.33
        p_jun = origin + RIGHT * 5.4 + UP * 3.83
        p_sep = origin + RIGHT * 8.0 + UP * 2.67
        seg1 = Line(p_jan, p_may, color=YELLOW, stroke_width=5)
        seg2 = Line(p_may, p_jun, color=YELLOW, stroke_width=5)
        seg3 = Line(p_jun, p_sep, color=YELLOW, stroke_width=5)
        d_jan = Dot(p_jan, color=RED)
        d_jun = Dot(p_jun, color=RED)
        self.play(Create(seg1), run_time=1.2)
        self.play(Create(seg2), Create(seg3), run_time=1.2)
        self.play(Create(d_jan), Create(d_jun))
        jan_lab = Tex("Jan: 320").scale(0.85).shift(p_jan + DOWN * 0.6 + RIGHT * 0.4)
        jun_lab = Tex("Jun: 575").scale(0.85).shift(p_jun + UP * 0.5)
        self.play(Write(jan_lab), Write(jun_lab))
        self.wait(2)
        read_rule = Tex("Month up to the point, across to the scale").scale(0.95).shift(UP * 1.6 + RIGHT * 0.2)
        self.play(Write(read_rule))
        self.wait(3)

        # --- Band 1 (subtopic_1): max, min, range, disciplines ---
        self.next_band(1)
        b1_t = Tex("Maximum, minimum, range").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("Maximum: June's 575 \\quad Minimum: Jan's 320").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"\text{Range} = 575 - 320 = 255 \text{ units}").scale(1.1).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("A wide range is the fingerprint of seasonal living").scale(0.95).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("Read the axis SCALE first; quote units always").scale(1.0).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): trends and percentage change ---
        self.next_band(2)
        b2_t = Tex("Trends and percentage change").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex("Trend = direction + numbers: rises 320 to 575,").scale(0.95).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("peaks in June, then declines").scale(0.95).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_wrong = MathTex(r"75 \div 575 \approx 13{,}0\% \text{ (new value!)}").scale(1.0).shift(band_shift(2) + DOWN * 0.5)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2)
        b2_l3 = MathTex(r"\frac{\text{change}}{\text{original}} \times 100 = \frac{75}{500} \times 100 = 15\%").scale(0.88).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the water bars ---
        self.next_band(3)
        b3_t = Tex("Water: before and after the tap repair").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_t))
        self.wait(1.5)
        base = band_shift(3) + DOWN * 2.4
        bar1 = Rectangle(width=1.6, height=3.1, color=BLUE).shift(base + LEFT * 3.6 + UP * 1.55)
        bar2 = Rectangle(width=1.6, height=2.25, color=TEAL).shift(base + LEFT * 1.2 + UP * 1.125)
        floor = Line(base + LEFT * 5.0, base + RIGHT * 0.4)
        self.play(Create(floor))
        self.play(Create(bar1))
        lab1 = Tex("25 kl").scale(0.9).shift(base + LEFT * 3.6 + UP * 3.5)
        self.play(Write(lab1))
        self.play(Create(bar2))
        lab2 = Tex("18 kl").scale(0.9).shift(base + LEFT * 1.2 + UP * 2.65)
        self.play(Write(lab2))
        self.wait(2)
        b3_l1 = MathTex(r"\text{Saving: } 25 - 18 = 7 \text{ kl}").scale(1.0).shift(band_shift(3) + RIGHT * 3.4 + UP * 0.6)
        b3_l2 = MathTex(r"\frac{7}{25} \times 100 = 28\%").scale(1.0).shift(band_shift(3) + RIGHT * 3.4 + DOWN * 0.6)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = Tex("One tap, over a quarter of the water").scale(0.95).shift(band_shift(3) + RIGHT * 3.4 + DOWN * 1.7)
        self.play(Write(b3_l3))
        self.wait(3)

        # --- Band 4 (subtopic_3): electricity into rand ---
        self.next_band(4)
        b4_t = Tex("From graph to rand: R2,40 per unit").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{June: } 575 \times 2{,}40 = 1\;150 + 230 = \text{R}1\;380").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"\text{January: } 320 \times 2{,}40 = \text{R}768").scale(1.0).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"\text{Seasonal swing: } 1\;380 - 768 = \text{R}612").scale(1.05).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        b4_l4 = Tex("The line graph is now a budgeting document").scale(0.95).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): pricing the repair ---
        self.next_band(5)
        b5_t = Tex("Was the R580 plumber worth it?").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"7 \text{ kl} \times \text{R}35 = \text{R}245 \text{ per month}").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"\text{Year: } 245 \times 12 = \text{R}2\;940").scale(1.05).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"\text{2 months: } 490 < 580; \quad \text{3 months: } 735 > 580").scale(0.94).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_ans = Tex("The repair pays for itself in month three").scale(1.05).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_ans))
        self.play(Create(SurroundingRectangle(b5_ans, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_3): the pie chart, share times whole ---
        self.next_band(6)
        b6_t = Tex("The pie: R3 200 split four ways").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Electricity } 45\%: \; 0{,}45 \times 3\;200 = \text{R}1\;440").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"\text{Water } 30\%: \text{R}960 \quad \text{Refuse } 15\%: \text{R}480").scale(0.86).shift(band_shift(6) + UP * 0.2)
        b6_l3 = MathTex(r"\text{Sewerage } 10\%: \text{R}320").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"\text{Audit: } 1\;440 + 960 + 480 + 320 = 3\;200 \; \checkmark").scale(0.91).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): conclusions and predictions ---
        self.next_band(7)
        b7_t = Tex("Conclude only what the numbers show").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex("Supported: winter uses most — 575 vs 320").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_wrong = Tex("Unsupported: the family is CARELESS with power").scale(0.95).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_wrong))
        self.play(Create(strike(b7_wrong)))
        self.wait(2.5)
        b7_l2 = Tex("Prediction = number + condition:").scale(1.0).shift(band_shift(7) + DOWN * 0.8)
        b7_l3 = Tex("probably near 575 again, IF habits stay the same").scale(0.95).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l2))
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_4): the axis that lies ---
        self.next_band(8)
        b8_t = Tex("The axis that lies").scale(1.2).shift(band_shift(8) + UP * 2.5)
        self.play(Write(b8_t))
        self.wait(1.5)
        base8 = band_shift(8) + DOWN * 2.3 + LEFT * 3.4
        axis_line = Line(base8 + LEFT * 1.4, base8 + RIGHT * 3.6)
        self.play(Create(axis_line))
        start_lab = Tex("axis starts at 300!").scale(0.85).shift(base8 + LEFT * 0.4 + DOWN * 0.6)
        self.play(Write(start_lab))
        barJ = Rectangle(width=1.2, height=0.25, color=BLUE).shift(base8 + RIGHT * 0.6 + UP * 0.125)
        barW = Rectangle(width=1.2, height=3.2, color=RED).shift(base8 + RIGHT * 2.6 + UP * 1.6)
        self.play(Create(barJ))
        labJ = Tex("Jan").scale(0.8).shift(base8 + RIGHT * 0.6 + UP * 0.8)
        self.play(Write(labJ))
        self.play(Create(barW))
        labW = Tex("Jun").scale(0.8).shift(base8 + RIGHT * 2.6 + UP * 3.6)
        self.play(Write(labW))
        self.wait(2)
        b8_l1 = Tex("Stub of 20 vs column of 275:").scale(0.95).shift(band_shift(8) + RIGHT * 3.3 + UP * 0.8)
        b8_l2 = Tex("LOOKS fourteen-fold; truth: 575 vs 320").scale(0.9).shift(band_shift(8) + RIGHT * 3.3 + DOWN * 0.0)
        b8_l3 = Tex("— less than double").scale(0.95).shift(band_shift(8) + RIGHT * 3.3 + DOWN * 0.8)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.wait(2)
        b8_rule = Tex("Trust no axis that does not start at 0").scale(1.0).shift(band_shift(8) + RIGHT * 2.9 + DOWN * 1.9)
        self.play(Write(b8_rule))
        self.play(Create(SurroundingRectangle(b8_rule, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): the graph is a story about your house ---
        self.next_band(9)
        b9_t = Tex("The graph is your house talking").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("The winter spike is the family's cold-months diary").scale(0.95).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("Finger exercise: month, up to the dot, left: 575").scale(0.95).shift(band_shift(9) + UP * 0.2)
        b9_l3 = MathTex(r"\text{The swing: } 575 - 320 = 255 \text{ units}").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l2))
        self.wait(2.5)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("The shorter water bar is the plumber's autograph").scale(0.95).shift(band_shift(9) + DOWN * 1.7)
        b9_l5 = Tex("Name the story first, then the details fit").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l4))
        self.wait(2)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_6): numbers first, opinions second ---
        self.next_band(10)
        b10_t = Tex("Numbers first, opinions second").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = MathTex(r"\text{Winter costs } 1\;380 - 768 = \text{R}612 \text{ more}").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex("Plumber: R245/month vs R580 once — a bargain").scale(0.95).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Aim at big slices: 10\\% off electricity = R144;").scale(0.95).shift(band_shift(10) + DOWN * 0.7)
        b10_l4 = Tex("10\\% off sewerage = only R32").scale(0.95).shift(band_shift(10) + DOWN * 1.4)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_ans = Tex("Read, multiply once, THEN judge").scale(1.05).shift(band_shift(10) + DOWN * 2.4)
        self.play(Write(b10_ans))
        self.play(Create(SurroundingRectangle(b10_ans, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_7): when a picture exaggerates ---
        self.next_band(11)
        b11_t = Tex("When a picture exaggerates").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(2)
        b11_l1 = Tex("The lie is the missing bottom of the picture —").scale(0.95).shift(band_shift(11) + UP * 1.1)
        b11_l2 = Tex("a photograph cropped down to the scowl").scale(0.95).shift(band_shift(11) + UP * 0.4)
        self.play(Write(b11_l1))
        self.play(Write(b11_l2))
        self.wait(2.5)
        b11_l3 = Tex("Five-second defence: where does the axis start?").scale(0.95).shift(band_shift(11) + DOWN * 0.6)
        self.play(Write(b11_l3))
        self.wait(2.5)
        b11_l4 = Tex("Answer sentences: axis starts at 300, so only the").scale(0.9).shift(band_shift(11) + DOWN * 1.5)
        b11_l5 = Tex("differences show; truly 575 vs 320 — under double").scale(0.9).shift(band_shift(11) + DOWN * 2.2)
        self.play(Write(b11_l4))
        self.play(Write(b11_l5))
        self.play(Create(SurroundingRectangle(b11_l5, color=GREEN)))
        self.wait(4)
