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

# Band-layout whiteboard scene for requirements-for-sustaining-life (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (120/150/180/120/120/120 of 810 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RequirementsForSustainingLifeSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Requirement 1: energy
        self.write_rows(0, "Requirement 1: energy", [
            "All life processes use energy",
            "Producers capture sunlight by photosynthesis",
            "Herbivores eat plants; carnivores eat herbivores",
            "Sun also warms Earth and drives the water cycle",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Requirements 2 and 3: gases and water
        self.next_band(1)
        self.write_rows(1, "Requirements 2 and 3: gases and water", [
            "Oxygen for respiration: lungs, gills, roots",
            "CO2 (about 0,04\\%) for photosynthesis",
            "Nitrogen made usable by soil bacteria",
            "Water: reactions, transport, temperature, home",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Requirements 4 and 5: soil and temperature
        self.next_band(2)
        self.write_rows(2, "Requirements 4 and 5: soil and temperature", [
            "Soil: anchors roots, gives minerals, houses decomposers",
            "Loam best; topsoil forms over hundreds of years",
            "Most life between 0 and 45 degrees",
            "Shortest supply = limiting factor (desert: water)",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Plants need only water and sunlight''",
            "``Fish do not need oxygen''",
            "``Soil is just dead dirt''",
            "``Every organism needs the same temperature''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.78).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): The survival backpack
        self.next_band(4)
        self.write_rows(4, "The survival backpack", [
            "Energy, gases, water, soil, temperature",
            "Plants: energy from sunlight",
            "You: about 60\\% water",
            "Most life likes 0 to 45 degrees",
        ], scale=0.88, box=0)

        # --- Band 5 (subtopic_5): Forest and desert
        self.next_band(5)
        self.write_rows(5, "Forest and desert", [
            "Forest: rain all year, deep soil, mild",
            "Desert: same Sun and air, little rain, thin soil",
            "Desert plants store water in fat leaves",
            "Shortest item = limiting factor",
        ], scale=0.82, box=3)

        # --- Band 6 (subtopic_6): Keep the backpack full
        self.next_band(6)
        self.write_rows(6, "Keep the backpack full", [
            "Pollution: algae, no oxygen, dead fish",
            "Bare soil washes away in one storm",
            "South Africa is a dry country: save water",
            "Clean water, healthy soil, clean air, plants",
        ], scale=0.88, box=3)

        last = Tex("Energy, gases, water, soil and the right temperature keep life going.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
