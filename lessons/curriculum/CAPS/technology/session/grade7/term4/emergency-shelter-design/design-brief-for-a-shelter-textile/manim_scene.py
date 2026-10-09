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

# Band-layout whiteboard scene for design-brief-for-a-shelter-textile (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (210/260/240/100/100/100 of 1010 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DesignBriefForAShelterTextileSession(MovingCameraScene):
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
        self.wait(70)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): From tests to a brief
        self.write_rows(0, "From tests to a brief", [
            "For a supplier and an inspector",
            "What, for whom, why; traceable",
            "Water: drip, thumb, 1 500 mm head",
            "Flame: no flame, no drip, out in 2 s",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): The full specification
        self.next_band(1)
        self.write_rows(1, "The full specification", [
            "Mass under 350 gsm; ripstop; UV",
            "Opaque, light roof; vents allowed",
            "Welded seams; eyelets at 500 mm",
            "Constraints: cost, SA stock, fit",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Choosing and justifying
        self.next_band(2)
        self.write_rows(2, "Choosing and justifying", [
            "Eliminate sample by sample",
            "FR coated ripstop at 300 gsm",
            "Tarpaulin floor; honest compromise",
            "List what you could not test",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Must be waterproof, no test''",
            "``Truck PVC two people cannot lift''",
            "``Fabric specified without the shelter''",
            "``Chosen by cost alone''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Tests become words
        self.next_band(4)
        self.write_rows(4, "Tests become words", [
            "Checkable lines",
            "Brief sentence",
            "Two safety lines",
            "Test, result, requirement, standard",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): The ten lines and the limits
        self.next_band(5)
        self.write_rows(5, "The ten lines and the limits", [
            "Water, flame, mass, strength, UV",
            "Opacity, vents, seams, eyelets, folding",
            "Price, place, time, quantity, fit",
            "Fabric or programme?",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Choose and say why
        self.next_band(6)
        self.write_rows(6, "Choose and say why", [
            "Fails water, flame, mass, sun",
            "Passes at a price",
            "Recommend, assume, justify, alternative",
            "Supplier and inspector read it",
        ], scale=0.9, box=2)

        last = Tex("A textile brief a supplier can quote and an inspector can check: ten measurable specifications from tests, programme constraints, and a justified choice with safety first.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
