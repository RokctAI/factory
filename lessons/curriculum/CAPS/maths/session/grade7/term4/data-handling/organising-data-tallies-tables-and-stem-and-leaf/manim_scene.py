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


class OrganisingDataSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Frequency table
        t0 = Tex(r"Frequency table").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = Tex(r"Walk 14   Taxi 11   Bus 6").scale(0.95).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex(r"Car 7   Bicycle 2").scale(0.95).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"14 + 11 + 6 + 7 + 2 = 40").scale(1.0).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Tally bundles of five").scale(0.95).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.wait(3)

        # --- Band 1 (subtopic_2): Ordering and grouping
        self.next_band(1)
        t1 = Tex(r"Ordering and grouping").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = Tex(r"23 25 27 29 31 32 33 35 36 38 38 40 41 45 47").scale(0.95).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        m6 = Tex(r"20 to 29: 4").scale(0.95).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = Tex(r"30 to 39: 7").scale(0.95).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = Tex(r"40 to 49: 4").scale(0.95).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m8))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): Stem and leaf
        self.next_band(2)
        t2 = Tex(r"Stem and leaf").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = Tex(r"2 | 3 5 7 9").scale(0.95).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m9))
        self.wait(2)
        m10 = Tex(r"3 | 1 2 3 5 6 8 8").scale(0.95).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = Tex(r"4 | 0 1 5 7").scale(0.95).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"Key: 2 | 3 means 23").scale(0.95).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m12))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): Counting in fives
        self.next_band(3)
        t3 = Tex(r"Counting in fives").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = Tex(r"Each answer = one stroke").scale(0.95).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m13))
        self.wait(2)
        m14 = Tex(r"Fifth stroke crosses the four").scale(0.95).shift(band_shift(3) + DOWN * 0.85)
        self.play(Write(m14))
        self.wait(2)
        m15 = Tex(r"2 gates + 4 strokes = 14").scale(0.95).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m15))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_5): Stems and leaves
        self.next_band(4)
        t4 = Tex(r"Stems and leaves").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m16 = Tex(r"1 | 2 5").scale(0.95).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m16))
        self.wait(2)
        m17 = Tex(r"2 | 1 3 3").scale(0.95).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m17))
        self.wait(2)
        m18 = Tex(r"3 | 0").scale(0.95).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m18))
        self.wait(2)
        m19 = Tex(r"Longest row: the 20s").scale(0.95).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m19))
        self.wait(2)
        self.wait(3)
