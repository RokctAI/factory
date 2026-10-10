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

# Band-layout whiteboard scene for places-in-the-news-on-a-map (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (260/130/140/110/110/110 of 860 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PlacesInTheNewsOnAMapSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): From the News to the Atlas
        self.write_rows(0, "From the News to the Atlas", [
            "Find the place name",
            "Look it up in the index",
            "Read latitude and longitude",
            "Pin it with date and headline",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Stories on the Map
        self.next_band(1)
        self.write_rows(1, "Stories on the Map", [
            "Durban floods, 2022",
            "Cyclone Idai, Beira, 2019",
            "Morocco earthquake, 2023",
            "Rugby final, Paris, 2023",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Asking Geography Questions
        self.next_band(2)
        self.write_rows(2, "Asking Geography Questions", [
            "Why did it happen here?",
            "What is the place like?",
            "Who was affected?",
            "Look for patterns",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Pin it without the atlas''",
            "``Similar names are the same place''",
            "``Trust every forwarded message''",
            "``Pin it and stop''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Four Steps
        self.next_band(4)
        self.write_rows(4, "Four Steps", [
            "Name",
            "Index",
            "Degrees",
            "Pin",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Pins on the Wall
        self.next_band(5)
        self.write_rows(5, "Pins on the Wall", [
            "Floods",
            "Cyclone",
            "Earthquake",
            "Rugby",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Why Here
        self.next_band(6)
        self.write_rows(6, "Why Here", [
            "Why",
            "Where",
            "Who",
            "Patterns",
        ], scale=0.9, box=0)

        last = Tex("Every news story happens somewhere, and a map in degrees helps us see where and ask why.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
