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


def balance(centre, left_label, right_label, width=4.0):
    """A balance scale: a beam, a pivot and two pans labelled with the two
    sides of an equation."""
    g = VGroup()
    g.add(Line(centre + LEFT * width / 2, centre + RIGHT * width / 2, color=GREY, stroke_width=5))
    g.add(Polygon(centre, centre + DOWN * 0.6 + LEFT * 0.3, centre + DOWN * 0.6 + RIGHT * 0.3, color=GREY))
    for side, lab in ((LEFT, left_label), (RIGHT, right_label)):
        pan = Rectangle(width=1.6, height=0.6, color=ORANGE).move_to(centre + side * width / 2 + DOWN * 0.5)
        g.add(Line(centre + side * width / 2, pan.get_top(), color=GREY))
        g.add(pan)
        g.add(MathTex(lab).scale(0.8).move_to(pan))
    return g


class EquationsInversesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): inspection
        title = Tex("Equations: inspection, inverses, exponents").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"x + 7 = 12 \Rightarrow x = 5 \qquad 3x = 21 \Rightarrow x = 7 \qquad \tfrac{x}{4} = 6 \Rightarrow x = 24").scale(0.9).shift(UP * 1.3)
        l2 = MathTex(r"x^2 = 49 \Rightarrow x = 7 \;\text{or}\; x = -7").scale(1.0).shift(UP * 0.3)
        l3 = MathTex(r"x^3 = -8 \Rightarrow x = -2 \qquad 2^x = 32 \Rightarrow x = 5").scale(1.0).shift(DOWN * 0.7)
        l4 = MathTex(r"x + 3 = x + 5: \;\text{no solution} \qquad 2(x + 1) = 2x + 2: \;\text{every } x").scale(0.85).shift(DOWN * 1.7)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l2, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): inverses
        self.next_band(1)
        b1_title = Tex("Inverses: undo in reverse order, both sides").scale(1.05).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        sc = balance(band_shift(1) + UP * 1.0, r"3x - 5", r"16")
        self.play(Create(sc))
        self.wait(1.5)
        b1_l1 = MathTex(r"3x - 5 = 16 \;\xrightarrow{+5}\; 3x = 21 \;\xrightarrow{\div 3}\; x = 7").scale(1.0).shift(band_shift(1) + DOWN * 0.3)
        b1_l2 = MathTex(r"\tfrac{x}{4} + 3 = 8 \;\xrightarrow{-3}\; \tfrac{x}{4} = 5 \;\xrightarrow{\times 4}\; x = 20").scale(0.95).shift(band_shift(1) + DOWN * 1.2)
        b1_l3 = MathTex(r"10 - 2x = 4 \;\xrightarrow{-10}\; -2x = -6 \;\xrightarrow{\div (-2)}\; x = 3").scale(0.95).shift(band_shift(1) + DOWN * 2.1)
        for m in (b1_l1, b1_l2, b1_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): brackets, fractions, exponents
        self.next_band(2)
        b2_title = Tex("Brackets first, LCD for fractions, same base for exponents").scale(0.95).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"2(x - 3) = x + 5 \Rightarrow 2x - 6 = x + 5 \Rightarrow x = 11").scale(0.95).shift(band_shift(2) + UP * 1.3)
        b2_l2 = MathTex(r"5(x + 2) = 3(x + 6) \Rightarrow 5x + 10 = 3x + 18 \Rightarrow 2x = 8 \Rightarrow x = 4").scale(0.9).shift(band_shift(2) + UP * 0.3)
        b2_l3 = MathTex(r"\tfrac{x}{2} - \tfrac{x}{3} = 2 \;\xrightarrow{\times 6}\; 3x - 2x = 12 \Rightarrow x = 12").scale(0.95).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = MathTex(r"3^{x + 1} = 81 = 3^4 \Rightarrow x + 1 = 4 \Rightarrow x = 3 \qquad 2^x = \tfrac{1}{8} = 2^{-3} \Rightarrow x = -3").scale(0.85).shift(band_shift(2) + DOWN * 1.7)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): word problems
        self.next_band(3)
        b3_title = Tex("Words to equations: letter, equation, solve, answer").scale(1.0).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{Taxi: } 12k + 20 = 104 \Rightarrow 12k = 84 \Rightarrow k = 7 \text{ km}").scale(0.95).shift(band_shift(3) + UP * 1.3)
        b3_l2 = MathTex(r"\text{Ages: } s + (2s + 3) = 27 \Rightarrow 3s = 24 \Rightarrow s = 8,\; \text{Sipho } 19").scale(0.9).shift(band_shift(3) + UP * 0.3)
        b3_l3 = MathTex(r"\text{Rectangle: } 2(w + w + 3) = 26 \Rightarrow 4w = 20 \Rightarrow w = 5 \text{ cm}").scale(0.9).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = Tex("Check against the story, and answer the quantity that was asked for.").scale(0.85).shift(band_shift(3) + DOWN * 1.7)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(1.5)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"3x - 5 = 16 \Rightarrow 3x = 11").scale(1.0).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"-2x = -6 \Rightarrow x = -3").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"2(x - 3) = 2x - 3").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"x^2 = 49 \Rightarrow x = 7 \;\text{only}").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): see it when you can
        self.next_band(5)
        b5_title = Tex("See it when you can").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        box = Square(side_length=1.2, color=ORANGE).shift(band_shift(5) + LEFT * 4.5 + UP * 1.0)
        box_lab = MathTex(r"x").scale(1.2).move_to(box)
        self.play(Create(box), Write(box_lab))
        self.wait(1.2)
        b5_l1 = MathTex(r"x + 7 = 12 \Rightarrow x = 5 \qquad 3x = 21 \Rightarrow x = 7").scale(0.95).shift(band_shift(5) + RIGHT * 1.2 + UP * 1.2)
        b5_l2 = MathTex(r"x^2 = 49 \Rightarrow x = 7 \;\text{or}\; -7 \qquad x^3 = -8 \Rightarrow x = -2").scale(0.9).shift(band_shift(5) + RIGHT * 1.2 + UP * 0.2)
        b5_l3 = MathTex(r"2^x = 32: \; 2, 4, 8, 16, 32 \Rightarrow x = 5").scale(0.95).shift(band_shift(5) + DOWN * 0.8)
        b5_l4 = Tex("One-step locks by sight. Two or more steps: undo buttons.").scale(0.85).shift(band_shift(5) + DOWN * 1.8)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): undo buttons
        self.next_band(6)
        b6_title = Tex("Undo buttons in reverse order").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"x \;\xrightarrow{\times 3}\; 3x \;\xrightarrow{-5}\; 3x - 5 = 16").scale(1.0).shift(band_shift(6) + UP * 1.3)
        b6_l2 = MathTex(r"16 \;\xrightarrow{+5}\; 21 \;\xrightarrow{\div 3}\; 7 = x").scale(1.0).shift(band_shift(6) + UP * 0.3)
        b6_l3 = MathTex(r"10 - 2x = 4 \Rightarrow -2x = -6 \Rightarrow x = 3 \;\;(\div\, -2,\;\text{not } 2)").scale(0.9).shift(band_shift(6) + DOWN * 0.7)
        b6_l4 = Tex("Shoes before socks. Both sides. Brackets open first. Fractions: times the LCD everywhere.").scale(0.75).shift(band_shift(6) + DOWN * 1.7)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2)

        # --- Band 7 (subtopic_7): story to equation
        self.next_band(7)
        b7_title = Tex("Turn the story into a sentence with an equals sign").scale(1.0).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("1. Letter and meaning \\quad 2. Equation \\quad 3. Undo \\quad 4. Answer with units").scale(0.8).shift(band_shift(7) + UP * 1.3)
        b7_l2 = MathTex(r"\text{Let } k = \text{km}: \; 12k + 20 = 104 \Rightarrow k = 7 \text{ km}").scale(0.95).shift(band_shift(7) + UP * 0.3)
        b7_l3 = MathTex(r"\text{Let } s = \text{sister}: \; 3s + 3 = 27 \Rightarrow s = 8,\; \text{Sipho} = 2(8) + 3 = 19").scale(0.9).shift(band_shift(7) + DOWN * 0.7)
        b7_l4 = Tex("See it. Undo it. Same base. Put it back in the box.").scale(0.85).shift(band_shift(7) + DOWN * 1.7)
        for m in (b7_l1, b7_l2, b7_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
