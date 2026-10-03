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

# Band-layout whiteboard scene for slavery-in-west-africa-before-europeans (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/160/180/220/90/90/110 of 1040 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class SlaveryInWestAfricaBeforeEuropeansSession(MovingCameraScene):
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
        # --- Band 0: What the Transatlantic Slave Trade Was
        self.write_rows(0, "What the Transatlantic Slave Trade Was", [
            "Slavery: people treated as property",
            "About 12.5 million embarked; 10.5 million arrived",
            "Most to Brazil and the Caribbean",
            "Sources: records, Equiano, oral testimony",
        ], scale=0.8, box=1)
        # --- Band 1: West Africa Before the Atlantic Trade
        self.next_band(1)
        self.write_rows(1, "West Africa Before the Atlantic Trade", [
            "Kingdoms: Mali, Songhay, Benin, Oyo",
            "Wealth measured in people",
            "Pawnship: a person as security for debt",
            "Slavery existed in many societies",
        ], scale=0.86, box=1)
        # --- Band 2: The Nature of Slavery in West Africa
        self.next_band(2)
        self.write_rows(2, "The Nature of Slavery in West Africa", [
            "Captives of war, debt, crime, famine",
            "Farm, household, crafts, even soldiers",
            "Children could become part of the community",
            "Outsiders, not defined by race",
        ], scale=0.86, box=2)
        # --- Band 3: How the Atlantic Trade Changed Things
        self.next_band(3)
        self.write_rows(3, "How the Atlantic Trade Changed Things", [
            "Portuguese on the coast from the 1440s",
            "Chattel slavery: owned like property, forever",
            "Racist ideas used to justify it",
            "Guns for captives; Afonso of Kongo objects",
        ], scale=0.8, box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: A Terrible Trade
        self.next_band(4)
        self.write_rows(4, "A Terrible Trade", [
            "People treated as property",
            "Over 12 million taken across the Atlantic",
            "Equiano wrote his story in 1789",
        ], scale=0.86, box=0)
        # --- Band 5: Slavery in West Africa Before
        self.next_band(5)
        self.write_rows(5, "Slavery in West Africa Before", [
            "Power came from people",
            "Captives of war",
            "Children could join the community",
        ], scale=0.86, box=0)
        # --- Band 6: What Changed
        self.next_band(6)
        self.write_rows(6, "What Changed", [
            "Owned forever, children too",
            "Linked to race and racism",
            "Guns for captives at the forts",
        ], scale=0.86, box=0)
        self.wait(4)
