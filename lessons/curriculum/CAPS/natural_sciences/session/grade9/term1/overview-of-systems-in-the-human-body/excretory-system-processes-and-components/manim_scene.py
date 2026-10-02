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


class ExcretorySystemSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Excretion and the Excretory Organs
        title = Tex("Excretion and the excretory organs").scale(1.0).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("Excretion: removal of wastes MADE by the body's cells").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Carbon dioxide (respiration) and urea (liver, from excess protein)").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Lungs: carbon dioxide. Skin: water and salt. Kidneys: urea, water, salts.").scale(0.75).shift(DOWN * 0.60)
        b0_l4 = Tex("Egestion of faeces is NOT excretion").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): The Urinary System
        self.next_band(1)
        b1_title = Tex("The urinary system").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Two kidneys, two ureters, bladder, urethra").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Renal artery in; renal vein out; about a million nephrons each").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Bladder stores about 400 to 500 millilitres").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Urine: about 95 percent water, about 2 percent urea, salts; no glucose").scale(0.75).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Filtration and Reabsorption
        self.next_band(2)
        b2_title = Tex("Filtration and reabsorption").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Filtration under pressure: water, glucose, salts, urea pass").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Blood cells and proteins stay: about 180 litres of filtrate a day").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Reabsorbed: all glucose, about 99 percent of water, needed salts").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Left: about 1,5 litres of urine. Hot day: more water kept, darker urine.").scale(0.75).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Health of the Excretory System and the Error Museum
        self.next_band(3)
        b3_title = Tex("Health of the system").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Kidney stones: concentrated urine; drink 1,5 to 2 litres a day").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Infections: bacteria in the urethra and bladder").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Kidney failure: diabetes, high blood pressure").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Dialysis: about 4 hours, 3 times a week; transplant is permanent").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Health of the Excretory System and the Error Museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``The kidneys make urea''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Faeces are excreted''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``The bladder filters the blood''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Urine normally contains glucose''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): The Rubbish Removal Service
        self.next_band(5)
        b5_title = Tex("The rubbish removal service").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Smoke = carbon dioxide; ash = urea").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Rubbish the cells made: excretion. Leftover food: egestion.").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Three exits: lungs, skin, kidneys").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Liver makes the bag; kidney takes it to the dump").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): A Sieve That Takes Things Back
        self.next_band(6)
        b6_title = Tex("A sieve that takes things back").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Sieve: everything small falls through (180 litres a day)").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Big things stay: blood cells, proteins").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Take back: all glucose, 99 drops in 100 of water, needed salt").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Left over: about 1,5 litres of urine. Kidney, ureter, bladder, urethra.").scale(0.75).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Water In, Water Out
        self.next_band(7)
        b7_title = Tex("Water in, water out").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Hot day: more water kept, little dark urine, thirst").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Cool day, lots of drinking: lots of pale urine").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Water prevents stones and flushes infections").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Failed sieves: dialysis or a transplant").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l1, color=YELLOW)))
        self.wait(4)
