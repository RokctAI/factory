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

# Band-layout whiteboard scene for the chemistry revision session duo
# (quantitative chemistry + acids and bases). Covers all seven subtopics
# (Part 1 Expert: 1-4, Part 2 Simplifier: 5-7), band time proportional to
# subtopics.json (240/250/255/255/195/195/200 of 1590 s). Add-only
# lifecycle; exporter-safe mobjects only; SA decimal commas.

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
        self.wait(15)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the mole hub, mass leg ---
        title = Tex("The Mole Toolkit").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Three doors into one hub:").scale(1.05).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(1.5)
        b0_f = MathTex(r"n = \frac{m}{M} \quad c = \frac{n}{V} \quad n = \frac{V}{22{,}4}").scale(1.1).shift(UP * 0.2)
        self.play(Write(b0_f))
        self.play(Create(SurroundingRectangle(b0_f, color=GREEN)))
        self.wait(2.5)
        b0_l2 = MathTex(r"M(KOH) = 39 + 16 + 1 = 56 \text{ g/mol}").scale(1.0).shift(DOWN * 1.1)
        b0_l3 = MathTex(r"n = \frac{14}{56} = 0{,}25 \text{ mol}").scale(1.05).shift(DOWN * 2.1)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(3)

        # --- Band 1 (subtopic_1): solution and gas legs ---
        self.next_band(1)
        b1_t = Tex("Same 0{,}25 mol, three disguises").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_l1 = MathTex(r"500 \text{ cm}^3 \div 1000 = 0{,}5 \text{ dm}^3 \text{ FIRST}").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"c = \frac{0{,}25}{0{,}5} = 0{,}5 \text{ mol/dm}^3").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"V = 0{,}25 \times 22{,}4 = 5{,}6 \text{ dm}^3 \text{ at STP}").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("Convert IN to moles, work, convert OUT —").scale(1.0).shift(band_shift(1) + DOWN * 1.8)
        b1_l5 = Tex("grams never talk directly to dm$^3$").scale(1.0).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l4))
        self.wait(1.5)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): the ideal model, kelvin, Boyle ---
        self.next_band(2)
        b2_t = Tex("The ideal gas model").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = Tex("Random motion, negligible particle volume,").scale(0.95).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("no forces, elastic collisions").scale(0.95).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2_l1))
        self.wait(1.5)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"T(K) = t(^\circ C) + 273 \quad \text{— no Celsius!}").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"p_1V_1 = p_2V_2: \; 120 \times 3 = 360 \times 1").scale(1.0).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = MathTex(r"\frac{p_1V_1}{T_1} = \frac{p_2V_2}{T_2}").scale(1.1).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): pV = nRT worked, and the fine print ---
        self.next_band(3)
        b3_f = MathTex(r"pV = nRT, \quad R = 8{,}31").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_f))
        self.wait(2)
        b3_l1 = Tex(r"Strict units: Pa, m$^3$, K").scale(1.05).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"p = \frac{nRT}{V} = \frac{0{,}2 \times 8{,}31 \times 350}{0{,}005}").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"p = 116\,340 \text{ Pa} \approx 116{,}3 \text{ kPa}").scale(1.05).shift(band_shift(3) + DOWN * 1.0)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("Real gases deviate at high $p$, low $T$ —").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        b3_l5 = Tex("crowded particles, forces that bite").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l4))
        self.wait(1.5)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the four-step bridge ---
        self.next_band(4)
        b4_t = Tex("Stoichiometry: the four-step bridge").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_l1 = Tex("Balance; given IN to moles;").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex("ratio across; answer OUT").scale(1.0).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l1))
        self.wait(1.5)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_eq = MathTex(r"N_2 + 3H_2 \rightarrow 2NH_3").scale(1.15).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4_eq))
        self.wait(2)
        b4_l3 = MathTex(r"2 \text{ mol } N_2 \xrightarrow{1:2} 4 \text{ mol } NH_3").scale(1.0).shift(band_shift(4) + DOWN * 1.5)
        b4_l4 = MathTex(r"m = 4 \times 17 = 68 \text{ g}").scale(1.05).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): limiting reagent, yield, purity ---
        self.next_band(5)
        b5_t = Tex(r"2 mol $N_2$ meets 4{,}5 mol $H_2$ — who limits?").scale(1.0).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_l1 = MathTex(r"2 \text{ mol } N_2 \text{ demands } 6 \text{ mol } H_2").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex(r"Available 4{,}5 mol: $N_2$ excess, $H_2$ LIMITING").scale(0.9).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = MathTex(r"\% \text{ yield} = \frac{40{,}8}{51} \times 100 = 80\%").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex(r"Purity: 10 g at 84\% = 8{,}4 g real $MgCO_3$ —").scale(0.9).shift(band_shift(5) + DOWN * 1.8)
        b5_l5 = Tex("only the 8{,}4 g enters the bridge").scale(1.0).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): definitions, pairs, two axes ---
        self.next_band(6)
        b6_t = Tex("Acid = proton donor; base = acceptor").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_eq = MathTex(r"NH_3 + H_2O \rightarrow NH_4^+ + OH^-").scale(1.1).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_eq))
        self.wait(2)
        b6_l1 = MathTex(r"\text{Pairs: } NH_4^+/NH_3 \; \text{ and } \; H_2O/OH^-").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex("Water plays both sides: AMPHOLYTE").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("Strong/weak = ionisation; conc/dilute").scale(1.0).shift(band_shift(6) + DOWN * 1.6)
        b6_l4 = Tex("= amount per volume — independent axes").scale(1.0).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l3))
        self.wait(1.5)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): the titration ---
        self.next_band(7)
        b7_t = Tex(r"Titration: 25 cm$^3$ of 0{,}2 KOH vs 20 cm$^3$ HNO$_3$").scale(0.95).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = MathTex(r"n(KOH) = cV = 0{,}2 \times 0{,}025 = 0{,}005").scale(1.0).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"1:1 \Rightarrow n(HNO_3) = 0{,}005 \text{ mol}").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = MathTex(r"c = \frac{0{,}005}{0{,}020} = 0{,}25 \text{ mol/dm}^3").scale(1.05).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex(r"Sulphuric acid? Ratio 1 : 2 — the most").scale(1.0).shift(band_shift(7) + DOWN * 1.8)
        b7_l5 = Tex("expensive titration slip there is").scale(1.0).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l4))
        self.wait(1.5)
        self.play(Write(b7_l5))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the currency exchange ---
        self.next_band(8)
        b8_t = Tex("The mole: the only currency exchange").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Grams, solutions, gas volumes:").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("none exchange directly — all via moles").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.wait(1.5)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex(r"Rates: periodic table, $c$ on the flask,").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        b8_l4 = Tex(r"22{,}4 dm$^3$/mol for ANY gas at STP").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l3))
        self.wait(1.5)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex(r"The skipped queue: cm$^3 \div 1000$ at the door").scale(1.0).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): pancakes and the empty shelf ---
        self.next_band(9)
        b9_t = Tex("Pancakes and the empty shelf").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Recipe: 1 cup flour + 3 eggs = 10 pancakes").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("Shelf: 4 cups flour, 9 eggs").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("Demand check: 4 cups need 12 eggs — have 9").scale(0.95).shift(band_shift(9) + DOWN * 0.5)
        b9_l4 = Tex("EGGS limit: 3 batches, 30 pancakes").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = MathTex(r"\text{Yield: } \frac{27}{30} \times 100 = 90\%").scale(1.0).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the proton pass and the trap list ---
        self.next_band(10)
        b10_t = Tex("The proton pass, and the trap list").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Acid passes the ball, base receives;").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("pairs = the player one ball apart").scale(1.0).shift(band_shift(10) + UP * 0.5)
        self.play(Write(b10_l1))
        self.wait(1.5)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("Traps: Celsius in gas laws; cm$^3$ unconverted;").scale(0.9).shift(band_shift(10) + DOWN * 0.4)
        b10_l4 = Tex("skipped mole ratio; excess reagent used;").scale(0.9).shift(band_shift(10) + DOWN * 1.1)
        b10_l5 = Tex("strong confused with concentrated").scale(0.9).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_l3))
        self.wait(1.5)
        self.play(Write(b10_l4))
        self.wait(1.5)
        self.play(Write(b10_l5))
        self.wait(2)
        b10_l6 = Tex("Final audit: disbelieve every answer once").scale(1.0).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
