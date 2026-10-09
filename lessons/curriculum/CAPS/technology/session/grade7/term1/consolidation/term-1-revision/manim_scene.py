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

# Band-layout whiteboard scene for term-1-revision (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (210/160/190/110/110/110 of 890 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class Term1RevisionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.8, box=None, box_color=YELLOW):
        t = Tex(title).scale(1.15).shift(band_shift(k) + UP * 2.4)
        self.play(Write(t))
        self.wait(1.5)
        made = []
        for i, r in enumerate(rows):
            m = Tex(r).scale(scale).shift(band_shift(k) + UP * (1.3 - 0.95 * i))
            self.play(Write(m))
            self.wait(2.3)
            made.append(m)
        if box is not None:
            self.play(Create(SurroundingRectangle(made[box], color=box_color)))
            self.wait(2)
        return made

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(42)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The process and the problem
        self.write_rows(0, "The process and the problem", [
            "Need: trapped people, large controlled force",
            "IDMEC: a loop, not a line",
            "Brief; specifications test, constraints limit",
            "Fit for purpose: eight considerations",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Levers and fluids
        self.next_band(1)
        self.write_rows(1, "Levers and fluids", [
            "MA = load divided by effort; distance is the price",
            "Middle: pivot 1st, load 2nd, effort 3rd",
            "Pressure spreads; bigger face, bigger force",
            "Liquid firm and instant, air springy and late",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Drawing and the confusions
        self.next_band(2)
        self.write_rows(2, "Drawing and the confusions", [
            "Dark, feint, dashed, chain; mm, each once",
            "Working drawing to make, oblique to show",
            "Load vs effort, spec vs constraint, value vs cheap",
            "Evaluation measures against the brief",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``mm after every dimension''",
            "``Classify a lever by its shape''",
            "``Hydraulics creates force''",
            "``Evaluate without the brief''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): The story of the term
        self.next_band(4)
        self.write_rows(4, "The story of the term", [
            "A need, written as a problem",
            "Five steps, round and round",
            "The brief is the promise",
            "Eight checks for fitness",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Two ways to multiply a push
        self.next_band(5)
        self.write_rows(5, "Two ways to multiply a push", [
            "Lever: far from the pivot, stronger",
            "Sort by what is in the middle",
            "Fluid: small piston to big piston",
            "Water firm, air spongy",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Drawing it, not mixing it up
        self.next_band(6)
        self.write_rows(6, "Drawing it, not mixing it up", [
            "Line rules, scale, millimetres",
            "Make with the working drawing, show with oblique",
            "Seven pairs, one sentence each",
            "You built all of this",
        ], scale=0.9, box=3)

        last = Tex("One need, one loop, two force multipliers, two drawings, one tested model: that is Term 1.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
