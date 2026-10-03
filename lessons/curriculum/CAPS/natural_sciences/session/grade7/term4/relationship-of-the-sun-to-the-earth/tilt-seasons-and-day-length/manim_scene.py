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

# Band-layout whiteboard scene for tilt-seasons-and-day-length (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (140/120/130/120/120/120 of 750 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TiltSeasonsAndDayLengthSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Tilt and orbit
        self.write_rows(0, "Tilt and orbit", [
            "Rotation: 24 h (day and night)",
            "Revolution: 365¼ days (a year)",
            "Axis tilted 23,5$^\\circ$, always pointing the same way",
            "Hemispheres take turns leaning to the Sun",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Seasons
        self.next_band(1)
        self.write_rows(1, "Seasons", [
            "Tilt, not distance, causes seasons",
            "Tilted towards: high Sun, concentrated rays, summer",
            "Tilted away: low Sun, spread rays, winter",
            "Opposite seasons north and south",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Day length
        self.next_band(2)
        self.write_rows(2, "Day length", [
            "Tilted towards: long days (21 Dec solstice)",
            "Tilted away: short days (21 June solstice)",
            "Equinoxes: about 12 h each",
            "Bigger changes further from the equator",
        ], scale=0.88, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Closer to the Sun means summer''",
            "``The axis rocks back and forth''",
            "``Same seasons in both hemispheres''",
            "``Day and night are always equal''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A leaning planet
        self.next_band(4)
        self.write_rows(4, "A leaning planet", [
            "Spins: day and night",
            "Goes round the Sun: a year",
            "Leans 23,5$^\\circ$, always the same way",
            "Halves take turns leaning to the Sun",
        ], scale=0.88, box=1)

        # --- Band 5 (subtopic_5): Summer and winter
        self.next_band(5)
        self.write_rows(5, "Summer and winter", [
            "Lean towards: high Sun, strong heat",
            "Lean away: low Sun, spread-out heat",
            "Torch: straight bright, tilted dim",
            "Not about distance",
        ], scale=0.88, box=2)

        # --- Band 6 (subtopic_6): Long days, short days
        self.next_band(6)
        self.write_rows(6, "Long days, short days", [
            "Summer: long days",
            "Winter: short days",
            "March and September: about equal",
            "Further from the equator: bigger change",
        ], scale=0.88, box=1)

        last = Tex("A 23,5$^\\circ$ tilt, one orbit a year: seasons and changing day length.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
