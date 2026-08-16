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

# Band-layout whiteboard scene for the Connected Bodies and Pulleys duo.
# Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7.
# Band dwell proportional to subtopics.json (215/230/230/265/180/175/185
# of 1480 s). Exporter-safe mobjects only; add-only lifecycle; camera bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ConnectedBodiesPulleysSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the rules of the system ---
        title = Tex("Connected Bodies and Pulleys").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Inextensible string: same magnitude of $a$").scale(1.0).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = Tex("Light string: same $T$ at both ends").scale(1.0).shift(UP * 0.4)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Frictionless pulley: changes direction only").scale(1.0).shift(DOWN * 0.4)
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_l4 = Tex("Tension always PULLS — never pushes").scale(1.0).shift(DOWN * 1.4)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=BLUE)))
        self.wait(2)
        b0_l5 = Tex("Tension is INTERNAL to the system").scale(1.0).shift(DOWN * 2.5)
        self.play(Write(b0_l5))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): two crates, frictionless — the system step ---
        self.next_band(1)
        b1_title = Tex("Two crates, frictionless floor, 50 N pull").scale(1.05).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        floor = Line(LEFT * 4.5 + UP * 0.6, RIGHT * 4.5 + UP * 0.6).shift(band_shift(1))
        crB = Rectangle(width=1.2, height=0.9).shift(band_shift(1) + LEFT * 2.8 + UP * 1.05)
        crA = Rectangle(width=1.6, height=1.1).shift(band_shift(1) + RIGHT * 0.2 + UP * 1.15)
        rope = Line(LEFT * 2.2 + UP * 1.05, LEFT * 0.6 + UP * 1.05).shift(band_shift(1))
        lB = Tex("B: 2 kg").scale(0.85).shift(band_shift(1) + LEFT * 2.8 + UP * 1.95)
        lA = Tex("A: 8 kg").scale(0.85).shift(band_shift(1) + RIGHT * 0.2 + UP * 2.1)
        pull = Arrow(RIGHT * 1.0 + UP * 1.15, RIGHT * 2.6 + UP * 1.15, buff=0, color=YELLOW).shift(band_shift(1))
        lF = Tex("50 N").scale(0.85).shift(band_shift(1) + RIGHT * 3.2 + UP * 1.15)
        self.play(Create(floor))
        self.play(Create(crB), Write(lB))
        self.play(Create(crA), Write(lA), Create(rope))
        self.play(Create(pull), Write(lF))
        self.wait(2)
        b1_l1 = Tex("Step 1 — whole system ($T$ cancels):").scale(1.0).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"F_{net} = m_{tot}\,a: \;\; 50 = 10a").scale(1.1).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"a = 5\ \text{m/s}^2 \text{ forward}").scale(1.1).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): one body for the tension ---
        self.next_band(2)
        b2_title = Tex("Step 2 — crate B alone").scale(1.1).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"T = m_B\,a = 2 \times 5").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"T = 10\ \text{N}").scale(1.15).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2)
        b2_l3 = MathTex(r"\text{Check A: } 50 - 10 = 40 = 8 \times 5").scale(1.05).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_trap = MathTex(r"50 + T = 10a").scale(1.05).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_trap))
        self.play(Create(strike(b2_trap)))
        self.wait(1.5)
        b2_rule = Tex("Tension never enters the system equation").scale(1.0).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_rule))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): rough floor — the system step ---
        self.next_band(3)
        b3_title = Tex(r"Same crates, rough floor: $\mu_k = 0{,}2$").scale(1.1).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"N_{tot} = 10 \times 9{,}8 = 98\ \text{N}").scale(1.05).shift(band_shift(3) + UP * 1.3)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"f_{tot} = 0{,}2 \times 98 = 19{,}6\ \text{N}").scale(1.05).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"F_{net} = 50 - 19{,}6 = 30{,}4\ \text{N}").scale(1.05).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"a = \frac{30{,}4}{10} = 3{,}04\ \text{m/s}^2").scale(1.05).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): crate B with its OWN friction ---
        self.next_band(4)
        b4_title = Tex("Crate B alone — its own friction only").scale(1.1).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"N_B = 2 \times 9{,}8 = 19{,}6\ \text{N}").scale(1.05).shift(band_shift(4) + UP * 1.3)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"f_B = 0{,}2 \times 19{,}6 = 3{,}92\ \text{N}").scale(1.05).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"T - 3{,}92 = 2 \times 3{,}04 = 6{,}08").scale(1.05).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"T = 10{,}0\ \text{N}").scale(1.15).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_trap = Tex(r"using $f_{tot} = 19{,}6$ N on crate B").scale(1.0).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_trap))
        self.play(Create(strike(b4_trap)))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): table-edge pulley — the picture ---
        self.next_band(5)
        b5_title = Tex("Block on a table, mass over a pulley").scale(1.1).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        table = Line(LEFT * 4.5 + UP * 0.8, RIGHT * 1.5 + UP * 0.8).shift(band_shift(5))
        leg = Line(RIGHT * 1.5 + UP * 0.8, RIGHT * 1.5 + DOWN * 2.6).shift(band_shift(5))
        blk = Rectangle(width=1.4, height=0.9).shift(band_shift(5) + LEFT * 2.0 + UP * 1.25)
        lblk = Tex(r"4 kg, $\mu_k = 0{,}25$").scale(0.8).shift(band_shift(5) + LEFT * 2.0 + UP * 2.1)
        pul = Circle(radius=0.3, color=WHITE).shift(band_shift(5) + RIGHT * 1.7 + UP * 1.1)
        s1 = Line(LEFT * 1.3 + UP * 1.25, RIGHT * 1.55 + UP * 1.35).shift(band_shift(5))
        s2 = Line(RIGHT * 2.0 + UP * 1.0, RIGHT * 2.0 + DOWN * 0.6).shift(band_shift(5))
        hang = Rectangle(width=1.0, height=0.8).shift(band_shift(5) + RIGHT * 2.0 + DOWN * 1.0)
        lhang = Tex("6 kg").scale(0.85).shift(band_shift(5) + RIGHT * 3.1 + DOWN * 1.0)
        self.play(Create(table), Create(leg))
        self.play(Create(blk), Write(lblk))
        self.play(Create(pul), Create(s1), Create(s2))
        self.play(Create(hang), Write(lhang))
        self.wait(2)
        wA = Arrow(RIGHT * 2.0 + DOWN * 1.4, RIGHT * 2.0 + DOWN * 2.5, buff=0, color=YELLOW).shift(band_shift(5))
        lw = MathTex(r"58{,}8\ \text{N}").scale(0.85).shift(band_shift(5) + RIGHT * 3.2 + DOWN * 2.0)
        self.play(Create(wA), Write(lw))
        self.wait(1.5)
        fA = Arrow(LEFT * 1.3 + UP * 1.6, LEFT * 3.0 + UP * 1.6, buff=0, color=RED).shift(band_shift(5))
        lf = Tex(r"$f = 9{,}8$ N").scale(0.8).shift(band_shift(5) + LEFT * 3.9 + UP * 2.0)
        self.play(Create(fA), Write(lf))
        self.wait(2)
        b5_note = Tex("Driving: hanging weight. Opposing: friction").scale(0.95).shift(band_shift(5) + LEFT * 1.6 + DOWN * 1.8)
        self.play(Write(b5_note))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): system, then hanging mass ---
        self.next_band(6)
        b6_l1 = MathTex(r"58{,}8 - 9{,}8 = 10a \;\Rightarrow\; 49 = 10a").scale(1.05).shift(band_shift(6) + UP * 2.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"a = 4{,}9\ \text{m/s}^2").scale(1.1).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2)
        b6_l3 = Tex("Hanging mass alone, down positive:").scale(1.0).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l3))
        self.wait(1.5)
        b6_l4 = MathTex(r"58{,}8 - T = 6 \times 4{,}9 = 29{,}4").scale(1.05).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = MathTex(r"T = 29{,}4\ \text{N}").scale(1.15).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(2)
        b6_l6 = Tex(r"$T <$ hanging weight (58,8 N) — always, if $a \neq 0$").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): the incline version ---
        self.next_band(7)
        b7_title = Tex(r"Incline: 6 kg on a smooth 30$^\circ$ slope, 9 kg hangs").scale(1.0).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        base = Line(LEFT * 4.0 + UP * 0.3, RIGHT * 0.5 + UP * 0.3).shift(band_shift(7))
        slope = Line(LEFT * 4.0 + UP * 0.3, RIGHT * 0.5 + UP * 1.9).shift(band_shift(7))
        lang = Tex(r"30$^\circ$").scale(0.8).shift(band_shift(7) + LEFT * 2.7 + UP * 0.65)
        self.play(Create(base), Create(slope), Write(lang))
        aDown = Arrow(LEFT * 1.0 + UP * 1.45, LEFT * 2.6 + UP * 0.85, buff=0, color=RED).shift(band_shift(7))
        lms = MathTex(r"mg\sin\theta = 29{,}4\ \text{N}").scale(0.85).shift(band_shift(7) + LEFT * 2.2 + UP * 2.1)
        self.play(Create(aDown), Write(lms))
        self.wait(2)
        aW = Arrow(RIGHT * 2.6 + UP * 1.4, RIGHT * 2.6 + UP * 0.2, buff=0, color=YELLOW).shift(band_shift(7))
        lW = MathTex(r"88{,}2\ \text{N}").scale(0.85).shift(band_shift(7) + RIGHT * 3.7 + UP * 0.8)
        self.play(Create(aW), Write(lW))
        self.wait(2)
        b7_l1 = MathTex(r"88{,}2 - 29{,}4 = 15a \;\Rightarrow\; a = 3{,}92\ \text{m/s}^2").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"88{,}2 - T = 9 \times 3{,}92 = 35{,}28").scale(1.0).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = MathTex(r"T = 52{,}92\ \text{N}").scale(1.1).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        b7_l4 = Tex(r"On a slope, only $mg\sin\theta$ opposes").scale(0.95).shift(band_shift(7) + DOWN * 3.3)
        self.play(Write(b7_l4))
        self.wait(2.5)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): two trolleys tied together ---
        self.next_band(8)
        b8_title = Tex("Two trolleys tied together").scale(1.2).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("They move together: ONE acceleration").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("The rope pulls equally at both ends").scale(1.0).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("A rope can only PULL, never push").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("Seen as one big trolley, the rope's pulls cancel").scale(0.95).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("The rope only matters one trolley at a time").scale(0.95).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): weigh the whole train first ---
        self.next_band(9)
        b9_title = Tex("Weigh the whole train first").scale(1.2).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Move 1: one big object, rope left out").scale(1.0).shift(band_shift(9) + UP * 1.3)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"a = \frac{50 - 19{,}6}{10} = 3{,}04\ \text{m/s}^2").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Move 2: the lazy crate alone").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = MathTex(r"T - 3{,}92 = 6{,}08 \;\Rightarrow\; T = 10\ \text{N}").scale(1.05).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex("Its own friction only — never the pair's").scale(0.95).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the bucket down the well ---
        self.next_band(10)
        b10_title = Tex("The bucket down the well").scale(1.2).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"\text{Driving } 58{,}8 - \text{ fighting } 9{,}8 = 49\ \text{N}").scale(1.0).shift(band_shift(10) + UP * 1.3)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"a = \frac{49}{10} = 4{,}9\ \text{m/s}^2").scale(1.05).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"58{,}8 - T = 29{,}4 \;\Rightarrow\; T = 29{,}4\ \text{N}").scale(1.0).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2.5)
        b10_l4 = Tex("The string holds LESS than the full weight").scale(0.95).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex(r"Ramp: $a = 3{,}92$ m/s$^2$, $T = 52{,}92$ N").scale(0.95).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10_l5))
        self.wait(4)
