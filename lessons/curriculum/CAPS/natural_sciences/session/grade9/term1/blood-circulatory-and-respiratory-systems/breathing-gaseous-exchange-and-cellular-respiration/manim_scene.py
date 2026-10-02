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


class GasExchangeRespirationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Breathing, Gas Exchange and Respiration Are Three Things
        title = Tex("Three processes, not one").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("Breathing: mechanical, air in and out, the chest").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Gaseous exchange: diffusion across alveoli and in the tissues").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Cellular respiration: chemical, mitochondria of every cell").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Blood carries the gases between lungs and cells").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Gaseous Exchange in the Alveoli
        self.next_band(1)
        b1_title = Tex("Gaseous exchange in the alveoli").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Oxygen: alveolus (high) to blood (low). Carbon dioxide: the reverse.").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("About 300 million alveoli, about 70 square metres: large surface area").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("One cell thick: short distance. Moist: gases dissolve.").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Dense moving capillaries and breathing keep the gradient steep").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Transport by the Blood
        self.next_band(2)
        b2_title = Tex("Transport by the blood").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Lungs: haemoglobin + oxygen gives oxyhaemoglobin, bright red").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Tissues: oxyhaemoglobin releases oxygen where it is scarce").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Carbon dioxide mostly dissolved in plasma, back to the lungs").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Carbon monoxide blocks the haemoglobin seats").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Cellular Respiration and the Error Museum
        self.next_band(3)
        b3_title = Tex("Cellular respiration").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("glucose + oxygen gives carbon dioxide + water + energy").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = MathTex(r"\mathrm{C_6H_{12}O_6 + 6O_2 \rightarrow 6CO_2 + 6H_2O + energy}").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Energy RELEASED into a carrier (ATP); some lost as heat").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Without enough oxygen: glucose to lactic acid, much less energy").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Cellular Respiration and the Error Museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Respiration is breathing''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Respiration happens in the lungs''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Respiration makes energy''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Oxygen is pumped into the blood''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Fetching, Swapping, Burning
        self.next_band(5)
        b5_title = Tex("Fetching, swapping, burning").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Fetching = breathing, in the chest").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Swapping = diffusion, in the lungs AND the tissues").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Burning = respiration, in every cell's mitochondria").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Fetch, swap, carry, swap, burn").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): The Wet Grape in a Net
        self.next_band(6)
        b6_title = Tex("The wet grape in a net").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Many grapes: half a tennis court, so more gas at once").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Skin one cell thick, so a short crossing").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Wet inside, so gases dissolve").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Moving blood in the net keeps the difference big").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): From Lungs to Leg Muscle and Back
        self.next_band(7)
        b7_title = Tex("Lungs to leg muscle and back").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Breath, alveolus, haemoglobin, heart, aorta, thigh capillary, cell").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Mitochondria: glucose + oxygen gives carbon dioxide + water + energy").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Sprint: breathing 15 to 40, heart 70 to 150; lactic acid burns").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Panting after: the oxygen debt is repaid in the liver").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l3, color=YELLOW)))
        self.wait(4)
