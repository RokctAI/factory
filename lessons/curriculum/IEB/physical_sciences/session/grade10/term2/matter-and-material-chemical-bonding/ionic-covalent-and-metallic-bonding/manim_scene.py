# Copyright (c) 2026 RokctAI
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

# Band-layout whiteboard scene for "Ionic, Covalent and Metallic Bonding"
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe mobjects only; write-only reveals; camera moves down band by
# band. Band time apportioned to subtopics.json
# (235/235/240/240/185/185/185 of 1505 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class BondingSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): why atoms bond ---
        title = Tex("Ionic, Covalent and Metallic Bonding").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Every bond has one goal:").scale(1.0).shift(UP * 1.0)
        b0_l2 = Tex("a FULL outer energy level — noble-gas stability").scale(0.95).shift(UP * 0.2)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(2.5)
        b0_l3 = Tex("octet of eight for most; two for the smallest").scale(0.9).shift(DOWN * 0.8)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("only VALENCE electrons take part").scale(0.95).shift(DOWN * 1.7)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): Lewis dots drawn + the three strategies ---
        self.next_band(1)
        b1_t = Tex("Lewis diagrams: dots for hooks").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        # carbon with four single dots
        b1_c = Tex("C").scale(1.2).shift(band_shift(1) + UP * 0.9 + LEFT * 2.5)
        d1 = Dot(b1_c.get_center() + UP * 0.5, radius=0.05)
        d2 = Dot(b1_c.get_center() + DOWN * 0.5, radius=0.05)
        d3 = Dot(b1_c.get_center() + LEFT * 0.5, radius=0.05)
        d4 = Dot(b1_c.get_center() + RIGHT * 0.5, radius=0.05)
        self.play(Write(b1_c), Create(d1), Create(d2), Create(d3), Create(d4))
        b1_lbl1 = Tex("four hooks").scale(0.7).shift(band_shift(1) + UP * 0.0 + LEFT * 2.5)
        self.play(Write(b1_lbl1))
        self.wait(2)
        # fluorine: three pairs + one single (drawn simplified as dots)
        b1_f = Tex("F").scale(1.2).shift(band_shift(1) + UP * 0.9 + RIGHT * 2.0)
        f1 = Dot(b1_f.get_center() + UP * 0.5 + LEFT * 0.08, radius=0.05)
        f2 = Dot(b1_f.get_center() + UP * 0.5 + RIGHT * 0.08, radius=0.05)
        f3 = Dot(b1_f.get_center() + LEFT * 0.5 + UP * 0.08, radius=0.05)
        f4 = Dot(b1_f.get_center() + LEFT * 0.5 + DOWN * 0.08, radius=0.05)
        f5 = Dot(b1_f.get_center() + DOWN * 0.5 + LEFT * 0.08, radius=0.05)
        f6 = Dot(b1_f.get_center() + DOWN * 0.5 + RIGHT * 0.08, radius=0.05)
        f7 = Dot(b1_f.get_center() + RIGHT * 0.5, radius=0.05)
        self.play(Write(b1_f), Create(f1), Create(f2), Create(f3), Create(f4), Create(f5), Create(f6), Create(f7))
        b1_lbl2 = Tex("one hook").scale(0.7).shift(band_shift(1) + UP * 0.0 + RIGHT * 2.0)
        self.play(Write(b1_lbl2))
        self.wait(2)
        b1_l1 = Tex("share (covalent); transfer (ionic); pool (metallic)").scale(0.85).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_l1))
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): covalent single bonds, water drawn ---
        self.next_band(2)
        b2_t = Tex("Covalent: sharing pairs").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        # water sketch: O centre, two H, bond lines
        o = Tex("O").scale(1.1).shift(band_shift(2) + UP * 0.8)
        h1 = Tex("H").scale(0.9).shift(band_shift(2) + UP * 0.2 + LEFT * 1.2)
        h2 = Tex("H").scale(0.9).shift(band_shift(2) + UP * 0.2 + RIGHT * 1.2)
        bd1 = Line(o.get_center() + LEFT * 0.3 + DOWN * 0.15, h1.get_center() + RIGHT * 0.2 + UP * 0.1, color=BLUE)
        bd2 = Line(o.get_center() + RIGHT * 0.3 + DOWN * 0.15, h2.get_center() + LEFT * 0.2 + UP * 0.1, color=BLUE)
        self.play(Write(o), Write(h1), Write(h2))
        self.play(Create(bd1), Create(bd2))
        b2_lbl = Tex("water: two single bonds, two lone pairs on O").scale(0.8).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_lbl))
        self.wait(2)
        b2_l1 = Tex("each shared pair counts for BOTH atoms").scale(0.9).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): double and triple bonds, naming ---
        self.next_band(3)
        b3_t = Tex("Double and triple bonds").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex(r"O$_2$: two shared pairs — a double bond").scale(0.95).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex(r"N$_2$: three shared pairs — the mighty triple").scale(0.95).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("that triple is why nitrogen in the air barely reacts").scale(0.85).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("naming by prefixes: carbon DIoxide, DInitrogen TETRoxide").scale(0.8).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): the ionic transfer, NaCl ---
        self.next_band(4)
        b4_t = Tex("Ionic: transfer, then attraction").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex(r"Na gives its one outer electron $\to$ Na$^{+}$").scale(0.95).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex(r"Cl receives it $\to$ Cl$^{-}$ with a full octet").scale(0.95).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex("the BOND is the plus-minus attraction,").scale(0.95).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = Tex("not the handover itself").scale(0.95).shift(band_shift(4) + DOWN * 1.4)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): charges and formulae balanced to zero ---
        self.next_band(5)
        b5_t = Tex("Balance every formula to zero").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("group 1: $+1$; group 2: $+2$; group 16: $-2$; group 17: $-1$").scale(0.8).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex(r"LiF: $+1-1$; MgCl$_2$: $+2$ against two $-1$'s").scale(0.85).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex(r"Na$_2$O: two $+1$'s settle one $-2$ —").scale(0.9).shift(band_shift(5) + DOWN * 0.6)
        b5_l4 = Tex("the subscript lands on the METAL").scale(0.9).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_3): the crystal lattice, drawn ---
        self.next_band(6)
        b6_t = Tex("No molecules — a lattice").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        # 3x3 alternating grid of + and - dots
        for i in range(3):
            for j in range(3):
                p = band_shift(6) + UP * (0.9 - i * 0.8) + LEFT * (1.0 - j * 1.0)
                if (i + j) % 2 == 0:
                    self.play(Write(Tex("+").scale(0.8).move_to(p)), run_time=0.3)
                else:
                    self.play(Write(Tex("--").scale(0.6).move_to(p)), run_time=0.3)
        b6_l1 = Tex("every + ringed by $-$'s, attraction in all directions").scale(0.8).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex("hence: high melting point, brittle, conducts only freed").scale(0.8).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l2))
        self.wait(3)

        # --- Band 7 (subtopic_4): metallic bonding, the sea drawn ---
        self.next_band(7)
        b7_t = Tex("Metallic: kernels in an electron sea").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        for j in range(4):
            p = band_shift(7) + UP * 0.9 + LEFT * (1.5 - j * 1.0)
            self.play(Create(Circle(radius=0.25, color=YELLOW).move_to(p)), run_time=0.3)
        for k in range(6):
            p = band_shift(7) + UP * 0.3 + LEFT * (1.8 - k * 0.7) + DOWN * (0.2 * (k % 2))
            self.play(Create(Dot(p, radius=0.05, color=BLUE)), run_time=0.2)
        b7_l1 = Tex("positive ions fixed; electrons delocalised — the sea").scale(0.8).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l1))
        self.play(Create(SurroundingRectangle(b7_l1, color=GREEN)))
        self.wait(2)
        b7_l2 = Tex("sea explains: conduction, bending, shine").scale(0.85).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l2))
        self.wait(3)

        # --- Band 8 (subtopic_4): formula masses, subscripts honoured ---
        self.next_band(8)
        b8_t = Tex("Formula masses, subscripts honoured").scale(1.05).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(1.5)
        b8_l1 = Tex(r"CH$_4$: $12 + 4 = 16$; \quad HCl: $1 + 35{,}5 = 36{,}5$").scale(0.85).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex(r"KBr: $39 + 80 = 119$").scale(0.9).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex(r"MgCl$_2$: $24 + 2 \times 35{,}5 = 95$").scale(0.9).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex(r"Na$_2$O: $2 \times 23 + 16 = 62$ — the two on the METAL").scale(0.85).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): share the data, swap the chairs ---
        self.next_band(9)
        b9_t = Tex("Share the data, swap the chairs").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("covalent = one data bundle, both phones run on it").scale(0.85).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("ionic = the chair given away; plus and minus").scale(0.85).shift(band_shift(9) + UP * 0.3)
        b9_l3 = Tex("badges attract — THAT is the bond").scale(0.85).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex("two non-metals share; metal + non-metal swap").scale(0.85).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9_l4))
        self.wait(3)

        # --- Band 10 (subtopic_6): the salt grid and the electron sea ---
        self.next_band(10)
        b10_t = Tex("The salt grid and the electron sea").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("ions stack millions deep — no couples, a grid").scale(0.85).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = Tex("grid: hard to melt, shatters, NaCl is a recipe ratio").scale(0.8).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("metals: electrons in one communal pot — the sea").scale(0.8).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex("sea flows: conduction, bending, shine").scale(0.85).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_7): weighing the recipe ---
        self.next_band(11)
        b11_t = Tex("Weighing the recipe").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(2)
        b11_l1 = Tex("periodic table = the price list, mass per atom").scale(0.85).shift(band_shift(11) + UP * 1.2)
        self.play(Write(b11_l1))
        self.wait(2)
        b11_l2 = Tex(r"KBr: $39 + 80 = 119$; MgCl$_2$: $24 + 71 = 95$").scale(0.85).shift(band_shift(11) + UP * 0.3)
        self.play(Write(b11_l2))
        self.wait(2)
        b11_l3 = Tex(r"Na$_2$O: $46 + 16 = 62$ — inventory before adding").scale(0.85).shift(band_shift(11) + DOWN * 0.6)
        self.play(Write(b11_l3))
        self.wait(2)
        b11_l4 = Tex("inventory, multiply, add — three beats every time").scale(0.85).shift(band_shift(11) + DOWN * 1.5)
        self.play(Write(b11_l4))
        self.play(Create(SurroundingRectangle(b11_l4, color=GREEN)))
        self.wait(4)
