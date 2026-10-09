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

# Band-layout whiteboard scene for npn-transistors-as-switches-and-amplifiers (Part 1 Expert
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


class NpnTransistorsAsSwitchesAndAmplifiersSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): The npn Transistor: Three Legs and a Tiny Current That Controls a Large One
        self.write_rows(0, "The npn Transistor: Three Legs and a Tiny Current That Controls a Large One", [
            "npn: collector, base, emitter; check the card",
            "Symbol: base bar, emitter arrow outward",
            "No base current: off; small base current: on",
            "Gain ~100; base 0.6 V above emitter",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): The Transistor as a Switch Driven by a Sensor
        self.next_band(1)
        self.write_rows(1, "The Transistor as a Switch Driven by a Sensor", [
            "Load and + to collector; emitter to -",
            "Base resistor 10-100 kilohms: essential",
            "LDR to base: light on; swap for dark on",
            "Off or saturated; in-between gets warm",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): The Transistor as an Amplifier and Practical Precautions
        self.next_band(2)
        self.write_rows(2, "The Transistor as an Amplifier and Practical Precautions", [
            "Amplifier: small wobble in, big wobble out, same shape",
            "Energy from the supply, not the transistor",
            "Switch and amplifier: one property, two drives",
            "Precautions: legs, base R, 100 mA, heat, static",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``No base resistor''",
            "``Legs in the wrong holes''",
            "``LED in the collector circuit without its resistor''",
            "``BC547 expected to drive a one ampere motor''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A Switch With No Moving Parts
        self.next_band(4)
        self.write_rows(4, "A Switch With No Moving Parts", [
            "Switch with no moving parts",
            "Trickle opens the tap",
            "Collector to load, emitter to minus",
            "Base is the control",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): A Trickle Opens the Tap
        self.next_band(5)
        self.write_rows(5, "A Trickle Opens the Tap", [
            "Touch and it lights",
            "Sensor decides",
            "Night light by swapping",
            "Clean on or off",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Small In, Big Out, Mind the Legs
        self.next_band(6)
        self.write_rows(6, "Small In, Big Out, Mind the Legs", [
            "Radio, microphone, guitar",
            "Bigger, same shape",
            "Battery does the work",
            "Check the legs first",
        ], scale=0.9, box=3)

        last = Tex("An npn transistor lets a small base current control a much larger collector current: a sensor-driven switch, or an amplifier, always with a base resistor.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
