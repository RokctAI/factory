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

# Band-layout whiteboard scene for the-scrap-metal-crane-scenario (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (200/170/150/110/110/110 of 850 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TheScrapMetalCraneScenarioSession(MovingCameraScene):
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
        self.wait(56)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Reading the scenario
        self.write_rows(0, "Reading the scenario", [
            "Mixed scrap: steel, copper, aluminium",
            "Need: sort ferrous from non-ferrous",
            "User, situation, must do, must not do",
            "Magnet must switch off: electromagnet",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Case study of cranes
        self.next_band(1)
        self.write_rows(1, "Case study of cranes", [
            "Base, body, jib, cable, pulley, lifter",
            "Hoist, luff, slew",
            "Counterweight and outriggers",
            "Record in a table",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Pictures to ideas
        self.next_band(2)
        self.write_rows(2, "Pictures to ideas", [
            "Borrow from several, copy none",
            "Thumbnail sketches: an idea bank",
            "Model at small scale tests the idea",
            "Safety line in the record",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``The need is a crane''",
            "``Skip the case study''",
            "``Copy one picture exactly''",
            "``Forget the counterweight''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): What the dealer needs
        self.next_band(4)
        self.write_rows(4, "What the dealer needs", [
            "Mixed load sells for nothing",
            "Need first, answer second",
            "Ask who, where, must, must not",
            "Write it all down",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Looking at real cranes
        self.next_band(5)
        self.write_rows(5, "Looking at real cranes", [
            "Every crane: base to magnet",
            "Lift, tilt, swing",
            "Counterweight twice",
            "Model needs lift and swing",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Borrow, do not copy
        self.next_band(6)
        self.write_rows(6, "Borrow, do not copy", [
            "One idea per picture",
            "Nail and wire lifts paper clips",
            "Hot wire, sharp nail, glue gun",
            "Safety in the record",
        ], scale=0.9, box=0)

        last = Tex("Find the need, study what exists, borrow ideas, and plan a magnet that switches off.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
