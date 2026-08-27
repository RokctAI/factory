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

# Band layout: one frame-height band per teaching beat; the camera moves down,
# nothing is removed. Every mobject serializes to the exporter's
# text/line/rect/dot/circle vocabulary; every line of working is a
# single-string Tex/MathTex revealed with Write — no sub-part transforms.
#
# Covers all seven subtopics of the session duo (Part 1 — Expert: subtopics
# 1-4; Part 2 — Simplifier: subtopics 5-7), band time roughly proportional to
# subtopics.json (215/225/220/225/190/200/190 of 1465 s).

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
        # Intro beat: topic held full screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the two variables ---
        title = Tex("Relationships, Tables and Formulae").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        v1 = Tex("INDEPENDENT: what you choose — hours, litres, people").scale(0.95).shift(UP * 1.0)
        v2 = Tex("DEPENDENT: what follows — the amount you pay").scale(0.95).shift(UP * 0.1)
        v3 = Tex("Horizontal axis: independent. Vertical: dependent.").scale(0.95).shift(DOWN * 0.8)
        self.play(Write(v1)); self.wait(2.5)
        self.play(Write(v2)); self.wait(2.5)
        self.play(Write(v3)); self.wait(3)

        # --- Band 1 (subtopic_1): the plumber's table and formula ---
        self.next_band(1)
        b1_title = Tex("Plumber: R400 call-out $+$ R260 per hour").scale(1.05).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_t = MathTex(r"660; \quad 920; \quad 1\,180; \quad 1\,440").scale(1.05).shift(band_shift(1) + UP * 1.3)
        self.play(Write(b1_t)); self.wait(2)
        b1_d = MathTex(r"+260 \qquad +260 \qquad +260").scale(0.95).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_d)); self.wait(2.5)
        b1_f = MathTex(r"\text{Cost} = 400 + 260 \times \text{hours}").scale(1.05).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_f))
        self.play(Create(SurroundingRectangle(b1_f, color=GREEN)))
        self.wait(2.5)
        b1_c = MathTex(r"\text{Check: } 400 + 260 \times 3 = 1\,180 \checkmark").scale(0.95).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(b1_c))
        self.wait(3)

        # --- Band 2 (subtopic_2): constant product — inverse proportion ---
        self.next_band(2)
        b2_title = Tex("Bakkie hire R2\\,400, split equally").scale(1.1).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_t = MathTex(r"2\,400; \; 1\,200; \; 800; \; 600; \; 480; \; 400").scale(0.95).shift(band_shift(2) + UP * 1.3)
        self.play(Write(b2_t)); self.wait(2.5)
        b2_p = MathTex(r"1 \times 2\,400 = 2 \times 1\,200 = 3 \times 800 = 2\,400").scale(0.95).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_p))
        self.play(Create(SurroundingRectangle(b2_p, color=GREEN)))
        self.wait(2.5)
        b2_f = MathTex(r"\text{Cost per person} = 2\,400 \div \text{people}").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_f)); self.wait(2)
        b2_s = Tex("Constant PRODUCT $=$ inverse proportion").scale(0.95).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_s))
        self.wait(3)

        # --- Band 3 (subtopic_2): constant ratio, and the routine ---
        self.next_band(3)
        b3_title = Tex("Stokvel: R5\\,000 at 6\\% a year, untouched").scale(1.05).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_t = MathTex(r"5\,000; \; 5\,300; \; 5\,618; \; 5\,955{,}08").scale(1.0).shift(band_shift(3) + UP * 1.3)
        self.play(Write(b3_t)); self.wait(2.5)
        b3_r = MathTex(r"5\,300 \div 5\,000 = 1{,}06; \quad 5\,618 \div 5\,300 = 1{,}06").scale(0.9).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_r))
        self.play(Create(SurroundingRectangle(b3_r, color=GREEN)))
        self.wait(2.5)
        b3_route = Tex("Routine: differences? products? ratios?").scale(0.95).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_route))
        self.wait(3)

        # --- Band 4 (subtopic_3): formula, table, graph ---
        self.next_band(4)
        b4_title = Tex("One relationship, three costumes").scale(1.1).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("FORMULA $\\to$ TABLE: substitute inputs").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l2 = MathTex(r"8 \text{ people: } 2\,400 \div 8 = R300").scale(1.0).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l1)); self.wait(2)
        self.play(Write(b4_l2)); self.wait(2.5)
        b4_l3 = Tex("Discrete (people): plot, never join").scale(0.95).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = Tex("Continuous (hours): join the points").scale(0.95).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l3)); self.wait(2.5)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): the shapes that check you ---
        self.next_band(5)
        b5_title = Tex("Shapes that audit your arithmetic").scale(1.1).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Constant difference: straight line, lifted by the fixed charge").scale(0.85).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("Inverse proportion: falling curve that flattens").scale(0.9).shift(band_shift(5) + UP * 0.3)
        b5_l3 = Tex("Constant ratio: rising curve that steepens").scale(0.9).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_l1)); self.wait(2.5)
        self.play(Write(b5_l2)); self.wait(2.5)
        self.play(Write(b5_l3)); self.wait(2.5)
        b5_l4 = Tex("Label both axes with quantity AND unit — marks live there").scale(0.85).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): combination tariff forwards ---
        self.next_band(6)
        b6_title = Tex("Water: R160 basic $+$ R24,50 per k$\\ell$").scale(1.05).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_f = MathTex(r"\text{Bill} = 160 + 24{,}50 \times \text{k}\ell").scale(1.05).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_f)); self.wait(2.5)
        b6_l1 = MathTex(r"12 \text{ k}\ell: \; 160 + 294 = R454{,}00").scale(1.0).shift(band_shift(6) + UP * 0.2)
        b6_l2 = MathTex(r"20 \text{ k}\ell: \; 160 + 490 = R650{,}00").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l1)); self.wait(2.5)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): working backwards ---
        self.next_band(7)
        b7_title = Tex("The bill says R699 — how much water?").scale(1.05).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_w = MathTex(r"699 \div 24{,}50 = 28{,}5 \quad \text{(wrong!)}").scale(1.0).shift(band_shift(7) + UP * 1.3)
        self.play(Write(b7_w))
        self.play(Create(strike(b7_w)))
        self.wait(2)
        b7_l1 = MathTex(r"699 - 160 = R539").scale(1.05).shift(band_shift(7) + UP * 0.2)
        b7_l2 = MathTex(r"539 \div 24{,}50 = 22 \text{ k}\ell").scale(1.05).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l1)); self.wait(2.5)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_c = MathTex(r"\text{Check: } 160 + 24{,}50 \times 22 = 699 \checkmark").scale(0.95).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_c))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the plumber who charges twice ---
        self.next_band(8)
        b8_title = Tex("The plumber who charges twice").scale(1.15).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2.5)
        b8_l1 = Tex("R400 for arriving. R260 an hour after that.").scale(0.95).shift(band_shift(8) + UP * 1.3)
        self.play(Write(b8_l1)); self.wait(3)
        b8_l2 = MathTex(r"660; \; 920; \; 1\,180; \; 1\,440 \quad (+260)").scale(1.0).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l2)); self.wait(3)
        b8_l3 = Tex("The R400 sits still; the R260 multiplies").scale(0.95).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(3.5)

        # --- Band 9 (subtopic_6): the bakkie and the stokvel ---
        self.next_band(9)
        b9_title = Tex("Splitting the bakkie, growing the stokvel").scale(1.1).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = MathTex(r"\text{People} \times \text{price} = 2\,400, \text{ always}").scale(1.0).shift(band_shift(9) + UP * 1.3)
        self.play(Write(b9_l1)); self.wait(3)
        b9_l2 = Tex("1 to 2 saves R1\\,200; 5 to 6 saves R80").scale(0.95).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2)); self.wait(3)
        b9_l3 = MathTex(r"\text{Stokvel: } \times 1{,}06 \text{ each year — jumps grow}").scale(0.95).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(3.5)

        # --- Band 10 (subtopic_7): reading the rule backwards ---
        self.next_band(10)
        b10_title = Tex("Reading the rule backwards").scale(1.15).shift(band_shift(10) + UP * 2.4)
        self.play(Write(b10_title))
        self.wait(2.5)
        b10_l1 = Tex("Fixed part off FIRST: $699 - 160 = 539$").scale(1.0).shift(band_shift(10) + UP * 1.3)
        self.play(Write(b10_l1)); self.wait(3)
        b10_l2 = MathTex(r"539 \div 24{,}50 = 22 \text{ k}\ell").scale(1.05).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(3)
        b10_l3 = Tex("Check forwards, then answer in a sentence with units").scale(0.9).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10_l3))
        self.wait(4)
