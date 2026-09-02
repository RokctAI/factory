# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from manim import *

# Band-layout whiteboard scene for the acid-base definitions session duo.
# Covers all seven subtopics (Part 1 Expert: subtopics 1-4, Part 2
# Simplifier: subtopics 5-7) with band time proportional to subtopics.json
# (235/235/245/235/195/205/210 of 1560 s). Add-only lifecycle: nothing is
# faded out; the camera moves down to a fresh band for every teaching step.
# Only exporter-safe mobjects are used (Tex/MathTex/Line/Dot/Rectangle).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AcidBaseDefinitionsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): Arrhenius and its failures ---
        title = Tex("What Makes an Acid an Acid?").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Arrhenius acid: gives $H^+$ in water").scale(1.1).shift(UP * 1.1)
        b0_l2 = Tex(r"Arrhenius base: gives $OH^-$ in water").scale(1.1).shift(UP * 0.2)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("Two failures: works only in water,").scale(1.1).shift(DOWN * 0.9)
        b0_l4 = Tex(r"and cannot explain $NH_3$ (no $OH^-$!)").scale(1.1).shift(DOWN * 1.8)
        self.play(Write(b0_l3))
        self.wait(1.5)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): Bronsted-Lowry, both dissolutions ---
        self.next_band(1)
        b1_t = Tex("Bronsted-Lowry: follow the proton").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_l1 = Tex("Acid = proton DONOR").scale(1.15).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("Base = proton ACCEPTOR").scale(1.15).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l1))
        self.wait(1.5)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_eq1 = MathTex(r"HCl + H_2O \rightarrow H_3O^+ + Cl^-").scale(1.15).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_eq1))
        self.wait(2)
        b1_n1 = Tex("HCl donates: acid. Water accepts: base").scale(1.0).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_n1))
        self.wait(2)
        b1_eq2 = MathTex(r"NH_3 + H_2O \rightleftharpoons NH_4^+ + OH^-").scale(1.0).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(b1_eq2))
        self.wait(2)
        b1_n2 = Tex(r"$NH_3$ accepts: base. Water donates: acid").scale(1.0).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_n2))
        self.wait(3)

        # --- Band 2 (subtopic_2): conjugate pairs from the HCl equation ---
        self.next_band(2)
        b2_t = Tex("Conjugate acid-base pairs").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = Tex("Two species, exactly ONE proton apart").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_eq = MathTex(r"HCl + H_2O \rightarrow H_3O^+ + Cl^-").scale(1.15).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_eq))
        self.wait(2)
        b2_p1 = MathTex(r"\text{Pair 1: } HCl \;/\; Cl^-").scale(1.1).shift(band_shift(2) + DOWN * 0.8)
        b2_p2 = MathTex(r"\text{Pair 2: } H_3O^+ \;/\; H_2O").scale(1.1).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_p1))
        self.wait(2)
        self.play(Write(b2_p2))
        self.wait(2)
        b2_n = Tex("The partner WITH the proton is the acid").scale(1.0).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_n))
        self.wait(3)

        # --- Band 3 (subtopic_2): ammonia's pairs, and the traps ---
        self.next_band(3)
        b3_eq = MathTex(r"NH_3 + H_2O \rightleftharpoons NH_4^+ + OH^-").scale(1.0).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_eq))
        self.wait(2)
        b3_p1 = MathTex(r"\text{Pair 1: } NH_4^+ \;/\; NH_3").scale(1.1).shift(band_shift(3) + UP * 1.2)
        b3_p2 = MathTex(r"\text{Pair 2: } H_2O \;/\; OH^-").scale(1.1).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_p1))
        self.wait(2)
        self.play(Write(b3_p2))
        self.wait(2)
        b3_wrong = MathTex(r"H_2SO_4 \;/\; SO_4^{2-} \text{ a pair?}").scale(1.1).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_fix1 = MathTex(r"\text{TWO H apart: } H_2SO_4 / HSO_4^-").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        b3_fix2 = MathTex(r"\text{then } HSO_4^- / SO_4^{2-}").scale(1.0).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_fix1))
        self.wait(2)
        self.play(Write(b3_fix2))
        self.wait(2)
        b3_n = Tex("Pairs sit diagonal, never side-by-side").scale(1.0).shift(band_shift(3) + DOWN * 3.2)
        self.play(Write(b3_n))
        self.wait(3)

        # --- Band 4 (subtopic_3): ampholytes — HCO3- both ways ---
        self.next_band(4)
        b4_t = Tex(r"Ampholyte: acid OR base — $HCO_3^-$").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_a = Tex("As an acid (donates):").scale(1.05).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_a))
        b4_eq1 = MathTex(r"HCO_3^- + H_2O \rightleftharpoons CO_3^{2-} + H_3O^+").scale(0.9).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_eq1))
        self.wait(2.5)
        b4_b = Tex("As a base (accepts):").scale(1.05).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4_b))
        b4_eq2 = MathTex(r"HCO_3^- + H_2O \rightleftharpoons H_2CO_3 + OH^-").scale(0.9).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4_eq2))
        self.wait(2.5)
        b4_n = Tex(r"Water and $HSO_4^-$ do the same trick").scale(1.0).shift(band_shift(4) + DOWN * 2.3)
        self.play(Write(b4_n))
        self.wait(3)

        # --- Band 5 (subtopic_3): the three reactions of acids ---
        self.next_band(5)
        b5_t = Tex("Three reactions of acids").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_r1 = MathTex(r"HCl + NaOH \rightarrow NaCl + H_2O").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_r1))
        self.wait(2)
        b5_r2 = MathTex(r"2HCl + MgO \rightarrow MgCl_2 + H_2O").scale(1.05).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_r2))
        self.wait(2)
        b5_r3 = MathTex(r"2HCl + Na_2CO_3 \rightarrow 2NaCl + H_2O + CO_2").scale(1.0).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_r3))
        self.wait(2)
        b5_r4 = MathTex(r"H_2SO_4 + CaCO_3 \rightarrow CaSO_4 + H_2O + CO_2").scale(1.0).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_r4))
        self.wait(2)
        b5_n = Tex(r"Carbonates add the bonus gas: $CO_2$ fizz").scale(1.05).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_n))
        self.play(Create(SurroundingRectangle(b5_n, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the four indicators ---
        self.next_band(6)
        b6_t = Tex("Indicators: four spies, eight colours").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = Tex("Litmus: RED acid, BLUE base").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("Methyl orange: RED acid, YELLOW base").scale(1.05).shift(band_shift(6) + UP * 0.2)
        b6_l3 = Tex("Bromothymol blue: YELLOW acid, BLUE base").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        b6_l4 = Tex("...and GREEN at neutral — the only one").scale(1.05).shift(band_shift(6) + DOWN * 1.6)
        b6_l5 = Tex("Phenolphthalein: COLOURLESS acid, PINK base").scale(1.0).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(1.5)
        self.play(Write(b6_l4))
        self.wait(2)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): reading the changeover ---
        self.next_band(7)
        b7_t = Tex("Watching a neutralisation").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("Acid dripped into base + phenolphthalein:").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("pink holds... then VANISHES at changeover").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("Bromothymol blue on the same journey:").scale(1.05).shift(band_shift(7) + DOWN * 0.8)
        b7_l4 = Tex("blue, GREEN at neutral, yellow in excess").scale(1.05).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): pass-the-ball ---
        self.next_band(8)
        b8_t = Tex("Acid-base is pass-the-ball").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex(r"The ball is a proton, $H^+$").scale(1.1).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("Thrower = acid, catcher = base").scale(1.1).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_eq = MathTex(r"NH_3 + H_2O \rightleftharpoons NH_4^+ + OH^-").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_eq))
        self.wait(2)
        b8_l3 = Tex(r"Here WATER throws — $NH_3$ is the catcher").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        b8_l4 = Tex(r"and $OH^-$ is made at the moment of the catch").scale(1.0).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): pairs as before/after photos ---
        self.next_band(9)
        b9_t = Tex("Before-and-after photos").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("A pair = same player, one proton apart").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = MathTex(r"HCl \;/\; Cl^- \qquad H_3O^+ \;/\; H_2O").scale(1.1).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("Water throws at ammonia, catches from HCl:").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        b9_l4 = Tex("the player who plays both sides — ampholyte").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex(r"Show it: write TWO equations for $HCO_3^-$").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): three fizzes, four colour changes ---
        self.next_band(10)
        b10_t = Tex("Three trades, one fizz").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Acid + hydroxide: salt + water").scale(1.05).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("Acid + metal oxide: salt + water").scale(1.05).shift(band_shift(10) + UP * 0.2)
        b10_l3 = Tex(r"Acid + carbonate: salt + water + $CO_2$").scale(1.05).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10_l1))
        self.wait(2)
        self.play(Write(b10_l2))
        self.wait(2)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2)
        b10_l4 = Tex("Vinegar on baking soda = the school volcano").scale(1.0).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("The spies: litmus, methyl orange,").scale(1.0).shift(band_shift(10) + DOWN * 2.5)
        b10_l6 = Tex("bromothymol blue (green!), phenolphthalein").scale(1.0).shift(band_shift(10) + DOWN * 3.2)
        self.play(Write(b10_l5))
        self.wait(1.5)
        self.play(Write(b10_l6))
        self.wait(4)
