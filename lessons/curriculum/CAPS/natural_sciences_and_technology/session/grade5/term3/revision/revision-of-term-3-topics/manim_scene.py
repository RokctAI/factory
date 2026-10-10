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

# Band-layout whiteboard scene for revision-of-term-3-topics (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (270/170/140/110/110/110 of 910 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RevisionOfTerm3TopicsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Fuels, Burning and Fire Safety
        self.write_rows(0, "Fuels, Burning and Fire Safety", [
            "Fuels store energy",
            "Burning: heat and light",
            "Needs fuel, heat, oxygen",
            "Candles in sand, call 10177",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Cells, Circuits and Mains Electricity
        self.next_band(1)
        self.write_rows(1, "Cells, Circuits and Mains Electricity", [
            "Cells store energy",
            "Complete circuit lights bulb",
            "Coal, steam, turbine, generator",
            "Dry hands, stay away from lines",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Elastic, Springs and Movement
        self.next_band(2)
        self.write_rows(2, "Elastic, Springs and Movement", [
            "Stretch, twist, compress",
            "More stretch, more energy",
            "Release gives movement",
            "Energy came from the Sun",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Food is not a fuel''",
            "``A fire only needs fuel''",
            "``A switch makes electricity''",
            "``An unstretched band stores energy''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Fuel and Fire
        self.next_band(4)
        self.write_rows(4, "Fuel and Fire", [
            "Fuel and fire",
            "Fuel stores energy",
            "Fuel, heat, oxygen",
            "Stay safe",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Electricity
        self.next_band(5)
        self.write_rows(5, "Electricity", [
            "Electricity",
            "Cells and circuits",
            "Power stations",
            "Stay safe",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Springs and Elastic
        self.next_band(6)
        self.write_rows(6, "Springs and Elastic", [
            "Springs and elastic",
            "Stretch or squash",
            "Let go",
            "It moves",
        ], scale=0.9, box=3)

        last = Tex("Energy is stored in fuels, cells, elastic and springs, and is released as heat, light, electrical energy or movement, which we must use safely.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
