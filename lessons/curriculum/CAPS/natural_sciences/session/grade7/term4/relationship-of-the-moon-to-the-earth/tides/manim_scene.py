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

# Band-layout whiteboard scene for tides (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (130/120/130/120/120/120 of 740 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TidesSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What causes the tides
        self.write_rows(0, "What causes the tides", [
            "Tide: regular rise and fall of the sea",
            "Moon's gravity pulls the ocean into bulges",
            "Two bulges: towards and away from the Moon",
            "Earth spins: two highs, two lows (about 24 h 50 min)",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Spring and neap tides
        self.next_band(1)
        self.write_rows(1, "Spring and neap tides", [
            "Sun's tidal effect: just under half the Moon's",
            "Spring: in line (new, full): biggest range",
            "Neap: right angles (quarters): smallest range",
            "Tide tables predict times and heights",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Shoreline ecosystems
        self.next_band(2)
        self.write_rows(2, "Shoreline ecosystems", [
            "Intertidal zone: covered, then exposed",
            "Limpets clamp, mussels shut, anemones fold",
            "Rock pools: klipfish, crabs, octopus",
            "Oystercatchers feed at low tide",
        ], scale=0.88, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Wind causes the tides''",
            "``Spring tides only in spring''",
            "``Only one high tide a day''",
            "``No bulge on the far side''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): The Moon pulls the sea
        self.next_band(4)
        self.write_rows(4, "The Moon pulls the sea", [
            "Tide: the sea rises and falls",
            "Moon pulls the water into bulges",
            "Two bulges",
            "Two highs and two lows a day",
        ], scale=0.88, box=1)

        # --- Band 5 (subtopic_5): Big and small tides
        self.next_band(5)
        self.write_rows(5, "Big and small tides", [
            "Line up: spring tides, extra big",
            "Right angles: neap tides, small",
            "Sun pulls less than the Moon",
            "Tide tables predict them",
        ], scale=0.88, box=2)

        # --- Band 6 (subtopic_6): Life between the tides
        self.next_band(6)
        self.write_rows(6, "Life between the tides", [
            "Covered, then exposed, twice a day",
            "Limpets clamp, mussels shut, anemones fold",
            "Rock pools are shelters",
            "Look, do not take",
        ], scale=0.88, box=1)

        last = Tex("The Moon's pull makes the tides; spring and neap tides shape the shore.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
