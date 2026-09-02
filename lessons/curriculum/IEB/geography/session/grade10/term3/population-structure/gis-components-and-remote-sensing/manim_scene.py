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
        d1 = Tex("GIS: captures, stores, analyses,").scale(1.05).shift(UP * 1.0)
        d2 = Tex("manages and displays information...").scale(1.05).shift(UP * 0.2)
        d3 = Tex("...that is GEOREFERENCED").scale(1.1).shift(DOWN * 0.7)
        self.play(Write(d1))
        self.play(Write(d2))
        self.wait(2)
        self.play(Write(d3))
        self.play(Create(SurroundingRectangle(d3, color=GREEN)))
        self.wait(2)
        d4 = Tex("A list of hospitals + coordinates").scale(1.0).shift(DOWN * 1.7)
        d5 = Tex("= geographical information").scale(1.0).shift(DOWN * 2.5)
        self.play(Write(d4))
        self.play(Write(d5))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): layers, overlay, spatial vs attribute ---
        self.next_band(1)
        b1_title = Tex("The layer principle").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        # stacked transparent sheets, drawn one at a time
        names = ["rivers", "roads", "homesteads", "density", "schools"]
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
        q1 = Tex("Where should the next school go?").scale(0.9).shift(band_shift(1) + RIGHT * 3.4 + DOWN * 0.5)
        self.play(Write(q1))
        self.wait(2)
        sp = Tex("Spatial data: where, and what shape").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
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
        c2 = Tex("2. Software: QGIS, ArcGIS, map apps").scale(1.0).shift(band_shift(2) + UP * 0.4)
        c3 = Tex("3. DATA: most valuable, most costly").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        c4 = Tex("4. People: capture, analyse, decide").scale(1.0).shift(band_shift(2) + DOWN * 1.2)
        c5 = Tex("5. Procedures: updates, checks, records").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
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
        c6 = Tex("Engine, fuel, steering, service manual").scale(1.0).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(c6))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): remote sensing and reflection ---
        self.next_band(3)
        b3_title = Tex("Remote sensing: no contact").scale(1.15).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_title))
        self.wait(1.5)
        # ground line, satellite box, energy arrows down and up
        ground = Line(band_shift(3) + LEFT * 5.0 + DOWN * 2.0, band_shift(3) + RIGHT * 5.0 + DOWN * 2.0,
                      stroke_width=5)
        sat = Rectangle(width=1.6, height=0.8).shift(band_shift(3) + RIGHT * 3.2 + UP * 1.6)
        sat_l = Tex("sensor").scale(0.7).shift(band_shift(3) + RIGHT * 3.2 + UP * 1.6)
        self.play(Create(ground))
        self.play(Create(sat), Write(sat_l))
        self.wait(1.5)
        sun_a = Arrow(band_shift(3) + LEFT * 3.8 + UP * 1.8, band_shift(3) + LEFT * 1.6 + DOWN * 1.8,
                      buff=0, color=YELLOW, stroke_width=5)
        sun_l = Tex("sun's energy").scale(0.8).shift(band_shift(3) + LEFT * 4.0 + UP * 2.2)
        refl_a = Arrow(band_shift(3) + LEFT * 1.2 + DOWN * 1.8, band_shift(3) + RIGHT * 2.6 + UP * 1.2,
                       buff=0, color=BLUE, stroke_width=5)
        refl_l = Tex("reflection, each surface its own").scale(0.8).shift(band_shift(3) + RIGHT * 1.2 + DOWN * 0.2)
        self.play(Create(sun_a), Write(sun_l))
        self.wait(1.5)
        self.play(Create(refl_a), Write(refl_l))
        self.wait(2)
        b3_l1 = Tex("Sensors read invisible wavelengths:").scale(0.95).shift(band_shift(3) + DOWN * 2.6)
        b3_l2 = Tex("infrared shows crop stress before wilting").scale(0.95).shift(band_shift(3) + DOWN * 3.3)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): satellite vs aerial; strengths and limits ---
        self.next_band(4)
        b4_title = Tex("Satellite vs aerial").scale(1.2).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        s_box = Rectangle(width=5.6, height=2.4).shift(band_shift(4) + LEFT * 3.1 + UP * 0.7)
        s_1 = Tex("Satellite: Landsat, Sentinel").scale(0.8).shift(band_shift(4) + LEFT * 3.1 + UP * 1.3)
        s_2 = Tex("vast areas, fixed revisit,").scale(0.8).shift(band_shift(4) + LEFT * 3.1 + UP * 0.6)
        s_3 = Tex("time series of change").scale(0.8).shift(band_shift(4) + LEFT * 3.1 + UP * 0.0)
        self.play(Create(s_box))
        self.play(Write(s_1))
        self.play(Write(s_2))
        self.play(Write(s_3))
        self.wait(2)
        a_box = Rectangle(width=5.6, height=2.4).shift(band_shift(4) + RIGHT * 3.1 + UP * 0.7)
        a_1 = Tex("Aerial: low, small area,").scale(0.8).shift(band_shift(4) + RIGHT * 3.1 + UP * 1.3)
        a_2 = Tex("fine detail; orthophotos").scale(0.8).shift(band_shift(4) + RIGHT * 3.1 + UP * 0.6)
        a_3 = Tex("$\\to$ 1:10 000 map series").scale(0.8).shift(band_shift(4) + RIGHT * 3.1 + UP * 0.0)
        self.play(Create(a_box))
        self.play(Write(a_1))
        self.play(Write(a_2))
        self.play(Write(a_3))
        self.wait(2)
        b4_l1 = Tex("Strengths: reach, repetition, economy").scale(0.95).shift(band_shift(4) + DOWN * 1.4)
        b4_l2 = Tex("Limits: cloud, interpretation needed,").scale(0.95).shift(band_shift(4) + DOWN * 2.2)
        b4_l3 = Tex("counts roofs, never people").scale(0.95).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): population work in South Africa ---
        self.next_band(5)
        b5_title = Tex("Pointed at population").scale(1.2).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(1.5)
        p1 = Tex("New roofs on the informal fringe").scale(0.95).shift(band_shift(5) + UP * 1.3)
        p1b = Tex("$\\to$ layer $\\to$ overlay $\\to$ services").scale(0.95).shift(band_shift(5) + UP * 0.6)
        self.play(Write(p1))
        self.play(Write(p1b))
        self.wait(2)
        p2 = Tex("Census: enumeration areas from imagery,").scale(0.95).shift(band_shift(5) + DOWN * 0.2)
        p2b = Tex("every dwelling on someone's map").scale(0.95).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(p2))
        self.play(Write(p2b))
        self.wait(2)
        p3 = Tex("Knysna fires 2017: burn scars mapped;").scale(0.95).shift(band_shift(5) + DOWN * 1.7)
        p3b = Tex("Theewaterskloof: the drought, watched").scale(0.95).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(p3))
        self.play(Write(p3b))
        self.wait(2)
        p4 = Tex("SANSA at Hartebeesthoek; ZACube-2").scale(0.95).shift(band_shift(5) + DOWN * 3.2)
        self.play(Write(p4))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): the smartphone map ---
        self.next_band(6)
        b6_title = Tex("The GIS in your pocket").scale(1.2).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(2)
        m1 = Tex("Find an open pharmacy on a Sunday:").scale(1.0).shift(band_shift(6) + UP * 1.3)
        m2 = Tex("captured, stored, analysed, displayed").scale(1.0).shift(band_shift(6) + UP * 0.5)
        self.play(Write(m1))
        self.play(Write(m2))
        self.play(Create(SurroundingRectangle(m2, color=GREEN)))
        self.wait(2.5)
        m3 = Tex("Hardware: phone. Software: the app.").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        m4 = Tex("Data: every street and opening time.").scale(0.95).shift(band_shift(6) + DOWN * 1.1)
        m5 = Tex("People: you. Procedures: update rules.").scale(0.95).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(m3))
        self.wait(1.5)
        self.play(Write(m4))
        self.wait(1.5)
        self.play(Write(m5))
        self.wait(2)
        m6 = Tex("Pin = spatial; name and hours = attribute").scale(0.95).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(m6))
        self.wait(2.5)

        # --- Band 7 (subtopic_6): a stack of tracing paper ---
        self.next_band(7)
        b7_title = Tex("A stack of tracing paper").scale(1.2).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(2)
        for i, nm in enumerate(["rivers", "gravel roads", "homesteads", "density", "schools"]):
            y = 1.4 - i * 0.7
            sheet = Rectangle(width=4.6, height=0.55).shift(band_shift(7) + LEFT * 2.8 + UP * y)
            lab = Tex(nm).scale(0.75).shift(band_shift(7) + LEFT * 2.8 + UP * y)
            self.play(Create(sheet), Write(lab), run_time=0.7)
        self.wait(1.5)
        h1 = Tex("Press the pile to the window:").scale(0.9).shift(band_shift(7) + RIGHT * 3.3 + UP * 1.1)
        h2 = Tex("crowded homesteads, no school —").scale(0.9).shift(band_shift(7) + RIGHT * 3.3 + UP * 0.3)
        h3 = Tex("long walks, seen in a glance").scale(0.9).shift(band_shift(7) + RIGHT * 3.3 + DOWN * 0.5)
        self.play(Write(h1))
        self.play(Write(h2))
        self.play(Write(h3))
        self.wait(2.5)
        b7_l1 = Tex("Bad ingredients, bad result:").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        b7_l2 = Tex("a GIS makes stale data look authoritative").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)

        # --- Band 8 (subtopic_7): the eye in the sky and the census ---
        self.next_band(8)
        b8_title = Tex("The eye in the sky and the census").scale(1.1).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        e1 = Tex("Satellite: huge view, returns for years —").scale(0.95).shift(band_shift(8) + UP * 1.3)
        e2 = Tex("Theewaterskloof shrinking, frame by frame").scale(0.95).shift(band_shift(8) + UP * 0.6)
        self.play(Write(e1))
        self.play(Write(e2))
        self.wait(2)
        e3 = Tex("Aircraft: low and sharp — orthophotos").scale(0.95).shift(band_shift(8) + DOWN * 0.2)
        self.play(Write(e3))
        self.wait(2)
        e4 = Tex("Infrared: thriving maize blazes,").scale(0.95).shift(band_shift(8) + DOWN * 1.0)
        e4b = Tex("failing maize dims").scale(0.95).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(e4))
        self.play(Write(e4b))
        self.wait(2)
        e5 = Tex("New roofs $\\to$ services; imagery $\\to$ census areas").scale(0.9).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(e5))
        self.wait(2)
        e6 = Tex("Roofs, never people: someone still knocks").scale(0.95).shift(band_shift(8) + DOWN * 3.3)
        self.play(Write(e6))
        self.play(Create(SurroundingRectangle(e6, color=GREEN)))
        self.wait(3)
