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


def flow_diagram(labels, origin, box_w=1.6):
    """Input -> [box] -> [box] -> output as a VGroup of primitives."""
    g = VGroup()
    x = origin[0]
    y = origin[1]
    inp = MathTex(labels[0]).scale(0.9).move_to([x, y, 0])
    g.add(inp)
    x += 1.2
    for lab in labels[1:-1]:
        g.add(Line([x, y, 0], [x + 0.5, y, 0], color=WHITE))
        x += 0.5
        box = Rectangle(width=box_w, height=0.8, color=BLUE).move_to([x + box_w / 2, y, 0])
        g.add(box)
        g.add(Tex(lab).scale(0.75).move_to(box))
        x += box_w
    g.add(Line([x, y, 0], [x + 0.5, y, 0], color=WHITE))
    x += 0.5
    g.add(MathTex(labels[-1]).scale(0.9).move_to([x + 0.5, y, 0]))
    return g


class InputOutputRulesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): flow diagrams
        title = Tex("Input, Rule, Output").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        fd = flow_diagram([r"x", r"$\times 3$", r"$+ 2$", r"y"], np.array([-3.5, 1.4, 0]))
        self.play(Create(fd))
        self.wait(1.5)
        l1 = MathTex(r"4 \to 12 \to 14 \qquad -2 \to -6 \to -4 \qquad 0 \to 0 \to 2").scale(0.95).shift(UP * 0.3)
        l2 = MathTex(r"\text{Swapped: } +2 \text{ then } \times 3: \; 4 \to 6 \to 18 \quad y = 3(x+2)").scale(0.9).shift(DOWN * 0.6)
        l3 = MathTex(r"\text{Backwards from } 20: \; 20 - 2 = 18,\; 18 \div 3 = 6").scale(0.95).shift(DOWN * 1.5)
        for m in (l1, l2, l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): tables
        self.next_band(1)
        b1_title = Tex("Tables: rise per unit input").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"x: 1, 2, 3, 4 \quad y: 5, 8, 11, 14 \quad\Rightarrow\quad y = 3x + 2").scale(0.95).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"x: 2, 5, 10 \quad y: 7, 16, 31 \quad \tfrac{9}{3} = \tfrac{15}{5} = 3 \;\Rightarrow\; y = 3x + 1").scale(0.9).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"x: 1, 2, 3, 4 \quad y: 2, 5, 10, 17 \quad\Rightarrow\quad y = x^2 + 1").scale(0.95).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = MathTex(r"\text{At } x = 0: \; y = c \;\text{(the constant on its own)}").scale(0.95).shift(band_shift(1) + DOWN * 1.8)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): equations
        self.next_band(2)
        b2_title = Tex("Finding inputs: the diagram in reverse").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"3x + 2 = 32 \;\Rightarrow\; 3x = 30 \;\Rightarrow\; x = 10").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = MathTex(r"2x - 5 = -11 \;\Rightarrow\; 2x = -6 \;\Rightarrow\; x = -3").scale(1.0).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"x^2 - 1 = 24 \;\Rightarrow\; x^2 = 25 \;\Rightarrow\; x = 5 \text{ or } x = -5").scale(1.0).shift(band_shift(2) + DOWN * 0.8)
        b2_l4 = MathTex(r"\frac{2x - 3}{5} = 3 \;\Rightarrow\; 2x - 3 = 15 \;\Rightarrow\; x = 9").scale(1.0).shift(band_shift(2) + DOWN * 1.8)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): representations
        self.next_band(3)
        b3_title = Tex("Four representations, one rule").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        rows = [
            r"\text{Flow diagram: order of operations}",
            r"\text{Table: spot and test the rule}",
            r"\text{Formula: } y = 3x + 2 \text{ (general)}",
            r"\text{Equation: } 3x + 2 = 32 \text{ (recover an input)}",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.9).shift(band_shift(3) + UP * (1.3 - 0.8 * i))
            self.play(Write(m))
            self.wait(2.0)
        self.wait(1.5)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"3x + 2 \text{ read as } 3(x + 2): \; 4 \to 18").scale(1.0).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"20 \div 3 - 2 = 4{,}67 \;\text{(undone in forward order)}").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"y = 9x - 11 \;\text{(raw difference used as rate)}").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"x^2 = 25 \Rightarrow x = 5 \;\text{only}").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): the machine
        self.next_band(5)
        b5_title = Tex("The sausage machine").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        fd2 = flow_diagram([r"4", r"$\times 3$", r"$+ 2$", r"14"], band_shift(5) + np.array([-3.5, 1.2, 0]))
        self.play(Create(fd2))
        self.wait(2)
        b5_l1 = Tex("Same gears, different order: a different machine").scale(0.95).shift(band_shift(5) + UP * 0.2)
        b5_l2 = MathTex(r"3x + 2 \quad\text{vs}\quad 3(x + 2): \text{ the bracket says ``do me first''}").scale(0.9).shift(band_shift(5) + DOWN * 0.7)
        b5_l3 = Tex(r"Missing gear: $4 \to 12 \to 14$ and $1 \to 3 \to 5$, so ``$+2$''").scale(0.9).shift(band_shift(5) + DOWN * 1.6)
        for m in (b5_l1, b5_l2, b5_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(1.5)

        # --- Band 6 (subtopic_6): backwards
        self.next_band(6)
        b6_title = Tex("Backwards: socks and shoes").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        fd3 = flow_diagram([r"6", r"$\div 3$", r"$- 2$", r"20"], band_shift(6) + np.array([-3.5, 1.2, 0]))
        self.play(Create(fd3))
        self.wait(1.5)
        b6_l1 = Tex(r"Read right to left: $20 \to 18 \to 6$. Undo the last gear first.").scale(0.9).shift(band_shift(6) + UP * 0.2)
        b6_l2 = Tex(r"Wrong order: $20 \div 3 - 2 = 4{,}67$ -- ugly means wrong").scale(0.9).shift(band_shift(6) + DOWN * 0.7)
        b6_l3 = MathTex(r"\text{Square gear: } 24 \to 25 \to 5 \text{ or } -5").scale(0.95).shift(band_shift(6) + DOWN * 1.6)
        for m in (b6_l1, b6_l2, b6_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): detective
        self.next_band(7)
        b7_title = Tex("Reading a table like a detective").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"Clue 1: output rises 3 per step of input $\Rightarrow$ ``$\times 3$''").scale(0.9).shift(band_shift(7) + UP * 1.3)
        b7_l2 = Tex(r"Clue 2: one row (best: input 0) $\Rightarrow$ ``$+2$''").scale(0.9).shift(band_shift(7) + UP * 0.4)
        b7_l3 = Tex(r"Jumps growing by 2 $\Rightarrow$ a square gear: 2, 5, 10, 17 is $x^2 + 1$").scale(0.9).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = MathTex(r"\text{Hole: output } 29 \to 29 - 2 = 27 \to 27 \div 3 = 9").scale(0.95).shift(band_shift(7) + DOWN * 1.4)
        b7_l5 = Tex("Forwards for outputs. Backwards for inputs. Check forwards.").scale(0.9).shift(band_shift(7) + DOWN * 2.3)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=YELLOW)))
        self.wait(4)
