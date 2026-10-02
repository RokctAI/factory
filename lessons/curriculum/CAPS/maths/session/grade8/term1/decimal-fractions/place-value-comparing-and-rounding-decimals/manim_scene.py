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
# dwell time proportional to subtopics.json (240/200/190/210/210/200/230 of
# 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DecimalPlaceValueSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Decimals: Place Value, Order, Rounding
        t0 = Tex(r"Decimals: Place Value, Order, Rounding").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"3{,}407 = 3 + \frac{4}{10} + \frac{0}{100} + \frac{7}{1000}").scale(1.1).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex(r"tenths, hundredths, thousandths").scale(1.05).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"0{,}4 = 0{,}40 \qquad 0{,}4 \neq 0{,}04").scale(1.1).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"A digit's value depends on its position, not its size").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 1 (subtopic_2): Comparing Decimals
        self.next_band(1)
        t1 = Tex(r"Comparing Decimals").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"0{,}8 = 0{,}80 > 0{,}75").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"2{,}035 < 2{,}305 < 2{,}35 < 2{,}53").scale(1.1).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = Tex(r"Pad to equal places, then read left to right").scale(1.05).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = Tex(r"A longer decimal is not a bigger decimal").scale(1.05).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m8))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m8, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 2 (subtopic_3): Rounding
        self.next_band(2)
        t2 = Tex(r"Rounding").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"3{,}45\underline{6}7 \approx 3{,}46 \qquad 0{,}04\underline{4}9 \approx 0{,}04").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"7{,}99\underline{5} \approx 8{,}00 \quad \text{(keep the zeros)}").scale(1.1).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = Tex(r"Only the digit right after the cut decides").scale(1.05).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"Round at the end, never in the middle").scale(1.05).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(m12))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m12, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 3 (subtopic_4): Number Lines and Technique
        self.next_band(3)
        t3 = Tex(r"Number Lines and Technique").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"0{,}375 = \frac{375}{1000} = \frac{3}{8} \qquad \frac{7}{20} = \frac{35}{100} = 0{,}35").scale(1.1).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m13))
        self.wait(2)
        m14 = Tex(r"Find the two marked values, then the fraction of the gap").scale(1.05).shift(band_shift(3) + DOWN * 0.85)
        self.play(Write(m14))
        self.wait(2)
        m15 = Tex(r"Say the place name, pad, underline the deciding digit").scale(1.05).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m15))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m15, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): Cents and Millilitres
        self.next_band(4)
        t4 = Tex(r"Cents and Millilitres").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m16 = MathTex(r"\text{R}12{,}35: \quad 3 \to 30\text{c}, \quad 5 \to 5\text{c}").scale(1.1).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m16))
        self.wait(2)
        m17 = MathTex(r"42{,}305 \text{ L}: \quad 5 \to 5 \text{ ml}").scale(1.1).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"11{,}08 \text{ s} < 11{,}80 \text{ s}").scale(1.1).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m18))
        self.wait(2)
        m19 = Tex(r"Say the unit of each digit").scale(1.05).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m19))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m19, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 5 (subtopic_6): Race Times
        self.next_band(5)
        t5 = Tex(r"Race Times").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        m20 = MathTex(r"2{,}350 \quad 2{,}305 \quad 2{,}530 \quad 2{,}035").scale(1.1).shift(band_shift(5) + UP * 1.2)
        self.play(Write(m20))
        self.wait(2)
        m21 = MathTex(r"35 < 305 < 350 < 530 \text{ thousandths}").scale(1.1).shift(band_shift(5) + DOWN * 0.17)
        self.play(Write(m21))
        self.wait(2)
        m22 = MathTex(r"2{,}035 < 2{,}305 < 2{,}35 < 2{,}53").scale(1.1).shift(band_shift(5) + DOWN * 1.53)
        self.play(Write(m22))
        self.wait(2)
        m23 = Tex(r"Pad, order as whole numbers, translate back").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(m23))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m23, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 6 (subtopic_7): Rounding at the Till
        self.next_band(6)
        t6 = Tex(r"Rounding at the Till").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(t6))
        self.wait(1.5)
        m24 = MathTex(r"743{,}99\underline{5} \approx 744{,}00").scale(1.1).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m24))
        self.wait(2)
        m25 = MathTex(r"12{,}34\underline{5} \approx 12{,}35 \qquad 0{,}04\underline{4}9 \approx 0{,}04").scale(1.1).shift(band_shift(6) + DOWN * 0.17)
        self.play(Write(m25))
        self.wait(2)
        m26 = Tex(r"Only the next digit decides; carries ripple left").scale(1.05).shift(band_shift(6) + DOWN * 1.53)
        self.play(Write(m26))
        self.wait(2)
        m27 = Tex(r"Say the place, pad, round, keep the zeros").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m27))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m27, color=GREEN)))
        self.wait(1.5)
        self.wait(3)
