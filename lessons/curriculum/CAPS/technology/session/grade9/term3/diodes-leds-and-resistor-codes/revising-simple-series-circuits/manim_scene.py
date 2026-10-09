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

# Band-layout whiteboard scene for revising-simple-series-circuits (Part 1 Expert
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


class RevisingSimpleSeriesCircuitsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): The Simple Series Circuit: Cell, Switch and Lamp
        self.write_rows(0, "The Simple Series Circuit: Cell, Switch and Lamp", [
            "Supply, switch, load in one loop",
            "Open: gap, off; closed: current, on",
            "Match volts: 4.5 V battery, 4.5 V bulb",
            "Switch in series: it breaks the path",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Building, Fault-Finding and Measuring the Circuit
        self.next_band(1)
        self.write_rows(1, "Building, Fault-Finding and Measuring the Circuit", [
            "Faults in order: supply, load, switch, leads",
            "Lamp to battery; swap lamp; bridge switch; check clips",
            "Voltmeter across: 4.5 V battery; full V across open switch",
            "Ammeter in loop: ~0.3 A; never across battery",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): From the Series Circuit to the PAT Indicator Circuit
        self.next_band(2)
        self.write_rows(2, "From the Series Circuit to the PAT Indicator Circuit", [
            "Lamp -> LED + resistor; switch -> sensor",
            "Battery: three cells, 4.5 V",
            "Habits: draw, match, series, test in order, measure",
            "Exercise: torch -> tank indicator",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Switch in parallel with the lamp''",
            "``9 V battery on a 4.5 V bulb''",
            "``Ammeter connected across the battery''",
            "``All leads wiggled at once''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): One Loop, Three Parts
        self.next_band(4)
        self.write_rows(4, "One Loop, Three Parts", [
            "One loop, three parts",
            "Gap means dark",
            "Right volts for the bulb",
            "Switch breaks the loop",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): When It Does Not Work
        self.next_band(5)
        self.write_rows(5, "When It Does Not Work", [
            "Do not shake it",
            "Battery, lamp, switch, leads",
            "Clip on plastic",
            "Volts across, amps through",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): The Same Loop With Better Parts
        self.next_band(6)
        self.write_rows(6, "The Same Loop With Better Parts", [
            "Same loop, better parts",
            "LED, resistor, sensor",
            "Draw first",
            "Fix it on the bench, not on the day",
        ], scale=0.9, box=3)

        last = Tex("A series circuit works only as a complete loop; find faults in order, measure volts across and amps through, and grow the loop into the PAT indicator.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
