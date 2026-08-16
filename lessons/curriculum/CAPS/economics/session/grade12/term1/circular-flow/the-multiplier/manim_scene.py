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

# Band layout: one frame-tall bands down a long canvas; camera moves down,
# nothing is removed. Exporter-safe mobjects only (Tex/MathTex/Line/Arrow/
# Dot/Circle/Rectangle/VGroup); write-only reveals — no Transform/FadeOut.
#
# Mirrors script.md across the seven subtopics of the duo
# (Expert 1-4: bands 0-6; Simplifier 5-7: bands 7-9), scene time
# apportioned to subtopics.json (210/250/240/240/180/185/185 of 1490 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TheMultiplierSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md plays (~4-5%).
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): autonomous, induced, MPC, MPS ---
        title = Tex("The Multiplier").scale(1.35).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        a1 = Tex(r"Autonomous C: spent even at zero income").scale(1.05).shift(UP * 1.2)
        a2 = Tex(r"Induced C: varies with income").scale(1.05).shift(UP * 0.4)
        self.play(Write(a1))
        self.wait(2)
        self.play(Write(a2))
        self.wait(2)
        cf = MathTex(r"C = C_0 + cY").scale(1.25).shift(DOWN * 0.5)
        self.play(Write(cf))
        self.wait(2)
        mpc = MathTex(r"MPC = \frac{\Delta C}{\Delta Y}, \quad MPS = \frac{\Delta S}{\Delta Y}").scale(0.85).shift(DOWN * 1.7)
        self.play(Write(mpc))
        self.wait(2)
        sum1 = MathTex(r"MPC + MPS = 1").scale(1.15).shift(DOWN * 2.8)
        self.play(Write(sum1))
        self.play(Create(SurroundingRectangle(sum1, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): worked MPC, marginal vs average ---
        self.next_band(1)
        b1_title = Tex(r"Income up R2\,000, spending up R1\,500").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        w1 = MathTex(r"MPC = \frac{1\,500}{2\,000} = 0{,}75").scale(1.15).shift(band_shift(1) + UP * 1.0)
        w2 = MathTex(r"MPS = \frac{500}{2\,000} = 0{,}25").scale(1.15).shift(band_shift(1) + DOWN * 0.2)
        self.play(Write(w1))
        self.wait(2.5)
        self.play(Write(w2))
        self.wait(2)
        w3 = MathTex(r"0{,}75 + 0{,}25 = 1, \text{ as it must}").scale(1.1).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(w3))
        self.play(Create(SurroundingRectangle(w3, color=GREEN)))
        self.wait(2)
        wrong = Tex(r"MPC $=$ share of TOTAL income spent").scale(1.0).shift(band_shift(1) + DOWN * 2.1 + LEFT * 2.4)
        self.play(Write(wrong))
        self.play(Create(strike(wrong)))
        right = Tex(r"Marginal $=$ the EXTRA rand only").scale(1.0).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(right))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the echo and the formula ---
        self.next_band(2)
        b2_title = Tex(r"R1\,000 injected, MPC $= 0{,}8$").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        s1 = MathTex(r"1\,000 + 800 + 640 + 512 + \dots").scale(1.15).shift(band_shift(2) + UP * 1.1)
        self.play(Write(s1))
        self.wait(2.5)
        s2 = MathTex(r"\text{Sum} = \frac{1\,000}{1 - 0{,}8} = \frac{1\,000}{0{,}2} = R5\,000").scale(0.98).shift(band_shift(2) + UP * 0.0)
        self.play(Write(s2))
        self.wait(2.5)
        k1 = MathTex(r"k = \frac{1}{1 - MPC} = \frac{1}{MPS}").scale(1.2).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(k1))
        self.wait(2)
        k2 = MathTex(r"\Delta Y = k \times \Delta J").scale(1.25).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(k2))
        self.play(Create(SurroundingRectangle(k2, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the 45-degree diagram ---
        self.next_band(3)
        b3_title = Tex("The 45-degree diagram").scale(1.15).shift(band_shift(3) + UP * 2.9)
        self.play(Write(b3_title))
        self.wait(1.5)
        o = band_shift(3) + DOWN * 2.9 + LEFT * 5.2
        y_ax = Arrow(o, o + UP * 4.9, buff=0, stroke_width=3)
        x_ax = Arrow(o, o + RIGHT * 9.8, buff=0, stroke_width=3)
        y_lab = Tex("spending").scale(0.7).shift(o + UP * 4.9 + RIGHT * 1.0)
        x_lab = Tex("income Y").scale(0.7).shift(o + RIGHT * 9.8 + DOWN * 0.35)
        self.play(Create(y_ax), Create(x_ax), Write(y_lab), Write(x_lab))
        self.wait(1.5)
        deg45 = Line(o, o + RIGHT * 4.6 + UP * 4.6, color=GREY)
        deg_lab = MathTex(r"45^\circ", color=GREY).scale(0.8).shift(o + RIGHT * 4.9 + UP * 4.3)
        self.play(Create(deg45), Write(deg_lab))
        self.wait(1.5)
        ae1 = Line(o + UP * 1.5, o + RIGHT * 6.0 + UP * 4.5, color=BLUE)
        ae1_lab = MathTex(r"AE_1", color=BLUE).scale(0.8).shift(o + RIGHT * 6.6 + UP * 4.5)
        self.play(Create(ae1), Write(ae1_lab))
        e1 = Dot(o + RIGHT * 3.0 + UP * 3.0, color=YELLOW)
        e1_lab = MathTex(r"E_1").scale(0.75).shift(o + RIGHT * 3.0 + UP * 3.5)
        self.play(Create(e1), Write(e1_lab))
        self.wait(2)
        ae2 = Line(o + UP * 2.2, o + RIGHT * 5.2 + UP * 4.8, color=GREEN)
        ae2_lab = MathTex(r"AE_2", color=GREEN).scale(0.8).shift(o + LEFT * 0.7 + UP * 2.3)
        dj = Arrow(o + RIGHT * 1.0 + UP * 2.0, o + RIGHT * 1.0 + UP * 2.7, buff=0, color=ORANGE)
        dj_lab = MathTex(r"\Delta J", color=ORANGE).scale(0.75).shift(o + RIGHT * 1.7 + UP * 2.4)
        self.play(Create(ae2), Write(ae2_lab))
        self.play(Create(dj), Write(dj_lab))
        self.wait(2)
        e2 = Dot(o + RIGHT * 4.4 + UP * 4.4, color=YELLOW)
        e2_lab = MathTex(r"E_2").scale(0.75).shift(o + RIGHT * 4.4 + UP * 4.9)
        self.play(Create(e2), Write(e2_lab))
        dy = Arrow(o + RIGHT * 3.0 + UP * 0.4, o + RIGHT * 4.4 + UP * 0.4, buff=0, color=ORANGE)
        dy_lab = MathTex(r"\Delta Y > \Delta J", color=ORANGE).scale(0.8).shift(o + RIGHT * 3.7 + DOWN * 0.35)
        self.play(Create(dy), Write(dy_lab))
        self.wait(2)
        note = Tex(r"Horizontal move beats vertical shift").scale(0.85).shift(o + RIGHT * 7.6 + UP * 1.6)
        note2 = Tex(r"— the ratio is $k$").scale(0.85).shift(o + RIGHT * 7.6 + UP * 0.9)
        self.play(Write(note))
        self.play(Write(note2))
        self.wait(3)

        # --- Band 4 (subtopic_3): cases one and two ---
        self.next_band(4)
        b4_title = Tex(r"Case 1: R6 bn injected, MPC $0{,}75$").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        c1 = MathTex(r"k = \frac{1}{1 - 0{,}75} = \frac{1}{0{,}25} = 4").scale(1.1).shift(band_shift(4) + UP * 1.0)
        c2 = MathTex(r"\Delta Y = 4 \times R6\text{ bn} = R24\text{ bn}").scale(1.1).shift(band_shift(4) + UP * 0.0)
        self.play(Write(c1))
        self.wait(2.5)
        self.play(Write(c2))
        self.play(Create(SurroundingRectangle(c2, color=GREEN)))
        self.wait(2)
        interp = Tex(r"Interpret: re-spent round after round").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(interp))
        self.wait(2)
        b4b = Tex(r"Case 2 (backwards): $\Delta Y$ 30, $\Delta J$ 7,5").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4b))
        self.wait(1.5)
        c3 = MathTex(r"k = \frac{30}{7{,}5} = 4 \;\Rightarrow\; MPC = 0{,}75").scale(1.05).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(c3))
        self.play(Create(SurroundingRectangle(c3, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the open-economy multiplier ---
        self.next_band(5)
        b5_title = Tex("Case 3: the open economy leaks 3 ways").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        o1 = MathTex(r"k = \frac{1}{MPS + MPT + MPM}").scale(1.2).shift(band_shift(5) + UP * 1.0)
        self.play(Write(o1))
        self.wait(2.5)
        o2 = MathTex(r"k = \frac{1}{0{,}10 + 0{,}25 + 0{,}15} = \frac{1}{0{,}50} = 2").scale(1.1).shift(band_shift(5) + DOWN * 0.2)
        self.play(Write(o2))
        self.wait(2.5)
        o3 = MathTex(r"\Delta Y = 2 \times R6\text{ bn} = R12\text{ bn, not } R24").scale(1.05).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(o3))
        self.play(Create(SurroundingRectangle(o3, color=GREEN)))
        self.wait(2)
        o4 = Tex(r"Heavy tax + imports $=$ small multiplier;").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        o5 = Tex(r"local spending circulates further").scale(0.95).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(o4))
        self.play(Write(o5))
        self.wait(3)

        # --- Band 6 (subtopic_4): conditions and the reverse gear ---
        self.next_band(6)
        b6_title = Tex("Conditions, and the reverse gear").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        n1 = Tex(r"1. SPARE CAPACITY — else it multiplies prices").scale(0.95).shift(band_shift(6) + UP * 1.2)
        n2 = Tex(r"2. TIME — rounds take months").scale(0.95).shift(band_shift(6) + UP * 0.4)
        n3 = Tex(r"3. FINANCE — borrowing can crowd out").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(n1))
        self.wait(2)
        self.play(Write(n2))
        self.wait(2)
        self.play(Write(n3))
        self.wait(2)
        rev = MathTex(r"\text{Exports} - R5\text{ bn}, \; k=2: \; \Delta Y = -R10\text{ bn}").scale(0.94).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(rev))
        self.play(Create(SurroundingRectangle(rev, color=GREEN)))
        self.wait(2)
        rev2 = Tex(r"Every recession is a multiplier in reverse;").scale(0.95).shift(band_shift(6) + DOWN * 2.3)
        rev3 = Tex(r"accelerator: induced investment multiplies again").scale(0.9).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(rev2))
        self.play(Write(rev3))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): one rand, many pockets ---
        self.next_band(7)
        b7_title = Tex("One rand, many pockets").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        p1 = Tex(r"Road crew paid R1\,000").scale(1.05).shift(band_shift(7) + UP * 1.3)
        self.play(Write(p1))
        self.wait(2)
        chain = MathTex(r"1\,000 \rightarrow 800 \rightarrow 640 \rightarrow 512 \rightarrow \dots").scale(1.1).shift(band_shift(7) + UP * 0.4)
        self.play(Write(chain))
        self.wait(2.5)
        p2 = Tex(r"Bricklayer, spaza, wholesaler, helper,").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        p3 = Tex(r"tavern, barber — six people paid").scale(1.0).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(p2))
        self.play(Write(p3))
        self.wait(2.5)
        p4 = MathTex(r"\text{Town's income up } R5\,000").scale(1.1).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(p4))
        self.play(Create(SurroundingRectangle(p4, color=GREEN)))
        p5 = Tex(r"A spent rand becomes income and goes again").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(p5))
        self.wait(3.5)

        # --- Band 8 (subtopic_6): why the chain gets shorter ---
        self.next_band(8)
        b8_title = Tex("Why the chain gets shorter").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        e1_ = Tex(r"Three exits: SAVED, TAXED, IMPORTED").scale(1.05).shift(band_shift(8) + UP * 1.2)
        self.play(Write(e1_))
        self.wait(2.5)
        e2_ = MathTex(r"\tfrac{1}{5} + \tfrac{1}{4} + 0{,}15 = \text{half exits each stop}").scale(1.0).shift(band_shift(8) + UP * 0.3)
        self.play(Write(e2_))
        self.wait(2.5)
        e3_ = MathTex(r"R1\,000 \text{ adds only } R2\,000, \text{ not } R5\,000").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(e3_))
        self.play(Create(SurroundingRectangle(e3_, color=GREEN)))
        self.wait(2.5)
        e4_ = Tex(r"WHO gets it matters: a poor household").scale(0.95).shift(band_shift(8) + DOWN * 1.6)
        e5_ = Tex(r"spends nearly all — the chain runs long").scale(0.95).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(e4_))
        self.play(Write(e5_))
        self.wait(2.5)
        e6_ = Tex(r"Reverse: one closure empties several tills").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(e6_))
        self.wait(3)

        # --- Band 9 (subtopic_7): budget day ---
        self.next_band(9)
        b9_title = Tex("Three questions on budget day").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        q1 = Tex(r"1. Spare capacity? Else prices rise").scale(1.0).shift(band_shift(9) + UP * 1.2)
        q2 = Tex(r"2. How much leaks? Small leak, long chain").scale(1.0).shift(band_shift(9) + UP * 0.4)
        q3 = Tex(r"3. How long? Rounds land over a year").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(q1))
        self.wait(2.5)
        self.play(Write(q2))
        self.wait(2.5)
        self.play(Write(q3))
        self.wait(2.5)
        q4 = Tex(r"The objection: borrowed money costs interest").scale(0.95).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(q4))
        self.wait(2.5)
        fin = Tex(r"One rand spent $>$ one rand of income").scale(1.05).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(fin))
        self.play(Create(SurroundingRectangle(fin, color=GREEN)))
        self.wait(4)
