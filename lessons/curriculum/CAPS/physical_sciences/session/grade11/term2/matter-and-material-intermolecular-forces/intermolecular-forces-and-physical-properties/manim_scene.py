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

# Band-layout whiteboard scene for the Intermolecular Forces duo.
# Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7.
# Band dwell proportional to subtopics.json (220/250/245/235/185/195/195
# of 1525 s). Exporter-safe mobjects only; add-only lifecycle; camera bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class IntermolecularForcesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): between, not within ---
        title = Tex("Intermolecular Forces").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("INTRAmolecular: bonds INSIDE — strong").scale(1.0).shift(UP * 1.3)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = Tex("INTERmolecular: grip BETWEEN — far weaker").scale(1.0).shift(UP * 0.4)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex(r"Steam is still H$_2$O — boiling fights").scale(0.95).shift(DOWN * 0.6)
        b0_l4 = Tex("only the grip between molecules").scale(0.95).shift(DOWN * 1.3)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(VGroup(b0_l3, b0_l4), color=BLUE)))
        self.wait(2.5)
        b0_trap = Tex("the bonds break when water boils").scale(0.95).shift(DOWN * 2.4)
        self.play(Write(b0_trap))
        self.play(Create(strike(b0_trap)))
        self.wait(1.5)
        b0_l5 = Tex("Say: the intermolecular forces are overcome").scale(0.9).shift(DOWN * 3.1)
        self.play(Write(b0_l5))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): London forces ---
        self.next_band(1)
        b1_title = Tex("London forces: the flickering dipole").scale(1.1).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Electrons bunch for an instant — a temporary").scale(0.95).shift(band_shift(1) + UP * 1.3)
        b1_l2 = Tex("dipole that induces one next door").scale(0.95).shift(band_shift(1) + UP * 0.6)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Between ALL molecules; the only option").scale(0.95).shift(band_shift(1) + DOWN * 0.4)
        b1_l4 = Tex("for non-polar ones").scale(0.95).shift(band_shift(1) + DOWN * 1.1)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(2.5)
        b1_l5 = Tex("Bigger molecules, bigger clouds, stronger grip:").scale(0.9).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l5))
        self.wait(2)
        b1_l6 = Tex(r"F$_2$, Cl$_2$ gas $\to$ Br$_2$ liquid $\to$ I$_2$ solid").scale(0.95).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l6))
        self.play(Create(SurroundingRectangle(b1_l6, color=GREEN)))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the rest of the family ---
        self.next_band(2)
        b2_title = Tex("The family, weakest to strongest").scale(1.1).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("1. London — every molecule").scale(0.95).shift(band_shift(2) + UP * 1.3)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex(r"2. Dipole-dipole — polar molecules (HCl)").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("3. Hydrogen bonding — H on N, O or F").scale(0.95).shift(band_shift(2) + DOWN * 0.5)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("4. Ion-dipole — ions with polar molecules").scale(0.95).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(VGroup(b2_l1, b2_l2, b2_l3, b2_l4), color=BLUE)))
        self.wait(2.5)
        b2_l5 = Tex("A hydrogen bond is a FORCE, not a bond —").scale(0.9).shift(band_shift(2) + DOWN * 2.4)
        b2_l6 = Tex("about a tenth of a covalent bond").scale(0.9).shift(band_shift(2) + DOWN * 3.1)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): boiling points and the water anomaly ---
        self.next_band(3)
        b3_title = Tex("Force TYPE beats molecular size").scale(1.1).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Stronger grip: more energy to break free,").scale(0.95).shift(band_shift(3) + UP * 1.3)
        b3_l2 = Tex("higher boiling point").scale(0.95).shift(band_shift(3) + UP * 0.6)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex(r"H$_2$O: 100 $^\circ$C. \; H$_2$S: $-$60 $^\circ$C").scale(1.0).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex(r"H$_2$S is heavier — but only water").scale(0.95).shift(band_shift(3) + DOWN * 1.5)
        b3_l5 = Tex("can hydrogen-bond").scale(0.95).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(2.5)
        b3_l6 = Tex("Also: oceans steady the climate; ice floats").scale(0.9).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(b3_l6))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): vapour pressure ---
        self.next_band(4)
        b4_title = Tex("Vapour pressure: the ranking reversed").scale(1.1).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Weak forces: easy escape — high vapour").scale(0.95).shift(band_shift(4) + UP * 1.3)
        b4_l2 = Tex("pressure, fast evaporation, low boiling point").scale(0.95).shift(band_shift(4) + UP * 0.6)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("Strong forces: molecules held back —").scale(0.95).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex("low vapour pressure, slow evaporation").scale(0.95).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = Tex("Propanone streams off your hand in seconds;").scale(0.9).shift(band_shift(4) + DOWN * 2.1)
        b4_l6 = Tex("hydrogen-bonded water lingers").scale(0.9).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l5))
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_4): how salt dissolves ---
        self.next_band(5)
        b5_title = Tex("Ion-dipole: how salt dissolves").scale(1.1).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        ion = Dot(band_shift(5) + UP * 0.9)
        lion = MathTex(r"\text{Na}^+").scale(0.85).shift(band_shift(5) + UP * 0.9 + RIGHT * 0.75)
        self.play(FadeIn(ion), Write(lion))
        arr = VGroup(
            Arrow(UP * 2.1, UP * 1.25, buff=0, color=YELLOW),
            Arrow(DOWN * 0.3 + UP * 0.0, UP * 0.55, buff=0, color=YELLOW),
            Arrow(LEFT * 1.4 + UP * 0.9, LEFT * 0.35 + UP * 0.9, buff=0, color=YELLOW),
            Arrow(RIGHT * 1.9 + UP * 1.7, RIGHT * 0.35 + UP * 1.1, buff=0, color=YELLOW),
        )
        arr.shift(band_shift(5))
        lwat = Tex(r"water's $\delta-$ oxygen corners point in").scale(0.9).shift(band_shift(5) + LEFT * 0.2 + DOWN * 1.0)
        self.play(Create(arr))
        self.play(Write(lwat))
        self.wait(2.5)
        b5_l1 = Tex("Together they out-pull the lattice, pluck the").scale(0.9).shift(band_shift(5) + DOWN * 1.9)
        b5_l2 = Tex("ion free, and wrap it in a hydration shell").scale(0.9).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(3)

        # --- Band 6 (subtopic_4): like dissolves like ---
        self.next_band(6)
        b6_title = Tex("Like dissolves like — with the forces named").scale(1.05).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Polar dissolves polar and ionic: salt, sugar").scale(0.95).shift(band_shift(6) + UP * 1.3)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = Tex("Non-polar dissolves non-polar: wax in petrol").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Wax in water fails: water's hydrogen bonds").scale(0.95).shift(band_shift(6) + DOWN * 0.6)
        b6_l4 = Tex("cling to each other and exclude the intruder").scale(0.95).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("Exam skill: name the forces in solute, in").scale(0.95).shift(band_shift(6) + DOWN * 2.3)
        b6_l6 = Tex("solvent, and between — then judge the deal").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): bricks and mortar ---
        self.next_band(7)
        b7_title = Tex("The glue between, not the glue within").scale(1.1).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Bricks: bonds inside each molecule").scale(0.95).shift(band_shift(7) + UP * 1.3)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex("Mortar: the weak grip between neighbours").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Melting and boiling only ever attack the mortar").scale(0.95).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex("Sanitiser: weak mortar, gone in seconds.").scale(0.95).shift(band_shift(7) + DOWN * 1.6)
        b7_l5 = Tex("Water: strongest everyday mortar, lingers").scale(0.95).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): three grades of sticky ---
        self.next_band(8)
        b8_title = Tex("Three grades of sticky").scale(1.2).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("1. The flicker — every molecule, weakest;").scale(0.95).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex("bigger molecules flicker harder").scale(0.95).shift(band_shift(8) + UP * 0.6)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("2. The permanent lean — polar molecules").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("3. The special handshake — H on N, O or F").scale(0.95).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2.5)
        b8_l5 = Tex(r"H$_2$S: $-$60 $^\circ$C; H$_2$O: $+$100 $^\circ$C").scale(0.95).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8_l5))
        self.wait(2)
        b8_l6 = Tex("Without handshakes, the oceans would be vapour").scale(0.9).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_7): salt disappears, oil refuses ---
        self.next_band(9)
        b9_title = Tex("Why salt disappears and oil refuses").scale(1.1).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Water's tiny magnets swarm each ion and").scale(0.95).shift(band_shift(9) + UP * 1.3)
        b9_l2 = Tex("carry it off in a watery escort").scale(0.95).shift(band_shift(9) + UP * 0.6)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Oil offers water nothing — the water closes").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        b9_l4 = Tex("ranks and squeezes the oil out on top").scale(0.95).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("New attractions must pay for the old ones broken").scale(0.9).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l5))
        self.wait(2.5)
        b9_l6 = Tex("Read the grip, predict the behaviour").scale(1.0).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(4)
