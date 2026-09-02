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

# Band-layout whiteboard scene: one band per teaching beat, camera moves down
# to fresh space, nothing removed.
# Write-only reveals on single-string Tex/MathTex keep the export clean; the
# right-triangle sketch is hand-built from Lines + Dots + Tex (exporter-
# supported shapes only). Bands cover all seven subtopics (Part 1 — Expert:
# 1-4; Part 2 — Simplifier: 5-7), dwell time proportional to subtopics.json
# (215/210/245/260/180/180/200 of 1490 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DistanceMidpointGradientSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(12)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the distance formula from Pythagoras
        title = Tex("Distance, Midpoint and Gradient").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        pts = MathTex(r"A(-1;\,3) \quad B(5;\,11)").scale(1.1).shift(UP * 0.9)
        self.play(Write(pts))
        self.wait(2)
        # right triangle sketch: A lower-left, B upper-right
        Apt = LEFT * 4.6 + DOWN * 1.6
        Bpt = LEFT * 2.2 + UP * 0.6
        Cpt = LEFT * 2.2 + DOWN * 1.6
        dA = Dot(Apt)
        dB = Dot(Bpt)
        tri = VGroup(Line(Apt, Cpt), Line(Cpt, Bpt), Line(Apt, Bpt))
        self.play(Create(dA), Create(dB))
        self.play(Create(tri))
        labA = MathTex(r"A").scale(0.8).shift(Apt + LEFT * 0.35)
        labB = MathTex(r"B").scale(0.8).shift(Bpt + UP * 0.3)
        lab6 = MathTex(r"6").scale(0.8).shift((Apt + Cpt) / 2 + DOWN * 0.35)
        lab8 = MathTex(r"8").scale(0.8).shift((Cpt + Bpt) / 2 + RIGHT * 0.3)
        self.play(Write(labA), Write(labB), Write(lab6), Write(lab8))
        self.wait(2)
        d1 = MathTex(r"5 - (-1) = 6, \quad 11 - 3 = 8").scale(1.0).shift(RIGHT * 2.3 + DOWN * 0.2)
        d2 = MathTex(r"AB = \sqrt{6^2 + 8^2} = \sqrt{100} = 10").scale(1.0).shift(RIGHT * 2.2 + DOWN * 1.2)
        self.play(Write(d1))
        self.wait(2)
        self.play(Write(d2))
        self.play(Create(SurroundingRectangle(d2, color=GREEN)))
        form = MathTex(r"d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}").scale(1.05).shift(DOWN * 2.7)
        self.play(Write(form))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): properties + surd answer
        self.next_band(1)
        b1_l0 = Tex("Order never matters — squaring erases the sign").scale(1.05).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_l0))
        self.wait(2)
        b1_l1 = MathTex(r"(-6)^2 = 36 = 6^2").scale(1.05).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex(r"No perfect square? Leave the surd:").scale(1.05).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"BC = \sqrt{5^2 + (-3)^2} = \sqrt{34} \approx 5{,}83").scale(1.05).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l2))
        self.wait(1.5)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex(r"Watch the double negative: $5 - (-1) = 6$, not 4").scale(1.0).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l4))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): midpoint, forwards and backwards
        self.next_band(2)
        b2_title = Tex("Midpoint: add and halve").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"M = \left(\tfrac{x_1 + x_2}{2};\; \tfrac{y_1 + y_2}{2}\right)").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"M_{AB} = \left(\tfrac{-1+5}{2};\; \tfrac{3+11}{2}\right) = (2;\, 7)").scale(1.05).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = Tex(r"Backwards: $M(2; 7)$, $A(-1; 3)$ — find $B$").scale(1.0).shift(band_shift(2) + DOWN * 1.1)
        b2_l4 = MathTex(r"\tfrac{-1+x}{2} = 2, \quad \tfrac{3+y}{2} = 7 \;\Rightarrow\; B(5;\, 11)").scale(0.8).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Midpoint is the only one that ADDS").scale(1.0).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l5))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): gradient
        self.next_band(3)
        b3_title = Tex("Gradient: rise over run").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"m = \frac{y_2 - y_1}{x_2 - x_1}").scale(1.0).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l1b = MathTex(r"m = \frac{11-3}{5-(-1)} = \frac{8}{6} = \frac{4}{3}").scale(1.0).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l1b))
        self.play(Create(SurroundingRectangle(b3_l1b, color=GREEN)))
        self.wait(2.5)
        b3_l2 = Tex(r"Positive rises; negative falls; horizontal: $m = 0$;").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        b3_l3 = Tex(r"vertical: UNDEFINED — never zero").scale(1.0).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"\text{Parallel: } m_1 = m_2 \qquad \perp: \; m_1 \times m_2 = -1").scale(1.0).shift(band_shift(3) + DOWN * 2.3)
        b3_l5 = MathTex(r"\tfrac{4}{3} \times \left(-\tfrac{3}{4}\right) = -1 \;\checkmark").scale(1.0).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_4): the quadrilateral — sides and gradients
        self.next_band(4)
        b4_title = Tex(r"Classify: $A(-1;3)$, $B(5;11)$, $C(10;8)$, $D(4;0)$").scale(1.0).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"AB = 10, \; BC = \sqrt{34}, \; CD = 10, \; DA = \sqrt{34}").scale(1.0).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex(r"Both pairs of opposite sides equal").scale(1.0).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"m_{AB} = m_{DC} = \tfrac{4}{3}, \;\; m_{AD} = m_{BC} = -\tfrac{3}{5}").scale(0.9).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = MathTex(r"M_{AC} = (4{,}5;\, 5{,}5) = M_{BD}").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        b4_l5 = Tex(r"Diagonals bisect each other — parallelogram, three ways").scale(0.95).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): rectangle? rhombus? + error museum
        self.next_band(5)
        b5_title = Tex("Push further: rectangle? rhombus?").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"\tfrac{4}{3} \times \left(-\tfrac{3}{5}\right) = -\tfrac{4}{5} \neq -1").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex(r"No right angle — not a rectangle").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"10 \neq \sqrt{34} \;\text{ — not a rhombus}").scale(1.0).shift(band_shift(5) + DOWN * 0.7)
        b5_l4 = Tex(r"Conclusion: a parallelogram, nothing more").scale(1.05).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex(r"Never trust the sketch — only $m_1 m_2 = -1$ proves").scale(0.95).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l5))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): eight blocks across, six blocks up
        self.next_band(6)
        b6_title = Tex("Eight blocks across, six blocks up").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"Walking the streets: $8 + 6 = 14$ blocks").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"Cutting across the fields:").scale(1.0).shift(band_shift(6) + UP * 0.4)
        b6_l3 = MathTex(r"\sqrt{8^2 + 6^2} = \sqrt{100} = 10 \text{ blocks}").scale(1.05).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = Tex(r"Our points give the same triangle, turned:").scale(1.0).shift(band_shift(6) + DOWN * 1.5)
        b6_l5 = MathTex(r"5 - (-1) = 6, \quad 11 - 3 = 8").scale(1.0).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(2.5)

        # --- Band 7 (subtopic_6): meeting in the middle
        self.next_band(7)
        b7_title = Tex("Meeting exactly in the middle").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"Houses 5 and 17 meet at $\tfrac{5+17}{2} = 11$").scale(1.0).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"\left(\tfrac{-1+5}{2};\; \tfrac{3+11}{2}\right) = (2;\, 7)").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex(r"Middle means ADD; everything else takes away").scale(1.0).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex(r"Same middle for both diagonals? They bisect —").scale(1.0).shift(band_shift(7) + DOWN * 1.7)
        b7_l5 = Tex(r"and the shape is a parallelogram").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(2.5)

        # --- Band 8 (subtopic_7): steepness you can feel
        self.next_band(8)
        b8_title = Tex("Steepness you can feel").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"m = \frac{\text{rise}}{\text{run}} = \frac{8}{6} = \frac{4}{3}").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex(r"Every 3 steps forward, 4 steps up").scale(1.0).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex(r"Flat court: $m = 0$. Wall: undefined — never zero").scale(1.0).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = MathTex(r"\perp: \text{ flip and change sign — } \tfrac{4}{3} \to -\tfrac{3}{4}").scale(1.0).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex(r"Brackets on double negatives; same order top and bottom;").scale(0.9).shift(band_shift(8) + DOWN * 2.5)
        b8_l6 = Tex(r"the numbers decide, not the drawing").scale(0.9).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.wait(4)
