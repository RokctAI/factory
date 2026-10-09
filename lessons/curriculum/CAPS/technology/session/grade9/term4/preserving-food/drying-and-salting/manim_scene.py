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

# Band-layout whiteboard scene for drying-and-salting (Part 1 Expert
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


class DryingAndSaltingSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Drying: Removing the Water That Spoilers Need
        self.write_rows(0, "Drying: Removing the Water That Spoilers Need", [
            "Organisms need water; dry below ~15\\% and they stop",
            "Biltong, bokkoms, dried maize, fruit; dehydrators",
            "Fast not hot: thin, moving air, mesh, dry climate",
            "Light, keeps sealed; texture changes; re-moulds if damp",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Salting: Drawing Water Out and Making Food Inhospitable
        self.next_band(1)
        self.write_rows(1, "Salting: Drawing Water Out and Making Food Inhospitable", [
            "Salt draws water out by osmosis; organisms shrivel",
            "Remaining salt: too salty to grow",
            "Salted snoek, corned beef, bacon, salt cod",
            "Limits: soak first, health, some survive; sugar works too",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): The Practical Investigation: Drying and Salting Compared
        self.next_band(2)
        self.write_rows(2, "The Practical Investigation: Drying and Salting Compared", [
            "Six equal slices, weighed; control, salted, drying",
            "Same room; daily mass and appearance; no tasting",
            "Control moulds day 3-5; salted firm in brine; dried leathery, half mass",
            "Graph mass vs day; both treatments prevent mould",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Slices of different thickness''",
            "``Trays kept in different places''",
            "``Samples tasted''",
            "``No untreated control''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): No Water, No Spoiling
        self.next_band(4)
        self.write_rows(4, "No Water, No Spoiling", [
            "No water, no spoiling",
            "Karoo wind, West Coast racks",
            "Thin slices, mesh on top",
            "Keep it dry after",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Salt Pulls the Water Out
        self.next_band(5)
        self.write_rows(5, "Salt Pulls the Water Out", [
            "Salt pulls the water out",
            "Too salty to live in",
            "Soak before cooking",
            "Jam is the sweet version",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Weigh It, Treat It, Wait, Weigh Again
        self.next_band(6)
        self.write_rows(6, "Weigh It, Treat It, Wait, Weigh Again", [
            "Weigh, treat, wait, weigh",
            "Same place, same time",
            "Plain plate moulds",
            "The control is the proof",
        ], scale=0.9, box=3)

        last = Tex("Drying removes the water organisms need and salting draws it out by osmosis; a fair test with a control shows both prevent the mould seen on untreated food.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
