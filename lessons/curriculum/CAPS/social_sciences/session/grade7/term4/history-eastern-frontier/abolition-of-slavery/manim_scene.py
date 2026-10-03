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

# Band-layout whiteboard scene for abolition-of-slavery (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/180/190/180/90/90/90 of 1000 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class AbolitionOfSlaverySession(MovingCameraScene):
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
        # --- Band 0: Why Slavery Was Abolished
        self.write_rows(0, "Why Slavery Was Abolished", [
            "Abolitionists: Wilberforce, Clarkson, Equiano",
            "Rebellions: Jamaica 1831 to 1832",
            "Free labour argued to be better",
            "1807 trade ended; 1833 Abolition Act",
        ], scale=0.8, box=1)
        # --- Band 1: Steps Towards Abolition at the Cape
        self.next_band(1)
        self.write_rows(1, "Steps Towards Abolition at the Cape", [
            "1808: no new slaves imported",
            "1816: slave registration",
            "1820s amelioration laws; Protector of Slaves",
            "1 December 1834: abolition; apprenticeship",
        ], scale=0.86, box=4)
        # --- Band 2: Compensation and Reactions
        self.next_band(2)
        self.write_rows(2, "Compensation and Reactions", [
            "20 million pounds for owners empire-wide",
            "Cape owners: about 1.2 million pounds",
            "Enslaved people received nothing",
            "1 December 1838: full freedom",
        ], scale=0.86, box=4)
        # --- Band 3: What Freedom Meant
        self.next_band(3)
        self.write_rows(3, "What Freedom Meant", [
            "Many left the farms",
            "Moved to towns and mission stations",
            "Masters and Servants Ordinance, 1841",
            "No land or compensation for freed people",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Why Slavery Ended
        self.next_band(4)
        self.write_rows(4, "Why Slavery Ended", [
            "Campaigners in Britain",
            "Rebellions by the enslaved",
            "1807 trade ends; 1833 law",
        ], scale=0.86, box=0)
        # --- Band 5: Ending Slavery at the Cape
        self.next_band(5)
        self.write_rows(5, "Ending Slavery at the Cape", [
            "1808: no new slaves",
            "1834: slavery abolished",
            "Apprentices until 1838; owners paid",
        ], scale=0.86, box=0)
        # --- Band 6: Free at Last?
        self.next_band(6)
        self.write_rows(6, "Free at Last?", [
            "1 December 1838: celebrations",
            "Towns and mission stations",
            "No land, low wages",
        ], scale=0.86, box=0)
        self.wait(4)
