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

# Band-layout whiteboard scene for properties-of-metals-non-metals-and-semi-metals (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (150/140/160/120/120/120 of 810 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PropertiesOfMetalsNonMetalsAndSemiMetalsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Properties of metals
        self.write_rows(0, "Properties of metals", [
            "Lustre: shiny when cut or polished",
            "Conduct heat and electricity",
            "Malleable (sheets), ductile (wires), sonorous",
            "High melting points; mercury liquid; only some magnetic",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Properties of non-metals
        self.next_band(1)
        self.write_rows(1, "Properties of non-metals", [
            "Many are gases; bromine liquid; some solids",
            "Dull, brittle, poor conductors (insulators)",
            "Low melting points (sulphur about 115 degrees)",
            "Carbon: graphite conducts; diamond hardest",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Semi-metals and the comparison
        self.next_band(2)
        self.write_rows(2, "Semi-metals and the comparison", [
            "Staircase: boron, silicon, germanium, arsenic",
            "Silicon: shiny but brittle; a semiconductor",
            "Chips (transistors) and solar panels",
            "Tests: look, bulb circuit, gentle tap",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``All metals are magnetic''",
            "``All non-metals are gases''",
            "``No non-metal conducts electricity''",
            "``Silicon is a metal because it is shiny''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Metal superpowers
        self.next_band(4)
        self.write_rows(4, "Metal superpowers", [
            "Shine when polished",
            "Carry electricity and heat",
            "Hammer flat; stretch into wire; ring like a bell",
            "Mercury is liquid; only some are magnetic",
        ], scale=0.82, box=1)

        # --- Band 5 (subtopic_5): The opposite team
        self.next_band(5)
        self.write_rows(5, "The opposite team", [
            "Many are gases: oxygen, nitrogen",
            "Solids are dull and brittle",
            "Insulators: the plastic keeps you safe",
            "Carbon: graphite conducts; diamond is hardest",
        ], scale=0.82, box=1)

        # --- Band 6 (subtopic_6): Somewhere in between
        self.next_band(6)
        self.write_rows(6, "Somewhere in between", [
            "Silicon: shiny but shatters",
            "Lets a controlled bit of current through",
            "Chips in cellphones; solar panels",
            "Tests: shiny? bulb lights? flattens or shatters?",
        ], scale=0.82, box=1)

        last = Tex("Shiny, conducting, bendable metals; dull, brittle, insulating non-metals.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
