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

# Band-layout whiteboard scene for the Paper 1 practice-run session.
# This practice script runs all seven subtopics as one exam walk-through
# (Section A, short items, two data responses, paragraphs, two essays).
# Subtopic durations 240/220/240/250/240/270/240 of 1700 s — bands
# 0-1 / 2 / 3-4 / 5-6 / 7 / 8-9 / 10 apportioned to match.
# Business-cycle and Laffer sketches hand-built from Arrow/Line/Dot/Tex.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


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


class PaperOnePracticeRunSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # --- Band 0 (subtopic_1): Section A, the MCQ items ---
        title = Tex("Paper 1 Practice Run — 150 marks").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0 = Tex("Q1 compulsory, 30 marks: 8 MCQ $\\times$ 2,").scale(1.05).shift(UP * 1.5)
        s0b = Tex("8 matching $\\times$ 1, 6 give-the-term $\\times$ 1").scale(1.05).shift(UP * 0.8)
        self.play(Write(s0))
        self.play(Write(s0b))
        self.wait(2.5)
        m1 = Tex("Withdrawal via savings, taxes, imports?").scale(1.0).shift(DOWN * 0.1)
        m1a = Tex("$\\rightarrow$ LEAKAGES").scale(1.0).shift(DOWN * 0.8)
        self.play(Write(m1))
        self.play(Write(m1a))
        self.wait(2)
        m2 = Tex("Highest point before turning down? $\\rightarrow$ PEAK").scale(1.0).shift(DOWN * 1.6)
        self.play(Write(m2))
        self.wait(2)
        m3 = Tex("SA exchange rate system? $\\rightarrow$ FREE FLOATING").scale(1.0).shift(DOWN * 2.4)
        m3b = Tex("(SARB smooths extremes, defends no level)").scale(0.95).shift(DOWN * 3.1)
        self.play(Write(m3))
        self.play(Write(m3b))
        self.wait(3)

        # --- Band 1 (subtopic_1): matching and give-the-term ---
        self.next_band(1)
        b1_title = Tex("Matching, and give-the-term").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Rolling 3-year spending plan $\\rightarrow$ MTEF").scale(1.0).shift(band_shift(1) + UP * 1.4)
        b1_l2 = Tex("Direct and portfolio investment $\\rightarrow$ financial account").scale(0.95).shift(band_shift(1) + UP * 0.7)
        b1_l3 = Tex("Cycles caused from inside $\\rightarrow$ the Keynesians").scale(1.0).shift(band_shift(1))
        for m in (b1_l1, b1_l2, b1_l3):
            self.play(Write(m))
            self.wait(1.8)
        b1_l4 = Tex("Compensation for capital $\\rightarrow$ interest").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        b1_l5 = Tex("Deliberate lowering, fixed system $\\rightarrow$ devaluation").scale(0.95).shift(band_shift(1) + DOWN * 1.6)
        b1_l6 = Tex("Extra income from an injection $\\rightarrow$ multiplier effect").scale(0.95).shift(band_shift(1) + DOWN * 2.3)
        for m in (b1_l4, b1_l5, b1_l6):
            self.play(Write(m))
            self.wait(1.8)
        b1_l7 = Tex("Write the FULL term — abbreviations earn nothing").scale(1.0).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(b1_l7))
        self.play(Create(SurroundingRectangle(b1_l7, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): short items, banked in seconds ---
        self.next_band(2)
        b2_title = Tex("Short items: bank the first four marks").scale(1.1).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("TWO leakages $\\rightarrow$ savings, taxes (imports too)").scale(1.0).shift(band_shift(2) + UP * 1.4)
        b2_l2 = Tex("TWO monetary instruments $\\rightarrow$ repo rate,").scale(1.0).shift(band_shift(2) + UP * 0.7)
        b2_l3 = Tex("open market transactions").scale(1.0).shift(band_shift(2))
        b2_l4 = Tex("TWO trade protocols $\\rightarrow$ SACU, SADC").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(1.8)
        b2_l5 = Tex("Depreciation $\\rightarrow$ exports cheaper abroad,").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        b2_l6 = Tex("so volumes rise: direction + reason = 2 marks").scale(1.0).shift(band_shift(2) + DOWN * 2.3)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.wait(2.5)
        b2_l7 = Tex("A two-mark answer is two lines, never a paragraph").scale(1.0).shift(band_shift(2) + DOWN * 3.1)
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
        wave = chain(o, [(0.4, 1.6), (1.6, 0.6), (3.0, 1.6), (4.4, 3.2),
                         (5.8, 4.1), (7.2, 3.0), (8.4, 2.4), (9.8, 3.8)],
                     color=YELLOW)
        self.play(Create(wave), run_time=2)
        self.wait(1.5)
        a_dot = Dot(o + RIGHT * 1.6 + UP * 0.6, color=RED)
        a_lab = Tex("A").scale(0.95).next_to(o + RIGHT * 1.6 + UP * 0.6, DOWN, buff=0.15)
        b_dot = Dot(o + RIGHT * 4.4 + UP * 3.2, color=GREEN)
        b_lab = Tex("B").scale(0.95).next_to(o + RIGHT * 4.4 + UP * 3.2, LEFT, buff=0.15)
        c_dot = Dot(o + RIGHT * 5.8 + UP * 4.1, color=YELLOW)
        c_lab = Tex("C").scale(0.95).next_to(o + RIGHT * 5.8 + UP * 4.1, UP, buff=0.15)
        self.play(Create(a_dot), Write(a_lab))
        self.play(Create(b_dot), Write(b_lab))
        self.play(Create(c_dot), Write(c_lab))
        self.wait(1.5)
        x_line = DashedLine(o + RIGHT * 5.8 + UP * 2.4, o + RIGHT * 5.8 + UP * 4.1,
                            color=RED, stroke_width=4)
        x_lab = Tex("X").scale(0.95).next_to(o + RIGHT * 5.8 + UP * 3.2, RIGHT, buff=0.15)
        self.play(Create(x_line), Write(x_lab))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): reading the diagram for marks ---
        self.next_band(4)
        b4_title = Tex("Reading the diagram for marks").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("A $=$ trough; B $=$ recovery (1 mark each)").scale(1.05).shift(band_shift(4) + UP * 1.4)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex("Trend line: the long-term average path of").scale(1.0).shift(band_shift(4) + UP * 0.6)
        b4_l3 = Tex("growth, drawn through the cycles (2 marks)").scale(1.0).shift(band_shift(4) + DOWN * 0.1)
        self.play(Write(b4_l2))
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = Tex("C: spending presses on full capacity —").scale(1.0).shift(band_shift(4) + DOWN * 1.0)
        b4_l5 = Tex("excess demand pulls prices up (2 marks)").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(2.5)
        b4_l6 = Tex("X $=$ AMPLITUDE: the swing from trend; large").scale(1.0).shift(band_shift(4) + DOWN * 2.5)
        b4_l7 = Tex("$=$ violent cycle $\\Rightarrow$ heavier stabilisation (4)").scale(1.0).shift(band_shift(4) + DOWN * 3.1)
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
        r_l1 = Tex("Goods exports 1 200").scale(0.95).shift(band_shift(5) + LEFT * 3.4 + UP * 1.0)
        r_l2 = Tex("Net gold exports 100").scale(0.95).shift(band_shift(5) + LEFT * 3.4 + UP * 0.3)
        r_l3 = Tex("Services receipts 200").scale(0.95).shift(band_shift(5) + LEFT * 3.4 + DOWN * 0.4)
        r_l4 = Tex("Income receipts 150").scale(0.95).shift(band_shift(5) + LEFT * 3.4 + DOWN * 1.1)
        p_l1 = Tex("Imports 1 400").scale(0.95).shift(band_shift(5) + RIGHT * 3.4 + UP * 1.0)
        p_l2 = Tex("Services paid 250").scale(0.95).shift(band_shift(5) + RIGHT * 3.4 + UP * 0.3)
        p_l3 = Tex("Income paid 200").scale(0.95).shift(band_shift(5) + RIGHT * 3.4 + DOWN * 0.4)
        p_l4 = Tex("Transfers $-50$").scale(0.95).shift(band_shift(5) + RIGHT * 3.4 + DOWN * 1.1)
        for m in (r_l1, r_l2, r_l3, r_l4):
            self.play(Write(m), run_time=0.8)
        for m in (p_l1, p_l2, p_l3, p_l4):
            self.play(Write(m), run_time=0.8)
        self.wait(2)
        b5_l1 = Tex("Tourist earnings? $\\rightarrow$ services receipts").scale(1.0).shift(band_shift(5) + DOWN * 2.1)
        b5_l2 = Tex("Largest debit? $\\rightarrow$ merchandise imports").scale(1.0).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l1))
        self.wait(1.5)
        self.play(Write(b5_l2))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the calculations ---
        self.next_band(6)
        b6_title = Tex("The calculations, as number sentences").scale(1.1).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Trade balance} = 1\,200 + 100 - 1\,400").scale(1.05).shift(band_shift(6) + UP * 1.4)
        b6_l2 = MathTex(r"= -\text{R}100 \text{ million (deficit)}").scale(1.05).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = MathTex(r"1\,200 + 100 + 200 + 150 = 1\,650").scale(1.05).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = MathTex(r"1\,650 - 1\,400 - 250 - 200 - 50 = -250").scale(1.05).shift(band_shift(6) + DOWN * 1.4)
        b6_l5 = Tex("Current account deficit of R250 million").scale(1.05).shift(band_shift(6) + DOWN * 2.3)
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

        # --- Band 7 (subtopic_5): the eight-mark paragraphs ---
        self.next_band(7)
        b7_title = Tex("Eight-mark paragraphs: the Laffer curve").scale(1.1).shift(band_shift(7) + UP * 2.6)
        self.play(Write(b7_title))
        self.wait(1.5)
        o2 = band_shift(7) + LEFT * 5.6 + DOWN * 1.6
        ax2 = axes(o2, 5.4, 3.6, "tax rate", "revenue")
        self.play(Create(ax2))
        laffer = chain(o2, [(0.3, 0.2), (1.4, 1.9), (2.6, 2.9), (3.8, 2.0), (4.9, 0.3)],
                       color=YELLOW)
        self.play(Create(laffer), run_time=1.5)
        opt = DashedLine(o2 + RIGHT * 2.6, o2 + RIGHT * 2.6 + UP * 2.9, stroke_width=3)
        opt_lab = Tex("optimal").scale(0.85).next_to(o2 + RIGHT * 2.6, DOWN, buff=0.15)
        self.play(Create(opt), Write(opt_lab))
        self.wait(2)
        b7_l1 = Tex("0\\% and 100\\% both raise zero;").scale(0.95).shift(band_shift(7) + RIGHT * 3.4 + UP * 1.2)
        b7_l2 = Tex("beyond the optimum, CUTTING").scale(0.95).shift(band_shift(7) + RIGHT * 3.4 + UP * 0.4)
        b7_l3 = Tex("rates raises MORE revenue").scale(0.95).shift(band_shift(7) + RIGHT * 3.4 + DOWN * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex("Higher order: stimulus crowds out, spills into").scale(0.95).shift(band_shift(7) + DOWN * 2.5)
        b7_l5 = Tex("inflation and imports — 4 facts $\\times$ 2 marks $=$ 8").scale(0.95).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): the essay's fixed skeleton ---
        self.next_band(8)
        b8_title = Tex("The 40-mark essay: smoothing cycles").scale(1.15).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(1.5)
        seg = [("Intro", "2", -5.0, 1.6), ("Body", "26", -1.7, 3.4),
               ("Extra", "10", 2.0, 2.4), ("Concl.", "2", 4.9, 1.6)]
        for name, marks, x, w in seg:
            r = Rectangle(width=w, height=1.1).shift(band_shift(8) + RIGHT * x + UP * 1.2)
            t = Tex(name + " " + marks).scale(0.9).shift(band_shift(8) + RIGHT * x + UP * 1.2)
            self.play(Create(r), Write(t), run_time=0.8)
        self.wait(2)
        b8_l1 = Tex("Intro (2): one clean definition — cycles are").scale(1.0).shift(band_shift(8) + UP * 0.1)
        b8_l2 = Tex("expansion and contraction around a trend").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Body (26): downswing — repo down, credit cheap,").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        b8_l4 = Tex("spending and tax cuts inject via the multiplier;").scale(1.0).shift(band_shift(8) + DOWN * 2.2)
        b8_l5 = Tex("upswing — reverse every lever; add stabilisers").scale(1.0).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): evaluation and conclusion ---
        self.next_band(9)
        b9_title = Tex("The additional part and conclusion").scale(1.15).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(1.5)
        b9_l1 = Tex("Evaluate (10): lags land stimulus in the wrong").scale(1.0).shift(band_shift(9) + UP * 1.4)
        b9_l2 = Tex("phase; Phillips trade-off; repo cannot fix").scale(1.0).shift(band_shift(9) + UP * 0.7)
        b9_l3 = Tex("supply shocks; debt service crowds budgets").scale(1.0).shift(band_shift(9))
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(3)
        b9_l4 = Tex("Judged whole: smooths moderately well, best").scale(1.0).shift(band_shift(9) + DOWN * 0.9)
        b9_l5 = Tex("paired with supply-side reform").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(2)
        b9_l6 = Tex("Conclusion (2): a FRESH judgement — never").scale(1.0).shift(band_shift(9) + DOWN * 2.5)
        b9_l7 = Tex("a repeat of the body").scale(1.0).shift(band_shift(9) + DOWN * 3.2)
        self.play(Write(b9_l6))
        self.play(Write(b9_l7))
        self.play(Create(SurroundingRectangle(b9_l7, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): second option and marking wisdom ---
        self.next_band(10)
        b10_title = Tex("Second essay, and the marking wisdom").scale(1.1).shift(band_shift(10) + UP * 2.6)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Regional development skeleton: SDIs, the Maputo").scale(0.95).shift(band_shift(10) + UP * 1.8)
        b10_l2 = Tex("corridor, IDZs at Coega, East London, Richards").scale(0.95).shift(band_shift(10) + UP * 1.1)
        b10_l3 = Tex("Bay; SEZs with tax incentives; honest scorecard").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.play(Write(b10_l3))
        self.wait(3)
        b10_l4 = Tex("1. Obey command verbs — evaluate needs judgement").scale(0.95).shift(band_shift(10) + DOWN * 0.4)
        b10_l5 = Tex("2. Mark allocation is the recipe: 2 per fact").scale(0.95).shift(band_shift(10) + DOWN * 1.1)
        b10_l6 = Tex("3. Formula line and units ARE marks").scale(0.95).shift(band_shift(10) + DOWN * 1.8)
        b10_l7 = Tex("4. Never spend the conclusion summarising").scale(0.95).shift(band_shift(10) + DOWN * 2.4)
        b10_l8 = Tex("5. Choose essays by your strongest DATA topics").scale(0.95).shift(band_shift(10) + DOWN * 3.1)
        for m in (b10_l4, b10_l5, b10_l6, b10_l7, b10_l8):
            self.play(Write(m))
            self.wait(1.8)
        self.play(Create(SurroundingRectangle(b10_l8, color=GREEN)))
        self.wait(4)
