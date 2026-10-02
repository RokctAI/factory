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
# the allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (260/190/190/210/240/200/200 of
# 1490 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ScientificNotationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Powers of Ten and Scientific Notation
        t0 = Tex(r"Powers of Ten and Scientific Notation").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"10^2 = 100 \qquad 10^3 = 1\,000 \qquad 10^6 = 1\,000\,000").scale(1.1).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"3{,}4 \times 10^5 = 340\,000").scale(1.1).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"a \times 10^n, \quad 1 \le a < 10").scale(1.1).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"34 x 10^4 and 0,34 x 10^6 have the same value but are not scientific notation").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 1 (subtopic_2): Converting into Scientific Notation
        self.next_band(1)
        t1 = Tex(r"Converting into Scientific Notation").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"150\,000\,000 = 1{,}5 \times 10^8").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"62\,000\,000 = 6{,}2 \times 10^7 \qquad 300\,000 = 3 \times 10^5").scale(1.1).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"425\,000 = 4{,}25 \times 10^5").scale(1.1).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = Tex(r"Exponent = number of digits minus one").scale(1.05).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m8))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m8, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 2 (subtopic_3): Converting Back
        self.next_band(2)
        t2 = Tex(r"Converting Back").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"2{,}7 \times 10^6 = 2\,700\,000").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"9{,}05 \times 10^4 = 90\,500 \qquad 8 \times 10^3 = 8\,000").scale(1.1).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = Tex(r"Calculator 2.7E06 means 2,7 x 10^6").scale(1.05).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"Digits in the ordinary number = exponent + 1").scale(1.05).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(m12))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m12, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 3 (subtopic_4): Comparing in Scientific Notation
        self.next_band(3)
        t3 = Tex(r"Comparing in Scientific Notation").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"3{,}9 \times 10^6 < 1{,}2 \times 10^7 \quad \text{(exponents 6 < 7)}").scale(1.1).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"4{,}25 \times 10^5 < 4{,}8 \times 10^5 \quad \text{(same exponent)}").scale(1.1).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"25 \times 10^5 = 2{,}5 \times 10^6 \quad \text{normalise first}").scale(1.1).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        m16 = Tex(r"Exponent first; first factor only when exponents tie").scale(1.05).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m16))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m16, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): When the Calculator Runs Out of Room
        self.next_band(4)
        t4 = Tex(r"When the Calculator Runs Out of Room").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = Tex(r"Calculator 1.2E10 means 1,2 x 10^10").scale(1.05).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"1{,}2 \times 10^{10} = 12\,000\,000\,000").scale(1.1).shift(band_shift(4) + UP * 0.18)
        self.play(Write(m18))
        self.wait(2)
        m19 = Tex(r"Exponent = zoom setting: 10^6 millions, 10^9 billions").scale(1.05).shift(band_shift(4) + DOWN * 0.85)
        self.play(Write(m19))
        self.wait(2)
        m20 = MathTex(r"34 \times 10^4 \to 3{,}4 \times 10^5").scale(1.1).shift(band_shift(4) + DOWN * 1.87)
        self.play(Write(m20))
        self.wait(2)
        m21 = Tex(r"Exactly one non-zero digit before the comma").scale(1.05).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m21))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m21, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 5 (subtopic_6): Real Numbers in Scientific Notation
        self.next_band(5)
        t5 = Tex(r"Real Numbers in Scientific Notation").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        m22 = MathTex(r"\text{Earth–Sun } 1{,}5 \times 10^8 \text{ km} \qquad \text{Neptune } 4{,}5 \times 10^9 \text{ km}").scale(1.1).shift(band_shift(5) + UP * 1.2)
        self.play(Write(m22))
        self.wait(2)
        m23 = MathTex(r"\text{SA } 6{,}2 \times 10^7 \qquad \text{World } 8 \times 10^9").scale(1.1).shift(band_shift(5) + DOWN * 0.17)
        self.play(Write(m23))
        self.wait(2)
        m24 = MathTex(r"\text{Sand } 7{,}5 \times 10^{18} < \text{Stars } 2 \times 10^{22}").scale(1.1).shift(band_shift(5) + DOWN * 1.53)
        self.play(Write(m24))
        self.wait(2)
        m25 = Tex(r"Exponent gives the size class; first factor fine-tunes").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(m25))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m25, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 6 (subtopic_7): Examination Technique
        self.next_band(6)
        t6 = Tex(r"Examination Technique").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(t6))
        self.wait(1.5)
        m26 = MathTex(r"307\,000\,000 = 3{,}07 \times 10^8").scale(1.1).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m26))
        self.wait(2)
        m27 = MathTex(r"5{,}02 \times 10^6 = 5\,020\,000").scale(1.1).shift(band_shift(6) + DOWN * 0.17)
        self.play(Write(m27))
        self.wait(2)
        m28 = MathTex(r"70 \times 10^4 = 7 \times 10^5").scale(1.1).shift(band_shift(6) + DOWN * 1.53)
        self.play(Write(m28))
        self.wait(2)
        m29 = Tex(r"Normalise, then compare exponents, then first factors.").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m29))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m29, color=GREEN)))
        self.wait(1.5)
        self.wait(3)
