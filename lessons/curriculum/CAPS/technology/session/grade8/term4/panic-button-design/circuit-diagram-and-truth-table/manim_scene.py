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

# Band-layout whiteboard scene for circuit-diagram-and-truth-table (Part 1 Expert
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


class PanicButtonCircuitSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): From Specification to Gate: Why the Panic Button Is an OR
        self.write_rows(0, "From Specification to Gate: Why the Panic Button Is an OR", [
            "'Any one button': three-input OR",
            "Parallel switches; series would never sound",
            "Buzzer and lamp in parallel",
            "LED: 330 ohm resistor, long leg to plus",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Drawing the Circuit Diagram With Standard Symbols
        self.next_band(1)
        self.write_rows(1, "Drawing the Circuit Diagram With Standard Symbols", [
            "Battery left; three branches; six dots",
            "Push-to-make symbols B, S, T",
            "Toggle R in parallel as reset",
            "Zero standby; toilet lead noted",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): The Eight-Row Truth Table and Testing the Built Circuit
        self.next_band(2)
        self.write_rows(2, "The Eight-Row Truth Table and Testing the Built Circuit", [
            "Eight rows 000 to 111",
            "One 0, seven 1s",
            "Test each row; failed row locates fault",
            "Loudness, reset, standby: met or not",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Switches in series, an AND''",
            "``Buzzer and lamp in series''",
            "``Four-row table for three inputs''",
            "``No junction dots''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Which Gate Does the Spec Ask For?
        self.next_band(4)
        self.write_rows(4, "Which Gate Does the Spec Ask For?", [
            "Read the spec, do not assume",
            "Series shares volts; buzzer may fail",
            "Match battery to buzzer and lamp",
            "State the rejected alternative",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Drawing It Properly
        self.next_band(5)
        self.write_rows(5, "Drawing It Properly", [
            "Relay latch is Grade 9",
            "Title, name, date",
            "Partner traces each switch alone",
            "Diagram, not wiring plan",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Eight Rows and a Bench Test
        self.next_band(6)
        self.write_rows(6, "Eight Rows and a Bench Test", [
            "Alarm with nothing pressed: short or closed switch",
            "Two-button rows catch mis-wiring",
            "Diagram, table, test record",
            "No dots, no clarity",
        ], scale=0.9, box=2)

        last = Tex("The spec's 'any one button' is a three-input OR: three parallel switches, buzzer and lamp in parallel, a reset toggle, eight rows with a single 0, and every row tested.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
