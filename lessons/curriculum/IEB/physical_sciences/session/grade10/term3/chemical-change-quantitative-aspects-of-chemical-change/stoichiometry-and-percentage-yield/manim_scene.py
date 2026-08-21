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

# Band-layout whiteboard scene for stoichiometry-and-percentage-yield
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe mobjects only; add-only lifecycle; the 42 g MgCO3 problem
# worked line by line with the script's exact numbers and units.
# Time apportioned to subtopics.json (225/235/230/260/175/180/175 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class StoichiometryPercentageYieldSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the equation is a mole recipe ---
        title = Tex("Stoichiometry and Percentage Yield").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        a1 = MathTex(r"\text{MgCO}_3 \rightarrow \text{MgO} + \text{CO}_2").scale(1.15).shift(UP * 0.9)
        self.play(Write(a1))
        self.wait(2)
        a2 = Tex("Balanced: Mg 1:1, C 1:1, O 3:3 $\\checkmark$").scale(1.0).shift(UP * 0.0)
        self.play(Write(a2))
        self.wait(2)
        a3 = Tex("Coefficients are a MOLE ratio").scale(1.05).shift(DOWN * 0.9)
        self.play(Write(a3))
        self.play(Create(SurroundingRectangle(a3, color=GREEN)))
        self.wait(2)
        a4 = Tex("Never a mass ratio: moles weigh differently").scale(0.95).shift(DOWN * 1.9)
        self.play(Write(a4))
        self.wait(3)

        # --- Band 1 (subtopic_1): the three-leg journey ---
        self.next_band(1)
        b1_t = Tex("The three-leg journey").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_1 = MathTex(r"\text{Leg 1: } n = \frac{m}{M} \; \text{(mass to moles)}").scale(1.05).shift(band_shift(1) + UP * 1.0)
        self.play(Write(b1_1))
        self.wait(2)
        b1_2 = Tex("Leg 2: cross with the coefficient ratio").scale(1.05).shift(band_shift(1) + UP * 0.0)
        self.play(Write(b1_2))
        self.wait(2)
        b1_3 = MathTex(r"\text{Leg 3: } m = n \times M \; \text{(moles back out)}").scale(1.05).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(b1_3))
        self.wait(2)
        b1_4 = Tex("Grams never jump the equation directly:").scale(1.0).shift(band_shift(1) + DOWN * 2.0)
        b1_5 = Tex("they become moles at the border").scale(1.0).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_4))
        self.play(Write(b1_5))
        self.wait(3)

        # --- Band 2 (subtopic_2): legs one and two ---
        self.next_band(2)
        b2_t = Tex("42 g in: legs one and two").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_1 = MathTex(r"M(\text{MgCO}_3) = 24 + 12 + 48 = 84").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_1))
        self.wait(2.5)
        b2_2 = MathTex(r"n = \frac{m}{M} = \frac{42}{84} = 0{,}5\ \text{mol}").scale(1.05).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_2))
        self.wait(2.5)
        b2_3 = MathTex(r"\text{MgCO}_3 : \text{MgO} = 1 : 1").scale(1.05).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_3))
        self.wait(2)
        b2_4 = MathTex(r"\Rightarrow 0{,}5\ \text{mol MgO}").scale(1.05).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2_4))
        self.play(Create(SurroundingRectangle(b2_4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): leg three + conservation check ---
        self.next_band(3)
        b3_t = Tex("Leg three, and the free check").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_1 = MathTex(r"M(\text{MgO}) = 24 + 16 = 40").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_1))
        self.wait(2)
        b3_2 = MathTex(r"m = n M = 0{,}5 \times 40 = 20\ \text{g}").scale(1.1).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_2))
        self.play(Create(SurroundingRectangle(b3_2, color=GREEN)))
        self.wait(2.5)
        b3_3 = Tex("20 g is the THEORETICAL yield (a ceiling)").scale(0.95).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_3))
        self.wait(2)
        b3_4 = MathTex(r"\text{CO}_2: 0{,}5 \times 44 = 22\ \text{g escapes}").scale(1.0).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_4))
        self.wait(2)
        b3_5 = MathTex(r"20 + 22 = 42\ \text{g: mass conserved} \; \checkmark").scale(1.0).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_5))
        self.wait(3)

        # --- Band 4 (subtopic_3): percentage yield ---
        self.next_band(4)
        b4_t = Tex("The learner collects 17 g").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_1 = MathTex(r"\%\ \text{yield} = \frac{\text{actual}}{\text{theoretical}} \times 100").scale(1.05).shift(band_shift(4) + UP * 1.0)
        self.play(Write(b4_1))
        self.wait(2.5)
        b4_2 = MathTex(r"= \frac{17}{20} \times 100 = 85\%").scale(1.1).shift(band_shift(4) + DOWN * 0.1)
        self.play(Write(b4_2))
        self.play(Create(SurroundingRectangle(b4_2, color=GREEN)))
        self.wait(2.5)
        b4_3 = Tex("Falls short honestly: incomplete reaction,").scale(0.95).shift(band_shift(4) + DOWN * 1.2)
        b4_4 = Tex("transfer losses, side reactions").scale(0.95).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_3))
        self.wait(1.5)
        self.play(Write(b4_4))
        self.wait(2)
        b4_5 = Tex("Industry fights for every point: 1\\% = tonnes").scale(0.95).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_5))
        self.wait(3)

        # --- Band 5 (subtopic_3): the over-one-hundred alarm ---
        self.next_band(5)
        b5_t = Tex("The over-100\\% alarm").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_trap = Tex("Yield over 100\\% = overachieving!").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_trap))
        self.play(Create(strike(b5_trap)))
        self.wait(2)
        b5_1 = Tex("More than the atoms allow is impossible").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_1))
        self.wait(2)
        b5_2 = Tex("Diagnosis: wet product, contamination,").scale(1.0).shift(band_shift(5) + DOWN * 0.7)
        b5_3 = Tex("or faulty weighing").scale(1.0).shift(band_shift(5) + DOWN * 1.5)
        self.play(Write(b5_2))
        self.play(Write(b5_3))
        self.wait(2)
        b5_4 = Tex("85\\% credible; 40\\% = leaky technique").scale(1.0).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_4))
        self.wait(3)

        # --- Band 6 (subtopic_4): the five-step method ---
        self.next_band(6)
        b6_t = Tex("The full method, five steps").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_1 = Tex("1. Write and BALANCE the equation").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_2 = Tex("2. Given quantity to moles").scale(1.0).shift(band_shift(6) + UP * 0.3)
        b6_3 = Tex("3. Ratio: wanted over given coefficients").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        b6_4 = Tex("4. Convert to the units demanded").scale(1.0).shift(band_shift(6) + DOWN * 1.3)
        b6_5 = Tex("5. \\% yield if an actual mass is given").scale(1.0).shift(band_shift(6) + DOWN * 2.1)
        for m in (b6_1, b6_2, b6_3, b6_4, b6_5):
            self.play(Write(m))
            self.wait(1.6)
        b6_6 = Tex("Sense-check: yield below 100").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_6))
        self.wait(3)

        # --- Band 7 (subtopic_4): the classic traps ---
        self.next_band(7)
        b7_t = Tex("The classic traps").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_trap = Tex("1:1 in moles means 1 g gives 1 g").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_trap))
        self.play(Create(strike(b7_trap)))
        self.wait(2)
        b7_1 = MathTex(r"1:1 \text{ in moles} = 84 : 40 \text{ in grams}").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_1))
        self.play(Create(SurroundingRectangle(b7_1, color=GREEN)))
        self.wait(2.5)
        b7_2 = Tex(r"Subscripts: three O in MgCO$_3$ = 48, not 16").scale(0.95).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_2))
        self.wait(2)
        b7_3 = MathTex(r"\frac{20}{17} \times 100 = 118\% \; \text{(inverted!)}").scale(1.0).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_3))
        self.play(Create(strike(b7_3)))
        self.wait(2)
        b7_4 = Tex("Theoretical yield is a ceiling, not a promise").scale(0.95).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): a recipe promises in its own units ---
        self.next_band(8)
        b8_t = Tex("A recipe promises, in its own units").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_1 = Tex("One batch of dough = one tray of rolls").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_1))
        self.wait(2)
        b8_2 = Tex("Batches and trays — never kilograms").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_2))
        self.wait(2)
        b8_3 = Tex("Equation promises in MOLES (batches):").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        b8_4 = Tex("1 mol carbonate = 1 mol oxide").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_3))
        self.wait(2)
        self.play(Write(b8_4))
        self.wait(2)
        b8_5 = Tex("Molar mass translates at each door").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_5))
        self.play(Create(SurroundingRectangle(b8_5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): forty-two grams through the bakery ---
        self.next_band(9)
        b9_t = Tex("Forty-two grams through the bakery").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_1 = MathTex(r"\frac{42}{84} = 0{,}5\ \text{mol — half a batch}").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_1))
        self.wait(2.5)
        b9_2 = Tex("One tray per batch: 0,5 mol MgO").scale(1.0).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_2))
        self.wait(2)
        b9_3 = MathTex(r"0{,}5 \times 40 = 20\ \text{g at most}").scale(1.05).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_3))
        self.play(Create(SurroundingRectangle(b9_3, color=GREEN)))
        self.wait(2.5)
        b9_4 = MathTex(r"\text{Gas carried off: } 0{,}5 \times 44 = 22\ \text{g}").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_4))
        self.wait(2)
        b9_5 = MathTex(r"20 + 22 = 42 \; \checkmark \; \text{atoms change address}").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_5))
        self.wait(3)

        # --- Band 10 (subtopic_7): what reaches the shelf ---
        self.next_band(10)
        b10_t = Tex("What actually reaches the shelf").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_1 = Tex("Promised 20 g; the balance says 17 g").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_1))
        self.wait(2)
        b10_2 = MathTex(r"\frac{17}{20} \times 100 = 85\%").scale(1.1).shift(band_shift(10) + UP * 0.0)
        self.play(Write(b10_2))
        self.play(Create(SurroundingRectangle(b10_2, color=GREEN)))
        self.wait(2.5)
        b10_3 = Tex("Unfinished bake, rolls stuck to the pan,").scale(0.95).shift(band_shift(10) + DOWN * 1.0)
        b10_4 = Tex("dough pinched by side reactions").scale(0.95).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_3))
        self.wait(1.5)
        self.play(Write(b10_4))
        self.wait(2)
        b10_5 = Tex("Over 100\\%: contaminated tray, not a kind oven").scale(0.95).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_5))
        self.wait(4)
