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

# Band-layout whiteboard scene for seeds-yeast-and-eggs-that-wait-to-live (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/150/150/110/110/110 of 810 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SeedsYeastAndEggsThatWaitToLiveSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Dried Beans Are Waiting to Grow
        self.write_rows(0, "Dried Beans Are Waiting to Grow", [
            "A seed has a baby plant inside",
            "Water and warmth wake it up",
            "Root first, then a shoot",
            "Cooked seeds never grow",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Yeast Wakes Up
        self.next_band(1)
        self.write_rows(1, "Yeast Wakes Up", [
            "Yeast is a living fungus",
            "Warm water and sugar",
            "Feeding makes bubbles",
            "Boiling water kills it",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): A Fertilised Egg Is Alive
        self.next_band(2)
        self.write_rows(2, "A Fertilised Egg Is Alive", [
            "Fertilised egg: a chick inside",
            "Kept warm for about 21 days",
            "Yolk is the food store",
            "Shop eggs: not fertilised",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``A dry bean is dead''",
            "``Yeast is just a powder''",
            "``Any warm egg will hatch''",
            "``Wake yeast with boiling water''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Sleeping Seeds
        self.next_band(4)
        self.write_rows(4, "Sleeping Seeds", [
            "Sleeping seeds",
            "Water and warmth",
            "Root, then shoot",
            "Cooked: never grows",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Bubbly Yeast
        self.next_band(5)
        self.write_rows(5, "Bubbly Yeast", [
            "Bubbly yeast",
            "Warm water and sugar",
            "Bubbles and rising dough",
            "Too hot: dead",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Eggs That Hatch
        self.next_band(6)
        self.write_rows(6, "Eggs That Hatch", [
            "Eggs that hatch",
            "Kept warm, 21 days",
            "Chick hatches",
            "Shop eggs: no chick",
        ], scale=0.9, box=1)

        last = Tex("Some things look dead but are resting; the right water, warmth and food wake them up.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
