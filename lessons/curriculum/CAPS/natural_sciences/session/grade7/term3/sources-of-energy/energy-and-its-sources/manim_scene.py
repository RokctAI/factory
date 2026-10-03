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

# Band-layout whiteboard scene for energy-and-its-sources (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (130/160/190/120/120/120 of 840 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class EnergyAndItsSourcesSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Energy makes things happen
        self.write_rows(0, "Energy makes things happen", [
            "Energy: to work, move, grow, heat, light, sound",
            "Measured in joules (J); 1 kJ = 1 000 J",
            "Chemical, kinetic, potential, heat, light, sound, electrical",
            "Energy changes form; food energy began as sunlight",
        ], scale=0.76, box=1)

        # --- Band 1 (subtopic_2): Non-renewable sources
        self.next_band(1)
        self.write_rows(1, "Non-renewable sources", [
            "Fossil fuels: coal, oil, gas (millions of years)",
            "SA: most electricity from coal in Mpumalanga",
            "Burning: CO2, pollution; they will run out",
            "Nuclear (Koeberg): little CO2, radioactive waste",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Renewable sources
        self.next_band(2)
        self.write_rows(2, "Renewable sources", [
            "Solar: panels and water heaters; Northern Cape",
            "Wind: Eastern, Western, Northern Cape",
            "Hydro and pumped storage; biofuel and biogas",
            "Clean, never run out; but weather-dependent",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Electricity is an energy source''",
            "``Renewable means free''",
            "``Fossil fuels are renewable''",
            "``Uranium is renewable''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Nothing happens without energy
        self.next_band(4)
        self.write_rows(4, "Nothing happens without energy", [
            "Energy makes things move, heat, light, sound, grow",
            "Measured in joules; food labels in kilojoules",
            "Gas to heat; battery to light; food to movement",
            "Food energy started as sunlight",
        ], scale=0.82, box=0)

        # --- Band 5 (subtopic_5): Energy that runs out
        self.next_band(5)
        self.write_rows(5, "Energy that runs out", [
            "Coal, oil, gas: fossil fuels",
            "Took millions of years; will run out",
            "Smoke and carbon dioxide",
            "Nuclear: little smoke, dangerous waste",
        ], scale=0.88, box=1)

        # --- Band 6 (subtopic_6): Energy that comes back
        self.next_band(6)
        self.write_rows(6, "Energy that comes back", [
            "Sun: panels and geysers",
            "Wind: turbines in the Cape",
            "Water: hydro; biofuel: wood, biogas",
            "Clean, but need batteries or backup",
        ], scale=0.88, box=3)

        last = Tex("Everything runs on energy; choose sources that will not run out.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
