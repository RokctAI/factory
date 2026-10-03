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


class CollectingDataSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Posing a question
        t0 = Tex(r"Posing a question").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = Tex(r"Vague: Do learners like transport?").scale(0.95).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex(r"Clear: How do Grade 7 learners travel to school?").scale(0.95).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = Tex(r"Categories: walk, taxi, bus, car").scale(0.95).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Numbers: minutes travelling").scale(0.95).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.wait(3)

        # --- Band 1 (subtopic_2): Sources of data
        self.next_band(1)
        t1 = Tex(r"Sources of data").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = Tex(r"Collect yourself: questionnaire, observe, measure").scale(0.95).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        m6 = Tex(r"Use existing data: registers, newspapers, Stats SA").scale(0.95).shift(band_shift(1) + DOWN * 0.85)
        self.play(Write(m6))
        self.wait(2)
        m7 = Tex(r"Transport question: ask the learners").scale(0.95).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m7))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): Population and sample
        self.next_band(2)
        t2 = Tex(r"Population and sample").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m8 = Tex(r"Population: all 240 Grade 7 learners").scale(0.95).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m8))
        self.wait(2)
        m9 = Tex(r"Sample: 40 learners chosen fairly").scale(0.95).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m9))
        self.wait(2)
        m10 = Tex(r"Unfair: only learners on the school bus").scale(0.95).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m10))
        self.wait(2)
        m11 = Tex(r"Fair: names drawn at random").scale(0.95).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m11))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): Who are we asking?
        self.next_band(3)
        t3 = Tex(r"Who are we asking?").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m12 = Tex(r"Everyone in the grade = population").scale(0.95).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m12))
        self.wait(2)
        m13 = Tex(r"Some of them = sample").scale(0.95).shift(band_shift(3) + DOWN * 0.85)
        self.play(Write(m13))
        self.wait(2)
        m14 = Tex(r"Names in a hat = fair").scale(0.95).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m14))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_5): A clear question
        self.next_band(4)
        t4 = Tex(r"A clear question").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m15 = Tex(r"Who? Grade 7 learners at our school").scale(0.95).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m15))
        self.wait(2)
        m16 = Tex(r"What? Favourite sport to play").scale(0.95).shift(band_shift(4) + DOWN * 0.85)
        self.play(Write(m16))
        self.wait(2)
        m17 = Tex(r"Source: ask the learners").scale(0.95).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m17))
        self.wait(2)
        self.wait(3)
