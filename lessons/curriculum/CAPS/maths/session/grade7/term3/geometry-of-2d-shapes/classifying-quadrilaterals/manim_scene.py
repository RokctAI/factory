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
# dwell time proportional to subtopics.json (130/120/120/120/120 of
# 610 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ClassifyingQuadrilateralsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The parallelogram family
        t0 = Tex(r"The parallelogram family").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = Tex(r"Parallelogram: both pairs of opposite sides parallel").scale(0.95).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex(r"Rectangle: parallelogram with 4 right angles").scale(0.95).shift(UP * 0.18)
        self.play(Write(m2))
        self.wait(2)
        m3 = Tex(r"Rhombus: parallelogram with 4 equal sides").scale(0.95).shift(DOWN * 0.85)
        self.play(Write(m3))
        self.wait(2)
        m4 = MathTex(r"\text{Square: 4 equal sides AND 4 right angles}").scale(1.0).shift(DOWN * 1.87)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        m5 = MathTex(r"\text{Angles of a quadrilateral: } 360^\circ").scale(1.0).shift(DOWN * 2.90)
        self.play(Write(m5))
        self.wait(2)
        self.wait(3)

        # --- Band 1 (subtopic_2): Trapeziums and kites
        self.next_band(1)
        t1 = Tex(r"Trapeziums and kites").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m6 = Tex(r"Trapezium: at least one pair of parallel sides").scale(0.95).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m6))
        self.wait(2)
        m7 = Tex(r"Kite: two pairs of ADJACENT sides equal").scale(0.95).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m7))
        self.wait(2)
        m8 = MathTex(r"\text{Kite diagonals are perpendicular}").scale(1.0).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m8))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m8, color=GREEN)))
        self.wait(1.5)
        m9 = Tex(r"Opposite sides do not touch; adjacent sides share a corner").scale(0.95).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m9))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): Family tree
        self.next_band(2)
        t2 = Tex(r"Family tree").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m10 = Tex(r"Quadrilateral $\to$ trapezium $\to$ parallelogram $\to$ rectangle / rhombus $\to$ square").scale(0.95).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m10))
        self.wait(2)
        m11 = Tex(r"Kite $\to$ rhombus $\to$ square").scale(0.95).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m11))
        self.wait(2)
        m12 = MathTex(r"\text{All sides equal: rhombus, square}").scale(1.0).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m12))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m12, color=GREEN)))
        self.wait(1.5)
        m13 = Tex(r"All angles $90^\circ$: rectangle, square").scale(0.95).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m13))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): Cutting shapes
        self.next_band(3)
        t3 = Tex(r"Cutting shapes").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m14 = Tex(r"A4 sheet: rectangle").scale(0.95).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m14))
        self.wait(2)
        m15 = Tex(r"Cut to equal sides: square").scale(0.95).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m15))
        self.wait(2)
        m16 = Tex(r"Push a square over: rhombus").scale(0.95).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m16))
        self.wait(2)
        m17 = MathTex(r"\text{Push a rectangle over: parallelogram}").scale(1.0).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m17))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m17, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 4 (subtopic_5): Building the kite
        self.next_band(4)
        t4 = Tex(r"Building the kite").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m18 = Tex(r"Equal sides that are NEIGHBOURS: kite").scale(0.95).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"\text{Sticks (diagonals) cross at } 90^\circ").scale(1.0).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m19))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m19, color=GREEN)))
        self.wait(1.5)
        m20 = Tex(r"One pair of parallel sides: trapezium").scale(0.95).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m20))
        self.wait(2)
        m21 = Tex(r"Check: parallel? equal? square corners?").scale(0.95).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m21))
        self.wait(2)
        self.wait(3)
