# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
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

# Band-layout whiteboard scene for the GIS data layering, buffering and
# querying duo lesson. Exporter-safe primitives only (Tex/Line/Arrow/
# Dot/Circle/Rectangle/VGroup); add-only lifecycle; camera moves down
# one frame-height per band. Layer stacks and buffers are hand-built
# from Rectangles, Circles and Lines in script order.
#
# Subtopic shares (subtopics.json, total 1495 s):
# 235/225/230/240 expert, 200/190/175 simplifier. Bands 0-7 = Part 1
# (two per expert subtopic), bands 8-10 = fresh Part 2 bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class GISToolkitSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): definition + spatial vs attribute ---
        title = Tex("GIS: five verbs, two kinds of data").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        v1 = Tex(r"capture $\cdot$ store $\cdot$ manipulate $\cdot$ analyse $\cdot$ display").scale(0.95).shift(UP * 1.4)
        self.play(Write(v1))
        self.play(Create(SurroundingRectangle(v1, color=GREEN)))
        self.wait(2.5)
        s1 = Tex(r"SPATIAL: position and shape — the drawing").scale(0.95).shift(UP * 0.3)
        s2 = Tex(r"ATTRIBUTE: facts attached — the label").scale(0.95).shift(DOWN * 0.5)
        self.play(Write(s1))
        self.wait(2)
        self.play(Write(s2))
        self.wait(2)
        road = Line(LEFT * 3.6 + DOWN * 1.8, RIGHT * 3.6 + DOWN * 1.8, color=GREY, stroke_width=5)
        road_num = Tex(r"R 62").scale(0.8).shift(DOWN * 1.35)
        road_lab = Tex(r"drawn road = spatial; its number = attribute").scale(0.85).shift(DOWN * 2.6)
        self.play(Create(road))
        self.play(Write(road_num))
        self.play(Write(road_lab))
        self.wait(3)

        # --- Band 1 (subtopic_1): feature shapes + vector vs raster ---
        self.next_band(1)
        b1_t = Tex("Point, line, area — vector, raster").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        pt = Dot(band_shift(1) + LEFT * 3.6 + UP * 0.8, radius=0.1, color=WHITE)
        pt_lab = Tex(r"point: beacon, borehole").scale(0.8).shift(band_shift(1) + LEFT * 3.4 + UP * 0.2)
        ln = Line(band_shift(1) + LEFT * 0.8 + UP * 0.9, band_shift(1) + RIGHT * 1.6 + UP * 0.5, color=BLUE, stroke_width=4)
        ln_lab = Tex(r"line: river, road").scale(0.8).shift(band_shift(1) + RIGHT * 0.4 + UP * 0.0)
        ar = Rectangle(width=1.6, height=1.0, color=GREEN).shift(band_shift(1) + RIGHT * 3.6 + UP * 0.7)
        ar_lab = Tex(r"area: reservoir, block").scale(0.8).shift(band_shift(1) + RIGHT * 3.5 + DOWN * 0.2)
        self.play(Create(pt), Write(pt_lab))
        self.play(Create(ln), Write(ln_lab))
        self.play(Create(ar), Write(ar_lab))
        self.wait(2.5)
        vr1 = Tex(r"VECTOR: crisp outlines — fences, erven").scale(0.9).shift(band_shift(1) + DOWN * 1.2)
        vr2 = Tex(r"RASTER: grid of cells — photos, satellite images").scale(0.9).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(vr1))
        self.wait(2)
        self.play(Write(vr2))
        self.play(Create(SurroundingRectangle(vr2, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the transparency stack ---
        self.next_band(2)
        b2_t = Tex("Layers: the transparency stack").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        l1 = Rectangle(width=5.6, height=1.0, color=BLUE).shift(band_shift(2) + UP * 1.0)
        l1_lab = Tex(r"drainage").scale(0.8).shift(band_shift(2) + UP * 1.0 + RIGHT * 3.6)
        l2 = Rectangle(width=5.6, height=1.0, color=GREY).shift(band_shift(2) + UP * 0.0)
        l2_lab = Tex(r"transport").scale(0.8).shift(band_shift(2) + UP * 0.0 + RIGHT * 3.6)
        l3 = Rectangle(width=5.6, height=1.0, color=YELLOW).shift(band_shift(2) + DOWN * 1.0)
        l3_lab = Tex(r"contours").scale(0.8).shift(band_shift(2) + DOWN * 1.0 + RIGHT * 3.6)
        l4 = Rectangle(width=5.6, height=1.0, color=GREEN).shift(band_shift(2) + DOWN * 2.0)
        l4_lab = Tex(r"cadastral (erven)").scale(0.8).shift(band_shift(2) + DOWN * 2.0 + RIGHT * 3.9)
        self.play(Create(l1), Write(l1_lab))
        self.play(Create(l2), Write(l2_lab))
        self.play(Create(l3), Write(l3_lab))
        self.play(Create(l4), Write(l4_lab))
        self.wait(2.5)
        g1 = Tex(r"Same coordinates $\Rightarrow$ perfect alignment").scale(0.9).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(g1))
        self.play(Create(SurroundingRectangle(g1, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): why separate + the redraw skill ---
        self.next_band(3)
        b3_t = Tex("Why separate, and the redraw").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        w1 = Tex(r"Pull only what the task needs:").scale(0.95).shift(band_shift(3) + UP * 1.2)
        w2 = Tex(r"clinic siting = transport + contours + drainage").scale(0.9).shift(band_shift(3) + UP * 0.4)
        self.play(Write(w1))
        self.play(Write(w2))
        self.wait(2.5)
        w3 = Tex(r"Name the LAYER by theme, not the object").scale(0.9).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(w3))
        self.wait(2)
        w4 = Tex(r"Redraw skill: copy each feature in place,").scale(0.9).shift(band_shift(3) + DOWN * 1.4)
        w4b = Tex(r"overlap where the originals overlap").scale(0.9).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(w4))
        self.play(Write(w4b))
        self.play(Create(SurroundingRectangle(w4b, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): buffering ---
        self.next_band(4)
        b4_t = Tex("Buffering: a measured edge around trouble").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        # Stream with corridor buffer
        stream = Line(band_shift(4) + LEFT * 4.6 + DOWN * 0.4, band_shift(4) + RIGHT * 4.6 + UP * 0.6, color=BLUE, stroke_width=4)
        buf_top = Line(band_shift(4) + LEFT * 4.6 + UP * 0.4, band_shift(4) + RIGHT * 4.6 + UP * 1.4, color=RED, stroke_width=3)
        buf_bot = Line(band_shift(4) + LEFT * 4.6 + DOWN * 1.2, band_shift(4) + RIGHT * 4.6 + DOWN * 0.2, color=RED, stroke_width=3)
        buf_lab = Tex(r"100 m corridor: no building — floods").scale(0.85).shift(band_shift(4) + DOWN * 1.9)
        self.play(Create(stream))
        self.play(Create(buf_top), Create(buf_bot))
        self.play(Write(buf_lab))
        self.wait(2.5)
        b1 = Tex(r"Point $\rightarrow$ circle; line $\rightarrow$ corridor; area $\rightarrow$ band").scale(0.9).shift(band_shift(4) + UP * 1.4)
        self.play(Write(b1))
        self.play(Create(SurroundingRectangle(b1, color=GREEN)))
        self.wait(2)
        b2 = Tex(r"Power-line servitude, wetland band, dune strip").scale(0.85).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b2))
        self.wait(3)

        # --- Band 5 (subtopic_3): querying + integration ---
        self.next_band(5)
        b5_t = Tex("Querying and integration").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        q1 = Tex(r"Query: fetch all features matching conditions").scale(0.9).shift(band_shift(5) + UP * 1.2)
        q2 = Tex(r"``open erven $>$ 400 m$^2$, within 2 km of a taxi route''").scale(0.85).shift(band_shift(5) + UP * 0.4)
        self.play(Write(q1))
        self.wait(2)
        self.play(Write(q2))
        self.wait(2.5)
        q3 = Tex(r"Searches spatial + attribute data together").scale(0.9).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(q3))
        self.wait(2)
        q4 = Tex(r"Integration first: register + imagery + census").scale(0.9).shift(band_shift(5) + DOWN * 1.4)
        q4b = Tex(r"one system, one grid — then statistics can count").scale(0.9).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(q4))
        self.play(Write(q4b))
        self.play(Create(SurroundingRectangle(q4, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): resolution + manipulation ---
        self.next_band(6)
        b6_t = Tex("Resolution and manipulation").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        r1 = Tex(r"Resolution = detail held, set by cell size").scale(0.9).shift(band_shift(6) + UP * 1.2)
        self.play(Write(r1))
        self.wait(2)
        r2 = Tex(r"Small cells: sharp. Large cells: blocky blur").scale(0.9).shift(band_shift(6) + UP * 0.4)
        self.play(Write(r2))
        self.wait(2)
        r3 = Tex(r"Fewer pixels $\Rightarrow$ the blurrier image").scale(0.9).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(r3))
        self.play(Create(SurroundingRectangle(r3, color=GREEN)))
        self.wait(2)
        r4 = Tex(r"Unclear orthophoto? ENLARGE the scale — zoom in").scale(0.9).shift(band_shift(6) + DOWN * 1.3)
        r5 = Tex(r"(also: convert formats, reproject)").scale(0.85).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(r4))
        self.wait(2)
        self.play(Write(r5))
        self.wait(3)

        # --- Band 7 (subtopic_4): the three question types + the decision ---
        self.next_band(7)
        b7_t = Tex("Three question types, one decision").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        t1 = Tex(r"1. Vocabulary: definitions score instantly").scale(0.95).shift(band_shift(7) + UP * 1.2)
        t2 = Tex(r"2. Application: name features, layers, evidence").scale(0.95).shift(band_shift(7) + UP * 0.4)
        t3 = Tex(r"3. Redraw: one mark per feature placed true").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(t1))
        self.wait(2)
        self.play(Write(t2))
        self.wait(2)
        self.play(Write(t3))
        self.wait(2)
        t4 = Tex(r"Layers stacked, buffers drawn, query run:").scale(0.95).shift(band_shift(7) + DOWN * 1.4)
        t4b = Tex(r"the clinic is placed by evidence").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(t4))
        self.play(Write(t4b))
        self.play(Create(SurroundingRectangle(t4b, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the burger ---
        self.next_band(8)
        b8_t = Tex("The burger that explains the system").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        x1 = Tex(r"Bun, patty, lettuce: made apart, eaten stacked").scale(0.9).shift(band_shift(8) + UP * 1.2)
        self.play(Write(x1))
        self.wait(2)
        x2 = Tex(r"= rivers, roads, erven on aligned layers").scale(0.9).shift(band_shift(8) + UP * 0.4)
        self.play(Write(x2))
        self.wait(2)
        x3 = Tex(r"WHERE she stands = spatial; her NAME = attribute").scale(0.9).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(x3))
        self.play(Create(SurroundingRectangle(x3, color=GREEN)))
        self.wait(2.5)
        x4 = Tex(r"Pen drawing = vector; phone photo = raster").scale(0.9).shift(band_shift(8) + DOWN * 1.4)
        x4b = Tex(r"drawings zoom sharp; photos go blocky").scale(0.9).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(x4))
        self.play(Write(x4b))
        self.wait(3)

        # --- Band 9 (subtopic_6): the chalk circle around the beehive ---
        self.next_band(9)
        b9_t = Tex("The chalk circle around the beehive").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        hive = Dot(band_shift(9) + LEFT * 2.6 + DOWN * 0.4, radius=0.12, color=YELLOW)
        chalk = Circle(radius=1.3, color=WHITE).shift(band_shift(9) + LEFT * 2.6 + DOWN * 0.4)
        ch_lab = Tex(r"nobody crosses the chalk").scale(0.8).shift(band_shift(9) + LEFT * 2.6 + DOWN * 2.2)
        self.play(Create(hive))
        self.play(Create(chalk))
        self.play(Write(ch_lab))
        self.wait(2.5)
        y1 = Tex(r"Buffer = a measured edge around trouble").scale(0.9).shift(band_shift(9) + RIGHT * 2.4 + UP * 1.0)
        self.play(Write(y1))
        self.play(Create(SurroundingRectangle(y1, color=GREEN)))
        self.wait(2)
        y2 = Tex(r"Empty ribbon on the map? A buffer at work").scale(0.85).shift(band_shift(9) + RIGHT * 2.4 + UP * 0.1)
        self.play(Write(y2))
        self.wait(2)
        y3 = Tex(r"Query = the music-app search for land;").scale(0.85).shift(band_shift(9) + DOWN * 2.9 + LEFT * 0.4)
        y3b = Tex(r"integration loads the library first").scale(0.85).shift(band_shift(9) + DOWN * 3.5 + LEFT * 0.4)
        self.play(Write(y3))
        self.play(Write(y3b))
        self.wait(3)

        # --- Band 10 (subtopic_7): pixels, zooming and free marks ---
        self.next_band(10)
        b10_t = Tex("Pixels, zooming in and free marks").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        z1 = Tex(r"Zoomed bird photo $\rightarrow$ fuzzy squares").scale(0.9).shift(band_shift(10) + UP * 1.2)
        self.play(Write(z1))
        self.wait(2)
        z2 = Tex(r"Fewer pixels = larger pixels = lower resolution").scale(0.9).shift(band_shift(10) + UP * 0.4)
        self.play(Write(z2))
        self.play(Create(SurroundingRectangle(z2, color=GREEN)))
        self.wait(2.5)
        z3 = Tex(r"Unclear area? Enlarge the scale — zoom in").scale(0.9).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(z3))
        self.wait(2)
        z4 = Tex(r"Six ideas, one story: layers, where + what,").scale(0.85).shift(band_shift(10) + DOWN * 1.4)
        z4b = Tex(r"vector/raster, buffers, queries, integration").scale(0.85).shift(band_shift(10) + DOWN * 2.1)
        self.play(Write(z4))
        self.play(Write(z4b))
        self.wait(2)
        z5 = Tex(r"Calm + definitions = marks on sight").scale(0.9).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(z5))
        self.wait(4)
