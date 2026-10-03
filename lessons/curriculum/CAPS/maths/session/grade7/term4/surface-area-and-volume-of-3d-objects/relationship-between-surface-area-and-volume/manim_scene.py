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


class SurfaceAreaVolumeRelationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): 24 cubes, three boxes
        t0 = Tex(r"24 cubes, three boxes").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"24 \times 1 \times 1: \; SA = 98 \text{ cm}^2").scale(1.0).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"6 \times 4 \times 1: \; SA = 68 \text{ cm}^2").scale(1.0).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"4 \times 3 \times 2: \; SA = 52 \text{ cm}^2").scale(1.0).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m3, color=GREEN)))
        self.wait(1.5)
        m4 = Tex(r"Same volume 24 cm$^3$; compact = less surface").scale(0.95).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.wait(3)

        # --- Band 1 (subtopic_2): Growing a cube
        self.next_band(1)
        t1 = Tex(r"Growing a cube").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"s = 1: \; SA = 6, \; V = 1").scale(1.0).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"s = 2: \; SA = 24 \; (\times 4), \; V = 8 \; (\times 8)").scale(1.0).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"s = 3: \; SA = 54 \; (\times 9), \; V = 27 \; (\times 27)").scale(1.0).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m7, color=GREEN)))
        self.wait(1.5)
        m8 = Tex(r"Volume grows faster than surface area").scale(0.95).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m8))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): Surface per volume
        self.next_band(2)
        t2 = Tex(r"Surface per volume").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"s=1: 6/1 \quad s=2: 24/8 = 3 \quad s=3: 54/27 = 2").scale(1.0).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"1\,000 \text{ cm}^3: \; 10^3 \to 600, \; 20 \times 10 \times 5 \to 700, \; 40 \times 5 \times 5 \to 850").scale(1.0).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m10, color=GREEN)))
        self.wait(1.5)
        m11 = Tex(r"Cube: least cardboard").scale(0.95).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"Real boxes balance cost, shelves, advertising").scale(0.95).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m12))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): 24 blocks, different boxes
        self.next_band(3)
        t3 = Tex(r"24 blocks, different boxes").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = Tex(r"Long row: 98 squares of wrapping").scale(0.95).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m13))
        self.wait(2)
        m14 = Tex(r"Flat slab: 68 squares").scale(0.95).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"\text{Chunky block: 52 squares}").scale(1.0).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m15, color=GREEN)))
        self.wait(1.5)
        m16 = Tex(r"Compact = less wrapping").scale(0.95).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m16))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_5): When a cube grows
        self.next_band(4)
        t4 = Tex(r"When a cube grows").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = MathTex(r"1 \to 2: \; V \times 8, \; SA \times 4").scale(1.0).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"1 \to 3: \; V \times 27, \; SA \times 9").scale(1.0).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"\text{Inside grows faster than outside}").scale(1.0).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m19, color=GREEN)))
        self.wait(1.5)
        m20 = Tex(r"Elephants stay warm; crushed ice melts fast").scale(0.95).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m20))
        self.wait(2)
        self.wait(3)
