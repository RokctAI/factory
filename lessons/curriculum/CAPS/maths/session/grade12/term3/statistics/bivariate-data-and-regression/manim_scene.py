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

# Band-layout whiteboard scene: sequential vertical bands, one per teaching
# beat, camera moves down between bands, add-only lifecycle. Exporter-safe
# mobjects only (Tex/MathTex/Line/Arrow/Dot/Rectangle) — the scatterplot is
# built manually from two Arrows, Dots and a Line, never Axes. Covers all
# seven subtopics of the duo (Part 1 — Expert: 1-4; Part 2 — Simplifier:
# 5-7); band time apportioned to subtopics.json
# (230/260/240/230/190/210/230 of 1590 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BivariateDataRegressionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): bivariate data — pairs, kept attached
        title = Tex("Bivariate Data and Regression").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex(r"Two measurements per individual, kept PAIRED").scale(1.05).shift(UP * 0.9)
        self.play(Write(s0_l1))
        self.wait(2)
        s0_l2 = MathTex(r"\text{Hours: } 1,\;2,\;3,\;4,\;5,\;6").scale(1.05).shift(DOWN * 0.1)
        s0_l3 = MathTex(r"\text{Marks: } 50,\;56,\;60,\;64,\;68,\;74").scale(1.05).shift(DOWN * 1.0)
        self.play(Write(s0_l2))
        self.play(Write(s0_l3))
        self.wait(2.5)
        s0_l4 = Tex(r"Explanatory across, response up — scramble a column").scale(0.95).shift(DOWN * 2.0)
        s0_l5 = Tex(r"and the information dies").scale(0.95).shift(DOWN * 2.8)
        self.play(Write(s0_l4))
        self.play(Write(s0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): the scatterplot, built dot by dot
        self.next_band(1)
        b1_title = Tex("The scatterplot: one dot per learner").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        orig = band_shift(1) + DOWN * 1.8 + LEFT * 2.8
        x_axis = Arrow(orig + LEFT * 0.2, orig + RIGHT * 5.4, buff=0, stroke_width=3)
        y_axis = Arrow(orig + DOWN * 0.2, orig + UP * 3.4, buff=0, stroke_width=3)
        x_lab = Tex("hours").scale(0.8).move_to(orig + RIGHT * 5.0 + DOWN * 0.4)
        y_lab = Tex("mark").scale(0.8).move_to(orig + UP * 3.2 + LEFT * 0.7)
        self.play(Create(x_axis), Create(y_axis))
        self.play(Write(x_lab), Write(y_lab))
        self.wait(1.5)
        data = [(1, 50), (2, 56), (3, 60), (4, 64), (5, 68), (6, 74)]

        def plot(h, m):
            return orig + RIGHT * (h * 0.78) + UP * ((m - 46) * 0.105)

        dots = [Dot(plot(h, m), radius=0.07, color=YELLOW) for h, m in data]
        self.play(Create(dots[0]), Create(dots[1]), Create(dots[2]))
        self.play(Create(dots[3]), Create(dots[4]), Create(dots[5]))
        self.wait(2)
        b1_l1 = Tex(r"Direction: uphill. Form: straight. Strength: tight").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l1))
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the least squares regression line
        self.next_band(2)
        b2_title = Tex("The least squares regression line").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Residual} = y_{\text{actual}} - y_{\text{predicted}}").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex(r"Choose the line minimising the SUM OF SQUARES").scale(1.0).shift(band_shift(2) + UP * 0.2)
        b2_l3 = Tex(r"Calculator, two-variable statistics mode:").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = MathTex(r"a = 46, \quad b = 4{,}57").scale(1.1).shift(band_shift(2) + DOWN * 1.6)
        b2_l5 = MathTex(r"\hat{y} = 46 + 4{,}57\,x").scale(1.2).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2.5)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): interpretation + the mean point
        self.next_band(3)
        b3_title = Tex("The marks are in the interpretation").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"$b = 4{,}57$: each extra hour adds about 4,57 points").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex(r"$a = 46$: zero hours predicts 46\% (sensible here)").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"\text{The line always passes through } (\bar{x};\,\bar{y})").scale(1.05).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = MathTex(r"\bar{x} = 3{,}5, \;\; \bar{y} = 62").scale(1.05).shift(band_shift(3) + DOWN * 1.7)
        b3_l5 = MathTex(r"46 + 4{,}57 \times 3{,}5 = 62 \;\; \checkmark").scale(1.05).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the correlation coefficient r
        self.next_band(4)
        b4_title = Tex(r"The correlation coefficient $r$").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"-1 \leq r \leq 1").scale(1.15).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex(r"Sign copies direction; size measures tightness").scale(1.0).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"0{,}9+ \text{ very strong}; \;\; 0{,}7\text{–}0{,}9 \text{ strong}").scale(0.9).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"0{,}5\text{–}0{,}7 \text{ moderate}; \;\; 0{,}3\text{–}0{,}5 \text{ weak}").scale(0.9).shift(band_shift(4) + DOWN * 1.5)
        b4_l4b = MathTex(r"\text{below } 0{,}3: \text{ very weak to none}").scale(0.9).shift(band_shift(4) + DOWN * 2.3)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l4b))
        self.wait(2)
        b4_l5 = MathTex(r"r = 0{,}997: \text{ very strong positive linear}").scale(0.9).shift(band_shift(4) + DOWN * 3.05)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the three cautions
        self.next_band(5)
        b5_title = Tex(r"Three cautions guard $r$").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"1. $r$ sees LINEAR association only — plot first").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex(r"2. $r$ has no units; changing units leaves it untouched").scale(1.0).shift(band_shift(5) + UP * 0.2)
        b5_l3 = Tex(r"3. Correlation is not causation").scale(1.1).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2.5)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=YELLOW)))
        self.wait(2.5)
        b5_l4 = Tex(r"Ice cream sales and drownings: both driven by summer").scale(0.95).shift(band_shift(5) + DOWN * 1.9)
        b5_l5 = Tex(r"Comment on association; never claim proof of cause").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): prediction — inside and outside the fence
        self.next_band(6)
        b6_title = Tex("Prediction: interpolation vs extrapolation").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"x = 4{,}5: \;\; \hat{y} = 46 + 4{,}57 \times 4{,}5 = 66{,}57").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex(r"About 67\% — interpolation, inside 1 to 6 hours").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_wrong = MathTex(r"x = 15: \;\; \hat{y} = 46 + 4{,}57 \times 15 \approx 114{,}55\%").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_wrong))
        self.play(Create(strike(b6_wrong)))
        self.wait(2)
        b6_l3 = Tex(r"Extrapolation: unreliable — and no mark exceeds 100").scale(0.95).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l3))
        self.wait(3)

        # --- Band 7 (subtopic_4): the full examination routine
        self.next_band(7)
        b7_title = Tex("The examination routine, in order").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"1. Inspect the scatterplot: direction, form, strength").scale(0.95).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex(r"2. If linear, fit $\hat{y} = a + bx$ by calculator").scale(0.95).shift(band_shift(7) + UP * 0.3)
        b7_l3 = Tex(r"3. Interpret $b$ in context; quote $r$ with words").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex(r"4. Predict only inside the data range").scale(0.95).shift(band_shift(7) + DOWN * 1.3)
        b7_l5 = Tex(r"5. Never convert association into cause").scale(0.95).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(2)
        self.play(Write(b7_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): two numbers per person
        self.next_band(8)
        b8_title = Tex("Two numbers per person").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Pairs stay attached — the attachment carries the story").scale(0.95).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex(r"A photograph of six people, not a journey: never join dots").scale(0.9).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"Driver across, outcome up").scale(1.1).shift(band_shift(8) + DOWN * 0.8)
        b8_l4 = Tex(r"Three judgements: lean, lane, tightness").scale(1.05).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(3.5)

        # --- Band 9 (subtopic_6): the line that owes the least
        self.next_band(9)
        b9_title = Tex("The broomstick that owes the least").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Each dot files a complaint: its vertical gap").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex(r"Least squares: smallest total of SQUARED complaints").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"\hat{y} = 46 + 4{,}57\,x \;\; \text{($b$ = the price of an hour)}").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = MathTex(r"\text{Balances at the average point: } 46 + 4{,}57 \times 3{,}5 = 62").scale(0.95).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l4))
        self.wait(3.5)

        # --- Band 10 (subtopic_7): how tight is the queue
        self.next_band(10)
        b10_title = Tex("How tight is the queue").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"$r$: sign is the lean, size is the hug").scale(1.05).shift(band_shift(10) + UP * 1.1)
        b10_l2 = MathTex(r"r = 0{,}997: \text{ almost single file, uphill}").scale(1.05).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = Tex(r"Warning labels: straight lanes only; tightness is not blame").scale(0.9).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex(r"Inside the fence: 4,5 h $\to$ about 67\%").scale(1.0).shift(band_shift(10) + DOWN * 1.7)
        b10_l5 = Tex(r"Jumping the fence: 15 h $\to$ 114\% — flag it").scale(1.0).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10_l4))
        self.wait(2)
        self.play(Write(b10_l5))
        self.wait(4)
