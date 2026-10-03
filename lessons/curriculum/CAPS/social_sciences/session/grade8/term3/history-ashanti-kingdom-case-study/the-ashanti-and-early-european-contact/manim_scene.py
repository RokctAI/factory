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

# Band-layout whiteboard scene for the-ashanti-and-early-european-contact (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (260/260/250/260/130/130/130 of 1420 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class AshantiEarlyContactSession(MovingCameraScene):
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
        # --- Band 0: The rise of the Asante
        self.write_rows(0, "The rise of the Asante", [
            "Osei Tutu and Okomfo Anokye",
            "The Golden Stool",
            "Independence, about 1701",
            "Kumasi: roads and officials",
        ], scale=0.86, box=1)
        # --- Band 1: Gold, trade and the coast
        self.next_band(1)
        self.write_rows(1, "Gold, trade and the coast", [
            "Gold dust as money",
            "Kola nuts to the north",
            "Elmina, 1482",
            "Forts and the slave trade",
        ], scale=0.86, box=2)
        # --- Band 2: Envoys and war
        self.next_band(2)
        self.write_rows(2, "Envoys and war", [
            "Bowdich in Kumasi, 1817",
            "Asante envoys and princes",
            "Nsamankow, 1824",
            "Katamanso, 1826",
        ], scale=0.86, box=2)
        # --- Band 3: Sources and time
        self.next_band(3)
        self.write_rows(3, "Sources and time", [
            "Oral traditions",
            "European eyewitnesses",
            "1901 - 1701 = 200 years",
            "No one sat on the stool",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: The Golden Stool
        self.next_band(4)
        self.write_rows(4, "The Golden Stool", [
            "One nation, one stool",
        ], scale=0.86, box=0)
        # --- Band 5: Gold and forts
        self.next_band(5)
        self.write_rows(5, "Gold and forts", [
            "Gold dust and coastal forts",
        ], scale=0.86, box=0)
        # --- Band 6: Talking and fighting
        self.next_band(6)
        self.write_rows(6, "Talking and fighting", [
            "Equals and rivals",
        ], scale=0.86, box=0)
        self.wait(4)
