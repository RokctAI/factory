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

# Running coin record from the script: (tosses, heads).
RUNNING = [(10, 7), (50, 27), (100, 46), (500, 258), (1000, 512)]


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


def table(rows, origin, col_w=1.7, row_h=0.5, scale=0.5):
    """Plain grid of Tex cells; rows is a list of lists of strings."""
    g = VGroup()
    n_r, n_c = len(rows), len(rows[0])
    for i in range(n_r + 1):
        g.add(Line(origin + DOWN * row_h * i, origin + RIGHT * col_w * n_c + DOWN * row_h * i,
                   color=GREY, stroke_width=2))
    for j in range(n_c + 1):
        g.add(Line(origin + RIGHT * col_w * j, origin + RIGHT * col_w * j + DOWN * row_h * n_r,
                   color=GREY, stroke_width=2))
    for i, row in enumerate(rows):
        for j, cell in enumerate(row):
            g.add(Tex(cell).scale(scale).move_to(origin + RIGHT * col_w * (j + 0.5) + DOWN * row_h * (i + 0.5)))
    return g


def running_graph(origin, width=6.0, height=3.0):
    """Broken-line graph of relative frequency of heads against toss number.
    Horizontal positions are evenly spaced by stage (not to scale)."""
    g = VGroup()
    g.add(Line(origin, origin + RIGHT * width, color=WHITE))
    g.add(Line(origin, origin + UP * height, color=WHITE))
    y_of = lambda rf: origin[1] + (rf - 0.3) / 0.5 * height
    half = Line(np.array([origin[0], y_of(0.5), 0]), np.array([origin[0] + width, y_of(0.5), 0]),
                color=YELLOW, stroke_width=2)
    g.add(half)
    g.add(Tex("0.5").scale(0.45).move_to(np.array([origin[0] - 0.35, y_of(0.5), 0])))
    pts = []
    for k, (n, h) in enumerate(RUNNING):
        x = origin[0] + width * (k + 0.5) / len(RUNNING)
        p = np.array([x, y_of(h / n), 0])
        pts.append(p)
        g.add(Dot(p, color=BLUE))
        g.add(Tex(str(n)).scale(0.42).move_to(np.array([x, origin[1] - 0.25, 0])))
    for a, b in zip(pts, pts[1:]):
        g.add(Line(a, b, color=BLUE, stroke_width=3))
    return g


class RelativeFrequencyVsProbabilitySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): side-by-side comparison
        title = Tex("Probability against relative frequency").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        rows = [["Outcome", "P", "Expected", "Observed", "RF"],
                ["Heads (50)", "0.5", "25", "27", "0.54"],
                ["Red (50)", "0.5", "25", "22", "0.44"],
                ["Blue (50)", "0.3", "15", "18", "0.36"],
                ["Yellow (50)", "0.2", "10", "10", "0.2"]]
        t = table(rows, np.array([-4.25, 2.1, 0]))
        self.play(Create(t), run_time=3)
        self.wait(3)
        c1 = MathTex(r"0.54 - 0.5 = 0.04 \text{ (4 points more heads)}").scale(0.8).shift(DOWN * 1.2)
        c2 = Tex("Die, 60 rolls: 8, 11, 9, 12, 10, 10 against 10 each").scale(0.75).shift(DOWN * 2.0)
        c3 = Tex("Differences $-2, +1, -1, +2, 0, 0$ add to zero").scale(0.75).shift(DOWN * 2.8)
        for m in (c1, c2, c3):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(c1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): chance or bias
        self.next_band(1)
        b1_title = Tex("Chance variation or bias?").scale(1.2).shift(band_shift(1) + UP * 2.8)
        self.play(Write(b1_title))
        self.wait(1.5)
        ch = Tex("Chance: unavoidable, either direction, large for few trials").scale(0.75).shift(band_shift(1) + UP * 1.6)
        bi = Tex("Bias: weighted die, bent coin, sticky spinner, sloppy method").scale(0.75).shift(band_shift(1) + UP * 0.8)
        self.play(Write(ch))
        self.wait(2.5)
        self.play(Write(bi))
        self.wait(2.5)
        d1 = MathTex(r"600 \text{ rolls: expected } \tfrac{1}{6} \times 600 = 100 \text{ sixes}").scale(0.8).shift(band_shift(1) + DOWN * 0.2)
        d2 = Tex("108 sixes: chance \\qquad 160 sixes: probably bias").scale(0.8).shift(band_shift(1) + DOWN * 1.1)
        d3 = Tex("Explain: size of gap, large or small for n, named cause").scale(0.75).shift(band_shift(1) + DOWN * 2.0)
        for m in (d1, d2, d3):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(d3, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): running graph
        self.next_band(2)
        b2_title = Tex("More trials: the fraction settles").scale(1.1).shift(band_shift(2) + UP * 3.1)
        self.play(Write(b2_title))
        self.wait(1.5)
        g = running_graph(band_shift(2) + LEFT * 6.3 + DOWN * 1.9)
        self.play(Create(g), run_time=3)
        self.wait(2)
        rows2 = [["n", "Heads", "RF", "Count gap"],
                 ["10", "7", "0.7", "+2"],
                 ["50", "27", "0.54", "+2"],
                 ["100", "46", "0.46", "$-4$"],
                 ["500", "258", "0.516", "+8"],
                 ["1000", "512", "0.512", "+12"]]
        t2 = table(rows2, band_shift(2) + RIGHT * 0.9 + UP * 1.9, col_w=1.35, row_h=0.45, scale=0.45)
        self.play(Create(t2), run_time=2.5)
        self.wait(2.5)
        s1 = Tex("Fraction gap shrinks; count gap does not").scale(0.75).shift(band_shift(2) + RIGHT * 3.6 + DOWN * 1.4)
        s2 = Tex("Dilution, not compensation").scale(0.75).shift(band_shift(2) + RIGHT * 3.6 + DOWN * 2.2)
        self.play(Write(s1))
        self.wait(2.4)
        self.play(Write(s2))
        self.play(Create(SurroundingRectangle(s2, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): estimating from data
        self.next_band(3)
        b3_title = Tex("Estimating a probability from data").scale(1.1).shift(band_shift(3) + UP * 2.6)
        self.play(Write(b3_title))
        self.wait(1.5)
        rows3 = [
            r"\text{Taxi late } 6 \text{ of } 40: \tfrac{6}{40} = 0.15;\; 0.15 \times 200 = 30 \text{ days}",
            r"\text{April rain } 9 \text{ of } 30: 0.3",
            r"\text{Bottle cap } 105 \text{ of } 300: 0.35;\; 0.35 \times 1000 = 350",
        ]
        for i, r in enumerate(rows3):
            m = MathTex(r).scale(0.8).shift(band_shift(3) + UP * (1.4 - 0.9 * i))
            self.play(Write(m))
            self.wait(2.5)
        cav = Tex("State the number of trials and the conditions assumed").scale(0.8).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(cav))
        self.play(Create(SurroundingRectangle(cav, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        e1 = Tex("27 heads in 50, so the coin is unfair").scale(0.8).shift(band_shift(4) + UP * 1.5)
        e2 = Tex("Five heads in a row, so tails is due").scale(0.8).shift(band_shift(4) + UP * 0.6)
        e3 = Tex("The heads and tails counts must even out").scale(0.8).shift(band_shift(4) + DOWN * 0.3)
        e4 = Tex("3 out of 5 trials, so P is 0.6").scale(0.8).shift(band_shift(4) + DOWN * 1.2)
        e5 = Tex("160 sixes in 600 rolls is just luck").scale(0.8).shift(band_shift(4) + DOWN * 2.1)
        for m in (e1, e2, e3, e4, e5):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.6)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): should against did
        self.next_band(5)
        b5_title = Tex("Should against did").scale(1.2).shift(band_shift(5) + UP * 2.6)
        self.play(Write(b5_title))
        self.wait(2)
        p1 = Tex("Coin: should 25 heads, did 27; 0.5 against 0.54").scale(0.85).shift(band_shift(5) + UP * 1.4)
        p2 = Tex("Die: should 10 each, did 8 to 12").scale(0.85).shift(band_shift(5) + UP * 0.5)
        p3 = Tex("Small gap: luck. Big gap that keeps happening: bias.").scale(0.85).shift(band_shift(5) + DOWN * 0.4)
        p4 = Tex("600 rolls: 108 sixes is luck, 160 is a problem").scale(0.85).shift(band_shift(5) + DOWN * 1.3)
        for m in (p1, p2, p3, p4):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(p3, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): luck evens out slowly
        self.next_band(6)
        b6_title = Tex("Luck evens out slowly").scale(1.2).shift(band_shift(6) + UP * 2.6)
        self.play(Write(b6_title))
        self.wait(2)
        q1 = Tex("0.7, 0.54, 0.46, 0.516, 0.512: creeping to 0.5").scale(0.85).shift(band_shift(6) + UP * 1.4)
        q2 = Tex("Extra heads: 2 after 10 tosses, 12 after 1000").scale(0.85).shift(band_shift(6) + UP * 0.5)
        q3 = Tex("The extras are drowned, never paid back").scale(0.85).shift(band_shift(6) + DOWN * 0.4)
        q4 = Tex("Pool the class: 30 learners times 20 tosses is 600").scale(0.85).shift(band_shift(6) + DOWN * 1.3)
        for m in (q1, q2, q3, q4):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(q3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): the data is the judge
        self.next_band(7)
        b7_title = Tex("When only the data can tell").scale(1.2).shift(band_shift(7) + UP * 2.6)
        self.play(Write(b7_title))
        self.wait(2)
        w1 = Tex("Taxi late 6 of 40 days: about 0.15, about 30 days a year").scale(0.8).shift(band_shift(7) + UP * 1.4)
        w2 = Tex("Say how many tries; say what stays the same").scale(0.85).shift(band_shift(7) + UP * 0.5)
        w3 = Tex("No coin is due a tail. Five tries is too few.").scale(0.85).shift(band_shift(7) + DOWN * 0.4)
        for m in (w1, w2, w3):
            self.play(Write(m))
            self.wait(2.4)
        w4 = Tex("Should, did, size, cause.").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(w4))
        self.play(Create(SurroundingRectangle(w4, color=YELLOW)))
        self.wait(4)
