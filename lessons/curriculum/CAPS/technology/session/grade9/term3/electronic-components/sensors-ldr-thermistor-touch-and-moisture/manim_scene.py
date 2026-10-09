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

# Band-layout whiteboard scene for sensors-ldr-thermistor-touch-and-moisture (Part 1 Expert
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


class SensorsLdrThermistorTouchAndMoistureSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): The Light-Dependent Resistor: Resistance Falls as Light Rises
        self.write_rows(0, "The Light-Dependent Resistor: Resistance Falls as Light Rises", [
            "LDR: resistance falls as light rises",
            "Dark ~1 M; room ~kilohms; sun ~hundreds of ohms",
            "No polarity; arrows-in symbol; meter test",
            "Divider with fixed R; base from the junction",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Thermistors: Negative and Positive Temperature Types
        self.next_band(1)
        self.write_rows(1, "Thermistors: Negative and Positive Temperature Types", [
            "NTC: falls when warm; PTC: rises when warm",
            "10 k bench -> 3 k fingers (NTC)",
            "Symbol: rectangle, slash, t; never in flame",
            "Upper: on when hot; lower: on when cold",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Touch and Moisture Detectors and Choosing a Sensor for the PAT
        self.next_band(2)
        self.write_rows(2, "Touch and Moisture Detectors and Choosing a Sensor for the PAT", [
            "Touch/moisture: two contacts, bridged gap",
            "Dry open; wet kilohms; rainwater poor",
            "Corrosion: stainless or carbon; intermittent",
            "Choose: biggest clean change at the condition",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``LDR or thermistor expected to light an LED directly''",
            "``Thermistor placed in a flame''",
            "``Probes tested in tap water for a rainwater tank''",
            "``LDR placed where the circuit's own LED shines on it''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A Resistor That Reacts to Light
        self.next_band(4)
        self.write_rows(4, "A Resistor That Reacts to Light", [
            "Reacts to light",
            "Cover it, it climbs",
            "Street lights, night lights",
            "Pair with a resistor",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): A Resistor That Reacts to Heat
        self.next_band(5)
        self.write_rows(5, "A Resistor That Reacts to Heat", [
            "Reacts to heat",
            "Warm fingers, lower number",
            "PTC as a fuse",
            "Fire alarm or frost warning",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Two Contacts and Something That Conducts
        self.next_band(6)
        self.write_rows(6, "Two Contacts and Something That Conducts", [
            "Finger or wet soil bridges",
            "Test in the real water",
            "Probes corrode",
            "Dark, hot, hand, wet",
        ], scale=0.9, box=3)

        last = Tex("LDRs, thermistors and probe pairs are resistors that respond to light, heat and wetness; tested on a meter and fed to a transistor base, the one with the biggest clean change is chosen.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
