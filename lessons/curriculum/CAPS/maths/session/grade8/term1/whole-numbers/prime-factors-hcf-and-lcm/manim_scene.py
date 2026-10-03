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
# dwell time proportional to subtopics.json (240/200/210/260/220/230/230 of
# 1590 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PrimeFactorsHcfLcmSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Prime Factors, HCF and LCM
        t0 = Tex(r"Prime Factors, HCF and LCM").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"180 = 2 \times 2 \times 3 \times 3 \times 5 = 2^2 \times 3^2 \times 5").scale(1.1).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"300 = 2 \times 2 \times 3 \times 5 \times 5 = 2^2 \times 3 \times 5^2").scale(1.1).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m2, color=GREEN)))
        self.wait(1.5)
        m3 = Tex(r"Ladder: smallest prime that divides, repeat to 1").scale(1.05).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Check: multiply back").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(m4))
        self.wait(2)
        self.wait(3)

        # --- Band 1 (subtopic_2): HCF: shared primes, LOWER powers
        self.next_band(1)
        t1 = Tex(r"HCF: shared primes, LOWER powers").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"180 = 2^2 \times 3^2 \times 5 \qquad 300 = 2^2 \times 3 \times 5^2").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"\text{HCF} = 2^2 \times 3 \times 5 = 60").scale(1.1).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m6, color=GREEN)))
        self.wait(1.5)
        m7 = MathTex(r"180 \div 60 = 3 \qquad 300 \div 60 = 5").scale(1.1).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = Tex(r"Largest thing that goes INTO both").scale(1.05).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m8))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): LCM: every prime, HIGHER powers
        self.next_band(2)
        t2 = Tex(r"LCM: every prime, HIGHER powers").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"180 = 2^2 \times 3^2 \times 5 \qquad 300 = 2^2 \times 3 \times 5^2").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"\text{LCM} = 2^2 \times 3^2 \times 5^2 = 900").scale(1.1).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m10, color=GREEN)))
        self.wait(1.5)
        m11 = MathTex(r"\text{HCF} \times \text{LCM} = 60 \times 900 = 54\,000 = 180 \times 300").scale(1.1).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"Smallest thing both go INTO").scale(1.05).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(m12))
        self.wait(2)
        self.wait(3)

        # --- Band 3 (subtopic_3): Taxis: 18 and 24 minutes
        self.next_band(3)
        t3 = Tex(r"Taxis: 18 and 24 minutes").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"18 = 2 \times 3^2 \qquad 24 = 2^3 \times 3").scale(1.1).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"\text{LCM} = 2^3 \times 3^2 = 72 \text{ min}").scale(1.1).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m14, color=GREEN)))
        self.wait(1.5)
        m15 = MathTex(r"\text{HCF} = 2 \times 3 = 6").scale(1.1).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        m16 = Tex(r"Together again after 72 minutes").scale(1.05).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m16))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_4): HCF or LCM? Read the question
        self.next_band(4)
        t4 = Tex(r"HCF or LCM? Read the question").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = Tex(r"Largest size that goes INTO both $\to$ HCF").scale(1.05).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m17))
        self.wait(2)
        m18 = Tex(r"Smallest size both go INTO $\to$ LCM").scale(1.05).shift(band_shift(4) + UP * 0.18)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"\text{groups of } 60: \; 180 \div 60 + 300 \div 60 = 3 + 5 = 8").scale(1.1).shift(band_shift(4) + DOWN * 0.85)
        self.play(Write(m19))
        self.wait(2)
        m20 = MathTex(r"\text{post meets light at LCM} = 900 \text{ cm} = 9 \text{ m}").scale(1.1).shift(band_shift(4) + DOWN * 1.87)
        self.play(Write(m20))
        self.wait(2)
        m21 = Tex(r"Sanity: HCF $\le$ smaller number, LCM $\ge$ larger number").scale(1.05).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m21))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Breaking a number into bricks
        self.next_band(5)
        t5 = Tex(r"Breaking a number into bricks").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        m22 = MathTex(r"180 \to 90 \to 45 \to 15 \to 5 \to 1 \quad \text{bricks } 2, 2, 3, 3, 5").scale(1.1).shift(band_shift(5) + UP * 1.2)
        self.play(Write(m22))
        self.wait(2)
        m23 = MathTex(r"300 \to 150 \to 75 \to 25 \to 5 \to 1 \quad \text{bricks } 2, 2, 3, 5, 5").scale(1.1).shift(band_shift(5) + UP * 0.18)
        self.play(Write(m23))
        self.wait(2)
        m24 = Tex(r"Both share: two 2s, one 3, one 5").scale(1.05).shift(band_shift(5) + DOWN * 0.85)
        self.play(Write(m24))
        self.wait(2)
        m25 = Tex(r"180 has a spare 3; 300 has a spare 5").scale(1.05).shift(band_shift(5) + DOWN * 1.87)
        self.play(Write(m25))
        self.wait(2)
        m26 = MathTex(r"\text{Rebuild: } 2 \times 2 \times 3 \times 5 \times 5 = 300").scale(1.1).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(m26))
        self.wait(2)
        self.wait(3)

        # --- Band 6 (subtopic_6): The biggest tile: what the piles share
        self.next_band(6)
        t6 = Tex(r"The biggest tile: what the piles share").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(t6))
        self.wait(1.5)
        m27 = Tex(r"Floor $180 \times 300$ cm; square tiles, no cutting").scale(1.05).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m27))
        self.wait(2)
        m28 = MathTex(r"\text{shared bricks: } 2 \times 2 \times 3 \times 5 = 60 \text{ cm}").scale(1.1).shift(band_shift(6) + DOWN * 0.17)
        self.play(Write(m28))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m28, color=GREEN)))
        self.wait(1.5)
        m29 = MathTex(r"180 \div 60 = 3, \quad 300 \div 60 = 5 \quad \text{tiles: } 15").scale(1.1).shift(band_shift(6) + DOWN * 1.53)
        self.play(Write(m29))
        self.wait(2)
        m30 = Tex(r"HCF $\le$ smaller number, always").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m30))
        self.wait(2)
        self.wait(3)

        # --- Band 7 (subtopic_7): When the taxis meet again: what the piles need
        self.next_band(7)
        t7 = Tex(r"When the taxis meet again: what the piles need").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(t7))
        self.wait(1.5)
        m31 = MathTex(r"18: 18, 36, 54, 72 \qquad 24: 24, 48, 72").scale(1.1).shift(band_shift(7) + UP * 1.2)
        self.play(Write(m31))
        self.wait(2)
        m32 = MathTex(r"18 = 2 \times 3 \times 3, \quad 24 = 2 \times 2 \times 2 \times 3 \quad \to \quad 2^3 \times 3^2 = 72").scale(1.1).shift(band_shift(7) + DOWN * 0.17)
        self.play(Write(m32))
        self.wait(2)
        m33 = MathTex(r"\text{LCM}(180, 300) = 2^2 \times 3^2 \times 5^2 = 900").scale(1.1).shift(band_shift(7) + DOWN * 1.53)
        self.play(Write(m33))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m33, color=GREEN)))
        self.wait(1.5)
        m34 = Tex(r"Tile = share, smaller count. Taxis = need, bigger count.").scale(1.05).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(m34))
        self.wait(2)
        self.wait(3)
