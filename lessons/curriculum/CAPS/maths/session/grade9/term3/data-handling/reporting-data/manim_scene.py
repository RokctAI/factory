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


def flow_diagram(labels, origin, step=1.75, scale=0.5):
    boxes = VGroup()
    arrows = VGroup()
    for k, lab in enumerate(labels):
        t = Tex(lab).scale(scale).move_to(origin + RIGHT * step * k)
        boxes.add(VGroup(SurroundingRectangle(t, color=BLUE, buff=0.1), t))
    for k in range(len(labels) - 1):
        arrows.add(Arrow(boxes[k].get_right(), boxes[k + 1].get_left(), buff=0.04, color=GREY, stroke_width=3))
    return boxes, arrows


def table(rows, origin, col_w=1.1, row_h=0.5, scale=0.55):
    g = VGroup()
    for i, row in enumerate(rows):
        for j, cell in enumerate(row):
            g.add(Tex(cell).scale(scale).move_to(origin + RIGHT * col_w * j + DOWN * row_h * i))
    return g


def three_boxes(origin, texts, w=3.6, scale=0.6):
    g = VGroup()
    for k, (lab, body) in enumerate(texts):
        box = Rectangle(width=w, height=1.1, color=YELLOW, stroke_width=3).move_to(origin + RIGHT * (w + 0.3) * k)
        g.add(box, Tex(lab).scale(0.5).move_to(box.get_top() + DOWN * 0.22), Tex(body).scale(scale).move_to(box.get_center() + DOWN * 0.15))
    return g


class ReportingDataSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the shape of a report
        title = Tex("The data report: eight parts in order").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        boxes, arrows = flow_diagram(["question", "method", "data", "statistics", "findings", "predictions", "limitations", "answer"], np.array([-6.3, 2.0, 0]), step=1.8, scale=0.45)
        for b in boxes:
            self.play(Create(b), run_time=0.35)
        for a in arrows:
            self.play(Create(a), run_time=0.2)
        tw = table([["", "walk", "taxi", "car", "total"], ["boys", "18", "9", "3", "30"], ["girls", "15", "12", "3", "30"], ["total", "33", "21", "6", "60"]], np.array([-5.4, 0.6, 0]), col_w=1.0, row_h=0.5)
        self.play(Write(tw))
        r1 = Tex("Population 300 Grade 9s; sample 60, 20 per class, every 15th name;").scale(0.62).move_to(np.array([2.4, 0.6, 0]))
        r2 = Tex("anonymous two-item questionnaire during register on a Tuesday.").scale(0.62).move_to(np.array([2.4, 0.0, 0]))
        r3 = Tex("Every number in the findings traces back to this table.").scale(0.7).move_to(np.array([0.0, -2.4, 0]))
        for m in (r1, r2, r3):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(r3, color=YELLOW)))
        self.wait(3)

        # --- Band 1 (subtopic_2): findings
        self.next_band(1)
        h1 = Tex("Findings: claim fused to its number").scale(1.05).move_to(band_shift(1) + UP * 3.2)
        self.play(Write(h1))
        f1 = Tex("Walking is the most common mode: 33 of 60, which is 55\\%.").scale(0.72).move_to(band_shift(1) + UP * 2.1)
        f2 = Tex("Girls use taxis more: 12 of 30 (40\\%) against 9 of 30 (30\\%).").scale(0.72).move_to(band_shift(1) + UP * 1.3)
        f3 = Tex("Boys walk more: 18 of 30 (60\\%) against 15 of 30 (50\\%). Car: 3 of 30 each.").scale(0.68).move_to(band_shift(1) + UP * 0.5)
        f4 = Tex("Spending: median 12 rands, because 60 is an outlier pulling the mean to 17.25.").scale(0.66).move_to(band_shift(1) + DOWN * 0.4)
        f5 = Tex("Wording matches strength: 55 vs 35 is clear; 40 vs 30 is somewhat.").scale(0.68).move_to(band_shift(1) + DOWN * 1.3)
        for m in (f1, f2, f3, f4, f5):
            self.play(Write(m))
            self.wait(2.5)
        self.play(Create(SurroundingRectangle(f5, color=YELLOW)))
        self.wait(3)

        # --- Band 2 (subtopic_3): predictions and outliers
        self.next_band(2)
        h2 = Tex("Predictions with about; extremes and outliers reported").scale(1.0).move_to(band_shift(2) + UP * 3.2)
        self.play(Write(h2))
        p1 = MathTex(r"55\% \text{ of } 300 \approx 165,\quad 35\% \approx 105,\quad 10\% \approx 30").scale(0.85).move_to(band_shift(2) + UP * 2.1)
        p2 = Tex("About, because 60 learners cannot pin 300 to the learner; whole school needs more caution.").scale(0.6).move_to(band_shift(2) + UP * 1.3)
        p3 = Tex("Trend: 420 to 480 is up 60, so July about 540, but winter peaks.").scale(0.7).move_to(band_shift(2) + UP * 0.5)
        p4 = Tex("Extremes answer real questions: furthest traveller, heaviest user, lowest mark.").scale(0.66).move_to(band_shift(2) + DOWN * 0.4)
        p5 = Tex("Outlier 60: checked, genuine, kept, effect stated. Error 35: checked, corrected to 350, recalculated.").scale(0.6).move_to(band_shift(2) + DOWN * 1.3)
        for m in (p1, p2, p3, p4, p5):
            self.play(Write(m))
            self.wait(2.5)
        self.play(Create(SurroundingRectangle(p1, color=YELLOW)))
        self.wait(3)

        # --- Band 3 (subtopic_4): limitations
        self.next_band(3)
        h3 = Tex("Limitations with directions; the recommendation").scale(1.05).move_to(band_shift(3) + UP * 3.2)
        self.play(Write(h3))
        l1 = Tex("Grade 9 only: whole-school predictions assume other grades are similar.").scale(0.66).move_to(band_shift(3) + UP * 2.1)
        l2 = Tex("One Tuesday: absent long-distance learners missed, walking pushed slightly up.").scale(0.66).move_to(band_shift(3) + UP * 1.3)
        l3 = Tex("Sampling error: another 60 could land several points from 55\\%.").scale(0.66).move_to(band_shift(3) + UP * 0.5)
        l4 = Tex("Reduced: anonymous closed questions; stratified across three classes.").scale(0.66).move_to(band_shift(3) + DOWN * 0.3)
        l5 = Tex("Answer: most Grade 9s walk; plan for about 165; survey all grades before whole-school plans.").scale(0.62).move_to(band_shift(3) + DOWN * 1.3)
        for m in (l1, l2, l3, l4, l5):
            self.play(Write(m))
            self.wait(2.5)
        self.play(Create(SurroundingRectangle(l5, color=YELLOW)))
        self.wait(3)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        h4 = Tex("Error museum").scale(1.05).move_to(band_shift(4) + UP * 3.2)
        self.play(Write(h4))
        e1 = Tex("Most learners walk.").scale(0.85).move_to(band_shift(4) + UP * 1.8)
        e2 = Tex("165 learners walk to school.").scale(0.85).move_to(band_shift(4) + UP * 0.6)
        e3 = Tex("Girls prefer taxis because they feel unsafe walking.").scale(0.8).move_to(band_shift(4) + DOWN * 0.6)
        for m in (e1, e2, e3):
            self.play(Write(m))
            self.wait(1.5)
            self.play(Create(strike(m)))
            self.wait(1.5)
        fix = Tex("Number with every claim; about with every prediction; nothing the data never asked.").scale(0.66).move_to(band_shift(4) + DOWN * 2.2)
        self.play(Write(fix))
        self.play(Create(SurroundingRectangle(fix, color=GREEN)))
        self.wait(5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): story in order
        self.next_band(5)
        h5 = Tex("Tell the story in order").scale(1.05).move_to(band_shift(5) + UP * 3.2)
        self.play(Write(h5))
        chapters = ["1 question", "2 how you got the data", "3 table and graph", "4 middles and spreads, and why",
                    "5 what you found", "6 what you predict", "7 what could have gone wrong", "8 your answer"]
        y = 2.1
        for k, c in enumerate(chapters):
            self.play(Write(Tex(c).scale(0.62).move_to(band_shift(5) + UP * y + LEFT * 3.2 * (1 if k < 4 else -1))), run_time=0.5)
            self.wait(0.9)
            y -= 0.6
            if k == 3:
                y = 2.1
        s1 = Tex("Two or three sentences each. Skip one and the story has a hole.").scale(0.7).move_to(band_shift(5) + DOWN * 1.0)
        s2 = Tex("Every number in your sentences must be findable in your table.").scale(0.72).move_to(band_shift(5) + DOWN * 1.9)
        for m in (s1, s2):
            self.play(Write(m))
            self.wait(2.6)
        self.play(Create(SurroundingRectangle(s2, color=YELLOW)))
        self.wait(3)

        # --- Band 6 (subtopic_6): claim number caution
        self.next_band(6)
        h6 = Tex("Claim, number, caution").scale(1.05).move_to(band_shift(6) + UP * 3.2)
        self.play(Write(h6))
        tb = three_boxes(band_shift(6) + LEFT * 3.9 + UP * 1.6, [("claim", "walking is most common"), ("number", "33 of 60, which is 55\\%"), ("caution", "Grade 9 only")], w=3.6, scale=0.55)
        self.play(Create(tb))
        tb2 = three_boxes(band_shift(6) + LEFT * 3.9 + UP * 0.1, [("claim", "girls use taxis more"), ("number", "40\\% against 30\\%"), ("caution", "3 in 30; could shrink")], w=3.6, scale=0.55)
        self.play(Create(tb2))
        c1 = Tex("Typical spend: median 12. Why not the mean? The giant at 60 pulls it to 17.25.").scale(0.66).move_to(band_shift(6) + DOWN * 1.2)
        c2 = Tex("The giant gets his own sentence: checked, real, kept, effect reported.").scale(0.68).move_to(band_shift(6) + DOWN * 2.0)
        for m in (c1, c2):
            self.play(Write(m))
            self.wait(2.6)
        self.wait(3)

        # --- Band 7 (subtopic_7): forecast rule
        self.next_band(7)
        h7 = Tex("The weather forecast rule").scale(1.05).move_to(band_shift(7) + UP * 3.2)
        self.play(Write(h7))
        w1 = Tex("Never it will rain; always 70\\% chance of rain. Never 165; always about 165.").scale(0.68).move_to(band_shift(7) + UP * 2.1)
        w2 = MathTex(r"0.55 \times 300 \approx 165,\quad 0.35 \times 300 \approx 105,\quad 0.10 \times 300 \approx 30").scale(0.8).move_to(band_shift(7) + UP * 1.3)
        w3 = Tex("Trend: July about 540, and say why it might not happen.").scale(0.7).move_to(band_shift(7) + UP * 0.5)
        w4 = Tex("What could have gone wrong, each with its direction; and what you did right.").scale(0.66).move_to(band_shift(7) + DOWN * 0.4)
        w5 = Tex("Story in order, claim-number-caution, the forecast rule.").scale(0.8).move_to(band_shift(7) + DOWN * 1.6)
        for m in (w1, w2, w3, w4, w5):
            self.play(Write(m))
            self.wait(2.5)
        self.play(Create(SurroundingRectangle(w5, color=YELLOW)))
        self.wait(6)
