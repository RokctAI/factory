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


class TheHolocaustAndTheFinalSolutionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): From Persecution to Genocide: Ghettos and Mass Shootings
        title = Tex('From persecution to genocide').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("Holocaust, or Shoah: the genocide of Europe's Jews").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('Ghettos: Warsaw, 400 000 people in about 3,4 square km').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('From 1941: Einsatzgruppen mass shootings').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('Babi Yar, September 1941: 33 771 murdered').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): The Final Solution and the Wannsee Conference
        self.next_band(1)
        b1_title = Tex('The Final Solution').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('20 January 1942: the Wannsee Conference').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('Coordinating murder across the whole state').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('Minutes list about 11 million Jews').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('Disguised words: evacuation meant murder').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): The Extermination Camps
        self.next_band(2)
        b2_title = Tex('The extermination camps').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('Six death camps, all in occupied Poland').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('Deportation in sealed goods wagons').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('Auschwitz: about 1,1 million murdered').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('Roma and Sinti, Soviet prisoners, Poles also murdered').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Responsibility, Rescue, Remembrance and the Error Museum
        self.next_band(3)
        b3_title = Tex('Responsibility and remembrance').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('About 6 million Jews murdered, 1,5 million children').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('Perpetrators, collaborators, bystanders, rescuers').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('Liberation of Auschwitz: 27 January 1945').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('Nuremberg: crimes against humanity').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Responsibility, Rescue, Remembrance and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``It happened mainly inside Germany''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Wannsee decided to begin the killing''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``All camps were extermination camps''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Only a few leaders were responsible''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Walls Around a Neighbourhood
        self.next_band(5)
        b5_title = Tex('Walls around a neighbourhood').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('Ghettos: families locked behind walls').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('Hunger and disease; the yellow star').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('Killing squads in the Soviet Union').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('Genocide: destroying a whole group').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): A Meeting at a House Beside a Lake
        self.next_band(6)
        b6_title = Tex('A meeting beside a lake').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Wannsee, 20 January 1942: the Final Solution').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('Trains to death camps in Poland').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('About 6 million Jewish people murdered').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('Many people did their jobs and asked no questions').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Anne's Diary and Why We Remember
        self.next_band(7)
        b7_title = Tex("Anne's diary and why we remember").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('Anne Frank: hidden two years; died aged 15').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('Rescuers: Sendler, Schindler, the Danish boats').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('27 January 1945: Auschwitz liberated').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('Words, laws, walls, murder: remember the steps').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
