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


def table_row(n, origin, size=0.7):
    """n square tables in a row with one seat dot per free side."""
    g = VGroup()
    for i in range(n):
        c = origin + RIGHT * i * size
        g.add(Square(side_length=size, color=BLUE).move_to(c))
        g.add(Dot(c + UP * size * 0.75, radius=0.07, color=YELLOW))
        g.add(Dot(c + DOWN * size * 0.75, radius=0.07, color=YELLOW))
    g.add(Dot(origin + LEFT * size * 0.75, radius=0.07, color=YELLOW))
    g.add(Dot(origin + RIGHT * (n - 1) * size + RIGHT * size * 0.75, radius=0.07, color=YELLOW))
    return g


def border_square(n, origin, gap=0.32):
    g = VGroup()
    for i in range(n):
        for j in range(n):
            edge = i in (0, n - 1) or j in (0, n - 1)
            g.add(Dot(origin + RIGHT * i * gap + UP * j * gap, radius=0.06,
                      color=YELLOW if edge else GREY))
    return g


class JustifyingRulesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): words and algebra
        title = Tex("Describing and Justifying Rules").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = Tex(r"``Start at 5, add 3 each time'' $\;\to\; T_n = 3n + 2$").scale(1.0).shift(UP * 1.3)
        l2 = Tex(r"``Double the position, add 1'' $\;\to\; T_n = 2n + 1$: 3, 5, 7, 9").scale(1.0).shift(UP * 0.3)
        l3 = MathTex(r"T_n = 3(n - 1) + 5: \;\text{one less than } n, \times 3, + 5 \;\to\; 5, 8, 11").scale(0.9).shift(DOWN * 0.7)
        l4 = MathTex(r"P = 2t + 2 \qquad C = 3k + 2 \qquad T_5 \neq T \times 5").scale(0.95).shift(DOWN * 1.7)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): justify from structure
        self.next_band(1)
        b1_title = Tex("Tables in a row: 4, 6, 8, ...").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        tables = table_row(3, band_shift(1) + UP * 1.0 + LEFT * 3.5)
        self.play(Create(tables))
        self.wait(2)
        b1_l1 = MathTex(r"P = \underbrace{n + n}_{\text{two long sides}} + \underbrace{2}_{\text{two ends}} = 2n + 2").scale(1.0).shift(band_shift(1) + UP * 0.9 + RIGHT * 2.5)
        b1_l2 = MathTex(r"\text{Matchsticks: } 3n + 1 \;(\text{3 per square, 1 to close the first})").scale(0.9).shift(band_shift(1) + DOWN * 0.7)
        b1_l3 = MathTex(r"\text{Border dots: } 4n - 4 \;(\text{four sides, corners counted twice})").scale(0.9).shift(band_shift(1) + DOWN * 1.6)
        for m in (b1_l1, b1_l2, b1_l3):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): equivalent rules
        self.next_band(2)
        b2_title = Tex("One border, four rules").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        sq = border_square(5, band_shift(2) + UP * 0.2 + LEFT * 5.5)
        self.play(Create(sq))
        self.wait(1.5)
        rows = [
            r"4n - 4",
            r"4(n - 1) = 4n - 4",
            r"2n + 2(n - 2) = 4n - 4",
            r"n^2 - (n - 2)^2 = 4n - 4",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.95).shift(band_shift(2) + UP * (1.3 - 0.8 * i) + RIGHT * 1.5)
            self.play(Write(m))
            self.wait(2.0)
        b2_l5 = MathTex(r"n = 5: \; 16, 16, 16, 16 \qquad n = 3: \; 8, 8, 8, 8").scale(0.9).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2_l5))
        self.wait(2.5)

        # --- Band 3 (subtopic_4): the circle that breaks
        self.next_band(3)
        b3_title = Tex("When a rule fails").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        circ = Circle(radius=1.0, color=WHITE).shift(band_shift(3) + UP * 0.6 + LEFT * 4.5)
        pts = [circ.point_at_angle(a) for a in np.linspace(0, TAU, 6, endpoint=False)]
        chords = VGroup(*[Line(pts[i], pts[j], stroke_width=2, color=BLUE)
                          for i in range(6) for j in range(i + 1, 6)])
        self.play(Create(circ))
        self.play(Create(chords))
        self.wait(1.5)
        b3_l1 = MathTex(r"1,\; 2,\; 4,\; 8,\; 16,\; \mathbf{31}").scale(1.2).shift(band_shift(3) + UP * 1.0 + RIGHT * 2.0)
        b3_l2 = MathTex(r"2^{n-1} \text{ predicts } 32").scale(1.0).shift(band_shift(3) + UP * 0.1 + RIGHT * 2.0)
        b3_l3 = Tex("One counter-example disproves. Only structure proves.").scale(0.95).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.play(Create(strike(b3_l2)))
        self.wait(1.5)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"T_n = n + 3 \text{ for } 5, 8, 11 \;(\text{gives } 4, 5, 6)").scale(1.0).shift(band_shift(4) + UP * 1.3)
        b4_l2 = Tex(r"``It works for $n = 1, 2, 3$'' as a justification").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4_l3 = Tex(r"``$4(n-1)$ and $4n - 4$ are different rules''").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = Tex(r"Coefficient explained, constant not").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): words first
        self.next_band(5)
        b5_title = Tex("Say it in words first").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex(r"``Square the position and take away 1'' $\to n^2 - 1 \to$ 0, 3, 8, 15").scale(0.95).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex(r"Could a friend write the next term from your words?").scale(0.95).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex(r"``Goes up by 3'' -- from where? \quad ``Square it'' -- square what?").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = MathTex(r"T_5 \text{ is the fifth term, not } T \times 5").scale(0.95).shift(band_shift(5) + DOWN * 1.5)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): why it works
        self.next_band(6)
        b6_title = Tex("Why it works, not just that it works").scale(1.1).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        tables2 = table_row(4, band_shift(6) + UP * 1.0 + LEFT * 4.0)
        self.play(Create(tables2))
        self.wait(1.5)
        b6_l1 = Tex(r"Top: $n$. Bottom: $n$. Ends: 2. \quad $2n + 2$").scale(1.0).shift(band_shift(6) + UP * 1.0 + RIGHT * 3.0)
        b6_l2 = Tex("Every piece of the rule points at a piece of the picture").scale(0.95).shift(band_shift(6) + DOWN * 0.3)
        b6_l3 = Tex(r"``This works because...''").scale(1.1).shift(band_shift(6) + DOWN * 1.3)
        for m in (b6_l1, b6_l2):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): many rules, and the circle
        self.next_band(7)
        b7_title = Tex("One pattern, many rules").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"4n - 4 \quad 4(n-1) \quad 2n + 2(n-2) \quad n^2 - (n-2)^2").scale(0.95).shift(band_shift(7) + UP * 1.3)
        b7_l2 = Tex(r"Test two values, then expand: all are $4n - 4$").scale(0.95).shift(band_shift(7) + UP * 0.4)
        b7_l3 = MathTex(r"1, 2, 4, 8, 16, 31: \text{ fitting is not proving}").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex("Words a friend could use. Point each piece at the picture. Expand to compare.").scale(0.8).shift(band_shift(7) + DOWN * 1.5)
        for m in (b7_l1, b7_l2, b7_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
