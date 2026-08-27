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

# Band-layout whiteboard scene for the rural-settlements duo (types,
# patterns and functions). Exporter-safe primitives only
# (Tex/MathTex/Line/Arrow/Dot/Circle/Rectangle/VGroup); add-only lifecycle;
# camera moves down one frame-height per band. Settlement patterns and the
# four village shapes are hand-built dot-and-line diagrams (dispersed vs
# nucleated dots, round ring, linear string, T and crossroad arms), each
# assembled element by element in script order.
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
        title = Tex("Settlement, Site and Situation").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex(r"Settlement: any place where people live,").scale(1.0).shift(UP * 1.2)
        d1b = Tex(r"with the buildings and structures they use").scale(1.0).shift(UP * 0.4)
        self.play(Write(d1))
        self.play(Write(d1b))
        self.wait(2.5)
        d2 = Tex(r"Rural: small, low density, PRIMARY work").scale(1.0).shift(DOWN * 0.5)
        d3 = Tex(r"Urban: larger, dense, secondary + tertiary").scale(1.0).shift(DOWN * 1.3)
        self.play(Write(d2))
        self.wait(2)
        self.play(Write(d3))
        self.wait(2)
        d4 = Tex(r"The line is dominant ACTIVITY, not size").scale(1.0).shift(DOWN * 2.3)
        self.play(Write(d4))
        self.play(Create(SurroundingRectangle(d4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): site vs situation + wet/dry point ---
        self.next_band(1)
        b1_t = Tex("Site under your feet, situation around you").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        s1 = Tex(r"SITE: the land built on — relief, drainage,").scale(1.0).shift(band_shift(1) + UP * 1.2)
        s1b = Tex(r"soil, water supply, aspect").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(s1))
        self.play(Write(s1b))
        self.wait(2.5)
        s2 = Tex(r"SITUATION: position relative to routes,").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        s2b = Tex(r"rivers, passes and other settlements").scale(1.0).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(s2))
        self.play(Write(s2b))
        self.wait(2.5)
        s3 = Tex(r"Wet-point: built AT water (Karoo borehole)").scale(0.95).shift(band_shift(1) + DOWN * 2.2)
        s4 = Tex(r"Dry-point: built ABOVE floods (KZN homesteads)").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(s3))
        self.wait(2)
        self.play(Write(s4))
        self.play(Create(SurroundingRectangle(s4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the ladder + two master patterns ---
        self.next_band(2)
        b2_t = Tex("The ladder, and the two master patterns").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        l1 = Tex(r"farmstead $\rightarrow$ hamlet $\rightarrow$ village $\rightarrow$ town").scale(0.95).shift(band_shift(2) + UP * 1.3)
        l1b = Tex(r"$\rightarrow$ city $\rightarrow$ metropolis (rural = bottom 3)").scale(0.95).shift(band_shift(2) + UP * 0.6)
        self.play(Write(l1))
        self.play(Write(l1b))
        self.wait(2.5)
        # Dispersed: scattered dots; nucleated: tight cluster
        dsp1 = Dot(band_shift(2) + LEFT * 4.6 + DOWN * 0.6, color=YELLOW)
        dsp2 = Dot(band_shift(2) + LEFT * 3.2 + DOWN * 1.8, color=YELLOW)
        dsp3 = Dot(band_shift(2) + LEFT * 1.8 + DOWN * 0.9, color=YELLOW)
        dsp_lab = Tex(r"dispersed").scale(0.9).shift(band_shift(2) + LEFT * 3.2 + DOWN * 2.6)
        self.play(Create(dsp1), Create(dsp2), Create(dsp3))
        self.play(Write(dsp_lab))
        self.wait(2)
        nuc1 = Dot(band_shift(2) + RIGHT * 2.6 + DOWN * 1.1, color=YELLOW)
        nuc2 = Dot(band_shift(2) + RIGHT * 3.0 + DOWN * 1.4, color=YELLOW)
        nuc3 = Dot(band_shift(2) + RIGHT * 3.4 + DOWN * 1.0, color=YELLOW)
        nuc4 = Dot(band_shift(2) + RIGHT * 3.0 + DOWN * 0.8, color=YELLOW)
        nuc_lab = Tex(r"nucleated").scale(0.9).shift(band_shift(2) + RIGHT * 3.0 + DOWN * 2.6)
        self.play(Create(nuc1), Create(nuc2), Create(nuc3), Create(nuc4))
        self.play(Write(nuc_lab))
        self.wait(2)
        pat = Tex(r"Free State farms scatter; homeland villages cluster").scale(0.9).shift(band_shift(2) + DOWN * 3.3)
        self.play(Write(pat))
        self.wait(3)

        # --- Band 3 (subtopic_2): the reasons + function contrast ---
        self.next_band(3)
        b3_t = Tex("Each pattern answers the land's question").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        r1 = Tex(r"Dispersal: large PRIVATE farms — the farmer").scale(0.95).shift(band_shift(3) + UP * 1.2)
        r1b = Tex(r"must live on the land being worked").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(r1))
        self.play(Write(r1b))
        self.wait(2.5)
        r2 = Tex(r"Nucleation: COMMUNAL tenure, defence,").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        r2b = Tex(r"shared water and community life").scale(0.95).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(r2))
        self.play(Write(r2b))
        self.wait(2.5)
        r3 = Tex(r"Rural = UNIFUNCTIONAL (one land-tied job);").scale(0.95).shift(band_shift(3) + DOWN * 2.2)
        r3b = Tex(r"urban = multifunctional").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(r3))
        self.play(Write(r3b))
        self.play(Create(SurroundingRectangle(r3b, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): round and linear villages ---
        self.next_band(4)
        b4_t = Tex("Rural shapes 1--2: round and linear").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        # Round: ring of dots around a central kraal circle
        ring = Circle(radius=1.1, color=GREY).shift(band_shift(4) + LEFT * 3.2 + DOWN * 0.4)
        kraal = Circle(radius=0.35, color=YELLOW).shift(band_shift(4) + LEFT * 3.2 + DOWN * 0.4)
        rd1 = Dot(band_shift(4) + LEFT * 3.2 + UP * 0.7, color=WHITE)
        rd2 = Dot(band_shift(4) + LEFT * 2.1 + DOWN * 0.4, color=WHITE)
        rd3 = Dot(band_shift(4) + LEFT * 3.2 + DOWN * 1.5, color=WHITE)
        rd4 = Dot(band_shift(4) + LEFT * 4.3 + DOWN * 0.4, color=WHITE)
        rnd_lab = Tex(r"round: homes ring the kraal").scale(0.85).shift(band_shift(4) + LEFT * 3.0 + DOWN * 2.3)
        self.play(Create(ring), Create(kraal))
        self.play(Create(rd1), Create(rd2), Create(rd3), Create(rd4))
        self.play(Write(rnd_lab))
        self.wait(2)
        # Linear: dots along a road line
        road = Line(band_shift(4) + RIGHT * 0.6 + DOWN * 0.4, band_shift(4) + RIGHT * 5.2 + DOWN * 0.4,
                    color=GREY, stroke_width=5)
        ld1 = Dot(band_shift(4) + RIGHT * 1.4 + DOWN * 0.1, color=WHITE)
        ld2 = Dot(band_shift(4) + RIGHT * 2.4 + DOWN * 0.1, color=WHITE)
        ld3 = Dot(band_shift(4) + RIGHT * 3.4 + DOWN * 0.1, color=WHITE)
        ld4 = Dot(band_shift(4) + RIGHT * 4.4 + DOWN * 0.1, color=WHITE)
        lin_lab = Tex(r"linear: beads on a string").scale(0.85).shift(band_shift(4) + RIGHT * 2.9 + DOWN * 1.2)
        self.play(Create(road))
        self.play(Create(ld1), Create(ld2), Create(ld3), Create(ld4))
        self.play(Write(lin_lab))
        self.wait(2)
        why = Tex(r"Round: defence + community. Linear: frontage").scale(0.95).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(why))
        self.wait(3)

        # --- Band 5 (subtopic_3): T-shaped and crossroad villages ---
        self.next_band(5)
        b5_t = Tex("Rural shapes 3--4: T-shaped and crossroad").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        # T: main road horizontal, side road up from it
        t_main = Line(band_shift(5) + LEFT * 5.0 + DOWN * 0.6, band_shift(5) + LEFT * 1.4 + DOWN * 0.6,
                      color=GREY, stroke_width=5)
        t_side = Line(band_shift(5) + LEFT * 3.2 + DOWN * 0.6, band_shift(5) + LEFT * 3.2 + UP * 1.2,
                      color=GREY, stroke_width=5)
        t_lab = Tex(r"T: side road ends on main road").scale(0.85).shift(band_shift(5) + LEFT * 3.0 + DOWN * 1.5)
        self.play(Create(t_main), Create(t_side))
        self.play(Write(t_lab))
        self.wait(2)
        # Crossroad: two crossing lines
        xr1 = Line(band_shift(5) + RIGHT * 1.2 + DOWN * 0.2, band_shift(5) + RIGHT * 5.0 + DOWN * 0.2,
                   color=GREY, stroke_width=5)
        xr2 = Line(band_shift(5) + RIGHT * 3.1 + UP * 1.4, band_shift(5) + RIGHT * 3.1 + DOWN * 1.6,
                   color=GREY, stroke_width=5)
        x_lab = Tex(r"crossroad: buildings on all four arms").scale(0.85).shift(band_shift(5) + RIGHT * 3.1 + DOWN * 2.1)
        self.play(Create(xr1), Create(xr2))
        self.play(Write(x_lab))
        self.wait(2)
        jt = Tex(r"Junctions slow traffic — trade plants itself there").scale(0.95).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(jt))
        self.wait(2)
        tech = Tex(r"Name the shape (1 mark), give the reason (the rest)").scale(0.9).shift(band_shift(5) + DOWN * 3.5)
        self.play(Write(tech))
        self.play(Create(SurroundingRectangle(tech, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the three land-use functions ---
        self.next_band(6)
        b6_t = Tex("Function read straight off the land use").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        f1 = Tex(r"Farming: crops (Free State maize, KZN cane,").scale(0.95).shift(band_shift(6) + UP * 1.2)
        f1b = Tex(r"Cape fruit) or stock (bushveld, Karoo sheep)").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(f1))
        self.play(Write(f1b))
        self.wait(2.5)
        f2 = Tex(r"Intensive plots: dense settlement; extensive").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        f2b = Tex(r"Karoo runs: farmsteads far apart").scale(0.95).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(f2))
        self.play(Write(f2b))
        self.wait(2.5)
        f3 = Tex(r"Forestry: plantation villages, sawmill towns").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        f4 = Tex(r"Conservation: Kruger staff villages, camps").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(f3))
        self.wait(2)
        self.play(Write(f4))
        self.wait(3)

        # --- Band 7 (subtopic_4): the five-move commentary ---
        self.next_band(7)
        b7_t = Tex("The five-move commentary").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        c1 = Tex(r"1. Classify: rural — primary activity").scale(0.95).shift(band_shift(7) + UP * 1.2)
        c2 = Tex(r"2. Pattern: dispersed/nucleated + tenure reason").scale(0.95).shift(band_shift(7) + UP * 0.4)
        c3 = Tex(r"3. Shape: round, linear, T, crossroad + cause").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        c4 = Tex(r"4. Function: from the land-use evidence").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        c5 = Tex(r"5. Site + situation: wet/dry point, routes").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.wait(2)
        self.play(Write(c3))
        self.wait(2)
        self.play(Write(c4))
        self.wait(2)
        self.play(Write(c5))
        self.wait(2)
        c6 = Tex(r"Five moves, each worth marks").scale(1.0).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(c6))
        self.play(Create(SurroundingRectangle(c6, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the stand and the street ---
        self.next_band(8)
        b8_t = Tex("The stand and the street").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        k1 = Tex(r"Conversation 1 — the stand: flat? drains?").scale(1.0).shift(band_shift(8) + UP * 1.2)
        k1b = Tex(r"solid soil? water? winter sun? = SITE").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(k1))
        self.play(Write(k1b))
        self.wait(2.5)
        k2 = Tex(r"Conversation 2 — the street: near school,").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        k2b = Tex(r"clinic, rank, town? = SITUATION").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(k2))
        self.play(Write(k2b))
        self.wait(2.5)
        k3 = Tex(r"Karoo village on its borehole: wet-point").scale(0.95).shift(band_shift(8) + DOWN * 2.2)
        k4 = Tex(r"Homes above the floodplain: dry-point").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(k3))
        self.wait(2)
        self.play(Write(k4))
        self.play(Create(SurroundingRectangle(k4, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): scattered mealies or one pot ---
        self.next_band(9)
        b9_t = Tex("Scattered mealies or one pot").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        m1 = Tex(r"Ladder: farmstead, hamlet, village, town...").scale(1.0).shift(band_shift(9) + UP * 1.2)
        m1b = Tex(r"each step = more people AND more services").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(m1))
        self.play(Write(m1b))
        self.wait(2.5)
        m2 = Tex(r"Kernels flung across the floor = DISPERSED").scale(1.0).shift(band_shift(9) + DOWN * 0.5)
        m3 = Tex(r"Kernels dropped in one pot = NUCLEATED").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(m2))
        self.wait(2)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Scattered kernels: private land; one pot: shared").scale(0.95).shift(band_shift(9) + DOWN * 2.2)
        self.play(Write(m4))
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(2)
        m5 = Tex(r"One kind of work off the land = unifunctional").scale(0.95).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(m5))
        self.wait(3)

        # --- Band 10 (subtopic_7): reading a village like a taxi route ---
        self.next_band(10)
        b10_t = Tex("Reading a village like a taxi route").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        z1 = Tex(r"Ring of huts, kraal in the middle: ROUND").scale(0.95).shift(band_shift(10) + UP * 1.2)
        z2 = Tex(r"Every door facing the tar, one long line: LINEAR").scale(0.95).shift(band_shift(10) + UP * 0.4)
        z3 = Tex(r"Side road ends at the main road: T-SHAPED").scale(0.95).shift(band_shift(10) + DOWN * 0.4)
        z4 = Tex(r"Two roads cross, four arms build up: CROSSROAD").scale(0.95).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(z1))
        self.wait(2)
        self.play(Write(z2))
        self.wait(2)
        self.play(Write(z3))
        self.wait(2)
        self.play(Write(z4))
        self.wait(2)
        z5 = Tex(r"The junction is the magnet; the shape is filings").scale(0.95).shift(band_shift(10) + DOWN * 2.1)
        self.play(Write(z5))
        self.play(Create(SurroundingRectangle(z5, color=GREEN)))
        self.wait(2)
        z6 = Tex(r"Mealies = crops; kraals = stock; pine rows =").scale(0.95).shift(band_shift(10) + DOWN * 2.9)
        z6b = Tex(r"forestry; Kruger camp = conservation").scale(0.95).shift(band_shift(10) + DOWN * 3.6)
        self.play(Write(z6))
        self.play(Write(z6b))
        self.wait(4)
