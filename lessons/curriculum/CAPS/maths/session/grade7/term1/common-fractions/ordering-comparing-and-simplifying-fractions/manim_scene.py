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
# dwell time proportional to subtopics.json (160/130/120/130/130 of
# 670 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class OrderingFractionsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Equivalent fractions
        t0 = Tex(r"Equivalent fractions").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"\frac{3}{4} = \frac{15}{20} = \frac{750}{1000}").scale(1.0).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"\frac{375}{1000} = \frac{75}{200} = \frac{15}{40} = \frac{3}{8}").scale(1.0).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"\frac{375 \div 125}{1000 \div 125} = \frac{3}{8}").scale(1.0).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m3, color=GREEN)))
        self.wait(1.5)
        m4 = Tex(r"Same number on top and bottom: value unchanged").scale(0.95).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.wait(4)

        # --- Band 1 (subtopic_2): Ordering fractions
        self.next_band(1)
        t1 = Tex(r"Ordering fractions").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"\text{LCM}(4, 8, 10) = 40").scale(1.0).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"\frac{3}{4} = \frac{30}{40} \quad \frac{5}{8} = \frac{25}{40} \quad \frac{7}{10} = \frac{28}{40}").scale(1.0).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"\frac{5}{8} < \frac{7}{10} < \frac{3}{4}").scale(1.0).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m7, color=GREEN)))
        self.wait(1.5)
        m8 = MathTex(r"625 < 700 < 750 \text{ thousandths}").scale(1.0).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m8))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): Number line and mixed numbers
        self.next_band(2)
        t2 = Tex(r"Number line and mixed numbers").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = Tex(r"Further right on the number line = larger").scale(0.95).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"\frac{11}{4} = 2\frac{3}{4}").scale(1.0).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m10, color=GREEN)))
        self.wait(1.5)
        m11 = MathTex(r"2\frac{3}{4} = \frac{2 \times 4 + 3}{4} = \frac{11}{4}").scale(1.0).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = MathTex(r"3\frac{1}{10} > 2\frac{9}{10} \qquad 2\frac{6}{8} = 2\frac{3}{4}").scale(1.0).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m12))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): Same-size pieces
        self.next_band(3)
        t3 = Tex(r"Same-size pieces").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = Tex(r"Cut every lunch into 40 tiny pieces").scale(0.95).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"\text{Ayanda } 30 \quad \text{Chloe } 28 \quad \text{Ben } 25").scale(1.0).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"\frac{3}{4} > \frac{7}{10} > \frac{5}{8}").scale(1.0).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m15, color=GREEN)))
        self.wait(1.5)
        m16 = Tex(r"Same-size pieces: just count them").scale(0.95).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m16))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_5): Making fractions simpler
        self.next_band(4)
        t4 = Tex(r"Making fractions simpler").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = MathTex(r"\frac{375}{1000} \to \frac{75}{200} \to \frac{15}{40} \to \frac{3}{8}").scale(1.0).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m17))
        self.wait(2)
        m18 = Tex(r"Divide top and bottom by the same number").scale(0.95).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"\frac{375}{1000} = \frac{3}{8}").scale(1.0).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m19, color=GREEN)))
        self.wait(1.5)
        m20 = Tex(r"Stop when nothing divides both").scale(0.95).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m20))
        self.wait(2)
        self.wait(3)
