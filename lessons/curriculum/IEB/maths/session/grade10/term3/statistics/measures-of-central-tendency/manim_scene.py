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

# Band-layout whiteboard scene. One band per teaching beat; the camera moves
# down to clean space and nothing is ever removed. Covers all seven subtopics
# of the duo (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7), dwell times
# roughly proportional to subtopics.json (170/170/170/170/160/160/160 of 1160 s).

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
        b0_l1 = MathTex(r"10, \; 13, \; 16, \; 16, \; 19, \; 22, \; 24, \; 27, \; 33").scale(1.0).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = Tex(r"Nine reading times, already ordered").scale(0.95).shift(UP * 0.4)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = MathTex(r"\text{Mean} = \frac{180}{9} = 20 \;\text{minutes}").scale(1.1).shift(DOWN * 0.6)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2.5)
        b0_l4 = Tex(r"Share the total out equally — the mean touches every value").scale(0.85).shift(DOWN * 1.7)
        self.play(Write(b0_l4))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): median and mode
        self.next_band(1)
        b1_title = Tex("Median: middle of the ORDERED list").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"10, 13, 16, 16, \underline{19}, 22, 24, 27, 33").scale(1.0).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex(r"Fifth of nine: four below, four above — median 19").scale(0.95).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex(r"Even count? Mean of the two middle values").scale(0.95).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex(r"Mode: most frequent — only 16 appears twice").scale(0.95).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = MathTex(r"\text{Mean } 20, \;\; \text{median } 19, \;\; \text{mode } 16").scale(1.0).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the outlier arrives
        self.next_band(2)
        b2_title = Tex("An outlier arrives: 130 minutes").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Mean: } \frac{310}{10} = 31 \;\text{— dragged!}").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = Tex(r"Nine of ten learners sit BELOW 31").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"\text{Median: } \frac{19 + 22}{2} = 20{,}5 \;\text{— barely moved}").scale(1.0).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex(r"The median is RESISTANT: position, not size").scale(0.95).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l4))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): choosing and justifying
        self.next_band(3)
        b3_title = Tex("Choose the measure — and say why").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Calm, symmetric data: MEAN — it uses every value").scale(0.95).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = Tex(r"Outliers or strong skew: MEDIAN — unaffected by extremes").scale(0.9).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex(r"Categories (flavours, shoe sizes): MODE").scale(0.95).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex(r"``The median, because the data contains an outlier").scale(0.9).shift(band_shift(3) + DOWN * 1.5)
        b3_l5 = Tex(r"which distorts the mean.''").scale(0.9).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(VGroup(b3_l4, b3_l5), color=GREEN)))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): the grouped table
        self.next_band(4)
        b4_title = Tex("Grouped data: fifty test marks").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"$40$–$50$: 6 \quad $50$–$60$: 12 \quad $60$–$70$: 13").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex(r"$70$–$80$: 14 \quad $80$–$90$: 5").scale(0.95).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"6 + 12 + 13 + 14 + 5 = 50 \;\checkmark").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex(r"The table hides the marks — an exact mean is impossible").scale(0.85).shift(band_shift(4) + DOWN * 1.7)
        b4_l5 = Tex(r"Fair assumption: everyone sits at the interval MIDPOINT").scale(0.85).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l4))
        self.wait(2.5)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): the estimated mean
        self.next_band(5)
        b5_title = Tex("The estimated mean").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"\text{Midpoints: } 45, \; 55, \; 65, \; 75, \; 85").scale(1.0).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"6 \times 45 = 270 \quad 12 \times 55 = 660 \quad 13 \times 65 = 845").scale(0.9).shift(band_shift(5) + UP * 0.3)
        b5_l3 = MathTex(r"14 \times 75 = 1\,050 \quad 5 \times 85 = 425").scale(0.9).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_l2))
        self.wait(2.5)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = MathTex(r"\bar{x} \approx \frac{3\,250}{50} = 65\%").scale(1.1).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2.5)
        b5_l5 = Tex(r"Say ESTIMATED — the midpoint assumption is a fair guess").scale(0.85).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l5))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): modal and median intervals
        self.next_band(6)
        b6_title = Tex("Modal and median intervals").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Largest frequency 14 $\to$ modal interval $70$–$80$").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"(the answer is the interval, never the 14)").scale(0.85).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"\text{Cumulative: } 6, \; 18, \; 31 \; \Rightarrow \; \text{25th and 26th sit in class 3}").scale(0.85).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex(r"Median interval: $60$–$70$").scale(1.0).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_l5 = Tex(r"Mean 65 sits below the modal class — the weak tail drags it").scale(0.8).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): three ways to say typical
        self.next_band(7)
        b7_title = Tex("Three ways to say typical").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"The POOL: tip in all 180 minutes, split equally $\to$ 20 each").scale(0.9).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex(r"The QUEUE: order the nine, tap the middle shoulder $\to$ 19").scale(0.9).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex(r"The BESTSELLER: the value seen most $\to$ 16").scale(0.9).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex(r"Pool $=$ mean; queue $=$ median; bestseller $=$ mode").scale(0.95).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): when one number lies
        self.next_band(8)
        b8_title = Tex("When one number lies").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"130 minutes tips into the pool: split jumps to 31").scale(0.95).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex(r"— but nine of ten read LESS than that").scale(0.95).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"In the queue, the newcomer stands at the back:").scale(0.95).shift(band_shift(8) + DOWN * 0.7)
        b8_l4 = MathTex(r"\text{median } \frac{19 + 22}{2} = 20{,}5 \;\text{— barely a flicker}").scale(0.95).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2.5)
        b8_l5 = Tex(r"Extremes wreck the pool, never the queue").scale(0.95).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l5))
        self.wait(2.5)

        # --- Band 9 (subtopic_7): grouped data without fear
        self.next_band(9)
        b9_title = Tex("Grouped data without fear").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Five crates: 6, 12, 13, 14, 5 learners — crates hide details").scale(0.85).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex(r"Call each crate by its middle: 45, 55, 65, 75, 85").scale(0.9).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"\text{Pool: } \frac{3\,250}{50} = 65\% \;\text{(estimated)}").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex(r"Fullest crate: the seventies — modal interval").scale(0.9).shift(band_shift(9) + DOWN * 1.7)
        b9_l5 = Tex(r"Count 6, 18, 31: middle pair in the sixties — median interval").scale(0.85).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l4))
        self.wait(2.5)
        self.play(Write(b9_l5))
        self.wait(4)
