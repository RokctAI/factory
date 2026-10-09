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

# Band-layout whiteboard scene for sequence-of-manufacture-for-a-food-item (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (170/190/230/100/100/100 of 890 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SequenceOfManufactureForAFoodItemSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Cooking as manufacturing
        self.write_rows(0, "Cooking as manufacturing", [
            "Inputs, processes, output",
            "Relish for ten in one pot",
            "Steps with verbs, times, tools",
            "Fourteen steps from hands to wash-up",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Order, hygiene, safety
        self.next_band(1)
        self.write_rows(1, "Order, hygiene, safety", [
            "Chop before the oil is hot",
            "Hygiene boxes: soap, boards, cover",
            "Serve steaming within two hours",
            "Blade away; lid by edge; dry cloth",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Draw, time, rehearse
        self.next_band(2)
        self.write_rows(2, "Draw, time, rehearse", [
            "Diamonds: soft? seasoned? hot?",
            "Pap column starts ten minutes early",
            "Fit the period or shorten",
            "Four roles; walk it through",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Hygiene left off the chart''",
            "``Tins opened half an hour early''",
            "``Sixty minutes in a forty-five period''",
            "``No test before serving''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A kitchen is a factory
        self.next_band(4)
        self.write_rows(4, "A kitchen is a factory", [
            "Meal, tins, onions in",
            "Plates out",
            "Pick one item",
            "Verb for every step",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Order, clean, safe
        self.next_band(5)
        self.write_rows(5, "Order, clean, safe", [
            "Hands first; tins last",
            "Twenty seconds of soap",
            "Separate boards",
            "Two thirds full; handle in",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Draw it, time it, rehearse it
        self.next_band(6)
        self.write_rows(6, "Draw it, time it, rehearse it", [
            "Oval, boxes, diamonds, oval",
            "Relish thirty, pap forty",
            "Pap, relish, hygiene, safety",
            "Move any clash",
        ], scale=0.9, box=1)

        last = Tex("Food preparation is manufacturing: steps with verbs, times and names in dependency order, hygiene and safety as steps, tests of texture, taste and temperature before serving.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
