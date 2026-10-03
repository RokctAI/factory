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


def flow_diagram(centre, steps, width=2.3):
    """A left-to-right chain of boxed steps joined by arrows: the five moves
    of the factorising method."""
    g = VGroup()
    n = len(steps)
    total = n * width + (n - 1) * 0.5
    x0 = -total / 2 + width / 2
    boxes = []
    for i, s in enumerate(steps):
        pos = centre + RIGHT * (x0 + i * (width + 0.5))
        b = Rectangle(width=width, height=0.8, color=BLUE).move_to(pos)
        g.add(b)
        g.add(Tex(s).scale(0.55).move_to(pos))
        boxes.append(b)
    for a, b in zip(boxes, boxes[1:]):
        g.add(Arrow(a.get_right(), b.get_left(), buff=0.05, color=GREY))
    return g


class FactorisedEquationsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): zero product
        title = Tex("Solving by factorising: a product equal to zero").scale(1.05).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"ab = 0 \;\Rightarrow\; a = 0 \;\text{or}\; b = 0").scale(1.1).shift(UP * 1.3)
        l2 = MathTex(r"(x - 2)(x + 7) = 0 \;\Rightarrow\; x - 2 = 0 \;\text{or}\; x + 7 = 0 \;\Rightarrow\; x = 2 \;\text{or}\; x = -7").scale(0.85).shift(UP * 0.3)
        l3 = MathTex(r"3x(x - 4) = 0 \;\Rightarrow\; x = 0 \;\text{or}\; x = 4").scale(1.0).shift(DOWN * 0.7)
        l4 = MathTex(r"(x - 2)(x + 7) = 6 \;\text{cannot be split: } 1 \times 6,\; 2 \times 3,\; \ldots").scale(0.85).shift(DOWN * 1.7)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): trinomial equations
        self.next_band(1)
        b1_title = Tex("Trinomial equations: factorise, then each factor to zero").scale(0.95).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"x^2 + 8x + 15 = 0 \;\Rightarrow\; (x + 3)(x + 5) = 0 \;\Rightarrow\; x = -3 \;\text{or}\; x = -5").scale(0.85).shift(band_shift(1) + UP * 1.3)
        b1_l2 = MathTex(r"\text{check } x = -3: \; 9 - 24 + 15 = 0 \;\checkmark").scale(0.9).shift(band_shift(1) + UP * 0.3)
        b1_l3 = MathTex(r"x^2 - 3x - 10 = 0 \;\Rightarrow\; (x + 2)(x - 5) = 0 \;\Rightarrow\; x = -2 \;\text{or}\; x = 5").scale(0.85).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = MathTex(r"x^2 - 8x + 16 = 0 \;\Rightarrow\; (x - 4)^2 = 0 \;\Rightarrow\; x = 4 \;\text{(repeated)}").scale(0.85).shift(band_shift(1) + DOWN * 1.7)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): rearranging to zero
        self.next_band(2)
        b2_title = Tex("Zero on one side first").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"x^2 = 5x \;\Rightarrow\; x^2 - 5x = 0 \;\Rightarrow\; x(x - 5) = 0 \;\Rightarrow\; x = 0 \;\text{or}\; x = 5").scale(0.85).shift(band_shift(2) + UP * 1.3)
        b2_l2 = MathTex(r"x^2 = 49 \;\Rightarrow\; (x + 7)(x - 7) = 0 \;\Rightarrow\; x = \pm 7").scale(0.9).shift(band_shift(2) + UP * 0.3)
        b2_l3 = MathTex(r"x^2 + 6x = -8 \;\Rightarrow\; (x + 2)(x + 4) = 0 \;\Rightarrow\; x = -2 \;\text{or}\; x = -4").scale(0.85).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = MathTex(r"x(x + 3) = 10 \;\Rightarrow\; x^2 + 3x - 10 = 0 \;\Rightarrow\; (x + 5)(x - 2) = 0 \;\Rightarrow\; x = -5 \;\text{or}\; 2").scale(0.8).shift(band_shift(2) + DOWN * 1.7)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): context
        self.next_band(3)
        b3_title = Tex("In context: solve, then interpret both solutions").scale(1.0).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        rect = Rectangle(width=3.2, height=2.0, color=ORANGE).shift(band_shift(3) + LEFT * 4.2 + UP * 0.6)
        lw = MathTex(r"w").scale(0.8).next_to(rect, LEFT)
        ll = MathTex(r"w + 3").scale(0.8).next_to(rect, UP)
        la = MathTex(r"40").scale(0.9).move_to(rect)
        self.play(Create(rect), Write(lw), Write(ll), Write(la))
        self.wait(1.5)
        b3_l1 = MathTex(r"w(w + 3) = 40 \;\Rightarrow\; w^2 + 3w - 40 = 0 \;\Rightarrow\; (w + 8)(w - 5) = 0").scale(0.8).shift(band_shift(3) + RIGHT * 1.8 + UP * 1.2)
        b3_l2 = MathTex(r"w = -8 \;\text{(rejected: width cannot be negative)} \;\text{or}\; w = 5").scale(0.8).shift(band_shift(3) + RIGHT * 1.8 + UP * 0.2)
        b3_l3 = MathTex(r"\text{width } 5 \text{ cm, length } 8 \text{ cm}; \; 5 \times 8 = 40 \;\checkmark").scale(0.85).shift(band_shift(3) + RIGHT * 1.8 + DOWN * 0.8)
        b3_l4 = MathTex(r"n^2 + n = 12 \;\Rightarrow\; (n + 4)(n - 3) = 0 \;\Rightarrow\; n = -4 \;\text{or}\; 3 \;\text{(both kept)}").scale(0.8).shift(band_shift(3) + DOWN * 1.9)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(1.5)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"x^2 = 5x \;\Rightarrow\; x = 5 \;\text{(divided by } x)").scale(0.95).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"(x - 2)(x + 7) = 6 \;\Rightarrow\; x - 2 = 6").scale(0.95).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"(x + 3)(x + 5) = 0 \;\Rightarrow\; x = 3 \;\text{or}\; x = 5").scale(0.95).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"w = -8 \;\text{or}\; w = 5 \;\text{(no rejection)}").scale(0.95).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): zero's one trick
        self.next_band(5)
        b5_title = Tex("Zero's one trick").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"\square \times \square = 12: \; 3 \times 4,\; 2 \times 6,\; 1 \times 12,\; 24 \times \tfrac{1}{2} \ldots \;\text{(no idea)}").scale(0.85).shift(band_shift(5) + UP * 1.3)
        b5_l2 = MathTex(r"\square \times \square = 0: \;\text{one of them IS } 0").scale(1.0).shift(band_shift(5) + UP * 0.3)
        b5_l3 = MathTex(r"(x - 2)(x + 7) = 0 \;\Rightarrow\; x = 2 \;\text{or}\; x = -7 \qquad 3x(x - 4) = 0 \;\Rightarrow\; x = 0 \;\text{or}\; 4").scale(0.8).shift(band_shift(5) + DOWN * 0.7)
        b5_l4 = Tex("Only zero does this. A product equal to 6 tells you nothing.").scale(0.85).shift(band_shift(5) + DOWN * 1.7)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): zero on one side, two-number game
        self.next_band(6)
        b6_title = Tex("Zero on one side, then the two-number game").scale(1.05).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"x^2 = 5x \;\Rightarrow\; x^2 - 5x = 0 \;\Rightarrow\; x(x - 5) = 0 \;\Rightarrow\; x = 0 \;\text{or}\; 5").scale(0.85).shift(band_shift(6) + UP * 1.3)
        b6_l2 = MathTex(r"x^2 + 8x + 15 = 0: \;\text{multiply to } 15,\;\text{add to } 8 \;\Rightarrow\; (x + 3)(x + 5) = 0").scale(0.8).shift(band_shift(6) + UP * 0.3)
        b6_l3 = MathTex(r"x + 3 = 0 \;\Rightarrow\; x = -3 \qquad x + 5 = 0 \;\Rightarrow\; x = -5 \;\text{(signs flip)}").scale(0.85).shift(band_shift(6) + DOWN * 0.7)
        b6_l4 = Tex("Never divide by $x$. Solve the little equations; do not read the brackets.").scale(0.8).shift(band_shift(6) + DOWN * 1.7)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)

        # --- Band 7 (subtopic_7): check both, keep the ones that make sense
        self.next_band(7)
        b7_title = Tex("Check both, keep the ones that make sense").scale(1.05).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        fd = flow_diagram(band_shift(7) + UP * 1.2, ["zero on one side", "factorise", "each bracket to 0", "solve", "check both"], width=2.2)
        self.play(Create(fd))
        self.wait(2.5)
        b7_l1 = MathTex(r"w = -8 \;\text{or}\; 5: \;\text{a width cannot be negative} \;\Rightarrow\; w = 5 \text{ cm}").scale(0.85).shift(band_shift(7) + UP * 0.1)
        b7_l2 = MathTex(r"n = -4 \;\text{or}\; 3: \;\text{no story forbids either} \;\Rightarrow\; \text{both stay}").scale(0.85).shift(band_shift(7) + DOWN * 0.8)
        b7_l3 = Tex("Zero across. Factorise. Each bracket to zero. Solve. Check both and decide.").scale(0.8).shift(band_shift(7) + DOWN * 1.8)
        for m in (b7_l1, b7_l2):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=YELLOW)))
        self.wait(4)
