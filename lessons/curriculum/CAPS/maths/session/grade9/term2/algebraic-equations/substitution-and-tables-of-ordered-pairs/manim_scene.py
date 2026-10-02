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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex/MathTex keep the export to
# the allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (220/230/230/230/190/190/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


def table(xs, ys, centre, cell=1.1):
    """Two-row table of ordered pairs: x across the top, y beneath."""
    g = VGroup()
    n = len(xs)
    left = centre + LEFT * (n + 1) * cell / 2
    for r in range(3):
        g.add(Line(left + UP * (0.5 - r) * 0.7, left + RIGHT * (n + 1) * cell + UP * (0.5 - r) * 0.7, color=GREY))
    for c in range(n + 2):
        g.add(Line(left + RIGHT * c * cell + UP * 0.35, left + RIGHT * c * cell + DOWN * 1.05, color=GREY))
    g.add(MathTex(r"x").scale(0.8).move_to(left + RIGHT * cell / 2))
    g.add(MathTex(r"y").scale(0.8).move_to(left + RIGHT * cell / 2 + DOWN * 0.7))
    for i, (a, b) in enumerate(zip(xs, ys)):
        g.add(MathTex(a).scale(0.8).move_to(left + RIGHT * (i + 1.5) * cell))
        g.add(MathTex(b).scale(0.8).move_to(left + RIGHT * (i + 1.5) * cell + DOWN * 0.7))
    return g


def machine(centre, rule):
    """An input-output machine box with its rule printed on it."""
    box = Rectangle(width=3.2, height=1.2, color=BLUE).move_to(centre)
    lab = Tex(rule).scale(0.7).move_to(centre)
    arr_in = Arrow(centre + LEFT * 2.8, centre + LEFT * 1.7, buff=0, color=GREY)
    arr_out = Arrow(centre + RIGHT * 1.7, centre + RIGHT * 2.8, buff=0, color=GREY)
    return VGroup(box, lab, arr_in, arr_out)


class OrderedPairsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): substituting into y = 2x + 1
        title = Tex("Tables of ordered pairs: $y = 2x + 1$").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        t0 = table([r"-2", r"-1", r"0", r"1", r"2"], [r"-3", r"-1", r"1", r"3", r"5"], UP * 1.0)
        self.play(Create(t0))
        self.wait(2.5)
        l1 = MathTex(r"x = -2: \; 2(-2) + 1 = -4 + 1 = -3").scale(0.95).shift(DOWN * 0.6)
        l2 = MathTex(r"(-2;\,-3),\;(-1;\,-1),\;(0;\,1),\;(1;\,3),\;(2;\,5)").scale(0.95).shift(DOWN * 1.5)
        l3 = Tex("$x$ first, $y$ second. $(5;\\,2)$ is a different point: $2(5) + 1 = 11$.").scale(0.85).shift(DOWN * 2.4)
        for m in (l1, l2, l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l2, color=GREEN)))
        self.wait(2)

        # --- Band 1 (subtopic_2): linear vs non-linear
        self.next_band(1)
        b1_title = Tex("Constant differences mean linear").scale(1.1).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_title))
        self.wait(1.5)
        t1 = table([r"-2", r"-1", r"0", r"1", r"2"], [r"-8", r"-5", r"-2", r"1", r"4"], band_shift(1) + UP * 1.2)
        self.play(Create(t1))
        self.wait(1.5)
        b1_l1 = MathTex(r"y = 3x - 2: \;\text{differences } 3, 3, 3, 3").scale(0.9).shift(band_shift(1) + UP * 0.0)
        t2 = table([r"-2", r"-1", r"0", r"1", r"2"], [r"3", r"0", r"-1", r"0", r"3"], band_shift(1) + DOWN * 1.1)
        b1_l2 = MathTex(r"y = x^2 - 1: \;\text{differences } -3, -1, 1, 3 \;\text{(not linear)}").scale(0.85).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Create(t2))
        self.wait(1.5)
        self.play(Write(b1_l2))
        self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): finding x when y is given
        self.next_band(2)
        b2_title = Tex("Given $y$: substitute and solve").scale(1.1).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"y = 3x - 2,\; y = 10: \quad 10 = 3x - 2 \Rightarrow 12 = 3x \Rightarrow x = 4 \quad (4;\,10)").scale(0.85).shift(band_shift(2) + UP * 1.3)
        b2_l2 = MathTex(r"y = 2x + 1,\; y = 15: \quad 2x = 14 \Rightarrow x = 7 \quad (7;\,15)").scale(0.9).shift(band_shift(2) + UP * 0.3)
        b2_l3 = MathTex(r"y = x^2 - 1,\; y = 8: \quad x^2 = 9 \Rightarrow x = 3 \text{ or } x = -3").scale(0.9).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = MathTex(r"\text{Taxi } 20 + 12k = 92 \Rightarrow 12k = 72 \Rightarrow k = 6 \text{ km}").scale(0.9).shift(band_shift(2) + DOWN * 1.7)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): table to rule
        self.next_band(3)
        b3_title = Tex("From table to rule").scale(1.2).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_title))
        self.wait(1.5)
        t3 = table([r"0", r"1", r"2", r"3"], [r"5", r"8", r"11", r"14"], band_shift(3) + UP * 1.2)
        self.play(Create(t3))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{differences } 3, 3, 3 \Rightarrow m = 3; \quad y = 5 \text{ at } x = 0 \Rightarrow c = 5").scale(0.85).shift(band_shift(3) + UP * 0.0)
        b3_l2 = MathTex(r"y = 3x + 5 \qquad \text{check } x = 3: \; 9 + 5 = 14 \;\checkmark").scale(0.95).shift(band_shift(3) + DOWN * 0.9)
        b3_l3 = MathTex(r"x: 2, 3, 4;\; y: 7, 10, 13 \Rightarrow m = 3,\; 7 = 6 + c \Rightarrow c = 1 \Rightarrow y = 3x + 1").scale(0.8).shift(band_shift(3) + DOWN * 1.9)
        for m in (b3_l1, b3_l2, b3_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(1.5)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"x = -2: \; 2 - 2 + 1 = 1 \;\text{(no bracket)}").scale(0.95).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"(5;\,2) \;\text{for } x = 2,\, y = 5").scale(0.95).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"\text{find } x \text{ when } y = 10: \; y = 3(10) - 2 = 28").scale(0.95).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"x^2 = 9 \Rightarrow x = 3 \;\text{only}").scale(0.95).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): the machine makes the table
        self.next_band(5)
        b5_title = Tex("The machine makes the table").scale(1.15).shift(band_shift(5) + UP * 2.5)
        self.play(Write(b5_title))
        self.wait(2)
        mc = machine(band_shift(5) + UP * 1.2, "double, then add 1")
        self.play(Create(mc))
        self.wait(1.5)
        t5 = table([r"-2", r"-1", r"0", r"1", r"2"], [r"-3", r"-1", r"1", r"3", r"5"], band_shift(5) + DOWN * 0.3)
        self.play(Create(t5))
        self.wait(2)
        b5_l1 = Tex("Input first, output second: $(2;\\,5)$. Negatives in brackets: $2(-2) + 1 = -3$.").scale(0.8).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l1))
        self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): running the machine backwards
        self.next_band(6)
        b6_title = Tex("Running the machine backwards").scale(1.15).shift(band_shift(6) + UP * 2.5)
        self.play(Write(b6_title))
        self.wait(2)
        mc6 = machine(band_shift(6) + UP * 1.2, "times 3, then take away 2")
        self.play(Create(mc6))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{out came } 10: \; 10 \xrightarrow{+2} 12 \xrightarrow{\div 3} 4 \;\text{went in} \quad (4;\,10)").scale(0.9).shift(band_shift(6) + UP * 0.1)
        b6_l2 = MathTex(r"\text{square, take away 1; out came } 8: \; 9 \Rightarrow 3 \text{ or } -3").scale(0.9).shift(band_shift(6) + DOWN * 0.8)
        b6_l3 = Tex("Read which number you were given. Forwards is arithmetic; backwards is an equation.").scale(0.8).shift(band_shift(6) + DOWN * 1.8)
        for m in (b6_l1, b6_l2, b6_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2)

        # --- Band 7 (subtopic_7): spot the pattern
        self.next_band(7)
        b7_title = Tex("Spot the pattern, write the rule").scale(1.15).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7_title))
        self.wait(2)
        t7 = table([r"1", r"2", r"3", r"4", r"5"], [r"32", r"44", r"56", r"68", r"80"], band_shift(7) + UP * 1.1)
        self.play(Create(t7))
        self.wait(2)
        b7_l1 = MathTex(r"\text{jumps of } 12 \Rightarrow \times 12; \quad 32 = 12 + 20 \Rightarrow \text{add } 20; \quad \text{fare} = 12k + 20").scale(0.85).shift(band_shift(7) + DOWN * 0.2)
        b7_l2 = Tex("Same jumps: straight line. Changing jumps: curve. Three columns before deciding.").scale(0.8).shift(band_shift(7) + DOWN * 1.1)
        b7_l3 = Tex("Brackets. Input first. Forwards or backwards. Check the jumps.").scale(0.85).shift(band_shift(7) + DOWN * 2.0)
        for m in (b7_l1, b7_l2):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=YELLOW)))
        self.wait(4)
