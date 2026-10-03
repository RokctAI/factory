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


def mini_axes(origin, w=3.2, h=3.0):
    """Small Cartesian axes drawn from primitives, origin at bottom-left."""
    g = VGroup()
    g.add(Line(origin + LEFT * 0.4, origin + RIGHT * w, color=WHITE))
    g.add(Line(origin + DOWN * 0.4, origin + UP * h, color=WHITE))
    return g


def plot_points(origin, pairs, sx=0.5, sy=0.25, color=YELLOW):
    return VGroup(*[Dot(origin + RIGHT * x * sx + UP * y * sy, radius=0.07, color=color) for x, y in pairs])


class EquivalentRepresentationsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): five descriptions
        title = Tex("One Relationship, Five Descriptions").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = Tex(r"Words: ``multiply by 3, then add 2'' \quad Diagram: $x \to \times 3 \to +2 \to y$").scale(0.85).shift(UP * 1.4)
        l2 = MathTex(r"\text{Formula: } y = 3x + 2 \qquad \text{Table: } (0, 2), (1, 5), (2, 8), (3, 11)").scale(0.9).shift(UP * 0.5)
        ax = mini_axes(np.array([-5.5, -2.2, 0]), w=3.0, h=2.6)
        pts = plot_points(np.array([-5.5, -2.2, 0]), [(0, 2), (1, 5), (2, 8), (3, 11)], sx=0.6, sy=0.2)
        line = Line(np.array([-5.5, -2.2 + 2 * 0.2, 0]), np.array([-5.5 + 3.4 * 0.6, -2.2 + (3 * 3.4 + 2) * 0.2, 0]), color=BLUE)
        self.play(Write(l1))
        self.wait(2)
        self.play(Write(l2))
        self.wait(2)
        self.play(Create(ax))
        self.play(Create(pts))
        self.play(Create(line))
        l3 = Tex("Constant step in the table $\\Rightarrow$ a straight line").scale(0.9).shift(DOWN * 1.2 + RIGHT * 2.0)
        self.play(Write(l3))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): table to graph and back
        self.next_band(1)
        b1_title = Tex("Table to graph and back").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Crossing on the vertical axis: output at $x = 0$, the constant 2").scale(0.9).shift(band_shift(1) + UP * 1.3)
        b1_l2 = Tex(r"Steepness: up 3 for every 1 across, the coefficient 3").scale(0.9).shift(band_shift(1) + UP * 0.4)
        b1_l3 = MathTex(r"y = x^2 + 1: \; (-2, 5), (-1, 2), (0, 1), (1, 2), (2, 5) \;\text{-- a curve, not a line}").scale(0.85).shift(band_shift(1) + DOWN * 0.5)
        b1_l4 = MathTex(r"3x + 2 = 2x + 5 \Rightarrow x = 3,\; y = 11: \text{ the lines meet at } (3, 11)").scale(0.85).shift(band_shift(1) + DOWN * 1.5)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): testing equivalence
        self.next_band(2)
        b2_title = Tex("Testing equivalence").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"3x + 2 \text{ vs } 3(x + 2): \; x = 1 \text{ gives } 5 \text{ and } 9 \;\Rightarrow\; \text{not equivalent}").scale(0.85).shift(band_shift(2) + UP * 1.3)
        b2_l2 = MathTex(r"2x + 4 \text{ vs } 2(x + 2) = 2x + 4 \;\Rightarrow\; \text{equivalent}").scale(0.9).shift(band_shift(2) + UP * 0.3)
        b2_l3 = Tex(r"One disagreement disproves. Matching expanded formulae prove.").scale(0.9).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = Tex(r"``three times the sum of a number and two'' $= 3(x+2)$, not $3x + 2$").scale(0.85).shift(band_shift(2) + DOWN * 1.6)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): interpreting in context
        self.next_band(3)
        b3_title = Tex("Interpreting the graph in context").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"C = 3k + 2: \; 2 = \text{flag fall},\; 3 = \text{rand per km}").scale(0.95).shift(band_shift(3) + UP * 1.3)
        b3_l2 = MathTex(r"C = 5k \text{ meets it where } 3k + 2 = 5k \Rightarrow k = 1,\; C = 5").scale(0.9).shift(band_shift(3) + UP * 0.4)
        b3_l3 = MathTex(r"B = 20 - 3t: \text{ starts at 20, falls 3 per hour, zero at } t \approx 6{,}67").scale(0.85).shift(band_shift(3) + DOWN * 0.5)
        b3_l4 = Tex(r"Whole-number contexts: separate points, not a continuous line").scale(0.9).shift(band_shift(3) + DOWN * 1.4)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(1.5)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"(2, 5) \text{ plotted as 5 across, 2 up}").scale(1.0).shift(band_shift(4) + UP * 1.3)
        b4_l2 = Tex(r"A straight line through the points of $x^2 + 1$").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4_l3 = Tex(r"``Equivalent because they agree at $x = 1$''").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = Tex(r"Crossing point called the rate").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): same taxi
        self.next_band(5)
        b5_title = Tex("Same taxi, five pictures").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        rows = [
            r"\text{Words: R2 to get in, R3 a kilometre}",
            r"\text{Diagram: } k \to \times 3 \to +2 \to C",
            r"\text{Formula: } C = 3k + 2",
            r"\text{Table: } 2, 5, 8, 11 \qquad \text{Graph: dots in a straight row}",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.9).shift(band_shift(5) + UP * (1.3 - 0.8 * i))
            self.play(Write(m))
            self.wait(2.0)
        b5_l5 = Tex("Changing pictures never changes the taxi").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): plotting
        self.next_band(6)
        b6_title = Tex("Plotting the dots: across, then up").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        ax2 = mini_axes(band_shift(6) + np.array([-5.5, -2.0, 0]), w=3.4, h=3.0)
        pts2 = plot_points(band_shift(6) + np.array([-5.5, -2.0, 0]), [(0, 2), (1, 5), (2, 8), (3, 11), (5, 17)], sx=0.55, sy=0.16)
        self.play(Create(ax2))
        self.play(Create(pts2))
        self.wait(1.5)
        b6_l1 = Tex(r"5 km: up to the line, across to the money axis: R17").scale(0.85).shift(band_shift(6) + UP * 1.0 + RIGHT * 2.3)
        b6_l2 = Tex(r"R20: across to the line, down: 6 km").scale(0.85).shift(band_shift(6) + UP * 0.2 + RIGHT * 2.3)
        b6_l3 = Tex(r"Downhill: $20 - 3t$. U-shape: $x^2 + 1$.").scale(0.85).shift(band_shift(6) + DOWN * 0.6 + RIGHT * 2.3)
        for m in (b6_l1, b6_l2, b6_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(1.5)

        # --- Band 7 (subtopic_7): are they the same
        self.next_band(7)
        b7_title = Tex("Are they really the same?").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"Step 1: try a number. Disagree once? Different. Done.").scale(0.9).shift(band_shift(7) + UP * 1.3)
        b7_l2 = Tex(r"Step 2: keep agreeing? Formulas, expand, compare.").scale(0.9).shift(band_shift(7) + UP * 0.4)
        b7_l3 = MathTex(r"2(x + 2) = 2x + 4 \;\checkmark \qquad 3(x + 2) = 3x + 6 \neq 3x + 2").scale(0.9).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex("Across then up. Constant step, straight line. Start and rate. Words to formula first.").scale(0.75).shift(band_shift(7) + DOWN * 1.5)
        for m in (b7_l1, b7_l2, b7_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
