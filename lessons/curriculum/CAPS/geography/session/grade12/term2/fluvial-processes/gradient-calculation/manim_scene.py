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

# Band-layout whiteboard scene for the gradient-calculation session duo.
# Mapwork calculation lesson: every worked line appears exactly as the
# script speaks it (VI = 1200 - 900 = 300 m; HE = 4,5 km = 4500 m;
# gradient = 300/4500 = 1:15), with red strikes on the script-named traps
# (1:66,7 mixed units; 15:1 inverted). Exporter-safe primitives only
# (Tex/MathTex/Line/Arrow/Dot/Circle/Rectangle/VGroup); add-only lifecycle.
#
# Subtopic shares (subtopics.json, total 1480 s):
# 210/230/230/250 expert, 180/190/190 simplifier. Bands 0-7 = Part 1
# (two per expert subtopic), bands 8-10 = fresh Part 2 bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class GradientCalculationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(13)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): definition and formula ---
        title = Tex("Average Gradient").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        g1 = Tex(r"How steeply the land rises or falls").scale(1.1).shift(UP * 1.2)
        self.play(Write(g1))
        self.wait(2)
        g2 = MathTex(r"\text{Gradient} = \frac{\text{VI}}{\text{HE}}").scale(1.25).shift(UP * 0.1)
        self.play(Write(g2))
        self.play(Create(SurroundingRectangle(g2, color=GREEN)))
        self.wait(2.5)
        g3 = Tex(r"VI = vertical interval (rise)").scale(1.05).shift(DOWN * 1.2)
        g4 = Tex(r"HE = horizontal equivalent (run)").scale(1.05).shift(DOWN * 2.0)
        self.play(Write(g3))
        self.wait(2)
        self.play(Write(g4))
        self.wait(2)
        g5 = Tex(r"Answer as 1 : $x$ — climb 1 m per $x$ m along").scale(1.0).shift(DOWN * 2.9)
        self.play(Write(g5))
        self.wait(3)

        # --- Band 1 (subtopic_1): the interpretation rule ---
        self.next_band(1)
        b1_t = Tex("Bigger $x$ = GENTLER slope").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        # Two hand-built slope lines: steep 1:15 vs gentle 1:150
        steep = Line(band_shift(1) + LEFT * 4.6 + DOWN * 1.0, band_shift(1) + LEFT * 1.6 + UP * 1.0,
                     color=YELLOW, stroke_width=5)
        steep_lab = Tex(r"1 : 15 — steep").scale(0.95).shift(band_shift(1) + LEFT * 3.2 + UP * 1.4)
        gentle = Line(band_shift(1) + RIGHT * 0.6 + DOWN * 1.0, band_shift(1) + RIGHT * 5.0 + DOWN * 0.5,
                      color=YELLOW, stroke_width=5)
        gentle_lab = Tex(r"1 : 150 — gentle").scale(0.95).shift(band_shift(1) + RIGHT * 2.8 + UP * 0.2)
        self.play(Create(steep), Write(steep_lab))
        self.wait(2)
        self.play(Create(gentle), Write(gentle_lab))
        self.wait(2)
        r1 = Tex(r"1 : 5 — brutally steep; 1 : 500 — barely felt").scale(1.0).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(r1))
        self.wait(2)
        r2 = Tex(r"The metre of climb is diluted across more walking").scale(0.95).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(r2))
        self.wait(3)

        # --- Band 2 (subtopic_2): harvesting the VI ---
        self.next_band(2)
        b2_t = Tex("Ingredient 1: the vertical interval").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        v1 = Tex(r"Trig beacon 251 (triangle symbol): 1 200 m").scale(1.0).shift(band_shift(2) + UP * 1.2)
        v2 = Tex(r"Spot height (dot + number): 900 m").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(v1))
        self.wait(2)
        self.play(Write(v2))
        self.wait(2)
        v3 = MathTex(r"\text{VI} = 1\,200 - 900").scale(1.15).shift(band_shift(2) + DOWN * 0.6)
        v4 = MathTex(r"\text{VI} = 300 \text{ m}").scale(1.15).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(v3))
        self.wait(2)
        self.play(Write(v4))
        self.play(Create(SurroundingRectangle(v4, color=GREEN)))
        self.wait(2)
        v5 = Tex(r"Write the subtraction — the memo pays for it").scale(0.95).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(v5))
        self.wait(3)

        # --- Band 3 (subtopic_2): harvesting the HE + unit discipline ---
        self.next_band(3)
        b3_t = Tex("Ingredient 2: the horizontal equivalent").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        h1 = Tex(r"Ruler on a 1:50 000 sheet reads 9 cm").scale(1.0).shift(band_shift(3) + UP * 1.2)
        self.play(Write(h1))
        self.wait(2)
        h2 = MathTex(r"9 \times 50\,000 = 450\,000 \text{ cm}").scale(1.1).shift(band_shift(3) + UP * 0.3)
        h3 = MathTex(r"450\,000 \div 100 = 4\,500 \text{ m}").scale(1.1).shift(band_shift(3) + DOWN * 0.6)
        h4 = MathTex(r"4\,500 \div 1\,000 = 4{,}5 \text{ km}").scale(1.1).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(h2))
        self.wait(2)
        self.play(Write(h3))
        self.wait(2)
        self.play(Write(h4))
        self.wait(2)
        h5 = Tex(r"Same units before dividing: HE = 4 500 m").scale(1.0).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(h5))
        self.play(Create(SurroundingRectangle(h5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the four-line exam layout ---
        self.next_band(4)
        b4_t = Tex("The layout the memo rewards").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        l1 = MathTex(r"\text{Gradient} = \frac{\text{VI}}{\text{HE}}").scale(1.1).shift(band_shift(4) + UP * 1.1)
        l2 = MathTex(r"= \frac{300 \text{ m}}{4\,500 \text{ m}}").scale(1.1).shift(band_shift(4) + UP * 0.0)
        l3 = MathTex(r"= \frac{1}{15} \quad (4\,500 \div 300 = 15)").scale(1.1).shift(band_shift(4) + DOWN * 1.1)
        l4 = MathTex(r"\text{Gradient} = 1 : 15").scale(1.2).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(l1))
        self.wait(2)
        self.play(Write(l2))
        self.wait(2)
        self.play(Write(l3))
        self.wait(2)
        self.play(Write(l4))
        self.play(Create(SurroundingRectangle(l4, color=GREEN)))
        self.wait(2)
        l5 = Tex(r"0,067 or $\frac{300}{4500}$ left unsimplified: no mark").scale(0.95).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): interpretation + the word average ---
        self.next_band(5)
        b5_t = Tex("Interpret it, then defend ``average''").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        i1 = Tex(r"1 : 15 = rise 1 m per 15 m travelled").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(i1))
        self.wait(2)
        i2 = Tex(r"For land: noticeably steep — trucks labour,").scale(1.0).shift(band_shift(5) + UP * 0.2)
        i2b = Tex(r"railways refuse (they want gentler than 1 : 50)").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(i2))
        self.play(Write(i2b))
        self.wait(2.5)
        i3 = Tex(r"``Average'': the real land may dip and climb;").scale(1.0).shift(band_shift(5) + DOWN * 1.6)
        i3b = Tex(r"1 : 15 smears total rise over total distance").scale(1.0).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(i3))
        self.wait(2)
        self.play(Write(i3b))
        self.wait(3)

        # --- Band 6 (subtopic_4): the three verification checks ---
        self.next_band(6)
        b6_t = Tex("Thirty seconds, three checks").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        c1 = Tex(r"1. Sense: 0,15 or 15 000 screams unit error").scale(1.0).shift(band_shift(6) + UP * 1.1)
        c2 = MathTex(r"2.\; 15 \times 300 = 4\,500 \;\checkmark").scale(1.05).shift(band_shift(6) + UP * 0.1)
        c3 = Tex(r"3. Units: both in metres before dividing").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(c1))
        self.wait(2.5)
        self.play(Write(c2))
        self.wait(2.5)
        self.play(Write(c3))
        self.wait(2)
        c4 = Tex(r"Pass all three and the answer is safe").scale(1.0).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(c4))
        self.play(Create(SurroundingRectangle(c4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the traps, struck out ---
        self.next_band(7)
        b7_t = Tex("The traps that cost matrics marks").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        t1 = MathTex(r"300 \div 4{,}5 = 1 : 66{,}7 \;\; \text{(mixed units)}").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(t1))
        self.play(Create(strike(t1)))
        self.wait(2.5)
        t2 = MathTex(r"15 : 1 \;\; \text{(inverted — the 1 is the climb)}").scale(1.05).shift(band_shift(7) + UP * 0.1)
        self.play(Write(t2))
        self.play(Create(strike(t2)))
        self.wait(2.5)
        t3 = Tex(r"Negative VI? Take the absolute difference").scale(1.0).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(t3))
        self.wait(2)
        t4 = Tex(r"Measure sharp: 2 mm off = 100 m of ground").scale(1.0).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(t4))
        self.wait(2)
        t5 = Tex(r"Method: heights, VI; distance, HE in m;").scale(0.95).shift(band_shift(7) + DOWN * 2.7)
        t5b = Tex(r"formula, substitute, 1 : $x$, interpret, check").scale(0.95).shift(band_shift(7) + DOWN * 3.4)
        self.play(Write(t5))
        self.play(Write(t5b))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the ramp and the staircase ---
        self.next_band(8)
        b8_t = Tex("The ramp and the staircase").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        # Stairs: steep line; ramp: gentle line — same height gained
        st = Line(band_shift(8) + LEFT * 4.6 + DOWN * 0.8, band_shift(8) + LEFT * 2.8 + UP * 1.0,
                  color=YELLOW, stroke_width=5)
        st_lab = Tex(r"stairs: 1 up per 2 along").scale(0.9).shift(band_shift(8) + LEFT * 3.4 + UP * 1.5)
        rp = Line(band_shift(8) + LEFT * 0.8 + DOWN * 0.8, band_shift(8) + RIGHT * 5.0 + DOWN * 0.2,
                  color=YELLOW, stroke_width=5)
        rp_lab = Tex(r"ramp: 1 up per 20 along = 1 : 20").scale(0.9).shift(band_shift(8) + RIGHT * 2.2 + UP * 0.5)
        self.play(Create(st), Write(st_lab))
        self.wait(2)
        self.play(Create(rp), Write(rp_lab))
        self.wait(2.5)
        s1 = Tex(r"Sugar in a cup vs a 2-litre jug: spread thinner").scale(0.95).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(s1))
        self.wait(2.5)
        s2 = Tex(r"Bigger second number, gentler slope. Always.").scale(1.0).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(s2))
        self.play(Create(SurroundingRectangle(s2, color=GREEN)))
        self.wait(2)
        s3 = Tex(r"Up = VI, along = HE, the pair = gradient").scale(0.95).shift(band_shift(8) + DOWN * 3.4)
        self.play(Write(s3))
        self.wait(3)

        # --- Band 9 (subtopic_6): two numbers, both speaking metres ---
        self.next_band(9)
        b9_t = Tex("Two numbers off the map, both in metres").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        n1 = Tex(r"Triangle = trig beacon 251: 1 200 m").scale(1.0).shift(band_shift(9) + UP * 1.2)
        n2 = Tex(r"Dot = spot height: 900 m").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(n1))
        self.wait(2)
        self.play(Write(n2))
        self.wait(2)
        n3 = MathTex(r"\text{Up} = 1\,200 - 900 = 300 \text{ m}").scale(1.1).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(n3))
        self.wait(2.5)
        n4 = MathTex(r"9 \text{ cm} \times 50\,000 = 450\,000 \text{ cm} = 4\,500 \text{ m}").scale(1.0).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(n4))
        self.wait(2.5)
        n5 = Tex(r"Rands $\div$ cents means nothing — same units first!").scale(0.95).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(n5))
        self.play(Create(SurroundingRectangle(n5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): share it out, say it in one line ---
        self.next_band(10)
        b10_t = Tex("Share it out, then say it in one line").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        z1 = Tex(r"R4 500 buys how many R300 vouchers? 15").scale(1.0).shift(band_shift(10) + UP * 1.2)
        self.play(Write(z1))
        self.wait(2)
        z2 = MathTex(r"\text{Gradient} = \frac{300 \text{ m}}{4\,500 \text{ m}} = \frac{1}{15}").scale(0.96).shift(band_shift(10) + UP * 0.1)
        self.play(Write(z2))
        self.wait(2.5)
        z3 = MathTex(r"\text{Gradient} = 1 : 15").scale(1.2).shift(band_shift(10) + DOWN * 1.0)
        self.play(Write(z3))
        self.play(Create(SurroundingRectangle(z3, color=GREEN)))
        self.wait(2)
        z4 = Tex(r"Check: $300 \times 15 = 4\,500$").scale(1.0).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(z4))
        self.wait(2)
        z5 = Tex(r"Say it: 1 m up per 15 m along — properly steep").scale(0.95).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(z5))
        self.wait(2)
        z6 = Tex(r"Guards: metres both sides; the 1 is the climb").scale(0.95).shift(band_shift(10) + DOWN * 3.4)
        self.play(Write(z6))
        self.wait(4)
