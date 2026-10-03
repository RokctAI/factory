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


class DrawingGraphsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Bar graph rules
        t0 = Tex(r"Bar graph rules").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = Tex(r"Title and labelled axes").scale(0.95).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex(r"Frequency axis starts at 0, even scale").scale(0.95).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = Tex(r"Equal widths, equal gaps").scale(0.95).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Double bar graph: add a key").scale(0.95).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.wait(3)

        # --- Band 1 (subtopic_2): Histogram
        self.next_band(1)
        t1 = Tex(r"Histogram").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = Tex(r"20-29: 4   30-39: 7   40-49: 4").scale(0.95).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        m6 = Tex(r"Bars touch: intervals follow on").scale(0.95).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = Tex(r"Horizontal axis is a number line").scale(0.95).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = Tex(r"Equal interval widths").scale(0.95).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m8))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): Pie chart angles
        self.next_band(2)
        t2 = Tex(r"Pie chart angles").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"\text{angle} = \frac{\text{frequency}}{\text{total}} \times 360^\circ").scale(1.0).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m9))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m9, color=GREEN)))
        self.wait(1.5)
        m10 = MathTex(r"\text{Walk: } \tfrac{14}{40} \times 360^\circ = 126^\circ").scale(1.0).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"126 + 99 + 54 + 63 + 18 = 360").scale(1.0).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = MathTex(r"\tfrac{14}{40} = 35\%").scale(1.0).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m12))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): Slicing the pie
        self.next_band(3)
        t3 = Tex(r"Slicing the pie").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"\text{Apple: } \tfrac{10}{20} \times 360^\circ = 180^\circ").scale(1.0).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"\text{Banana: } \tfrac{5}{20} \times 360^\circ = 90^\circ").scale(1.0).shift(band_shift(3) + DOWN * 0.85)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"180 + 90 + 90 = 360").scale(1.0).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m15))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_5): Gaps or no gaps?
        self.next_band(4)
        t4 = Tex(r"Gaps or no gaps?").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m16 = Tex(r"Separate things: bar graph with gaps").scale(0.95).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m16))
        self.wait(2)
        m17 = Tex(r"Number groups: histogram, bars touch").scale(0.95).shift(band_shift(4) + DOWN * 0.85)
        self.play(Write(m17))
        self.wait(2)
        m18 = Tex(r"Parts of a whole: pie chart").scale(0.95).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m18))
        self.wait(2)
        self.wait(3)
