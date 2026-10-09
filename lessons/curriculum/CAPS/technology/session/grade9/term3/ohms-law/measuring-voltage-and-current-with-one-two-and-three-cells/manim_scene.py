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

# Band-layout whiteboard scene for measuring-voltage-and-current-with-one-two-and-three-cells (Part 1 Expert
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


class MeasuringVoltageAndCurrentWithOneTwoAndThreeCellsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Setting Up the Investigation: Resistor, Cells and Two Meters
        self.write_rows(0, "Setting Up the Investigation: Resistor, Cells and Two Meters", [
            "Loop: cells, switch, 100 ohm resistor",
            "Voltmeter across; ammeter in series gap",
            "Red to positive; ranges set first",
            "Draw the circuit with V and A first",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Taking Readings With One, Two and Three Cells
        self.next_band(1)
        self.write_rows(1, "Taking Readings With One, Two and Three Cells", [
            "1 cell: ~1.45 V, ~14 mA",
            "2 cells: ~2.9 V, ~29 mA; 3: ~4.4 V, ~44 mA",
            "No current rise: dead or reversed cell, or meter wrong",
            "Read to last stable digit; repeat",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Recording, Repeating and Handling the Readings Honestly
        self.next_band(2)
        self.write_rows(2, "Recording, Repeating and Handling the Readings Honestly", [
            "Table: cells, 3 V readings, mean, 3 I readings, mean, V/I",
            "V/I near 100 every row",
            "Odd row: remeasure and note, never delete",
            "Fresh cells, no shorts, ammeter never across cells",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Ammeter connected across the resistor''",
            "``Readings rounded to the prediction''",
            "``Single reading with no repeat''",
            "``Anomalous row deleted instead of remeasured''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Build the Loop, Add the Meters
        self.next_band(4)
        self.write_rows(4, "Build the Loop, Add the Meters", [
            "Cells, switch, resistor",
            "V across, A in the gap",
            "Set volts and milliamps",
            "Diagram first",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Add a Cell, Read Both Meters
        self.next_band(5)
        self.write_rows(5, "Add a Cell, Read Both Meters", [
            "About 1.5 V and 15 mA per cell",
            "Each cell adds the same",
            "Write what it says",
            "Repeat with the switch open between",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Write It Down the Way It Was
        self.next_band(6)
        self.write_rows(6, "Write It Down the Way It Was", [
            "Volts over amps near 100",
            "Small wobble is real",
            "Note the warm cell and loose clip",
            "Switch open, probes by the insulation",
        ], scale=0.9, box=1)

        last = Tex("Voltmeter across, ammeter in line; each added cell raises volts and milliamps in step, and honest repeated readings make volts over amps hold near the resistor's value.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
