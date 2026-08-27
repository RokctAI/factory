# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from manim import *

# Band-layout whiteboard scene for the ionic-covalent-and-metallic-bonding
# session duo (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe vocabulary only (Tex/MathTex, Line/Arrow, Dot, Circle,
# Rectangle/SurroundingRectangle, VGroup); add-only lifecycle; band k sits
# one frame-height below band k-1 and the camera moves between bands.
# Time apportioned to subtopics.json (235/235/240/240/185/185/185 of 1505 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class IonicCovalentMetallicBondingSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): why atoms bond ---
        title = Tex("Ionic, Covalent and Metallic Bonding").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        a1 = Tex("A bond = a force holding atoms together").scale(1.05).shift(UP * 1.0)
        self.play(Write(a1))
        self.wait(2)
        a2 = Tex("Goal: a FULL outer level (noble gas)").scale(1.05).shift(UP * 0.1)
        self.play(Write(a2))
        self.wait(2)
        a3 = Tex("Octet: 8 electrons; H wants 2 (He)").scale(1.05).shift(DOWN * 0.8)
        self.play(Write(a3))
        self.wait(2)
        a4 = Tex("Only VALENCE electrons take part").scale(1.05).shift(DOWN * 1.7)
        self.play(Write(a4))
        self.wait(2)
        a5 = Tex("Lewis diagram: symbol + valence dots").scale(1.05).shift(DOWN * 2.6)
        self.play(Write(a5))
        self.wait(3)

        # --- Band 1 (subtopic_1): Lewis dots drawn + the three strategies ---
        self.next_band(1)
        b1_t = Tex("Dots = group's valence count").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        # Carbon: 4 single dots (4 hooks)
        cC = band_shift(1) + UP * 0.9 + LEFT * 3.4
        symC = Tex("C").scale(1.3).move_to(cC)
        dotsC = VGroup(Dot(cC + UP * 0.5), Dot(cC + DOWN * 0.5),
                       Dot(cC + LEFT * 0.5), Dot(cC + RIGHT * 0.5))
        labC = Tex("4 hooks").scale(0.8).move_to(cC + DOWN * 1.1)
        self.play(Write(symC))
        self.play(Create(dotsC), Write(labC))
        self.wait(2)
        # Oxygen: 2 pairs + 2 singles (2 hooks)
        cO = band_shift(1) + UP * 0.9
        symO = Tex("O").scale(1.3).move_to(cO)
        dotsO = VGroup(Dot(cO + UP * 0.5 + LEFT * 0.12), Dot(cO + UP * 0.5 + RIGHT * 0.12),
                       Dot(cO + LEFT * 0.5 + UP * 0.12), Dot(cO + LEFT * 0.5 + DOWN * 0.12),
                       Dot(cO + DOWN * 0.5), Dot(cO + RIGHT * 0.5))
        labO = Tex("2 hooks").scale(0.8).move_to(cO + DOWN * 1.1)
        self.play(Write(symO))
        self.play(Create(dotsO), Write(labO))
        self.wait(2)
        # Chlorine: 3 pairs + 1 single (1 hook)
        cL = band_shift(1) + UP * 0.9 + RIGHT * 3.4
        symL = Tex("Cl").scale(1.3).move_to(cL)
        dotsL = VGroup(Dot(cL + UP * 0.55 + LEFT * 0.12), Dot(cL + UP * 0.55 + RIGHT * 0.12),
                       Dot(cL + LEFT * 0.6 + UP * 0.12), Dot(cL + LEFT * 0.6 + DOWN * 0.12),
                       Dot(cL + DOWN * 0.55 + LEFT * 0.12), Dot(cL + DOWN * 0.55 + RIGHT * 0.12),
                       Dot(cL + RIGHT * 0.6))
        labL = Tex("1 hook").scale(0.8).move_to(cL + DOWN * 1.1)
        self.play(Write(symL))
        self.play(Create(dotsL), Write(labL))
        self.wait(2.5)
        b1_1 = Tex("Non-metal + non-metal: SHARE").scale(1.0).shift(band_shift(1) + DOWN * 1.1)
        b1_2 = Tex("Metal + non-metal: TRANSFER").scale(1.0).shift(band_shift(1) + DOWN * 1.9)
        b1_3 = Tex("Metal alone: pool an electron sea").scale(1.0).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_1))
        self.wait(1.5)
        self.play(Write(b1_2))
        self.wait(1.5)
        self.play(Write(b1_3))
        self.wait(3)

        # --- Band 2 (subtopic_2): covalent single bonds, water drawn ---
        self.next_band(2)
        b2_t = Tex("Covalent: sharing pairs").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_1 = Tex("Shared pair = one bond, counted by both").scale(1.0).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_1))
        self.wait(2)
        # Water Lewis: H - O - H with bonding pairs and two lone pairs
        w = band_shift(2) + UP * 0.0
        wO = Tex("O").scale(1.3).move_to(w)
        wH1 = Tex("H").scale(1.2).move_to(w + LEFT * 1.4)
        wH2 = Tex("H").scale(1.2).move_to(w + RIGHT * 1.4)
        pair1 = VGroup(Dot(w + LEFT * 0.7 + UP * 0.12), Dot(w + LEFT * 0.7 + DOWN * 0.12))
        pair2 = VGroup(Dot(w + RIGHT * 0.7 + UP * 0.12), Dot(w + RIGHT * 0.7 + DOWN * 0.12))
        lone = VGroup(Dot(w + UP * 0.5 + LEFT * 0.12), Dot(w + UP * 0.5 + RIGHT * 0.12),
                      Dot(w + DOWN * 0.5 + LEFT * 0.12), Dot(w + DOWN * 0.5 + RIGHT * 0.12))
        wlab = Tex(r"H$_2$O: two single bonds, two lone pairs").scale(0.95).move_to(w + DOWN * 1.2)
        self.play(Write(wO), Write(wH1), Write(wH2))
        self.play(Create(pair1), Create(pair2))
        self.wait(1.5)
        self.play(Create(lone))
        self.play(Write(wlab))
        self.wait(2.5)
        b2_2 = Tex(r"NH$_3$: 3 bonds, 1 lone pair").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
        b2_3 = Tex(r"CH$_4$: 4 bonds, no lone pairs").scale(1.0).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_2))
        self.wait(1.5)
        self.play(Write(b2_3))
        self.wait(3)

        # --- Band 3 (subtopic_2): double and triple bonds, naming ---
        self.next_band(3)
        b3_t = Tex("Double and triple bonds").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_1 = Tex(r"O$_2$: each O needs 2 more").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_1))
        self.wait(1.5)
        b3_2 = Tex(r"share TWO pairs — a DOUBLE bond").scale(1.05).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_2))
        self.wait(2)
        b3_3 = Tex(r"N$_2$: share THREE pairs — TRIPLE bond").scale(1.05).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_3))
        self.wait(2)
        b3_4 = Tex("(so nitrogen gas barely reacts)").scale(0.95).shift(band_shift(3) + DOWN * 1.4)
        self.play(Write(b3_4))
        self.wait(2)
        b3_5 = Tex("Prefixes: carbon DIoxide, carbon MONoxide").scale(0.95).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(b3_5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the ionic transfer, NaCl ---
        self.next_band(4)
        b4_t = Tex("Ionic: transfer, then attraction").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        n = band_shift(4) + UP * 0.8
        nNa = Tex("Na").scale(1.2).move_to(n + LEFT * 2.8)
        nNadot = Dot(n + LEFT * 2.8 + RIGHT * 0.6)
        nCl = Tex("Cl").scale(1.2).move_to(n + RIGHT * 1.6)
        nCldots = VGroup(Dot(n + RIGHT * 1.6 + UP * 0.5 + LEFT * 0.12), Dot(n + RIGHT * 1.6 + UP * 0.5 + RIGHT * 0.12),
                         Dot(n + RIGHT * 1.6 + DOWN * 0.5 + LEFT * 0.12), Dot(n + RIGHT * 1.6 + DOWN * 0.5 + RIGHT * 0.12),
                         Dot(n + RIGHT * 2.2 + UP * 0.12), Dot(n + RIGHT * 2.2 + DOWN * 0.12),
                         Dot(n + RIGHT * 1.0))
        tarrow = Arrow(n + LEFT * 1.9, n + RIGHT * 0.5, buff=0)
        tlab = Tex("electron transferred").scale(0.85).move_to(n + DOWN * 1.0 + LEFT * 0.6)
        self.play(Write(nNa), Create(nNadot))
        self.play(Write(nCl), Create(nCldots))
        self.wait(1.5)
        self.play(Create(tarrow), Write(tlab))
        self.wait(2)
        b4_1 = MathTex(r"\text{Na}^{+} \text{(neon)}, \quad \text{Cl}^{-} \text{(argon)}").scale(1.05).shift(band_shift(4) + DOWN * 1.0)
        self.play(Write(b4_1))
        self.wait(2.5)
        b4_2 = Tex("The bond = attraction of $+$ and $-$").scale(1.05).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_2))
        self.play(Create(SurroundingRectangle(b4_2, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): charges and formulae balanced to zero ---
        self.next_band(5)
        b5_t = Tex("Balance charge to zero").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_1 = Tex("Group 1: $+1$; group 2: $+2$").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_2 = Tex("group 16: $-2$; group 17: $-1$").scale(1.05).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_1))
        self.wait(1.5)
        self.play(Write(b5_2))
        self.wait(2)
        b5_3 = MathTex(r"\text{K}^{+} + \text{Cl}^{-} \Rightarrow \text{KCl}").scale(1.05).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_3))
        self.wait(2)
        b5_4 = MathTex(r"\text{Ca}^{2+} + 2\,\text{Cl}^{-} \Rightarrow \text{CaCl}_2").scale(1.05).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_4))
        self.wait(2)
        b5_5 = MathTex(r"\text{Mg}^{2+} + 2\,\text{Br}^{-} \Rightarrow \text{MgBr}_2").scale(1.05).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_5))
        self.play(Create(SurroundingRectangle(b5_5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_3): the crystal lattice, drawn ---
        self.next_band(6)
        b6_t = Tex("No molecules — a giant lattice").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        g = band_shift(6) + UP * 0.3
        ions = VGroup()
        for i in range(3):
            for j in range(3):
                pos = g + RIGHT * (j - 1) * 1.1 + UP * (1 - i) * 1.1
                ring = Circle(radius=0.4).move_to(pos)
                sign = Tex("$+$" if (i + j) % 2 == 0 else "$-$").scale(0.9).move_to(pos)
                ions.add(VGroup(ring, sign))
        for k in range(9):
            self.play(Create(ions[k]), run_time=0.4)
        self.wait(2)
        b6_1 = Tex("NaCl = a FORMULA UNIT (1:1 ratio)").scale(1.0).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_1))
        self.wait(2)
        b6_2 = Tex("High melting point; brittle;").scale(1.0).shift(band_shift(6) + DOWN * 2.4)
        b6_3 = Tex("conducts only molten or dissolved").scale(1.0).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_2))
        self.play(Write(b6_3))
        self.wait(3)

        # --- Band 7 (subtopic_4): metallic bonding, the sea drawn ---
        self.next_band(7)
        b7_t = Tex("Metallic: ions in an electron sea").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        m = band_shift(7) + UP * 0.6
        kernels = VGroup()
        for i in range(2):
            for j in range(4):
                pos = m + RIGHT * (j - 1.5) * 1.4 + DOWN * i * 1.1
                kernels.add(VGroup(Circle(radius=0.35).move_to(pos),
                                   Tex("$+$").scale(0.8).move_to(pos)))
        self.play(Create(kernels))
        self.wait(1.5)
        sea = VGroup(Dot(m + LEFT * 1.4 + UP * 0.55), Dot(m + RIGHT * 0.1 + UP * 0.5),
                     Dot(m + RIGHT * 1.5 + UP * 0.55), Dot(m + LEFT * 0.7 + DOWN * 0.55),
                     Dot(m + RIGHT * 0.7 + DOWN * 0.5), Dot(m + LEFT * 2.1 + DOWN * 0.5),
                     Dot(m + RIGHT * 2.1 + DOWN * 0.55))
        sea_lab = Tex("delocalised electrons").scale(0.9).move_to(m + DOWN * 1.5)
        self.play(Create(sea), Write(sea_lab))
        self.wait(2.5)
        b7_1 = Tex("Mobile sea: conducts charge and heat").scale(1.0).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_1))
        self.wait(2)
        b7_2 = Tex("Sea flows when layers slide: bends,").scale(1.0).shift(band_shift(7) + DOWN * 2.4)
        b7_3 = Tex("never shatters; and it gives the shine").scale(1.0).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_2))
        self.play(Write(b7_3))
        self.wait(3)

        # --- Band 8 (subtopic_4): formula masses, subscripts honoured ---
        self.next_band(8)
        b8_t = Tex("Relative molecular / formula mass").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(1.5)
        b8_1 = MathTex(r"\text{H}_2\text{O}: 2(1) + 16 = 18").scale(1.05).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_1))
        self.wait(2)
        b8_2 = MathTex(r"\text{CO}_2: 12 + 2(16) = 44, \quad \text{NH}_3: 17").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_2))
        self.wait(2)
        b8_3 = MathTex(r"\text{NaCl}: 23 + 35{,}5 = 58{,}5").scale(1.05).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_3))
        self.wait(2)
        b8_trap = MathTex(r"\text{CaCl}_2: 40 + 35{,}5 \; \text{(one Cl?!)}").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_trap))
        self.play(Create(strike(b8_trap)))
        self.wait(2)
        b8_4 = MathTex(r"\text{CaCl}_2: 40 + 2(35{,}5) = 111").scale(1.05).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_4))
        self.play(Create(SurroundingRectangle(b8_4, color=GREEN)))
        self.wait(2)
        b8_5 = MathTex(r"\text{MgBr}_2: 24 + 2(80) = 184").scale(1.05).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): share the data, swap the chairs ---
        self.next_band(9)
        b9_t = Tex("Share the data, swap the chairs").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_1 = Tex("Every atom wants a FULL outer shelf").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_1))
        self.wait(2)
        b9_2 = Tex("Share: one data bundle, both count it").scale(1.0).shift(band_shift(9) + UP * 0.2)
        b9_3 = Tex("= covalent (two non-metals)").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_2))
        self.wait(2)
        self.play(Write(b9_3))
        self.wait(2)
        b9_4 = Tex("Swap: Na gives its chair to Cl").scale(1.0).shift(band_shift(9) + DOWN * 1.5)
        b9_5 = Tex("$+$ badge meets $-$ badge = ionic").scale(1.0).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9_4))
        self.wait(2)
        self.play(Write(b9_5))
        self.play(Create(SurroundingRectangle(b9_5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_6): the salt grid and the electron sea ---
        self.next_band(10)
        b10_t = Tex("The salt grid and the electron sea").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_1 = Tex("Ions stack: every $+$ ringed by $-$").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_1))
        self.wait(2)
        b10_2 = Tex("Hard to melt, shatters when hit").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_2))
        self.wait(2)
        b10_3 = Tex(r"CaCl$_2$: a $2+$ needs two $1-$ chlorides").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_3))
        self.wait(2)
        b10_4 = Tex("Metals: electrons in one communal pot").scale(1.0).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10_4))
        self.wait(2)
        b10_5 = Tex("Sea wiggles: conducts; flows: bends").scale(1.0).shift(band_shift(10) + DOWN * 2.4)
        self.play(Write(b10_5))
        self.play(Create(SurroundingRectangle(b10_5, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_7): weighing the recipe ---
        self.next_band(11)
        b11_t = Tex("Weighing the recipe").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(2)
        b11_1 = Tex("Inventory, multiply, add").scale(1.05).shift(band_shift(11) + UP * 1.2)
        self.play(Write(b11_1))
        self.wait(2)
        b11_2 = MathTex(r"\text{H}_2\text{O}: 2 + 16 = 18, \quad \text{CO}_2: 44").scale(1.0).shift(band_shift(11) + UP * 0.3)
        self.play(Write(b11_2))
        self.wait(2.5)
        b11_3 = MathTex(r"\text{NaCl}: 23 + 35{,}5 = 58{,}5").scale(1.0).shift(band_shift(11) + DOWN * 0.6)
        self.play(Write(b11_3))
        self.wait(2)
        b11_4 = MathTex(r"\text{CaCl}_2: 40 + 2(35{,}5) = 111").scale(1.05).shift(band_shift(11) + DOWN * 1.5)
        self.play(Write(b11_4))
        self.play(Create(SurroundingRectangle(b11_4, color=GREEN)))
        self.wait(2.5)
        b11_5 = Tex(r"58,5 becomes GRAMS next topic — the mole").scale(0.95).shift(band_shift(11) + DOWN * 2.5)
        self.play(Write(b11_5))
        self.wait(4)
