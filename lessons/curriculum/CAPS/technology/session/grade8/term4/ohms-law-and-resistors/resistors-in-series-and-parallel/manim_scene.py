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

# Band-layout whiteboard scene for resistors-in-series-and-parallel (Part 1 Expert
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


class ResistorNetworksSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Resistors: What They Are, Their Values and Their Symbol
        self.write_rows(0, "Resistors: What They Are, Their Values and Their Symbol", [
            "Striped tube; no polarity",
            "Digit, digit, zeros; gold five percent",
            "Brown black brown: 100 Ω",
            "Rectangle symbol; zigzag is old",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Resistors in Series: Resistances Add, Current Falls
        self.next_band(1)
        self.write_rows(1, "Resistors in Series: Resistances Add, Current Falls", [
            "Series: resistances add",
            "Current falls; same through all",
            "Volts shared: voltage divider",
            "One path, no dots",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Resistors in Parallel: More Paths, Lower Resistance, and Drawing Both
        self.next_band(2)
        self.write_rows(2, "Resistors in Parallel: More Paths, Lower Resistance, and Drawing Both", [
            "Parallel: more paths, lower total",
            "Two 100s act like 50",
            "Full volts on each branch",
            "Dots at junctions; house wiring",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Parallel resistances added like series''",
            "``Resistors joined at one end only''",
            "``Dot where lines merely cross''",
            "``Bands read from the wrong end''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Striped Little Tubes
        self.next_band(4)
        self.write_rows(4, "Striped Little Tubes", [
            "Orange orange brown: 330",
            "Red red red: 2.2 k",
            "Heater element is a resistor",
            "Meter checks out of circuit",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): In a Line
        self.next_band(5)
        self.write_rows(5, "In a Line", [
            "3 V over 100, 200, 300: 30, 15, 10 mA",
            "LED resistor in series",
            "Order does not matter",
            "Lamp dims with each one",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Side by Side, and the Drawings
        self.next_band(6)
        self.write_rows(6, "Side by Side, and the Drawings", [
            "Total below the smallest branch",
            "Ammeter before the split",
            "One end joined: dead end",
            "Read bands from the right end",
        ], scale=0.9, box=1)

        last = Tex("Resistors in a line add up and dim the lamp; side by side they open more paths and brighten it; the colour code and the dot at the junction keep it honest.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
