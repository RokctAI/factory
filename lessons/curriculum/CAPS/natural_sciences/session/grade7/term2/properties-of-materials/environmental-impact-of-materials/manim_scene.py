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

# Band-layout whiteboard scene for environmental-impact-of-materials (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (150/150/170/120/120/120 of 830 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class EnvironmentalImpactOfMaterialsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Metals: mining and processing
        self.write_rows(0, "Metals: mining and processing", [
            "Land: pits, waste rock, tailings dumps, dust",
            "Water: acid mine drainage carries heavy metals",
            "Air: smelting uses coal, releases CO2 and SO2",
            "Reduce: rehabilitate, treat water, recycle",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Plastics
        self.next_band(1)
        self.write_rows(1, "Plastics", [
            "From oil, gas or coal; light, cheap, waterproof",
            "Do not biodegrade; break into microplastics",
            "Turtles, seabirds, blocked drains, Durban beaches",
            "Reduce, reuse, recycle (PET 1, HDPE 2)",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Fuels
        self.next_band(2)
        self.write_rows(2, "Fuels", [
            "Coal: most electricity; Secunda fuels",
            "Burning: CO2 and climate change",
            "Air pollution: SO2, soot, indoor smoke, Highveld",
            "Use less; solar and wind; cleaner cooking",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Recycling is the first step''",
            "``Plastics rot away quickly''",
            "``Mining only affects the land''",
            "``Burning fuel only makes local smoke''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): The story of a can
        self.next_band(4)
        self.write_rows(4, "The story of a can", [
            "Iron ore from an open pit",
            "Furnace with coal: CO2",
            "Used for a few minutes",
            "Recycle: new steel, over and over",
        ], scale=0.88, box=3)

        # --- Band 5 (subtopic_5): The story of a bottle
        self.next_band(5)
        self.write_rows(5, "The story of a bottle", [
            "From oil, gas or coal",
            "Does not rot; breaks into microplastics",
            "Turtles, seabirds, blocked drains",
            "Reduce, reuse, recycle; thank waste pickers",
        ], scale=0.88, box=1)

        # --- Band 6 (subtopic_6): The story of a lump of coal
        self.next_band(6)
        self.write_rows(6, "The story of a lump of coal", [
            "Coal mines scar land and leak acid",
            "Power stations: dirty air, asthma",
            "CO2: a hotter planet",
            "Use less; Sun and wind burn nothing",
        ], scale=0.88, box=3)

        last = Tex("Every material has a story: extraction, use and what happens after.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
