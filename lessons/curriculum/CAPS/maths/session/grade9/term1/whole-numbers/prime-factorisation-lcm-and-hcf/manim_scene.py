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
# dwell time proportional to subtopics.json (210/210/240/260/180/180/190 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PrimeFactorisationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the ladder for 360
        title = Tex("Prime Factorisation, HCF and LCM").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l0 = Tex(r"Primes: $2,\,3,\,5,\,7,\,11,\,13,\,\ldots$ (1 is not prime)").scale(1.05).shift(UP * 1.3)
        self.play(Write(l0))
        self.wait(2)
        ladder = [r"2 \mid 360", r"2 \mid 180", r"2 \mid 90", r"3 \mid 45", r"3 \mid 15", r"5 \mid 5 \to 1"]
        for i, s in enumerate(ladder):
            m = MathTex(s).scale(1.05).shift(LEFT * 3.5 + UP * (0.5 - 0.6 * i))
            self.play(Write(m), run_time=0.7)
            self.wait(0.8)
        res = MathTex(r"360 = 2^3 \times 3^2 \times 5").scale(1.2).shift(RIGHT * 2.5 + DOWN * 0.6)
        self.play(Write(res))
        self.play(Create(SurroundingRectangle(res, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the ladder for 84 and the index form
        self.next_band(1)
        b1_title = Tex("Now 84").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        ladder2 = [r"2 \mid 84", r"2 \mid 42", r"3 \mid 21", r"7 \mid 7 \to 1"]
        for i, s in enumerate(ladder2):
            m = MathTex(s).scale(1.05).shift(band_shift(1) + LEFT * 3.5 + UP * (1.3 - 0.6 * i))
            self.play(Write(m), run_time=0.7)
            self.wait(0.8)
        b1_res = MathTex(r"84 = 2^2 \times 3 \times 7").scale(1.2).shift(band_shift(1) + RIGHT * 2.5 + UP * 0.5)
        self.play(Write(b1_res))
        self.play(Create(SurroundingRectangle(b1_res, color=GREEN)))
        self.wait(2)
        b1_note = Tex("Index form, primes ascending; never stop at 6, 9 or 12").scale(1.0).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_note))
        self.wait(3)

        # --- Band 2 (subtopic_2): HCF — common primes, lower powers
        self.next_band(2)
        b2_title = Tex("HCF: common primes, LOWER power").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"360 = 2^3 \times 3^2 \times 5").scale(1.1).shift(band_shift(2) + UP * 1.3)
        b2_l2 = MathTex(r"84 = 2^2 \times 3 \times 7").scale(1.1).shift(band_shift(2) + UP * 0.5)
        b2_l3 = MathTex(r"\text{HCF} = 2^2 \times 3 = 12").scale(1.2).shift(band_shift(2) + DOWN * 0.5)
        b2_l4 = MathTex(r"360 \div 12 = 30 \qquad 84 \div 12 = 7").scale(1.05).shift(band_shift(2) + DOWN * 1.5)
        b2_l5 = Tex(r"HCF$(48, 72) = 2^3 \times 3 = 24$").scale(1.05).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l1))
        self.wait(1.5)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        self.play(Write(b2_l5))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): LCM — every prime, higher power
        self.next_band(3)
        b3_title = Tex("LCM: every prime, HIGHER power").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{LCM} = 2^3 \times 3^2 \times 5 \times 7").scale(1.15).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"= 8 \times 9 \times 5 \times 7 = 2\,520").scale(1.15).shift(band_shift(3) + UP * 0.3)
        b3_l3 = MathTex(r"2\,520 \div 360 = 7 \qquad 2\,520 \div 84 = 30").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = Tex(r"LCM$(48, 72) = 2^4 \times 3^2 = 144$").scale(1.05).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): HCF x LCM = product
        self.next_band(4)
        b4_title = Tex(r"Check: HCF $\times$ LCM $=$ product").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"12 \times 2\,520 = 30\,240 = 360 \times 84").scale(1.1).shift(band_shift(4) + UP * 1.2)
        b4_l2 = MathTex(r"24 \times 144 = 3\,456 = 48 \times 72").scale(1.1).shift(band_shift(4) + UP * 0.3)
        b4_l3 = Tex("Lower powers go to the HCF, higher powers to the LCM").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = Tex(r"HCF $\le$ smaller number; LCM $\ge$ larger number").scale(1.0).shift(band_shift(4) + DOWN * 1.6)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.wait(2.2)
        self.play(Create(SurroundingRectangle(b4_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 5 (subtopic_4): which one does the question want?
        self.next_band(5)
        b5_title = Tex("HCF or LCM?").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Split into biggest equal pieces / packs $\\to$ HCF").scale(1.0).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex("Repeating events coincide / first meeting $\\to$ LCM").scale(1.0).shift(band_shift(5) + UP * 0.4)
        b5_l3 = MathTex(r"\text{Taxis 12, 18 min: LCM} = 2^2 \times 3^2 = 36 \to 6{:}36").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = MathTex(r"\text{Tiles: HCF} = 12\text{ cm}, \; 30 \times 7 = 210 \text{ tiles}").scale(1.0).shift(band_shift(5) + DOWN * 1.4)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(2)

        # --- Band 6 (subtopic_4): three numbers and roots
        self.next_band(6)
        b6_title = Tex("Three numbers, and roots from exponents").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"12 = 2^2 \times 3,\; 18 = 2 \times 3^2,\; 30 = 2 \times 3 \times 5").scale(1.0).shift(band_shift(6) + UP * 1.3)
        b6_l2 = MathTex(r"\text{HCF} = 2 \times 3 = 6 \qquad \text{LCM} = 2^2 \times 3^2 \times 5 = 180").scale(1.0).shift(band_shift(6) + UP * 0.4)
        b6_l3 = MathTex(r"\sqrt{900} = \sqrt{2^2 \times 3^2 \times 5^2} = 2 \times 3 \times 5 = 30").scale(1.0).shift(band_shift(6) + DOWN * 0.6)
        b6_l4 = MathTex(r"\sqrt[3]{216} = \sqrt[3]{2^3 \times 3^3} = 2 \times 3 = 6").scale(1.0).shift(band_shift(6) + DOWN * 1.5)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): Lego bricks
        self.next_band(7)
        b7_title = Tex("Breaking a number into its Lego bricks").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"360: halve, halve, halve $\to$ 45; then 3, 3; then 5").scale(1.0).shift(band_shift(7) + UP * 1.3)
        b7_l2 = Tex(r"Bricks: $2,\,2,\,2,\,3,\,3,\,5$").scale(1.1).shift(band_shift(7) + UP * 0.4)
        b7_l3 = Tex(r"84: halve, halve $\to$ 21; then 3; then 7").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex(r"Bricks: $2,\,2,\,3,\,7$").scale(1.1).shift(band_shift(7) + DOWN * 1.4)
        b7_l5 = Tex("Smallest brick first; never leave a 6, 9 or 15 in the row").scale(0.95).shift(band_shift(7) + DOWN * 2.3)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4, b7_l5):
            self.play(Write(m))
            self.wait(2)
        self.wait(1.5)

        # --- Band 8 (subtopic_6): shared bricks and the biggest pack
        self.next_band(8)
        b8_title = Tex("Shared bricks and the biggest pack").scale(1.15).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        r360 = Tex(r"360: $\mathbf{2},\,\mathbf{2},\,2,\,\mathbf{3},\,3,\,5$").scale(1.1).shift(band_shift(8) + UP * 1.3)
        r84 = Tex(r"84: $\mathbf{2},\,\mathbf{2},\,\mathbf{3},\,7$").scale(1.1).shift(band_shift(8) + UP * 0.4)
        self.play(Write(r360))
        self.wait(1.5)
        self.play(Write(r84))
        self.wait(2)
        b8_l3 = MathTex(r"\text{Shared: } 2 \times 2 \times 3 = 12 \text{ packs}").scale(1.1).shift(band_shift(8) + DOWN * 0.6)
        b8_l4 = Tex(r"Each pack: $360 \div 12 = 30$ sweets, $84 \div 12 = 7$ chips").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        b8_l5 = Tex("Leftovers 30 and 7 share nothing — 12 was the biggest").scale(0.95).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(2)
        self.play(Write(b8_l5))
        self.wait(2.5)

        # --- Band 9 (subtopic_7): when do the taxis meet again?
        self.next_band(9)
        b9_title = Tex("When do the taxis meet again?").scale(1.15).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Taxi A: 12, 24, $\mathbf{36}$, 48 \quad Taxi B: 18, $\mathbf{36}$, 54").scale(1.0).shift(band_shift(9) + UP * 1.3)
        b9_l2 = Tex(r"All of 360's bricks + 84's missing brick (7)").scale(1.0).shift(band_shift(9) + UP * 0.4)
        b9_l3 = MathTex(r"2 \times 2 \times 2 \times 3 \times 3 \times 5 \times 7 = 2\,520").scale(1.05).shift(band_shift(9) + DOWN * 0.5)
        b9_l4 = MathTex(r"12 \times 2\,520 = 30\,240 = 360 \times 84 \;\checkmark").scale(1.05).shift(band_shift(9) + DOWN * 1.4)
        b9_l5 = Tex("Shared bricks to split; combined bricks to meet").scale(1.0).shift(band_shift(9) + DOWN * 2.3)
        for m in (b9_l1, b9_l2, b9_l3, b9_l4):
            self.play(Write(m))
            self.wait(2.2)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=YELLOW)))
        self.wait(4)
