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

# Band-layout whiteboard scene for concentration-and-empirical-formula
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe mobjects, add-only lifecycle, one band per teaching beat.
# Time apportioned to subtopics.json (230/220/240/260/180/180/170 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ConcentrationAndEmpiricalFormulaSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the formula and its two guards ---
        title = Tex("Concentration and Empirical Formula").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = MathTex(r"c = \frac{n}{V}").scale(1.4).shift(UP * 0.6)
        self.play(Write(d1))
        self.play(Create(SurroundingRectangle(d1, color=GREEN)))
        self.wait(2.5)
        d2 = Tex("Guard 1: grams $\\to$ moles ($n = m/M$)").scale(1.0).shift(DOWN * 0.8)
        self.play(Write(d2))
        self.wait(2)
        d3 = Tex("Guard 2: cm$^3$ $\\div$ 1000 $\\to$ dm$^3$").scale(1.0).shift(DOWN * 1.8)
        self.play(Write(d3))
        self.wait(3)

        # --- Band 1 (subtopic_1): Na2CO3 worked in full ---
        self.next_band(1)
        b1t = Tex("10,6 g of Na$_2$CO$_3$ in 200 cm$^3$").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = MathTex(r"M = 46 + 12 + 48 = 106 \text{ g/mol}").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1a))
        self.wait(2.5)
        b1b = MathTex(r"n = \frac{10{,}6}{106} = 0{,}1 \text{ mol}").scale(1.0).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1b))
        self.wait(2.5)
        b1c = MathTex(r"V = \frac{200}{1000} = 0{,}2 \text{ dm}^3").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1c))
        self.wait(2.5)
        b1d = MathTex(r"c = \frac{0{,}1}{0{,}2} = 0{,}5 \text{ mol/dm}^3").scale(1.05).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1d))
        self.play(Create(SurroundingRectangle(b1d, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): percentage composition, ammonia ---
        self.next_band(2)
        b2t = Tex("Percentage composition: NH$_3$").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = MathTex(r"M = 14 + 3 \times 1 = 17 \text{ g/mol}").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2a))
        self.wait(2.5)
        b2b = MathTex(r"\text{N: } \frac{14}{17} \times 100 = 82{,}4\%").scale(1.0).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2b))
        self.wait(2.5)
        b2c = MathTex(r"\text{H: } \frac{3}{17} \times 100 = 17{,}6\%").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2c))
        self.wait(2)
        b2d = MathTex(r"82{,}4 + 17{,}6 = 100 \; \checkmark").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2d))
        self.play(Create(SurroundingRectangle(b2d, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): methane and subscript discipline ---
        self.next_band(3)
        b3t = Tex("CH$_4$ and subscript discipline").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = MathTex(r"M = 12 + 4 = 16 \text{ g/mol}").scale(1.0).shift(band_shift(3) + UP * 1.0)
        self.play(Write(b3a))
        self.wait(2)
        b3b = MathTex(r"\text{C: } \frac{12}{16} = 75\%; \quad \text{H: } \frac{4}{16} = 25\%").scale(1.0).shift(band_shift(3) + UP * 0.0)
        self.play(Write(b3b))
        self.wait(2.5)
        b3c = Tex("The four hydrogens contribute as a team of 4 g").scale(0.95).shift(band_shift(3) + DOWN * 1.0)
        self.play(Write(b3c))
        self.wait(2)
        b3d = Tex("Percentages are measurable — burn, weigh, recover").scale(0.95).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3d))
        self.wait(3)

        # --- Band 4 (subtopic_3): empirical formula, steps 1-2 ---
        self.next_band(4)
        b4t = Tex("Empirical formula: steps 1 and 2").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        b4a = Tex("Assume 100 g: 52,2 g C; 13,0 g H; 34,8 g O").scale(0.95).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4a))
        self.wait(2.5)
        b4b = MathTex(r"\text{C: } \frac{52{,}2}{12} = 4{,}35 \text{ mol}").scale(0.95).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4b))
        self.wait(2)
        b4c = MathTex(r"\text{H: } \frac{13{,}0}{1} = 13{,}0 \text{ mol}").scale(0.95).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4c))
        self.wait(2)
        b4d = MathTex(r"\text{O: } \frac{34{,}8}{16} = 2{,}175 \text{ mol}").scale(0.95).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4d))
        self.wait(3)

        # --- Band 5 (subtopic_3): steps 3-4 + the multiply-up rule ---
        self.next_band(5)
        b5t = Tex("Steps 3 and 4: divide by the smallest").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = MathTex(r"\frac{4{,}35}{2{,}175} = 2; \; \frac{13{,}0}{2{,}175} \approx 6; \; \frac{2{,}175}{2{,}175} = 1").scale(0.95).shift(band_shift(5) + UP * 1.0)
        self.play(Write(b5a))
        self.wait(2.5)
        b5b = MathTex(r"\Rightarrow \; \text{C}_2\text{H}_6\text{O}").scale(1.2).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5b))
        self.play(Create(SurroundingRectangle(b5b, color=GREEN)))
        self.wait(2.5)
        b5c = Tex("Ratio holds a 1,5? Multiply everything by 2").scale(0.95).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5c))
        self.wait(2)
        b5d = Tex("Rounding 1,5 away invents a different compound").scale(0.95).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5d))
        self.play(Create(strike(b5d)))
        self.wait(3)

        # --- Band 6 (subtopic_4): water of crystallisation ---
        self.next_band(6)
        b6t = Tex("Water of crystallisation: Na$_2$CO$_3\\cdot$10H$_2$O").scale(1.0).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = MathTex(r"M(\text{Na}_2\text{CO}_3) = 106; \; 10\text{H}_2\text{O} = 180").scale(0.95).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6a))
        self.wait(2.5)
        b6b = MathTex(r"M_{\text{total}} = 286 \text{ g/mol}").scale(1.0).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6b))
        self.wait(2)
        b6c = MathTex(r"\text{Water: } \frac{180}{286} \times 100 = 62{,}9\%").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6c))
        self.play(Create(SurroundingRectangle(b6c, color=GREEN)))
        self.wait(2.5)
        b6d = Tex("Nearly two-thirds of a `dry' crystal is water").scale(0.95).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6d))
        self.wait(3)

        # --- Band 7 (subtopic_4): the four traps ---
        self.next_band(7)
        b7t = Tex("The four traps").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex("1. Volume left in cm$^3$ — thousandfold error").scale(0.95).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7a))
        self.play(Create(strike(b7a)))
        self.wait(2)
        b7b = Tex("2. Mass ratios treated as atom ratios").scale(0.95).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7b))
        self.wait(2)
        b7c = Tex("3. Rounding a 1,5 instead of doubling").scale(0.95).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7c))
        self.wait(2)
        b7d = Tex("4. Subscripts skipped in molar masses").scale(0.95).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7d))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): how strong is the cooldrink ---
        self.next_band(8)
        b8t = Tex("How strong is the cooldrink").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("Strong: crowded jug. Weak: same packs, bigger jug.").scale(0.95).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8a))
        self.wait(2.5)
        b8b = MathTex(r"n = \frac{10{,}6}{106} = 0{,}1; \; V = 0{,}2 \text{ dm}^3").scale(0.95).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8b))
        self.wait(2.5)
        b8c = MathTex(r"c = \frac{0{,}1}{0{,}2} = 0{,}5 \text{ mol/dm}^3").scale(1.05).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8c))
        self.play(Create(SurroundingRectangle(b8c, color=GREEN)))
        self.wait(2.5)
        b8d = Tex("Crowding, not totals — volume under the line").scale(0.95).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8d))
        self.wait(3)

        # --- Band 9 (subtopic_6): reading the recipe backwards ---
        self.next_band(9)
        b9t = Tex("Reading the recipe backwards").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Pretend 100 g: label percentages become masses").scale(0.95).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9a))
        self.wait(2.5)
        b9b = Tex("Weigh each ingredient in MOLES: 4,35; 13,0; 2,175").scale(0.95).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = Tex("Divide by the smallest: 2 : 6 : 1").scale(1.0).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9c))
        self.wait(2)
        b9d = MathTex(r"\text{C}_2\text{H}_6\text{O}").scale(1.2).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9d))
        self.play(Create(SurroundingRectangle(b9d, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the water hiding in dry crystals ---
        self.next_band(10)
        b10t = Tex("The water hiding in dry crystals").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("Washing soda: ten waters escort every Na$_2$CO$_3$").scale(0.95).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10a))
        self.wait(2.5)
        b10b = MathTex(r"\frac{180}{286} \times 100 = 62{,}9\%").scale(1.05).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10b))
        self.play(Create(SurroundingRectangle(b10b, color=GREEN)))
        self.wait(2.5)
        b10c = Tex("Warm air: crystals crumble, balance drops").scale(0.95).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10c))
        self.wait(2)
        b10d = Tex("Formulas predict; scales confirm").scale(1.0).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10d))
        self.wait(4)
