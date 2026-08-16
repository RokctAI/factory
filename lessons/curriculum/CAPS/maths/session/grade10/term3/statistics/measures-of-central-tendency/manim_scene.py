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

# Band-layout whiteboard scene (see the quadratics-by-factorisation worked
# example). One band per teaching beat; the camera moves down to clean space
# and nothing is ever removed. Covers all seven subtopics of the duo
# (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7), dwell times roughly
# proportional to subtopics.json (170/170/170/170/160/160/160 of 1160 s).

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k."""
    return DOWN * BAND * k


class CentralTendencySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(13)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the dataset and the mean
        title = Tex("Mean, Median and Mode").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"12,\; 14,\; 15,\; 15,\; 18,\; 21,\; 23,\; 25,\; 28").scale(1.05).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = Tex(r"The mean: the share-out-equally number").scale(1.05).shift(UP * 0.3)
        b0_l3 = MathTex(r"\text{Sum} = 171 \quad\text{(nine values)}").scale(1.1).shift(DOWN * 0.6)
        b0_l4 = MathTex(r"\text{Mean} = \frac{171}{9} = 19 \text{ minutes}").scale(1.1).shift(DOWN * 1.7)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2.5)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): median and mode
        self.next_band(1)
        b1_title = Tex("Median: middle of the ORDERED list").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Order first, always — unordered medians are meaningless").scale(0.95).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"9 \text{ values} \to 5\text{th}: \; 12, 14, 15, 15, \mathbf{18}").scale(1.05).shift(band_shift(1) + UP * 0.3)
        b1_l3 = Tex(r"Median $= 18$; even count: mean of the middle two").scale(1.0).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.wait(2.5)
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = Tex(r"Mode: appears most often — only 15 repeats").scale(1.05).shift(band_shift(1) + DOWN * 1.5)
        b1_l5 = MathTex(r"\text{Mean } 19, \;\; \text{median } 18, \;\; \text{mode } 15").scale(0.95).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1_l4))
        self.wait(2.5)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the outlier arrives
        self.next_band(2)
        b2_title = Tex("A tenth value arrives: 120 minutes").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"\text{Mean}: \frac{171 + 120}{10} = \frac{291}{10} = 29{,}1").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex(r"Nine of ten sit BELOW 29,1 — typical of nobody").scale(1.0).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"\text{Median}: \frac{18 + 21}{2} = 19{,}5").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        b2_l4 = Tex(r"Mode: still 15. The median is RESISTANT to outliers").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l3))
        self.wait(2.5)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): choosing and justifying
        self.next_band(3)
        b3_title = Tex("Choose the measure — and say why").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Symmetrical, no extremes: MEAN — it uses every value").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"Outliers or strong skew: MEDIAN").scale(1.05).shift(band_shift(3) + UP * 0.3)
        b3_l3 = Tex(r"Most popular shoe size: MODE").scale(1.05).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex(r"``The median, because the data contains an outlier").scale(1.0).shift(band_shift(3) + DOWN * 1.6)
        b3_l5 = Tex(r"which distorts the mean.''").scale(1.0).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(VGroup(b3_l4, b3_l5), color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the grouped table
        self.next_band(4)
        b4_title = Tex("Grouped data: 40 test marks in five classes").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"30\text{--}40: 4 \quad 40\text{--}50: 6 \quad 50\text{--}60: 11").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = MathTex(r"60\text{--}70: 12 \quad 70\text{--}80: 7 \;\; (40 \checkmark)").scale(0.9).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex(r"The table destroyed the individual marks").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = Tex(r"Fair assumption: everyone sits at the MIDPOINT").scale(1.0).shift(band_shift(4) + DOWN * 1.5)
        b4_l5 = MathTex(r"\text{Midpoints: } 35, \; 45, \; 55, \; 65, \; 75").scale(1.05).shift(band_shift(4) + DOWN * 2.4)
        self.play(Write(b4_l3))
        self.wait(2.5)
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): the estimated mean
        self.next_band(5)
        b5_title = Tex("The estimated mean").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"4 \times 35 = 140 \qquad 6 \times 45 = 270").scale(1.05).shift(band_shift(5) + UP * 1.2)
        b5_l2 = MathTex(r"11 \times 55 = 605 \qquad 12 \times 65 = 780").scale(1.05).shift(band_shift(5) + UP * 0.3)
        b5_l3 = MathTex(r"7 \times 75 = 525").scale(1.05).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2.5)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = MathTex(r"\text{Estimated mean} = \frac{2\,320}{40} = 58\%").scale(1.1).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2.5)
        b5_l5 = Tex(r"Say ESTIMATED — the midpoint is a fair guess, not a fact").scale(0.95).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(b5_l5))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): modal and median intervals
        self.next_band(6)
        b6_title = Tex("Modal interval, median interval").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Largest frequency 12 $\to$ modal interval $60$–$70$").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"The answer is the INTERVAL, never the 12").scale(1.0).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"4, 10, 21: \; \text{20th and 21st sit in class 3}").scale(0.9).shift(band_shift(6) + DOWN * 0.6)
        b6_l4 = Tex(r"Median interval: $50$ to below $60$").scale(1.05).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(b6_l3))
        self.wait(2.5)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2.5)
        b6_l5 = Tex(r"Mean 58 sits below the modal class: low marks drag it down").scale(0.9).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): three ways to say typical
        self.next_band(7)
        b7_title = Tex("The pot, the line, the show of hands").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"Pot: pour in all 171 minutes, share among 9 $\to$ 19 each").scale(0.95).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex(r"Line: order the nine, ask the middle person $\to$ 18").scale(0.95).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex(r"Show of hands: only 15 gets two hands $\to$ mode 15").scale(0.95).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex(r"Shoe shop: nobody wears the mean size 7,3 —").scale(0.95).shift(band_shift(7) + DOWN * 1.5)
        b7_l5 = Tex(r"the manager wants the size most feet wear").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): when one number lies
        self.next_band(8)
        b8_title = Tex("When one number lies").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"The newcomer tips two hours into the pot").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = MathTex(r"\frac{291}{10} = 29{,}1 \;\text{— fair to the total only}").scale(0.9).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"The line: he joins the far end; the middle barely moves").scale(0.95).shift(band_shift(8) + DOWN * 0.8)
        b8_l4 = MathTex(r"\text{Median} = \frac{18 + 21}{2} = 19{,}5").scale(1.05).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l3))
        self.wait(2.5)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2)
        b8_l5 = Tex(r"One mansion in the suburb? Pot ruined — use the line").scale(0.95).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_7): grouped data without fear
        self.next_band(9)
        b9_title = Tex("Grouped data without fear").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Buckets hide details: a 51 and a 59 look identical").scale(0.95).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex(r"Fairest guess: everyone at the bucket's middle").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"\frac{140 + 270 + 605 + 780 + 525}{40} = 58\%").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex(r"Fullest bucket: the sixties — modal interval").scale(1.0).shift(band_shift(9) + DOWN * 1.8)
        b9_l5 = Tex(r"Count to the middle pair: they stand in the fifties").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l4))
        self.wait(2.5)
        self.play(Write(b9_l5))
        self.wait(4)
