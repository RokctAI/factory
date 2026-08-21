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

# Band-layout whiteboard scene for "Drawing and Reading Market Graphs"
# (grade 10, term 2 — IEB catalogue). One band per teaching beat; camera moves
# down, earlier work stays. The schedule runs R5-R25 against quantities
# 50-250; equilibrium at R15/150; excess supply of 100 units read at R20.
# All graph work is hand-built from exporter-safe primitives: Arrows for axes,
# chained Lines for curves, Dots for plotted points, DashedLines for readings.
#
# Subtopic shares (subtopics.json, total 1450 s):
# 190/230/190/270/190/190/190 — subtopic_4 (the R20 reading) is the
# heavyweight and gets two bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def chain(points, color, width=5):
    return VGroup(*[Line(points[i], points[i + 1], color=color,
                         stroke_width=width) for i in range(len(points) - 1)])


# Grid mapping for the schedule: quantity 50->0.7, +50 -> +1.5;
# price R5->0.7, +R5 -> +0.9 (relative to each band's origin).
D_OFFSETS = [(6.7, 0.7), (5.2, 1.6), (3.7, 2.5), (2.2, 3.4), (0.7, 4.3)]
S_OFFSETS = [(0.7, 0.7), (2.2, 1.6), (3.7, 2.5), (5.2, 3.4), (6.7, 4.3)]


class DrawingReadingMarketGraphsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def axes(self, origin):
        x_axis = Arrow(origin, origin + RIGHT * 8.2, buff=0, stroke_width=4)
        y_axis = Arrow(origin, origin + UP * 5.2, buff=0, stroke_width=4)
        p_lab = Tex("Price (R)").scale(0.7).next_to(y_axis.get_end(), UP, buff=0.12)
        q_lab = Tex("Quantity").scale(0.7).next_to(x_axis.get_end(), DOWN, buff=0.12)
        return x_axis, y_axis, p_lab, q_lab

    def pts(self, origin, offsets):
        return [origin + RIGHT * dx + UP * dy for dx, dy in offsets]

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the schedule ---
        title = Tex("Drawing and Reading Market Graphs").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        rows = [
            r"R5:\quad D 250 \quad S 50",
            r"R10:\quad D 200 \quad S 100",
            r"R15:\quad D 150 \quad S 150",
            r"R20:\quad D 100 \quad S 200",
            r"R25:\quad D 50 \quad S 250",
        ]
        row_mobs = []
        for i, row in enumerate(rows):
            m = Tex(row).scale(0.9).shift(UP * (1.6 - i * 0.8))
            row_mobs.append(m)
            self.play(Write(m), run_time=0.8)
        self.wait(2)
        b0a = Tex(r"One row $=$ one price, two plans").scale(0.95).shift(DOWN * 2.6)
        self.play(Write(b0a))
        self.wait(3)

        # --- Band 1 (subtopic_1): interrogate the table ---
        self.next_band(1)
        b1t = Tex("Question the table first").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        b1a = Tex(r"D column: 250 $\to$ 50 as price climbs —").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1b = Tex(r"law of demand: a downhill curve coming").scale(1.0).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1a))
        self.play(Write(b1b))
        self.wait(2.5)
        b1c = Tex(r"S column: 50 $\to$ 250 — law of supply:").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        b1d = Tex(r"an uphill curve coming").scale(1.0).shift(band_shift(1) + DOWN * 1.1)
        self.play(Write(b1c))
        self.play(Write(b1d))
        self.wait(2.5)
        b1e = Tex(r"R15: both columns say 150 —").scale(1.0).shift(band_shift(1) + DOWN * 2.0)
        b1f = Tex(r"flag that row; the graph pivots on it").scale(1.0).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1e))
        self.play(Write(b1f))
        self.play(Create(SurroundingRectangle(VGroup(b1e, b1f), color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the three setup rules ---
        self.next_band(2)
        b2t = Tex("Three rules of setup").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        b2a = Tex(r"1. Price UP the side, quantity ALONG").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2b = Tex(r"the bottom — always").scale(1.0).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2a))
        self.play(Write(b2b))
        self.wait(2)
        b2c = Tex(r"2. Even steps: 5s for prices, 50s for").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        b2d = Tex(r"quantities — uneven scales bend truth").scale(1.0).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2c))
        self.play(Write(b2d))
        self.wait(2.5)
        b2e = Tex(r"3. Name everything: axes, heading,").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
        b2f = Tex(r"D and S on the lines themselves").scale(1.0).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2e))
        self.play(Write(b2f))
        self.play(Create(SurroundingRectangle(VGroup(b2e, b2f), color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): plotting both curves ---
        self.next_band(3)
        b3t = Tex("Row by row onto the frame").scale(1.1).shift(band_shift(3) + UP * 3.2)
        self.play(Write(b3t))
        self.wait(1.5)
        o3 = band_shift(3) + LEFT * 4.4 + DOWN * 3.2
        xa3, ya3, pl3, ql3 = self.axes(o3)
        self.play(Create(xa3), Create(ya3), Write(pl3), Write(ql3))
        d3_pts = self.pts(o3, D_OFFSETS)
        s3_pts = self.pts(o3, S_OFFSETS)
        for p in d3_pts:
            self.play(Create(Dot(p, color=BLUE)), run_time=0.4)
        d3 = chain(list(reversed(d3_pts)), BLUE)
        self.play(Create(d3), run_time=1.5)
        d3_lab = Tex("D", color=BLUE).scale(0.95).next_to(d3_pts[0], RIGHT, buff=0.15)
        self.play(Write(d3_lab))
        self.wait(1.5)
        for p in s3_pts:
            self.play(Create(Dot(p, color=YELLOW)), run_time=0.4)
        s3 = chain(s3_pts, YELLOW)
        self.play(Create(s3), run_time=1.5)
        s3_lab = Tex("S", color=YELLOW).scale(0.95).next_to(s3_pts[-1], RIGHT, buff=0.15)
        self.play(Write(s3_lab))
        self.wait(3)

        # --- Band 4 (subtopic_3): equilibrium read off ---
        self.next_band(4)
        b4t = Tex("The crossing: equilibrium").scale(1.15).shift(band_shift(4) + UP * 3.2)
        self.play(Write(b4t))
        self.wait(1.5)
        o4 = band_shift(4) + LEFT * 4.4 + DOWN * 3.2
        xa4, ya4, pl4, ql4 = self.axes(o4)
        self.play(Create(xa4), Create(ya4), Write(pl4), Write(ql4))
        d4_pts = self.pts(o4, D_OFFSETS)
        s4_pts = self.pts(o4, S_OFFSETS)
        d4 = chain(list(reversed(d4_pts)), BLUE)
        s4 = chain(s4_pts, YELLOW)
        self.play(Create(d4), run_time=1.2)
        self.play(Create(s4), run_time=1.2)
        e4 = o4 + RIGHT * 3.7 + UP * 2.5
        e4_dot = Dot(e4, color=GREEN)
        self.play(Create(e4_dot))
        dash_p = DashedLine(e4, o4 + UP * 2.5, color=GREEN, stroke_width=3)
        dash_q = DashedLine(e4, o4 + RIGHT * 3.7, color=GREEN, stroke_width=3)
        self.play(Create(dash_p), Create(dash_q))
        p4_lab = Tex("R15").scale(0.8).next_to(o4 + UP * 2.5, LEFT, buff=0.12)
        q4_lab = Tex("150").scale(0.8).next_to(o4 + RIGHT * 3.7, DOWN, buff=0.12)
        e4_lab = Tex("E", color=GREEN).scale(0.9).next_to(e4, UR, buff=0.1)
        self.play(Write(p4_lab), Write(q4_lab), Write(e4_lab))
        self.wait(2)
        b4a = Tex(r"Graph and table must agree:").scale(0.9).shift(band_shift(4) + RIGHT * 3.4 + UP * 1.6)
        b4b = Tex(r"the crossing sits on the 150/150 row").scale(0.9).shift(band_shift(4) + RIGHT * 3.4 + UP * 0.9)
        self.play(Write(b4a))
        self.play(Write(b4b))
        self.wait(3)

        # --- Band 5 (subtopic_4): excess supply at R20 ---
        self.next_band(5)
        b5t = Tex("Reading the gap at R20").scale(1.15).shift(band_shift(5) + UP * 3.2)
        self.play(Write(b5t))
        self.wait(1.5)
        o5 = band_shift(5) + LEFT * 4.4 + DOWN * 3.2
        xa5, ya5, pl5, ql5 = self.axes(o5)
        self.play(Create(xa5), Create(ya5), Write(pl5), Write(ql5))
        d5 = chain(list(reversed(self.pts(o5, D_OFFSETS))), BLUE)
        s5 = chain(self.pts(o5, S_OFFSETS), YELLOW)
        self.play(Create(d5), run_time=1.2)
        self.play(Create(s5), run_time=1.2)
        # Level sweep at R20 (height 3.4): demand at 100 (x=2.2), supply at 200 (x=5.2).
        sweep = DashedLine(o5 + UP * 3.4, o5 + RIGHT * 5.2 + UP * 3.4,
                           color=RED, stroke_width=3)
        self.play(Create(sweep))
        r20_lab = Tex("R20").scale(0.8).next_to(o5 + UP * 3.4, LEFT, buff=0.12)
        self.play(Write(r20_lab))
        d_hit = Dot(o5 + RIGHT * 2.2 + UP * 3.4, color=BLUE)
        s_hit = Dot(o5 + RIGHT * 5.2 + UP * 3.4, color=YELLOW)
        self.play(Create(d_hit), Create(s_hit))
        drop_d = DashedLine(o5 + RIGHT * 2.2 + UP * 3.4, o5 + RIGHT * 2.2,
                            color=BLUE, stroke_width=3)
        drop_s = DashedLine(o5 + RIGHT * 5.2 + UP * 3.4, o5 + RIGHT * 5.2,
                            color=YELLOW, stroke_width=3)
        self.play(Create(drop_d), Create(drop_s))
        q100 = Tex("100").scale(0.75).next_to(o5 + RIGHT * 2.2, DOWN, buff=0.12)
        q200 = Tex("200").scale(0.75).next_to(o5 + RIGHT * 5.2, DOWN, buff=0.12)
        self.play(Write(q100), Write(q200))
        self.wait(2)
        gap = Line(o5 + RIGHT * 2.2 + UP * 3.4, o5 + RIGHT * 5.2 + UP * 3.4,
                   color=RED, stroke_width=7)
        self.play(Create(gap))
        b5a = Tex(r"excess supply $= 200 - 100 = 100$").scale(0.9).shift(band_shift(5) + RIGHT * 3.2 + UP * 1.6)
        self.play(Write(b5a))
        self.play(Create(SurroundingRectangle(b5a, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the mirror skill + verification ---
        self.next_band(6)
        b6t = Tex("The mirror, and the checks").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        b6a = Tex(r"At R10: D reads 200, S reads 100 —").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6b = Tex(r"excess DEMAND of 100 below equilibrium").scale(1.0).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6a))
        self.play(Write(b6b))
        self.wait(2.5)
        b6c = Tex(r"Verify: points match rows; D down, S up;").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        b6d = Tex(r"crossing on the equal row").scale(0.95).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6c))
        self.play(Write(b6d))
        self.wait(2.5)
        b6e = Tex(r"Both readings at ONE price —").scale(1.0).shift(band_shift(6) + DOWN * 2.0)
        b6f = Tex(r"the sweep must stay level").scale(1.0).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6e))
        self.play(Write(b6f))
        self.play(Create(SurroundingRectangle(VGroup(b6e, b6f), color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the table is the boss ---
        self.next_band(7)
        b7t = Tex("The table is the boss").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex(r"The graph invents NOTHING —").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7b = Tex(r"every dot walks out of a row").scale(1.0).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7a))
        self.play(Write(b7b))
        self.wait(2.5)
        b7c = Tex(r"Interview first: D shrinks (downhill),").scale(1.0).shift(band_shift(7) + DOWN * 0.4)
        b7d = Tex(r"S grows (uphill) — shapes known early").scale(1.0).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7c))
        self.play(Write(b7d))
        self.wait(2.5)
        b7e = Tex(r"Handshake row: R15, both sides 150 —").scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        b7f = Tex(r"the lines MUST cross there").scale(1.0).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7e))
        self.play(Write(b7f))
        self.play(Create(SurroundingRectangle(b7f, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): building the picture frame ---
        self.next_band(8)
        b8t = Tex("Building the picture frame").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex(r"Habit 1: price up, quantity along").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8a))
        self.wait(2)
        b8b = Tex(r"Habit 2: even steps — a warped tape").scale(1.0).shift(band_shift(8) + UP * 0.4)
        b8c = Tex(r"measures nothing").scale(1.0).shift(band_shift(8) + DOWN * 0.3)
        self.play(Write(b8b))
        self.play(Write(b8c))
        self.wait(2.5)
        b8d = Tex(r"Habit 3: name everything — free marks").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8d))
        self.wait(2)
        b8e = Tex(r"Then deliveries: each row an address,").scale(1.0).shift(band_shift(8) + DOWN * 2.1)
        b8f = Tex(r"each address a dot — the laws draw the rest").scale(1.0).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8e))
        self.play(Write(b8f))
        self.play(Create(SurroundingRectangle(VGroup(b8e, b8f), color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): the answer machine ---
        self.next_band(9)
        b9t = Tex("The answer machine").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex(r"Crossing: R15 across, 150 down —").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9b = Tex(r"landing gear to both axes").scale(1.0).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9a))
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = Tex(r"Feed it R20: level sweep — D at 100,").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        b9d = Tex(r"S at 200 — gap of 100 in plain sight").scale(1.0).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9c))
        self.play(Write(b9d))
        self.wait(2.5)
        b9e = Tex(r"One rule: BOTH touches, ONE height —").scale(1.0).shift(band_shift(9) + DOWN * 2.0)
        b9f = Tex(r"level sweep, two touches, subtract").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9e))
        self.play(Write(b9f))
        self.play(Create(SurroundingRectangle(VGroup(b9e, b9f), color=GREEN)))
        self.wait(4)
