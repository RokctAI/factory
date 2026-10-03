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

# Band-layout whiteboard scene for shifting-balance-of-power-1902-to-1910 (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (260/260/240/270/130/130/130 of 1420 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ShiftingBalanceOfPowerSession(MovingCameraScene):
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
        # --- Band 0: War and peace
        self.write_rows(0, "War and peace", [
            "Gold in the Transvaal",
            "South African War, 1899 to 1902",
            "Peace of Vereeniging, 1902",
            "Black vote postponed",
        ], scale=0.86, box=3)
        # --- Band 1: New voices
        self.next_band(1)
        self.write_rows(1, "New voices", [
            "APO, 1902: Dr Abdurahman",
            "Transvaal Indians organise, 1903",
            "Gandhi and satyagraha, 1906",
            "Petitions, papers, delegations",
        ], scale=0.86, box=0)
        # --- Band 2: Bambatha and Union
        self.next_band(2)
        self.write_rows(2, "Bambatha and Union", [
            "Poll tax, 1905",
            "Bambatha Rebellion, 1906",
            "Union of South Africa, 1910",
            "Only white men in Parliament",
        ], scale=0.86, box=3)
        # --- Band 3: Sources and calculations
        self.next_band(3)
        self.write_rows(3, "Sources and calculations", [
            "1 276 000 $\\div$ 5 973 000 = 0.21",
            "About one in five white",
            "Reconciliation or exclusion?",
            "Ask who made the source",
        ], scale=0.86, box=0)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: War and peace
        self.next_band(4)
        self.write_rows(4, "War and peace", [
            "Gold, war, peace, 1902",
        ], scale=0.86, box=0)
        # --- Band 5: People get organised
        self.next_band(5)
        self.write_rows(5, "People get organised", [
            "APO, Indians, Bambatha",
        ], scale=0.86, box=0)
        # --- Band 6: One country, whose country?
        self.next_band(6)
        self.write_rows(6, "One country, whose country?", [
            "Union, 1910",
        ], scale=0.86, box=0)
        self.wait(4)
