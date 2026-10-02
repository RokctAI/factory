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
# the allowed primitive vocabulary. Co-ordinate grids and figures are drawn
# from plain line segments and dots. Bands cover all seven subtopics of the
# duo (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7),
# with dwell time proportional to subtopics.json
# (220/230/230/230/190/190/180 of 1470 s).

BAND = config.frame_height
U = 0.42  # one grid unit in scene units

# Fingerprints of (3; 5): (image, name)
FINGERPRINTS = [
    ("(3; $-5$)", "no swap, y sign: reflection in the x-axis"),
    ("($-3$; 5)", "no swap, x sign: reflection in the y-axis"),
    ("(5; 3)", "swap only: reflection in y = x"),
    ("($-3$; $-5$)", "both signs: rotation 180$^\\circ$ about O"),
    ("($-5$; 3)", "swap, new first negative: 90$^\\circ$ anticlockwise"),
    ("(5; $-3$)", "swap, new second negative: 90$^\\circ$ clockwise"),
    ("(7; 2)", "shift: translation 4 right, 3 down"),
]


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


def grid(origin, n=5):
    g = VGroup()
    for k in range(-n, n + 1):
        if k == 0:
            continue
        g.add(Line(origin + np.array([k * U, -n * U, 0]), origin + np.array([k * U, n * U, 0]),
                   color=GREY, stroke_width=1, stroke_opacity=0.4))
        g.add(Line(origin + np.array([-n * U, k * U, 0]), origin + np.array([n * U, k * U, 0]),
                   color=GREY, stroke_width=1, stroke_opacity=0.4))
    g.add(Arrow(origin + LEFT * n * U, origin + RIGHT * (n + 0.6) * U, buff=0, stroke_width=2, color=WHITE))
    g.add(Arrow(origin + DOWN * n * U, origin + UP * (n + 0.6) * U, buff=0, stroke_width=2, color=WHITE))
    return g


def pt(origin, p):
    return origin + np.array([p[0] * U, p[1] * U, 0])


def figure(origin, pts, color=YELLOW):
    g = VGroup()
    for i in range(len(pts)):
        g.add(Line(pt(origin, pts[i]), pt(origin, pts[(i + 1) % len(pts)]), color=color, stroke_width=3))
        g.add(Dot(pt(origin, pts[i]), color=color, radius=0.05))
    return g


class IdentifyTransformationsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): fingerprints of (3; 5)
        title = Tex("Fingerprints of (3; 5)").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        for i, (img, name) in enumerate(FINGERPRINTS):
            a = Tex(img).scale(0.7).move_to(LEFT * 4.6 + UP * (2.0 - 0.62 * i))
            b = Tex(name).scale(0.62).move_to(RIGHT * 1.4 + UP * (2.0 - 0.62 * i))
            self.play(Write(a), Write(b))
            self.wait(1.8)
        q = Tex("Swapped? Which signs? Otherwise: image minus original").scale(0.75).shift(DOWN * 2.8)
        self.play(Write(q))
        self.play(Create(SurroundingRectangle(q, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): ambiguous points
        self.next_band(1)
        b1_title = Tex("When one point is not enough").scale(1.15).shift(band_shift(1) + UP * 3.1)
        self.play(Write(b1_title))
        self.wait(1.5)
        o = band_shift(1) + LEFT * 4.3 + DOWN * 0.2
        self.play(Create(grid(o)), run_time=1.5)
        A, B = (2, -2), (4, 1)
        A2, B2 = (-2, 2), (1, 4)
        self.play(Create(Line(pt(o, A), pt(o, B), color=YELLOW)), Create(Dot(pt(o, A), color=YELLOW)), Create(Dot(pt(o, B), color=YELLOW)))
        self.play(Create(Line(pt(o, A2), pt(o, B2), color=GREEN)), Create(Dot(pt(o, A2), color=GREEN)), Create(Dot(pt(o, B2), color=GREEN)))
        self.play(Create(DashedLine(pt(o, (-5, -5)), pt(o, (5, 5)), color=GREEN)))
        n = [
            "A(2; $-2$) to A$'$($-2$; 2): swap? half turn? slide?",
            "Test B(4; 1) to B$'$(1; 4)",
            "y = x: (1; 4) yes. 180$^\\circ$: ($-4$; $-1$) no.",
            "Answer: reflection in y = x",
            "Orientation reversed: a reflection",
        ]
        for i, s in enumerate(n):
            m = Tex(s).scale(0.62).shift(band_shift(1) + RIGHT * 2.6 + UP * (1.8 - 0.75 * i))
            self.play(Write(m))
            self.wait(2.2)
        self.play(Create(SurroundingRectangle(m, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): full description
        self.next_band(2)
        b2_title = Tex("Describe it fully").scale(1.15).shift(band_shift(2) + UP * 3.1)
        self.play(Write(b2_title))
        self.wait(1.5)
        o2 = band_shift(2) + LEFT * 4.3 + DOWN * 0.2
        self.play(Create(grid(o2)), run_time=1.5)
        PQR = [(1, 1), (3, 1), (3, 4)]
        PQR2 = [(-1, 1), (-1, 3), (-4, 3)]
        self.play(Create(figure(o2, PQR)))
        self.play(Create(figure(o2, PQR2, color=PURPLE)))
        d = [
            "P(1; 1), Q(3; 1), R(3; 4)",
            "P$'$($-1$; 1), Q$'$($-1$; 3), R$'$($-4$; 3)",
            "Rotation 90$^\\circ$ anticlockwise about O",
            "$(x; y) \\to (-y; x)$, true for every vertex",
            "Half-turn centre: midpoint of P(5; 3), P$'$($-1$; $-1$) is (2; 1)",
        ]
        for i, s in enumerate(d):
            m = Tex(s).scale(0.6).shift(band_shift(2) + RIGHT * 2.7 + UP * (1.8 - 0.75 * i))
            self.play(Write(m))
            self.wait(2.2)
        rot = Tex("Rotation: centre, angle, direction").scale(0.75).shift(band_shift(2) + RIGHT * 2.7 + DOWN * 2.4)
        self.play(Write(rot))
        self.play(Create(SurroundingRectangle(rot, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): combined transformations
        self.next_band(3)
        b3_title = Tex("Two moves in a row").scale(1.15).shift(band_shift(3) + UP * 3.0)
        self.play(Write(b3_title))
        self.wait(1.5)
        c = [
            r"(2;\,5) \to (2;\,-5) \to (-2;\,-5): \text{ two mirrors} = 180^\circ",
            r"(2;\,5) \to (5;\,2) \to (5;\,-2): \text{ a quarter turn clockwise}",
            r"(3;\,1): \text{ mirror then slide } \to (-1;\,1)",
            r"(3;\,1): \text{ slide then mirror } \to (-5;\,1)",
        ]
        for i, s in enumerate(c):
            m = MathTex(s).scale(0.75).shift(band_shift(3) + UP * (1.7 - 0.95 * i))
            self.play(Write(m))
            self.wait(2.6)
        order = Tex("Follow the order you are given").scale(0.85).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(order))
        self.play(Create(SurroundingRectangle(order, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        e1 = Tex("Deciding from one ambiguous point").scale(0.8).shift(band_shift(4) + UP * 1.5)
        e2 = Tex("Rotation 90$^\\circ$, with no centre or direction").scale(0.8).shift(band_shift(4) + UP * 0.6)
        e3 = Tex("Calling a quarter turn a reflection in y = x").scale(0.8).shift(band_shift(4) + DOWN * 0.3)
        e4 = Tex("Translation as original minus image").scale(0.8).shift(band_shift(4) + DOWN * 1.2)
        e5 = Tex("Two moves done in the wrong order").scale(0.8).shift(band_shift(4) + DOWN * 2.1)
        for m in (e1, e2, e3, e4, e5):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.6)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): spot the sign change and the swap
        self.next_band(5)
        b5_title = Tex("Spot the sign change and the swap").scale(1.1).shift(band_shift(5) + UP * 2.8)
        self.play(Write(b5_title))
        self.wait(2)
        s1 = Tex("One sign flips, no swap: a mirror in an axis").scale(0.8).shift(band_shift(5) + UP * 1.5)
        s2 = Tex("Swap, no sign: the slanted mirror y = x").scale(0.8).shift(band_shift(5) + UP * 0.6)
        s3 = Tex("Both signs, no swap: half a turn").scale(0.8).shift(band_shift(5) + DOWN * 0.3)
        s4 = Tex("Swap and one sign: a quarter turn").scale(0.8).shift(band_shift(5) + DOWN * 1.2)
        s5 = Tex("None of these: a slide, finish take away start").scale(0.8).shift(band_shift(5) + DOWN * 2.1)
        for m in (s1, s2, s3, s4, s5):
            self.play(Write(m))
            self.wait(2.0)
        self.play(Create(SurroundingRectangle(s5, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): check a second point
        self.next_band(6)
        b6_title = Tex("Check a second point").scale(1.2).shift(band_shift(6) + UP * 2.8)
        self.play(Write(b6_title))
        self.wait(2)
        p1 = Tex("Tricky: zeros, or numbers the same size").scale(0.85).shift(band_shift(6) + UP * 1.4)
        p2 = Tex("(0; 4) to (0; $-4$): mirror or half turn?").scale(0.85).shift(band_shift(6) + UP * 0.5)
        p3 = Tex("Test another corner until one move fits").scale(0.85).shift(band_shift(6) + DOWN * 0.4)
        p4 = Tex("Name every detail: line, slide, or pin, angle, direction").scale(0.75).shift(band_shift(6) + DOWN * 1.3)
        for m in (p1, p2, p3, p4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(p3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): two moves in a row
        self.next_band(7)
        b7_title = Tex("Two moves in a row").scale(1.2).shift(band_shift(7) + UP * 2.8)
        self.play(Write(b7_title))
        self.wait(2)
        t1 = Tex("Two mirrors make a turn").scale(0.85).shift(band_shift(7) + UP * 1.4)
        t2 = Tex("x-axis then y-axis: half a turn").scale(0.85).shift(band_shift(7) + UP * 0.5)
        t3 = Tex("Mirror and slide: order changes the answer").scale(0.85).shift(band_shift(7) + DOWN * 0.4)
        for m in (t1, t2, t3):
            self.play(Write(m))
            self.wait(2.3)
        t4 = Tex("Swap and signs. Second point. Moves in order.").scale(0.85).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(t4))
        self.play(Create(SurroundingRectangle(t4, color=YELLOW)))
        self.wait(4)
