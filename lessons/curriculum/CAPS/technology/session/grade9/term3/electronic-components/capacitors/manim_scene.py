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

# Band-layout whiteboard scene for capacitors (Part 1 Expert
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


class CapacitorsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What a Capacitor Is and How It Stores Charge
        self.write_rows(0, "What a Capacitor Is and How It Stores Charge", [
            "Two plates + dielectric; charge builds to supply V",
            "Capacitance: farads; micro, nano, pico",
            "Symbol: two parallel lines; curve or + for polarised",
            "Not a battery: little energy, fast, repeatable",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Charging, Discharging and the Time It Takes
        self.next_band(1)
        self.write_rows(1, "Charging, Discharging and the Time It Takes", [
            "Charging: fast then slow as V rises",
            "2/3 full after R x C; nearly full after 5 R C",
            "10 k x 100 uF = 1 s; 100 k x 1000 uF = 100 s",
            "Discharge mirrors: LED flares and fades",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Capacitor Types, Polarity and Uses in Simple Circuits
        self.next_band(2)
        self.write_rows(2, "Capacitor Types, Polarity and Uses in Simple Circuits", [
            "Ceramic: small, unpolarised, code 104 = 100 nF",
            "Electrolytic: large, stripe = negative, shorter leg",
            "Rated V above supply; reversed = swell and burst",
            "Uses: smoothing, timing, energy burst; discharge before handling",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Electrolytic connected backwards''",
            "``16 V capacitor on a 24 V supply''",
            "``Capacitor expected to power a lamp for minutes''",
            "``Code 104 read as 104 microfarads''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Two Plates and a Gap
        self.next_band(4)
        self.write_rows(4, "Two Plates and a Gap", [
            "Tiny bucket for charge",
            "Battery fills it; LED empties it",
            "Microfarads",
            "Holds a little, gives it fast",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Fill It Up, Let It Out
        self.next_band(5)
        self.write_rows(5, "Fill It Up, Let It Out", [
            "Fills fast, then slower",
            "Ohms x farads = seconds",
            "Double either, double the time",
            "Timers",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Big Ones Have a Plus and a Minus
        self.next_band(6)
        self.write_rows(6, "Big Ones Have a Plus and a Minus", [
            "Discs either way",
            "Cans: stripe on minus",
            "Volts on the can beat the supply",
            "Drain through a resistor first",
        ], scale=0.9, box=1)

        last = Tex("A capacitor stores charge between two plates and releases it; resistance times capacitance sets its timing, and electrolytics must be connected the right way round.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
