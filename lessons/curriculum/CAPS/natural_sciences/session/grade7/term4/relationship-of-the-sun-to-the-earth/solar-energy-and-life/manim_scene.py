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

# Band-layout whiteboard scene for solar-energy-and-life (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (130/130/160/120/120/120 of 780 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SolarEnergyAndLifeSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): The Sun, our energy source
        self.write_rows(0, "The Sun, our energy source", [
            "Star; nuclear reactions in the core",
            "Light, infrared (heat), ultraviolet",
            "Warms Earth, drives water cycle and winds",
            "Light for plants to make food",
        ], scale=0.88, box=1)

        # --- Band 1 (subtopic_2): Plants capture solar energy
        self.next_band(1)
        self.write_rows(1, "Plants capture solar energy", [
            "Producers: photosynthesis in chloroplasts",
            "Chlorophyll absorbs light",
            "CO₂ + water $\\rightarrow$ glucose + oxygen (light)",
            "Stored as chemical energy: grain, stem, tuber",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Food chains and webs
        self.next_band(2)
        self.write_rows(2, "Food chains and webs", [
            "Sun $\\rightarrow$ mealie $\\rightarrow$ grasshopper $\\rightarrow$ frog $\\rightarrow$ hawk",
            "Herbivore, carnivore, omnivore, decomposer",
            "Linked chains make a food web",
            "Only about a tenth passed on each step",
        ], scale=0.88, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Plants get food from the soil''",
            "``Arrows from eater to food''",
            "``Food chains without a producer''",
            "``All energy passes along''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): The Sun powers everything
        self.next_band(4)
        self.write_rows(4, "The Sun powers everything", [
            "A star sending light and heat",
            "Warms Earth, makes rain and wind",
            "Gives plants light",
            "No Sun: frozen and dark",
        ], scale=0.88, box=1)

        # --- Band 5 (subtopic_5): Plants catch sunlight
        self.next_band(5)
        self.write_rows(5, "Plants catch sunlight", [
            "Chlorophyll catches light",
            "Carbon dioxide + water $\\rightarrow$ sugar + oxygen",
            "Food stored in grains, stems, roots",
            "Stored Sun energy",
        ], scale=0.88, box=2)

        # --- Band 6 (subtopic_6): Passing it on
        self.next_band(6)
        self.write_rows(6, "Passing it on", [
            "Sun $\\rightarrow$ plant $\\rightarrow$ grasshopper $\\rightarrow$ frog $\\rightarrow$ hawk",
            "Arrows show the energy's path",
            "Only about a tenth passes on",
            "Pap is stored sunshine",
        ], scale=0.88, box=1)

        last = Tex("Sunlight, captured by plants, feeds almost every living thing on Earth.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
