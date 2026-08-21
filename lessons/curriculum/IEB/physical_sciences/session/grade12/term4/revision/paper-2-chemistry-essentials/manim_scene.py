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

# Band-layout whiteboard scene for "Paper Two Chemistry Essentials" (Part 1 —
# Expert subtopics 1-4, Part 2 — Simplifier subtopics 5-7).
# Exporter-safe mobjects only, write-only reveals, camera moves between bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class Paper2ChemistryEssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): series and functional groups
        title = Tex("Chemistry Essentials: The Final Sweep").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Nine series, each stamped by its group:").scale(1.0).shift(UP * 1.3)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("ane, ene, yne — the bond family").scale(0.95).shift(UP * 0.5)
        b0_l3 = Tex("ol, al, one, oic acid — the oxygen family").scale(0.95).shift(DOWN * 0.3)
        b0_l4 = Tex("haloalkanes and esters complete the list").scale(0.95).shift(DOWN * 1.1)
        self.play(Write(b0_l2))
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(2.5)
        b0_l5 = Tex(r"Homologous series: one formula, steps of CH$_2$").scale(0.95).shift(DOWN * 2.1)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): naming, isomers, boiling points
        self.next_band(1)
        b1_title = Tex("The algorithm, spoken once").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("5-C chain, OH on C2, methyl on C4:").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex("4-methylpentan-2-ol").scale(1.15).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("Chain: hexane / 2-methylpentane").scale(0.95).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = Tex("Position: propan-1-ol / propan-2-ol").scale(0.95).shift(band_shift(1) + DOWN * 1.4)
        b1_l5 = Tex("Function: propanal / propanone").scale(0.95).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(2.5)
        b1_l6 = Tex("Longer boils higher; branched lower; OH highest").scale(0.95).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): the reaction map
        self.next_band(2)
        b2_title = Tex("Count the bonds first").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Double bond consumed: ADDITION").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("Double bond created: ELIMINATION").scale(1.0).shift(band_shift(2) + UP * 0.4)
        b2_l3 = Tex("Swap on a saturated molecule: SUBSTITUTION").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex("Bromine water: unsaturated decolourises fast").scale(0.95).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): major product and the ester ceremony
        self.next_band(3)
        b3_title = Tex("Major product, and the ester").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("H adds to the C already richer in H:").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("but-1-ene $+$ HBr $\\rightarrow$ 2-bromobutane (major)").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex("Esterification: acid $+$ alcohol, conc. H$_2$SO$_4$, warm").scale(0.95).shift(band_shift(3) + DOWN * 0.6)
        b3_l4 = Tex("propanoic acid $+$ methanol").scale(1.0).shift(band_shift(3) + DOWN * 1.4)
        b3_l5 = Tex("$\\rightarrow$ methyl propanoate $+$ water").scale(1.0).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(2.5)
        b3_l6 = Tex("Alcohol names the first half, acid the second").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): rates and collision theory
        self.next_band(4)
        b4_title = Tex("Collision theory: two levers").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Lever 1: frequency of effective collisions").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex("Lever 2: fraction above the activation energy").scale(1.0).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("Temperature: curve flattens, tail grows").scale(0.95).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex("Catalyst: lower path, curve untouched —").scale(0.95).shift(band_shift(4) + DOWN * 1.3)
        b4_l5 = Tex("the finish line moves, not the runners").scale(0.95).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the RICE table into Kc
        self.next_band(5)
        b5_title = Tex(r"H$_2$ + Br$_2 \rightleftharpoons$ 2HBr in 4 dm$^3$").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"\text{Reacted: } 0{,}6\ \text{each} \Rightarrow 1{,}2\ \text{mol HBr}").scale(0.95).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"[H_2] = 0{,}05,\ [Br_2] = 0{,}05,\ [HBr] = 0{,}3").scale(0.95).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("Divide by the volume BEFORE the constant").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = MathTex(r"K_c = \frac{(0{,}3)^2}{0{,}05 \times 0{,}05} = \frac{0{,}09}{0{,}0025} = 36").scale(1.0).shift(band_shift(5) + DOWN * 1.5)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex("Large $K_c$: equilibrium well towards products").scale(0.95).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): acid-base definitions
        self.next_band(6)
        b6_title = Tex("The acid-base definitions").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Lowry-Brønsted: acid donates a proton,").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("base accepts one; conjugates differ by H$^+$").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("STRONG: fraction ionised — complete").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex("CONCENTRATED: amount dissolved").scale(1.0).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("A dilute STRONG acid is entirely possible").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): pH both ways, and the titration
        self.next_band(7)
        b7_title = Tex("pH logs run both ways").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"\text{HCl } 0{,}001\ \text{M}: pH = -\log 10^{-3} = 3").scale(0.95).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"\text{NaOH } 0{,}001\ \text{M}: [H_3O^+] = 10^{-11},\ pH = 11").scale(0.95).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = MathTex(r"\text{Titration: } n_{base} = 0{,}002,\ \text{ratio } 1:1").scale(0.95).shift(band_shift(7) + DOWN * 0.7)
        b7_l4 = MathTex(r"c_{acid} = \frac{0{,}002}{0{,}020} = 0{,}1\ \text{mol}\cdot\text{dm}^{-3}").scale(0.95).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("Hydrolysis: weak-strong salts tip the pH").scale(0.95).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_4): the two cells
        self.next_band(8)
        b8_title = Tex("Mg-Cu galvanic cell").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = Tex("Mg: stronger reducing agent — the anode").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"E_{cell} = 0{,}34 - (-2{,}36) = 2{,}70\ \text{V}").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex("Positive emf: spontaneous — galvanic").scale(1.0).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("Electrolytic: energy forced in — plating, refining,").scale(0.95).shift(band_shift(8) + DOWN * 1.7)
        b8_l5 = Tex("NaCl electrolysis: Cl$_2$ at anode, H$_2$ at cathode").scale(0.95).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_4): the fixed labels
        self.next_band(9)
        b9_title = Tex("The labels never move").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(1.5)
        b9_l1 = Tex("Oxidation: loss of electrons — at the ANODE").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("Reduction: gain of electrons — at the CATHODE").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("In BOTH cells — only the energy direction changes").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("An ox, red cat — the chant that survives exams").scale(0.95).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 10 (subtopic_5): the family tree and the compass
        self.next_band(10)
        b10_title = Tex("Name tags and the compass").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(1.5)
        b10_l1 = Tex("Surname: the chain — meth, eth, prop, but").scale(0.95).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("First name: the group — ane, ene, ol, oic acid").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Full bus: substitution — swap a passenger").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        b10_l4 = Tex("Folded seats: addition — the bond unfolds").scale(0.95).shift(band_shift(10) + DOWN * 1.2)
        b10_l5 = Tex("Elimination: seats fold back up").scale(0.95).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l3))
        self.wait(2)
        self.play(Write(b10_l4))
        self.wait(2)
        self.play(Write(b10_l5))
        self.wait(2)
        b10_l6 = Tex("Made, filled, or swapped — the type names itself").scale(0.95).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_6): the seesaw and the opponent
        self.next_band(11)
        b11_title = Tex("The seesaw never stops").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(1.5)
        b11_l1 = Tex("Equal RATES at balance — not equal amounts").scale(1.0).shift(band_shift(11) + UP * 1.2)
        self.play(Write(b11_l1))
        self.play(Create(SurroundingRectangle(b11_l1, color=GREEN)))
        self.wait(2.5)
        b11_l2 = Tex("The stubborn opponent leans the other way:").scale(0.95).shift(band_shift(11) + UP * 0.2)
        b11_l3 = Tex("add reactant — tips forward; squeeze — fewer moles;").scale(0.95).shift(band_shift(11) + DOWN * 0.6)
        b11_l4 = Tex("heat — the endothermic direction").scale(0.95).shift(band_shift(11) + DOWN * 1.3)
        self.play(Write(b11_l2))
        self.play(Write(b11_l3))
        self.play(Write(b11_l4))
        self.wait(2.5)
        b11_l5 = Tex("$K_c$ is the factory setting: only temperature").scale(0.95).shift(band_shift(11) + DOWN * 2.2)
        b11_l6 = Tex("reaches into the factory").scale(0.95).shift(band_shift(11) + DOWN * 2.9)
        self.play(Write(b11_l5))
        self.play(Write(b11_l6))
        self.wait(3)

        # --- Band 12 (subtopic_7): the machine and the last audit
        self.next_band(12)
        b12_title = Tex("One machine, two gears — and four traps").scale(1.1).shift(band_shift(12) + UP * 2.4)
        self.play(Write(b12_title))
        self.wait(1.5)
        b12_l1 = Tex("Forward: galvanic — chemistry pushes electrons").scale(0.95).shift(band_shift(12) + UP * 1.4)
        b12_l2 = Tex("Reverse: electrolytic — electrons force chemistry").scale(0.95).shift(band_shift(12) + UP * 0.6)
        self.play(Write(b12_l1))
        self.play(Write(b12_l2))
        self.wait(2.5)
        b12_l3 = Tex("1. Strong $\\neq$ concentrated").scale(0.95).shift(band_shift(12) + DOWN * 0.3)
        b12_l4 = Tex("2. Equal rates, not equal amounts").scale(0.95).shift(band_shift(12) + DOWN * 1.0)
        b12_l5 = Tex("3. $K_c$ moves only with temperature").scale(0.95).shift(band_shift(12) + DOWN * 1.7)
        b12_l6 = Tex("4. Electrons OUT means anode, in any cell").scale(0.95).shift(band_shift(12) + DOWN * 2.4)
        self.play(Write(b12_l3))
        self.wait(1.5)
        self.play(Write(b12_l4))
        self.wait(1.5)
        self.play(Write(b12_l5))
        self.wait(1.5)
        self.play(Write(b12_l6))
        self.play(Create(SurroundingRectangle(b12_l6, color=GREEN)))
        self.wait(4)
