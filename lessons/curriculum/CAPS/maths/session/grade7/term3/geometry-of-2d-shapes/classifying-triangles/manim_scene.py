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
# dwell time proportional to subtopics.json (140/120/120/120/120 of
# 620 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ClassifyingTrianglesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Triangles by sides
        t0 = Tex(r"Triangles by sides").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = Tex(r"Equilateral: 3 equal sides (all angles $60^\circ$)").scale(0.95).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex(r"Isosceles: at least 2 equal sides (equal base angles)").scale(0.95).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = Tex(r"Scalene: no equal sides").scale(0.95).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = MathTex(r"2;2;2 \text{ equilateral} \quad 2{,}5;2{,}5;3 \text{ isosceles} \quad 1{,}2;1{,}6;2 \text{ scalene}").scale(1.0).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        self.wait(4)

        # --- Band 1 (subtopic_2): Triangles by angles
        self.next_band(1)
        t1 = Tex(r"Triangles by angles").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = Tex(r"Acute-angled: all angles $< 90^\circ$").scale(0.95).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        m6 = Tex(r"Right-angled: one angle $= 90^\circ$").scale(0.95).shift(band_shift(1) + UP * 0.18)
        self.play(Write(m6))
        self.wait(2)
        m7 = Tex(r"Obtuse-angled: one angle $> 90^\circ$").scale(0.95).shift(band_shift(1) + DOWN * 0.85)
        self.play(Write(m7))
        self.wait(2)
        m8 = MathTex(r"\text{Angles add to } 180^\circ \text{: at most one right or obtuse angle}").scale(1.0).shift(band_shift(1) + DOWN * 1.87)
        self.play(Write(m8))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m8, color=GREEN)))
        self.wait(1.5)
        m9 = Tex(r"Check the LARGEST angle only").scale(0.95).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m9))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): Both names
        self.next_band(2)
        t2 = Tex(r"Both names").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m10 = MathTex(r"\text{Right-angled isosceles: } 90^\circ, 45^\circ, 45^\circ").scale(1.0).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m10))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m10, color=GREEN)))
        self.wait(1.5)
        m11 = MathTex(r"\text{Obtuse isosceles: } 30^\circ, 30^\circ, 120^\circ").scale(1.0).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m11))
        self.wait(2)
        m12 = MathTex(r"\text{Acute scalene: } 50^\circ, 60^\circ, 70^\circ").scale(1.0).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m12))
        self.wait(2)
        m13 = Tex(r"Right-angled equilateral? Impossible.").scale(0.95).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m13))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): Triangles in the roof
        self.next_band(3)
        t3 = Tex(r"Triangles in the roof").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m14 = Tex(r"3 equal sides: equilateral").scale(0.95).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m14))
        self.wait(2)
        m15 = Tex(r"2 equal sides: isosceles").scale(0.95).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m15))
        self.wait(2)
        m16 = Tex(r"No equal sides: scalene").scale(0.95).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m16))
        self.wait(2)
        m17 = MathTex(r"\text{Count the equal sides}").scale(1.0).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m17))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m17, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 4 (subtopic_5): Sharp, square and wide
        self.next_band(4)
        t4 = Tex(r"Sharp, square and wide").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m18 = Tex(r"All sharp: acute-angled").scale(0.95).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m18))
        self.wait(2)
        m19 = Tex(r"One square corner: right-angled").scale(0.95).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m19))
        self.wait(2)
        m20 = Tex(r"One wide corner: obtuse-angled").scale(0.95).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m20))
        self.wait(2)
        m21 = MathTex(r"\text{Set square: right-angled isosceles}").scale(1.0).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m21))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m21, color=GREEN)))
        self.wait(1.5)
        self.wait(3)
