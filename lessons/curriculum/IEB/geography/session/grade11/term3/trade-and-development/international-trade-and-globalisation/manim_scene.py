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

# Band-layout whiteboard scene for the IEB Grade 11 Geography session duo
# "International Trade and Globalisation". One band per teaching beat; the
# camera moves down, nothing is removed. Text-led with primitive accents.
# Subtopic shares follow subtopics.json: 220/235/235/230/185/195/200 of 1500 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class InternationalTradeGlobalisationIEBSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): trade, exports, imports, what gets traded
        title = Tex("International Trade and Globalisation").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex("Exports $-$ imports $=$ balance of trade").scale(1.0).shift(UP * 1.1)
        self.play(Write(s0_l1))
        self.wait(2.5)
        s0_l2 = Tex("PRIMARY: raw ores, crops, timber").scale(1.0).shift(UP * 0.2)
        s0_l3 = Tex("MANUFACTURED: skill and technology").scale(1.0).shift(DOWN * 0.6)
        s0_l3b = Tex("folded in — machines, medicines").scale(1.0).shift(DOWN * 1.4)
        self.play(Write(s0_l2))
        self.wait(2)
        self.play(Write(s0_l3))
        self.play(Write(s0_l3b))
        self.wait(2.5)
        s0_l4 = Tex("Raw out, machines in: sell cheap, buy dear").scale(0.95).shift(DOWN * 2.4)
        self.play(Write(s0_l4))
        self.play(Create(SurroundingRectangle(s0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): SA profile + commodity rollercoaster
        self.next_band(1)
        b1_title = Tex("World markets and the rollercoaster").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("One ruling world price — no small").scale(0.95).shift(band_shift(1) + UP * 1.2)
        b1_l1b = Tex("producer moves it; prices lurch").scale(0.95).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1))
        self.play(Write(b1_l1b))
        self.wait(2.5)
        b1_l2 = Tex("Angola swings with oil; Botswana").scale(0.95).shift(band_shift(1) + DOWN * 0.5)
        b1_l2b = Tex("with diamonds — no steering wheel").scale(0.95).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(b1_l2))
        self.play(Write(b1_l2b))
        self.wait(2.5)
        b1_l3 = Tex("SA: PGMs, gold, coal, ore out;").scale(0.95).shift(band_shift(1) + DOWN * 2.2)
        b1_l3b = Tex("machines in — vehicles the exception").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l3))
        self.play(Write(b1_l3b))
        self.play(Create(SurroundingRectangle(b1_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): terms of trade
        self.next_band(2)
        b2_title = Tex("Terms of trade: the swap rate").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"Terms of trade $=$ export prices $\div$").scale(0.95).shift(band_shift(2) + UP * 1.2)
        b2_l1b = Tex("import prices").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.play(Write(b2_l1b))
        self.wait(2.5)
        b2_l2 = Tex("Primary prices slide against manufactures:").scale(0.9).shift(band_shift(2) + DOWN * 0.5)
        b2_l2b = Tex("substitution vs patents and brands").scale(0.9).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(b2_l2))
        self.play(Write(b2_l2b))
        self.wait(2.5)
        b2_l3 = Tex("Raw exporters: running up an").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        b2_l3b = Tex("escalator that is moving down").scale(0.95).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l3))
        self.play(Write(b2_l3b))
        self.play(Create(SurroundingRectangle(b2_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): trading relationships
        self.next_band(3)
        b3_title = Tex("Trading relationships, matched").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Free trade: no tariffs — unequal players").scale(0.9).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("Protection: rich farm subsidies undercut").scale(0.9).shift(band_shift(3) + UP * 0.4)
        b3_l2b = Tex("African farmers at home").scale(0.9).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.play(Write(b3_l2b))
        self.wait(2)
        b3_l3 = Tex("Blocs: EU, SADC, AfCFTA — one African").scale(0.9).shift(band_shift(3) + DOWN * 1.3)
        b3_l3b = Tex("market; AGOA: preferential US entry").scale(0.9).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l3))
        self.play(Write(b3_l3b))
        self.wait(2)
        b3_l4 = Tex("Fair trade: floor price plus premium").scale(0.9).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): globalisation and the TNC
        self.next_band(4)
        b4_title = Tex("Globalisation and the TNC").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Drivers: the container, instant").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l1b = Tex("communication, lowered barriers").scale(0.95).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1))
        self.play(Write(b4_l1b))
        self.wait(2.5)
        b4_l2 = Tex("TNC: HQ in one country, factories in").scale(0.95).shift(band_shift(4) + DOWN * 0.5)
        b4_l2b = Tex("others, customers everywhere").scale(0.95).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4_l2))
        self.play(Write(b4_l2b))
        self.wait(2.5)
        b4_l3 = Tex("Samsung, Nestl\\'e, Sasol, Shoprite").scale(0.95).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): gains and costs, two columns
        self.next_band(5)
        b5_title = Tex("Two columns, both required").scale(1.1).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        gains_h = Tex("Gains").scale(0.95).shift(band_shift(5) + LEFT * 3.2 + UP * 1.4)
        costs_h = Tex("Costs").scale(0.95).shift(band_shift(5) + RIGHT * 3.2 + UP * 1.4)
        divider = Line(UP * 1.8, DOWN * 3.4, color=WHITE).shift(band_shift(5))
        self.play(Write(gains_h), Write(costs_h), Create(divider))
        self.wait(1.5)
        g1 = Tex("world markets").scale(0.8).shift(band_shift(5) + LEFT * 3.2 + UP * 0.6)
        g2 = Tex("investment, technology").scale(0.8).shift(band_shift(5) + LEFT * 3.2 + DOWN * 0.2)
        g3 = Tex("millions of jobs").scale(0.8).shift(band_shift(5) + LEFT * 3.2 + DOWN * 1.0)
        g4 = Tex("cheaper goods").scale(0.8).shift(band_shift(5) + LEFT * 3.2 + DOWN * 1.8)
        c1 = Tex("benefits cluster").scale(0.8).shift(band_shift(5) + RIGHT * 3.2 + UP * 0.6)
        c2 = Tex("race to the bottom").scale(0.8).shift(band_shift(5) + RIGHT * 3.2 + DOWN * 0.2)
        c3 = Tex("infant industries crushed").scale(0.8).shift(band_shift(5) + RIGHT * 3.2 + DOWN * 1.0)
        c4 = Tex("shocks transmitted: 2008").scale(0.8).shift(band_shift(5) + RIGHT * 3.2 + DOWN * 1.8)
        for m in (g1, c1, g2, c2, g3, c3, g4, c4):
            self.play(Write(m), run_time=0.6)
        self.wait(1.5)
        b5_l1 = Tex("An engine that pulls unevenly").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): export-led development — the Korean ladder
        self.next_band(6)
        b6_title = Tex("The Tigers' ladder").scale(1.15).shift(band_shift(6) + UP * 2.6)
        self.play(Write(b6_title))
        self.wait(1.5)
        rungs = [
            ("textiles", LEFT * 4.6 + DOWN * 2.0),
            ("steel", LEFT * 2.3 + DOWN * 1.2),
            ("ships", UP * 0.0 + DOWN * 0.4),
            ("cars", RIGHT * 2.3 + UP * 0.4),
            ("semiconductors", RIGHT * 4.4 + UP * 1.2),
        ]
        prev = None
        for label, pos in rungs:
            t = Tex(label).scale(0.85).shift(band_shift(6) + pos)
            self.play(Write(t), run_time=0.6)
            if prev is not None:
                self.play(Create(Line(prev + RIGHT * 0.8, pos + LEFT * 1.2,
                                      color=YELLOW).shift(band_shift(6))), run_time=0.4)
            prev = pos
            self.wait(0.6)
        b6_l1 = Tex("Earn abroad, reinvest in schools and").scale(0.9).shift(band_shift(6) + DOWN * 2.9)
        b6_l1b = Tex("infrastructure — the state steered").scale(0.9).shift(band_shift(6) + DOWN * 3.6)
        self.play(Write(b6_l1))
        self.play(Write(b6_l1b))
        self.play(Create(SurroundingRectangle(b6_l1b, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the critical examination + SA
        self.next_band(7)
        b7_title = Tex("Read the warnings on the label").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Needs open markets; conditions were").scale(0.95).shift(band_shift(7) + UP * 1.2)
        b7_l1b = Tex("unrepeatable; bottom rungs bruise").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l1b))
        self.wait(2.5)
        b7_l2 = Tex("Shocks imported (2008); environmental").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        b7_l2b = Tex("bill deferred into smog").scale(0.95).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(b7_l2))
        self.play(Write(b7_l2b))
        self.wait(2.5)
        b7_l3 = Tex("SA: on the ladder — with a heavy").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        b7_l3b = Tex("backpack of power, distance, skills").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l3))
        self.play(Write(b7_l3b))
        self.play(Create(SurroundingRectangle(b7_l3b, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the spaza and the supermarket
        self.next_band(8)
        b8_title = Tex("The spaza and the supermarket").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Spaza: sells cheap raw things,").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8_l1b = Tex("buys dear processed things").scale(0.95).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.play(Write(b8_l1b))
        self.wait(2.5)
        b8_l2 = Tex("Beans: a few rand; branded slabs:").scale(0.95).shift(band_shift(8) + DOWN * 0.5)
        b8_l2b = Tex("hundreds — value stays with processing").scale(0.95).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l2))
        self.play(Write(b8_l2b))
        self.wait(2.5)
        b8_l3 = Tex("SA plays both ends: ore out spaza-style,").scale(0.9).shift(band_shift(8) + DOWN * 2.2)
        b8_l3b = Tex("cars out supermarket-style").scale(0.9).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l3))
        self.play(Write(b8_l3b))
        self.play(Create(SurroundingRectangle(b8_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): oranges for phones — the swap rate
        self.next_band(9)
        b9_title = Tex("Oranges for phones: the swap rate").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("This year: 1 bag $=$ 1 phone;").scale(0.95).shift(band_shift(9) + UP * 1.2)
        b9_l1b = Tex("next season: 4 bags $=$ 1 phone").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1))
        self.play(Write(b9_l1b))
        self.play(Create(SurroundingRectangle(b9_l1b, color=RED)))
        self.wait(2.5)
        b9_l2 = Tex("Anyone grows oranges; few build phones —").scale(0.9).shift(band_shift(9) + DOWN * 0.5)
        b9_l2b = Tex("patents and brands hold the price").scale(0.9).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l2))
        self.play(Write(b9_l2b))
        self.wait(2.5)
        b9_l3 = Tex("Team rules: SADC, AfCFTA, AGOA,").scale(0.95).shift(band_shift(9) + DOWN * 2.2)
        b9_l3b = Tex("fair trade floors — and subsidies to argue").scale(0.9).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l3))
        self.play(Write(b9_l3b))
        self.play(Create(SurroundingRectangle(b9_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the ladder the Tigers climbed
        self.next_band(10)
        b10_title = Tex("The ladder the Tigers climbed").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("T-shirts, schools and steel, ships,").scale(0.95).shift(band_shift(10) + UP * 1.2)
        b10_l1b = Tex("cars, semiconductors — bank every dollar").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l1b))
        self.wait(2.5)
        b10_l2 = Tex("Warnings: buyers needed at the top;").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        b10_l2b = Tex("bruising rungs; shocks; smog").scale(0.95).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l2))
        self.play(Write(b10_l2b))
        self.wait(2.5)
        b10_l3 = Tex("A ladder, not an escalator — grip with").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        b10_l3b = Tex("education, infrastructure, capable state").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l3))
        self.play(Write(b10_l3b))
        self.play(Create(SurroundingRectangle(b10_l3b, color=GREEN)))
        self.wait(4)
