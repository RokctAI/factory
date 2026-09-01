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
# mobjects only (Tex/MathTex/Line/Rectangle); every working line is a
# single-string MathTex revealed with Write. Covers all seven subtopics of
# the duo (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7); band time
# apportioned to subtopics.json (245/240/245/235/195/195/195 of 1550 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class AnnuitiesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): future value — derive, never memorise
        title = Tex("Future value: a stream of payments").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = MathTex(r"\text{last: } x, \quad \text{before: } x(1+i), \quad \dots, \quad \text{first: } x(1+i)^{n-1}").scale(0.9).shift(UP * 0.9)
        self.play(Write(s0_l1))
        self.wait(2.5)
        s0_l2 = Tex(r"Geometric series: first term $x$, ratio $1+i$, $n$ terms").scale(1.0).shift(UP * 0.0)
        self.play(Write(s0_l2))
        self.wait(2)
        s0_l3 = MathTex(r"F = \frac{x\left[(1+i)^n - 1\right]}{i}").scale(1.2).shift(DOWN * 1.3)
        self.play(Write(s0_l3))
        self.play(Create(SurroundingRectangle(s0_l3, color=YELLOW)))
        self.wait(3)

        # --- Band 1 (subtopic_1): worked case — R1 500 monthly for 5 years
        self.next_band(1)
        b1_title = Tex(r"R1\,500 monthly, 5 years, 9\% p.a. monthly").scale(1.05).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"i = 0{,}0075, \quad n = 60").scale(1.1).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"1{,}0075^{60} = 1{,}56568 \Rightarrow \text{factor} = \frac{0{,}56568}{0{,}0075} = 75{,}4241").scale(0.9).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = MathTex(r"F = 1\,500 \times 75{,}4241 = \text{R}113\,136{,}21").scale(1.05).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_l4 = MathTex(r"\text{deposits } 90\,000 + \text{ interest } 23\,136{,}21").scale(1.0).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): present value — discount every payment
        self.next_band(2)
        b2_title = Tex("Present value: the mathematics of loans").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"x \text{ in } k \text{ months is worth } \frac{x}{(1+i)^k} \text{ today}").scale(1.0).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"P = \frac{x\left[1 - (1+i)^{-n}\right]}{i}").scale(1.2).shift(band_shift(2) + DOWN * 0.2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=YELLOW)))
        self.wait(2.5)
        b2_l3 = Tex(r"The lump today equals the stream's value today").scale(1.0).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(b2_l3))
        self.wait(3)

        # --- Band 3 (subtopic_2): the bakkie loan, worked in full
        self.next_band(3)
        b3_title = Tex(r"R180\,000 bakkie, 10{,}5\% p.a. monthly, 48 months").scale(1.0).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"1{,}00875^{48} = 1{,}5192 \Rightarrow 1 - 1{,}00875^{-48} = 0{,}3418").scale(0.9).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"x = \frac{180\,000 \times 0{,}00875}{0{,}3418} = \text{R}4\,608{,}61").scale(1.05).shift(band_shift(3) + UP * 0.0)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = MathTex(r"48 \times 4\,608{,}61 \approx \text{R}221\,213").scale(1.0).shift(band_shift(3) + DOWN * 1.1)
        b3_l4 = MathTex(r"\text{cost of credit} \approx \text{R}41\,213").scale(1.05).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): sinking fund — price the gap
        self.next_band(4)
        b4_title = Tex("Sinking fund: price the gap").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{new: } 800\,000 \times 1{,}07^{6} = 1\,200\,584{,}28").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"\text{scrap: } 800\,000 \times 0{,}88^{6} = 371\,523{,}27").scale(1.0).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"\text{target: } 1\,200\,584{,}28 - 371\,523{,}27 = 829\,061{,}01").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex(r"Inflation, depreciation, fund rate — three lanes").scale(1.0).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): solve the monthly payment
        self.next_band(5)
        b5_title = Tex("Solve the monthly payment").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"\frac{x\left[1{,}0075^{72} - 1\right]}{0{,}0075} = 829\,061{,}01").scale(1.0).shift(band_shift(5) + UP * 1.0)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"\text{factor} = 95{,}0070").scale(1.05).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"x = \frac{829\,061{,}01}{95{,}0070} = \text{R}8\,726{,}31").scale(1.1).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex(r"Timeline diagram guards the exponents").scale(1.0).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): outstanding balance after 18 payments
        self.next_band(6)
        b6_title = Tex("Outstanding balance after 18 payments").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Balance = present value of the REMAINING payments").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=YELLOW)))
        self.wait(2.5)
        b6_l2 = MathTex(r"B = \frac{4\,608{,}61\left[1 - 1{,}00875^{-30}\right]}{0{,}00875}").scale(1.0).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"B \approx \text{R}121\,138").scale(1.1).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = MathTex(r"\approx 83\,000 \text{ paid, yet two thirds still owing}").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): amortisation — interest first, debt second
        self.next_band(7)
        b7_title = Tex("Inside one instalment").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"\text{month 1 interest: } 0{,}00875 \times 180\,000 = 1\,575").scale(1.0).shift(band_shift(7) + UP * 1.0)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"\text{debt reduced: } 4\,608{,}61 - 1\,575 = 3\,033{,}61").scale(1.0).shift(band_shift(7) + UP * 0.0)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex(r"Interest first, debt second — the split shifts monthly").scale(1.0).shift(band_shift(7) + DOWN * 1.1)
        b7_l4 = Tex(r"Early overpayments shorten a loan dramatically").scale(1.0).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): sixty envelopes on the table
        self.next_band(8)
        b8_title = Tex("Sixty envelopes on the table").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"\text{last: } 1\,500, \quad \text{next: } 1\,500 \times 1{,}0075, \; \dots").scale(0.95).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"\text{first: } 1\,500 \times 1{,}0075^{59} \; \text{ — a geometric series}").scale(0.95).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"\text{sum} = \text{R}113\,136{,}21").scale(1.1).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex(r"Check the calendar: month-end drops, count stops at the last").scale(0.9).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): the furniture shop's fair price
        self.next_band(9)
        b9_title = Tex("The furniture shop's fair price").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Every promised payment shrinks back to today").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"\text{cash price} = \frac{x\left[1 - (1+i)^{-n}\right]}{i}").scale(1.05).shift(band_shift(9) + UP * 0.0)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=YELLOW)))
        self.wait(2.5)
        b9_l3 = MathTex(r"180\,000 \text{ loan} \Rightarrow 48 \times 4\,608{,}61 \approx 221\,213").scale(0.95).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex(r"SAVE means future value; OWE means present value").scale(1.0).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l4))
        self.wait(3)

        # --- Band 10 (subtopic_7): the debt that shrinks from the wrong end
        self.next_band(10)
        b10_title = Tex("The debt that shrinks from the wrong end").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"\text{tank fills: } 1\,575 \text{ in} \quad \text{bucket bails: } 4\,608{,}61").scale(0.95).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"\text{settlement} = \text{PV of 30 remaining} \approx \text{R}121\,138").scale(0.95).shift(band_shift(10) + UP * 0.0)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = Tex(r"Early extra rands strike the water at its deepest").scale(1.0).shift(band_shift(10) + DOWN * 1.1)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex(r"Compare loans by their leaks, never their instalments").scale(1.0).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(4)
