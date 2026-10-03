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
    """Quadrilateral from four points in order."""
    return Polygon(*pts, color=color, stroke_width=4)


def tick(p, q, color=YELLOW):
    """A short dash across the midpoint of segment pq, marking equal sides."""
    m = (p + q) / 2
    d = q - p
    n = np.array([-d[1], d[0], 0])
    n = n / np.linalg.norm(n) * 0.15
    return Line(m - n, m + n, color=color, stroke_width=3)


def diag(p, q, color=BLUE):
    return Line(p, q, color=color, stroke_width=3)


def para(origin, w=2.0, h=1.3, slant=0.6):
    o = origin
    return [o, o + RIGHT * w, o + RIGHT * (w + slant) + UP * h, o + RIGHT * slant + UP * h]


def rect(origin, w=2.0, h=1.3):
    return para(origin, w, h, 0.0)


def rhomb(origin, s=1.6):
    o = origin
    return [o + RIGHT * s, o + RIGHT * 2 * s + UP * 0.9 * s, o + RIGHT * s + UP * 1.8 * s, o + UP * 0.9 * s]


def trap(origin, w=2.4, top=1.4, h=1.3):
    o = origin
    off = (w - top) / 2
    return [o, o + RIGHT * w, o + RIGHT * (off + top) + UP * h, o + RIGHT * off + UP * h]


def kite(origin):
    o = origin
    return [o + RIGHT * 1.0, o + RIGHT * 2.0 + UP * 0.7, o + RIGHT * 1.0 + UP * 2.2, o + UP * 0.7]


class QuadrilateralsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the six definitions
        title = Tex("Six quadrilaterals, six definitions").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        base = np.array([-6.0, -2.6, 0])
        shapes = [
            quad(para(base)), quad(rect(base + RIGHT * 3.2)), quad(rhomb(base + RIGHT * 6.0, 0.9)),
        ]
        names = ["parallelogram", "rectangle", "rhombus"]
        for s, n in zip(shapes, names):
            self.play(Create(s))
            self.play(Write(Tex(n).scale(0.55).next_to(s, DOWN, buff=0.15)))
        base2 = np.array([-6.0, 0.4, 0])
        shapes2 = [quad(rect(base2, 1.4, 1.4)), quad(trap(base2 + RIGHT * 3.0)), quad(kite(base2 + RIGHT * 6.4))]
        names2 = ["square", "trapezium", "kite"]
        for s, n in zip(shapes2, names2):
            self.play(Create(s))
            self.play(Write(Tex(n).scale(0.55).next_to(s, DOWN, buff=0.15)))
        self.wait(1.5)
        d1 = Tex("Parallelogram: two pairs of opposite sides parallel.").scale(0.72).shift(UP * 2.6 + RIGHT * 1.0)
        d2 = Tex("Rectangle: a parallelogram with ONE right angle.").scale(0.72).shift(UP * 2.0 + RIGHT * 1.0)
        for m in (d1, d2):
            self.play(Write(m))
            self.wait(2.5)
        self.play(Create(SurroundingRectangle(d2, color=YELLOW)))
        self.wait(5)

        # --- Band 1 (subtopic_2): sides and angles
        self.next_band(1)
        t1 = Tex("Angles: the 360 and the parallelogram pairs").scale(1.05).move_to(band_shift(1) + UP * 3.2)
        self.play(Write(t1))
        q = quad([np.array([-6.0, -1.5, 0]), np.array([-3.0, -1.8, 0]), np.array([-2.4, 0.8, 0]), np.array([-5.4, 1.2, 0])])
        q.shift(band_shift(1))
        self.play(Create(q))
        self.play(Create(diag(q.get_vertices()[0], q.get_vertices()[2], color=YELLOW)))
        s1 = Tex("Diagonal: two triangles of $180^\\circ$, so $360^\\circ$.").scale(0.75).move_to(band_shift(1) + UP * 2.2 + RIGHT * 2.2)
        s2 = MathTex(r"90 + 85 + 110 = 285,\quad 360 - 285 = 75^\circ").scale(0.8).move_to(band_shift(1) + UP * 1.4 + RIGHT * 2.2)
        s3 = Tex("Parallelogram: opposite angles equal; consecutive add to $180^\\circ$.").scale(0.72).move_to(band_shift(1) + UP * 0.4 + RIGHT * 2.2)
        s4 = MathTex(r"x + (2x + 30) = 180 \Rightarrow 3x = 150 \Rightarrow x = 50").scale(0.8).move_to(band_shift(1) + DOWN * 0.5 + RIGHT * 2.2)
        s5 = Tex("Angles $50^\\circ,\\ 130^\\circ,\\ 50^\\circ,\\ 130^\\circ$; check sum $360^\\circ$.").scale(0.75).move_to(band_shift(1) + DOWN * 1.4 + RIGHT * 2.2)
        for m in (s1, s2, s3, s4, s5):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(s4, color=YELLOW)))
        self.wait(5)

        # --- Band 2 (subtopic_3): diagonals
        self.next_band(2)
        t2 = Tex("What the diagonals do").scale(1.05).move_to(band_shift(2) + UP * 3.2)
        self.play(Write(t2))
        o = np.array([-6.4, -0.6, 0]) + band_shift(2)
        pg = quad(para(o))
        rc = quad(rect(o + RIGHT * 3.3))
        rh = quad(rhomb(o + RIGHT * 6.4, 0.85))
        for s in (pg, rc, rh):
            self.play(Create(s))
            v = s.get_vertices()
            self.play(Create(diag(v[0], v[2])), Create(diag(v[1], v[3])))
        lab = VGroup(
            Tex("bisect each other").scale(0.5).next_to(pg, DOWN, buff=0.15),
            Tex("bisect + equal").scale(0.5).next_to(rc, DOWN, buff=0.15),
            Tex("bisect + $90^\\circ$ + halve angles").scale(0.5).next_to(rh, DOWN, buff=0.15),
        )
        self.play(Write(lab))
        self.wait(2)
        r1 = Tex("Rhombus, angle $60^\\circ$: diagonal halves it to $30^\\circ$, cross at $90^\\circ$,").scale(0.72).move_to(band_shift(2) + UP * 2.2)
        r2 = Tex("so the small triangle is $30^\\circ$, $90^\\circ$, $60^\\circ$ (sum of angles in a triangle).").scale(0.72).move_to(band_shift(2) + UP * 1.5)
        r3 = Tex("Kite: only the axis bisects the other diagonal at $90^\\circ$. Trapezium: nothing special.").scale(0.7).move_to(band_shift(2) + DOWN * 2.6)
        for m in (r1, r2, r3):
            self.play(Write(m))
            self.wait(2.6)
        self.wait(4)

        # --- Band 3 (subtopic_4): the family tree
        self.next_band(3)
        t3 = Tex("The family tree: arrows point down only").scale(1.05).move_to(band_shift(3) + UP * 3.2)
        self.play(Write(t3))
        node = lambda txt, pos: Tex(txt).scale(0.7).move_to(band_shift(3) + pos)
        n_q = node("quadrilateral", UP * 2.2)
        n_t = node("trapezium", UP * 1.0 + LEFT * 4.0)
        n_k = node("kite", UP * 1.0 + RIGHT * 4.0)
        n_p = node("parallelogram", UP * 1.0)
        n_r = node("rectangle", DOWN * 0.3 + LEFT * 2.0)
        n_h = node("rhombus", DOWN * 0.3 + RIGHT * 2.0)
        n_s = node("square", DOWN * 1.6)
        for n in (n_q, n_t, n_k, n_p, n_r, n_h, n_s):
            self.play(Write(n))
        edges = [(n_q, n_t), (n_q, n_k), (n_q, n_p), (n_p, n_r), (n_p, n_h), (n_r, n_s), (n_h, n_s)]
        for a, b in edges:
            self.play(Create(Arrow(a.get_bottom(), b.get_top(), buff=0.1, color=BLUE, stroke_width=3)), run_time=0.5)
        self.wait(2)
        f1 = Tex("Every square is a rectangle: true. Every rectangle is a square: false.").scale(0.7).move_to(band_shift(3) + DOWN * 2.5)
        self.play(Write(f1))
        self.wait(2.5)
        self.play(Create(SurroundingRectangle(n_s, color=YELLOW)))
        self.wait(4)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        t4 = Tex("Error museum").scale(1.05).move_to(band_shift(4) + UP * 3.2)
        self.play(Write(t4))
        e1 = Tex("A square is not a rectangle").scale(0.78).move_to(band_shift(4) + UP * 1.8)
        e2 = Tex("Diagonals at $90^\\circ$ in an unmarked parallelogram").scale(0.78).move_to(band_shift(4) + UP * 0.6)
        e3 = Tex("Trapezium diagonals bisect each other").scale(0.78).move_to(band_shift(4) + DOWN * 0.6)
        for m in (e1, e2, e3):
            self.play(Write(m))
            self.wait(1.5)
            self.play(Create(strike(m)))
            self.wait(1.5)
        fix = Tex("Read the marks, name the shape, shape in every reason, check with $360^\\circ$.").scale(0.72).move_to(band_shift(4) + DOWN * 2.2)
        self.play(Write(fix))
        self.play(Create(SurroundingRectangle(fix, color=GREEN)))
        self.wait(5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): the family
        self.next_band(5)
        t5 = Tex("One family, children inherit everything").scale(1.05).move_to(band_shift(5) + UP * 3.2)
        self.play(Write(t5))
        g1 = Tex("Grandparent: any four-sided shape.").scale(0.8).move_to(band_shift(5) + UP * 2.0)
        g2 = Tex("Children: trapezium (one pair parallel), kite (neighbours equal), parallelogram.").scale(0.72).move_to(band_shift(5) + UP * 1.1)
        g3 = Tex("Parallelogram's children: rectangle (right angle), rhombus (equal sides).").scale(0.72).move_to(band_shift(5) + UP * 0.2)
        g4 = Tex("Their shared child: the square. A square IS a rectangle IS a rhombus.").scale(0.72).move_to(band_shift(5) + DOWN * 0.7)
        g5 = Tex("Definition: say the least. Rectangle = parallelogram with one right angle.").scale(0.72).move_to(band_shift(5) + DOWN * 1.7)
        for m in (g1, g2, g3, g4, g5):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(g4, color=YELLOW)))
        self.wait(5)

        # --- Band 6 (subtopic_6): full turn
        self.next_band(6)
        t6 = Tex("Four corners make a full turn").scale(1.05).move_to(band_shift(6) + UP * 3.2)
        self.play(Write(t6))
        pgm = quad(para(np.array([-6.2, -1.2, 0]) + band_shift(6), 2.6, 1.8, 0.8))
        self.play(Create(pgm))
        v = pgm.get_vertices()
        angs = VGroup(
            MathTex("50^\\circ").scale(0.6).move_to(v[0] + RIGHT * 0.55 + UP * 0.3),
            MathTex("130^\\circ").scale(0.6).move_to(v[1] + LEFT * 0.6 + UP * 0.3),
            MathTex("50^\\circ").scale(0.6).move_to(v[2] + LEFT * 0.6 + DOWN * 0.3),
            MathTex("130^\\circ").scale(0.6).move_to(v[3] + RIGHT * 0.6 + DOWN * 0.3),
        )
        self.play(Write(angs))
        h1 = Tex("Two triangles of a half-turn: $360^\\circ$ in total.").scale(0.75).move_to(band_shift(6) + UP * 2.0 + RIGHT * 2.4)
        h2 = Tex("Opposite corners: twins. Neighbours: a couple adding to $180^\\circ$.").scale(0.72).move_to(band_shift(6) + UP * 1.1 + RIGHT * 2.4)
        h3 = MathTex(r"50 + 130 + 50 + 130 = 360").scale(0.8).move_to(band_shift(6) + UP * 0.2 + RIGHT * 2.4)
        h4 = Tex("Trapezium: one C couple per slanted side. Kite: one pair of equal corners.").scale(0.68).move_to(band_shift(6) + DOWN * 2.6)
        for m in (h1, h2, h3, h4):
            self.play(Write(m))
            self.wait(2.6)
        self.wait(4)

        # --- Band 7 (subtopic_7): two sticks
        self.next_band(7)
        t7 = Tex("Two sticks: the diagonal table").scale(1.05).move_to(band_shift(7) + UP * 3.2)
        self.play(Write(t7))
        rows = [
            ("Halve each other", "parallelogram and all its descendants"),
            ("Equal", "rectangle, square"),
            ("Cross at $90^\\circ$", "rhombus, square, kite's middle stick"),
            ("Halve the corners", "rhombus, square, kite's middle stick at its ends"),
        ]
        y = 2.0
        for a, b in rows:
            la = Tex(a).scale(0.75).move_to(band_shift(7) + UP * y + LEFT * 4.0)
            lb = Tex(b).scale(0.7).move_to(band_shift(7) + UP * y + RIGHT * 1.6)
            self.play(Write(la), Write(lb))
            self.wait(2.4)
            y -= 0.9
        rh2 = quad(rhomb(np.array([-6.0, -3.2, 0]) + band_shift(7), 0.8))
        self.play(Create(rh2))
        vv = rh2.get_vertices()
        self.play(Create(diag(vv[0], vv[2])), Create(diag(vv[1], vv[3])))
        last = Tex("Rhombus with a $60^\\circ$ corner: little triangle $30^\\circ$, $90^\\circ$, $60^\\circ$.").scale(0.72).move_to(band_shift(7) + DOWN * 2.3 + RIGHT * 1.5)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(6)
