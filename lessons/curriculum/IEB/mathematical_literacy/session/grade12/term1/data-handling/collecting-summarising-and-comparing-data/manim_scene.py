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

# Band-layout whiteboard scene for the Collecting, Summarising and Comparing
# Data session duo. Part 1 — Expert: subtopics 1-4 (question & collection,
# organising, summary statistics, box-and-whisker comparison of two clinic
# queues). Part 2 — Simplifier: subtopics 5-7 seat the queue on the bench.
# Durations 215/215/225/230/195/195/195 of 1470 s. Exporter-safe mobjects only
# (box plots hand-built from Rectangle + Line); add-only lifecycle.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CollectingSummarisingComparingDataSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the question, the population, the sample ---
        title = Tex("Collecting, Summarising, Comparing Data").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Question: minutes waited at the clinic?").scale(1.05).shift(UP * 1.1)
        b0_l2 = Tex("Population: EVERY patient at each clinic").scale(1.05).shift(UP * 0.2)
        b0_l3 = Tex("Sample: spread across the whole day").scale(1.05).shift(DOWN * 0.7)
        b0_l4 = Tex("Only before-seven arrivals = bias downward").scale(1.0).shift(DOWN * 1.7)
        self.play(Write(b0_l1)); self.wait(2)
        self.play(Write(b0_l2)); self.wait(2)
        self.play(Write(b0_l3)); self.wait(2)
        self.play(Write(b0_l4)); self.wait(3)

        # --- Band 1 (subtopic_1): instruments and data types ---
        self.next_band(1)
        b1_title = Tex("Instrument, then data type").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Questionnaire: cheap, many, unleading").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("Interview: follow-ups, slow, may influence").scale(1.05).shift(band_shift(1) + UP * 0.2)
        b1_l3 = Tex("Recording sheet: clerk logs arrivals directly").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = Tex("Minutes waited: NUMERICAL — calculate away").scale(1.05).shift(band_shift(1) + DOWN * 1.7)
        b1_l5 = Tex("Reason for visit: CATEGORICAL — count only").scale(1.05).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        self.play(Write(b1_l3)); self.wait(2)
        self.play(Write(b1_l4)); self.wait(2)
        self.play(Write(b1_l5)); self.wait(3)

        # --- Band 2 (subtopic_2): frequency table with class intervals ---
        self.next_band(2)
        b2_title = Tex("Eleven Ntabeni waits, grouped in twenty-fives").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_data = MathTex(r"20,30,30,45,50,60,70,85,90,100,120").scale(0.95).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_data)); self.wait(2)
        tbl = Rectangle(width=6.6, height=2.6).shift(band_shift(2) + DOWN * 0.5)
        self.play(Create(tbl))
        r1 = MathTex(r"0\text{--}24: 1 \qquad 25\text{--}49: 3").scale(1.0).shift(band_shift(2) + UP * 0.1)
        r2 = MathTex(r"50\text{--}74: 3 \qquad 75\text{--}99: 2").scale(1.0).shift(band_shift(2) + DOWN * 0.6)
        r3 = MathTex(r"100\text{--}124: 2").scale(1.0).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(r1)); self.wait(2)
        self.play(Write(r2)); self.wait(2)
        self.play(Write(r3)); self.wait(1.5)
        b2_l1 = MathTex(r"\text{Check: } 1+3+3+2+2 = 11").scale(1.05).shift(band_shift(2) + DOWN * 2.3)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): mean, median, mode, range ---
        self.next_band(3)
        b3_title = Tex("Order first — then summarise").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{Mean: } 700 \div 11 = 63,6 \text{ min}").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"\text{Median: 6th value} = 60 \text{ min}").scale(1.05).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"\text{Mode: } 30 \quad \text{Range: } 120 - 20 = 100").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = Tex("The two-hour patient pulls the mean up").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        b3_l5 = Tex("The mean chases extremes; the median resists").scale(1.0).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l1)); self.wait(2)
        self.play(Write(b3_l2)); self.wait(2)
        self.play(Write(b3_l3)); self.wait(2)
        self.play(Write(b3_l4)); self.wait(2)
        self.play(Write(b3_l5)); self.wait(3)

        # --- Band 4 (subtopic_3): quartiles and percentiles ---
        self.next_band(4)
        b4_title = Tex("Quartiles cut the ordered queue in four").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"Q_1: \text{ middle of } 20,30,30,45,50 = 30").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"Q_3: \text{ middle of } 70,85,90,100,120 = 90").scale(1.0).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"\text{IQR} = 90 - 30 = 60 \text{ min}").scale(1.1).shift(band_shift(4) + DOWN * 0.8)
        b4_l4 = Tex("IQR ignores the extremes entirely").scale(1.05).shift(band_shift(4) + DOWN * 1.8)
        b4_l5 = Tex("90th percentile: longer than 90 in 100").scale(1.0).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l1)); self.wait(2.5)
        self.play(Write(b4_l2)); self.wait(2.5)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        self.play(Write(b4_l4)); self.wait(2)
        self.play(Write(b4_l5)); self.wait(3)

        # --- Band 5 (subtopic_4): the two five-number summaries ---
        self.next_band(5)
        b5_title = Tex("Five numbers per clinic").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"\text{Ntabeni: } 20,\;30,\;60,\;90,\;120").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"\text{Umbilo data: } 15,15,20,25,30,35,40,40,45,50,55").scale(0.85).shift(band_shift(5) + UP * 0.2)
        b5_l3 = MathTex(r"\text{Median } 35, \; Q_1 = 20, \; Q_3 = 45").scale(1.05).shift(band_shift(5) + DOWN * 0.7)
        b5_l4 = MathTex(r"\text{Umbilo: } 15,\;20,\;35,\;45,\;55").scale(1.05).shift(band_shift(5) + DOWN * 1.6)
        b5_l5 = MathTex(r"\text{IQR: Ntabeni } 60 \text{ vs Umbilo } 25").scale(1.0).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l1)); self.wait(2)
        self.play(Write(b5_l2)); self.wait(2.5)
        self.play(Write(b5_l3)); self.wait(2)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        self.play(Write(b5_l5)); self.wait(3)

        # --- Band 6 (subtopic_4): both box plots on one scale ---
        self.next_band(6)
        b6_title = Tex("Two box plots, one scale").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)

        def bx(v):
            # 0-120 minutes mapped across the band width
            return LEFT * 3.3 + RIGHT * (v * 0.0525)

        # Axis with three ticks
        axis = Line(band_shift(6) + bx(0) + DOWN * 2.4, band_shift(6) + bx(120) + DOWN * 2.4)
        t0 = Tex("0").scale(0.8).shift(band_shift(6) + bx(0) + DOWN * 2.8)
        t60 = Tex("60").scale(0.8).shift(band_shift(6) + bx(60) + DOWN * 2.8)
        t120 = Tex("120").scale(0.8).shift(band_shift(6) + bx(120) + DOWN * 2.8)
        self.play(Create(axis), Write(t0), Write(t60), Write(t120))
        self.wait(1.5)
        # Ntabeni plot at y = +0.8
        ny = UP * 0.8
        n_lab = Tex("Ntabeni").scale(0.9).shift(band_shift(6) + ny + LEFT * 4.8)
        n_box = Rectangle(width=(90 - 30) * 0.0525, height=0.7).shift(
            band_shift(6) + ny + bx(60))
        n_med = Line(band_shift(6) + ny + bx(60) + UP * 0.35,
                     band_shift(6) + ny + bx(60) + DOWN * 0.35, color=YELLOW)
        n_w1 = Line(band_shift(6) + ny + bx(20), band_shift(6) + ny + bx(30))
        n_w2 = Line(band_shift(6) + ny + bx(90), band_shift(6) + ny + bx(120))
        self.play(Write(n_lab))
        self.play(Create(n_box), Create(n_med))
        self.play(Create(n_w1), Create(n_w2))
        self.wait(2)
        # Umbilo plot at y = -0.8
        uy = DOWN * 0.8
        u_lab = Tex("Umbilo").scale(0.9).shift(band_shift(6) + uy + LEFT * 4.8)
        u_box = Rectangle(width=(45 - 20) * 0.0525, height=0.7).shift(
            band_shift(6) + uy + bx(32.5))
        u_med = Line(band_shift(6) + uy + bx(35) + UP * 0.35,
                     band_shift(6) + uy + bx(35) + DOWN * 0.35, color=YELLOW)
        u_w1 = Line(band_shift(6) + uy + bx(15), band_shift(6) + uy + bx(20))
        u_w2 = Line(band_shift(6) + uy + bx(45), band_shift(6) + uy + bx(55))
        self.play(Write(u_lab))
        self.play(Create(u_box), Create(u_med))
        self.play(Create(u_w1), Create(u_w2))
        self.wait(2)
        b6_l1 = Tex("Medians 60 vs 35; a quarter above $Q_3$").scale(1.0).shift(band_shift(6) + UP * 1.7)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): lining up the queue ---
        self.next_band(7)
        b7_title = Tex("Lining up the queue").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2.5)
        b7_l1 = Tex("Median: the patient seated dead centre").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"\text{6th of 11 waited } 60 \text{ minutes}").scale(1.05).shift(band_shift(7) + UP * 0.2)
        b7_l3 = MathTex(r"Q_1 = 30: \text{ middle of the left five}").scale(1.05).shift(band_shift(7) + DOWN * 0.8)
        b7_l4 = MathTex(r"Q_3 = 90; \;\; \text{IQR} = 60").scale(1.05).shift(band_shift(7) + DOWN * 1.8)
        b7_l5 = Tex("Count to the middles — don't calculate").scale(1.05).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l1)); self.wait(3)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(3)
        self.play(Write(b7_l3)); self.wait(3)
        self.play(Write(b7_l4)); self.wait(3)
        self.play(Write(b7_l5)); self.wait(3)

        # --- Band 8 (subtopic_6): the box tells the story ---
        self.next_band(8)
        b8_title = Tex("The box tells the story").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2.5)
        b8_l1 = Tex("The box holds the middle HALF of the queue").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("Each whisker, each box half: a QUARTER").scale(1.05).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex("A quarter of Ntabeni patients wait 90+ min").scale(1.05).shift(band_shift(8) + DOWN * 0.8)
        b8_l4 = Tex("The box never shows mean, mode or count").scale(1.05).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l1)); self.wait(3)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(3)
        self.play(Write(b8_l3)); self.wait(3.5)
        self.play(Write(b8_l4)); self.wait(3.5)

        # --- Band 9 (subtopic_7): mean or median, which to trust ---
        self.next_band(9)
        b9_title = Tex("Mean or median: which one to trust").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = MathTex(r"\text{Mean } 63,6 \text{ vs median } 60").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"\text{Swap 120 for 60: mean} \to 58,2").scale(1.05).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex("The median did not move at all").scale(1.05).shift(band_shift(9) + DOWN * 0.7)
        b9_l4 = Tex("Outliers? The median is the safer typical").scale(1.05).shift(band_shift(9) + DOWN * 1.7)
        b9_l5 = Tex("Big range, modest IQR: outliers at the edges").scale(1.0).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l1)); self.wait(3)
        self.play(Write(b9_l2)); self.wait(3)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(3)
        self.play(Write(b9_l4)); self.wait(3)
        self.play(Write(b9_l5)); self.wait(4)
