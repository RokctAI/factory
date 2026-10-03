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

# Band-layout whiteboard scene for nat-turner-and-the-amistad-mutiny (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/180/190/240/90/90/110 of 1090 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class NatTurnerAndTheAmistadMutinySession(MovingCameraScene):
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
        # --- Band 0: Rebellion in Context
        self.write_rows(0, "Rebellion in Context", [
            "Outnumbered, scattered, heavily policed",
            "1811 German Coast; 1822 Vesey plot",
            "Haiti 1791 to 1804: a free Black republic",
            "Causes, events, reactions, consequences",
        ], scale=0.86, box=1)
        # --- Band 1: Nat Turner's Revolt, 1831
        self.next_band(1)
        self.write_rows(1, "Nat Turner's Revolt, 1831", [
            "Born 1800 in Virginia; a preacher",
            "Revolt began 21 August 1831",
            "Crushed in about two days",
            "Captured 30 October; hanged 11 November",
        ], scale=0.86, box=1)
        # --- Band 2: Reactions and Consequences of the Revolt
        self.next_band(2)
        self.write_rows(2, "Reactions and Consequences of the Revolt", [
            "Revenge killings of innocent Black people",
            "Harsher laws: no reading, no gatherings",
            "Virginia rejects gradual emancipation, 1832",
            "Murderer or freedom fighter? Perspectives",
        ], scale=0.86, box=3)
        # --- Band 3: Sengbe Pieh and the Amistad, 1839
        self.next_band(3)
        self.write_rows(3, "Sengbe Pieh and the Amistad, 1839", [
            "Mende captives kidnapped illegally, 1839",
            "Sengbe Pieh leads the mutiny",
            "Supreme Court, 1841: they are free",
            "Survivors home to Sierra Leone, 1842",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Rising Up
        self.next_band(4)
        self.write_rows(4, "Rising Up", [
            "Outnumbered and heavily guarded",
            "Haiti free in 1804",
            "Why, what, who saw what, what changed",
        ], scale=0.86, box=0)
        # --- Band 5: Nat Turner
        self.next_band(5)
        self.write_rows(5, "Nat Turner", [
            "Preacher and prophet, Virginia 1831",
            "Crushed in two days; hanged",
            "Harsher laws afterwards",
        ], scale=0.86, box=0)
        # --- Band 6: The Amistad
        self.next_band(6)
        self.write_rows(6, "The Amistad", [
            "Chains broken, ship seized, 1839",
            "Supreme Court: free, 1841",
            "Home to Sierra Leone, 1842",
        ], scale=0.86, box=0)
        self.wait(4)
