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


def crossing(centre, angle_deg=35, length=2.0):
    g = VGroup()
    g.add(Line(centre + LEFT * length, centre + RIGHT * length, color=WHITE, stroke_width=4))
    a = angle_deg * DEGREES
    d = np.array([np.cos(a), np.sin(a), 0]) * length
    g.add(Line(centre - d, centre + d, color=WHITE, stroke_width=4))
    return g


def parallels(centre, gap=1.6, length=2.8, arrows=True):
    g = VGroup()
    for y in (centre + UP * gap / 2, centre + DOWN * gap / 2):
        g.add(Line(y + LEFT * length, y + RIGHT * length, color=WHITE, stroke_width=4))
        if arrows:
            g.add(Arrow(y + RIGHT * 0.8, y + RIGHT * 1.5, buff=0, color=WHITE, stroke_width=3))
    return g


def triangle_between(centre, gap=1.6, apex_x=0.0, f_x=-1.2, g_x=1.0):
    """Triangle EFG with apex E on the top parallel and base FG on the bottom."""
    e = centre + UP * gap / 2 + RIGHT * apex_x
    f = centre + DOWN * gap / 2 + RIGHT * f_x
    gpt = centre + DOWN * gap / 2 + RIGHT * g_x
    return VGroup(Line(e, f, color=BLUE, stroke_width=4), Line(e, gpt, color=BLUE, stroke_width=4)), e, f, gpt


class AnglePairProblemsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): intersecting lines with algebra
        title = Tex("Angle problems: a chain of statements and reasons").scale(1.05).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        c0 = np.array([-3.8, -0.4, 0])
        self.play(Create(crossing(c0, angle_deg=40)))
        la = MathTex(r"2x").scale(0.7).move_to(c0 + RIGHT * 0.9 + UP * 0.35)
        lb = MathTex(r"x + 30").scale(0.65).move_to(c0 + UP * 0.7 + LEFT * 0.5)
        self.play(Write(la), Write(lb))
        l1 = MathTex(r"2x + x + 30 = 180 \quad(\angle\text{s on a str line}) \;\Rightarrow\; x = 50").scale(0.8).shift(RIGHT * 2.6 + UP * 1.3)
        l2 = MathTex(r"2x = 100^\circ, \quad x + 30 = 80^\circ").scale(0.9).shift(RIGHT * 2.6 + UP * 0.4)
        l3 = MathTex(r"\text{opposite angles } 100^\circ, 80^\circ \quad(\text{vert opp }\angle\text{s})").scale(0.8).shift(RIGHT * 2.6 + DOWN * 0.5)
        l4 = MathTex(r"\text{check: } 100 + 80 + 100 + 80 = 360").scale(0.85).shift(RIGHT * 2.6 + DOWN * 1.4)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l2, color=GREEN)))
        self.wait(2)

        # --- Band 1 (subtopic_2): algebra with parallel lines
        self.next_band(1)
        b1_title = Tex("Algebra with parallel lines: say the pair first").scale(1.05).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_title))
        self.wait(1.5)
        c1 = band_shift(1) + np.array([-3.8, -0.4, 0])
        self.play(Create(parallels(c1)))
        tr = Line(c1 + LEFT * 1.4 + DOWN * 1.3, c1 + RIGHT * 1.4 + UP * 1.3, color=BLUE, stroke_width=4)
        self.play(Create(tr))
        b1_l1 = MathTex(r"\text{corresp: } 3x - 15 = 2x + 25 \;\Rightarrow\; x = 40,\; 105^\circ").scale(0.8).shift(band_shift(1) + RIGHT * 2.6 + UP * 1.3)
        b1_l2 = MathTex(r"\text{alt: } 4x = 2x + 50 \;\Rightarrow\; x = 25,\; 100^\circ").scale(0.8).shift(band_shift(1) + RIGHT * 2.6 + UP * 0.4)
        b1_l3 = MathTex(r"\text{co-int: } 2x + 10 + x + 20 = 180 \;\Rightarrow\; x = 50,\; 110^\circ \text{ and } 70^\circ").scale(0.75).shift(band_shift(1) + RIGHT * 2.6 + DOWN * 0.5)
        b1_l4 = Tex("F and Z: equal. C: sum to 180. Then substitute back.").scale(0.78).shift(band_shift(1) + RIGHT * 2.6 + DOWN * 1.4)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): two transversals, triangle
        self.next_band(2)
        b2_title = Tex("Two transversals: the triangle between the parallels").scale(1.0).shift(band_shift(2) + UP * 2.5)
        self.play(Write(b2_title))
        self.wait(1.5)
        c2 = band_shift(2) + np.array([-3.8, -0.4, 0])
        self.play(Create(parallels(c2)))
        tri, e, f, gpt = triangle_between(c2)
        self.play(Create(tri))
        lE = MathTex(r"E").scale(0.6).next_to(e, UP, buff=0.1)
        lF = MathTex(r"F").scale(0.6).next_to(f, DOWN, buff=0.1)
        lG = MathTex(r"G").scale(0.6).next_to(gpt, DOWN, buff=0.1)
        a50 = MathTex(r"50^\circ").scale(0.55).move_to(f + RIGHT * 0.45 + UP * 0.25)
        a60 = MathTex(r"60^\circ").scale(0.55).move_to(gpt + LEFT * 0.45 + UP * 0.25)
        self.play(Write(lE), Write(lF), Write(lG), Write(a50), Write(a60))
        b2_l1 = MathTex(r"\angle AEF = 50^\circ \quad(\text{alt }\angle\text{s, AB} \parallel \text{CD})").scale(0.8).shift(band_shift(2) + RIGHT * 2.6 + UP * 1.3)
        b2_l2 = MathTex(r"\angle BEG = 60^\circ \quad(\text{alt }\angle\text{s, AB} \parallel \text{CD})").scale(0.8).shift(band_shift(2) + RIGHT * 2.6 + UP * 0.4)
        b2_l3 = MathTex(r"\angle FEG = 180 - 50 - 60 = 70^\circ \quad(\angle\text{s on a str line})").scale(0.75).shift(band_shift(2) + RIGHT * 2.6 + DOWN * 0.5)
        b2_l4 = Tex("The angles of the triangle add to 180: proved, not assumed.").scale(0.75).shift(band_shift(2) + RIGHT * 2.6 + DOWN * 1.4)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): proving parallel
        self.next_band(3)
        b3_title = Tex("Proving lines parallel: the converses").scale(1.1).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_title))
        self.wait(1.5)
        c3 = band_shift(3) + np.array([-3.8, -0.4, 0])
        self.play(Create(parallels(c3, arrows=False)))
        tr3 = Line(c3 + LEFT * 1.4 + DOWN * 1.3, c3 + RIGHT * 1.4 + UP * 1.3, color=BLUE, stroke_width=4)
        self.play(Create(tr3))
        q1 = MathTex(r"65^\circ").scale(0.55).move_to(c3 + UP * 0.8 + LEFT * 0.75)
        q2 = MathTex(r"65^\circ").scale(0.55).move_to(c3 + DOWN * 0.8 + RIGHT * 0.75)
        self.play(Write(q1), Write(q2))
        b3_l1 = MathTex(r"\text{alt } \angle\text{s equal} \;\Rightarrow\; PQ \parallel RS").scale(0.9).shift(band_shift(3) + RIGHT * 2.6 + UP * 1.3)
        b3_l2 = MathTex(r"110 + 70 = 180 \;\Rightarrow\; PQ \parallel RS \quad(\text{co-int }\angle\text{s suppl.})").scale(0.75).shift(band_shift(3) + RIGHT * 2.6 + UP * 0.4)
        b3_l3 = MathTex(r"110 + 65 = 175 \neq 180 \;\Rightarrow\; \text{not parallel}").scale(0.8).shift(band_shift(3) + RIGHT * 2.6 + DOWN * 0.5)
        b3_l4 = Tex("Build the pair with the straight line and the X, then compare.").scale(0.72).shift(band_shift(3) + RIGHT * 2.6 + DOWN * 1.4)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(1.5)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Using a parallel rule inside a proof that the lines are parallel").scale(0.85).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"x = 50 \;\text{(and stop)}").scale(0.95).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"\text{co-int: } 2x + 10 = x + 20").scale(0.95).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = Tex("An angle used before it has been found; reasons left off").scale(0.85).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): dominoes
        self.next_band(5)
        b5_title = Tex("Find one, then the next").scale(1.2).shift(band_shift(5) + UP * 2.5)
        self.play(Write(b5_title))
        self.wait(2)
        doms = VGroup(*[Rectangle(width=0.5, height=1.4, color=ORANGE).shift(band_shift(5) + LEFT * 4.5 + RIGHT * i * 0.8 + UP * 0.6) for i in range(5)])
        self.play(Create(doms))
        b5_l1 = MathTex(r"3x + 30 = 180 \;\Rightarrow\; x = 50 \quad(\angle\text{s on a straight line})").scale(0.8).shift(band_shift(5) + RIGHT * 2.4 + UP * 1.3)
        b5_l2 = MathTex(r"\text{put } x \text{ back: } 100^\circ, 80^\circ; \;\text{X rule: } 100^\circ, 80^\circ").scale(0.8).shift(band_shift(5) + RIGHT * 2.4 + UP * 0.4)
        b5_l3 = Tex("$x$ is the key, not the angle. Open the door.").scale(0.85).shift(band_shift(5) + RIGHT * 2.4 + DOWN * 0.5)
        b5_l4 = Tex("Pizza of six slices: 40, 65, 75 and their twins; total 360.").scale(0.75).shift(band_shift(5) + RIGHT * 2.4 + DOWN * 1.4)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): letters inside F Z C
        self.next_band(6)
        b6_title = Tex("Letters inside the F, Z and C").scale(1.15).shift(band_shift(6) + UP * 2.5)
        self.play(Write(b6_title))
        self.wait(2)
        c6 = band_shift(6) + np.array([-3.8, -0.4, 0])
        self.play(Create(parallels(c6)))
        tr6 = Line(c6 + LEFT * 1.4 + DOWN * 1.3, c6 + RIGHT * 1.4 + UP * 1.3, color=BLUE, stroke_width=4)
        self.play(Create(tr6))
        b6_l1 = MathTex(r"\text{F or Z: twins} \;\Rightarrow\; 3x - 15 = 2x + 25 \;\Rightarrow\; x = 40").scale(0.8).shift(band_shift(6) + RIGHT * 2.6 + UP * 1.3)
        b6_l2 = MathTex(r"\text{C: a couple} \;\Rightarrow\; 2x + 10 + x + 20 = 180 \;\Rightarrow\; x = 50").scale(0.8).shift(band_shift(6) + RIGHT * 2.6 + UP * 0.4)
        b6_l3 = Tex("Set the C pair equal by mistake: 30 and 30, not 180. Busted.").scale(0.75).shift(band_shift(6) + RIGHT * 2.6 + DOWN * 0.5)
        b6_l4 = Tex("Say the letter. Equals for twins. Plus and 180 for the couple.").scale(0.75).shift(band_shift(6) + RIGHT * 2.6 + DOWN * 1.4)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)

        # --- Band 7 (subtopic_7): prove it parallel
        self.next_band(7)
        b7_title = Tex("Prove it parallel, or prove it not").scale(1.15).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7_title))
        self.wait(2)
        c7 = band_shift(7) + np.array([-3.8, -0.4, 0])
        self.play(Create(parallels(c7, arrows=False)))
        tr7 = Line(c7 + LEFT * 1.4 + DOWN * 1.3, c7 + RIGHT * 1.4 + UP * 1.3, color=BLUE, stroke_width=4)
        self.play(Create(tr7))
        b7_l1 = Tex("Equal Z or F angles: parallel. C angles adding to 180: parallel.").scale(0.75).shift(band_shift(7) + RIGHT * 2.6 + UP * 1.3)
        b7_l2 = MathTex(r"110 + 70 = 180: \text{ parallel.} \qquad 110 + 65 = 175: \text{ not parallel.}").scale(0.78).shift(band_shift(7) + RIGHT * 2.6 + UP * 0.4)
        b7_l3 = Tex("Build the pair with the X first if you must. Never assume the answer.").scale(0.72).shift(band_shift(7) + RIGHT * 2.6 + DOWN * 0.5)
        b7_l4 = Tex("Dominoes in order. Say the letter. Put $x$ back. Run the letters backwards.").scale(0.72).shift(band_shift(7) + RIGHT * 2.6 + DOWN * 1.4)
        for m in (b7_l1, b7_l2, b7_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
