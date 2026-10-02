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

# Band-layout whiteboard scene for respiration-releases-energy-from-food
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex/MathTex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to subtopics.json
# (220/220/240/230/190/190/180 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RespirationEnergySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the word equation
        title = Tex("Respiration: the word equation").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"\text{glucose} + \text{oxygen} \rightarrow \text{carbon dioxide} + \text{water} + \text{ENERGY}").scale(0.9).shift(UP * 1.2)
        l2 = Tex("Every living cell, every organism, day AND night").scale(0.95).shift(UP * 0.2)
        l3 = Tex("Site: the mitochondria").scale(0.95).shift(DOWN * 0.7)
        l4 = Tex("Energy for movement, growth, repair, warmth, transport").scale(0.85).shift(DOWN * 1.7)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): breathing vs respiration
        self.next_band(1)
        b1_title = Tex("Breathing is NOT respiration").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        rows = [
            r"\text{Breathing: physical, lungs, gas exchange}",
            r"\text{Respiration: chemical, in cells, releases energy}",
            r"\text{Air} \rightarrow \text{lungs} \rightarrow \text{blood} \rightarrow \text{cell} \rightarrow \text{mitochondrion}",
            r"\text{Fish, earthworm, tree: respire without lungs}",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.85).shift(band_shift(1) + UP * (1.3 - 0.8 * i))
            self.play(Write(m))
            self.wait(2.2)
        self.wait(1.5)

        # --- Band 2 (subtopic_3): limewater and seeds
        self.next_band(2)
        b2_title = Tex("Evidence for respiration").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Limewater: clear, turns MILKY with carbon dioxide").scale(0.9).shift(band_shift(2) + UP * 1.3)
        b2_l2 = Tex("Exhaled air about 4\\% CO$_2$; room air about 0,04\\%").scale(0.9).shift(band_shift(2) + UP * 0.4)
        b2_l3 = Tex("Germinating seeds, sealed, dark: limewater milky").scale(0.9).shift(band_shift(2) + DOWN * 0.5)
        b2_l4 = Tex("Control: boiled, dead seeds: limewater stays clear").scale(0.9).shift(band_shift(2) + DOWN * 1.5)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.4)
        self.play(Create(SurroundingRectangle(b2_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_3): heat, and the write-up
        self.next_band(3)
        b3_title = Tex("Heat, and the conclusion").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Thermometer in living seeds: a few degrees warmer").scale(0.9).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("Compost heap, crowded room, your own skin: respiration heat").scale(0.85).shift(band_shift(3) + UP * 0.2)
        b3_l3 = Tex("Observation: limewater milky. Conclusion: CO$_2$ made, so cells respire").scale(0.8).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = Tex("Independent: living vs dead. Dependent: limewater / temperature").scale(0.8).shift(band_shift(3) + DOWN * 1.8)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): mirror images + error museum
        self.next_band(4)
        b4_title = Tex("Two equations, mirror images").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{CO}_2 + \text{H}_2\text{O} \xrightarrow{\text{light, chlorophyll}} \text{glucose} + \text{O}_2").scale(0.85).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"\text{glucose} + \text{O}_2 \rightarrow \text{CO}_2 + \text{H}_2\text{O} + \text{energy}").scale(0.85).shift(band_shift(4) + UP * 0.4)
        b4_l3 = Tex("Plant by day: net O$_2$ out. Plant by night: O$_2$ in, CO$_2$ out").scale(0.85).shift(band_shift(4) + DOWN * 0.5)
        b4_l4 = Tex("``Plants do not respire''").scale(0.9).shift(band_shift(4) + DOWN * 1.5)
        for m in (b4_l1, b4_l2, b4_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b4_l4))
        self.play(Create(strike(b4_l4)))
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): burning without flames
        self.next_band(5)
        b5_title = Tex("Burning without flames").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("Braai: fuel + oxygen gives CO$_2$ + water + heat").scale(0.9).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex("Cell: glucose + oxygen gives CO$_2$ + water + energy").scale(0.9).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex("Same reaction, tiny steps, in the mitochondria, at 37 degrees").scale(0.85).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex("You are warm because you are a slow fire").scale(0.9).shift(band_shift(5) + DOWN * 1.5)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): delivery vs fire
        self.next_band(6)
        b6_title = Tex("Breathing is delivery, respiration is the fire").scale(1.1).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Truck: lungs and blood bring O$_2$, remove CO$_2$").scale(0.9).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex("Fire: inside the cell, glucose meets oxygen, energy out").scale(0.9).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("Fish, worm, tree: no lungs, still every cell respires").scale(0.9).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex("Sprint: fires roar, truck works overtime, you breathe hard").scale(0.85).shift(band_shift(6) + DOWN * 1.5)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): day and night in the garden
        self.next_band(7)
        b7_title = Tex("Day and night in the garden").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        rows = [
            r"\text{Kitchen (photosynthesis): light only, green cells only}",
            r"\text{Fire (respiration): always, every cell}",
            r"\text{Day: kitchen wins, O}_2 \text{ out. Night: fire only, CO}_2 \text{ out}",
            r"\text{Seeds in a dark jar turn limewater milky}",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.85).shift(band_shift(7) + UP * (1.3 - 0.75 * i))
            self.play(Write(m))
            self.wait(2.0)
        b7_l5 = Tex("One equation stores the Sun's energy; the other spends it.").scale(0.9).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=YELLOW)))
        self.wait(4)
