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


class ExponentialFormSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Base and exponent
        t0 = Tex(r"Base and exponent").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"2 \times 2 \times 2 \times 2 \times 2 = 2^5").scale(1.0).shift(UP * 1.20)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex(r"Base 2, exponent 5").scale(0.95).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"2^5 = 32 \qquad 3^4 = 81 \qquad 10^3 = 1\,000").scale(1.0).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m3, color=GREEN)))
        self.wait(1.5)
        m4 = Tex(r"$2^5 \neq 2 \times 5$").scale(0.95).shift(DOWN * 2.90)
        self.play(Write(m4))
        self.wait(2)
        self.wait(4)

        # --- Band 1 (subtopic_2): Calculating powers
        self.next_band(1)
        t1 = Tex(r"Calculating powers").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"2^5: \; 2, 4, 8, 16, 32").scale(1.0).shift(band_shift(1) + UP * 1.20)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"3^5: \; 3, 9, 27, 81, 243").scale(1.0).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"10^5 = 100\,000 \qquad 300\,000 = 3 \times 10^5").scale(1.0).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m7, color=GREEN)))
        self.wait(1.5)
        m8 = Tex(r"Day 5 of the message: $2^5$ = 32 new people").scale(0.95).shift(band_shift(1) + DOWN * 2.90)
        self.play(Write(m8))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): Comparing powers
        self.next_band(2)
        t2 = Tex(r"Comparing powers").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"2^5 = 32 > 5^2 = 25").scale(1.0).shift(band_shift(2) + UP * 1.20)
        self.play(Write(m9))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m9, color=GREEN)))
        self.wait(1.5)
        m10 = MathTex(r"3^4 = 81 > 4^3 = 64").scale(1.0).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = Tex(r"Same base: bigger exponent wins. Same exponent: bigger base wins.").scale(0.95).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = MathTex(r"64 = 2^6 = 4^3 = 8^2").scale(1.0).shift(band_shift(2) + DOWN * 2.90)
        self.play(Write(m12))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4): The message that doubles
        self.next_band(3)
        t3 = Tex(r"The message that doubles").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"2, \; 4, \; 8, \; 16, \; 32").scale(1.0).shift(band_shift(3) + UP * 1.20)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"2 \times 2 \times 2 \times 2 \times 2 = 2^5 = 32").scale(1.0).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m14, color=GREEN)))
        self.wait(1.5)
        m15 = Tex(r"Base = what we multiply; exponent = how many times").scale(0.95).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        m16 = MathTex(r"2^{10} = 1\,024").scale(1.0).shift(band_shift(3) + DOWN * 2.90)
        self.play(Write(m16))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_5): Which power is bigger?
        self.next_band(4)
        t4 = Tex(r"Which power is bigger?").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = MathTex(r"2^5 = 32 \qquad 5^2 = 25").scale(1.0).shift(band_shift(4) + UP * 1.20)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"2^5 > 5^2").scale(1.0).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m18, color=GREEN)))
        self.wait(1.5)
        m19 = Tex(r"Work them out, then compare").scale(0.95).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        m20 = MathTex(r"64 = 2^6 = 4^3 = 8^2").scale(1.0).shift(band_shift(4) + DOWN * 2.90)
        self.play(Write(m20))
        self.wait(2)
        self.wait(3)
