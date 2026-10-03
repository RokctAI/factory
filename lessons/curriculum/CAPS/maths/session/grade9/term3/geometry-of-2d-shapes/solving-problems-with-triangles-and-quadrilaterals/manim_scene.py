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


def quad(pts, color=WHITE):
    return Polygon(*pts, color=color, stroke_width=4)


def seg(p, q, color=BLUE):
    return Line(p, q, color=color, stroke_width=3)


def kite(origin):
    o = origin
    return [o + UP * 2.4, o + RIGHT * 1.2 + UP * 1.5, o, o + LEFT * 1.2 + UP * 1.5]


def rhomb(origin, s=1.5):
    o = origin
    return [o, o + RIGHT * s * 1.6, o + RIGHT * s * 1.6 + RIGHT * s * 0.55 + UP * s * 1.5, o + RIGHT * s * 0.55 + UP * s * 1.5]


def rect(origin, w, h):
    o = origin
    return [o, o + RIGHT * w, o + RIGHT * w + UP * h, o + UP * h]


class TriQuadProblemsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): angle chasing
        title = Tex("Angle chasing: name the shape, then the property").scale(1.05).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        k = quad(kite(np.array([-5.0, -2.6, 0])))
        self.play(Create(k))
        kv = k.get_vertices()
        self.play(Write(MathTex("50^\\circ").scale(0.55).move_to(kv[0] + DOWN * 0.45)), Write(MathTex("110^\\circ").scale(0.55).move_to(kv[2] + UP * 0.4)))
        self.play(Write(MathTex("x").scale(0.6).move_to(kv[1] + LEFT * 0.3)), Write(MathTex("x").scale(0.6).move_to(kv[3] + RIGHT * 0.3)))
        a1 = MathTex(r"50 + 110 + x + x = 360 \Rightarrow x = 100").scale(0.8).shift(UP * 2.0 + RIGHT * 2.2)
        a2 = Tex("Rhombus, $\\hat{B} = 70^\\circ$: $\\hat{A} = 110^\\circ$ (co-int), diagonal halves it: $55^\\circ$.").scale(0.68).shift(UP * 1.1 + RIGHT * 2.2)
        a3 = Tex("Trapezium: $115 + x = 180$ (co-int), $x = 65$; $\\hat{B} = 140^\\circ$, $\\hat{C} = 40^\\circ$.").scale(0.68).shift(UP * 0.2 + RIGHT * 2.2)
        a4 = MathTex(r"(3x - 20) + (x + 40) = 180 \Rightarrow x = 40:\ 100^\circ,\ 80^\circ").scale(0.75).shift(DOWN * 0.7 + RIGHT * 2.2)
        for m in (a1, a2, a3, a4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(a1, color=YELLOW)))
        self.wait(4)

        # --- Band 1 (subtopic_2): triangles inside
        self.next_band(1)
        h1 = Tex("Triangles inside quadrilaterals").scale(1.05).move_to(band_shift(1) + UP * 3.2)
        self.play(Write(h1))
        r = quad(rect(np.array([-6.4, -2.4, 0]) + band_shift(1), 4.0, 2.4))
        self.play(Create(r))
        rv = r.get_vertices()
        e = (rv[2] + rv[3]) / 2
        self.play(Create(seg(e, rv[0])), Create(seg(e, rv[1])))
        self.play(Write(Tex("E").scale(0.6).move_to(e + UP * 0.3)))
        b1 = Tex("$AE = EB$ (midpoint); $\\hat{A} = \\hat{B} = 90^\\circ$; $AD = BC$ (opp sides of rectangle)").scale(0.65).move_to(band_shift(1) + UP * 2.2 + RIGHT * 2.0)
        b2 = MathTex(r"\triangle AED \equiv \triangle BEC\ (SAS) \Rightarrow ED = EC").scale(0.8).move_to(band_shift(1) + UP * 1.3 + RIGHT * 2.0)
        b3 = Tex("$\\hat{ADE} = 32^\\circ$: $\\hat{AED} = 58^\\circ$, $\\hat{BEC} = 58^\\circ$, $\\hat{DEC} = 64^\\circ$.").scale(0.7).move_to(band_shift(1) + UP * 0.4 + RIGHT * 2.0)
        b4 = Tex("Isosceles, exterior $124^\\circ$ at C: $\\hat{C} = 56$, $\\hat{B} = 56$, $\\hat{A} = 68$. Check $68 + 56 = 124$.").scale(0.65).move_to(band_shift(1) + DOWN * 0.5 + RIGHT * 2.0)
        for m in (b1, b2, b3, b4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(b2, color=YELLOW)))
        self.wait(4)

        # --- Band 2 (subtopic_3): sides
        self.next_band(2)
        h2 = Tex("Unknown sides: properties, congruence, similarity").scale(1.05).move_to(band_shift(2) + UP * 3.2)
        self.play(Write(h2))
        A = np.array([-5.0, 2.0, 0]) + band_shift(2)
        B = np.array([-6.6, -2.0, 0]) + band_shift(2)
        C = np.array([-2.6, -2.0, 0]) + band_shift(2)
        big = Polygon(A, B, C, color=WHITE, stroke_width=4)
        self.play(Create(big))
        D = A + (B - A) * 3 / 8
        E = A + (C - A) * 3 / 8
        self.play(Create(seg(D, E, color=YELLOW)))
        self.play(Write(Tex("3").scale(0.55).move_to((A + D) / 2 + LEFT * 0.3)), Write(Tex("5").scale(0.55).move_to((D + B) / 2 + LEFT * 0.3)), Write(Tex("4.5").scale(0.55).move_to((D + E) / 2 + UP * 0.25)))
        s1 = Tex("$\\hat{A}$ common; $\\hat{ADE} = \\hat{ABC}$ (corresp, $DE \\parallel BC$): $\\triangle ADE \\mid\\mid\\mid \\triangle ABC$ (AAA)").scale(0.62).move_to(band_shift(2) + UP * 2.2 + RIGHT * 2.6)
        s2 = MathTex(r"\frac{BC}{DE} = \frac{AB}{AD} = \frac{8}{3} \Rightarrow BC = 4.5 \times \frac{8}{3} = 12").scale(0.8).move_to(band_shift(2) + UP * 1.2 + RIGHT * 2.6)
        s3 = MathTex(r"2x + 1 = 3x - 4 \Rightarrow x = 5\ \text{(opp sides of a parallelogram)}").scale(0.72).move_to(band_shift(2) + UP * 0.2 + RIGHT * 2.6)
        s4 = Tex("Rectangle $AO = 6.5 \\Rightarrow BD = 13$. Rhombus side 7: perimeter 28.").scale(0.7).move_to(band_shift(2) + DOWN * 0.7 + RIGHT * 2.6)
        s5 = Tex("Shadows: $15 \\div 1.2 = 12.5$, building $1.8 \\times 12.5 = 22.5$ m.").scale(0.7).move_to(band_shift(2) + DOWN * 1.6 + RIGHT * 2.6)
        for m in (s1, s2, s3, s4, s5):
            self.play(Write(m))
            self.wait(2.5)
        self.play(Create(SurroundingRectangle(s2, color=YELLOW)))
        self.wait(3)

        # --- Band 3 (subtopic_4): multi-step
        self.next_band(3)
        h3 = Tex("Multi-step: collect, name, chain, check").scale(1.05).move_to(band_shift(3) + UP * 3.2)
        self.play(Write(h3))
        rh = quad(rhomb(np.array([-6.6, -2.0, 0]) + band_shift(3), 1.6))
        self.play(Create(rh))
        hv = rh.get_vertices()
        self.play(Create(seg(hv[0], hv[2])), Create(seg(hv[1], hv[3])))
        c1 = Tex("Rhombus, $\\hat{D} = 100^\\circ$. $\\hat{A} = 80^\\circ$ (consecutive angles of a rhombus)").scale(0.68).move_to(band_shift(3) + UP * 2.2 + RIGHT * 2.2)
        c2 = Tex("$\\hat{OAB} = 40^\\circ$ (diagonals of a rhombus bisect the angles)").scale(0.68).move_to(band_shift(3) + UP * 1.4 + RIGHT * 2.2)
        c3 = Tex("$\\hat{AOB} = 90^\\circ$ (diagonals of a rhombus are perpendicular)").scale(0.68).move_to(band_shift(3) + UP * 0.6 + RIGHT * 2.2)
        c4 = Tex("$\\hat{ABO} = 50^\\circ$ (sum of angles in $\\triangle AOB$). Check: half of $\\hat{B} = 100^\\circ$.").scale(0.68).move_to(band_shift(3) + DOWN * 0.2 + RIGHT * 2.2)
        c5 = Tex("Isosceles trapezium, $\\hat{P} = 70$: $\\hat{Q} = 70$, $\\hat{S} = \\hat{R} = 110$; $\\triangle PSR$: $30 + 110 + 40$.").scale(0.65).move_to(band_shift(3) + DOWN * 1.2 + RIGHT * 2.2)
        for m in (c1, c2, c3, c4, c5):
            self.play(Write(m))
            self.wait(2.5)
        self.play(Create(SurroundingRectangle(c4, color=YELLOW)))
        self.wait(3)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        h4 = Tex("Error museum").scale(1.05).move_to(band_shift(4) + UP * 3.2)
        self.play(Write(h4))
        e1 = Tex("Rectangle diagonal makes $45^\\circ$").scale(0.8).move_to(band_shift(4) + UP * 1.8)
        e2 = Tex("Kite: consecutive angles add to $180^\\circ$").scale(0.8).move_to(band_shift(4) + UP * 0.6)
        e3 = Tex("Correct numbers, no reasons").scale(0.8).move_to(band_shift(4) + DOWN * 0.6)
        for m in (e1, e2, e3):
            self.play(Write(m))
            self.wait(1.5)
            self.play(Create(strike(m)))
            self.wait(1.5)
        fix = Tex("Collect the marks, name the shape, one reason per line, check the sum.").scale(0.72).move_to(band_shift(4) + DOWN * 2.2)
        self.play(Write(fix))
        self.play(Create(SurroundingRectangle(fix, color=GREEN)))
        self.wait(5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): the routine
        self.next_band(5)
        h5 = Tex("Collect, name, chain, check").scale(1.05).move_to(band_shift(5) + UP * 3.2)
        self.play(Write(h5))
        g1 = Tex("Collect: dashes, arcs, arrowheads, tiny squares, the question's words.").scale(0.72).move_to(band_shift(5) + UP * 2.0)
        g2 = Tex("Name: the rules live in the shape's name.").scale(0.78).move_to(band_shift(5) + UP * 1.1)
        g3 = Tex("Chain: one fact per line, rule in brackets.").scale(0.78).move_to(band_shift(5) + UP * 0.2)
        g4 = Tex("Check: add to 360 or 180. If it fails, re-read the name.").scale(0.75).move_to(band_shift(5) + DOWN * 0.7)
        g5 = MathTex(r"\text{Kite: } 50 + 110 + 2x = 360,\ x = 100").scale(0.8).move_to(band_shift(5) + DOWN * 1.7)
        for m in (g1, g2, g3, g4, g5):
            self.play(Write(m))
            self.wait(2.5)
        self.play(Create(SurroundingRectangle(g2, color=YELLOW)))
        self.wait(4)

        # --- Band 6 (subtopic_6): hidden shapes
        self.next_band(6)
        h6 = Tex("Shapes hiding inside shapes").scale(1.05).move_to(band_shift(6) + UP * 3.2)
        self.play(Write(h6))
        sq = quad(rect(np.array([-6.2, -1.6, 0]) + band_shift(6), 2.4, 2.4))
        self.play(Create(sq))
        sv = sq.get_vertices()
        self.play(Create(seg(sv[0], sv[2], color=YELLOW)))
        self.play(Write(MathTex("45^\\circ").scale(0.55).move_to(sv[0] + RIGHT * 0.7 + UP * 0.3)))
        d1 = Tex("Midpoint twins in a rectangle: SAS, so the two slanted lines are equal.").scale(0.7).move_to(band_shift(6) + UP * 2.0 + RIGHT * 2.4)
        d2 = Tex("Roof with the ramp: outside 124, inside 56, roof rule 56, top 68.").scale(0.7).move_to(band_shift(6) + UP * 1.1 + RIGHT * 2.4)
        d3 = Tex("Square's diagonal halves the corner: 45, 45, 90. A rectangle's does NOT.").scale(0.7).move_to(band_shift(6) + UP * 0.2 + RIGHT * 2.4)
        d4 = Tex("Parallelogram diagonal: Z rule moves 35 across, triangle gives 65, corner 100.").scale(0.68).move_to(band_shift(6) + DOWN * 0.7 + RIGHT * 2.4)
        for m in (d1, d2, d3, d4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(d3, color=YELLOW)))
        self.wait(4)

        # --- Band 7 (subtopic_7): letters
        self.next_band(7)
        h7 = Tex("Letters for angles and sides").scale(1.05).move_to(band_shift(7) + UP * 3.2)
        self.play(Write(h7))
        l1 = MathTex(r"2x + 1 = 3x - 4 \Rightarrow x = 5,\ AB = 11").scale(0.85).move_to(band_shift(7) + UP * 2.0)
        l2 = MathTex(r"\text{photocopy: } BC = 4.5 \times \frac{8}{3} = 12").scale(0.85).move_to(band_shift(7) + UP * 1.0)
        l3 = MathTex(r"\text{shadows: } 1.8 \times 12.5 = 22.5\ \text{m}").scale(0.85).move_to(band_shift(7) + UP * 0.0)
        l4 = Tex("Rhombus chain: 100, 80, 40, 90, 50. Check: half of 100 is 50.").scale(0.75).move_to(band_shift(7) + DOWN * 1.0)
        l5 = Tex("Collect, name, chain, check.").scale(0.85).move_to(band_shift(7) + DOWN * 2.2)
        for m in (l1, l2, l3, l4, l5):
            self.play(Write(m))
            self.wait(2.5)
        self.play(Create(SurroundingRectangle(l5, color=YELLOW)))
        self.wait(6)
