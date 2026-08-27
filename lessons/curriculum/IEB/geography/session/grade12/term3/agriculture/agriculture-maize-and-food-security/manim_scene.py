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

# Band-layout whiteboard scene for the IEB Grade 12 Geography session duo
# "Agriculture, Maize and Food Security". Bands cover all seven subtopics
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7) with
# dwell time proportional to subtopics.json (225/225/240/240/230/220/240 of
# 1620 s). The Maize Triangle sketch and the two-farms fence are hand-built
# from exporter-safe primitives only (Tex/Line/Arrow/Dot/Rectangle/VGroup);
# add-only lifecycle, the camera moves down between bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AgricultureMaizeFoodSecuritySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # --- Band 0 (subtopic_1): the small-percentage paradox ---
        title = Tex("Agriculture, Maize and Food Security").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"GDP share: only 2--3\%").scale(1.1).shift(UP * 0.9)
        self.play(Write(b0_l1)); self.wait(2)
        b0_wrong = Tex(r"Small share $=$ unimportant").scale(1.05).shift(UP * 0.0)
        self.play(Write(b0_wrong))
        self.play(Create(strike(b0_wrong)))
        self.wait(2)
        b0_l2 = Tex(r"Only $\pm$12\% of the land is arable;").scale(1.0).shift(DOWN * 0.9)
        b0_l3 = Tex(r"rain unreliable over most of it").scale(1.0).shift(DOWN * 1.6)
        self.play(Write(b0_l2)); self.wait(1.7)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the five levers + two markets ---
        self.next_band(1)
        b1_t = Tex("Five levers against \\lq{}unimportant\\rq{}").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        rows = [
            r"1. Feeds 60+ million people",
            r"2. Rural jobs where none else exist",
            r"3. Linkages: feeds agro-processing",
            r"4. Exports: citrus, wine, wool, maize",
            r"5. Anchors rural settlement",
        ]
        for i, txt in enumerate(rows):
            m = Tex(txt).scale(1.0).shift(band_shift(1) + UP * (1.2 - 0.7 * i))
            self.play(Write(m))
            self.wait(1.6)
        b1_l6 = Tex(r"Home market: staples; export market: high value").scale(0.95).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l6))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): two farming worlds, five comparison lines ---
        self.next_band(2)
        b2_t = Tex("Two farming worlds").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex(r"Commercial: 30--40 000 units, big capital,").scale(0.95).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex(r"hired labour, market and export production").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1)); self.wait(1.7)
        self.play(Write(b2_l2)); self.wait(2)
        b2_l3 = Tex(r"Small-scale: family labour, communal land,").scale(0.95).shift(band_shift(2) + DOWN * 0.4)
        b2_l4 = Tex(r"household production, blocked credit").scale(0.95).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_l3)); self.wait(1.7)
        self.play(Write(b2_l4)); self.wait(2)
        b2_l5 = Tex(r"Compare on: size, capital, labour, market, tenure").scale(0.9).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): balanced evaluation + the policy bridge ---
        self.next_band(3)
        b3_t = Tex("Evaluate with balance").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex(r"Large-scale: feeds the nation, exports ---").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex(r"but fewer workers per hectare").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1)); self.wait(1.7)
        self.play(Write(b3_l2)); self.wait(2)
        b3_l3 = Tex(r"Small-scale: millions of livelihoods ---").scale(1.0).shift(band_shift(3) + DOWN * 0.4)
        b3_l4 = Tex(r"but low yields, exposed households").scale(1.0).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l3)); self.wait(1.7)
        self.play(Write(b3_l4)); self.wait(2)
        b3_l5 = Tex(r"Bridge: finance, tenure, extension, markets").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the Maize Triangle, drawn corner by corner ---
        self.next_band(4)
        b4_t = Tex("The Maize Triangle").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        sc4 = band_shift(4)
        p1 = sc4 + DOWN * 1.0 + LEFT * 3.4
        p2 = sc4 + UP * 0.9 + RIGHT * 0.2
        p3 = sc4 + DOWN * 1.0 + RIGHT * 3.4
        d1, d2, d3 = Dot(p1, color=YELLOW), Dot(p2, color=YELLOW), Dot(p3, color=YELLOW)
        l1 = Tex("W Free State\\\\grainlands").scale(0.7).shift(p1 + DOWN * 0.7)
        l2 = Tex("North West\\\\Lichtenburg").scale(0.7).shift(p2 + UP * 0.7)
        l3 = Tex("Mpumalanga\\\\Ermelo").scale(0.7).shift(p3 + DOWN * 0.7)
        self.play(Create(d1), Write(l1)); self.wait(1.4)
        self.play(Create(d2), Write(l2)); self.wait(1.4)
        self.play(Create(d3), Write(l3)); self.wait(1.4)
        t_lines = VGroup(Line(p1, p2, color=GREEN), Line(p2, p3, color=GREEN), Line(p3, p1, color=GREEN))
        self.play(Create(t_lines))
        self.wait(2)
        b4_l1 = Tex(r"Free State: the largest producer").scale(0.95).shift(sc4 + DOWN * 2.4)
        self.play(Write(b4_l1))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): favouring factors and their shadows ---
        self.next_band(5)
        b5_t = Tex("Favouring factors and their shadows").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex(r"Summer rain 500--800 mm in growing season").scale(0.95).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex(r"Long, hot, frost-free summers").scale(0.95).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex(r"Deep soils, gently rolling machine country").scale(0.95).shift(band_shift(5) + DOWN * 0.3)
        b5_l4 = Tex(r"Silos, rail, mills, cultivar research").scale(0.95).shift(band_shift(5) + DOWN * 1.0)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(1.7)
        b5_l5 = Tex(r"Shadows: drought, hail, frost, input costs,").scale(0.95).shift(band_shift(5) + DOWN * 1.9)
        b5_l6 = Tex(r"and a shifting climate").scale(0.95).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l5)); self.wait(1.6)
        self.play(Write(b5_l6))
        self.wait(2.5)

        # --- Band 6 (subtopic_3): maize feeds the country twice ---
        self.next_band(6)
        b6_t = Tex("Maize feeds the country twice").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex(r"White maize $\rightarrow$ mealie meal $\rightarrow$ the staple plate").scale(1.0).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6_l1)); self.wait(2)
        b6_l2 = Tex(r"Yellow maize $\rightarrow$ feed $\rightarrow$ chicken, eggs, dairy, beef").scale(0.95).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2)); self.wait(2)
        b6_l3 = Tex(r"Around it: mills, feed makers, silo towns").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l3)); self.wait(1.8)
        b6_l4 = Tex(r"Surplus years: the subcontinent's grain shed").scale(1.0).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the definition, clause by clause ---
        self.next_band(7)
        b7_t = Tex("Food security, clause by clause").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        rows7 = [
            r"ALL people --- averages hide hunger",
            r"At ALL times --- drought years, month-end",
            r"Physical AND economic access",
            r"Sufficient, safe, nutritious",
        ]
        for i, txt in enumerate(rows7):
            m = Tex(txt).scale(1.0).shift(band_shift(7) + UP * (1.1 - 0.75 * i))
            self.play(Write(m))
            self.wait(1.8)
        b7_l5 = Tex(r"Paradox: national security, household hunger").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_4): factor triads and matched fixes ---
        self.next_band(8)
        b8_t = Tex("Factors in threes, fixes matched").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(1.5)
        b8_l1 = Tex(r"Environmental: drought, degradation, water").scale(0.95).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex(r"Economic: joblessness, food inflation, inputs").scale(0.95).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex(r"Social: population, illness, land uncertainty").scale(0.95).shift(band_shift(8) + DOWN * 0.3)
        for m in (b8_l1, b8_l2, b8_l3):
            self.play(Write(m))
            self.wait(1.7)
        b8_l4 = Tex(r"Fixes: school feeding ($\pm$9 million learners),").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        b8_l5 = Tex(r"grants, gardens, farmer support, storage").scale(0.95).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4)); self.wait(1.6)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): the country that runs on pap ---
        self.next_band(9)
        b9_t = Tex("The country that runs on pap").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex(r"Plate rewound: pap $\leftarrow$ meal $\leftarrow$ white maize").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex(r"Chicken and egg $\leftarrow$ feed $\leftarrow$ yellow maize").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1)); self.wait(1.8)
        self.play(Write(b9_l2)); self.wait(2)
        b9_l3 = Tex(r"Maize on the plate twice --- the diet's floor").scale(1.0).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex(r"Thunderstorm rain keeps its own diary:").scale(1.0).shift(band_shift(9) + DOWN * 1.4)
        b9_l5 = Tex(r"drought is the standing threat").scale(1.0).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l4)); self.wait(1.6)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_6): two farmers, one fence ---
        self.next_band(10)
        b10_t = Tex("Two farmers, one fence").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        sc10 = band_shift(10)
        fence = Line(sc10 + UP * 1.5, sc10 + DOWN * 0.6, color=RED, stroke_width=5)
        self.play(Create(fence))
        big = Tex(r"3 000 ha\\tractors, loan,\\silo contract").scale(0.8).shift(sc10 + UP * 0.5 + LEFT * 2.8)
        small = Tex(r"2 ha communal\\family labour,\\no title, no loan").scale(0.8).shift(sc10 + UP * 0.5 + RIGHT * 2.8)
        self.play(Write(big)); self.wait(1.8)
        self.play(Write(small)); self.wait(2)
        b10_l1 = Tex(r"Five fingers: size, capital, labour, market, tenure").scale(0.9).shift(sc10 + DOWN * 1.4)
        self.play(Write(b10_l1))
        self.play(Create(SurroundingRectangle(b10_l1, color=GREEN)))
        self.wait(2)
        b10_l2 = Tex(r"The fix is a bridge over the fence, not a winner").scale(0.9).shift(sc10 + DOWN * 2.3)
        self.play(Write(b10_l2))
        self.wait(3)

        # --- Band 11 (subtopic_7): full silos, empty plates ---
        self.next_band(11)
        b11_t = Tex("Full silos, empty plates").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(2)
        b11_l1 = Tex(r"Riddle: full silos, hungry children --- how?").scale(1.0).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11_l1)); self.wait(2)
        b11_l2 = Tex(r"Country secure: farms + imports suffice").scale(1.0).shift(band_shift(11) + UP * 0.3)
        b11_l3 = Tex(r"Households insecure: the money is missing").scale(1.0).shift(band_shift(11) + DOWN * 0.4)
        self.play(Write(b11_l2)); self.wait(1.7)
        self.play(Write(b11_l3))
        self.play(Create(SurroundingRectangle(b11_l3, color=GREEN)))
        self.wait(2)
        b11_l4 = Tex(r"Three bags: nature, money, people").scale(1.0).shift(band_shift(11) + DOWN * 1.3)
        self.play(Write(b11_l4)); self.wait(1.8)
        b11_l5 = Tex(r"Fixes aimed at bags: feeding schemes, grants,").scale(0.95).shift(band_shift(11) + DOWN * 2.1)
        b11_l6 = Tex(r"gardens, farmer support, tougher seed").scale(0.95).shift(band_shift(11) + DOWN * 2.8)
        self.play(Write(b11_l5)); self.wait(1.5)
        self.play(Write(b11_l6))
        self.wait(4)
