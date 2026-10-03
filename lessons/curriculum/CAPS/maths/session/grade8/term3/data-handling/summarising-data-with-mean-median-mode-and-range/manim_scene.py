# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from manim import *

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex/MathTex keep the export to
# the allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (270/200/220/230/240/210/210 of
# 1580 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SummariseDataSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The Mean
        t0 = Tex(r"The Mean").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"\text{mean} = \frac{20 + 35 + 50 + 15 + 30}{5} = \frac{150}{5} = 30").scale(1.1).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"\frac{619}{20} = 30{,}95").scale(1.1).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"\frac{0 \times 4 + 1 \times 9 + 2 \times 6 + 3 \times 1}{4 + 9 + 6 + 1} = \frac{24}{20} = 1{,}2").scale(1.1).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Missing value: mean times count gives the total; subtract the known values").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 1 (subtopic_2): The Median
        self.next_band(1)
        t1 = Tex(r"The Median").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = Tex(r"Order first. Odd count: the single middle value. Even count: mean of the two middle values.").scale(1.05).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m5))
        self.wait(2)
        m6 = Tex(r"Six values 4, 7, 9, 12, 15, 20: middle pair 9 and 12").scale(1.05).shift(band_shift(1) + UP * 0.18)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"\text{median} = \frac{9 + 12}{2} = 10{,}5").scale(1.1).shift(band_shift(1) + DOWN * 0.85)
        self.play(Write(m7))
        self.wait(2)
        m8 = Tex(r"Twenty marks: 10th and 11th leaves are 31 and 31, median 31").scale(1.05).shift(band_shift(1) + DOWN * 1.87)
        self.play(Write(m8))
        self.wait(2)
        m9 = Tex(r"Unmoved by extreme values; the right summary for skewed data").scale(1.05).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m9))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m9, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 2 (subtopic_3): Mode, Range and Extremes
        self.next_band(2)
        t2 = Tex(r"Mode, Range and Extremes").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m10 = Tex(r"Mode: most frequent value; works for categories; may be two or none").scale(1.05).shift(band_shift(2) + UP * 1.2)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"\text{range} = 50 - 15 = 35 \qquad \text{range} = 48 - 12 = 36").scale(1.1).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"Extremes: minimum and maximum themselves, 12 and 48").scale(1.05).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m12))
        self.wait(2)
        m13 = Tex(r"Range is one number; it is pulled by a single unusual value").scale(1.05).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(m13))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m13, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 3 (subtopic_4): Choosing a Measure
        self.next_band(3)
        t3 = Tex(r"Choosing a Measure").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m14 = MathTex(r"\text{mean} = \frac{96\,500}{5} = 19\,300 \qquad \text{median} = 9\,500").scale(1.1).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m14))
        self.wait(2)
        m15 = Tex(r"The extreme value 60 000 pulls the mean; the median stays with the middle person").scale(1.05).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m15))
        self.wait(2)
        m16 = Tex(r"Mean: even data. Median: extremes or a long tail. Mode: categories or most common.").scale(1.05).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m16))
        self.wait(2)
        m17 = Tex(r"Say which measure; average alone is ambiguous").scale(1.05).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m17))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m17, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): The Team's Average
        self.next_band(4)
        t4 = Tex(r"The Team's Average").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m18 = Tex(r"Ordered goals: 0, 0, 1, 1, 1, 1, 1, 2, 3, 20").scale(1.05).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"\text{mean} = \frac{30}{10} = 3 \qquad \text{median} = 1 \qquad \text{mode} = 1").scale(1.1).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m19))
        self.wait(2)
        m20 = MathTex(r"\text{range} = 20 - 0 = 20").scale(1.1).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m20))
        self.wait(2)
        m21 = Tex(r"One freak match makes the mean; the median and mode plan the season").scale(1.05).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m21))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m21, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 5 (subtopic_6): One House, Every Average
        self.next_band(5)
        t5 = Tex(r"One House, Every Average").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        m22 = MathTex(r"\text{mean} = \frac{10\,650}{8} = 1\,331{,}25 \qquad \text{median} = \frac{950 + 1\,000}{2} = 975").scale(1.1).shift(band_shift(5) + UP * 1.2)
        self.play(Write(m22))
        self.wait(2)
        m23 = MathTex(r"\text{range} = 4\,000 - 800 = 3\,200").scale(1.1).shift(band_shift(5) + DOWN * 0.17)
        self.play(Write(m23))
        self.wait(2)
        m24 = MathTex(r"\text{without the outlier: mean} = \frac{6\,650}{7} = 950, \quad \text{range} = 300").scale(1.1).shift(band_shift(5) + DOWN * 1.53)
        self.play(Write(m24))
        self.wait(2)
        m25 = Tex(r"The median answers what a typical house costs").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(m25))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m25, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 6 (subtopic_7): Examination Technique
        self.next_band(6)
        t6 = Tex(r"Examination Technique").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(t6))
        self.wait(1.5)
        m26 = Tex(r"Order, count, total, divide; middle by position; most frequent; max minus min").scale(1.05).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m26))
        self.wait(2)
        m27 = MathTex(r"5 \times 62 = 310, \quad 55 + 60 + 68 + 70 = 253, \quad 310 - 253 = 57").scale(1.1).shift(band_shift(6) + DOWN * 0.17)
        self.play(Write(m27))
        self.wait(2)
        m28 = Tex(r"Frequency table: divide by total frequency, not rows").scale(1.05).shift(band_shift(6) + DOWN * 1.53)
        self.play(Write(m28))
        self.wait(2)
        m29 = Tex(r"Choose the measure with a reason; state units; name the extreme value").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m29))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m29, color=GREEN)))
        self.wait(1.5)
        self.wait(3)
