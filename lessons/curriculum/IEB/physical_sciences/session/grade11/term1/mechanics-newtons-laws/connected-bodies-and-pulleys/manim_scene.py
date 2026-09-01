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

# Band-layout whiteboard scene for the Connected Bodies and Pulleys duo.
# Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7.
# Band dwell proportional to subtopics.json (215/230/230/265/180/175/185
# of 1480 s). Exporter-safe mobjects only; add-only lifecycle; camera bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ConnectedBodiesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the three assumptions ---
        title = Tex("Connected Bodies and Pulleys").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Inextensible string: ONE acceleration magnitude").scale(0.9).shift(UP * 1.1)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("Light string: SAME tension at both ends").scale(0.9).shift(UP * 0.3)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("Frictionless pulley: direction changes, size does not").scale(0.9).shift(DOWN * 0.5)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(VGroup(b0_l1, b0_l2, b0_l3), color=BLUE)))
        self.wait(2.5)
        b0_l4 = Tex("Strings PULL. They never push").scale(0.95).shift(DOWN * 1.6)
        self.play(Write(b0_l4))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): the two-step method ---
        self.next_band(1)
        b1_title = Tex("The two-step method").scale(1.15).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Step 1: whole system — tensions cancel,").scale(0.95).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"F_{net,\ external} = (m_1 + m_2)a").scale(1.0).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=BLUE)))
        self.wait(2.5)
        b1_l3 = Tex("Step 2: one body alone — tension is the").scale(0.95).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = Tex("only unknown, and it falls out in one line").scale(0.95).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): frictionless trolleys ---
        self.next_band(2)
        b2_title = Tex("6 kg + 4 kg, smooth floor, 40 N pull").scale(1.0).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{system: } 40 = 10a \Rightarrow a = 4\ \text{m}\cdot\text{s}^{-2}").scale(0.95).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2.5)
        b2_l2 = MathTex(r"\text{trolley B: } T = 4 \times 4 = 16\ \text{N}").scale(0.95).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = MathTex(r"\text{audit A: } 40 - 16 = 24 = 6 \times 4\ \checkmark").scale(0.95).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("Tension never enters the system equation").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): rough floor ---
        self.next_band(3)
        b3_title = Tex(r"Same pair, rough floor: $\mu_k = 0{,}15$").scale(1.0).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"f_{total} = 0{,}15 \times 98 = 14{,}7\ \text{N}").scale(0.95).shift(band_shift(3) + UP * 1.3)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"a = \frac{40 - 14{,}7}{10} = 2{,}53\ \text{m}\cdot\text{s}^{-2}").scale(0.95).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = MathTex(r"\text{B alone: } T - 5{,}88 = 4 \times 2{,}53 \Rightarrow T = 16{,}0\ \text{N}").scale(0.9).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex("One body, its OWN friction — never the total").scale(0.9).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_4): bench edge pulley ---
        self.next_band(4)
        b4_title = Tex(r"3 kg on bench ($\mu_k = 0{,}2$), 5 kg hanging").scale(0.95).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        bench = Line(LEFT * 3.4 + UP * 0.6, RIGHT * 0.6 + UP * 0.6, color=WHITE).shift(band_shift(4))
        blockA = Square(side_length=0.8, color=YELLOW).shift(band_shift(4) + LEFT * 1.6 + UP * 1.1)
        cord = Line(LEFT * 1.2 + UP * 1.1, RIGHT * 0.6 + UP * 1.1, color=BLUE).shift(band_shift(4))
        drop = Line(RIGHT * 0.6 + UP * 1.1, RIGHT * 0.6 + DOWN * 0.6, color=BLUE).shift(band_shift(4))
        blockB = Square(side_length=0.8, color=YELLOW).shift(band_shift(4) + RIGHT * 0.6 + DOWN * 1.1)
        self.play(Create(bench), Create(blockA), Create(cord), Create(drop), Create(blockB))
        self.wait(2)
        b4_l1 = MathTex(r"\text{system: } 49 - 5{,}88 = 8a \Rightarrow a = 5{,}39").scale(0.9).shift(band_shift(4) + RIGHT * 3.2 + UP * 1.0)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(2.5)
        b4_l2 = MathTex(r"\text{dangler: } 49 - T = 26{,}95 \Rightarrow T = 22{,}05\ \text{N}").scale(0.9).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): the tension-below-weight idea ---
        self.next_band(5)
        b5_l1 = Tex("Tension 22,05 N $<$ hanging weight 49 N").scale(1.0).shift(band_shift(5) + UP * 2.0)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=RED)))
        self.wait(2.5)
        b5_l2 = Tex("Necessarily — a falling mass needs a net downward force").scale(0.9).shift(band_shift(5) + UP * 0.9)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("String equals full weight only at zero acceleration").scale(0.9).shift(band_shift(5) + DOWN * 0.3)
        self.play(Write(b5_l3))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the incline version ---
        self.next_band(6)
        b6i_title = Tex(r"Incline: 5 kg on a 30$^\circ$ slope, 8 kg hanging").scale(0.95).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6i_title))
        self.wait(2)
        b6i_l1 = MathTex(r"\text{system: } \frac{78{,}4 - 24{,}5}{13} = 4{,}15\ \text{m}\cdot\text{s}^{-2}").scale(0.95).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6i_l1))
        self.wait(2.5)
        b6i_l2 = MathTex(r"T = 78{,}4 - 8 \times 4{,}15 = 45{,}2\ \text{N}").scale(0.95).shift(band_shift(6) + DOWN * 0.1)
        self.play(Write(b6i_l2))
        self.play(Create(SurroundingRectangle(b6i_l2, color=GREEN)))
        self.wait(2.5)
        b6i_l3 = Tex(r"On slopes, only $mg\sin\theta$ enters the system sum").scale(0.9).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6i_l3))
        self.wait(2.5)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): two trolleys tied together ---
        self.next_band(7)
        b6_title = Tex("Two trolleys tied together").scale(1.15).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("They move together: one acceleration").scale(0.95).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex("The cord pulls equally at both ends").scale(0.95).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("Zoomed out, the cord's two tugs cancel —").scale(0.95).shift(band_shift(7) + DOWN * 0.6)
        b6_l4 = Tex("the cord only matters one trolley at a time").scale(0.95).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(VGroup(b6_l3, b6_l4), color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): weigh the whole train ---
        self.next_band(8)
        b7_title = Tex("Weigh the whole train first").scale(1.1).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Move 1: one big object, outside forces only").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"a = \frac{40 - 14{,}7}{10} = 2{,}53\ \text{m}\cdot\text{s}^{-2}").scale(0.95).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex("Move 2: the laziest wagon alone").scale(0.95).shift(band_shift(8) + DOWN * 1.0)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = MathTex(r"T - 5{,}88 = 4 \times 2{,}53 \Rightarrow T = 16\ \text{N}").scale(0.95).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): the bucket down the well ---
        self.next_band(9)
        b8_title = Tex("The bucket down the well").scale(1.15).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Driver: the dangler's 49 N. Resister: 5,88 N of grip").scale(0.9).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"a = \frac{43{,}12}{8} = 5{,}39\ \text{m}\cdot\text{s}^{-2}").scale(1.0).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"49 - T = 26{,}95 \Rightarrow T = 22{,}05\ \text{N}").scale(1.0).shift(band_shift(9) + DOWN * 1.0)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("String below full weight: the mark of acceleration").scale(0.9).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 10 (subtopic_7): the tilted twin and the summary ---
        self.next_band(10)
        b9_l1 = Tex("Tilted twin: 5 kg on a 30$^\\circ$ slope, 8 kg hanging").scale(0.95).shift(band_shift(10) + UP * 2.0)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = MathTex(r"a = \frac{78{,}4 - 24{,}5}{13} = 4{,}15, \quad T = 45{,}2\ \text{N}").scale(0.95).shift(band_shift(10) + UP * 0.9)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = Tex("Two moves, one shared acceleration,").scale(0.95).shift(band_shift(10) + DOWN * 0.3)
        b9_l4 = Tex("a string that pulls and never pushes").scale(0.95).shift(band_shift(10) + DOWN * 1.0)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(4)
