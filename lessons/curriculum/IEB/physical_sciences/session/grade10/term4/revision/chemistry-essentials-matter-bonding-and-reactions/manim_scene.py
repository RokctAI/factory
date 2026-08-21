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

# Band-layout whiteboard scene for the revision session "Chemistry Essentials:
# Matter, Bonding and Reactions" (Part 1 — Expert: subtopics 1-4; Part 2 —
# Simplifier: subtopics 5-7). Exporter-safe mobjects only, add-only lifecycle,
# every worked calculation line by line with the script's numbers. Band time
# apportioned to subtopics.json (240/250/245/250/195/190/190 of 1560 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ChemistryEssentialsRevisionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(15)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the atom's two numbers ---
        title = Tex("Chemistry Essentials — Revision Sweep").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Atomic number: protons — the element's identity").scale(0.9).shift(UP * 1.2)
        self.play(Write(d1))
        self.wait(2)
        d2 = Tex("Mass number: protons $+$ neutrons").scale(0.9).shift(UP * 0.4)
        self.play(Write(d2))
        self.wait(2)
        d3 = Tex("Isotopes: same protons, different neutrons").scale(0.9).shift(DOWN * 0.4)
        self.play(Write(d3))
        self.wait(2.5)
        d4 = MathTex(r"0{,}2 \times 10 + 0{,}8 \times 11 = 10{,}8").scale(1.0).shift(DOWN * 1.4)
        self.play(Write(d4))
        self.play(Create(SurroundingRectangle(d4, color=GREEN)))
        self.wait(2.5)
        d5 = Tex("Boron's decimal is a weighted average").scale(0.9).shift(DOWN * 2.5)
        self.play(Write(d5))
        self.wait(3)

        # --- Band 1 (subtopic_1): configurations and the map ---
        self.next_band(1)
        b1t = Tex("Configurations and the map").scale(1.15).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1t))
        self.wait(2)
        b1a = MathTex(r"\text{Al (13): } 1s^2\,2s^2\,2p^6\,3s^2\,3p^1").scale(0.95).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1a))
        self.wait(2.5)
        b1b = MathTex(r"\text{P (15): } 1s^2\,2s^2\,2p^6\,3s^2\,3p^3").scale(0.95).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1b))
        self.wait(2.5)
        b1c = Tex("Valence electrons do ALL the chemistry").scale(0.95).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1c))
        self.wait(2)
        b1d = Tex("Across a period: smaller, more electronegative").scale(0.9).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(b1d))
        self.wait(2)
        b1e = Tex("Down a group: bigger, less electronegative").scale(0.9).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1e))
        self.wait(3)

        # --- Band 2 (subtopic_2): ionic bonding ---
        self.next_band(2)
        b2t = Tex("Ionic: the TRANSFER").scale(1.15).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2t))
        self.wait(2)
        b2a = Tex("Metal $+$ non-metal: electrons change owners").scale(0.9).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2a))
        self.wait(2.5)
        b2b = MathTex(r"\text{Mg}^{2+} + 2\,\text{Cl}^- \to \text{MgCl}_2").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2b))
        self.wait(2.5)
        b2c = MathTex(r"\text{Mg}_3\text{N}_2: \; 3(+2) + 2(-3) = 0").scale(1.0).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2c))
        self.play(Create(SurroundingRectangle(b2c, color=GREEN)))
        self.wait(2.5)
        b2d = Tex("Audit every formula to neutral — always").scale(0.9).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2d))
        self.wait(3)

        # --- Band 3 (subtopic_2): covalent, metallic, properties ---
        self.next_band(3)
        b3t = Tex("Covalent shares; metallic pools").scale(1.1).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3t))
        self.wait(2)
        b3a = Tex("NH$_3$: three shared pairs; CO$_2$: double bonds").scale(0.9).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3a))
        self.wait(2.5)
        b3b = Tex("Diatomic seven: H$_2$ N$_2$ O$_2$ F$_2$ Cl$_2$ Br$_2$ I$_2$").scale(0.9).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3b))
        self.play(Create(SurroundingRectangle(b3b, color=GREEN)))
        self.wait(2.5)
        b3c = Tex("Metals: kernels in a lattice, electron sea around").scale(0.9).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3c))
        self.wait(2.5)
        b3d = Tex("Ionic: conducts molten/dissolved. Covalent: never").scale(0.85).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3d))
        self.wait(2)
        b3e = Tex("Metals: conduct always — the sea is free").scale(0.9).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3e))
        self.wait(3)

        # --- Band 4 (subtopic_3): change, and the equation ---
        self.next_band(4)
        b4t = Tex("Physical vs chemical change").scale(1.15).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4t))
        self.wait(2)
        b4a = Tex("Physical: no new substance — ice is still water").scale(0.9).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4a))
        self.wait(2.5)
        b4b = Tex("Chemical: NEW substance — calcium burns to CaO").scale(0.9).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4b))
        self.wait(2.5)
        b4c = Tex("Both conserve mass: atoms only rearrange").scale(0.9).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4c))
        self.play(Create(SurroundingRectangle(b4c, color=GREEN)))
        self.wait(2.5)
        b4d = Tex("States: (s) (l) (g) (aq) — chemistry, compressed").scale(0.9).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4d))
        self.wait(3)

        # --- Band 5 (subtopic_3): balancing propane ---
        self.next_band(5)
        b5t = Tex("Balance the braai gas").scale(1.15).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5t))
        self.wait(2)
        b5a = MathTex(r"\text{C}_3\text{H}_8 + \text{O}_2 \to \text{CO}_2 + \text{H}_2\text{O}").scale(0.95).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5a))
        self.wait(2.5)
        b5b = Tex("C: 3 $\\to$ 3CO$_2$. \\; H: 8 $\\to$ 4H$_2$O").scale(0.95).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5b))
        self.wait(2.5)
        b5c = Tex("O right: $6+4=10$ $\\to$ 5O$_2$ left").scale(0.95).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5c))
        self.wait(2.5)
        b5d = MathTex(r"\text{C}_3\text{H}_8 + 5\text{O}_2 \to 3\text{CO}_2 + 4\text{H}_2\text{O}").scale(0.95).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5d))
        self.play(Create(SurroundingRectangle(b5d, color=GREEN)))
        self.wait(2.5)
        b5e = Tex("Audit aloud: C 3$=$3, H 8$=$8, O 10$=$10").scale(0.9).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5e))
        self.wait(3)

        # --- Band 6 (subtopic_3): calcium, and the absolute law ---
        self.next_band(6)
        b6t = Tex("Calcium burns — and the absolute law").scale(1.05).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6t))
        self.wait(2)
        b6a = MathTex(r"2\text{Ca} + \text{O}_2 \to 2\text{CaO}").scale(1.05).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6a))
        self.play(Create(SurroundingRectangle(b6a, color=GREEN)))
        self.wait(2.5)
        b6b = Tex("Two calciums, two oxygens — each side").scale(0.9).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6b))
        self.wait(2.5)
        b6c = Tex("Balance by editing subscripts").scale(0.95).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6c))
        self.play(Create(strike(b6c)))
        self.wait(2)
        b6d = Tex("Subscripts are identity; coefficients are quantity").scale(0.9).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6d))
        self.wait(3)

        # --- Band 7 (subtopic_4): the mole's three formulas ---
        self.next_band(7)
        b7t = Tex("The mole: one hub, three formulas").scale(1.1).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7t))
        self.wait(2)
        b7a = MathTex(r"n = \frac{m}{M}").scale(1.1).shift(band_shift(7) + UP * 1.1 + LEFT * 3.0)
        b7b = MathTex(r"c = \frac{n}{V}").scale(1.1).shift(band_shift(7) + UP * 1.1)
        b7c = MathTex(r"22{,}4 \text{ dm}^3/\text{mol}").scale(0.9).shift(band_shift(7) + UP * 1.1 + RIGHT * 3.0)
        self.play(Write(b7a))
        self.play(Write(b7b))
        self.play(Write(b7c))
        self.wait(2.5)
        b7d = MathTex(r"N_A = 6{,}02 \times 10^{23} \text{ particles/mol}").scale(0.95).shift(band_shift(7) + DOWN * 0.2)
        self.play(Write(b7d))
        self.play(Create(SurroundingRectangle(b7d, color=GREEN)))
        self.wait(2.5)
        b7e = Tex("Scale, measuring jug, balloon — one currency").scale(0.9).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(b7e))
        self.wait(3)

        # --- Band 8 (subtopic_4): the four conversions, worked ---
        self.next_band(8)
        b8t = Tex("Four exchanges, worked").scale(1.15).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8t))
        self.wait(2)
        b8a = MathTex(r"\text{CO}_2: M = 44 \Rightarrow 22 \text{ g} = 0{,}5 \text{ mol}").scale(0.9).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8a))
        self.wait(2.5)
        b8b = MathTex(r"\text{Na}_2\text{CO}_3: M = 106 \Rightarrow 53 \text{ g} = 0{,}5 \text{ mol}").scale(0.9).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8b))
        self.wait(2.5)
        b8c = MathTex(r"c = \frac{0{,}3}{0{,}6} = 0{,}5 \text{ mol/dm}^3").scale(0.9).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8c))
        self.wait(2.5)
        b8d = MathTex(r"2 \text{ mol gas at STP} = 44{,}8 \text{ dm}^3").scale(0.9).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8d))
        self.play(Create(SurroundingRectangle(b8d, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_4): into the water ---
        self.next_band(9)
        b9t = Tex("Into the water").scale(1.2).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9t))
        self.wait(2)
        b9a = MathTex(r"\text{MgCl}_2\text{(s)} \to \text{Mg}^{2+}(aq) + 2\text{Cl}^-(aq)").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9a))
        self.wait(2.5)
        b9b = Tex("Free ions $\\Rightarrow$ electrolyte: it conducts").scale(0.9).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = MathTex(r"\text{Pb(NO}_3)_2\text{(aq)} + 2\text{KI(aq)}").scale(0.9).shift(band_shift(9) + DOWN * 0.6)
        b9d = MathTex(r"\to \text{PbI}_2\text{(s)} + 2\text{KNO}_3\text{(aq)}").scale(0.9).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9c))
        self.play(Write(b9d))
        self.play(Create(SurroundingRectangle(VGroup(b9c, b9d), color=GREEN)))
        self.wait(2.5)
        b9e = Tex("Golden snow: the (s) is the precipitate").scale(0.9).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9e))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 10 (subtopic_5): bricks and the catalogue ---
        self.next_band(10)
        b10t = Tex("Bricks, and three ways to click").scale(1.15).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("Catalogue sorted by BEHAVIOUR: columns click alike").scale(0.85).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10a))
        self.wait(2.5)
        b10b = Tex("SWAP: metal gives, non-metal takes — ionic").scale(0.9).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10b))
        self.wait(2)
        b10c = Tex("SHARE: two hands, one handle — covalent").scale(0.9).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10c))
        self.wait(2)
        b10d = Tex("POOL: electron sea glues the stack — metallic").scale(0.9).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10d))
        self.wait(2)
        b10e = Tex("Name the click; the properties recite themselves").scale(0.9).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(b10e))
        self.play(Create(SurroundingRectangle(b10e, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_6): counting eggs by weighing ---
        self.next_band(11)
        b11t = Tex("Counting eggs by weighing the crate").scale(1.1).shift(band_shift(11) + UP * 2.3)
        self.play(Write(b11t))
        self.wait(2)
        b11a = Tex("One egg 50 g $\\Rightarrow$ 600 g is 12 eggs").scale(0.95).shift(band_shift(11) + UP * 1.2)
        self.play(Write(b11a))
        self.wait(2.5)
        b11b = Tex("One mole CO$_2$ weighs 44 g").scale(0.95).shift(band_shift(11) + UP * 0.3)
        self.play(Write(b11b))
        self.wait(2)
        b11c = Tex("22 g on the scale $=$ half a mole, counted").scale(0.95).shift(band_shift(11) + DOWN * 0.6)
        self.play(Write(b11c))
        self.play(Create(SurroundingRectangle(b11c, color=GREEN)))
        self.wait(2.5)
        b11d = Tex("Into moles $\\to$ chemistry $\\to$ out of moles").scale(0.95).shift(band_shift(11) + DOWN * 1.6)
        self.play(Write(b11d))
        self.wait(2)
        b11e = Tex("Never exchange grams for volumes directly").scale(0.9).shift(band_shift(11) + DOWN * 2.5)
        self.play(Write(b11e))
        self.wait(3)

        # --- Band 12 (subtopic_7): the trap list ---
        self.next_band(12)
        b12t = Tex("The trap list and the final audit").scale(1.1).shift(band_shift(12) + UP * 2.3)
        self.play(Write(b12t))
        self.wait(2)
        b12a = Tex("1. Subscripts edited \\; 2. Diatomic seven forgotten").scale(0.85).shift(band_shift(12) + UP * 1.2)
        self.play(Write(b12a))
        self.wait(2.5)
        b12b = Tex("3. cm$^3$ fed raw: 250 cm$^3$ $=$ 0,25 dm$^3$").scale(0.85).shift(band_shift(12) + UP * 0.3)
        self.play(Write(b12b))
        self.wait(2.5)
        b12c = Tex("4. Grams through mole ratios \\; 5. Dissolving called chemical").scale(0.8).shift(band_shift(12) + DOWN * 0.6)
        self.play(Write(b12c))
        self.wait(2.5)
        b12d = Tex("Audit: count elements, cancel units, name spectators").scale(0.85).shift(band_shift(12) + DOWN * 1.6)
        self.play(Write(b12d))
        self.play(Create(SurroundingRectangle(b12d, color=GREEN)))
        self.wait(2.5)
        b12e = Tex("Every toolkit carries its own free proof").scale(0.9).shift(band_shift(12) + DOWN * 2.6)
        self.play(Write(b12e))
        self.wait(4)
