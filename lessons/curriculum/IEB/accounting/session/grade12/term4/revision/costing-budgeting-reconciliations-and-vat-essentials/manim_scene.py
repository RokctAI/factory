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

# Band-layout whiteboard scene for the IEB grade 12 accounting session duo
# "Costing, Budgeting, Reconciliations and VAT Essentials" — revision of the
# managerial pillars on one factory (Marang Apparel), with the simplifier
# part retelling everything at a vetkoek stall. Exporter-safe mobjects only;
# write-only reveals — no Transform/FadeOut/sub-part indexing on MathTex.
#
# Subtopic time shares (subtopics.json, total 1570 s):
# 240/240/235/245/205/200/205 — subtopic_1 gets two bands (funnel + traps).

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

        # --- Band 0 (subtopic_1): production cost statement in one sweep ---
        title = Tex("The five-level funnel").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Direct materials R495\,000; direct labour R360\,000").scale(0.9).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = Tex(r"Prime cost: $495\,000 + 360\,000 = $ R855\,000").scale(0.95).shift(UP * 0.4)
        b0_l3 = Tex(r"Overheads R345\,000 $\Rightarrow$ total cost R1\,200\,000").scale(0.9).shift(DOWN * 0.4)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_l4 = Tex(r"WIP: opened and closed at R45\,000 — cancels").scale(0.9).shift(DOWN * 1.2)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = MathTex(r"\frac{1\,200\,000}{15\,000 \text{ units}} = R80 \text{ per unit}").scale(1.0).shift(DOWN * 2.2)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the classification traps ---
        self.next_band(1)
        b1_title = Tex("The classification traps").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_wrong = Tex(r"Commission R180\,000 into factory overheads").scale(0.9).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2)
        b1_l1 = Tex(r"Commission $\rightarrow$ selling and distribution").scale(0.9).shift(band_shift(1) + UP * 0.3)
        b1_l2 = Tex(r"Office salaries and stationery R75\,000 $\rightarrow$ admin").scale(0.9).shift(band_shift(1) + DOWN * 0.5)
        b1_l3 = Tex(r"Shared rent: split by floor area — the mark hides there").scale(0.85).shift(band_shift(1) + DOWN * 1.3)
        b1_l4 = Tex(r"Carriage on raw materials $\rightarrow$ direct materials").scale(0.9).shift(band_shift(1) + DOWN * 2.1)
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
        b2_title = Tex("Break-even: the tracksuit factory").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"Contribution: $160 - 110 = $ R50 (variable ONLY)").scale(0.95).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"\text{BEP} = \frac{420\,000}{50} = 8\,400 \text{ units}").scale(1.05).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = Tex(r"Made 15\,000: 6\,600 past the line $\times$ R50 $=$ R330\,000").scale(0.85).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex(r"Proof: $2\,400\,000 - 1\,650\,000 - 420\,000 = 330\,000$").scale(0.85).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l4))
        self.wait(2.5)
        b2_l5 = Tex(r"Target $+$R120\,000: $\tfrac{120\,000}{50} = 2\,400$ more units").scale(0.85).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_3): cash budget vs projection ---
        self.next_band(3)
        b3_title = Tex("The collection schedule: June").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"$25\% \times 260\,000 = 65\,000$ (June's own)").scale(0.9).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"$55\% \times 220\,000 = 121\,000$ (May)").scale(0.9).shift(band_shift(3) + UP * 0.4)
        b3_l3 = Tex(r"$17\% \times 160\,000 = 27\,200$ $\Rightarrow$ total R213\,200").scale(0.9).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_wrong = Tex(r"Budgeting the 3\% bad debts as a receipt").scale(0.9).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_l4 = Tex("Depreciation: projection only; loans: cash only").scale(0.9).shift(band_shift(3) + DOWN * 2.1)
        b3_l5 = Tex(r"Advertising R9\,000 $\rightarrow$ R3\,000: query, not praise").scale(0.85).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_4): reconciliation, ages, VAT ---
        self.next_band(4)
        b4_title = Tex("Reconciliation, ages, VAT").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"51\,800 - 4\,200 - 5\,300 = 42\,300").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex(r"Ledger: $45\,900 - 3\,600$ duplicate $=$ R42\,300 — agree").scale(0.85).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex(r"Ages of R320\,000: 45\% current; 25\% 30d;").scale(0.9).shift(band_shift(4) + DOWN * 0.5)
        b4_l4 = Tex(r"20\% 60d; 10\% 90d$+$ — thirty percent beyond terms").scale(0.9).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = MathTex(r"\text{VAT: } 57\,000 - 39\,600 + 900 - 300 = 18\,000").scale(0.9).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_5): the price of one vetkoek ---
        self.next_band(5)
        b5_title = Tex("The price of one vetkoek").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Each vetkoek eats R7; sells at R12 — R5 contributes").scale(0.9).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex(r"Stall and gas: R3\,500 a month, rain or shine").scale(0.9).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"\frac{3\,500}{5} = 700 \text{ vetkoek}").scale(1.05).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex(r"Sells 1\,000: 300 past the line $\times$ R5 $=$ R1\,500").scale(0.9).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex(r"Flour spike: R4 contribution $\Rightarrow$ break-even 875").scale(0.9).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_6): planning next month's money ---
        self.next_band(6)
        b6_title = Tex("The tin list vs the earning list").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Earning list: what next month SHOULD earn").scale(0.9).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("Tin list: what actually lands in the tin —").scale(0.9).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("last month's drivers paying, this month's cash").scale(0.9).shift(band_shift(6) + DOWN * 0.3)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex("Gas refill week $=$ big order week: move one,").scale(0.9).shift(band_shift(6) + DOWN * 1.2)
        b6_l5 = Tex("or arrange grace in advance — planned, not begged").scale(0.9).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.wait(2)
        self.play(Write(b6_l5))
        self.wait(2.5)
        b6_l6 = Tex("A number off its budget is a question, not an answer").scale(0.85).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_7): two books and the taxman's slice ---
        self.next_band(7)
        b7_title = Tex("Two books, one truth — and SARS's coins").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"Statement R6\,180 $-$ R600 post $-$ R280 Tuesday flour").scale(0.85).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex(r"$=$ R5\,300 $=$ her book — reconciled").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex(r"R12 vetkoek $\rightarrow$ R13,80 incl.\ VAT: R1,80 held in trust").scale(0.85).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex("Settlement: collected minus paid, nudged honestly").scale(0.9).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("Hiding Friday's cash sales: theft from the public purse").scale(0.85).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l5))
        self.wait(4)
