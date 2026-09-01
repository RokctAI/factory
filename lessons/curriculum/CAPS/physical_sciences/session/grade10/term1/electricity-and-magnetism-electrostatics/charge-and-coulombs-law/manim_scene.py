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

# Band-layout whiteboard scene for "Charge and Coulomb's Law" (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). Exporter-safe mobjects
# only; write-only reveals; camera moves down band by band. Band time is
# apportioned to subtopics.json (225/235/235/245/180/185/185 of 1490 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ChargeAndCoulombsLawSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): charge, unit, quantisation ---
        title = Tex("Charge and Coulomb's Law").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Two kinds of charge: $+$ and $-$").scale(1.1).shift(UP * 1.1)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex(r"$\mu$C is $10^{-6}$ C; nC is $10^{-9}$ C").scale(1.05).shift(UP * 0.2)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("Charge is quantised:").scale(1.1).shift(DOWN * 0.8)
        b0_l4 = MathTex(r"Q = nq, \quad q = 1{,}6 \times 10^{-19}\;\text{C}").scale(1.1).shift(DOWN * 1.7)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex("whole electrons only — never half").scale(1.0).shift(DOWN * 2.7)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): Q = nq both ways ---
        self.next_band(1)
        b1_t = Tex(r"Sphere holds $-4{,}8 \times 10^{-17}$ C — how many $e$?").scale(1.0).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_l1 = MathTex(r"n = \frac{Q}{q} = \frac{4{,}8 \times 10^{-17}}{1{,}6 \times 10^{-19}}").scale(1.1).shift(band_shift(1) + UP * 0.9)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = MathTex(r"n = 300 \;\text{excess electrons}").scale(1.1).shift(band_shift(1) + DOWN * 0.3)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)
        b1_l3 = Tex(r"Lost $5 \times 10^{10}$ electrons:").scale(1.05).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(b1_l3))
        self.wait(1.5)
        b1_l4 = MathTex(r"Q = (5 \times 10^{10})(1{,}6 \times 10^{-19}) = 8 \times 10^{-9}\;\text{C}").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        b1_l5 = Tex("positive — losing electrons leaves $+$").scale(1.0).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): the three charging methods ---
        self.next_band(2)
        b2_t = Tex("Three ways to charge an object").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l0 = Tex("Only ELECTRONS ever move").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l0))
        self.play(Create(SurroundingRectangle(b2_l0, color=GREEN)))
        self.wait(2)
        b2_l1 = Tex("Friction: insulators, opposite signs").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex("Contact: conductors share, SAME sign").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("Induction: no touch, OPPOSITE sign").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("Say ``the cloth gained electrons''").scale(1.0).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): induction, drawn step by step ---
        self.next_band(3)
        b3_t = Tex("Induction on a metal sphere").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        rod = Rectangle(width=2.2, height=0.5).shift(band_shift(3) + LEFT * 3.4 + UP * 0.3)
        rod_lab = MathTex(r"- \; - \; -").scale(0.9).shift(band_shift(3) + LEFT * 3.4 + UP * 0.3)
        self.play(Create(rod), Write(rod_lab))
        self.wait(1.5)
        sphere = Circle(radius=1.1, color=WHITE).shift(band_shift(3) + RIGHT * 0.8 + UP * 0.3)
        self.play(Create(sphere))
        near = MathTex(r"+\;+").scale(0.9).shift(band_shift(3) + RIGHT * 0.1 + UP * 0.3)
        far = MathTex(r"-\;-").scale(0.9).shift(band_shift(3) + RIGHT * 1.5 + UP * 0.3)
        self.play(Write(near), Write(far))
        b3_l1 = Tex("electrons repelled to the far side").scale(1.0).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        earth = Line(band_shift(3) + RIGHT * 1.9 + UP * 0.3, band_shift(3) + RIGHT * 3.1 + DOWN * 0.5)
        earth_lab = Tex("earth the far side").scale(0.9).shift(band_shift(3) + RIGHT * 3.0 + DOWN * 1.0)
        self.play(Create(earth), Write(earth_lab))
        self.wait(2)
        b3_l2 = Tex("finger away, rod away: sphere left $+$").scale(1.0).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): conservation and the sharing rule ---
        self.next_band(4)
        b4_t = Tex("Identical spheres share the total").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("Charge is conserved — only transferred").scale(1.0).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"Q = \frac{Q_1 + Q_2}{2} \quad \text{(signs included!)}").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"Q = \frac{+5 + (-3)}{2} = \frac{+2}{2}").scale(1.05).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"Q = +1\;\text{nC on each sphere}").scale(1.05).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = Tex("check: $+1 + 1 = +2$ nC, same as before").scale(1.0).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): electrons transferred + the sign trap ---
        self.next_band(5)
        b5_t = Tex("How many electrons moved?").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex(r"A went $+5 \to +1$ nC: gained 4 nC of $-$").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"n = \frac{4 \times 10^{-9}}{1{,}6 \times 10^{-19}}").scale(1.05).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"n = 2{,}5 \times 10^{10} \;\text{electrons, B to A}").scale(1.0).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_l4 = MathTex(r"\frac{5 + 3}{2} = 4\;\text{nC (ignored the signs)}").scale(1.0).shift(band_shift(5) + DOWN * 2.3)
        self.play(Write(b5_l4))
        self.play(Create(strike(b5_l4)))
        self.wait(3)

        # --- Band 6 (subtopic_4): Coulomb's law worked ---
        self.next_band(6)
        b6_t = Tex(r"Coulomb's law: $+3\,\mu$C and $-4\,\mu$C, 0,30 m apart").scale(1.0).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = MathTex(r"F = \frac{k Q_1 Q_2}{r^2}, \quad k = 9 \times 10^9").scale(1.05).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"F = \frac{(9 \times 10^9)(3 \times 10^{-6})(4 \times 10^{-6})}{(0{,}30)^2}").scale(1.0).shift(band_shift(6) + DOWN * 0.2)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"F = \frac{0{,}108}{0{,}09} = 1{,}2\;\text{N}").scale(1.05).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex("unlike charges: ATTRACTION, said in words").scale(1.0).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): inverse square + the named traps ---
        self.next_band(7)
        b7_t = Tex("Double the distance, quarter the force").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = MathTex(r"r = 0{,}60: \;\; F = \frac{0{,}108}{0{,}36} = 0{,}3\;\text{N}").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.play(Create(SurroundingRectangle(b7_l1, color=GREEN)))
        self.wait(2)
        b7_l2 = MathTex(r"F = \frac{0{,}108}{0{,}30} \quad \text{(forgot to square } r)").scale(1.0).shift(band_shift(7) + UP * 0.0)
        self.play(Write(b7_l2))
        self.play(Create(strike(b7_l2)))
        self.wait(2)
        b7_l3 = MathTex(r"r = 30 \quad \text{(cm left in — } 10^4 \text{ too big)}").scale(1.0).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l3))
        self.play(Create(strike(b7_l3)))
        self.wait(2)
        b7_l4 = Tex("magnitudes in, direction in words out").scale(1.0).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the balloon and the jersey ---
        self.next_band(8)
        b8_t = Tex("The balloon and the school jersey").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Rubbing scrapes electrons onto the balloon").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex(r"balloon $-$, jersey $+$: nothing created").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2)
        b8_l3 = Tex("Wall's face turns slightly $+$: balloon sticks").scale(1.0).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("Count charge like coins: whole electrons,").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        b8_l5 = Tex("never two and a half — quantised").scale(1.0).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): three pictures + the taxi fare ---
        self.next_band(9)
        b9_t = Tex("Rub, touch, bring near — then share").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Rub: doorknob shock season").scale(1.0).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(1.5)
        b9_l2 = Tex("Touch: both end up the SAME sign").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l2))
        self.wait(1.5)
        b9_l3 = Tex("Bring near + earth: OPPOSITE sign").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = MathTex(r"\text{Taxi fare: } \frac{+5 + (-3)}{2} = +1 \text{ each}").scale(1.0).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = MathTex(r"\frac{5 + 3}{2} = 4 \quad \text{(charge from nowhere!)}").scale(1.0).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l5))
        self.play(Create(strike(b9_l5)))
        self.wait(3)

        # --- Band 10 (subtopic_7): close is strong ---
        self.next_band(10)
        b10_t = Tex("Close is strong").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex(r"$2\times$ the distance $\Rightarrow$ $\tfrac{1}{4}$ the force").scale(1.05).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = Tex("like heat from a fire — it spreads out").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = MathTex(r"30\;\text{cm} = 0{,}30\;\text{m BEFORE squaring}").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = MathTex(r"F = \frac{0{,}108}{0{,}09} = 1{,}2\;\text{N, attraction}").scale(1.0).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = MathTex(r"\text{at } 0{,}60\;\text{m}: \; \frac{0{,}108}{0{,}36} = 0{,}3\;\text{N}").scale(1.0).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10_l5))
        self.wait(4)
