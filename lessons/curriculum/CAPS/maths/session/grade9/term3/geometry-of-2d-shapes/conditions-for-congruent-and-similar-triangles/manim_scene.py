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
    return Polygon(a, b, c, color=color, stroke_width=4)


def tick(p, q, color=YELLOW):
    m = (p + q) / 2
    d = q - p
    n = np.array([-d[1], d[0], 0])
    n = n / np.linalg.norm(n) * 0.15
    return Line(m - n, m + n, color=color, stroke_width=3)


def scaled_tri(origin, k):
    """A 3-4-5 triangle scaled by k with its right angle at origin."""
    return tri(origin, origin + RIGHT * 1.2 * k, origin + UP * 0.9 * k)


class CongruenceSimilaritySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the four conditions
        title = Tex("Congruent triangles: four conditions").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        a = np.array([-6.0, -2.2, 0])
        t1 = tri(a, a + RIGHT * 2.4, a + RIGHT * 0.8 + UP * 1.8)
        b = a + RIGHT * 3.4
        t2 = tri(b, b + RIGHT * 2.4, b + RIGHT * 0.8 + UP * 1.8)
        self.play(Create(t1), Create(t2))
        self.play(Create(tick(a, a + RIGHT * 2.4)), Create(tick(b, b + RIGHT * 2.4)))
        c1 = MathTex(r"\triangle ABC \equiv \triangle DEF").scale(0.9).shift(UP * 2.2 + RIGHT * 2.0)
        c2 = Tex("Letters in order: $A \\leftrightarrow D$, $B \\leftrightarrow E$, $C \\leftrightarrow F$.").scale(0.72).shift(UP * 1.4 + RIGHT * 2.0)
        c3 = Tex("SSS: three sides. \\quad SAS: two sides and the included angle.").scale(0.72).shift(UP * 0.5 + RIGHT * 2.0)
        c4 = Tex("AAS: two angles and a side. \\quad RHS: right angle, hypotenuse, side.").scale(0.72).shift(DOWN * 0.3 + RIGHT * 2.0)
        for m in (c1, c2, c3, c4):
            self.play(Write(m))
            self.wait(2.5)
        self.play(Create(SurroundingRectangle(c2, color=YELLOW)))
        self.wait(5)

        # --- Band 1 (subtopic_2): what fails
        self.next_band(1)
        h1 = Tex("Not enough: AAA and SSA").scale(1.05).move_to(band_shift(1) + UP * 3.2)
        self.play(Write(h1))
        o = np.array([-6.2, -1.8, 0]) + band_shift(1)
        small = tri(o, o + RIGHT * 1.6, o + RIGHT * 0.5 + UP * 1.3)
        big = tri(o + RIGHT * 2.2, o + RIGHT * 5.4, o + RIGHT * 3.2 + UP * 2.6)
        self.play(Create(small), Create(big))
        f1 = Tex("Angles 40, 60, 80: base 4 or base 8. Same shape, different size.").scale(0.7).move_to(band_shift(1) + UP * 2.2 + RIGHT * 1.6)
        f2 = Tex("AAA fixes shape, not size: similarity, not congruence.").scale(0.72).move_to(band_shift(1) + UP * 1.4 + RIGHT * 1.6)
        f3 = Tex("SSA: side 7, angle $40^\\circ$ at its end, arc of 5 from the other end").scale(0.7).move_to(band_shift(1) + UP * 0.5 + RIGHT * 1.6)
        f4 = Tex("cuts the arm TWICE: two triangles. Not a condition.").scale(0.72).move_to(band_shift(1) + DOWN * 0.3 + RIGHT * 1.6)
        f5 = Tex("Collect: common sides, radii, vertically opposite angles, bisectors.").scale(0.7).move_to(band_shift(1) + DOWN * 2.6 + RIGHT * 1.0)
        for m in (f1, f2, f3, f4, f5):
            self.play(Write(m))
            self.wait(2.4)
        self.wait(4)

        # --- Band 2 (subtopic_3): similarity
        self.next_band(2)
        h2 = Tex("Similar: equal angles, sides in the same ratio").scale(1.05).move_to(band_shift(2) + UP * 3.2)
        self.play(Write(h2))
        p = np.array([-6.4, -2.4, 0]) + band_shift(2)
        s1 = scaled_tri(p, 1.0)
        s2 = scaled_tri(p + RIGHT * 2.0, 2.0)
        self.play(Create(s1), Create(s2))
        lab = Tex("3, 4, 5 and 6, 8, 10: scale factor 2").scale(0.6).move_to(p + RIGHT * 2.2 + DOWN * 0.4)
        self.play(Write(lab))
        r1 = MathTex(r"\frac{6}{3} = \frac{8}{4} = \frac{10}{5} = 2").scale(0.85).move_to(band_shift(2) + UP * 2.0 + RIGHT * 2.6)
        r2 = Tex("4, 6, 8 against 6, 9, 11: $1.5,\\ 1.5,\\ 1.375$. Not similar.").scale(0.72).move_to(band_shift(2) + UP * 1.1 + RIGHT * 2.6)
        r3 = MathTex(r"\frac{XY}{PQ} = \frac{YZ}{QR}:\quad \frac{15}{5} = \frac{YZ}{7} \Rightarrow YZ = 21").scale(0.8).move_to(band_shift(2) + UP * 0.1 + RIGHT * 2.6)
        r4 = Tex("Pole 2 m, shadow 3 m; tree shadow 12 m: tree $= 2 \\times 4 = 8$ m.").scale(0.72).move_to(band_shift(2) + DOWN * 0.9 + RIGHT * 2.6)
        for m in (r1, r2, r3, r4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(r3, color=YELLOW)))
        self.wait(4)

        # --- Band 3 (subtopic_4): problems
        self.next_band(3)
        h3 = Tex("Problems: facts, statement, deduction").scale(1.05).move_to(band_shift(3) + UP * 3.2)
        self.play(Write(h3))
        q1 = Tex("In $\\triangle ABC$ and $\\triangle DCB$: $AB = DC$ (given); $\\hat{B} = \\hat{C}$ (given); $BC$ common.").scale(0.7).move_to(band_shift(3) + UP * 2.1)
        q2 = MathTex(r"\therefore\ \triangle ABC \equiv \triangle DCB\ (SAS),\quad AC = DB").scale(0.8).move_to(band_shift(3) + UP * 1.2)
        q3 = Tex("Angles 50, 60 and 60, 70: third angles 70 and 50, so similar (AAA).").scale(0.7).move_to(band_shift(3) + UP * 0.3)
        q4 = Tex("$DE \\parallel BC$, $AD = 4$, $DB = 6$, $DE = 5$: $\\frac{AB}{AD} = \\frac{BC}{DE}$, $BC = 2.5 \\times 5 = 12.5$.").scale(0.7).move_to(band_shift(3) + DOWN * 0.6)
        q5 = Tex("5, 12, 13 and 10, 24, 26: ratios 2, 2, 2, similar and right-angled.").scale(0.7).move_to(band_shift(3) + DOWN * 1.5)
        for m in (q1, q2, q3, q4, q5):
            self.play(Write(m))
            self.wait(2.5)
        self.play(Create(SurroundingRectangle(q2, color=YELLOW)))
        self.wait(3)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        h4 = Tex("Error museum").scale(1.05).move_to(band_shift(4) + UP * 3.2)
        self.play(Write(h4))
        e1 = Tex("(SSA) as a reason").scale(0.8).move_to(band_shift(4) + UP * 1.8)
        e2 = Tex("(AAA) for congruence").scale(0.8).move_to(band_shift(4) + UP * 0.6)
        e3 = MathTex(r"\frac{\text{longest of one}}{\text{shortest of the other}}").scale(0.8).move_to(band_shift(4) + DOWN * 0.6)
        for m in (e1, e2, e3):
            self.play(Write(m))
            self.wait(1.5)
            self.play(Create(strike(m)))
            self.wait(1.5)
        fix = Tex("Three facts with reasons, letters in order, condition in brackets, then deduce.").scale(0.7).move_to(band_shift(4) + DOWN * 2.2)
        self.play(Write(fix))
        self.play(Create(SurroundingRectangle(fix, color=GREEN)))
        self.wait(5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): twins and photocopies
        self.next_band(5)
        h5 = Tex("Identical twins and photocopies").scale(1.05).move_to(band_shift(5) + UP * 3.2)
        self.play(Write(h5))
        g1 = Tex("Congruent: identical twins, one drops exactly onto the other.").scale(0.75).move_to(band_shift(5) + UP * 2.0)
        g2 = Tex("Similar: a photocopy at a different size, same angles, sides times one number.").scale(0.7).move_to(band_shift(5) + UP * 1.1)
        g3 = Tex("Letters in order tell you which sides match afterwards.").scale(0.75).move_to(band_shift(5) + UP * 0.2)
        g4 = Tex("Collect dashes, arcs, common sides and radii before deciding.").scale(0.75).move_to(band_shift(5) + DOWN * 0.7)
        for m in (g1, g2, g3, g4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(g3, color=YELLOW)))
        self.wait(5)

        # --- Band 6 (subtopic_6): four keys
        self.next_band(6)
        h6 = Tex("Four keys that lock a triangle").scale(1.05).move_to(band_shift(6) + UP * 3.2)
        self.play(Write(h6))
        keys = ["SSS: three sides, arcs cross in one place.",
                "SAS: two sides and the hinge angle between them.",
                "AAS: two angles (third is free) and one side.",
                "RHS: right angle, hypotenuse, one more side."]
        y = 2.0
        for k in keys:
            self.play(Write(Tex(k).scale(0.75).move_to(band_shift(6) + UP * y)))
            self.wait(2.2)
            y -= 0.8
        fake = Tex("Fake keys: AAA (size free) and SSA (two doors).").scale(0.78).move_to(band_shift(6) + DOWN * 1.6)
        self.play(Write(fake))
        self.play(Create(strike(fake)))
        self.wait(4)

        # --- Band 7 (subtopic_7): scale factor
        self.next_band(7)
        h7 = Tex("Scale factor: one number for every side").scale(1.05).move_to(band_shift(7) + UP * 3.2)
        self.play(Write(h7))
        pole = Line(np.array([-6.0, -2.4, 0]) + band_shift(7), np.array([-6.0, -1.2, 0]) + band_shift(7), color=YELLOW, stroke_width=5)
        shadow = Line(np.array([-6.0, -2.4, 0]) + band_shift(7), np.array([-4.2, -2.4, 0]) + band_shift(7), color=GREY, stroke_width=5)
        tree = Line(np.array([-3.4, -2.4, 0]) + band_shift(7), np.array([-3.4, 2.4, 0]) + band_shift(7), color=GREEN, stroke_width=5)
        tshadow = Line(np.array([-3.4, -2.4, 0]) + band_shift(7), np.array([3.8, -2.4, 0]) + band_shift(7), color=GREY, stroke_width=5)
        self.play(Create(pole), Create(shadow))
        self.play(Create(tree), Create(tshadow))
        self.play(Create(Line(pole.get_end(), shadow.get_end(), color=BLUE, stroke_width=2)), Create(Line(tree.get_end(), tshadow.get_end(), color=BLUE, stroke_width=2)))
        w1 = Tex("Shadow 3 to shadow 12: scale factor 4.").scale(0.78).move_to(band_shift(7) + UP * 2.2 + RIGHT * 3.0)
        w2 = MathTex(r"\text{tree} = 2 \times 4 = 8\ \text{m}").scale(0.9).move_to(band_shift(7) + UP * 1.3 + RIGHT * 3.0)
        w3 = Tex("Smallest with smallest, biggest with biggest; all three ratios agree.").scale(0.65).move_to(band_shift(7) + UP * 0.4 + RIGHT * 3.0)
        w4 = Tex("$PQ\\ 5 \\to XY\\ 15$ is times 3, so $QR\\ 7 \\to YZ\\ 21$.").scale(0.72).move_to(band_shift(7) + DOWN * 0.5 + RIGHT * 3.0)
        for m in (w1, w2, w3, w4):
            self.play(Write(m))
            self.wait(2.5)
        self.play(Create(SurroundingRectangle(w2, color=YELLOW)))
        self.wait(6)
