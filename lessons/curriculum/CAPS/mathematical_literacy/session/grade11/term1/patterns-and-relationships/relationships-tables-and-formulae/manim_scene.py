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

# Band layout: one frame-height band per teaching beat; the camera moves down,
# nothing is removed. Exporter-supported mobjects only (Tex/MathTex/Line/
# Rectangle/SurroundingRectangle); single-string Write reveals throughout.
#
# Covers all seven subtopics (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7),
# band time roughly proportional to subtopics.json
# (215/225/220/225/190/200/190 of 1465 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RelationshipsTablesFormulaeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the two variables ---
        title = Tex("Relationships, Tables and Formulae").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l1 = Tex("INDEPENDENT: what you choose — hours, litres, km").scale(1.0).shift(UP * 1.1)
        l2 = Tex("DEPENDENT: what follows — the amount you pay").scale(1.0).shift(UP * 0.2)
        self.play(Write(l1)); self.wait(2.5)
        self.play(Write(l2)); self.wait(2.5)
        l3 = Tex(r"``The cost depends on the number of hours''").scale(1.05).shift(DOWN * 0.8)
        l4 = Tex("Independent across, dependent up the side").scale(1.0).shift(DOWN * 1.8)
        self.play(Write(l3)); self.wait(2.5)
        self.play(Write(l4)); self.wait(2.5)

        # --- Band 1 (subtopic_1): the plumber's table and formula ---
        self.next_band(1)
        b1_title = Tex(r"Plumber: call-out R350, then R280 per hour").scale(1.05).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        tbl = Rectangle(width=9.4, height=2.0).shift(band_shift(1) + UP * 1.2)
        self.play(Create(tbl))
        b1_r1 = Tex(r"Hours: 1 \quad\;\; 2 \quad\;\; 3 \quad\;\; 4").scale(1.0).shift(band_shift(1) + UP * 1.6)
        b1_r2 = Tex(r"Cost: 630 \; 910 \; 1\,190 \; 1\,470").scale(1.0).shift(band_shift(1) + UP * 0.7)
        self.play(Write(b1_r1)); self.wait(1.5)
        self.play(Write(b1_r2)); self.wait(2)
        b1_l1 = MathTex(r"910 - 630 = 280; \;\; 1\,190 - 910 = 280").scale(1.0).shift(band_shift(1) + DOWN * 0.3)
        self.play(Write(b1_l1)); self.wait(2.5)
        b1_l2 = MathTex(r"\text{Cost} = 350 + 280 \times \text{hours}").scale(1.1).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)
        b1_l3 = MathTex(r"\text{Check: } 350 + 280 \times 3 = R1\,190 \;\checkmark").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1_l3)); self.wait(2.5)

        # --- Band 2 (subtopic_2): constant product — inverse proportion ---
        self.next_band(2)
        b2_title = Tex(r"Bakkie hire R1\,800, split equally").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"1 pays 1\,800; 2 pay 900; 3 pay 600; 6 pay 300").scale(0.95).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1)); self.wait(2.5)
        b2_l2 = MathTex(r"1 \times 1\,800 = 2 \times 900 = 3 \times 600 = 1\,800").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2)); self.wait(2.5)
        b2_l3 = Tex("Constant PRODUCT: inverse proportion").scale(1.05).shift(band_shift(2) + DOWN * 0.8)
        b2_l4 = MathTex(r"\text{Cost per person} = 1\,800 \div \text{people}").scale(1.05).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l3)); self.wait(2)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): constant ratio, and the routine ---
        self.next_band(3)
        b3_title = Tex(r"Stokvel: R2\,000 at 8\% a year, untouched").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"2\,000 \to 2\,160 \to 2\,332{,}80 \to 2\,519{,}42").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"2\,160 \div 2\,000 = 1{,}08; \;\; 2\,332{,}80 \div 2\,160 = 1{,}08").scale(0.95).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l1)); self.wait(2.5)
        self.play(Write(b3_l2)); self.wait(2.5)
        b3_l3 = Tex(r"Rule: multiply by 1,08 each year — climbs ever steeper").scale(0.95).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3)); self.wait(2.5)
        b3_l4 = Tex("Differences? Products? Ratios? — test in that order").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): formula, table, graph ---
        self.next_band(4)
        b4_title = Tex("One relationship, three costumes").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Formula $\\to$ table: substitute chosen inputs").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"8 \text{ passengers: } 1\,800 \div 8 = R225 \text{ each}").scale(1.0).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l1)); self.wait(2.5)
        self.play(Write(b4_l2)); self.wait(2.5)
        b4_l3 = Tex("Passengers are DISCRETE: plot, do not join").scale(1.0).shift(band_shift(4) + DOWN * 0.8)
        b4_l4 = Tex("Hours are CONTINUOUS: join with a straight line").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l3)); self.wait(2.5)
        self.play(Write(b4_l4)); self.wait(2.5)

        # --- Band 5 (subtopic_3): the shapes that check you ---
        self.next_band(5)
        b5_title = Tex("The shapes are your self-check").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Constant difference: straight line, lifted by the fee").scale(0.95).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("Inverse proportion: falling curve that flattens").scale(0.95).shift(band_shift(5) + UP * 0.2)
        b5_l3 = Tex("Constant ratio: rising curve that steepens").scale(0.95).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l1)); self.wait(2.5)
        self.play(Write(b5_l2)); self.wait(2.5)
        self.play(Write(b5_l3)); self.wait(2.5)
        b5_l4 = Tex("Label both axes with quantity and unit — marks live there").scale(0.9).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l4)); self.wait(2.5)

        # --- Band 6 (subtopic_4): combination tariff forwards ---
        self.next_band(6)
        b6_title = Tex(r"Water: R145 basic $+$ R21,50 per k$\ell$").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Bill} = 145 + 21{,}50 \times \text{k}\ell").scale(1.1).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1)); self.wait(2.5)
        b6_l2 = MathTex(r"15\text{ k}\ell: \; 145 + 322{,}50 = R467{,}50").scale(1.05).shift(band_shift(6) + UP * 0.1)
        b6_l3 = MathTex(r"25\text{ k}\ell: \; 145 + 537{,}50 = R682{,}50").scale(1.05).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l2)); self.wait(2.5)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): working backwards ---
        self.next_band(7)
        b7_title = Tex(r"The bill is R790 — how much water?").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_wrong = MathTex(r"790 \div 21{,}50 = 36{,}7 \quad \text{(basic charge not removed!)}").scale(0.91).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_wrong))
        self.play(Create(strike(b7_wrong)))
        self.wait(2.5)
        b7_l1 = MathTex(r"790 - 145 = R645 \quad \text{(the water part)}").scale(1.05).shift(band_shift(7) + UP * 0.1)
        b7_l2 = MathTex(r"645 \div 21{,}50 = 30\text{ k}\ell").scale(1.1).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l1)); self.wait(2.5)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = MathTex(r"\text{Check: } 145 + 21{,}50 \times 30 = R790 \;\checkmark").scale(1.0).shift(band_shift(7) + DOWN * 1.9)
        b7_l4 = Tex("Subtract the fixed part FIRST, then divide by the rate").scale(0.95).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l3)); self.wait(2)
        self.play(Write(b7_l4)); self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the plumber who charges twice ---
        self.next_band(8)
        b8_title = Tex("The plumber charges twice").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2.5)
        b8_l1 = Tex("R350 just for arriving; then R280 an hour").scale(1.05).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1)); self.wait(3)
        b8_l2 = MathTex(r"630; \;\; 910; \;\; 1\,190; \;\; 1\,470 \quad \text{(+280 each step)}").scale(0.91).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2)); self.wait(3)
        b8_l3 = Tex("The R350 sits still; the R280 multiplies").scale(1.05).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(3)
        b8_l4 = Tex("Ask: what before anything happens, what per extra unit?").scale(0.95).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l4)); self.wait(3.5)

        # --- Band 9 (subtopic_6): the bakkie and the stokvel ---
        self.next_band(9)
        b9_title = Tex("Splitting the bakkie, growing the stokvel").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = Tex(r"1 to 2 people saves R900; 5 to 6 saves only R60").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1)); self.wait(3)
        b9_l2 = MathTex(r"\text{people} \times \text{price} = 1\,800 \text{ every time}").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(3)
        b9_l3 = Tex(r"Stokvel jumps GROW: 160; 172,80; 186,62").scale(0.95).shift(band_shift(9) + DOWN * 0.8)
        b9_l4 = Tex(r"Not ``add something'' — multiply by 1,08 each year").scale(0.95).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l3)); self.wait(3)
        self.play(Write(b9_l4)); self.wait(3.5)

        # --- Band 10 (subtopic_7): reading the rule backwards ---
        self.next_band(10)
        b10_title = Tex("Undo the rule in reverse order").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2.5)
        b10_l1 = MathTex(r"790 - 145 = R645 \quad \text{(pure water)}").scale(1.05).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1)); self.wait(3)
        b10_l2 = MathTex(r"645 \div 21{,}50 = 30\text{ k}\ell").scale(1.1).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(3)
        b10_l3 = Tex("The basic charge bought pipes, not water — off first").scale(0.95).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l3)); self.wait(3)
        b10_l4 = Tex(r"``The household used 30 kilolitres that month''").scale(1.0).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_l4)); self.wait(4)
