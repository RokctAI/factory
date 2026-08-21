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
        title = Tex("Population Indicators").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        v1 = Tex("Rates per thousand per year:").scale(1.05).shift(UP * 1.1)
        v2 = Tex("fair comparison between countries").scale(1.0).shift(UP * 0.3)
        self.play(Write(v1))
        self.play(Write(v2))
        self.wait(2)
        v3 = Tex("SA births $\\approx$ 19; Mali $>$ 40; S. Korea $<$ 6").scale(0.95).shift(DOWN * 0.7)
        self.play(Write(v3))
        self.wait(2)
        v4 = MathTex(r"\text{NI} = 19 - 9 = 10 \text{ per thousand} = 1\%").scale(1.0).shift(DOWN * 1.7)
        self.play(Write(v4))
        self.play(Create(SurroundingRectangle(v4, color=GREEN)))
        self.wait(2)
        v5 = Tex("Natural: migration fenced out").scale(0.95).shift(DOWN * 2.7)
        self.play(Write(v5))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the death-rate trap and the drivers ---
        self.next_band(1)
        b1_title = Tex("The death-rate trap").scale(1.2).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        t1 = Tex("Italy $>$ 10 per thousand;").scale(1.0).shift(band_shift(1) + UP * 1.2)
        t2 = Tex("Uganda $<$ 6 per thousand").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(t1))
        self.play(Write(t2))
        self.wait(2)
        t3 = Tex("Worse hospitals in Italy?").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        self.play(Write(t3))
        self.play(Create(strike(t3)))
        self.wait(2)
        t4 = Tex("Age structure: Italy old, Uganda young").scale(1.0).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(t4))
        self.play(Create(SurroundingRectangle(t4, color=GREEN)))
        self.wait(2)
        t5 = Tex("Births fall with women's education;").scale(0.95).shift(band_shift(1) + DOWN * 2.3)
        t6 = Tex("deaths fall with water, vaccines, food").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(t5))
        self.play(Write(t6))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): fertility and replacement ---
        self.next_band(2)
        b2_title = Tex("Total fertility and 2,1").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        f1 = Tex("TFR: children per woman, lifetime average").scale(1.0).shift(band_shift(2) + UP * 1.2)
        self.play(Write(f1))
        self.wait(2)
        f2 = Tex("REPLACEMENT = 2,1").scale(1.15).shift(band_shift(2) + UP * 0.3)
        self.play(Write(f2))
        self.play(Create(SurroundingRectangle(f2, color=GREEN)))
        self.wait(2)
        f3 = Tex("Above it: eventual growth.").scale(1.0).shift(band_shift(2) + DOWN * 0.6)
        f4 = Tex("Below it: eventual shrinkage.").scale(1.0).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(f3))
        self.play(Write(f4))
        self.wait(2)
        f5 = Tex("Somalia $>$ 6; S. Korea $<$ 1; Spain 1,2").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        f6 = Tex("SA: 6 (1960s) $\\to$ 2,3 today").scale(0.95).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(f5))
        self.wait(2)
        self.play(Write(f6))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): infant mortality and life expectancy ---
        self.next_band(3)
        b3_title = Tex("The honest measure, and the average").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        i1 = Tex("Infant mortality: deaths before age one,").scale(0.95).shift(band_shift(3) + UP * 1.2)
        i2 = Tex("per thousand live births").scale(0.95).shift(band_shift(3) + UP * 0.5)
        self.play(Write(i1))
        self.play(Write(i2))
        self.wait(2)
        i3 = Tex("CAR $>$ 70; Iceland, Finland $<$ 2; SA $\\approx$ 25").scale(0.95).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(i3))
        self.wait(2)
        i4 = Tex("Life expectancy: Switzerland $>$ 84").scale(0.95).shift(band_shift(3) + DOWN * 1.3)
        i5 = Tex("SA: 53 in the Aids years $\\to$ 65 with").scale(0.95).shift(band_shift(3) + DOWN * 2.1)
        i6 = Tex("the world's largest treatment programme").scale(0.95).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(i4))
        self.wait(2)
        self.play(Write(i5))
        self.play(Write(i6))
        self.play(Create(SurroundingRectangle(i6, color=GREEN)))
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
        h1 = Tex("1. BASE: broad = high births; pinched = falling").scale(0.95).shift(band_shift(5) + UP * 1.2)
        h2 = Tex("2. SLOPE: steep taper = high mortality").scale(0.95).shift(band_shift(5) + UP * 0.4)
        h3 = Tex("3. IRREGULARITIES: notch = catastrophe,").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        h3b = Tex("bulge = boom or immigration").scale(0.95).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(h1))
        self.wait(2)
        self.play(Write(h2))
        self.wait(2)
        self.play(Write(h3))
        self.play(Write(h3b))
        self.wait(2)
        dr = MathTex(r"\frac{30 + 6}{64} \times 100 \approx 56 \text{ per } 100 \text{ workers}").scale(0.95).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(dr))
        self.play(Create(SurroundingRectangle(dr, color=GREEN)))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the three classic shapes ---
        self.next_band(6)
        b6_title = Tex("Three classic shapes").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        # three miniature pyramids side by side
        cxs = [-4.2, 0.0, 4.2]
        shapes = [
            [2.0, 1.6, 1.2, 0.8, 0.4],
            [1.6, 1.6, 1.55, 1.5, 0.9],
            [1.0, 1.5, 1.8, 1.6, 1.2],
        ]
        labels = ["expansive", "stationary", "constrictive"]
        subs = ["Mali, Uganda", "Australia, Denmark", "Japan, S. Korea"]
        for cx3, ws, lab, sub in zip(cxs, shapes, labels, subs):
            by = float(band_shift(6)[1]) - 1.6
            for i, w in enumerate(ws):
                row = pyramid_row(cx3, by + i * 0.42, w / 2, w / 2 * 1.02, h=0.34)
                self.play(Create(row), run_time=0.35)
            l1 = Tex(lab).scale(0.75).shift(np.array([cx3, by - 0.7, 0]))
            l2 = Tex(sub).scale(0.6).shift(np.array([cx3, by - 1.25, 0]))
            self.play(Write(l1), Write(l2), run_time=0.6)
        self.wait(2)
        b6_l1 = Tex("Momentum: giant child cohorts become").scale(0.9).shift(band_shift(6) + DOWN * 3.0)
        b6_l2 = Tex("giant parent cohorts — growth rolls on").scale(0.9).shift(band_shift(6) + DOWN * 3.6)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): South Africa's transitional pyramid ---
        self.next_band(7)
        b7_title = Tex("South Africa: transitional").scale(1.15).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(1.5)
        s1 = Tex("Base broad but no longer widening (TFR 2,3)").scale(0.95).shift(band_shift(7) + UP * 1.3)
        self.play(Write(s1))
        self.wait(2)
        s2 = Tex("Bulge through the twenties and thirties").scale(0.95).shift(band_shift(7) + UP * 0.5)
        self.play(Write(s2))
        self.wait(2)
        s3 = Tex("Faster taper above: the Aids scar").scale(0.95).shift(band_shift(7) + DOWN * 0.3)
        s4 = Tex("in the middle-aged cohorts").scale(0.95).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(s3))
        self.play(Write(s4))
        self.wait(2)
        s5 = Tex("Big working-age share vs dependants:").scale(0.95).shift(band_shift(7) + DOWN * 1.9)
        s6 = Tex("demographic dividend — if jobs arrive").scale(0.95).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(s5))
        self.play(Write(s6))
        self.play(Create(SurroundingRectangle(s6, color=GREEN)))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the report card ---
        self.next_band(8)
        b8_title = Tex("A country's report card").scale(1.2).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        r1 = Tex("Births /1000; deaths /1000;").scale(1.0).shift(band_shift(8) + UP * 1.3)
        r2 = Tex("births $-$ deaths = natural increase").scale(1.0).shift(band_shift(8) + UP * 0.5)
        self.play(Write(r1))
        self.play(Write(r2))
        self.wait(2)
        r3 = Tex("Fertility: remember 2,1 forever").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(r3))
        self.play(Create(SurroundingRectangle(r3, color=GREEN)))
        self.wait(2)
        r4 = Tex("Infant mortality: the strictest subject").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        r5 = Tex("Life expectancy: an average — lost").scale(1.0).shift(band_shift(8) + DOWN * 2.1)
        r5b = Tex("babies drag it down, elders still exist").scale(1.0).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(r4))
        self.wait(2)
        self.play(Write(r5))
        self.play(Write(r5b))
        self.wait(2.5)

        # --- Band 9 (subtopic_6): the family photograph ---
        self.next_band(9)
        b9_title = Tex("The photograph by age rows").scale(1.15).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        p1 = Tex("Babies in front, elders at the back,").scale(1.0).shift(band_shift(9) + UP * 1.3)
        p2 = Tex("males left, females right of the aisle").scale(1.0).shift(band_shift(9) + UP * 0.5)
        self.play(Write(p1))
        self.play(Write(p2))
        self.wait(2)
        p3 = Tex("From the ladder: the outline is the pyramid").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(p3))
        self.play(Create(SurroundingRectangle(p3, color=GREEN)))
        self.wait(2.5)
        p4 = Tex("Short row: a bitten generation —").scale(0.95).shift(band_shift(9) + DOWN * 1.3)
        p4b = Tex("war, epidemic, famine").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(p4))
        self.play(Write(p4b))
        self.wait(2)
        p5 = Tex("Three blocks: young, workers, retired —").scale(0.95).shift(band_shift(9) + DOWN * 2.8)
        p5b = Tex("how many ride on each hundred workers?").scale(0.95).shift(band_shift(9) + DOWN * 3.5)
        self.play(Write(p5))
        self.play(Write(p5b))
        self.wait(2.5)

        # --- Band 10 (subtopic_7): stacks of crates ---
        self.next_band(10)
        b10_title = Tex("Three stacks of crates").scale(1.2).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        c1 = Tex("Pyramid stack: children everywhere,").scale(0.95).shift(band_shift(10) + UP * 1.3)
        c1b = Tex("growth rolling on — momentum").scale(0.95).shift(band_shift(10) + UP * 0.6)
        self.play(Write(c1))
        self.play(Write(c1b))
        self.wait(2)
        c2 = Tex("Column stack: steady size, long lives").scale(0.95).shift(band_shift(10) + DOWN * 0.2)
        self.play(Write(c2))
        self.wait(2)
        c3 = Tex("Pinched stack: fewer children than adults —").scale(0.95).shift(band_shift(10) + DOWN * 1.0)
        c3b = Tex("thirty years on, pensioners on few workers").scale(0.95).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(c3))
        self.play(Write(c3b))
        self.wait(2.5)
        c4 = Tex("SA: between pyramid and column —").scale(0.95).shift(band_shift(10) + DOWN * 2.5)
        c4b = Tex("a bulge that needs jobs").scale(0.95).shift(band_shift(10) + DOWN * 3.2)
        self.play(Write(c4))
        self.play(Write(c4b))
        self.play(Create(SurroundingRectangle(c4b, color=GREEN)))
        self.wait(3)
