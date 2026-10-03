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
# dwell time proportional to subtopics.json (200/180/180/210/200/190/200 of
# 1360 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FractionTechniquesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Fraction Calculation Techniques
        t0 = Tex(r"Fraction Calculation Techniques").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"4\tfrac{2}{5} = \frac{4 \times 5 + 2}{5} = \frac{22}{5}").scale(1.1).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"\frac{29}{6} = 4\tfrac{5}{6} \qquad (29 \div 6 = 4 \text{ rem } 5)").scale(1.1).shift(DOWN * 0.85)
        self.play(Write(m2))
        self.wait(2)
        m3 = Tex(r"Improper to calculate, mixed to answer").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(m3))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m3, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 1 (subtopic_2): Simplifying
        self.next_band(1)
        t1 = Tex(r"Simplifying").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m4 = MathTex(r"\frac{36}{48} = \frac{36 \div 12}{48 \div 12} = \frac{3}{4}").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m4))
        self.wait(2)
        m5 = MathTex(r"36 = 2^2 \times 3^2 \qquad 48 = 2^4 \times 3 \qquad \text{HCF} = 12").scale(1.1).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"\frac{15}{35} = \frac{3}{7} \qquad \frac{28}{63} = \frac{4}{9}").scale(1.1).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m6))
        self.wait(2)
        m7 = Tex(r"Cancel factors, never terms").scale(1.05).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m7))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m7, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 2 (subtopic_3): Equivalence and Ordering
        self.next_band(2)
        t2 = Tex(r"Equivalence and Ordering").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m8 = MathTex(r"\frac{3}{8} = \frac{15}{40}").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(m8))
        self.wait(2)
        m9 = MathTex(r"\frac{2}{3} = \frac{16}{24}, \quad \frac{5}{8} = \frac{15}{24}, \quad \frac{7}{12} = \frac{14}{24}").scale(1.1).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"\frac{5}{8} \text{ vs } \frac{7}{11}: \quad 55 < 56 \Rightarrow \frac{7}{11} \text{ larger}").scale(1.1).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"\frac{5}{12} + \frac{7}{18} = \frac{15}{36} + \frac{14}{36} = \frac{29}{36}").scale(1.1).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(m11))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m11, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 3 (subtopic_4): Cancelling in Products
        self.next_band(3)
        t3 = Tex(r"Cancelling in Products").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m12 = MathTex(r"\frac{14}{15} \times \frac{25}{21} = \frac{2}{3} \times \frac{5}{3} = \frac{10}{9}").scale(1.1).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m12))
        self.wait(2)
        m13 = Tex(r"Any numerator against any denominator in a product").scale(1.05).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"2\tfrac{2}{5} \times 1\tfrac{7}{8} = \frac{12}{5} \times \frac{15}{8} = \frac{3 \times 3}{2} = \frac{9}{2}").scale(1.1).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m14))
        self.wait(2)
        m15 = Tex(r"Never cancel in a sum").scale(1.05).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m15))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m15, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): Same Cake, Different Slices
        self.next_band(4)
        t4 = Tex(r"Same Cake, Different Slices").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m16 = MathTex(r"\frac{3}{4} = \frac{6}{8} = \frac{12}{16}").scale(1.1).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m16))
        self.wait(2)
        m17 = MathTex(r"\frac{36}{48} \to \text{glue in twelves} \to \frac{3}{4}").scale(1.1).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"\frac{5}{8} = \frac{15}{24} \qquad \frac{7}{12} = \frac{14}{24}").scale(1.1).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m18))
        self.wait(2)
        m19 = Tex(r"One knife for everyone").scale(1.05).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m19))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m19, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 5 (subtopic_6): Cut It Down First
        self.next_band(5)
        t5 = Tex(r"Cut It Down First").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        m20 = MathTex(r"\frac{14}{15} \times \frac{25}{21}: \quad 14 = 2 \times 7, \; 21 = 3 \times 7").scale(1.1).shift(band_shift(5) + UP * 1.2)
        self.play(Write(m20))
        self.wait(2)
        m21 = MathTex(r"25 = 5 \times 5, \; 15 = 3 \times 5").scale(1.1).shift(band_shift(5) + DOWN * 0.17)
        self.play(Write(m21))
        self.wait(2)
        m22 = MathTex(r"= \frac{2}{3} \times \frac{5}{3} = \frac{10}{9}").scale(1.1).shift(band_shift(5) + DOWN * 1.53)
        self.play(Write(m22))
        self.wait(2)
        m23 = MathTex(r"\frac{2}{3} + \frac{3}{5} = \frac{10}{15} + \frac{9}{15} = \frac{19}{15} \quad \text{no cancelling}").scale(1.1).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(m23))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m23, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 6 (subtopic_7): The Toolkit
        self.next_band(6)
        t6 = Tex(r"The Toolkit").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(t6))
        self.wait(1.5)
        m24 = Tex(r"Convert: before multiply, divide, power, root").scale(1.05).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m24))
        self.wait(2)
        m25 = Tex(r"Simplify: at the end, with the HCF").scale(1.05).shift(band_shift(6) + DOWN * 0.17)
        self.play(Write(m25))
        self.wait(2)
        m26 = Tex(r"Equivalents over the LCM: add, subtract, compare").scale(1.05).shift(band_shift(6) + DOWN * 1.53)
        self.play(Write(m26))
        self.wait(2)
        m27 = MathTex(r"2\tfrac{1}{4} \times 1\tfrac{1}{3} = \frac{9}{4} \times \frac{4}{3} = 3").scale(1.1).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m27))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m27, color=GREEN)))
        self.wait(1.5)
        self.wait(3)
