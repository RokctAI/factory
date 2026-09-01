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

# Band-layout whiteboard scene: sequential vertical bands, one per teaching
# beat, camera moves down between bands, add-only lifecycle. Exporter-safe
# mobjects only; every working line is a single-string MathTex revealed with
# Write. Covers all seven subtopics of the duo (Part 1 — Expert: 1-4;
# Part 2 — Simplifier: 5-7); band time apportioned to subtopics.json
# (245/235/245/240/195/195/195 of 1550 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AnnuitiesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): future value — derive, never memorise
        title = Tex("Annuities: Streams of Equal Payments").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = MathTex(r"\text{Last payment: } x, \;\; \text{one before: } x(1+i)").scale(1.0).shift(UP * 1.0)
        s0_l2 = MathTex(r"\text{First payment: } x(1+i)^{n-1}").scale(1.05).shift(UP * 0.1)
        s0_l3 = Tex(r"Geometric series: first term $x$, ratio $1+i$, $n$ terms").scale(1.0).shift(DOWN * 0.8)
        s0_l4 = MathTex(r"F = \frac{x\left[(1+i)^n - 1\right]}{i}").scale(1.25).shift(DOWN * 2.1)
        self.play(Write(s0_l1))
        self.wait(2.5)
        self.play(Write(s0_l2))
        self.wait(2)
        self.play(Write(s0_l3))
        self.wait(2)
        self.play(Write(s0_l4))
        self.play(Create(SurroundingRectangle(s0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): worked case — R1 000 monthly for 5 years
        self.next_band(1)
        b1_title = Tex(r"Save R1\,000 monthly, 5 years, 6\% p.a.\ monthly").scale(1.05).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = MathTex(r"i = \frac{0{,}06}{12} = 0{,}005, \quad n = 60").scale(1.1).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"1{,}005^{60} = 1{,}34885").scale(1.1).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"F = \frac{1\,000\,(0{,}34885)}{0{,}005} = 1\,000 \times 69{,}77").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = MathTex(r"F = \text{R}69\,770{,}03").scale(1.15).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)
        b1_l5 = Tex(r"Deposits R60\,000; interest earned R9\,770{,}03").scale(1.0).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): present value — discount every payment
        self.next_band(2)
        b2_title = Tex("Present value: the mathematics of loans").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"x \text{ in } k \text{ months: worth } \frac{x}{(1+i)^k}").scale(1.05).shift(band_shift(2) + UP * 1.0)
        b2_l2 = Tex(r"Sum the discounted payments — geometric again:").scale(1.0).shift(band_shift(2) + UP * 0.0)
        b2_l3 = MathTex(r"P = \frac{x\left[1 - (1+i)^{-n}\right]}{i}").scale(1.25).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex(r"Save $\Rightarrow$ future value").scale(1.0).shift(band_shift(2) + DOWN * 2.4)
        b2_l5 = Tex(r"Borrow $\Rightarrow$ present value").scale(1.0).shift(band_shift(2) + DOWN * 3.1)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): the car loan, worked in full
        self.next_band(3)
        b3_title = Tex(r"Borrow R250\,000 at 12\% p.a.\ monthly, 60 months").scale(1.0).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l0 = MathTex(r"x = \frac{P\,i}{1 - (1+i)^{-n}}").scale(1.05).shift(band_shift(3) + UP * 1.2)
        b3_l1 = MathTex(r"x = \frac{250\,000 \times 0{,}01}{1 - 1{,}01^{-60}}").scale(1.05).shift(band_shift(3) + UP * 0.2)
        b3_l2 = MathTex(r"1{,}01^{-60} = \frac{1}{1{,}8167} = 0{,}5504").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        b3_l3 = MathTex(r"x = \frac{2\,500}{0{,}4496} = \text{R}5\,561{,}11").scale(1.1).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l0))
        self.wait(2.5)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex(r"Total R333\,667 — borrowing costs R83\,667").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): sinking fund — price the gap
        self.next_band(4)
        b4_title = Tex("Sinking fund: saving for the machine's funeral").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"\text{New machine: } 500\,000 \times 1{,}06^5 = 669\,112{,}79").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"\text{Scrap: } 500\,000 \times 0{,}85^5 = 221\,852{,}66").scale(1.0).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"\text{Shortfall: } 669\,112{,}79 - 221\,852{,}66").scale(1.0).shift(band_shift(4) + DOWN * 0.8)
        b4_l4 = MathTex(r"= \text{R}447\,260{,}13").scale(1.1).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.wait(2.5)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = Tex(r"Inflation, depreciation, fund interest: three lanes").scale(1.0).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): solve the monthly payment
        self.next_band(5)
        b5_title = Tex(r"Fund earns 8\% p.a.\ monthly, 60 payments").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l0 = MathTex(r"i = \frac{0{,}08}{12}, \quad n = 60").scale(1.05).shift(band_shift(5) + UP * 1.2)
        b5_l1 = MathTex(r"x \times \frac{(1+i)^{60} - 1}{i} = 447\,260{,}13").scale(1.0).shift(band_shift(5) + UP * 0.2)
        b5_l2 = MathTex(r"\text{Factor} = 73{,}4769").scale(1.1).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_l0))
        self.wait(2)
        b5_l3 = MathTex(r"x = \frac{447\,260{,}13}{73{,}4769}").scale(1.1).shift(band_shift(5) + DOWN * 1.6)
        b5_l4 = MathTex(r"x = \text{R}6\,087{,}09 \text{ per month}").scale(1.1).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex(r"Timing traps: draw the timeline first").scale(0.95).shift(band_shift(5) + DOWN * 3.1)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): outstanding balance after 24 payments
        self.next_band(6)
        b6_title = Tex("Outstanding balance = PV of REMAINING payments").scale(1.0).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_wrong = MathTex(r"\text{After 24 of 60: } \tfrac{3}{5} \text{ of the debt left?}").scale(1.05).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_wrong))
        self.play(Create(strike(b6_wrong)))
        self.wait(2)
        b6_l1 = MathTex(r"\text{Bal} = \frac{5\,561{,}11\left[1 - 1{,}01^{-36}\right]}{0{,}01}").scale(1.0).shift(band_shift(6) + UP * 0.1)
        b6_l2 = MathTex(r"1{,}01^{36} = 1{,}4308 \;\Rightarrow\; \text{bracket} = 0{,}3011").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        b6_l3 = MathTex(r"\text{Balance} \approx \text{R}167\,431").scale(1.15).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex(r"R133\,467 paid, yet two thirds of R250\,000 still owing").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): amortisation — interest first, debt second
        self.next_band(7)
        b7_title = Tex("Inside every instalment").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"\text{Month 1 interest: } 1\% \times 250\,000 = 2\,500").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"\text{Debt reduced: } 5\,561{,}11 - 2\,500 = 3\,061{,}11").scale(1.05).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex(r"Fat balance: interest devours the payment").scale(1.05).shift(band_shift(7) + DOWN * 1.0)
        b7_l4 = Tex(r"Thin balance: almost all demolition").scale(1.05).shift(band_shift(7) + DOWN * 1.9)
        b7_l5 = Tex(r"Early overpayments shorten a loan dramatically").scale(1.0).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(2)
        self.play(Write(b7_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): sixty envelopes on the table
        self.next_band(8)
        b8_title = Tex("Sixty envelopes on the table").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Ask each envelope: how long did YOU earn?").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = MathTex(r"\text{Last: } 1\,000; \;\; \text{before: } 1\,000 \times 1{,}005; \;\ldots").scale(1.0).shift(band_shift(8) + UP * 0.2)
        b8_l3 = MathTex(r"\text{First: } 1\,000 \times 1{,}005^{59} \;\; \text{(geometric row)}").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = MathTex(r"\text{Sum} = \text{R}69\,770{,}03").scale(1.1).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        b8_l5 = Tex(r"Suspect the calendar: month-end drops, count stops at last").scale(0.9).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l5))
        self.wait(3.5)

        # --- Band 9 (subtopic_6): the furniture shop's fair price
        self.next_band(9)
        b9_title = Tex("The furniture shop's fair price").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"R500 next year is worth less than R500 today").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex(r"Fair cash price: all 24 payments, shrunk back, added").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"P = \frac{x\left[1 - (1+i)^{-n}\right]}{i}").scale(1.1).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = MathTex(r"\text{Paid } 333\,667 \text{ for a } 250\,000 \text{ loan}").scale(0.95).shift(band_shift(9) + DOWN * 1.9)
        b9_l5 = Tex(r"SAVE means future, OWE means present").scale(1.05).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l4))
        self.wait(2.5)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the debt that shrinks from the wrong end
        self.next_band(10)
        b10_title = Tex("The debt that shrinks from the wrong end").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Water tank: interest pours in, your bucket bails out").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10_l2 = MathTex(r"\text{In } 2\,500; \text{ out } 5\,561{,}11: \text{ debt} - 3\,061").scale(0.95).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex(r"Settlement after 24: shrink the 36 unpaid instalments").scale(0.95).shift(band_shift(10) + DOWN * 0.8)
        b10_l4 = MathTex(r"\text{Settlement} \approx \text{R}167\,431").scale(1.1).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10_l3))
        self.wait(2.5)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex(r"Every early extra rand strikes the flood at its strongest").scale(0.95).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10_l5))
        self.wait(4)
