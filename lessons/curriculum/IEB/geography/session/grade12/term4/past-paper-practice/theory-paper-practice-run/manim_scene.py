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

# Band-layout whiteboard scene for the IEB Grade 12 Geography session
# "Theory Paper Practice Run". Bands cover all seven subtopics with dwell
# time proportional to subtopics.json (200/220/240/220/240/220/220 of
# 1560 s). The synoptic-chart sketch and the river-capture sketch are
# hand-built from exporter-safe primitives only (Tex/MathTex/Line/Arrow/
# Dot/Circle/Rectangle/VGroup); add-only lifecycle, camera moves between
# bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TheoryPaperPracticeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # --- Band 0 (subtopic_1): how the practice set is built ---
        title = Tex("Theory Paper Practice Run").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Five stations: a quick-fire warm-up, then").scale(1.0).shift(UP * 0.9)
        b0_l2 = Tex(r"four walked questions, one per theory pillar").scale(1.0).shift(UP * 0.2)
        self.play(Write(b0_l1)); self.wait(1.8)
        self.play(Write(b0_l2)); self.wait(2)
        b0_l3 = Tex(r"Every question climbs a staircase: definition,").scale(0.95).shift(DOWN * 0.6)
        b0_l4 = Tex(r"source-reading, explanation, insight").scale(1.0).shift(DOWN * 1.3)
        self.play(Write(b0_l3)); self.wait(1.6)
        self.play(Write(b0_l4)); self.wait(1.8)
        b0_l5 = MathTex(r"\text{Paragraph task: } 8 = 4 \times 2,\ \text{full sentences}").scale(0.95).shift(DOWN * 2.2)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(2)
        b0_l6 = Tex(r"A blank can never earn a mark --- answer everything").scale(0.9).shift(DOWN * 3.0)
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_2): the warm-up, climate five ---
        self.next_band(1)
        b1_t = Tex("Warm-up: retrieval speed (climate five)").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        rows = [
            r"Spin for all large systems? Coriolis force",
            r"Cold front's violent cloud? Cumulonimbus",
            r"SH highs circle anticlockwise? True",
            r"Daytime up-slope wind? Anabatic",
            r"Moisture front splits? Moist east, dry west",
        ]
        for i, txt in enumerate(rows):
            m = Tex(txt).scale(0.95).shift(band_shift(1) + UP * (1.1 - 0.8 * i))
            self.play(Write(m))
            self.wait(1.8)
        self.wait(2)

        # --- Band 2 (subtopic_2): the warm-up, geomorphology five ---
        self.next_band(2)
        b2_t = Tex("Warm-up: the geomorphology five").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        rows = [
            r"High ground between basins? Watershed",
            r"Pattern converging on a pan? Centripetal",
            r"Unequal orders raise the order? False",
            r"Lowest level a river can cut to? Base level",
            r"Paired terraces prove? Rejuvenation",
        ]
        for i, txt in enumerate(rows):
            m = Tex(txt).scale(0.95).shift(band_shift(2) + UP * (1.1 - 0.8 * i))
            self.play(Write(m))
            self.wait(1.8)
        b2_l = Tex(r"Train it like vocabulary: daily, aloud, fast").scale(0.95).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l))
        self.wait(2)

        # --- Band 3 (subtopic_3): the summer synoptic chart, sketched ---
        self.next_band(3)
        b3_t = Tex("Climate walk: a late-January chart").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        sc3 = band_shift(3) + DOWN * 0.4
        coast = VGroup(
            Line(sc3 + LEFT * 1.2 + UP * 1.6, sc3 + LEFT * 1.8 + DOWN * 0.2, stroke_width=3),
            Line(sc3 + LEFT * 1.8 + DOWN * 0.2, sc3 + LEFT * 0.6 + DOWN * 1.2, stroke_width=3),
            Line(sc3 + LEFT * 0.6 + DOWN * 1.2, sc3 + RIGHT * 1.6 + DOWN * 0.8, stroke_width=3),
        )
        for seg in coast:
            self.play(Create(seg), run_time=0.5)
        cyc = Circle(radius=0.7, color=RED).shift(sc3 + RIGHT * 3.2 + UP * 1.0)
        eye = Circle(radius=0.18, color=WHITE).shift(sc3 + RIGHT * 3.2 + UP * 1.0)
        self.play(Create(cyc))
        self.play(Create(eye))
        l_cyc = Tex(r"Cyclone Denga: circular isobars, no fronts").scale(0.8).shift(sc3 + RIGHT * 2.6 + DOWN * 0.2)
        self.play(Write(l_cyc))
        self.wait(1.8)
        l_heat = Tex(r"heat low L").scale(0.9).shift(sc3 + LEFT * 0.4 + UP * 0.5)
        l_high = Tex(r"highs far south").scale(0.85).shift(sc3 + LEFT * 2.6 + DOWN * 2.2)
        self.play(Write(l_heat), Write(l_high))
        self.wait(1.8)
        b3_l1 = Tex(r"Summer evidence: highs migrated south,").scale(0.9).shift(sc3 + UP * 2.0)
        self.play(Write(b3_l1))
        b3_l2 = Tex(r"a late-summer cyclone even exists").scale(0.85).shift(sc3 + UP * 1.4 + RIGHT * 3.0)
        self.play(Write(b3_l2))
        self.wait(3)

        # --- Band 4 (subtopic_3): the coastal forecast, mark by mark ---
        self.next_band(4)
        b4_t = Tex("Coastal forecast: 2 + 4 + 6 + 3 = 15").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex(r"Winds climb as the eye wall approaches").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex(r"Torrential spiral-band rain,").scale(1.0).shift(band_shift(4) + UP * 0.4)
        b4_l3 = Tex(r"flooding on the coastal lowlands").scale(1.0).shift(band_shift(4) + DOWN * 0.3)
        b4_l4 = Tex(r"Storm surge pushed ashore at landfall").scale(1.0).shift(band_shift(4) + DOWN * 1.0)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.wait(1.8)
        b4_l5 = Tex(r"Why not the Highveld? Fuel cut over land;").scale(0.95).shift(band_shift(4) + DOWN * 1.9)
        b4_l6 = Tex(r"distance and escarpment leave only rain").scale(0.95).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l5)); self.wait(1.6)
        self.play(Write(b4_l6))
        self.play(Create(SurroundingRectangle(b4_l6, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): river capture, sketched and named ---
        self.next_band(5)
        b5_t = Tex("Geomorphology walk: river capture").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        sc5 = band_shift(5) + DOWN * 0.6
        river_x = Line(sc5 + LEFT * 2.6 + UP * 1.6, sc5 + LEFT * 2.6 + DOWN * 1.8, color=BLUE, stroke_width=5)
        l_x = Tex(r"X: off the scarp, steep").scale(0.8).shift(sc5 + LEFT * 4.2 + UP * 1.4)
        self.play(Create(river_x), Write(l_x))
        river_y_up = Line(sc5 + RIGHT * 2.6 + UP * 1.6, sc5 + RIGHT * 2.6 + UP * 0.2, color=BLUE, stroke_width=5)
        river_y_low = Line(sc5 + RIGHT * 2.6 + DOWN * 0.6, sc5 + RIGHT * 2.6 + DOWN * 1.8, color=BLUE, stroke_width=2)
        l_y = Tex(r"Y: plateau wanderer").scale(0.8).shift(sc5 + RIGHT * 4.3 + UP * 1.4)
        self.play(Create(river_y_up), Create(river_y_low), Write(l_y))
        self.wait(1.5)
        elbow = Line(sc5 + RIGHT * 2.6 + UP * 0.2, sc5 + LEFT * 2.6 + DOWN * 0.6, color=BLUE, stroke_width=4)
        self.play(Create(elbow))
        d_e = Dot(sc5 + RIGHT * 2.6 + UP * 0.2, color=RED)
        l_e = Tex(r"elbow of capture").scale(0.8).shift(sc5 + RIGHT * 4.3 + UP * 0.2)
        self.play(Create(d_e), Write(l_e))
        self.wait(1.5)
        d_w = Dot(sc5 + RIGHT * 2.6 + DOWN * 0.35, color=YELLOW)
        l_w = Tex(r"wind gap").scale(0.8).shift(sc5 + RIGHT * 3.9 + DOWN * 0.35)
        d_m = Dot(sc5 + RIGHT * 2.6 + DOWN * 1.5, color=YELLOW)
        l_m = Tex(r"misfit stream").scale(0.8).shift(sc5 + RIGHT * 4.2 + DOWN * 1.5)
        self.play(Create(d_w), Write(l_w))
        self.play(Create(d_m), Write(l_m))
        self.wait(2)
        b5_l1 = Tex(r"Why X wins: steeper gradient, headward erosion").scale(0.9).shift(sc5 + DOWN * 2.6)
        self.play(Write(b5_l1))
        self.wait(3)

        # --- Band 6 (subtopic_5): the settlement walk ---
        self.next_band(6)
        b6_t = Tex("Settlement walk: the emptying Platteland").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex(r"Define rural depopulation --- $1 \times 2$").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex(r"Push factors from the extract --- $2 \times 2$:").scale(1.0).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex(r"mechanised farms, the closed mill and co-op").scale(0.95).shift(band_shift(6) + DOWN * 0.3)
        for m in (b6_l1, b6_l2, b6_l3):
            self.play(Write(m))
            self.wait(1.8)
        b6_l4 = Tex(r"Consequences: an ageing town, cascading closures").scale(0.9).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_l4)); self.wait(2)
        b6_l5 = Tex(r"Paragraph contract: state the idea,").scale(1.0).shift(band_shift(6) + DOWN * 2.1)
        b6_l6 = Tex(r"then develop it --- never bullet it").scale(1.0).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l5)); self.wait(1.5)
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_6): the economic geography walk ---
        self.next_band(7)
        b7_t = Tex("Economy walk: zones and sectors").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex(r"IDZ: serviced export estate at a port,").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex(r"with incentives --- $1 \times 2$").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1)); self.wait(1.5)
        self.play(Write(b7_l2)); self.wait(1.8)
        b7_l3 = Tex(r"Tertiary dominates: urbanised service economy").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(b7_l3)); self.wait(1.8)
        b7_l4 = Tex(r"Coega: deep-water port cuts shipping costs,").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        b7_l5 = Tex(r"ready infrastructure lowers set-up costs").scale(0.95).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4)); self.wait(1.5)
        self.play(Write(b7_l5)); self.wait(1.8)
        b7_l6 = MathTex(r"2 + 3 + 4 + 6 = 15\ \text{marks, each sized to fit}").scale(0.95).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_7): the paragraph recipe ---
        self.next_band(8)
        b8_t = Tex("The paragraph question").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex(r"Move 1: obey the instruction verb").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex(r"Move 2: plan four keywords in the margin").scale(1.0).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex(r"Move 3: one sentence per idea + because-clause").scale(1.0).shift(band_shift(8) + DOWN * 0.3)
        b8_l4 = Tex(r"Move 4: keep the topic's vocabulary").scale(1.0).shift(band_shift(8) + DOWN * 1.0)
        for m in (b8_l1, b8_l2, b8_l3, b8_l4):
            self.play(Write(m))
            self.wait(1.9)
        b8_wrong = Tex(r"Bullet points in the paragraph").scale(1.0).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_wrong))
        self.play(Create(strike(b8_wrong)))
        self.wait(1.8)
        b8_l5 = MathTex(r"4\ \text{ideas} \times 2\ \text{marks} = 8").scale(1.1).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(4)
