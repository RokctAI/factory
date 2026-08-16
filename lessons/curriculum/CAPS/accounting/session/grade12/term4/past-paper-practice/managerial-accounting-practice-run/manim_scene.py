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

# Band-layout whiteboard scene for the CAPS grade 12 accounting session
# "Managerial Accounting Practice Run" — a full Paper 2 walkthrough. This
# session's script runs seven exam-question subtopics (no simplifier part),
# so each question gets its own band(s). Exporter-safe mobjects only;
# write-only reveals — no Transform/FadeOut/sub-part indexing on MathTex.
#
# Subtopic time shares (subtopics.json, total 1560 s):
# 210/235/220/225/230/225/215 — near-equal; bands are spread evenly.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ManagerialAccountingPracticeRunSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # --- Band 0 (subtopic_1): concepts and cost sorting ---
        title = Tex("Paper 2 Practice Run: 150 marks").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Direct vs indirect; fixed vs variable;").scale(1.0).shift(UP * 1.3)
        b0_l2 = Tex("perpetual vs periodic — a mark per rung").scale(1.0).shift(UP * 0.6)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex(r"Commission $\rightarrow$ selling; factory cleaner $\rightarrow$ overheads").scale(0.9).shift(DOWN * 0.3)
        b0_l4 = Tex(r"Carriage on raw materials $\rightarrow$ direct materials").scale(0.9).shift(DOWN * 1.1)
        b0_l5 = Tex(r"Delivery depr.\ $\rightarrow$ selling; machine depr.\ $\rightarrow$ factory").scale(0.85).shift(DOWN * 1.9)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2)
        self.play(Write(b0_l5))
        self.wait(2)
        b0_l6 = Tex("Sort slowly — the statement reuses every answer").scale(0.95).shift(DOWN * 2.8)
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_2): production cost statement ---
        self.next_band(1)
        b1_title = Tex("Production cost statement").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\text{DMC: } 60\,000 + 540\,000 + 12\,000 - 72\,000 = 540\,000").scale(0.85).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = Tex(r"DLC: wages 336\,000 $+$ contributions 24\,000 $=$ 360\,000").scale(0.85).shift(band_shift(1) + UP * 0.4)
        b1_l3 = Tex(r"Prime cost: $540\,000 + 360\,000 = $ R900\,000").scale(0.95).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex(r"Overheads: $320\,000 + 70\% \times 40\,000 = $ R348\,000").scale(0.9).shift(band_shift(1) + DOWN * 1.2)
        b1_l5 = Tex(r"Total cost of production: R1\,248\,000").scale(0.95).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l4))
        self.wait(2.5)
        self.play(Write(b1_l5))
        self.wait(2)
        b1_l6 = Tex(r"WIP: $+52\,000 - 40\,000$; finished R1\,260\,000").scale(0.9).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l6))
        self.play(Create(SurroundingRectangle(b1_l6, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): unit cost + interpretation ---
        self.next_band(2)
        b2_title = Tex("Unit cost and its meaning").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\frac{1\,260\,000}{21\,000 \text{ units}} = R60 \text{ per unit}").scale(1.0).shift(band_shift(2) + UP * 0.9)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2.5)
        b2_l2 = Tex(r"Last year R64 $\rightarrow$ better — but NAME a reason:").scale(1.0).shift(band_shift(2) + DOWN * 0.3)
        b2_l3 = Tex("cheaper cotton, less waste, or higher volume").scale(1.0).shift(band_shift(2) + DOWN * 1.1)
        b2_l4 = Tex("spreading the fixed overheads thinner").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_3): break-even ---
        self.next_band(3)
        b3_title = Tex("Break-even: the shoe factory").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Contribution: $240 - 150 = $ R90 (variable ONLY)").scale(0.95).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_wrong = Tex("Sliding fixed cost into the variable figure").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_l2 = MathTex(r"\text{BEP} = \frac{630\,000}{90} = 7\,000 \text{ pairs}").scale(1.05).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex(r"Made 8\,200: 1\,200 past the line — profitable;").scale(0.9).shift(band_shift(3) + DOWN * 1.5)
        b3_l4 = Tex(r"last year 7\,500 vs 7\,600 — 100 pairs short, a loss").scale(0.9).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex(r"Profit: $1\,200 \times R90$ = R108\,000; leather +R15 $\Rightarrow$ BEP 8\,400").scale(0.8).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_4): inventory valuation ---
        self.next_band(4)
        b4_title = Tex("Inventory: 3\\,000 bags costing R276\\,000").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"500 @ R84; 1\,500 @ R90; 1\,000 @ R99; 800 remain").scale(0.9).shift(band_shift(4) + UP * 1.3)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex(r"FIFO: 800 @ R99 $=$ R79\,200; COS R196\,800").scale(0.95).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = MathTex(r"\text{WA: } \frac{276\,000}{3\,000} = R92").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = Tex(r"800 @ R92 $=$ R73\,600; COS R202\,400").scale(0.95).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2.5)
        b4_l5 = Tex(r"Rising prices: FIFO stock R5\,600 higher — higher profit").scale(0.85).shift(band_shift(4) + DOWN * 2.4)
        b4_l6 = Tex(r"800 left $\approx$ 133 days of stock — season or sleeping capital?").scale(0.8).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4_l5))
        self.wait(2.5)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_5): cash budget question ---
        self.next_band(5)
        b5_title = Tex("Cash budget: October's receipts").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Cash sales: $40\% \times 220\,000 = $ R88\,000").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex(r"Sept credit R120\,000: 50\% $=$ R60\,000").scale(0.95).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex(r"Aug credit R108\,000: 45\% $=$ R48\,600").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex(r"Total from sales: R196\,600").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_wrong = Tex(r"Writing the 5\% bad debts into the budget").scale(0.95).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_wrong))
        self.play(Create(strike(b5_wrong)))
        self.wait(2)
        b5_l5 = Tex(r"Advertising cut R10\,000 $\rightarrow$ R2\,500: seed, not luxury").scale(0.85).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_6): reconciliation + age analysis ---
        self.next_band(6)
        b6_title = Tex("Creditors' reconciliation, then the ages").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Ledger R66\,300 vs statement R84\,500").scale(0.95).shift(band_shift(6) + UP * 1.3)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"84\,500 - 12\,000 - 8\,400 - 300 = 63\,800").scale(0.95).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex(r"Ledger: $66\,300 - 2\,500$ returns $=$ R63\,800 — agree").scale(0.9).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6_l2))
        self.wait(2.5)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = Tex(r"Ages of R240\,000: current 40\%; 30d 30\%;").scale(0.9).shift(band_shift(6) + DOWN * 1.3)
        b6_l5 = Tex(r"60d 20\%; 90d$+$ 10\% — a third beyond terms").scale(0.9).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(2.5)
        b6_l6 = Tex("Cash receiver must not keep the debtors' ledger").scale(0.9).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_7): VAT, control, ethics ---
        self.next_band(7)
        b7_title = Tex("VAT settlement, control, ethics").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"Output: $15\% \times 720\,000 = 108\,000$; input R79\,500").scale(0.9).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex(r"Base owed: R28\,500").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex(r"Drawings R6\,000 excl.: $+$R900; bad debt R9\,200 incl.:").scale(0.85).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = MathTex(r"9\,200 \times \tfrac{15}{115} = 1\,200 \Rightarrow 28\,500 + 900 - 1\,200").scale(0.85).shift(band_shift(7) + DOWN * 1.2)
        b7_l5 = Tex(r"Owed to SARS: R28\,200").scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l3))
        self.wait(2.5)
        self.play(Write(b7_l4))
        self.wait(2.5)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(2)
        b7_l6 = Tex("Second till $=$ VAT fraud: trust broken, public robbed").scale(0.85).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l6))
        self.wait(4)
