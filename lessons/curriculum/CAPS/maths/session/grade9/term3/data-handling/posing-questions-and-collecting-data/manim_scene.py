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


def dots(origin, rows, cols, spacing=0.22, color=WHITE, radius=0.06):
    """A rows-by-cols grid of small dots standing for members of a population."""
    g = VGroup()
    for i in range(rows):
        for j in range(cols):
            g.add(Dot(origin + RIGHT * spacing * j + DOWN * spacing * i, radius=radius, color=color))
    return g


def flow_diagram(labels, origin, step=2.6, scale=0.6):
    """Boxes joined by arrows, left to right."""
    boxes = VGroup()
    arrows = VGroup()
    for k, lab in enumerate(labels):
        t = Tex(lab).scale(scale).move_to(origin + RIGHT * step * k)
        boxes.add(VGroup(SurroundingRectangle(t, color=BLUE, buff=0.12), t))
    for k in range(len(labels) - 1):
        arrows.add(Arrow(boxes[k].get_right(), boxes[k + 1].get_left(), buff=0.05, color=GREY, stroke_width=3))
    return boxes, arrows


class CollectingDataSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the question
        title = Tex("A question data can answer: variable, group, period").scale(1.0).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        boxes, arrows = flow_diagram(["pose", "collect", "organise", "represent", "interpret", "report"], np.array([-6.2, 2.2, 0]), step=2.45, scale=0.55)
        for b in boxes:
            self.play(Create(b), run_time=0.4)
        for a in arrows:
            self.play(Create(a), run_time=0.25)
        q1 = Tex("Not statistical: how tall is the tallest learner? Is load shedding bad?").scale(0.7).shift(UP * 1.0)
        q2 = Tex("Statistical: how many hours of power did homes in our ward lose last week?").scale(0.7).shift(UP * 0.2)
        q3 = Tex("Categorical: transport mode. Discrete: siblings. Continuous: height, litres.").scale(0.7).shift(DOWN * 0.7)
        q4 = Tex("Fix the unit first: rands to the nearest rand, km to one decimal place.").scale(0.7).shift(DOWN * 1.5)
        for m in (q1, q2, q3, q4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(q2, color=YELLOW)))
        self.wait(4)

        # --- Band 1 (subtopic_2): population and sample
        self.next_band(1)
        h1 = Tex("Population and sample").scale(1.05).move_to(band_shift(1) + UP * 3.2)
        self.play(Write(h1))
        pop = dots(np.array([-6.4, 2.2, 0]) + band_shift(1), 10, 12, color=GREY)
        self.play(Create(pop), run_time=1.5)
        self.play(Write(Tex("population: 1200").scale(0.6).next_to(pop, DOWN, buff=0.15)))
        picked = VGroup(*[pop[20 * k] for k in range(6)])
        self.play(*[d.animate.set_color(YELLOW) for d in picked])
        self.play(Write(Tex("every 20th: systematic").scale(0.55).next_to(pop, DOWN, buff=0.6)))
        s1 = Tex("Census: everyone (Census 2022). Sample: a part that stands in.").scale(0.72).move_to(band_shift(1) + UP * 2.2 + RIGHT * 2.6)
        s2 = Tex("Convenience sample: whoever is nearest. Biased.").scale(0.72).move_to(band_shift(1) + UP * 1.3 + RIGHT * 2.6)
        s3 = Tex("Random: equal chance. Systematic: every 20th. Stratified: 15 per grade.").scale(0.68).move_to(band_shift(1) + UP * 0.4 + RIGHT * 2.6)
        s4 = MathTex(r"\frac{42}{60} = 70\%\ \Rightarrow\ \text{about } 0.7 \times 1200 = 840").scale(0.8).move_to(band_shift(1) + DOWN * 0.6 + RIGHT * 2.6)
        for m in (s1, s2, s3, s4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(s4, color=YELLOW)))
        self.wait(3)

        # --- Band 2 (subtopic_3): sources and methods
        self.next_band(2)
        h2 = Tex("Sources and methods").scale(1.05).move_to(band_shift(2) + UP * 3.2)
        self.play(Write(h2))
        m1 = Tex("Primary: questionnaire, interview, observation, measurement, experiment.").scale(0.7).move_to(band_shift(2) + UP * 2.1)
        m2 = Tex("Secondary: Statistics South Africa, municipality, Weather Service, register.").scale(0.7).move_to(band_shift(2) + UP * 1.3)
        m3 = Tex("Cars at the gate: tally. Water use: meter. Provincial unemployment: QLFS.").scale(0.7).move_to(band_shift(2) + UP * 0.5)
        m4 = Tex("Leading: do you agree prices are far too high? Neutral: how much did you spend?").scale(0.68).move_to(band_shift(2) + DOWN * 0.4)
        m5 = Tex("Ranges 0 to 9, 10 to 19, 20 to 29: no overlap. Pilot on five. Anonymous.").scale(0.7).move_to(band_shift(2) + DOWN * 1.2)
        m6 = Tex("Check a source: who, when, which definition.").scale(0.72).move_to(band_shift(2) + DOWN * 2.0)
        for m in (m1, m2, m3, m4, m5, m6):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(m4, color=YELLOW)))
        self.wait(3)

        # --- Band 3 (subtopic_4): the plan
        self.next_band(3)
        h3 = Tex("The plan").scale(1.05).move_to(band_shift(3) + UP * 3.2)
        self.play(Write(h3))
        plan = [
            "Question: distance (nearest 100 m) and mode of travel, Grade 9, each morning",
            "Population: 300 Grade 9 learners",
            "Sample: 45, 15 per class, every 20th name on each list",
            "Method: four closed questions, piloted on five, anonymous",
            "Variables: distance (continuous), mode (categorical)",
            "Collection: Tuesday register; watch for early-arrival bias",
        ]
        y = 2.2
        for p in plan:
            self.play(Write(Tex(p).scale(0.65).move_to(band_shift(3) + UP * y)))
            self.wait(2.0)
            y -= 0.75
        self.wait(4)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        h4 = Tex("Error museum").scale(1.05).move_to(band_shift(4) + UP * 3.2)
        self.play(Write(h4))
        e1 = Tex("Do learners like school transport?").scale(0.8).move_to(band_shift(4) + UP * 1.8)
        e2 = Tex("First 20 through the gate: representative").scale(0.8).move_to(band_shift(4) + UP * 0.6)
        e3 = Tex("70\\% of the sample, so exactly 840 learners").scale(0.8).move_to(band_shift(4) + DOWN * 0.6)
        for m in (e1, e2, e3):
            self.play(Write(m))
            self.wait(1.5)
            self.play(Create(strike(m)))
            self.wait(1.5)
        fix = Tex("Variable, group, period; a fair sample; about, not exactly; source and date.").scale(0.7).move_to(band_shift(4) + DOWN * 2.2)
        self.play(Write(fix))
        self.play(Create(SurroundingRectangle(fix, color=GREEN)))
        self.wait(5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): countable question
        self.next_band(5)
        h5 = Tex("Ask a question you can actually count").scale(1.05).move_to(band_shift(5) + UP * 3.2)
        self.play(Write(h5))
        g1 = Tex("Opinion: is load shedding bad? Countable: hours of power lost, our street, last week.").scale(0.68).move_to(band_shift(5) + UP * 2.0)
        g2 = Tex("What, who, when.").scale(0.95).move_to(band_shift(5) + UP * 1.0)
        g3 = Tex("Groups with names: categorical. Whole-step counts: discrete. Scale measures: continuous.").scale(0.66).move_to(band_shift(5) + UP * 0.1)
        g4 = Tex("Fix the unit, or half the page says 2 km and half says 20 minutes.").scale(0.7).move_to(band_shift(5) + DOWN * 0.8)
        for m in (g1, g2, g3, g4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(g2, color=YELLOW)))
        self.wait(4)

        # --- Band 6 (subtopic_6): soup
        self.next_band(6)
        h6 = Tex("Tasting the soup: stir first").scale(1.05).move_to(band_shift(6) + UP * 3.2)
        self.play(Write(h6))
        pot = Arc(radius=1.6, start_angle=PI, angle=PI, color=WHITE, stroke_width=4).move_arc_center_to(band_shift(6) + LEFT * 4.6 + DOWN * 0.4)
        rim = Line(band_shift(6) + LEFT * 6.2 + DOWN * 0.4, band_shift(6) + LEFT * 3.0 + DOWN * 0.4, color=WHITE, stroke_width=4)
        self.play(Create(pot), Create(rim))
        salt = dots(band_shift(6) + LEFT * 5.2 + DOWN * 1.4, 2, 6, spacing=0.2, color=YELLOW, radius=0.04)
        self.play(Create(salt))
        self.play(Write(Tex("salt at the bottom").scale(0.5).next_to(pot, DOWN, buff=0.15)))
        t1 = Tex("Pot: population. Spoonful: sample.").scale(0.78).move_to(band_shift(6) + UP * 2.0 + RIGHT * 2.4)
        t2 = Tex("Unstirred spoon: only Grade 12s, only the soccer team, only who is near.").scale(0.66).move_to(band_shift(6) + UP * 1.1 + RIGHT * 2.4)
        t3 = Tex("Stir: random (hat), systematic (every 20th), stratified (15 per grade).").scale(0.66).move_to(band_shift(6) + UP * 0.2 + RIGHT * 2.4)
        t4 = Tex("42 of 60 walk: 70\\%, so ABOUT 840 of 1200.").scale(0.75).move_to(band_shift(6) + DOWN * 0.7 + RIGHT * 2.4)
        for m in (t1, t2, t3, t4):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(t4, color=YELLOW)))
        self.wait(3)

        # --- Band 7 (subtopic_7): sources
        self.next_band(7)
        h7 = Tex("Where the numbers come from").scale(1.05).move_to(band_shift(7) + UP * 3.2)
        self.play(Write(h7))
        w1 = Tex("Yours: primary. Borrowed: secondary (Stats SA, municipality, Weather Service).").scale(0.68).move_to(band_shift(7) + UP * 2.0)
        w2 = Tex("Cars at the gate: tally. Water: read the meter. Province: Stats SA, and say so.").scale(0.68).move_to(band_shift(7) + UP * 1.1)
        w3 = Tex("Fair questionnaire: neutral wording, ranges that do not overlap, try it on five.").scale(0.68).move_to(band_shift(7) + UP * 0.2)
        w4 = Tex("Borrowed numbers: who, when, what exactly they counted.").scale(0.72).move_to(band_shift(7) + DOWN * 0.7)
        w5 = Tex("Countable question, stirred spoonful, honest source.").scale(0.85).move_to(band_shift(7) + DOWN * 2.0)
        for m in (w1, w2, w3, w4, w5):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(w5, color=YELLOW)))
        self.wait(6)
