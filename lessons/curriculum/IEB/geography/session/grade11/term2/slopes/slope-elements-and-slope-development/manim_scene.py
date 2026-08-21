# Copyright (c) 2026 RokctAI
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from manim import *

# Band-layout whiteboard scene for the IEB Grade 11 Geography session duo
# "Slope Elements and Slope Development" (slopes).
# One band per teaching beat; the camera moves down, nothing is removed.
# Diagrams hand-built from Line/Arrow/Dot/Circle/Rectangle/Tex only.
# Subtopic shares follow subtopics.json: 220/230/235/240/185/190/210 of 1510 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SlopeElementsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the three-part stage
        title = Tex("Slope Elements and Slope Development").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex("Interior plateau: 1\\,200--1\\,800 m").scale(1.05).shift(UP * 1.0)
        s0_l2 = Tex("Great Escarpment: Drakensberg $>$ 3\\,000 m").scale(1.05).shift(UP * 0.2)
        s0_l3 = Tex("Marginal zone: Cape folds to east coast").scale(1.05).shift(DOWN * 0.6)
        self.play(Write(s0_l1))
        self.wait(2)
        self.play(Write(s0_l2))
        self.wait(2)
        self.play(Write(s0_l3))
        self.wait(2)
        s0_l4 = Tex("Rivers jump the rim: Tugela, near 950 m").scale(1.0).shift(DOWN * 1.6)
        self.play(Write(s0_l4))
        self.play(Create(SurroundingRectangle(s0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the profile stage + slope shapes
        self.next_band(1)
        b1_title = Tex("Plateau, rim, coast — then four shapes").scale(1.1).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        # country cross-section: high flat, steep drop, coastal step
        prof = VGroup(
            Line(LEFT * 6.0 + UP * 1.0, LEFT * 1.5 + UP * 1.0, color=YELLOW),
            Line(LEFT * 1.5 + UP * 1.0, RIGHT * 0.5 + DOWN * 1.4, color=RED),
            Line(RIGHT * 0.5 + DOWN * 1.4, RIGHT * 6.0 + DOWN * 1.8, color=BLUE),
        ).shift(band_shift(1))
        self.play(Create(prof[0]), Create(prof[1]), Create(prof[2]))
        p_lab = Tex("plateau").scale(0.8).shift(band_shift(1) + LEFT * 4.0 + UP * 1.6)
        e_lab = Tex("escarpment").scale(0.8).shift(band_shift(1) + LEFT * 0.2 + UP * 0.4)
        m_lab = Tex("marginal zone").scale(0.8).shift(band_shift(1) + RIGHT * 3.6 + DOWN * 1.0)
        self.play(Write(p_lab), Write(e_lab), Write(m_lab))
        self.wait(2.5)
        b1_l1 = Tex("Convex: rugby ball. Concave: skate ramp.").scale(0.95).shift(band_shift(1) + DOWN * 2.4)
        b1_l2 = Tex("Rectilinear: ruler. Compound: stacked.").scale(0.95).shift(band_shift(1) + DOWN * 3.2)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(3)

        # --- Band 2 (subtopic_2): the four elements drawn
        self.next_band(2)
        b2_title = Tex("Crest, cliff, talus, pediment").scale(1.15).shift(band_shift(2) + UP * 2.6)
        self.play(Write(b2_title))
        self.wait(1.5)
        base2 = Line(LEFT * 6.0 + DOWN * 2.2, RIGHT * 6.0 + DOWN * 2.2, color=WHITE).shift(band_shift(2))
        self.play(Create(base2))
        # profile: crest curve approximated by two lines, cliff, talus, pediment
        crest = VGroup(
            Line(LEFT * 5.4 + UP * 1.6, LEFT * 4.2 + UP * 1.4, color=YELLOW),
            Line(LEFT * 4.2 + UP * 1.4, LEFT * 3.4 + UP * 1.0, color=YELLOW),
        ).shift(band_shift(2))
        cliff = Line(LEFT * 3.4 + UP * 1.0, LEFT * 3.0 + DOWN * 0.4, color=RED).shift(band_shift(2))
        talus = Line(LEFT * 3.0 + DOWN * 0.4, LEFT * 0.6 + DOWN * 1.6, color=BLUE).shift(band_shift(2))
        pedi = VGroup(
            Line(LEFT * 0.6 + DOWN * 1.6, RIGHT * 2.4 + DOWN * 2.0, color=GREEN),
            Line(RIGHT * 2.4 + DOWN * 2.0, RIGHT * 5.6 + DOWN * 2.2, color=GREEN),
        ).shift(band_shift(2))
        self.play(Create(crest[0]), Create(crest[1]))
        self.play(Create(cliff))
        self.play(Create(talus))
        self.play(Create(pedi[0]), Create(pedi[1]))
        self.wait(1.5)
        c_lab = Tex("crest: convex").scale(0.75).shift(band_shift(2) + LEFT * 4.6 + UP * 2.2)
        f_lab = Tex("cliff: free face").scale(0.75).shift(band_shift(2) + LEFT * 1.6 + UP * 0.8)
        t_lab = Tex("talus: straight").scale(0.75).shift(band_shift(2) + LEFT * 0.8 + DOWN * 0.4)
        pd_lab = Tex("pediment: concave").scale(0.75).shift(band_shift(2) + RIGHT * 3.6 + DOWN * 1.3)
        self.play(Write(c_lab), Write(f_lab))
        self.play(Write(t_lab), Write(pd_lab))
        self.wait(3)

        # --- Band 3 (subtopic_2): each element's numbers
        self.next_band(3)
        b3_title = Tex("The numbers on the profile").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Free face: bare rock, near-vertical,").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l1b = Tex("loosened rock falls away at once").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.play(Write(b3_l1b))
        self.wait(2.5)
        b3_l2 = Tex(r"Talus: angle of repose, $\approx 25^\circ$--$35^\circ$").scale(1.0).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = Tex(r"Pediment: bedrock, $< 5^\circ$, thin veneer").scale(1.0).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("No resistant band: no cliff, no talus").scale(0.95).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): slope retreat — the machine
        self.next_band(4)
        b4_title = Tex("Slope retreat: the machine runs").scale(1.15).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        base4 = Line(LEFT * 6.0 + DOWN * 1.8, RIGHT * 6.0 + DOWN * 1.8, color=WHITE).shift(band_shift(4))
        self.play(Create(base4))
        # two profile positions marching left
        pr1 = VGroup(
            Line(RIGHT * 0.4 + UP * 1.2, RIGHT * 0.8 + DOWN * 0.2, color=BLUE),
            Line(RIGHT * 0.8 + DOWN * 0.2, RIGHT * 2.6 + DOWN * 1.8, color=BLUE),
        ).shift(band_shift(4))
        pr2 = VGroup(
            Line(LEFT * 2.2 + UP * 1.2, LEFT * 1.8 + DOWN * 0.2, color=RED),
            Line(LEFT * 1.8 + DOWN * 0.2, RIGHT * 0.0 + DOWN * 1.8, color=RED),
        ).shift(band_shift(4))
        cap4 = Line(LEFT * 6.0 + UP * 1.2, RIGHT * 0.4 + UP * 1.2, color=WHITE).shift(band_shift(4))
        self.play(Create(cap4))
        self.play(Create(pr1[0]), Create(pr1[1]))
        self.play(Create(pr2[0]), Create(pr2[1]))
        ret = Arrow(RIGHT * 1.6 + UP * 1.8, LEFT * 1.4 + UP * 1.8, color=RED, buff=0).shift(band_shift(4))
        ret_lab = Tex("same proportions, further back").scale(0.85).shift(band_shift(4) + RIGHT * 4.2 + UP * 1.8)
        self.play(Create(ret), Write(ret_lab))
        self.wait(2.5)
        b4_l1 = Tex("Cliff sheds, talus follows, pediment grows").scale(0.95).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l1))
        self.wait(3)

        # --- Band 5 (subtopic_3): retreat vs decline; people
        self.next_band(5)
        b5_title = Tex("Retreat or decline?").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("PARALLEL RETREAT: profile relocates,").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l1b = Tex("pediments merge into the PEDIPLAIN").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.play(Write(b5_l1b))
        self.wait(2.5)
        b5_l2 = Tex("DECLINE: humid, deep-soiled slopes").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        b5_l2b = Tex("lower and round with age").scale(1.0).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l2))
        self.play(Write(b5_l2b))
        self.wait(2.5)
        b5_l3 = Tex("Semi-arid, capped, sparse veld: SA retreats —").scale(0.9).shift(band_shift(5) + DOWN * 2.2)
        b5_l3b = Tex("farms on pediments, rockfall below cliffs").scale(0.9).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l3))
        self.play(Write(b5_l3b))
        self.play(Create(SurroundingRectangle(b5_l3b, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): resolution, two kinds
        self.next_band(6)
        b6_title = Tex("Resolution: spatial and spectral").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("SPATIAL: ground size of one pixel —").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l1b = Tex("30 m sees the school, not the minibus").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l1b))
        self.wait(2.5)
        b6_l2 = Tex("SPECTRAL: number and narrowness of bands —").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        b6_l2b = Tex("infrared tells stressed crops from veld").scale(0.95).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l2))
        self.play(Write(b6_l2b))
        self.wait(2.5)
        b6_l3 = Tex("Finer pixels, more bands: more information").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): vector and raster
        self.next_band(7)
        b7_title = Tex("Vector and raster").scale(1.15).shift(band_shift(7) + UP * 2.6)
        self.play(Write(b7_title))
        self.wait(1.5)
        # vector: point, line, polygon
        vp = Dot(LEFT * 4.6 + UP * 1.2).shift(band_shift(7))
        vl = Line(LEFT * 5.4 + UP * 0.2, LEFT * 3.4 + UP * 0.6, color=BLUE).shift(band_shift(7))
        va = Rectangle(width=1.8, height=1.1, color=GREEN).shift(band_shift(7) + LEFT * 4.4 + DOWN * 1.1)
        v_lab = Tex("vector: point, line, area $+$ attributes").scale(0.8).shift(band_shift(7) + LEFT * 3.4 + DOWN * 2.3)
        self.play(Create(vp), Create(vl), Create(va))
        self.play(Write(v_lab))
        self.wait(2.5)
        # raster: grid of cells
        r1 = Rectangle(width=0.8, height=0.8, color=YELLOW).shift(band_shift(7) + RIGHT * 2.2 + UP * 0.8)
        r2 = Rectangle(width=0.8, height=0.8, color=YELLOW).shift(band_shift(7) + RIGHT * 3.0 + UP * 0.8)
        r3 = Rectangle(width=0.8, height=0.8, color=YELLOW).shift(band_shift(7) + RIGHT * 2.2 + UP * 0.0)
        r4 = Rectangle(width=0.8, height=0.8, color=YELLOW).shift(band_shift(7) + RIGHT * 3.0 + UP * 0.0)
        r_lab = Tex("raster: grid, one value per cell").scale(0.8).shift(band_shift(7) + RIGHT * 3.0 + DOWN * 1.0)
        self.play(Create(r1), Create(r2), Create(r3), Create(r4))
        self.play(Write(r_lab))
        self.wait(2.5)
        b7_l1 = Tex("DEM in, slope map of a district out").scale(0.95).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(b7_l1))
        self.play(Create(SurroundingRectangle(b7_l1, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the wedding cake
        self.next_band(8)
        b8_title = Tex("The country is a wedding cake").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Cake top: plateau — Bloemfontein 1\\,400 m").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("Cake side: escarpment — Drakensberg wall").scale(0.95).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex("Table: coastal belt, wrinkled at the Cape").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("Shapes: rugby ball, skate ramp, ruler —").scale(0.95).shift(band_shift(8) + DOWN * 1.4)
        b8_l4b = Tex("real hills stack them in one order").scale(0.95).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_l4))
        self.play(Write(b8_l4b))
        self.play(Create(SurroundingRectangle(b8_l4b, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): roof, wall, stands, pitch
        self.next_band(9)
        b9_title = Tex("Roof, wall, stands, pitch").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Roof: crest, convex, slowly rounding").scale(0.95).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("Wall: cliff, free face — drops its rock").scale(0.95).shift(band_shift(9) + UP * 0.4)
        b9_l3 = Tex(r"Stands: talus at repose, $25^\circ$--$35^\circ$").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        b9_l4 = Tex(r"Pitch: pediment, concave, $< 5^\circ$").scale(0.95).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("Soft hill: no wall, no stands —").scale(0.95).shift(band_shift(9) + DOWN * 2.1)
        b9_l5b = Tex("just roof curving into pitch").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l5))
        self.play(Write(b9_l5b))
        self.play(Create(SurroundingRectangle(b9_l5b, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the walking hill and the chessboard
        self.next_band(10)
        b10_title = Tex("The walking hill, the chessboard map").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Wall rebuilt backward, stands follow,").scale(0.95).shift(band_shift(10) + UP * 1.2)
        b10_l1b = Tex("pitch stretches — shape never sags").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l1b))
        self.wait(2.5)
        b10_l2 = Tex("Pitches merge: pediplain with koppies").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2)
        b10_l3 = Tex("Vector: pins, string, patches $+$ fact cards").scale(0.95).shift(band_shift(10) + DOWN * 1.4)
        b10_l3b = Tex("Raster: chessboard, one value per square").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10_l3))
        self.play(Write(b10_l3b))
        self.wait(2.5)
        b10_l4 = Tex("Heights in, steepness out — in seconds").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(4)
