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

# Band-layout whiteboard scene for simple-electric-circuits-and-circuit-diagrams (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (200/160/160/110/110/110 of 850 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SimpleElectricCircuitsAndCircuitDiagramsSession(MovingCameraScene):
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
        self.wait(46)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Building a circuit that works
        self.write_rows(0, "Building a circuit that works", [
            "Cell, conductors, switch, output",
            "Complete loop or nothing",
            "Switch: a gap you control",
            "Buzzer one way; bulb any way",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Conductors and the group build
        self.next_band(1)
        self.write_rows(1, "Conductors and the group build", [
            "Metals conduct; plastic, rubber insulate",
            "Clip on bare metal, bulb screwed home",
            "Two bulbs dim; two cells bright",
            "Never short a cell; never touch mains",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Drawing the circuit diagram
        self.next_band(2)
        self.write_rows(2, "Drawing the circuit diagram", [
            "Cell: long thin plus, short thick minus",
            "Switch: hinged gap; bulb: circle and cross",
            "Ruler, rectangle, square corners",
            "Symbols are a world language",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Draw pictures instead of symbols''",
            "``Leave a gap in the drawn loop''",
            "``Cell symbol backwards''",
            "``Wavy freehand wires''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Make the bulb light
        self.next_band(4)
        self.write_rows(4, "Make the bulb light", [
            "Ring it up, press, light",
            "One gap, all dark",
            "Buzzer has plus and minus",
            "Write it down",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): What lets current through
        self.next_band(5)
        self.write_rows(5, "What lets current through", [
            "Nail, foil, coin: light",
            "Plastic, rubber, wood: dark",
            "Check cell, clips, bulb, switch",
            "Hot wire warning",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Draw it so anyone can build it
        self.next_band(6)
        self.write_rows(6, "Draw it so anyone can build it", [
            "Cell left, plus on top",
            "Top to switch, down to bulb, back",
            "Label every part",
            "Dot means join",
        ], scale=0.9, box=0)

        last = Tex("A closed loop of cell, switch and output makes current flow; draw it with standard symbols and a ruler.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
