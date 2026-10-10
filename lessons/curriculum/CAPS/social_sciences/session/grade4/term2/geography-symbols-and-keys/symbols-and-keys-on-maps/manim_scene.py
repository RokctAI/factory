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

# Band-layout whiteboard scene for symbols-and-keys-on-maps (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/170/180/110/110/110 of 870 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SymbolsAndKeysOnMapsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What Symbols Are
        self.write_rows(0, "What Symbols Are", [
            "Symbol: stands for something real",
            "Pictures and letters",
            "Lines: river, road, railway",
            "Colours: blue for water",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Symbols on a Large-scale Map
        self.next_band(1)
        self.write_rows(1, "Symbols on a Large-scale Map", [
            "Large scale: small area, detail",
            "Small scale: big area, less detail",
            "Symbols for buildings",
            "Maps differ, so check",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Keys on South African Maps
        self.next_band(2)
        self.write_rows(2, "Keys on South African Maps", [
            "Key, or legend",
            "Usually in a corner box",
            "Title first, then the key",
            "Official symbols across South Africa",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Symbols are decorations''",
            "``Guess what a symbol means''",
            "``All maps use the same symbols''",
            "``Large scale shows a large area''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Map Code
        self.next_band(4)
        self.write_rows(4, "Map Code", [
            "Symbols",
            "Stand for real things",
            "Pictures and letters",
            "Blue for water",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Small Area, Lots of Detail
        self.next_band(5)
        self.write_rows(5, "Small Area, Lots of Detail", [
            "Large-scale map",
            "Small area",
            "Lots of detail",
            "Streets and buildings",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Crack the Code
        self.next_band(6)
        self.write_rows(6, "Crack the Code", [
            "Key",
            "Legend",
            "Meaning of symbols",
            "Look it up",
        ], scale=0.9, box=0)

        last = Tex("Symbols stand for real things, and the key tells us what each symbol means.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
