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
# dwell time proportional to subtopics.json (150/130/120/120/120 of
# 640 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class MeasuringAnglesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Types of angles
        t0 = Tex(r"Types of angles").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = Tex(r"Acute $< 90^\circ$, right $= 90^\circ$, obtuse 90--180").scale(0.95).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex(r"Straight $= 180^\circ$, reflex 180--360, revolution $= 360^\circ$").scale(0.95).shift(UP * 0.18)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"\text{Clock: } 360^\circ \div 12 = 30^\circ \text{ per hour}").scale(1.0).shift(DOWN * 0.85)
        self.play(Write(m3))
        self.wait(2)
        m4 = MathTex(r"2\text{h} = 60^\circ \quad 3\text{h} = 90^\circ \quad 5\text{h} = 150^\circ \quad 6\text{h} = 180^\circ").scale(1.0).shift(DOWN * 1.87)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        m5 = MathTex(r"360^\circ - 60^\circ = 300^\circ \text{ (reflex)}").scale(1.0).shift(DOWN * 2.90)
        self.play(Write(m5))
        self.wait(2)
        self.wait(4)

        # --- Band 1 (subtopic_2): Using a protractor
        self.next_band(1)
        t1 = Tex(r"Using a protractor").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m6 = Tex(r"1. Centre on the vertex").scale(0.95).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m6))
        self.wait(2)
        m7 = Tex(r"2. Baseline along one arm (through 0)").scale(0.95).shift(band_shift(1) + UP * 0.18)
        self.play(Write(m7))
        self.wait(2)
        m8 = Tex(r"3. Read the scale that starts at 0 on that arm").scale(0.95).shift(band_shift(1) + DOWN * 0.85)
        self.play(Write(m8))
        self.wait(2)
        m9 = MathTex(r"\text{Acute? Then } 60^\circ, \text{ not } 120^\circ").scale(1.0).shift(band_shift(1) + DOWN * 1.87)
        self.play(Write(m9))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m9, color=GREEN)))
        self.wait(1.5)
        m10 = Tex(r"Arms too short? Extend them").scale(0.95).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m10))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): Reflex angles
        self.next_band(2)
        t2 = Tex(r"Reflex angles").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m11 = MathTex(r"360^\circ - 60^\circ = 300^\circ").scale(1.0).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m11))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m11, color=GREEN)))
        self.wait(1.5)
        m12 = MathTex(r"180^\circ + 120^\circ = 300^\circ").scale(1.0).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m12))
        self.wait(2)
        m13 = Tex(r"Two methods, one check").scale(0.95).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m13))
        self.wait(2)
        m14 = Tex(r"Big arc on the outside = reflex").scale(0.95).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m14))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): Angles on a clock
        self.next_band(3)
        t3 = Tex(r"Angles on a clock").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m15 = MathTex(r"360^\circ \div 12 = 30^\circ").scale(1.0).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m15))
        self.wait(2)
        m16 = MathTex(r"2 \to 60^\circ \text{ acute} \quad 3 \to 90^\circ \text{ right}").scale(1.0).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m16))
        self.wait(2)
        m17 = MathTex(r"5 \to 150^\circ \text{ obtuse} \quad 6 \to 180^\circ \text{ straight}").scale(1.0).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"\text{Long way at 2: } 300^\circ \text{ reflex}").scale(1.0).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m18))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m18, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 4 (subtopic_5): Measuring like a pro
        self.next_band(4)
        t4 = Tex(r"Measuring like a pro").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m19 = Tex(r"Centre on the corner").scale(0.95).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m19))
        self.wait(2)
        m20 = Tex(r"Flat edge along one arm, at 0").scale(0.95).shift(band_shift(4) + UP * 0.18)
        self.play(Write(m20))
        self.wait(2)
        m21 = Tex(r"Read the row that starts at 0").scale(0.95).shift(band_shift(4) + DOWN * 0.85)
        self.play(Write(m21))
        self.wait(2)
        m22 = MathTex(r"\text{Looks small? Must be } < 90^\circ").scale(1.0).shift(band_shift(4) + DOWN * 1.87)
        self.play(Write(m22))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m22, color=GREEN)))
        self.wait(1.5)
        m23 = MathTex(r"\text{Reflex: } 360^\circ - \text{inside angle}").scale(1.0).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m23))
        self.wait(2)
        self.wait(3)
