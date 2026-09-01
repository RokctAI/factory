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

# Band-layout whiteboard scene for the meanders / oxbow lakes /
# longitudinal profiles duo lesson. Exporter-safe primitives only
# (Tex/Line/Arrow/Dot/Circle/Rectangle/VGroup); add-only lifecycle;
# camera moves down one frame-height per band. Profiles and meander
# bends are hand-built from Line chains, Arrows and Dots, assembled
# element by element in script order.
#
# Subtopic shares (subtopics.json, total 1500 s):
# 240/230/230/235 expert, 200/185/180 simplifier. Bands 0-7 = Part 1
# (two per expert subtopic), bands 8-10 = fresh Part 2 bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MeandersOxbowProfilesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the graded longitudinal profile ---
        title = Tex("The Longitudinal Profile").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d0 = Tex(r"Side view of a river, source to mouth").scale(1.0).shift(UP * 1.5)
        self.play(Write(d0))
        self.wait(2)
        # Graded curve: concave sweep built from line segments
        g1 = Line(LEFT * 5.2 + UP * 0.6, LEFT * 3.2 + DOWN * 0.9, color=BLUE, stroke_width=5)
        g2 = Line(LEFT * 3.2 + DOWN * 0.9, LEFT * 0.6 + DOWN * 1.8, color=BLUE, stroke_width=5)
        g3 = Line(LEFT * 0.6 + DOWN * 1.8, RIGHT * 2.4 + DOWN * 2.3, color=BLUE, stroke_width=5)
        g4 = Line(RIGHT * 2.4 + DOWN * 2.3, RIGHT * 5.2 + DOWN * 2.5, color=BLUE, stroke_width=5)
        src = Tex(r"source").scale(0.8).shift(LEFT * 5.2 + UP * 1.1)
        mth = Tex(r"mouth").scale(0.8).shift(RIGHT * 5.2 + DOWN * 2.0)
        self.play(Write(src))
        self.play(Create(g1), Create(g2))
        self.play(Create(g3), Create(g4))
        self.play(Write(mth))
        self.wait(2)
        lab = Tex(r"GRADED: smooth, concave, no steps").scale(0.95).shift(DOWN * 3.1)
        self.play(Write(lab))
        self.play(Create(SurroundingRectangle(lab, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): ungraded profile + base levels ---
        self.next_band(1)
        b1_t = Tex("Ungraded: steps and stalls").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        # Ungraded curve with a waterfall step and a ponded flat
        u1 = Line(band_shift(1) + LEFT * 5.2 + UP * 1.0, band_shift(1) + LEFT * 3.0 + UP * 0.2, color=BLUE, stroke_width=5)
        u2 = Line(band_shift(1) + LEFT * 3.0 + UP * 0.2, band_shift(1) + LEFT * 3.0 + DOWN * 1.0, color=BLUE, stroke_width=5)
        u3 = Line(band_shift(1) + LEFT * 3.0 + DOWN * 1.0, band_shift(1) + LEFT * 0.4 + DOWN * 1.3, color=BLUE, stroke_width=5)
        u4 = Line(band_shift(1) + LEFT * 0.4 + DOWN * 1.3, band_shift(1) + RIGHT * 1.8 + DOWN * 1.3, color=BLUE, stroke_width=5)
        u5 = Line(band_shift(1) + RIGHT * 1.8 + DOWN * 1.3, band_shift(1) + RIGHT * 5.0 + DOWN * 2.3, color=BLUE, stroke_width=5)
        wf = Tex(r"waterfall (resistant rock)").scale(0.8).shift(band_shift(1) + LEFT * 2.6 + UP * 0.9)
        dm = Tex(r"reservoir: temporary base level").scale(0.8).shift(band_shift(1) + RIGHT * 0.7 + DOWN * 0.5)
        self.play(Create(u1), Create(u2))
        self.play(Write(wf))
        self.wait(2)
        self.play(Create(u3), Create(u4))
        self.play(Write(dm))
        self.wait(2)
        self.play(Create(u5))
        sea = Line(band_shift(1) + LEFT * 5.4 + DOWN * 2.3, band_shift(1) + RIGHT * 5.4 + DOWN * 2.3,
                   color=YELLOW, stroke_width=3)
        sea_lab = Tex(r"sea = PERMANENT base level").scale(0.85).shift(band_shift(1) + DOWN * 2.9)
        self.play(Create(sea))
        self.play(Write(sea_lab))
        self.play(Create(SurroundingRectangle(sea_lab, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the meander bend, two banks ---
        self.next_band(2)
        b2_t = Tex("One bend, two banks, two jobs").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        # Meander bend drawn as a curve of line segments
        m1 = Line(band_shift(2) + LEFT * 4.6 + DOWN * 1.8, band_shift(2) + LEFT * 2.6 + UP * 0.2, color=BLUE, stroke_width=5)
        m2 = Line(band_shift(2) + LEFT * 2.6 + UP * 0.2, band_shift(2) + LEFT * 0.2 + UP * 1.0, color=BLUE, stroke_width=5)
        m3 = Line(band_shift(2) + LEFT * 0.2 + UP * 1.0, band_shift(2) + RIGHT * 2.2 + UP * 0.2, color=BLUE, stroke_width=5)
        m4 = Line(band_shift(2) + RIGHT * 2.2 + UP * 0.2, band_shift(2) + RIGHT * 4.2 + DOWN * 1.8, color=BLUE, stroke_width=5)
        self.play(Create(m1), Create(m2), Create(m3), Create(m4))
        self.wait(2)
        fast = Arrow(band_shift(2) + LEFT * 1.6 + UP * 1.6, band_shift(2) + RIGHT * 1.6 + UP * 1.6,
                     buff=0, color=RED)
        fast_lab = Tex(r"outside: fast $\rightarrow$ erodes (undercut slope)").scale(0.85).shift(band_shift(2) + UP * 2.9 + RIGHT * 0.4)
        self.play(Create(fast), Write(fast_lab))
        self.wait(2)
        slow = Arrow(band_shift(2) + LEFT * 1.0 + DOWN * 0.6, band_shift(2) + RIGHT * 1.0 + DOWN * 0.6,
                     buff=0, color=GREEN)
        slow_lab = Tex(r"inside: slow $\rightarrow$ deposits (slip-off slope)").scale(0.85).shift(band_shift(2) + DOWN * 1.4)
        self.play(Create(slow), Write(slow_lab))
        self.wait(2)
        one = Tex(r"Fast outer water erodes; slow inner water deposits").scale(0.9).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(one))
        self.play(Create(SurroundingRectangle(one, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): where meanders live + migration ---
        self.next_band(3)
        b3_t = Tex("Where meanders live, and how they move").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        w1 = Tex(r"Lower course: gentle gradient, big volume").scale(1.0).shift(band_shift(3) + UP * 1.2)
        w2 = Tex(r"Lateral erosion $>$ vertical erosion").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(w1))
        self.wait(2)
        self.play(Write(w2))
        self.wait(2)
        w3 = Tex(r"Each flood: outer bank retreats, beach follows").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        w4 = Tex(r"Loop swells, swings, migrates downstream").scale(0.95).shift(band_shift(3) + DOWN * 1.3)
        w5 = Tex(r"Wandering loops sweep the floodplain flat").scale(0.95).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(w3))
        self.wait(2)
        self.play(Write(w4))
        self.wait(2)
        self.play(Write(w5))
        self.play(Create(SurroundingRectangle(w5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): neck narrows, flood breaks through ---
        self.next_band(4)
        b4_t = Tex("The neck, and the flood that ends it").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        # Loop with narrowing neck: two limbs drawn as line chains
        l1 = Line(band_shift(4) + LEFT * 3.8 + DOWN * 1.6, band_shift(4) + LEFT * 2.6 + UP * 0.6, color=BLUE, stroke_width=5)
        l2 = Line(band_shift(4) + LEFT * 2.6 + UP * 0.6, band_shift(4) + LEFT * 0.6 + UP * 1.4, color=BLUE, stroke_width=5)
        l3 = Line(band_shift(4) + LEFT * 0.6 + UP * 1.4, band_shift(4) + RIGHT * 1.4 + UP * 0.6, color=BLUE, stroke_width=5)
        l4 = Line(band_shift(4) + RIGHT * 1.4 + UP * 0.6, band_shift(4) + RIGHT * 0.6 + DOWN * 1.6, color=BLUE, stroke_width=5)
        self.play(Create(l1), Create(l2), Create(l3), Create(l4))
        self.wait(2)
        n1 = Arrow(band_shift(4) + LEFT * 3.4 + DOWN * 0.6, band_shift(4) + LEFT * 2.0 + DOWN * 0.9, buff=0, color=RED)
        n2 = Arrow(band_shift(4) + RIGHT * 1.6 + DOWN * 0.6, band_shift(4) + RIGHT * 0.2 + DOWN * 0.9, buff=0, color=RED)
        neck = Tex(r"neck eaten from both sides").scale(0.85).shift(band_shift(4) + DOWN * 1.7 + LEFT * 1.0)
        self.play(Create(n1), Create(n2))
        self.play(Write(neck))
        self.wait(2)
        brk = Line(band_shift(4) + LEFT * 3.0 + DOWN * 1.2, band_shift(4) + RIGHT * 0.2 + DOWN * 1.2,
                   color=YELLOW, stroke_width=6)
        brk_lab = Tex(r"flood punches through: shortcut adopted").scale(0.9).shift(band_shift(4) + DOWN * 2.6)
        self.play(Create(brk))
        self.play(Write(brk_lab))
        self.play(Create(SurroundingRectangle(brk_lab, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): sealing, the lake, the scar ---
        self.next_band(5)
        b5_t = Tex("Sealed, stranded, silted").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        s1 = Tex(r"1. Sediment plugs the loop's two ends").scale(1.0).shift(band_shift(5) + UP * 1.2)
        s2 = Tex(r"2. Horseshoe of still water = OXBOW LAKE").scale(1.0).shift(band_shift(5) + UP * 0.4)
        s3 = Tex(r"3. Evaporates, silts up, reeds close in").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        s4 = Tex(r"4. Curved marshy scar = MEANDER SCAR").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(s1))
        self.wait(2)
        self.play(Write(s2))
        self.play(Create(SurroundingRectangle(s2, color=GREEN)))
        self.wait(2)
        self.play(Write(s3))
        self.wait(2)
        self.play(Write(s4))
        self.wait(2)
        s5 = Tex(r"Pongola floodplain: every stage on one map").scale(0.9).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(s5))
        self.wait(3)

        # --- Band 6 (subtopic_4): reading sketches and photographs ---
        self.next_band(6)
        b6_t = Tex("Reading the sketch and the photo").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        r1 = Tex(r"Profile: step = waterfall; flat = reservoir;").scale(0.95).shift(band_shift(6) + UP * 1.2)
        r1b = Tex(r"dashed line at sea = permanent base level").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(r1))
        self.play(Write(r1b))
        self.wait(2.5)
        r2 = Tex(r"Photo: raw collapsing bank = fast outer side").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        r3 = Tex(r"gentle sand apron = slow inner side").scale(0.95).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(r2))
        self.wait(2)
        self.play(Write(r3))
        self.wait(2)
        r4 = Tex(r"Account for a bank = speed + process, always").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(r4))
        self.play(Create(SurroundingRectangle(r4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): map signatures + look-alike questions ---
        self.next_band(7)
        b7_t = Tex("Map signatures and look-alikes").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        p1 = Tex(r"Loops on pale flat land, contours far back:").scale(0.95).shift(band_shift(7) + UP * 1.2)
        p1b = Tex(r"meanders on a floodplain").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(p1))
        self.play(Write(p1b))
        self.wait(2.5)
        p2 = Tex(r"Detached blue crescent: oxbow lake").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        p3 = Tex(r"Loops inside crowded contours: incised meanders").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(p2))
        self.wait(2)
        self.play(Write(p3))
        self.wait(2)
        p4 = Tex(r"Meander answer $\subset$ oxbow answer — never reversed").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(p4))
        self.play(Create(SurroundingRectangle(p4, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the slide from the mountain to the sea ---
        self.next_band(8)
        b8_t = Tex("The slide from the mountain to the sea").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        sl1 = Tex(r"Perfect slide: one smooth swoop = graded").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(sl1))
        self.wait(2)
        sl2 = Tex(r"Unfinished slide: ledge = waterfall,").scale(0.95).shift(band_shift(8) + UP * 0.4)
        sl2b = Tex(r"stalling pan = reservoir").scale(0.95).shift(band_shift(8) + DOWN * 0.3)
        self.play(Write(sl2))
        self.play(Write(sl2b))
        self.wait(2.5)
        sl3 = Tex(r"Splash pool = sea = the floor forever").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(sl3))
        self.play(Create(SurroundingRectangle(sl3, color=GREEN)))
        self.wait(2)
        sl4 = Tex(r"Knife-cut V up top; spade-smoothed flat below").scale(0.9).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(sl4))
        self.wait(3)

        # --- Band 9 (subtopic_6): the taxi around the corner ---
        self.next_band(9)
        b9_t = Tex("The taxi around the corner").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        tx1 = Tex(r"Far window: long path, fast, pressed to the door").scale(0.9).shift(band_shift(9) + UP * 1.2)
        tx2 = Tex(r"Inside seat: short path, slow, easy ride").scale(0.9).shift(band_shift(9) + UP * 0.4)
        self.play(Write(tx1))
        self.wait(2)
        self.play(Write(tx2))
        self.wait(2)
        tx3 = Tex(r"Fast lane digs the cliff (undercut slope)").scale(0.95).shift(band_shift(9) + DOWN * 0.5)
        tx4 = Tex(r"Slow lane drops the beach (slip-off slope)").scale(0.95).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(tx3))
        self.wait(2)
        self.play(Write(tx4))
        self.play(Create(SurroundingRectangle(tx4, color=GREEN)))
        self.wait(2)
        tx5 = Tex(r"Loops drift like a flicked rope; floodplain = their sweep").scale(0.85).shift(band_shift(9) + DOWN * 2.2)
        self.play(Write(tx5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the shortcut through the empty plot ---
        self.next_band(10)
        b10_t = Tex("The shortcut through the empty plot").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        z1 = Tex(r"Neck trenched from both sides, flood by flood").scale(0.95).shift(band_shift(10) + UP * 1.2)
        self.play(Write(z1))
        self.wait(2)
        z2 = Tex(r"Big flood opens the diagonal path — for good").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(z2))
        self.wait(2)
        z3 = Tex(r"Sand gates close the loop: OXBOW LAKE").scale(0.95).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(z3))
        self.play(Create(SurroundingRectangle(z3, color=GREEN)))
        self.wait(2)
        z4 = Tex(r"Sun, silt and reeds $\rightarrow$ meander scar").scale(0.95).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(z4))
        self.wait(2)
        z5 = Tex(r"Eight steps in order: erode, build, thin, break,").scale(0.9).shift(band_shift(10) + DOWN * 2.1)
        z5b = Tex(r"adopt, seal, lake, scar").scale(0.9).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(z5))
        self.play(Write(z5b))
        self.wait(4)
