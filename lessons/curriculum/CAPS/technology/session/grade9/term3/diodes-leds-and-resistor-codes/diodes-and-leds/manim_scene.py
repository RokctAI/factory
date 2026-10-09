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

# Band-layout whiteboard scene for diodes-and-leds (Part 1 Expert
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


class DiodesAndLedsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): The Diode: A One-Way Valve for Current
        self.write_rows(0, "The Diode: A One-Way Valve for Current", [
            "Diode: anode, cathode; one-way conduction",
            "Forward: conducts, ~0.7 V; reverse: blocks",
            "Symbol: triangle -> bar; band marks cathode",
            "Uses: rectifier, solar backflow, spike protection",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): The LED: A Diode That Lights, and Why It Needs a Resistor
        self.next_band(1)
        self.write_rows(1, "The LED: A Diode That Lights, and Why It Needs a Resistor", [
            "LED: diode that emits light; arrows on symbol",
            "Long leg anode; flat spot cathode",
            "Drops ~2 V, near-zero resistance when on",
            "Series resistor: (4.5 - 2) / 0.01 = 250 ohms; use 270 or 470",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Using LEDs as Indicators in the PAT Device
        self.next_band(2)
        self.write_rows(2, "Using LEDs as Indicators in the PAT Device", [
            "PAT: battery, sensor, resistor, LED in series",
            "High-brightness or flashing red for daylight",
            "Two states: two LEDs, a resistor each, in parallel",
            "Handle: identify legs, never without resistor, check polarity",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``LED straight across the battery''",
            "``LED reversed, long leg to negative''",
            "``One resistor shared by parallel LEDs''",
            "``LED symbol drawn without arrows''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Current Goes One Way Only
        self.next_band(4)
        self.write_rows(4, "Current Goes One Way Only", [
            "One-way valve",
            "Triangle shows the way",
            "Charger, solar, motor",
            "Backwards: dark",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): A Light That Must Be Protected
        self.next_band(5)
        self.write_rows(5, "A Light That Must Be Protected", [
            "Glows when forward",
            "Long leg to plus",
            "Straight on battery: dead",
            "Resistor takes the spare volts",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Long Leg to Plus, Resistor in Line
        self.next_band(6)
        self.write_rows(6, "Long Leg to Plus, Resistor in Line", [
            "Loop: battery, sensor, resistor, LED",
            "Red and bright, or flashing",
            "Own resistor each",
            "Not lit? Flip it",
        ], scale=0.9, box=3)

        last = Tex("A diode passes current one way; an LED is a diode that lights, drops about 2 volts and must have its own series resistor to survive.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
