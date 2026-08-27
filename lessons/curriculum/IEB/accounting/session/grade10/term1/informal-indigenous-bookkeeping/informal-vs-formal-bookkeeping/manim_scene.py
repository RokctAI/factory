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

# Band-layout whiteboard scene for the informal-vs-formal-bookkeeping session
# duo. Exporter-safe primitives only (Tex/MathTex/Line/Arrow/Rectangle/
# VGroup); write-only reveals. Band time follows subtopics.json
# (160/170/170/190/170/160/160 of 1180 s).

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
        title = Tex("Informal vs Formal Bookkeeping").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("Formal: registered, recorded, banked,").scale(0.95).shift(UP * 1.1)
        l02 = Tex("answerable to outsiders").scale(0.95).shift(UP * 0.3)
        self.play(Write(l01)); self.play(Write(l02)); self.wait(2.5)
        l03 = Tex("Informal: unregistered traders,").scale(0.95).shift(DOWN * 0.6)
        l04 = Tex("few or no written records").scale(0.95).shift(DOWN * 1.4)
        self.play(Write(l03)); self.play(Write(l04)); self.wait(2)
        l05 = Tex("SAME concepts — different RECORDING").scale(1.0).shift(DOWN * 2.4)
        self.play(Write(l05))
        self.play(Create(SurroundingRectangle(l05, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the vocabulary ---
        self.next_band(1)
        b1_t = Tex("The vocabulary that carries marks").scale(1.1).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_t)); self.wait(2)
        b1_l1 = Tex("Capital: owner's resources in").scale(0.9).shift(band_shift(1) + UP * 1.5)
        b1_l2 = Tex("Fixed assets: kept for USE, not sale").scale(0.9).shift(band_shift(1) + UP * 0.7)
        b1_l3 = Tex("Stock: goods bought to resell").scale(0.9).shift(band_shift(1) + DOWN * 0.1)
        b1_l4 = Tex("Cost price paid; selling price charged").scale(0.9).shift(band_shift(1) + DOWN * 0.9)
        b1_l5 = Tex("Profit = income $-$ expenses").scale(0.95).shift(band_shift(1) + DOWN * 1.9)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(1.5)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the comparison, first concepts ---
        self.next_band(2)
        b2_t = Tex("Two columns, same concepts").scale(1.15).shift(band_shift(2) + UP * 2.5)
        self.play(Write(b2_t)); self.wait(2)
        b2_l1 = Tex("Capital: R600 000 banked").scale(0.9).shift(band_shift(2) + UP * 1.4)
        b2_l2 = Tex("vs R4 000 cash from a stokvel").scale(0.9).shift(band_shift(2) + UP * 0.6)
        self.play(Write(b2_l1)); self.play(Write(b2_l2)); self.wait(2.5)
        b2_l3 = Tex("Assets: shelving and tills vs fridge and table").scale(0.85).shift(band_shift(2) + DOWN * 0.3)
        self.play(Write(b2_l3)); self.wait(2)
        b2_l4 = Tex("Stock: invoiced deliveries vs").scale(0.9).shift(band_shift(2) + DOWN * 1.2)
        b2_l5 = Tex("two bags from the wholesaler").scale(0.9).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4)); self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): prices and the invisible labour ---
        self.next_band(3)
        b3_t = Tex("Prices, and the invisible labour").scale(1.1).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_t)); self.wait(2)
        b3_l1 = Tex("Chips: cost R8, sell R11 —").scale(0.95).shift(band_shift(3) + UP * 1.4)
        b3_l2 = Tex("the R3 margin lives in her head").scale(0.95).shift(band_shift(3) + UP * 0.6)
        self.play(Write(b3_l1)); self.play(Write(b3_l2)); self.wait(2.5)
        b3_l3 = Tex("Supermarket wages: recorded expense").scale(0.9).shift(band_shift(3) + DOWN * 0.3)
        self.play(Write(b3_l3)); self.wait(2)
        b3_l4 = Tex("Owner pays herself nothing:").scale(0.9).shift(band_shift(3) + DOWN * 1.2)
        b3_l5 = Tex("invisible labour overstates profit").scale(0.9).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_l4)); self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): where the difference bites ---
        self.next_band(4)
        b4_t = Tex("Where the difference bites").scale(1.15).shift(band_shift(4) + UP * 2.5)
        self.play(Write(b4_t)); self.wait(2)
        b4_l1 = Tex("1. Proof: banks lend against records").scale(0.9).shift(band_shift(4) + UP * 1.4)
        b4_l2 = Tex("2. Accuracy: expenses leak from memory").scale(0.9).shift(band_shift(4) + UP * 0.6)
        b4_l3 = Tex("3. Separation: shop tin $\\neq$ household purse").scale(0.9).shift(band_shift(4) + DOWN * 0.2)
        b4_l4 = Tex("4. Continuity: records survive, memory dies").scale(0.9).shift(band_shift(4) + DOWN * 1.0)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.wait(1.8)
        b4_l5 = Tex("Recording ADDS to skill that exists").scale(0.95).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_4): indigenous practices ---
        self.next_band(5)
        b5_t = Tex("Indigenous practices: the original books").scale(1.0).shift(band_shift(5) + UP * 2.5)
        self.play(Write(b5_t)); self.wait(2)
        b5_l1 = Tex("Stokvel: contributions = capital;").scale(0.9).shift(band_shift(5) + UP * 1.4)
        b5_l2 = Tex("member book = ledger; report = accountability").scale(0.85).shift(band_shift(5) + UP * 0.6)
        self.play(Write(b5_l1)); self.play(Write(b5_l2)); self.wait(2.5)
        b5_l3 = Tex("Cattle: countable, visible assets").scale(0.9).shift(band_shift(5) + DOWN * 0.3)
        self.play(Write(b5_l3)); self.wait(2)
        b5_l4 = Tex("Grazing rotas: internal control —").scale(0.9).shift(band_shift(5) + DOWN * 1.2)
        b5_l5 = Tex("rules, plus the community as auditor").scale(0.9).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l4)); self.play(Write(b5_l5))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 6 (subtopic_5): the shop you already understand ---
        self.next_band(6)
        b6_t = Tex("The shop you already understand").scale(1.1).shift(band_shift(6) + UP * 2.5)
        self.play(Write(b6_t)); self.wait(2)
        b6_l1 = Tex("R4 000 saved to start: capital").scale(0.9).shift(band_shift(6) + UP * 1.4)
        b6_l2 = Tex("Fridge and table: fixed assets").scale(0.9).shift(band_shift(6) + UP * 0.6)
        b6_l3 = Tex("Two bags from the wholesaler: stock").scale(0.9).shift(band_shift(6) + DOWN * 0.2)
        b6_l4 = Tex("R8 in, R11 out: cost vs selling price").scale(0.9).shift(band_shift(6) + DOWN * 1.0)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(1.6)
        b6_l5 = Tex("Count the tin: income $-$ expenses = profit").scale(0.9).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_6): one month, two notebooks ---
        self.next_band(7)
        b7_t = Tex("One month, two notebooks").scale(1.15).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7_t)); self.wait(2)
        b7_l1 = Tex("The head: 5 200 $-$ 3 400 $\\approx$ R1 800").scale(0.95).shift(band_shift(7) + UP * 1.4)
        self.play(Write(b7_l1)); self.wait(2)
        b7_l2 = Tex("The notebook: $-$ taxi 175 $-$ power 110").scale(0.9).shift(band_shift(7) + UP * 0.5)
        b7_l3 = Tex("$-$ airtime 65 = R1 450").scale(0.95).shift(band_shift(7) + DOWN * 0.3)
        self.play(Write(b7_l2)); self.play(Write(b7_l3)); self.wait(2.5)
        b7_l4 = Tex("The R350 leak — always spent, never held").scale(0.9).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        b7_l5 = Tex("Twelve months: R4 200 of imagined profit").scale(0.9).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_7): your grandmother's ledger ---
        self.next_band(8)
        b8_t = Tex("Your grandmother's ledger").scale(1.15).shift(band_shift(8) + UP * 2.5)
        self.play(Write(b8_t)); self.wait(2)
        b8_l1 = Tex("Stokvel book: who paid, who is behind").scale(0.9).shift(band_shift(8) + UP * 1.4)
        b8_l2 = Tex("December meeting: the annual report").scale(0.9).shift(band_shift(8) + UP * 0.6)
        self.play(Write(b8_l1)); self.wait(2)
        self.play(Write(b8_l2)); self.wait(2)
        b8_l3 = Tex("Cattle in the kraal: a visible asset register").scale(0.85).shift(band_shift(8) + DOWN * 0.3)
        self.play(Write(b8_l3)); self.wait(2)
        b8_l4 = Tex("Accounting formalises the familiar —").scale(0.9).shift(band_shift(8) + DOWN * 1.2)
        b8_l5 = Tex("you are just getting a better pen").scale(0.95).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l4)); self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(4)
