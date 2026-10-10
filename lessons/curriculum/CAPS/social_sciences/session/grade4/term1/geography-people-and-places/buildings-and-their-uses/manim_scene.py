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

# Band-layout whiteboard scene for buildings-and-their-uses (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/160/210/110/110/110 of 860 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BuildingsAndTheirUsesSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Houses and Animal Shelters
        self.write_rows(0, "Houses and Animal Shelters", [
            "House: a home for people",
            "Brick, iron, mud and thatch",
            "Kraal: keeps cattle safe",
            "Coop, stable, pigsty",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Shops, Schools, Clinics and Banks
        self.next_band(1)
        self.write_rows(1, "Shops, Schools, Clinics and Banks", [
            "Service: done for people",
            "Shop, school, clinic, bank",
            "Hospital: doctors and beds",
            "Post office, police, library",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Places of Worship, Factories and Stations
        self.next_band(2)
        self.write_rows(2, "Places of Worship, Factories and Stations", [
            "Worship: church, mosque, temple",
            "Factory: makes goods",
            "Station: journeys start and end",
            "More buildings in bigger places",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``A kraal is a house for people''",
            "``A clinic is a hospital''",
            "``Every religion uses a church''",
            "``Factories sell goods''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Homes for People and Animals
        self.next_band(4)
        self.write_rows(4, "Homes for People and Animals", [
            "House: a home",
            "Kraal: cattle",
            "Coop: chickens",
            "Keep animals safe",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Service Buildings
        self.next_band(5)
        self.write_rows(5, "Service Buildings", [
            "Shop: buying",
            "School: learning",
            "Clinic: getting well",
            "Bank: money safe",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Worship, Making and Travelling
        self.next_band(6)
        self.write_rows(6, "Worship, Making and Travelling", [
            "Worship",
            "Factory: making",
            "Station: travelling",
            "Every building has a use",
        ], scale=0.9, box=1)

        last = Tex("Every building has a use, and bigger settlements have more kinds of buildings.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
