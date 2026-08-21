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

# BAND LAYOUT: sequential vertical bands, one frame-height each; the camera
# moves down between teaching steps and nothing is ever removed. Only
# exporter-supported mobjects (Tex/MathTex, Line, Dot, Rectangle/
# SurroundingRectangle) with write-only reveals — no sub-part transforms.
# The 0-to-1 scale, the two-way table and the coin tree are hand-built from
# Lines and Tex cells.
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
        title = Tex("Probability in Everyday Contexts").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        axis = Line(LEFT * 4.5, RIGHT * 4.5).shift(UP * 0.2)
        self.play(Create(axis))
        d0 = Dot(LEFT * 4.5 + UP * 0.2)
        dh = Dot(UP * 0.2)
        d1 = Dot(RIGHT * 4.5 + UP * 0.2)
        self.play(Create(d0), Create(dh), Create(d1))
        l01 = Tex("0 — impossible").scale(0.85).shift(LEFT * 4.0 + DOWN * 0.6)
        l02 = Tex("0,5 — even chance").scale(0.85).shift(DOWN * 0.6)
        l03 = Tex("1 — certain").scale(0.85).shift(RIGHT * 4.0 + DOWN * 0.6)
        self.play(Write(l01))
        self.play(Write(l02))
        self.play(Write(l03))
        self.wait(2)
        l04 = Tex("Nothing negative, nothing above 1 — ever").scale(0.95).shift(DOWN * 1.6)
        self.play(Write(l04))
        self.play(Create(SurroundingRectangle(l04, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): three costumes and the complement ---
        self.next_band(1)
        b1_t = Tex("One chance, three costumes").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("Jar: 14 blue + 10 white + 16 pink = 40").scale(0.95).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"P(\text{blue}) = \frac{14}{40} = 0{,}35 = 35\%").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)
        b1_l3 = MathTex(r"P(\text{not blue}) = 1 - 0{,}35 = 0{,}65").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("``Not'' or ``at least one'': use the complement").scale(0.95).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): theoretical vs relative frequency ---
        self.next_band(2)
        b2_t = Tex("Thinking vs counting").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex("Theoretical: reasoned BEFORE, equal outcomes").scale(0.9).shift(band_shift(2) + UP * 1.2)
        b2_l2 = MathTex(r"P(\text{pink}) = \frac{16}{40} = 0{,}4").scale(1.0).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("Relative frequency: counted AFTER").scale(0.9).shift(band_shift(2) + DOWN * 0.6)
        b2_l4 = MathTex(r"\frac{93}{150} = 0{,}62 \text{ of taxis head for town}").scale(0.95).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)
        b2_l5 = Tex("Unequal outcomes? Only counting works").scale(0.9).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): samples wander; coins have no memory ---
        self.next_band(3)
        b3_t = Tex("Samples wander; coins have no memory").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"60 \text{ tosses: } \frac{27}{60} = 0{,}45 \ne 0{,}5").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("Not loaded — small runs drift").scale(0.95).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("6 000 tosses settle close to 0,5").scale(0.95).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("Three heads in a row: next toss is STILL 0,5").scale(0.95).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex("Each toss is independent — nothing is ``due''").scale(0.95).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the transport two-way table ---
        self.next_band(4)
        b4_t = Tex("The transport survey: a two-way table").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        grid_h1 = Line(LEFT * 4.2, RIGHT * 4.2).shift(band_shift(4) + UP * 0.9)
        grid_h2 = Line(LEFT * 4.2, RIGHT * 4.2).shift(band_shift(4) + UP * 0.1)
        grid_h3 = Line(LEFT * 4.2, RIGHT * 4.2).shift(band_shift(4) + DOWN * 0.7)
        grid_v1 = Line(UP * 1.5, DOWN * 1.4).shift(band_shift(4) + LEFT * 1.6)
        grid_v2 = Line(UP * 1.5, DOWN * 1.4).shift(band_shift(4) + RIGHT * 0.8)
        for g in (grid_h1, grid_h2, grid_h3, grid_v1, grid_v2):
            self.play(Create(g), run_time=0.5)
        hdr = Tex("Walk / Taxi / Total").scale(0.8).shift(band_shift(4) + UP * 1.3 + RIGHT * 0.6)
        self.play(Write(hdr))
        r1 = Tex("Under 16: 36 / 64 / 100").scale(0.8).shift(band_shift(4) + UP * 0.5)
        r2 = Tex("16 and over: 28 / 32 / 60").scale(0.8).shift(band_shift(4) + DOWN * 0.3)
        r3 = Tex("Total: 64 / 96 / 160").scale(0.8).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(r1))
        self.wait(1.5)
        self.play(Write(r2))
        self.wait(1.5)
        self.play(Write(r3))
        self.wait(2)
        b4_l1 = Tex("Check the margins before anything else").scale(0.9).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): reading probabilities off the table ---
        self.next_band(5)
        b5_t = Tex("Reading probabilities off the table").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"P(\text{taxi}) = \frac{96}{160} = 0{,}6").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"P(\text{under 16 AND taxi}) = \frac{64}{160} = 0{,}4").scale(1.0).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"\text{Of the under-16s: } \frac{64}{100} = 0{,}64").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_l4 = MathTex(r"\text{Of the 16-and-overs: } \frac{32}{60} = 0{,}533").scale(1.0).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("The denominator follows the group — ask ``out of whom?''").scale(0.85).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the coin tree ---
        self.next_band(6)
        b6_t = Tex("Two coins: the tree").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        root = Dot(band_shift(6) + UP * 1.2 + LEFT * 3.0)
        self.play(Create(root))
        br1 = Line(band_shift(6) + UP * 1.2 + LEFT * 3.0, band_shift(6) + UP * 1.8 + LEFT * 1.2)
        br2 = Line(band_shift(6) + UP * 1.2 + LEFT * 3.0, band_shift(6) + UP * 0.6 + LEFT * 1.2)
        self.play(Create(br1), Create(br2))
        n1 = Tex("H").scale(0.9).shift(band_shift(6) + UP * 1.8 + LEFT * 0.9)
        n2 = Tex("T").scale(0.9).shift(band_shift(6) + UP * 0.6 + LEFT * 0.9)
        self.play(Write(n1), Write(n2))
        self.wait(1.5)
        b6_l1 = Tex("Ends: HH, HT, TH, TT — four paths").scale(0.95).shift(band_shift(6) + DOWN * 0.3)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex("HT and TH are DIFFERENT paths").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2)
        b6_l3 = MathTex(r"P(\text{TT}) = 0{,}5 \times 0{,}5 = 0{,}25").scale(1.0).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("Multiply ALONG the branches").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): is the game fair? ---
        self.next_band(7)
        b7_t = Tex("Is the game fair?").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex("R4 a turn; R12 for two tails; 100 turns").scale(0.95).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"\text{In: } 100 \times 4 = 400").scale(1.0).shift(band_shift(7) + UP * 0.3)
        b7_l3 = MathTex(r"\text{Out: } 25 \times 12 = 300").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("Stall keeps R100 of every R400 staked").scale(0.95).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = MathTex(r"\text{Fair prize: } 400 \div 25 = 16").scale(1.05).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): from never to always ---
        self.next_band(8)
        b8_t = Tex("From never to always").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        axis2 = Line(LEFT * 4.0, RIGHT * 4.0).shift(band_shift(8) + UP * 1.0)
        self.play(Create(axis2))
        b8_l1 = Tex("0 never — 0,5 coin — 1 always").scale(0.95).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"\frac{14}{40} = 0{,}35 = 35\% \text{ — same fact, three outfits}").scale(0.9).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2)
        b8_l3 = Tex("Not blue? What is left: 1 $-$ 0,35 = 0,65").scale(0.95).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("Negative or above 1 = a free error alarm").scale(0.95).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): counting instead of guessing ---
        self.next_band(9)
        b9_t = Tex("Counting instead of guessing").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Think it: 16 pink of 40 = 40\\%").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("Count it: 93 of 150 taxis = 62\\%").scale(0.95).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("More tries: counting creeps toward thinking").scale(0.95).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = MathTex(r"\text{Under 16: } \frac{64}{100}; \;\; 16+: \frac{32}{60}").scale(0.95).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex("Narrow group, narrow denominator — out of whom?").scale(0.9).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): is the game fair? ---
        self.next_band(10)
        b10_t = Tex("Is the game fair?").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("HH, HT, TH, TT — two tails is 1 in 4").scale(0.95).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = MathTex(r"\text{In: } 400; \;\; \text{out: } 25 \times 12 = 300").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("Stall keeps R100 — honestly, openly, every time").scale(0.9).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = MathTex(r"\text{Fair: } 400 \div 25 = \text{R}16").scale(1.05).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex("Cost, winning fraction, prize — then compare").scale(0.95).shift(band_shift(10) + DOWN * 2.4)
        self.play(Write(b10_l5))
        self.wait(4)
