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


class NurembergLawsAndPersecutionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): From Boycott to Exclusion, 1933 to 1935
        title = Tex('From boycott to exclusion').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('1933: about 525 000 Jews, under 1 percent of Germany').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('1 April 1933: boycott of Jewish shops').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('7 April 1933: Jewish civil servants dismissed').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('Small, legal-looking steps; constant propaganda').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): The Nuremberg Laws of 1935
        self.next_band(1)
        b1_title = Tex('The Nuremberg Laws, 15 September 1935').scale(1.0).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('Citizenship Law: Jews become subjects, not citizens').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('Blood and Honour Law: mixed marriages banned').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('Jewish if three or four Jewish grandparents').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('A race law that checked religious records').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Kristallnacht and the Refugee Crisis
        self.next_band(2)
        b2_title = Tex('Kristallnacht and refugees').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('1938: Aryanisation; passports stamped J').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('9 to 10 November 1938: Kristallnacht').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('About 30 000 Jewish men sent to camps').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Evian 1938 and South Africa's Aliens Act of 1937").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Persecution of Other Groups and the Error Museum
        self.next_band(3)
        b3_title = Tex('Other groups persecuted').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('Roma and Sinti: racial persecution, then genocide').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('Disabled people: 400 000 sterilised; T4 murders').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Gay men, Black Germans, Jehovah's Witnesses").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('Political opponents: the first camp prisoners').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Persecution of Other Groups and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Jews were a large part of Germany''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``The race laws were scientific''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Persecution began with the war''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Only Jews were persecuted''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): A Staircase of Small Steps
        self.next_band(5)
        b5_title = Tex('A staircase of small steps').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('Less than one person in a hundred was Jewish').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('A lie repeated every day').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('Boycott, sackings, bans, burned books').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('Many neighbours looked away').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): A Law That Decided Who Belonged
        self.next_band(6)
        b6_title = Tex('A law that decided who belonged').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('No longer citizens; no vote').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('No marriage between Jews and other Germans').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Decided by grandparents' religion: the lie exposed").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('Kristallnacht, 1938: the Night of Broken Glass').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): The Coloured Triangles
        self.next_band(7)
        b7_title = Tex('The coloured triangles').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Red: political prisoners. Purple: Jehovah's Witnesses.").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('Pink: gay men. Yellow: Jewish prisoners.').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('Roma and Sinti, disabled people, Black Germans').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('Niemoller: when they came for me, no one was left').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
