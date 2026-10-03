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


def dotline(values, origin, unit=1.0, color=WHITE, lo=0.0):
    """Dots on a number line at the given values, stacked when repeated."""
    g = VGroup()
    seen = {}
    for v in values:
        k = seen.get(v, 0)
        seen[v] = k + 1
        g.add(Dot(origin + RIGHT * unit * (v - lo) + UP * 0.2 * k, radius=0.07, color=color))
    return g


def target(centre, radius=1.0):
    return VGroup(*[Circle(radius=radius * r, color=GREY, stroke_width=2).move_to(centre) for r in (1.0, 0.66, 0.33)])


def scatter(centre, offsets, color=YELLOW):
    return VGroup(*[Dot(centre + np.array([dx, dy, 0]), radius=0.06, color=color) for dx, dy in offsets])


class ErrorBiasSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): random error vs bias
        title = Tex("Random error scatters; bias leans").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        t1c = np.array([-5.0, -0.6, 0])
        t2c = np.array([-1.6, -0.6, 0])
        t3c = np.array([1.8, -0.6, 0])
        for c in (t1c, t2c, t3c):
            self.play(Create(target(c)), run_time=0.5)
        self.play(Create(scatter(t1c, [(0.4, 0.5), (-0.5, 0.3), (0.2, -0.6), (-0.3, -0.4), (0.6, -0.1)])))
        self.play(Write(Tex("random: scattered, accurate on average").scale(0.45).next_to(target(t1c), DOWN, buff=0.15)))
        self.play(Create(scatter(t2c, [(0.6, 0.6), (0.7, 0.5), (0.5, 0.7), (0.65, 0.65), (0.55, 0.55)], color=RED)))
        self.play(Write(Tex("bias: precise and wrong").scale(0.45).next_to(target(t2c), DOWN, buff=0.15)))
        self.play(Create(scatter(t3c, [(0.05, 0.05), (-0.05, 0.08), (0.08, -0.04), (-0.06, -0.06), (0.0, 0.0)], color=GREEN)))
        self.play(Write(Tex("precise and accurate").scale(0.45).next_to(target(t3c), DOWN, buff=0.15)))
        e1 = Tex("Stopwatch 14.2, 14.5, 14.3, 14.4, 14.1: both sides of the truth, averages out.").scale(0.62).shift(UP * 2.3)
        e2 = Tex("All watches started late: every time too short; averaging a thousand gives a precise wrong answer.").scale(0.58).shift(UP * 1.7)
        e3 = Tex("Bigger sample fixes random error, never bias. Small fair beats large biased.").scale(0.62).shift(DOWN * 2.6)
        for m in (e1, e2, e3):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(e3, color=YELLOW)))
        self.wait(3)

        # --- Band 1 (subtopic_2): collection bias
        self.next_band(1)
        h1 = Tex("Bias in collecting: who was asked, who answered, how").scale(1.0).move_to(band_shift(1) + UP * 3.2)
        self.play(Write(h1))
        b1 = Tex("SMS poll: 4 000 self-selected listeners, 78\\%. Stratified 1 000 adults: 41\\%.").scale(0.68).move_to(band_shift(1) + UP * 2.1)
        b2 = Tex("Selection and self-selection lean towards strong opinions. Size does not cure it.").scale(0.66).move_to(band_shift(1) + UP * 1.3)
        b3 = Tex("Non-response: 60 of 300 returned, leaning towards the organised.").scale(0.68).move_to(band_shift(1) + UP * 0.5)
        b4 = Tex("Wording: far too high? pushes yes. Order: anger carries over.").scale(0.68).move_to(band_shift(1) + DOWN * 0.3)
        b5 = Tex("Owner at the counter: 45 of 50 happy. Anonymous in class: 28 of 50, which is 56\\%.").scale(0.66).move_to(band_shift(1) + DOWN * 1.1)
        b6 = Tex("Timing: the 7 a.m. gate misses the long journeys.").scale(0.68).move_to(band_shift(1) + DOWN * 1.9)
        for m in (b1, b2, b3, b4, b5, b6):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2, color=YELLOW)))
        self.wait(3)

        # --- Band 2 (subtopic_3): summarising errors
        self.next_band(2)
        h2 = Tex("Errors after collection").scale(1.05).move_to(band_shift(2) + UP * 3.2)
        self.play(Write(h2))
        base = band_shift(2) + LEFT * 6.4 + UP * 1.4
        self.play(Create(Line(base, base + RIGHT * 6.4, color=GREY, stroke_width=3)))
        vals = [280, 300, 310, 290, 350, 320, 305, 295, 330, 320]
        self.play(Create(dotline(vals, base + UP * 0.2, unit=0.02, lo=0)))
        bad = Dot(base + RIGHT * 0.02 * 35 + UP * 0.2, radius=0.09, color=RED)
        self.play(Create(bad))
        self.play(Write(Tex("35?").scale(0.5).next_to(bad, UP, buff=0.1)))
        s1 = MathTex(r"\text{mean} = \frac{3100}{10} = 310;\quad \text{with } 35:\ \frac{2785}{10} = 278.5").scale(0.8).move_to(band_shift(2) + UP * 0.3)
        s2 = Tex("A value that does not belong is a recording question first.").scale(0.7).move_to(band_shift(2) + DOWN * 0.5)
        s3 = Tex("Mean income R18 000 with a few very high earners: report the median.").scale(0.68).move_to(band_shift(2) + DOWN * 1.3)
        s4 = Tex("Streetlights and crime: association, not cause; wealth may drive both.").scale(0.68).move_to(band_shift(2) + DOWN * 2.1)
        for m in (s1, s2, s3, s4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(s1, color=YELLOW)))
        self.wait(3)

        # --- Band 3 (subtopic_4): audit
        self.next_band(3)
        h3 = Tex("Auditing a report").scale(1.05).move_to(band_shift(3) + UP * 3.2)
        self.play(Write(h3))
        qs = [
            "Population and sample: who, how, how many?",
            "Collection: instrument and wording?",
            "Measurement: units and recording checks?",
            "Summary: the right statistic for the shape?",
            "Graphs: honest scale, intervals, comparisons?",
            "Conclusion: follows, with caution? Limitations admitted?",
        ]
        y = 2.1
        for q in qs:
            self.play(Write(Tex(q).scale(0.68).move_to(band_shift(3) + UP * y)))
            self.wait(1.8)
            y -= 0.7
        v1 = Tex("For each problem: name, direction, evidence, fix.").scale(0.78).move_to(band_shift(3) + DOWN * 2.3)
        self.play(Write(v1))
        self.play(Create(SurroundingRectangle(v1, color=YELLOW)))
        self.wait(4)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        h4 = Tex("Error museum").scale(1.05).move_to(band_shift(4) + UP * 3.2)
        self.play(Write(h4))
        x1 = Tex("4 000 replies must beat 1 000").scale(0.8).move_to(band_shift(4) + UP * 1.8)
        x2 = Tex("35 litres is just a low user").scale(0.8).move_to(band_shift(4) + UP * 0.6)
        x3 = Tex("More lights, less crime, so lights cut crime").scale(0.8).move_to(band_shift(4) + DOWN * 0.6)
        for m in (x1, x2, x3):
            self.play(Write(m))
            self.wait(1.5)
            self.play(Create(strike(m)))
            self.wait(1.5)
        fix = Tex("Fair beats big; check the source; association is not cause; admit limitations.").scale(0.66).move_to(band_shift(4) + DOWN * 2.2)
        self.play(Write(fix))
        self.play(Create(SurroundingRectangle(fix, color=GREEN)))
        self.wait(5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): noise and lean
        self.next_band(5)
        h5 = Tex("Noise and lean").scale(1.05).move_to(band_shift(5) + UP * 3.2)
        self.play(Write(h5))
        n1 = Tex("Noise: wobble on both sides, cancels when you average; bigger sample, less noise.").scale(0.64).move_to(band_shift(5) + UP * 2.0)
        n2 = Tex("Lean: a tilt in the method; bigger sample, same tilt, more confidence.").scale(0.66).move_to(band_shift(5) + UP * 1.1)
        n3 = Tex("Fix noise by repeating and averaging. Fix lean by fixing the method.").scale(0.68).move_to(band_shift(5) + UP * 0.2)
        n4 = Tex("Precise: readings agree with each other. Accurate: they agree with the truth.").scale(0.66).move_to(band_shift(5) + DOWN * 0.7)
        n5 = Tex("Small and fair is wobbly but honest. Huge and tilted is confident and wrong.").scale(0.66).move_to(band_shift(5) + DOWN * 1.6)
        for m in (n1, n2, n3, n4, n5):
            self.play(Write(m))
            self.wait(2.5)
        self.play(Create(SurroundingRectangle(n5, color=YELLOW)))
        self.wait(3)

        # --- Band 6 (subtopic_6): who asked
        self.next_band(6)
        h6 = Tex("Who asked, who answered, how they asked").scale(1.05).move_to(band_shift(6) + UP * 3.2)
        self.play(Write(h6))
        w1 = Tex("Who answered: 4 000 who chose themselves, leaning loud. 1 000 chosen fairly wins.").scale(0.64).move_to(band_shift(6) + UP * 2.0)
        w2 = Tex("60 of 300 forms returned: the organised answered.").scale(0.7).move_to(band_shift(6) + UP * 1.1)
        w3 = Tex("How they asked: far too high? and are the prices reasonable? both lean.").scale(0.66).move_to(band_shift(6) + UP * 0.2)
        w4 = Tex("Who asked: the owner at the counter, 45 of 50. Anonymous: 28 of 50.").scale(0.68).move_to(band_shift(6) + DOWN * 0.7)
        w5 = Tex("Name the lean and its direction every time.").scale(0.78).move_to(band_shift(6) + DOWN * 1.7)
        for m in (w1, w2, w3, w4, w5):
            self.play(Write(m))
            self.wait(2.5)
        self.play(Create(SurroundingRectangle(w5, color=YELLOW)))
        self.wait(3)

        # --- Band 7 (subtopic_7): sums and pictures
        self.next_band(7)
        h7 = Tex("Check the sums and the picture").scale(1.05).move_to(band_shift(7) + UP * 3.2)
        self.play(Write(h7))
        c1 = MathTex(r"350 \to 35:\quad 310 \to 278.5").scale(0.9).move_to(band_shift(7) + UP * 2.0)
        c2 = Tex("The value that does not belong is a recording question first.").scale(0.7).move_to(band_shift(7) + UP * 1.1)
        c3 = Tex("Wrong middle: mean R18 000, median for the typical household.").scale(0.7).move_to(band_shift(7) + UP * 0.2)
        c4 = Tex("Crooked pictures: chopped axis, pie of 362, unequal bands, counts across sizes.").scale(0.64).move_to(band_shift(7) + DOWN * 0.7)
        c5 = Tex("Together is not because.").scale(0.9).move_to(band_shift(7) + DOWN * 1.6)
        c6 = Tex("Noise and lean; who asked, answered, how; sums and pictures.").scale(0.7).move_to(band_shift(7) + DOWN * 2.5)
        for m in (c1, c2, c3, c4, c5, c6):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(c5, color=YELLOW)))
        self.wait(6)
