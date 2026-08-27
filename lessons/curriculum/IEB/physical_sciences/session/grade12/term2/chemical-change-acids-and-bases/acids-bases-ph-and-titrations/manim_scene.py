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

# Band-layout whiteboard scene for "Acids, Bases, pH and Titrations"
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe vocabulary only; hand-built from Line/Dot/Tex.
# Write-only reveals.
# Subtopic durations 240/245/245/250/195/200/200 of 1575 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AcidsBasesTitrationsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the two definitions + conjugate pairs ---
        title = Tex("Acids, Bases, pH and Titrations").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Lowry-Br\\o{}nsted: acid $=$ PROTON DONOR").scale(0.95).shift(UP * 1.2)
        b0_l2 = Tex("base $=$ PROTON ACCEPTOR").scale(0.95).shift(UP * 0.4)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(2.5)
        b0_eq = MathTex(r"HNO_3 + H_2O \rightarrow NO_3^- + H_3O^+").scale(1.0).shift(DOWN * 0.6)
        self.play(Write(b0_eq))
        self.wait(2.5)
        b0_l3 = Tex("pairs differ by ONE proton:").scale(0.9).shift(DOWN * 1.6)
        b0_l4 = Tex("$HNO_3/NO_3^-$ and $H_3O^+/H_2O$").scale(0.9).shift(DOWN * 2.4)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): ampholytes and proton supply ---
        self.next_band(1)
        b1_title = Tex("Ampholytes and proton supply").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = Tex("water: gives to ammonia, takes from nitric acid").scale(0.9).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = Tex("also ampholytes: $HCO_3^-$, $HSO_4^-$").scale(0.95).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("monoprotic: HCl, HNO$_3$ — one proton each").scale(0.9).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = Tex("diprotic: H$_2$SO$_4$ — TWO, and it will matter").scale(0.9).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): strength vs concentration, K_a ---
        self.next_band(2)
        b2_title = Tex("Strength is not concentration").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = Tex("STRONG: ionises completely — HCl, HNO$_3$, H$_2$SO$_4$").scale(0.85).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("WEAK: partial, an equilibrium — ethanoic, carbonic").scale(0.85).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("CONCENTRATED / DILUTE: moles per dm$^3$ — a different axis").scale(0.8).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex("$K_a$ large: strong. $K_a$ tiny: weak.").scale(0.95).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("bench test: lower pH, better conduction, faster fizz").scale(0.85).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_3): pH calculations 1 and 2 ---
        self.next_band(3)
        b3_eq = MathTex(r"pH = -\log[H_3O^+]").scale(1.15).shift(band_shift(3) + UP * 2.0)
        self.play(Write(b3_eq))
        self.play(Create(SurroundingRectangle(b3_eq, color=GREEN)))
        self.wait(2.5)
        b3_l1 = Tex("HNO$_3$ at 0,001: $[H_3O^+] = 10^{-3}$, pH $= 3$").scale(0.9).shift(band_shift(3) + UP * 0.8)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = Tex("H$_2$SO$_4$ at 0,005: TWO protons").scale(0.9).shift(band_shift(3) + DOWN * 0.2)
        b3_l3 = MathTex(r"[H_3O^+] = 2 \times 0{,}005 = 0{,}01 \Rightarrow pH = 2").scale(0.95).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("the factor of two comes BEFORE the log").scale(0.9).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): base through K_w + the weak-acid caveat ---
        self.next_band(4)
        b4_title = Tex("Bases go through $K_w$").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"K_w = [H_3O^+][OH^-] = 10^{-14}").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(2.5)
        b4_l2 = Tex("KOH at 0,01: $[OH^-] = 10^{-2}$").scale(0.9).shift(band_shift(4) + UP * 0.1)
        b4_l3 = MathTex(r"[H_3O^+] = 10^{-14} / 10^{-2} = 10^{-12} \Rightarrow pH = 12").scale(0.9).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_wrong = Tex("Ethanoic acid at 0,001 has pH 3").scale(0.9).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_wrong))
        self.play(Create(strike(b4_wrong)))
        self.wait(2)
        b4_l4 = Tex("weak: partly ionised — pH lands near 3,9").scale(0.9).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_4): the four-line titration ---
        self.next_band(5)
        b5_title = Tex("Titration: 30 cm$^3$ KOH vs 15 cm$^3$ of 0,2 HNO$_3$").scale(0.9).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"n_{acid} = 0{,}2 \times 0{,}015 = 0{,}003\ \text{mol}").scale(0.95).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("ratio 1:1, so $n_{base} = 0{,}003$ mol").scale(0.95).shift(band_shift(5) + UP * 0.2)
        b5_l3 = MathTex(r"c = 0{,}003 \div 0{,}030 = 0{,}1\ \text{mol·dm}^{-3}").scale(0.95).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex("volumes to dm$^3$ FIRST; sulfuric acid brings a factor 2").scale(0.85).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): salts and indicator choice ---
        self.next_band(6)
        b6_title = Tex("The salt sets the equivalence pH").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("strong + strong: neutral — bromothymol blue").scale(0.9).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("weak acid + strong base: BASIC — phenolphthalein").scale(0.9).shift(band_shift(6) + UP * 0.2)
        b6_l3 = Tex("strong acid + weak base: ACIDIC — methyl orange").scale(0.9).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_rule = Tex("the STRONG parent wins; flip at the equivalence pH").scale(0.9).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_rule))
        self.play(Create(SurroundingRectangle(b6_rule, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): givers and takers ---
        self.next_band(7)
        b7_title = Tex("Givers and takers").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("one parcel: the proton").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("acid gives, base takes — every reaction one hand-off").scale(0.9).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex("giver minus parcel $=$ its conjugate base").scale(0.9).shift(band_shift(7) + DOWN * 0.8)
        b7_l4 = Tex("count hydrogens: pairs differ by exactly one").scale(0.9).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("water: the utility player — gives OR takes").scale(0.9).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): the cordial picture ---
        self.next_band(8)
        b8_title = Tex("Strong is not concentrated").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("amount of syrup $=$ CONCENTRATION").scale(0.95).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("eagerness to split $=$ STRENGTH ($K_a$)").scale(0.95).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex("battery acid: concentrated strong").scale(0.85).shift(band_shift(8) + DOWN * 0.7)
        b8_l4 = Tex("pool drops: dilute strong. vinegar: concentrated weak.").scale(0.85).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("symptoms: pH, conductivity, fizz").scale(0.9).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_7): ladder of tens + the exact balance ---
        self.next_band(9)
        b9_title = Tex("The ladder of tens; the exact balance").scale(1.05).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("every pH rung: a factor of TEN").scale(0.95).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.play(Create(SurroundingRectangle(b9_l1, color=GREEN)))
        self.wait(2.5)
        b9_l2 = Tex("rung 7: equal, tiny crowds of $H_3O^+$ and $OH^-$").scale(0.85).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("titration: drop by drop until givers $=$ takers").scale(0.9).shift(band_shift(9) + DOWN * 0.8)
        b9_l4 = Tex("indicator: the dye that shouts at the balance").scale(0.9).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("the salt takes after its STRONGER parent").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(4)
