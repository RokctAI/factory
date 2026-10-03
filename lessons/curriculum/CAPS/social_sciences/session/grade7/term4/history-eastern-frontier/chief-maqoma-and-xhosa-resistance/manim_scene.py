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

# Band-layout whiteboard scene for chief-maqoma-and-xhosa-resistance (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (170/200/180/190/90/90/90 of 1010 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ChiefMaqomaAndXhosaResistanceSession(MovingCameraScene):
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
        # --- Band 0: Maqoma's Background
        self.write_rows(0, "Maqoma's Background", [
            "Born 1798, eldest son of Ngqika",
            "Sandile was the heir; Maqoma regent",
            "Skilled warrior and speaker",
            "Settled in the Kat River valley",
        ], scale=0.86, box=1)
        # --- Band 1: Expulsion and the War of 1834 to 1835
        self.next_band(1)
        self.write_rows(1, "Expulsion and the War of 1834 to 1835", [
            "1829: expelled from the Kat River valley",
            "Land given to the Kat River Settlement",
            "1834: Maqoma and Tyhali lead invasion",
            "1836: Queen Adelaide Province returned",
        ], scale=0.86, box=2)
        # --- Band 2: The War of 1850 to 1853
        self.next_band(2)
        self.write_rows(2, "The War of 1850 to 1853", [
            "1847: British Kaffraria annexed",
            "Harry Smith humiliates Maqoma",
            "1850 to 1853: Mlanjeni's War",
            "Waterkloof guerrilla war; scorched earth",
        ], scale=0.86, box=4)
        # --- Band 3: Robben Island and Legacy
        self.next_band(3)
        self.write_rows(3, "Robben Island and Legacy", [
            "1857: arrested, sent to Robben Island",
            "1869: released; 1871 re-arrested",
            "Died on Robben Island, 1873",
            "Remembered as a great resistance leader",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Who Was Maqoma?
        self.next_band(4)
        self.write_rows(4, "Who Was Maqoma?", [
            "Born 1798, son of Ngqika",
            "Brave warrior, great speaker",
            "First tried to live peacefully",
        ], scale=0.86, box=0)
        # --- Band 5: Wars
        self.next_band(5)
        self.write_rows(5, "Wars", [
            "1829: driven out of Kat River",
            "1834: invasion of the colony",
            "1850 to 1853: forest guerrilla war",
        ], scale=0.86, box=0)
        # --- Band 6: Prisoner and Hero
        self.next_band(6)
        self.write_rows(6, "Prisoner and Hero", [
            "1857: Robben Island",
            "Died there in 1873",
            "Honoured as a hero",
        ], scale=0.86, box=0)
        self.wait(4)
