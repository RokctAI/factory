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

# Band-layout whiteboard scene for ways-to-strengthen-paper (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (150/160/180/110/110/110 of 820 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class WaysToStrengthenPaperSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): A Flat Sheet Is Weak
        self.write_rows(0, "A Flat Sheet Is Weak", [
            "A flat sheet sags",
            "Thin and flexible",
            "Change the shape",
            "Fair test: same gap, same coins",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Folding and Rolling
        self.next_band(1)
        self.write_rows(1, "Folding and Rolling", [
            "Concertina fold: stiff",
            "Folds run across the gap",
            "Rolled tubes are strong",
            "U-shaped edges stiffen",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Layering and Corrugating
        self.next_band(2)
        self.write_rows(2, "Layering and Corrugating", [
            "Layers glued together",
            "Corrugated: wavy middle",
            "Light and stiff",
            "Same paper, new shape",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Only strong materials work''",
            "``Folds the wrong way''",
            "``Different gaps and coins''",
            "``A box is just thick paper''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Floppy Paper
        self.next_band(4)
        self.write_rows(4, "Floppy Paper", [
            "Floppy paper",
            "Flat sheets sag",
            "Change the shape",
            "No new material",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Fold It, Roll It
        self.next_band(5)
        self.write_rows(5, "Fold It, Roll It", [
            "Fold it",
            "Roll it",
            "Zigzag is stiff",
            "Tubes are strong",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Stack It, Wave It
        self.next_band(6)
        self.write_rows(6, "Stack It, Wave It", [
            "Stack it",
            "Wave it",
            "Layers are stiff",
            "Corrugated is light",
        ], scale=0.9, box=3)

        last = Tex("Folding, rolling, layering and corrugating turn floppy paper into strong shapes.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
