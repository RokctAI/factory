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

# Band layout: one frame-height band per teaching beat; the camera moves down,
# nothing is removed. Exporter-supported mobjects only (Tex/MathTex/Line/
# Rectangle/SurroundingRectangle); single-string Write reveals throughout.
#
# Covers all seven subtopics (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7),
# band time roughly proportional to subtopics.json
# (215/220/225/230/195/195/195 of 1475 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class VatUifTariffsExchangeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): adding VAT ---
        title = Tex("VAT, UIF, Tariffs and Exchange Rates").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l1 = Tex(r"VAT $= 15\%$ added to most goods and services").scale(1.05).shift(UP * 1.1)
        self.play(Write(l1)); self.wait(2)
        l2 = MathTex(r"\text{VAT: } 360 \times 0{,}15 = R54").scale(1.1).shift(UP * 0.2)
        l3 = MathTex(r"\text{Till price: } 360 \times 1{,}15 = R414").scale(1.1).shift(DOWN * 0.7)
        self.play(Write(l2)); self.wait(2)
        self.play(Write(l3))
        self.play(Create(SurroundingRectangle(l3, color=GREEN)))
        self.wait(2.5)
        l4 = Tex("Excluding $=$ before tax; including $=$ what you pay").scale(1.0).shift(DOWN * 1.8)
        self.play(Write(l4)); self.wait(2.5)

        # --- Band 1 (subtopic_1): removing VAT, zero-rated basket ---
        self.next_band(1)
        b1_title = Tex("Removing VAT: the classic trap").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_wrong = MathTex(r"414 \times 0{,}85 = R351{,}90 \quad \text{(wrong by } R8{,}10)").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2.5)
        b1_l1 = Tex(r"R414 is 115\% of the original — divide by 1,15").scale(1.0).shift(band_shift(1) + UP * 0.1)
        b1_l2 = MathTex(r"414 \div 1{,}15 = R360").scale(1.15).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l1)); self.wait(2.5)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("Zero-rated: brown bread, maize meal, rice, milk, eggs").scale(0.95).shift(band_shift(1) + DOWN * 1.9)
        b1_l4 = Tex("Tax the taxable lines; leave the protected basket alone").scale(0.95).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l3)); self.wait(2)
        self.play(Write(b1_l4)); self.wait(2.5)

        # --- Band 2 (subtopic_2): UIF, one percent from each side ---
        self.next_band(2)
        b2_title = Tex(r"UIF: 1\% collected twice").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Worker: } 9\,200 \times 0{,}01 = R92").scale(1.1).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"\text{Employer adds another } R92").scale(1.05).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"\text{Fund receives } 92 + 92 = R184").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l1)); self.wait(2.5)
        self.play(Write(b2_l2)); self.wait(2)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex("Only R92 comes off Naledi's pay — read what is asked").scale(0.95).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l4)); self.wait(2.5)

        # --- Band 3 (subtopic_2): the payslip, gross to net ---
        self.next_band(3)
        b3_title = Tex("The payslip: gross to net").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        slip = Rectangle(width=8.6, height=3.4).shift(band_shift(3) + UP * 0.2)
        self.play(Create(slip))
        b3_r1 = Tex(r"Gross pay \hfill R9\,200").scale(1.0).shift(band_shift(3) + UP * 1.3)
        b3_r2 = Tex(r"UIF (1\% of gross) \quad $-$R92").scale(1.0).shift(band_shift(3) + UP * 0.5)
        b3_r3 = Tex(r"Other deductions \quad $-$R648").scale(1.0).shift(band_shift(3) + DOWN * 0.3)
        b3_r4 = MathTex(r"\text{Net: } 9\,200 - 92 - 648 = R8\,460").scale(1.0).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_r1)); self.wait(2)
        self.play(Write(b3_r2)); self.wait(2)
        self.play(Write(b3_r3)); self.wait(2)
        self.play(Write(b3_r4))
        self.play(Create(SurroundingRectangle(b3_r4, color=GREEN)))
        self.wait(2.5)
        b3_l1 = Tex("UIF is worked on GROSS, before other deductions").scale(0.95).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3_l1)); self.wait(2.5)

        # --- Band 4 (subtopic_3): exchange rates, both directions ---
        self.next_band(4)
        b4_title = Tex(r"Exchange rate: one euro costs R19,80").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{Buy 150 euros: } 150 \times 19{,}80 = R2\,970").scale(1.05).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"R6\,000 \text{ buys } 6\,000 \div 19{,}80 = 303{,}03 \text{ euros}").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l1)); self.wait(2.5)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex("Toward rands: multiply. Toward the foreign unit: divide.").scale(0.95).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3)); self.wait(2.5)
        b4_l4 = Tex(r"R19,80 $\to$ R20,60 per euro: the rand WEAKENED").scale(0.95).shift(band_shift(4) + DOWN * 1.8)
        b4_l5 = MathTex(r"\text{250 euros: } 250 \times 19{,}80 = R4\,950; \;\; \text{at } 20{,}60 = R5\,150").scale(0.87).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l4)); self.wait(2)
        self.play(Write(b4_l5)); self.wait(2.5)

        # --- Band 5 (subtopic_4): two phone deals, tested ---
        self.next_band(5)
        b5_title = Tex(r"Option P: R120 $+$ R0,60/min. \; Q: R1,40/min.").scale(1.0).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"P = 120 + 0{,}60 \times m; \qquad Q = 1{,}40 \times m").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1)); self.wait(2.5)
        b5_l2 = MathTex(r"100\text{ min: } P = R180, \; Q = R140 \;\; (Q \text{ wins})").scale(1.0).shift(band_shift(5) + UP * 0.2)
        b5_l3 = MathTex(r"250\text{ min: } P = R270, \; Q = R350 \;\; (P \text{ wins})").scale(1.0).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l2)); self.wait(2.5)
        self.play(Write(b5_l3)); self.wait(2.5)

        # --- Band 6 (subtopic_4): the crossing point ---
        self.next_band(6)
        b6_title = Tex("Where the options trade places").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"120 + 0{,}60 \times m = 1{,}40 \times m").scale(1.1).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"120 = 0{,}80 \times m").scale(1.1).shift(band_shift(6) + UP * 0.2)
        b6_l3 = MathTex(r"m = 150 \text{ minutes}").scale(1.1).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l1)); self.wait(2.5)
        self.play(Write(b6_l2)); self.wait(2)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = Tex("Below 150 min: take Q. Above: take P.").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        b6_l5 = Tex("Answer as advice in words — who chooses what, and why").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_l4)); self.wait(2.5)
        self.play(Write(b6_l5)); self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the stowaway in the price ---
        self.next_band(7)
        b7_title = Tex("Fifteen percent hiding inside the price").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2.5)
        b7_l1 = MathTex(r"\text{No tax yet? } 360 \times 1{,}15 = R414").scale(1.05).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1)); self.wait(3)
        b7_l2 = MathTex(r"\text{Tax inside? } 414 \div 1{,}15 = R360").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(3)
        b7_l3 = Tex(r"Taking 15\% off gives R351,90 — feels safe, scores nothing").scale(0.95).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3)); self.wait(3)
        b7_l4 = Tex("The protected basket rides free: bread, maize, milk, eggs").scale(0.9).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l4)); self.wait(3.5)

        # --- Band 8 (subtopic_6): the two R92s ---
        self.next_band(8)
        b8_title = Tex("The two R92s on the payslip").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2.5)
        b8_l1 = Tex(r"One percent: slide the comma — R9\,200 $\to$ R92").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1)); self.wait(3)
        b8_l2 = Tex(r"Naledi contributes R92; the fund receives R184").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(3)
        b8_l3 = MathTex(r"9\,200 - 92 - 648 = R8\,460 \text{ net}").scale(1.05).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3)); self.wait(3)
        b8_l4 = Tex("Gross minus deductions equals net — always").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l4)); self.wait(3.5)

        # --- Band 9 (subtopic_7): rands abroad, and the phone shop ---
        self.next_band(9)
        b9_title = Tex("A euro is an item priced at R19,80").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = MathTex(r"150 \text{ of them: } 150 \times 19{,}80 = R2\,970").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l2 = MathTex(r"R6\,000 \text{ buys: } 6\,000 \div 19{,}80 \approx 303 \text{ euros}").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1)); self.wait(3)
        self.play(Write(b9_l2)); self.wait(3)
        b9_l3 = Tex(r"Weaker rand: petrol hurts, but Dublin's 250 euros grow").scale(0.95).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3)); self.wait(3)
        b9_l4 = Tex(r"Phone deals: rent $+$ cheap minutes vs no rent, dear minutes").scale(0.9).shift(band_shift(9) + DOWN * 1.7)
        b9_l5 = Tex(r"``At 100 minutes, take Q and keep R40''").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l4)); self.wait(3)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(4)
