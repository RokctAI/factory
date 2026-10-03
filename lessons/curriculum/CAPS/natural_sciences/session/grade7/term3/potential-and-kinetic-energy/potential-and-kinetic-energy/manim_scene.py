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

# Band-layout whiteboard scene for potential-and-kinetic-energy (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (130/140/190/120/120/120 of 820 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PotentialAndKineticEnergySession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Potential energy: stored
        self.write_rows(0, "Potential energy: stored", [
            "Gravitational: raised up (cliff rock, dam, swing top)",
            "Elastic: stretched or squashed (catapult, spring)",
            "Chemical: fuels, batteries, food, matches",
            "Hidden until released",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Energy in food
        self.next_band(1)
        self.write_rows(1, "Energy in food", [
            "Plants store sunlight as chemical energy",
            "Labels: kilojoules per serving and per 100 g",
            "Fat about 37 kJ/g; carbs and protein about 17 kJ/g",
            "Balance energy in with energy used",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Kinetic energy: motion
        self.next_band(2)
        self.write_rows(2, "Kinetic energy: motion", [
            "Moving things: runner, taxi, wind, water",
            "More speed and more mass: more kinetic energy",
            "Double speed: about 4 times the energy",
            "Swing: top = most PE; bottom = most KE",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``A still object has no energy''",
            "``Potential energy is only about height''",
            "``Kinetic energy depends only on speed''",
            "``Food energy is measured in grams''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Energy in waiting
        self.next_band(4)
        self.write_rows(4, "Energy in waiting", [
            "High up: slide, dam",
            "Stretched: catapult, rubber band",
            "Chemicals: food, petrol, batteries",
            "Potential = stored",
        ], scale=0.88, box=3)

        # --- Band 5 (subtopic_5): Lunchbox power
        self.next_band(5)
        self.write_rows(5, "Lunchbox power", [
            "Food stores sunlight energy",
            "Labels show kilojoules",
            "Fatty foods: lots; fruit and veg: fewer",
            "Extra energy stored as fat",
        ], scale=0.88, box=1)

        # --- Band 6 (subtopic_6): On the move
        self.next_band(6)
        self.write_rows(6, "On the move", [
            "Moving things have kinetic energy",
            "Faster and heavier: more",
            "Double speed: about 4 times the energy",
            "Swing: height energy and speed trade places",
        ], scale=0.88, box=3)

        last = Tex("Stored energy waits; kinetic energy moves.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
