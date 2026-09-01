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
# "Karoo Landscapes — Mesas and Buttes" (horizontally layered rocks).
# One band per teaching beat; camera moves down, nothing is removed.
# Diagrams hand-built from Line/Arrow/Dot/Circle/Rectangle/Tex only.
# Subtopic shares follow subtopics.json: 220/230/225/245/180/185/210 of 1495 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class KarooMesasButtesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): strata and differential erosion
        title = Tex("Karoo Landscapes: Mesas and Buttes").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex("STRATA: layers laid flat, undisturbed").scale(1.1).shift(UP * 1.0)
        self.play(Write(s0_l1))
        self.wait(2)
        s0_l2 = Tex("Karoo Supergroup: shale, mudstone,").scale(1.05).shift(UP * 0.2)
        s0_l3 = Tex("sandstone — plus hard DOLERITE sills").scale(1.05).shift(DOWN * 0.6)
        self.play(Write(s0_l2))
        self.play(Write(s0_l3))
        self.wait(2.5)
        s0_l4 = Tex("Soft strips fast, hard survives:").scale(1.1).shift(DOWN * 1.6)
        s0_l5 = Tex("DIFFERENTIAL EROSION").scale(1.15).shift(DOWN * 2.5)
        self.play(Write(s0_l4))
        self.play(Write(s0_l5))
        self.play(Create(SurroundingRectangle(s0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the cap-rock stack
        self.next_band(1)
        b1_title = Tex("The cap rock is a hard hat").scale(1.15).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        # layer stack: dolerite cap over soft layers
        cap = Rectangle(width=5.0, height=0.6, color=RED).shift(band_shift(1) + UP * 1.3)
        cap_lab = Tex("dolerite sill (cap)").scale(0.85).shift(band_shift(1) + RIGHT * 4.4 + UP * 1.3)
        soft1 = Rectangle(width=5.0, height=0.8, color=BLUE).shift(band_shift(1) + DOWN * 0.1)
        soft1_lab = Tex("soft shale").scale(0.85).shift(band_shift(1) + RIGHT * 3.9 + DOWN * 0.1)
        soft2 = Rectangle(width=5.0, height=0.8, color=BLUE).shift(band_shift(1) + DOWN * 0.9)
        soft2_lab = Tex("mudstone").scale(0.85).shift(band_shift(1) + RIGHT * 3.9 + DOWN * 0.9)
        self.play(Create(cap), Write(cap_lab))
        self.wait(2)
        self.play(Create(soft1), Write(soft1_lab))
        self.play(Create(soft2), Write(soft2_lab))
        self.wait(2)
        b1_l1 = Tex("Cap intact: flat top, steep sides").scale(1.0).shift(band_shift(1) + DOWN * 1.9)
        b1_l2 = Tex("Cap breached: soft rock gutted").scale(1.0).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Drakensberg: stacked basalt, same trick").scale(0.95).shift(band_shift(1) + UP * 2.0 + LEFT * 0.0)
        self.play(Write(b1_l3))
        self.wait(3)

        # --- Band 2 (subtopic_2): the landform family in profile
        self.next_band(2)
        b2_title = Tex("Plateau, mesa, butte, conical hill").scale(1.15).shift(band_shift(2) + UP * 2.6)
        self.play(Write(b2_title))
        self.wait(1.5)
        base2 = Line(LEFT * 6.2 + DOWN * 1.6, RIGHT * 6.2 + DOWN * 1.6, color=WHITE).shift(band_shift(2))
        self.play(Create(base2))
        # plateau: wide flat top with steep edge
        plat = VGroup(
            Line(LEFT * 6.2 + UP * 0.9, LEFT * 4.0 + UP * 0.9, color=YELLOW),
            Line(LEFT * 4.0 + UP * 0.9, LEFT * 3.6 + DOWN * 1.6, color=YELLOW),
        ).shift(band_shift(2))
        plat_lab = Tex("plateau").scale(0.8).shift(band_shift(2) + LEFT * 5.3 + UP * 1.5)
        self.play(Create(plat[0]), Create(plat[1]), Write(plat_lab))
        self.wait(2)
        # mesa: wide flat block
        mesa = VGroup(
            Line(LEFT * 2.6 + DOWN * 1.6, LEFT * 2.3 + UP * 0.7, color=YELLOW),
            Line(LEFT * 2.3 + UP * 0.7, LEFT * 0.3 + UP * 0.7, color=YELLOW),
            Line(LEFT * 0.3 + UP * 0.7, DOWN * 1.6 + LEFT * 0.0, color=YELLOW),
        ).shift(band_shift(2))
        mesa_lab = Tex("mesa: wider than high").scale(0.8).shift(band_shift(2) + LEFT * 1.3 + UP * 1.4)
        self.play(Create(mesa[0]), Create(mesa[1]), Create(mesa[2]), Write(mesa_lab))
        self.wait(2)
        # butte: narrow tall block
        butte = VGroup(
            Line(RIGHT * 1.4 + DOWN * 1.6, RIGHT * 1.6 + UP * 0.9, color=YELLOW),
            Line(RIGHT * 1.6 + UP * 0.9, RIGHT * 2.2 + UP * 0.9, color=YELLOW),
            Line(RIGHT * 2.2 + UP * 0.9, RIGHT * 2.4 + DOWN * 1.6, color=YELLOW),
        ).shift(band_shift(2))
        butte_lab = Tex("butte: higher than wide").scale(0.8).shift(band_shift(2) + RIGHT * 2.0 + UP * 1.6)
        self.play(Create(butte[0]), Create(butte[1]), Create(butte[2]), Write(butte_lab))
        self.wait(2)
        # conical hill
        cone = VGroup(
            Line(RIGHT * 3.6 + DOWN * 1.6, RIGHT * 4.5 + UP * 0.4, color=YELLOW),
            Line(RIGHT * 4.5 + UP * 0.4, RIGHT * 5.4 + DOWN * 1.6, color=YELLOW),
        ).shift(band_shift(2))
        cone_lab = Tex("conical hill").scale(0.8).shift(band_shift(2) + RIGHT * 4.5 + UP * 1.0)
        self.play(Create(cone[0]), Create(cone[1]), Write(cone_lab))
        self.wait(2)
        b2_l1 = Tex("Three Sisters, N1: dolerite-capped buttes").scale(0.95).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l1))
        self.wait(3)

        # --- Band 3 (subtopic_2): the five-age sequence
        self.next_band(3)
        b3_title = Tex("One family at five ages").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("plateau (escarpment edge)").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex(r"$\rightarrow$ mesa (tafelberg, table)").scale(1.05).shift(band_shift(3) + UP * 0.3)
        b3_l3 = Tex(r"$\rightarrow$ butte (summit now small)").scale(1.05).shift(band_shift(3) + DOWN * 0.5)
        b3_l4 = Tex(r"$\rightarrow$ conical hill (cap breached)").scale(1.05).shift(band_shift(3) + DOWN * 1.3)
        b3_l5 = Tex(r"$\rightarrow$ plain").scale(1.05).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l1))
        self.wait(1.5)
        self.play(Write(b3_l2))
        self.wait(1.5)
        self.play(Write(b3_l3))
        self.wait(1.5)
        self.play(Write(b3_l4))
        self.wait(1.5)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(VGroup(b3_l1, b3_l5), color=GREEN)))
        self.wait(2)
        b3_l6 = Tex("Sheep, solar, road stone, fossils, tourism").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): scarp retreat drawn
        self.next_band(4)
        b4_title = Tex("Scarp retreat: parallel, backwards").scale(1.15).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        base4 = Line(LEFT * 6.0 + DOWN * 1.6, RIGHT * 6.0 + DOWN * 1.6, color=WHITE).shift(band_shift(4))
        self.play(Create(base4))
        # three cliff positions, same angle, marching right
        c1 = VGroup(
            Line(LEFT * 4.6 + UP * 1.0, LEFT * 3.9 + DOWN * 0.2, color=BLUE),
            Line(LEFT * 3.9 + DOWN * 0.2, LEFT * 2.2 + DOWN * 1.6, color=BLUE),
        ).shift(band_shift(4))
        c2 = VGroup(
            Line(LEFT * 2.6 + UP * 1.0, LEFT * 1.9 + DOWN * 0.2, color=YELLOW),
            Line(LEFT * 1.9 + DOWN * 0.2, LEFT * 0.2 + DOWN * 1.6, color=YELLOW),
        ).shift(band_shift(4))
        c3 = VGroup(
            Line(LEFT * 0.6 + UP * 1.0, RIGHT * 0.1 + DOWN * 0.2, color=RED),
            Line(RIGHT * 0.1 + DOWN * 0.2, RIGHT * 1.8 + DOWN * 1.6, color=RED),
        ).shift(band_shift(4))
        cap4 = Line(LEFT * 6.0 + UP * 1.0, LEFT * 0.6 + UP * 1.0, color=WHITE).shift(band_shift(4))
        self.play(Create(cap4))
        self.play(Create(c1[0]), Create(c1[1]))
        self.play(Create(c2[0]), Create(c2[1]))
        self.play(Create(c3[0]), Create(c3[1]))
        retreat = Arrow(RIGHT * 1.2 + UP * 1.6, LEFT * 2.6 + UP * 1.6, color=RED, buff=0).shift(band_shift(4))
        r_lab = Tex("same angle, further back").scale(0.85).shift(band_shift(4) + RIGHT * 4.2 + UP * 1.6)
        self.play(Create(retreat), Write(r_lab))
        self.wait(2.5)
        ped_lab = Tex("pediment: rock floor left at the foot").scale(0.9).shift(band_shift(4) + RIGHT * 2.4 + DOWN * 2.3)
        self.play(Write(ped_lab))
        self.wait(2)
        b4_l1 = Tex("Frost wedges the cap; storms gut the shale").scale(0.9).shift(band_shift(4) + DOWN * 3.0 + LEFT * 1.0)
        self.play(Write(b4_l1))
        self.wait(3)

        # --- Band 5 (subtopic_3): back wasting vs down wasting; pediplain
        self.next_band(5)
        b5_title = Tex("Back wasting vs down wasting").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("BACK WASTING: slopes retreat sideways,").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l1b = Tex("keeping their shape — cap holds the top").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.play(Write(b5_l1b))
        self.wait(2.5)
        b5_l2 = Tex("DOWN WASTING: lowered from the top,").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        b5_l2b = Tex("profile flattens and softens").scale(1.0).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l2))
        self.play(Write(b5_l2b))
        self.wait(2.5)
        b5_l3 = Tex("Pediments merge: PEDIPLAIN — the Karoo,").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        b5_l3b = Tex("studded with flat-topped survivors").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l3))
        self.play(Write(b5_l3b))
        self.play(Create(SurroundingRectangle(b5_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): canyons and contour signatures
        self.next_band(6)
        b6_title = Tex("Canyons and the contour signature").scale(1.15).shift(band_shift(6) + UP * 2.6)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("River cuts DOWN: stepped vertical walls").scale(1.0).shift(band_shift(6) + UP * 1.7)
        b6_l2 = Tex("Fish River, Blyde River, Oribi Gorge").scale(1.0).shift(band_shift(6) + UP * 0.9)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        # contour signature of a mesa: nested lines with empty summit
        r_out = Rectangle(width=4.6, height=2.2, color=BLUE).shift(band_shift(6) + LEFT * 3.0 + DOWN * 1.3)
        r_mid = Rectangle(width=4.0, height=1.7, color=BLUE).shift(band_shift(6) + LEFT * 3.0 + DOWN * 1.3)
        r_in = Rectangle(width=3.4, height=1.2, color=BLUE).shift(band_shift(6) + LEFT * 3.0 + DOWN * 1.3)
        m_lab = Tex("crowded ring, wide empty top").scale(0.8).shift(band_shift(6) + LEFT * 3.0 + DOWN * 2.9)
        self.play(Create(r_out), Create(r_mid), Create(r_in))
        self.play(Write(m_lab))
        self.wait(2.5)
        # canyon: paired crowded contours with river between
        can = VGroup(
            Line(RIGHT * 1.6 + DOWN * 0.4, RIGHT * 5.6 + DOWN * 0.4, color=BLUE),
            Line(RIGHT * 1.6 + DOWN * 0.7, RIGHT * 5.6 + DOWN * 0.7, color=BLUE),
            Line(RIGHT * 1.6 + DOWN * 1.3, RIGHT * 5.6 + DOWN * 1.3, color=WHITE),
            Line(RIGHT * 1.6 + DOWN * 1.9, RIGHT * 5.6 + DOWN * 1.9, color=BLUE),
            Line(RIGHT * 1.6 + DOWN * 2.2, RIGHT * 5.6 + DOWN * 2.2, color=BLUE),
        ).shift(band_shift(6))
        c_lab = Tex("paired walls, river pinched").scale(0.8).shift(band_shift(6) + RIGHT * 3.6 + DOWN * 2.9)
        self.play(Create(can[0]), Create(can[1]), Create(can[2]), Create(can[3]), Create(can[4]))
        self.play(Write(c_lab))
        self.wait(3)

        # --- Band 7 (subtopic_4): the two calculations
        self.next_band(7)
        b7_title = Tex("Vertical exaggeration and gradient").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"\text{VE} = \frac{\text{vertical scale}}{\text{horizontal scale}}").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"= \frac{1/2\,000}{1/50\,000} = \frac{50\,000}{2\,000}").scale(1.05).shift(band_shift(7) + UP * 0.0)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = MathTex(r"= 25 \text{ times}").scale(1.1).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        b7_l4 = MathTex(r"\text{Gradient} = \frac{200\text{ m}}{1\,000\text{ m}}").scale(1.05).shift(band_shift(7) + DOWN * 1.9)
        b7_l5 = MathTex(r"= 1:5").scale(1.15).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(b7_l4))
        self.wait(2)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the layer cake with icing
        self.next_band(8)
        b8_title = Tex("The layer cake with icing").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Sponge $=$ shale and mudstone (soft)").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("Icing $=$ dolerite, set rock-hard").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("Weather eats sponge first, every time").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("Icing holds: flat top survives").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        b8_l5 = Tex("Icing cracked: cake gutted below").scale(1.0).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_l4))
        self.wait(2)
        self.play(Write(b8_l5))
        self.wait(2)
        b8_l6 = Tex("Drakensberg: lava icing, tallest wall").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_6): table, stool, traffic cone
        self.next_band(9)
        b9_title = Tex("Table, stool, traffic cone").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Whole slab: plateau — table-land").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("Cut-off chunk, still wide: mesa — table").scale(1.0).shift(band_shift(9) + UP * 0.4)
        b9_l3 = Tex("Taller than wide: butte — bar stool").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        b9_l4 = Tex("Hard hat gone: conical hill — cone").scale(1.0).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("Countdown: table-land, table, stool,").scale(1.0).shift(band_shift(9) + DOWN * 2.1)
        b9_l5b = Tex("cone, flat — all five in one Karoo view").scale(1.0).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l5))
        self.play(Write(b9_l5b))
        self.play(Create(SurroundingRectangle(b9_l5b, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the cliff that marches backwards
        self.next_band(10)
        b10_title = Tex("The cliff that marches backwards").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Hills do NOT slump round — the cliff").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l1b = Tex("retreats at the same steepness").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l1b))
        self.wait(2.5)
        b10_l2 = Tex("Winter frost levers blocks; summer").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        b10_l2b = Tex("storms undermine — rebuilt further back").scale(0.95).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l2))
        self.play(Write(b10_l2b))
        self.wait(2.5)
        b10_l3 = Tex("Apron left behind: pediment; aprons").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        b10_l3b = Tex("merge into the pediplain — the Karoo").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l3))
        self.play(Write(b10_l3b))
        self.play(Create(SurroundingRectangle(b10_l3b, color=GREEN)))
        self.wait(4)
