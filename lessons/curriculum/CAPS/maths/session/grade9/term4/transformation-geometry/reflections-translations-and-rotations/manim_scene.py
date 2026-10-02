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
# the allowed primitive vocabulary. Co-ordinate grids and triangles are drawn
# from plain line segments and dots. Bands cover all seven subtopics of the
# duo (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7),
# with dwell time proportional to subtopics.json
# (220/230/230/230/190/190/180 of 1470 s).

BAND = config.frame_height
U = 0.42  # one grid unit in scene units

ABC = [(1, 2), (4, 2), (1, 4)]


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


def grid(origin, n=5):
    """Axes from -n to n with faint unit lines; origin is the scene point of (0; 0)."""
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
    g.add(Tex("x").scale(0.45).move_to(origin + RIGHT * (n + 0.9) * U))
    g.add(Tex("y").scale(0.45).move_to(origin + UP * (n + 0.9) * U))
    return g


def pt(origin, p):
    return origin + np.array([p[0] * U, p[1] * U, 0])


def triangle(origin, pts, color=YELLOW):
    g = VGroup()
    for i in range(3):
        g.add(Line(pt(origin, pts[i]), pt(origin, pts[(i + 1) % 3]), color=color, stroke_width=3))
        g.add(Dot(pt(origin, pts[i]), color=color, radius=0.05))
    return g


def image(rule):
    return [rule(x, y) for x, y in ABC]


class TransformationsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def show_case(self, k, heading, rule, rule_tex, notes, color):
        """One band: grid on the left, original and image, rule and notes on the right."""
        h = Tex(heading).scale(1.1).shift(band_shift(k) + UP * 3.1)
        self.play(Write(h))
        o = band_shift(k) + LEFT * 4.2 + DOWN * 0.2
        self.play(Create(grid(o)), run_time=1.5)
        self.play(Create(triangle(o, ABC)))
        self.wait(1)
        self.play(Create(triangle(o, image(rule), color=color)), run_time=1.5)
        r = MathTex(rule_tex).scale(0.85).shift(band_shift(k) + RIGHT * 2.6 + UP * 1.8)
        self.play(Write(r))
        self.wait(2)
        for i, n in enumerate(notes):
            m = Tex(n).scale(0.66).shift(band_shift(k) + RIGHT * 2.6 + UP * (0.9 - 0.75 * i))
            self.play(Write(m))
            self.wait(2.2)
        self.play(Create(SurroundingRectangle(r, color=color)))
        self.wait(2)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): reflections in the axes
        self.show_case(0, "Reflection in the x-axis", lambda x, y: (x, -y),
                       r"(x;\,y) \to (x;\,-y)",
                       ["A(1; 2), B(4; 2), C(1; 4)",
                        "A'(1; $-2$), B'(4; $-2$), C'(1; $-4$)",
                        "y-axis: $(x; y) \\to (-x; y)$",
                        "Congruent; orientation reversed",
                        "Points on the mirror stay put"], BLUE)

        # --- Band 1 (subtopic_2): reflection in y = x
        self.next_band(1)
        o1 = band_shift(1) + LEFT * 4.2 + DOWN * 0.2
        self.show_case(1, "Reflection in the line y = x", lambda x, y: (y, x),
                       r"(x;\,y) \to (y;\,x)",
                       ["A'(2; 1), B'(2; 4), C'(4; 1)",
                        "Midpoint of AA$'$: (1.5; 1.5), on the mirror",
                        "Horizontal sides become vertical",
                        "Swap only: no sign changes"], GREEN)
        mirror = DashedLine(pt(o1, (-5, -5)), pt(o1, (5, 5)), color=GREEN)
        self.play(Create(mirror))
        self.wait(2)

        # --- Band 2 (subtopic_3): translation
        self.next_band(2)
        self.show_case(2, "Translation: 3 left, 2 down", lambda x, y: (x - 3, y - 2),
                       r"(x;\,y) \to (x - 3;\,y - 2)",
                       ["A'($-2$; 0), B'(1; 0), C'($-2$; 2)",
                        "Right and up add; left and down subtract",
                        "Same size, shape and orientation",
                        "Then 5 right, 1 up: net 2 right, 1 down"], ORANGE)

        # --- Band 3 (subtopic_4): rotations about the origin and another centre
        self.next_band(3)
        self.show_case(3, "Rotation 90$^\\circ$ anticlockwise about O", lambda x, y: (-y, x),
                       r"(x;\,y) \to (-y;\,x)",
                       ["Clockwise: $(x; y) \\to (y; -x)$",
                        "180$^\\circ$: $(x; y) \\to (-x; -y)$",
                        "Check the quadrant: (1; 2) to ($-2$; 1)",
                        "About (2; 1): P(5; 3) to ($-1$; $-1$) by 180$^\\circ$"], PURPLE)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        e1 = Tex("x-axis reflection: (1; 2) to ($-1$; 2)").scale(0.8).shift(band_shift(4) + UP * 1.5)
        e2 = Tex("y = x reflection: (1; 2) to ($-2$; 1)").scale(0.8).shift(band_shift(4) + UP * 0.6)
        e3 = Tex("3 left: $x + 3$").scale(0.8).shift(band_shift(4) + DOWN * 0.3)
        e4 = Tex("90$^\\circ$ anticlockwise: (1; 2) to (2; $-1$)").scale(0.8).shift(band_shift(4) + DOWN * 1.2)
        e5 = Tex("Rotating about O when the centre is (2; 1)").scale(0.8).shift(band_shift(4) + DOWN * 2.1)
        for m in (e1, e2, e3, e4, e5):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.6)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): mirrors on the grid
        self.next_band(5)
        b5_title = Tex("Mirrors on the grid").scale(1.2).shift(band_shift(5) + UP * 2.8)
        self.play(Write(b5_title))
        self.wait(2)
        m1 = Tex("The mirror axis keeps its own number").scale(0.85).shift(band_shift(5) + UP * 1.4)
        m2 = Tex("x-axis: (1; 2) to (1; $-2$) \\qquad y-axis: (1; 2) to ($-1$; 2)").scale(0.8).shift(band_shift(5) + UP * 0.5)
        m3 = Tex("Slanted mirror y = x: just swap, (1; 2) to (2; 1)").scale(0.8).shift(band_shift(5) + DOWN * 0.4)
        m4 = Tex("Same size and shape, but flipped").scale(0.85).shift(band_shift(5) + DOWN * 1.3)
        for m in (m1, m2, m3, m4):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(m1, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): sliding
        self.next_band(6)
        b6_title = Tex("Sliding without turning").scale(1.2).shift(band_shift(6) + UP * 2.8)
        self.play(Write(b6_title))
        self.wait(2)
        s1 = Tex("Right and up: add. Left and down: subtract.").scale(0.85).shift(band_shift(6) + UP * 1.4)
        s2 = Tex("3 left, 2 down: (1; 2) to ($-2$; 0)").scale(0.85).shift(band_shift(6) + UP * 0.5)
        s3 = Tex("Two slides add up; undo with the opposite slide").scale(0.85).shift(band_shift(6) + DOWN * 0.4)
        s4 = Tex("Game character: (120; 80), (135; 90), (150; 100)").scale(0.8).shift(band_shift(6) + DOWN * 1.3)
        for m in (s1, s2, s3, s4):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(s1, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): turning around a pin
        self.next_band(7)
        b7_title = Tex("Turning around a pin").scale(1.2).shift(band_shift(7) + UP * 2.8)
        self.play(Write(b7_title))
        self.wait(2)
        t1 = Tex("Half turn: both signs change").scale(0.85).shift(band_shift(7) + UP * 1.5)
        t2 = Tex("Quarter turn anticlockwise: swap, first negative").scale(0.85).shift(band_shift(7) + UP * 0.6)
        t3 = Tex("Quarter turn clockwise: swap, second negative").scale(0.85).shift(band_shift(7) + DOWN * 0.3)
        t4 = Tex("Pin not at O: count from the pin").scale(0.85).shift(band_shift(7) + DOWN * 1.2)
        for m in (t1, t2, t3, t4):
            self.play(Write(m))
            self.wait(2.2)
        t5 = Tex("Mirror, slide, turn, and check the quadrant.").scale(0.9).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(t5))
        self.play(Create(SurroundingRectangle(t5, color=YELLOW)))
        self.wait(4)
