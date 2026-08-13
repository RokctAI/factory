from manim import *

# Band-layout whiteboard scene for "GIS Components and Remote Sensing"
# (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier 5-7). Exporter-safe
# primitives only: the GIS layer stack is offset Rectangles + Tex, the
# remote-sensing reflection sketch is Arrows + a ground Line + a satellite
# Rectangle. Add-only lifecycle; the camera moves down band by band.
# Band time apportioned to subtopics.json (225/225/250/240/190/185/180
# of 1495 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class GISRemoteSensingSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the GIS definition ---
        title = Tex("GIS and Remote Sensing").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("GIS: a computerised system that captures,").scale(1.0).shift(UP * 1.0)
        d2 = Tex("stores, analyses and displays").scale(1.0).shift(UP * 0.2)
        d3 = Tex("GEOREFERENCED information").scale(1.1).shift(DOWN * 0.7)
        self.play(Write(d1))
        self.play(Write(d2))
        self.play(Write(d3))
        self.play(Create(SurroundingRectangle(d3, color=GREEN)))
        self.wait(2.5)
        d4 = Tex("Two halves: a database + every entry").scale(1.0).shift(DOWN * 1.7)
        d5 = Tex("knows its position (coordinates)").scale(1.0).shift(DOWN * 2.5)
        self.play(Write(d4))
        self.play(Write(d5))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): layers, overlay, spatial vs attribute ---
        self.next_band(1)
        b1_title = Tex("The layer principle").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        # stacked transparent sheets, drawn one at a time
        names = ["rivers", "roads", "settlements", "density", "clinics"]
        for i, nm in enumerate(names):
            y = 1.5 - i * 0.75
            sheet = Rectangle(width=5.6, height=0.62).shift(band_shift(1) + LEFT * 2.2 + UP * y)
            lab = Tex(nm).scale(0.8).shift(band_shift(1) + LEFT * 2.2 + UP * y)
            self.play(Create(sheet), Write(lab), run_time=0.8)
        self.wait(1.5)
        ov1 = Tex("Stack them, aligned:").scale(0.95).shift(band_shift(1) + RIGHT * 3.4 + UP * 1.2)
        ov2 = Tex("OVERLAY ANALYSIS").scale(1.0).shift(band_shift(1) + RIGHT * 3.4 + UP * 0.4)
        self.play(Write(ov1))
        self.play(Write(ov2))
        self.play(Create(SurroundingRectangle(ov2, color=GREEN)))
        self.wait(2)
        q1 = Tex("Where should a new clinic go?").scale(0.9).shift(band_shift(1) + RIGHT * 3.4 + DOWN * 0.5)
        self.play(Write(q1))
        self.wait(2)
        sp = Tex("Spatial data: where it is, its shape").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        at = Tex("Attribute data: what it is like").scale(1.0).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(sp))
        self.wait(1.5)
        self.play(Write(at))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the five components ---
        self.next_band(2)
        b2_title = Tex("The five components of a GIS").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        c1 = Tex("1. Hardware: computers, GPS receivers").scale(1.0).shift(band_shift(2) + UP * 1.2)
        c2 = Tex("2. Software: ArcGIS, QGIS, map apps").scale(1.0).shift(band_shift(2) + UP * 0.4)
        c3 = Tex("3. DATA: most important, most expensive").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        c4 = Tex("4. People: capture, analyse, decide").scale(1.0).shift(band_shift(2) + DOWN * 1.2)
        c5 = Tex("5. Procedures: update and accuracy rules").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(c1))
        self.wait(1.5)
        self.play(Write(c2))
        self.wait(1.5)
        self.play(Write(c3))
        self.play(Create(SurroundingRectangle(c3, color=GREEN)))
        self.wait(2)
        self.play(Write(c4))
        self.wait(1.5)
        self.play(Write(c5))
        self.wait(2)
        c6 = Tex("Drop any one and the system fails").scale(1.0).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(c6))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): remote sensing and reflection ---
        self.next_band(3)
        b3_title = Tex("Remote sensing: no contact").scale(1.15).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_d = Tex("Information about the surface, from a distance").scale(0.95).shift(band_shift(3) + UP * 1.5)
        self.play(Write(b3_d))
        self.wait(2)
        # reflection sketch: sun -> ground -> sensor
        ground = Line(band_shift(3) + LEFT * 4.8 + DOWN * 1.6, band_shift(3) + RIGHT * 4.8 + DOWN * 1.6,
                      stroke_width=5)
        g_lab = Tex("surface").scale(0.8).shift(band_shift(3) + RIGHT * 4.0 + DOWN * 2.0)
        self.play(Create(ground), Write(g_lab))
        sun = Circle(radius=0.4, color=YELLOW).shift(band_shift(3) + LEFT * 3.8 + UP * 0.8)
        sun_lab = Tex("sun").scale(0.8).shift(band_shift(3) + LEFT * 4.6 + UP * 0.8)
        self.play(Create(sun), Write(sun_lab))
        down_a = Arrow(band_shift(3) + LEFT * 3.4 + UP * 0.5, band_shift(3) + LEFT * 1.2 + DOWN * 1.5,
                       buff=0, color=YELLOW, stroke_width=5)
        self.play(Create(down_a))
        sat = Rectangle(width=1.2, height=0.6).shift(band_shift(3) + RIGHT * 2.6 + UP * 0.9)
        sat_lab = Tex("sensor").scale(0.8).shift(band_shift(3) + RIGHT * 3.8 + UP * 0.9)
        up_a = Arrow(band_shift(3) + LEFT * 1.0 + DOWN * 1.5, band_shift(3) + RIGHT * 2.3 + UP * 0.6,
                     buff=0, color=BLUE, stroke_width=5)
        self.play(Create(up_a), Create(sat), Write(sat_lab))
        self.wait(2)
        b3_l1 = Tex("Every surface reflects its own signature").scale(0.95).shift(band_shift(3) + DOWN * 2.5)
        b3_l2 = Tex("Sensors read infrared eyes cannot see").scale(0.95).shift(band_shift(3) + DOWN * 3.2)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): satellite vs aerial; strengths and limits ---
        self.next_band(4)
        b4_title = Tex("Satellite image vs aerial photograph").scale(1.1).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        s_box = Rectangle(width=5.6, height=2.4).shift(band_shift(4) + LEFT * 3.1 + UP * 0.6)
        s1 = Tex("Satellite (Landsat, Sentinel):").scale(0.8).shift(band_shift(4) + LEFT * 3.1 + UP * 1.3)
        s2 = Tex("huge areas, returns on a cycle,").scale(0.8).shift(band_shift(4) + LEFT * 3.1 + UP * 0.6)
        s3 = Tex("builds a time series").scale(0.8).shift(band_shift(4) + LEFT * 3.1 + DOWN * 0.1)
        self.play(Create(s_box))
        self.play(Write(s1))
        self.play(Write(s2))
        self.play(Write(s3))
        self.wait(2)
        a_box = Rectangle(width=5.6, height=2.4).shift(band_shift(4) + RIGHT * 3.1 + UP * 0.6)
        a1 = Tex("Aerial photo (aircraft):").scale(0.8).shift(band_shift(4) + RIGHT * 3.1 + UP * 1.3)
        a2 = Tex("lower, finer detail, small areas;").scale(0.8).shift(band_shift(4) + RIGHT * 3.1 + UP * 0.6)
        a3 = Tex("orthophoto maps 1:10 000").scale(0.8).shift(band_shift(4) + RIGHT * 3.1 + DOWN * 0.1)
        self.play(Create(a_box))
        self.play(Write(a1))
        self.play(Write(a2))
        self.play(Write(a3))
        self.wait(2)
        st1 = Tex("Strengths: vast areas, repeats, detects change").scale(0.9).shift(band_shift(4) + DOWN * 1.4)
        st2 = Tex("Limits: clouds, interpretation,").scale(0.9).shift(band_shift(4) + DOWN * 2.2)
        st3 = Tex("counts roofs, not names").scale(0.95).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(st1))
        self.wait(2)
        self.play(Write(st2))
        self.play(Write(st3))
        self.play(Create(SurroundingRectangle(st3, color=GREEN)))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): population work in South Africa ---
        self.next_band(5)
        b5_title = Tex("The toolkit at work on population").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        p1 = Tex("Informal settlements: new roofs on images").scale(0.95).shift(band_shift(5) + UP * 1.2)
        p1b = Tex("$\\to$ GIS layer $\\to$ map of unserved homes").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(p1))
        self.play(Write(p1b))
        self.wait(2.5)
        p2 = Tex("Census: images ensure no dwelling missed").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(p2))
        self.wait(2)
        p3 = Tex("KZN floods 2022: before-and-after images").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        p3b = Tex("found damage while roads were cut").scale(0.95).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(p3))
        self.play(Write(p3b))
        self.wait(2)
        p4 = Tex("Infrared crop health; SANSA, SumbandilaSat").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(p4))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): the smartphone map ---
        self.next_band(6)
        b6_title = Tex("The GIS in your pocket").scale(1.15).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Nearest pizza: captured, stored,").scale(1.0).shift(band_shift(6) + UP * 1.3)
        b6_l2 = Tex("analysed, displayed — a GIS ran").scale(1.0).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Hardware: phone. Software: the app.").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        b6_l4 = Tex("Data: every road and shop. People: you.").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        b6_l5 = Tex("Procedures: the update rules.").scale(0.95).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.wait(2)
        self.play(Write(b6_l5))
        self.wait(2)
        b6_l6 = Tex("Pin = spatial; menu and rating = attribute").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(2.5)

        # --- Band 7 (subtopic_6): a lasagne of maps ---
        self.next_band(7)
        b7_title = Tex("A lasagne of maps").scale(1.2).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(2)
        for i, nm in enumerate(["rivers", "roads", "towns", "density", "clinics"]):
            y = 1.4 - i * 0.7
            sheet = Rectangle(width=4.6, height=0.55).shift(band_shift(7) + LEFT * 2.8 + UP * y)
            lab = Tex(nm).scale(0.75).shift(band_shift(7) + LEFT * 2.8 + UP * y)
            self.play(Create(sheet), Write(lab), run_time=0.7)
        self.wait(1.5)
        h1 = Tex("Hold the stack to the light:").scale(0.9).shift(band_shift(7) + RIGHT * 3.3 + UP * 1.1)
        h2 = Tex("dense people, no clinic —").scale(0.9).shift(band_shift(7) + RIGHT * 3.3 + UP * 0.3)
        h3 = Tex("underserved, in a second").scale(0.9).shift(band_shift(7) + RIGHT * 3.3 + DOWN * 0.5)
        self.play(Write(h1))
        self.play(Write(h2))
        self.play(Write(h3))
        self.wait(2.5)
        b7_l1 = Tex("Only as good as its ingredients:").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        b7_l2 = Tex("a GIS never makes old data true").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)

        # --- Band 8 (subtopic_7): the eye in the sky and the census ---
        self.next_band(8)
        b8_title = Tex("The eye in the sky and the census").scale(1.1).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Satellite: sees everywhere, returns often,").scale(0.95).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex("lines up images like frames of a film").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Healthy plants shout in infrared").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("New roofs $\\to$ layer $\\to$ services follow;").scale(0.95).shift(band_shift(8) + DOWN * 1.3)
        b8_l5 = Tex("images put every dwelling in the count").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l4))
        self.wait(2)
        self.play(Write(b8_l5))
        self.wait(2)
        b8_l6 = Tex("Satellite counts roofs; the census asks names").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(3)
