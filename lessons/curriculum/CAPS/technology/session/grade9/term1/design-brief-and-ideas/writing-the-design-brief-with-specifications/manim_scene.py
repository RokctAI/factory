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

# Band-layout whiteboard scene for writing-the-design-brief-with-specifications (Part 1 Expert
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


class WritingTheDesignBriefWithSpecificationsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What a Design Brief Is and Is Not
        self.write_rows(0, "What a Design Brief Is and Is Not", [
            "What, for whom, where, why",
            "Facts of the site: rise 600, space 12 x 4",
            "Not the answer: no step count, no route",
            "Could a stranger design from it?",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Specifications: What the Stairs and Ramp Must Be
        self.next_band(1)
        self.write_rows(1, "Specifications: What the Stairs and Ramp Must Be", [
            "1 in 12 or gentler; 1 200 wide",
            "Equal risers 150-180; treads 250",
            "Rails 900-1 000 both sides, +300",
            "Landings 1 200; kerb 75; non-slip",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Constraints and Design Considerations
        self.next_band(2)
        self.write_rows(2, "Constraints and Design Considerations", [
            "Constraints: space, budget, materials, time, law",
            "Considerations: purpose, safety, cost, ergonomics, looks",
            "Specs tested after; constraints shape before",
            "Three kinds, one yardstick",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Brief that is a finished design''",
            "``Specifications without numbers''",
            "``Budget written as a specification''",
            "``Model constraints forgotten''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): One Short Statement of the Job
        self.next_band(4)
        self.write_rows(4, "One Short Statement of the Job", [
            "Short and exact",
            "Who, where, why",
            "Facts in, answer out",
            "Stranger test",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): The Must-Be List
        self.next_band(5)
        self.write_rows(5, "The Must-Be List", [
            "Must-be list",
            "Yes or no at the end",
            "Numbers wherever possible",
            "Nice is a wish",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): The Limits and the Values
        self.next_band(6)
        self.write_rows(6, "The Limits and the Values", [
            "Limits you did not pick",
            "Values you judge by",
            "Model has constraints too",
            "Yardstick for the PAT",
        ], scale=0.9, box=3)

        last = Tex("A brief states the job without the answer; specifications are testable, constraints are limits, considerations are values, and together they judge every idea.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
