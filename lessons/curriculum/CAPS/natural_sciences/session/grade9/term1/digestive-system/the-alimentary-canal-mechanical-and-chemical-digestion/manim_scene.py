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


class AlimentaryCanalDigestionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Mechanical Digestion: Teeth, Tongue and Churning
        title = Tex("Mechanical digestion").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("Smaller pieces, same molecules: more surface area").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Incisors cut, canines tear, premolars and molars grind").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Tongue makes a bolus; stomach churns food into chyme").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Bile emulsifies fat into droplets; no enzymes in bile").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Enzymes and Chemical Digestion
        self.next_band(1)
        b1_title = Tex("Enzymes").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Protein catalyst; not used up").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Specific: substrate fits the active site, lock and key").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Optimum about 37 degrees; cold slows; heat denatures").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Amylase: starch. Protease: protein. Lipase: fat.").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Digestion Along the Canal: Mouth, Stomach and Small Intestine
        self.next_band(2)
        b2_title = Tex("Along the canal").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Mouth, pH about 7: salivary amylase, starch to maltose").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Stomach, pH about 2: hydrochloric acid, pepsin on protein").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Duodenum: bile; pancreatic amylase, trypsin, lipase").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Gut wall: maltase and proteases finish the job").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Investigating Digestion and the Error Museum
        self.next_band(3)
        b3_title = Tex("Investigating amylase").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Independent: temperature. Dependent: time for starch to go.").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Controlled: volumes, concentrations, pH").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Control tube: starch + water, no amylase").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Fastest near 37; none at 80, denatured").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Investigating Digestion and the Error Museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Bile is an enzyme''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Enzymes are killed by cold''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Chewing is chemical digestion''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``The stomach digests starch''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Scissors, Millstones and a Washing Machine
        self.next_band(5)
        b5_title = Tex("Scissors, millstones, washing machine").scale(1.0).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Incisors: scissors. Canines: hooks.").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Molars: millstones").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Stomach: a washing machine with acid").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Bile: dishwashing liquid on fat").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Locks, Keys and Scissors for Molecules
        self.next_band(6)
        b6_title = Tex("Locks and keys").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("One enzyme, one substrate").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("37 degrees: best. Cold: slow. Hot: ruined.").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Amylase stops in stomach acid").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Iodine stays brown when the starch is gone").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Three Big Molecules, Three Small Ones
        self.next_band(7)
        b7_title = Tex("Three big, three small").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Starch to glucose").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Protein to amino acids").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Fat to fatty acids and glycerol").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Most of it in the small intestine").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
