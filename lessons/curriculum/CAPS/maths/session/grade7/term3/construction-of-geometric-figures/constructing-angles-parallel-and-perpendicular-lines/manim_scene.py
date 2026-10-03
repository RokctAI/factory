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


class ConstructionsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Constructing $65^\circ$
        t0 = Tex(r"Constructing $65^\circ$").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = Tex(r"1. Draw an arm, mark the vertex").scale(0.95).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex(r"2. Centre on vertex, baseline on arm").scale(0.95).shift(UP * 0.18)
        self.play(Write(m2))
        self.wait(2)
        m3 = Tex(r"3. Dot at 65 on the scale from 0").scale(0.95).shift(DOWN * 0.85)
        self.play(Write(m3))
        self.wait(2)
        m4 = MathTex(r"4. \text{Join vertex to dot: } 65^\circ").scale(1.0).shift(DOWN * 1.87)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        m5 = MathTex(r"250^\circ: \; \text{draw } 110^\circ, \text{ mark outside}").scale(1.0).shift(DOWN * 2.90)
        self.play(Write(m5))
        self.wait(2)
        self.wait(4)

        # --- Band 1 (subtopic_2): Perpendicular lines
        self.next_band(1)
        t1 = Tex(r"Perpendicular lines").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m6 = Tex(r"Meet at $90^\circ$, symbol $\perp$").scale(0.95).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m6))
        self.wait(2)
        m7 = Tex(r"Protractor: mark 90 and join").scale(0.95).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m7))
        self.wait(2)
        m8 = MathTex(r"\text{Compass: arcs from } A \text{ and } B, \text{ join the crossings}").scale(1.0).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m8))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m8, color=GREEN)))
        self.wait(1.5)
        m9 = Tex(r"Check with a protractor or set square").scale(0.95).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m9))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): Parallel lines
        self.next_band(2)
        t2 = Tex(r"Parallel lines").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m10 = Tex(r"Never meet, always equal distance apart, symbol $\parallel$").scale(0.95).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m10))
        self.wait(2)
        m11 = Tex(r"Method 1: two perpendiculars, equal lengths").scale(0.95).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m11))
        self.wait(2)
        m12 = MathTex(r"\text{Method 2: equal angles on a transversal}").scale(1.0).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m12))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m12, color=GREEN)))
        self.wait(1.5)
        m13 = Tex(r"Check: equal distance at two places").scale(0.95).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m13))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): The garden path
        self.next_band(3)
        t3 = Tex(r"The garden path").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m14 = Tex(r"Draw the fence, dot the start").scale(0.95).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m14))
        self.wait(2)
        m15 = Tex(r"Protractor on the dot, flat edge on the fence").scale(0.95).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m15))
        self.wait(2)
        m16 = MathTex(r"\text{Mark } 65, \text{ join: the path}").scale(1.0).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m16))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m16, color=GREEN)))
        self.wait(1.5)
        m17 = Tex(r"65 is less than a square corner").scale(0.95).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m17))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_5): Square corners and tracks
        self.next_band(4)
        t4 = Tex(r"Square corners and tracks").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m18 = Tex(r"Perpendicular: square corner, $90^\circ$").scale(0.95).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m18))
        self.wait(2)
        m19 = Tex(r"Compass: arcs from both ends, join the crossings").scale(0.95).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m19))
        self.wait(2)
        m20 = MathTex(r"\text{Parallel: same gap at two places}").scale(1.0).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m20))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m20, color=GREEN)))
        self.wait(1.5)
        m21 = Tex(r"Like railway tracks: never meet").scale(0.95).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m21))
        self.wait(2)
        self.wait(3)
