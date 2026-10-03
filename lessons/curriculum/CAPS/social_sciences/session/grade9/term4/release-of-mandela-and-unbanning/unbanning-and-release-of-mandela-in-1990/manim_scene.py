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


class UnbanningAndReleaseOfMandelaIn1990Session(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Why De Klerk Unbanned the Liberation Movements
        title = Tex('Why De Klerk acted').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('A country hard to govern').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('A weakened economy').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('The Cold War ends').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('Secret talks build trust').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): The Speech of 2 February 1990
        self.next_band(1)
        b1_title = Tex('2 February 1990').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('ANC, PAC and SACP unbanned').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('Political prisoners to be freed').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('Mandela to be released').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('The time for talking has arrived').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): The Release of Nelson Mandela on 11 February 1990
        self.next_band(2)
        b2_title = Tex('11 February 1990').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('Twenty-seven years in prison').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Out of Victor Verster's gate").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('A humble servant of the people').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('Celebration and caution').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Prisoners, Exiles and the First Agreements, and the Error Museum
        self.next_band(3)
        b3_title = Tex('Coming home').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('Sisulu and others freed').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('Exiles return, Tambo in 1990').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('Armed struggle suspended').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('Apartheid laws repealed in 1991').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Prisoners, Exiles and the First Agreements, and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Apartheid ended in February 1990''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``There were no talks before release''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Only the ANC was unbanned''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Everyone welcomed the unbanning''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): A Speech That Surprised Everyone
        self.next_band(5)
        b5_title = Tex('A surprising speech').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('A country stuck in crisis').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('A new president').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('Bans lifted').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('Mandela will be freed').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): A Walk Through a Prison Gate
        self.next_band(6)
        b6_title = Tex('Through the prison gate').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Robben Island, Pollsmoor, Paarl').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('Hand in hand with Winnie').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('A fist raised high').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('The world watches').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): A Long Road Home
        self.next_band(7)
        b7_title = Tex('A long road home').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('Leaders freed').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('Exiles return').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('Talks begin').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('No vote yet').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
