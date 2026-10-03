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


class HealthEducationAndPoliticalStabilitySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Health and Welfare
        title = Tex('Health and welfare').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('Malaria: over 600 000 deaths in 2022').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('South Africa: about 7,8 million with HIV').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('Water, food, vaccines, housing').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('Grants and school meals protect families').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Education and the Quality of Learning
        self.next_band(1)
        b1_title = Tex('Education').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('Each extra year: about 10 per cent more earnings').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('Educating girls benefits whole families').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('PIRLS 2021: 81 per cent cannot read for meaning').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('Skills must match the economy').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Political Stability, Conflict and Governance
        self.next_band(2)
        b2_title = Tex('Stability and governance').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('Conflict trap: war deepens poverty').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('Corruption: the Zondo Commission').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('Botswana: diamonds and democracy').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('Rwanda: growth after 1994').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Cycles of Poverty and Development, and the Error Museum
        self.next_band(3)
        b3_title = Tex('Cycles of poverty').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('Sick, hungry children learn less').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('Less learning, lower income').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('Grants, reading, clinics, jobs').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('Break the cycle at many points').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Cycles of Poverty and Development, and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Health does not affect the economy''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``More years in school is always enough''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Minerals always bring development''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Social grants make people lazy''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): A Worker With a Fever
        self.next_band(5)
        b5_title = Tex('A worker with a fever').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('One bite, two weeks of fever').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('A lost harvest and lost schooling').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('HIV treatment saves lives').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('School meals for nine million learners').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): A Ladder of Learning
        self.next_band(6)
        b6_title = Tex('A ladder of learning').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Each year of school is a step').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Girls' education helps families").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('Strong steps: learning to read').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('Toilets and pads keep girls in school').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): A Calm House
        self.next_band(7)
        b7_title = Tex('A calm house').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('War destroys schools and clinics').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('Corruption steals public money').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('Botswana: diamonds used wisely').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('Health, learning and peace together').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
