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

# Band-layout whiteboard scene for core-mantle-crust-and-tectonic-plates (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (200/170/200/210/90/90/100 of 1060 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CoreMantleCrustAndTectonicPlatesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.8, box=None, box_color=YELLOW):
        t = Tex(title).scale(1.1).shift(band_shift(k) + UP * 2.4)
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
        # --- Band 0: The Layers of the Earth
        self.write_rows(0, "The Layers of the Earth", [
            "Crust: thin rocky skin, 5 to 70 km",
            "Mantle: about 2900 km of hot, slowly flowing rock",
            "Outer core: liquid iron and nickel",
            "Inner core: solid, about 5000 to 6000 degrees C",
        ], scale=0.8, box=1)
        # --- Band 1: How We Know What Is Inside
        self.next_band(1)
        self.write_rows(1, "How We Know What Is Inside", [
            "Deepest hole: about 12 km",
            "SA gold mines: about 4 km deep",
            "Seismic waves reveal the layers",
            "Some waves cannot cross the liquid outer core",
        ], scale=0.8, box=2)
        # --- Band 2: Tectonic Plates
        self.next_band(2)
        self.write_rows(2, "Tectonic Plates", [
            "About 7 large plates and many small ones",
            "2 to 10 cm a year: fingernail speed",
            "Convection currents in the mantle",
            "Wegener 1912, du Toit: Pangaea",
        ], scale=0.86, box=1)
        # --- Band 3: Plate Boundaries
        self.next_band(3)
        self.write_rows(3, "Plate Boundaries", [
            "Divergent: apart, new crust, ridges and rifts",
            "Convergent: together, subduction, fold mountains",
            "Transform: sliding past, earthquakes",
            "South Africa: middle of the African Plate",
        ], scale=0.8, box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: A Peach With a Metal Stone
        self.next_band(4)
        self.write_rows(4, "A Peach With a Metal Stone", [
            "Skin: the crust",
            "Flesh: the mantle",
            "Stone: the iron core",
        ], scale=0.86, box=0)
        # --- Band 5: Giant Puzzle Pieces
        self.next_band(5)
        self.write_rows(5, "Giant Puzzle Pieces", [
            "Earthquake waves show the inside",
            "Plates move like growing fingernails",
            "Pangaea: all joined together",
        ], scale=0.86, box=0)
        # --- Band 6: Where Plates Meet
        self.next_band(6)
        self.write_rows(6, "Where Plates Meet", [
            "Apart: new crust",
            "Together: volcanoes and mountains",
            "Sliding: earthquakes",
        ], scale=0.86, box=0)
        self.wait(4)
