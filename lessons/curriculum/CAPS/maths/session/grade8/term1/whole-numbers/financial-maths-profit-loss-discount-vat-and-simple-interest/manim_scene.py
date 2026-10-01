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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex/MathTex keep the export to
# the allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (220/180/220/240/230/230/220 of
# 1540 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FinancialContextsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Financial Contexts
        t0 = Tex(r"Financial Contexts").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"\text{profit} = \text{SP} - \text{CP} = 100 - 80 = 20").scale(1.1).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"\% \text{ profit} = \frac{\text{profit}}{\text{CP}} \times 100 = \frac{20}{80} \times 100 = 25\%").scale(1.1).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m2, color=GREEN)))
        self.wait(1.5)
        m3 = MathTex(r"\text{loss: } 2\,500 - 2\,000 = 500, \quad \frac{500}{2\,500} \times 100 = 20\%").scale(1.1).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = MathTex(r"30\% \text{ profit on } 150: \quad 1{,}3 \times 150 = 195").scale(1.1).shift(DOWN * 2.9)
        self.play(Write(m4))
        self.wait(2)
        self.wait(3)

        # --- Band 1 (subtopic_2): Discount and VAT
        self.next_band(1)
        t1 = Tex(r"Discount and VAT").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"20\% \text{ off } 450: \quad 450 - 90 = 360 \quad \text{or} \quad 0{,}8 \times 450 = 360").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"\text{VAT } 15\% \text{ of } 460 = 69 \quad \Rightarrow \quad 460 + 69 = 529").scale(1.1).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"\text{or } 1{,}15 \times 460 = 529").scale(1.1).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m7, color=GREEN)))
        self.wait(1.5)
        m8 = MathTex(r"\text{remove VAT: } 529 \div 1{,}15 = 460 \quad (\text{NOT } 15\% \text{ of } 529)").scale(1.1).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m8))
        self.wait(2)
        self.wait(3)

        # --- Band 2 (subtopic_3): Simple interest: $I = P \times i \times n$
        self.next_band(2)
        t2 = Tex(r"Simple interest: $I = P \times i \times n$").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"P = 2\,000, \quad i = \tfrac{8}{100} = 0{,}08, \quad n = 3").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"I = 2\,000 \times 0{,}08 \times 3 = 480").scale(1.1).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"A = 2\,000 + 480 = 2\,480").scale(1.1).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m11, color=GREEN)))
        self.wait(1.5)
        m12 = Tex(r"The rate enters as a DECIMAL").scale(1.05).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(m12))
        self.wait(2)
        self.wait(3)

        # --- Band 3 (subtopic_3): Hire purchase: R6 000 fridge
        self.next_band(3)
        t3 = Tex(r"Hire purchase: R6 000 fridge").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"\text{deposit } 10\% \text{ of } 6\,000 = 600 \qquad \text{balance } 5\,400").scale(1.1).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"I = 5\,400 \times 0{,}12 \times 2 = 1\,296").scale(1.1).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        m15 = MathTex(r"\text{owed: } 5\,400 + 1\,296 = 6\,696 \qquad 6\,696 \div 24 = 279 \text{ per month}").scale(1.1).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m15, color=GREEN)))
        self.wait(1.5)
        m16 = MathTex(r"\text{real cost: } 600 + 6\,696 = 7\,296").scale(1.1).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m16))
        self.wait(2)
        self.wait(3)

        # --- Band 4 (subtopic_4): Budgets and exchange rates
        self.next_band(4)
        t4 = Tex(r"Budgets and exchange rates").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = MathTex(r"\text{expenses: } 180 + 150 + 200 = 530 \qquad 600 - 530 = 70 \text{ surplus}").scale(1.1).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"\$1 = \text{R}18: \quad \$50 \to 50 \times 18 = \text{R}900").scale(1.1).shift(band_shift(4) + UP * 0.18)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"\text{R}1\,800 \to 1\,800 \div 18 = \$100").scale(1.1).shift(band_shift(4) + DOWN * 0.85)
        self.play(Write(m19))
        self.wait(2)
        m20 = Tex(r"Into rand: multiply. Out of rand: divide.").scale(1.05).shift(band_shift(4) + DOWN * 1.87)
        self.play(Write(m20))
        self.wait(2)
        m21 = Tex(r"Multipliers: $1{,}15$ VAT, $0{,}8$ for $20\%$ off, $1{,}3$ for $30\%$ up").scale(1.05).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m21))
        self.wait(2)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Counting the profit at the spaza counter
        self.next_band(5)
        t5 = Tex(r"Counting the profit at the spaza counter").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        m22 = MathTex(r"\text{paid } 80, \quad \text{took in } 100, \quad 100 - 80 = 20 \text{ profit}").scale(1.1).shift(band_shift(5) + UP * 1.2)
        self.play(Write(m22))
        self.wait(2)
        m23 = MathTex(r"\frac{20}{80} \times 100 = 25\% \quad \text{(of the COST)}").scale(1.1).shift(band_shift(5) + DOWN * 0.17)
        self.play(Write(m23))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m23, color=GREEN)))
        self.wait(1.5)
        m24 = MathTex(r"30\% \text{ of } 150 = 45 \quad \to \quad 150 + 45 = 195").scale(1.1).shift(band_shift(5) + DOWN * 1.53)
        self.play(Write(m24))
        self.wait(2)
        m25 = MathTex(r"\text{one move: } 1{,}3 \times 150 = 195").scale(1.1).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(m25))
        self.wait(2)
        self.wait(3)

        # --- Band 6 (subtopic_6): Sale prices and the tax on the till slip
        self.next_band(6)
        t6 = Tex(r"Sale prices and the tax on the till slip").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(t6))
        self.wait(1.5)
        m26 = MathTex(r"20\% \text{ off } 450: \quad 450 - 90 = 360 \quad \text{or} \quad 0{,}8 \times 450 = 360").scale(1.1).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m26))
        self.wait(2)
        m27 = MathTex(r"\text{VAT on } 460: \quad 69 \quad \to \quad 1{,}15 \times 460 = 529").scale(1.1).shift(band_shift(6) + DOWN * 0.17)
        self.play(Write(m27))
        self.wait(2)
        m28 = Tex(r"UP the staircase: $\times 1{,}15$. DOWN: $\div 1{,}15$.").scale(1.05).shift(band_shift(6) + DOWN * 1.53)
        self.play(Write(m28))
        self.wait(2)
        m29 = MathTex(r"529 \div 1{,}15 = 460 \qquad \text{VAT} = 69").scale(1.1).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m29))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m29, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 7 (subtopic_7): What the fridge really costs
        self.next_band(7)
        t7 = Tex(r"What the fridge really costs").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(t7))
        self.wait(1.5)
        m30 = MathTex(r"\text{deposit: } 10\% \text{ of } 6\,000 = 600 \qquad \text{owe } 5\,400").scale(1.1).shift(band_shift(7) + UP * 1.2)
        self.play(Write(m30))
        self.wait(2)
        m31 = MathTex(r"\text{interest: } 5\,400 \times 0{,}12 \times 2 = 1\,296").scale(1.1).shift(band_shift(7) + DOWN * 0.17)
        self.play(Write(m31))
        self.wait(2)
        m32 = MathTex(r"\text{instalment: } 6\,696 \div 24 = 279").scale(1.1).shift(band_shift(7) + DOWN * 1.53)
        self.play(Write(m32))
        self.wait(2)
        m33 = MathTex(r"\text{real cost: } 600 + 6\,696 = 7\,296").scale(1.1).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(m33))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m33, color=RED)))
        self.wait(1.5)
        self.wait(3)
