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

# Band-layout whiteboard scene for physical-properties-and-uses (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (150/140/180/120/120/120 of 830 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PhysicalPropertiesAndUsesSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Melting and boiling points
        self.write_rows(0, "Melting and boiling points", [
            "Physical property: measured without changing the substance",
            "Water: melts 0, boils 100 degrees at sea level",
            "Pots: high melting point; solder and fuses: low",
            "Higher altitude: lower boiling point",
        ], scale=0.76, box=2)

        # --- Band 1 (subtopic_2): Conductors and insulators
        self.next_band(1)
        self.write_rows(1, "Conductors and insulators", [
            "Electrical conductors: copper, aluminium, steel, graphite",
            "Insulators: plastic, rubber, glass, dry wood",
            "Test: bulb lights = conductor",
            "Heat: metals conduct; wood, plastic, trapped air insulate",
        ], scale=0.76, box=1)

        # --- Band 2 (subtopic_3): Strength, hardness, flexibility, density
        self.next_band(2)
        self.write_rows(2, "Strength, hardness, flexibility, density", [
            "Strong: steel; hard but brittle: glass",
            "Flexible and elastic: rubber",
            "Density: lead 11, steel 8, aluminium 2,7, water 1",
            "Match SEVERAL properties to the job",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Hard means strong''",
            "``Water always conducts well''",
            "``All metals are heavy''",
            "``Insulators are useless''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Will it melt?
        self.next_band(4)
        self.write_rows(4, "Will it melt?", [
            "Chocolate 34, wax 60, iron about 1 500 degrees",
            "Potjie pot: iron in the coals",
            "Water boils lower up high",
            "Solder: low melting point, joins wires",
        ], scale=0.82, box=1)

        # --- Band 5 (subtopic_5): Let it through or keep it out
        self.next_band(5)
        self.write_rows(5, "Let it through or keep it out", [
            "Bulb lights: conductor; stays dark: insulator",
            "Cable: copper inside, plastic outside",
            "Metal spoon gets hot; wooden spoon stays cool",
            "Never touch plugs with wet hands",
        ], scale=0.82, box=0)

        # --- Band 6 (subtopic_6): Pick the right material
        self.next_band(6)
        self.write_rows(6, "Pick the right material", [
            "Strong: steel; hard but brittle: glass",
            "Flexible: rubber; elastic: rubber band",
            "Dense: lead; light: polystyrene; wood floats",
            "Window: glass; aeroplane: aluminium; potjie: iron",
        ], scale=0.82, box=3)

        last = Tex("The right property for the job: that is how materials are chosen.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
