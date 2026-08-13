from manim import *

# Band-layout whiteboard scene for the urban-settlements duo on GIS
# (data layering, buffering and querying). Exporter-safe primitives only
# (Tex/MathTex/Line/Arrow/Dot/Circle/Rectangle/VGroup); add-only lifecycle;
# camera moves down one frame-height per band. The layer stack is offset
# Rectangles, the buffers are a Circle around a Dot and a Line corridor —
# all hand-built element by element in script order.
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
        self.wait(13)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): definition + spatial vs attribute ---
        title = Tex("GIS: The Whole Toolkit").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex(r"Five verbs the memo pays for:").scale(1.05).shift(UP * 1.3)
        d2 = Tex(r"capture, store, manipulate, analyse, display").scale(1.05).shift(UP * 0.5)
        self.play(Write(d1))
        self.play(Write(d2))
        self.play(Create(SurroundingRectangle(d2, color=GREEN)))
        self.wait(2.5)
        d3 = Tex(r"Spatial data: position and shape (the drawing)").scale(1.0).shift(DOWN * 0.6)
        d4 = Tex(r"Attribute data: facts attached (the label)").scale(1.0).shift(DOWN * 1.4)
        self.play(Write(d3))
        self.wait(2)
        self.play(Write(d4))
        self.wait(2)
        d5 = Tex(r"Trap: the drawn road is spatial; the route").scale(0.95).shift(DOWN * 2.3)
        d5b = Tex(r"number 310 written on it is attribute").scale(0.95).shift(DOWN * 3.0)
        self.play(Write(d5))
        self.play(Write(d5b))
        self.wait(3)

        # --- Band 1 (subtopic_1): feature shapes + vector vs raster ---
        self.next_band(1)
        b1_t = Tex("Three shapes, two ways to store a map").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        # Point, line, area examples drawn
        pt = Dot(band_shift(1) + LEFT * 4.0 + UP * 1.0, color=YELLOW)
        pt_lab = Tex(r"point: trig beacon").scale(0.85).shift(band_shift(1) + LEFT * 4.0 + UP * 0.4)
        ln = Line(band_shift(1) + LEFT * 1.4 + UP * 1.2, band_shift(1) + RIGHT * 1.0 + UP * 0.8,
                  color=BLUE, stroke_width=5)
        ln_lab = Tex(r"line: river, road").scale(0.85).shift(band_shift(1) + LEFT * 0.2 + UP * 0.2)
        ar = Rectangle(width=1.6, height=1.0, color=GREEN).shift(band_shift(1) + RIGHT * 3.6 + UP * 1.0)
        ar_lab = Tex(r"area: dam, field").scale(0.85).shift(band_shift(1) + RIGHT * 3.6 + UP * 0.1)
        self.play(Create(pt), Write(pt_lab))
        self.play(Create(ln), Write(ln_lab))
        self.play(Create(ar), Write(ar_lab))
        self.wait(2)
        q1 = Tex(r"Natural line = river; constructed line = road").scale(0.95).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(q1))
        self.wait(2)
        q2 = Tex(r"Vector: crisp points/lines/polygons (fences)").scale(0.95).shift(band_shift(1) + DOWN * 1.9)
        q3 = Tex(r"Raster: grid of equal cells, like a photo's pixels").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(q2))
        self.wait(2)
        self.play(Write(q3))
        self.wait(3)

        # --- Band 2 (subtopic_2): the transparency stack ---
        self.next_band(2)
        b2_t = Tex("Data layering: the transparency stack").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        # Offset stacked sheets
        sh1 = Rectangle(width=4.6, height=1.6, color=BLUE).shift(band_shift(2) + LEFT * 1.6 + UP * 0.8)
        sh1_lab = Tex(r"drainage").scale(0.85).shift(band_shift(2) + RIGHT * 1.6 + UP * 0.8)
        sh2 = Rectangle(width=4.6, height=1.6, color=GREY).shift(band_shift(2) + LEFT * 1.2 + UP * 0.2)
        sh2_lab = Tex(r"transport").scale(0.85).shift(band_shift(2) + RIGHT * 2.0 + UP * 0.2)
        sh3 = Rectangle(width=4.6, height=1.6, color=YELLOW).shift(band_shift(2) + LEFT * 0.8 + DOWN * 0.4)
        sh3_lab = Tex(r"contours").scale(0.85).shift(band_shift(2) + RIGHT * 2.4 + DOWN * 0.4)
        sh4 = Rectangle(width=4.6, height=1.6, color=GREEN).shift(band_shift(2) + LEFT * 0.4 + DOWN * 1.0)
        sh4_lab = Tex(r"cadastral (property)").scale(0.85).shift(band_shift(2) + RIGHT * 3.2 + DOWN * 1.0)
        self.play(Create(sh1), Write(sh1_lab))
        self.play(Create(sh2), Write(sh2_lab))
        self.play(Create(sh3), Write(sh3_lab))
        self.play(Create(sh4), Write(sh4_lab))
        self.wait(2)
        st1 = Tex(r"Separate sheets, same coordinates —").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        st1b = Tex(r"they align perfectly when stacked").scale(0.95).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(st1))
        self.play(Write(st1b))
        self.wait(3)

        # --- Band 3 (subtopic_2): why separate + the redraw skill ---
        self.next_band(3)
        b3_t = Tex("Why separate? Analysis.").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        w1 = Tex(r"The planner pulls three sheets only:").scale(1.0).shift(band_shift(3) + UP * 1.2)
        w1b = Tex(r"drainage, contours, existing buildings").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(w1))
        self.play(Write(w1b))
        self.wait(2.5)
        w2 = Tex(r"Name the LAYER by its theme: rivers + dams").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        w2b = Tex(r"= drainage layer, not ``water''").scale(0.95).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(w2))
        self.play(Write(w2b))
        self.wait(2.5)
        w3 = Tex(r"Combine-the-layers sketch: copy each feature").scale(0.95).shift(band_shift(3) + DOWN * 2.2)
        w3b = Tex(r"in its own position — one mark per feature").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(w3))
        self.play(Write(w3b))
        self.play(Create(SurroundingRectangle(w3b, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): buffering ---
        self.next_band(4)
        b4_t = Tex("Buffering: a zone with an edge").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        # Point buffer: circle around a dot
        bp = Dot(band_shift(4) + LEFT * 3.6 + UP * 0.6, color=RED)
        bc = Circle(radius=0.9, color=YELLOW).shift(band_shift(4) + LEFT * 3.6 + UP * 0.6)
        bp_lab = Tex(r"point $\rightarrow$ circle").scale(0.85).shift(band_shift(4) + LEFT * 3.6 + DOWN * 0.7)
        self.play(Create(bp), Create(bc))
        self.play(Write(bp_lab))
        self.wait(2)
        # Line buffer: corridor around a stream line
        stream = Line(band_shift(4) + RIGHT * 0.6 + UP * 0.6, band_shift(4) + RIGHT * 5.0 + UP * 0.6,
                      color=BLUE, stroke_width=5)
        cor1 = DashedLine(band_shift(4) + RIGHT * 0.6 + UP * 1.2, band_shift(4) + RIGHT * 5.0 + UP * 1.2,
                          color=YELLOW)
        cor2 = DashedLine(band_shift(4) + RIGHT * 0.6 + UP * 0.0, band_shift(4) + RIGHT * 5.0 + UP * 0.0,
                          color=YELLOW)
        cor_lab = Tex(r"line $\rightarrow$ corridor: 100 m, no houses").scale(0.85).shift(band_shift(4) + RIGHT * 2.9 + DOWN * 0.7)
        self.play(Create(stream))
        self.play(Create(cor1), Create(cor2))
        self.play(Write(cor_lab))
        self.wait(2.5)
        bf1 = Tex(r"Sinkholes: no-build ring; woodland: distance").scale(0.95).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(bf1))
        self.wait(2)
        bf2 = Tex(r"Empty gap next to a hazard? Say BUFFERING").scale(0.95).shift(band_shift(4) + DOWN * 2.6)
        bf2b = Tex(r"and name the hazard as evidence").scale(0.95).shift(band_shift(4) + DOWN * 3.3)
        self.play(Write(bf2))
        self.play(Write(bf2b))
        self.play(Create(SurroundingRectangle(bf2b, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): querying + integration ---
        self.next_band(5)
        b5_t = Tex("Querying and data integration").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        qy1 = Tex(r"Query: ask, and the database fetches —").scale(1.0).shift(band_shift(5) + UP * 1.2)
        qy1b = Tex(r"``show all erven larger than 500 m$^2$''").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(qy1))
        self.play(Write(qy1b))
        self.wait(2.5)
        qy2 = Tex(r"Searches spatial AND attribute data together").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(qy2))
        self.wait(2)
        qy3 = Tex(r"Integration first: registers, images, census").scale(0.95).shift(band_shift(5) + DOWN * 1.4)
        qy3b = Tex(r"all georeferenced onto one grid").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(qy3))
        self.play(Write(qy3b))
        self.wait(2.5)
        qy4 = Tex(r"Then statistics: households in the flood buffer").scale(0.9).shift(band_shift(5) + DOWN * 3.1)
        self.play(Write(qy4))
        self.wait(3)

        # --- Band 6 (subtopic_4): resolution + manipulation ---
        self.next_band(6)
        b6_t = Tex("Resolution and data manipulation").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        rz1 = Tex(r"Small cells, many pixels = HIGH resolution").scale(1.0).shift(band_shift(6) + UP * 1.2)
        rz2 = Tex(r"Large cells, few pixels = blocky blur").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(rz1))
        self.wait(2)
        self.play(Write(rz2))
        self.wait(2)
        rz3 = Tex(r"``Which has fewer pixels?'' — the blurrier one").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(rz3))
        self.wait(2)
        rz4 = Tex(r"``Manipulate the scale for clarity''").scale(0.95).shift(band_shift(6) + DOWN * 1.4)
        rz5 = Tex(r"= ENLARGE the scale — zoom in").scale(1.0).shift(band_shift(6) + DOWN * 2.3)
        self.play(Write(rz4))
        self.wait(2)
        self.play(Write(rz5))
        self.play(Create(SurroundingRectangle(rz5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): how the GIS block is examined ---
        self.next_band(7)
        b7_t = Tex("The GIS block: roughly eight marks").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        e1 = Tex(r"1. Vocabulary MCQs — memorised definitions").scale(0.95).shift(band_shift(7) + UP * 1.2)
        e2 = Tex(r"2. Application: name the feature, the layer,").scale(0.95).shift(band_shift(7) + UP * 0.4)
        e2b = Tex(r"the evidence behind a buffer").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        e3 = Tex(r"3. Practical redraw into one frame").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(e1))
        self.wait(2)
        self.play(Write(e2))
        self.play(Write(e2b))
        self.wait(2.5)
        self.play(Write(e3))
        self.wait(2)
        e4 = Tex(r"The planner ends with safe, flat, dry land:").scale(0.95).shift(band_shift(7) + DOWN * 2.1)
        e4b = Tex(r"GIS turns a map into an argument").scale(0.95).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(e4))
        self.play(Write(e4b))
        self.play(Create(SurroundingRectangle(e4b, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the burger ---
        self.next_band(8)
        b8_t = Tex("The burger that explains the system").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        g1 = Tex(r"Bun, patty, lettuce: made separately,").scale(1.0).shift(band_shift(8) + UP * 1.2)
        g1b = Tex(r"eaten together — layers over one spot").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(g1))
        self.play(Write(g1b))
        self.wait(2.5)
        g2 = Tex(r"Where your friend stands = spatial;").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        g2b = Tex(r"name, age, number = attributes").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(g2))
        self.play(Write(g2b))
        self.wait(2.5)
        g3 = Tex(r"Vector = pen drawing (stays sharp);").scale(1.0).shift(band_shift(8) + DOWN * 2.2)
        g3b = Tex(r"raster = phone photo (crumbles to blocks)").scale(1.0).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(g3))
        self.play(Write(g3b))
        self.play(Create(SurroundingRectangle(g3b, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the chalk circle around the beehive ---
        self.next_band(9)
        b9_t = Tex("The chalk circle around the beehive").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        c1 = Tex(r"Beehive in the tree: chalk circle, ten steps —").scale(0.95).shift(band_shift(9) + UP * 1.2)
        c1b = Tex(r"nobody plays inside. That is a BUFFER").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(c1))
        self.play(Write(c1b))
        self.wait(2.5)
        c2 = Tex(r"Towns buffer rivers, sinkholes, woodlands").scale(0.95).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(c2))
        self.wait(2)
        c3 = Tex(r"Query = typing a song into the music app:").scale(0.95).shift(band_shift(9) + DOWN * 1.4)
        c3b = Tex(r"the database fetches what matches").scale(0.95).shift(band_shift(9) + DOWN * 2.2)
        self.play(Write(c3))
        self.play(Write(c3b))
        self.wait(2.5)
        c4 = Tex(r"Integration first: all the music must be IN the app").scale(0.9).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(c4))
        self.play(Create(SurroundingRectangle(c4, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): pixels, zooming and free marks ---
        self.next_band(10)
        b10_t = Tex("Pixels, zooming in and free marks").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        z1 = Tex(r"Zoomed scoreboard photo goes blocky:").scale(1.0).shift(band_shift(10) + UP * 1.2)
        z1b = Tex(r"big pixels, LOW resolution").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(z1))
        self.play(Write(z1b))
        self.wait(2.5)
        z2 = Tex(r"Fewer pixels? Pick the blurry one — larger").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        z2b = Tex(r"pixels, lower resolution").scale(0.95).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(z2))
        self.play(Write(z2b))
        self.wait(2.5)
        z3 = Tex(r"Unclear orthophoto? ENLARGE the scale — zoom in").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(z3))
        self.play(Create(SurroundingRectangle(z3, color=GREEN)))
        self.wait(2.5)
        z4 = Tex(r"Six ideas, one story, eight calm marks").scale(0.95).shift(band_shift(10) + DOWN * 3.1)
        self.play(Write(z4))
        self.wait(4)
