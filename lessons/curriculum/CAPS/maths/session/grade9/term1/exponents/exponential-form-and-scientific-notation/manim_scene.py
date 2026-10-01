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
# dwell time proportional to subtopics.json (220/230/230/230/190/190/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ScientificNotationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): exponential form
        title = Tex("Exponential Form").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"2^5 = 2 \times 2 \times 2 \times 2 \times 2 = 32 \quad (\text{not } 2 \times 5)").scale(1.0).shift(UP * 1.3)
        l2 = MathTex(r"72 = 2^3 \times 3^2 \qquad 10^6 = 1\,000\,000").scale(1.0).shift(UP * 0.3)
        l3 = MathTex(r"(-2)^4 = 16 \qquad -2^4 = -16 \qquad (-2)^3 = -8").scale(1.05).shift(DOWN * 0.7)
        l4 = MathTex(r"a^0 = 1 \quad (a \neq 0)").scale(1.0).shift(DOWN * 1.7)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): large numbers
        self.next_band(1)
        b1_title = Tex(r"Scientific notation: $a \times 10^n$, $1 \le a < 10$").scale(1.1).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"149\,600\,000 = 1{,}496 \times 10^{8}").scale(1.15).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"62\,000\,000 = 6{,}2 \times 10^{7} \qquad 384\,400 = 3{,}844 \times 10^{5}").scale(0.95).shift(band_shift(1) + UP * 0.3)
        b1_l3 = MathTex(r"45 \times 10^{6} \;\to\; 4{,}5 \times 10^{7}").scale(1.05).shift(band_shift(1) + DOWN * 0.6)
        b1_l4 = Tex(r"Calculator 1.496E8 means $1{,}496 \times 10^{8}$").scale(0.95).shift(band_shift(1) + DOWN * 1.6)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): negative exponents
        self.next_band(2)
        b2_title = Tex("Negative exponents: small, not negative").scale(1.1).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"10^3 = 1\,000,\; 10^2 = 100,\; 10^1 = 10,\; 10^0 = 1").scale(0.95).shift(band_shift(2) + UP * 1.3)
        b2_l2 = MathTex(r"10^{-1} = 0{,}1,\; 10^{-2} = 0{,}01,\; 10^{-3} = 0{,}001").scale(0.95).shift(band_shift(2) + UP * 0.4)
        b2_l3 = MathTex(r"0{,}0000075 = 7{,}5 \times 10^{-6} \qquad 0{,}00052 = 5{,}2 \times 10^{-4}").scale(0.95).shift(band_shift(2) + DOWN * 0.6)
        b2_l4 = MathTex(r"0{,}5 \times 10^{-3} \;\to\; 5 \times 10^{-4}").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): compare, order, round
        self.next_band(3)
        b3_title = Tex("Compare exponents first; round $a$ only").scale(1.1).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"3{,}2 \times 10^{5} > 9{,}8 \times 10^{4} \quad (320\,000 > 98\,000)").scale(0.95).shift(band_shift(3) + UP * 1.3)
        b3_l2 = MathTex(r"2 \times 10^{-3} > 9 \times 10^{-6}").scale(1.0).shift(band_shift(3) + UP * 0.4)
        b3_l3 = MathTex(r"1{,}496 \times 10^{8} \approx 1{,}5 \times 10^{8} \qquad 9{,}97 \times 10^{4} \approx 1{,}0 \times 10^{5}").scale(0.9).shift(band_shift(3) + DOWN * 0.6)
        for m in (b3_l1, b3_l2, b3_l3):
            self.play(Write(m))
            self.wait(2.4)
        self.wait(1.5)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"12 \times 10^{3} \;\text{as standard form}").scale(1.0).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"10^{-4} = -10\,000").scale(1.0).shift(band_shift(4) + UP * 0.4)
        b4_l3 = MathTex(r"1.496\text{E}8 \;\text{copied as}\; 1{,}496^{8}").scale(1.0).shift(band_shift(4) + DOWN * 0.5)
        b4_l4 = Tex("Counting the comma shift from the wrong end").scale(0.95).shift(band_shift(4) + DOWN * 1.4)
        for m in (b4_l1, b4_l2, b4_l3):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.play(Write(b4_l4))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): the forwarding chain
        self.next_band(5)
        b5_title = Tex("Forwarding chain: the exponent counts rounds").scale(1.05).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"2,\; 4,\; 8,\; 16,\; 32 \;\Rightarrow\; 2^5 = 32").scale(1.05).shift(band_shift(5) + UP * 1.3)
        b5_l2 = MathTex(r"2^{10} = 1\,024").scale(1.05).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex(r"Bracket: minus is in the base, $(-2)^4 = 16$").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex(r"No bracket: minus waits outside, $-2^4 = -16$").scale(0.95).shift(band_shift(5) + DOWN * 1.4)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): the walking comma
        self.next_band(6)
        b6_title = Tex("The comma takes a walk").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"149 600 000: comma walks 8 left $\to 1{,}496 \times 10^{8}$").scale(0.95).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex(r"0,0000075: comma walks 6 right $\to 7{,}5 \times 10^{-6}$").scale(0.95).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("Left walk: positive exponent. Right walk: negative exponent.").scale(0.9).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex(r"One digit in front: $45 \times 10^6 \to 4{,}5 \times 10^7$").scale(0.95).shift(band_shift(6) + DOWN * 1.5)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): the real world
        self.next_band(7)
        b7_title = Tex("Big and small numbers in the real world").scale(1.1).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        rows = [
            r"\text{64 GB} = 6{,}4 \times 10^{10} \text{ bytes}",
            r"\text{Light year} \approx 9{,}46 \times 10^{12} \text{ km}",
            r"\text{Earth} \approx 5{,}97 \times 10^{24} \text{ kg}",
            r"\text{Electron} \approx 9{,}11 \times 10^{-31} \text{ kg}",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.95).shift(band_shift(7) + UP * (1.3 - 0.8 * i))
            self.play(Write(m))
            self.wait(2)
        b7_l5 = Tex("Exponent first, then $a$; round $a$ only; E means times ten to the").scale(0.85).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=YELLOW)))
        self.wait(4)
