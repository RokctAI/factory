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


def spinner(centre, radius, sectors, highlight=(), color=YELLOW):
    """A circle cut into equal sectors by radii; highlighted sectors get a dot."""
    g = VGroup(Circle(radius=radius, color=WHITE).move_to(centre))
    for k in range(sectors):
        ang = TAU * k / sectors + PI / 2
        g.add(Line(centre, centre + radius * np.array([np.cos(ang), np.sin(ang), 0]),
                   color=WHITE, stroke_width=2))
    for k in highlight:
        mid = TAU * (k + 0.5) / sectors + PI / 2
        g.add(Dot(centre + 0.6 * radius * np.array([np.cos(mid), np.sin(mid), 0]), color=color))
    return g


def bar_chart(origin, values, labels, unit=0.18, width=0.5, gap=0.25, color=BLUE):
    """Vertical bars standing on a baseline that starts at origin."""
    g = VGroup()
    n = len(values)
    g.add(Line(origin, origin + RIGHT * (n * (width + gap) + gap), color=WHITE))
    for i, (v, lab) in enumerate(zip(values, labels)):
        x = gap + i * (width + gap) + width / 2
        bar = Rectangle(width=width, height=v * unit, color=color, fill_opacity=0.5)
        bar.move_to(origin + RIGHT * x + UP * v * unit / 2)
        g.add(bar)
        g.add(Tex(lab).scale(0.5).move_to(origin + RIGHT * x + DOWN * 0.25))
        g.add(Tex(str(v)).scale(0.45).move_to(origin + RIGHT * x + UP * (v * unit + 0.2)))
    return g


class RelativeFrequencySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): equally likely outcomes
        title = Tex("Probability: favourable over total").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"P(6) = \tfrac{1}{6} \qquad P(\text{even}) = \tfrac{3}{6} = \tfrac{1}{2} \qquad P(\text{less than } 3) = \tfrac{2}{6} = \tfrac{1}{3}").scale(0.85).shift(UP * 1.5)
        l2 = MathTex(r"\text{Bag: 5 red, 3 blue, 2 yellow} \quad P(R) = \tfrac{5}{10},\; P(B) = \tfrac{3}{10},\; P(Y) = \tfrac{2}{10}").scale(0.8).shift(UP * 0.6)
        l3 = MathTex(r"\tfrac{5}{10} + \tfrac{3}{10} + \tfrac{2}{10} = 1 \qquad P(\text{not blue}) = 1 - \tfrac{3}{10} = \tfrac{7}{10}").scale(0.85).shift(DOWN * 0.3)
        l4 = Tex("0 impossible \\quad 1/2 even chance \\quad 1 certain").scale(0.8).shift(DOWN * 1.2)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        sp = spinner(np.array([4.6, -2.6, 0]), 0.8, 4, highlight=(0,), color=RED)
        sp_lab = Tex("One quarter red: P(red) = 1/4, not 1/2").scale(0.6).move_to(np.array([0.2, -2.6, 0]))
        self.play(Create(sp), Write(sp_lab))
        self.play(Create(SurroundingRectangle(l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): relative frequency table and chart
        self.next_band(1)
        b1_title = Tex("Relative frequency = frequency over trials").scale(1.05).shift(band_shift(1) + UP * 3.1)
        self.play(Write(b1_title))
        self.wait(1.5)
        chart = bar_chart(band_shift(1) + LEFT * 6.4 + DOWN * 1.6, [8, 11, 9, 12, 10, 10],
                          ["1", "2", "3", "4", "5", "6"])
        chart_lab = Tex("60 rolls of a die").scale(0.6).move_to(band_shift(1) + LEFT * 4.2 + DOWN * 2.3)
        self.play(Create(chart), run_time=2)
        self.play(Write(chart_lab))
        r1 = MathTex(r"8 + 11 + 9 + 12 + 10 + 10 = 60").scale(0.75).move_to(band_shift(1) + RIGHT * 2.6 + UP * 1.6)
        r2 = MathTex(r"RF(4) = \tfrac{12}{60} = 0.2 = 20\%").scale(0.8).move_to(band_shift(1) + RIGHT * 2.6 + UP * 0.7)
        r3 = MathTex(r"RF(\text{even}) = \tfrac{33}{60} = 0.55").scale(0.8).move_to(band_shift(1) + RIGHT * 2.6 + DOWN * 0.2)
        r4 = MathTex(r"\text{Coin: } \tfrac{27}{50} = 0.54 \text{ heads}").scale(0.8).move_to(band_shift(1) + RIGHT * 2.6 + DOWN * 1.1)
        r5 = Tex("Divide by the trials, never by the outcomes").scale(0.7).move_to(band_shift(1) + RIGHT * 2.6 + DOWN * 2.0)
        for m in (r1, r2, r3, r4, r5):
            self.play(Write(m))
            self.wait(2.1)
        self.play(Create(SurroundingRectangle(r5, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): predicting frequency
        self.next_band(2)
        b2_title = Tex("Expected frequency = P times n").scale(1.15).shift(band_shift(2) + UP * 2.9)
        self.play(Write(b2_title))
        self.wait(1.5)
        rows = [
            r"\text{Die, 120 rolls: } \tfrac{1}{6} \times 120 = 20 \text{ sixes}",
            r"\text{Bag, 50 draws, replaced: } 25 \text{ red},\; 15 \text{ blue},\; 10 \text{ yellow}",
            r"\text{8 sectors, 200 spins: } \tfrac{3}{8} \times 200 = 75",
            r"\text{Fun day: } \tfrac{1}{8} \times 240 = 30 \text{ prizes},\; 30 \times R15 = R450",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.8).shift(band_shift(2) + UP * (1.7 - 0.85 * i))
            self.play(Write(m))
            self.wait(2.4)
        sp2 = spinner(band_shift(2) + RIGHT * 5.3 + DOWN * 2.2, 0.75, 8, highlight=(2,))
        about = Tex("Always about: 17 or 24 sixes is normal").scale(0.8).shift(band_shift(2) + DOWN * 2.2 + LEFT * 1.0)
        self.play(Create(sp2), Write(about))
        self.play(Create(SurroundingRectangle(about, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): fair experiment
        self.next_band(3)
        b3_title = Tex("A fair experiment").scale(1.2).shift(band_shift(3) + UP * 2.6)
        self.play(Write(b3_title))
        self.wait(1.5)
        f1 = Tex("Same way every trial; trials do not affect each other").scale(0.8).shift(band_shift(3) + UP * 1.4)
        f2 = Tex("Replace the marble and shake the bag").scale(0.8).shift(band_shift(3) + UP * 0.5)
        f3 = Tex("At least 50 trials; tally as it happens").scale(0.8).shift(band_shift(3) + DOWN * 0.4)
        f4 = Tex("Totals row: frequencies make n, relative frequencies make 1").scale(0.8).shift(band_shift(3) + DOWN * 1.3)
        for m in (f1, f2, f3, f4):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(f4, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        e1 = MathTex(r"P(6) = \tfrac{6}{1}").scale(0.9).shift(band_shift(4) + UP * 1.5)
        e2 = Tex("Pass or fail, so P(pass) = 1/2").scale(0.8).shift(band_shift(4) + UP * 0.6)
        e3 = MathTex(r"RF(\text{heads}) = \tfrac{27}{2}").scale(0.9).shift(band_shift(4) + DOWN * 0.3)
        e4 = Tex("No 6 in ten rolls, so a 6 is due").scale(0.8).shift(band_shift(4) + DOWN * 1.2)
        e5 = Tex("Marbles kept out in a same-chance experiment").scale(0.8).shift(band_shift(4) + DOWN * 2.1)
        for m in (e1, e2, e3, e4, e5):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.6)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): ways that win
        self.next_band(5)
        b5_title = Tex("Count the ways that win").scale(1.2).shift(band_shift(5) + UP * 2.6)
        self.play(Write(b5_title))
        self.wait(2)
        s1 = Tex("Ways you want over all the ways (equal ways only)").scale(0.85).shift(band_shift(5) + UP * 1.4)
        s2 = Tex("Die: a 6 is 1 out of 6; even is 3 out of 6, a half").scale(0.85).shift(band_shift(5) + UP * 0.5)
        s3 = Tex("Every chance is between 0 and 1; all of them make 1").scale(0.85).shift(band_shift(5) + DOWN * 0.4)
        s4 = Tex("Lopsided spinner: a quarter red means a chance of a quarter").scale(0.8).shift(band_shift(5) + DOWN * 1.3)
        for m in (s1, s2, s3, s4):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(s1, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): tally what happened
        self.next_band(6)
        b6_title = Tex("Tally what happened").scale(1.2).shift(band_shift(6) + UP * 2.6)
        self.play(Write(b6_title))
        self.wait(2)
        t1 = Tex("Frequency: the count. Relative frequency: count over tries.").scale(0.8).shift(band_shift(6) + UP * 1.4)
        t2 = Tex("12 fours in 60 rolls: 12 over 60, a fifth").scale(0.85).shift(band_shift(6) + UP * 0.5)
        t3 = Tex("27 heads in 50 tosses: 54 percent").scale(0.85).shift(band_shift(6) + DOWN * 0.4)
        t4 = Tex("Drawing pin: 62 point up in 100, best guess 0.62").scale(0.85).shift(band_shift(6) + DOWN * 1.3)
        for m in (t1, t2, t3, t4):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(t1, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): chance times tries
        self.next_band(7)
        b7_title = Tex("Chance times tries").scale(1.2).shift(band_shift(7) + UP * 2.6)
        self.play(Write(b7_title))
        self.wait(2)
        c1 = Tex("A sixth of 120 rolls: about 20 sixes").scale(0.85).shift(band_shift(7) + UP * 1.4)
        c2 = Tex("50 draws, marble back: about 25, 15 and 10").scale(0.85).shift(band_shift(7) + UP * 0.5)
        c3 = Tex("An eighth of 240 players: about 30 prizes, about R450").scale(0.85).shift(band_shift(7) + DOWN * 0.4)
        c4 = Tex("The die has no memory: never due a 6").scale(0.85).shift(band_shift(7) + DOWN * 1.3)
        for m in (c1, c2, c3, c4):
            self.play(Write(m))
            self.wait(2.2)
        c5 = Tex("Count the ways. Tally the tries. Multiply, and say about.").scale(0.85).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(c5))
        self.play(Create(SurroundingRectangle(c5, color=YELLOW)))
        self.wait(4)
