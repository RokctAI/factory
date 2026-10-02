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
# removed. Write-only reveals on single-string Tex/MathTex keep the export to
# the allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (220/230/230/230/190/190/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RespiratorySystemSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Components of the Respiratory System
        title = Tex("Components of the respiratory system").scale(1.0).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("Nose: filters, warms, moistens").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Trachea: cartilage rings, cilia and mucus").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Bronchi, bronchioles, about 300 million alveoli (about 70 square metres)").scale(0.75).shift(DOWN * 0.60)
        b0_l4 = Tex("nasal cavity, pharynx, larynx, trachea, bronchi, bronchioles, alveoli").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): The Mechanism of Breathing
        self.next_band(1)
        b1_title = Tex("The mechanism of breathing").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("IN: diaphragm contracts and flattens; ribs up and out").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("volume increases, pressure decreases, air flows in").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("OUT: diaphragm relaxes and domes; ribs fall; lungs recoil").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("volume decreases, pressure increases, air flows out").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Inhaled and Exhaled Air
        self.next_band(2)
        b2_title = Tex("Inhaled and exhaled air").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Oxygen: 21 percent in, about 16 percent out").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Carbon dioxide: 0,04 percent in, about 4 percent out").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Nitrogen about 78 percent, unchanged; out is warm and wet").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Lime water turns milky with carbon dioxide").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Health of the Respiratory System and the Error Museum
        self.next_band(3)
        b3_title = Tex("Health of the respiratory system").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Asthma: bronchioles narrow; inhaler relaxes them").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("TB: bacterium spread by coughing; six months of antibiotics").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Pneumonia: alveoli fill with fluid").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Smoking: tar paralyses cilia; emphysema; cancer; carbon monoxide").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Health of the Respiratory System and the Error Museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Breathing is respiration''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``The lungs pump themselves''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Exhaled air has no oxygen''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``We breathe in oxygen and out carbon dioxide''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): An Upside-Down Tree
        self.next_band(5)
        b5_title = Tex("An upside-down tree").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Trunk = trachea with cartilage rings").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Branches = bronchi; twigs = bronchioles").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Grapes = alveoli, wrapped in capillaries").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Waving hairs sweep the dirt up; smoke paralyses them").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): The Balloon in the Bottle
        self.next_band(6)
        b6_title = Tex("The balloon in the bottle").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Bottle = chest; rubber sheet = diaphragm; balloon = lung").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Pull the sheet down: bigger space, lower pressure, air pushes in").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Nobody sucks: the outside air pushes itself in").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Muscles, volume, pressure, air: always that order").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): The Window on a Cold Morning
        self.next_band(7)
        b7_title = Tex("The window on a cold morning").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Out: warm, wet, oxygen 16 percent, carbon dioxide 4 percent").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("You use about a quarter of the oxygen you breathe").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Asthma tightens twigs; pneumonia floods grapes; TB eats the tree").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Smoking: cough, emphysema, cancer, stolen oxygen seats").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l1, color=YELLOW)))
        self.wait(4)
