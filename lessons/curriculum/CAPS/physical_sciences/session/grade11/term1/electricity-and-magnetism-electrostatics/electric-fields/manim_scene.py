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

# Band-layout whiteboard scene for the Electric Fields session duo.
# Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7.
# Band dwell proportional to subtopics.json (235/225/230/240/185/185/190
# of 1490 s). Exporter-safe mobjects only; add-only lifecycle; camera bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


def radial_arrows(center, outward=True, r0=0.35, r1=1.1, n=8, color=YELLOW):
    """Sea-urchin field pattern from plain Arrows."""
    arrows = VGroup()
    for i in range(n):
        ang = TAU * i / n
        d = np.array([np.cos(ang), np.sin(ang), 0.0])
        a, b = center + d * r0, center + d * r1
        arrows.add(Arrow(a, b, buff=0, color=color) if outward
                   else Arrow(b, a, buff=0, color=color))
    return arrows


class ElectricFieldsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the field concept ---
        title = Tex("Electric Fields").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("A region of space where a charge").scale(1.05).shift(UP * 1.2)
        b0_l2 = Tex("experiences a force").scale(1.05).shift(UP * 0.5)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Direction: force on a POSITIVE test charge").scale(1.0).shift(DOWN * 0.6)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=BLUE)))
        self.wait(2.5)
        b0_l4 = Tex("Away from $+$, toward $-$").scale(1.1).shift(DOWN * 1.8)
        self.play(Write(b0_l4))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): field-line patterns and rules ---
        self.next_band(1)
        b1_title = Tex("Field lines: the four rules").scale(1.15).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        cplus = Dot(band_shift(1) + LEFT * 2.6 + UP * 0.9)
        lplus = MathTex(r"+").scale(1.0).shift(band_shift(1) + LEFT * 2.6 + UP * 1.55)
        self.play(FadeIn(cplus), Write(lplus))
        self.play(Create(radial_arrows(band_shift(1) + LEFT * 2.6 + UP * 0.9, outward=True)))
        self.wait(2)
        cneg = Dot(band_shift(1) + RIGHT * 2.6 + UP * 0.9)
        lneg = MathTex(r"-").scale(1.0).shift(band_shift(1) + RIGHT * 2.6 + UP * 1.55)
        self.play(FadeIn(cneg), Write(lneg))
        self.play(Create(radial_arrows(band_shift(1) + RIGHT * 2.6 + UP * 0.9, outward=False)))
        self.wait(2)
        b1_r1 = Tex("Start on $+$, end on $-$").scale(0.95).shift(band_shift(1) + DOWN * 0.8)
        b1_r2 = Tex("Never cross").scale(0.95).shift(band_shift(1) + DOWN * 1.5)
        b1_r3 = Tex("Arrows: the way a $+$ test charge moves").scale(0.95).shift(band_shift(1) + DOWN * 2.2)
        b1_r4 = Tex("Closer lines $=$ stronger field").scale(0.95).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_r1))
        self.wait(1.5)
        self.play(Write(b1_r2))
        self.wait(1.5)
        self.play(Write(b1_r3))
        self.wait(1.5)
        self.play(Write(b1_r4))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): E = F/q worked forward ---
        self.next_band(2)
        b2_title = Tex("Field strength: force per unit charge").scale(1.1).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"E = \frac{F}{q} \quad \text{(N/C)}").scale(1.2).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=BLUE)))
        self.wait(2.5)
        b2_l2 = Tex(r"$+2 \times 10^{-6}$ C at P feels 0,008 N east").scale(1.0).shift(band_shift(2) + DOWN * 0.1)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"E = \frac{0{,}008}{2 \times 10^{-6}}").scale(1.1).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"E = 4\ 000\ \text{N/C east}").scale(1.1).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): backward, and the electron reversal ---
        self.next_band(3)
        b3_title = Tex("Same field, now acting on an electron").scale(1.1).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"F = Eq = 4\ 000 \times 1{,}6 \times 10^{-19}").scale(1.05).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"F = 6{,}4 \times 10^{-16}\ \text{N, west}").scale(1.1).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = Tex("Negative charge: force AGAINST the field").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_trap = Tex(r"dividing by the SOURCE charge").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_trap))
        self.play(Create(strike(b3_trap)))
        self.wait(1.5)
        b3_l4 = Tex("$q$ is the charge FEELING the force").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): the source formula ---
        self.next_band(4)
        b4_title = Tex("Field created by a point charge").scale(1.1).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"F = \frac{k Q q}{r^2}, \;\; E = \frac{F}{q}").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"E = \frac{k Q}{r^2}").scale(1.3).shift(band_shift(4) + DOWN * 0.1)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=BLUE)))
        self.wait(2.5)
        b4_l3 = Tex("The test charge cancels — field of the source alone").scale(0.95).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex(r"Double $r$ $\Rightarrow$ quarter the field").scale(1.0).shift(band_shift(4) + DOWN * 2.3)
        self.play(Write(b4_l4))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): worked example and choosing the formula ---
        self.next_band(5)
        b5_title = Tex(r"Field 0,3 m from $+5\ \mu$C").scale(1.1).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"E = \frac{9 \times 10^{9} \times 5 \times 10^{-6}}{(0{,}3)^2}").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"E = \frac{45\ 000}{0{,}09}").scale(1.05).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"E = 5 \times 10^{5}\ \text{N/C away}").scale(1.1).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex(r"Force known? $E = F/q$. Source known? $E = kQ/r^2$").scale(0.95).shift(band_shift(5) + DOWN * 2.3)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): two sources, the setup at midpoint P ---
        self.next_band(6)
        b6_title = Tex("Net field midway between two charges").scale(1.1).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        rail = Line(LEFT * 3.5 + UP * 1.2, RIGHT * 3.5 + UP * 1.2).shift(band_shift(6))
        dA = Dot(band_shift(6) + LEFT * 3.5 + UP * 1.2)
        dB = Dot(band_shift(6) + RIGHT * 3.5 + UP * 1.2)
        dP = Dot(band_shift(6) + UP * 1.2, color=YELLOW)
        lA = Tex(r"A $+2\ \mu$C").scale(0.85).shift(band_shift(6) + LEFT * 3.5 + UP * 1.9)
        lB = Tex(r"B $-3\ \mu$C").scale(0.85).shift(band_shift(6) + RIGHT * 3.5 + UP * 1.9)
        lP = Tex("P (0,2 m from each)").scale(0.8).shift(band_shift(6) + UP * 1.9)
        self.play(Create(rail))
        self.play(FadeIn(dA), Write(lA))
        self.play(FadeIn(dB), Write(lB))
        self.play(FadeIn(dP), Write(lP))
        self.wait(2)
        aA = Arrow(UP * 0.5, UP * 0.5 + RIGHT * 1.4, buff=0, color=YELLOW).shift(band_shift(6) + LEFT * 0.7)
        lEA = Tex(r"$E_A$: away from A").scale(0.8).shift(band_shift(6) + UP * 0.5 + RIGHT * 3.0)
        self.play(Create(aA), Write(lEA))
        self.wait(2)
        aB = Arrow(DOWN * 0.3, DOWN * 0.3 + RIGHT * 1.4, buff=0, color=YELLOW).shift(band_shift(6) + LEFT * 0.7)
        lEB = Tex(r"$E_B$: toward B").scale(0.8).shift(band_shift(6) + DOWN * 0.3 + RIGHT * 2.9)
        self.play(Create(aB), Write(lEB))
        self.wait(2)
        b6_note = Tex("No charge needs to sit at P").scale(1.0).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_note))
        self.wait(2)
        b6_note2 = Tex("Both arrows agree: from A toward B").scale(1.0).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_note2))
        self.wait(2)

        # --- Band 7 (subtopic_4): the two contributions, then add ---
        self.next_band(7)
        b7_l1 = MathTex(r"E_A = \frac{18\ 000}{0{,}04} = 4{,}5 \times 10^{5}\ \text{N/C}").scale(1.0).shift(band_shift(7) + UP * 2.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"E_B = \frac{27\ 000}{0{,}04} = 6{,}75 \times 10^{5}\ \text{N/C}").scale(1.0).shift(band_shift(7) + UP * 1.0)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"E_{net} = (4{,}5 + 6{,}75) \times 10^{5}").scale(1.05).shift(band_shift(7) + DOWN * 0.1)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = MathTex(r"E_{net} = 1{,}125 \times 10^{6}\ \text{N/C, A to B}").scale(1.05).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2.5)
        b7_trap = MathTex(r"E_B = \frac{k(-3 \times 10^{-6})}{r^2}").scale(1.0).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_trap))
        self.play(Create(strike(b7_trap)))
        self.wait(1.5)
        b7_rule = Tex("Signs set arrows, never magnitudes").scale(0.95).shift(band_shift(7) + DOWN * 3.2)
        self.play(Write(b7_rule))
        self.wait(2)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the invisible cushion ---
        self.next_band(8)
        b8_title = Tex("The invisible cushion around every charge").scale(1.1).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        urchin = Dot(band_shift(8) + UP * 0.9)
        self.play(FadeIn(urchin))
        self.play(Create(radial_arrows(band_shift(8) + UP * 0.9, outward=True, n=8)))
        self.wait(2)
        b8_l1 = Tex("A sea urchin of influence — thick close up").scale(0.95).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Map it with a small positive probe").scale(0.95).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Away from $+$, toward $-$, crowded $=$ strong").scale(0.95).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): how hard is the shove ---
        self.next_band(9)
        b9_title = Tex("How hard is the shove at this spot?").scale(1.1).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Quote the force PER COULOMB — like rand per kg").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"E = \frac{F}{q}").scale(1.2).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"4\ 000\ \text{N/C} \times 2 \times 10^{-6}\ \text{C} = 0{,}008\ \text{N}").scale(0.95).shift(band_shift(9) + DOWN * 1.0)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("The rate belongs to the spot, not the visitor").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("Electrons read the map in reverse").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): two charges both have a say ---
        self.next_band(10)
        b10_title = Tex("When two charges both have a say").scale(1.15).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Between $+$ and $-$: both votes agree — add").scale(0.95).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex(r"Between $+$ and $+$: votes fight — subtract").scale(0.95).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.wait(2.5)
        dl = Dot(band_shift(10) + DOWN * 0.7 + LEFT * 3.0)
        dr = Dot(band_shift(10) + DOWN * 0.7 + RIGHT * 3.0)
        lp1 = MathTex(r"+").scale(0.9).shift(band_shift(10) + DOWN * 0.2 + LEFT * 3.0)
        lp2 = MathTex(r"+").scale(0.9).shift(band_shift(10) + DOWN * 0.2 + RIGHT * 3.0)
        zero = Dot(band_shift(10) + DOWN * 0.7, color=YELLOW)
        lz = Tex("dead spot: field zero").scale(0.85).shift(band_shift(10) + DOWN * 1.4)
        self.play(FadeIn(dl), Write(lp1), FadeIn(dr), Write(lp2))
        self.play(FadeIn(zero), Write(lz))
        self.wait(2.5)
        b10_l3 = Tex("Each charge: own distance, own arrow").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex("Then let the arrows vote").scale(1.0).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(4)
