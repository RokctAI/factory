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

# Band layout: one frame-height band per teaching beat, camera moves down to
# clean space, nothing is ever removed. Every mobject serializes to the
# exporter's text/line/rect/dot/circle vocabulary; every line of working is a
# single-string Tex/MathTex revealed with Write — no sub-part transforms.
#
# Covers all seven subtopics of the session duo (Part 1 — Expert: subtopics
# 1-4; Part 2 — Simplifier: subtopics 5-7), band time roughly proportional to
# subtopics.json (215/215/225/230/195/195/195 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FinancialDocumentsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the document and its vocabulary ---
        title = Tex("Financial Documents: Income and Expenditure").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        v1 = Tex(r"Consumption $=$ current reading $-$ previous").scale(1.1).shift(UP * 1.1)
        v2 = Tex(r"Tariff $=$ price per unit (kWh, k$\ell$)").scale(1.1).shift(UP * 0.2)
        v3 = Tex("Arrears $=$ unpaid amounts from earlier months").scale(1.1).shift(DOWN * 0.7)
        v4 = Tex("Due date $=$ last day to pay").scale(1.1).shift(DOWN * 1.6)
        self.play(Write(v1)); self.wait(2)
        self.play(Write(v2)); self.wait(2)
        self.play(Write(v3)); self.wait(2)
        self.play(Write(v4)); self.wait(2.5)

        # --- Band 1 (subtopic_1): the municipal account, checked line by line ---
        self.next_band(1)
        b1_title = Tex("Municipal account — check every line").scale(1.15).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        doc = Rectangle(width=10.0, height=4.6).shift(band_shift(1) + DOWN * 0.3)
        self.play(Create(doc))
        rows_y = [1.4, 0.5, -0.4, -1.3, -2.2]
        labels = [
            r"Electricity: $320 \times 2{,}10$",
            r"Basic charge (fixed)",
            r"Subtotal",
            r"VAT: $852 \times 0{,}15$",
            r"TOTAL DUE",
        ]
        amounts = [r"R672{,}00", r"R180{,}00", r"R852{,}00", r"R127{,}80", r"R979{,}80"]
        for y, lab, amt in zip(rows_y, labels, amounts):
            row_l = Tex(lab).scale(1.0).shift(band_shift(1) + UP * y + LEFT * 2.6)
            row_r = MathTex(amt).scale(1.0).shift(band_shift(1) + UP * y + RIGHT * 3.4)
            self.play(Write(row_l), Write(row_r))
            self.wait(2)
        sep = Line(band_shift(1) + LEFT * 5.0 + DOWN * 1.75, band_shift(1) + RIGHT * 5.0 + DOWN * 1.75)
        self.play(Create(sep))
        total_row = MathTex(r"R979{,}80").scale(1.0).shift(band_shift(1) + DOWN * 2.2 + RIGHT * 3.4)
        self.play(Create(SurroundingRectangle(total_row, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_1): recovering the amount before VAT ---
        self.next_band(2)
        b2_title = Tex("Given the VAT-inclusive total only?").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_wrong = MathTex(r"979{,}80 - 15\% \quad \text{(wrong!)}").scale(1.1).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2)
        b2_l1 = Tex(r"Divide by 1,15 to go back before VAT").scale(1.1).shift(band_shift(2))
        b2_l2 = MathTex(r"979{,}80 \div 1{,}15 = R852{,}00").scale(1.15).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l1)); self.wait(2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the three kinds of income ---
        self.next_band(3)
        b3_title = Tex("Income: fixed, variable, occasional").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Fixed: same amount, regular — salary R9\\,500").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("Variable: regular, changing — wages, commission").scale(1.05).shift(band_shift(3) + UP * 0.2)
        b3_l3 = Tex("Occasional: now and then — gift, bonus").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l1)); self.wait(2.5)
        self.play(Write(b3_l2)); self.wait(2.5)
        self.play(Write(b3_l3)); self.wait(2)
        b3_rule = Tex("Classify BEFORE calculating — marks for the reason").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_rule))
        self.wait(2.5)

        # --- Band 4 (subtopic_2): variable income, worked ---
        self.next_band(4)
        b4_title = Tex("Palesa's variable income").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{Wages: } 28{,}50 \times 40 = R1\,140").scale(1.1).shift(band_shift(4) + UP * 1.0)
        b4_l2 = MathTex(r"\text{Commission: } 0{,}03 \times 42\,000 = R1\,260").scale(1.1).shift(band_shift(4) + UP * 0.1)
        b4_l3 = Tex("February sales: nothing $\\Rightarrow$ commission R0").scale(1.05).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l1)); self.wait(2.5)
        self.play(Write(b4_l2)); self.wait(2.5)
        self.play(Write(b4_l3)); self.wait(2)
        b4_rule = Tex("Budget on a realistic month, never the best one").scale(1.0).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_rule))
        self.wait(3)

        # --- Band 5 (subtopic_3): the household budget, totalled ---
        self.next_band(5)
        b5_title = Tex("The monthly budget").scale(1.15).shift(band_shift(5) + UP * 2.6)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_in = MathTex(r"\text{Income: } 9\,500 + 2\,500 = R12\,000").scale(1.05).shift(band_shift(5) + UP * 1.7)
        self.play(Write(b5_in))
        self.wait(2)
        b5_taxi = MathTex(r"\text{Taxi: } 14{,}50 \times 44 = R638").scale(1.05).shift(band_shift(5) + UP * 0.8)
        self.play(Write(b5_taxi))
        self.wait(2)
        b5_e1 = Tex(r"Rent 3\,800; groceries 2\,500; electricity 850").scale(1.0).shift(band_shift(5) + DOWN * 0.1)
        b5_e2 = Tex(r"airtime 450; stokvel 500; school 600").scale(1.0).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_e1)); self.wait(2)
        self.play(Write(b5_e2)); self.wait(2)
        b5_tot = MathTex(r"\text{Total expenditure} = R9\,338").scale(1.1).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_tot))
        self.play(Create(SurroundingRectangle(b5_tot, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_3): surplus or deficit ---
        self.next_band(6)
        b6_title = Tex("Income minus expenditure").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"12\,000 - 9\,338 = R2\,662").scale(1.2).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2.5)
        b6_l2 = Tex("Positive $=$ SURPLUS; negative $=$ DEFICIT").scale(1.05).shift(band_shift(6))
        b6_l3 = Tex("Surplus of R2\\,662: the R302 instalment is affordable").scale(1.0).shift(band_shift(6) + DOWN * 1.0)
        b6_l4 = Tex("Taxi fare recurs, but the AMOUNT changes: variable").scale(1.0).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l2)); self.wait(2.5)
        self.play(Write(b6_l3)); self.wait(2.5)
        self.play(Write(b6_l4)); self.wait(3)

        # --- Band 7 (subtopic_4): simple interest on the fridge loan ---
        self.next_band(7)
        b7_title = Tex(r"Fridge loan: R8\,000 at 12\% for 3 years").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Simple interest: on the ORIGINAL amount only").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = MathTex(r"\text{One year: } 8\,000 \times 0{,}12 = R960").scale(1.1).shift(band_shift(7) + UP * 0.3)
        b7_l3 = MathTex(r"\text{Three years: } 960 \times 3 = R2\,880").scale(1.1).shift(band_shift(7) + DOWN * 0.6)
        b7_l4 = MathTex(r"\text{Total: } 8\,000 + 2\,880 = R10\,880").scale(1.1).shift(band_shift(7) + DOWN * 1.5)
        b7_l5 = MathTex(r"10\,880 \div 36 = R302{,}22 \text{ a month}").scale(1.1).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l1)); self.wait(2)
        self.play(Write(b7_l2)); self.wait(2)
        self.play(Write(b7_l3)); self.wait(2)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        self.play(Write(b7_l5)); self.wait(3)

        # --- Band 8 (subtopic_4): savings side and the two traps ---
        self.next_band(8)
        b8_title = Tex("Interest for the saver — and two traps").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = MathTex(r"5\,000 \times 0{,}065 = R325 \text{ per year}").scale(1.1).shift(band_shift(8) + UP * 1.0)
        b8_l2 = MathTex(r"\text{Two years: } 5\,000 + 650 = R5\,650").scale(1.1).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l1)); self.wait(2.5)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_w1 = MathTex(r"8\,000 \times 12 \quad \text{(rate not converted!)}").scale(1.05).shift(band_shift(8) + DOWN * 1.0)
        self.play(Write(b8_w1))
        self.play(Create(strike(b8_w1)))
        self.wait(2)
        b8_l3 = Tex(r"12\% $= 0{,}12$; \; 18 months $= 1{,}5$ years").scale(1.05).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l3))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): the envelope from the municipality ---
        self.next_band(9)
        b9_title = Tex("The bill only says three things").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = Tex("What you used, what it costs, when to pay").scale(1.05).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1)); self.wait(3)
        b9_l2 = MathTex(r"\text{Used: } 320 \times 2{,}10 = R672").scale(1.1).shift(band_shift(9) + UP * 0.3)
        b9_l3 = MathTex(r"\text{Plus basic charge: } 672 + 180 = R852").scale(1.1).shift(band_shift(9) + DOWN * 0.6)
        b9_l4 = MathTex(r"\text{Plus VAT: } 852 + 127{,}80 = R979{,}80").scale(1.1).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_l2)); self.wait(3)
        self.play(Write(b9_l3)); self.wait(3)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(3)
        b9_l5 = Tex(r"Backwards? Divide by 1,15 — never take 15\% off").scale(1.0).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l5))
        self.wait(3.5)

        # --- Band 10 (subtopic_6): the bucket ---
        self.next_band(10)
        b10_title = Tex("The household is a bucket").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2.5)
        b10_l1 = Tex("Income pours in the top; expenses leak out").scale(1.05).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1)); self.wait(3)
        b10_l2 = MathTex(r"\text{In: } R12\,000").scale(1.1).shift(band_shift(10) + UP * 0.3)
        b10_l3 = MathTex(r"\text{Out: } R9\,338").scale(1.1).shift(band_shift(10) + DOWN * 0.5)
        b10_l4 = MathTex(r"12\,000 - 9\,338 = R2\,662 \text{ surplus}").scale(1.1).shift(band_shift(10) + DOWN * 1.4)
        self.play(Write(b10_l2)); self.wait(2.5)
        self.play(Write(b10_l3)); self.wait(2.5)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(3)
        b10_l5 = Tex("Short instead? A deficit — a plan to borrow").scale(1.0).shift(band_shift(10) + DOWN * 2.4)
        self.play(Write(b10_l5))
        self.wait(3.5)

        # --- Band 11 (subtopic_7): sticker price vs the truth ---
        self.next_band(11)
        b11_title = Tex("What the loan really costs").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2.5)
        b11_l1 = MathTex(r"\text{Each year: } 8\,000 \times 0{,}12 = R960").scale(1.1).shift(band_shift(11) + UP * 1.1)
        b11_l2 = MathTex(r"\text{Three years: } 3 \times 960 = R2\,880").scale(1.1).shift(band_shift(11) + UP * 0.2)
        b11_l3 = MathTex(r"8\,000 + 2\,880 = R10\,880").scale(1.15).shift(band_shift(11) + DOWN * 0.7)
        self.play(Write(b11_l1)); self.wait(3)
        self.play(Write(b11_l2)); self.wait(3)
        self.play(Write(b11_l3))
        self.play(Create(SurroundingRectangle(b11_l3, color=GREEN)))
        self.wait(3)
        b11_l4 = Tex(r"Sticker says R8\,000; the truth says R10\,880").scale(1.05).shift(band_shift(11) + DOWN * 1.7)
        b11_l5 = Tex(r"About R302 a month for 36 months").scale(1.05).shift(band_shift(11) + DOWN * 2.6)
        self.play(Write(b11_l4)); self.wait(3)
        self.play(Write(b11_l5)); self.wait(4)
