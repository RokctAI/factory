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

# Band-layout whiteboard scene for kinds-of-living-things-and-the-seven-life-processes (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/140/160/110/110/110 of 820 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class KindsOfLivingThingsAndTheSevenLifeProcessesSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Many Kinds of Living Things
        self.write_rows(0, "Many Kinds of Living Things", [
            "Plants, animals and fungi",
            "Big and small, everywhere",
            "People are animals too",
            "Mushrooms are fungi",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): The Seven Life Processes
        self.next_band(1)
        self.write_rows(1, "The Seven Life Processes", [
            "Feed, grow, reproduce, breathe",
            "Excrete, sense, move",
            "Excrete: get rid of waste",
            "Sense: notice the world",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Plants Do All Seven Too
        self.next_band(2)
        self.write_rows(2, "Plants Do All Seven Too", [
            "Plants make their own food",
            "Plants do all seven",
            "Leaves breathe and excrete",
            "Leaves turn to the light",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``A plant cannot move''",
            "``Plants do not feed''",
            "``Only animals breathe''",
            "``A car is alive because it moves''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): So Many Living Things
        self.next_band(4)
        self.write_rows(4, "So Many Living Things", [
            "So many living things",
            "Plants and animals",
            "People are animals",
            "Mushrooms are fungi",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Seven Things Living Things Do
        self.next_band(5)
        self.write_rows(5, "Seven Things Living Things Do", [
            "Seven on your fingers",
            "Feed, grow, reproduce",
            "Breathe, excrete",
            "Sense, move",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Plants Are Alive Too
        self.next_band(6)
        self.write_rows(6, "Plants Are Alive Too", [
            "Plants are alive too",
            "Food made in leaves",
            "All seven, slowly",
            "Turns to the light",
        ], scale=0.9, box=2)

        last = Tex("Every living thing feeds, grows, reproduces, breathes, excretes, senses and moves.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
