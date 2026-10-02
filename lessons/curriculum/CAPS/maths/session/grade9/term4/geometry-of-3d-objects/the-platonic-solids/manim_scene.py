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
# the allowed primitive vocabulary. Solids are drawn as line-segment wireframes
# (hidden edges dashed) so every stroke exports as a plain line. Bands cover
# all seven subtopics of the duo (Part 1 — Expert: subtopics 1-4; Part 2 —
# Simplifier: subtopics 5-7), with dwell time proportional to subtopics.json
# (220/230/230/230/190/190/180 of 1470 s).

BAND = config.frame_height

# (name, face, F, faces per vertex, V, E)
SOLIDS = [
    ("Tetrahedron", "triangle", 4, 3, 4, 6),
    ("Cube", "square", 6, 3, 8, 12),
    ("Octahedron", "triangle", 8, 4, 6, 12),
    ("Dodecahedron", "pentagon", 12, 3, 20, 30),
    ("Icosahedron", "triangle", 20, 5, 12, 30),
]


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


def wire(points, edges, hidden=(), color=WHITE):
    """Wireframe from 2D points and index pairs; hidden edges are dashed."""
    g = VGroup()
    for k, (a, b) in enumerate(edges):
        seg = Line(points[a], points[b], color=color, stroke_width=3)
        if k in hidden:
            seg = DashedLine(points[a], points[b], color=GREY, stroke_width=2)
        g.add(seg)
    return g


def cube(origin, s=1.3, d=0.55):
    p = [origin + v for v in (
        np.array([0, 0, 0]), np.array([s, 0, 0]), np.array([s, s, 0]), np.array([0, s, 0]),
        np.array([d, d, 0]), np.array([s + d, d, 0]), np.array([s + d, s + d, 0]), np.array([d, s + d, 0]))]
    e = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]
    return wire(p, e, hidden={4, 7, 8})


def tetrahedron(origin, s=1.6):
    p = [origin + v for v in (np.array([0, 0, 0]), np.array([s, 0, 0]),
                              np.array([0.62 * s, 0.35 * s, 0]), np.array([0.45 * s, 0.95 * s, 0]))]
    e = [(0, 1), (1, 3), (3, 0), (0, 2), (1, 2), (2, 3)]
    return wire(p, e, hidden={3, 4, 5})


def octahedron(origin, s=0.9):
    p = [origin + v for v in (np.array([0, s * 1.2, 0]), np.array([0, -s * 1.2, 0]),
                              np.array([-s, 0, 0]), np.array([s, 0, 0]),
                              np.array([0.35 * s, 0.3 * s, 0]), np.array([-0.35 * s, -0.3 * s, 0]))]
    e = [(0, 2), (0, 3), (0, 5), (1, 2), (1, 3), (1, 5), (2, 5), (3, 5), (0, 4), (1, 4), (2, 4), (3, 4)]
    return wire(p, e, hidden={8, 9, 10, 11})


def fan(centre, n_faces, angle_deg, r=1.1, color=BLUE):
    """n_faces polygon corners of angle_deg laid round a point, as rays."""
    g = VGroup()
    a = 0.0
    for k in range(n_faces + 1):
        th = np.radians(a)
        g.add(Line(centre, centre + r * np.array([np.cos(th), np.sin(th), 0]), color=color, stroke_width=3))
        a += angle_deg
    g.add(Dot(centre, color=YELLOW))
    return g


class PlatonicSolidsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): faces, edges, vertices
        title = Tex("Polyhedra: faces, edges, vertices").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        cb = cube(np.array([-5.8, 0.2, 0]))
        self.play(Create(cb), run_time=2)
        cb_lab = Tex("Cube: F 6, V 8, E 12").scale(0.6).move_to(np.array([-4.9, -0.6, 0]))
        self.play(Write(cb_lab))
        l1 = Tex("Triangular prism: F 5, V 6, E 9").scale(0.75).shift(RIGHT * 2.0 + UP * 1.6)
        l2 = Tex("Square pyramid: F 5, V 5, E 8").scale(0.75).shift(RIGHT * 2.0 + UP * 0.8)
        l3 = Tex("Prism on an n-gon: n + 2 faces, 2n vertices, 3n edges").scale(0.7).shift(RIGHT * 1.6 + UP * 0.0)
        l4 = Tex("Pyramid on an n-gon: n + 1 faces, n + 1 vertices, 2n edges").scale(0.7).shift(RIGHT * 1.6 + DOWN * 0.8)
        l5 = Tex("Count by structure, never by pointing at a picture").scale(0.75).shift(DOWN * 2.2)
        for m in (l1, l2, l3, l4, l5):
            self.play(Write(m))
            self.wait(2.1)
        self.play(Create(SurroundingRectangle(l5, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): the five solids
        self.next_band(1)
        b1_title = Tex("The five Platonic solids").scale(1.2).shift(band_shift(1) + UP * 3.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        cond = Tex("Same regular polygon faces; same number of faces at every vertex").scale(0.7).shift(band_shift(1) + UP * 2.4)
        self.play(Write(cond))
        self.wait(2)
        tet = tetrahedron(band_shift(1) + LEFT * 6.4 + UP * 0.3)
        cub = cube(band_shift(1) + LEFT * 3.9 + UP * 0.3, s=1.1, d=0.45)
        octa = octahedron(band_shift(1) + LEFT * 0.6 + UP * 1.0)
        self.play(Create(tet), Create(cub), Create(octa), run_time=2.5)
        header = Tex("Name \\quad Face \\quad F \\quad at vertex \\quad V \\quad E").scale(0.6).shift(band_shift(1) + RIGHT * 3.9 + UP * 1.4)
        self.play(Write(header))
        for i, (n, f, F, m, V, E) in enumerate(SOLIDS):
            row = Tex(f"{n} \\quad {f} \\quad {F} \\quad {m} \\quad {V} \\quad {E}").scale(0.6)
            row.shift(band_shift(1) + RIGHT * 3.9 + UP * (0.8 - 0.55 * i))
            self.play(Write(row))
            self.wait(1.8)
        dual = Tex("Duals: cube and octahedron swap 6 and 8; dodecahedron and icosahedron swap 12 and 20").scale(0.62).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(dual))
        self.play(Create(SurroundingRectangle(dual, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Euler and counting from faces
        self.next_band(2)
        b2_title = Tex("Euler: V $-$ E + F = 2").scale(1.2).shift(band_shift(2) + UP * 2.9)
        self.play(Write(b2_title))
        self.wait(1.5)
        eu = [
            r"4 - 6 + 4 = 2 \qquad 8 - 12 + 6 = 2 \qquad 6 - 12 + 8 = 2",
            r"20 - 30 + 12 = 2 \qquad 12 - 30 + 20 = 2",
            r"E = \frac{\text{faces} \times \text{sides}}{2}: \quad \frac{12 \times 5}{2} = 30",
            r"V = \frac{\text{faces} \times \text{corners}}{\text{faces at a vertex}}: \quad \frac{20 \times 3}{5} = 12",
        ]
        for i, r in enumerate(eu):
            m = MathTex(r).scale(0.85).shift(band_shift(2) + UP * (1.7 - 1.0 * i))
            self.play(Write(m))
            self.wait(2.6)
        miss = Tex("V = 10, E = 15, so F = 2 $-$ 10 + 15 = 7").scale(0.8).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(miss))
        self.play(Create(SurroundingRectangle(miss, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): why only five
        self.next_band(3)
        b3_title = Tex("Why only five: angles at one vertex").scale(1.1).shift(band_shift(3) + UP * 3.1)
        self.play(Write(b3_title))
        self.wait(1.5)
        fans = [
            (3, 60, "3 triangles: 180", LEFT * 5.4),
            (4, 60, "4 triangles: 240", LEFT * 2.7),
            (5, 60, "5 triangles: 300", ORIGIN),
            (3, 90, "3 squares: 270", RIGHT * 2.7),
            (3, 108, "3 pentagons: 324", RIGHT * 5.4),
        ]
        for n, ang, lab, x in fans:
            f = fan(band_shift(3) + x + UP * 1.0, n, ang, r=0.9)
            t = Tex(lab).scale(0.5).move_to(band_shift(3) + x + DOWN * 0.3)
            self.play(Create(f), Write(t), run_time=1.4)
            self.wait(1.2)
        flat = Tex("6 triangles, 4 squares, 3 hexagons: exactly 360, flat").scale(0.75).shift(band_shift(3) + DOWN * 1.4)
        over = Tex("4 pentagons: 432, too much. Nothing else fits.").scale(0.75).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(flat))
        self.wait(2.4)
        self.play(Write(over))
        self.play(Create(SurroundingRectangle(over, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        e1 = Tex("Triangular bipyramid is Platonic (3 and 4 faces at vertices)").scale(0.75).shift(band_shift(4) + UP * 1.5)
        e2 = Tex("Cube from a drawing: 3 faces, 7 vertices").scale(0.75).shift(band_shift(4) + UP * 0.6)
        e3 = Tex("Cube: 8 faces and 6 vertices").scale(0.75).shift(band_shift(4) + DOWN * 0.3)
        e4 = Tex("Dodecahedron: 12 times 5, so 60 edges").scale(0.75).shift(band_shift(4) + DOWN * 1.2)
        e5 = Tex("Soccer ball is an icosahedron").scale(0.75).shift(band_shift(4) + DOWN * 2.1)
        for m in (e1, e2, e3, e4, e5):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.6)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): flat sides, folds, corners
        self.next_band(5)
        b5_title = Tex("Flat sides, folds and corners").scale(1.2).shift(band_shift(5) + UP * 2.6)
        self.play(Write(b5_title))
        self.wait(2)
        box = cube(band_shift(5) + LEFT * 6.0 + DOWN * 0.6, s=1.4, d=0.6)
        self.play(Create(box), run_time=2)
        s1 = Tex("Box: 6 faces, 12 edges, 8 corners").scale(0.8).shift(band_shift(5) + RIGHT * 1.6 + UP * 1.3)
        s2 = Tex("Triangular box: 5 faces, 9 edges, 6 corners").scale(0.8).shift(band_shift(5) + RIGHT * 1.6 + UP * 0.4)
        s3 = Tex("Corners take away edges add faces: always 2").scale(0.8).shift(band_shift(5) + RIGHT * 1.6 + DOWN * 0.5)
        s4 = Tex("8 $-$ 12 + 6 = 2").scale(0.9).shift(band_shift(5) + RIGHT * 1.6 + DOWN * 1.4)
        for m in (s1, s2, s3, s4):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(s3, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): five fair dice
        self.next_band(6)
        b6_title = Tex("Five fair dice").scale(1.2).shift(band_shift(6) + UP * 2.6)
        self.play(Write(b6_title))
        self.wait(2)
        dice = [
            "4-sided: tetrahedron, 4 triangles",
            "6-sided: cube, 6 squares",
            "8-sided: octahedron, 8 triangles",
            "12-sided: dodecahedron, 12 pentagons",
            "20-sided: icosahedron, 20 triangles",
        ]
        for i, d in enumerate(dice):
            m = Tex(d).scale(0.8).shift(band_shift(6) + UP * (1.6 - 0.7 * i))
            self.play(Write(m))
            self.wait(1.8)
        half = Tex("Edges: all the sides, halved. 20 times 3 is 60, so 30 edges.").scale(0.8).shift(band_shift(6) + DOWN * 2.3)
        self.play(Write(half))
        self.play(Create(SurroundingRectangle(half, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): why only five fit
        self.next_band(7)
        b7_title = Tex("Why only five fit").scale(1.2).shift(band_shift(7) + UP * 2.6)
        self.play(Write(b7_title))
        self.wait(2)
        six = fan(band_shift(7) + LEFT * 4.5 + UP * 0.6, 6, 60, r=1.0, color=GREY)
        five = fan(band_shift(7) + LEFT * 1.5 + UP * 0.6, 5, 60, r=1.0)
        self.play(Create(six), Create(five), run_time=2)
        t6 = Tex("Six triangles: 360, flat").scale(0.6).move_to(band_shift(7) + LEFT * 4.5 + DOWN * 0.8)
        t5 = Tex("Five: 300, a corner").scale(0.6).move_to(band_shift(7) + LEFT * 1.5 + DOWN * 0.8)
        self.play(Write(t6), Write(t5))
        w1 = Tex("Less than 360: a corner").scale(0.8).shift(band_shift(7) + RIGHT * 3.6 + UP * 1.2)
        w2 = Tex("Exactly 360: flat").scale(0.8).shift(band_shift(7) + RIGHT * 3.6 + UP * 0.4)
        w3 = Tex("More than 360: will not fit").scale(0.8).shift(band_shift(7) + RIGHT * 3.6 + DOWN * 0.4)
        for m in (w1, w2, w3):
            self.play(Write(m))
            self.wait(2.0)
        w4 = Tex("Count, check with 2, halve the sides, fit the corner.").scale(0.85).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(w4))
        self.play(Create(SurroundingRectangle(w4, color=YELLOW)))
        self.wait(4)
