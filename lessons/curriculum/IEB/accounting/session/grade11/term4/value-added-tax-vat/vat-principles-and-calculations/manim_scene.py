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

# Band-layout whiteboard scene for "VAT Principles and Calculations"
# (grade 11, term 4, value-added tax). One band per teaching beat; the
# camera moves down and nothing is removed. Part 1 (Expert) = subtopics
# 1-4, Part 2 (Simplifier) = subtopics 5-7 in fresh bands. Exporter-safe
# primitives only; write-only reveals. Subtopic durations
# 220/220/230/230/190/200/200 of 1490 s guide the apportioning.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class VatPrinciplesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): what VAT is ---
        title = Tex("VAT: Principles and Calculations").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("An INDIRECT tax on consumption").scale(1.1).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("Borne by the final CONSUMER;").scale(1.05).shift(UP * 0.4)
        b0_l3 = Tex("collected and paid over by businesses").scale(1.05).shift(DOWN * 0.4)
        self.play(Write(b0_l2))
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_l4 = Tex("Output tax on sales; input tax on").scale(1.05).shift(DOWN * 1.3)
        b0_l5 = Tex("purchases; pay over the difference").scale(1.05).shift(DOWN * 2.1)
        self.play(Write(b0_l4))
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        b0_l6 = Tex("Gathered at every stage — harder to evade").scale(0.95).shift(DOWN * 3.0)
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_1): the three-business chain ---
        self.next_band(1)
        b1_t = Tex("Tax on the value ADDED at each stage").scale(1.1).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_t))
        self.wait(2)
        boxm = Rectangle(width=2.6, height=1.0).shift(band_shift(1) + UP * 1.2 + LEFT * 4.0)
        boxb = Rectangle(width=2.6, height=1.0).shift(band_shift(1) + UP * 1.2)
        boxs = Rectangle(width=2.6, height=1.0).shift(band_shift(1) + UP * 1.2 + RIGHT * 4.0)
        tm = Tex("Sawmill\\\\R400").scale(0.85).shift(band_shift(1) + UP * 1.2 + LEFT * 4.0)
        tb = Tex("Workshop\\\\R700").scale(0.85).shift(band_shift(1) + UP * 1.2)
        ts = Tex("Store\\\\R1 000").scale(0.85).shift(band_shift(1) + UP * 1.2 + RIGHT * 4.0)
        a1 = Arrow(band_shift(1) + UP * 1.2 + LEFT * 2.6, band_shift(1) + UP * 1.2 + LEFT * 1.4, buff=0)
        a2 = Arrow(band_shift(1) + UP * 1.2 + RIGHT * 1.4, band_shift(1) + UP * 1.2 + RIGHT * 2.6, buff=0)
        self.play(Create(boxm), Write(tm))
        self.play(Create(a1), Create(boxb), Write(tb))
        self.play(Create(a2), Create(boxs), Write(ts))
        self.wait(2.5)
        b1_l1 = Tex("Workshop: output on R700, input on R400").scale(1.0).shift(band_shift(1) + DOWN * 0.1)
        b1_l2 = Tex("$\\Rightarrow$ pays SARS tax on R300 it added").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)
        b1_l3 = Tex("All slices together $=$ tax on the final R1 000").scale(0.95).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("Invoice basis: VAT when invoiced;").scale(0.95).shift(band_shift(1) + DOWN * 2.6)
        b1_l5 = Tex("payments basis: VAT when money moves").scale(0.95).shift(band_shift(1) + DOWN * 3.3)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): the three categories ---
        self.next_band(2)
        b2_t = Tex("Standard, zero-rated, exempt").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = Tex("Standard-rated: most goods, 15\\%").scale(1.0).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex("Zero-rated: taxable at 0\\% — staples").scale(1.0).shift(band_shift(2) + UP * 0.4)
        b2_l3 = Tex("(brown bread, maize meal, milk, eggs)").scale(0.95).shift(band_shift(2) + DOWN * 0.3)
        b2_l4 = Tex("and exports; inputs STILL recovered").scale(1.0).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l2))
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Exempt: outside the system — interest,").scale(1.0).shift(band_shift(2) + DOWN * 1.8)
        b2_l6 = Tex("residential rent, transport, education;").scale(1.0).shift(band_shift(2) + DOWN * 2.5)
        b2_l7 = Tex("NO input tax recoverable").scale(1.0).shift(band_shift(2) + DOWN * 3.2)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.wait(2)
        self.play(Write(b2_l7))
        self.play(Create(SurroundingRectangle(b2_l7, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): calculations one and two ---
        self.next_band(3)
        b3_t = Tex("Adding VAT, extracting VAT").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_l1 = MathTex(r"3\,200 \times \tfrac{15}{100} = 480").scale(1.05).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("inclusive: R3 680 (or 3 200 $\\times$ 1,15)").scale(1.0).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_trap = Tex("VAT in R3 680 $=$ 15\\% of R3 680?").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_trap))
        self.play(Create(strike(b3_trap)))
        self.wait(2)
        b3_l3 = MathTex(r"3\,680 \times \tfrac{15}{115} = \text{R}480").scale(1.1).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = Tex("Cross-check: the two answers must meet").scale(0.95).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): calculations three and four ---
        self.next_band(4)
        b4_t = Tex("Exclusive amount; cost-plus pricing").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_l1 = MathTex(r"3\,680 \div 1{,}15 = \text{R}3\,200").scale(1.05).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex("Cost R1 600 $+$ 75\\% mark-up $=$ R2 800").scale(1.0).shift(band_shift(4) + UP * 0.2)
        b4_l3 = Tex("then VAT: 2 800 $\\times$ 1,15 $=$ R3 220").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        b4_l4 = Tex("Order: MARK-UP FIRST, then VAT —").scale(1.0).shift(band_shift(4) + DOWN * 1.5)
        b4_l5 = Tex("profit is the R1 200, never the R420").scale(1.0).shift(band_shift(4) + DOWN * 2.3)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(2.5)
        b4_l6 = Tex("Return: output $-$ input $=$ payable (or refund)").scale(0.95).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_4): the three adjustments ---
        self.next_band(5)
        b5_t = Tex("Returns, discounts, bad debts").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_l1 = Tex("Goods returned: credit note unwinds").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("the sale AND its output tax").scale(1.0).shift(band_shift(5) + UP * 0.5)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Discounts: trade discount before VAT;").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex("settlement discount corrected by credit note").scale(0.95).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex("Bad debts: recover the VAT portion as").scale(1.0).shift(band_shift(5) + DOWN * 2.0)
        b5_l6 = Tex("input tax; declare again if debtor pays").scale(1.0).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): ethics and control ---
        self.next_band(6)
        b6_t = Tex("Trust money, and its controls").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_trap = Tex("Spend collected VAT to ease cash flow?").scale(1.0).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_trap))
        self.play(Create(strike(b6_trap)))
        b6_l1 = Tex("It belongs to the state, not the vendor").scale(1.0).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = Tex("Frauds: private inputs, invented invoices,").scale(0.95).shift(band_shift(6) + DOWN * 0.6)
        b6_l3 = Tex("charging VAT while unregistered, cash off books").scale(0.9).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l2))
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex("Controls: valid tax invoices, control account").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        b6_l5 = Tex("reconciled monthly, submit and pay on time").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(2.5)
        b6_l6 = Tex("Audit: a real invoice, a business purpose?").scale(0.95).shift(band_shift(6) + DOWN * 3.6)
        self.play(Write(b6_l6))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): the line at the bottom of the slip ---
        self.next_band(7)
        b7_t = Tex("The line at the bottom of the slip").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("You paid it; the shop kept none of it").scale(1.05).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("Businesses COLLECT; consumers PAY").scale(1.05).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex("The table's chain: each business hands over").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex("tax only on the slice of value IT added").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("All slices $=$ the tax on what YOU paid").scale(1.0).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l5))
        self.wait(2)
        b7_l6 = Tex("A registered business channels VAT;").scale(0.95).shift(band_shift(7) + DOWN * 2.9)
        b7_l7 = Tex("it pays collected less charged").scale(0.95).shift(band_shift(7) + DOWN * 3.6)
        self.play(Write(b7_l6))
        self.play(Write(b7_l7))
        self.wait(3)

        # --- Band 8 (subtopic_6): the three baskets ---
        self.next_band(8)
        b8_t = Tex("Three baskets at the till").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("1. Most things: standard rate added").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("2. Essentials: zero — a tax on staples").scale(1.0).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex("punishes poor households hardest").scale(1.0).shift(band_shift(8) + DOWN * 0.3)
        b8_l4 = Tex("(brown loaf yes; artisanal loaf no)").scale(0.95).shift(band_shift(8) + DOWN * 1.0)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("3. Outside entirely: interest, home rent,").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        b8_l6 = Tex("bus fares, school fees — exempt").scale(1.0).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.wait(2.5)
        b8_l7 = Tex("Splitter: does the seller get its VAT back?").scale(0.95).shift(band_shift(8) + DOWN * 3.3)
        self.play(Write(b8_l7))
        self.play(Create(SurroundingRectangle(b8_l7, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): fifteen on one-fifteen ---
        self.next_band(9)
        b9_t = Tex("The fifteen-on-one-fifteen trick").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_trap = Tex("R3 680 incl.: VAT $=$ 15\\% $=$ R552?").scale(1.0).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_trap))
        self.play(Create(strike(b9_trap)))
        self.wait(2)
        b9_l1 = Tex("R3 680 is 115 parts: 100 price $+$ 15 tax").scale(1.0).shift(band_shift(9) + UP * 0.2)
        b9_l2 = MathTex(r"3\,680 \times \tfrac{15}{115} = \text{R}480").scale(1.1).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = Tex("Going up: 15 on 100").scale(1.0).shift(band_shift(9) + DOWN * 1.8)
        b9_l4 = Tex("Coming down: 15 on 115").scale(1.0).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(3)

        # --- Band 10 (subtopic_7): profit first, and whose money it is ---
        self.next_band(10)
        b10_t = Tex("Profit first — and whose money it is").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Cost R1 600 $+$ 75\\% $=$ R2 800 (yours: R1 200)").scale(0.95).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("then VAT: R2 800 $\\times$ 1,15 $=$ R3 220").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.wait(2)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("The R420 is SARS's money in your till").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2.5)
        b10_l4 = Tex("``Borrowing'' it for wages compounds").scale(1.0).shift(band_shift(10) + DOWN * 1.4)
        b10_l5 = Tex("with penalties until the business sinks").scale(1.0).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(2.5)
        b10_l6 = Tex("Every rand claimed: real invoice,").scale(1.0).shift(band_shift(10) + DOWN * 3.0)
        b10_l7 = Tex("real business purchase — or it is theft").scale(1.0).shift(band_shift(10) + DOWN * 3.7)
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.wait(4)
