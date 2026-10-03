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
# the allowed primitive vocabulary. Nets are drawn from squares, rectangles,
# circles and line-segment triangles. Bands cover all seven subtopics of the
# duo (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7),
# with dwell time proportional to subtopics.json
# (220/230/230/230/190/190/180 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


def squares_net(origin, cells, s=0.7, labels=None, color=WHITE):
    """Unit squares at (col, row) grid cells, row 0 at the top."""
    g = VGroup()
    for k, (c, r) in enumerate(cells):
        sq = Square(side_length=s, color=color).move_to(origin + RIGHT * s * c + DOWN * s * r)
        g.add(sq)
        if labels:
            g.add(Tex(labels[k]).scale(0.55).move_to(sq.get_center()))
    return g


def tri(a, b, c, color=WHITE):
    return VGroup(Line(a, b, color=color), Line(b, c, color=color), Line(c, a, color=color))


class NetsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): cube nets
        title = Tex("Nets of a cube").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        cross = squares_net(np.array([-6.2, 1.2, 0]), [(0, 1), (1, 1), (2, 1), (3, 1), (1, 0), (1, 2)],
                            labels=["1", "2", "6", "5", "3", "4"])
        self.play(Create(cross), run_time=2)
        cross_lab = Tex("Cross net, die numbered: opposites add to 7").scale(0.55).move_to(np.array([-4.9, -1.2, 0]))
        self.play(Write(cross_lab))
        self.wait(1.5)
        strip = squares_net(np.array([0.4, 1.6, 0]), [(k, 0) for k in range(6)], s=0.55, color=GREY)
        block = squares_net(np.array([0.4, 0.2, 0]), [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)], s=0.55, color=GREY)
        self.play(Create(strip), Create(block), run_time=2)
        self.play(Create(strike(strip)), Create(strike(block)))
        n1 = Tex("Fake: a row of 5 or more").scale(0.6).move_to(np.array([5.3, 1.6, 0]))
        n2 = Tex("Fake: a 2 by 2 block").scale(0.6).move_to(np.array([5.3, 0.0, 0]))
        self.play(Write(n1), Write(n2))
        rule = Tex("Line of 3 squares: first and third are opposite").scale(0.75).shift(DOWN * 2.3 + RIGHT * 1.6)
        self.play(Write(rule))
        self.play(Create(SurroundingRectangle(rule, color=YELLOW)))
        self.wait(3)

        # --- Band 1 (subtopic_2): prism nets
        self.next_band(1)
        b1_title = Tex("Nets of prisms: meeting edges are equal").scale(1.05).shift(band_shift(1) + UP * 3.1)
        self.play(Write(b1_title))
        self.wait(1.5)
        o = band_shift(1) + LEFT * 6.0 + DOWN * 1.0
        u = 0.32
        r1 = Rectangle(width=3 * u, height=10 * u, color=WHITE).move_to(o + RIGHT * 1.5 * u + UP * 5 * u)
        r2 = Rectangle(width=4 * u, height=10 * u, color=WHITE).move_to(o + RIGHT * 5 * u + UP * 5 * u)
        r3 = Rectangle(width=5 * u, height=10 * u, color=WHITE).move_to(o + RIGHT * 9.5 * u + UP * 5 * u)
        top = o + UP * 10 * u
        t_top = tri(top, top + RIGHT * 3 * u, top + UP * 4 * u, color=BLUE)
        t_bot = tri(o, o + RIGHT * 3 * u, o + DOWN * 4 * u, color=BLUE)
        self.play(Create(r1), Create(r2), Create(r3), run_time=2)
        self.play(Create(t_top), Create(t_bot))
        labs = VGroup(
            Tex("3").scale(0.5).move_to(r1.get_center()),
            Tex("4").scale(0.5).move_to(r2.get_center()),
            Tex("5").scale(0.5).move_to(r3.get_center()),
        )
        self.play(Write(labs))
        p1 = Tex("Ends: 3, 4, 5 triangles; length 10").scale(0.7).shift(band_shift(1) + RIGHT * 2.4 + UP * 1.8)
        p2 = MathTex(r"\text{Strip: } 3 + 4 + 5 = 12 \text{ cm, the perimeter}").scale(0.75).shift(band_shift(1) + RIGHT * 2.4 + UP * 1.0)
        p3 = Tex("Triangle's 3 cm side on the 3 cm edge, never 4 on 3").scale(0.65).shift(band_shift(1) + RIGHT * 2.4 + UP * 0.2)
        p4 = Tex("Box 4 by 3 by 2: pairs 4 by 3, 4 by 2, 3 by 2").scale(0.7).shift(band_shift(1) + RIGHT * 2.4 + DOWN * 0.6)
        p5 = Tex("Strip: perimeter of end by length of prism").scale(0.7).shift(band_shift(1) + RIGHT * 2.4 + DOWN * 1.4)
        for m in (p1, p2, p3, p4, p5):
            self.play(Write(m))
            self.wait(2.0)
        self.play(Create(SurroundingRectangle(p5, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): pyramid and cylinder nets
        self.next_band(2)
        b2_title = Tex("Nets of pyramids and cylinders").scale(1.1).shift(band_shift(2) + UP * 3.1)
        self.play(Write(b2_title))
        self.wait(1.5)
        c = band_shift(2) + LEFT * 4.6 + UP * 0.2
        s = 1.2
        base = Square(side_length=s, color=WHITE).move_to(c)
        h = 1.0
        tris = VGroup(
            tri(c + np.array([-s / 2, s / 2, 0]), c + np.array([s / 2, s / 2, 0]), c + UP * (s / 2 + h), BLUE),
            tri(c + np.array([-s / 2, -s / 2, 0]), c + np.array([s / 2, -s / 2, 0]), c + DOWN * (s / 2 + h), BLUE),
            tri(c + np.array([-s / 2, s / 2, 0]), c + np.array([-s / 2, -s / 2, 0]), c + LEFT * (s / 2 + h), BLUE),
            tri(c + np.array([s / 2, s / 2, 0]), c + np.array([s / 2, -s / 2, 0]), c + RIGHT * (s / 2 + h), BLUE),
        )
        self.play(Create(base), Create(tris), run_time=2)
        q1 = MathTex(r"\text{Base } 6,\ \text{slant } 5: \sqrt{5^2 - 3^2} = 4 \text{ cm high}").scale(0.7).shift(band_shift(2) + LEFT * 3.6 + DOWN * 2.4)
        self.play(Write(q1))
        self.wait(2)
        rect = Rectangle(width=4.4, height=2.0, color=WHITE).move_to(band_shift(2) + RIGHT * 3.0 + UP * 0.2)
        top_c = Circle(radius=0.7, color=GREEN).next_to(rect, UP, buff=0)
        bot_c = Circle(radius=0.7, color=GREEN).next_to(rect, DOWN, buff=0)
        self.play(Create(rect), Create(top_c), Create(bot_c), run_time=2)
        q2 = MathTex(r"2\pi \times 3.5 \approx 21.99 \approx 22 \text{ cm long},\ 10 \text{ cm wide}").scale(0.65).shift(band_shift(2) + RIGHT * 3.0 + DOWN * 2.4)
        self.play(Write(q2))
        self.play(Create(SurroundingRectangle(q2, color=YELLOW)))
        self.wait(3)

        # --- Band 3 (subtopic_4): building models
        self.next_band(3)
        b3_title = Tex("Building the model").scale(1.2).shift(band_shift(3) + UP * 2.8)
        self.play(Write(b3_title))
        self.wait(1.5)
        m1 = Tex("Draw with ruler and compass; score every fold").scale(0.8).shift(band_shift(3) + UP * 1.6)
        m2 = Tex("Folds: F $-$ 1. Tabs: E $-$ (F $-$ 1)").scale(0.85).shift(band_shift(3) + UP * 0.7)
        m3 = MathTex(r"\text{Cube: } 12 - 5 = 7 \qquad \text{Prism: } 9 - 4 = 5").scale(0.85).shift(band_shift(3) + DOWN * 0.2)
        m4 = MathTex(r"\text{Square pyramid: } 8 - 4 = 4 \qquad \text{Tetrahedron: } 6 - 3 = 3").scale(0.85).shift(band_shift(3) + DOWN * 1.1)
        m5 = Tex("One tab per join, on one edge only").scale(0.8).shift(band_shift(3) + DOWN * 2.0)
        for m in (m1, m2, m3, m4, m5):
            self.play(Write(m))
            self.wait(2.1)
        self.play(Create(SurroundingRectangle(m2, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        e1 = Tex("Cube net with a row of 5 or a 2 by 2 block").scale(0.8).shift(band_shift(4) + UP * 1.5)
        e2 = Tex("Cylinder rectangle 7 cm long (the diameter)").scale(0.8).shift(band_shift(4) + UP * 0.6)
        e3 = Tex("Triangle's 5 cm side on the 3 by 10 rectangle").scale(0.8).shift(band_shift(4) + DOWN * 0.3)
        e4 = Tex("Pyramid slant height 3 on a 6 cm base").scale(0.8).shift(band_shift(4) + DOWN * 1.2)
        e5 = Tex("Two faces folding onto the same place").scale(0.8).shift(band_shift(4) + DOWN * 2.1)
        for m in (e1, e2, e3, e4, e5):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.6)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): unfold a box
        self.next_band(5)
        b5_title = Tex("Unfold a box").scale(1.2).shift(band_shift(5) + UP * 2.8)
        self.play(Write(b5_title))
        self.wait(2)
        cross2 = squares_net(band_shift(5) + LEFT * 6.0 + UP * 1.0, [(0, 1), (1, 1), (2, 1), (3, 1), (1, 0), (1, 2)], s=0.75)
        self.play(Create(cross2), run_time=2)
        u1 = Tex("Every face once, one piece, no overlaps").scale(0.8).shift(band_shift(5) + RIGHT * 2.0 + UP * 1.3)
        u2 = Tex("Fakes: a row of 5, a 2 by 2 block").scale(0.8).shift(band_shift(5) + RIGHT * 2.0 + UP * 0.4)
        u3 = Tex("Line of 3: first and third are opposite").scale(0.8).shift(band_shift(5) + RIGHT * 2.0 + DOWN * 0.5)
        u4 = Tex("Die opposites: 1 and 6, 2 and 5, 3 and 4").scale(0.8).shift(band_shift(5) + RIGHT * 2.0 + DOWN * 1.4)
        for m in (u1, u2, u3, u4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(u2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): tents and pyramids
        self.next_band(6)
        b6_title = Tex("Tents and pyramids").scale(1.2).shift(band_shift(6) + UP * 2.8)
        self.play(Write(b6_title))
        self.wait(2)
        w1 = Tex("Tent: two triangles and a strip of three rectangles").scale(0.8).shift(band_shift(6) + UP * 1.5)
        w2 = Tex("Strip 3, 4, 5 wide: 12 cm, all the way round the triangle").scale(0.8).shift(band_shift(6) + UP * 0.6)
        w3 = Tex("Every edge meets an edge of the same length").scale(0.8).shift(band_shift(6) + DOWN * 0.3)
        w4 = Tex("Pyramid: 6 cm square, 5 cm triangles, top 4 cm up").scale(0.8).shift(band_shift(6) + DOWN * 1.2)
        w5 = Tex("Big triangle, join the middles: 4 small triangles").scale(0.8).shift(band_shift(6) + DOWN * 2.1)
        for m in (w1, w2, w3, w4, w5):
            self.play(Write(m))
            self.wait(2.0)
        self.play(Create(SurroundingRectangle(w3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): unroll the label
        self.next_band(7)
        b7_title = Tex("Unroll the label").scale(1.2).shift(band_shift(7) + UP * 2.8)
        self.play(Write(b7_title))
        self.wait(2)
        lab_rect = Rectangle(width=4.4, height=2.0, color=WHITE).move_to(band_shift(7) + LEFT * 3.4 + UP * 0.3)
        short = Rectangle(width=1.4, height=2.0, color=RED).move_to(band_shift(7) + LEFT * 3.4 + DOWN * 2.1)
        self.play(Create(lab_rect))
        self.play(Create(short))
        lr = Tex("About 22 cm: right").scale(0.6).next_to(lab_rect, RIGHT, buff=0.2)
        sr = Tex("7 cm: wraps less than a third").scale(0.6).next_to(short, RIGHT, buff=0.2)
        self.play(Write(lr), Write(sr))
        x1 = Tex("Tall as the tin, long as the way round").scale(0.8).shift(band_shift(7) + RIGHT * 3.4 + UP * 1.5)
        x2 = Tex("Tabs: edges take away folds").scale(0.8).shift(band_shift(7) + RIGHT * 3.4 + UP * 0.7)
        for m in (x1, x2):
            self.play(Write(m))
            self.wait(2.2)
        x3 = Tex("Unfold, match the edges, unroll to the circumference.").scale(0.8).shift(band_shift(7) + DOWN * 3.2)
        self.play(Write(x3))
        self.play(Create(SurroundingRectangle(x3, color=YELLOW)))
        self.wait(4)
