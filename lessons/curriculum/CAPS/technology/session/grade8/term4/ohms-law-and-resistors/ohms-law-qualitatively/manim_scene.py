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

# Band-layout whiteboard scene for ohms-law-qualitatively (Part 1 Expert
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


class OhmsLawSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Voltage, Current and Resistance: Three Quantities in One Circuit
        self.write_rows(0, "Voltage, Current and Resistance: Three Quantities in One Circuit", [
            "Volts push; amps flow; ohms squeeze",
            "Tank, pipe, kink; charge never leaks",
            "Same current all round one loop",
            "Ammeter in series; voltmeter across",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): More Cells in Series, More Current: The Investigation
        self.next_band(1)
        self.write_rows(1, "More Cells in Series, More Current: The Investigation", [
            "Change cells; measure current; keep the lamp",
            "Dim orange, yellow, bright white",
            "Rises, not quite doubling: hot filament",
            "Repeat, average, same-age cells",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Changing the Resistance and Stating Ohm's Law in Words
        self.next_band(2)
        self.write_rows(2, "Changing the Resistance and Stating Ohm's Law in Words", [
            "Same cells, add resistors: current falls",
            "Law both ways; V = I x R later",
            "LED resistor; dimmer; short circuit",
            "Filament and diode are exceptions",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Ammeter across the cell''",
            "``Two variables changed at once''",
            "``Conclusion from one reading''",
            "``Data forced to double''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Push, Flow and Squeeze
        self.next_band(4)
        self.write_rows(4, "Push, Flow and Squeeze", [
            "Torch quarter amp; kettle ten",
            "Open switch: infinite ohms",
            "Never ammeter across a cell",
            "Lamp as rough meter",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Add a Cell, Watch the Lamp
        self.next_band(5)
        self.write_rows(5, "Add a Cell, Watch the Lamp", [
            "Independent, dependent, controlled",
            "6 volt lamp for three cells",
            "Open switch between readings",
            "One variable at a time",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Add a Resistor, Watch Again
        self.next_band(6)
        self.write_rows(6, "Add a Resistor, Watch Again", [
            "Thin long wire: more ohms, warm leads",
            "Grid: thick wire, high volts",
            "Fuse: weakest link on purpose",
            "Record the real pattern",
        ], scale=0.9, box=3)

        last = Tex("Volts push, amps flow, ohms squeeze; more cells in series means more current through the same lamp, more resistance means less, and that is Ohm's law in words.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
