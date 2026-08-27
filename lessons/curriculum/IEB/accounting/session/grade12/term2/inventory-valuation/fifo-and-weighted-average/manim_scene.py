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

# Band-layout whiteboard scene for the grade 12 accounting session duo
# "FIFO and Weighted Average". One band per teaching beat; the camera moves
# down to fresh space and earlier work stays on the canvas. Exporter-safe
# mobjects only; write-only reveals — no Transform/FadeOut/sub-part indexing.
#
# Subtopic time shares (subtopics.json, total 1530 s):
# 230/240/230/230 expert, 190/210/200 simplifier.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FifoAndWeightedAverageSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): systems and the three methods ---
        title = Tex("FIFO and Weighted Average").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Perpetual: stock is a running account").scale(1.05).shift(UP * 1.3)
        b0_l2 = Tex(r"Periodic: opening $+$ purchases $-$ closing $=$ COS").scale(1.05).shift(UP * 0.5)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("1. Specific identification — few, costly, traceable").scale(1.0).shift(DOWN * 0.5)
        b0_l4 = Tex("2. FIFO — oldest sold first, shelf holds newest costs").scale(1.0).shift(DOWN * 1.3)
        b0_l5 = Tex("3. Weighted average — one pooled cost per unit").scale(1.0).shift(DOWN * 2.1)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2)
        self.play(Write(b0_l5))
        self.wait(2)
        b0_l6 = Tex("GAAP: historical cost, prudence, consistency").scale(1.0).shift(DOWN * 2.9)
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_2): the Radebe Electrical stock story ---
        self.next_band(1)
        b1_title = Tex("Radebe Electrical: the year's stock story").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Opening: 250 units @ R42 $=$ R10\,500").scale(1.05).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex(r"May: 500 @ R45 $=$ R22\,500").scale(1.05).shift(band_shift(1) + UP * 0.4)
        b1_l3 = Tex(r"Aug: 350 @ R48 $=$ R16\,800").scale(1.05).shift(band_shift(1) + DOWN * 0.4)
        b1_l4 = Tex(r"Nov: 150 @ R50 $=$ R7\,500").scale(1.05).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_l1))
        self.wait(1.5)
        self.play(Write(b1_l2))
        self.wait(1.5)
        self.play(Write(b1_l3))
        self.wait(1.5)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex(r"Available: 1\,250 units costing R57\,300").scale(1.05).shift(band_shift(1) + DOWN * 2.1)
        b1_l6 = Tex(r"Sold 950 @ R70 $=$ R66\,500; 300 remain").scale(1.05).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(2)
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): FIFO worked to the rand ---
        self.next_band(2)
        b2_title = Tex("FIFO: value the 300 from the NEWEST back").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_wrong = Tex("Counting forward from opening stock").scale(1.0).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2)
        b2_l1 = Tex(r"150 @ R50 (Nov) $=$ R7\,500").scale(1.05).shift(band_shift(2) + UP * 0.3)
        b2_l2 = Tex(r"150 @ R48 (Aug) $=$ R7\,200").scale(1.05).shift(band_shift(2) + DOWN * 0.5)
        b2_l3 = Tex(r"Closing stock $=$ R14\,700").scale(1.1).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_l4 = Tex(r"COS: $57\,300 - 14\,700 = $ R42\,600").scale(1.05).shift(band_shift(2) + DOWN * 2.1)
        b2_l5 = Tex(r"Gross profit: $66\,500 - 42\,600 = $ R23\,900").scale(1.05).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l4))
        self.wait(2)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_3): weighted average worked to the rand ---
        self.next_band(3)
        b3_title = Tex("Weighted average: pool everything").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\frac{R57\,300}{1\,250 \text{ units}} = R45{,}84 \text{ per unit}").scale(1.0).shift(band_shift(3) + UP * 1.0)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = Tex(r"Closing stock: 300 @ R45,84 $=$ R13\,752").scale(1.05).shift(band_shift(3) + UP * 0.0)
        b3_l3 = Tex(r"Cost of sales: 950 @ R45,84 $=$ R43\,548").scale(1.05).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = Tex(r"Check: $13\,752 + 43\,548 = R57\,300$ — the pool").scale(1.0).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex(r"Gross profit: $66\,500 - 43\,548 = $ R22\,952").scale(1.05).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the comparison and the two traps ---
        self.next_band(4)
        b4_title = Tex("Side by side: the R948 law").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Closing stock: R14\,700 vs R13\,752 $=$ R948").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex(r"Gross profit: R23\,900 vs R22\,952 $=$ R948").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4_l3 = Tex("Rands on the shelf are rands kept out of COS").scale(1.0).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        b4_wrong = Tex(r"Simple average of prices: $\frac{42+45+48+50}{4} = R46{,}25$").scale(0.95).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_wrong))
        self.play(Create(strike(b4_wrong)))
        self.wait(2)
        b4_l4 = Tex("Weight by UNITS; carriage joins the cost pool").scale(1.0).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_4): validation, controls, ethics ---
        self.next_band(5)
        b5_title = Tex("Validation, control, ethics").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Books say 300; the count finds 275").scale(1.05).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex(r"Deficit: 25 @ R45,84 $=$ R1\,146 written off").scale(1.05).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2)
        b5_l3 = Tex("Controls: divide duties; pre-numbered documents;").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex("locked storerooms; independent counts; review").scale(0.95).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex(r"Overstate stock $\rightarrow$ inflate profit; understate $\rightarrow$ cheat SARS").scale(0.9).shift(band_shift(5) + DOWN * 2.1)
        b5_l6 = Tex("Consistency is the GAAP answer to convenient switches").scale(0.9).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5))
        self.wait(2)
        self.play(Write(b5_l6))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): the fridge that ate the profits ---
        self.next_band(6)
        b6_title = Tex("Karabo's fridge: three honest options").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"35 boxes: some cost R8, some R10 — no name tags").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex("Know each item — works for dated yoghurt tubs").scale(1.0).shift(band_shift(6) + UP * 0.2)
        b6_l3 = Tex("Oldest sells first — the fridge holds the newest").scale(1.0).shift(band_shift(6) + DOWN * 0.6)
        b6_l4 = Tex("Or call every box the average of the batch").scale(1.0).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("The fridge and the profit share one pot of rands").scale(1.0).shift(band_shift(6) + DOWN * 2.3)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_6): two honest answers on 75 boxes ---
        self.next_band(7)
        b7_title = Tex("Two honest answers, 75 boxes").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"45 @ R8 $+$ 30 @ R10 $=$ 75 boxes, R660; sold 40 @ R14").scale(0.95).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex(r"FIFO fridge: 30 @ R10 $+$ 5 @ R8 $=$ R340").scale(1.0).shift(band_shift(7) + UP * 0.3)
        b7_l3 = Tex(r"COS R320; profit $560 - 320 = $ R240").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex(r"Average: $R660 \div 75 = R8{,}80$; fridge R308").scale(1.0).shift(band_shift(7) + DOWN * 1.4)
        b7_l5 = Tex(r"COS R352; profit $560 - 352 = $ R208").scale(1.0).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l4))
        self.wait(2)
        self.play(Write(b7_l5))
        self.wait(2)
        b7_l6 = Tex(r"R32 apart — the same R32 sitting in the fridge").scale(1.0).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_7): when the count and the book disagree ---
        self.next_band(8)
        b8_title = Tex("When the count and the book disagree").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Notebook: 35 boxes. Count: 32. Three missing").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex(r"Deficit: 3 @ R8,80 $=$ R26,40 written off").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2)
        b8_l3 = Tex(r"3 boxes a week $=$ 150-plus a year — a ghost's feast").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("Fences: split the jobs, keep the papers, lock up,").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        b8_l5 = Tex("surprise counts by someone else, read the trend").scale(0.95).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2.5)
        b8_l6 = Tex("Puff the fridge up or squash it down — both are lies").scale(0.95).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_l6))
        self.wait(4)
