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


class StraightLinesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Segments, rays and lines
        t0 = Tex(r"Segments, rays and lines").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = Tex(r"Segment AB: two endpoints, measurable").scale(0.95).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex(r"Ray AB: starts at A, goes on forever through B").scale(0.95).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = Tex(r"Line AB: no endpoints, goes on both ways").scale(0.95).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = MathTex(r"\text{Endpoints: segment 2, ray 1, line 0}").scale(1.0).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        self.wait(4)

        # --- Band 1 (subtopic_2): Parallel and perpendicular
        self.next_band(1)
        t1 = Tex(r"Parallel and perpendicular").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"AB \parallel CD: \text{ never meet, same distance apart}").scale(1.0).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"AB \perp CD: \text{ meet at } 90^\circ").scale(1.0).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = Tex(r"Diagrams: matching arrows for parallel; small square for $90^\circ$").scale(0.95).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = MathTex(r"\text{Intersecting: meet at one point}").scale(1.0).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m8))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m8, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 2 (subtopic_3): Using the language
        self.next_band(2)
        t2 = Tex(r"Using the language").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"ABCD: \; AB \parallel DC, \; AD \parallel BC, \; AB \perp BC").scale(1.0).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m9))
        self.wait(2)
        m10 = Tex(r"Main road: line PQ. Taxi route: ray RS. Side street: segment TU.").scale(0.95).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"\text{Endpoints? Then it is a segment}").scale(1.0).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m11, color=GREEN)))
        self.wait(1.5)
        m12 = Tex(r"Ruler, capital letters, arrows, markings").scale(0.95).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m12))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): Roads, routes and streets
        self.next_band(3)
        t3 = Tex(r"Roads, routes and streets").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = Tex(r"Main road: line (no ends)").scale(0.95).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m13))
        self.wait(2)
        m14 = Tex(r"Taxi route: ray (one end)").scale(0.95).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"\text{Side street: segment (two ends), 250 m}").scale(1.0).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m15, color=GREEN)))
        self.wait(1.5)
        m16 = Tex(r"Count the ends!").scale(0.95).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m16))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_5): Meeting and never meeting
        self.next_band(4)
        t4 = Tex(r"Meeting and never meeting").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = Tex(r"Highway lanes: parallel, never meet").scale(0.95).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m17))
        self.wait(2)
        m18 = Tex(r"T-junction: perpendicular, square corner").scale(0.95).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"\text{Slanted crossing: intersecting only}").scale(1.0).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m19, color=GREEN)))
        self.wait(1.5)
        m20 = Tex(r"Test: equal gaps, or a book corner fits").scale(0.95).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m20))
        self.wait(2)
        self.wait(3)
