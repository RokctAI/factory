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

# Band-layout whiteboard scene for the Resultant by Component Method duo.
# Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7.
# Band dwell proportional to subtopics.json (215/230/220/235/180/195/185
# of 1460 s). Exporter-safe mobjects only; add-only lifecycle; camera bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ResultantComponentMethodSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): vocabulary ---
        title = Tex("Resultant by the Component Method").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Vector: magnitude AND direction").scale(1.05).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("Scalar: magnitude only").scale(1.05).shift(UP * 0.3)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("Resultant: the ONE vector with the").scale(1.0).shift(DOWN * 0.7)
        b0_l4 = Tex("same effect as all of them together").scale(1.0).shift(DOWN * 1.4)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(VGroup(b0_l3, b0_l4), color=BLUE)))
        self.wait(3)

        # --- Band 1 (subtopic_1): tail-to-head, closed diagram ---
        self.next_band(1)
        b1_title = Tex("Tail-to-head: 60 N east, then 80 N north").scale(1.0).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        aE = Arrow(LEFT * 2.8 + DOWN * 1.7, LEFT * 0.55 + DOWN * 1.7, buff=0, color=YELLOW).shift(band_shift(1))
        lE = Tex("60 N").scale(0.85).shift(band_shift(1) + LEFT * 1.7 + DOWN * 2.2)
        self.play(Create(aE), Write(lE))
        self.wait(1.5)
        aN = Arrow(LEFT * 0.55 + DOWN * 1.7, LEFT * 0.55 + UP * 1.3, buff=0, color=YELLOW).shift(band_shift(1))
        lN = Tex("80 N").scale(0.85).shift(band_shift(1) + RIGHT * 0.3 + DOWN * 0.2)
        self.play(Create(aN), Write(lN))
        self.wait(1.5)
        aR = Arrow(LEFT * 2.8 + DOWN * 1.7, LEFT * 0.55 + UP * 1.3, buff=0, color=GREEN).shift(band_shift(1))
        lR = Tex("R = 100 N").scale(0.9).shift(band_shift(1) + LEFT * 2.6 + UP * 0.4)
        self.play(Create(aR), Write(lR))
        self.wait(2.5)
        b1_l1 = Tex("Tail of the first to head of the last").scale(0.95).shift(band_shift(1) + RIGHT * 3.0 + UP * 1.3)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Closed diagram: resultant zero,").scale(0.95).shift(band_shift(1) + RIGHT * 3.0 + UP * 0.2)
        b1_l3 = Tex("object in EQUILIBRIUM").scale(0.95).shift(band_shift(1) + RIGHT * 3.0 + DOWN * 0.5)
        self.play(Write(b1_l2))
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("Equilibrant: equal to R, opposite direction").scale(0.95).shift(band_shift(1) + RIGHT * 1.6 + DOWN * 2.9)
        self.play(Write(b1_l4))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): resolving formulas ---
        self.next_band(2)
        b2_title = Tex("Resolving into components").scale(1.15).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"R_x = R\cos\theta \qquad R_y = R\sin\theta").scale(1.15).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=BLUE)))
        self.wait(2.5)
        hyp = Arrow(LEFT * 3.0 + DOWN * 1.6, RIGHT * 0.2 + UP * 0.2, buff=0, color=YELLOW).shift(band_shift(2))
        adj = Line(LEFT * 3.0 + DOWN * 1.6, RIGHT * 0.2 + DOWN * 1.6).shift(band_shift(2))
        opp = DashedLine(RIGHT * 0.2 + DOWN * 1.6, RIGHT * 0.2 + UP * 0.2).shift(band_shift(2))
        lth = MathTex(r"\theta").scale(0.9).shift(band_shift(2) + LEFT * 2.0 + DOWN * 1.25)
        self.play(Create(hyp), Create(adj), Create(opp), Write(lth))
        self.wait(2)
        b2_l2 = Tex("Adjacent takes cosine,").scale(1.0).shift(band_shift(2) + RIGHT * 3.3 + DOWN * 0.6)
        b2_l3 = Tex("opposite takes sine").scale(1.0).shift(band_shift(2) + RIGHT * 3.3 + DOWN * 1.3)
        self.play(Write(b2_l2))
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex("Angle from the vertical? They swap — sketch it").scale(0.95).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l4))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): 250 N at 30 degrees ---
        self.next_band(3)
        b3_title = Tex(r"250 N at 30$^\circ$ above the horizontal").scale(1.05).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"F_x = 250\cos 30^\circ = 250 \times 0{,}866").scale(1.0).shift(band_shift(3) + UP * 1.3)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"F_x = 216{,}5\ \text{N forward}").scale(1.05).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = MathTex(r"F_y = 250\sin 30^\circ = 250 \times 0{,}5").scale(1.0).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"F_y = 125\ \text{N upward}").scale(1.05).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex(r"East/north positive: 120 N west is $x = -120$ N").scale(0.95).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): four forces, resolved ---
        self.next_band(4)
        b4_title = Tex("Four forces on a ring — resolve them all").scale(1.05).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"F_1 (250, 30^\circ): \; x = +216{,}5, \; y = +125").scale(0.95).shift(band_shift(4) + UP * 1.3)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"F_2 (180\ \text{N north}): \; x = 0, \; y = +180").scale(0.95).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"F_3 (120\ \text{N west}): \; x = -120, \; y = 0").scale(0.95).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"F_4 (90\ \text{N south}): \; x = 0, \; y = -90").scale(0.95).shift(band_shift(4) + DOWN * 1.4)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex(r"Write the zeros — proof you forgot nothing").scale(0.95).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): sum the columns ---
        self.next_band(5)
        b5_title = Tex("Sum each column separately").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"R_x = 216{,}5 + 0 - 120 + 0").scale(1.05).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"R_x = 96{,}5\ \text{N east}").scale(1.1).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2)
        b5_l3 = MathTex(r"R_y = 125 + 180 + 0 - 90").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = MathTex(r"R_y = 215\ \text{N north}").scale(1.1).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex("Carry 216,5 — never round components early").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l5))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): Pythagoras and the angle ---
        self.next_band(6)
        b6_title = Tex("Rebuild one resultant").scale(1.15).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"R = \sqrt{96{,}5^2 + 215^2} = \sqrt{55\ 537{,}25}").scale(1.0).shift(band_shift(6) + UP * 1.3)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"R = 235{,}7\ \text{N}").scale(1.15).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"\tan\theta = \frac{215}{96{,}5} = 2{,}228").scale(1.0).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"\theta = 65{,}8^\circ").scale(1.1).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_ans = Tex(r"235,7 N at 65,8$^\circ$ north of east").scale(1.0).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_ans))
        self.play(Create(SurroundingRectangle(b6_ans, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the check and the traps ---
        self.next_band(7)
        b7_l1 = MathTex(r"\text{Check: } \sqrt{60^2 + 80^2} = 100\ \text{N}, \; 53{,}1^\circ").scale(0.95).shift(band_shift(7) + UP * 2.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex("Trap 1: calculator must show DEG, not RAD").scale(0.95).shift(band_shift(7) + UP * 1.0)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex(r"Trap 2: $R_x < 0$? Add 180$^\circ$ to the angle").scale(0.95).shift(band_shift(7) + UP * 0.0)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex(r"Trap 3: bearings — 65,8$^\circ$ N of E is bearing 24,2$^\circ$").scale(0.9).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("Magnitude without direction: half an answer").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=BLUE)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): walking to the shop ---
        self.next_band(8)
        b8_title = Tex("Walking to the shop the long way").scale(1.15).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("60 m east, then 80 m north: 140 m of pavement").scale(0.95).shift(band_shift(8) + UP * 1.3)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("The bird flies 100 m — that is the resultant").scale(0.95).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex("Arrows join like train carriages, tip to tail").scale(0.95).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("Walk back to your own gate: zero resultant,").scale(0.95).shift(band_shift(8) + DOWN * 1.6)
        b8_l5 = Tex("everything balanced — equilibrium").scale(0.95).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): splitting one push ---
        self.next_band(9)
        b9_title = Tex("Splitting one push into two honest pushes").scale(1.05).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Sort the tilted pull into piles, like change").scale(0.95).shift(band_shift(9) + UP * 1.3)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"\text{forward: } 250 \times 0{,}866 = 216{,}5\ \text{N}").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"\text{upward: } 250 \times 0{,}5 = 125\ \text{N}").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("Next to the angle: cosine. Across: sine").scale(0.95).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex("West or south: a minus sign, like money owed").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): two piles, one answer ---
        self.next_band(10)
        b10_title = Tex("Two piles, one answer").scale(1.2).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"\text{sideways: } 216{,}5 - 120 = 96{,}5\ \text{N east}").scale(0.95).shift(band_shift(10) + UP * 1.3)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"\text{upward: } 125 + 180 - 90 = 215\ \text{N north}").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"\sqrt{96{,}5^2 + 215^2} = 235{,}7\ \text{N}").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex(r"at 65,8$^\circ$ from east towards north").scale(1.0).shift(band_shift(10) + DOWN * 1.6)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(VGroup(b10_l3, b10_l4), color=GREEN)))
        self.wait(2.5)
        b10_l5 = Tex("Say the size, then say where it points").scale(0.95).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l5))
        self.wait(4)
