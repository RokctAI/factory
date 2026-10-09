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

# Band-layout whiteboard scene for investigating-the-scenario-and-possible-mechanisms (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/180/160/120/110/90 of 850 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class InvestigatingTheScenarioAndPossibleMechanismsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Reading the Scenario: A Machine to Solve a Real Need
        self.write_rows(0, "Reading the Scenario: A Machine to Solve a Real Need", [
            "Scenario -> facts: load, height, frequency",
            "User, place, limits, budget",
            "Each fact rules options in or out",
            "Existing solutions: forklift, hoist, tackle, winch",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Matching Mechanisms to Jobs: Lift, Move, Turn, Hold
        self.next_band(1)
        self.write_rows(1, "Matching Mechanisms to Jobs: Lift, Move, Turn, Hold", [
            "Lift: tackle, jack, worm winch, lever",
            "Move: rack, trolley, boom; input: crank, pedal",
            "Guide: frame or scissor platform",
            "Table: MA, travel, speed, cost, problem",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Choosing Controls and Recording the Investigation
        self.next_band(2)
        self.write_rows(2, "Choosing Controls and Recording the Investigation", [
            "Hazard -> control: fall -> ratchet / worm",
            "Slide -> stop; pinch -> guard; top -> limit",
            "Ergonomics: measure force, handle height",
            "Summary: need, numbers, shortlist, questions",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Drawing before the facts are known''",
            "``Mechanism chosen for cleverness, not fit''",
            "``No control against the load falling''",
            "``Budget and doorway ignored until building''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): What Does the Machine Have to Do?
        self.next_band(4)
        self.write_rows(4, "What Does the Machine Have to Do?", [
            "500 N up 900 mm, 20 times a week",
            "Alone, children, narrow door, no power",
            "Advantage 3 to 4 needed",
            "Too big, too costly: useful to know",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Pick the Right Part for Each Job
        self.next_band(5)
        self.write_rows(5, "Pick the Right Part for Each Job", [
            "Lift, move, input, guide",
            "Tackle 4, jack 50 short, winch 30 holds",
            "Crank beats rope",
            "The table is the investigation",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Write It Down Before You Draw
        self.next_band(6)
        self.write_rows(6, "Write It Down Before You Draw", [
            "Load must never fall",
            "Measure the owner",
            "Do not block the door",
            "One page before any drawing",
        ], scale=0.9, box=3)

        last = Tex("Investigate first: state the need in numbers, match mechanisms to each part of the job, pair every hazard with a control, and write it down.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
