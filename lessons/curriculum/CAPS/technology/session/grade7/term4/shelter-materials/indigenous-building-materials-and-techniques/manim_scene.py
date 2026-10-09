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

# Band-layout whiteboard scene for indigenous-building-materials-and-techniques (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (240/250/250/100/100/100 of 1040 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class IndigenousBuildingMaterialsSession(MovingCameraScene):
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
        self.wait(60)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Houses built from the landscape
        self.write_rows(0, "Houses built from the landscape", [
            "Beehive: lashed sapling dome, thatch",
            "Rondavel: wattle and daga, thatched cone",
            "Matjieshuis: rush mats, moved in a day",
            "Grass, sticks, mud, dung, stone, rushes",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Why the materials work
        self.next_band(1)
        self.write_rows(1, "Why the materials work", [
            "Readily available: walking distance",
            "Appropriate: trapped air, thermal walls",
            "Environmentally friendly: it grows back",
            "Honest: thatch burns, building is slow",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): What to borrow
        self.next_band(2)
        self.write_rows(2, "What to borrow", [
            "Bent-rod dome, hoops, lashings",
            "Overlaps, eaves, tie-down, mats",
            "Mound floor; courtyard layout",
            "Let the people build it",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Indigenous housing is primitive''",
            "``Thatch has no downsides''",
            "``Thatch the emergency shelter''",
            "``Cone tent with no overhang or tie-down''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Built from what is there
        self.next_band(4)
        self.write_rows(4, "Built from what is there", [
            "Dome, thatch, grass net, low door",
            "Mud walls, cone roof, overhang",
            "Mats that breathe and swell",
            "A few kilometres away",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Why they work
        self.next_band(5)
        self.write_rows(5, "Why they work", [
            "Three words as principles",
            "Thatch insulates; mud stores heat",
            "Burns; insects; yearly recoat",
            "Only the matjieshuis is quick",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): What to borrow
        self.next_band(6)
        self.write_rows(6, "What to borrow", [
            "Same shape as a hoop tent",
            "Rain steps off bottom up",
            "Reed mats made locally",
            "Not the thatch",
        ], scale=0.9, box=3)

        last = Tex("Indigenous houses use readily available, appropriate, environmentally friendly materials with sound engineering; borrow the dome, overlaps, eaves, tie-downs, floor, layout and builders, not the thatch.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
