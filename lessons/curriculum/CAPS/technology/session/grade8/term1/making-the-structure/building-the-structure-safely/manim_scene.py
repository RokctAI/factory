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

# Band-layout whiteboard scene for building-the-structure-safely (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/190/160/120/110/90 of 850 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BuildingStructureSafelySession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Planning the Build
        self.write_rows(0, "Planning the Build", [
            "Cutting list: part, quantity, size, material",
            "Sequence: cut, base, uprights, braces, axle, test",
            "Share the jobs; nobody idle",
            "Mark out in pencil, labelled",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Safe Working Practices
        self.next_band(1)
        self.write_rows(1, "Safe Working Practices", [
            "Knife: mat, steel ruler, away, fingers back",
            "Wire: pliers, goggles, tape the ends",
            "Glue gun: handle only; cold water",
            "Clear desk, tools in a tray, count them back",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Building Frame and Mechanism Together
        self.next_band(2)
        self.write_rows(2, "Building Frame and Mechanism Together", [
            "Base square: equal diagonals",
            "Uprights with a set square, then braces",
            "Holes opened to turn free; card washers",
            "Load gradually, fix, photograph",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Cut parts as you need them''",
            "``Glue uprights before the base sets''",
            "``Force the dowel through a tight hole''",
            "``Test with the full load first''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Before You Cut
        self.next_band(4)
        self.write_rows(4, "Before You Cut", [
            "Two lists before you cut",
            "Count the parts",
            "Order of work, who does what",
            "Mark every part in pencil",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Knives, Wire and Glue
        self.next_band(5)
        self.write_rows(5, "Knives, Wire and Glue", [
            "Mat under, steel ruler beside",
            "Cut away, light passes, blade in",
            "Pliers and goggles for wire",
            "Handle only on the glue gun",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Putting It Together
        self.next_band(6)
        self.write_rows(6, "Putting It Together", [
            "Base, check square, let it set",
            "Uprights, top rails, braces",
            "Dowel spins free, washer round the hole",
            "Load bit by bit, photos",
        ], scale=0.9, box=2)

        last = Tex("Plan the parts and the order, follow the tool rules, build base to braces to axle, and test gradually: that is how the model gets made safely.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
