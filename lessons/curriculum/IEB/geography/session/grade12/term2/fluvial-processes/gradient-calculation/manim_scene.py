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

# Band-layout whiteboard scene for the gradient-calculation duo lesson.
# Worked problem: trig beacon 89 at 1 350 m, spot height 1 100 m, 5 km
# apart on a 1:50 000 sheet -> VI 250 m, HE 5 000 m, gradient 1 : 20.
# Exporter-safe primitives only (Tex/MathTex/Line/Arrow/Dot/Circle/
# Rectangle/VGroup); add-only lifecycle; camera moves down one
# frame-height per band.
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
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): definition and formula ---
        title = Tex("What Gradient Means").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s1 = Tex(r"Contour spacing = impression; gradient = number").scale(0.95).shift(UP * 1.3)
        self.play(Write(s1))
        self.wait(2)
        f1 = MathTex(r"\text{Gradient} = \frac{\text{Vertical Interval}}{\text{Horizontal Equivalent}}").scale(1.05).shift(UP * 0.2)
        self.play(Write(f1))
        self.play(Create(SurroundingRectangle(f1, color=GREEN)))
        self.wait(2.5)
        s2 = Tex(r"Answer form: $1 : x$ — 1 m up per $x$ m along").scale(1.0).shift(DOWN * 1.0)
        self.play(Write(s2))
        self.wait(2)
        s3 = Tex(r"$1:4$ punishing; $1:400$ feels flat").scale(1.0).shift(DOWN * 1.9)
        self.play(Write(s3))
        self.wait(2.5)
        s4 = Tex(r"Roads, rail, rivers, vineyards — all live on this").scale(0.9).shift(DOWN * 2.8)
        self.play(Write(s4))
        self.wait(3)

        # --- Band 1 (subtopic_1): the interpretation rule ---
        self.next_band(1)
        b1_t = Tex("Bigger number after the colon = GENTLER").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        # Steep slope: 1 in 20 drawn short and sharp
        st = Line(band_shift(1) + LEFT * 4.4 + DOWN * 1.0, band_shift(1) + LEFT * 1.4 + UP * 0.6,
                  color=RED, stroke_width=5)
        st_lab = Tex(r"$1:20$ — steep").scale(0.9).shift(band_shift(1) + LEFT * 3.0 + UP * 1.1)
        self.play(Create(st), Write(st_lab))
        self.wait(2)
        # Gentle slope: 1 in 200 drawn long and shallow
        gt = Line(band_shift(1) + RIGHT * 0.2 + DOWN * 1.0, band_shift(1) + RIGHT * 4.6 + DOWN * 0.55,
                  color=BLUE, stroke_width=5)
        gt_lab = Tex(r"$1:200$ — gentle").scale(0.9).shift(band_shift(1) + RIGHT * 2.4 + UP * 0.1)
        self.play(Create(gt), Write(gt_lab))
        self.wait(2)
        r1 = Tex(r"Same 1 m of climb, thinned over a longer walk").scale(0.95).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(r1))
        self.play(Create(SurroundingRectangle(r1, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): harvesting the VI ---
        self.next_band(2)
        b2_t = Tex("Ingredient 1: the vertical interval").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        tb = Tex(r"$\triangle$ 89 trig beacon: 1 350 m (surveyed)").scale(1.0).shift(band_shift(2) + UP * 1.2)
        sh = Tex(r"$\bullet$ spot height: 1 100 m (exact)").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(tb))
        self.wait(2)
        self.play(Write(sh))
        self.wait(2)
        vi = MathTex(r"VI = 1\,350 - 1\,100 = 250 \text{ m}").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(vi))
        self.play(Create(SurroundingRectangle(vi, color=GREEN)))
        self.wait(2.5)
        vi2 = Tex(r"Write the subtraction — it earns credit").scale(0.95).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(vi2))
        self.wait(3)

        # --- Band 3 (subtopic_2): harvesting the HE + unit discipline ---
        self.next_band(3)
        b3_t = Tex("Ingredient 2: the horizontal equivalent").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        h1 = Tex(r"Ruler reads 10 cm on the 1:50 000 sheet").scale(1.0).shift(band_shift(3) + UP * 1.2)
        h2 = MathTex(r"10 \times 50\,000 = 500\,000 \text{ cm}").scale(1.0).shift(band_shift(3) + UP * 0.3)
        h3 = MathTex(r"= 5\,000 \text{ m} = 5 \text{ km}").scale(1.0).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(h1))
        self.wait(2)
        self.play(Write(h2))
        self.wait(2)
        self.play(Write(h3))
        self.wait(2)
        u1 = Tex(r"UNITS: metres over kilometres = gibberish").scale(0.95).shift(band_shift(3) + DOWN * 1.5)
        u2 = MathTex(r"HE = 5 \text{ km} = 5\,000 \text{ m}").scale(1.0).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(u1))
        self.wait(2)
        self.play(Write(u2))
        self.play(Create(SurroundingRectangle(u2, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the four-line written layout ---
        self.next_band(4)
        b4_t = Tex("The four paying lines").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        l1 = MathTex(r"1.\ \text{Gradient} = \frac{VI}{HE}").scale(0.95).shift(band_shift(4) + UP * 1.2)
        l2 = MathTex(r"2.\ = \frac{250 \text{ m}}{5\,000 \text{ m}}").scale(0.95).shift(band_shift(4) + UP * 0.2)
        l3 = MathTex(r"3.\ = \frac{1}{20}").scale(0.95).shift(band_shift(4) + DOWN * 0.8)
        l4 = MathTex(r"4.\ \text{Gradient} = 1 : 20").scale(1.1).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(l1))
        self.wait(2)
        self.play(Write(l2))
        self.wait(2)
        self.play(Write(l3))
        self.wait(2)
        self.play(Write(l4))
        self.play(Create(SurroundingRectangle(l4, color=GREEN)))
        self.wait(2)
        l5 = Tex(r"Not 0,05; not 250/5\,000 — the ratio is the currency").scale(0.9).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): interpretation + the word average ---
        self.next_band(5)
        b5_t = Tex("Interpret it, then explain ``average''").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        p1 = Tex(r"$1:20$: rises 1 m per 20 m along — steep").scale(1.0).shift(band_shift(5) + UP * 1.2)
        p2 = Tex(r"Truck labours; rail needs gentler than $\sim 1:50$").scale(0.95).shift(band_shift(5) + UP * 0.3)
        self.play(Write(p1))
        self.wait(2)
        self.play(Write(p2))
        self.wait(2.5)
        # Straight-line summary over a wavy reality
        wav1 = Line(band_shift(5) + LEFT * 3.8 + DOWN * 1.6, band_shift(5) + LEFT * 1.6 + DOWN * 2.3, color=BLUE, stroke_width=4)
        wav2 = Line(band_shift(5) + LEFT * 1.6 + DOWN * 2.3, band_shift(5) + RIGHT * 0.6 + DOWN * 1.9, color=BLUE, stroke_width=4)
        wav3 = Line(band_shift(5) + RIGHT * 0.6 + DOWN * 1.9, band_shift(5) + RIGHT * 3.6 + DOWN * 0.7, color=BLUE, stroke_width=4)
        chord = Line(band_shift(5) + LEFT * 3.8 + DOWN * 1.6, band_shift(5) + RIGHT * 3.6 + DOWN * 0.7, color=YELLOW, stroke_width=4)
        wav_lab = Tex(r"average = straight-line summary of a crooked land").scale(0.85).shift(band_shift(5) + DOWN * 3.1)
        self.play(Create(wav1), Create(wav2), Create(wav3))
        self.wait(2)
        self.play(Create(chord))
        self.play(Write(wav_lab))
        self.wait(3)

        # --- Band 6 (subtopic_4): the three verification checks ---
        self.next_band(6)
        b6_t = Tex("Three checks, thirty seconds").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        c1 = Tex(r"1. Sense: hill country, not $1:0{,}02$ or $1:20\,000$").scale(0.95).shift(band_shift(6) + UP * 1.1)
        c2 = MathTex(r"2.\ \text{Reverse: } 250 \times 20 = 5\,000").scale(0.95).shift(band_shift(6) + UP * 0.1)
        c3 = Tex(r"3. Units: both metres at the divide").scale(0.95).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(c1))
        self.wait(2.5)
        self.play(Write(c2))
        self.wait(2.5)
        self.play(Write(c3))
        self.play(Create(SurroundingRectangle(c3, color=GREEN)))
        self.wait(2)
        c4 = Tex(r"Pass all three and the answer is safe").scale(0.95).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(c4))
        self.wait(3)

        # --- Band 7 (subtopic_4): the traps, struck out ---
        self.next_band(7)
        b7_t = Tex("The four traps").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        t1 = MathTex(r"\frac{250}{5} \text{ (mixed units)}").scale(0.95).shift(band_shift(7) + UP * 1.2)
        self.play(Write(t1))
        self.play(Create(strike(t1)))
        self.wait(2)
        t2 = MathTex(r"20 : 1 \text{ (inverted)}").scale(0.95).shift(band_shift(7) + UP * 0.2)
        self.play(Write(t2))
        self.play(Create(strike(t2)))
        self.wait(2)
        t3 = MathTex(r"-250 \text{ m (wrong-order subtraction)}").scale(0.95).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(t3))
        self.play(Create(strike(t3)))
        self.wait(2)
        t4 = Tex(r"2 mm of ruler error = 100 m of ground").scale(0.95).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(t4))
        self.wait(2)
        t5 = Tex(r"Method: heights, distance, formula, units,").scale(0.9).shift(band_shift(7) + DOWN * 2.7)
        t5b = Tex(r"simplify, interpret, check").scale(0.9).shift(band_shift(7) + DOWN * 3.3)
        self.play(Write(t5))
        self.play(Write(t5b))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the ramp and the staircase ---
        self.next_band(8)
        b8_t = Tex("The ramp and the staircase").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        # Staircase: short steep line; ramp: long shallow line to same height
        stair = Line(band_shift(8) + LEFT * 4.2 + DOWN * 1.6, band_shift(8) + LEFT * 2.8 + UP * 0.4,
                     color=RED, stroke_width=5)
        stair_lab = Tex(r"stairs: 1 up per 2 along").scale(0.85).shift(band_shift(8) + LEFT * 3.4 + UP * 1.0)
        ramp = Line(band_shift(8) + LEFT * 1.6 + DOWN * 1.6, band_shift(8) + RIGHT * 4.4 + UP * 0.4,
                    color=BLUE, stroke_width=5)
        ramp_lab = Tex(r"ramp: 1 up per 12 along").scale(0.85).shift(band_shift(8) + RIGHT * 1.6 + UP * 1.0)
        self.play(Create(stair), Write(stair_lab))
        self.wait(2)
        self.play(Create(ramp), Write(ramp_lab))
        self.wait(2)
        q1 = Tex(r"Ask the slope: 1 m up = how many along?").scale(0.95).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(q1))
        self.play(Create(SurroundingRectangle(q1, color=GREEN)))
        self.wait(2.5)
        q2 = Tex(r"Teaspoon in a jug: bigger number, gentler slope").scale(0.9).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(q2))
        self.wait(3)

        # --- Band 9 (subtopic_6): two numbers, both speaking metres ---
        self.next_band(9)
        b9_t = Tex("Two numbers, both speaking metres").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        y1 = Tex(r"Up: $1\,350 - 1\,100 = 250$ m (beacon, spot height)").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(y1))
        self.wait(2.5)
        y2 = Tex(r"Along: 10 cm $\times$ 50 000 = 5 km").scale(0.95).shift(band_shift(9) + UP * 0.3)
        self.play(Write(y2))
        self.wait(2.5)
        y3 = Tex(r"Rands $\div$ cents = nonsense; convert first").scale(0.95).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(y3))
        self.wait(2)
        y4 = MathTex(r"5 \text{ km} = 5\,000 \text{ m}").scale(1.05).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(y4))
        self.play(Create(SurroundingRectangle(y4, color=GREEN)))
        self.wait(2)
        y5 = Tex(r"250 up, 5 000 along — both metres, ready").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(y5))
        self.wait(3)

        # --- Band 10 (subtopic_7): share it out, say it in one line ---
        self.next_band(10)
        b10_t = Tex("Share it out, then say it in one line").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        z1 = Tex(r"R5 000 buys how many R250 tickets? 20").scale(1.0).shift(band_shift(10) + UP * 1.2)
        self.play(Write(z1))
        self.wait(2)
        z2 = MathTex(r"\text{Gradient} = \frac{250 \text{ m}}{5\,000 \text{ m}} = \frac{1}{20}").scale(0.96).shift(band_shift(10) + UP * 0.1)
        self.play(Write(z2))
        self.wait(2.5)
        z3 = MathTex(r"\text{Gradient} = 1 : 20").scale(1.2).shift(band_shift(10) + DOWN * 1.0)
        self.play(Write(z3))
        self.play(Create(SurroundingRectangle(z3, color=GREEN)))
        self.wait(2)
        z4 = Tex(r"Check: $250 \times 20 = 5\,000$").scale(1.0).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(z4))
        self.wait(2)
        z5 = Tex(r"Say it: 1 m up per 20 m along — properly steep").scale(0.95).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(z5))
        self.wait(2)
        z6 = Tex(r"Guards: metres both sides; the 1 is the climb").scale(0.95).shift(band_shift(10) + DOWN * 3.4)
        self.play(Write(z6))
        self.wait(4)
