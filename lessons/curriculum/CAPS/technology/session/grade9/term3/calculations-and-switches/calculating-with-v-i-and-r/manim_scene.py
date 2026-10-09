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

# Band-layout whiteboard scene for calculating-with-v-i-and-r (Part 1 Expert
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


class CalculatingWithVIAndRSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Setting Out an Ohm's Law Calculation
        self.write_rows(0, "Setting Out an Ohm's Law Calculation", [
            "Five lines: known, formula, substitute, calculate, answer + check",
            "Convert mA to A, kilohms to ohms first",
            "Sense: mA in battery circuits; V below supply",
            "150 ohms; 4.1 mA; 4.4 V examples",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Resistors in Series and the Shared Current
        self.next_band(1)
        self.write_rows(1, "Resistors in Series and the Shared Current", [
            "Series: same I, R adds: 470 + 330 = 800",
            "V shared by ratio: 2.6 V and 1.9 V",
            "LED: (V - 2) / I: 250, 400, 700 ohms -> 270, 390, 680",
            "Fixed + variable: current never exceeds the fixed limit",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Resistors in Parallel and Calculations for the PAT Circuit
        self.next_band(2)
        self.write_rows(2, "Resistors in Parallel and Calculations for the PAT Circuit", [
            "Parallel: full V each, currents add",
            "Two 470s -> 235 ohms; less than smallest",
            "PAT: LED 5.3 mA + buzzer 15 mA = 20 mA",
            "Battery: 2000 mAh; standby 0 mA; 380 h warning",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Parallel resistances added like series''",
            "``Same LED resistor used on 9 V as on 4.5 V''",
            "``Milliamperes not converted before dividing''",
            "``Battery life taken from warning current, ignoring standby''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Formula, Numbers, Unit
        self.next_band(4)
        self.write_rows(4, "Formula, Numbers, Unit", [
            "Formula, numbers, unit",
            "Divide by 1000 first",
            "Milliamps, not amps",
            "Does it make sense?",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): In a Line, They Add Up
        self.next_band(5)
        self.write_rows(5, "In a Line, They Add Up", [
            "Add them up",
            "Bigger takes more volts",
            "Battery minus 2, over current",
            "New volts, new resistor",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Side by Side, Less Than the Smallest
        self.next_band(6)
        self.write_rows(6, "Side by Side, Less Than the Smallest", [
            "Full volts each",
            "Add the currents",
            "Below the smallest",
            "Sleeps, so it lasts",
        ], scale=0.9, box=3)

        last = Tex("Set out V equals I R in five lines; series adds resistance and shares voltage, parallel shares voltage and adds current, and battery life is capacity over current.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
