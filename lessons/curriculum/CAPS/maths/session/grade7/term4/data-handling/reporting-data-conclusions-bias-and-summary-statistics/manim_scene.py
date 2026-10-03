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
# the allowed primitive vocabulary. Bands cover all 5 subtopics
# (Part 1 — Expert: subtopics 1-3; Part 2 — Simplifier: subtopics 4-5), with
# dwell time proportional to subtopics.json (120/120/120/120/120 of
# 600 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ReportingDataSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Summarising
        t0 = Tex(r"Summarising").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = Tex(r"Walk 14 of 40 = 35%: most common").scale(0.95).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex(r"Taxi 11 = 27,5%").scale(0.95).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = Tex(r"Prediction: about a third of 240 walk").scale(0.95).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Not shown: why they walk").scale(0.95).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.wait(3)

        # --- Band 1 (subtopic_2): Bias and error
        self.next_band(1)
        t1 = Tex(r"Bias and error").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = Tex(r"Sampling bias: only bus learners").scale(0.95).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        m6 = Tex(r"Question bias: leading wording").scale(0.95).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = Tex(r"Sample too small").scale(0.95).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = Tex(r"Recording errors and unusual timing").scale(0.95).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m8))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): What to report
        self.next_band(2)
        t2 = Tex(r"What to report").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = Tex(r"Categories: frequencies, %, mode").scale(0.95).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m9))
        self.wait(2)
        m10 = Tex(r"Numbers: mean or median, and range").scale(0.95).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = Tex(r"Outlier: report the median").scale(0.95).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"Question, method, graph, stats, conclusion, limits").scale(0.95).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m12))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): Say only what it shows
        self.next_band(3)
        t3 = Tex(r"Say only what it shows").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = Tex(r"12 of 30 chose pizza = 40%").scale(0.95).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m13))
        self.wait(2)
        m14 = Tex(r"Supported: most popular in our class").scale(0.95).shift(band_shift(3) + DOWN * 0.85)
        self.play(Write(m14))
        self.wait(2)
        m15 = Tex(r"Not supported: everyone in South Africa").scale(0.95).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m15))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_5): The data cycle
        self.next_band(4)
        t4 = Tex(r"The data cycle").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m16 = Tex(r"Ask, collect, organise").scale(0.95).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m16))
        self.wait(2)
        m17 = Tex(r"Show, analyse, report").scale(0.95).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"\tfrac{15}{40} = 37{,}5\%").scale(1.0).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m18))
        self.wait(2)
        m19 = Tex(r"New question, cycle again").scale(0.95).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m19))
        self.wait(2)
        self.wait(3)
