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


class CirculatorySystemSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Blood and Its Components
        title = Tex("Blood and its components").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("Plasma (about 55 percent): transports dissolved substances").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Red cells: haemoglobin carries oxygen; no nucleus; about 120 days").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("White cells: defence. Platelets: clotting.").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Functions: transport, defence, clotting, temperature").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): The Heart and the Double Circulation
        self.next_band(1)
        b1_title = Tex("The heart and double circulation").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Atria receive; ventricles pump; valves one way").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Right side to lungs (pulmonary); left side to body (systemic)").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("vena cava, RA, RV, pulmonary artery, lungs, pulmonary vein, LA, LV, aorta").scale(0.75).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Left ventricle wall about 3 times thicker").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Arteries, Veins and Capillaries
        self.next_band(2)
        b2_title = Tex("Arteries, veins, capillaries").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Arteries: thick elastic walls, high pressure, away from heart").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Capillaries: one cell thick, exchange with cells").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Veins: thin walls, valves, towards heart").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Exceptions: pulmonary artery deoxygenated, pulmonary vein oxygenated").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Health of the Circulatory System and the Error Museum
        self.next_band(3)
        b3_title = Tex("Health of the system").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Blood pressure about 120 over 80; hypertension 140 over 90 or more").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Heart attack: blocked coronary artery. Stroke: blocked brain artery.").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Anaemia: too little iron, less haemoglobin").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Exercise, less salt and fat, no smoking").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Health of the Circulatory System and the Error Museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``All arteries carry oxygenated blood''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Deoxygenated blood is blue''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``The heart makes blood''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``120 over 80 is a heart rate''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): The Delivery Fleet
        self.next_band(5)
        b5_title = Tex("The delivery fleet").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Plasma = the road and the open bakkie").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Red taxis = red cells with oxygen; dark red when empty, never blue").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Security = white cells; puncture kit = platelets").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Five litres; donate 450 millilitres").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): A Two-Pump Engine
        self.next_band(6)
        b6_title = Tex("A two-pump engine").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("A fist, about 70 times a minute, 100 000 times a day").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Right pump: used blood next door to the lungs").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Left pump: fresh blood down the aorta to the toes, thicker wall").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Through the heart twice per lap: double circulation").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Highways, Back Roads and Footpaths
        self.next_band(7)
        b7_title = Tex("Highways, footpaths, back roads").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Highways = arteries: thick, stretchy, the pulse").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Footpaths = capillaries: one cell thick, exchange").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Back roads = veins: thin, valves, walking pumps them").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("120 over 80 are pressures, not beats").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l2, color=YELLOW)))
        self.wait(4)
