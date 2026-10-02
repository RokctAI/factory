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

# Band-layout whiteboard scene for properties-of-metals-semi-metals-and-non-metals (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (240/230/210/230/180/190/190 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PropertiesOfMetalsNonMetalsSession(MovingCameraScene):
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
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1)
        self.write_rows(0, 'Metals', [
            'Lustrous, conduct heat and electricity',
            'Malleable (sheets), ductile (wires), sonorous',
            'Exceptions: mercury liquid at $-39^\\circ$C; sodium 0.97 g/cm$^3$',
            'Copper wiring, aluminium cables, gold contacts',
        ], scale=0.8, box=1)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, 'Non-metals', [
            'Dull, insulators, brittle, low melting points',
            '11 gases, 1 liquid (bromine), the rest solids',
            'Graphite conducts; diamond hardest, does not',
            'Chlorine purifies water; helium balloons',
        ], scale=0.8, box=2)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, 'Semi-metals: B, Si, Ge, As, Sb, Te', [
            'Silicon: shiny but brittle',
            'Semiconductor: conducts a little',
            'Conductivity rises with heat or light',
            'Chips, solar panels; boron heat-proof glass',
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, 'A fair conductivity test', [
            'Change: the sample. \\ Observe: the bulb',
            'Keep: cell, bulb, wires, sample size',
            'Sand samples clean of oxide',
            'Property, because, use',
        ], scale=0.82, box=2)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        errs = [
            "``All metals are hard and heavy''",
            "``All metals are solid''",
            "``No non-metal conducts''",
            "``Malleable means drawn into wires''",
        ]
        for i, e in enumerate(errs):
            m = Tex(e).scale(0.85).shift(band_shift(4) + UP * (1.3 - 1.0 * i))
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5)
        self.next_band(5)
        self.write_rows(5, 'The metal personality', [
            'Shiny, conducts, flattens, stretches',
            'Surprises: mercury, sodium, gallium',
            'Copper wires, aluminium planes, gold rings',
        ], scale=0.85, box=0)

        # --- Band 6 (subtopic_6)
        self.next_band(6)
        self.write_rows(6, 'The non-metal personality', [
            'Dull, insulating, brittle, often gas',
            'Pencil lead conducts: graphite',
            'Diamond: same carbon, hardest of all',
        ], scale=0.85, box=1)

        # --- Band 7 (subtopic_7)
        self.next_band(7)
        self.write_rows(7, 'The in-betweeners', [
            'Silicon: shiny, brittle, half-hearted conductor',
            'Heat or light: conducts better',
            'Chips and solar panels',
        ], scale=0.85, box=0)

        last = Tex('Shine, bend, conduct: three tests.').scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
