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


def bars(origin, heights, width=0.5, gap=0.3, unit=0.07, color=BLUE):
    g = VGroup()
    x = 0.0
    for hgt in heights:
        g.add(Rectangle(width=width, height=unit * hgt, color=color, fill_opacity=0.5).move_to(origin + RIGHT * (x + width / 2) + UP * unit * hgt / 2))
        x += width + gap
    return g


def polyline(pts, color=YELLOW):
    return VGroup(*[Line(pts[i], pts[i + 1], color=color, stroke_width=3) for i in range(len(pts) - 1)])


def dots(pts, color=WHITE):
    return VGroup(*[Dot(p, radius=0.07, color=color) for p in pts])


def pie(centre, angles, radius=1.2, colors=(BLUE, GREEN, ORANGE)):
    g = VGroup()
    start = 0.0
    for a, c in zip(angles, colors):
        g.add(Sector(outer_radius=radius, inner_radius=0, start_angle=start * DEGREES, angle=a * DEGREES, color=c, fill_opacity=0.6, stroke_width=2).move_arc_center_to(centre))
        start += a
    return g


class RepresentingDataSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): bars and pies
        title = Tex("Categorical data: bar graph, double bar graph, pie chart").scale(0.95).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        o = np.array([-6.4, -2.4, 0])
        self.play(Create(mini_axes(o, 3.2, 2.8)))
        b = bars(o + RIGHT * 0.3, [33, 21, 6], width=0.6, gap=0.4)
        self.play(Create(b))
        for lab, x in zip(("walk", "taxi", "car"), (0.6, 1.6, 2.6)):
            self.play(Write(Tex(lab).scale(0.5).move_to(o + RIGHT * x + DOWN * 0.3)), run_time=0.4)
        o2 = np.array([-2.4, -2.4, 0])
        self.play(Create(mini_axes(o2, 3.4, 2.8)))
        db = VGroup()
        for i, (bb, gg) in enumerate(((18, 15), (9, 12), (3, 3))):
            db.add(Rectangle(width=0.35, height=0.12 * bb, color=BLUE, fill_opacity=0.5).move_to(o2 + RIGHT * (0.5 + 1.1 * i) + UP * 0.06 * bb))
            db.add(Rectangle(width=0.35, height=0.12 * gg, color=GREEN, fill_opacity=0.5).move_to(o2 + RIGHT * (0.88 + 1.1 * i) + UP * 0.06 * gg))
        self.play(Create(db))
        self.play(Write(Tex("key: blue boys, green girls").scale(0.45).move_to(o2 + RIGHT * 1.7 + DOWN * 0.3)))
        pc = pie(np.array([4.2, -1.0, 0]), [198, 126, 36])
        self.play(Create(pc))
        p1 = MathTex(r"\tfrac{33}{60} \times 360 = 198^\circ,\ \tfrac{21}{60} \times 360 = 126^\circ,\ \tfrac{6}{60} \times 360 = 36^\circ").scale(0.65).shift(UP * 2.2 + RIGHT * 1.2)
        p2 = Tex("Check: $198 + 126 + 36 = 360$. Shares 55\\%, 35\\%, 10\\%.").scale(0.7).shift(UP * 1.5 + RIGHT * 1.2)
        for m in (p1, p2):
            self.play(Write(m))
            self.wait(2.6)
        self.wait(4)

        # --- Band 1 (subtopic_2): histogram
        self.next_band(1)
        h1 = Tex("Histogram: numerical data in intervals, bars touch").scale(1.0).move_to(band_shift(1) + UP * 3.2)
        self.play(Write(h1))
        oh = np.array([-6.4, -2.4, 0]) + band_shift(1)
        self.play(Create(mini_axes(oh, 5.6, 3.0)))
        hb = bars(oh, [8, 11, 6, 3, 2], width=1.0, gap=0.0, unit=0.22, color=TEAL)
        self.play(Create(hb))
        for k in range(6):
            self.play(Write(Tex(str(k)).scale(0.5).move_to(oh + RIGHT * k + DOWN * 0.3)), run_time=0.2)
        self.play(Write(Tex("distance to school (km)").scale(0.5).move_to(oh + RIGHT * 2.8 + DOWN * 0.7)))
        s1 = Tex("Frequencies 8, 11, 6, 3, 2 add to 30. Modal interval: 1 to under 2.").scale(0.7).move_to(band_shift(1) + UP * 2.1 + RIGHT * 2.6)
        s2 = Tex("Right-skewed: a pile near school, a tail to 5 km.").scale(0.7).move_to(band_shift(1) + UP * 1.3 + RIGHT * 2.6)
        s3 = Tex("Own intervals: range $4.8 - 0.2 = 4.6$; five to eight equal widths; round edges.").scale(0.65).move_to(band_shift(1) + UP * 0.5 + RIGHT * 2.6)
        s4 = Tex("0 to under 1, 1 to under 2: no value in two intervals.").scale(0.68).move_to(band_shift(1) + DOWN * 0.3 + RIGHT * 2.6)
        for m in (s1, s2, s3, s4):
            self.play(Write(m))
            self.wait(2.6)
        self.wait(3)

        # --- Band 2 (subtopic_3): line and scatter
        self.next_band(2)
        h2 = Tex("Broken-line graph and scatter plot").scale(1.05).move_to(band_shift(2) + UP * 3.2)
        self.play(Write(h2))
        ol = np.array([-6.6, -2.4, 0]) + band_shift(2)
        self.play(Create(mini_axes(ol, 4.4, 3.2)))
        kwh = [320, 300, 310, 350, 420, 480]
        lp = [ol + RIGHT * (0.4 + 0.7 * i) + UP * 0.006 * v for i, v in enumerate(kwh)]
        self.play(Create(dots(lp)))
        self.play(Create(polyline(lp)))
        self.play(Write(Tex("kWh, Jan to Jun: 320, 300, 310, 350, 420, 480").scale(0.5).move_to(ol + RIGHT * 2.2 + DOWN * 0.3)))
        osc = np.array([0.6, -2.4, 0]) + band_shift(2)
        self.play(Create(mini_axes(osc, 4.4, 3.2)))
        pairs = [(1, 35), (2, 42), (2, 50), (3, 55), (4, 60), (5, 68), (6, 75), (7, 80)]
        sp = [osc + RIGHT * 0.55 * x + UP * 0.036 * y for x, y in pairs]
        self.play(Create(dots(sp, color=YELLOW)))
        self.play(Write(Tex("hours studied vs mark: not joined").scale(0.5).move_to(osc + RIGHT * 2.2 + DOWN * 0.3)))
        l1 = Tex("Steepest segment May to June: a rise of 60. Axis from zero, or the rise is exaggerated.").scale(0.62).move_to(band_shift(2) + UP * 2.2)
        l2 = Tex("Dots rise left to right: positive relationship. Association, not cause.").scale(0.68).move_to(band_shift(2) + UP * 1.5)
        for m in (l1, l2):
            self.play(Write(m))
            self.wait(2.8)
        self.wait(3)

        # --- Band 3 (subtopic_4): choosing
        self.next_band(3)
        h3 = Tex("Match the data to the graph; dress every graph").scale(1.0).move_to(band_shift(3) + UP * 3.2)
        self.play(Write(h3))
        rows = [
            "categorical: bar graph; shares of a whole: pie; two groups: double bar",
            "numerical in intervals: histogram",
            "one quantity over time: broken-line graph",
            "two numerical variables per individual: scatter plot",
            "title (what, who, when); axes labelled with units; even scale from zero; key",
            "angle table summing to 360; frequency table summing to the total",
        ]
        y = 2.1
        for r in rows:
            self.play(Write(Tex(r).scale(0.66).move_to(band_shift(3) + UP * y)))
            self.wait(2.0)
            y -= 0.75
        self.wait(3)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        h4 = Tex("Error museum").scale(1.05).move_to(band_shift(4) + UP * 3.2)
        self.play(Write(h4))
        e1 = Tex("Histogram with gaps between the bars").scale(0.8).move_to(band_shift(4) + UP * 1.8)
        e2 = Tex("Pie angles adding to 362").scale(0.8).move_to(band_shift(4) + UP * 0.6)
        e3 = Tex("Scatter plot with the dots joined").scale(0.8).move_to(band_shift(4) + DOWN * 0.6)
        for m in (e1, e2, e3):
            self.play(Write(m))
            self.wait(1.5)
            self.play(Create(strike(m)))
            self.wait(1.5)
        fix = Tex("Numbers touch, words apart; check the 360; one dot per person, unjoined.").scale(0.7).move_to(band_shift(4) + DOWN * 2.2)
        self.play(Write(fix))
        self.play(Create(SurroundingRectangle(fix, color=GREEN)))
        self.wait(5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): towers and slices
        self.next_band(5)
        h5 = Tex("Towers and slices").scale(1.05).move_to(band_shift(5) + UP * 3.2)
        self.play(Write(h5))
        ot = np.array([-6.4, -2.2, 0]) + band_shift(5)
        self.play(Create(mini_axes(ot, 3.2, 2.8)))
        self.play(Create(bars(ot + RIGHT * 0.3, [33, 21, 6], width=0.6, gap=0.4)))
        pc2 = pie(np.array([-1.2, -0.8, 0]) + band_shift(5), [198, 126, 36])
        self.play(Create(pc2))
        t1 = Tex("Words: one tower per word, gaps between. Tallest tower is the mode.").scale(0.68).move_to(band_shift(5) + UP * 2.0 + RIGHT * 2.6)
        t2 = Tex("Two groups: two towers per word and a key.").scale(0.72).move_to(band_shift(5) + UP * 1.2 + RIGHT * 2.6)
        t3 = Tex("Pie: count over total times 360. 198, 126, 36: the pie closes.").scale(0.7).move_to(band_shift(5) + UP * 0.4 + RIGHT * 2.6)
        t4 = Tex("Pies show shares, not counts; crowded past six slices.").scale(0.7).move_to(band_shift(5) + DOWN * 0.4 + RIGHT * 2.6)
        for m in (t1, t2, t3, t4):
            self.play(Write(m))
            self.wait(2.6)
        self.wait(3)

        # --- Band 6 (subtopic_6): bars that touch
        self.next_band(6)
        h6 = Tex("Bars that touch").scale(1.05).move_to(band_shift(6) + UP * 3.2)
        self.play(Write(h6))
        ob = np.array([-6.4, -2.4, 0]) + band_shift(6)
        self.play(Create(mini_axes(ob, 5.6, 3.0)))
        self.play(Create(bars(ob, [8, 11, 6, 3, 2], width=1.0, gap=0.0, unit=0.22, color=TEAL)))
        u1 = Tex("No gap between 0.99 and 1, so no gap between the bars.").scale(0.7).move_to(band_shift(6) + UP * 2.0 + RIGHT * 2.6)
        u2 = Tex("$8 + 11 + 6 + 3 + 2 = 30$. Tallest band: 1 to under 2.").scale(0.72).move_to(band_shift(6) + UP * 1.2 + RIGHT * 2.6)
        u3 = Tex("Make your own bands: range 4.6, five bands of width 1, round edges.").scale(0.68).move_to(band_shift(6) + UP * 0.4 + RIGHT * 2.6)
        u4 = Tex("Too few: two blocks. Too many: lonely spikes. Keep widths equal.").scale(0.68).move_to(band_shift(6) + DOWN * 0.4 + RIGHT * 2.6)
        for m in (u1, u2, u3, u4):
            self.play(Write(m))
            self.wait(2.6)
        self.wait(3)

        # --- Band 7 (subtopic_7): lines and clouds
        self.next_band(7)
        h7 = Tex("Lines through time and clouds of dots").scale(1.05).move_to(band_shift(7) + UP * 3.2)
        self.play(Write(h7))
        o7 = np.array([-6.6, -2.4, 0]) + band_shift(7)
        self.play(Create(mini_axes(o7, 4.4, 3.2)))
        lp2 = [o7 + RIGHT * (0.4 + 0.7 * i) + UP * 0.006 * v for i, v in enumerate(kwh)]
        self.play(Create(dots(lp2)), Create(polyline(lp2)))
        o8 = np.array([0.6, -2.4, 0]) + band_shift(7)
        self.play(Create(mini_axes(o8, 4.4, 3.2)))
        sp2 = [o8 + RIGHT * 0.55 * x + UP * 0.036 * y for x, y in pairs]
        self.play(Create(dots(sp2, color=YELLOW)))
        v1 = Tex("One thing month after month: dots joined, side scale from zero.").scale(0.68).move_to(band_shift(7) + UP * 2.2)
        v2 = Tex("Two numbers per person: a cloud, not joined. Up-slope: together, not because.").scale(0.66).move_to(band_shift(7) + UP * 1.5)
        v3 = Tex("Towers and slices, bars that touch, lines and clouds.").scale(0.8).move_to(band_shift(7) + UP * 0.6)
        for m in (v1, v2, v3):
            self.play(Write(m))
            self.wait(2.8)
        self.play(Create(SurroundingRectangle(v3, color=YELLOW)))
        self.wait(6)
