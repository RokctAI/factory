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

# Band-layout whiteboard scene for "Droughts and Desertification: Causes,
# Effects, Management" (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier
# 5-7). Exporter-safe primitives only: the four deepening drought stages are
# a staircase of Rectangles, the desertification feedback loop is a cycle of
# Tex nodes joined by straight Arrows, and Day Zero's numbers are boxed
# MathTex. Add-only lifecycle; camera moves down band by band. Band time
# apportioned to subtopics.json (220/230/235/240/185/185/210 of 1505 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DroughtsDesertificationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): drought defined, four stages ---
        title = Tex("Droughts and Desertification").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d_wrong = Tex("Drought = low rainfall?").scale(1.05).shift(UP * 1.1)
        self.play(Write(d_wrong))
        self.play(Create(strike(d_wrong)))
        self.wait(2)
        d1 = Tex("Rainfall well below the LOCAL NORMAL —").scale(1.0).shift(UP * 0.2)
        d2 = Tex("250 mm is normal for Upington,").scale(0.95).shift(DOWN * 0.6)
        d3 = Tex("catastrophic for Durban").scale(0.95).shift(DOWN * 1.4)
        self.play(Write(d1))
        self.play(Write(d2))
        self.play(Write(d3))
        self.play(Create(SurroundingRectangle(d1, color=GREEN)))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the four deepening stages + causes ---
        self.next_band(1)
        b1_title = Tex("Four deepening stages").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        stages = [
            ("1 meteorological: the rains underperform", 1.5),
            ("2 agricultural: soil moisture fails crops", 0.7),
            ("3 hydrological: rivers, dams, boreholes sink", -0.1),
            ("4 socio-economic: supply $<$ demand", -0.9),
        ]
        for txt, y in stages:
            box = Rectangle(width=9.6, height=0.72).shift(band_shift(1) + UP * y)
            lab = Tex(txt).scale(0.8).shift(band_shift(1) + UP * y)
            self.play(Create(box), Write(lab))
            self.wait(1.2)
        c1 = Tex("Causes: strengthened subsidence, a stalling ITCZ,").scale(0.85).shift(band_shift(1) + DOWN * 2.0)
        c2 = Tex("a stubborn Kalahari High, El Ni\\~no (2015-16),").scale(0.85).shift(band_shift(1) + DOWN * 2.7)
        c3 = Tex("climate change — deepened by human demand").scale(0.85).shift(band_shift(1) + DOWN * 3.4)
        self.play(Write(c1))
        self.play(Write(c2))
        self.play(Write(c3))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): desertification and its chain ---
        self.next_band(2)
        b2_title = Tex("Desertification: land degradation").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        e1 = Tex("Not a desert advancing — productive land").scale(0.95).shift(band_shift(2) + UP * 1.2)
        e2 = Tex("dying in patches where people press hardest").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(e1))
        self.play(Write(e2))
        self.wait(2.5)
        e3 = Tex("Overgrazing; over-cultivation; deforestation;").scale(0.95).shift(band_shift(2) + DOWN * 0.5)
        e4 = Tex("poor irrigation $\\to$ salinisation —").scale(0.95).shift(band_shift(2) + DOWN * 1.3)
        e5 = Tex("behind all four: population pressure and poverty").scale(0.9).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(e3))
        self.wait(2)
        self.play(Write(e4))
        self.play(Write(e5))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): the feedback loop ---
        self.next_band(3)
        b3_title = Tex("The runaway loop").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        n1 = Tex("bare soil bakes hard").scale(0.85).shift(band_shift(3) + UP * 1.3)
        n2 = Tex("rain runs off: dongas").scale(0.85).shift(band_shift(3) + RIGHT * 3.6 + DOWN * 0.2)
        n3 = Tex("topsoil lost").scale(0.85).shift(band_shift(3) + DOWN * 1.7)
        n4 = Tex("less vegetation returns").scale(0.85).shift(band_shift(3) + LEFT * 3.6 + DOWN * 0.2)
        self.play(Write(n1))
        a1 = Arrow(band_shift(3) + RIGHT * 1.7 + UP * 1.1, band_shift(3) + RIGHT * 3.3 + UP * 0.2,
                   buff=0, color=RED, stroke_width=4)
        self.play(Create(a1), Write(n2))
        a2 = Arrow(band_shift(3) + RIGHT * 3.3 + DOWN * 0.6, band_shift(3) + RIGHT * 1.5 + DOWN * 1.6,
                   buff=0, color=RED, stroke_width=4)
        self.play(Create(a2), Write(n3))
        a3 = Arrow(band_shift(3) + LEFT * 1.5 + DOWN * 1.6, band_shift(3) + LEFT * 3.3 + DOWN * 0.6,
                   buff=0, color=RED, stroke_width=4)
        self.play(Create(a3), Write(n4))
        a4 = Arrow(band_shift(3) + LEFT * 3.3 + UP * 0.2, band_shift(3) + LEFT * 1.7 + UP * 1.1,
                   buff=0, color=RED, stroke_width=4)
        self.play(Create(a4))
        self.wait(2.5)
        s1 = Tex("Sahel: the world's warning region;").scale(0.9).shift(band_shift(3) + DOWN * 2.7)
        s2 = Tex("Karoo, Kalahari margins, old homelands here").scale(0.9).shift(band_shift(3) + DOWN * 3.4)
        self.play(Write(s1))
        self.play(Write(s2))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): effects on environment and people ---
        self.next_band(4)
        b4_title = Tex("Effects: the cascade").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        f1 = Tex("Environment: vegetation $\\to$ habitats $\\to$ soils").scale(0.9).shift(band_shift(4) + UP * 1.2)
        f2 = Tex("$\\to$ rivers to sand, dams to dead storage, dust").scale(0.9).shift(band_shift(4) + UP * 0.4)
        self.play(Write(f1))
        self.play(Write(f2))
        self.wait(2.5)
        f3 = Tex("People: crops fail, cattle die (2015-16: maize").scale(0.9).shift(band_shift(4) + DOWN * 0.5)
        f4 = Tex("imported), prices climb, farm jobs vanish,").scale(0.9).shift(band_shift(4) + DOWN * 1.3)
        f5 = Tex("drought migration swells settlements, conflict").scale(0.9).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(f3))
        self.play(Write(f4))
        self.wait(2)
        self.play(Write(f5))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): Day Zero, the numbers ---
        self.next_band(5)
        b5_title = Tex("Case study: Day Zero, 2018").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        z1 = Tex("Three failed winters 2015--2017;").scale(0.95).shift(band_shift(5) + UP * 1.2)
        z2 = Tex("dams toward 13\\%; a published cut-off date").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(z1))
        self.play(Write(z2))
        self.wait(2.5)
        z3 = MathTex(r"\approx 1\,200 \to 500 \text{ million litres a day}").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(z3))
        self.play(Create(SurroundingRectangle(z3, color=GREEN)))
        self.wait(2.5)
        z4 = Tex("Restrictions, steep tariffs, pressure management,").scale(0.9).shift(band_shift(5) + DOWN * 1.6)
        z5 = Tex("a relentless campaign — Day Zero never came").scale(0.9).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(z4))
        self.play(Write(z5))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the three management families ---
        self.next_band(6)
        b6_title = Tex("Management: three families").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        m1 = Tex("1. SEE IT COMING: satellites, GIS overlays,").scale(0.9).shift(band_shift(6) + UP * 1.2)
        m2 = Tex("sell stock early, drought-resistant crops").scale(0.9).shift(band_shift(6) + UP * 0.4)
        self.play(Write(m1))
        self.play(Write(m2))
        self.wait(2.5)
        m3 = Tex("2. USE LESS: drip irrigation, night watering,").scale(0.9).shift(band_shift(6) + DOWN * 0.5)
        m4 = Tex("mulch, fixed leaks, tariffs, desalination").scale(0.9).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(m3))
        self.play(Write(m4))
        self.wait(2.5)
        m5 = Tex("3. HEAL THE LAND: rotational grazing, contour").scale(0.9).shift(band_shift(6) + DOWN * 2.2)
        m6 = Tex("ploughing, check dams in dongas, windbreaks").scale(0.9).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(m5))
        self.play(Write(m6))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): the named programmes ---
        self.next_band(7)
        b7_title = Tex("Programmes that carry marks").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        p1 = Tex("Working for Water: teams clear thirsty alien").scale(0.95).shift(band_shift(7) + UP * 1.2)
        p2 = Tex("wattles, pines, eucalypts — water AND jobs").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(p1))
        self.play(Write(p2))
        self.play(Create(SurroundingRectangle(p2, color=GREEN)))
        self.wait(2.5)
        p3 = Tex("LandCare rehabilitates eroded communal land").scale(0.95).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(p3))
        self.wait(2)
        p4 = Tex("Great Green Wall: Senegal to Djibouti —").scale(0.95).shift(band_shift(7) + DOWN * 1.5)
        p5 = Tex("thousands of community restoration projects").scale(0.95).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(p4))
        self.play(Write(p5))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the rainfall bank account ---
        self.next_band(8)
        b8_title = Tex("The rainfall bank account").scale(1.15).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        k1 = Tex("Rain is the salary; drought is a salary far").scale(0.95).shift(band_shift(8) + UP * 1.3)
        k2 = Tex("below what THIS account was built on").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(k1))
        self.play(Write(k2))
        self.wait(2.5)
        k3 = Tex("Pay cut $\\to$ pantry $\\to$ savings $\\to$ debt:").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        k4 = Tex("meteorological, agricultural,").scale(0.95).shift(band_shift(8) + DOWN * 1.4)
        k5 = Tex("hydrological, socio-economic").scale(0.95).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(k3))
        self.wait(2)
        self.play(Write(k4))
        self.play(Write(k5))
        self.play(Create(SurroundingRectangle(k5, color=GREEN)))
        self.wait(2.5)
        k6 = Tex("Dice-loaders: stalled rain belt, El Ni\\~no,").scale(0.9).shift(band_shift(8) + DOWN * 3.1)
        k7 = Tex("climate change — and harder spending").scale(0.9).shift(band_shift(8) + DOWN * 3.8)
        self.play(Write(k6))
        self.play(Write(k7))
        self.wait(2.5)

        # --- Band 9 (subtopic_6): how to make a desert ---
        self.next_band(9)
        b9_title = Tex("How to make a desert").scale(1.2).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        r1 = Tex("Too many goats + ploughed-out fields +").scale(0.95).shift(band_shift(9) + UP * 1.3)
        r2 = Tex("chopped trees + salty irrigation = bald land").scale(0.95).shift(band_shift(9) + UP * 0.5)
        self.play(Write(r1))
        self.play(Write(r2))
        self.wait(2.5)
        r3 = Tex("Soil is hair on a scalp: shave it and rain").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        r4 = Tex("bounces, rips dongas, carries the soil away").scale(0.95).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(r3))
        self.play(Write(r4))
        self.wait(2.5)
        r5 = Tex("Less soil $\\to$ less grass $\\to$ more bare ground:").scale(0.95).shift(band_shift(9) + DOWN * 2.1)
        r6 = Tex("the spiral feeds itself — patch by patch").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(r5))
        self.play(Write(r6))
        self.play(Create(SurroundingRectangle(r6, color=GREEN)))
        self.wait(2)
        r7 = Tex("Sahel worldwide; Karoo and old homelands here").scale(0.9).shift(band_shift(9) + DOWN * 3.6)
        self.play(Write(r7))
        self.wait(2.5)

        # --- Band 10 (subtopic_7): Day Zero and the bucket brigade ---
        self.next_band(10)
        b10_title = Tex("Day Zero and the bucket brigade").scale(1.1).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        t1 = Tex("Dams at 13\\%, a date on the calendar,").scale(0.95).shift(band_shift(10) + UP * 1.3)
        t2 = Tex("25 litres — two buckets — per person").scale(0.95).shift(band_shift(10) + UP * 0.5)
        self.play(Write(t1))
        self.play(Write(t2))
        self.wait(2.5)
        t3 = Tex("The city halved its use; behaviour beat it").scale(0.95).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(t3))
        self.play(Create(SurroundingRectangle(t3, color=GREEN)))
        self.wait(2.5)
        t4 = Tex("Three moves for any answer: see it coming,").scale(0.95).shift(band_shift(10) + DOWN * 1.4)
        t5 = Tex("spend less, heal the land — with Working for").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        t6 = Tex("Water and the Great Green Wall as your names").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(t4))
        self.play(Write(t5))
        self.play(Write(t6))
        self.wait(3)
