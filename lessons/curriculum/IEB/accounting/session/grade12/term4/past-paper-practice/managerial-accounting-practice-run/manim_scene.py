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

# Band-layout whiteboard scene for the IEB grade 12 accounting session
# "Managerial Accounting Practice Run" — a full managerial-accounting
# practice set. This session's script runs seven task subtopics (no
# simplifier part), so each task gets its own band(s). Exporter-safe
# mobjects only; write-only reveals — no Transform/FadeOut/sub-part
# indexing on MathTex.
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
        title = Tex("Practice Set: 150 marks").scale(1.25).to_edge(UP)
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
        b1_l1 = MathTex(r"\text{DMC: } 84\,000 + 612\,000 + 18\,000 - 90\,000 = 624\,000").scale(0.85).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = Tex(r"DLC: wages 390\,000 $+$ contributions 30\,000 $=$ 420\,000").scale(0.85).shift(band_shift(1) + UP * 0.4)
        b1_l3 = Tex(r"Prime cost: $624\,000 + 420\,000 = $ R1\,044\,000").scale(0.95).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex(r"Overheads: $296\,000 + 60\% \times 60\,000 = $ R332\,000").scale(0.9).shift(band_shift(1) + DOWN * 1.2)
        b1_l5 = Tex(r"Total cost of production: R1\,376\,000").scale(0.95).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l4))
        self.wait(2.5)
        self.play(Write(b1_l5))
        self.wait(2)
        b1_l6 = Tex(r"WIP: $+64\,000 - 48\,000$; finished R1\,392\,000").scale(0.9).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l6))
        self.play(Create(SurroundingRectangle(b1_l6, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): unit cost + interpretation ---
        self.next_band(2)
        b2_title = Tex("Unit cost and its meaning").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\frac{1\,392\,000}{24\,000 \text{ desks}} = R58 \text{ per desk}").scale(1.0).shift(band_shift(2) + UP * 0.9)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2.5)
        b2_l2 = Tex(r"Last year R62 $\rightarrow$ better — but NAME a reason:").scale(1.0).shift(band_shift(2) + DOWN * 0.3)
        b2_l3 = Tex("cheaper timber, less waste, or higher volume").scale(1.0).shift(band_shift(2) + DOWN * 1.1)
        b2_l4 = Tex("spreading the fixed overheads thinner").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_3): break-even ---
        self.next_band(3)
        b3_title = Tex("Break-even: the mug factory").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Contribution: $80 - 56 = $ R24 (variable ONLY)").scale(0.95).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_wrong = Tex("Sliding fixed cost into the variable figure").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_l2 = MathTex(r"\text{BEP} = \frac{432\,000}{24} = 18\,000 \text{ mugs}").scale(1.05).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex(r"Made 21\,000: 3\,000 past the line — profitable;").scale(0.9).shift(band_shift(3) + DOWN * 1.5)
        b3_l4 = Tex(r"last year 17\,500 vs 17\,800 — 300 mugs short, a loss").scale(0.9).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex(r"Profit: $3\,000 \times R24$ = R72\,000; clay +R6 $\Rightarrow$ BEP 24\,000").scale(0.8).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_4): inventory valuation ---
        self.next_band(4)
        b4_title = Tex("Inventory: 2\\,500 balls costing R180\\,000").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"400 @ R60; 1\,200 @ R70; 900 @ R80; 600 remain").scale(0.9).shift(band_shift(4) + UP * 1.3)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex(r"FIFO: 600 @ R80 $=$ R48\,000; COS R132\,000").scale(0.95).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = MathTex(r"\text{WA: } \frac{180\,000}{2\,500} = R72").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = Tex(r"600 @ R72 $=$ R43\,200; COS R136\,800").scale(0.95).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2.5)
        b4_l5 = Tex(r"Rising prices: FIFO stock R4\,800 higher — higher profit").scale(0.85).shift(band_shift(4) + DOWN * 2.4)
        b4_l6 = Tex(r"600 left $\approx$ 115 days of stock — season or sleeping capital?").scale(0.8).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4_l5))
        self.wait(2.5)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_5): cash budget task ---
        self.next_band(5)
        b5_title = Tex("Cash budget: March's receipts").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Cash sales: $30\% \times 210\,000 = $ R63\,000").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex(r"Feb credit R133\,000: 60\% $=$ R79\,800").scale(0.95).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex(r"Jan credit R105\,000: 35\% $=$ R36\,750").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex(r"Total from sales: R179\,550").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_wrong = Tex(r"Writing the 5\% bad debts into the budget").scale(0.95).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_wrong))
        self.play(Create(strike(b5_wrong)))
        self.wait(2)
        b5_l5 = Tex(r"Advertising cut R12\,000 $\rightarrow$ R5\,000: seed, not luxury").scale(0.85).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_6): reconciliation + age analysis ---
        self.next_band(6)
        b6_title = Tex("Creditors' reconciliation, then the ages").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Ledger R64\,550 vs statement R78\,400").scale(0.95).shift(band_shift(6) + UP * 1.3)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"78\,400 - 9\,800 - 5\,600 - 450 = 62\,550").scale(0.95).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex(r"Ledger: $64\,550 - 2\,000$ returns $=$ R62\,550 — agree").scale(0.9).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6_l2))
        self.wait(2.5)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = Tex(r"Ages of R180\,000: current 45\%; 30d 25\%;").scale(0.9).shift(band_shift(6) + DOWN * 1.3)
        b6_l5 = Tex(r"60d 20\%; 90d$+$ 10\% — thirty percent beyond terms").scale(0.9).shift(band_shift(6) + DOWN * 2.0)
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
        b7_l1 = Tex(r"Output: $15\% \times 560\,000 = 84\,000$; input R61\,500").scale(0.9).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex(r"Base owed: R22\,500").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex(r"Drawings R4\,000 excl.: $+$R600; bad debt R6\,900 incl.:").scale(0.85).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = MathTex(r"6\,900 \times \tfrac{15}{115} = 900 \Rightarrow 22\,500 + 600 - 900").scale(0.85).shift(band_shift(7) + DOWN * 1.2)
        b7_l5 = Tex(r"Owed to SARS: R22\,200").scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l3))
        self.wait(2.5)
        self.play(Write(b7_l4))
        self.wait(2.5)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(2)
        b7_l6 = Tex("Hidden cash sales $=$ VAT fraud: trust broken, public robbed").scale(0.85).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l6))
        self.wait(4)
