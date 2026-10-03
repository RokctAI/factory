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
# dwell time proportional to subtopics.json (120/120/120/120/120 of
# 600 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class EquivalentDescriptionsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Five descriptions
        t0 = Tex(r"Five descriptions").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = Tex(r"Words: R50 plus R2 per minute").scale(0.95).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex(r"Flow: $m \to \times 2 \to + 50 \to c$").scale(0.95).shift(UP * 0.18)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"m: 0, 10, 20, 30 \qquad c: 50, 70, 90, 110").scale(1.0).shift(DOWN * 0.85)
        self.play(Write(m3))
        self.wait(2)
        m4 = MathTex(r"c = 2 \times m + 50").scale(1.0).shift(DOWN * 1.87)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        m5 = MathTex(r"2 \times 10 + 50 = 70").scale(1.0).shift(DOWN * 2.90)
        self.play(Write(m5))
        self.wait(2)
        self.wait(3)

        # --- Band 1 (subtopic_2): Equivalent or not?
        self.next_band(1)
        t1 = Tex(r"Equivalent or not?").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m6 = MathTex(r"c = 2m + 50: \; 0 \to 50, \; 10 \to 70, \; 20 \to 90").scale(1.0).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"+50 \text{ then } \times 2: \; 10 \to 120 \; \text{(not equivalent)}").scale(1.0).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m7))
        self.wait(2)
        m8 = MathTex(r"2 \times (m + 25) = 2m + 50").scale(1.0).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m8))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m8, color=GREEN)))
        self.wait(1.5)
        m9 = Tex(r"Test several inputs, then give a reason").scale(0.95).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m9))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): Interpreting in context
        self.next_band(2)
        t2 = Tex(r"Interpreting in context").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m10 = Tex(r"In $c = 2m + 50$: 2 = rand per minute, 50 = fixed fee").scale(0.95).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"\text{Plan B: } c = 4m").scale(1.0).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m11))
        self.wait(2)
        m12 = MathTex(r"m = 10: \; A = 70, \; B = 40 \qquad m = 30: \; A = 110, \; B = 120").scale(1.0).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m12))
        self.wait(2)
        m13 = MathTex(r"m = 25: \; A = B = R100").scale(1.0).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m13))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m13, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): Five outfits, one rule
        self.next_band(3)
        t3 = Tex(r"Five outfits, one rule").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m14 = Tex(r"Words: R50 + R2 per minute").scale(0.95).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m14))
        self.wait(2)
        m15 = Tex(r"Machine: $\times 2 \to +50$").scale(0.95).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m15))
        self.wait(2)
        m16 = MathTex(r"0 \to 50, \; 10 \to 70, \; 20 \to 90, \; 30 \to 110").scale(1.0).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m16))
        self.wait(2)
        m17 = MathTex(r"c = 2 \times m + 50").scale(1.0).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m17))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m17, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 4 (subtopic_5): Spot the imposter
        self.next_band(4)
        t4 = Tex(r"Spot the imposter").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m18 = MathTex(r"\text{Table: } 10 \to 70 \; \checkmark").scale(1.0).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"+50 \text{ then } \times 2: \; 10 \to 120 \; \times").scale(1.0).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m19))
        self.wait(2)
        m20 = MathTex(r"2 \times (10 + 25) = 70 \; \checkmark").scale(1.0).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m20))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m20, color=GREEN)))
        self.wait(1.5)
        m21 = Tex(r"Test several inputs, including 0").scale(0.95).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m21))
        self.wait(2)
        self.wait(3)
