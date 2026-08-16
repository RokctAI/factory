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

# Band-layout whiteboard scene for concentration-and-empirical-formula
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe mobjects only; add-only lifecycle; every worked calculation
# appears line by line with the script's exact numbers and units.
# Time apportioned to subtopics.json (230/220/240/260/180/180/170 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ConcentrationEmpiricalFormulaSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the formula and its two guards ---
        title = Tex("Concentration and Empirical Formula").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        a1 = MathTex(r"c = \frac{n}{V} \quad \text{(mol·dm}^{-3}\text{)}").scale(1.2).shift(UP * 0.9)
        self.play(Write(a1))
        self.wait(2.5)
        a2 = Tex("1 dm$^3$ = 1 litre").scale(1.05).shift(DOWN * 0.2)
        self.play(Write(a2))
        self.wait(2)
        a3 = MathTex(r"\text{cm}^3 \div 1000 \to \text{dm}^3").scale(1.05).shift(DOWN * 1.1)
        self.play(Write(a3))
        self.wait(2)
        a4 = MathTex(r"n = \frac{m}{M} \; \text{(grams to moles)}").scale(1.05).shift(DOWN * 2.1)
        self.play(Write(a4))
        self.wait(3)

        # --- Band 1 (subtopic_1): NaOH worked in full ---
        self.next_band(1)
        b1_t = Tex(r"8 g NaOH in 500 cm$^3$: find $c$").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_1 = MathTex(r"M = 23 + 16 + 1 = 40\ \text{g·mol}^{-1}").scale(1.05).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_1))
        self.wait(2)
        b1_2 = MathTex(r"n = \frac{m}{M} = \frac{8}{40} = 0{,}2\ \text{mol}").scale(1.05).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_2))
        self.wait(2.5)
        b1_3 = MathTex(r"V = \frac{500}{1000} = 0{,}5\ \text{dm}^3").scale(1.05).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(b1_3))
        self.wait(2)
        b1_4 = MathTex(r"c = \frac{n}{V} = \frac{0{,}2}{0{,}5} = 0{,}4\ \text{mol·dm}^{-3}").scale(1.05).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1_4))
        self.play(Create(SurroundingRectangle(b1_4, color=GREEN)))
        self.wait(2)
        b1_5 = Tex("Check: a full dm$^3$ holds twice 0,2").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_5))
        self.wait(3)

        # --- Band 2 (subtopic_2): percentage composition, water ---
        self.next_band(2)
        b2_t = Tex("Percentage composition").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_1 = MathTex(r"\%\ \text{element} = \frac{\text{mass in 1 mol}}{M} \times 100").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_1))
        self.wait(2.5)
        b2_2 = MathTex(r"\text{H}_2\text{O}: M = 2(1) + 16 = 18").scale(1.05).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_2))
        self.wait(2)
        b2_3 = MathTex(r"\%\text{H} = \frac{2}{18} \times 100 = 11{,}1\%").scale(1.05).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_3))
        self.wait(2)
        b2_4 = MathTex(r"\%\text{O} = \frac{16}{18} \times 100 = 88{,}9\%").scale(1.05).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_4))
        self.wait(2)
        b2_5 = MathTex(r"11{,}1 + 88{,}9 = 100 \; \checkmark").scale(1.05).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_5))
        self.play(Create(SurroundingRectangle(b2_5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): CO2 and subscript discipline ---
        self.next_band(3)
        b3_t = Tex(r"CO$_2$: subscripts are multipliers").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_trap = MathTex(r"\%\text{O} = \frac{16}{44} \times 100 \; \text{(one O?!)}").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_trap))
        self.play(Create(strike(b3_trap)))
        self.wait(2)
        b3_1 = MathTex(r"M = 12 + 2(16) = 44").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_1))
        self.wait(2)
        b3_2 = MathTex(r"\%\text{C} = \frac{12}{44} \times 100 = 27{,}3\%").scale(1.05).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_2))
        self.wait(2)
        b3_3 = MathTex(r"\%\text{O} = \frac{32}{44} \times 100 = 72{,}7\%").scale(1.05).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_3))
        self.play(Create(SurroundingRectangle(b3_3, color=GREEN)))
        self.wait(2)
        b3_4 = Tex("Lab-measurable: burn, weigh, recover \\%s").scale(0.95).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_4))
        self.wait(3)

        # --- Band 4 (subtopic_3): empirical formula, steps 1-2 ---
        self.next_band(4)
        b4_t = Tex(r"40,0\% C, 6,7\% H, 53,3\% O: formula?").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_1 = Tex("Step 1: assume 100 g of sample").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_1))
        self.wait(2)
        b4_2 = Tex("40,0 g C; 6,7 g H; 53,3 g O").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_2))
        self.wait(2)
        b4_3 = Tex("Step 2: masses to moles").scale(1.05).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_3))
        self.wait(1.5)
        b4_4 = MathTex(r"\text{C}: \frac{40{,}0}{12} = 3{,}33 \quad \text{H}: \frac{6{,}7}{1} = 6{,}7").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_4))
        self.wait(2.5)
        b4_5 = MathTex(r"\text{O}: \frac{53{,}3}{16} = 3{,}33").scale(1.0).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_5))
        self.wait(3)

        # --- Band 5 (subtopic_3): steps 3-4 + the multiply-up rule ---
        self.next_band(5)
        b5_t = Tex("Divide by the smallest").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_1 = MathTex(r"\text{C}: \frac{3{,}33}{3{,}33} = 1 \quad \text{H}: \frac{6{,}7}{3{,}33} = 2").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_1))
        self.wait(2.5)
        b5_2 = MathTex(r"\text{O}: \frac{3{,}33}{3{,}33} = 1").scale(1.0).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_2))
        self.wait(2)
        b5_3 = MathTex(r"\text{Ratio } 1 : 2 : 1 \;\Rightarrow\; \text{CH}_2\text{O}").scale(1.1).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_3))
        self.play(Create(SurroundingRectangle(b5_3, color=GREEN)))
        self.wait(2.5)
        b5_trap = Tex("Round 1,5 down to 1").scale(1.0).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_trap))
        self.play(Create(strike(b5_trap)))
        self.wait(1.5)
        b5_4 = MathTex(r"1 : 1{,}5 \; \text{is honestly} \; 2 : 3 \; (\times 2)").scale(1.0).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_4))
        self.wait(3)

        # --- Band 6 (subtopic_4): water of crystallisation ---
        self.next_band(6)
        b6_t = Tex(r"CuSO$_4\cdot$5H$_2$O: water's share").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_1 = MathTex(r"\text{CuSO}_4: 63{,}5 + 32 + 4(16) = 159{,}5").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_1))
        self.wait(2.5)
        b6_2 = MathTex(r"5\,\text{H}_2\text{O}: 5 \times 18 = 90").scale(1.05).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_2))
        self.wait(2)
        b6_3 = MathTex(r"\text{Total: } 159{,}5 + 90 = 249{,}5").scale(1.05).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_3))
        self.wait(2)
        b6_4 = MathTex(r"\%\text{H}_2\text{O} = \frac{90}{249{,}5} \times 100 = 36{,}1\%").scale(1.05).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_4))
        self.play(Create(SurroundingRectangle(b6_4, color=GREEN)))
        self.wait(2.5)
        b6_5 = Tex("Heat: blue to white, mass drops by 36,1\\%").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_5))
        self.wait(3)

        # --- Band 7 (subtopic_4): the four traps ---
        self.next_band(7)
        b7_t = Tex("The four traps").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_trap = MathTex(r"c = \frac{0{,}2}{500} \; \text{(cm}^3\text{ not converted)}").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_trap))
        self.play(Create(strike(b7_trap)))
        self.wait(2)
        b7_1 = Tex("Convert to dm$^3$ when listing data").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_1))
        self.wait(2)
        b7_2 = Tex("Mass ratio $\\neq$ atom ratio: only moles count").scale(0.95).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_2))
        self.wait(2)
        b7_3 = Tex("Never round 1,5 — multiply the ratio up").scale(0.95).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_3))
        self.wait(2)
        b7_4 = Tex("Subscripts multiply: 2 in H$_2$O, 5 in 5H$_2$O").scale(0.95).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_4))
        self.play(Create(SurroundingRectangle(b7_4, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): how strong is the cooldrink ---
        self.next_band(8)
        b8_t = Tex("How strong is the cooldrink?").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_1 = Tex("Strong = lots of concentrate per jug").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_1))
        self.wait(2)
        b8_2 = MathTex(r"n = \frac{8}{40} = 0{,}2\ \text{mol (count the packs)}").scale(1.0).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_2))
        self.wait(2.5)
        b8_3 = MathTex(r"V = 500\ \text{cm}^3 = 0{,}5\ \text{dm}^3").scale(1.0).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_3))
        self.wait(2)
        b8_4 = MathTex(r"c = \frac{0{,}2}{0{,}5} = 0{,}4\ \text{mol·dm}^{-3}").scale(1.05).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_4))
        self.play(Create(SurroundingRectangle(b8_4, color=GREEN)))
        self.wait(2)
        b8_5 = Tex("Crowding, not total: volume sits below").scale(0.95).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_5))
        self.wait(3)

        # --- Band 9 (subtopic_6): reading the recipe backwards ---
        self.next_band(9)
        b9_t = Tex("Reading the recipe backwards").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_1 = Tex("Pretend 100 g: \\%s become grams").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_1))
        self.wait(2)
        b9_2 = MathTex(r"\text{C}: 3{,}33 \quad \text{H}: 6{,}7 \quad \text{O}: 3{,}33").scale(1.0).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_2))
        self.wait(2.5)
        b9_3 = MathTex(r"\div\, 3{,}33: \quad 1 : 2 : 1").scale(1.05).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_3))
        self.wait(2)
        b9_4 = MathTex(r"\text{CH}_2\text{O}").scale(1.2).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_4))
        self.play(Create(SurroundingRectangle(b9_4, color=GREEN)))
        self.wait(2)
        b9_5 = Tex("Half atoms not on the menu: double up").scale(0.95).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the water hiding in dry crystals ---
        self.next_band(10)
        b10_t = Tex("The water hiding in dry crystals").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_1 = Tex(r"Blue CuSO$_4\cdot$5H$_2$O: a third is water").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_1))
        self.wait(2)
        b10_2 = MathTex(r"\text{Invoice: } 159{,}5 + 90 = 249{,}5").scale(1.0).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_2))
        self.wait(2.5)
        b10_3 = MathTex(r"\frac{90}{249{,}5} \times 100 = 36{,}1\%").scale(1.05).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_3))
        self.play(Create(SurroundingRectangle(b10_3, color=GREEN)))
        self.wait(2.5)
        b10_4 = Tex("The balance agrees with the paper").scale(1.0).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_4))
        self.wait(2)
        b10_5 = Tex("Habits: moles first; subscripts multiply").scale(1.0).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10_5))
        self.wait(4)
