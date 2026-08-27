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

# Band-layout whiteboard scene for the functional groups and IUPAC naming
# session duo. Covers all seven subtopics (Part 1 Expert: 1-4, Part 2
# Simplifier: 5-7), band time proportional to subtopics.json
# (235/245/250/230/190/195/190 of 1535 s). Add-only lifecycle; the
# 2-methylpentane skeleton is hand-built from Tex atoms and Line bonds
# (exporter-safe primitives only).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FunctionalGroupsIupacNamingSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the vocabulary ---
        title = Tex("Organic Chemistry: The Vocabulary").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Carbon: exactly FOUR bonds, no exceptions").scale(1.0).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.play(Create(SurroundingRectangle(b0_l1, color=GREEN)))
        self.wait(2)
        b0_l2 = Tex("Hydrocarbon: only C and H atoms").scale(1.0).shift(UP * 0.2)
        b0_l3 = Tex("Functional group: bond/atom/group that").scale(1.0).shift(DOWN * 0.6)
        b0_l4 = Tex("sets the properties of a family").scale(1.0).shift(DOWN * 1.3)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(1.5)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex(r"Homologous series: one general formula,").scale(1.0).shift(DOWN * 2.2)
        b0_l6 = Tex(r"neighbours differ by one $CH_2$ unit").scale(1.0).shift(DOWN * 2.9)
        self.play(Write(b0_l5))
        self.wait(1.5)
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_1): saturation, and three formula types ---
        self.next_band(1)
        b1_l1 = Tex("Saturated: only C--C single bonds").scale(1.05).shift(band_shift(1) + UP * 2.2)
        b1_l2 = Tex("Unsaturated: a double or triple C--C bond").scale(1.0).shift(band_shift(1) + UP * 1.4)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"\text{Molecular: } C_5H_{12} \text{ — a census only}").scale(1.0).shift(band_shift(1) + UP * 0.3)
        b1_l4 = MathTex(r"\text{Condensed: } CH_3CH_2CH_2CH_2CH_3").scale(1.0).shift(band_shift(1) + DOWN * 0.6)
        b1_l5 = Tex("Structural: EVERY atom and bond shown").scale(1.0).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2)
        self.play(Write(b1_l5))
        self.wait(2)
        b1_l6 = Tex("Asked 'structural', answered condensed: no credit").scale(0.9).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): the first five families ---
        self.next_band(2)
        b2_t = Tex("Nine families, part one").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = MathTex(r"\text{Alkanes: } C_nH_{2n+2}, \text{ -ane}").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = MathTex(r"\text{Alkenes: } C_nH_{2n}, \text{ -ene (C=C)}").scale(1.0).shift(band_shift(2) + UP * 0.3)
        b2_l3 = MathTex(r"\text{Alkynes: } C_nH_{2n-2}, \text{ -yne (C}\equiv\text{C)}").scale(1.0).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("Alcohols: --OH on a chain carbon, -anol").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        b2_l5 = Tex("Haloalkanes: fluoro-, chloro-, bromo-, iodo-").scale(0.95).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l4))
        self.wait(2)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): the four carbonyl families ---
        self.next_band(3)
        b3_t = Tex("Four families carry C=O").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_l1 = Tex("Aldehyde: C=O at the END, -al (butanal)").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("Ketone: C=O INSIDE, -one (butanone)").scale(0.95).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("Carboxylic acid: --COOH, -anoic acid").scale(0.95).shift(band_shift(3) + DOWN * 0.6)
        b3_l4 = Tex("Ester: chain--COO--chain (methyl propanoate)").scale(0.95).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("Opening move, always: find the group").scale(0.95).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the four steps, and 2-methylpentane ---
        self.next_band(4)
        b4_t = Tex("IUPAC naming: four fixed steps").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_l1 = Tex("1. Longest chain with the group — root").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex("2. Number: lowest to the functional group").scale(0.95).shift(band_shift(4) + UP * 0.5)
        b4_l3 = Tex("3. Substituents + position numbers").scale(0.95).shift(band_shift(4) + DOWN * 0.2)
        b4_l4 = Tex("4. Assemble alphabetically, di/tri").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l1))
        self.wait(1.5)
        self.play(Write(b4_l2))
        self.wait(1.5)
        self.play(Write(b4_l3))
        self.wait(1.5)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex("Five-carbon chain, methyl on carbon 2:").scale(1.0).shift(band_shift(4) + DOWN * 1.8)
        b4_l6 = Tex("2-methylpentane (never 4- from the far end)").scale(1.0).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l5))
        self.wait(2)
        self.play(Write(b4_l6))
        self.play(Create(SurroundingRectangle(b4_l6, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): named examples, both directions ---
        self.next_band(5)
        b5_l1 = Tex("OH on carbon 2 of four: butan-2-ol").scale(1.0).shift(band_shift(5) + UP * 2.2)
        b5_l2 = Tex("(on the end carbon: butan-1-ol — different!)").scale(0.9).shift(band_shift(5) + UP * 1.4)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("Double bond outranks the branch:").scale(1.0).shift(band_shift(5) + UP * 0.4)
        b5_l4 = Tex("4-methylpent-2-ene").scale(1.1).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l3))
        self.wait(1.5)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("Two bromines: 1,2-dibromopropane").scale(1.0).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l5))
        self.wait(2)
        b5_l6 = Tex("Reverse: 2-chloropentane — five carbons,").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        b5_l7 = Tex("Cl on carbon 2, then audit four bonds each").scale(0.95).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l6))
        self.wait(1.5)
        self.play(Write(b5_l7))
        self.wait(3)

        # --- Band 6 (subtopic_4): the three kinds of isomer ---
        self.next_band(6)
        b6_t = Tex("Isomers: same formula, different molecule").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = MathTex(r"\text{Chain: } C_5H_{12} = \text{pentane or 2,2-dimethylpropane}").scale(0.85).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex("Positional: pentan-1-ol vs pentan-2-ol").scale(0.95).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"\text{Functional: butanal / butanone } (C_4H_8O)").scale(0.9).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_wrong = Tex("A bent drawing of hexane = an isomer?").scale(0.95).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_wrong))
        self.play(Create(strike(b6_wrong)))
        self.wait(2)
        b6_l4 = Tex("Only changing WHO BONDS TO WHOM counts").scale(0.95).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_l4))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): the address system ---
        self.next_band(7)
        b7_t = Tex("A surname, a first name, a house number").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("Suffix = family surname: -ane, -anol, -anoic").scale(0.95).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("Middle = street length: meth 1, eth 2,").scale(0.95).shift(band_shift(7) + UP * 0.3)
        b7_l3 = Tex("prop 3, but 4, pent, hex, hept, oct").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(b7_l2))
        self.wait(1.5)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("Numbers = house numbers; the functional").scale(0.95).shift(band_shift(7) + DOWN * 1.3)
        b7_l5 = Tex("group takes the LOWEST one available").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l4))
        self.wait(1.5)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(2)
        b7_l6 = Tex("Prefixes = lodgers: methyl, ethyl, chloro...").scale(0.95).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(b7_l6))
        self.wait(3)

        # --- Band 8 (subtopic_6): four hands — build 2-methylpentane ---
        self.next_band(8)
        b8_t = Tex("Carbon has four hands: build 2-methylpentane").scale(1.0).shift(band_shift(8) + UP * 2.6)
        self.play(Write(b8_t))
        self.wait(2)
        # skeleton: five Tex C atoms joined by Line bonds, methyl branch on C2
        base = band_shift(8) + LEFT * 3.8 + UP * 0.6
        c1 = MathTex(r"C").scale(1.1).move_to(base)
        c2 = MathTex(r"C").scale(1.1).move_to(base + RIGHT * 1.6)
        c3 = MathTex(r"C").scale(1.1).move_to(base + RIGHT * 3.2)
        c4 = MathTex(r"C").scale(1.1).move_to(base + RIGHT * 4.8)
        c5 = MathTex(r"C").scale(1.1).move_to(base + RIGHT * 6.4)
        bond1 = Line(base + RIGHT * 0.35, base + RIGHT * 1.25)
        bond2 = Line(base + RIGHT * 1.95, base + RIGHT * 2.85)
        bond3 = Line(base + RIGHT * 3.55, base + RIGHT * 4.45)
        bond4 = Line(base + RIGHT * 5.15, base + RIGHT * 6.05)
        self.play(Write(c1), Write(c2), Write(c3), Write(c4), Write(c5))
        self.play(Create(bond1), Create(bond2), Create(bond3), Create(bond4))
        self.wait(2)
        cm = MathTex(r"CH_3").scale(0.95).move_to(base + RIGHT * 1.6 + UP * 1.3)
        bondm = Line(base + RIGHT * 1.6 + UP * 0.35, base + RIGHT * 1.6 + UP * 0.9)
        self.play(Create(bondm), Write(cm))
        self.wait(2)
        b8_l1 = Tex("Pass 3: fill every spare hand with H").scale(0.95).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"C_6H_{14}, \text{ four bonds per C} \; \checkmark").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2)
        b8_l3 = Tex("A five-handed carbon = an alarm bell").scale(0.95).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_l3))
        self.wait(3)

        # --- Band 9 (subtopic_7): spot the twins ---
        self.next_band(9)
        b9_t = Tex("Spot the twins").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Same bricks, three different buildings:").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l2 = MathTex(r"C_5H_{12}: \text{ pentane, 2-methylbutane, ...}").scale(0.95).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.wait(1.5)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("Three twin types: rebuild the skeleton,").scale(0.95).shift(band_shift(9) + DOWN * 0.6)
        b9_l4 = Tex("move the house number, switch the family").scale(0.95).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l3))
        self.wait(1.5)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("A bent photograph is NOT a twin —").scale(1.0).shift(band_shift(9) + DOWN * 2.2)
        b9_l6 = Tex("only a moved bond makes a new molecule").scale(1.0).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l5))
        self.wait(1.5)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(4)
