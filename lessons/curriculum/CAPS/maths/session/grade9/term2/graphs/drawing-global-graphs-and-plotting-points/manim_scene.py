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


def cart_axes(origin, half_w=3.0, half_h=2.6):
    """Four-quadrant axes centred on origin, drawn from primitives."""
    g = VGroup()
    g.add(Line(origin + LEFT * half_w, origin + RIGHT * half_w, color=WHITE))
    g.add(Line(origin + DOWN * half_h, origin + UP * half_h, color=WHITE))
    return g


def grid(origin, half_w=3.0, half_h=2.6, s=0.5):
    """Faint grid lines every s units."""
    g = VGroup()
    n_w = int(half_w / s)
    n_h = int(half_h / s)
    for i in range(-n_w, n_w + 1):
        g.add(Line(origin + RIGHT * i * s + DOWN * half_h, origin + RIGHT * i * s + UP * half_h,
                   color=GREY, stroke_width=1, stroke_opacity=0.4))
    for j in range(-n_h, n_h + 1):
        g.add(Line(origin + UP * j * s + LEFT * half_w, origin + UP * j * s + RIGHT * half_w,
                   color=GREY, stroke_width=1, stroke_opacity=0.4))
    return g


def pt(origin, p, s=0.5, color=YELLOW):
    return Dot(origin + RIGHT * p[0] * s + UP * p[1] * s, radius=0.08, color=color)


def polyline(origin, pts, sx=1.0, sy=1.0, color=BLUE):
    g = VGroup()
    p = [origin + RIGHT * x * sx + UP * y * sy for x, y in pts]
    for a, b in zip(p, p[1:]):
        g.add(Line(a, b, color=color, stroke_width=4))
    return g


class PlottingPointsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the plane and quadrants
        title = Tex("The Cartesian plane: four quadrants").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        o0 = np.array([-3.6, -0.4, 0])
        self.play(Create(grid(o0, half_w=2.8, half_h=2.4)))
        self.play(Create(cart_axes(o0, half_w=2.8, half_h=2.4)))
        q1 = MathTex(r"\text{I}\;(+;\,+)").scale(0.7).move_to(o0 + RIGHT * 1.6 + UP * 1.6)
        q2 = MathTex(r"\text{II}\;(-;\,+)").scale(0.7).move_to(o0 + LEFT * 1.6 + UP * 1.6)
        q3 = MathTex(r"\text{III}\;(-;\,-)").scale(0.7).move_to(o0 + LEFT * 1.6 + DOWN * 1.6)
        q4 = MathTex(r"\text{IV}\;(+;\,-)").scale(0.7).move_to(o0 + RIGHT * 1.6 + DOWN * 1.6)
        for m in (q1, q2, q3, q4):
            self.play(Write(m))
            self.wait(1.2)
        l1 = Tex("Origin $(0;\\,0)$. Anticlockwise from top right.").scale(0.8).shift(RIGHT * 3.0 + UP * 1.2)
        l2 = Tex("$(4;\\,0)$ on the $x$-axis; $(0;\\,-5)$ on the $y$-axis: no quadrant.").scale(0.75).shift(RIGHT * 3.0 + UP * 0.3)
        l3 = Tex("Uniform scale: every block the same number of units.").scale(0.75).shift(RIGHT * 3.0 + DOWN * 0.6)
        for m in (l1, l2, l3):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(1.5)

        # --- Band 1 (subtopic_2): plotting pairs
        self.next_band(1)
        b1_title = Tex("Plotting: $x$ across first, then $y$ up or down").scale(1.05).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_title))
        self.wait(1.5)
        o1 = band_shift(1) + np.array([-3.6, -0.6, 0])
        self.play(Create(grid(o1, half_w=2.8, half_h=2.4)))
        self.play(Create(cart_axes(o1, half_w=2.8, half_h=2.4)))
        pts1 = [((3, 2), r"(3;\,2)"), ((-2, 4), r"(-2;\,4)"), ((-3, -1), r"(-3;\,-1)"), ((4, -2), r"(4;\,-2)")]
        for p, lab in pts1:
            d = pt(o1, p, s=0.5)
            t = MathTex(lab).scale(0.55).next_to(d, UR, buff=0.05)
            self.play(Create(d), Write(t))
            self.wait(1.2)
        b1_l1 = Tex("3 right, 2 up. \\quad 2 left, 4 up. \\quad 3 left, 1 down. \\quad 4 right, 2 down.").scale(0.7).shift(band_shift(1) + RIGHT * 2.8 + UP * 1.2)
        b1_l2 = Tex("Small sharp cross, labelled. Check the quadrant from the signs.").scale(0.72).shift(band_shift(1) + RIGHT * 2.8 + UP * 0.3)
        b1_l3 = Tex("$y = 2x + 1$: five points that line up like beads.").scale(0.75).shift(band_shift(1) + RIGHT * 2.8 + DOWN * 0.6)
        for m in (b1_l1, b1_l2, b1_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): story graph
        self.next_band(2)
        b2_title = Tex("Global graph from a story: the bath").scale(1.1).shift(band_shift(2) + UP * 2.5)
        self.play(Write(b2_title))
        self.wait(1.5)
        o2 = band_shift(2) + np.array([-5.5, -2.2, 0])
        self.play(Create(VGroup(Line(o2 + LEFT * 0.3, o2 + RIGHT * 5.4, color=WHITE), Line(o2 + DOWN * 0.3, o2 + UP * 3.4, color=WHITE))))
        bath = polyline(o2, [(0, 0), (10, 100), (30, 100), (35, 0)], sx=0.14, sy=0.028, color=BLUE)
        self.play(Create(bath), run_time=3)
        ticks = VGroup(*[MathTex(str(t)).scale(0.55).move_to(o2 + RIGHT * t * 0.14 + DOWN * 0.3) for t in (10, 30, 35)])
        self.play(Write(ticks))
        b2_l1 = Tex("time (min) across; volume (litres) up").scale(0.75).shift(band_shift(2) + RIGHT * 3.0 + UP * 1.3)
        b2_l2 = Tex("0--10 fill: straight up. 10--30 sit: flat. 30--35 drain: straight down.").scale(0.68).shift(band_shift(2) + RIGHT * 3.0 + UP * 0.4)
        b2_l3 = Tex("Drain steeper than fill: same volume in half the time.").scale(0.72).shift(band_shift(2) + RIGHT * 3.0 + DOWN * 0.5)
        b2_l4 = Tex("Ball: smooth hill. Tea: steep slide that flattens.").scale(0.72).shift(band_shift(2) + RIGHT * 3.0 + DOWN * 1.4)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): from a table, joining
        self.next_band(3)
        b3_title = Tex("From a table: plot everything, then decide the join").scale(1.0).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_title))
        self.wait(1.5)
        o3 = band_shift(3) + np.array([-3.6, -1.0, 0])
        self.play(Create(grid(o3, half_w=2.8, half_h=2.4)))
        self.play(Create(cart_axes(o3, half_w=2.8, half_h=2.4)))
        para = [(-2, 3), (-1, 0), (0, -1), (1, 0), (2, 3)]
        for p in para:
            self.play(Create(pt(o3, p, s=0.6)), run_time=0.4)
        curve = polyline(o3, [(-2, 3), (-1.5, 1.25), (-1, 0), (-0.5, -0.75), (0, -1), (0.5, -0.75), (1, 0), (1.5, 1.25), (2, 3)], sx=0.6, sy=0.6, color=ORANGE)
        self.play(Create(curve), run_time=2)
        b3_l1 = Tex("$y = x^2 - 1$: a smooth U, lowest at $(0;\\,-1)$. No ruler.").scale(0.75).shift(band_shift(3) + RIGHT * 3.0 + UP * 1.3)
        b3_l2 = Tex("Linear and continuous: ruler, extend a little.").scale(0.75).shift(band_shift(3) + RIGHT * 3.0 + UP * 0.4)
        b3_l3 = Tex("Discrete (passengers): dots only.").scale(0.75).shift(band_shift(3) + RIGHT * 3.0 + DOWN * 0.5)
        b3_l4 = Tex("A point off the pattern: check it before joining.").scale(0.75).shift(band_shift(3) + RIGHT * 3.0 + DOWN * 1.4)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(1.5)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("$(2;\\,5)$ plotted five across, two up").scale(0.95).shift(band_shift(4) + UP * 1.3)
        b4_l2 = Tex("Scale 0, 5, 10, 20, 50 at equal spacing").scale(0.95).shift(band_shift(4) + UP * 0.3)
        b4_l3 = Tex("A ruler on a parabola: a pointed V").scale(0.95).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = Tex("Unlabelled axes; discrete dots joined").scale(0.95).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): hall then lift
        self.next_band(5)
        b5_title = Tex("Across the hall, then up the lift").scale(1.15).shift(band_shift(5) + UP * 2.5)
        self.play(Write(b5_title))
        self.wait(2)
        o5 = band_shift(5) + np.array([-3.6, -0.6, 0])
        self.play(Create(grid(o5, half_w=2.8, half_h=2.4)))
        self.play(Create(cart_axes(o5, half_w=2.8, half_h=2.4)))
        hall = Line(o5, o5 + RIGHT * 3 * 0.5, color=GREEN, stroke_width=5)
        lift = Line(o5 + RIGHT * 3 * 0.5, o5 + RIGHT * 3 * 0.5 + UP * 2 * 0.5, color=GREEN, stroke_width=5)
        self.play(Create(hall))
        self.play(Create(lift))
        self.play(Create(pt(o5, (3, 2), s=0.5)))
        b5_l1 = Tex("$(3;\\,2)$: 3 along the hall, then 2 up the lift.").scale(0.78).shift(band_shift(5) + RIGHT * 3.0 + UP * 1.3)
        b5_l2 = Tex("$(-2;\\,4)$: 2 LEFT, 4 up. $(4;\\,-2)$: 4 right, 2 DOWN.").scale(0.75).shift(band_shift(5) + RIGHT * 3.0 + UP * 0.4)
        b5_l3 = Tex("Signs choose the corner before you move.").scale(0.78).shift(band_shift(5) + RIGHT * 3.0 + DOWN * 0.5)
        b5_l4 = Tex("Small sharp cross with a name.").scale(0.78).shift(band_shift(5) + RIGHT * 3.0 + DOWN * 1.4)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): sketch the story
        self.next_band(6)
        b6_title = Tex("Sketch the story, one chapter at a time").scale(1.1).shift(band_shift(6) + UP * 2.5)
        self.play(Write(b6_title))
        self.wait(2)
        o6 = band_shift(6) + np.array([-5.5, -2.2, 0])
        self.play(Create(VGroup(Line(o6 + LEFT * 0.3, o6 + RIGHT * 5.4, color=WHITE), Line(o6 + DOWN * 0.3, o6 + UP * 3.4, color=WHITE))))
        bath6 = polyline(o6, [(0, 0), (10, 100), (30, 100), (35, 0)], sx=0.14, sy=0.028, color=BLUE)
        self.play(Create(bath6), run_time=3)
        b6_l1 = Tex("Axes with units first.").scale(0.8).shift(band_shift(6) + RIGHT * 3.0 + UP * 1.3)
        b6_l2 = Tex("Fill: up. Sit: flat. Drain: down, steeper.").scale(0.8).shift(band_shift(6) + RIGHT * 3.0 + UP * 0.4)
        b6_l3 = Tex("Mark 10, 30, 35 so the chapters are the right length.").scale(0.72).shift(band_shift(6) + RIGHT * 3.0 + DOWN * 0.5)
        b6_l4 = Tex("Smooth hill for a ball; steep slide that flattens for tea.").scale(0.7).shift(band_shift(6) + RIGHT * 3.0 + DOWN * 1.4)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2)

        # --- Band 7 (subtopic_7): dots then decide
        self.next_band(7)
        b7_title = Tex("Dots, then a ruler or a smooth hand").scale(1.1).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7_title))
        self.wait(2)
        o7 = band_shift(7) + np.array([-3.6, -1.0, 0])
        self.play(Create(grid(o7, half_w=2.8, half_h=2.4)))
        self.play(Create(cart_axes(o7, half_w=2.8, half_h=2.4)))
        for p in [(-2, -3), (-1, -1), (0, 1), (1, 3), (2, 5)]:
            self.play(Create(pt(o7, p, s=0.45)), run_time=0.4)
        line7 = Line(o7 + RIGHT * (-2.4) * 0.45 + UP * (-3.8) * 0.45, o7 + RIGHT * 2.4 * 0.45 + UP * 5.8 * 0.45, color=BLUE, stroke_width=4)
        self.play(Create(line7))
        b7_l1 = Tex("Dots line up and the bottom flows: ruler.").scale(0.78).shift(band_shift(7) + RIGHT * 3.0 + UP * 1.3)
        b7_l2 = Tex("Dots bend: smooth hand, never a ruler.").scale(0.78).shift(band_shift(7) + RIGHT * 3.0 + UP * 0.4)
        b7_l3 = Tex("Whole pieces along the bottom: leave the dots.").scale(0.78).shift(band_shift(7) + RIGHT * 3.0 + DOWN * 0.5)
        b7_l4 = Tex("Hall then lift. Chapter by chapter. Dots, then decide.").scale(0.78).shift(band_shift(7) + RIGHT * 3.0 + DOWN * 1.4)
        for m in (b7_l1, b7_l2, b7_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
