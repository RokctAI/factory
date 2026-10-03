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
# dwell time proportional to subtopics.json (150/120/120/120/120 of
# 630 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class FractionDecimalPercentSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Fraction to decimal
        t0 = Tex(r"Fraction to decimal").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"\frac{3}{5} = \frac{6}{10} = 0{,}6 \qquad \frac{7}{20} = \frac{35}{100} = 0{,}35").scale(1.0).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"\frac{3}{8} = \frac{375}{1000} = 0{,}375").scale(1.0).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m2, color=GREEN)))
        self.wait(1.5)
        m3 = MathTex(r"3 \div 8 = 0{,}375 \qquad \frac{1}{3} = 0{,}333\ldots").scale(1.0).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Learn: 1/2, 1/4, 3/4, 1/5, 1/8, 1/10").scale(0.95).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.wait(4)

        # --- Band 1 (subtopic_2): Decimal to fraction
        self.next_band(1)
        t1 = Tex(r"Decimal to fraction").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"0{,}6 = \frac{6}{10} = \frac{3}{5} \qquad 0{,}35 = \frac{35}{100} = \frac{7}{20}").scale(1.0).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"0{,}375 = \frac{375}{1000} = \frac{3}{8}").scale(1.0).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m6, color=GREEN)))
        self.wait(1.5)
        m7 = MathTex(r"2{,}75 = 2\frac{75}{100} = 2\frac{3}{4}").scale(1.0).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = MathTex(r"0{,}05 = \frac{5}{100} = \frac{1}{20}").scale(1.0).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m8))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): Three forms, one number
        self.next_band(2)
        t2 = Tex(r"Three forms, one number").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"\frac{3}{8} = 0{,}375 = 37{,}5\%").scale(1.0).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m9))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m9, color=GREEN)))
        self.wait(1.5)
        m10 = MathTex(r"0{,}6 = 60\% \qquad 1{,}25 = 125\%").scale(1.0).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"45\% = 0{,}45 = \frac{9}{20} \qquad 7\% = 0{,}07").scale(1.0).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"Decimal $\times$ 100 = percentage").scale(0.95).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m12))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): One result, three names
        self.next_band(3)
        t3 = Tex(r"One result, three names").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = Tex(r"3 out of 8 = 375 out of 1 000 = 37,5 out of 100").scale(0.95).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"\frac{3}{8} = 0{,}375 = 37{,}5\%").scale(1.0).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m14, color=GREEN)))
        self.wait(1.5)
        m15 = MathTex(r"\frac{1}{2} = 0{,}5 = 50\% \qquad \frac{1}{4} = 0{,}25 = 25\%").scale(1.0).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        m16 = MathTex(r"\frac{3}{4} = 0{,}75 = 75\% \qquad \frac{1}{10} = 0{,}1 = 10\%").scale(1.0).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m16))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_5): Switching between forms
        self.next_band(4)
        t4 = Tex(r"Switching between forms").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = Tex(r"Percent to decimal: divide by 100").scale(0.95).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m17))
        self.wait(2)
        m18 = Tex(r"Decimal to percent: multiply by 100").scale(0.95).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"0{,}35 = \frac{35}{100} = \frac{7}{20} \qquad \frac{3}{8} = 3 \div 8").scale(1.0).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        m20 = MathTex(r"0{,}4 = \frac{2}{5} = 40\% < 45\%").scale(1.0).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m20))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m20, color=GREEN)))
        self.wait(1.5)
        self.wait(3)
