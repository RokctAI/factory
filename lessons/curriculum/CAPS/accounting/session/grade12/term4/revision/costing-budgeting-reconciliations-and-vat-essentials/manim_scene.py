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

# Band-layout whiteboard scene for the CAPS grade 12 accounting session duo
# "Costing, Budgeting, Reconciliations and VAT Essentials" (term 4
# revision). One band per teaching beat; camera moves down, earlier work
# stays. Exporter-safe mobjects only; write-only reveals — no Transform/
# FadeOut/sub-part indexing on MathTex.
#
# Subtopic time shares (subtopics.json, total 1570 s):
# 240/240/235/245 expert, 205/200/205 simplifier.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CostingBudgetingVatEssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): production cost statement in one sweep ---
        title = Tex("Paper 2 Essentials: Four Topics").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Thola Workwear: direct materials R480\,000").scale(0.95).shift(UP * 1.3)
        b0_l2 = Tex(r"Direct labour (wages $+$ contributions) R360\,000").scale(0.95).shift(UP * 0.5)
        b0_l3 = Tex(r"Prime cost: R840\,000; overheads R300\,000").scale(0.95).shift(DOWN * 0.3)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex(r"Total cost of production: R1\,140\,000").scale(1.0).shift(DOWN * 1.2)
        b0_l5 = Tex(r"WIP opened and closed at R30\,000 — cancels").scale(0.9).shift(DOWN * 2.0)
        b0_l6 = Tex(r"12\,000 overalls $\Rightarrow$ unit cost R95").scale(1.0).shift(DOWN * 2.8)
        self.play(Write(b0_l4))
        self.wait(2)
        self.play(Write(b0_l5))
        self.wait(2)
        self.play(Write(b0_l6))
        self.play(Create(SurroundingRectangle(b0_l6, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the classification traps ---
        self.next_band(1)
        b1_title = Tex("The classification traps").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_wrong = Tex(r"Salesperson's commission in factory overheads").scale(0.95).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2)
        b1_l1 = Tex(r"Commission R240\,000: selling and distribution").scale(0.95).shift(band_shift(1) + UP * 0.3)
        b1_l2 = Tex(r"Office salaries R60\,000: administration").scale(0.95).shift(band_shift(1) + DOWN * 0.5)
        b1_l3 = Tex("Shared rent: split by floor area — the mark hides there").scale(0.9).shift(band_shift(1) + DOWN * 1.3)
        b1_l4 = Tex("Carriage on raw materials: joins direct materials").scale(0.9).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("One misfiled cost: three wounds — prime, total, unit").scale(0.9).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): contribution and break-even ---
        self.next_band(2)
        b2_title = Tex("Contribution and break-even").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"Sells R135; variable $40 + 30 + 20 = $ R90").scale(0.95).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex(r"Contribution R45; fixed costs R360\,000").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"\text{BEP} = \frac{360\,000}{45} = 8\,000 \text{ units}").scale(1.05).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex(r"Sold 12\,000: $4\,000 \times R45 = $ R180\,000 profit").scale(0.95).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex(r"Proof: $1\,620\,000 - 1\,080\,000 - 360\,000 = 180\,000$").scale(0.9).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l5))
        self.wait(2)
        b2_l6 = Tex(r"Target $+$R90\,000? $\div$ R45 $=$ 2\,000 more units").scale(0.9).shift(band_shift(2) + DOWN * 3.2)
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_3): cash budget vs projection ---
        self.next_band(3)
        b3_title = Tex("Two documents, two clocks").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"September collections, three slices:").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"$30\% \times 300\,000 = 90\,000$; $50\% \times 240\,000 = 120\,000$").scale(0.85).shift(band_shift(3) + UP * 0.4)
        b3_l3 = Tex(r"$18\% \times 200\,000 = 36\,000$ $\Rightarrow$ total R246\,000").scale(0.9).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2.5)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_wrong = Tex(r"The 2\% bad debts written into the cash budget").scale(0.9).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_l4 = Tex("Depreciation: income statement only; loans: cash only").scale(0.85).shift(band_shift(3) + DOWN * 2.2)
        b3_l5 = Tex(r"Advertising R10\,000 $\rightarrow$ R4\,000: sabotage, not saving").scale(0.85).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_4): reconciliation, ages, VAT ---
        self.next_band(4)
        b4_title = Tex("Reconciliation, ages, VAT settlement").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Ledger R44\,000 vs statement R52\,400:").scale(0.9).shift(band_shift(4) + UP * 1.3)
        b4_l2 = Tex(r"statement $- 4\,000 - 9\,200 = 39\,200$;").scale(0.9).shift(band_shift(4) + UP * 0.5)
        b4_l3 = Tex(r"ledger $-$ duplicate 4\,800 $=$ R39\,200 — agree").scale(0.9).shift(band_shift(4) + DOWN * 0.3)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex(r"Ages: 40/30/20/10\% — a third overdue, a tenth drifting").scale(0.85).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = Tex(r"VAT: $69\,000 - 48\,000 = 21\,000$; drawings $+1\,200$;").scale(0.85).shift(band_shift(4) + DOWN * 2.0)
        b4_l6 = Tex(r"bad debt $4\,600 \times \tfrac{15}{115} = 600$ off $\Rightarrow$ R21\,600").scale(0.9).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l5))
        self.wait(2.5)
        self.play(Write(b4_l6))
        self.play(Create(SurroundingRectangle(b4_l6, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): the price of one vetkoek ---
        self.next_band(5)
        b5_title = Tex("The price of one vetkoek").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex(r"Each vetkoek eats R6 (travels); rent R2\,400 sits still").scale(0.9).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex(r"Sells at R10: each drops R4 toward the rent").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"\frac{2\,400}{4} = 600 \text{ vetkoek to break even}").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex(r"Sells 900: $300 \times R4 = $ R1\,200 profit").scale(0.95).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex(r"Flour spikes to R7: contribution R3, break-even 800").scale(0.9).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_6): planning next month's money ---
        self.next_band(6)
        b6_title = Tex("Planning next month's money").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("The earning list: what next month SHOULD earn").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("The tin list: what actually lands, and when —").scale(0.95).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("drivers pay a month late; the gap kills stalls").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex("Refill clashes with the big order: move it earlier,").scale(0.9).shift(band_shift(6) + DOWN * 1.3)
        b6_l5 = Tex("or arrange grace in advance — never beg on the day").scale(0.9).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(2.5)
        b6_l6 = Tex("A number off its budget is a question, not an answer").scale(0.9).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_7): two books and the taxman's slice ---
        self.next_band(7)
        b7_title = Tex("Two books and the taxman's slice").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"Statement R5\,240: $-$ Friday's R500 $=$ R4\,740;").scale(0.9).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex(r"$-$ R340 flour not yet delivered $=$ R4\,400 — agree").scale(0.9).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex(r"Her R2\,400 book: R240 three months old — stop the").scale(0.85).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex("account, discount the slow, vet the new").scale(0.9).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex(r"Vendor vetkoek R11,50: the R1,50 sleeps for SARS").scale(0.9).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l5))
        self.wait(2)
        b7_l6 = Tex("Collected minus paid, nudged honestly — held in trust").scale(0.9).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(4)
