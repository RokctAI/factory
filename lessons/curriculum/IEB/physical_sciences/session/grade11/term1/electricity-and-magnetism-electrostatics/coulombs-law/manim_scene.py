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

# Band-layout whiteboard scene for the Coulomb's Law duo.
# Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7.
# Band dwell proportional to subtopics.json (230/240/240/235/180/180/195
# of 1500 s). Exporter-safe mobjects only; add-only lifecycle; camera bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CoulombLawElectrostaticsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the law ---
        title = Tex("Coulomb's Law").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"F = \frac{k Q_1 Q_2}{r^2}").scale(1.3).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.play(Create(SurroundingRectangle(b0_l1, color=BLUE)))
        self.wait(2.5)
        b0_l2 = MathTex(r"k = 9 \times 10^9\ \text{N}\cdot\text{m}^2\cdot\text{C}^{-2}").scale(0.9).shift(DOWN * 0.2)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("Magnitudes into the formula;").scale(0.9).shift(DOWN * 1.1)
        b0_l4 = Tex("signs decide attract or repel, in words").scale(0.9).shift(DOWN * 1.8)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): the standard substitution ---
        self.next_band(1)
        b1_title = Tex(r"$+3\ \mu$C and $-5\ \mu$C, 15 cm apart").scale(1.0).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Convert first: $3 \\times 10^{-6}$ C, $5 \\times 10^{-6}$ C, 0,15 m").scale(0.9).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = MathTex(r"F = \frac{9 \times 10^9 \times 3 \times 10^{-6} \times 5 \times 10^{-6}}{0{,}15^2}").scale(0.95).shift(band_shift(1) + UP * 0.0)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = MathTex(r"F = \frac{0{,}135}{0{,}0225} = 6{,}0\ \text{N attractive}").scale(1.0).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_l4 = Tex(r"$-4{,}8\ \mu$C $= 3 \times 10^{13}$ extra electrons").scale(0.9).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1_l4))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): straight line setup ---
        self.next_band(2)
        b2_title = Tex("Three charges in a line — net force on B").scale(1.0).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        dA = Dot(color=YELLOW).shift(band_shift(2) + LEFT * 3.0 + UP * 1.0)
        dB = Dot(color=YELLOW).shift(band_shift(2) + LEFT * 0.5 + UP * 1.0)
        dC = Dot(color=YELLOW).shift(band_shift(2) + RIGHT * 2.8 + UP * 1.0)
        lA = MathTex(r"A: +3\ \mu\text{C}").scale(0.75).shift(band_shift(2) + LEFT * 3.0 + UP * 1.7)
        lB = MathTex(r"B: -2\ \mu\text{C}").scale(0.75).shift(band_shift(2) + LEFT * 0.5 + UP * 1.7)
        lC = MathTex(r"C: +4\ \mu\text{C}").scale(0.75).shift(band_shift(2) + RIGHT * 2.8 + UP * 1.7)
        self.play(Create(dA), Create(dB), Create(dC), Write(lA), Write(lB), Write(lC))
        self.wait(2)
        aL = Arrow(LEFT * 0.5 + UP * 1.0, LEFT * 2.0 + UP * 1.0, buff=0.1, color=RED).shift(band_shift(2))
        aR = Arrow(LEFT * 0.5 + UP * 1.0, RIGHT * 0.7 + UP * 1.0, buff=0.1, color=BLUE).shift(band_shift(2))
        self.play(Create(aL), Create(aR))
        self.wait(2)
        b2_l1 = Tex("A attracts B left; C attracts B right").scale(0.9).shift(band_shift(2) + DOWN * 0.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex("Arrows drawn BEFORE any arithmetic").scale(0.9).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): straight line numbers ---
        self.next_band(3)
        b3_l1 = MathTex(r"F_{AB} = \frac{0{,}054}{0{,}04} = 1{,}35\ \text{N left}").scale(1.0).shift(band_shift(3) + UP * 1.7)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"F_{CB} = \frac{0{,}072}{0{,}09} = 0{,}8\ \text{N right}").scale(1.0).shift(band_shift(3) + UP * 0.6)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"F_{net} = 1{,}35 - 0{,}8 = 0{,}55\ \text{N toward A}").scale(1.0).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("Each pair keeps its OWN separation").scale(0.95).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): right-angle arrangement ---
        self.next_band(4)
        b4_title = Tex("Charges at right angles").scale(1.1).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"F_{from\ Q_2} = \frac{0{,}09}{0{,}25} = 0{,}36\ \text{N north}").scale(0.95).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"F_{from\ Q_3} = \frac{0{,}054}{0{,}09} = 0{,}6\ \text{N west}").scale(0.95).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        aN = Arrow(DOWN * 1.8, DOWN * 0.9, buff=0, color=BLUE).shift(band_shift(4) + LEFT * 1.5)
        aW = Arrow(LEFT * 1.5 + DOWN * 1.8, LEFT * 3.0 + DOWN * 1.8, buff=0, color=BLUE).shift(band_shift(4))
        aRes = Arrow(LEFT * 1.5 + DOWN * 1.8, LEFT * 3.0 + DOWN * 0.9, buff=0, color=GREEN).shift(band_shift(4))
        self.play(Create(aN), Create(aW))
        self.wait(1.5)
        self.play(Create(aRes))
        self.wait(2)
        b4_l3 = Tex("Perpendicular arrows: Pythagoras next").scale(0.9).shift(band_shift(4) + RIGHT * 2.6 + DOWN * 1.4)
        self.play(Write(b4_l3))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): the resultant ---
        self.next_band(5)
        b5_l1 = MathTex(r"R = \sqrt{0{,}36^2 + 0{,}6^2} = \sqrt{0{,}4896} = 0{,}7\ \text{N}").scale(1.0).shift(band_shift(5) + UP * 1.5)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(2.5)
        b5_l2 = MathTex(r"\tan\theta = \frac{0{,}36}{0{,}6} = 0{,}6 \Rightarrow \theta = 31{,}0^\circ").scale(1.0).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex(r"0,7 N at 31,0$^\circ$ north of west").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): touching spheres and traps ---
        self.next_band(6)
        b6_title = Tex(r"Identical spheres: $+8\ \mu$C and $-4\ \mu$C touch").scale(0.95).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{before: } F = \frac{0{,}288}{0{,}04} = 7{,}2\ \text{N attractive}").scale(0.9).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"\text{share: } \frac{+8 - 4}{2} = +2\ \mu\text{C each}").scale(0.9).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"\text{after: } F = \frac{0{,}036}{0{,}04} = 0{,}9\ \text{N repulsive}").scale(0.9).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = Tex("One touch changed size AND character").scale(0.9).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): the trap inventory ---
        self.next_band(7)
        b7t_title = Tex("The trap inventory").scale(1.15).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7t_title))
        self.wait(1.5)
        b7t_l1 = Tex("1. Units: micro to $\\times 10^{-6}$, cm to m BEFORE squaring").scale(0.85).shift(band_shift(7) + UP * 1.3)
        self.play(Write(b7t_l1))
        self.wait(2)
        b7t_l2 = Tex("2. Magnitudes only; signs reasoned separately").scale(0.85).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7t_l2))
        self.wait(2)
        b7t_l3 = Tex("3. Distance runs centre to centre").scale(0.85).shift(band_shift(7) + DOWN * 0.3)
        self.play(Write(b7t_l3))
        self.wait(2)
        b7t_l4 = Tex("4. Halve r: force $\\times$ 4 — gravitation logic").scale(0.85).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7t_l4))
        self.wait(2)
        b7t_l5 = Tex("5. Equal sharing needs IDENTICAL spheres").scale(0.85).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7t_l5))
        self.play(Create(SurroundingRectangle(b7t_l5, color=GREEN)))
        self.wait(2.5)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the crackle ---
        self.next_band(8)
        b7_title = Tex("The crackle in your jersey").scale(1.15).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Rubbing scrapes electrons across —").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b7_l2 = Tex("charge moves house, none is created").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Gains electrons: negative. Loses them: positive").scale(0.9).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex("Opposites attract, likes repel — one rule").scale(0.95).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): gravity's louder twin ---
        self.next_band(9)
        b8_title = Tex("Gravity's louder twin").scale(1.15).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Same skeleton: multiply sources, divide by $r^2$").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Double the distance: quarter the force — both laws").scale(0.9).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Differences: electricity pushes AND pulls,").scale(0.9).shift(band_shift(9) + DOWN * 0.8)
        b8_l4 = Tex("and its constant is enormous").scale(0.9).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 10 (subtopic_7): the tug-of-war ---
        self.next_band(10)
        b9_title = Tex("The tug-of-war on the middle charge").scale(1.05).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("One arrow per neighbour: toward if pulling,").scale(0.9).shift(band_shift(10) + UP * 1.2)
        b9_l2 = Tex("away if shoving — each at its own distance").scale(0.9).shift(band_shift(10) + UP * 0.5)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Arrows agree: add. Arrows fight: subtract").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("At right angles: square, add, root — 0,36 and 0,6 give 0,7").scale(0.85).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("Arrows, then sizes, then combine").scale(0.95).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(b9_l5))
        self.wait(4)
