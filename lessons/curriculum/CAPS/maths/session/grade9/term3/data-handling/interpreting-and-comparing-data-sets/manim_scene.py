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


def mini_axes(origin, w=4.0, h=2.6, color=GREY):
    return VGroup(Line(origin, origin + RIGHT * w, color=color, stroke_width=3),
                  Line(origin, origin + UP * h, color=color, stroke_width=3))


def polyline(pts, color=YELLOW):
    return VGroup(*[Line(pts[i], pts[i + 1], color=color, stroke_width=3) for i in range(len(pts) - 1)])


def dots(pts, color=WHITE):
    return VGroup(*[Dot(p, radius=0.07, color=color) for p in pts])


def dotline(values, origin, unit=0.16, color=WHITE):
    """Dots on a number line at the given values, stacked when repeated."""
    g = VGroup()
    seen = {}
    for v in values:
        k = seen.get(v, 0)
        seen[v] = k + 1
        g.add(Dot(origin + RIGHT * unit * v + UP * 0.2 * k, radius=0.07, color=color))
    return g


def table(rows, origin, col_w=1.4, row_h=0.5, scale=0.55):
    g = VGroup()
    for i, row in enumerate(rows):
        for j, cell in enumerate(row):
            g.add(Tex(cell).scale(scale).move_to(origin + RIGHT * col_w * j + DOWN * row_h * i))
    return g


class ComparingDataSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): read critically
        title = Tex("Read the graph critically before you read its values").scale(1.0).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        o1 = np.array([-6.6, -2.4, 0])
        self.play(Create(mini_axes(o1, 3.6, 3.0)))
        kwh = [320, 300, 310, 350, 420, 480]
        p_full = [o1 + RIGHT * (0.3 + 0.6 * i) + UP * 0.006 * v for i, v in enumerate(kwh)]
        self.play(Create(dots(p_full)), Create(polyline(p_full)))
        self.play(Write(Tex("axis from 0").scale(0.5).move_to(o1 + RIGHT * 1.8 + DOWN * 0.3)))
        o2 = np.array([-2.2, -2.4, 0])
        self.play(Create(mini_axes(o2, 3.6, 3.0)))
        p_cut = [o2 + RIGHT * (0.3 + 0.6 * i) + UP * 0.016 * (v - 300) for i, v in enumerate(kwh)]
        self.play(Create(dots(p_cut, color=RED)), Create(polyline(p_cut, color=RED)))
        self.play(Write(Tex("axis from 300: chopped").scale(0.5).move_to(o2 + RIGHT * 1.8 + DOWN * 0.3)))
        c1 = Tex("Check: title, labels with units, scale start, key.").scale(0.7).shift(UP * 2.2 + RIGHT * 2.6)
        c2 = Tex("Read: 320 to 480 kWh, a rise of 160, which is 50\\%.").scale(0.7).shift(UP * 1.4 + RIGHT * 2.6)
        c3 = Tex("Distortion: chopped axis, uneven spacing, 3D pie, unequal intervals, cherry-picked months.").scale(0.6).shift(UP * 0.6 + RIGHT * 2.6)
        c4 = Tex("Match the graph to the claim: counts answer how many, not which school cares more.").scale(0.6).shift(DOWN * 0.2 + RIGHT * 2.6)
        for m in (c1, c2, c3, c4):
            self.play(Write(m))
            self.wait(2.6)
        self.wait(3)

        # --- Band 1 (subtopic_2): statistics
        self.next_band(1)
        h1 = Tex("Two classes, same measures").scale(1.05).move_to(band_shift(1) + UP * 3.2)
        self.play(Write(h1))
        A = [23, 31, 35, 35, 38, 40, 42, 44, 45, 47]
        B = [30, 33, 36, 37, 38, 39, 40, 41, 43, 49]
        base = band_shift(1) + LEFT * 6.6 + UP * 1.4
        self.play(Create(Line(base + RIGHT * 0.16 * 20, base + RIGHT * 0.16 * 50, color=GREY, stroke_width=3)))
        self.play(Create(dotline(A, base + UP * 0.2, color=BLUE)))
        self.play(Write(Tex("Class A").scale(0.5).move_to(base + RIGHT * 0.16 * 18 + UP * 0.3)))
        base2 = band_shift(1) + LEFT * 6.6 + DOWN * 0.4
        self.play(Create(Line(base2 + RIGHT * 0.16 * 20, base2 + RIGHT * 0.16 * 50, color=GREY, stroke_width=3)))
        self.play(Create(dotline(B, base2 + UP * 0.2, color=GREEN)))
        self.play(Write(Tex("Class B").scale(0.5).move_to(base2 + RIGHT * 0.16 * 18 + UP * 0.3)))
        tb = table([["", "mean", "median", "range", "min", "max"], ["A", "38.0", "39", "24", "23", "47"], ["B", "38.6", "38.5", "19", "30", "49"]], band_shift(1) + RIGHT * 1.2 + UP * 2.0, col_w=1.0)
        self.play(Write(tb))
        s1 = Tex("Centres nearly equal; B more consistent; A has a weaker tail.").scale(0.7).move_to(band_shift(1) + DOWN * 1.8)
        s2 = Tex("Ten each: a 0.6 gap says nothing about teaching. Sizes differ: 30\\% vs 37.5\\%, not 240 vs 150.").scale(0.62).move_to(band_shift(1) + DOWN * 2.6)
        for m in (s1, s2):
            self.play(Write(m))
            self.wait(2.8)
        self.play(Create(SurroundingRectangle(s1, color=YELLOW)))
        self.wait(3)

        # --- Band 2 (subtopic_3): graphs
        self.next_band(2)
        h2 = Tex("Two lines on one graph; back-to-back stems").scale(1.05).move_to(band_shift(2) + UP * 3.2)
        self.play(Write(h2))
        o3 = np.array([-6.6, -2.4, 0]) + band_shift(2)
        self.play(Create(mini_axes(o3, 4.6, 3.4)))
        dbn = [130, 120, 110, 70, 50, 30]
        cpt = [15, 15, 20, 50, 80, 95]
        pd = [o3 + RIGHT * (0.4 + 0.75 * i) + UP * 0.024 * v for i, v in enumerate(dbn)]
        pc = [o3 + RIGHT * (0.4 + 0.75 * i) + UP * 0.024 * v for i, v in enumerate(cpt)]
        self.play(Create(dots(pd, color=ORANGE)), Create(polyline(pd, color=ORANGE)))
        self.play(Create(dots(pc, color=BLUE)), Create(polyline(pc, color=BLUE)))
        self.play(Write(Tex("key: orange Durban, blue Cape Town; mm, Jan to Jun").scale(0.45).move_to(o3 + RIGHT * 2.3 + DOWN * 0.3)))
        st = table([["A leaves", "stem", "B leaves"], ["3", "2", ""], ["8 5 5 1", "3", "0 3 6 7 8 9"], ["7 5 4 2 0", "4", "0 1 3 9"]], band_shift(2) + RIGHT * 1.0 + UP * 1.8, col_w=1.9, row_h=0.55)
        self.play(Write(st))
        g1 = Tex("Lines cross between April and May: opposite seasons. Totals 510 and 275.").scale(0.62).move_to(band_shift(2) + DOWN * 1.6 + RIGHT * 1.8)
        g2 = Tex("Same scale, or the eye is fooled; percentages when sizes differ.").scale(0.65).move_to(band_shift(2) + DOWN * 2.4 + RIGHT * 1.8)
        for m in (g1, g2):
            self.play(Write(m))
            self.wait(2.8)
        self.wait(3)

        # --- Band 3 (subtopic_4): writing
        self.next_band(3)
        h3 = Tex("Writing the comparison: four moves").scale(1.05).move_to(band_shift(3) + UP * 3.2)
        self.play(Write(h3))
        moves = [
            "1. What is compared, and with which measures.",
            "2. Centres with values: 38.0 and 39 against 38.6 and 38.5.",
            "3. Spreads with values: range 24 against 19; lows 23 and 30; highs 47 and 49.",
            "4. Conclusion no bigger than the data: similar, B steadier, ten is too few.",
        ]
        y = 2.0
        for mv in moves:
            self.play(Write(Tex(mv).scale(0.7).move_to(band_shift(3) + UP * y)))
            self.wait(2.4)
            y -= 0.85
        r1 = Tex("Rain: 510 vs 275, lines crossing, opposite seasons, a full year needed.").scale(0.68).move_to(band_shift(3) + DOWN * 1.8)
        self.play(Write(r1))
        self.wait(4)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        h4 = Tex("Error museum").scale(1.05).move_to(band_shift(4) + UP * 3.2)
        self.play(Write(h4))
        e1 = Tex("240 recyclers beats 150, so X cares more").scale(0.8).move_to(band_shift(4) + UP * 1.8)
        e2 = Tex("38.6 beats 38.0, so B is better").scale(0.8).move_to(band_shift(4) + UP * 0.6)
        e3 = Tex("Higher and more spread (no numbers)").scale(0.8).move_to(band_shift(4) + DOWN * 0.6)
        for m in (e1, e2, e3):
            self.play(Write(m))
            self.wait(1.5)
            self.play(Create(strike(m)))
            self.wait(1.5)
        fix = Tex("Percentages for unequal groups; centre AND spread; values quoted; caution stated.").scale(0.66).move_to(band_shift(4) + DOWN * 2.2)
        self.play(Write(fix))
        self.play(Create(SurroundingRectangle(fix, color=GREEN)))
        self.wait(5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): whole picture
        self.next_band(5)
        h5 = Tex("Read the whole picture").scale(1.05).move_to(band_shift(5) + UP * 3.2)
        self.play(Write(h5))
        w1 = Tex("Title: what, who, when. Labels with units. Where the side scale starts. The key.").scale(0.66).move_to(band_shift(5) + UP * 2.0)
        w2 = Tex("No units: a picture, not evidence.").scale(0.8).move_to(band_shift(5) + UP * 1.1)
        w3 = Tex("Chopped axis: 320 to 480 looks like a rocket instead of a half.").scale(0.7).move_to(band_shift(5) + UP * 0.2)
        w4 = Tex("Does the graph answer the question being argued? Counts cannot say who cares more.").scale(0.64).move_to(band_shift(5) + DOWN * 0.7)
        for m in (w1, w2, w3, w4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(w2, color=YELLOW)))
        self.wait(4)

        # --- Band 6 (subtopic_6): same middle
        self.next_band(6)
        h6 = Tex("Same middle, different spread").scale(1.05).move_to(band_shift(6) + UP * 3.2)
        self.play(Write(h6))
        b6 = band_shift(6) + LEFT * 6.6 + UP * 1.4
        self.play(Create(Line(b6 + RIGHT * 0.16 * 20, b6 + RIGHT * 0.16 * 50, color=GREY, stroke_width=3)))
        self.play(Create(dotline(A, b6 + UP * 0.2, color=BLUE)))
        b7 = band_shift(6) + LEFT * 6.6 + DOWN * 0.2
        self.play(Create(Line(b7 + RIGHT * 0.16 * 20, b7 + RIGHT * 0.16 * 50, color=GREY, stroke_width=3)))
        self.play(Create(dotline(B, b7 + UP * 0.2, color=GREEN)))
        self.play(Create(Line(b6 + RIGHT * 0.16 * 23, b6 + RIGHT * 0.16 * 47, color=BLUE, stroke_width=6).shift(DOWN * 0.3)))
        self.play(Create(Line(b7 + RIGHT * 0.16 * 30, b7 + RIGHT * 0.16 * 49, color=GREEN, stroke_width=6).shift(DOWN * 0.3)))
        m1 = Tex("Middles: 38.0 and 39 against 38.6 and 38.5. A draw.").scale(0.7).move_to(band_shift(6) + DOWN * 1.4 + RIGHT * 1.6)
        m2 = Tex("Spreads: 24 against 19. B tighter; A has a straggler at 23.").scale(0.7).move_to(band_shift(6) + DOWN * 2.1 + RIGHT * 1.6)
        m3 = Tex("Different sizes: 30\\% and 37.5\\%, never 240 and 150.").scale(0.7).move_to(band_shift(6) + DOWN * 2.8 + RIGHT * 1.6)
        for m in (m1, m2, m3):
            self.play(Write(m))
            self.wait(2.6)
        self.wait(3)

        # --- Band 7 (subtopic_7): two lines
        self.next_band(7)
        h7 = Tex("Two lines on one graph").scale(1.05).move_to(band_shift(7) + UP * 3.2)
        self.play(Write(h7))
        o7 = np.array([-6.6, -2.4, 0]) + band_shift(7)
        self.play(Create(mini_axes(o7, 4.6, 3.4)))
        pd2 = [o7 + RIGHT * (0.4 + 0.75 * i) + UP * 0.024 * v for i, v in enumerate(dbn)]
        pc2 = [o7 + RIGHT * (0.4 + 0.75 * i) + UP * 0.024 * v for i, v in enumerate(cpt)]
        self.play(Create(dots(pd2, color=ORANGE)), Create(polyline(pd2, color=ORANGE)))
        self.play(Create(dots(pc2, color=BLUE)), Create(polyline(pc2, color=BLUE)))
        l1 = Tex("Same scale, one key. The crossing is the story: seasons change hands.").scale(0.66).move_to(band_shift(7) + UP * 2.0 + RIGHT * 2.4)
        l2 = Tex("Back-to-back stems: A's straggler and B's tight cluster, no arithmetic.").scale(0.66).move_to(band_shift(7) + UP * 1.1 + RIGHT * 2.4)
        l3 = Tex("Four moves: what and how; middles; spreads; a conclusion the data allows.").scale(0.66).move_to(band_shift(7) + UP * 0.2 + RIGHT * 2.4)
        l4 = Tex("Whole picture, same middle different spread, two lines on one graph.").scale(0.7).move_to(band_shift(7) + DOWN * 0.8 + RIGHT * 2.4)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(l4, color=YELLOW)))
        self.wait(6)
