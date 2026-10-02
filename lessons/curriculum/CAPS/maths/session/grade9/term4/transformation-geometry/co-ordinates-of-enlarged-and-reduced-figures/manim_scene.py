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
# the allowed primitive vocabulary. Co-ordinate grids, triangles and rays are
# drawn from plain line segments and dots. Bands cover all seven subtopics of
# the duo (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7),
# with dwell time proportional to subtopics.json
# (220/230/230/230/190/190/180 of 1470 s).

BAND = config.frame_height
U = 0.55  # one grid unit in scene units

ABC = [(1, 1), (3, 1), (1, 2)]
PQR = [(4, 6), (8, 2), (2, 2)]


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


def grid(origin, n=9, m=7):
    """First-quadrant grid 0..n by 0..m; origin is the scene point of (0; 0)."""
    g = VGroup()
    for k in range(1, n + 1):
        g.add(Line(origin + RIGHT * k * U, origin + RIGHT * k * U + UP * m * U,
                   color=GREY, stroke_width=1, stroke_opacity=0.4))
    for k in range(1, m + 1):
        g.add(Line(origin + UP * k * U, origin + UP * k * U + RIGHT * n * U,
                   color=GREY, stroke_width=1, stroke_opacity=0.4))
    g.add(Arrow(origin, origin + RIGHT * (n + 0.6) * U, buff=0, stroke_width=2, color=WHITE))
    g.add(Arrow(origin, origin + UP * (m + 0.6) * U, buff=0, stroke_width=2, color=WHITE))
    return g


def pt(origin, p):
    return origin + np.array([p[0] * U, p[1] * U, 0])


def triangle(origin, pts, color=YELLOW):
    g = VGroup()
    for i in range(3):
        g.add(Line(pt(origin, pts[i]), pt(origin, pts[(i + 1) % 3]), color=color, stroke_width=3))
        g.add(Dot(pt(origin, pts[i]), color=color, radius=0.05))
    return g


def scaled(pts, k):
    return [(k * x, k * y) for x, y in pts]


class EnlargementCoordinatesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def notes(self, k, lines, x=3.0, top=1.6, step=0.75, scale=0.66, wait=2.4):
        out = []
        for i, n in enumerate(lines):
            m = Tex(n).scale(scale).shift(band_shift(k) + RIGHT * x + UP * (top - step * i))
            self.play(Write(m))
            self.wait(wait)
            out.append(m)
        return out

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): (x; y) -> (kx; ky)
        h0 = Tex("Enlargement about the origin").scale(1.0).shift(band_shift(0) + UP * 3.2)
        self.play(Write(h0))
        o0 = band_shift(0) + LEFT * 6.3 + DOWN * 2.6
        self.play(Create(grid(o0)), run_time=1.5)
        self.play(Create(triangle(o0, ABC)))
        self.play(Create(triangle(o0, scaled(ABC, 2), color=BLUE)), run_time=1.5)
        self.play(Create(triangle(o0, scaled(ABC, 3), color=GREEN)), run_time=1.5)
        r0 = MathTex(r"(x;\,y) \to (kx;\,ky)").scale(0.9).shift(band_shift(0) + RIGHT * 3.0 + UP * 2.3)
        self.play(Write(r0))
        self.notes(0, ["$k = 2$: (2; 2), (6; 2), (2; 4)",
                       "$k = 3$: (3; 3), (9; 3), (3; 6)",
                       "($-2$; 4) times 3: ($-6$; 12)",
                       "(4; $-2$) to (10; $-5$): $k = 2.5$"], top=1.3)
        self.play(Create(SurroundingRectangle(r0, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): reductions
        self.next_band(1)
        h1 = Tex("Reduction: $0 < k < 1$").scale(1.0).shift(band_shift(1) + UP * 3.2)
        self.play(Write(h1))
        o1 = band_shift(1) + LEFT * 6.3 + DOWN * 2.6
        self.play(Create(grid(o1)), run_time=1.5)
        self.play(Create(triangle(o1, PQR)))
        self.play(Create(triangle(o1, [(2, 3), (4, 1), (1, 1)], color=BLUE)), run_time=1.5)
        self.notes(1, ["$k = \\frac{1}{2}$: (2; 3), (4; 1), (1; 1)",
                       "$\\frac{3}{4}$ of (8; 12) is (6; 9)",
                       "Inverse of $k$ is $\\frac{1}{k}$",
                       "Image (3; $-6$), $k = 3$: original (1; $-2$)",
                       "(3; 5) halved: (1.5; 2.5)"], top=2.0)

        # --- Band 2 (subtopic_3): rays from the origin
        self.next_band(2)
        h2 = Tex("Every point slides along its ray").scale(1.0).shift(band_shift(2) + UP * 3.2)
        self.play(Write(h2))
        o2 = band_shift(2) + LEFT * 6.3 + DOWN * 2.6
        self.play(Create(grid(o2)), run_time=1.5)
        for p in ABC:
            self.play(Create(DashedLine(o2, pt(o2, (3 * p[0], 3 * p[1])), color=GREY)), run_time=0.6)
        self.play(Create(triangle(o2, ABC)))
        self.play(Create(triangle(o2, scaled(ABC, 3), color=GREEN)), run_time=1.5)
        self.notes(2, ["(3; 4) is 5 from O; (6; 8) is 10",
                       "Rays meet at the centre",
                       "Test: every quotient equals $k$",
                       "(2; 3) to (4; 9): 2 and 3, not an enlargement",
                       "Image sides parallel to original sides"], top=2.0)

        # --- Band 3 (subtopic_4): area of the image
        self.next_band(3)
        h3 = Tex("Area of the image").scale(1.1).shift(band_shift(3) + UP * 3.1)
        self.play(Write(h3))
        self.notes(3, ["3 by 2 rectangle, area 6",
                       "Times 2: 6 by 4, area 24, which is $2^2 \\times 6$",
                       "Triangle area 1, times 3: area 9",
                       "PQR area 12, halved: area 3",
                       "Times 2 then times 1.5: times 3"], x=0, top=1.9)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        errs = ["$k = 2$: (3; 1) to (5; 3)",
                "Multiply only x: (1; 2) to (2; 2)",
                "$(kx; ky)$ with centre (1; 1)",
                "Area of the image is $k$ times",
                "(2; 3) to (4; 9) called an enlargement"]
        for i, e in enumerate(errs):
            m = Tex(e).scale(0.8).shift(band_shift(4) + UP * (1.5 - 0.9 * i))
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.6)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): multiply both co-ordinates
        self.next_band(5)
        b5 = Tex("Multiply both co-ordinates").scale(1.2).shift(band_shift(5) + UP * 2.8)
        self.play(Write(b5))
        s = self.notes(5, ["Both numbers, same multiplier",
                           "(1; 1), (3; 1), (1; 2) times 2: (2; 2), (6; 2), (2; 4)",
                           "Signs stay: ($-2$; 4) times 3 is ($-6$; 12)",
                           "Find $k$: new number $\\div$ old number"], x=0, top=1.4, scale=0.8)
        self.play(Create(SurroundingRectangle(s[0], color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): halving brings it home
        self.next_band(6)
        b6 = Tex("Halving brings it home").scale(1.2).shift(band_shift(6) + UP * 2.8)
        self.play(Write(b6))
        s = self.notes(6, ["(4; 6) halved is (2; 3)",
                           "A third: divide by 3",
                           "Undo times 3: (3; $-6$) back to (1; $-2$)",
                           "Half the sides, a quarter of the area"], x=0, top=1.4, scale=0.85)
        self.play(Create(SurroundingRectangle(s[0], color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): rays from the origin
        self.next_band(7)
        b7 = Tex("Rays from the origin").scale(1.2).shift(band_shift(7) + UP * 2.8)
        self.play(Write(b7))
        self.notes(7, ["(3; 4) is 5 away; (6; 8) is 10 away",
                       "Join corners to images: lines meet at O",
                       "(2; 3) to (4; 9): two multipliers, not an enlargement"],
                   x=0, top=1.5, scale=0.8, wait=2.2)
        t5 = Tex("Multiply both; halve to shrink; rays from the origin.").scale(0.85).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(t5))
        self.play(Create(SurroundingRectangle(t5, color=YELLOW)))
        self.wait(4)
