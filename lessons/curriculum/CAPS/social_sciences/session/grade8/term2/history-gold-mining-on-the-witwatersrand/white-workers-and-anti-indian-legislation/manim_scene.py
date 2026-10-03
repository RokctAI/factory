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

# Band-layout whiteboard scene for white-workers-and-anti-indian-legislation (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (240/250/250/220/150/150/150 of 1410 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class WhiteWorkersAndAntiIndianLegislationSession(MovingCameraScene):
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
        # --- Band 0: Skilled white workers
        self.write_rows(0, "Skilled white workers", [
            "From Cornwall, Australia, America",
            "High wages and unions",
            "Fear of cheaper black workers",
            "The colour bar",
        ], scale=0.86, box=3)
        # --- Band 1: Poor whites
        self.next_band(1)
        self.write_rows(1, "Poor whites", [
            "Small farms, rinderpest, drought, war",
            "Unskilled in the towns",
            "The poor white problem",
            "63 000 Chinese workers, 1904 to 1907",
        ], scale=0.86, box=2)
        # --- Band 2: Anti-Indian laws
        self.next_band(2)
        self.write_rows(2, "Anti-Indian laws", [
            "Transvaal Law 3 of 1885",
            "Free State ban, 1891",
            "Natal: £3 tax, vote, immigration",
            "Black Act, 1907",
        ], scale=0.86, box=2)
        # --- Band 3: Divisions were made
        self.next_band(3)
        self.write_rows(3, "Divisions were made", [
            "10 $\\times$ 12 = 120 shillings",
            "60 is half of 120",
            "Workers divided, not united",
            "Laws made about, not by",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: The skilled workers
        self.next_band(4)
        self.write_rows(4, "The skilled workers", [
            "Jobs kept for whites",
        ], scale=0.86, box=0)
        # --- Band 5: Poor whites
        self.next_band(5)
        self.write_rows(5, "Poor whites", [
            "Off the land, into the towns",
        ], scale=0.86, box=0)
        # --- Band 6: Laws against Indians
        self.next_band(6)
        self.write_rows(6, "Laws against Indians", [
            "Land, tax, vote, fingerprints",
        ], scale=0.86, box=0)
        self.wait(4)
