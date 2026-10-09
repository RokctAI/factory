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

# Band-layout whiteboard scene for transistor-thermistor-timing-circuit (Part 1 Expert
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


class TransistorThermistorTimingCircuitSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): The Circuit: Thermistor, Variable Resistor, Transistor, LED, Capacitor and Switch
        self.write_rows(0, "The Circuit: Thermistor, Variable Resistor, Transistor, LED, Capacitor and Switch", [
            "4.5 V + SPST; divider: NTC above, variable R below",
            "Junction -> 10 k -> base; 470 + LED to collector",
            "100 uF from base to -, plus on base",
            "One job per part: sense, set, protect, switch, show, smooth",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): How It Works: Sensing Temperature and Setting the Threshold
        self.next_band(1)
        self.write_rows(1, "How It Works: Sensing Temperature and Setting the Threshold", [
            "V\\_junction = 4.5 x bottom / total",
            "10 k / 2 k: 0.75 V on; 20 k: 0.4 V off; 3 k: 1.8 V on",
            "Variable R sets threshold; adjust until LED just on",
            "Swap sensor and R: cold-on frost warning",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): The Capacitor's Role, Building the Circuit and Adapting It
        self.next_band(2)
        self.write_rows(2, "The Capacitor's Role, Building the Circuit and Adapting It", [
            "Capacitor: smooths flicker, delays ~R x C = 1 s",
            "Build: rails, rows, three polarised parts, check first",
            "Test: adjust, warm, pause, on; cool, pause, off",
            "Adapt: LDR, probes; buzzer; within rating",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Electrolytic capacitor reversed''",
            "``Thermistor and variable resistor swapped by accident''",
            "``Variable resistor at zero, junction stuck at negative''",
            "``Circuit explained without each part's job''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Six Parts, One Job
        self.next_band(4)
        self.write_rows(4, "Six Parts, One Job", [
            "Battery, switch, sensor line, base, LED, capacitor",
            "Label every value",
            "Sensing, deciding, showing",
            "Name each job",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Warm Enough, Light On
        self.next_band(5)
        self.write_rows(5, "Warm Enough, Light On", [
            "Share the volts",
            "Warm: on; cold: off",
            "Knob sets the temperature",
            "Sensor below: cold-on",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): A Pause Before It Switches
        self.next_band(6)
        self.write_rows(6, "A Pause Before It Switches", [
            "No flicker, one-second pause",
            "Check polarities, then power",
            "Warm mug, damp cloth",
            "Light alarm, moisture alarm, buzzer",
        ], scale=0.9, box=3)

        last = Tex("A thermistor divider sets a transistor's base past 0.6 volts at a chosen temperature, switching an LED, with a capacitor smoothing and delaying the change.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
