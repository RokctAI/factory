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

# Band-layout whiteboard scene for block-and-tackle-and-load-bearing-ropes (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/180/160/120/110/90 of 850 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BlockAndTackleAndLoadBearingRopesSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Combining Fixed and Movable Pulleys Into a Block and Tackle
        self.write_rows(0, "Combining Fixed and Movable Pulleys Into a Block and Tackle", [
            "Block = frame + sheaves; tackle = rope between two blocks",
            "Fixed block: pull down",
            "Movable block: load on several sections",
            "Boats, hoists, cranes",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Counting Load-Bearing Ropes to Find the Mechanical Advantage
        self.next_band(1)
        self.write_rows(1, "Counting Load-Bearing Ropes to Find the Mechanical Advantage", [
            "Ideal MA = number of load-bearing sections",
            "Same tension throughout the rope",
            "Hand rope from fixed block does not count",
            "Rope pulled = MA x lift",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Investigating Two-, Three- and Four-Rope Tackles
        self.next_band(2)
        self.write_rows(2, "Investigating Two-, Three- and Four-Rope Tackles", [
            "20 N: 2, 3, 4 sections -> ~10, 7, 5 N",
            "Rope: 400, 600, 800 mm for 200 mm lift",
            "Efficiency = actual / ideal, 70-90\\%",
            "Never stand under the load",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Hand rope from the fixed block counted''",
            "``Four sheaves assumed to mean MA 4''",
            "``Load expected to rise as far as rope pulled''",
            "``Ideal and measured MA confused''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Two Blocks, One Rope
        self.next_band(4)
        self.write_rows(4, "Two Blocks, One Rope", [
            "Two blocks, one rope",
            "Top block: pull down",
            "Bottom block: shares the load",
            "Workshop chain block",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Count the Ropes Holding the Load
        self.next_band(5)
        self.write_rows(5, "Count the Ropes Holding the Load", [
            "Count up-arrows at the bottom block",
            "Three ropes: pull a third",
            "Hand rope: no",
            "4 m rope per 1 m up",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): More Ropes, Less Pull, Longer Haul
        self.next_band(6)
        self.write_rows(6, "More Ropes, Less Pull, Longer Haul", [
            "Table 2, 3, 4 ropes",
            "A bit under the count",
            "Efficiency drops with more wheels",
            "Fingers clear, hook closed",
        ], scale=0.9, box=1)

        last = Tex("In a block and tackle the ideal mechanical advantage equals the number of rope sections supporting the movable block; more ropes mean less effort and more rope to haul.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
