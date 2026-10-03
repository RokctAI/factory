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

# Band-layout whiteboard scene for camel-caravans-across-the-sahara (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (200/180/160/200/90/90/90 of 1010 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CamelCaravansAcrossTheSaharaSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.8, box=None, box_color=YELLOW):
        t = Tex(title).scale(1.1).shift(band_shift(k) + UP * 2.4)
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
        # --- Band 0: Doing History in Grade 7
        self.write_rows(0, "Doing History in Grade 7", [
            "History: the past, studied through evidence",
            "Primary: from the time; secondary: written later",
            "Ask who, when, why and for whom",
            "Identify, extract, evaluate, discuss",
        ], scale=0.8, box=1)
        # --- Band 1: Transport on Land Through Time
        self.next_band(1)
        self.write_rows(1, "Transport on Land Through Time", [
            "Porters on foot, then pack animals",
            "Donkeys, oxen, horses",
            "Wheels need firm, flat ground",
            "Horses and oxen need daily water and grass",
        ], scale=0.86, box=1)
        # --- Band 2: The Ship of the Desert
        self.next_band(2)
        self.write_rows(2, "The Ship of the Desert", [
            "Dromedary: one-humped camel",
            "Hump stores fat, not water",
            "Broad feet, closing nostrils, long lashes",
            "About 150 kg, 30 to 40 km a day",
        ], scale=0.86, box=1)
        # --- Band 3: The Camel Caravan
        self.next_band(3)
        self.write_rows(3, "The Camel Caravan", [
            "Caravan: travel together for safety",
            "About two months, in the cooler season",
            "Guides read stars, dunes and wells",
            "Oases: water in the desert",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: History Detectives
        self.next_band(4)
        self.write_rows(4, "History Detectives", [
            "Evidence, like a detective",
            "Primary: from then; secondary: later",
            "Who, when, why?",
        ], scale=0.86, box=0)
        # --- Band 5: The Amazing Camel
        self.next_band(5)
        self.write_rows(5, "The Amazing Camel", [
            "Horses and oxen need daily water",
            "Camel: a week without drinking",
            "The ship of the desert",
        ], scale=0.86, box=0)
        # --- Band 6: Two Months on Foot
        self.next_band(6)
        self.write_rows(6, "Two Months on Foot", [
            "Caravans of hundreds or thousands",
            "About two months across",
            "Guides: stars, dunes, wells",
        ], scale=0.86, box=0)
        self.wait(4)
