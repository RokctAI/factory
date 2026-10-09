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

# Band-layout whiteboard scene for term-3-revision-circuits-ohms-law-and-components (Part 1 Expert
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


class Term3RevisionCircuitsOhmsLawAndComponentsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Revising Circuits: Symbols, Series, Parallel and Logic
        self.write_rows(0, "Revising Circuits: Symbols, Series, Parallel and Logic", [
            "Complete loop; standard symbols; dots; + to -",
            "Series: same I, V shared, cells add, one fails all",
            "Parallel: full V each, currents add, independent",
            "Series switches AND; parallel switches OR",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Revising Ohm's Law: Measuring, Graphing and Calculating
        self.next_band(1)
        self.write_rows(1, "Revising Ohm's Law: Measuring, Graphing and Calculating", [
            "V across, A in line, never across supply",
            "V = I R at constant temperature; convert mA",
            "Graph: V vs I, straight through origin, gradient = R",
            "Sums in five lines; LED R = (V - 2) / I; life = Ah / A",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Revising Components: Diodes, LEDs, Resistors, Switches, Transistors, Sensors and Capacitors
        self.next_band(2)
        self.write_rows(2, "Revising Components: Diodes, LEDs, Resistors, Switches, Transistors, Sensors and Capacitors", [
            "Diode one way; LED 2 V + resistor; codes: 470",
            "Switches: push, SPST, SPDT, DPDT",
            "Transistor: base trickle, collector flood, base R",
            "LDR, NTC, PTC, probes; capacitor R x C",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``LED or electrolytic connected backwards''",
            "``Transistor without base resistor or legs reversed''",
            "``Sensor expected to drive a load directly''",
            "``Circuit explained without each component's job''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): One Loop or Many, Both or Either
        self.next_band(4)
        self.write_rows(4, "One Loop or Many, Both or Either", [
            "One loop or many",
            "Shares volts or shares current",
            "Both or either",
            "Trace and count",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Volts, Amps, Ohms and the Straight Line
        self.next_band(5)
        self.write_rows(5, "Volts, Amps, Ohms and the Straight Line", [
            "Volts, amps, ohms",
            "Straight line through zero",
            "Convert first",
            "Five lines",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Every Part and Its One Job
        self.next_band(6)
        self.write_rows(6, "Every Part and Its One Job", [
            "One way, lights, 470",
            "Count poles and throws",
            "Small controls big",
            "Each part, one job",
        ], scale=0.9, box=3)

        last = Tex("A complete loop, series and parallel, V equals I R, and one job per component: the whole term in four lines.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
