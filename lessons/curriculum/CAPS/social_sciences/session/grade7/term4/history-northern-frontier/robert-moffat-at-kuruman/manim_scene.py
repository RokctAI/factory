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

# Band-layout whiteboard scene for robert-moffat-at-kuruman (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/170/200/200/90/90/90 of 1020 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class RobertMoffatAtKurumanSession(MovingCameraScene):
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
        # --- Band 0: Missionaries and Traders on the Frontier
        self.write_rows(0, "Missionaries and Traders on the Frontier", [
            "LMS founded 1795; active in southern Africa",
            "Schools, translation, crops, irrigation",
            "Missions became trading centres",
            "Chiefs welcomed them for practical reasons",
        ], scale=0.86, box=1)
        # --- Band 1: Robert Moffat's Early Life
        self.next_band(1)
        self.write_rows(1, "Robert Moffat's Early Life", [
            "Born 1795, Scotland; trained as a gardener",
            "Arrived at the Cape in 1817",
            "Jager Afrikaner becomes a Christian",
            "1821: joins the Batlhaping mission",
        ], scale=0.86, box=3)
        # --- Band 2: The Kuruman Mission
        self.next_band(2)
        self.write_rows(2, "The Kuruman Mission", [
            "1824: mission at the Kuruman Eye",
            "Irrigation furrow; gardens and wheat",
            "Stone church completed 1838",
            "Setswana Bible: complete in 1857",
        ], scale=0.86, box=4)
        # --- Band 3: Relationships and Legacy
        self.next_band(3)
        self.write_rows(3, "Relationships and Legacy", [
            "Friend of Mzilikazi of the Ndebele",
            "Conversions slow at first",
            "Left Kuruman 1870; died 1883",
            "Legacy: literacy, but cultural disruption",
        ], scale=0.86, box=4)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Missionaries and Traders
        self.next_band(4)
        self.write_rows(4, "Missionaries and Traders", [
            "Spread Christianity",
            "Schools and translation",
            "Missions became trading centres",
        ], scale=0.86, box=0)
        # --- Band 5: Moffat's Story
        self.next_band(5)
        self.write_rows(5, "Moffat's Story", [
            "Born 1795, Scotland; a gardener",
            "Kuruman mission, 1824",
            "Furrow, church, school",
        ], scale=0.86, box=0)
        # --- Band 6: The Setswana Bible and Legacy
        self.next_band(6)
        self.write_rows(6, "The Setswana Bible and Legacy", [
            "Setswana Bible, 1857",
            "Printing press",
            "Friend of Mzilikazi",
        ], scale=0.86, box=0)
        self.wait(4)
