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

# Band-layout whiteboard scene for the energy-and-change session duo.
# Covers all seven subtopics (Part 1 Expert: subtopics 1-4, Part 2
# Simplifier: subtopics 5-7) with band time proportional to subtopics.json
# (225/235/235/245/200/200/205 of 1545 s). Add-only lifecycle: nothing is
# faded out; the camera moves down to a fresh band for every teaching step.
# Only exporter-safe mobjects are used (Tex/MathTex/Line/Dot/Rectangle).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ExoEndoEnergyGraphsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the two bond laws and delta H ---
        title = Tex("The Energy Ledger of a Reaction").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Breaking a bond COSTS energy").scale(1.1).shift(UP * 1.1)
        b0_l2 = Tex("Forming a bond PAYS energy out").scale(1.1).shift(UP * 0.3)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("Two laws, zero exceptions").scale(1.0).shift(DOWN * 0.5)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_eq = MathTex(r"\Delta H = E_{products} - E_{reactants}").scale(1.2).shift(DOWN * 1.5)
        self.play(Write(b0_eq))
        self.play(Create(SurroundingRectangle(b0_eq, color=GREEN)))
        self.wait(2)
        b0_l4 = Tex("units: kJ, or kJ per mole").scale(1.0).shift(DOWN * 2.6)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): the sign belongs to the SYSTEM ---
        self.next_band(1)
        b1_t = Tex("Whose account is it?").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_l1 = Tex("Forming pays out more than breaking costs:").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"\Delta H < 0 \quad \text{(products sit LOWER)}").scale(1.1).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_wrong = Tex("Beaker feels hot, so delta H is positive?").scale(1.05).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2)
        b1_fix = Tex("Delta H reads the CHEMICALS' account:").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        b1_fix2 = Tex("the chemicals finished poorer — negative").scale(1.0).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_fix))
        self.wait(2)
        self.play(Write(b1_fix2))
        self.wait(3)

        # --- Band 2 (subtopic_2): exothermic reactions ---
        self.next_band(2)
        b2_t = Tex(r"Exothermic: exports energy, $\Delta H < 0$").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_eq = MathTex(r"C_3H_8 + 5O_2 \rightarrow 3CO_2 + 4H_2O").scale(1.1).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_eq))
        self.wait(2)
        b2_l1 = Tex("The named three: combustion,").scale(1.05).shift(band_shift(2) + UP * 0.1)
        b2_l2 = Tex("respiration, neutralisation").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l1))
        self.wait(1.5)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("Surroundings warm; products finish").scale(1.0).shift(band_shift(2) + DOWN * 1.7)
        b2_l4 = Tex("BELOW the reactants on the energy axis").scale(1.0).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l3))
        self.wait(1.5)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): endothermic reactions ---
        self.next_band(3)
        b3_t = Tex(r"Endothermic: imports energy, $\Delta H > 0$").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_eq = MathTex(r"6CO_2 + 6H_2O \rightarrow C_6H_{12}O_6 + 6O_2").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_eq))
        self.wait(2)
        b3_l1 = Tex("Photosynthesis, funded by sunlight,").scale(1.0).shift(band_shift(3) + UP * 0.2)
        b3_l2 = Tex(r"and thermal decomposition of $MgCO_3$").scale(1.0).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex(r"Beaker warms: exothermic, $\Delta H < 0$").scale(1.05).shift(band_shift(3) + DOWN * 1.6)
        b3_l4 = Tex(r"Beaker chills: endothermic, $\Delta H > 0$").scale(1.05).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): activation energy and the complex ---
        self.next_band(4)
        b4_t = Tex("The barrier before the descent").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_l1 = Tex(r"$E_A$: the minimum energy colliding").scale(1.05).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex("particles must carry to react").scale(1.05).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l1))
        self.wait(1.5)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex("At the summit: the ACTIVATED COMPLEX —").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = Tex("a fleeting arrangement, old bonds").scale(1.0).shift(band_shift(4) + DOWN * 1.4)
        b4_l5 = Tex("part-broken, new part-formed, max energy").scale(1.0).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(b4_l3))
        self.wait(1.5)
        self.play(Write(b4_l4))
        self.wait(1.5)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): the match, and keeping EA apart from dH ---
        self.next_band(5)
        b5_t = Tex("The physics of the matchstick").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_l1 = Tex("The match funds the FIRST crossing only;").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("the reaction's surplus funds the rest").scale(1.05).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"\Delta H: \text{ start level to finish level}").scale(1.05).shift(band_shift(5) + DOWN * 0.7)
        b5_l4 = MathTex(r"E_A: \text{ start level to the summit}").scale(1.05).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("A steep drop can still charge steep admission").scale(1.0).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the potential energy graph, in numbers ---
        self.next_band(6)
        b6_t = Tex("The potential energy graph").scale(1.15).shift(band_shift(6) + UP * 2.6)
        self.play(Write(b6_t))
        self.wait(2)
        # Hand-built axes: PE vertical, reaction course horizontal.
        origin = band_shift(6) + LEFT * 4.8 + DOWN * 2.6
        y_axis = Arrow(origin, origin + UP * 4.6, buff=0, stroke_width=3)
        x_axis = Arrow(origin, origin + RIGHT * 8.6, buff=0, stroke_width=3)
        y_lab = Tex("PE (kJ)").scale(0.8).shift(band_shift(6) + LEFT * 5.4 + UP * 2.0)
        x_lab = Tex("reaction progress").scale(0.8).shift(band_shift(6) + RIGHT * 2.6 + DOWN * 3.1)
        self.play(Create(y_axis), Create(x_axis))
        self.play(Write(y_lab), Write(x_lab))
        self.wait(2)
        # Levels: reactants 80 kJ, summit 170 kJ, products 30 kJ.
        r_y = origin + UP * 1.8
        p_y = origin + UP * 0.7
        top = origin + UP * 4.0
        seg1 = Line(r_y + RIGHT * 0.5, r_y + RIGHT * 1.7, color=BLUE, stroke_width=5)
        seg2 = Line(r_y + RIGHT * 1.7, top + RIGHT * 2.9, color=BLUE, stroke_width=5)
        seg3 = Line(top + RIGHT * 2.9, top + RIGHT * 3.9, color=BLUE, stroke_width=5)
        seg4 = Line(top + RIGHT * 3.9, p_y + RIGHT * 5.7, color=BLUE, stroke_width=5)
        seg5 = Line(p_y + RIGHT * 5.7, p_y + RIGHT * 7.2, color=BLUE, stroke_width=5)
        lab_r = MathTex(r"80").scale(0.85).next_to(seg1, LEFT, buff=0.15)
        self.play(Create(seg1), Write(lab_r))
        self.wait(1.5)
        self.play(Create(seg2))
        self.play(Create(seg3))
        lab_top = MathTex(r"170").scale(0.85).next_to(seg3, UP, buff=0.15)
        self.play(Write(lab_top))
        self.wait(1.5)
        self.play(Create(seg4))
        self.play(Create(seg5))
        lab_p = MathTex(r"30").scale(0.85).next_to(seg5, RIGHT, buff=0.15)
        self.play(Write(lab_p))
        self.wait(2)
        b6_r1 = MathTex(r"E_A = 170 - 80 = 90 \text{ kJ}").scale(0.95).shift(band_shift(6) + RIGHT * 2.9 + UP * 1.6)
        b6_r2 = MathTex(r"\Delta H = 30 - 80 = -50 \text{ kJ}").scale(0.95).shift(band_shift(6) + RIGHT * 2.9 + UP * 0.7)
        self.play(Write(b6_r1))
        self.wait(2)
        self.play(Write(b6_r2))
        self.play(Create(SurroundingRectangle(b6_r2, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): reverse reaction and the catalyst ---
        self.next_band(7)
        b7_t = Tex("Read it backwards, then catalyse it").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = MathTex(r"E_{A,rev} = 170 - 30 = 140 \text{ kJ}").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = MathTex(r"\Delta H_{rev} = +50 \text{ kJ (sign flips)}").scale(1.0).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("Catalyst: alternative path, 170 drops to 130").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_l3))
        self.wait(2)
        # sketch: original summit (solid) with lower dashed catalysed summit
        base = band_shift(7) + DOWN * 2.9 + LEFT * 3.4
        c1 = Line(base, base + RIGHT * 2.4 + UP * 1.6, color=BLUE, stroke_width=4)
        c2 = Line(base + RIGHT * 2.4 + UP * 1.6, base + RIGHT * 4.8 + UP * 0.3, color=BLUE, stroke_width=4)
        d1 = DashedLine(base, base + RIGHT * 2.4 + UP * 1.0, color=YELLOW, stroke_width=4)
        d2 = DashedLine(base + RIGHT * 2.4 + UP * 1.0, base + RIGHT * 4.8 + UP * 0.3, color=YELLOW, stroke_width=4)
        self.play(Create(c1), Create(c2))
        self.play(Create(d1), Create(d2))
        self.wait(2)
        b7_l4 = Tex(r"Levels bolted down: $\Delta H$ unchanged").scale(1.0).shift(band_shift(7) + RIGHT * 3.2 + DOWN * 1.7)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): buckets, costs and payouts ---
        self.next_band(8)
        b8_t = Tex("Paying to break, earning to build").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Bonds are buckets in wells: winching up").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("costs, dropping back pays — always").scale(1.05).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("Payout beats cost: gas heater, exothermic").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        b8_l4 = Tex("Cost beats payout: cold pack, endothermic").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Delta H = the chemicals' closing balance").scale(1.05).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the entry fee ---
        self.next_band(9)
        b9_t = Tex("Why the braai needs a match").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Every reaction charges admission first:").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex(r"the activation energy $E_A$").scale(1.1).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("The match is a startup loan; each payout").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        b9_l4 = Tex("buys admission for the neighbours").scale(1.0).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("Steep admission: paraffin and air at peace").scale(1.0).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the hill between two valleys ---
        self.next_band(10)
        b10_t = Tex("The hill between two valleys").scale(1.2).shift(band_shift(10) + UP * 2.5)
        self.play(Write(b10_t))
        self.wait(2)
        # compact trail sketch: valley 80 -> ridge 170 -> valley 30
        base = band_shift(10) + LEFT * 4.6 + DOWN * 1.6
        v1 = Line(base, base + RIGHT * 1.4, color=BLUE, stroke_width=5)
        up1 = Line(base + RIGHT * 1.4, base + RIGHT * 3.4 + UP * 2.6, color=BLUE, stroke_width=5)
        rg = Line(base + RIGHT * 3.4 + UP * 2.6, base + RIGHT * 4.4 + UP * 2.6, color=BLUE, stroke_width=5)
        dn1 = Line(base + RIGHT * 4.4 + UP * 2.6, base + RIGHT * 6.4 + DOWN * 0.9, color=BLUE, stroke_width=5)
        v2 = Line(base + RIGHT * 6.4 + DOWN * 0.9, base + RIGHT * 7.8 + DOWN * 0.9, color=BLUE, stroke_width=5)
        t1 = MathTex(r"80").scale(0.85).next_to(v1, LEFT, buff=0.15)
        t2 = MathTex(r"170").scale(0.85).next_to(rg, UP, buff=0.15)
        t3 = MathTex(r"30").scale(0.85).next_to(v2, RIGHT, buff=0.15)
        self.play(Create(v1), Write(t1))
        self.play(Create(up1), Create(rg), Write(t2))
        self.play(Create(dn1), Create(v2), Write(t3))
        self.wait(2)
        b10_l1 = Tex(r"Climb 90; drop 50: $\Delta H = -50$ kJ").scale(1.0).shift(band_shift(10) + DOWN * 2.3)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = Tex("Backwards: climb 140, finish 50 higher").scale(1.0).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("Catalyst = tunnel: quicker, valleys fixed").scale(1.0).shift(band_shift(10) + UP * 1.4 + RIGHT * 2.6)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(4)
