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
# dwell time proportional to subtopics.json (240/180/220/230/210/210/210 of
# 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RatioRateSharingSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Ratio, Rate and Sharing
        t0 = Tex(r"Ratio, Rate and Sharing").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"12 : 18 = 2 : 3 \quad (\div 6)").scale(1.1).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = Tex(r"Same kind, same units, order matters").scale(1.05).shift(UP * 0.18)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"50 \text{ cm} : 2 \text{ m} = 50 : 200 = 1 : 4").scale(1.1).shift(DOWN * 0.85)
        self.play(Write(m3))
        self.wait(2)
        m4 = MathTex(r"2 : 3 \;\Rightarrow\; \text{boys } \tfrac{2}{5}, \; \text{girls } \tfrac{3}{5}").scale(1.1).shift(DOWN * 1.87)
        self.play(Write(m4))
        self.wait(2)
        m5 = Tex(r"Part : part is a ratio; part of whole is a fraction").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(m5))
        self.wait(2)
        self.wait(3)

        # --- Band 1 (subtopic_2): Share R1 800 in the ratio $4 : 5$
        self.next_band(1)
        t1 = Tex(r"Share R1 800 in the ratio $4 : 5$").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m6 = MathTex(r"\text{parts: } 4 + 5 = 9").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"\text{one part: } 1\,800 \div 9 = 200").scale(1.1).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m7))
        self.wait(2)
        m8 = MathTex(r"4 \times 200 = 800 \qquad 5 \times 200 = 1\,000").scale(1.1).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m8))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m8, color=GREEN)))
        self.wait(1.5)
        m9 = MathTex(r"\text{check: } 800 + 1\,000 = 1\,800").scale(1.1).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m9))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_2): Three parts, and a difference
        self.next_band(2)
        t2 = Tex(r"Three parts, and a difference").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m10 = MathTex(r"60 \text{ in } 1 : 2 : 3 \;\to\; 6 \text{ parts}, \; 60 \div 6 = 10").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"\text{shares } 10, \; 20, \; 30").scale(1.1).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"Given the DIFFERENCE instead? $5 - 4 = 1$ part").scale(1.05).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m12))
        self.wait(2)
        m13 = MathTex(r"1 \text{ part} = 200 \;\Rightarrow\; 800 \text{ and } 1\,000").scale(1.1).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(m13))
        self.wait(2)
        self.wait(3)

        # --- Band 3 (subtopic_3): Increase or decrease in a ratio
        self.next_band(3)
        t3 = Tex(r"Increase or decrease in a ratio").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m14 = MathTex(r"\text{increase } 240 \text{ in } 5 : 3 \;\to\; 240 \times \tfrac{5}{3} = 400").scale(1.1).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"\text{decrease } 240 \text{ in } 3 : 5 \;\to\; 240 \times \tfrac{3}{5} = 144").scale(1.1).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m15))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m15, color=GREEN)))
        self.wait(1.5)
        m16 = Tex(r"Increase: fraction $> 1$. Decrease: fraction $< 1$.").scale(1.05).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m16))
        self.wait(2)
        m17 = MathTex(r"150 \to 180: \quad 180 : 150 = 6 : 5").scale(1.1).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m17))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_4): Rate: different kinds, units kept
        self.next_band(4)
        t4 = Tex(r"Rate: different kinds, units kept").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m18 = MathTex(r"240 \text{ km in } 3 \text{ h}: \quad 240 \div 3 = 80 \text{ km/h}").scale(1.1).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"\text{A: } 21 \div 6 = 3{,}50 \text{ per egg} \qquad \text{B: } 54 \div 18 = 3 \text{ per egg}").scale(1.1).shift(band_shift(4) + UP * 0.18)
        self.play(Write(m19))
        self.wait(2)
        m20 = Tex(r"Better buy: compare UNIT rates").scale(1.05).shift(band_shift(4) + DOWN * 0.85)
        self.play(Write(m20))
        self.wait(2)
        m21 = MathTex(r"80 \text{ km/h} \times 5 \text{ h} = 400 \text{ km}").scale(1.1).shift(band_shift(4) + DOWN * 1.87)
        self.play(Write(m21))
        self.wait(2)
        m22 = Tex(r"Ratio: no units. Rate: units attached.").scale(1.05).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m22))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Splitting R1 800 on the kitchen table
        self.next_band(5)
        t5 = Tex(r"Splitting R1 800 on the kitchen table").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        m23 = Tex(r"Stacks: $4 + 5 = 9$").scale(1.05).shift(band_shift(5) + UP * 1.2)
        self.play(Write(m23))
        self.wait(2)
        m24 = MathTex(r"\text{one stack: } 1\,800 \div 9 = 200").scale(1.1).shift(band_shift(5) + DOWN * 0.17)
        self.play(Write(m24))
        self.wait(2)
        m25 = MathTex(r"4 \text{ stacks} = 800 \qquad 5 \text{ stacks} = 1\,000").scale(1.1).shift(band_shift(5) + DOWN * 1.53)
        self.play(Write(m25))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m25, color=GREEN)))
        self.wait(1.5)
        m26 = Tex(r"Divide by the STACKS, never by the PEOPLE").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(m26))
        self.wait(2)
        self.wait(3)

        # --- Band 6 (subtopic_6): Scaling a recipe up and down
        self.next_band(6)
        t6 = Tex(r"Scaling a recipe up and down").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(t6))
        self.wait(1.5)
        m27 = MathTex(r"240 \text{ g for } 3 \;\to\; 80 \text{ g each} \;\to\; 5 \times 80 = 400 \text{ g}").scale(1.1).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m27))
        self.wait(2)
        m28 = MathTex(r"240 \text{ g for } 5 \;\to\; 48 \text{ g each} \;\to\; 3 \times 48 = 144 \text{ g}").scale(1.1).shift(band_shift(6) + UP * 0.18)
        self.play(Write(m28))
        self.wait(2)
        m29 = Tex(r"New on top, old underneath: $\tfrac{5}{3}$ or $\tfrac{3}{5}$").scale(1.05).shift(band_shift(6) + DOWN * 0.85)
        self.play(Write(m29))
        self.wait(2)
        m30 = Tex(r"More $\Rightarrow$ fraction $> 1$; less $\Rightarrow$ fraction $< 1$").scale(1.05).shift(band_shift(6) + DOWN * 1.87)
        self.play(Write(m30))
        self.wait(2)
        m31 = MathTex(r"15 \to 18: \quad 18 : 15 = 6 : 5").scale(1.1).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m31))
        self.wait(2)
        self.wait(3)

        # --- Band 7 (subtopic_7): Taxi fares and the better buy
        self.next_band(7)
        t7 = Tex(r"Taxi fares and the better buy").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(t7))
        self.wait(1.5)
        m32 = MathTex(r"240 \text{ km} \div 3 \text{ h} = 80 \text{ km per hour}").scale(1.1).shift(band_shift(7) + UP * 1.2)
        self.play(Write(m32))
        self.wait(2)
        m33 = MathTex(r"\text{A: } 21 \div 6 = 3{,}50 \qquad \text{B: } 54 \div 18 = 3").scale(1.1).shift(band_shift(7) + UP * 0.18)
        self.play(Write(m33))
        self.wait(2)
        m34 = Tex(r"Better buy: the rate for ONE").scale(1.05).shift(band_shift(7) + DOWN * 0.85)
        self.play(Write(m34))
        self.wait(2)
        m35 = MathTex(r"80 \times 5 = 400 \text{ km} \qquad 9 \times 30 = 270 \text{ rand}").scale(1.1).shift(band_shift(7) + DOWN * 1.87)
        self.play(Write(m35))
        self.wait(2)
        m36 = Tex(r"Ratios lose units; rates keep them").scale(1.05).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(m36))
        self.wait(2)
        self.wait(3)
