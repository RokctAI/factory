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


class ReadingGraphsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Library books borrowed
        t0 = Tex(r"Library books borrowed").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = Tex(r"Feb 45   Mar 60   Apr 30   May 75").scale(0.95).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"75 - 30 = 45 \text{ more in May}").scale(1.0).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"45 + 60 + 30 + 75 = 210").scale(1.0).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = MathTex(r"210 \div 4 = 52{,}5").scale(1.0).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.wait(3)

        # --- Band 1 (subtopic_2): Pie charts and histograms
        self.next_band(1)
        t1 = Tex(r"Pie charts and histograms").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"90^\circ = \tfrac{1}{4}: \; \tfrac{1}{4} \times 200 = 50").scale(1.0).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"72^\circ = \tfrac{72}{360} = \tfrac{1}{5}: \; 40 \text{ learners}").scale(1.0).shift(band_shift(1) + DOWN * 0.85)
        self.play(Write(m6))
        self.wait(2)
        m7 = Tex(r"Histogram: counts per interval, not exact values").scale(0.95).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m7))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): Misleading graphs
        self.next_band(2)
        t2 = Tex(r"Misleading graphs").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m8 = Tex(r"Sales 98, 100, 102").scale(0.95).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m8))
        self.wait(2)
        m9 = Tex(r"Axis from 96: looks like huge growth").scale(0.95).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m9))
        self.wait(2)
        m10 = Tex(r"Axis from 0: small growth").scale(0.95).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m10))
        self.wait(2)
        m11 = Tex(r"Check: zero start, even scale, nothing missing").scale(0.95).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m11))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): Read the labels first
        self.next_band(3)
        t3 = Tex(r"Read the labels first").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m12 = Tex(r"1. Title").scale(0.95).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m12))
        self.wait(2)
        m13 = Tex(r"2. Axis labels").scale(0.95).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m13))
        self.wait(2)
        m14 = Tex(r"3. Scale: each line = 2").scale(0.95).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m14))
        self.wait(2)
        m15 = Tex(r"Bar to the 5th line = 10").scale(0.95).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m15))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_5): Squashed and stretched
        self.next_band(4)
        t4 = Tex(r"Squashed and stretched").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m16 = Tex(r"20 s and 21 s").scale(0.95).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m16))
        self.wait(2)
        m17 = Tex(r"Axis from 19: looks twice as tall").scale(0.95).shift(band_shift(4) + DOWN * 0.85)
        self.play(Write(m17))
        self.wait(2)
        m18 = Tex(r"Axis from 0: almost equal").scale(0.95).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m18))
        self.wait(2)
        self.wait(3)
