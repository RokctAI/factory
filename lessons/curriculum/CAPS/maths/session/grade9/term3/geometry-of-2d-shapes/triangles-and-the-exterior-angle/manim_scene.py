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


def tri(a, b, c, color=WHITE):
    """Triangle from three points."""
    return Polygon(a, b, c, color=color, stroke_width=4)


def tick(p, q, color=YELLOW):
    """A short dash across the midpoint of segment pq, marking equal sides."""
    m = (p + q) / 2
    d = q - p
    n = np.array([-d[1], d[0], 0])
    n = n / np.linalg.norm(n) * 0.15
    return Line(m - n, m + n, color=color, stroke_width=3)


class TrianglesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): classification
        title = Tex("Triangles: by sides and by angles").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        base = np.array([-5.2, -1.4, 0])
        t_sc = tri(base, base + RIGHT * 2.0, base + RIGHT * 0.5 + UP * 1.6)
        b2 = base + RIGHT * 2.8
        t_is = tri(b2, b2 + RIGHT * 2.0, b2 + RIGHT * 1.0 + UP * 1.8)
        b3 = base + RIGHT * 5.6
        t_eq = tri(b3, b3 + RIGHT * 2.0, b3 + RIGHT * 1.0 + UP * 1.73)
        self.play(Create(t_sc), Create(t_is), Create(t_eq))
        self.play(Create(tick(b2, b2 + RIGHT * 1.0 + UP * 1.8)), Create(tick(b2 + RIGHT * 2.0, b2 + RIGHT * 1.0 + UP * 1.8)))
        labs = VGroup(Tex("scalene").scale(0.6).next_to(t_sc, DOWN), Tex("isosceles").scale(0.6).next_to(t_is, DOWN), Tex("equilateral").scale(0.6).next_to(t_eq, DOWN))
        self.play(Write(labs))
        l1 = Tex("By angles: acute, right-angled (small square), obtuse.").scale(0.8).shift(UP * 1.6)
        l2 = Tex("Isosceles: angles opposite the equal sides are equal (base angles).").scale(0.78).shift(UP * 0.8)
        l3 = Tex("Equilateral: three angles of $60^\\circ$. Never two right angles.").scale(0.78).shift(UP * 0.0)
        for m in (l1, l2, l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l2, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): angle sum
        self.next_band(1)
        b1_title = Tex("Sum of angles in a triangle: $180^\\circ$").scale(1.15).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_title))
        self.wait(1.5)
        a = band_shift(1) + np.array([-5.0, -1.6, 0])
        t1 = tri(a, a + RIGHT * 3.2, a + RIGHT * 2.2 + UP * 2.2, color=BLUE)
        self.play(Create(t1))
        ang = VGroup(MathTex(r"50^\circ").scale(0.6).move_to(a + RIGHT * 0.7 + UP * 0.3),
                     MathTex(r"60^\circ").scale(0.6).move_to(a + RIGHT * 2.6 + UP * 0.3),
                     MathTex(r"70^\circ").scale(0.6).move_to(a + RIGHT * 2.1 + UP * 1.7))
        self.play(Write(ang))
        b1_l1 = MathTex(r"180 - 50 - 60 = 70^\circ \quad(\text{sum of }\angle\text{s in a triangle})").scale(0.8).shift(band_shift(1) + RIGHT * 2.4 + UP * 1.3)
        b1_l2 = MathTex(r"\text{isosceles, apex } 40^\circ: \; 40 + 2x = 180 \Rightarrow x = 70^\circ").scale(0.8).shift(band_shift(1) + RIGHT * 2.4 + UP * 0.4)
        b1_l3 = MathTex(r"x + 2x + 3x = 180 \Rightarrow x = 30: \; 30^\circ, 60^\circ, 90^\circ").scale(0.8).shift(band_shift(1) + RIGHT * 2.4 + DOWN * 0.5)
        b1_l4 = Tex("Right-angled: the other two angles add to 90.").scale(0.8).shift(band_shift(1) + RIGHT * 2.4 + DOWN * 1.4)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): exterior angle
        self.next_band(2)
        b2_title = Tex("Exterior angle = sum of the two interior opposite angles").scale(0.95).shift(band_shift(2) + UP * 2.5)
        self.play(Write(b2_title))
        self.wait(1.5)
        a2 = band_shift(2) + np.array([-5.4, -1.6, 0])
        pb = a2 + RIGHT * 3.0
        pc = a2 + RIGHT * 2.0 + UP * 2.0
        t2 = tri(a2, pb, pc, color=BLUE)
        self.play(Create(t2))
        ext = Line(pb, pb + RIGHT * 1.6, color=ORANGE, stroke_width=4)
        self.play(Create(ext))
        labs2 = VGroup(MathTex(r"A").scale(0.6).next_to(a2, DL, buff=0.05), MathTex(r"B").scale(0.6).next_to(pb, DOWN, buff=0.1), MathTex(r"C").scale(0.6).next_to(pc, UP, buff=0.1))
        angs2 = VGroup(MathTex(r"50^\circ").scale(0.55).move_to(a2 + RIGHT * 0.75 + UP * 0.3),
                       MathTex(r"60^\circ").scale(0.55).move_to(pc + DOWN * 0.55),
                       MathTex(r"110^\circ").scale(0.55).move_to(pb + RIGHT * 0.5 + UP * 0.45))
        self.play(Write(labs2), Write(angs2))
        b2_l1 = MathTex(r"\text{ext } \angle \text{ at } B = 180 - \angle B \quad(\angle\text{s on a str line})").scale(0.78).shift(band_shift(2) + RIGHT * 2.6 + UP * 1.3)
        b2_l2 = MathTex(r"\angle A + \angle C = 180 - \angle B \quad(\text{sum of }\angle\text{s in a triangle})").scale(0.78).shift(band_shift(2) + RIGHT * 2.6 + UP * 0.4)
        b2_l3 = MathTex(r"\therefore \text{ ext } \angle \text{ at } B = \angle A + \angle C = 50 + 60 = 110^\circ").scale(0.78).shift(band_shift(2) + RIGHT * 2.6 + DOWN * 0.5)
        b2_l4 = Tex("Construct, measure, suspect; then prove in two lines.").scale(0.78).shift(band_shift(2) + RIGHT * 2.6 + DOWN * 1.4)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): problems
        self.next_band(3)
        b3_title = Tex("Problems: numbers, algebra, isosceles").scale(1.1).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{ext } 120^\circ,\; \angle A = 45^\circ \Rightarrow \angle B = 75^\circ \quad(\text{ext }\angle\text{ of a triangle})").scale(0.78).shift(band_shift(3) + UP * 1.3)
        b3_l2 = MathTex(r"2x + 10 = (x + 15) + 35 \Rightarrow x = 40: \; \text{ext } 90^\circ,\; 55^\circ \text{ and } 35^\circ").scale(0.78).shift(band_shift(3) + UP * 0.4)
        b3_l3 = MathTex(r"\text{isosceles, ext } 100^\circ \text{ at apex} \Rightarrow \text{base angles } 50^\circ \text{ each}").scale(0.78).shift(band_shift(3) + DOWN * 0.5)
        b3_l4 = MathTex(r"\text{check: } 45 + 75 + 60 = 180 \qquad 55 + 35 = 90").scale(0.8).shift(band_shift(3) + DOWN * 1.4)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(1.5)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Exterior angle = adjacent interior + one other").scale(0.95).shift(band_shift(4) + UP * 1.3)
        b4_l2 = Tex("An exterior angle of $190^\\circ$ accepted without a check").scale(0.95).shift(band_shift(4) + UP * 0.3)
        b4_l3 = Tex("Equal angles placed NEXT to the equal sides").scale(0.95).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = Tex("A right angle assumed with no square mark").scale(0.95).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): sorting boxes
        self.next_band(5)
        b5_title = Tex("Sorting triangles into boxes").scale(1.2).shift(band_shift(5) + UP * 2.5)
        self.play(Write(b5_title))
        self.wait(2)
        box1 = Rectangle(width=4.0, height=2.2, color=ORANGE).shift(band_shift(5) + LEFT * 3.0 + UP * 0.3)
        box2 = Rectangle(width=4.0, height=2.2, color=BLUE).shift(band_shift(5) + RIGHT * 3.0 + UP * 0.3)
        self.play(Create(box1), Create(box2))
        s1 = Tex("Sides: scalene, isosceles, equilateral").scale(0.7).move_to(box1.get_center() + UP * 0.6)
        s2 = Tex("Angles: acute, right-angled, obtuse").scale(0.7).move_to(box2.get_center() + UP * 0.6)
        self.play(Write(s1), Write(s2))
        b5_l1 = Tex("Roof rule: equal sides face equal angles.").scale(0.75).move_to(box1.get_center() + DOWN * 0.4)
        b5_l2 = Tex("Never two square or two wide corners.").scale(0.75).move_to(box2.get_center() + DOWN * 0.4)
        b5_l3 = Tex("Read the marks: dashes, tiny square, matching arcs.").scale(0.85).shift(band_shift(5) + DOWN * 1.7)
        for m in (b5_l1, b5_l2, b5_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): half a turn
        self.next_band(6)
        b6_title = Tex("Half a turn folded into three corners").scale(1.1).shift(band_shift(6) + UP * 2.5)
        self.play(Write(b6_title))
        self.wait(2)
        a6 = band_shift(6) + np.array([-5.0, -1.6, 0])
        t6 = tri(a6, a6 + RIGHT * 3.2, a6 + RIGHT * 2.2 + UP * 2.2, color=BLUE)
        self.play(Create(t6))
        line6 = Line(band_shift(6) + LEFT * 1.0 + DOWN * 2.0, band_shift(6) + RIGHT * 3.0 + DOWN * 2.0, color=GREEN, stroke_width=4)
        self.play(Create(line6))
        b6_l1 = Tex("Tear off the corners; they make a straight line.").scale(0.8).shift(band_shift(6) + RIGHT * 2.4 + UP * 1.3)
        b6_l2 = MathTex(r"50 + 60 \Rightarrow 70 \qquad \text{roof } 40 \Rightarrow 70, 70").scale(0.85).shift(band_shift(6) + RIGHT * 2.4 + UP * 0.4)
        b6_l3 = MathTex(r"x + 2x + 3x = 180 \Rightarrow x = 30 \Rightarrow 30, 60, 90").scale(0.85).shift(band_shift(6) + RIGHT * 2.4 + DOWN * 0.5)
        b6_l4 = Tex("Put $x$ back. $x$ is the key, not the corner.").scale(0.8).shift(band_shift(6) + RIGHT * 2.4 + DOWN * 1.4)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)

        # --- Band 7 (subtopic_7): the ramp
        self.next_band(7)
        b7_title = Tex("The outside angle equals the two far corners").scale(1.05).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7_title))
        self.wait(2)
        a7 = band_shift(7) + np.array([-5.4, -1.6, 0])
        pb7 = a7 + RIGHT * 3.0
        pc7 = a7 + RIGHT * 2.0 + UP * 2.0
        self.play(Create(tri(a7, pb7, pc7, color=BLUE)))
        self.play(Create(Line(pb7, pb7 + RIGHT * 1.6, color=ORANGE, stroke_width=4)))
        far = VGroup(MathTex(r"50").scale(0.6).move_to(a7 + RIGHT * 0.75 + UP * 0.3), MathTex(r"60").scale(0.6).move_to(pc7 + DOWN * 0.55))
        out = MathTex(r"110").scale(0.6).move_to(pb7 + RIGHT * 0.5 + UP * 0.45)
        self.play(Write(far), Write(out))
        b7_l1 = Tex("Far corners 50 and 60: outside angle 110. Not the near one.").scale(0.75).shift(band_shift(7) + RIGHT * 2.6 + UP * 1.3)
        b7_l2 = MathTex(r"2x + 10 = x + 15 + 35 \Rightarrow x = 40 \Rightarrow 90 = 55 + 35").scale(0.8).shift(band_shift(7) + RIGHT * 2.6 + UP * 0.4)
        b7_l3 = Tex("Outside and near corner make 180; far corners and near corner make 180.").scale(0.7).shift(band_shift(7) + RIGHT * 2.6 + DOWN * 0.5)
        b7_l4 = Tex("Two boxes. Half-turn. Outside equals the two far corners.").scale(0.78).shift(band_shift(7) + RIGHT * 2.6 + DOWN * 1.4)
        for m in (b7_l1, b7_l2, b7_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
