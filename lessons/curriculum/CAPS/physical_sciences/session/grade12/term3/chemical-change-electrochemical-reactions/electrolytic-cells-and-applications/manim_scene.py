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

# Band-layout whiteboard scene for "Electrolytic Cells and Applications"
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe vocabulary only; the electrolytic cell is hand-built from
# Rectangles (battery, electrodes), Lines (wires, beaker) and Tex labels.
# Subtopic durations 235/240/240/235/190/195/195 of 1530 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ElectrolyticCellsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): galvanic versus electrolytic ---
        title = Tex("Electrolytic Cells and Applications").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Galvanic: chemical to electrical, spontaneous").scale(1.0).shift(UP * 1.2)
        b0_l2 = Tex("Electrolytic: electrical FORCES the chemistry").scale(1.0).shift(UP * 0.4)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Never bends: oxidation at the anode,").scale(1.0).shift(DOWN * 0.5)
        b0_l4 = Tex("reduction at the cathode").scale(1.0).shift(DOWN * 1.3)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2.5)
        b0_l5 = Tex("Flip: here the anode is POSITIVE").scale(1.0).shift(DOWN * 2.2)
        b0_l6 = Tex("Anions to the ANode, cations to the CAThode").scale(0.95).shift(DOWN * 3.0)
        self.play(Write(b0_l5))
        self.wait(2)
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_2): the copper chloride cell, drawn ---
        self.next_band(1)
        b1_title = Tex(r"Electrolysis of $CuCl_2$ solution").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        # Battery on top, wires down to two carbon electrodes in a beaker.
        c1 = band_shift(1) + DOWN * 0.4
        batt = Rectangle(width=1.6, height=0.6).move_to(c1 + UP * 2.0)
        lab_plus = Tex("$+$").scale(0.8).shift(c1 + UP * 2.45 + RIGHT * 0.6)
        lab_min = Tex("$-$").scale(0.8).shift(c1 + UP * 2.45 + LEFT * 0.6)
        self.play(Create(batt))
        self.play(Write(lab_plus), Write(lab_min))
        wire_l = VGroup(
            Line(c1 + UP * 2.0 + LEFT * 0.8, c1 + UP * 2.0 + LEFT * 2.6),
            Line(c1 + UP * 2.0 + LEFT * 2.6, c1 + UP * 0.6 + LEFT * 2.6),
        )
        wire_r = VGroup(
            Line(c1 + UP * 2.0 + RIGHT * 0.8, c1 + UP * 2.0 + RIGHT * 2.6),
            Line(c1 + UP * 2.0 + RIGHT * 2.6, c1 + UP * 0.6 + RIGHT * 2.6),
        )
        self.play(Create(wire_l), Create(wire_r))
        beaker = VGroup(
            Line(c1 + LEFT * 3.6 + UP * 0.4, c1 + LEFT * 3.6 + DOWN * 1.6),
            Line(c1 + LEFT * 3.6 + DOWN * 1.6, c1 + RIGHT * 3.6 + DOWN * 1.6),
            Line(c1 + RIGHT * 3.6 + DOWN * 1.6, c1 + RIGHT * 3.6 + UP * 0.4),
        )
        self.play(Create(beaker))
        el_l = Rectangle(width=0.25, height=1.7).move_to(c1 + LEFT * 2.6 + DOWN * 0.3)
        el_r = Rectangle(width=0.25, height=1.7).move_to(c1 + RIGHT * 2.6 + DOWN * 0.3)
        self.play(Create(el_l), Create(el_r))
        lab_cat = Tex("cathode $-$").scale(0.8).shift(c1 + LEFT * 2.6 + DOWN * 2.1)
        lab_an = Tex("anode $+$").scale(0.8).shift(c1 + RIGHT * 2.6 + DOWN * 2.1)
        self.play(Write(lab_cat), Write(lab_an))
        self.wait(2)
        lab_cu = Tex("Cu plates here").scale(0.75).shift(c1 + LEFT * 1.2 + DOWN * 0.3)
        lab_cl = Tex("$Cl_2$ bubbles").scale(0.75).shift(c1 + RIGHT * 1.2 + DOWN * 0.3)
        self.play(Write(lab_cu))
        self.play(Write(lab_cl))
        self.wait(3)

        # --- Band 2 (subtopic_2): half-reactions and observables ---
        self.next_band(2)
        b2_title = Tex("The half-reactions").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{cathode: } Cu^{2+} + 2e^- \rightarrow Cu(s)").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"\text{anode: } 2Cl^- \rightarrow Cl_2(g) + 2e^-").scale(1.05).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"Cu^{2+} + 2Cl^- \rightarrow Cu + Cl_2").scale(1.05).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex("Observe: copper plates the cathode,").scale(1.0).shift(band_shift(2) + DOWN * 1.8)
        b2_l5 = Tex("chlorine smells at the anode,").scale(1.0).shift(band_shift(2) + DOWN * 2.6)
        b2_l6 = Tex("blue-green colour fades").scale(1.0).shift(band_shift(2) + DOWN * 3.4)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_3): electroplating the spoon ---
        self.next_band(3)
        b3_title = Tex("Electroplating: silver on a spoon").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Object $=$ CATHODE (negative terminal)").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("Anode $=$ bar of the plating metal").scale(1.0).shift(band_shift(3) + UP * 0.2)
        b3_l3 = Tex("Bath $=$ solution of that metal's ions").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = MathTex(r"\text{anode: } Ag \rightarrow Ag^+ + e^-").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        b3_l5 = MathTex(r"\text{cathode: } Ag^+ + e^- \rightarrow Ag").scale(1.0).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.wait(2)
        b3_l6 = Tex("Bar dissolves, spoon gains: bath constant").scale(0.95).shift(band_shift(3) + DOWN * 3.4)
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): refining copper ---
        self.next_band(4)
        b4_title = Tex("Refining copper: 99\\% to 99,99\\%").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Impure slab: anode. Pure sheet: cathode.").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex("Electrolyte: copper sulfate solution").scale(1.0).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex("Cu dissolves out, plates pure on the sheet").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex("Ag, Au, Pt never oxidise: drop as").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        b4_l5 = Tex("anode mud — sold to fund the refinery").scale(1.0).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(2)
        b4_l6 = Tex("More reactive impurities: stay dissolved").scale(0.95).shift(band_shift(4) + DOWN * 3.3)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_4): brine — competition at each electrode ---
        self.next_band(5)
        b5_title = Tex("Concentrated brine: every electrode").scale(1.1).shift(band_shift(5) + UP * 2.4)
        b5_title2 = Tex("is a competition").scale(1.1).shift(band_shift(5) + UP * 1.7)
        self.play(Write(b5_title))
        self.play(Write(b5_title2))
        self.wait(2)
        b5_l1 = MathTex(r"\text{anode: } 2Cl^- \rightarrow Cl_2 + 2e^-").scale(1.0).shift(band_shift(5) + UP * 0.7)
        b5_l2 = Tex("(concentrated chloride beats water)").scale(0.95).shift(band_shift(5) + DOWN * 0.1)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"\text{cathode: } 2H_2O + 2e^- \rightarrow H_2 + 2OH^-").scale(1.0).shift(band_shift(5) + DOWN * 1.1)
        b5_l4 = Tex("(water beats $Na^+$ — Na is too hard to reduce)").scale(0.9).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): three products, one caveat ---
        self.next_band(6)
        b6_title = Tex("Salt water: three products").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("$Cl_2$ at the anode: water treatment, PVC").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("$H_2$ at the cathode: fuel, ammonia").scale(1.0).shift(band_shift(6) + UP * 0.2)
        b6_l3 = Tex("$NaOH$ left in the cell: soap, paper").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = Tex("DILUTE brine: water wins the anode too —").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        b6_l5 = Tex("oxygen instead of chlorine").scale(1.0).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): running the reaction backwards ---
        self.next_band(7)
        b7_title = Tex("Running the reaction backwards").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Galvanic: water flowing downhill, for free").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("Electrolytic: the pump pushing it back up").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Your phone: galvanic all day,").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        b7_l4 = Tex("electrolytic all night on the charger").scale(1.0).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("Lost? Ask: where are electrons torn away?").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        b7_l6 = Tex("That is oxidation; that is the anode.").scale(1.0).shift(band_shift(7) + DOWN * 3.3)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): a silver skin on a steel spoon ---
        self.next_band(8)
        b8_title = Tex("A silver skin on a steel spoon").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("The only painter that works atom by atom").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("Spoon at the negative: ions drift in, deposit").scale(1.0).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex("Bar at the positive: paint tin AND refill").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l2))
        self.wait(2.5)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("Refinery: dirty copper in, pure copper out,").scale(1.0).shift(band_shift(8) + DOWN * 1.7)
        b8_l5 = Tex("and gold-rich mud pays the bills").scale(1.0).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_7): salt water in, three industries out ---
        self.next_band(9)
        b9_title = Tex("Salt water in, three industries out").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_wrong = Tex("Sodium metal forms at the cathode").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_wrong))
        self.play(Create(strike(b9_wrong)))
        self.wait(2)
        b9_l1 = Tex("Sodium clings to its ion; WATER is reduced:").scale(0.95).shift(band_shift(9) + UP * 0.2)
        b9_l2 = Tex("hydrogen bubbles, hydroxide stays").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Concentrated chloride wins the positive:").scale(1.0).shift(band_shift(9) + DOWN * 1.5)
        b9_l4 = Tex("chlorine for pools, bleach and PVC").scale(1.0).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("Leftovers $=$ caustic soda: a product too").scale(1.0).shift(band_shift(9) + DOWN * 3.2)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(4)
