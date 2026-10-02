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


def diag(p, q, color=BLUE):
    return Line(p, q, color=color, stroke_width=3)


def rect(origin, w, h):
    o = origin
    return [o, o + RIGHT * w, o + RIGHT * w + UP * h, o + UP * h]


def rhomb(origin, s):
    o = origin
    return [o + RIGHT * s, o + RIGHT * 2 * s + UP * 0.9 * s, o + RIGHT * s + UP * 1.8 * s, o + UP * 0.9 * s]


def regular(n, centre, r):
    """Vertices of a regular n-gon."""
    return [centre + r * np.array([np.cos(2 * np.pi * k / n + np.pi / 2), np.sin(2 * np.pi * k / n + np.pi / 2), 0]) for k in range(n)]


def fan(pts, color=YELLOW):
    """Diagonals from vertex 0 to every non-adjacent vertex."""
    return VGroup(*[Line(pts[0], pts[k], color=color, stroke_width=3) for k in range(2, len(pts) - 1)])


class DiagonalsPolygonsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): construct and measure
        title = Tex("Investigate by construction: the diagonals").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        r = quad(rect(np.array([-6.2, -1.6, 0]), 3.2, 2.4))
        self.play(Create(r))
        v = r.get_vertices()
        self.play(Create(diag(v[0], v[2])), Create(diag(v[1], v[3])))
        o_lab = Tex("O").scale(0.6).move_to((v[0] + v[2]) / 2 + UP * 0.25)
        self.play(Write(o_lab))
        m1 = Tex("Rectangle $8 \\times 6$: diagonals both 10, pieces all 5.").scale(0.75).shift(UP * 2.0 + RIGHT * 2.4)
        m2 = Tex("Protractor at O: not $90^\\circ$. Equal, bisect, not perpendicular.").scale(0.72).shift(UP * 1.2 + RIGHT * 2.4)
        m3 = Tex("Square: equal, bisect, $90^\\circ$, halves corners into $45^\\circ$.").scale(0.72).shift(UP * 0.3 + RIGHT * 2.4)
        m4 = Tex("Parallelogram: bisect only. Rhombus: bisect, $90^\\circ$, halve angles.").scale(0.7).shift(DOWN * 0.6 + RIGHT * 2.4)
        m5 = Tex("Kite: the axis is the perpendicular bisector of the other diagonal.").scale(0.7).shift(DOWN * 1.5 + RIGHT * 2.4)
        for m in (m1, m2, m3, m4, m5):
            self.play(Write(m))
            self.wait(2.4)
        self.wait(4)

        # --- Band 1 (subtopic_2): the table and reasons
        self.next_band(1)
        t1 = Tex("The table, forwards and backwards").scale(1.05).move_to(band_shift(1) + UP * 3.2)
        self.play(Write(t1))
        head = Tex("shape \\quad bisect \\quad equal \\quad $90^\\circ$ \\quad halve angles").scale(0.7).move_to(band_shift(1) + UP * 2.3)
        self.play(Write(head))
        rows = [
            "parallelogram \\quad yes \\quad no \\quad no \\quad no",
            "rectangle \\quad yes \\quad yes \\quad no \\quad no",
            "rhombus \\quad yes \\quad no \\quad yes \\quad yes",
            "square \\quad yes \\quad yes \\quad yes \\quad yes",
            "kite \\quad axis only \\quad no \\quad yes \\quad axis ends",
        ]
        y = 1.6
        for rtext in rows:
            self.play(Write(Tex(rtext).scale(0.65).move_to(band_shift(1) + UP * y)))
            self.wait(1.2)
            y -= 0.6
        b1 = Tex("Backwards: diagonals bisect each other $\\Rightarrow$ parallelogram.").scale(0.72).move_to(band_shift(1) + DOWN * 1.6)
        b2 = Tex("Rectangle, $AC$ at $35^\\circ$ to $AB$: $AO = BO$, so $35^\\circ, 35^\\circ, 110^\\circ$.").scale(0.72).move_to(band_shift(1) + DOWN * 2.4)
        for m in (b1, b2):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(b2, color=YELLOW)))
        self.wait(4)

        # --- Band 2 (subtopic_3): polygon angle sum
        self.next_band(2)
        t2 = Tex("Interior angle sum: $(n-2) \\times 180^\\circ$").scale(1.05).move_to(band_shift(2) + UP * 3.2)
        self.play(Write(t2))
        pent = regular(5, np.array([-4.8, -0.4, 0]) + band_shift(2), 1.5)
        hexa = regular(6, np.array([-1.0, -0.4, 0]) + band_shift(2), 1.5)
        for pts, n in ((pent, "3 triangles: 540"), (hexa, "4 triangles: 720")):
            self.play(Create(quad(pts)))
            self.play(Create(fan(pts)))
            self.play(Write(Tex(n).scale(0.6).move_to(pts[0] + DOWN * 3.4)))
        s1 = Tex("Regular: each angle is the sum over $n$.").scale(0.72).move_to(band_shift(2) + UP * 2.0 + RIGHT * 3.6)
        s2 = Tex("Pentagon 108, hexagon 120, octagon 135.").scale(0.72).move_to(band_shift(2) + UP * 1.2 + RIGHT * 3.6)
        s3 = Tex("Exterior angles always add to $360^\\circ$.").scale(0.72).move_to(band_shift(2) + UP * 0.4 + RIGHT * 3.6)
        s4 = MathTex(r"150^\circ \Rightarrow \text{ext } 30^\circ \Rightarrow n = 360 \div 30 = 12").scale(0.7).move_to(band_shift(2) + DOWN * 0.5 + RIGHT * 3.6)
        for m in (s1, s2, s3, s4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(s4, color=YELLOW)))
        self.wait(4)

        # --- Band 3 (subtopic_4): problems
        self.next_band(3)
        t3 = Tex("Problems: layout for marks").scale(1.05).move_to(band_shift(3) + UP * 3.2)
        self.play(Write(t3))
        p1 = Tex("Pentagon: sum 540. $100 + 110 + 120 + 130 = 460$, fifth angle $80^\\circ$.").scale(0.72).move_to(band_shift(3) + UP * 2.0)
        p2 = MathTex(r"x + (x+10) + (x+20) + (x+30) + (x+40) = 5x + 100 = 540").scale(0.75).move_to(band_shift(3) + UP * 1.1)
        p3 = Tex("$x = 88$: angles 88, 98, 108, 118, 128. Check: 540.").scale(0.75).move_to(band_shift(3) + UP * 0.3)
        p4 = Tex("Exterior $24^\\circ$: $n = 15$, interior $156^\\circ$.").scale(0.75).move_to(band_shift(3) + DOWN * 0.6)
        p5 = Tex("Parallelogram, diagonals bisect: $3x - 1 = x + 7$, $x = 4$, $PR = 22$.").scale(0.72).move_to(band_shift(3) + DOWN * 1.5)
        for m in (p1, p2, p3, p4, p5):
            self.play(Write(m))
            self.wait(2.5)
        self.play(Create(SurroundingRectangle(p3, color=YELLOW)))
        self.wait(3)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        t4 = Tex("Error museum").scale(1.05).move_to(band_shift(4) + UP * 3.2)
        self.play(Write(t4))
        e1 = MathTex(r"\text{hexagon: } 6 \times 180 = 1080").scale(0.8).move_to(band_shift(4) + UP * 1.8)
        e2 = Tex("Dividing by $n$ without the word regular").scale(0.78).move_to(band_shift(4) + UP * 0.6)
        e3 = Tex("Equal diagonals used in a parallelogram").scale(0.78).move_to(band_shift(4) + DOWN * 0.6)
        for m in (e1, e2, e3):
            self.play(Write(m))
            self.wait(1.5)
            self.play(Create(strike(m)))
            self.wait(1.5)
        fix = Tex("One vertex, $n - 2$ triangles, name the shape, check the sum.").scale(0.75).move_to(band_shift(4) + DOWN * 2.2)
        self.play(Write(fix))
        self.play(Create(SurroundingRectangle(fix, color=GREEN)))
        self.wait(5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): measure the sticks
        self.next_band(5)
        t5 = Tex("Draw it, measure it, believe it").scale(1.05).move_to(band_shift(5) + UP * 3.2)
        self.play(Write(t5))
        rr = quad(rect(np.array([-6.2, -1.4, 0]) + band_shift(5), 3.2, 2.4))
        self.play(Create(rr))
        vv = rr.get_vertices()
        self.play(Create(diag(vv[0], vv[2])), Create(diag(vv[1], vv[3])))
        self.play(Write(MathTex("10").scale(0.6).move_to((vv[0] + vv[2]) / 2 + UP * 0.9 + RIGHT * 0.9)))
        k1 = Tex("Both sticks 10, pieces 5: equal and cut in half. Not $90^\\circ$.").scale(0.72).move_to(band_shift(5) + UP * 2.0 + RIGHT * 2.4)
        k2 = Tex("Square: full marks. Parallelogram: cut in half only.").scale(0.72).move_to(band_shift(5) + UP * 1.1 + RIGHT * 2.4)
        k3 = Tex("Rhombus: half, $90^\\circ$, corners halved. Kite: middle stick works.").scale(0.7).move_to(band_shift(5) + UP * 0.2 + RIGHT * 2.4)
        k4 = Tex("A millimetre or a degree off is fine; look for the pattern.").scale(0.7).move_to(band_shift(5) + DOWN * 0.8 + RIGHT * 2.4)
        for m in (k1, k2, k3, k4):
            self.play(Write(m))
            self.wait(2.6)
        self.wait(4)

        # --- Band 6 (subtopic_6): pizza slices
        self.next_band(6)
        t6 = Tex("Slice from one corner").scale(1.05).move_to(band_shift(6) + UP * 3.2)
        self.play(Write(t6))
        octo = regular(8, np.array([-4.6, -0.4, 0]) + band_shift(6), 1.9)
        self.play(Create(quad(octo)))
        self.play(Create(fan(octo)))
        self.play(Write(Tex("8 sides, 6 slices, $6 \\times 180 = 1080$").scale(0.6).move_to(octo[0] + DOWN * 4.3)))
        c1 = Tex("Two fewer slices than sides: (sides $- 2$) $\\times 180$.").scale(0.75).move_to(band_shift(6) + UP * 2.0 + RIGHT * 3.0)
        c2 = Tex("Pentagon 540: $540 - 460 = 80$ for the fifth corner.").scale(0.72).move_to(band_shift(6) + UP * 1.1 + RIGHT * 3.0)
        c3 = Tex("Regular hexagon: $720 \\div 6 = 120$. Three fit together: beehive.").scale(0.7).move_to(band_shift(6) + UP * 0.2 + RIGHT * 3.0)
        c4 = Tex("Share equally ONLY when the word regular is there.").scale(0.72).move_to(band_shift(6) + DOWN * 0.8 + RIGHT * 3.0)
        for m in (c1, c2, c3, c4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(c4, color=YELLOW)))
        self.wait(3)

        # --- Band 7 (subtopic_7): walk the block
        self.next_band(7)
        t7 = Tex("Walk around the block: $360^\\circ$ of turning").scale(1.05).move_to(band_shift(7) + UP * 3.2)
        self.play(Write(t7))
        hx = regular(6, np.array([-4.6, -0.6, 0]) + band_shift(7), 1.8)
        self.play(Create(quad(hx)))
        for k in range(6):
            a, b = hx[k], hx[(k + 1) % 6]
            self.play(Create(Arrow(a, b, buff=0.05, color=YELLOW, stroke_width=3)), run_time=0.35)
        w1 = Tex("Every polygon: outside turns add to $360^\\circ$.").scale(0.75).move_to(band_shift(7) + UP * 2.0 + RIGHT * 3.0)
        w2 = Tex("Regular: each outside angle is $360 \\div$ sides. Hexagon 60, octagon 45.").scale(0.7).move_to(band_shift(7) + UP * 1.1 + RIGHT * 3.0)
        w3 = Tex("Inside 150 means outside 30: $360 \\div 30 = 12$ sides.").scale(0.72).move_to(band_shift(7) + UP * 0.2 + RIGHT * 3.0)
        w4 = Tex("Outside 24: 15 sides, inside 156.").scale(0.72).move_to(band_shift(7) + DOWN * 0.7 + RIGHT * 3.0)
        w5 = Tex("Sticks, slices, the walk.").scale(0.8).move_to(band_shift(7) + DOWN * 2.2 + RIGHT * 3.0)
        for m in (w1, w2, w3, w4, w5):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(w5, color=YELLOW)))
        self.wait(6)
