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

# Band-layout whiteboard scene for the Representing Data with Graphs session
# duo. One band per teaching beat, camera-only transitions, add-only
# lifecycle. Exporter-supported mobjects only: bars are Rectangles, the line
# graph is a chain of Lines with Dots, axes are Arrows. Band time apportioned
# to subtopics.json (220/220/220/270/180/185/185 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RepresentingDataWithGraphsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): data arrives in three shapes ---
        title = Tex("Representing Data with Graphs").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Categories with counts $\\Rightarrow$ BAR graph").scale(1.05).shift(UP * 1.0)
        b0_l2 = Tex("(pies: chicken 32, beef 24, veg 16, cheese 8)").scale(0.9).shift(UP * 0.3)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Numbers grouped in intervals $\\Rightarrow$ HISTOGRAM").scale(0.95).shift(DOWN * 0.6)
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_l4 = Tex("A quantity over time $\\Rightarrow$ LINE graph").scale(1.05).shift(DOWN * 1.5)
        self.play(Write(b0_l4))
        self.wait(2.5)
        b0_l5 = Tex("Shares of a whole $\\Rightarrow$ PIE — read, never drawn").scale(0.95).shift(DOWN * 2.4)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_2): the bar graph, drawn ---
        self.next_band(1)
        b1_t = Tex("Pie sales by type, one week").scale(1.1).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_t))
        self.wait(1.5)
        org = band_shift(1) + DOWN * 2.4 + LEFT * 4.8
        x_ax = Arrow(org, org + RIGHT * 8.8, buff=0, stroke_width=4)
        y_ax = Arrow(org, org + UP * 4.4, buff=0, stroke_width=4)
        self.play(Create(x_ax), Create(y_ax))
        y_lab = Tex("pies sold").scale(0.75).shift(org + UP * 4.1 + RIGHT * 1.4)
        self.play(Write(y_lab))
        self.wait(1)
        # heights: 32->3.2, 24->2.4, 16->1.6, 8->0.8 (scale 0.1/unit)
        bar_c = Rectangle(width=1.2, height=3.2, color=BLUE).shift(org + RIGHT * 1.5 + UP * 1.6)
        bar_b = Rectangle(width=1.2, height=2.4, color=ORANGE).shift(org + RIGHT * 3.5 + UP * 1.2)
        bar_v = Rectangle(width=1.2, height=1.6, color=PURPLE).shift(org + RIGHT * 5.5 + UP * 0.8)
        bar_k = Rectangle(width=1.2, height=0.8, color=GREEN).shift(org + RIGHT * 7.5 + UP * 0.4)
        self.play(Create(bar_c))
        lab_c = Tex("chicken 32").scale(0.75).shift(org + RIGHT * 1.5 + UP * 3.55)
        self.play(Write(lab_c))
        self.play(Create(bar_b))
        lab_b = Tex("beef 24").scale(0.75).shift(org + RIGHT * 3.5 + UP * 2.75)
        self.play(Write(lab_b))
        self.play(Create(bar_v))
        lab_v = Tex("veg 16").scale(0.75).shift(org + RIGHT * 5.5 + UP * 1.95)
        self.play(Write(lab_v))
        self.play(Create(bar_k))
        lab_k = Tex("cheese 8").scale(0.75).shift(org + RIGHT * 7.5 + UP * 1.15)
        self.play(Write(lab_k))
        self.wait(2)
        b1_note = Tex("Gaps: the categories are separate islands").scale(0.9).shift(band_shift(1) + UP * 1.7 + RIGHT * 2.2)
        self.play(Write(b1_note))
        self.wait(3)

        # --- Band 2 (subtopic_2): the five parts markers check ---
        self.next_band(2)
        b2_t = Tex("The five parts of a bar graph").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex("1. Title: what, where, when").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("2. Category axis: one label per bar").scale(1.0).shift(band_shift(2) + UP * 0.2)
        b2_l3 = Tex("3. Number axis: starts at 0, EQUAL steps").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = Tex("4. Bars: equal width, equal gaps").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        b2_l5 = Tex("5. Check: read each bar back to the table").scale(1.0).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): the histogram, bars touching ---
        self.next_band(3)
        b3_t = Tex("Science marks, grouped in tens").scale(1.1).shift(band_shift(3) + UP * 2.6)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_check = MathTex(r"3 + 6 + 9 + 14 + 8 = 40 \; \checkmark").scale(1.0).shift(band_shift(3) + UP * 1.8)
        self.play(Write(b3_check))
        self.wait(2)
        org3 = band_shift(3) + DOWN * 2.6 + LEFT * 4.6
        base3 = Line(org3 + LEFT * 0.4, org3 + RIGHT * 8.6)
        self.play(Create(base3))
        # frequencies 3,6,9,14,8 -> heights x0.24: 0.72, 1.44, 2.16, 3.36, 1.92; touching, width 1.6
        h_vals = [(3, 0.72), (6, 1.44), (9, 2.16), (14, 3.36), (8, 1.92)]
        for i, (freq, h) in enumerate(h_vals):
            bar = Rectangle(width=1.6, height=h, color=TEAL).shift(org3 + RIGHT * (0.8 + 1.6 * i) + UP * h / 2)
            lab = Tex(str(freq)).scale(0.75).shift(org3 + RIGHT * (0.8 + 1.6 * i) + UP * (h + 0.35))
            self.play(Create(bar), Write(lab), run_time=0.8)
        int_lab = Tex("0--9 \\; 10--19 \\; 20--29 \\; 30--39 \\; 40--49").scale(0.8).shift(org3 + RIGHT * 4.1 + DOWN * 0.5)
        self.play(Write(int_lab))
        self.wait(2)
        b3_note = Tex("NO gaps — the intervals tile the number line").scale(0.9).shift(band_shift(3) + UP * 0.9 + RIGHT * 1.6)
        self.play(Write(b3_note))
        self.wait(3)

        # --- Band 4 (subtopic_3): why they touch, and the modal class ---
        self.next_band(4)
        b4_t = Tex("Why must the bars touch?").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("A gap would claim marks nobody could score —").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex("29 is followed by 30; there is no empty ground").scale(1.0).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("Bar graph gaps: separate categories — true").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = Tex("Histogram touching: continuous line — true").scale(1.0).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex("Modal class: 30--39, with 14 of the 40 learners").scale(1.0).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): the takings line graph ---
        self.next_band(5)
        b5_t = Tex("Takings per day: the broken line").scale(1.1).shift(band_shift(5) + UP * 2.6)
        self.play(Write(b5_t))
        self.wait(1.5)
        org5 = band_shift(5) + DOWN * 2.6 + LEFT * 4.8
        x5 = Arrow(org5, org5 + RIGHT * 9.0, buff=0, stroke_width=4)
        y5 = Arrow(org5, org5 + UP * 4.6, buff=0, stroke_width=4)
        self.play(Create(x5), Create(y5))
        y5_lab = Tex("rand").scale(0.75).shift(org5 + UP * 4.3 + RIGHT * 0.9)
        self.play(Write(y5_lab))
        # values 340,430,120,450,490 scaled /130 -> 2.62,3.31,0.92,3.46,3.77
        pts = [org5 + RIGHT * (1.0 + 1.7 * i) + UP * h
               for i, h in enumerate([2.62, 3.31, 0.92, 3.46, 3.77])]
        dots = VGroup(*[Dot(p, color=RED) for p in pts])
        self.play(Create(dots))
        for a, b in zip(pts, pts[1:]):
            self.play(Create(Line(a, b, color=YELLOW, stroke_width=5)), run_time=0.6)
        day_lab = Tex("Mon 340 \\; Tue 430 \\; Wed 120 \\; Thu 450 \\; Fri 490").scale(0.8).shift(org5 + RIGHT * 4.4 + DOWN * 0.5)
        self.play(Write(day_lab))
        self.wait(2)
        b5_note = Tex("Rising week — with a Wednesday cliff-dive").scale(0.9).shift(band_shift(5) + UP * 1.6 + RIGHT * 2.0)
        self.play(Write(b5_note))
        self.wait(3)

        # --- Band 6 (subtopic_4): reading the pie ---
        self.next_band(6)
        b6_t = Tex("Reading the pie: share $\\times$ whole").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Veg } 20\% \text{ of } 80 = 16 \text{ pies}").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"\text{Next week: chicken } 40\% \text{ of } 150 = 60").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"\text{Angle: } 0{,}40 \times 360^\circ = 144^\circ").scale(1.0).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = MathTex(r"144 + 108 + 72 + 36 = 360 \; \checkmark").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        b6_l5 = Tex("Shares total 100\\%; angles total 360$^\\circ$").scale(0.95).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): piles, buckets and journeys ---
        self.next_band(7)
        b7_t = Tex("Piles, buckets and journeys").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("Piles: separate pie types $\\Rightarrow$ bars with gaps").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex("Buckets: marks scooped rim to rim $\\Rightarrow$").scale(1.0).shift(band_shift(7) + UP * 0.2)
        b7_l3 = Tex("histogram bars that touch").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l2))
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex("Journeys: the cash box checked daily $\\Rightarrow$ line graph").scale(0.95).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("The pie is just the piles squashed into one tart").scale(0.95).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): the ruler rules ---
        self.next_band(8)
        b8_t = Tex("A graph is a promise: equal distance,").scale(1.1).shift(band_shift(8) + UP * 2.4)
        b8_t2 = Tex("equal amount").scale(1.1).shift(band_shift(8) + UP * 1.7)
        self.play(Write(b8_t))
        self.play(Write(b8_t2))
        self.wait(2)
        b8_l1 = Tex("1. Start at 0, climb in equal steps (50s to 500)").scale(0.95).shift(band_shift(8) + UP * 0.7)
        b8_l2 = Tex("2. Label everything — title and both axes").scale(0.95).shift(band_shift(8) + DOWN * 0.2)
        b8_l3 = Tex("3. Equal widths; only HEIGHT speaks").scale(0.95).shift(band_shift(8) + DOWN * 1.1)
        b8_l4 = Tex("4. Transcribe, then audit against the table").scale(0.95).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): the Wednesday dip, in three layers ---
        self.next_band(9)
        b9_t = Tex("The Wednesday dip, read in three layers").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = MathTex(r"\text{Facts: range } 490 - 120 = \text{R}370").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"\text{Total: } 340 + 430 + 120 + 450 + 490 = \text{R}1\;830").scale(0.95).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Trend: rising — Friday stands 150 above Monday").scale(0.95).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("Exception + reason: power cut, cold warmers,").scale(0.95).shift(band_shift(9) + DOWN * 1.7)
        b9_l5 = Tex("no hot pies to sell").scale(0.95).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(2)
        b9_l6 = Tex("The joining line is a guide for the eye, not data").scale(0.9).shift(band_shift(9) + DOWN * 3.2)
        self.play(Write(b9_l6))
        self.wait(4)
