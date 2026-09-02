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
# of 1525 s). Exporter-safe mobjects only (molecules drawn from Circles,
# Dots, Lines and Tex labels); add-only lifecycle; camera bands.

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
        title = Tex("Intermolecular Forces and Physical Properties").scale(1.05).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        # two water molecules: strong bonds inside, weak dashes between
        m1o = Circle(radius=0.35, color=RED).shift(LEFT * 2.6 + UP * 0.6)
        m1h1 = Circle(radius=0.2, color=WHITE).shift(LEFT * 3.3 + UP * 0.0)
        m1h2 = Circle(radius=0.2, color=WHITE).shift(LEFT * 1.9 + UP * 0.0)
        m1b1 = Line(LEFT * 2.6 + UP * 0.45, LEFT * 3.2 + UP * 0.1, stroke_width=6)
        m1b2 = Line(LEFT * 2.6 + UP * 0.45, LEFT * 2.0 + UP * 0.1, stroke_width=6)
        m2o = Circle(radius=0.35, color=RED).shift(RIGHT * 2.6 + UP * 0.6)
        m2h1 = Circle(radius=0.2, color=WHITE).shift(RIGHT * 1.9 + UP * 0.0)
        m2h2 = Circle(radius=0.2, color=WHITE).shift(RIGHT * 3.3 + UP * 0.0)
        m2b1 = Line(RIGHT * 2.6 + UP * 0.45, RIGHT * 2.0 + UP * 0.1, stroke_width=6)
        m2b2 = Line(RIGHT * 2.6 + UP * 0.45, RIGHT * 3.2 + UP * 0.1, stroke_width=6)
        self.play(Create(m1o), Create(m1h1), Create(m1h2), Create(m1b1), Create(m1b2))
        self.play(Create(m2o), Create(m2h1), Create(m2h2), Create(m2b1), Create(m2b2))
        between = VGroup(
            Line(LEFT * 1.4 + UP * 0.3, LEFT * 0.8 + UP * 0.3, color=BLUE, stroke_width=3),
            Line(LEFT * 0.5 + UP * 0.3, RIGHT * 0.1 + UP * 0.3, color=BLUE, stroke_width=3),
            Line(RIGHT * 0.4 + UP * 0.3, RIGHT * 1.0 + UP * 0.3, color=BLUE, stroke_width=3),
        )
        self.play(Create(between))
        self.wait(2)
        b0_l1 = Tex("Inside: strong covalent bonds — the substance itself").scale(0.85).shift(DOWN * 1.0)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("Between: weak attractions — the physical state").scale(0.85).shift(DOWN * 1.8)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("Boiling overcomes ONLY the forces between").scale(0.9).shift(DOWN * 2.7)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=BLUE)))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): London forces ---
        self.next_band(1)
        b1_title = Tex("London forces: the universal flicker").scale(1.05).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Moving electrons bunch briefly: a temporary dipole").scale(0.85).shift(band_shift(1) + UP * 1.3)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = Tex("The neighbour's cloud leans to match: attraction").scale(0.85).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Bigger molecules, more electrons: stronger flickers").scale(0.85).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=BLUE)))
        self.wait(2.5)
        b1_l4 = Tex(r"Halogens: F$_2$, Cl$_2$ gas $\rightarrow$ Br$_2$ liquid $\rightarrow$ I$_2$ solid").scale(0.85).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l4))
        self.wait(2.5)
        b1_l5 = Tex("Only London forces at work — size alone").scale(0.85).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l5))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the rest of the family ---
        self.next_band(2)
        b2_title = Tex("The family, weakest to strongest").scale(1.05).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("London: all molecules, fleeting dipoles").scale(0.85).shift(band_shift(2) + UP * 1.3)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex(r"Dipole-dipole: polar molecules, $\delta+$ to $\delta-$").scale(0.85).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("Hydrogen bonding: H on N, O or F only").scale(0.85).shift(band_shift(2) + DOWN * 0.5)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=BLUE)))
        self.wait(2.5)
        b2_l4 = Tex("A force, not a bond: about a tenth of covalent strength").scale(0.8).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Ion-dipole: ions with polar molecules — dissolving salt").scale(0.8).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l5))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): boiling points and the water anomaly ---
        self.next_band(3)
        b3_title = Tex("The water anomaly").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"H$_2$S: heavier, boils at $-60\,^\circ$C").scale(0.95).shift(band_shift(3) + UP * 1.3)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex(r"H$_2$O: lighter, boils at $+100\,^\circ$C").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("Water hydrogen-bonds; sulfur cannot").scale(0.9).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("Force TYPE beats molecular size").scale(0.95).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("Also: huge specific heat, surface tension, floating ice").scale(0.8).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): vapour pressure ---
        self.next_band(4)
        b4_title = Tex("Vapour pressure: the ranking reversed").scale(1.05).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Fast surface molecules escape; their vapour presses back").scale(0.8).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex("Weak forces: high vapour pressure, quick evaporation").scale(0.85).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("Strong forces: low vapour pressure, slow evaporation").scale(0.85).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = Tex("Propanone streams off the hand; water lingers").scale(0.85).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2.5)
        b4_l5 = Tex("Melting point: same logic, same ranking").scale(0.85).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): how salt dissolves ---
        self.next_band(5)
        b5_title = Tex("Ion-dipole: dismantling a salt crystal").scale(1.05).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(1.5)
        # lattice sketch: alternating dots, waters approaching
        lat = VGroup(*[Dot(LEFT * 2.6 + RIGHT * 0.6 * i + DOWN * 0.6 * j + UP * 0.6,
                           color=(BLUE if (i + j) % 2 == 0 else RED))
                       for i in range(4) for j in range(2)])
        lat.shift(band_shift(5))
        self.play(Create(lat))
        w1 = Circle(radius=0.22, color=WHITE).shift(band_shift(5) + RIGHT * 1.4 + UP * 0.9)
        w2 = Circle(radius=0.22, color=WHITE).shift(band_shift(5) + RIGHT * 1.9 + UP * 0.1)
        self.play(Create(w1), Create(w2))
        self.wait(2)
        b5_l1 = Tex("Oxygen corners court the positive ions").scale(0.85).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex("Hydrogen sides court the negative ions").scale(0.85).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("Many together prise each ion into a hydration shell").scale(0.8).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): like dissolves like ---
        self.next_band(6)
        b6_title = Tex("Like dissolves like — with its engine showing").scale(1.0).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Water takes salt: ion-dipole pays the lattice bill").scale(0.85).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = Tex("Water takes sugar: hydrogen bonds to its O-H groups").scale(0.85).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Petrol takes wax: London forces on both sides").scale(0.85).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex("Wax in water fails: hydrogen bonds refuse the trade").scale(0.85).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("Name solute, solvent and new forces — then judge").scale(0.85).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=BLUE)))
        self.wait(2.5)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): bricks and mortar ---
        self.next_band(7)
        b7_title = Tex("The glue between, not the glue within").scale(1.1).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(2)
        # brick wall sketch
        bricks = VGroup(
            Rectangle(width=1.6, height=0.6).shift(LEFT * 1.7 + UP * 1.0),
            Rectangle(width=1.6, height=0.6).shift(RIGHT * 0.1 + UP * 1.0),
            Rectangle(width=1.6, height=0.6).shift(LEFT * 0.8 + UP * 0.3),
            Rectangle(width=1.6, height=0.6).shift(RIGHT * 1.0 + UP * 0.3),
        )
        bricks.shift(band_shift(7))
        self.play(Create(bricks))
        self.wait(2)
        b7_l1 = Tex("Bricks: bonds inside molecules").scale(0.9).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("Mortar: the weak grip between neighbours").scale(0.9).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("Heat attacks only the mortar — steam is still water").scale(0.85).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): three grades of sticky ---
        self.next_band(8)
        b8_title = Tex("Three grades of sticky").scale(1.15).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Grade one: the flicker — every molecule, grows with size").scale(0.8).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Grade two: the permanent lean — polar molecules line up").scale(0.8).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Grade three: the handshake — H on N, O or F locks on").scale(0.8).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=BLUE)))
        self.wait(2.5)
        b8_l4 = Tex(r"H$_2$S flickers and leans: $-60\,^\circ$C").scale(0.85).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex(r"Water shakes hands: $+100\,^\circ$C — hence oceans").scale(0.85).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): salt disappears, oil refuses ---
        self.next_band(9)
        b9_title = Tex("Why salt disappears and oil refuses").scale(1.1).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Water's charged corners mob each ion and carry it off").scale(0.8).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("The salt rides first class in a hydration escort").scale(0.85).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Oil offers nothing; water keeps its handshakes").scale(0.85).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("Not repulsion — a trade not worth making").scale(0.85).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex("Read the grip, predict the behaviour").scale(0.95).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l5))
        self.wait(4)
