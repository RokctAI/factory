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

# Band-layout whiteboard scene for the macroeconomics practice-run session.
# This practice script runs all seven subtopics as one exam-technique
# walk-through (quick-fire recall, short answers, two data responses,
# paragraph answers, the essay built live, a second essay plan).
# Subtopic durations 240/220/240/250/240/270/240 of 1700 s — bands
# 0-1 / 2 / 3-4 / 5-6 / 7 / 8-9 / 10 apportioned to match.
# Business-cycle and multiplier sketches hand-built from Arrow/Line/Dot/Tex.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def axes(origin, w, h, xlab, ylab):
    xa = Arrow(origin, origin + RIGHT * w, buff=0, stroke_width=3)
    ya = Arrow(origin, origin + UP * h, buff=0, stroke_width=3)
    xl = Tex(xlab).scale(0.9).next_to(origin + RIGHT * w, DOWN, buff=0.2)
    yl = Tex(ylab).scale(0.9).next_to(origin + UP * h, RIGHT, buff=0.15)
    return VGroup(xa, ya, xl, yl)


def chain(origin, pts, color=WHITE, sw=5):
    g = VGroup()
    for a, b in zip(pts[:-1], pts[1:]):
        g.add(Line(origin + RIGHT * a[0] + UP * a[1],
                   origin + RIGHT * b[0] + UP * b[1],
                   color=color, stroke_width=sw))
    return g


class MacroPracticeRunSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # --- Band 0 (subtopic_1): quick-fire multiple choice ---
        title = Tex("Macro Practice Run — own mark plan").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0 = Tex("Quick-fire block, 30 marks: MCQ $\\times$ 2,").scale(1.05).shift(UP * 1.5)
        s0b = Tex("matching $\\times$ 1, give-the-term $\\times$ 1").scale(1.05).shift(UP * 0.8)
        self.play(Write(s0))
        self.play(Write(s0b))
        self.wait(2.5)
        m1 = Tex("Entry via investment, spending, exports?").scale(1.0).shift(DOWN * 0.1)
        m1a = Tex("$\\rightarrow$ INJECTIONS").scale(1.0).shift(DOWN * 0.8)
        self.play(Write(m1))
        self.play(Write(m1a))
        self.wait(2)
        m2 = Tex("Falling stops, climbing begins? $\\rightarrow$ RECOVERY").scale(1.0).shift(DOWN * 1.6)
        self.play(Write(m2))
        self.wait(2)
        m3 = Tex("Reward for natural resources? $\\rightarrow$ RENT").scale(1.0).shift(DOWN * 2.4)
        m3b = Tex("factor rewards are a matched set").scale(0.95).shift(DOWN * 3.1)
        self.play(Write(m3))
        self.play(Write(m3b))
        self.wait(3)

        # --- Band 1 (subtopic_1): matching and give-the-term ---
        self.next_band(1)
        b1_title = Tex("Matching, and give-the-term").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Everyday trade account $\\rightarrow$ current account").scale(1.0).shift(band_shift(1) + UP * 1.4)
        b1_l2 = Tex("Outside shocks cause cycles $\\rightarrow$ monetarists").scale(0.95).shift(band_shift(1) + UP * 0.7)
        b1_l3 = Tex("Central bank's lending rate $\\rightarrow$ repo rate").scale(1.0).shift(band_shift(1))
        for m in (b1_l1, b1_l2, b1_l3):
            self.play(Write(m))
            self.wait(1.8)
        b1_l4 = Tex("Export over import prices $\\times$ 100 $\\rightarrow$ terms of trade").scale(0.95).shift(band_shift(1) + DOWN * 0.9)
        b1_l5 = Tex("Floating currency gains value $\\rightarrow$ appreciation").scale(0.95).shift(band_shift(1) + DOWN * 1.6)
        b1_l6 = Tex("Spent share of an extra rand $\\rightarrow$ marginal").scale(0.95).shift(band_shift(1) + DOWN * 2.3)
        b1_l6b = Tex("propensity to consume, in full").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        for m in (b1_l4, b1_l5, b1_l6, b1_l6b):
            self.play(Write(m))
            self.wait(1.8)
        self.play(Create(SurroundingRectangle(b1_l6b, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): short answers, banked in seconds ---
        self.next_band(2)
        b2_title = Tex("Short answers: bank the easy marks first").scale(1.1).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("TWO injections $\\rightarrow$ investment, spending").scale(1.0).shift(band_shift(2) + UP * 1.4)
        b2_l2 = Tex("TWO fiscal instruments $\\rightarrow$ taxation,").scale(1.0).shift(band_shift(2) + UP * 0.7)
        b2_l3 = Tex("government spending").scale(1.0).shift(band_shift(2))
        b2_l4 = Tex("TWO social indicators $\\rightarrow$ life expectancy,").scale(0.95).shift(band_shift(2) + DOWN * 0.7)
        b2_l4b = Tex("clean water access").scale(0.95).shift(band_shift(2) + DOWN * 1.3)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4, b2_l4b):
            self.play(Write(m))
            self.wait(1.6)
        b2_l5 = Tex("Appreciation $\\rightarrow$ imports cheaper in rands,").scale(0.95).shift(band_shift(2) + DOWN * 2.1)
        b2_l6 = Tex("so volumes rise: direction + reason = 2 marks").scale(0.95).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.wait(2.5)
        b2_l7 = Tex("A two-mark answer is two lines, never a paragraph").scale(0.95).shift(band_shift(2) + DOWN * 3.3)
        self.play(Write(b2_l7))
        self.play(Create(SurroundingRectangle(b2_l7, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): the business cycle diagram ---
        self.next_band(3)
        b3_title = Tex("Data response: the business cycle").scale(1.15).shift(band_shift(3) + UP * 2.6)
        self.play(Write(b3_title))
        self.wait(1.5)
        o = band_shift(3) + LEFT * 5.4 + DOWN * 2.6
        ax = axes(o, 10.4, 4.6, "time", "activity")
        self.play(Create(ax))
        self.wait(1)
        trend = Line(o + RIGHT * 0.4 + UP * 1.0, o + RIGHT * 9.8 + UP * 3.4,
                     color=BLUE, stroke_width=4)
        trend_lab = Tex("trend line").scale(0.9).next_to(o + RIGHT * 9.8 + UP * 3.4, UP, buff=0.15)
        self.play(Create(trend), Write(trend_lab))
        self.wait(1.5)
        wave = chain(o, [(0.4, 1.2), (1.8, 3.0), (3.2, 1.2), (4.6, 1.0),
                         (6.0, 3.6), (7.4, 1.8), (8.6, 2.6), (9.8, 4.0)],
                     color=YELLOW)
        self.play(Create(wave), run_time=2)
        self.wait(1.5)
        p_dot = Dot(o + RIGHT * 1.8 + UP * 3.0, color=YELLOW)
        p_lab = Tex("P").scale(0.95).next_to(o + RIGHT * 1.8 + UP * 3.0, UP, buff=0.15)
        q_dot = Dot(o + RIGHT * 2.5 + UP * 2.1, color=GREEN)
        q_lab = Tex("Q").scale(0.95).next_to(o + RIGHT * 2.5 + UP * 2.1, RIGHT, buff=0.15)
        r_dot = Dot(o + RIGHT * 4.6 + UP * 1.0, color=RED)
        r_lab = Tex("R").scale(0.95).next_to(o + RIGHT * 4.6 + UP * 1.0, DOWN, buff=0.15)
        self.play(Create(p_dot), Write(p_lab))
        self.play(Create(q_dot), Write(q_lab))
        self.play(Create(r_dot), Write(r_lab))
        self.wait(1.5)
        l_line = DashedLine(o + RIGHT * 1.8 + UP * 4.3, o + RIGHT * 6.0 + UP * 4.3,
                            color=RED, stroke_width=4)
        l_lab = Tex("L").scale(0.95).next_to(o + RIGHT * 3.9 + UP * 4.3, UP, buff=0.15)
        self.play(Create(l_line), Write(l_lab))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): reading the diagram for marks ---
        self.next_band(4)
        b4_title = Tex("Reading the diagram for marks").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("P $=$ peak; Q $=$ recession (1 mark each)").scale(1.05).shift(band_shift(4) + UP * 1.4)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex("Extrapolation: extending the trend beyond").scale(1.0).shift(band_shift(4) + UP * 0.6)
        b4_l3 = Tex("the present to predict the path (2 marks)").scale(1.0).shift(band_shift(4) + DOWN * 0.1)
        self.play(Write(b4_l2))
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = Tex("R is the trough: stimulus there supports").scale(1.0).shift(band_shift(4) + DOWN * 1.0)
        b4_l5 = Tex("recovery, never a boom (2 marks)").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(2.5)
        b4_l6 = Tex("L $=$ CYCLE LENGTH: peak to peak; with moving").scale(1.0).shift(band_shift(4) + DOWN * 2.5)
        b4_l7 = Tex("averages it times the next turning point (4)").scale(1.0).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4_l6))
        self.play(Write(b4_l7))
        self.play(Create(SurroundingRectangle(b4_l7, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): the current account table ---
        self.next_band(5)
        b5_title = Tex("Data response: current account (R millions)").scale(1.1).shift(band_shift(5) + UP * 2.6)
        self.play(Write(b5_title))
        self.wait(1.5)
        rec_head = Tex("Receipts").scale(1.0).shift(band_shift(5) + LEFT * 3.4 + UP * 1.8)
        pay_head = Tex("Payments").scale(1.0).shift(band_shift(5) + RIGHT * 3.4 + UP * 1.8)
        mid = Line(band_shift(5) + UP * 2.1, band_shift(5) + DOWN * 1.6, stroke_width=2)
        self.play(Write(rec_head), Write(pay_head), Create(mid))
        self.wait(1.5)
        r_l1 = Tex("Goods exports 950").scale(0.95).shift(band_shift(5) + LEFT * 3.4 + UP * 1.0)
        r_l2 = Tex("Net gold exports 150").scale(0.95).shift(band_shift(5) + LEFT * 3.4 + UP * 0.3)
        r_l3 = Tex("Services receipts 300").scale(0.95).shift(band_shift(5) + LEFT * 3.4 + DOWN * 0.4)
        r_l4 = Tex("Income receipts 100").scale(0.95).shift(band_shift(5) + LEFT * 3.4 + DOWN * 1.1)
        p_l1 = Tex("Imports 1 250").scale(0.95).shift(band_shift(5) + RIGHT * 3.4 + UP * 1.0)
        p_l2 = Tex("Services paid 180").scale(0.95).shift(band_shift(5) + RIGHT * 3.4 + UP * 0.3)
        p_l3 = Tex("Income paid 220").scale(0.95).shift(band_shift(5) + RIGHT * 3.4 + DOWN * 0.4)
        p_l4 = Tex("Transfers $+30$").scale(0.95).shift(band_shift(5) + RIGHT * 3.4 + DOWN * 1.1)
        for m in (r_l1, r_l2, r_l3, r_l4):
            self.play(Write(m), run_time=0.8)
        for m in (p_l1, p_l2, p_l3, p_l4):
            self.play(Write(m), run_time=0.8)
        self.wait(2)
        b5_l1 = Tex("London branch profits home? $\\rightarrow$ income receipts").scale(0.95).shift(band_shift(5) + DOWN * 2.1)
        b5_l2 = Tex("Largest credit? $\\rightarrow$ goods exports").scale(1.0).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l1))
        self.wait(1.5)
        self.play(Write(b5_l2))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the calculations ---
        self.next_band(6)
        b6_title = Tex("The calculations, as number sentences").scale(1.1).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Trade balance} = 950 + 150 - 1\,250").scale(1.05).shift(band_shift(6) + UP * 1.4)
        b6_l2 = MathTex(r"= -\text{R}150 \text{ million (deficit)}").scale(1.05).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = MathTex(r"950 + 150 + 300 + 100 = 1\,500").scale(1.05).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = MathTex(r"1\,500 - 1\,250 - 180 - 220 + 30 = -120").scale(1.05).shift(band_shift(6) + DOWN * 1.4)
        b6_l5 = Tex("Current account deficit of R120 million").scale(1.05).shift(band_shift(6) + DOWN * 2.3)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.wait(2)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(2)
        b6_l6 = Tex("Fixes: raise rates, promote exports, depreciate").scale(1.0).shift(band_shift(6) + DOWN * 3.2)
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_5): the ten-mark paragraphs ---
        self.next_band(7)
        b7_title = Tex("Ten-mark paragraphs: the multiplier").scale(1.1).shift(band_shift(7) + UP * 2.6)
        self.play(Write(b7_title))
        self.wait(1.5)
        o2 = band_shift(7) + LEFT * 5.6 + DOWN * 1.6
        ax2 = axes(o2, 5.4, 3.6, "income", "spending")
        self.play(Create(ax2))
        line45 = Line(o2, o2 + RIGHT * 3.6 + UP * 3.6, color=BLUE, stroke_width=3)
        spend1 = Line(o2 + UP * 1.0, o2 + RIGHT * 5.0 + UP * 3.0, color=YELLOW, stroke_width=4)
        spend2 = Line(o2 + UP * 1.6, o2 + RIGHT * 5.0 + UP * 3.6, color=GREEN, stroke_width=4)
        self.play(Create(line45))
        self.play(Create(spend1))
        self.play(Create(spend2))
        self.wait(2)
        b7_l1 = Tex("Injection lifts spending a little;").scale(0.95).shift(band_shift(7) + RIGHT * 3.4 + UP * 1.2)
        b7_l2 = Tex("equilibrium income moves MORE:").scale(0.95).shift(band_shift(7) + RIGHT * 3.4 + UP * 0.4)
        b7_l3 = Tex("mpc 0,75 $\\Rightarrow$ multiplier 4").scale(0.95).shift(band_shift(7) + RIGHT * 3.4 + DOWN * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex("Arguing: weak rand helps exporters, taxes").scale(0.95).shift(band_shift(7) + DOWN * 2.5)
        b7_l5 = Tex("consumers — weigh it: 5 facts $\\times$ 2 marks $=$ 10").scale(0.95).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): the essay's mark plan ---
        self.next_band(8)
        b8_title = Tex("The 30-mark essay: smoothing cycles").scale(1.15).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(1.5)
        seg = [("Define", "2", -5.0, 1.7), ("Body", "20", -1.7, 3.2),
               ("Judge", "6", 1.9, 2.2), ("Close", "2", 4.8, 1.7)]
        for name, marks, x, w in seg:
            r = Rectangle(width=w, height=1.1).shift(band_shift(8) + RIGHT * x + UP * 1.2)
            t = Tex(name + " " + marks).scale(0.9).shift(band_shift(8) + RIGHT * x + UP * 1.2)
            self.play(Create(r), Write(t), run_time=0.8)
        self.wait(2)
        b8_l1 = Tex("Define (2): cycles are repeating expansions").scale(1.0).shift(band_shift(8) + UP * 0.1)
        b8_l2 = Tex("and contractions around a long-term trend").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Body (20): downswing — repo cut, credit cheap,").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        b8_l4 = Tex("spending up, taxes trimmed, multiplier enlarges;").scale(1.0).shift(band_shift(8) + DOWN * 2.2)
        b8_l5 = Tex("upswing — reverse the levers; add stabilisers").scale(1.0).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): evaluation and closing judgement ---
        self.next_band(9)
        b9_title = Tex("The evaluation and the closing line").scale(1.15).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(1.5)
        b9_l1 = Tex("Judge (6): lags land stimulus in the wrong").scale(1.0).shift(band_shift(9) + UP * 1.4)
        b9_l2 = Tex("phase; lower unemployment costs inflation;").scale(1.0).shift(band_shift(9) + UP * 0.7)
        b9_l3 = Tex("repo cannot fix droughts; debt bills grow").scale(1.0).shift(band_shift(9))
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(3)
        b9_l4 = Tex("Weighed whole: smooths moderately well, best").scale(1.0).shift(band_shift(9) + DOWN * 0.9)
        b9_l5 = Tex("beside supply-side reform").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(2)
        b9_l6 = Tex("Close (2): a FRESH judgement — never").scale(1.0).shift(band_shift(9) + DOWN * 2.5)
        b9_l7 = Tex("a repeat of the body").scale(1.0).shift(band_shift(9) + DOWN * 3.2)
        self.play(Write(b9_l6))
        self.play(Write(b9_l7))
        self.play(Create(SurroundingRectangle(b9_l7, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): second essay plan and exam wisdom ---
        self.next_band(10)
        b10_title = Tex("Second essay plan, and the exam wisdom").scale(1.1).shift(band_shift(10) + UP * 2.6)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Trade policy skeleton: export promotion with").scale(0.95).shift(band_shift(10) + UP * 1.8)
        b10_l2 = Tex("incentives; import substitution behind tariffs;").scale(0.95).shift(band_shift(10) + UP * 1.1)
        b10_l3 = Tex("freer trade case; the honest scorecard").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.play(Write(b10_l3))
        self.wait(3)
        b10_l4 = Tex("1. Obey command verbs — evaluate needs judgement").scale(0.95).shift(band_shift(10) + DOWN * 0.4)
        b10_l5 = Tex("2. Mark value is the recipe: 2 per fact").scale(0.95).shift(band_shift(10) + DOWN * 1.1)
        b10_l6 = Tex("3. Setup line and units ARE marks").scale(0.95).shift(band_shift(10) + DOWN * 1.8)
        b10_l7 = Tex("4. Never spend the closing paragraph summarising").scale(0.95).shift(band_shift(10) + DOWN * 2.4)
        b10_l8 = Tex("5. Choose questions by your strongest data").scale(0.95).shift(band_shift(10) + DOWN * 3.1)
        for m in (b10_l4, b10_l5, b10_l6, b10_l7, b10_l8):
            self.play(Write(m))
            self.wait(1.8)
        self.play(Create(SurroundingRectangle(b10_l8, color=GREEN)))
        self.wait(4)
