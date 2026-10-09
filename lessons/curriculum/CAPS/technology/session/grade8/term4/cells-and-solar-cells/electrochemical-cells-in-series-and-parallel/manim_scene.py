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

# Band-layout whiteboard scene for electrochemical-cells-in-series-and-parallel (Part 1 Expert
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


class ElectrochemicalCellsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): How an Electrochemical Cell Makes Electricity
        self.write_rows(0, "How an Electrochemical Cell Makes Electricity", [
            "Two electrodes and an electrolyte",
            "Chemistry fixes volts: 1.5, 2, 3.7",
            "Capacity: how long, in mAh",
            "Primary dies; secondary recharges",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Cells in Series: More Voltage, Same Capacity
        self.next_band(1)
        self.write_rows(1, "Cells in Series: More Voltage, Same Capacity", [
            "Series: plus to minus, end to end",
            "Volts add: 3, 4.5, 6",
            "Capacity stays one cell's",
            "Weakest or reversed cell rules",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Cells in Parallel: Same Voltage, More Capacity, and Choosing Between Them
        self.next_band(2)
        self.write_rows(2, "Cells in Parallel: Same Voltage, More Capacity, and Choosing Between Them", [
            "Parallel: plus to plus, minus to minus",
            "Volts stay; capacity adds",
            "Cells must match",
            "Volts? Series. Hours? Parallel.",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Capacities added in series''",
            "``Old and new cells mixed''",
            "``Cell in backwards, torch dim''",
            "``Three cells on a 3 volt bulb''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Chemistry in a Can
        self.next_band(4)
        self.write_rows(4, "Chemistry in a Can", [
            "Button plus, flat minus",
            "Recycle; never short or heat",
            "Bigger cell, same volts, longer",
            "9 volt battery: six cells",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Stacking for Volts
        self.next_band(5)
        self.write_rows(5, "Stacking for Volts", [
            "One cell: dull; two: white; three: dead",
            "Same current through all",
            "One reversed: 3 not 6",
            "Bigger cells for long life",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Side by Side for Hours
        self.next_band(6)
        self.write_rows(6, "Side by Side for Hours", [
            "Fresh heats tired in parallel",
            "One open: others carry on",
            "Two 12 volt in parallel: 12 volts, double hours",
            "Car pack: series-parallel",
        ], scale=0.9, box=2)

        last = Tex("Chemistry fixes a cell's volts; series stacks them for voltage, parallel pairs them for hours, and matched cells the right way round make either work.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
