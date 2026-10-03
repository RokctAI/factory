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


class WeatheringErosionAndDepositionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Three Processes, One Chain
        title = Tex('Three processes, one chain').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('Weathering breaks (in place)').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('Erosion takes (removes and carries)').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('Deposition drops (energy runs out)').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('Weathering makes erosion easier').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): The Agents of Erosion
        self.next_band(1)
        b1_title = Tex('Agents of erosion').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('Running water: rills, dongas, rivers').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('Wind: deflation and abrasion').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('Ice and waves').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('Gravity: rockfalls, landslides, creep').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Transport and Deposition
        self.next_band(2)
        b2_title = Tex('Transport and deposition').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('Traction, saltation, suspension, solution').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('More energy: more erosion').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('Less energy: deposition').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('Biggest material dropped first').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): From Mountain to Sea and the Error Museum
        self.next_band(3)
        b3_title = Tex('From mountain to sea').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('Kimberlite weathered and eroded').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('Orange River carries diamonds').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('Waves drop them on west coast beaches').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('Siltation fills dams').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): From Mountain to Sea and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Erosion breaks rock in place''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Rivers deposit when they speed up''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Wind is the main agent everywhere''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Mass movement needs a river''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): The Crumbling Biscuit
        self.next_band(5)
        b5_title = Tex('The crumbling biscuit').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('Crumbs on the windowsill').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('A broom sweeps them away').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('A pile in the corner').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('Breaks, takes, drops').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): The Broom
        self.next_band(6)
        b6_title = Tex('The broom').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Water: the biggest broom').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('Wind in dry places').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('Ice and waves').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('Gravity on its own').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): The Pile in the Corner
        self.next_band(7)
        b7_title = Tex('The pile in the corner').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('Out of energy, drop the load').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('Heavy stones first, mud last').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('Wind piles up dunes').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('Diamonds on the beach').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l1, color=YELLOW)))
        self.wait(4)
