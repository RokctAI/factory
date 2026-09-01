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

# Band-layout whiteboard scene for the IEB revision session "Climate,
# Geomorphology and Mapwork Essentials" (grade 11, term 4). Seven subtopics of
# the duo: Part 1 Expert (subtopics 1-4), Part 2 Simplifier (subtopics 5-7).
# Band time apportioned to subtopics.json (250/260/255/255/190/195/195 of
# 1600 s). Exporter-safe primitives only; diagrams (pressure belts, cake
# sequence, slope profile, contour rings) hand-built from
# Line/Arrow/Dot/Circle/Rectangle/Tex element by element.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ClimateGeomorphologyMapworkSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): unequal heating and the pressure chain
        title = Tex("Climate, Geomorphology and Mapwork").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Vertical rays: concentrated. Slanted rays: spread.").scale(0.9).shift(UP * 1.3)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex(r"Surplus to $\approx 40^\circ$; deficit beyond").scale(0.95).shift(UP * 0.5)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex(r"warm rises $\to$ LOW; cold sinks $\to$ HIGH;").scale(0.95).shift(DOWN * 0.4)
        b0_l4 = Tex(r"wind drains high $\to$ low").scale(0.95).shift(DOWN * 1.2)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2.5)
        b0_l5 = Tex(r"Belts: equatorial low, 30$^\circ$ highs,").scale(0.9).shift(DOWN * 2.1)
        b0_l6 = Tex(r"60$^\circ$ lows, polar highs — all migrating").scale(0.9).shift(DOWN * 2.8)
        self.play(Write(b0_l5))
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_1): belts, cells, Coriolis
        self.next_band(1)
        b1_title = Tex("Cells and the bend").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        # Hadley loop: rise arrow, poleward aloft, sink arrow, return arrow.
        up_ar = Arrow(band_shift(1) + DOWN * 0.6 + LEFT * 3.4, band_shift(1) + UP * 1.0 + LEFT * 3.4, color=RED)
        al_ar = Arrow(band_shift(1) + UP * 1.1 + LEFT * 3.0, band_shift(1) + UP * 1.1 + RIGHT * 3.0, color=YELLOW)
        dn_ar = Arrow(band_shift(1) + UP * 1.0 + RIGHT * 3.4, band_shift(1) + DOWN * 0.6 + RIGHT * 3.4, color=BLUE)
        bk_ar = Arrow(band_shift(1) + DOWN * 0.7 + RIGHT * 3.0, band_shift(1) + DOWN * 0.7 + LEFT * 3.0, color=GREEN)
        self.play(Create(up_ar))
        self.play(Create(al_ar))
        self.play(Create(dn_ar))
        self.play(Create(bk_ar))
        self.wait(2)
        b1_l1 = Tex(r"Hadley: rise at 0$^\circ$, sink at 30$^\circ$, trades return").scale(0.85).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex(r"Ferrel drives the westerlies; polar cell the easterlies").scale(0.85).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex(r"Coriolis: LEFT in the south — SE trades, SW gales").scale(0.85).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): Africa's rain switch
        self.next_band(2)
        b2_title = Tex("Africa: convergence against subsidence").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"ITCZ: the thundery seam of colliding trades,").scale(0.9).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex(r"migrating with the sun — the wet season IS its visit").scale(0.85).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex(r"Three highs box us in: South Atlantic,").scale(0.9).shift(band_shift(2) + DOWN * 0.4)
        b2_l4 = Tex(r"South Indian, winter's Kalahari lid").scale(0.9).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.wait(2.5)
        b2_l5 = Tex(r"East coast: warm Agulhas feeds rain").scale(0.9).shift(band_shift(2) + DOWN * 2.0)
        b2_l6 = Tex(r"West coast: cold Benguela — fog, no rain").scale(0.9).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): drought ladder and desertification
        self.next_band(3)
        b3_title = Tex("Drought and desertification").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Drought $=$ rain below what the region expects").scale(0.9).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex(r"Ladder: meteorological $\to$ hydrological").scale(0.9).shift(band_shift(3) + UP * 0.4)
        b3_l3 = Tex(r"$\to$ agricultural $\to$ socio-economic").scale(0.9).shift(band_shift(3) + DOWN * 0.3)
        self.play(Write(b3_l2))
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex(r"El Ni\~no dries our summers; La Ni\~na wets them").scale(0.85).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex(r"Desertification: long-term, human-driven land").scale(0.9).shift(band_shift(3) + DOWN * 1.9)
        b3_l6 = Tex(r"damage that drought exposes — Sahel, Karoo edge").scale(0.85).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(b3_l6, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): horizontal strata — the Karoo sequence
        self.next_band(4)
        b4_title = Tex("Flat strata: the tabletop family").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        # Shrinking sequence: four rectangles of decreasing width.
        m1 = Rectangle(width=3.2, height=0.8).shift(band_shift(4) + UP * 0.9 + LEFT * 4.0)
        m1_lab = Tex("plateau").scale(0.7).shift(band_shift(4) + UP * 0.0 + LEFT * 4.0)
        m2 = Rectangle(width=2.0, height=0.8).shift(band_shift(4) + UP * 0.9 + LEFT * 1.2)
        m2_lab = Tex("mesa").scale(0.7).shift(band_shift(4) + UP * 0.0 + LEFT * 1.2)
        m3 = Rectangle(width=0.9, height=1.2).shift(band_shift(4) + UP * 1.1 + RIGHT * 1.3)
        m3_lab = Tex("butte").scale(0.7).shift(band_shift(4) + UP * 0.1 + RIGHT * 1.3)
        c_left = Line(band_shift(4) + UP * 0.5 + RIGHT * 2.9, band_shift(4) + UP * 1.6 + RIGHT * 3.5)
        c_right = Line(band_shift(4) + UP * 1.6 + RIGHT * 3.5, band_shift(4) + UP * 0.5 + RIGHT * 4.1)
        c_lab = Tex("cone").scale(0.7).shift(band_shift(4) + UP * 0.1 + RIGHT * 3.5)
        self.play(Create(m1), Write(m1_lab))
        self.play(Create(m2), Write(m2_lab))
        self.play(Create(m3), Write(m3_lab))
        self.play(Create(c_left), Create(c_right), Write(c_lab))
        self.wait(2)
        b4_l1 = Tex(r"Dolerite cap shields soft shale — differential").scale(0.85).shift(band_shift(4) + DOWN * 1.2)
        b4_l2 = Tex(r"erosion; slopes retreat, the cap rim holds a cliff").scale(0.85).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex(r"Mesa: top wider than height. Butte: taller than wide.").scale(0.85).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): inclined and massive rock
        self.next_band(5)
        b5_title = Tex("Tilted strata and massive granite").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        # Cuesta profile: gentle dip line, steep scarp line.
        dip = Line(band_shift(5) + DOWN * 0.4 + LEFT * 4.2, band_shift(5) + UP * 1.0 + LEFT * 0.8)
        scarp = Line(band_shift(5) + UP * 1.0 + LEFT * 0.8, band_shift(5) + DOWN * 0.4 + RIGHT * 0.2)
        dip_lab = Tex("dip: gentle").scale(0.7).shift(band_shift(5) + UP * 0.7 + LEFT * 3.4)
        scarp_lab = Tex("scarp: steep").scale(0.7).shift(band_shift(5) + UP * 0.9 + RIGHT * 1.6)
        self.play(Create(dip), Create(scarp))
        self.play(Write(dip_lab), Write(scarp_lab))
        self.wait(2)
        b5_l1 = Tex(r"Cuesta $\to$ homoclinal $\to$ hogsback:").scale(0.9).shift(band_shift(5) + DOWN * 1.0)
        b5_l2 = Tex(r"steeper tilt, more equal slopes").scale(0.9).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex(r"Granite: batholith domes peel — exfoliation;").scale(0.85).shift(band_shift(5) + DOWN * 2.5)
        b5_l4 = Tex(r"rotted joint blocks stack as tors — Paarl, Matobo").scale(0.85).shift(band_shift(5) + DOWN * 3.2)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): the four slope elements
        self.next_band(6)
        b6_title = Tex("The four slope elements").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        # Slope profile: crest curve approximated, cliff, talus, pediment lines.
        crest = Line(band_shift(6) + UP * 1.4 + LEFT * 4.4, band_shift(6) + UP * 1.2 + LEFT * 3.2)
        cliff = Line(band_shift(6) + UP * 1.2 + LEFT * 3.2, band_shift(6) + DOWN * 0.2 + LEFT * 3.0)
        talus = Line(band_shift(6) + DOWN * 0.2 + LEFT * 3.0, band_shift(6) + DOWN * 1.2 + LEFT * 0.8)
        pedi = Line(band_shift(6) + DOWN * 1.2 + LEFT * 0.8, band_shift(6) + DOWN * 1.7 + RIGHT * 4.2)
        self.play(Create(crest))
        self.play(Create(cliff))
        self.play(Create(talus))
        self.play(Create(pedi))
        self.wait(1.5)
        e1 = Tex("crest").scale(0.7).shift(band_shift(6) + UP * 1.9 + LEFT * 3.8)
        e2 = Tex("cliff / free face").scale(0.7).shift(band_shift(6) + UP * 0.5 + LEFT * 4.6)
        e3 = Tex("talus").scale(0.7).shift(band_shift(6) + DOWN * 0.3 + LEFT * 1.6)
        e4 = Tex("pediment").scale(0.7).shift(band_shift(6) + DOWN * 1.0 + RIGHT * 2.4)
        self.play(Write(e1), Write(e2))
        self.play(Write(e3), Write(e4))
        self.wait(2)
        b6_l1 = Tex(r"Talus rests at the angle loose rock can hold").scale(0.85).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex(r"Parallel retreat: cliff eats back, pediment widens").scale(0.85).shift(band_shift(6) + DOWN * 3.2)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): mass movement and contour signatures
        self.next_band(7)
        b7_title = Tex("Mass movement and the map").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"Creep (slow, dry) $\to$ flows (wet) $\to$ slides").scale(0.9).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex(r"and slumps $\to$ rockfall (fast, free)").scale(0.9).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex(r"Primers: steepness, WATER, undercut foot,").scale(0.9).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex(r"stripped vegetation, shaking").scale(0.9).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        # Contour signature: three concentric circles for a dome.
        ring1 = Circle(radius=0.4).shift(band_shift(7) + DOWN * 2.4 + LEFT * 3.0)
        ring2 = Circle(radius=0.7).shift(band_shift(7) + DOWN * 2.4 + LEFT * 3.0)
        ring3 = Circle(radius=1.0).shift(band_shift(7) + DOWN * 2.4 + LEFT * 3.0)
        self.play(Create(ring1), Create(ring2), Create(ring3))
        b7_l5 = Tex(r"Dome: smooth rings. Mesa: crowded ring,").scale(0.85).shift(band_shift(7) + DOWN * 2.1 + RIGHT * 2.2)
        b7_l6 = Tex(r"empty top. Cuesta: asymmetric spacing.").scale(0.85).shift(band_shift(7) + DOWN * 2.8 + RIGHT * 2.2)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(2)
        b7_l7 = Tex(r"Gradient: 100 m over 2 000 m $=$ 1 in 20").scale(0.9).shift(band_shift(7) + DOWN * 3.7)
        self.play(Write(b7_l7))
        self.play(Create(SurroundingRectangle(b7_l7, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): conveyor belts and the merry-go-round
        self.next_band(8)
        b8_title = Tex("Three conveyor belts, one merry-go-round").scale(1.0).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Hot air rises at the equator, sinks at 30$^\circ$ —").scale(0.9).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex(r"and sinking dry air parks the deserts there").scale(0.9).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex(r"The ball on the merry-go-round: paths curve —").scale(0.85).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex(r"LEFT down here: SE trades, SW winter gales").scale(0.85).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex(r"Summer: ITCZ south — Highveld thunderstorms").scale(0.85).shift(band_shift(8) + DOWN * 2.0)
        b8_l6 = Tex(r"Winter: Kalahari lid; fronts reach the Cape").scale(0.85).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_6): cake, books, loaf
        self.next_band(9)
        b9_title = Tex("Cake, books, loaf").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Rained-on cake: wide table, small table,").scale(0.9).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex(r"tall stump, cone — plateau, mesa, butte, cone").scale(0.85).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = Tex(r"Leaning books: cover $=$ dip, spine $=$ scarp;").scale(0.85).shift(band_shift(9) + DOWN * 0.4)
        b9_l4 = Tex(r"steeper tilt $\to$ more equal slopes").scale(0.85).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex(r"Fresh loaf: granite peels in curved crusts —").scale(0.85).shift(band_shift(9) + DOWN * 2.0)
        b9_l6 = Tex(r"domes, never steps; rotted blocks stack as tors").scale(0.85).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.wait(3)

        # --- Band 10 (subtopic_7): one walk down the hillside
        self.next_band(10)
        b10_title = Tex("One walk down the hillside").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Crest (rounded) $\to$ cliff (bare) $\to$").scale(0.9).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex(r"talus (angle of rest) $\to$ pediment (run-out)").scale(0.85).shift(band_shift(10) + UP * 0.5)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = Tex(r"Creep: leaning posts. Flows: soaked soil.").scale(0.85).shift(band_shift(10) + DOWN * 0.4)
        b10_l4 = Tex(r"Slides and slumps: undercut feet. Rockfall: free").scale(0.8).shift(band_shift(10) + DOWN * 1.1)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex(r"The trigger is nearly always water or us").scale(0.9).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l5))
        self.wait(2)
        b10_l6 = Tex(r"On the map: crowded cliff rings, even talus,").scale(0.85).shift(band_shift(10) + DOWN * 2.7)
        b10_l7 = Tex(r"widening pediment — walk it, read it, calculate it").scale(0.8).shift(band_shift(10) + DOWN * 3.4)
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.play(Create(SurroundingRectangle(b10_l7, color=GREEN)))
        self.wait(4)
