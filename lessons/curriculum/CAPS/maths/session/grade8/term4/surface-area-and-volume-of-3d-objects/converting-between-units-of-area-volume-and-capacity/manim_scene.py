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
# dwell time proportional to subtopics.json (300/200/210/230/260/240/210 of
# 1650 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ConvertingVolumeCapacitySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Why Volume Factors Are Cubed
        t0 = Tex(r"Why Volume Factors Are Cubed").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"1 \text{ cm}^3 = 10 \times 10 \times 10 = 1\,000 \text{ mm}^3").scale(1.1).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"1 \text{ m}^3 = 100 \times 100 \times 100 = 1\,000\,000 \text{ cm}^3").scale(1.1).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = Tex(r"Length 10, area 100, volume 1 000; length 100, area 10 000, volume 1 000 000").scale(1.05).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Square for area, cube for volume").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 1 (subtopic_2): Converting Cubic Units
        self.next_band(1)
        t1 = Tex(r"Converting Cubic Units").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"2{,}5 \times 1\,000 = 2\,500 \text{ mm}^3 \qquad 4\,500 \div 1\,000 = 4{,}5 \text{ cm}^3").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"0{,}75 \times 1\,000\,000 = 750\,000 \text{ cm}^3").scale(1.1).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"0{,}2 \times 0{,}1 \times 0{,}05 = 0{,}001 \text{ m}^3").scale(1.1).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = Tex(r"Smaller unit: multiply. Larger unit: divide. 3 or 6 places.").scale(1.05).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m8))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m8, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 2 (subtopic_3): Capacity and the Bridge
        self.next_band(2)
        t2 = Tex(r"Capacity and the Bridge").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"1 \text{ ml} = 1 \text{ cm}^3 \qquad 1 \text{ l} = 1\,000 \text{ cm}^3 \qquad 1 \text{ kl} = 1 \text{ m}^3").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"3\,200 \text{ cm}^3 = 3\,200 \text{ ml} = 3{,}2 \text{ l}").scale(1.1).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"2{,}4 \text{ m}^3 = 2{,}4 \text{ kl} = 2\,400 \text{ l}").scale(1.1).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"Cubic metre to litres: times 1 000, not 1 000 000").scale(1.05).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(m12))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m12, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 3 (subtopic_4): Mixed Conversions
        self.next_band(3)
        t3 = Tex(r"Mixed Conversions").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"60 \times 30 \times 40 = 72\,000 \text{ cm}^3 = 72 \text{ l} = 0{,}072 \text{ m}^3").scale(1.1).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"2\,000 \div 250 = 8 \qquad 100 \div 5 = 20").scale(1.1).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"60 \text{ m}^3 = 60\,000 \text{ l} \qquad 60\,000 \div 40 = 1\,500 \text{ min}").scale(1.1).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        m16 = Tex(r"Pick one unit system; cross the bridge once").scale(1.05).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m16))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m16, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): The Water Bill
        self.next_band(4)
        t4 = Tex(r"The Water Bill").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = MathTex(r"1\,302 - 1\,284 = 18 \text{ kl} = 18\,000 \text{ l}").scale(1.1).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"18\,000 \div 30 = 600 \text{ l per day} \qquad 600 \div 25 = 24 \text{ buckets}").scale(1.1).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"20 \times 9 = 180 \text{ l} = 0{,}18 \text{ kl}").scale(1.1).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        m20 = Tex(r"Kilolitres on the bill; litres and buckets in the house").scale(1.05).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m20))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m20, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 5 (subtopic_6): Syringe and Dam
        self.next_band(5)
        t5 = Tex(r"Syringe and Dam").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        m21 = MathTex(r"7{,}5 \text{ ml} = 7{,}5 \text{ cm}^3 \qquad 7{,}5 \times 2 \times 7 = 105 \text{ ml}").scale(1.1).shift(band_shift(5) + UP * 1.2)
        self.play(Write(m21))
        self.wait(2)
        m22 = MathTex(r"40 \times 25 \times 3 = 3\,000 \text{ m}^3 = 3\,000 \text{ kl} = 3\,000\,000 \text{ l}").scale(1.1).shift(band_shift(5) + DOWN * 0.17)
        self.play(Write(m22))
        self.wait(2)
        m23 = MathTex(r"1\,000 \times 0{,}008 = 8 \text{ m}^3 = 8\,000 \text{ l}").scale(1.1).shift(band_shift(5) + DOWN * 1.53)
        self.play(Write(m23))
        self.wait(2)
        m24 = Tex(r"From a syringe to a dam: the same chain of units").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(m24))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m24, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 6 (subtopic_7): Examination Technique
        self.next_band(6)
        t6 = Tex(r"Examination Technique").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(t6))
        self.wait(1.5)
        m25 = MathTex(r"0{,}75 \text{ m}^3 = 0{,}75 \text{ kl} = 750 \text{ l} \qquad 5\,400 \div 1\,000 = 5{,}4 \text{ cm}^3").scale(1.1).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m25))
        self.wait(2)
        m26 = MathTex(r"25 \times 20 \times 12 = 6\,000 \text{ cm}^3 = 6 \text{ l}").scale(1.1).shift(band_shift(6) + DOWN * 0.17)
        self.play(Write(m26))
        self.wait(2)
        m27 = MathTex(r"1\,200 \div 20 = 60 \text{ buckets}").scale(1.1).shift(band_shift(6) + DOWN * 1.53)
        self.play(Write(m27))
        self.wait(2)
        m28 = Tex(r"Length k, area k squared, volume k cubed; cm cubed is ml, m cubed is kl").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m28))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m28, color=GREEN)))
        self.wait(1.5)
        self.wait(3)
