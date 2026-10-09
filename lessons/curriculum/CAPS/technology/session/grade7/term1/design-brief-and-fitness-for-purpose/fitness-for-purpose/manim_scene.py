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

# Band-layout whiteboard scene for fitness-for-purpose (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (210/170/200/110/110/110 of 910 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FitnessForPurposeSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Users, purpose, function, cost
        self.write_rows(0, "Users, purpose, function, cost", [
            "Users: who, and what are they like",
            "Purpose: the need; function: does it do it",
            "Cost-effectiveness is value, not cheapness",
            "Spreader: costly, yet a bargain",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Safety, ergonomics, aesthetics
        self.next_band(1)
        self.write_rows(1, "Safety, ergonomics, aesthetics", [
            "Safety: can it harm anyone",
            "Paraffin stove: works, but burns homes",
            "Ergonomics: fits the body and the grip",
            "Aesthetics serves the job: red to be found",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Impact on society and environment
        self.next_band(2)
        self.write_rows(2, "Impact on society and environment", [
            "Society: jobs, fairness, who waits for rescue",
            "Environment: materials, energy, waste",
            "Chair in a landfill for centuries",
            "All eight applied to the rescue device",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Function alone decides fitness''",
            "``Cost-effective means cheapest''",
            "``Aesthetics is not serious''",
            "``Only the user matters''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Does it do the job, and for whom
        self.next_band(4)
        self.write_rows(4, "Does it do the job, and for whom", [
            "Who uses it",
            "Why it exists",
            "Does it actually work",
            "Worth the money, not just cheap",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Safe, comfortable, good to look at
        self.next_band(5)
        self.write_rows(5, "Safe, comfortable, good to look at", [
            "Working but dangerous: not fit",
            "Feet on the floor, handles in gloves",
            "Looks that help the job",
            "They pull against each other",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): What about everyone else
        self.next_band(6)
        self.write_rows(6, "What about everyone else", [
            "Neighbours, jobs, hospitals",
            "Materials, smoke, rubbish",
            "Our device: water, flat base, recycle",
            "Eight questions, one judgement",
        ], scale=0.9, box=3)

        last = Tex("Fit for purpose is all eight considerations balanced, and the designer says what was traded.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
