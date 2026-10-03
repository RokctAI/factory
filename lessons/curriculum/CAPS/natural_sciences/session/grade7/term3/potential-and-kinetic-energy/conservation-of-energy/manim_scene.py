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

# Band-layout whiteboard scene for conservation-of-energy (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (140/120/130/120/120/120 of 750 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ConservationOfEnergySession(MovingCameraScene):
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
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Conservation of energy
        self.write_rows(0, "Conservation of energy", [
            "Energy cannot be created or destroyed",
            "Only changed in form or transferred",
            "Coaster: electrical, PE, KE, PE, heat",
            "Total stays the same; useful energy shrinks",
        ], scale=0.88, box=1)

        # --- Band 1 (subtopic_2): Transfer within a system
        self.next_band(1)
        self.write_rows(1, "Transfer within a system", [
            "Wind-up radio: arm KE, stored, electrical, sound",
            "Phone: battery, electrical, light, sound, heat",
            "Energy-flow diagram: boxes and arrows",
            "Total in equals total out",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Between systems
        self.next_band(2)
        self.write_rows(2, "Between systems", [
            "Output of one system is input of the next",
            "Sun, plants, oil, diesel, taxi, heat",
            "Leg to ball to net to air",
            "No perpetual motion",
        ], scale=0.88, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Energy is destroyed when a car stops''",
            "``Machines can make extra energy''",
            "``Diagrams without heat and sound''",
            "``Transfer and transformation are the same''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): The big rule
        self.next_band(4)
        self.write_rows(4, "The big rule", [
            "Energy is never made or destroyed",
            "It changes form or moves on",
            "Coaster: height, speed, height, a bit of heat",
            "Used up means spread out",
        ], scale=0.82, box=1)

        # --- Band 5 (subtopic_5): Inside one gadget
        self.next_band(5)
        self.write_rows(5, "Inside one gadget", [
            "Phone: battery, electricity, light, sound, heat",
            "Wind-up radio stores your arm's energy",
            "Boxes and arrows: in equals out",
            "Heat is always one of the outputs",
        ], scale=0.82, box=2)

        # --- Band 6 (subtopic_6): Passing it along
        self.next_band(6)
        self.write_rows(6, "Passing it along", [
            "Sun, plants, oil, diesel, taxi, heat",
            "Leg, ball, net, air",
            "No forever machines",
            "Same energy, changing form",
        ], scale=0.88, box=1)

        last = Tex("Energy is never made or destroyed: it only changes form and moves.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
