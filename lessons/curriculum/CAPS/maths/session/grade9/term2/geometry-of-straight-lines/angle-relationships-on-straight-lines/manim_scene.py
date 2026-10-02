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


def ray(origin, angle_deg, length=1.8, color=WHITE):
    a = angle_deg * DEGREES
    return Line(origin, origin + length * np.array([np.cos(a), np.sin(a), 0]), color=color, stroke_width=4)


def crossing(centre, angle_deg=35, length=2.0):
    """Two straight lines crossing at centre: one horizontal, one at angle_deg."""
    g = VGroup()
    g.add(Line(centre + LEFT * length, centre + RIGHT * length, color=WHITE, stroke_width=4))
    a = angle_deg * DEGREES
    d = np.array([np.cos(a), np.sin(a), 0]) * length
    g.add(Line(centre - d, centre + d, color=WHITE, stroke_width=4))
    return g


def parallels_with_transversal(centre, gap=1.4, length=2.6, angle_deg=60):
    """Two horizontal parallel lines with arrowheads and one transversal."""
    g = VGroup()
    top = centre + UP * gap / 2
    bot = centre + DOWN * gap / 2
    for y in (top, bot):
        g.add(Line(y + LEFT * length, y + RIGHT * length, color=WHITE, stroke_width=4))
        g.add(Arrow(y + RIGHT * 0.6, y + RIGHT * 1.3, buff=0, color=WHITE, stroke_width=3))
    a = angle_deg * DEGREES
    d = np.array([np.cos(a), np.sin(a), 0])
    t = gap / 2 / np.sin(a) + 0.8
    g.add(Line(centre - d * t, centre + d * t, color=BLUE, stroke_width=4))
    return g


class StraightLineAnglesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): straight line and around a point
        title = Tex("Angles on a straight line and around a point").scale(1.05).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        c0 = np.array([-3.8, -0.3, 0])
        base = Line(c0 + LEFT * 2.2, c0 + RIGHT * 2.2, color=WHITE, stroke_width=4)
        r0 = ray(c0, 65, length=1.8, color=ORANGE)
        self.play(Create(base), Create(r0))
        a115 = MathTex(r"115^\circ").scale(0.7).move_to(c0 + LEFT * 0.9 + UP * 0.45)
        a65 = MathTex(r"65^\circ").scale(0.7).move_to(c0 + RIGHT * 0.9 + UP * 0.35)
        self.play(Write(a115), Write(a65))
        l1 = MathTex(r"115^\circ + 65^\circ = 180^\circ \quad(\angle\text{s on a str line})").scale(0.85).shift(RIGHT * 2.6 + UP * 1.3)
        l2 = MathTex(r"90^\circ + 140^\circ + x = 360^\circ \;\Rightarrow\; x = 130^\circ \quad(\angle\text{s around a point})").scale(0.75).shift(RIGHT * 2.6 + UP * 0.4)
        l3 = MathTex(r"x + (2x + 30) = 180 \;\Rightarrow\; 3x = 150 \;\Rightarrow\; x = 50").scale(0.8).shift(RIGHT * 2.6 + DOWN * 0.5)
        l4 = Tex("Statement, equals, value, reason in brackets.").scale(0.8).shift(RIGHT * 2.6 + DOWN * 1.4)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l4, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): vertically opposite
        self.next_band(1)
        b1_title = Tex("Vertically opposite angles are equal").scale(1.1).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_title))
        self.wait(1.5)
        c1 = band_shift(1) + np.array([-3.8, -0.4, 0])
        self.play(Create(crossing(c1, angle_deg=35)))
        la = MathTex(r"70^\circ").scale(0.65).move_to(c1 + RIGHT * 0.95 + UP * 0.3)
        lc = MathTex(r"70^\circ").scale(0.65).move_to(c1 + LEFT * 0.95 + DOWN * 0.3)
        lb = MathTex(r"110^\circ").scale(0.65).move_to(c1 + UP * 0.6 + LEFT * 0.4)
        ld = MathTex(r"110^\circ").scale(0.65).move_to(c1 + DOWN * 0.6 + RIGHT * 0.4)
        self.play(Write(la), Write(lc))
        self.play(Write(lb), Write(ld))
        b1_l1 = MathTex(r"a + b = 180,\; b + c = 180 \;\Rightarrow\; a = c").scale(0.9).shift(band_shift(1) + RIGHT * 2.8 + UP * 1.3)
        b1_l2 = MathTex(r"3x - 10 = 2x + 20 \quad(\text{vert opp }\angle\text{s}) \;\Rightarrow\; x = 30").scale(0.8).shift(band_shift(1) + RIGHT * 2.8 + UP * 0.4)
        b1_l3 = MathTex(r"\text{angles } 80^\circ, 80^\circ, 100^\circ, 100^\circ").scale(0.85).shift(band_shift(1) + RIGHT * 2.8 + DOWN * 0.5)
        b1_l4 = Tex("Equal, not supplementary. Two full lines must cross.").scale(0.78).shift(band_shift(1) + RIGHT * 2.8 + DOWN * 1.4)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): parallel lines
        self.next_band(2)
        b2_title = Tex("Parallel lines and a transversal: F, Z, C").scale(1.05).shift(band_shift(2) + UP * 2.5)
        self.play(Write(b2_title))
        self.wait(1.5)
        c2 = band_shift(2) + np.array([-3.6, -0.4, 0])
        self.play(Create(parallels_with_transversal(c2)))
        top_c = c2 + UP * 0.7 + RIGHT * 0.7 / np.tan(60 * DEGREES)
        bot_c = c2 + DOWN * 0.7 - RIGHT * 0.7 / np.tan(60 * DEGREES)
        t125 = MathTex(r"125^\circ").scale(0.6).move_to(top_c + LEFT * 0.55 + UP * 0.3)
        b125 = MathTex(r"125^\circ").scale(0.6).move_to(bot_c + LEFT * 0.55 + UP * 0.3)
        b55 = MathTex(r"55^\circ").scale(0.6).move_to(bot_c + LEFT * 0.5 + DOWN * 0.3)
        self.play(Write(t125))
        self.play(Write(b125), Write(b55))
        b2_l1 = Tex("Corresponding (F): equal. \\quad $125^\\circ$ \;(corresp $\\angle$s, AB $\\parallel$ CD)").scale(0.72).shift(band_shift(2) + RIGHT * 2.8 + UP * 1.3)
        b2_l2 = Tex("Alternate (Z): equal. \\quad $125^\\circ$ \;(alt $\\angle$s, AB $\\parallel$ CD)").scale(0.72).shift(band_shift(2) + RIGHT * 2.8 + UP * 0.4)
        b2_l3 = Tex("Co-interior (C): add to $180^\\circ$. \\quad $55^\\circ$ \;(co-int $\\angle$s, AB $\\parallel$ CD)").scale(0.72).shift(band_shift(2) + RIGHT * 2.8 + DOWN * 0.5)
        b2_l4 = Tex("Converse: equal alt angles prove the lines parallel.").scale(0.75).shift(band_shift(2) + RIGHT * 2.8 + DOWN * 1.4)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): naming and notation
        self.next_band(3)
        b3_title = Tex("Naming, notation, reasons").scale(1.15).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("$\\angle ABC$: vertex $B$ in the middle, arms $BA$ and $BC$.").scale(0.85).shift(band_shift(3) + UP * 1.3)
        b3_l2 = Tex("Arrowheads: parallel. Matching arcs: equal. Small square: $90^\\circ$.").scale(0.85).shift(band_shift(3) + UP * 0.4)
        b3_l3 = Tex("Reasons: $\\angle$s on a str line; $\\angle$s around a point; vert opp $\\angle$s;").scale(0.8).shift(band_shift(3) + DOWN * 0.5)
        b3_l4 = Tex("corresp / alt / co-int $\\angle$s with the parallel lines named; given.").scale(0.8).shift(band_shift(3) + DOWN * 1.3)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(1.5)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("A parallel-line reason with no arrowheads").scale(0.95).shift(band_shift(4) + UP * 1.3)
        b4_l2 = Tex("``alt $\\angle$s'' written for a co-interior pair").scale(0.95).shift(band_shift(4) + UP * 0.3)
        b4_l3 = Tex("``They look equal''").scale(0.95).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = Tex("A correct value with no reason").scale(0.95).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): half a turn
        self.next_band(5)
        b5_title = Tex("Half a turn is 180").scale(1.2).shift(band_shift(5) + UP * 2.5)
        self.play(Write(b5_title))
        self.wait(2)
        c5 = band_shift(5) + np.array([-3.8, -0.3, 0])
        self.play(Create(Line(c5 + LEFT * 2.2, c5 + RIGHT * 2.2, color=WHITE, stroke_width=4)), Create(ray(c5, 65, color=ORANGE)))
        arc = Arc(radius=0.8, start_angle=0, angle=PI, arc_center=c5, color=GREEN)
        self.play(Create(arc))
        b5_l1 = Tex("Full turn 360. Half-turn 180. Quarter-turn 90.").scale(0.85).shift(band_shift(5) + RIGHT * 2.8 + UP * 1.3)
        b5_l2 = MathTex(r"180 - 115 = 65 \quad(\angle\text{s on a straight line})").scale(0.85).shift(band_shift(5) + RIGHT * 2.8 + UP * 0.4)
        b5_l3 = MathTex(r"x + 2x + 30 = 180 \;\Rightarrow\; x = 50: \; 50^\circ \text{ and } 130^\circ").scale(0.8).shift(band_shift(5) + RIGHT * 2.8 + DOWN * 0.5)
        b5_l4 = Tex("The reason in brackets is the mark.").scale(0.85).shift(band_shift(5) + RIGHT * 2.8 + DOWN * 1.4)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): scissors
        self.next_band(6)
        b6_title = Tex("Scissors and the X").scale(1.2).shift(band_shift(6) + UP * 2.5)
        self.play(Write(b6_title))
        self.wait(2)
        c6 = band_shift(6) + np.array([-3.8, -0.4, 0])
        self.play(Create(crossing(c6, angle_deg=35)))
        s_a = MathTex(r"70").scale(0.7).move_to(c6 + RIGHT * 0.95 + UP * 0.3)
        s_c = MathTex(r"70").scale(0.7).move_to(c6 + LEFT * 0.95 + DOWN * 0.3)
        s_b = MathTex(r"110").scale(0.7).move_to(c6 + UP * 0.6 + LEFT * 0.4)
        s_d = MathTex(r"110").scale(0.7).move_to(c6 + DOWN * 0.6 + RIGHT * 0.4)
        self.play(Write(s_a), Write(s_c))
        self.play(Write(s_b), Write(s_d))
        b6_l1 = Tex("Blades and handles: opposite angles are EQUAL.").scale(0.85).shift(band_shift(6) + RIGHT * 2.8 + UP * 1.3)
        b6_l2 = Tex("Neighbours add to 180. One number unlocks all four.").scale(0.8).shift(band_shift(6) + RIGHT * 2.8 + UP * 0.4)
        b6_l3 = MathTex(r"3x - 10 = 2x + 20 \;\Rightarrow\; x = 30 \;\Rightarrow\; 80, 80, 100, 100").scale(0.8).shift(band_shift(6) + RIGHT * 2.8 + DOWN * 0.5)
        b6_l4 = Tex("Two full lines must cross to make an X.").scale(0.85).shift(band_shift(6) + RIGHT * 2.8 + DOWN * 1.4)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2)

        # --- Band 7 (subtopic_7): F, Z, C
        self.next_band(7)
        b7_title = Tex("F, Z and C: the parallel line alphabet").scale(1.1).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7_title))
        self.wait(2)
        c7 = band_shift(7) + np.array([-3.6, -0.4, 0])
        self.play(Create(parallels_with_transversal(c7)))
        b7_l1 = Tex("F: corresponding, equal.").scale(0.85).shift(band_shift(7) + RIGHT * 2.8 + UP * 1.3)
        b7_l2 = Tex("Z (or N): alternate, equal.").scale(0.85).shift(band_shift(7) + RIGHT * 2.8 + UP * 0.5)
        b7_l3 = Tex("C (or U): co-interior, add to 180.").scale(0.85).shift(band_shift(7) + RIGHT * 2.8 + DOWN * 0.3)
        b7_l4 = Tex("Arrowheads first. Three letters per angle. Reason in brackets.").scale(0.72).shift(band_shift(7) + RIGHT * 2.8 + DOWN * 1.2)
        for m in (b7_l1, b7_l2, b7_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
