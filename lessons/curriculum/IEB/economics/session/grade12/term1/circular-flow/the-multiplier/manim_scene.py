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
        a1 = Tex(r"Autonomous C: continues even at zero income").scale(1.0).shift(UP * 1.2)
        a2 = Tex(r"Induced C: rises and falls with income").scale(1.0).shift(UP * 0.4)
        self.play(Write(a1))
        self.wait(2)
        self.play(Write(a2))
        self.wait(2)
        cf = MathTex(r"C = C_0 + cY").scale(1.2).shift(DOWN * 0.5)
        self.play(Write(cf))
        self.wait(2)
        mp = MathTex(r"MPC = \tfrac{\Delta C}{\Delta Y}, \quad MPS = \tfrac{\Delta S}{\Delta Y}").scale(1.05).shift(DOWN * 1.5)
        self.play(Write(mp))
        self.wait(2)
        one = MathTex(r"MPC + MPS = 1").scale(1.1).shift(DOWN * 2.5)
        self.play(Write(one))
        self.play(Create(SurroundingRectangle(one, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): worked MPC, marginal vs average ---
        self.next_band(1)
        b1_title = Tex("Compute one").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        w1 = MathTex(r"\Delta Y = 3\,000, \quad \Delta C = 2\,400").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(w1))
        self.wait(2)
        w2 = MathTex(r"MPC = \tfrac{2\,400}{3\,000} = 0{,}8").scale(1.1).shift(band_shift(1) + UP * 0.2)
        w3 = MathTex(r"MPS = \tfrac{600}{3\,000} = 0{,}2").scale(1.1).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(w2))
        self.wait(2)
        self.play(Write(w3))
        self.wait(2)
        wr = Tex(r"Marginal $=$ average").scale(1.0).shift(band_shift(1) + DOWN * 1.7 + LEFT * 3.0)
        self.play(Write(wr))
        self.play(Create(strike(wr)))
        rt = Tex(r"The MPC describes the EXTRA rand only").scale(0.95).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(rt))
        self.play(Create(SurroundingRectangle(rt, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the echo and the formula ---
        self.next_band(2)
        b2_title = Tex("The echo of R2\\,000 at MPC 0,75").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        e1 = MathTex(r"2\,000 \rightarrow 1\,500 \rightarrow 1\,125 \rightarrow 844 \rightarrow \dots").scale(1.05).shift(band_shift(2) + UP * 1.2)
        self.play(Write(e1))
        self.wait(2.5)
        e2 = MathTex(r"\text{Sum} = \tfrac{2\,000}{1 - 0{,}75} = \tfrac{2\,000}{0{,}25} = R8\,000").scale(1.05).shift(band_shift(2) + UP * 0.1)
        self.play(Write(e2))
        self.wait(2.5)
        f1 = MathTex(r"k = \tfrac{1}{1 - MPC} = \tfrac{1}{MPS}").scale(1.15).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(f1))
        self.play(Create(SurroundingRectangle(f1, color=GREEN)))
        self.wait(2)
        f2 = MathTex(r"\Delta Y = k \times \Delta J").scale(1.15).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(f2))
        self.wait(2)
        f3 = Tex(r"Big re-spending, big k; big leak, small k").scale(0.95).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(f3))
        self.wait(3)

        # --- Band 3 (subtopic_2): the 45-degree diagram ---
        self.next_band(3)
        b3_title = Tex("The forty-five degree picture").scale(1.15).shift(band_shift(3) + UP * 2.9)
        self.play(Write(b3_title))
        self.wait(1.5)
        o = band_shift(3) + DOWN * 2.9 + LEFT * 5.4
        y_ax = Arrow(o, o + UP * 4.8, buff=0, stroke_width=3)
        x_ax = Arrow(o, o + RIGHT * 10.4, buff=0, stroke_width=3)
        y_lab = Tex("spending").scale(0.7).shift(o + UP * 4.8 + RIGHT * 1.1)
        x_lab = Tex("national income").scale(0.7).shift(o + RIGHT * 10.0 + DOWN * 0.35)
        self.play(Create(y_ax), Create(x_ax))
        self.play(Write(y_lab), Write(x_lab))
        self.wait(1.5)
        deg45 = Line(o, o + RIGHT * 4.6 + UP * 4.6, color=GREY)
        deg_lab = Tex(r"45\textdegree: spending $=$ income", color=GREY).scale(0.7).shift(o + RIGHT * 5.8 + UP * 4.3)
        self.play(Create(deg45), Write(deg_lab))
        self.wait(2)
        sp1 = Line(o + UP * 1.0, o + RIGHT * 9.0 + UP * 3.7, color=BLUE)
        sp1_lab = Tex("spending line, slope $=$ MPC", color=BLUE).scale(0.7).shift(o + RIGHT * 8.2 + UP * 3.0)
        self.play(Create(sp1), Write(sp1_lab))
        self.wait(2)
        eq1 = Dot(o + RIGHT * 1.43 + UP * 1.43, color=YELLOW)
        self.play(Create(eq1))
        self.wait(1.5)
        sp2 = Line(o + UP * 1.8, o + RIGHT * 9.0 + UP * 4.5, color=GREEN)
        sp2_lab = Tex(r"shift UP by $\Delta J$", color=GREEN).scale(0.7).shift(o + RIGHT * 1.6 + UP * 2.6)
        self.play(Create(sp2), Write(sp2_lab))
        self.wait(2)
        eq2 = Dot(o + RIGHT * 2.57 + UP * 2.57, color=YELLOW)
        self.play(Create(eq2))
        self.wait(1.5)
        move = Line(o + RIGHT * 1.43 + UP * 0.3, o + RIGHT * 2.57 + UP * 0.3, color=RED, stroke_width=5)
        move_lab = Tex(r"income moves MORE than $\Delta J$", color=RED).scale(0.75).shift(o + RIGHT * 4.6 + UP * 0.6)
        self.play(Create(move), Write(move_lab))
        self.play(Create(SurroundingRectangle(move_lab, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): cases one and two ---
        self.next_band(4)
        b4_title = Tex("Forwards, then backwards").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        c1 = MathTex(r"\Delta J = R8\text{ bn}, \; MPC = 0{,}8").scale(1.0).shift(band_shift(4) + UP * 1.2)
        c2 = MathTex(r"k = \tfrac{1}{0{,}2} = 5 \;\Rightarrow\; \Delta Y = R40\text{ bn}").scale(1.05).shift(band_shift(4) + UP * 0.3)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.play(Create(SurroundingRectangle(c2, color=GREEN)))
        self.wait(2.5)
        c3 = MathTex(r"\Delta Y = R10\text{ bn from } \Delta J = R4\text{ bn}").scale(1.0).shift(band_shift(4) + DOWN * 0.8)
        c4 = MathTex(r"k = 2{,}5 \Rightarrow 1 - MPC = 0{,}4 \Rightarrow MPC = 0{,}6").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(c3))
        self.wait(2)
        self.play(Write(c4))
        self.wait(2)
        c5 = Tex(r"Always end with the interpretation sentence").scale(0.95).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(c5))
        self.wait(3)

        # --- Band 5 (subtopic_3): the open-economy multiplier ---
        self.next_band(5)
        b5_title = Tex("The South African version").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        o1 = MathTex(r"k = \tfrac{1}{MPS + MPT + MPM}").scale(1.15).shift(band_shift(5) + UP * 1.1)
        self.play(Write(o1))
        self.play(Create(SurroundingRectangle(o1, color=GREEN)))
        self.wait(2)
        o2 = MathTex(r"\tfrac{1}{0{,}15 + 0{,}20 + 0{,}15} = \tfrac{1}{0{,}50} = 2").scale(1.1).shift(band_shift(5) + UP * 0.0)
        self.play(Write(o2))
        self.wait(2.5)
        o3 = MathTex(r"R8\text{ bn} \Rightarrow R16\text{ bn, not } R40\text{ bn}").scale(1.05).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(o3))
        self.wait(2)
        o4 = Tex(r"Heavy tax + imports $=$ small multiplier;").scale(0.95).shift(band_shift(5) + DOWN * 1.9)
        o5 = Tex(r"local wages circulate, imported machines exit").scale(0.95).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(o4))
        self.play(Write(o5))
        self.wait(3)

        # --- Band 6 (subtopic_4): conditions and the reverse gear ---
        self.next_band(6)
        b6_title = Tex("Conditions, and the reverse gear").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        n1 = Tex(r"1. Spare capacity — else PRICES multiply").scale(1.0).shift(band_shift(6) + UP * 1.2)
        n2 = Tex(r"2. Time — rounds take months").scale(1.0).shift(band_shift(6) + UP * 0.4)
        n3 = Tex(r"3. Finance — borrowing can crowd out").scale(1.0).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(n1))
        self.wait(2)
        self.play(Write(n2))
        self.wait(2)
        self.play(Write(n3))
        self.wait(2)
        r1 = MathTex(r"X \downarrow R4\text{ bn}, \; k = 2 \Rightarrow Y \downarrow R8\text{ bn}").scale(1.0).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(r1))
        self.play(Create(SurroundingRectangle(r1, color=GREEN)))
        self.wait(2)
        r2 = Tex(r"Stabilisers damp the fall; the accelerator").scale(0.95).shift(band_shift(6) + DOWN * 2.3)
        r3 = Tex(r"turns rising demand into fresh injections").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(r2))
        self.play(Write(r3))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): one rand, many pockets ---
        self.next_band(7)
        b7_title = Tex("One payment, six pockets").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        p1 = Tex(r"Pipe job: R2\,000 to the fitter").scale(1.0).shift(band_shift(7) + UP * 1.2)
        p2 = MathTex(r"2\,000 \rightarrow 1\,500 \rightarrow 1\,125 \rightarrow 844 \rightarrow \dots").scale(1.0).shift(band_shift(7) + UP * 0.3)
        self.play(Write(p1))
        self.wait(2)
        self.play(Write(p2))
        self.wait(2.5)
        p3 = Tex(r"Fitter, butcher, baker, seamstress,").scale(0.95).shift(band_shift(7) + DOWN * 0.6)
        p4 = Tex(r"taxi owner, tuckshop — all paid once").scale(0.95).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(p3))
        self.play(Write(p4))
        self.wait(2.5)
        p5 = MathTex(r"\text{Town's gain} = R8\,000").scale(1.05).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(p5))
        self.play(Create(SurroundingRectangle(p5, color=GREEN)))
        self.wait(2)
        p6 = Tex(r"A spent rand becomes income and moves on").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(p6))
        self.wait(3)

        # --- Band 8 (subtopic_6): why the chain gets shorter ---
        self.next_band(8)
        b8_title = Tex("Three exits shorten the chain").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        x1 = Tex(r"SAVED — rests in the bank").scale(1.0).shift(band_shift(8) + UP * 1.2)
        x2 = Tex(r"TAXED — VAT and payslip").scale(1.0).shift(band_shift(8) + UP * 0.4)
        x3 = Tex(r"IMPORTED — leaves the country for good").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(x1))
        self.wait(2)
        self.play(Write(x2))
        self.wait(2)
        self.play(Write(x3))
        self.wait(2)
        x4 = MathTex(r"\text{Half exits each stop: } R2\,000 \Rightarrow R4\,000").scale(0.95).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(x4))
        self.play(Create(SurroundingRectangle(x4, color=GREEN)))
        self.wait(2.5)
        x5 = Tex(r"WHO gets it and WHAT it buys set the length;").scale(0.9).shift(band_shift(8) + DOWN * 2.2)
        x6 = Tex(r"and the chain runs backwards after retrenchment").scale(0.9).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(x5))
        self.play(Write(x6))
        self.wait(3)

        # --- Band 9 (subtopic_7): budget day ---
        self.next_band(9)
        b9_title = Tex("Three questions on budget day").scale(1.15).shift(band_shift(9) + UP * 2.2)
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
        q4 = Tex(r"Objection: borrowed money carries interest").scale(0.95).shift(band_shift(9) + DOWN * 1.4)
        q5 = Tex(r"and can crowd private builders out").scale(0.95).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(q4))
        self.play(Write(q5))
        self.wait(2.5)
        q6 = Tex(r"A rand travels — count how far, and who pays").scale(0.95).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(q6))
        self.play(Create(SurroundingRectangle(q6, color=GREEN)))
        self.wait(4)
