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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex/MathTex keep the export to
# the allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (220/230/230/230/190/190/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


def table(rows, origin, col_w=1.3, row_h=0.55, scale=0.55):
    """Plain text grid; rows is a list of lists of strings."""
    g = VGroup()
    for i, row in enumerate(rows):
        for j, cell in enumerate(row):
            g.add(Tex(cell).scale(scale).move_to(origin + RIGHT * col_w * j + DOWN * row_h * i))
    return g


def number_line_dots(values, origin, unit=0.11, color=WHITE):
    """Dots along a horizontal axis at the given values (stacked when repeated)."""
    g = VGroup()
    seen = {}
    for v in values:
        k = seen.get(v, 0)
        seen[v] = k + 1
        g.add(Dot(origin + RIGHT * unit * v + UP * 0.22 * k, radius=0.07, color=color))
    return g


class CentralTendencySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): organising
        title = Tex("Organise first: order, count, cross-tabulate").scale(1.05).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        raw = Tex("Raw: 12, 60, 10, 15, 8, 12, 20, 5, 25, 10, 18, 12").scale(0.72).shift(UP * 2.2)
        ordered = Tex("Ordered: 5, 8, 10, 10, 12, 12, 12, 15, 18, 20, 25, 60").scale(0.72).shift(UP * 1.5)
        self.play(Write(raw))
        self.wait(1.5)
        self.play(Write(ordered))
        self.wait(2)
        tb = table([["size", "4", "5", "6", "7", "8"], ["count", "3", "7", "8", "5", "2"]], np.array([-6.0, 0.4, 0]), col_w=0.9)
        self.play(Write(tb))
        self.play(Write(Tex("check: $3 + 7 + 8 + 5 + 2 = 25$").scale(0.6).move_to(np.array([-3.8, -0.5, 0]))))
        tw = table([["", "walk", "taxi", "car", "total"], ["boys", "18", "9", "3", "30"], ["girls", "15", "12", "3", "30"], ["total", "33", "21", "6", "60"]], np.array([1.4, 0.4, 0]), col_w=1.1, row_h=0.5)
        self.play(Write(tw))
        self.wait(2)
        sl = Tex("Stem-and-leaf: 2 $|$ 3 \\quad 3 $|$ 1 5 5 8 \\quad 4 $|$ 0 2 4 5 7").scale(0.7).shift(DOWN * 2.3)
        self.play(Write(sl))
        self.wait(4)

        # --- Band 1 (subtopic_2): three measures
        self.next_band(1)
        h1 = Tex("Mean, median, mode").scale(1.05).move_to(band_shift(1) + UP * 3.2)
        self.play(Write(h1))
        m1 = MathTex(r"\text{mean} = \frac{207}{12} = 17.25").scale(0.9).move_to(band_shift(1) + UP * 2.1)
        m2 = Tex("median: 6th and 7th of 12 are 12 and 12, so 12").scale(0.75).move_to(band_shift(1) + UP * 1.3)
        m3 = Tex("mode: 12 (three times)").scale(0.75).move_to(band_shift(1) + UP * 0.6)
        m4 = MathTex(r"\text{table mean} = \frac{12 + 35 + 48 + 35 + 16}{25} = \frac{146}{25} = 5.84").scale(0.8).move_to(band_shift(1) + DOWN * 0.3)
        m5 = Tex("median of 25: the 13th; cumulative 3, 10, 18, so size 6. Mode: 6.").scale(0.7).move_to(band_shift(1) + DOWN * 1.1)
        m6 = Tex("Backwards: mean 20 of five means sum 100; $100 - 80 = 20$. Combined: $3300 \\div 50 = 66$.").scale(0.66).move_to(band_shift(1) + DOWN * 1.9)
        for m in (m1, m2, m3, m4, m5, m6):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(m4, color=YELLOW)))
        self.wait(3)

        # --- Band 2 (subtopic_3): range and outliers
        self.next_band(2)
        h2 = Tex("Range, extremes, outliers").scale(1.05).move_to(band_shift(2) + UP * 3.2)
        self.play(Write(h2))
        axis = Line(band_shift(2) + LEFT * 6.4 + DOWN * 1.6, band_shift(2) + RIGHT * 1.2 + DOWN * 1.6, color=GREY, stroke_width=3)
        self.play(Create(axis))
        pts = number_line_dots([5, 8, 10, 10, 12, 12, 12, 15, 18, 20, 25, 60], band_shift(2) + LEFT * 6.4 + DOWN * 1.4)
        self.play(Create(pts))
        self.play(pts[-1].animate.set_color(RED))
        self.play(Write(Tex("outlier").scale(0.55).next_to(pts[-1], UP, buff=0.15)))
        r1 = Tex("Extremes 5 and 60; range $60 - 5 = 55$.").scale(0.75).move_to(band_shift(2) + UP * 2.1 + RIGHT * 1.6)
        r2 = Tex("Same centre, different spread: 48 to 52 has range 4; 30 to 70 has range 40.").scale(0.68).move_to(band_shift(2) + UP * 1.3 + RIGHT * 1.6)
        r3 = Tex("Remove the 60: mean 17.25 to 13.36, range 55 to 20.").scale(0.72).move_to(band_shift(2) + UP * 0.5 + RIGHT * 1.6)
        r4 = Tex("Median stays 12. Mode stays 12.").scale(0.78).move_to(band_shift(2) + DOWN * 0.3 + RIGHT * 1.6)
        for m in (r1, r2, r3, r4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(r4, color=YELLOW)))
        self.wait(3)

        # --- Band 3 (subtopic_4): choosing
        self.next_band(3)
        h3 = Tex("Choosing the measure").scale(1.05).move_to(band_shift(3) + UP * 3.2)
        self.play(Write(h3))
        c1 = Tex("Mean: symmetrical, no outliers (class test marks).").scale(0.75).move_to(band_shift(3) + UP * 2.1)
        c2 = Tex("Median: outliers or skew (incomes, house prices, spending).").scale(0.75).move_to(band_shift(3) + UP * 1.3)
        c3 = Tex("Mode: categorical data or the most common value (shoe sizes to stock).").scale(0.72).move_to(band_shift(3) + UP * 0.5)
        c4 = MathTex(r"8 \times 6000 + 40000 = 88000;\quad \text{mean} = 9777.78,\ \text{median} = 6000").scale(0.75).move_to(band_shift(3) + DOWN * 0.4)
        c5 = Tex("Recommend: the median, because 60 is an outlier pulling the mean to 17.25.").scale(0.7).move_to(band_shift(3) + DOWN * 1.3)
        for m in (c1, c2, c3, c4, c5):
            self.play(Write(m))
            self.wait(2.5)
        self.play(Create(SurroundingRectangle(c5, color=YELLOW)))
        self.wait(3)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        h4 = Tex("Error museum").scale(1.05).move_to(band_shift(4) + UP * 3.2)
        self.play(Write(h4))
        e1 = Tex("Median from the unordered list").scale(0.8).move_to(band_shift(4) + UP * 1.8)
        e2 = MathTex(r"\text{shoe mean} = \frac{4 + 5 + 6 + 7 + 8}{5} = 6").scale(0.85).move_to(band_shift(4) + UP * 0.6)
        e3 = MathTex(r"\text{combined mean} = \frac{60 + 75}{2} = 67.5").scale(0.85).move_to(band_shift(4) + DOWN * 0.6)
        for m in (e1, e2, e3):
            self.play(Write(m))
            self.wait(1.5)
            self.play(Create(strike(m)))
            self.wait(1.5)
        fix = Tex("Order first; weight by frequency; combine through the total; name the outlier.").scale(0.7).move_to(band_shift(4) + DOWN * 2.2)
        self.play(Write(fix))
        self.play(Create(SurroundingRectangle(fix, color=GREEN)))
        self.wait(5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): line up
        self.next_band(5)
        h5 = Tex("Line them up first").scale(1.05).move_to(band_shift(5) + UP * 3.2)
        self.play(Write(h5))
        heights = [5, 8, 10, 10, 12, 12, 12, 15, 18, 20, 25, 60]
        base = band_shift(5) + LEFT * 6.2 + DOWN * 2.6
        bars = VGroup(*[Rectangle(width=0.4, height=0.06 * h, color=BLUE, fill_opacity=0.6).move_to(base + RIGHT * 0.6 * i + UP * 0.03 * h) for i, h in enumerate(heights)])
        self.play(Create(bars), run_time=2)
        self.play(Write(Tex("5, 8, 10, 10, 12, 12, 12, 15, 18, 20, 25, 60").scale(0.6).move_to(base + RIGHT * 3.3 + DOWN * 0.4)))
        l1 = Tex("Smallest, biggest, the crowd, and the one far off.").scale(0.75).move_to(band_shift(5) + UP * 2.0 + RIGHT * 2.2)
        l2 = Tex("Many repeats: count them in a table and check the total.").scale(0.72).move_to(band_shift(5) + UP * 1.1 + RIGHT * 2.2)
        l3 = Tex("Two things at once: a two-way table, add across and down.").scale(0.72).move_to(band_shift(5) + UP * 0.2 + RIGHT * 2.2)
        for m in (l1, l2, l3):
            self.play(Write(m))
            self.wait(2.8)
        self.wait(4)

        # --- Band 6 (subtopic_6): three middles
        self.next_band(6)
        h6 = Tex("Three kinds of middle").scale(1.05).move_to(band_shift(6) + UP * 3.2)
        self.play(Write(h6))
        t1 = Tex("Mean: share it all out. $207 \\div 12 = 17.25$.").scale(0.78).move_to(band_shift(6) + UP * 2.0)
        t2 = Tex("Median: the person in the middle of the line. 12 and 12, so 12.").scale(0.75).move_to(band_shift(6) + UP * 1.1)
        t3 = Tex("Mode: the most common value. 12, three times. Works for words too.").scale(0.72).move_to(band_shift(6) + UP * 0.2)
        t4 = Tex("From a table: value times count, then share: $146 \\div 25 = 5.84$. 13th in line: size 6.").scale(0.68).move_to(band_shift(6) + DOWN * 0.7)
        t5 = Tex("Backwards: mean 20 of five is a sum of 100. Classes 60 and 75 combine to 66, not 67.5.").scale(0.66).move_to(band_shift(6) + DOWN * 1.6)
        for m in (t1, t2, t3, t4, t5):
            self.play(Write(m))
            self.wait(2.5)
        self.play(Create(SurroundingRectangle(t2, color=YELLOW)))
        self.wait(3)

        # --- Band 7 (subtopic_7): the giant
        self.next_band(7)
        h7 = Tex("The giant who spoils the average").scale(1.05).move_to(band_shift(7) + UP * 3.2)
        self.play(Write(h7))
        gb = band_shift(7) + LEFT * 6.2 + DOWN * 2.4
        figs = VGroup(*[Line(gb + RIGHT * 0.5 * i, gb + RIGHT * 0.5 * i + UP * 0.9, color=WHITE, stroke_width=5) for i in range(8)])
        giant = Line(gb + RIGHT * 4.0, gb + RIGHT * 4.0 + UP * 4.2, color=RED, stroke_width=6)
        self.play(Create(figs), Create(giant))
        self.play(Write(Tex("R6 000 each").scale(0.55).move_to(gb + RIGHT * 1.75 + DOWN * 0.3)), Write(Tex("R40 000").scale(0.55).move_to(gb + RIGHT * 4.0 + DOWN * 0.3)))
        g1 = Tex("Mean R9 777.78: true and misleading. Median R6 000: what a worker earns.").scale(0.68).move_to(band_shift(7) + UP * 2.0 + RIGHT * 2.0)
        g2 = Tex("Tuck shop giant 60: mean 17.25 to 13.36, range 55 to 20; median stays 12.").scale(0.68).move_to(band_shift(7) + UP * 1.1 + RIGHT * 2.0)
        g3 = Tex("Mean for fair, bunched data; median when there are giants; mode for words.").scale(0.68).move_to(band_shift(7) + UP * 0.2 + RIGHT * 2.0)
        g4 = Tex("Line them up, three middles, watch the giant.").scale(0.85).move_to(band_shift(7) + DOWN * 0.9 + RIGHT * 2.0)
        for m in (g1, g2, g3, g4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(g4, color=YELLOW)))
        self.wait(6)
