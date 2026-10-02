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


class NonMetalsOxygenSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The General Reaction: Non-Metal + Oxygen → Non-Metal Oxide
        title = Tex("The general reaction").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("non-metal + oxygen gives non-metal oxide").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Products are usually gases").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Deflagrating spoon into a jar of oxygen").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = MathTex(r"\mathrm{2H_2 + O_2 \rightarrow 2H_2O}").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Carbon Reacting with Oxygen
        self.next_band(1)
        b1_title = Tex("Carbon").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Glows brightly; seems to vanish").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = MathTex(r"\mathrm{C + O_2 \rightarrow CO_2}").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Limewater turns milky").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Too little air: 2C + O2 gives 2CO, poisonous").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Sulfur Reacting with Oxygen
        self.next_band(2)
        b2_title = Tex("Sulfur").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Melts, then burns with a blue flame").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = MathTex(r"\mathrm{S + O_2 \rightarrow SO_2}").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Choking gas: use a fume cupboard").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Coal with sulfur releases SO2").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Non-Metal Oxides Are Acidic and the Error Museum
        self.next_band(3)
        b3_title = Tex("Acidic oxides").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\mathrm{CO_2 + H_2O \rightarrow H_2CO_3}").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = MathTex(r"\mathrm{SO_2 + H_2O \rightarrow H_2SO_3}").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Metal oxides: bases. Non-metal oxides: acids").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Acid rain").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Non-Metal Oxides Are Acidic and the Error Museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Charcoal atoms are destroyed''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Non-metal oxides are bases''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``No smell means safe''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Sulfur dioxide is SO''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): The Vanishing Charcoal
        self.next_band(5)
        b5_title = Tex("The vanishing charcoal").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Product is a gas that floats away").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Limewater turns milky").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Too little air: carbon monoxide").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Never burn a brazier in a closed room").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): The Blue Flame
        self.next_band(6)
        b6_title = Tex("The blue flame").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Yellow powder melts, then burns blue").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Smells like a struck match").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Fume cupboard, tiny amount").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Keeps dried apricots orange").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): The Acid Pattern
        self.next_band(7)
        b7_title = Tex("The acid pattern").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Charcoal jar: yellow to orange").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Sulfur jar: orange to red").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Magnesium jar: blue").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Non-metal oxides make acids").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
