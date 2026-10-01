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
# dwell time proportional to subtopics.json (240/180/180/190/250/180/210 of
# 1430 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FractionPowersRootsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Squares, Cubes and Roots of Fractions
        t0 = Tex(r"Squares, Cubes and Roots of Fractions").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"\left(\frac{a}{b}\right)^2 = \frac{a^2}{b^2}").scale(1.1).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"\left(\frac{2}{3}\right)^2 = \frac{4}{9} \qquad \left(\frac{3}{4}\right)^2 = \frac{9}{16}").scale(1.1).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"\left(1\tfrac{1}{2}\right)^2 = \left(\frac{3}{2}\right)^2 = \frac{9}{4} = 2\tfrac{1}{4}").scale(1.1).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"A proper fraction squared gets smaller").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 1 (subtopic_2): Cubes
        self.next_band(1)
        t1 = Tex(r"Cubes").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"\left(\frac{a}{b}\right)^3 = \frac{a^3}{b^3}").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"\left(\frac{1}{2}\right)^3 = \frac{1}{8} \qquad \left(\frac{2}{3}\right)^3 = \frac{8}{27}").scale(1.1).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"\left(\frac{2}{3}\right)^2 + \left(\frac{1}{2}\right)^3 = \frac{32}{72} + \frac{9}{72} = \frac{41}{72}").scale(1.1).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = Tex(r"Convert mixed numbers before any power").scale(1.05).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m8))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m8, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 2 (subtopic_3): Square Roots
        self.next_band(2)
        t2 = Tex(r"Square Roots").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"\sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"\sqrt{\frac{9}{16}} = \frac{3}{4} \qquad \sqrt{2\tfrac{1}{4}} = \sqrt{\frac{9}{4}} = \frac{3}{2}").scale(1.1).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"\sqrt{\frac{8}{18}} = \sqrt{\frac{4}{9}} = \frac{2}{3}").scale(1.1).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"Simplify first, then look for perfect squares").scale(1.05).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(m12))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m12, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 3 (subtopic_4): Cube Roots and Mixed Work
        self.next_band(3)
        t3 = Tex(r"Cube Roots and Mixed Work").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"\sqrt[3]{\frac{8}{27}} = \frac{2}{3} \qquad \sqrt[3]{-\frac{1}{8}} = -\frac{1}{2}").scale(1.1).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"\sqrt{\frac{4}{9}} + \sqrt[3]{\frac{1}{8}} - \left(\frac{2}{3}\right)^2 = \frac{2}{3} + \frac{1}{2} - \frac{4}{9}").scale(1.1).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"= \frac{12}{18} + \frac{9}{18} - \frac{8}{18} = \frac{13}{18}").scale(1.1).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        m16 = Tex(r"Every power and root first, then combine").scale(1.05).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m16))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m16, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): A Garden Bed
        self.next_band(4)
        t4 = Tex(r"A Garden Bed").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = MathTex(r"\left(\frac{2}{3}\right)^2 = \frac{4}{9} \text{ m}^2 \qquad \text{4 of 9 small squares}").scale(1.1).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"\left(\frac{3}{2}\right)^2 = \frac{9}{4} = 2\tfrac{1}{4} \text{ m}^2").scale(1.1).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"\sqrt{\frac{9}{16}} = \frac{3}{4} \text{ m}").scale(1.1).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        m20 = Tex(r"Side less than a metre: area number smaller than side").scale(1.05).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m20))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m20, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 5 (subtopic_6): Boxes and Photos
        self.next_band(5)
        t5 = Tex(r"Boxes and Photos").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        m21 = MathTex(r"\left(\frac{1}{2}\right)^3 = \frac{1}{8} \qquad \left(\frac{2}{3}\right)^3 = \frac{8}{27}").scale(1.1).shift(band_shift(5) + UP * 1.2)
        self.play(Write(m21))
        self.wait(2)
        m22 = MathTex(r"\sqrt[3]{\frac{8}{27}} = \frac{2}{3} \qquad \sqrt[3]{3\tfrac{3}{8}} = \frac{3}{2}").scale(1.1).shift(band_shift(5) + DOWN * 0.85)
        self.play(Write(m22))
        self.wait(2)
        m23 = Tex(r"Powers of a proper fraction: repeated shrinking").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(m23))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m23, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 6 (subtopic_7): Bigger or Smaller?
        self.next_band(6)
        t6 = Tex(r"Bigger or Smaller?").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(t6))
        self.wait(1.5)
        m24 = Tex(r"Proper fraction: powers shrink it, roots grow it").scale(1.05).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m24))
        self.wait(2)
        m25 = Tex(r"Number above one: powers grow it, roots shrink it").scale(1.05).shift(band_shift(6) + DOWN * 0.17)
        self.play(Write(m25))
        self.wait(2)
        m26 = MathTex(r"\left(\frac{4}{5}\right)^2 = \frac{16}{25} \qquad \sqrt{\frac{25}{36}} = \frac{5}{6}").scale(1.1).shift(band_shift(6) + DOWN * 1.53)
        self.play(Write(m26))
        self.wait(2)
        m27 = Tex(r"Bracket, convert, top and bottom separately, simplify, check size").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m27))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m27, color=GREEN)))
        self.wait(1.5)
        self.wait(3)
