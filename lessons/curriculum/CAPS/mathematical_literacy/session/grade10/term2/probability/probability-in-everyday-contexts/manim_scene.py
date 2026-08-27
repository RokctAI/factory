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

# BAND LAYOUT: sequential vertical bands, one frame-height each; the camera
# moves down between teaching steps and nothing is ever removed. Only
# exporter-supported mobjects (Tex/MathTex, Line/Arrow, Dot,
# Rectangle/SurroundingRectangle) with write-only reveals — no sub-part
# transforms. The probability scale, the clinic two-way table and the coin
# tree are all hand-built from Lines, Dots, Rectangles and Tex.
#
# Mirrors script.md across the seven subtopics of the duo (Part 1 — Expert:
# subtopics 1-4; Part 2 — Simplifier: 5-7); band time proportional to
# subtopics.json.

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k."""
    return DOWN * BAND * k


class ProbabilityEverydayContextsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the scale from 0 to 1 ---
        title = Tex("Probability in Everyday Contexts").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        scale_line = Line(LEFT * 4.5 + UP * 0.6, RIGHT * 4.5 + UP * 0.6)
        self.play(Create(scale_line))
        d0 = Dot(LEFT * 4.5 + UP * 0.6, radius=0.07)
        dh = Dot(UP * 0.6, radius=0.07)
        d1 = Dot(RIGHT * 4.5 + UP * 0.6, radius=0.07)
        self.play(Create(d0), Create(dh), Create(d1))
        t0 = MathTex("0").scale(0.9).shift(LEFT * 4.5 + UP * 1.2)
        th = MathTex(r"\tfrac{1}{2}").scale(0.9).shift(UP * 1.3)
        t1 = MathTex("1").scale(0.9).shift(RIGHT * 4.5 + UP * 1.2)
        self.play(Write(t0), Write(th), Write(t1))
        n0 = Tex("impossible").scale(0.8).shift(LEFT * 4.3 + DOWN * 0.1)
        nh = Tex("even chance").scale(0.8).shift(DOWN * 0.1)
        n1 = Tex("certain").scale(0.8).shift(RIGHT * 4.4 + DOWN * 0.1)
        self.play(Write(n0), Write(nh), Write(n1))
        self.wait(2.5)
        l01 = Tex("Outcome, event, sample space — exact words").scale(0.95).shift(DOWN * 1.2)
        self.play(Write(l01))
        self.wait(2)
        l02 = Tex("Outside 0 to 1? Check your working.").scale(1.0).shift(DOWN * 2.2)
        self.play(Write(l02))
        self.play(Create(SurroundingRectangle(l02, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): three costumes and the complement ---
        self.next_band(1)
        b1_t = Tex("The jar: 12 red, 8 green, 5 yellow = 25").scale(1.05).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = MathTex(r"P(\text{red}) = \frac{12}{25} = 0{,}48 = 48\%").scale(1.1).shift(band_shift(1) + UP * 1.0)
        self.play(Write(b1_l1))
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2.5)
        b1_l2 = Tex("Fraction, decimal, percentage — one fact").scale(1.0).shift(band_shift(1) + UP * 0.0)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"P(\text{not red}) = \frac{13}{25} = 0{,}52").scale(1.05).shift(band_shift(1) + DOWN * 1.0)
        b1_l4 = MathTex(r"0{,}48 + 0{,}52 = 1 \;\Rightarrow\; P(\text{not } A) = 1 - P(A)").scale(0.95).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("``Not'' or ``at least one''? Use the complement").scale(0.95).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): theoretical vs relative frequency ---
        self.next_band(2)
        b2_t = Tex("Two kinds of probability").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex("Theoretical: reasoned BEFORE —").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = MathTex(r"P(\text{even on a die}) = \frac{3}{6} = 0{,}5").scale(1.05).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("Relative frequency: counted AFTER —").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = MathTex(r"\frac{128}{200} = 0{,}64 \;\; \text{(taxis to town)}").scale(1.05).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2.5)
        b2_l5 = Tex("Observation is all you have when outcomes").scale(0.95).shift(band_shift(2) + DOWN * 2.6)
        b2_l6 = Tex("are not equally likely").scale(0.95).shift(band_shift(2) + DOWN * 3.3)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): samples wander; coins have no memory ---
        self.next_band(3)
        b3_t = Tex("Small samples wander, large ones settle").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"50 \text{ tosses: } \frac{28}{50} = 0{,}56 \neq 0{,}5").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = Tex("5 000 tosses sit far closer to 0,5").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("More trials $\\Rightarrow$ relative frequency").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = Tex("tends towards the theoretical value").scale(1.0).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2.5)
        b3_l5 = Tex("After three heads, tails is NOT ``due'' —").scale(1.0).shift(band_shift(3) + DOWN * 2.4)
        b3_l6 = Tex("the coin has no memory; each toss is 0,5").scale(1.0).shift(band_shift(3) + DOWN * 3.2)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): the clinic's two-way table ---
        self.next_band(4)
        b4_t = Tex("Two-way table: 200 clinic patients").scale(1.1).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_t))
        self.wait(1.5)
        # Table: 4 cols (label, Walked, Taxi, Total) x 4 rows.
        tc = band_shift(4) + DOWN * 0.6
        tbl = Rectangle(width=8.4, height=3.6).shift(tc)
        self.play(Create(tbl))
        v1 = Line(tc + UP * 1.8 + LEFT * 1.6, tc + DOWN * 1.8 + LEFT * 1.6)
        v2 = Line(tc + UP * 1.8 + RIGHT * 0.6, tc + DOWN * 1.8 + RIGHT * 0.6)
        v3 = Line(tc + UP * 1.8 + RIGHT * 2.6, tc + DOWN * 1.8 + RIGHT * 2.6)
        h1 = Line(tc + UP * 0.9 + LEFT * 4.2, tc + UP * 0.9 + RIGHT * 4.2)
        h2 = Line(tc + DOWN * 0.9 + LEFT * 4.2, tc + DOWN * 0.9 + RIGHT * 4.2)
        self.play(Create(v1), Create(v2), Create(v3), Create(h1), Create(h2))
        hdr1 = Tex("Walked").scale(0.75).shift(tc + UP * 1.35 + LEFT * 0.5)
        hdr2 = Tex("Taxi").scale(0.75).shift(tc + UP * 1.35 + RIGHT * 1.6)
        hdr3 = Tex("Total").scale(0.75).shift(tc + UP * 1.35 + RIGHT * 3.4)
        self.play(Write(hdr1), Write(hdr2), Write(hdr3))
        r1 = Tex("Under 30").scale(0.75).shift(tc + UP * 0.45 + LEFT * 2.9)
        r1c = MathTex("46").scale(0.8).shift(tc + UP * 0.45 + LEFT * 0.5)
        r1t = MathTex("74").scale(0.8).shift(tc + UP * 0.45 + RIGHT * 1.6)
        r1s = MathTex("120").scale(0.8).shift(tc + UP * 0.45 + RIGHT * 3.4)
        self.play(Write(r1), Write(r1c), Write(r1t), Write(r1s))
        self.wait(1.5)
        r2 = Tex("30 and over").scale(0.7).shift(tc + DOWN * 0.45 + LEFT * 2.9)
        r2c = MathTex("34").scale(0.8).shift(tc + DOWN * 0.45 + LEFT * 0.5)
        r2t = MathTex("46").scale(0.8).shift(tc + DOWN * 0.45 + RIGHT * 1.6)
        r2s = MathTex("80").scale(0.8).shift(tc + DOWN * 0.45 + RIGHT * 3.4)
        self.play(Write(r2), Write(r2c), Write(r2t), Write(r2s))
        self.wait(1.5)
        r3 = Tex("Total").scale(0.75).shift(tc + DOWN * 1.35 + LEFT * 2.9)
        r3c = MathTex("80").scale(0.8).shift(tc + DOWN * 1.35 + LEFT * 0.5)
        r3t = MathTex("120").scale(0.8).shift(tc + DOWN * 1.35 + RIGHT * 1.6)
        r3s = MathTex("200").scale(0.8).shift(tc + DOWN * 1.35 + RIGHT * 3.4)
        self.play(Write(r3), Write(r3c), Write(r3t), Write(r3s))
        self.wait(2)
        b4_note = Tex("Check the margins before you use it").scale(0.95).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4_note))
        self.wait(3)

        # --- Band 5 (subtopic_3): reading probabilities off the table ---
        self.next_band(5)
        b5_t = Tex("The denominator is where the marks live").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"P(\text{taxi}) = \frac{120}{200} = 0{,}6").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"P(\text{under 30 AND taxi}) = \frac{74}{200} = 0{,}37").scale(1.0).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"\text{Of the under-30s: } \frac{74}{120} = 61{,}7\%").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = MathTex(r"\text{Of the older group: } \frac{46}{80} = 57{,}5\%").scale(1.0).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("Ask ``out of whom?'' before writing anything").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the coin tree ---
        self.next_band(6)
        b6_t = Tex("Tree diagram: toss two coins").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        root = band_shift(6) + LEFT * 4.0 + DOWN * 0.4
        s1h = band_shift(6) + LEFT * 1.5 + UP * 0.9
        s1t = band_shift(6) + LEFT * 1.5 + DOWN * 1.7
        self.play(Create(Line(root, s1h)), Create(Line(root, s1t)))
        l_h = Tex("H").scale(0.9).shift(s1h + LEFT * 0.4)
        l_t = Tex("T").scale(0.9).shift(s1t + LEFT * 0.4)
        self.play(Write(l_h), Write(l_t))
        ends = [
            (s1h, band_shift(6) + RIGHT * 1.0 + UP * 1.4, "HH"),
            (s1h, band_shift(6) + RIGHT * 1.0 + UP * 0.4, "HT"),
            (s1t, band_shift(6) + RIGHT * 1.0 + DOWN * 1.2, "TH"),
            (s1t, band_shift(6) + RIGHT * 1.0 + DOWN * 2.2, "TT"),
        ]
        for start, end, name in ends:
            self.play(Create(Line(start, end)), run_time=0.6)
            self.play(Write(Tex(name).scale(0.85).shift(end + RIGHT * 0.45)), run_time=0.6)
        self.wait(2)
        b6_l1 = Tex("HT and TH are DIFFERENT paths").scale(0.95).shift(band_shift(6) + RIGHT * 3.2 + UP * 1.3)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"P(HH) = 0{,}5 \times 0{,}5 = 0{,}25").scale(0.95).shift(band_shift(6) + RIGHT * 3.2 + UP * 0.1)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2)
        b6_l3 = Tex("Multiply ALONG the branches").scale(0.95).shift(band_shift(6) + RIGHT * 3.2 + DOWN * 1.0)
        self.play(Write(b6_l3))
        self.wait(3)

        # --- Band 7 (subtopic_4): is the game fair? ---
        self.next_band(7)
        b7_t = Tex("R5,00 to play, R15,00 for two heads").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex("Over 100 plays: money in $= 100 \\times$ R5 = R500").scale(0.95).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("25 expected wins: out $= 25 \\times$ R15 = R375").scale(0.95).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("Stall keeps R125 per 100 plays — UNFAIR").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = MathTex(r"\text{Fair prize: } 500 \div 25 = 20").scale(1.05).shift(band_shift(7) + DOWN * 1.6)
        b7_l5 = Tex("Fair game: money in = money out — R20,00").scale(0.95).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l4))
        self.wait(2)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): from never to always ---
        self.next_band(8)
        b8_t = Tex("From never to always").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("0 = impossible; 1 = certain; $\\tfrac{1}{2}$ = coin toss").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("Negative, or bigger than 1? A mistake —").scale(1.0).shift(band_shift(8) + UP * 0.3)
        b8_l3 = Tex("and a free check on every answer").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = MathTex(r"\text{Red: } \frac{12}{25} = 0{,}48 = 48\%").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2)
        b8_l5 = MathTex(r"\text{Not red: } 1 - 0{,}48 = 0{,}52").scale(1.0).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): counting instead of guessing ---
        self.next_band(9)
        b9_t = Tex("Counting instead of guessing").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Thinking: 5 yellow of 25 = 1 in 5 = 20\\%").scale(1.0).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("Counting: 128 of 200 taxis = 64\\%").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("28 heads in 50 is not a cheating coin —").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        b9_l4 = Tex("small tries wander; the coin has no memory").scale(1.0).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("Narrowed group? New denominator: $\\tfrac{74}{120}$ vs $\\tfrac{46}{80}$").scale(0.85).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): is the game fair? ---
        self.next_band(10)
        b10_t = Tex("Is the game fair?").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("List everything: HH, HT, TH, TT").scale(1.0).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = MathTex(r"P(\text{two heads}) = \tfrac{1}{2} \times \tfrac{1}{2} = \tfrac{1}{4}").scale(1.0).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("100 plays: R500 in, R375 out —").scale(1.0).shift(band_shift(10) + DOWN * 0.7)
        b10_l4 = Tex("the stall keeps R125").scale(1.0).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex("Fair prize: R500 $\\div$ 25 = R20,00").scale(1.05).shift(band_shift(10) + DOWN * 2.4)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        b10_l6 = Tex("Nobody can sell you a bad bet now").scale(0.95).shift(band_shift(10) + DOWN * 3.2)
        self.play(Write(b10_l6))
        self.wait(4)
