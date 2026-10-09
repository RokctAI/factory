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

# Band-layout whiteboard scene for mining-impact-indigenous-iron-and-gender-bias (Part 1 Expert
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


class MiningImpactAndBiasSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Acid Mine Drainage and Dust From Mine Dumps
        self.write_rows(0, "Acid Mine Drainage and Dust From Mine Dumps", [
            "Pyrite + water + air = acid with metals",
            "2002 West Rand decant; lime treatment",
            "Dumps: silica dust into townships",
            "Vegetate, spray, reprocess, relocate",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Indigenous Iron Mining in South Africa Before the Modern Era
        self.next_band(1)
        self.write_rows(1, "Indigenous Iron Mining in South Africa Before the Modern Era", [
            "Third century onward: clay shaft furnaces",
            "Charcoal, ore, bellows, tuyeres, bloom",
            "Mapungubwe, Phalaborwa, Soutpansberg",
            "Technology here before colonists",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Gender Bias in Mining Careers and Writing a Fair Report
        self.next_band(2)
        self.write_rows(2, "Gender Bias in Mining Careers and Writing a Fair Report", [
            "1911 ban; lifted 1996; Charter 2004",
            "15-20 percent today; barriers in kit and facilities",
            "Bias: one user assumed",
            "Question, background, three sources, views, conclusion",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Outrage without evidence''",
            "``One perspective only''",
            "``Indigenous smelting called primitive''",
            "``Gender report stops at the law''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Orange Water and Yellow Dust
        self.next_band(4)
        self.write_rows(4, "Orange Water and Yellow Dust", [
            "Flooded mines turn rivers orange",
            "Public pays for decades",
            "Dust in food and lungs",
            "Costs for people without the profit",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Iron Before the Mines
        self.next_band(5)
        self.write_rows(5, "Iron Before the Mines", [
            "A metre of clay, hot enough to smelt",
            "Hammer the bloom, forge the hoe",
            "Copper, gold, tin too",
            "Same chemistry as a blast furnace",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Who Gets to Go Underground
        self.next_band(6)
        self.write_rows(6, "Who Gets to Go Underground", [
            "Not allowed underground until 1996",
            "Overalls made for men",
            "Design the cage for every body",
            "One page, three sources, fair",
        ], scale=0.9, box=3)

        last = Tex("Know the ground you build on: acid water, dust, a thousand years of iron, and who was kept out; then report it fairly with evidence and act on it in your design.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
