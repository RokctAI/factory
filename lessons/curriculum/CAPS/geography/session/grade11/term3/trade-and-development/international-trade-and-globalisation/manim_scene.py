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

# Band-layout whiteboard scene for the session duo "International Trade and
# Globalisation" (grade 11, term 3). Covers all seven subtopics — Part 1
# Expert (subtopics 1-4) and Part 2 Simplifier (subtopics 5-7) — with band
# time apportioned to subtopics.json (220/235/235/230/185/195/200 of 1500 s).
# Exporter-safe primitives only: Tex/MathTex/Line/Arrow/Dot/Circle/Rectangle/
# SurroundingRectangle/VGroup; add-only lifecycle, camera moves between bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class InternationalTradeGlobalisationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): trade, exports, imports, what gets traded
        title = Tex("International Trade and Globalisation").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Exports: sold abroad \; Imports: bought in").scale(1.1).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex(r"Balance of trade $=$ exports $-$ imports").scale(1.1).shift(UP * 0.4)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex(r"Primary products: raw ore, crops, timber").scale(1.05).shift(DOWN * 0.6)
        b0_l4 = Tex(r"Manufactured goods: machines, medicines").scale(1.05).shift(DOWN * 1.4)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex(r"Value is added in the processing").scale(1.1).shift(DOWN * 2.4)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): SA profile + commodity rollercoaster
        self.next_band(1)
        b1_title = Tex("South Africa's trade profile").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_box = Rectangle(width=2.6, height=1.0).shift(band_shift(1) + UP * 0.8)
        b1_sa = Tex("SA").scale(1.1).shift(band_shift(1) + UP * 0.8)
        self.play(Create(b1_box), Write(b1_sa))
        b1_out = Arrow(band_shift(1) + UP * 0.8 + RIGHT * 1.4,
                       band_shift(1) + UP * 0.8 + RIGHT * 4.2, color=GREEN)
        b1_out_lab = Tex(r"platinum, gold, coal,\\ fruit, wine, vehicles").scale(0.9).shift(band_shift(1) + UP * 1.9 + RIGHT * 3.4)
        self.play(Create(b1_out), Write(b1_out_lab))
        self.wait(2)
        b1_in = Arrow(band_shift(1) + UP * 0.8 + LEFT * 4.2,
                      band_shift(1) + UP * 0.8 + LEFT * 1.4, color=RED)
        b1_in_lab = Tex(r"machinery,\\ fuel, medicines").scale(0.85).shift(band_shift(1) + UP * 1.9 + LEFT * 3.4)
        self.play(Create(b1_in), Write(b1_in_lab))
        self.wait(2.5)
        b1_l1 = Tex(r"Commodities: one world price, wild swings").scale(1.05).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex(r"Zambia rides copper; Nigeria rides oil").scale(1.05).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex(r"Vehicle exports: the value-added exception").scale(1.05).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): terms of trade
        self.next_band(2)
        b2_title = Tex("Terms of trade: what exports can buy").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Terms of trade} = \frac{\text{export prices}}{\text{import prices}}").scale(0.86).shift(band_shift(2) + UP * 0.9)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = Tex(r"Export prices rise faster $\Rightarrow$ improve").scale(1.05).shift(band_shift(2) + DOWN * 0.3)
        b2_l3 = Tex(r"Import prices outrun $\Rightarrow$ deteriorate").scale(1.05).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex(r"Primary prices fall vs manufactured —").scale(1.05).shift(band_shift(2) + DOWN * 2.1)
        b2_l5 = Tex(r"an escalator moving down").scale(1.1).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): trading relationships
        self.next_band(3)
        b3_title = Tex("Types of trading relationships").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Free trade: no tariffs — unequal players").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex(r"Protectionism: tariffs, quotas, subsidies").scale(1.05).shift(band_shift(3) + UP * 0.3)
        b3_l3 = Tex(r"Trade blocs: EU, SADC, AfCFTA").scale(1.05).shift(band_shift(3) + DOWN * 0.5)
        b3_l4 = Tex(r"Agreements: AGOA opens the US market").scale(1.05).shift(band_shift(3) + DOWN * 1.3)
        b3_l5 = Tex(r"Fair trade: floor price $+$ social premium").scale(1.05).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.wait(2)
        b3_l6 = Tex(r"Rich-world farm subsidies: the sore point").scale(1.05).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): globalisation and the TNC
        self.next_band(4)
        b4_title = Tex("Globalisation and the TNC").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Growing interconnection of economies").scale(1.05).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex(r"Drivers: containers, instant comms,\\ lower trade barriers").scale(0.94).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_hq = Circle(radius=0.35, color=YELLOW).shift(band_shift(4) + DOWN * 1.3)
        b4_hq_lab = Tex("HQ").scale(0.9).shift(band_shift(4) + DOWN * 1.3)
        self.play(Create(b4_hq), Write(b4_hq_lab))
        b4_a1 = Arrow(band_shift(4) + DOWN * 1.3 + LEFT * 0.5, band_shift(4) + DOWN * 1.9 + LEFT * 2.6)
        b4_a2 = Arrow(band_shift(4) + DOWN * 1.3 + RIGHT * 0.5, band_shift(4) + DOWN * 1.9 + RIGHT * 2.6)
        b4_f1 = Tex("factories abroad").scale(0.9).shift(band_shift(4) + DOWN * 2.3 + LEFT * 3.2)
        b4_f2 = Tex("markets everywhere").scale(0.9).shift(band_shift(4) + DOWN * 2.3 + RIGHT * 3.2)
        self.play(Create(b4_a1), Write(b4_f1))
        self.play(Create(b4_a2), Write(b4_f2))
        self.wait(2)
        b4_l3 = Tex(r"Toyota, Coca-Cola, Anglo American, MTN").scale(1.0).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l3))
        self.wait(3)

        # --- Band 5 (subtopic_3): gains and costs, two columns
        self.next_band(5)
        b5_title = Tex("Globalisation cuts both ways").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_mid = Line(band_shift(5) + UP * 1.6, band_shift(5) + DOWN * 2.2)
        self.play(Create(b5_mid))
        b5_gh = Tex("Gains", color=GREEN).scale(1.1).shift(band_shift(5) + UP * 1.3 + LEFT * 3.2)
        b5_ch = Tex("Costs", color=RED).scale(1.1).shift(band_shift(5) + UP * 1.3 + RIGHT * 3.2)
        self.play(Write(b5_gh), Write(b5_ch))
        self.wait(1.5)
        b5_g1 = Tex(r"sell to the\\ whole world").scale(0.95).shift(band_shift(5) + UP * 0.4 + LEFT * 3.2)
        b5_c1 = Tex(r"benefits concentrate\\ (core--periphery)").scale(0.95).shift(band_shift(5) + UP * 0.4 + RIGHT * 3.2)
        self.play(Write(b5_g1))
        self.play(Write(b5_c1))
        self.wait(2)
        b5_g2 = Tex(r"investment, jobs,\\ technology in").scale(0.95).shift(band_shift(5) + DOWN * 0.8 + LEFT * 3.2)
        b5_c2 = Tex(r"TNC power:\\ race to the bottom").scale(0.95).shift(band_shift(5) + DOWN * 0.8 + RIGHT * 3.2)
        self.play(Write(b5_g2))
        self.play(Write(b5_c2))
        self.wait(2)
        b5_g3 = Tex(r"cheaper goods,\\ East Asia lifted").scale(0.95).shift(band_shift(5) + DOWN * 2.0 + LEFT * 3.2)
        b5_c3 = Tex(r"infant industries hit;\\ 2008 shock spread").scale(0.95).shift(band_shift(5) + DOWN * 2.0 + RIGHT * 3.2)
        self.play(Write(b5_g3))
        self.play(Write(b5_c3))
        self.wait(2.5)
        b5_l1 = Tex(r"An engine that pulls unevenly").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): export-led development — the Korean ladder
        self.next_band(6)
        b6_title = Tex("Export-led development: the Tigers").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Korea, Taiwan, Singapore, Hong Kong").scale(1.0).shift(band_shift(6) + UP * 1.4)
        self.play(Write(b6_l1))
        self.wait(2)
        # Value ladder: ascending steps built from Lines, labelled as drawn.
        steps = [
            ("textiles", LEFT * 4.6 + DOWN * 2.2),
            ("steel", LEFT * 2.3 + DOWN * 1.5),
            ("ships", ORIGIN + DOWN * 0.8),
            ("cars", RIGHT * 2.3 + DOWN * 0.1),
            ("chips", RIGHT * 4.6 + UP * 0.6),
        ]
        prev = None
        for name, pos in steps:
            tread = Line(band_shift(6) + pos + LEFT * 0.9,
                         band_shift(6) + pos + RIGHT * 0.9, color=BLUE)
            lab = Tex(name).scale(0.9).shift(band_shift(6) + pos + DOWN * 0.45)
            if prev is not None:
                riser = Line(band_shift(6) + prev + RIGHT * 0.9,
                             band_shift(6) + pos + LEFT * 0.9, color=BLUE)
                self.play(Create(riser), run_time=0.5)
            self.play(Create(tread), Write(lab))
            self.wait(1.2)
            prev = pos
        b6_l2 = Tex(r"Earn, reinvest in schools, climb a rung").scale(1.0).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex(r"1960: Korea $\approx$ Ghana; now rich").scale(0.88).shift(band_shift(6) + UP * 0.6 + LEFT * 2.6)
        self.play(Write(b6_l3))
        self.wait(3)

        # --- Band 7 (subtopic_4): the critical examination + SA
        self.next_band(7)
        b7_title = Tex("Critically examined: five limits").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"1. Needs open, growing world markets").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex(r"2. Tigers' timing hard to replicate").scale(1.0).shift(band_shift(7) + UP * 0.5)
        b7_l3 = Tex(r"3. Brutal early rungs: low wages").scale(1.0).shift(band_shift(7) + DOWN * 0.2)
        b7_l4 = Tex(r"4. Vulnerable to shocks (2008)").scale(1.0).shift(band_shift(7) + DOWN * 0.9)
        b7_l5 = Tex(r"5. Environmental bill deferred: smog").scale(1.0).shift(band_shift(7) + DOWN * 1.6)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4, b7_l5):
            self.play(Write(m))
            self.wait(1.8)
        b7_l6 = Tex(r"SA: distance, electricity, skills, costs").scale(1.0).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_l6))
        self.wait(2)
        b7_l7 = Tex(r"A proven route, not a guaranteed one").scale(1.05).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(b7_l7))
        self.play(Create(SurroundingRectangle(b7_l7, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the spaza and the supermarket
        self.next_band(8)
        b8_title = Tex("The spaza and the supermarket").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_spaza = Rectangle(width=3.0, height=1.2).shift(band_shift(8) + UP * 0.7 + LEFT * 3.2)
        b8_sp_lab = Tex(r"Spaza:\\ raw, cheap").scale(0.95).shift(band_shift(8) + UP * 0.7 + LEFT * 3.2)
        self.play(Create(b8_spaza), Write(b8_sp_lab))
        b8_super = Rectangle(width=3.0, height=1.2).shift(band_shift(8) + UP * 0.7 + RIGHT * 3.2)
        b8_su_lab = Tex(r"Supermarket:\\ processed").scale(0.95).shift(band_shift(8) + UP * 0.7 + RIGHT * 3.2)
        self.play(Create(b8_super), Write(b8_su_lab))
        self.wait(2)
        b8_money = Arrow(band_shift(8) + UP * 0.1 + LEFT * 1.6,
                         band_shift(8) + UP * 0.1 + RIGHT * 1.6, color=RED)
        b8_m_lab = Tex("money trickles one way").scale(0.9).shift(band_shift(8) + DOWN * 0.5)
        self.play(Create(b8_money), Write(b8_m_lab))
        self.wait(2.5)
        b8_l1 = Tex(r"Beans: a few rand — roasted in Sandton:").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        b8_l2 = Tex(r"hundreds. Value stays with the processor").scale(1.0).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"Sell the coffee, not only the beans").scale(1.05).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): oranges for phones — the swap rate
        self.next_band(9)
        b9_title = Tex("Swapping bags of oranges for phones").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"\text{This year: } 1 \text{ bag} = 1 \text{ phone}").scale(1.1).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = MathTex(r"\text{Next year: } 3 \text{ bags} = 1 \text{ phone}").scale(1.1).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex(r"Working harder, affording less —").scale(1.05).shift(band_shift(9) + DOWN * 0.6)
        b9_l4 = Tex(r"terms of trade deteriorated").scale(1.05).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex(r"Team rules: SADC, AfCFTA, AGOA, fair trade").scale(1.0).shift(band_shift(9) + DOWN * 2.2)
        self.play(Write(b9_l5))
        self.wait(2)
        b9_l6 = Tex(r"Argue the farm subsidies in any essay").scale(1.0).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l6))
        self.wait(3)

        # --- Band 10 (subtopic_7): the ladder the Tigers climbed
        self.next_band(10)
        b10_title = Tex("The ladder the Tigers climbed").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"T-shirts $\to$ steel $\to$ ships $\to$ cars $\to$ chips").scale(0.95).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex(r"Bank every dollar, buy the next rung").scale(1.05).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex(r"Warnings: buyers needed at the top,").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        b10_l4 = Tex(r"brutal bottom rungs, shocks, smog").scale(1.0).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex(r"SA climbs with a heavy backpack:\\ load-shedding, skills gap").scale(0.9).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10_l5))
        self.wait(2.5)
        b10_l6 = Tex(r"A real ladder — not an escalator").scale(1.1).shift(band_shift(10) + DOWN * 3.1)
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
