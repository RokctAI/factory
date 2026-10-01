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
# dwell time proportional to subtopics.json (210/240/220/230/190/200/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RealNumberSystemSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the nested sets
        title = Tex("The Real Number System").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"\mathbb{N} = \{1;\,2;\,3;\,\ldots\}").scale(1.15).shift(UP * 1.1)
        l2 = MathTex(r"\mathbb{N}_0 = \{0;\,1;\,2;\,3;\,\ldots\}").scale(1.15).shift(UP * 0.3)
        l3 = MathTex(r"\mathbb{Z} = \{\ldots;\,-2;\,-1;\,0;\,1;\,2;\,\ldots\}").scale(1.15).shift(DOWN * 0.5)
        l4 = MathTex(r"\mathbb{Q}:\; \tfrac{a}{b},\; a, b \in \mathbb{Z},\; b \neq 0").scale(1.15).shift(DOWN * 1.3)
        l5 = MathTex(r"\mathbb{Q}':\; \text{not a fraction} \qquad \mathbb{R} = \mathbb{Q} \cup \mathbb{Q}'").scale(1.1).shift(DOWN * 2.2)
        for m in (l1, l2, l3, l4, l5):
            self.play(Write(m))
            self.wait(2)
        self.wait(2)

        # --- Band 1 (subtopic_1): boxes inside boxes
        self.next_band(1)
        b1_title = Tex("Boxes inside boxes").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        r5 = Rectangle(width=11.0, height=3.6).shift(band_shift(1) + DOWN * 0.3)
        r4 = Rectangle(width=8.4, height=2.9).shift(band_shift(1) + DOWN * 0.3 + LEFT * 1.0)
        r3 = Rectangle(width=6.0, height=2.2).shift(band_shift(1) + DOWN * 0.3 + LEFT * 2.0)
        r2 = Rectangle(width=4.0, height=1.5).shift(band_shift(1) + DOWN * 0.3 + LEFT * 2.8)
        r1 = Rectangle(width=2.2, height=0.9).shift(band_shift(1) + DOWN * 0.3 + LEFT * 3.5)
        t1 = MathTex(r"\mathbb{N}").scale(0.9).move_to(r1.get_center())
        t2 = MathTex(r"\mathbb{N}_0").scale(0.9).move_to(r2.get_corner(UR) + 0.35 * DL)
        t3 = MathTex(r"\mathbb{Z}").scale(0.9).move_to(r3.get_corner(UR) + 0.35 * DL)
        t4 = MathTex(r"\mathbb{Q}").scale(0.9).move_to(r4.get_corner(UR) + 0.35 * DL)
        t5 = MathTex(r"\mathbb{R}").scale(0.9).move_to(r5.get_corner(UR) + 0.35 * DL)
        t6 = MathTex(r"\mathbb{Q}'\;\; \sqrt{2},\; \pi").scale(0.9).move_to(band_shift(1) + RIGHT * 4.3 + DOWN * 0.3)
        for r, t in ((r1, t1), (r2, t2), (r3, t3), (r4, t4), (r5, t5)):
            self.play(Create(r), Write(t))
            self.wait(1.2)
        self.play(Write(t6))
        self.wait(2)
        b1_note = Tex("7 is in all five boxes; $-3$ starts at $\\mathbb{Z}$").scale(1.05).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_note))
        self.wait(3)

        # --- Band 2 (subtopic_2): stop or repeat
        self.next_band(2)
        b2_title = Tex("Rational: the decimal stops or repeats").scale(1.2).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\tfrac{3}{8} = 0{,}375 \quad \tfrac{7}{20} = 0{,}35").scale(1.1).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"\tfrac{2}{3} = 0{,}\dot{6} \quad \tfrac{1}{7} = 0{,}\dot{1}4285\dot{7}").scale(1.1).shift(band_shift(2) + UP * 0.1)
        b2_l3 = Tex(r"Denominator only 2s and 5s $\Rightarrow$ terminates").scale(1.05).shift(band_shift(2) + DOWN * 0.9)
        b2_l4 = MathTex(r"\tfrac{5}{12}:\; 12 = 2^2 \times 3 \;\Rightarrow\; 0{,}41\dot{6}").scale(1.1).shift(band_shift(2) + DOWN * 1.9)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.2)
        self.wait(2)

        # --- Band 3 (subtopic_2): recurring decimal to fraction
        self.next_band(3)
        b3_title = Tex(r"Convert $0{,}\dot{3}$ and $0{,}\dot{2}\dot{7}$ to fractions").scale(1.15).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"x = 0{,}333\ldots \qquad 10x = 3{,}333\ldots").scale(1.1).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"9x = 3 \;\Rightarrow\; x = \tfrac{3}{9} = \tfrac{1}{3}").scale(1.1).shift(band_shift(3) + UP * 0.3)
        b3_l3 = MathTex(r"x = 0{,}2727\ldots \qquad 100x = 27{,}2727\ldots").scale(1.1).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = MathTex(r"99x = 27 \;\Rightarrow\; x = \tfrac{27}{99} = \tfrac{3}{11}").scale(1.1).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        self.play(Write(b3_l3))
        self.wait(2.5)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): irrationals — roots and pi
        self.next_band(4)
        b4_title = Tex("Irrational: never stops, never repeats").scale(1.2).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\sqrt{2} = 1{,}41421356\ldots \qquad \pi = 3{,}14159265\ldots").scale(1.05).shift(band_shift(4) + UP * 1.2)
        b4_l2 = MathTex(r"\tfrac{22}{7} = 3{,}\dot{1}4285\dot{7} \neq \pi").scale(1.1).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.play(Create(strike(b4_l2)))
        self.wait(2)
        b4_l3 = MathTex(r"\sqrt{9} = 3 \in \mathbb{N} \qquad \sqrt{10} \in \mathbb{Q}'").scale(1.1).shift(band_shift(4) + DOWN * 0.8)
        b4_l4 = Tex("Perfect square under the root $\\Rightarrow$ rational").scale(1.05).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l3))
        self.wait(2.5)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=YELLOW)))
        self.wait(3)

        # --- Band 5 (subtopic_3): trapping root 10
        self.next_band(5)
        b5_title = Tex(r"Where does $\sqrt{10}$ sit?").scale(1.2).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(1.5)
        line = Line(band_shift(5) + LEFT * 5 + UP * 0.9, band_shift(5) + RIGHT * 5 + UP * 0.9)
        self.play(Create(line))
        for k, lab in ((-5, "2"), (-1.5, "3"), (2, "4"), (5, "5")):
            d = Dot(band_shift(5) + RIGHT * k + UP * 0.9)
            t = Tex(lab).scale(0.9).next_to(d, DOWN, buff=0.15)
            self.play(Create(d), Write(t), run_time=0.5)
        root = Dot(band_shift(5) + RIGHT * (-1.5 + 3.5 * 0.162) + UP * 0.9, color=YELLOW)
        rlab = MathTex(r"\sqrt{10}").scale(0.9).next_to(root, UP, buff=0.15)
        self.play(Create(root), Write(rlab))
        self.wait(2)
        b5_l1 = MathTex(r"9 < 10 < 16 \;\Rightarrow\; 3 < \sqrt{10} < 4").scale(1.1).shift(band_shift(5) + DOWN * 0.6)
        b5_l2 = MathTex(r"3{,}1^2 = 9{,}61 \quad 3{,}2^2 = 10{,}24").scale(1.1).shift(band_shift(5) + DOWN * 1.5)
        b5_l3 = MathTex(r"3{,}1 < \sqrt{10} < 3{,}2 \quad (\sqrt{10} \approx 3{,}162)").scale(1.1).shift(band_shift(5) + DOWN * 2.4)
        for m in (b5_l1, b5_l2, b5_l3):
            self.play(Write(m))
            self.wait(2.2)
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)

        # --- Band 6 (subtopic_4): classify the anchor list
        self.next_band(6)
        b6_title = Tex("Classify the anchor list").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        rows = [
            r"7:\; \mathbb{N},\, \mathbb{N}_0,\, \mathbb{Z},\, \mathbb{Q},\, \mathbb{R}",
            r"0:\; \mathbb{N}_0,\, \mathbb{Z},\, \mathbb{Q},\, \mathbb{R} \qquad -3:\; \mathbb{Z},\, \mathbb{Q},\, \mathbb{R}",
            r"\tfrac{2}{5},\; 0{,}75,\; 0{,}\dot{3}:\; \mathbb{Q},\, \mathbb{R}",
            r"\sqrt{9} = 3:\; \mathbb{N},\, \mathbb{N}_0,\, \mathbb{Z},\, \mathbb{Q},\, \mathbb{R}",
            r"\sqrt{2},\; \pi:\; \mathbb{Q}',\, \mathbb{R}",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(1.0).shift(band_shift(6) + UP * (1.4 - 0.85 * i))
            self.play(Write(m))
            self.wait(2)
        self.wait(2)

        # --- Band 7 (subtopic_4): the exam habits
        self.next_band(7)
        b7_title = Tex("Exam habits").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_s1 = MathTex(r"-\sqrt{16} = -4 \in \mathbb{Z} \quad \tfrac{8}{2} = 4 \in \mathbb{N}").scale(1.05).shift(band_shift(7) + UP * 1.3)
        b7_s2 = MathTex(r"\tfrac{5}{0}\; \text{undefined — in no set}").scale(1.05).shift(band_shift(7) + UP * 0.4)
        b7_s3 = MathTex(r"0{,}\dot{1}\dot{2} = \tfrac{12}{99} = \tfrac{4}{33} \in \mathbb{Q}").scale(1.05).shift(band_shift(7) + DOWN * 0.5)
        b7_s4 = Tex(r"Long $\neq$ endless: $0{,}123456789 \in \mathbb{Q}$").scale(1.05).shift(band_shift(7) + DOWN * 1.4)
        b7_s5 = Tex("Simplify first, then list every box").scale(1.05).shift(band_shift(7) + DOWN * 2.3)
        for m in (b7_s1, b7_s2, b7_s3, b7_s4, b7_s5):
            self.play(Write(m))
            self.wait(1.8)
        self.play(Create(SurroundingRectangle(b7_s5, color=YELLOW)))
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): sheep, debt, bread
        self.next_band(8)
        b8_title = Tex("Counting sheep, owing money, sharing bread").scale(1.15).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Count sheep: $1, 2, 3, \ldots$ — natural").scale(1.05).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex(r"No sheep: add $0$ — whole").scale(1.05).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex(r"Owe R30, Sutherland $-8^\circ$C — integers").scale(1.05).shift(band_shift(8) + DOWN * 0.5)
        b8_l4 = Tex(r"Share a loaf: $\tfrac{1}{3}$, taxi R12,50 — rational").scale(1.05).shift(band_shift(8) + DOWN * 1.4)
        for m in (b8_l1, b8_l2, b8_l3, b8_l4):
            self.play(Write(m))
            self.wait(2.2)
        b8_l5 = Tex("Smallest box first — then every box around it").scale(1.05).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l5))
        self.wait(2.5)

        # --- Band 9 (subtopic_6): does the decimal ever stop?
        self.next_band(9)
        b9_title = Tex("Does the decimal ever stop?").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Stops: $0{,}25$ of a rand $= 25$c — rational").scale(1.05).shift(band_shift(9) + UP * 1.3)
        b9_l2 = Tex(r"Repeats: R1 shared by 3 $= 0{,}333\ldots = \tfrac{1}{3}$ — rational").scale(1.0).shift(band_shift(9) + UP * 0.4)
        b9_l3 = MathTex(r"10x - x = 6{,}666\ldots - 0{,}666\ldots \Rightarrow 9x = 6,\; x = \tfrac{2}{3}").scale(0.95).shift(band_shift(9) + DOWN * 0.5)
        b9_l4 = Tex(r"Never stops, never repeats: $\sqrt{2}$, $\pi$ — irrational").scale(1.0).shift(band_shift(9) + DOWN * 1.4)
        b9_l5 = Tex(r"Impostors: $\tfrac{22}{7}$ repeats, $3{,}14$ stops — both rational").scale(1.0).shift(band_shift(9) + DOWN * 2.3)
        for m in (b9_l1, b9_l2, b9_l3, b9_l4, b9_l5):
            self.play(Write(m))
            self.wait(2.2)
        self.wait(1.5)

        # --- Band 10 (subtopic_7): every number in its box
        self.next_band(10)
        b10_title = Tex("Every number in its box").scale(1.2).shift(band_shift(10) + UP * 2.4)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"\sqrt{9} = 3 \to \text{every box} \qquad \sqrt{2} \to \mathbb{Q}'").scale(1.05).shift(band_shift(10) + UP * 1.3)
        b10_l2 = MathTex(r"-\sqrt{16} = -4 \to \mathbb{Z} \qquad \tfrac{8}{2} = 4 \to \mathbb{N}").scale(1.05).shift(band_shift(10) + UP * 0.4)
        b10_l3 = Tex(r"$0{,}123456789$ stops $\to$ rational; $\tfrac{5}{0}$ $\to$ no box").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        b10_l4 = MathTex(r"3^2 = 9 < 10 < 16 = 4^2 \Rightarrow 3 < \sqrt{10} < 4").scale(1.0).shift(band_shift(10) + DOWN * 1.4)
        b10_l5 = MathTex(r"3{,}1 < \sqrt{10} < 3{,}2 \approx 3{,}162").scale(1.05).shift(band_shift(10) + DOWN * 2.3)
        for m in (b10_l1, b10_l2, b10_l3, b10_l4):
            self.play(Write(m))
            self.wait(2.2)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(4)
