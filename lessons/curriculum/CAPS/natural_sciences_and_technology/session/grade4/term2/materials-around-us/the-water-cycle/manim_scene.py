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

# Band-layout whiteboard scene for the-water-cycle (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/170/160/110/110/110 of 820 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TheWaterCycleSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Evaporating Water Rises
        self.write_rows(0, "Evaporating Water Rises", [
            "The Sun heats the sea",
            "Water evaporates and rises",
            "Salt stays behind",
            "Rivers, dams and leaves too",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Clouds, Rain, Hail and Snow
        self.next_band(1)
        self.write_rows(1, "Clouds, Rain, Hail and Snow", [
            "Cold air high up",
            "Vapour condenses into clouds",
            "Drops join and fall as rain",
            "Frozen: hail and snow",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Round and Round
        self.next_band(2)
        self.write_rows(2, "Round and Round", [
            "Snow melts into rivers",
            "Rivers flow to the sea",
            "Same water round and round",
            "The Sun drives the cycle",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Clouds are water vapour''",
            "``Rain is salty''",
            "``The cycle makes new water''",
            "``The Sun plays no part''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Up into the Sky
        self.next_band(4)
        self.write_rows(4, "Up into the Sky", [
            "Up into the sky",
            "Sun heats water",
            "Evaporates and rises",
            "Salt stays behind",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Down Again
        self.next_band(5)
        self.write_rows(5, "Down Again", [
            "Down again",
            "Condenses into clouds",
            "Rain, hail, snow",
            "Back to rivers",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Round and Round
        self.next_band(6)
        self.write_rows(6, "Round and Round", [
            "Round and round",
            "Melt and evaporate",
            "Condense and freeze",
            "Same water forever",
        ], scale=0.9, box=3)

        last = Tex("The Sun evaporates water, cold air condenses it into clouds, it falls again, and the same water goes round and round.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
