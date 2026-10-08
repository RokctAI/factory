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

# Band-layout whiteboard scene for making-the-jaws-of-life-model (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (240/180/170/110/110/110 of 920 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MakingTheJawsOfLifeModelSession(MovingCameraScene):
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
        self.wait(44)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Planning and working safely
        self.write_rows(0, "Planning and working safely", [
            "Write the sequence: mark, cut, laminate, punch, glue, pin, fill, test",
            "Knife on a mat, light passes, cap it",
            "Never point a syringe at anyone",
            "Mark from the drawing, label each part",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Cutting, joining, filling
        self.next_band(1)
        self.write_rows(1, "Cutting, joining, filling", [
            "Laminate with ridges crossed, press flat",
            "Punch holes; pins turn freely, no wobble",
            "Crossed arms on the pin, rod with no slack",
            "Fill under water, crisp means bubble-free",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Testing, evaluating, communicating
        self.next_band(2)
        self.write_rows(2, "Testing, evaluating, communicating", [
            "Each specification: met or not, with a number",
            "Fix faults, record each fix",
            "Evaluate against the brief and the process",
            "Present the record and explain the principle",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Glue first, punch holes later''",
            "``Blame the syringe for a loose rod''",
            "``Fill the syringes in the air''",
            "``Evaluate by saying it is nice''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Plan first, cut safely
        self.next_band(4)
        self.write_rows(4, "Plan first, cut safely", [
            "Ten steps in order",
            "Mat, ruler, light cuts, cap it",
            "Measure twice, mark lightly",
            "Ridges along the base",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Cut, glue, pin, fill
        self.next_band(5)
        self.write_rows(5, "Cut, glue, pin, fill", [
            "Two layers, ridges crossed",
            "Punch, do not cut, the holes",
            "Straw rod, tight loop, no slack",
            "No bubbles: fill under water",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Test it, judge it, show it
        self.next_band(6)
        self.write_rows(6, "Test it, judge it, show it", [
            "Opening, block, distance, stands, ten times",
            "Sandpaper pads, straw ribs",
            "Honest evaluation, next version",
            "Short talk from the moving model",
        ], scale=0.9, box=2)

        last = Tex("Plan, cut safely, join without slack, fill without bubbles, test against the brief, and tell the story.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
