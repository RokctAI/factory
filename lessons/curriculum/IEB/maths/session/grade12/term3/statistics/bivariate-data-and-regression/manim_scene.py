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

# Band-layout whiteboard scene: sequential vertical bands, one per teaching
# beat, camera moves down between bands, add-only lifecycle. Exporter-safe
# mobjects only (Tex/MathTex/Line/Rectangle/Dot); every working line is a
# single-string MathTex revealed with Write. Covers all seven subtopics of
# the duo (Part 1 — Expert: 1-4; Part 2 — Simplifier:
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
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): bivariate data — pairs, kept attached
        title = Tex("Bivariate data: two numbers per person").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = MathTex(r"(2; 49)\;(3; 52)\;(4; 55)\;(5; 61)\;(6; 63)\;(7; 68)").scale(0.95).shift(UP * 0.9)
        self.play(Write(s0_l1))
        self.wait(2.5)
        s0_l2 = Tex(r"Practice papers paired with the mark achieved").scale(1.0).shift(UP * 0.0)
        self.play(Write(s0_l2))
        self.wait(2)
        s0_l3 = Tex(r"The pairing IS the information — never scramble a column").scale(0.95).shift(DOWN * 1.0)
        self.play(Write(s0_l3))
        self.play(Create(SurroundingRectangle(s0_l3, color=YELLOW)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the scatterplot, built dot by dot
        self.next_band(1)
        b1_title = Tex("The scatterplot").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        ax_o = band_shift(1) + DOWN * 1.6 + LEFT * 3.0
        x_axis = Line(ax_o, ax_o + RIGHT * 5.6, stroke_width=3)
        y_axis = Line(ax_o, ax_o + UP * 3.4, stroke_width=3)
        self.play(Create(x_axis), Create(y_axis))
        xs = [2, 3, 4, 5, 6, 7]
        ys = [49, 52, 55, 61, 63, 68]
        dots = [Dot(ax_o + RIGHT * (0.7 * x) + UP * ((y - 45) * 0.12), radius=0.07, color=BLUE)
                for x, y in zip(xs, ys)]
        self.play(Create(dots[0]), Create(dots[1]), Create(dots[2]),
                  Create(dots[3]), Create(dots[4]), Create(dots[5]))
        self.wait(2)
        b1_l1 = Tex(r"Explanatory across, response up, dots never joined").scale(0.9).shift(band_shift(1) + UP * 1.4)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = Tex(r"Direction, form, strength: positive, linear, strong").scale(0.9).shift(band_shift(1) + UP * 0.6)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the least squares regression line
        self.next_band(2)
        b2_title = Tex("The least squares regression line").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"Residual = actual $y$ $-$ predicted $y$ (vertical miss)").scale(0.95).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = Tex(r"Minimise the SUM of SQUARED residuals").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=YELLOW)))
        self.wait(2.5)
        b2_l3 = MathTex(r"\hat{y} = 40{,}77 + 3{,}83x").scale(1.2).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex(r"From the calculator: statistics mode, two-variable").scale(0.9).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): interpretation + the mean point
        self.next_band(3)
        b3_title = Tex("Interpretation carries the marks").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"$b = 3{,}83$: each paper adds about 3,83 percentage points").scale(0.9).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = Tex(r"$a = 40{,}77$: predicted mark for zero papers").scale(0.9).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"\text{always through } (\bar{x}; \bar{y}) = (4{,}5;\; 58)").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"40{,}77 + 3{,}83 \times 4{,}5 = 58 \;\checkmark").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the correlation coefficient r
        self.next_band(4)
        b4_title = Tex("The correlation coefficient $r$").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"-1 \le r \le 1").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex(r"Sign: direction of the lane. Size: tightness of the dots").scale(0.9).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"r = 0{,}99 \text{: very strong, positive, linear}").scale(1.0).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex(r"Bands: 0,9 very strong; 0,7 strong; 0,5 moderate; 0,3 weak").scale(0.85).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): the three cautions
        self.next_band(5)
        b5_title = Tex("Three cautions on $r$").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"1. $r$ sees LINEAR association only — plot first").scale(0.95).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex(r"2. $r$ has no units and ignores unit changes").scale(0.95).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex(r"3. Correlation is NOT causation").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=RED)))
        self.wait(2.5)
        b5_l4 = Tex(r"Shoe size and reading level: age drives both").scale(0.95).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): prediction — inside and outside the fence
        self.next_band(6)
        b6_title = Tex("Prediction: inside and outside the fence").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"x = 5{,}5:\; \hat{y} = 40{,}77 + 3{,}83 \times 5{,}5 \approx 62").scale(0.95).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2.5)
        b6_l2 = Tex(r"Interpolation — inside the observed range 2 to 7").scale(0.9).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_wrong = MathTex(r"x = 20:\; \hat{y} \approx 117\% \;?").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_wrong))
        self.play(Create(strike(b6_wrong)))
        self.wait(2)
        b6_l3 = Tex(r"Extrapolation — flag as unreliable, reject the impossible").scale(0.9).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l3))
        self.wait(3)

        # --- Band 7 (subtopic_4): the full working routine
        self.next_band(7)
        b7_title = Tex("The full routine, in order").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"Plot — judge direction, form, strength").scale(0.95).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex(r"Fit $\hat{y} = a + bx$; interpret $b$ in context").scale(0.95).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex(r"Quote $r$ with direction and strength in words").scale(0.95).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex(r"Predict inside the range; association, never cause").scale(0.95).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): two numbers per person
        self.next_band(8)
        b8_title = Tex("Two numbers per person").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Pairs pinned on a board: papers across, marks up").scale(0.95).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex(r"One dot per friend — a photograph, not a journey").scale(0.95).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"Lean, lane, tightness: uphill, straight, tight").scale(0.95).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex(r"7 papers with 35\%: an outlier with its own story").scale(0.95).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): the line that owes the least
        self.next_band(9)
        b9_title = Tex("The line that owes the least").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Every dot bills its vertical gap — squared").scale(0.95).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"\hat{y} = 40{,}77 + 3{,}83x").scale(1.1).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = Tex(r"$b$: the price of a paper, paid in marks").scale(0.95).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = MathTex(r"\text{balances at } (4{,}5;\; 58) \text{ — the see-saw pivot}").scale(0.95).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l4))
        self.wait(3)

        # --- Band 10 (subtopic_7): how tight is the queue
        self.next_band(10)
        b10_title = Tex("How tight is the queue").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"r = 0{,}99 \text{: nearly single file, uphill}").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.play(Create(SurroundingRectangle(b10_l1, color=GREEN)))
        self.wait(2.5)
        b10_l2 = Tex(r"Photo before score; straight lanes only").scale(0.95).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex(r"Tidiness is not blame: association, never cause").scale(0.95).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex(r"Predict inside the fence; flag every jump").scale(1.0).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=YELLOW)))
        self.wait(4)
