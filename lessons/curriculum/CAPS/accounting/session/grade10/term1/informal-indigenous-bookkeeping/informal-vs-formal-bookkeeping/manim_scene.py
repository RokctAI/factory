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

# Band-layout whiteboard scene for informal vs formal bookkeeping duo.
# Exporter-safe primitives only; write-only reveals; camera moves down bands.
# Band time follows subtopics.json (160/170/170/190/170/160/160 of 1180 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class InformalVsFormalBookkeepingSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(13)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): two sectors, one set of concepts ---
        title = Tex("Informal vs Formal Bookkeeping").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("Formal: registered, full records, banked,").scale(1.0).shift(UP * 1.0)
        l02 = Tex("answers to SARS, banks, auditors").scale(1.0).shift(UP * 0.2)
        self.play(Write(l01)); self.play(Write(l02)); self.wait(2.5)
        l03 = Tex("Informal: spaza, street vendor —").scale(1.0).shift(DOWN * 0.7)
        l04 = Tex("few or no written records").scale(1.0).shift(DOWN * 1.5)
        self.play(Write(l03)); self.play(Write(l04)); self.wait(2)
        l05 = Tex("Same CONCEPTS — only the RECORDING differs").scale(1.0).shift(DOWN * 2.5)
        self.play(Write(l05))
        self.play(Create(SurroundingRectangle(l05, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the vocabulary ---
        self.next_band(1)
        b1_t = Tex("The vocabulary that carries marks").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_t)); self.wait(1.5)
        b1_l1 = Tex("Capital: owner's resources put in").scale(1.0).shift(band_shift(1) + UP * 1.4)
        b1_l2 = Tex("Fixed assets: kept for USE, not sale").scale(1.0).shift(band_shift(1) + UP * 0.6)
        b1_l3 = Tex("Stock: goods bought to resell").scale(1.0).shift(band_shift(1) + DOWN * 0.2)
        b1_l4 = Tex("Cost price paid; selling price charged").scale(1.0).shift(band_shift(1) + DOWN * 1.0)
        b1_l5 = Tex("Income earned; expenses consumed").scale(1.0).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l1)); self.wait(1.5)
        self.play(Write(b1_l2)); self.wait(1.5)
        self.play(Write(b1_l3)); self.wait(1.5)
        self.play(Write(b1_l4)); self.wait(1.5)
        self.play(Write(b1_l5)); self.wait(1.5)
        b1_l6 = MathTex(r"\text{Profit} = \text{income} - \text{expenses}").scale(1.1).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l6))
        self.play(Create(SurroundingRectangle(b1_l6, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the comparison, first concepts ---
        self.next_band(2)
        b2_t = Tex("Two columns, same concepts").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_t)); self.wait(1.5)
        divider = Line(UP * 1.8, DOWN * 2.6, stroke_width=3).shift(band_shift(2))
        self.play(Create(divider))
        b2_h1 = Tex("Supermarket").scale(1.0).move_to([-3.2, 1.5, 0]).shift(band_shift(2))
        b2_h2 = Tex("Spaza").scale(1.0).move_to([3.2, 1.5, 0]).shift(band_shift(2))
        self.play(Write(b2_h1), Write(b2_h2)); self.wait(1.5)
        b2_l1 = Tex("Capital: R500 000 banked").scale(0.9).move_to([-3.2, 0.6, 0]).shift(band_shift(2))
        b2_r1 = Tex("R3 000 cash saved").scale(0.9).move_to([3.2, 0.6, 0]).shift(band_shift(2))
        self.play(Write(b2_l1)); self.play(Write(b2_r1)); self.wait(2)
        b2_l2 = Tex("Assets: tills, vehicle").scale(0.9).move_to([-3.2, -0.3, 0]).shift(band_shift(2))
        b2_r2 = Tex("fridge and a table").scale(0.9).move_to([3.2, -0.3, 0]).shift(band_shift(2))
        self.play(Write(b2_l2)); self.play(Write(b2_r2)); self.wait(2)
        b2_l3 = Tex("Stock: invoiced, counted").scale(0.9).move_to([-3.2, -1.2, 0]).shift(band_shift(2))
        b2_r3 = Tex("bread, airtime, cooldrinks").scale(0.9).move_to([3.2, -1.2, 0]).shift(band_shift(2))
        self.play(Write(b2_l3)); self.play(Write(b2_r3)); self.wait(2)
        b2_l4 = Tex("Wages recorded").scale(0.9).move_to([-3.2, -2.1, 0]).shift(band_shift(2))
        b2_r4 = Tex("owner pays herself nothing").scale(0.9).move_to([3.2, -2.1, 0]).shift(band_shift(2))
        self.play(Write(b2_l4)); self.play(Write(b2_r4))
        self.wait(3)

        # --- Band 3 (subtopic_2): prices and the invisible labour ---
        self.next_band(3)
        b3_t = Tex("Same calculation, different recording").scale(1.1).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_t)); self.wait(1.5)
        b3_l1 = Tex("Cooldrink: cost R8, sells R12").scale(1.05).shift(band_shift(3) + UP * 1.3)
        b3_l2 = MathTex(r"\text{margin} = 12 - 8 = \text{R4}").scale(1.1).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1)); self.wait(2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = Tex("Unpaid own labour = INVISIBLE labour cost —").scale(0.95).shift(band_shift(3) + DOWN * 0.6)
        b3_l4 = Tex("it quietly overstates her profit").scale(1.0).shift(band_shift(3) + DOWN * 1.4)
        self.play(Write(b3_l3)); self.play(Write(b3_l4)); self.wait(2.5)
        b3_l5 = Tex("Month end: count the tin — in minus out —").scale(0.95).shift(band_shift(3) + DOWN * 2.3)
        b3_l6 = Tex("accounting's oldest equation, no ledger needed").scale(0.95).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(b3_l5)); self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): where the difference bites ---
        self.next_band(4)
        b4_t = Tex("Where the difference bites").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_t)); self.wait(1.5)
        b4_l1 = Tex("1. Proof: no records, no loan —").scale(1.0).shift(band_shift(4) + UP * 1.3)
        b4_l2 = Tex("unrecorded success is invisible success").scale(1.0).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l1)); self.play(Write(b4_l2)); self.wait(2.5)
        b4_l3 = Tex("2. Accuracy: unrecorded expenses leak,").scale(1.0).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex("inflating apparent profit").scale(1.0).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(b4_l3)); self.play(Write(b4_l4)); self.wait(2.5)
        b4_l5 = Tex("3. Separation: business tin $\\neq$ household purse").scale(0.95).shift(band_shift(4) + DOWN * 2.1)
        b4_l6 = Tex("4. Continuity: records survive; memory does not").scale(0.95).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l5)); self.wait(2)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_4): indigenous practices ---
        self.next_band(5)
        b5_t = Tex("Indigenous practices: the original bookkeeping").scale(1.0).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_t)); self.wait(2)
        b5_l1 = Tex("Stokvel: contributions = capital formation;").scale(0.95).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex("member list = ledger; treasurer's report =").scale(0.95).shift(band_shift(5) + UP * 0.5)
        b5_l3 = Tex("financial reporting; payout rules = credit control").scale(0.9).shift(band_shift(5) + DOWN * 0.3)
        self.play(Write(b5_l1)); self.wait(2)
        self.play(Write(b5_l2)); self.play(Write(b5_l3)); self.wait(2.5)
        b5_l4 = Tex("Cattle: countable, visible assets").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        b5_l5 = Tex("Grazing rotas: internal control, community audited").scale(0.9).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l4)); self.wait(2)
        self.play(Write(b5_l5)); self.wait(2)
        b5_l6 = Tex("Method: name concept, define, show both sectors").scale(0.9).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l6))
        self.play(Create(SurroundingRectangle(b5_l6, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 6 (subtopic_5): the shop you already understand ---
        self.next_band(6)
        b6_t = Tex("The shop you already understand").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_t)); self.wait(2)
        b6_l1 = Tex("R3 000 saved to start $\\rightarrow$ capital").scale(1.0).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex("Fridge and table $\\rightarrow$ fixed assets").scale(1.0).shift(band_shift(6) + UP * 0.5)
        b6_l3 = Tex("Bread, chips, airtime $\\rightarrow$ stock at cost price").scale(0.95).shift(band_shift(6) + DOWN * 0.3)
        self.play(Write(b6_l1)); self.wait(1.5)
        self.play(Write(b6_l2)); self.wait(1.5)
        self.play(Write(b6_l3)); self.wait(2)
        b6_l4 = Tex("Chips: cost R7, sell R10 — ``the difference").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        b6_l5 = Tex("is what feeds us'' = the margin").scale(0.95).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l4)); self.play(Write(b6_l5)); self.wait(2)
        b6_l6 = Tex("Tin in $-$ tin out = profit, computed unwritten").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_6): one month, two notebooks ---
        self.next_band(7)
        b7_t = Tex("One month, two notebooks").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_t)); self.wait(2)
        b7_wrong = MathTex(r"\text{Head: } 4\,500 - 3\,000 \approx \text{R1 500 profit}").scale(1.0).shift(band_shift(7) + UP * 1.3)
        self.play(Write(b7_wrong)); self.wait(2)
        b7_l1 = Tex("Notebook: taxi 4 $\\times$ R40 = R160;").scale(0.95).shift(band_shift(7) + UP * 0.4)
        b7_l2 = Tex("electricity R90; airtime R50").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(b7_l1)); self.play(Write(b7_l2)); self.wait(2.5)
        b7_l3 = MathTex(r"4\,500 - 3\,000 - 160 - 90 - 50 = \text{R1 200}").scale(1.0).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.play(Create(strike(b7_wrong)))
        self.wait(2.5)
        b7_l4 = Tex("R300 leaked from memory — times 12 months,").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        b7_l5 = Tex("the shop believes in R3 600 that never was").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l4)); self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_7): your grandmother's ledger ---
        self.next_band(8)
        b8_t = Tex("Your grandmother's ledger").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_t)); self.wait(2)
        b8_l1 = Tex("Stokvel payments = capital contributions").scale(1.0).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex("The strict aunty's book = a ledger").scale(1.0).shift(band_shift(8) + UP * 0.5)
        b8_l3 = Tex("December meeting = the annual report").scale(1.0).shift(band_shift(8) + DOWN * 0.3)
        b8_l4 = Tex("No-skip payout rule = credit control").scale(1.0).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(b8_l1)); self.wait(1.8)
        self.play(Write(b8_l2)); self.wait(1.8)
        self.play(Write(b8_l3)); self.wait(1.8)
        self.play(Write(b8_l4)); self.wait(2)
        b8_l5 = Tex("Cattle in the kraal = an asset register;").scale(0.95).shift(band_shift(8) + DOWN * 2.0)
        b8_l6 = Tex("grazing turns = internal control").scale(0.95).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_l5)); self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(VGroup(b8_l5, b8_l6), color=GREEN)))
        self.wait(4)
