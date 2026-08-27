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

# Band-layout whiteboard scene for the rural settlement types, patterns
# and functions duo lesson. Exporter-safe primitives only (Tex/Line/
# Arrow/Dot/Circle/Rectangle/VGroup); add-only lifecycle; camera moves
# down one frame-height per band. Village shapes are hand-built from
# Dots, Circles and Line chains, assembled in script order.
#
# Subtopic shares (subtopics.json, total 1560 s):
# 235/225/230/240 expert, 210/200/220 simplifier. Bands 0-7 = Part 1
# (two per expert subtopic), bands 8-10 = fresh Part 2 bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RuralSettlementTypesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): definition + the dividing line ---
        title = Tex("Settlement, site and situation").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex(r"Settlement: any place people live + their structures").scale(0.9).shift(UP * 1.4)
        self.play(Write(d1))
        self.wait(2)
        d2 = Tex(r"Rural: primary activity, low density").scale(0.95).shift(UP * 0.5)
        d3 = Tex(r"Urban: secondary + tertiary, high density").scale(0.95).shift(DOWN * 0.3)
        self.play(Write(d2))
        self.wait(2)
        self.play(Write(d3))
        self.wait(2)
        d4 = Tex(r"Dividing line = dominant ACTIVITY, not size").scale(0.95).shift(DOWN * 1.3)
        self.play(Write(d4))
        self.play(Create(SurroundingRectangle(d4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): site vs situation + wet/dry point ---
        self.next_band(1)
        b1_t = Tex("Under the feet vs around the horizon").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        s1 = Tex(r"SITE: relief, drainage, soil, water, aspect").scale(0.95).shift(band_shift(1) + UP * 1.2)
        s2 = Tex(r"SITUATION: position among routes, rivers, towns").scale(0.95).shift(band_shift(1) + UP * 0.4)
        self.play(Write(s1))
        self.wait(2)
        self.play(Write(s2))
        self.wait(2)
        s3 = Tex(r"Wet-point: built FOR water (Namaqualand borehole)").scale(0.9).shift(band_shift(1) + DOWN * 0.5)
        s4 = Tex(r"Dry-point: built to ESCAPE water (above floodplain)").scale(0.9).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(s3))
        self.wait(2)
        self.play(Write(s4))
        self.play(Create(SurroundingRectangle(s4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the ladder + two master patterns ---
        self.next_band(2)
        b2_t = Tex("The ladder and the two patterns").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        l1 = Tex(r"farmstead $\rightarrow$ hamlet $\rightarrow$ village $\rightarrow$").scale(0.95).shift(band_shift(2) + UP * 1.2)
        l1b = Tex(r"town $\rightarrow$ city $\rightarrow$ metropolis").scale(0.95).shift(band_shift(2) + UP * 0.5)
        self.play(Write(l1))
        self.play(Write(l1b))
        self.wait(2.5)
        # Dispersed: scattered dots; nucleated: clustered dots
        dd1 = Dot(band_shift(2) + LEFT * 4.0 + DOWN * 0.8, radius=0.09, color=WHITE)
        dd2 = Dot(band_shift(2) + LEFT * 2.6 + DOWN * 1.6, radius=0.09, color=WHITE)
        dd3 = Dot(band_shift(2) + LEFT * 3.8 + DOWN * 2.3, radius=0.09, color=WHITE)
        dd_lab = Tex(r"dispersed").scale(0.8).shift(band_shift(2) + LEFT * 3.2 + DOWN * 2.9)
        self.play(Create(dd1), Create(dd2), Create(dd3))
        self.play(Write(dd_lab))
        self.wait(2)
        nn = VGroup(*[Dot(band_shift(2) + RIGHT * 3.0 + DOWN * 1.5 +
                          0.32 * np.array([np.cos(a), np.sin(a), 0]), radius=0.09, color=WHITE)
                      for a in np.linspace(0, TAU, 7, endpoint=False)])
        nn_lab = Tex(r"nucleated").scale(0.8).shift(band_shift(2) + RIGHT * 3.0 + DOWN * 2.9)
        self.play(Create(nn))
        self.play(Write(nn_lab))
        self.wait(3)

        # --- Band 3 (subtopic_2): the reasons + function contrast ---
        self.next_band(3)
        b3_t = Tex("Why each pattern, and the function test").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        r1 = Tex(r"Dispersed: large PRIVATE farms — live on the land").scale(0.9).shift(band_shift(3) + UP * 1.2)
        r2 = Tex(r"Nucleated: COMMUNAL tenure, defence, shared water").scale(0.9).shift(band_shift(3) + UP * 0.4)
        self.play(Write(r1))
        self.wait(2)
        self.play(Write(r2))
        self.wait(2)
        r3 = Tex(r"Rural = unifunctional (one land-tied activity)").scale(0.9).shift(band_shift(3) + DOWN * 0.5)
        r4 = Tex(r"Urban = multifunctional (many under one name)").scale(0.9).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(r3))
        self.wait(2)
        self.play(Write(r4))
        self.play(Create(SurroundingRectangle(r3, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): round and linear villages ---
        self.next_band(4)
        b4_t = Tex("Round and linear").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        # Round: dots on a circle around a small central circle (kraal)
        kraal = Circle(radius=0.35, color=YELLOW).shift(band_shift(4) + LEFT * 2.8 + DOWN * 0.6)
        ring = VGroup(*[Dot(band_shift(4) + LEFT * 2.8 + DOWN * 0.6 +
                            1.1 * np.array([np.cos(a), np.sin(a), 0]), radius=0.09, color=WHITE)
                        for a in np.linspace(0, TAU, 8, endpoint=False)])
        round_lab = Tex(r"round: homes on the rim, kraal in the heart").scale(0.8).shift(band_shift(4) + LEFT * 2.6 + DOWN * 2.3)
        self.play(Create(kraal))
        self.play(Create(ring))
        self.play(Write(round_lab))
        self.wait(2.5)
        # Linear: dots along a line (road)
        road = Line(band_shift(4) + RIGHT * 0.6 + UP * 1.0, band_shift(4) + RIGHT * 5.0 + DOWN * 1.4, color=GREY, stroke_width=4)
        beads = VGroup(*[Dot(road.point_from_proportion(t) + 0.25 * UP, radius=0.08, color=WHITE)
                         for t in np.linspace(0.08, 0.92, 6)])
        lin_lab = Tex(r"linear: beads on a string — frontage").scale(0.8).shift(band_shift(4) + RIGHT * 2.9 + DOWN * 2.3)
        self.play(Create(road))
        self.play(Create(beads))
        self.play(Write(lin_lab))
        self.wait(3)

        # --- Band 5 (subtopic_3): T-shaped and crossroad villages ---
        self.next_band(5)
        b5_t = Tex("T-shaped and crossroad").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        # T: main road horizontal, side road ends against it
        t_main = Line(band_shift(5) + LEFT * 4.8 + UP * 0.6, band_shift(5) + LEFT * 0.8 + UP * 0.6, color=GREY, stroke_width=4)
        t_side = Line(band_shift(5) + LEFT * 2.8 + UP * 0.6, band_shift(5) + LEFT * 2.8 + DOWN * 1.8, color=GREY, stroke_width=4)
        t_lab = Tex(r"T: side road ends — trade at the junction").scale(0.8).shift(band_shift(5) + LEFT * 2.6 + DOWN * 2.4)
        self.play(Create(t_main), Create(t_side))
        self.play(Write(t_lab))
        self.wait(2.5)
        # Crossroad: two crossing roads
        c_h = Line(band_shift(5) + RIGHT * 0.8 + DOWN * 0.4, band_shift(5) + RIGHT * 4.8 + DOWN * 0.4, color=GREY, stroke_width=4)
        c_v = Line(band_shift(5) + RIGHT * 2.8 + UP * 1.2, band_shift(5) + RIGHT * 2.8 + DOWN * 2.0, color=GREY, stroke_width=4)
        c_lab = Tex(r"crossroad: four arms, X of homes").scale(0.8).shift(band_shift(5) + RIGHT * 2.9 + DOWN * 2.6)
        self.play(Create(c_h), Create(c_v))
        self.play(Write(c_lab))
        self.wait(2)
        j1 = Tex(r"Cause for both: junctions concentrate passing trade").scale(0.85).shift(band_shift(5) + UP * 1.4)
        self.play(Write(j1))
        self.play(Create(SurroundingRectangle(j1, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the three land-use functions ---
        self.next_band(6)
        b6_t = Tex("Function read off the land").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        f1 = Tex(r"Farming: Swartland wheat, Sundays River citrus,").scale(0.85).shift(band_shift(6) + UP * 1.2)
        f1b = Tex(r"coastal cane; bushveld cattle, Karoo sheep").scale(0.85).shift(band_shift(6) + UP * 0.5)
        self.play(Write(f1))
        self.play(Write(f1b))
        self.wait(2.5)
        f2 = Tex(r"Intensive = dense settlement; extensive = far apart").scale(0.85).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(f2))
        self.play(Create(SurroundingRectangle(f2, color=GREEN)))
        self.wait(2)
        f3 = Tex(r"Forestry: plantation villages + sawmill towns").scale(0.85).shift(band_shift(6) + DOWN * 1.3)
        f4 = Tex(r"Conservation: staff villages, rest camps (Addo)").scale(0.85).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(f3))
        self.wait(2)
        self.play(Write(f4))
        self.wait(3)

        # --- Band 7 (subtopic_4): the five-move commentary ---
        self.next_band(7)
        b7_t = Tex("The five-move commentary").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        m1 = Tex(r"1. Classify: rural — activity is primary").scale(0.95).shift(band_shift(7) + UP * 1.2)
        m2 = Tex(r"2. Pattern: dispersed / nucleated + reason").scale(0.95).shift(band_shift(7) + UP * 0.4)
        m3 = Tex(r"3. Shape: round / linear / T / crossroad + cause").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        m4 = Tex(r"4. Function: from the land-use evidence").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        m5 = Tex(r"5. Site and situation: under vs around").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(m1))
        self.wait(2)
        self.play(Write(m2))
        self.wait(2)
        self.play(Write(m3))
        self.wait(2)
        self.play(Write(m4))
        self.wait(2)
        self.play(Write(m5))
        self.play(Create(SurroundingRectangle(m5, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the stand and the street ---
        self.next_band(8)
        b8_t = Tex("The stand and the street").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        x1 = Tex(r"Conversation 1 — the plot: slope, drainage,").scale(0.9).shift(band_shift(8) + UP * 1.2)
        x1b = Tex(r"soil, water, winter sun = SITE").scale(0.9).shift(band_shift(8) + UP * 0.5)
        self.play(Write(x1))
        self.play(Write(x1b))
        self.wait(2.5)
        x2 = Tex(r"Conversation 2 — the distances: school, clinic,").scale(0.9).shift(band_shift(8) + DOWN * 0.4)
        x2b = Tex(r"taxi rank, town = SITUATION").scale(0.9).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(x2))
        self.play(Write(x2b))
        self.wait(2.5)
        x3 = Tex(r"Wet-point: built for the borehole; dry-point:").scale(0.85).shift(band_shift(8) + DOWN * 2.0)
        x3b = Tex(r"built above the flood — braai-in-the-rain logic").scale(0.85).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(x3))
        self.play(Write(x3b))
        self.play(Create(SurroundingRectangle(x3b, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): scattered beans or one bowl ---
        self.next_band(9)
        b9_t = Tex("Scattered beans or one bowl").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        y1 = Tex(r"Ladder: farmstead, hamlet, village, town,").scale(0.9).shift(band_shift(9) + UP * 1.2)
        y1b = Tex(r"city, metropolis — people AND services rise").scale(0.9).shift(band_shift(9) + UP * 0.5)
        self.play(Write(y1))
        self.play(Write(y1b))
        self.wait(2.5)
        y2 = Tex(r"Flung beans = dispersed = private farms").scale(0.9).shift(band_shift(9) + DOWN * 0.4)
        y3 = Tex(r"One bowl = nucleated = communal land").scale(0.9).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(y2))
        self.wait(2)
        self.play(Write(y3))
        self.play(Create(SurroundingRectangle(y3, color=GREEN)))
        self.wait(2)
        y4 = Tex(r"One kind of work = unifunctional = rural").scale(0.9).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(y4))
        self.wait(3)

        # --- Band 10 (subtopic_7): reading a village like a taxi route ---
        self.next_band(10)
        b10_t = Tex("Reading a village like a taxi route").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        z1 = Tex(r"Ring around the kraal = round (protection)").scale(0.9).shift(band_shift(10) + UP * 1.2)
        z2 = Tex(r"Beads on the tar = linear (frontage)").scale(0.9).shift(band_shift(10) + UP * 0.4)
        z3 = Tex(r"T or X at the junction = trade magnet").scale(0.9).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(z1))
        self.wait(2)
        self.play(Write(z2))
        self.wait(2)
        self.play(Write(z3))
        self.play(Create(SurroundingRectangle(z3, color=GREEN)))
        self.wait(2)
        z4 = Tex(r"Land says the function: mealies = crops,").scale(0.85).shift(band_shift(10) + DOWN * 1.3)
        z4b = Tex(r"kraals = stock, pine rows = forestry, camps = parks").scale(0.85).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(z4))
        self.play(Write(z4b))
        self.wait(2)
        z5 = Tex(r"Five moves, marks on sight").scale(0.95).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(z5))
        self.wait(4)
