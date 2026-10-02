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


class TheFallOfTheSovietUnionIn1991Session(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): A Union of Fifteen Republics
        title = Tex('A union of fifteen republics').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('Russia the largest of fifteen').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('Nearly 290 million, over 100 nationalities').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('Power held in Moscow by the Party').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('Baltic states taken by force in 1940').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Crisis From 1989 to 1991
        self.next_band(1)
        b1_title = Tex('Crisis, 1989-1991').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('Baltic Way: two million hold hands').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('Lithuania declares independence, 1990').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('Shortages, inflation, rationing').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('Yeltsin elected President of Russia').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): The August Coup of 1991
        self.next_band(2)
        b2_title = Tex('The August coup').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('19 August 1991: Gorbachev held in Crimea').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('Tanks in Moscow').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('Yeltsin on a tank at the White House').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('Three days, then collapse').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): The Union Ends, Consequences and the Error Museum
        self.next_band(3)
        b3_title = Tex('The Union ends').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('1 December: Ukraine votes to leave').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('8 December: CIS formed').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('25 December 1991: the flag comes down').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('USA the only superpower').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): The Union Ends, Consequences and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``The Soviet Union was just Russia''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Reformers led the coup''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``The USA defeated it in war''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``The Berlin Wall fell in 1991''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): A House Held Together With Straps
        self.next_band(5)
        b5_title = Tex('A house held together with straps').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('Fifteen rooms, fifteen families').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('Straps: Party, army, secret police').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('Gorbachev loosens the straps').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('A chain of two million hands').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): A Man on a Tank
        self.next_band(6)
        b6_title = Tex('A man on a tank').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Gorbachev locked in his holiday house').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('Tanks in Moscow').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Yeltsin: ``Resist!''").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('The plot backfires').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): A Flag Comes Down on Christmas Night
        self.next_band(7)
        b7_title = Tex('A flag comes down on Christmas night').scale(1.0).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('The families move out').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('Ukraine votes to leave').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('25 December 1991: the flag comes down').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('Fifteen new countries').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l3, color=YELLOW)))
        self.wait(4)
