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

# Band-layout whiteboard scene for "Population Indicators and Population
# Pyramids" (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier 5-7).
# Exporter-safe primitives only: every pyramid is hand-built from paired
# Rectangles either side of a centre Line, revealed row by row in sync with
# the script. Add-only lifecycle; camera moves down band by band. Band time
# apportioned to subtopics.json (230/235/245/240/190/180/175 of 1495 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


def pyramid_row(cx, cy, w_left, w_right, h=0.4):
    """One age cohort: male bar to the left of centre, female bar to the
    right, built only from Rectangles."""
    left = Rectangle(width=w_left, height=h, color=BLUE).move_to(
        np.array([cx - w_left / 2 - 0.03, cy, 0]))
    right = Rectangle(width=w_right, height=h, color=RED).move_to(
        np.array([cx + w_right / 2 + 0.03, cy, 0]))
    return VGroup(left, right)


class PopulationPyramidsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the vital statistics ---
        title = Tex("Population Indicators and Pyramids").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l1 = Tex("Rates per thousand people per year").scale(1.05).shift(UP * 1.1)
        self.play(Write(l1))
        self.wait(2)
        l2 = Tex("SA birth rate $\\approx 19$ per thousand").scale(1.05).shift(UP * 0.2)
        l3 = Tex("SA death rate $\\approx 9$ per thousand").scale(1.05).shift(DOWN * 0.7)
        self.play(Write(l2))
        self.wait(1.5)
        self.play(Write(l3))
        self.wait(2)
        l4 = MathTex(r"\text{NI} = 19 - 9 = 10 \text{ per thousand} = 1\%").scale(1.05).shift(DOWN * 1.7)
        self.play(Write(l4))
        self.play(Create(SurroundingRectangle(l4, color=GREEN)))
        self.wait(2)
        l5 = Tex("Natural = migration excluded").scale(1.0).shift(DOWN * 2.7)
        self.play(Write(l5))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the death-rate trap and the drivers ---
        self.next_band(1)
        b1_title = Tex("The age-structure trap").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_w = Tex("High death rate = bad hospitals?").scale(1.05).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_w))
        self.play(Create(strike(b1_w)))
        self.wait(2)
        b1_l1 = Tex("Germany $>11$ per thousand, Kenya $<8$:").scale(1.0).shift(band_shift(1) + UP * 0.3)
        b1_l2 = Tex("Germany is simply older").scale(1.05).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("Births fall with education of women,").scale(0.95).shift(band_shift(1) + DOWN * 1.6)
        b1_l4 = Tex("child survival, urban life").scale(0.95).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): fertility and replacement ---
        self.next_band(2)
        b2_title = Tex("Total fertility rate").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Children per woman in a lifetime —").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("the best predictor of future growth").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"\text{Replacement level} = 2{,}1").scale(1.2).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex("Niger $>6$; Japan and Italy $\\approx 1{,}3$").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        b2_l5 = Tex("SA: about 6 in the 1960s $\\to$ 2,3 today").scale(1.0).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l4))
        self.wait(2)
        self.play(Write(b2_l5))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): infant mortality and life expectancy ---
        self.next_band(3)
        b3_title = Tex("Infant mortality and life expectancy").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Infant mortality: deaths before age 1").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("per 1000 births — most sensitive").scale(1.0).shift(band_shift(3) + UP * 0.4)
        b3_l3 = Tex("measure of development. SA $\\approx 25$").scale(1.0).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("SA life expectancy: 53 in early 2000s,").scale(1.0).shift(band_shift(3) + DOWN * 1.3)
        b3_l5 = Tex("$\\approx 65$ now — the ARV rollout").scale(1.0).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(2)
        b3_l6 = Tex("Never judge a country on one indicator").scale(1.0).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l6))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): building the pyramid ---
        self.next_band(4)
        b4_title = Tex("Reading a population pyramid").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        cx = -1.5
        base_y = float(band_shift(4)[1]) - 2.2
        axis = Line(np.array([cx, base_y - 0.3, 0]), np.array([cx, base_y + 3.2, 0]), stroke_width=4)
        self.play(Create(axis))
        m_lab = Tex("males").scale(0.85).shift(band_shift(4) + LEFT * 3.6 + UP * 1.6)
        f_lab = Tex("females").scale(0.85).shift(band_shift(4) + RIGHT * 0.8 + UP * 1.6)
        self.play(Write(m_lab), Write(f_lab))
        widths = [2.6, 2.3, 2.0, 1.6, 1.1, 0.6]
        for i, w in enumerate(widths):
            row = pyramid_row(cx, base_y + 0.25 + i * 0.5, w, w * 1.02, h=0.42)
            self.play(Create(row), run_time=0.7)
        y_lab0 = Tex("0--4").scale(0.7).shift(np.array([cx + 3.0, base_y + 0.25, 0]))
        y_lab1 = Tex("oldest").scale(0.7).shift(np.array([cx + 3.0, base_y + 2.75, 0]))
        self.play(Write(y_lab0), Write(y_lab1))
        self.wait(2)
        note1 = Tex("5-year cohorts,").scale(0.85).shift(band_shift(4) + RIGHT * 4.3 + UP * 0.6)
        note2 = Tex("youngest at the base;").scale(0.85).shift(band_shift(4) + RIGHT * 4.3 + DOWN * 0.1)
        note3 = Tex("bar length = people").scale(0.85).shift(band_shift(4) + RIGHT * 4.3 + DOWN * 0.8)
        self.play(Write(note1))
        self.play(Write(note2))
        self.play(Write(note3))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): reading habits and dependency ratio ---
        self.next_band(5)
        b5_title = Tex("Three reading habits").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        h1 = Tex("1. BASE: wide = high births; pinched = falling").scale(0.95).shift(band_shift(5) + UP * 1.2)
        h2 = Tex("2. SLOPE: sharp taper = high mortality").scale(0.95).shift(band_shift(5) + UP * 0.4)
        h3 = Tex("3. IRREGULARITIES: notch = war or epidemic,").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        h3b = Tex("bulge = baby boom or immigration").scale(0.95).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(h1))
        self.wait(2)
        self.play(Write(h2))
        self.wait(2)
        self.play(Write(h3))
        self.play(Write(h3b))
        self.wait(2)
        dr = MathTex(r"\text{Dep. ratio} = \frac{(0\text{--}14) + (65+)}{15\text{--}64} \times 100").scale(0.94).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(dr))
        self.play(Create(SurroundingRectangle(dr, color=GREEN)))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the three classic shapes ---
        self.next_band(6)
        b6_title = Tex("Three classic shapes").scale(1.2).shift(band_shift(6) + UP * 2.5)
        self.play(Write(b6_title))
        self.wait(1.5)
        shapes = [
            (-4.2, [1.7, 1.4, 1.1, 0.8, 0.5, 0.25], "expansive"),
            (0.0, [1.2, 1.2, 1.15, 1.15, 1.1, 0.6], "stationary"),
            (4.2, [0.7, 1.0, 1.3, 1.25, 1.0, 0.6], "constrictive"),
        ]
        base_y6 = float(band_shift(6)[1]) - 1.4
        for cx6, ws, name in shapes:
            rows = VGroup(*[
                Rectangle(width=w, height=0.38).move_to(
                    np.array([cx6, base_y6 + 0.2 + i * 0.45, 0]))
                for i, w in enumerate(ws)])
            lab = Tex(name).scale(0.8).shift(np.array([cx6, base_y6 - 0.55, 0]))
            self.play(Create(rows), Write(lab))
            self.wait(1.5)
        e1 = Tex("Expansive: Niger, DRC — rapid growth").scale(0.9).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(e1))
        self.wait(1.5)
        e2 = Tex("Stationary: Sweden. Constrictive: Japan").scale(0.9).shift(band_shift(6) + DOWN * 3.2)
        self.play(Write(e2))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): South Africa's transitional pyramid ---
        self.next_band(7)
        b7_title = Tex("South Africa: transitional").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Base fairly wide but no longer widening").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("Bulge through the 20s and 30s").scale(1.0).shift(band_shift(7) + UP * 0.4)
        b7_l3 = Tex("Taper carries the Aids-era scar").scale(1.0).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex("Females outnumber males at the top").scale(1.0).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("Big working-age share: demographic dividend").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the report card ---
        self.next_band(8)
        b8_title = Tex("A country's report card").scale(1.15).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Births and deaths per thousand;").scale(1.0).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex("SA: $19 - 9 = 10$ per thousand $= 1\\%$").scale(1.0).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Remember 2,1: above it grow, below it shrink").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("Infant mortality: the harshest, most honest mark").scale(0.95).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Life expectancy is an average —").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        b8_l6 = Tex("baby deaths drag it down hard").scale(0.95).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.wait(2.5)

        # --- Band 9 (subtopic_6): the family photograph ---
        self.next_band(9)
        b9_title = Tex("The pyramid as a family photograph").scale(1.1).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Everyone in rows by AGE: babies in front,").scale(0.95).shift(band_shift(9) + UP * 1.3)
        b9_l2 = Tex("great-grandparents at the back;").scale(0.95).shift(band_shift(9) + UP * 0.5)
        b9_l3 = Tex("men left of centre, women right").scale(0.95).shift(band_shift(9) + DOWN * 0.3)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("A short row = a bite from the crowd:").scale(0.95).shift(band_shift(9) + DOWN * 1.2)
        b9_l5 = Tex("war, epidemic or famine in those years").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(2.5)
        b9_l6 = Tex("Three blocks: young, workers, retired —").scale(0.95).shift(band_shift(9) + DOWN * 2.8)
        b9_l7 = Tex("how many riders per hundred workers?").scale(0.95).shift(band_shift(9) + DOWN * 3.5)
        self.play(Write(b9_l6))
        self.play(Write(b9_l7))
        self.wait(2.5)

        # --- Band 10 (subtopic_7): stacks of bricks ---
        self.next_band(10)
        b10_title = Tex("Wide base, narrow base").scale(1.15).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Triangle: babies everywhere, fast growth —").scale(0.95).shift(band_shift(10) + UP * 1.3)
        b10_l2 = Tex("and momentum keeps it rolling for decades").scale(0.95).shift(band_shift(10) + UP * 0.5)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Tower: steady size, long lives (Sweden)").scale(0.95).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex("Pinched base: fewer children than adults —").scale(0.95).shift(band_shift(10) + DOWN * 1.2)
        b10_l5 = Tex("Japan's future: many pensioners, few workers").scale(0.95).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(2.5)
        b10_l6 = Tex("SA: between the shapes — a working-age bulge,").scale(0.9).shift(band_shift(10) + DOWN * 2.8)
        b10_l7 = Tex("a once-off chance if the bulge finds jobs").scale(0.9).shift(band_shift(10) + DOWN * 3.5)
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.play(Create(SurroundingRectangle(b10_l7, color=GREEN)))
        self.wait(3)
