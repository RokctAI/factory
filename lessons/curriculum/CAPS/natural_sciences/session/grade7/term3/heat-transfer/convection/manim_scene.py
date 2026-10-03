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

# Band-layout whiteboard scene for convection (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (140/150/140/120/120/120 of 790 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ConvectionSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Convection in liquids
        self.write_rows(0, "Convection in liquids", [
            "Heated fluid expands, less dense, rises",
            "Cooler, denser fluid sinks to replace it",
            "Loop = convection current",
            "Purple dye traces the current",
        ], scale=0.88, box=1)

        # --- Band 1 (subtopic_2): Convection in air
        self.next_band(1)
        self.write_rows(1, "Convection in air", [
            "Warm air rises; cool air sinks",
            "Room loop: heater, ceiling, far wall, floor",
            "Heaters low, coolers high",
            "Smoke, hot-air balloons, chimneys",
        ], scale=0.88, box=3)

        # --- Band 2 (subtopic_3): Convection in nature
        self.next_band(2)
        self.write_rows(2, "Convection in nature", [
            "Sea breeze by day, land breeze by night",
            "Thermals lift vultures and paragliders",
            "Afternoon thunderstorms",
            "Oceans and air carry heat to the poles",
        ], scale=0.88, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Heat rises by itself''",
            "``Convection in solids''",
            "``Warm water has less water in it''",
            "``Straight-line convection arrows''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Moving water carries heat
        self.next_band(4)
        self.write_rows(4, "Moving water carries heat", [
            "Warm water rises",
            "Cool water sinks",
            "Round and round: convection current",
            "Purple dye shows the loop",
        ], scale=0.88, box=1)

        # --- Band 5 (subtopic_5): Moving air carries heat
        self.next_band(5)
        self.write_rows(5, "Moving air carries heat", [
            "Warm air up, cool air down",
            "Ceiling warmer than floor",
            "Heaters low, air conditioners high",
            "Smoke and balloons rise",
        ], scale=0.88, box=2)

        # --- Band 6 (subtopic_6): Wind and weather
        self.next_band(6)
        self.write_rows(6, "Wind and weather", [
            "Sea breeze by day, land breeze at night",
            "Warm wet air rises, storms by afternoon",
            "Birds ride rising warm air",
            "Convection needs a liquid or gas",
        ], scale=0.88, box=1)

        last = Tex("Warm fluid rises, cool fluid sinks: a convection current carries heat.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
