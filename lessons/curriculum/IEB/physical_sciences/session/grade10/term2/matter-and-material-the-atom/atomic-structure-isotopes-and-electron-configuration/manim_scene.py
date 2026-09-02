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

# Band-layout whiteboard scene for "Atomic Structure, Isotopes and Electron
# Configuration" (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics
# 5-7). Exporter-safe mobjects only; write-only reveals; camera moves down
# band by band. Band time apportioned to subtopics.json
# (230/235/235/245/180/180/190 of 1495 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class AtomicStructureSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the three particles ---
        title = Tex("Atomic Structure and Electron Configuration").scale(1.0).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("proton: charge $+1$, mass 1 — in the nucleus").scale(0.9).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.wait(1.5)
        b0_l2 = Tex("neutron: charge 0, mass 1 — in the nucleus").scale(0.9).shift(UP * 0.2)
        self.play(Write(b0_l2))
        self.wait(1.5)
        b0_l3 = Tex("electron: charge $-1$, mass about $\\frac{1}{2000}$ — around it").scale(0.9).shift(DOWN * 0.6)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("neutral atom: electrons = protons").scale(0.95).shift(DOWN * 1.6)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the atom drawn + neutrality ---
        self.next_band(1)
        b1_t = Tex("Mostly empty space").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        nucleus = Dot(band_shift(1) + DOWN * 0.2, radius=0.12, color=YELLOW)
        ring1 = Circle(radius=0.8, color=BLUE).move_to(band_shift(1) + DOWN * 0.2)
        ring2 = Circle(radius=1.5, color=BLUE).move_to(band_shift(1) + DOWN * 0.2)
        self.play(Create(nucleus))
        self.play(Create(ring1), Create(ring2))
        e1 = Dot(band_shift(1) + DOWN * 0.2 + RIGHT * 0.8, radius=0.06, color=WHITE)
        e2 = Dot(band_shift(1) + DOWN * 0.2 + LEFT * 1.5, radius=0.06, color=WHITE)
        self.play(Create(e1), Create(e2))
        b1_l1 = Tex("gold foil: most particles sail through;").scale(0.85).shift(band_shift(1) + DOWN * 2.0)
        b1_l2 = Tex("rare bounce-backs found the nucleus").scale(0.85).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(3)

        # --- Band 2 (subtopic_2): Z, A and the notation ---
        self.next_band(2)
        b2_t = Tex("Two numbers name the atom").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex("Z = protons — the identity; A = protons + neutrons").scale(0.85).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"^{27}_{13}\mathrm{Al}").scale(1.3).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2)
        b2_l3 = Tex("13 protons; $27 - 13 = 14$ neutrons; 13 electrons").scale(0.85).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.wait(3)

        # --- Band 3 (subtopic_2): ions ---
        self.next_band(3)
        b3_t = Tex("Ions: electrons move, protons never").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex(r"Mg loses two $\to$ Mg$^{2+}$: 12 p, 10 e").scale(0.95).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex(r"O gains two $\to$ O$^{2-}$: 8 p, 10 e").scale(0.95).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("a $2+$ charge means two electrons LOST").scale(0.9).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): isotopes and the weighted average ---
        self.next_band(4)
        b4_t = Tex("Isotopes and the weighted average").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("same protons, different neutrons: B-10 and B-11").scale(0.85).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex("identical electrons — identical chemistry").scale(0.85).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"0{,}2 \times 10 + 0{,}8 \times 11 = 2 + 8{,}8 = 10{,}8").scale(0.95).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        b4_l4 = Tex("close to 11: the heavier isotope dominates").scale(0.85).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_4): levels, orbitals, three rules ---
        self.next_band(5)
        b5_t = Tex("Levels, orbitals, three rules").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("s holds 2; the three p's hold 6; two per orbital").scale(0.85).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex("order: 1s, 2s, 2p, 3s, 3p, then 4s BEFORE 3d").scale(0.85).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2)
        b5_l3 = Tex("Aufbau: lowest first; pairs spin oppositely;").scale(0.85).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex("Hund: spread out singly across the p set").scale(0.85).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): aluminium's diagram + sp notation ---
        self.next_band(6)
        b6_t = Tex("Aluminium, written out").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        # aufbau blocks: 1s 2s 2p 3s 3p as rectangles climbing
        labels = ["1s", "2s", "2p", "3s", "3p"]
        fills = ["2", "2", "6", "2", "1"]
        for i, (lab, fil) in enumerate(zip(labels, fills)):
            pos = band_shift(6) + DOWN * 0.9 + UP * (i * 0.55) + LEFT * 2.5
            self.play(Create(Rectangle(width=0.9, height=0.4, color=BLUE).move_to(pos)), run_time=0.3)
            self.play(Write(Tex(lab + ": " + fil).scale(0.6).move_to(pos + RIGHT * 1.6)), run_time=0.3)
        b6_l1 = MathTex(r"1s^2\,2s^2\,2p^6\,3s^2\,3p^1").scale(1.0).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2)
        b6_l2 = Tex("check: $2+2+6+2+1 = 13 = Z$; K ends 4s$^1$, Ca 4s$^2$").scale(0.75).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l2))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the stadium and the pea ---
        self.next_band(7)
        b7_t = Tex("The stadium and the pea").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("atom = stadium; nucleus = pea on the centre spot").scale(0.85).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("the pea owns the mass and all the plus charge").scale(0.85).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2)
        b7_l3 = Tex("stands: near-empty space, patrolled by electrons").scale(0.85).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("one in thousands bounced back: the pea is real").scale(0.85).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(b7_l4))
        self.wait(3)

        # --- Band 8 (subtopic_6): twins with heavier backpacks ---
        self.next_band(8)
        b8_t = Tex("Twins with heavier backpacks").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("same face and voice: 5 protons, 5 electrons").scale(0.85).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("different backpacks: 5 or 6 neutrons — B-10, B-11").scale(0.85).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("marks arithmetic: $2 + 8{,}8 = 10{,}8$ — nobody weighs that").scale(0.8).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex("average leans to the twin who outnumbers").scale(0.85).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_7): filling the hotel ---
        self.next_band(9)
        b9_t = Tex("Filling the hotel from the ground floor").scale(1.05).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("floors = levels; rooms = orbitals; two guests max").scale(0.85).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("cheapest room first; roommates spin opposite;").scale(0.85).shift(band_shift(9) + UP * 0.4)
        b9_l3 = Tex("strangers spread out before doubling up").scale(0.85).shift(band_shift(9) + DOWN * 0.3)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("aluminium's register: 1s$^2$ 2s$^2$ 2p$^6$ 3s$^2$ 3p$^1$").scale(0.85).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex("top-floor guests do all the chemistry").scale(0.85).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l5))
        self.wait(4)
