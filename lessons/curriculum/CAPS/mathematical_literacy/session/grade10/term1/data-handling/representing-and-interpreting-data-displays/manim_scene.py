# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from manim import *

# BAND LAYOUT: sequential vertical bands, one frame-height each, camera moves
# down between teaching steps; nothing is faded out or overwritten. Only
# exporter-supported mobjects (Tex/MathTex, Line/Arrow, Rectangle, Dot,
# Circle) with write-only reveals — no sub-part transforms.
#
# Mirrors script.md across the seven subtopics of the duo (Part 1 — Expert:
# subtopics 1-4; Part 2 — Simplifier: 5-7); band time is proportional to
# subtopics.json. Diagrams (bar graph, histogram, pie quarter, line graph,
# truncated-axis trick) are built from primitives only.

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k."""
    return DOWN * BAND * k


def strike(m):
    """Diagonal cancellation stroke through a wrong line, teacher-style."""
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RepresentingInterpretingDataDisplaysSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): bar graph of the transport survey ---
        title = Tex("Representing and Interpreting Data Displays").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        sub0 = Tex("Bar graph: categorical data, gaps between bars").scale(1.0).shift(UP * 1.7)
        self.play(Write(sub0))
        self.wait(1.5)
        base_y = DOWN * 2.4
        y_ax = Arrow(base_y + LEFT * 3.4, base_y + LEFT * 3.4 + UP * 3.6, buff=0)
        x_ax = Arrow(base_y + LEFT * 3.4, base_y + RIGHT * 3.6, buff=0)
        y_lab = Tex("Learners").scale(0.8).shift(UP * 1.6 + LEFT * 3.2 + RIGHT * 0.0)
        self.play(Create(x_ax), Create(y_ax))
        self.play(Write(y_lab))
        bars = [("Walk", 90, 1.35), ("Taxi", 135, 2.025), ("Bus", 45, 0.675), ("Car", 30, 0.45)]
        for i, (name, val, h) in enumerate(bars):
            x = LEFT * 2.3 + RIGHT * (1.5 * i)
            bar = Rectangle(width=0.9, height=h).shift(base_y + x + UP * (h / 2))
            lab = Tex(name).scale(0.75).shift(base_y + x + DOWN * 0.35)
            num = MathTex(str(val)).scale(0.75).shift(base_y + x + UP * (h + 0.3))
            self.play(Create(bar), Write(lab), Write(num))
            self.wait(1.2)
        chk = Tex("Modal category: taxi — $\\tfrac{135}{300} = 45\\%$").scale(1.0).shift(DOWN * 3.35)
        self.play(Write(chk))
        self.wait(3)

        # --- Band 1 (subtopic_1): histogram — the bars touch ---
        self.next_band(1)
        b1_t = Tex("Histogram: continuous data, bars touch").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        hbase = band_shift(1) + DOWN * 2.0
        h_yax = Arrow(hbase + LEFT * 3.5, hbase + LEFT * 3.5 + UP * 3.2, buff=0)
        h_xax = Arrow(hbase + LEFT * 3.5, hbase + RIGHT * 3.5, buff=0)
        self.play(Create(h_xax), Create(h_yax))
        hbars = [("0", 8, 0.8), ("50", 15, 1.5), ("100", 21, 2.1), ("150", 10, 1.0), ("200", 6, 0.6)]
        for i, (edge, val, h) in enumerate(hbars):
            x = LEFT * 2.9 + RIGHT * (1.2 * i)
            bar = Rectangle(width=1.2, height=h).shift(hbase + x + UP * (h / 2))
            lab = MathTex(edge).scale(0.7).shift(hbase + x + LEFT * 0.6 + DOWN * 0.35)
            num = MathTex(str(val)).scale(0.75).shift(hbase + x + UP * (h + 0.3))
            self.play(Create(bar), Write(lab), Write(num))
            self.wait(1)
        h_last = MathTex("250").scale(0.7).shift(hbase + RIGHT * 3.1 + DOWN * 0.35)
        self.play(Write(h_last))
        b1_l1 = Tex("Modal class: R100 up to R150").scale(1.0).shift(band_shift(1) + UP * 1.3)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Under R100: $8 + 15 = 23$, about 38,3\\%").scale(1.0).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): pie chart — percentage to angle ---
        self.next_band(2)
        b2_t = Tex("Pie chart: percentage $\\times$ 3,6 = degrees").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        pie = Circle(radius=1.3).shift(band_shift(2) + LEFT * 3.6 + DOWN * 0.4)
        r1 = Line(band_shift(2) + LEFT * 3.6 + DOWN * 0.4,
                  band_shift(2) + LEFT * 3.6 + DOWN * 0.4 + UP * 1.3)
        r2 = Line(band_shift(2) + LEFT * 3.6 + DOWN * 0.4,
                  band_shift(2) + LEFT * 3.6 + DOWN * 0.4 + RIGHT * 1.3)
        p_lab = Tex("Housing 25\\% = 90$^\\circ$").scale(0.8).shift(band_shift(2) + LEFT * 3.6 + DOWN * 2.2)
        self.play(Create(pie))
        self.play(Create(r1), Create(r2))
        self.play(Write(p_lab))
        self.wait(2)
        b2_l1 = Tex("Income R12 000; shares total 100\\%").scale(0.95).shift(band_shift(2) + UP * 1.2 + RIGHT * 1.8)
        b2_l2 = MathTex(r"\text{Food: } 30 \times 3{,}6 = 108^\circ").scale(0.95).shift(band_shift(2) + UP * 0.4 + RIGHT * 1.8)
        b2_l3 = MathTex(r"\text{Transport: } 15 \times 3{,}6 = 54^\circ").scale(0.95).shift(band_shift(2) + DOWN * 0.4 + RIGHT * 1.8)
        b2_l4 = MathTex(r"\text{Savings: } 7 \times 3{,}6 = 25{,}2^\circ").scale(0.95).shift(band_shift(2) + DOWN * 1.2 + RIGHT * 1.8)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(1.5)
        self.play(Write(b2_l3))
        self.wait(1.5)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_chk = Tex("Check: all angles total 360$^\\circ$ — compulsory").scale(1.0).shift(band_shift(2) + DOWN * 3.1)
        self.play(Write(b2_chk))
        self.play(Create(SurroundingRectangle(b2_chk, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): angle back to rands, and the limits ---
        self.next_band(3)
        b3_t = Tex("From angle back to rands").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"\frac{54^\circ}{360^\circ} = 0{,}15 = 15\%").scale(1.1).shift(band_shift(3) + UP * 1.0)
        b3_l2 = Tex("15\\% of R12 000 = R1 800 on transport").scale(1.05).shift(band_shift(3) + UP * 0.0)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = Tex("Food: $\\tfrac{108}{360} = 0{,}30$ — R3 600").scale(1.05).shift(band_shift(3) + DOWN * 1.0)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("Pie charts show proportions, not rands;").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        b3_l5 = Tex("never compare two pies with different totals").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l4))
        self.wait(1.5)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the winter electricity line graph ---
        self.next_band(4)
        b4_t = Tex("Broken-line graph: units per month").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        gbase = band_shift(4) + DOWN * 2.2 + LEFT * 3.4
        g_yax = Arrow(gbase, gbase + UP * 3.6, buff=0)
        g_xax = Arrow(gbase, gbase + RIGHT * 6.8, buff=0)
        self.play(Create(g_xax), Create(g_yax))
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
        units = [250, 240, 260, 310, 420, 480]
        pts = []
        for i, (m, u) in enumerate(zip(months, units)):
            p = gbase + RIGHT * (0.6 + 1.1 * i) + UP * ((u - 180) / 100.0)
            pts.append(p)
            d = Dot(p, radius=0.06)
            lab = Tex(m).scale(0.65).shift(gbase + RIGHT * (0.6 + 1.1 * i) + DOWN * 0.3)
            num = MathTex(str(u)).scale(0.65).shift(p + UP * 0.35)
            self.play(Create(d), Write(lab), Write(num))
            if i > 0:
                self.play(Create(Line(pts[i - 1], p)), run_time=0.5)
            self.wait(0.8)
        b4_note = Tex("Flat through summer, climbing into winter").scale(0.95).shift(band_shift(4) + UP * 1.4)
        self.play(Write(b4_note))
        self.wait(3)

        # --- Band 5 (subtopic_3): reading and pricing the line ---
        self.next_band(5)
        b5_t = Tex("Read it, then price it").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("Max: 480 (Jun) \\quad Min: 240 (Feb)").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"\text{Apr--May: } 420 - 310 = 110 \text{ units}").scale(1.05).shift(band_shift(5) + UP * 0.2)
        b5_l3 = Tex("vs May--Jun's 60 — steepest is Apr--May").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = MathTex(r"480 - 250 = 230; \;\; \frac{230}{250} = 0{,}92 = 92\%").scale(1.0).shift(band_shift(5) + DOWN * 1.5)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("June: $480 \\times$ R2,80 = R1 344,00").scale(1.05).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): choosing a display ---
        self.next_band(6)
        b6_t = Tex("Choosing the right display").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex("Categories to compare — bar graph").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("Grouped continuous data — histogram").scale(1.0).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("Parts of one whole — pie chart").scale(1.0).shift(band_shift(6) + DOWN * 0.4)
        b6_l4 = Tex("Change over time — line graph").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(1.5)
        b6_l5 = Tex("Honest graph: title, axis labels, units,").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        b6_l6 = Tex("even scale, source").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): the truncated axis trick ---
        self.next_band(7)
        b7_t = Tex("The misleading graph: truncated axis").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        tbase = band_shift(7) + DOWN * 1.6 + LEFT * 3.0
        t_yax = Arrow(tbase, tbase + UP * 2.6, buff=0)
        t_xax = Line(tbase, tbase + RIGHT * 3.2)
        t_zero = MathTex("400").scale(0.7).shift(tbase + LEFT * 0.5)
        self.play(Create(t_xax), Create(t_yax), Write(t_zero))
        bar_may = Rectangle(width=0.8, height=0.4).shift(tbase + RIGHT * 1.0 + UP * 0.2)
        bar_jun = Rectangle(width=0.8, height=1.6).shift(tbase + RIGHT * 2.4 + UP * 0.8)
        l_may = Tex("May 420").scale(0.7).shift(tbase + RIGHT * 1.0 + DOWN * 0.35)
        l_jun = Tex("Jun 480").scale(0.7).shift(tbase + RIGHT * 2.4 + DOWN * 0.35)
        self.play(Create(bar_may), Write(l_may))
        self.play(Create(bar_jun), Write(l_jun))
        self.wait(2)
        b7_claim = Tex("``Use quadruples''").scale(1.0).shift(band_shift(7) + UP * 1.0 + RIGHT * 2.2)
        self.play(Write(b7_claim))
        self.play(Create(strike(b7_claim)))
        self.wait(2)
        b7_l1 = MathTex(r"\frac{60}{420} \approx 0{,}143 = 14{,}3\%").scale(1.05).shift(band_shift(7) + DOWN * 0.2 + RIGHT * 2.2)
        self.play(Write(b7_l1))
        self.play(Create(SurroundingRectangle(b7_l1, color=GREEN)))
        self.wait(2)
        b7_l2 = Tex("Answer: feature, effect, correct number").scale(1.0).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(b7_l2))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): bars with gaps, bars that touch ---
        self.next_band(8)
        b8_t = Tex("Bars with gaps, bars that touch").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Piles of different kinds — leave gaps:").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("Walk 90, taxi 135, bus 45, car 30 — 300").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("Taxi is tallest: $\\tfrac{135}{300} = 0{,}45 = 45\\%$").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex("Rands run in a line — bands touch").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        b8_l5 = Tex("Test: words below = gaps; numbers = touch").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l4))
        self.wait(2)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): slices of the same plate ---
        self.next_band(9)
        b9_t = Tex("Slices of the same plate").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("R12 000 a month, one plateful:").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("Housing 25\\% = R3 000; food 30\\% = R3 600").scale(1.0).shift(band_shift(9) + UP * 0.4)
        b9_l3 = Tex("Transport R1 800; lights R1 200; school R960").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = MathTex(r"1\% = 3{,}6^\circ: \;\; 30 \times 3{,}6 = 108^\circ").scale(1.0).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex("A pie shows shares — find the total first").scale(1.0).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the winter line and the lying graph ---
        self.next_band(10)
        b10_t = Tex("The winter line, and the graph that lies").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Flat in summer, climbing into winter").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("Steepest: Apr to May, up 110 units").scale(1.0).shift(band_shift(10) + UP * 0.4)
        b10_l3 = Tex("June: $480 \\times$ R2,80 = R1 344,00").scale(1.0).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(b10_l1))
        self.wait(2)
        self.play(Write(b10_l2))
        self.wait(2)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2)
        b10_l4 = Tex("Axis cut at 400 makes 14\\% look like 4$\\times$").scale(1.0).shift(band_shift(10) + DOWN * 1.4)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("Check: scale start, even gaps, labels, total").scale(0.95).shift(band_shift(10) + DOWN * 2.3)
        self.play(Write(b10_l5))
        self.wait(4)
