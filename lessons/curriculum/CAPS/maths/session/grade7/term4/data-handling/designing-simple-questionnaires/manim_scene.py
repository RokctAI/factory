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


class QuestionnaireSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Question formats
        t0 = Tex(r"Question formats").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = Tex(r"Yes / No: Do you play sport after school?").scale(0.95).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex(r"Multiple choice: sport, music, homework club, home, other").scale(0.95).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = Tex(r"Ranges: less than 1 h, 1 to less than 2 h, 2 h or more").scale(0.95).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"One idea per question").scale(0.95).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.wait(3)

        # --- Band 1 (subtopic_2): Leading or neutral?
        self.next_band(1)
        t1 = Tex(r"Leading or neutral?").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = Tex(r"Leading: Don't you agree the day is far too long?").scale(0.95).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        m6 = Tex(r"Neutral: How do you feel about the length of the day?").scale(0.95).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = Tex(r"Options: too long, about right, too short").scale(0.95).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = Tex(r"Respect privacy").scale(0.95).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m8))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): No gaps, no overlaps
        self.next_band(2)
        t2 = Tex(r"No gaps, no overlaps").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = Tex(r"Poor: 6-7, 7-8, 8-9: 7 fits twice, 10 fits nowhere").scale(0.95).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m9))
        self.wait(2)
        m10 = Tex(r"Better: less than 7, 7 to less than 8,").scale(0.95).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = Tex(r"8 to less than 9, 9 or more").scale(0.95).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"Pilot test first").scale(0.95).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m12))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): Fair questions
        self.next_band(3)
        t3 = Tex(r"Fair questions").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = Tex(r"Leading: You don't like it, do you?").scale(0.95).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m13))
        self.wait(2)
        m14 = Tex(r"Fair: What did you think? Loved it, okay, didn't like it").scale(0.95).shift(band_shift(3) + DOWN * 0.85)
        self.play(Write(m14))
        self.wait(2)
        m15 = Tex(r"Short, one thing, no hints").scale(0.95).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m15))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_5): Boxes with no gaps
        self.next_band(4)
        t4 = Tex(r"Boxes with no gaps").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m16 = Tex(r"Poor: 1-2, 2-3, 4 or more").scale(0.95).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m16))
        self.wait(2)
        m17 = Tex(r"Better: 0, 1, 2, 3, 4 or more").scale(0.95).shift(band_shift(4) + DOWN * 0.85)
        self.play(Write(m17))
        self.wait(2)
        m18 = Tex(r"Every answer, exactly one box").scale(0.95).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m18))
        self.wait(2)
        self.wait(3)
