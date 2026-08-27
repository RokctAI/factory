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
        title = Tex("Chemistry Essentials: the Revision Sweep").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Atomic number $=$ protons — never changes").scale(1.0).shift(UP * 0.9)
        self.play(Write(d1))
        self.wait(2)
        d2 = Tex("Mass number $=$ protons $+$ neutrons").scale(1.0).shift(UP * 0.0)
        self.play(Write(d2))
        self.wait(2)
        d3 = Tex("Isotopes: same element, different neutrons").scale(1.0).shift(DOWN * 0.9)
        self.play(Write(d3))
        self.wait(2)
        d4 = MathTex(r"0{,}75 \times 35 + 0{,}25 \times 37 = 35{,}5").scale(1.05).shift(DOWN * 1.9)
        self.play(Write(d4))
        self.play(Create(SurroundingRectangle(d4, color=GREEN)))
        self.wait(2)
        d5 = Tex("Chlorine's 35,5 is a weighted average").scale(0.95).shift(DOWN * 2.9)
        self.play(Write(d5))
        self.wait(3)

        # --- Band 1 (subtopic_1): configurations and the map ---
        self.next_band(1)
        b1t = Tex("Electrons in s p notation").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = MathTex(r"\text{Na: } 1s^2\,2s^2\,2p^6\,3s^1").scale(1.1).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1a))
        self.wait(2)
        b1b = MathTex(r"\text{Cl: } 1s^2\,2s^2\,2p^6\,3s^2\,3p^5").scale(1.1).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1b))
        self.wait(2)
        b1c = Tex("Valence electrons do ALL the chemistry: 1 and 7").scale(0.95).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1c))
        self.wait(2.5)
        b1d = Tex("Across a period: smaller, more electronegative").scale(0.95).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1d))
        self.wait(2)
        b1e = Tex("Down a group: bigger, less electronegative").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1e))
        self.wait(3)

        # --- Band 2 (subtopic_2): ionic bonding ---
        self.next_band(2)
        b2t = Tex("Three bonds — the table's sides decide").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = Tex("Metal $+$ non-metal: IONIC — transfer").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2a))
        self.wait(2)
        b2b = Tex(r"Na gives its electron: Na$^+$ and Cl$^-$ attract").scale(0.95).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2b))
        self.wait(2.5)
        b2c = MathTex(r"\text{Ca}^{2+} + 2\,\text{Cl}^- \to \text{CaCl}_2").scale(1.05).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2c))
        self.wait(2)
        b2d = MathTex(r"\text{Al}_2\text{O}_3: \; +6 \text{ and } -6 = 0").scale(1.05).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2d))
        self.play(Create(SurroundingRectangle(b2d, color=GREEN)))
        self.wait(2)
        b2e = Tex("Always audit the charges to zero").scale(1.0).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2e))
        self.wait(3)

        # --- Band 3 (subtopic_2): covalent, metallic, properties ---
        self.next_band(3)
        b3t = Tex("Sharing and pooling").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = Tex("Covalent: shared pairs — H$_2$O; CO$_2$ double bonds").scale(0.95).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3a))
        self.wait(2.5)
        b3b = Tex("Diatomic seven: H$_2$ N$_2$ O$_2$ F$_2$ Cl$_2$ Br$_2$ I$_2$").scale(0.95).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3b))
        self.play(Create(SurroundingRectangle(b3b, color=GREEN)))
        self.wait(2.5)
        b3c = Tex("Metallic: kernels in an electron sea").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3c))
        self.wait(2)
        b3d = Tex("Ionic: conducts only molten or dissolved").scale(0.95).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3d))
        self.wait(2)
        b3e = Tex("Covalent: never. \\; Metal: always").scale(0.95).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3e))
        self.wait(3)

        # --- Band 4 (subtopic_3): change, and the equation ---
        self.next_band(4)
        b4t = Tex("Physical or chemical?").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        b4a = Tex("Physical: no new substance — ice melts").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4a))
        self.wait(2)
        b4b = Tex("Chemical: NEW substance — Mg burns to MgO").scale(1.0).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4b))
        self.wait(2)
        b4c = Tex("Both conserve mass: atoms only rearrange").scale(1.0).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4c))
        self.play(Create(SurroundingRectangle(b4c, color=GREEN)))
        self.wait(2.5)
        b4d = Tex("State symbols: (s) (l) (g) (aq)").scale(1.0).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4d))
        self.wait(3)

        # --- Band 5 (subtopic_3): balancing methane ---
        self.next_band(5)
        b5t = Tex("Balance: methane burning").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = MathTex(r"\text{CH}_4 + \text{O}_2 \to \text{CO}_2 + \text{H}_2\text{O}").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5a))
        self.wait(2)
        b5b = Tex(r"H: 4 left, 2 right $\to$ put 2 before H$_2$O").scale(0.95).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5b))
        self.wait(2)
        b5c = Tex(r"O: now 4 right $\to$ put 2 before O$_2$").scale(0.95).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5c))
        self.wait(2)
        b5d = MathTex(r"\text{CH}_4 + 2\,\text{O}_2 \to \text{CO}_2 + 2\,\text{H}_2\text{O}").scale(0.95).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5d))
        self.play(Create(SurroundingRectangle(b5d, color=GREEN)))
        self.wait(2.5)
        b5e = Tex("Audit: 1 C, 4 H, 4 O each side").scale(1.0).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5e))
        self.wait(3)

        # --- Band 6 (subtopic_3): magnesium, and the absolute law ---
        self.next_band(6)
        b6t = Tex("The term's classic, and the one law").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = MathTex(r"2\,\text{Mg} + \text{O}_2 \to 2\,\text{MgO}").scale(1.1).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6a))
        self.play(Create(SurroundingRectangle(b6a, color=GREEN)))
        self.wait(2.5)
        b6b = Tex("2 Mg and 2 O on each side — audited").scale(1.0).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6b))
        self.wait(2)
        b6c = MathTex(r"\text{H}_2\text{O} \to \text{H}_2\text{O}_2 \text{ to balance O}").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6c))
        self.play(Create(strike(b6c)))
        self.wait(2)
        b6d = Tex("Change COEFFICIENTS, never subscripts").scale(1.05).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6d))
        self.play(Create(SurroundingRectangle(b6d, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the mole's three formulas ---
        self.next_band(7)
        b7t = Tex("The mole: the counting unit").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = MathTex(r"1 \text{ mol} = 6{,}02 \times 10^{23} \text{ particles}").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7a))
        self.wait(2.5)
        b7b = MathTex(r"n = \frac{m}{M}").scale(1.15).shift(band_shift(7) + UP * 0.0 + LEFT * 3.0)
        b7c = MathTex(r"c = \frac{n}{V}").scale(1.15).shift(band_shift(7) + UP * 0.0 + RIGHT * 3.0)
        self.play(Write(b7b))
        self.play(Write(b7c))
        self.wait(2.5)
        b7d = MathTex(r"\text{Gas at STP: } 22{,}4 \text{ dm}^3 \text{ per mol}").scale(1.05).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7d))
        self.wait(2)
        b7e = Tex("Everything passes through moles").scale(1.0).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7e))
        self.wait(3)

        # --- Band 8 (subtopic_4): the four conversions, worked ---
        self.next_band(8)
        b8t = Tex("Four conversions, one hub").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = MathTex(r"\text{H}_2\text{O}: M = 18, \; \frac{36}{18} = 2 \text{ mol}").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8a))
        self.wait(2.5)
        b8b = MathTex(r"\text{CaCO}_3: M = 100, \; \frac{25}{100} = 0{,}25 \text{ mol}").scale(0.95).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8b))
        self.wait(2.5)
        b8c = MathTex(r"c = \frac{0{,}2}{0{,}5} = 0{,}4 \text{ mol/dm}^3").scale(1.0).shift(band_shift(8) + DOWN * 1.0)
        self.play(Write(b8c))
        self.wait(2.5)
        b8d = MathTex(r"V = 0{,}5 \times 22{,}4 = 11{,}2 \text{ dm}^3").scale(1.0).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8d))
        self.play(Create(SurroundingRectangle(b8d, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_4): into the water ---
        self.next_band(9)
        b9t = Tex("Chemistry in water").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Dissolved ionic compounds DISSOCIATE").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9a))
        self.wait(2)
        b9b = Tex("Free ions conduct: an electrolyte").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9b))
        self.wait(2)
        b9c = Tex("Sugar never splits — no conduction").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9c))
        self.wait(2)
        b9d = MathTex(r"\text{AgNO}_3\text{(aq)} + \text{NaCl(aq)}").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        b9e = MathTex(r"\to \text{AgCl(s)} + \text{NaNO}_3\text{(aq)}").scale(1.0).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9d))
        self.play(Write(b9e))
        self.play(Create(SurroundingRectangle(VGroup(b9d, b9e), color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 10 (subtopic_5): bricks and the catalogue ---
        self.next_band(10)
        b10t = Tex("Bricks, and three ways to click").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("Catalogue by BEHAVIOUR: columns click alike").scale(0.95).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10a))
        self.wait(2.5)
        b10b = Tex("Swap: metal gives, non-metal takes — ionic").scale(0.95).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10b))
        self.wait(2)
        b10c = Tex("Share: two hands on one handle — covalent").scale(0.95).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10c))
        self.wait(2)
        b10d = Tex("Pool: an electron sea glues the stack — metallic").scale(0.95).shift(band_shift(10) + DOWN * 1.6)
        self.play(Write(b10d))
        self.wait(2)
        b10e = Tex("Name the click; the properties recite themselves").scale(0.95).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10e))
        self.play(Create(SurroundingRectangle(b10e, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_6): counting eggs by weighing ---
        self.next_band(11)
        b11t = Tex("Counting eggs by weighing the crate").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11t))
        self.wait(2)
        b11a = MathTex(r"60 \text{ g/egg}: \; \frac{720}{60} = 12 \text{ eggs}").scale(1.0).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11a))
        self.wait(2.5)
        b11b = Tex("The mole is the chemist's dozen: $6{,}02 \\times 10^{23}$").scale(0.95).shift(band_shift(11) + UP * 0.1)
        self.play(Write(b11b))
        self.wait(2.5)
        b11c = MathTex(r"\text{Water: } M = 18 \Rightarrow 36 \text{ g} = 2 \text{ mol}").scale(1.0).shift(band_shift(11) + DOWN * 0.9)
        self.play(Write(b11c))
        self.play(Create(SurroundingRectangle(b11c, color=GREEN)))
        self.wait(2.5)
        b11d = Tex("Scale, jug, balloon — all priced in moles").scale(0.95).shift(band_shift(11) + DOWN * 1.9)
        self.play(Write(b11d))
        self.wait(2)
        b11e = Tex("Into moles first; chemistry; out of moles last").scale(0.95).shift(band_shift(11) + DOWN * 2.8)
        self.play(Write(b11e))
        self.wait(3)

        # --- Band 12 (subtopic_7): the trap list ---
        self.next_band(12)
        b12t = Tex("The trap list and the final audit").scale(1.15).shift(band_shift(12) + UP * 2.2)
        self.play(Write(b12t))
        self.wait(2)
        b12a = Tex("Balancing by editing subscripts").scale(1.0).shift(band_shift(12) + UP * 1.2)
        self.play(Write(b12a))
        self.play(Create(strike(b12a)))
        self.wait(2)
        b12b = Tex("Free oxygen is O$_2$ — recite the seven").scale(0.95).shift(band_shift(12) + UP * 0.3)
        self.play(Write(b12b))
        self.wait(2)
        b12c = MathTex(r"500 \text{ cm}^3 = 0{,}5 \text{ dm}^3 \text{ before } c = \tfrac{n}{V}").scale(0.95).shift(band_shift(12) + DOWN * 0.7)
        self.play(Write(b12c))
        self.wait(2.5)
        b12d = Tex("Equation ratios speak MOLES, never grams").scale(0.95).shift(band_shift(12) + DOWN * 1.7)
        self.play(Write(b12d))
        self.wait(2)
        b12e = Tex("Audit out loud: count every element, both sides").scale(0.95).shift(band_shift(12) + DOWN * 2.7)
        self.play(Write(b12e))
        self.play(Create(SurroundingRectangle(b12e, color=GREEN)))
        self.wait(4)
