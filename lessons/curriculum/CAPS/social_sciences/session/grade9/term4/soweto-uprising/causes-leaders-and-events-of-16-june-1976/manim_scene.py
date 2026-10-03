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


class CausesLeadersAndEventsOf16June1976Session(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Long-Term Causes: Bantu Education and Life Under Apartheid
        title = Tex('Long-term causes').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('Bantu Education since 1953').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('Overcrowded, underfunded schools').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('Hard life in Soweto').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('Rising prices and unemployment').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): The Immediate Cause: The Afrikaans Medium Decree
        self.next_band(1)
        b1_title = Tex('The Afrikaans decree').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('1974: half the subjects in Afrikaans').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('Teachers and pupils struggled').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('Seen as the language of the oppressor').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('Boycotts begin in early 1976').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Black Consciousness and the Student Leaders
        self.next_band(2)
        b2_title = Tex('Black Consciousness and leaders').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('Steve Biko and SASO').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('Pride and self-reliance').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('SASM action committee, 13 June').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('Tsietsi Mashinini leads').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): The Events of 16 June 1976, and the Error Museum
        self.next_band(3)
        b3_title = Tex('16 June 1976').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('Thousands march peacefully').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('Police open fire').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('Hector Pieterson killed').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('Protest becomes an uprising').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): The Events of 16 June 1976, and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``The march was planned as a riot''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``It was only about Afrikaans''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``The ANC planned it from exile''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Hector was the only victim''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): A Crowded Classroom
        self.next_band(5)
        b5_title = Tex('A crowded classroom').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('Sixty pupils, few books').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('Maths in a third language').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('An order that felt like an insult').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('Anger grows').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): A Homemade Placard
        self.next_band(6)
        b6_title = Tex('A homemade placard').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Proud and confident students').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('A secret plan').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("``Down with Afrikaans!''").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('A peaceful march').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): A Famous Photograph
        self.next_band(7)
        b7_title = Tex('A famous photograph').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('Police fire on children').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('Hector Pieterson dies').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('The world sees the picture').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('16 June is Youth Day').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
