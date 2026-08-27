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

# Band-layout whiteboard scene for molar-gas-volume (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). Exporter-safe mobjects,
# add-only lifecycle, one band per teaching beat.
# Time apportioned to subtopics.json (230/235/235/250/180/180/170 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MolarGasVolumeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): Avogadro's law ---
        title = Tex("Molar Gas Volume").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("1 mol CO$_2$: 44 g. \\quad 1 mol H$_2$: 2 g.").scale(1.0).shift(UP * 0.8)
        self.play(Write(d1))
        self.wait(2.5)
        d2 = Tex("Same $T$ and $p$: SAME volume").scale(1.1).shift(DOWN * 0.2)
        self.play(Write(d2))
        self.play(Create(SurroundingRectangle(d2, color=GREEN)))
        self.wait(2.5)
        d3 = Tex("A gas is mostly empty space — spacing sets volume").scale(0.95).shift(DOWN * 1.4)
        self.play(Write(d3))
        self.wait(3)

        # --- Band 1 (subtopic_1): STP and the 22,4 ---
        self.next_band(1)
        b1t = Tex("STP and the 22,4").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = Tex("STP: 0 $^\\circ$C (273 K), 101,3 kPa").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1a))
        self.wait(2.5)
        b1b = MathTex(r"V_m = 22{,}4 \text{ dm}^3/\text{mol, any gas}").scale(1.05).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1b))
        self.play(Create(SurroundingRectangle(b1b, color=GREEN)))
        self.wait(2.5)
        b1c = MathTex(r"V = n \times V_m \quad ; \quad n = \frac{V}{22{,}4}").scale(1.0).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(b1c))
        self.wait(2.5)
        b1d = Tex("Licence: gases only, STP only").scale(1.0).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1d))
        self.wait(3)

        # --- Band 2 (subtopic_2): the reaction, balanced, and 'excess' ---
        self.next_band(2)
        b2t = Tex("13 g of zinc meets excess acid").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = MathTex(r"\text{Zn} + 2\text{HCl} \to \text{ZnCl}_2 + \text{H}_2").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2a))
        self.play(Create(SurroundingRectangle(b2a, color=GREEN)))
        self.wait(2.5)
        b2b = Tex("Balanced: 1 Zn, 2 H, 2 Cl each side").scale(0.95).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2b))
        self.wait(2.5)
        b2c = Tex("Excess acid: ALL the zinc reacts").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2c))
        self.wait(2)
        b2d = Tex("Base the calculation on the zinc").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2d))
        self.wait(3)

        # --- Band 3 (subtopic_2): the three-leg journey ---
        self.next_band(3)
        b3t = Tex("Three legs, new exit").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = MathTex(r"n = \frac{13}{65} = 0{,}2 \text{ mol Zn}").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3a))
        self.wait(2.5)
        b3b = MathTex(r"\text{Ratio } 1:1 \Rightarrow 0{,}2 \text{ mol H}_2").scale(1.0).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3b))
        self.wait(2.5)
        b3c = MathTex(r"V = 0{,}2 \times 22{,}4 = 4{,}48 \text{ dm}^3").scale(1.05).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3c))
        self.play(Create(SurroundingRectangle(b3c, color=GREEN)))
        self.wait(2.5)
        b3d = Tex("By mass instead: $0{,}2 \\times 2 = 0{,}4$ g").scale(0.95).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3d))
        self.wait(3)

        # --- Band 4 (subtopic_3): volume ratios read off coefficients ---
        self.next_band(4)
        b4t = Tex("Volume ratios, straight off the equation").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        b4a = MathTex(r"2\text{CO} + \text{O}_2 \to 2\text{CO}_2").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4a))
        self.wait(2.5)
        b4b = Tex("Coefficients wear litres: 2 : 1 : 2").scale(1.0).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4b))
        self.wait(2.5)
        b4c = MathTex(r"20 \text{ dm}^3 + 10 \text{ dm}^3 \to 20 \text{ dm}^3").scale(1.0).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4c))
        self.play(Create(SurroundingRectangle(b4c, color=GREEN)))
        self.wait(2.5)
        b4d = Tex("No molar masses, no moles, no 22,4").scale(0.95).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4d))
        self.wait(3)

        # --- Band 5 (subtopic_3): volume is not conserved ---
        self.next_band(5)
        b5t = Tex("30 in, 20 out — and nothing leaked").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = Tex("Three molecules become two").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5a))
        self.wait(2.5)
        b5b = Tex("Mass: always conserved. Volume: follows the count.").scale(0.95).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5b))
        self.play(Create(SurroundingRectangle(b5b, color=GREEN)))
        self.wait(2.5)
        b5c = Tex("Conditions: same $T$ and $p$ — not necessarily STP").scale(0.95).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5c))
        self.wait(2)
        b5d = Tex("Only species marked (g) join the ratio").scale(0.95).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5d))
        self.wait(3)

        # --- Band 6 (subtopic_4): the toolkit ---
        self.next_band(6)
        b6t = Tex("The gas toolkit").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = Tex("1. $V = n \\times V_m$ at STP, both directions").scale(0.95).shift(band_shift(6) + UP * 1.1)
        b6b = Tex("2. Mass $\\to$ moles $\\to$ ratio $\\to$ volume").scale(0.95).shift(band_shift(6) + UP * 0.2)
        b6c = Tex("3. Coefficients as volume ratios, shared conditions").scale(0.95).shift(band_shift(6) + DOWN * 0.7)
        for m in (b6a, b6b, b6c):
            self.play(Write(m))
            self.wait(2)
        b6d = Tex("Choose by what the question gives").scale(0.95).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6d))
        self.wait(3)

        # --- Band 7 (subtopic_4): the five traps ---
        self.next_band(7)
        b7t = Tex("The five traps").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex("1. 22,4 without STP — no licence").scale(0.95).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7a))
        self.play(Create(strike(b7a)))
        self.wait(2)
        b7b = Tex("2. 22,4 on liquids: 1 mol water $=$ 18 cm$^3$").scale(0.95).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7b))
        self.wait(2)
        b7c = Tex("3. cm$^3$ vs dm$^3$: divide by 1 000").scale(0.95).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7c))
        self.wait(2)
        b7d = Tex("4. Building on the excess reactant").scale(0.95).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7d))
        self.wait(2)
        b7e = Tex("5. Expecting volumes to balance like masses").scale(0.95).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7e))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): same crate, whatever the cargo ---
        self.next_band(8)
        b8t = Tex("Same crate, whatever the cargo").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        c1 = Rectangle(width=2.6, height=2.0, color=YELLOW).shift(band_shift(8) + LEFT * 2.2 + UP * 0.3)
        c2 = Rectangle(width=2.6, height=2.0, color=YELLOW).shift(band_shift(8) + RIGHT * 2.2 + UP * 0.3)
        self.play(Create(c1), Create(c2))
        l1 = Tex("H$_2$: 2 g").scale(0.9).move_to(c1.get_center())
        l2 = Tex("CO$_2$: 44 g").scale(0.9).move_to(c2.get_center())
        self.play(Write(l1), Write(l2))
        self.wait(2.5)
        b8a = Tex("Packed by COUNT, not by mass").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8a))
        self.wait(2)
        b8b = Tex("At STP the crate is 22,4 litres per mole").scale(1.0).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8b))
        self.play(Create(SurroundingRectangle(b8b, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): a spoonful of zinc ---
        self.next_band(9)
        b9t = Tex("A spoonful of zinc, a balloon of gas").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Plenty of acid: the zinc decides").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9a))
        self.wait(2.5)
        b9b = MathTex(r"\frac{13}{65} = 0{,}2 \text{ mol} \; \to \; 0{,}2 \text{ mol H}_2").scale(1.0).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = MathTex(r"0{,}2 \times 22{,}4 = 4{,}48 \text{ dm}^3").scale(1.05).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9c))
        self.play(Create(SurroundingRectangle(b9c, color=GREEN)))
        self.wait(2.5)
        b9d = Tex("Solids are cramped; gases are roomy").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9d))
        self.wait(3)

        # --- Band 10 (subtopic_7): recipes measured in litres ---
        self.next_band(10)
        b10t = Tex("Recipes measured in litres").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("Two cups CO, one cup O$_2$, two cups CO$_2$").scale(0.95).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10a))
        self.wait(2.5)
        b10b = MathTex(r"20 + 10 \to 20 \text{ litres}").scale(1.05).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10b))
        self.play(Create(SurroundingRectangle(b10b, color=GREEN)))
        self.wait(2.5)
        b10c = Tex("Where did the volume go? Into fewer molecules.").scale(0.95).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10c))
        self.wait(2)
        b10d = Tex("All gas, shared conditions? Read the coefficients.").scale(0.95).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10d))
        self.wait(4)
