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

# Band-layout whiteboard scene for ohms-law-quantitatively (Part 1 Expert
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


class OhmsLawQuantitativelySession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Voltage, Current and Resistance as Measured Quantities
        self.write_rows(0, "Voltage, Current and Resistance as Measured Quantities", [
            "Voltage: push, volts, voltmeter across",
            "Current: flow, amperes, ammeter in loop",
            "Resistance: opposition, ohms, bands",
            "Water: pressure, flow, pipe width",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Ohm's Law: Current Rises in Step With Voltage at Fixed Resistance
        self.next_band(1)
        self.write_rows(1, "Ohm's Law: Current Rises in Step With Voltage at Fixed Resistance", [
            "Current proportional to voltage at constant temperature",
            "V = I x R; 1 V across 1 ohm -> 1 A",
            "100 ohms: 1 V 10 mA, 2 V 20 mA, 3 V 30 mA",
            "Not for hot lamps or LEDs",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): The Three Forms of the Law and Simple Worked Examples
        self.next_band(2)
        self.write_rows(2, "The Three Forms of the Law and Simple Worked Examples", [
            "V = IR; I = V/R; R = V/I; triangle",
            "0.005 x 470 = 2.35 V; 4.5 / 1500 = 3 mA",
            "LED: (4.5 - 2) / 0.01 = 250 ohms; 470 -> 5.3 mA",
            "Formula, substitute, unit, sense check",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Milliamperes used unconverted''",
            "``Battery voltage used for the resistor with an LED present''",
            "``Ohm's law applied to the LED''",
            "``Law stated without constant temperature''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Push, Flow and Opposition
        self.next_band(4)
        self.write_rows(4, "Push, Flow and Opposition", [
            "Push, flow, opposition",
            "Across, in line, bands",
            "10 mA = 0.01 A",
            "Set the range first",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Double the Push, Double the Flow
        self.next_band(5)
        self.write_rows(5, "Double the Push, Double the Flow", [
            "Double the push, double the flow",
            "Straight line through zero",
            "Volts over amps = resistance",
            "Unless it gets hot",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): One Triangle, Three Sums
        self.next_band(6)
        self.write_rows(6, "One Triangle, Three Sums", [
            "Cover what you want",
            "Convert mA to A",
            "Battery minus LED drop",
            "A few volts, a few milliamps",
        ], scale=0.9, box=2)

        last = Tex("At constant temperature current is proportional to voltage, V equals I times R; convert units, treat the LED as a 2 volt drop, and calculate the resistor.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
