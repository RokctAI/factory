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

# Band-layout whiteboard scene for the Coulomb's Law session duo.
# Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7.
# Band dwell times are proportional to subtopics.json
# (230/240/240/235/180/180/195 of 1500 s). Exporter-safe mobjects only
# (Tex/MathTex/Line/Arrow/Dot/Circle/Rectangle/VGroup); add-only lifecycle.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CoulombsLawSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md audio plays (~4-5%).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): charge and the statement of the law ---
        title = Tex("Coulomb's Law").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Like charges repel; unlike charges attract").scale(1.1).shift(UP * 1.3)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = MathTex(r"q_e = 1{,}6 \times 10^{-19}\ \text{C}").scale(1.1).shift(UP * 0.4)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = MathTex(r"F = \frac{k\,Q_1 Q_2}{r^2}").scale(1.3).shift(DOWN * 0.8)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=BLUE)))
        self.wait(2.5)
        b0_l4 = MathTex(r"k = 9 \times 10^{9}\ \text{N m}^2\text{C}^{-2}").scale(1.1).shift(DOWN * 2.1)
        self.play(Write(b0_l4))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the standard substitution ---
        self.next_band(1)
        b1_title = Tex(r"$+2\ \mu$C and $-3\ \mu$C, 10 cm apart").scale(1.15).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"2 \times 10^{-6}\ \text{C}, \;\; 3 \times 10^{-6}\ \text{C}").scale(1.05).shift(band_shift(1) + UP * 1.3)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"r = 10\ \text{cm} = 0{,}1\ \text{m}").scale(1.05).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"F = \frac{9 \times 10^{9} \times 2 \times 10^{-6} \times 3 \times 10^{-6}}{(0{,}1)^2}").scale(0.95).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = MathTex(r"F = 5{,}4\ \text{N, attractive}").scale(1.15).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)
        b1_l5 = Tex("Magnitudes only — signs give direction in words").scale(1.0).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l5))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): three charges in a line, force of A on B ---
        self.next_band(2)
        b2_title = Tex("Three charges in a line: net force on B").scale(1.1).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        rail = Line(LEFT * 4.0, RIGHT * 2.2).shift(band_shift(2) + UP * 1.3)
        dA = Dot(LEFT * 3.5 + UP * 1.3).shift(band_shift(2))
        dB = Dot(LEFT * 0.5 + UP * 1.3).shift(band_shift(2))
        dC = Dot(RIGHT * 1.5 + UP * 1.3).shift(band_shift(2))
        labA = Tex(r"A $+2\ \mu$C").scale(0.85).shift(band_shift(2) + UP * 1.9 + LEFT * 3.5)
        labB = Tex(r"B $+1\ \mu$C").scale(0.85).shift(band_shift(2) + UP * 1.9 + LEFT * 0.5)
        labC = Tex(r"C $-3\ \mu$C").scale(0.85).shift(band_shift(2) + UP * 1.9 + RIGHT * 1.5)
        self.play(Create(rail))
        self.play(FadeIn(dA), Write(labA))
        self.play(FadeIn(dB), Write(labB))
        self.play(FadeIn(dC), Write(labC))
        d1 = Tex("0,3 m").scale(0.8).shift(band_shift(2) + UP * 0.8 + LEFT * 2.0)
        d2 = Tex("0,2 m").scale(0.8).shift(band_shift(2) + UP * 0.8 + RIGHT * 0.5)
        self.play(Write(d1), Write(d2))
        self.wait(2)
        arrA = Arrow(LEFT * 0.5 + UP * 0.1, RIGHT * 0.6 + UP * 0.1, buff=0, color=YELLOW).shift(band_shift(2))
        labFA = Tex(r"$F_A$ (repel, right)").scale(0.8).shift(band_shift(2) + UP * 0.1 + RIGHT * 2.6)
        self.play(Create(arrA), Write(labFA))
        self.wait(2)
        b2_l1 = MathTex(r"F_A = \frac{9 \times 10^{9} \times 2 \times 10^{-6} \times 1 \times 10^{-6}}{(0{,}3)^2}").scale(0.9).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"F_A = \frac{0{,}018}{0{,}09} = 0{,}2\ \text{N right}").scale(1.05).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l2))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): force of C on B, then add ---
        self.next_band(3)
        b3_title = Tex("C attracts B — also to the right").scale(1.1).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"F_C = \frac{9 \times 10^{9} \times 1 \times 10^{-6} \times 3 \times 10^{-6}}{(0{,}2)^2}").scale(0.9).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"F_C = \frac{0{,}027}{0{,}04} = 0{,}675\ \text{N right}").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"F_{net} = 0{,}2 + 0{,}675 = 0{,}875\ \text{N right}").scale(1.1).shift(band_shift(3) + DOWN * 1.0)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_trap = MathTex(r"\text{using } r = 0{,}5\ \text{m (A to C)}").scale(1.0).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_trap))
        self.play(Create(strike(b3_trap)))
        self.wait(1.5)
        b3_rule = Tex("Each pair keeps its own $r$").scale(1.05).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_rule))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): the right-angle arrangement ---
        self.next_band(4)
        b4_title = Tex("Right angle: net force on $Q_1$").scale(1.1).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        q1 = Dot(LEFT * 2.5 + DOWN * 0.4).shift(band_shift(4))
        q2 = Dot(LEFT * 2.5 + UP * 1.6).shift(band_shift(4))
        q3 = Dot(RIGHT * 0.5 + DOWN * 0.4).shift(band_shift(4))
        lq1 = Tex(r"$Q_1 +2\ \mu$C").scale(0.8).shift(band_shift(4) + LEFT * 4.0 + DOWN * 0.4)
        lq2 = Tex(r"$Q_2 +3\ \mu$C").scale(0.8).shift(band_shift(4) + LEFT * 2.5 + UP * 2.1)
        lq3 = Tex(r"$Q_3 -4\ \mu$C").scale(0.8).shift(band_shift(4) + RIGHT * 0.5 + UP * 0.1)
        e1 = Line(LEFT * 2.5 + DOWN * 0.4, LEFT * 2.5 + UP * 1.6).shift(band_shift(4))
        e2 = Line(LEFT * 2.5 + DOWN * 0.4, RIGHT * 0.5 + DOWN * 0.4).shift(band_shift(4))
        self.play(FadeIn(q1), Write(lq1))
        self.play(Create(e1), FadeIn(q2), Write(lq2))
        self.play(Create(e2), FadeIn(q3), Write(lq3))
        dv = Tex("0,3 m").scale(0.75).shift(band_shift(4) + LEFT * 3.3 + UP * 0.6)
        dh = Tex("0,4 m").scale(0.75).shift(band_shift(4) + LEFT * 1.0 + DOWN * 0.8)
        self.play(Write(dv), Write(dh))
        self.wait(2)
        aS = Arrow(LEFT * 2.5 + DOWN * 0.4, LEFT * 2.5 + DOWN * 1.6, buff=0, color=YELLOW).shift(band_shift(4))
        lS = Tex("pushed south").scale(0.8).shift(band_shift(4) + LEFT * 4.1 + DOWN * 1.6)
        self.play(Create(aS), Write(lS))
        self.wait(1.5)
        aE = Arrow(LEFT * 2.5 + DOWN * 0.4, LEFT * 1.0 + DOWN * 0.4, buff=0, color=YELLOW).shift(band_shift(4) + DOWN * 0.02)
        lE = Tex("pulled east").scale(0.8).shift(band_shift(4) + RIGHT * 0.3 + DOWN * 0.9)
        self.play(Create(aE), Write(lE))
        self.wait(2)
        b4_note = Tex("One Coulomb calculation per neighbour").scale(1.0).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_note))
        self.wait(2)

        # --- Band 5 (subtopic_3): the two magnitudes, then Pythagoras ---
        self.next_band(5)
        b5_l1 = MathTex(r"F_2 = \frac{0{,}054}{(0{,}3)^2} = 0{,}6\ \text{N south}").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"F_3 = \frac{0{,}072}{(0{,}4)^2} = 0{,}45\ \text{N east}").scale(1.05).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"F = \sqrt{0{,}6^2 + 0{,}45^2} = \sqrt{0{,}5625}").scale(1.05).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = MathTex(r"F = 0{,}75\ \text{N}").scale(1.15).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = MathTex(r"\tan\theta = \frac{0{,}6}{0{,}45} = 1{,}33").scale(1.05).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l5))
        self.wait(2)
        b5_ans = Tex(r"0,75 N at 53,1$^\circ$ south of east").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_ans))
        self.play(Create(SurroundingRectangle(b5_ans, color=GREEN)))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): touching identical spheres ---
        self.next_band(6)
        b6_title = Tex("Identical spheres touch, then separate").scale(1.1).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        cP = Circle(radius=0.5, color=WHITE).shift(band_shift(6) + LEFT * 2.5 + UP * 1.2)
        cT = Circle(radius=0.5, color=WHITE).shift(band_shift(6) + RIGHT * 2.5 + UP * 1.2)
        lP = Tex(r"P $+6\ \mu$C").scale(0.85).shift(band_shift(6) + LEFT * 2.5 + UP * 2.1)
        lT = Tex(r"T $-2\ \mu$C").scale(0.85).shift(band_shift(6) + RIGHT * 2.5 + UP * 2.1)
        self.play(Create(cP), Write(lP))
        self.play(Create(cT), Write(lT))
        self.wait(2)
        b6_l1 = MathTex(r"(+6) + (-2) = +4\ \mu\text{C}, \;\; \text{each } +2\ \mu\text{C}").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"F = \frac{9 \times 10^{9} \times 2 \times 10^{-6} \times 2 \times 10^{-6}}{(0{,}1)^2}").scale(0.9).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"F = 3{,}6\ \text{N, now repulsive}").scale(1.1).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex("Before touching: 10,8 N attractive").scale(1.0).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l4))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): the exam traps ---
        self.next_band(7)
        b7_title = Tex("The exam traps").scale(1.2).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"1. Convert to C and m BEFORE squaring").scale(1.0).shift(band_shift(7) + UP * 1.3)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_bad = MathTex(r"F = \frac{k(-3 \times 10^{-6})Q_2}{r^2}").scale(1.0).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_bad))
        self.play(Create(strike(b7_bad)))
        self.wait(1.5)
        b7_l2 = Tex("2. Signs never enter the formula").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("3. $r$ is between the CENTRES").scale(1.0).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex(r"4. Halve $r$ $\Rightarrow$ force $\times$ 4").scale(1.0).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("5. Sharing needs IDENTICAL spheres").scale(1.0).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(b7_l5))
        self.wait(2.5)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the crackle in your jersey ---
        self.next_band(8)
        b8_title = Tex("The crackle in your jersey").scale(1.2).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Rubbing moves electrons — charge moves house").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Gains electrons: negative. Loses: positive").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Opposites attract; likes repel").scale(1.05).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = MathTex(r"1\ \mu\text{C} = 10^{-6}\ \text{C: trillions of electrons}").scale(0.95).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): gravity's louder twin ---
        self.next_band(9)
        b9_title = Tex("Gravity's louder twin").scale(1.2).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1a = MathTex(r"\text{Gravity: } F = \frac{G m_1 m_2}{r^2}").scale(1.05).shift(band_shift(9) + UP * 1.3)
        self.play(Write(b9_l1a))
        self.wait(2)
        b9_l1b = MathTex(r"\text{Coulomb: } F = \frac{k Q_1 Q_2}{r^2}").scale(1.05).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1b))
        self.wait(2.5)
        b9_l2 = Tex(r"Double both charges $\Rightarrow$ 4$\times$ the force").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex(r"Double the distance $\Rightarrow$ quarter the force").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("Numbers give size; signs give direction").scale(1.0).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): tug-of-war on the middle charge ---
        self.next_band(10)
        b10_title = Tex("Tug-of-war on the middle charge").scale(1.15).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        mid = Dot(band_shift(10) + UP * 1.2)
        aL = Arrow(UP * 1.2, UP * 1.2 + LEFT * 1.8, buff=0, color=YELLOW).shift(band_shift(10))
        aR = Arrow(UP * 1.2, UP * 1.2 + RIGHT * 1.1, buff=0, color=YELLOW).shift(band_shift(10))
        self.play(FadeIn(mid))
        self.play(Create(aL), Create(aR))
        self.wait(2)
        b10_l1 = Tex("One arrow per neighbour — arrows FIRST").scale(1.0).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex("Same way: add. Opposite: subtract").scale(1.0).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"\text{Right angles: } \sqrt{0{,}45^2 + 0{,}6^2} = 0{,}75\ \text{N}").scale(1.0).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex("Arrows, then sizes, then combine").scale(1.05).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(4)
