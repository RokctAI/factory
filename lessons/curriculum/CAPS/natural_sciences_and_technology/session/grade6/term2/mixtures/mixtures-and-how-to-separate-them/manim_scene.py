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

# Band-layout whiteboard scene for mixtures-and-how-to-separate-them (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (210/120/150/110/110/110 of 810 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MixturesAndHowToSeparateThemSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What a Mixture Is
        self.write_rows(0, "What a Mixture Is", [
            "Mixture: two or more substances",
            "Not joined together",
            "Each keeps its properties",
            "Soil, sea water, umngqusho",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Sorting and Sieving
        self.next_band(1)
        self.write_rows(1, "Sorting and Sieving", [
            "Separate using a difference",
            "Hand sorting: big pieces",
            "Sieving: by size",
            "Small falls through the mesh",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Filtering, Settling and Decanting
        self.next_band(2)
        self.write_rows(2, "Filtering, Settling and Decanting", [
            "Settling: heavy bits sink",
            "Decanting: pour off the liquid",
            "Filtering: catch fine bits",
            "Often use more than one",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``A mixture makes a new substance''",
            "``A sieve can separate mud from water''",
            "``Decanting means pouring out everything''",
            "``Filtered water is always safe''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Things Mixed Together
        self.next_band(4)
        self.write_rows(4, "Things Mixed Together", [
            "Things mixed together",
            "Two or more",
            "Not joined",
            "Can be separated",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Pick It and Sieve It
        self.next_band(5)
        self.write_rows(5, "Pick It and Sieve It", [
            "Pick it and sieve it",
            "Fingers",
            "Sieve",
            "Big and small",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Let It Sink and Pour
        self.next_band(6)
        self.write_rows(6, "Let It Sink and Pour", [
            "Let it sink and pour",
            "Settle",
            "Decant",
            "Filter",
        ], scale=0.9, box=3)

        last = Tex("A mixture can be separated by hand sorting, sieving, settling, decanting and filtering.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
