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
# dwell time proportional to subtopics.json (150/130/130/130/130 of
# 670 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class AddSubFractionsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Same-size pieces first
        t0 = Tex(r"Same-size pieces first").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"\frac{2}{5} + \frac{1}{5} = \frac{3}{5} \qquad \frac{1}{2} + \frac{3}{8} = \frac{7}{8}").scale(1.0).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"\frac{3}{4} + \frac{2}{3} = \frac{9}{12} + \frac{8}{12} = \frac{17}{12} = 1\frac{5}{12}").scale(1.0).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m2, color=GREEN)))
        self.wait(1.5)
        m3 = MathTex(r"\frac{3}{4} - \frac{2}{3} = \frac{9}{12} - \frac{8}{12} = \frac{1}{12}").scale(1.0).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Never add the denominators").scale(0.95).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.wait(4)

        # --- Band 1 (subtopic_2): Adding mixed numbers
        self.next_band(1)
        t1 = Tex(r"Adding mixed numbers").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"2\frac{3}{4} + 1\frac{2}{3} = 3 + \frac{9}{12} + \frac{8}{12}").scale(1.0).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"= 3 + \frac{17}{12} = 3 + 1\frac{5}{12}").scale(1.0).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"= 4\frac{5}{12}").scale(1.0).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m7, color=GREEN)))
        self.wait(1.5)
        m8 = MathTex(r"\text{Or: } \frac{33}{12} + \frac{20}{12} = \frac{53}{12} = 4\frac{5}{12}").scale(1.0).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m8))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): Borrowing a whole
        self.next_band(2)
        t2 = Tex(r"Borrowing a whole").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"2\frac{3}{4} - 1\frac{2}{3} = 1\frac{1}{12}").scale(1.0).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"2\frac{2}{3} - 1\frac{3}{4} = 2\frac{8}{12} - 1\frac{9}{12}").scale(1.0).shift(band_shift(2) + UP * 0.18)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"= 1\frac{20}{12} - 1\frac{9}{12}").scale(1.0).shift(band_shift(2) + DOWN * 0.85)
        self.play(Write(m11))
        self.wait(2)
        m12 = MathTex(r"= \frac{11}{12}").scale(1.0).shift(band_shift(2) + DOWN * 1.87)
        self.play(Write(m12))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m12, color=GREEN)))
        self.wait(1.5)
        m13 = MathTex(r"\text{Check: } \frac{32}{12} - \frac{21}{12} = \frac{11}{12}").scale(1.0).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m13))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): Mixing the batter
        self.next_band(3)
        t3 = Tex(r"Mixing the batter").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m14 = Tex(r"Whole cups: 2 + 1 = 3").scale(0.95).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"\frac{3}{4} + \frac{2}{3} = \frac{9}{12} + \frac{8}{12} = 1\frac{5}{12}").scale(1.0).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m15))
        self.wait(2)
        m16 = MathTex(r"4\frac{5}{12} \text{ cups}").scale(1.0).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m16))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m16, color=GREEN)))
        self.wait(1.5)
        m17 = Tex(r"Check: almost 3 + almost 2 = almost 5").scale(0.95).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m17))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_5): How much more flour?
        self.next_band(4)
        t4 = Tex(r"How much more flour?").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m18 = MathTex(r"2\frac{3}{4} - 1\frac{2}{3} = 1\frac{1}{12}").scale(1.0).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m18))
        self.wait(2)
        m19 = Tex(r"Not enough twelfths? Open a whole cup: 12/12").scale(0.95).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m19))
        self.wait(2)
        m20 = MathTex(r"2\frac{2}{3} - 1\frac{3}{4} = \frac{11}{12}").scale(1.0).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m20))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m20, color=GREEN)))
        self.wait(1.5)
        m21 = Tex(r"Add back to check").scale(0.95).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m21))
        self.wait(2)
        self.wait(3)
