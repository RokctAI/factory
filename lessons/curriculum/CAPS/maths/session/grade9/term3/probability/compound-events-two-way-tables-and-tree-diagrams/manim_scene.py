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


def grid(origin, n=6, cell=0.55, color=GREY):
    """An n-by-n grid of squares with the given cell size, top-left at origin."""
    g = VGroup()
    for i in range(n + 1):
        g.add(Line(origin + DOWN * cell * i, origin + RIGHT * cell * n + DOWN * cell * i, color=color, stroke_width=2))
        g.add(Line(origin + RIGHT * cell * i, origin + RIGHT * cell * i + DOWN * cell * n, color=color, stroke_width=2))
    return g


def grid_labels(origin, n=6, cell=0.55, fn=lambda i, j: str(i + j + 2), scale=0.4, color=WHITE):
    g = VGroup()
    for i in range(n):
        for j in range(n):
            g.add(Tex(fn(i, j)).scale(scale).move_to(origin + RIGHT * cell * (j + 0.5) + DOWN * cell * (i + 0.5)).set_color(color))
    return g


def tree(origin, first, second, width=2.4, spread=1.4, scale=0.5):
    """Two-stage tree: first is a list of (label, prob), second a list of lists of (label, prob)."""
    g = VGroup()
    n1 = len(first)
    y1 = [spread * (n1 - 1) / 2 - spread * k for k in range(n1)]
    for k, (lab, pr) in enumerate(first):
        end = origin + RIGHT * width + UP * y1[k]
        g.add(Line(origin, end, color=BLUE, stroke_width=3))
        g.add(Tex(f"{lab} {pr}").scale(scale).move_to((origin + end) / 2 + UP * 0.25))
        n2 = len(second[k])
        y2 = [spread * 0.45 * (n2 - 1) / 2 - spread * 0.45 * m for m in range(n2)]
        for m, (lab2, pr2) in enumerate(second[k]):
            end2 = end + RIGHT * width + UP * y2[m]
            g.add(Line(end, end2, color=BLUE, stroke_width=3))
            g.add(Tex(f"{lab2} {pr2}").scale(scale).move_to((end + end2) / 2 + UP * 0.22))
    return g


class CompoundEventsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): listing outcomes
        title = Tex("Compound events: list every outcome").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        o1 = Tex("Two coins: HH, HT, TH, TT. Four equally likely outcomes.").scale(0.78).shift(UP * 2.0)
        o2 = MathTex(r"P(\text{two heads}) = \tfrac{1}{4},\quad P(\text{exactly one head}) = \tfrac{2}{4} = \tfrac{1}{2},\quad P(\text{at least one}) = \tfrac{3}{4}").scale(0.72).shift(UP * 1.2)
        o3 = Tex("Coin and die: $2 \\times 6 = 12$ outcomes, H1 to H6 and T1 to T6.").scale(0.75).shift(UP * 0.3)
        o4 = MathTex(r"P(\text{H and 6}) = \tfrac{1}{12},\quad P(\text{H and even}) = \tfrac{3}{12} = \tfrac{1}{4},\quad P(\text{T or 6}) = \tfrac{7}{12}").scale(0.72).shift(DOWN * 0.6)
        o5 = Tex("Rule: $m$ outcomes times $n$ outcomes gives $m \\times n$, when equally likely and independent.").scale(0.66).shift(DOWN * 1.6)
        for m in (o1, o2, o3, o4, o5):
            self.play(Write(m))
            self.wait(2.5)
        self.play(Create(SurroundingRectangle(o1, color=YELLOW)))
        self.wait(3)

        # --- Band 1 (subtopic_2): two-way table
        self.next_band(1)
        h1 = Tex("Two dice: a two-way table of 36 cells").scale(1.05).move_to(band_shift(1) + UP * 3.2)
        self.play(Write(h1))
        go = np.array([-6.0, 2.2, 0]) + band_shift(1)
        self.play(Create(grid(go)))
        for k in range(6):
            self.play(Write(Tex(str(k + 1)).scale(0.4).move_to(go + RIGHT * 0.55 * (k + 0.5) + UP * 0.25)), Write(Tex(str(k + 1)).scale(0.4).move_to(go + LEFT * 0.25 + DOWN * 0.55 * (k + 0.5))), run_time=0.2)
        labs = grid_labels(go)
        self.play(Write(labs), run_time=2)
        sevens = VGroup(*[labs[i * 6 + (5 - i)] for i in range(6)])
        self.play(*[s.animate.set_color(YELLOW) for s in sevens])
        t1 = MathTex(r"P(\text{sum } 7) = \tfrac{6}{36} = \tfrac{1}{6},\qquad P(\text{sum } 2) = \tfrac{1}{36}").scale(0.78).move_to(band_shift(1) + UP * 2.0 + RIGHT * 2.6)
        t2 = Tex("The eleven sums are NOT equally likely.").scale(0.75).move_to(band_shift(1) + UP * 1.2 + RIGHT * 2.6)
        t3 = MathTex(r"P(\text{double}) = \tfrac{6}{36},\quad P(\text{sum} \geq 10) = \tfrac{6}{36},\quad P(7 \text{ or } 11) = \tfrac{8}{36} = \tfrac{2}{9}").scale(0.68).move_to(band_shift(1) + UP * 0.3 + RIGHT * 2.6)
        t4 = Tex("Learner table: $P(\\text{girl and taxi}) = \\tfrac{12}{60} = \\tfrac{1}{5}$.").scale(0.72).move_to(band_shift(1) + DOWN * 0.6 + RIGHT * 2.6)
        for m in (t1, t2, t3, t4):
            self.play(Write(m))
            self.wait(2.6)
        self.wait(3)

        # --- Band 2 (subtopic_3): tree diagrams
        self.next_band(2)
        h2 = Tex("Tree diagrams: multiply along, add across").scale(1.05).move_to(band_shift(2) + UP * 3.2)
        self.play(Write(h2))
        tr = tree(np.array([-6.6, 1.2, 0]) + band_shift(2), [("R", "1/3"), ("B", "2/3")], [[("R", "1/3"), ("B", "2/3")], [("R", "1/3"), ("B", "2/3")]], width=2.0, spread=1.6)
        self.play(Create(tr), run_time=2)
        s1 = MathTex(r"RR = \tfrac{1}{9},\ RB = \tfrac{2}{9},\ BR = \tfrac{2}{9},\ BB = \tfrac{4}{9};\quad \text{tips add to } 1").scale(0.72).move_to(band_shift(2) + UP * 2.1 + RIGHT * 2.4)
        s2 = MathTex(r"P(\text{one of each}) = \tfrac{2}{9} + \tfrac{2}{9} = \tfrac{4}{9}").scale(0.8).move_to(band_shift(2) + UP * 1.2 + RIGHT * 2.4)
        tr2 = tree(np.array([-6.6, -1.6, 0]) + band_shift(2), [("R", "3/5"), ("G", "2/5")], [[("R", "2/4"), ("G", "2/4")], [("R", "3/4"), ("G", "1/4")]], width=2.0, spread=1.6)
        self.play(Create(tr2), run_time=2)
        s3 = MathTex(r"\text{without replacement: } RR = \tfrac{3}{5} \times \tfrac{2}{4} = \tfrac{3}{10},\ GG = \tfrac{1}{10},\ \text{different} = \tfrac{3}{5}").scale(0.66).move_to(band_shift(2) + DOWN * 0.8 + RIGHT * 2.4)
        s4 = MathTex(r"\text{with replacement: } RR = \tfrac{3}{5} \times \tfrac{3}{5} = \tfrac{9}{25}").scale(0.72).move_to(band_shift(2) + DOWN * 1.7 + RIGHT * 2.4)
        for m in (s1, s2, s3, s4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(s3, color=YELLOW)))
        self.wait(3)

        # --- Band 3 (subtopic_4): choosing the tool
        self.next_band(3)
        h3 = Tex("Table or tree?").scale(1.05).move_to(band_shift(3) + UP * 3.2)
        self.play(Write(h3))
        c1 = Tex("Table: two experiments, few outcomes each, event combines results (sums).").scale(0.7).move_to(band_shift(3) + UP * 2.0)
        c2 = Tex("Tree: in sequence, second depends on first (no replacement), unequal branches.").scale(0.7).move_to(band_shift(3) + UP * 1.1)
        c3 = Tex("Same method: find the outcomes of the event, their probabilities, add.").scale(0.72).move_to(band_shift(3) + UP * 0.2)
        c4 = Tex("Layout: sample space or labelled diagram; mark favourable; product or count; add; tips make 1.").scale(0.62).move_to(band_shift(3) + DOWN * 0.7)
        for m in (c1, c2, c3, c4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(c3, color=YELLOW)))
        self.wait(4)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        h4 = Tex("Error museum").scale(1.05).move_to(band_shift(4) + UP * 3.2)
        self.play(Write(h4))
        e1 = MathTex(r"\text{HH, HT, TT: } P(\text{two heads}) = \tfrac{1}{3}").scale(0.85).move_to(band_shift(4) + UP * 1.8)
        e2 = MathTex(r"P(\text{sum } 7) = \tfrac{1}{11}").scale(0.9).move_to(band_shift(4) + UP * 0.6)
        e3 = MathTex(r"P(RR) = \tfrac{1}{3} + \tfrac{1}{3}").scale(0.9).move_to(band_shift(4) + DOWN * 0.6)
        for m in (e1, e2, e3):
            self.play(Write(m))
            self.wait(1.5)
            self.play(Create(strike(m)))
            self.wait(1.5)
        fix = Tex("HT differs from TH; count cells, not sums; multiply along a path; change branches without replacement.").scale(0.6).move_to(band_shift(4) + DOWN * 2.2)
        self.play(Write(fix))
        self.play(Create(SurroundingRectangle(fix, color=GREEN)))
        self.wait(5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): every way
        self.next_band(5)
        h5 = Tex("Write every way it could happen").scale(1.05).move_to(band_shift(5) + UP * 3.2)
        self.play(Write(h5))
        w1 = Tex("HH \\quad HT \\quad TH \\quad TT").scale(1.1).move_to(band_shift(5) + UP * 2.0)
        w2 = Tex("Left shoe then right is not right then left: HT and TH are two ways.").scale(0.7).move_to(band_shift(5) + UP * 1.1)
        w3 = Tex("Two heads 1 in 4; exactly one head a half; at least one head 3 in 4.").scale(0.72).move_to(band_shift(5) + UP * 0.2)
        w4 = Tex("Ways times ways: coins $2 \\times 2$; coin and die $2 \\times 6$; two dice $6 \\times 6$; three coins 8.").scale(0.66).move_to(band_shift(5) + DOWN * 0.7)
        for m in (w1, w2, w3, w4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(w2, color=YELLOW)))
        self.wait(4)

        # --- Band 6 (subtopic_6): dice grid
        self.next_band(6)
        h6 = Tex("The dice grid").scale(1.05).move_to(band_shift(6) + UP * 3.2)
        self.play(Write(h6))
        go2 = np.array([-6.0, 2.2, 0]) + band_shift(6)
        self.play(Create(grid(go2)))
        labs2 = grid_labels(go2)
        self.play(Write(labs2), run_time=2)
        doubles = VGroup(*[labs2[i * 6 + i] for i in range(6)])
        self.play(*[d.animate.set_color(GREEN) for d in doubles])
        d1 = Tex("36 squares, each worth 1 over 36.").scale(0.75).move_to(band_shift(6) + UP * 2.0 + RIGHT * 2.6)
        d2 = Tex("Six 7s on a diagonal: 1 in 6. One 2: 1 in 36. Not eleven equal totals.").scale(0.68).move_to(band_shift(6) + UP * 1.2 + RIGHT * 2.6)
        d3 = Tex("Doubles (green): 1 in 6. Ten or more: six squares, 1 in 6. 7 or 11: 8 squares.").scale(0.66).move_to(band_shift(6) + UP * 0.3 + RIGHT * 2.6)
        d4 = Tex("Works for real counts too: girl and taxi, 12 of 60, which is 1 in 5.").scale(0.68).move_to(band_shift(6) + DOWN * 0.6 + RIGHT * 2.6)
        for m in (d1, d2, d3, d4):
            self.play(Write(m))
            self.wait(2.6)
        self.wait(3)

        # --- Band 7 (subtopic_7): branches
        self.next_band(7)
        h7 = Tex("Branches: multiply along, add across").scale(1.05).move_to(band_shift(7) + UP * 3.2)
        self.play(Write(h7))
        tr3 = tree(np.array([-6.6, 0.4, 0]) + band_shift(7), [("R", "3/5"), ("G", "2/5")], [[("R", "2/4"), ("G", "2/4")], [("R", "3/4"), ("G", "1/4")]], width=2.0, spread=1.8)
        self.play(Create(tr3), run_time=2)
        b1 = Tex("Branches leaving a dot add to 1; all tips add to 1.").scale(0.72).move_to(band_shift(7) + UP * 2.1 + RIGHT * 2.4)
        b2 = Tex("Spinner: RR 1 over 9; one of each 2 over 9 plus 2 over 9, which is 4 over 9.").scale(0.66).move_to(band_shift(7) + UP * 1.2 + RIGHT * 2.4)
        b3 = Tex("Bag, first marble not put back: the second branches change. RR 3 over 10.").scale(0.66).move_to(band_shift(7) + UP * 0.3 + RIGHT * 2.4)
        b4 = Tex("Put it back and the bag resets: RR 9 over 25.").scale(0.72).move_to(band_shift(7) + DOWN * 0.6 + RIGHT * 2.4)
        b5 = Tex("Every way, grid, branches.").scale(0.85).move_to(band_shift(7) + DOWN * 2.2 + RIGHT * 2.4)
        for m in (b1, b2, b3, b4, b5):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(b5, color=YELLOW)))
        self.wait(6)
