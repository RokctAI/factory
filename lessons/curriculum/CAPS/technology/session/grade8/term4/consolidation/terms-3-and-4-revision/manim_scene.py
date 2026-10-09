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

# Band-layout whiteboard scene for terms-3-and-4-revision (Part 1 Expert
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


class YearEndRevisionSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Revising Term 4: Circuits, Energy and Generation
        self.write_rows(0, "Revising Term 4: Circuits, Energy and Generation", [
            "Input, output, control; symbols and dots",
            "Series shares; parallel survives; shorts heat",
            "Six fuels, five criteria; wires lack protection",
            "Cells: series volts, parallel hours; solar half a volt",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Revising Term 4: Ohm's Law, Logic Gates and the Panic Button
        self.next_band(1)
        self.write_rows(1, "Revising Term 4: Ohm's Law, Logic Gates and the Panic Button", [
            "Volts push, amps flow, ohms squeeze",
            "Colour code; series adds; parallel drops",
            "AND series, D; OR parallel, shield",
            "Button: brief, specs, OR, eight rows, poster",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Revising Term 3 and Preparing for the End-of-Year Examination
        self.next_band(2)
        self.write_rows(2, "Revising Term 3 and Preparing for the End-of-Year Examination", [
            "Gears opposite; small-to-big slow and strong",
            "MA: driven over driver; levers by distance",
            "Headgear: braced frame, sheave, rope",
            "Command word; reason; both sides; working",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``One-word explain answer''",
            "``Advantages without disadvantages''",
            "``Gear ratio upside down''",
            "``Truth table missing a row''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Circuits and Power, Fast
        self.next_band(4)
        self.write_rows(4, "Circuits and Power, Fast", [
            "Heat, steam, turbine, generator: 40 percent",
            "Coal, gas, nuclear, solar thermal",
            "Hydro, pumped storage, wind",
            "AC, transformers, 50 hertz",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Ohm, Gates and the Button, Fast
        self.next_band(5)
        self.write_rows(5, "Ohm, Gates and the Button, Fast", [
            "Ammeter in series, voltmeter across",
            "Tables in binary; mixed rows differ",
            "Problem, users, purpose",
            "Honest, bilingual, ten seconds",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Gears Again, and Exam Craft
        self.next_band(6)
        self.write_rows(6, "Gears Again, and Exam Craft", [
            "Idler keeps ratio; bevel turns the corner",
            "Read twice; time by marks",
            "Answer everything",
            "Check dots, polarity, rows",
        ], scale=0.9, box=3)

        last = Tex("Two terms on one sheet: circuits, energy, cells, generation and the grid, Ohm's law, gates and the panic button, gears and the headgear, and the exam craft to turn them into marks.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
