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

# Band-layout whiteboard scene for the CAPS Grade 11 Geography session duo
# "Batholiths, Granite Domes and Tors" (massive igneous rocks).
# One band per teaching beat; the camera moves down, nothing is removed.
# Diagrams hand-built from Line/Arrow/Dot/Circle/Rectangle/Tex only.
# Subtopic shares follow subtopics.json: 220/230/230/240/185/185/210 of 1500 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BatholithsDomesTorsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): intrusive rock and the key test
        title = Tex("Batholiths, Granite Domes and Tors").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex("Magma stuck underground cools slowly:").scale(1.05).shift(UP * 1.0)
        s0_l2 = Tex("coarse-grained granite or dolerite").scale(1.05).shift(UP * 0.2)
        self.play(Write(s0_l1))
        self.play(Write(s0_l2))
        self.wait(2.5)
        s0_l3 = Tex("CONCORDANT: lies WITH the strata").scale(1.1).shift(DOWN * 0.8)
        s0_l4 = Tex("DISCORDANT: CUTS across the strata").scale(1.1).shift(DOWN * 1.7)
        self.play(Write(s0_l3))
        self.wait(2)
        self.play(Write(s0_l4))
        self.play(Create(SurroundingRectangle(VGroup(s0_l3, s0_l4), color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the family drawn in cross-section
        self.next_band(1)
        b1_title = Tex("The intrusion family").scale(1.15).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        # country rock strata: three horizontal lines
        strat = VGroup(
            Line(LEFT * 6.0 + UP * 1.4, RIGHT * 6.0 + UP * 1.4, color=GREY),
            Line(LEFT * 6.0 + UP * 0.6, RIGHT * 6.0 + UP * 0.6, color=GREY),
            Line(LEFT * 6.0 + DOWN * 0.2, RIGHT * 6.0 + DOWN * 0.2, color=GREY),
        ).shift(band_shift(1))
        self.play(Create(strat[0]), Create(strat[1]), Create(strat[2]))
        self.wait(1.5)
        # batholith: huge dome from below (2-line chain)
        bath = VGroup(
            Line(LEFT * 5.6 + DOWN * 2.6, LEFT * 4.0 + UP * 0.2, color=RED),
            Line(LEFT * 4.0 + UP * 0.2, LEFT * 2.4 + DOWN * 2.6, color=RED),
        ).shift(band_shift(1))
        bath_lab = Tex("batholith: no floor, discordant").scale(0.8).shift(band_shift(1) + LEFT * 3.9 + DOWN * 3.0)
        self.play(Create(bath[0]), Create(bath[1]), Write(bath_lab))
        self.wait(2)
        # laccolith: blister between strata
        lac = VGroup(
            Line(LEFT * 1.2 + UP * 0.6, LEFT * 0.2 + UP * 1.2, color=RED),
            Line(LEFT * 0.2 + UP * 1.2, RIGHT * 0.8 + UP * 0.6, color=RED),
        ).shift(band_shift(1))
        lac_lab = Tex("laccolith: domed roof").scale(0.8).shift(band_shift(1) + LEFT * 0.2 + UP * 1.9)
        self.play(Create(lac[0]), Create(lac[1]), Write(lac_lab))
        self.wait(2)
        # dyke: vertical wall
        dyke = VGroup(
            Line(RIGHT * 2.2 + DOWN * 2.6, RIGHT * 2.2 + UP * 1.4, color=RED),
            Line(RIGHT * 2.6 + DOWN * 2.6, RIGHT * 2.6 + UP * 1.4, color=RED),
        ).shift(band_shift(1))
        dyke_lab = Tex("dyke: cuts across").scale(0.8).shift(band_shift(1) + RIGHT * 2.4 + UP * 2.0)
        self.play(Create(dyke[0]), Create(dyke[1]), Write(dyke_lab))
        self.wait(2)
        # sill: horizontal sheet between strata
        sill = Rectangle(width=2.4, height=0.3, color=RED).shift(band_shift(1) + RIGHT * 4.6 + UP * 0.2)
        sill_lab = Tex("sill: between strata").scale(0.8).shift(band_shift(1) + RIGHT * 4.5 + DOWN * 0.6)
        self.play(Create(sill), Write(sill_lab))
        self.wait(2)
        b1_l1 = Tex("Lopolith: sagged saucer — Bushveld").scale(0.9).shift(band_shift(1) + RIGHT * 2.8 + DOWN * 3.0)
        self.play(Write(b1_l1))
        self.wait(3)

        # --- Band 2 (subtopic_2): exposure — the big bodies
        self.next_band(2)
        b2_title = Tex("Stripped cover, resistant survivor").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Two steps: erosion strips the cover;").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l1b = Tex("hard granite resists and stands").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.play(Write(b2_l1b))
        self.wait(2.5)
        b2_l2 = Tex("Batholith: granite dome mountains —").scale(0.95).shift(band_shift(2) + DOWN * 0.5)
        b2_l2b = Tex("Paarl's three domes over the Berg valley").scale(0.95).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(b2_l2))
        self.play(Write(b2_l2b))
        self.wait(2.5)
        b2_l3 = Tex("Laccolith: granite-cored dome hill").scale(0.95).shift(band_shift(2) + DOWN * 2.1)
        b2_l4 = Tex("Lopolith: broad basin — platinum mines").scale(0.95).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): exposure — the sheets
        self.next_band(3)
        b3_title = Tex("Dykes and sills at the surface").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Resistant dyke: straight wall-like ridge").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("Softer dyke: a straight trench").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("Sill: cliff band at one level, mesa cap,").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        b3_l3b = Tex("or a waterfall lip — the Tugela").scale(0.95).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_l3))
        self.play(Write(b3_l3b))
        self.wait(2.5)
        b3_l4 = Tex("Map: dyke $=$ dead-straight dark ridge;").scale(0.95).shift(band_shift(3) + DOWN * 2.2)
        b3_l4b = Tex("sill $=$ contour-hugging cliff line").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l4))
        self.play(Write(b3_l4b))
        self.play(Create(SurroundingRectangle(b3_l4b, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): pressure release and sheet joints
        self.next_band(4)
        b4_title = Tex("Pressure release: the rock unloads").scale(1.15).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Granite set under kilometres of weight;").scale(0.95).shift(band_shift(4) + UP * 1.7)
        b4_l2 = Tex("erosion removes it — granite expands").scale(0.95).shift(band_shift(4) + UP * 0.9)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        # dome with sheet joints: nested 3-segment arcs
        base4 = Line(LEFT * 5.0 + DOWN * 2.2, RIGHT * 5.0 + DOWN * 2.2, color=WHITE).shift(band_shift(4))
        outer = VGroup(
            Line(LEFT * 3.4 + DOWN * 2.2, LEFT * 1.6 + DOWN * 0.2, color=RED),
            Line(LEFT * 1.6 + DOWN * 0.2, RIGHT * 0.4 + DOWN * 0.1, color=RED),
            Line(RIGHT * 0.4 + DOWN * 0.1, RIGHT * 2.6 + DOWN * 2.2, color=RED),
        ).shift(band_shift(4))
        inner = VGroup(
            Line(LEFT * 2.6 + DOWN * 2.2, LEFT * 1.2 + DOWN * 0.8, color=YELLOW),
            Line(LEFT * 1.2 + DOWN * 0.8, RIGHT * 0.2 + DOWN * 0.7, color=YELLOW),
            Line(RIGHT * 0.2 + DOWN * 0.7, RIGHT * 1.8 + DOWN * 2.2, color=YELLOW),
        ).shift(band_shift(4))
        self.play(Create(base4))
        self.play(Create(outer[0]), Create(outer[1]), Create(outer[2]))
        self.play(Create(inner[0]), Create(inner[1]), Create(inner[2]))
        sheet_lab = Tex("curved sheet joints, onion layers").scale(0.85).shift(band_shift(4) + RIGHT * 3.6 + DOWN * 0.6)
        self.play(Write(sheet_lab))
        self.wait(2.5)
        b4_l3 = Tex("Physical weathering by removed WEIGHT,").scale(0.9).shift(band_shift(4) + DOWN * 2.9 + LEFT * 1.0)
        self.play(Write(b4_l3))
        self.wait(3)

        # --- Band 5 (subtopic_3): exfoliation perfects the dome
        self.next_band(5)
        b5_title = Tex("Exfoliation: peeling into a dome").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Water and temperature work the joints;").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("outer sheets loosen, slide off in slabs").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Each shed sheet leaves the surface").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex("MORE rounded — the dome perfects itself").scale(1.0).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2.5)
        b5_l5 = Tex("Isolated dome on a pediplain: BORNHARDT").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        b5_l6 = Tex("Paarl Rock; the Matopos whalebacks").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l5))
        self.wait(2)
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): tors stage one — underground rotting
        self.next_band(6)
        b6_title = Tex("Tors, stage 1: rotting underground").scale(1.1).shift(band_shift(6) + UP * 2.6)
        self.play(Write(b6_title))
        self.wait(1.5)
        # jointed granite brickwork: grid of rectangles
        blocks = VGroup(
            Rectangle(width=1.3, height=1.0, color=GREY).shift(LEFT * 4.2 + UP * 0.8),
            Rectangle(width=1.3, height=1.0, color=GREY).shift(LEFT * 2.9 + UP * 0.8),
            Rectangle(width=1.3, height=1.0, color=GREY).shift(LEFT * 4.2 + DOWN * 0.2),
            Rectangle(width=1.3, height=1.0, color=GREY).shift(LEFT * 2.9 + DOWN * 0.2),
        ).shift(band_shift(6))
        self.play(Create(blocks[0]), Create(blocks[1]), Create(blocks[2]), Create(blocks[3]))
        j_lab = Tex("joints: natural brickwork").scale(0.85).shift(band_shift(6) + LEFT * 3.5 + DOWN * 1.2)
        self.play(Write(j_lab))
        self.wait(2)
        # corestones: circles inside blocks
        core1 = Circle(radius=0.42, color=YELLOW).shift(band_shift(6) + RIGHT * 2.6 + UP * 0.8)
        core2 = Circle(radius=0.42, color=YELLOW).shift(band_shift(6) + RIGHT * 3.9 + UP * 0.8)
        core3 = Circle(radius=0.42, color=YELLOW).shift(band_shift(6) + RIGHT * 3.2 + DOWN * 0.2)
        c_lab = Tex("corners rot fastest: round CORESTONES").scale(0.85).shift(band_shift(6) + RIGHT * 3.2 + DOWN * 1.2)
        self.play(Create(core1), Create(core2), Create(core3))
        self.play(Write(c_lab))
        self.wait(2.5)
        b6_l1 = Tex("Water creeps along joints; rock rots").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        b6_l2 = Tex("outward-in, leaving crumbly GRUS").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(3)

        # --- Band 7 (subtopic_4): stage two and the spacing rule
        self.next_band(7)
        b7_title = Tex("Tors, stage 2: the great unveiling").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Erosion strips the grus; corestones").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l1b = Tex("stand stacked in their joint positions").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l1b))
        self.wait(2.5)
        b7_l2 = Tex("Order earns the marks: rot FIRST,").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l2b = Tex("underground; strip SECOND, in the open").scale(1.0).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(b7_l2))
        self.play(Write(b7_l2b))
        self.play(Create(SurroundingRectangle(b7_l2b, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex("Joints wide apart: dome; close: tor").scale(1.0).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        b7_l4 = Tex("Johannesburg Dome, Magoebaskloof, Paarl").scale(0.9).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the dough that never surfaced
        self.next_band(8)
        b8_title = Tex("The dough that never reached the surface").scale(1.05).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Batholith: the whole sack — no bottom").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("Laccolith: bun that puffed the ceiling").scale(0.95).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex("Lopolith: heavy saucer — the Bushveld,").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        b8_l3b = Tex("filled with platinum, not custard").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.play(Write(b8_l3b))
        self.wait(2.5)
        b8_l4 = Tex("Dyke: wall up a crack; sill: shelf").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Lies with $=$ concordant; cuts $=$ discordant").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): peeling the onion mountain
        self.next_band(9)
        b9_title = Tex("Peeling the onion mountain").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Squashed passenger freed: erosion").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l1b = Tex("unloads the taxi, granite breathes out").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1))
        self.play(Write(b9_l1b))
        self.wait(2.5)
        b9_l2 = Tex("Swelling cracks it in onion shells;").scale(1.0).shift(band_shift(9) + DOWN * 0.5)
        b9_l2b = Tex("outer shells slide off in slabs").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l2))
        self.play(Write(b9_l2b))
        self.wait(2.5)
        b9_l3 = Tex("Curved shells shed into curves: the").scale(1.0).shift(band_shift(9) + DOWN * 2.2)
        b9_l3b = Tex("dome polishes itself rounder — Paarl").scale(1.0).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l3))
        self.play(Write(b9_l3b))
        self.play(Create(SurroundingRectangle(b9_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the sugar-cube trick
        self.next_band(10)
        b10_title = Tex("The sugar-cube trick behind every tor").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Tea seeps between stacked cubes:").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l1b = Tex("corners hit from 3 sides melt first").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l1b))
        self.wait(2.5)
        b10_l2 = Tex("Underground: blocks round into").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        b10_l2b = Tex("corestones wrapped in crumbly grus").scale(1.0).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l2))
        self.play(Write(b10_l2b))
        self.wait(2.5)
        b10_l3 = Tex("Unveiling: grus washes away, survivors").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        b10_l3b = Tex("stand stacked — rot first, strip second").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l3))
        self.play(Write(b10_l3b))
        self.play(Create(SurroundingRectangle(b10_l3b, color=GREEN)))
        self.wait(4)
