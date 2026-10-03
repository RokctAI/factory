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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex keep the export to the
# allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (220/230/230/230/190/190/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SustainableDevelopmentSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): What Sustainable Development Means
        title = Tex('What sustainable development means').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('Brundtland Report, 1987').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('Needs of today, needs of tomorrow').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('Live on the interest, not the savings').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('Humanity uses about 1,7 Earths').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Balancing Economic, Social and Environmental Factors
        self.next_band(1)
        b1_title = Tex('Balancing three dimensions').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('Economic, social, environmental').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('Trade-offs: jobs versus pollution').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('Win-wins: solar heaters, wetlands').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('Section 24: environmental rights').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Global Agreements and the Sustainable Development Goals
        self.next_band(2)
        b2_title = Tex('Global agreements').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('Rio Earth Summit, 1992').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('17 Sustainable Development Goals, 2015').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('Targets for 2030, for all countries').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('Paris Agreement: well below 2 degrees').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Sustainable Development in South Africa and the Error Museum
        self.next_band(3)
        b3_title = Tex('South Africa').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('About 80 per cent of electricity from coal').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('Just transition from coal to sun and wind').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('Day Zero: 50 litres per person per day').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('Family of four: 6 000 litres a month').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Sustainable Development in South Africa and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``It means stopping development''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``It is only about the environment''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``The SDGs are only for poor countries''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Individual actions change nothing''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): A Savings Account for the Future
        self.next_band(5)
        b5_title = Tex('A savings account').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('Spend the interest, keep the savings').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('Forests and fish can regrow').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('Needs today and tomorrow').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('We only have one Earth').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): A Three-Strand Rope
        self.next_band(6)
        b6_title = Tex('A three-strand rope').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Economy, society, environment').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('Strands can pull against each other').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('Some actions strengthen all three').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('17 goals for every country').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): The City That Nearly Ran Dry
        self.next_band(7)
        b7_title = Tex('The city that nearly ran dry').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('Cape Town, 2018: Day Zero').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('50 litres a day each').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('Water use cut roughly in half').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('Sun and wind replace coal').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
