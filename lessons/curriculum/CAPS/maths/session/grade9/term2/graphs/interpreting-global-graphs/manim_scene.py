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


def polyline(origin, pts, sx=1.0, sy=1.0, color=BLUE):
    """A graph drawn as straight segments between scaled points."""
    g = VGroup()
    p = [origin + RIGHT * x * sx + UP * y * sy for x, y in pts]
    for a, b in zip(p, p[1:]):
        g.add(Line(a, b, color=color, stroke_width=4))
    return g


def dots(origin, pts, sx=1.0, sy=1.0, color=YELLOW):
    return VGroup(*[Dot(origin + RIGHT * x * sx + UP * y * sy, radius=0.07, color=color) for x, y in pts])


# Bloemfontein day: (hour, degrees) sampled every 2 hours, smooth-ish curve.
TEMP = [(0, 15), (2, 12), (4, 9), (5, 8), (6, 9), (8, 14), (10, 20), (12, 25),
        (14, 28), (16, 26), (18, 22), (20, 19), (22, 17), (24, 16)]
WALK = [(0, 0), (10, 600), (15, 600), (25, 1200)]
BALL = [(0, 0), (0.5, 8.75), (1, 15), (1.5, 18.75), (2, 20), (2.5, 18.75), (3, 15), (3.5, 8.75), (4, 0)]


class GlobalGraphsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): axes and the story
        title = Tex("Interpreting global graphs: read the axes first").scale(1.05).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        o0 = np.array([-5.5, -2.4, 0])
        ax0 = mini_axes(o0, w=5.2, h=3.6)
        self.play(Create(ax0))
        lx = Tex("time (hours)").scale(0.6).next_to(o0 + RIGHT * 5.2, DOWN)
        ly = Tex("temperature ($^\\circ$C)").scale(0.6).next_to(o0 + UP * 3.6, UP)
        self.play(Write(lx), Write(ly))
        curve0 = polyline(o0, TEMP, sx=0.2, sy=0.12)
        self.play(Create(curve0), run_time=3)
        self.wait(1.5)
        pt = Dot(o0 + RIGHT * 14 * 0.2 + UP * 28 * 0.12, radius=0.08, color=YELLOW)
        self.play(Create(pt))
        l1 = Tex("$(14;\\,28)$: 28 $^\\circ$C at 14:00").scale(0.8).shift(RIGHT * 3.3 + UP * 1.0)
        l2 = Tex("Independent across, dependent up.").scale(0.8).shift(RIGHT * 3.3 + UP * 0.1)
        l3 = Tex("Direction, time, value, unit.").scale(0.8).shift(RIGHT * 3.3 + DOWN * 0.8)
        for m in (l1, l2, l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l1, color=GREEN)))
        self.wait(2)

        # --- Band 1 (subtopic_2): linear / non-linear, direction
        self.next_band(1)
        b1_title = Tex("Increasing, decreasing, constant; straight or curved").scale(1.0).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_title))
        self.wait(1.5)
        o1 = band_shift(1) + np.array([-5.5, -2.2, 0])
        ax1 = mini_axes(o1, w=5.0, h=3.4)
        self.play(Create(ax1))
        walk = polyline(o1, WALK, sx=0.18, sy=0.0025, color=GREEN)
        self.play(Create(walk), run_time=2.5)
        self.wait(1)
        b1_l1 = Tex("0--10 min: increasing \\quad 10--15 min: constant (in the shop) \\quad 15--25 min: increasing").scale(0.7).shift(band_shift(1) + RIGHT * 1.0 + DOWN * 3.0)
        b1_l2 = Tex("Linear: same step each unit. Fare $20 + 12k$.").scale(0.8).shift(band_shift(1) + RIGHT * 3.3 + UP * 1.3)
        b1_l3 = Tex("Non-linear: the step changes. Ball, cooling tea.").scale(0.8).shift(band_shift(1) + RIGHT * 3.3 + UP * 0.4)
        b1_l4 = Tex("Steeper means faster: R15/km above R12/km.").scale(0.8).shift(band_shift(1) + RIGHT * 3.3 + DOWN * 0.5)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): maximum, minimum, turning points
        self.next_band(2)
        b2_title = Tex("Maximum and minimum: the value and when").scale(1.05).shift(band_shift(2) + UP * 2.5)
        self.play(Write(b2_title))
        self.wait(1.5)
        o2 = band_shift(2) + np.array([-5.5, -2.2, 0])
        ax2 = mini_axes(o2, w=5.0, h=3.4)
        self.play(Create(ax2))
        ball = polyline(o2, BALL, sx=1.1, sy=0.15, color=ORANGE)
        self.play(Create(ball), run_time=2.5)
        top = Dot(o2 + RIGHT * 2 * 1.1 + UP * 20 * 0.15, radius=0.08, color=YELLOW)
        self.play(Create(top))
        b2_l1 = Tex("Maximum height 20 m, after 2 s: a turning point.").scale(0.8).shift(band_shift(2) + RIGHT * 3.3 + UP * 1.3)
        b2_l2 = Tex("Temperature: min 8 $^\\circ$C at 05:00, max 28 $^\\circ$C at 14:00.").scale(0.75).shift(band_shift(2) + RIGHT * 3.3 + UP * 0.4)
        b2_l3 = Tex("Steepest at about 09:00; highest at 14:00. Different questions.").scale(0.75).shift(band_shift(2) + RIGHT * 3.3 + DOWN * 0.5)
        b2_l4 = Tex("No turning point? The extremes sit at the ends.").scale(0.8).shift(band_shift(2) + RIGHT * 3.3 + DOWN * 1.4)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): discrete or continuous
        self.next_band(3)
        b3_title = Tex("Discrete: dots. Continuous: a line.").scale(1.1).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_title))
        self.wait(1.5)
        o3 = band_shift(3) + np.array([-5.5, -2.2, 0])
        ax3 = mini_axes(o3, w=4.6, h=3.2)
        self.play(Create(ax3))
        fares = dots(o3, [(1, 15), (2, 30), (3, 45), (4, 60)], sx=1.0, sy=0.05)
        self.play(Create(fares))
        b3_l1 = Tex("Passengers at R15 each: $(1;15), (2;30), (3;45), (4;60)$ --- do not join.").scale(0.7).shift(band_shift(3) + RIGHT * 1.0 + DOWN * 3.0)
        o3b = band_shift(3) + np.array([1.2, -2.2, 0])
        ax3b = mini_axes(o3b, w=4.6, h=3.2)
        line3 = polyline(o3b, [(0, 20), (10, 140)], sx=0.42, sy=0.022, color=BLUE)
        self.play(Create(ax3b))
        self.play(Create(line3))
        b3_l2 = Tex("Fare against kilometres: continuous line.").scale(0.75).shift(band_shift(3) + RIGHT * 3.4 + UP * 1.6)
        b3_l3 = Tex("Can the bottom quantity be a fraction?").scale(0.75).shift(band_shift(3) + RIGHT * 3.4 + UP * 0.9)
        for m in (b3_l1, b3_l2, b3_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(1.5)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Joining the dots on a passengers graph").scale(0.95).shift(band_shift(4) + UP * 1.3)
        b4_l2 = Tex("Flat section means ``went backwards''").scale(0.95).shift(band_shift(4) + UP * 0.3)
        b4_l3 = Tex("``When was it hottest?'' answered with 28 $^\\circ$C").scale(0.95).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = Tex("``It goes up then down'' with no readings").scale(0.95).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): every graph tells a story
        self.next_band(5)
        b5_title = Tex("Every graph tells a story").scale(1.2).shift(band_shift(5) + UP * 2.5)
        self.play(Write(b5_title))
        self.wait(2)
        o5 = band_shift(5) + np.array([-5.5, -2.4, 0])
        ax5 = mini_axes(o5, w=5.2, h=3.6)
        self.play(Create(ax5))
        curve5 = polyline(o5, TEMP, sx=0.2, sy=0.12)
        self.play(Create(curve5), run_time=3)
        b5_l1 = Tex("Labels and units first. Then one point, both ways.").scale(0.75).shift(band_shift(5) + RIGHT * 3.3 + UP * 1.3)
        b5_l2 = Tex("15 at 00:00, down to 8 at 05:00,").scale(0.75).shift(band_shift(5) + RIGHT * 3.3 + UP * 0.4)
        b5_l3 = Tex("up to 28 at 14:00, down to 16 at 24:00.").scale(0.75).shift(band_shift(5) + RIGHT * 3.3 + DOWN * 0.5)
        b5_l4 = Tex("Direction, number, time: four sentences, full marks.").scale(0.75).shift(band_shift(5) + RIGHT * 3.3 + DOWN * 1.4)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): five words
        self.next_band(6)
        b6_title = Tex("Up, down, flat, straight or bendy").scale(1.15).shift(band_shift(6) + UP * 2.5)
        self.play(Write(b6_title))
        self.wait(2)
        o6 = band_shift(6) + np.array([-5.5, -2.2, 0])
        ax6 = mini_axes(o6, w=5.0, h=3.4)
        self.play(Create(ax6))
        walk6 = polyline(o6, WALK, sx=0.18, sy=0.0025, color=GREEN)
        self.play(Create(walk6), run_time=2.5)
        shop = Tex("shop").scale(0.6).move_to(o6 + RIGHT * 12.5 * 0.18 + UP * 600 * 0.0025 + UP * 0.4)
        self.play(Write(shop))
        b6_l1 = Tex("Up = increasing. Down = decreasing. Flat = constant (standing still).").scale(0.72).shift(band_shift(6) + RIGHT * 3.0 + UP * 1.3)
        b6_l2 = Tex("Straight = linear, same step. Bendy = non-linear.").scale(0.75).shift(band_shift(6) + RIGHT * 3.0 + UP * 0.4)
        b6_l3 = Tex("Steeper means faster. Say the word and the interval.").scale(0.75).shift(band_shift(6) + RIGHT * 3.0 + DOWN * 0.5)
        for m in (b6_l1, b6_l2, b6_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): dots or a line, and the peak
        self.next_band(7)
        b7_title = Tex("Dots or a line, and where the peak is").scale(1.1).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7_title))
        self.wait(2)
        o7 = band_shift(7) + np.array([-5.5, -2.2, 0])
        ax7 = mini_axes(o7, w=4.4, h=3.2)
        self.play(Create(ax7))
        fares7 = dots(o7, [(1, 15), (2, 30), (3, 45), (4, 60)], sx=1.0, sy=0.05)
        self.play(Create(fares7))
        b7_l1 = Tex("Whole pieces (passengers): dots. Flows (time, km): a line.").scale(0.72).shift(band_shift(7) + RIGHT * 2.8 + UP * 1.4)
        b7_l2 = Tex("Peak: how high AND when. 28 $^\\circ$C at 14:00. 20 m at 2 s.").scale(0.72).shift(band_shift(7) + RIGHT * 2.8 + UP * 0.5)
        b7_l3 = Tex("Steepest is not highest.").scale(0.8).shift(band_shift(7) + RIGHT * 2.8 + DOWN * 0.4)
        b7_l4 = Tex("Labels. A reading with a unit. Five words. Two numbers. Dots or a line.").scale(0.7).shift(band_shift(7) + RIGHT * 1.0 + DOWN * 3.0)
        for m in (b7_l1, b7_l2, b7_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
