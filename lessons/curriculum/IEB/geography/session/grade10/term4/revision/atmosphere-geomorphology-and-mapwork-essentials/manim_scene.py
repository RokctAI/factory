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

# Band-layout whiteboard scene for the Grade 10 physical-geography revision
# session "Atmosphere, Geomorphology and Mapwork Essentials" (Part 1 —
# Expert subtopics 1-4, Part 2 — Simplifier 5-7). Exporter-safe primitives
# only: the orographic mountain and the layer stack are Line builds, the
# contour rings are Circles, and the station model is Circle+Line+Tex.
# Add-only lifecycle; camera moves down band by band. Band time apportioned
# to subtopics.json (250/245/255/250/190/190/180 of 1560 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class Grade10PhysicalRevisionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(13)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): what the air is made of ---
        title = Tex("Physical Geography: the Year in One Line").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        g1 = Tex("Nitrogen $\\approx 78\\%$, Oxygen $\\approx 21\\%$, Argon $<1\\%$").scale(0.95).shift(UP * 1.0)
        self.play(Write(g1))
        self.wait(2)
        g2 = Tex("Trace gases with outsized jobs:").scale(0.95).shift(UP * 0.1)
        g3 = Tex("CO$_2$ ($\\approx 0.04\\%$) + water vapour trap heat;").scale(0.9).shift(DOWN * 0.7)
        g4 = Tex("ozone blocks ultraviolet").scale(0.9).shift(DOWN * 1.5)
        self.play(Write(g2))
        self.play(Write(g3))
        self.play(Write(g4))
        self.play(Create(SurroundingRectangle(VGroup(g3, g4), color=GREEN)))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the four layers, stacked ---
        self.next_band(1)
        b1_title = Tex("Four layers, by temperature behaviour").scale(1.1).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_title))
        self.wait(1.5)
        layers = [
            ("Troposphere: weather; cools 6.5$^{\\circ}$C/km", -1.9),
            ("Stratosphere: ozone; WARMS with height", -0.9),
            ("Mesosphere: coldest; meteors burn", 0.1),
            ("Thermosphere: thin air, soaring heat", 1.1),
        ]
        base_y = -2.6
        for i, (lab, y) in enumerate(layers):
            ln = Line(band_shift(1) + LEFT * 5.2 + UP * (base_y + i * 1.0 + 0.5),
                      band_shift(1) + RIGHT * 1.2 + UP * (base_y + i * 1.0 + 0.5),
                      stroke_width=4, color=BLUE)
            t = Tex(lab).scale(0.75).shift(band_shift(1) + LEFT * 1.6 + UP * y)
            self.play(Create(ln), run_time=0.5)
            self.play(Write(t))
            self.wait(1.2)
        n1 = Tex("Sunscreen up there,").scale(0.85).shift(band_shift(1) + RIGHT * 4.3 + UP * 0.4)
        n2 = Tex("weather down here").scale(0.85).shift(band_shift(1) + RIGHT * 4.3 + DOWN * 0.3)
        self.play(Write(n1), Write(n2))
        self.wait(2.5)

        # --- Band 2 (subtopic_1): heated from below ---
        self.next_band(2)
        b2_title = Tex("Heated from below").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        ground = Line(band_shift(2) + LEFT * 5.5 + DOWN * 2.0, band_shift(2) + RIGHT * 5.5 + DOWN * 2.0,
                      stroke_width=6)
        self.play(Create(ground))
        sw = Arrow(band_shift(2) + LEFT * 3.5 + UP * 2.0, band_shift(2) + LEFT * 2.2 + DOWN * 1.8,
                   buff=0, color=YELLOW, stroke_width=5)
        sw_lab = Tex("shortwave in ($\\approx$half arrives)").scale(0.75).shift(band_shift(2) + LEFT * 4.2 + UP * 1.2)
        lw = Arrow(band_shift(2) + RIGHT * 2.2 + DOWN * 1.8, band_shift(2) + RIGHT * 3.5 + UP * 1.6,
                   buff=0, color=RED, stroke_width=5)
        lw_lab = Tex("longwave out (greenhouse gases catch it)").scale(0.75).shift(band_shift(2) + RIGHT * 2.9 + UP * 2.0)
        self.play(Create(sw), Write(sw_lab))
        self.wait(1.5)
        self.play(Create(lw), Write(lw_lab))
        self.wait(2)
        h1 = Tex("Radiation, conduction, convection, advection").scale(0.9).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(h1))
        self.play(Create(SurroundingRectangle(h1, color=GREEN)))
        self.wait(2)
        h2 = Tex("Factors: latitude, altitude, sea distance,").scale(0.85).shift(band_shift(2) + UP * 0.2)
        h3 = Tex("Agulhas vs Benguela, aspect").scale(0.85).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(h2))
        self.play(Write(h3))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): moisture and clouds ---
        self.next_band(3)
        b3_title = Tex("Vapour to cloud").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        m1 = Tex("Relative humidity: \\% of what this").scale(0.9).shift(band_shift(3) + UP * 1.4)
        m2 = Tex("temperature of air COULD carry").scale(0.9).shift(band_shift(3) + UP * 0.6)
        self.play(Write(m1))
        self.play(Write(m2))
        self.wait(2)
        m3 = Tex("Cool to DEW POINT $\\to$ saturation $\\to$ condensation").scale(0.85).shift(band_shift(3) + DOWN * 0.3)
        self.play(Write(m3))
        self.play(Create(SurroundingRectangle(m3, color=GREEN)))
        self.wait(2)
        m4 = Tex("Cirrus: icy streaks. Cumulus: heaped towers").scale(0.85).shift(band_shift(3) + DOWN * 1.3)
        m5 = Tex("(cumulonimbus = thunder). Stratus: grey drizzle").scale(0.85).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(m4))
        self.play(Write(m5))
        self.wait(2)
        m6 = Tex("All real rain needs RISING air").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(m6))
        self.wait(2.5)

        # --- Band 4 (subtopic_2): three rainfall types, with the mountain ---
        self.next_band(4)
        b4_title = Tex("Three lifts, three rainfall types").scale(1.1).shift(band_shift(4) + UP * 2.5)
        self.play(Write(b4_title))
        self.wait(1.5)
        # orographic mountain: two-line profile
        base_l = band_shift(4) + LEFT * 4.6 + DOWN * 0.6
        peak = band_shift(4) + LEFT * 0.6 + UP * 1.6
        base_r = band_shift(4) + RIGHT * 3.4 + DOWN * 0.6
        slope1 = Line(base_l, peak, stroke_width=5)
        slope2 = Line(peak, base_r, stroke_width=5)
        self.play(Create(slope1), Create(slope2))
        wind = Arrow(band_shift(4) + LEFT * 6.0 + UP * 0.2, band_shift(4) + LEFT * 3.4 + UP * 1.0,
                     buff=0, color=BLUE, stroke_width=5)
        w_lab = Tex("moist air climbs, rains").scale(0.75).shift(band_shift(4) + LEFT * 4.0 + UP * 1.9)
        self.play(Create(wind), Write(w_lab))
        dry = Arrow(band_shift(4) + RIGHT * 0.2 + UP * 1.0, band_shift(4) + RIGHT * 2.8 + UP * 0.0,
                    buff=0, color=RED, stroke_width=5)
        d_lab = Tex("descends dry: rain shadow").scale(0.75).shift(band_shift(4) + RIGHT * 3.3 + UP * 1.5)
        self.play(Create(dry), Write(d_lab))
        self.wait(2.5)
        t1 = Tex("Convectional: Bloemfontein's four o'clock storm").scale(0.9).shift(band_shift(4) + DOWN * 1.4)
        t2 = Tex("Orographic: green George, dry Oudtshoorn").scale(0.9).shift(band_shift(4) + DOWN * 2.2)
        t3 = Tex("Frontal: Cape Town's soaked winter").scale(0.9).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(t1))
        self.wait(2)
        self.play(Write(t2))
        self.wait(2)
        self.play(Write(t3))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): plates and boundaries ---
        self.next_band(5)
        b5_title = Tex("Plates and their three moves").scale(1.1).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        p1 = Tex("Crust + upper mantle = lithosphere plates").scale(0.9).shift(band_shift(5) + UP * 1.4)
        p2 = Tex("riding mantle convection currents").scale(0.9).shift(band_shift(5) + UP * 0.6)
        self.play(Write(p1))
        self.play(Write(p2))
        self.wait(2)
        p3 = Tex("Wegener: jigsaw fit, Mesosaurus and Glossopteris,").scale(0.85).shift(band_shift(5) + DOWN * 0.3)
        p4 = Tex("matching rocks, glacial scars in warm lands").scale(0.85).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(p3))
        self.play(Write(p4))
        self.wait(2.5)
        p5 = Tex("Apart: ridges, rifts. Together: subduction,").scale(0.85).shift(band_shift(5) + DOWN * 2.0)
        p6 = Tex("Andes, Japan, Himalayas. Past: San Andreas quakes").scale(0.85).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(p5))
        self.play(Write(p6))
        self.play(Create(SurroundingRectangle(p6, color=GREEN)))
        self.wait(2.5)

        # --- Band 6 (subtopic_3): folds, faults, quakes, volcanoes ---
        self.next_band(6)
        b6_title = Tex("Bend, snap, shake, erupt").scale(1.1).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        f1 = Tex("Bend slowly: anticline up, syncline down —").scale(0.85).shift(band_shift(6) + UP * 1.4)
        f2 = Tex("Cape Fold ranges, $\\approx 300$ million years old").scale(0.85).shift(band_shift(6) + UP * 0.6)
        self.play(Write(f1))
        self.play(Write(f2))
        self.wait(2)
        f3 = Tex("Snap: normal and reverse faults;").scale(0.85).shift(band_shift(6) + DOWN * 0.3)
        f4 = Tex("graben (East African Rift) and horst").scale(0.85).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(f3))
        self.play(Write(f4))
        self.wait(2)
        f5 = Tex("Quake: focus below, epicentre above;").scale(0.85).shift(band_shift(6) + DOWN * 2.0)
        f6 = Tex("magnitude = energy, Mercalli = effects").scale(0.85).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(f5))
        self.play(Write(f6))
        self.play(Create(SurroundingRectangle(f6, color=GREEN)))
        self.wait(2)
        f7 = Tex("Shield: runny lava. Composite: sticky, explosive").scale(0.85).shift(band_shift(6) + DOWN * 3.6)
        self.play(Write(f7))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): scale, declination, contours ---
        self.next_band(7)
        b7_title = Tex("Mapwork: scale and contours").scale(1.1).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7_title))
        self.wait(1.5)
        s1 = Tex("1:50 000 $\\Rightarrow$ 2 cm = 1 km; interval 20 m").scale(0.9).shift(band_shift(7) + UP * 1.5)
        self.play(Write(s1))
        self.play(Create(SurroundingRectangle(s1, color=GREEN)))
        self.wait(2)
        s2 = Tex("True north vs magnetic north: the declination").scale(0.85).shift(band_shift(7) + UP * 0.5)
        self.play(Write(s2))
        self.wait(2)
        # contour rings: nested circles for a summit
        c_outer = Circle(radius=1.6, color=BLUE, stroke_width=4).shift(band_shift(7) + LEFT * 3.0 + DOWN * 1.7)
        c_mid = Circle(radius=1.0, color=BLUE, stroke_width=4).shift(band_shift(7) + LEFT * 3.0 + DOWN * 1.7)
        c_inner = Circle(radius=0.45, color=BLUE, stroke_width=4).shift(band_shift(7) + LEFT * 3.0 + DOWN * 1.7)
        self.play(Create(c_outer))
        self.play(Create(c_mid))
        self.play(Create(c_inner))
        ring_lab = Tex("rings in, height up: a summit").scale(0.75).shift(band_shift(7) + LEFT * 3.0 + DOWN * 3.6)
        self.play(Write(ring_lab))
        self.wait(2)
        s3 = Tex("Crowded = steep; spaced = gentle;").scale(0.85).shift(band_shift(7) + RIGHT * 3.0 + DOWN * 1.3)
        s4 = Tex("valley V points upstream").scale(0.85).shift(band_shift(7) + RIGHT * 3.0 + DOWN * 2.1)
        self.play(Write(s3))
        self.play(Write(s4))
        self.wait(2.5)

        # --- Band 8 (subtopic_4): gradient worked + station model ---
        self.next_band(8)
        b8_title = Tex("Gradient, and the station model").scale(1.1).shift(band_shift(8) + UP * 2.5)
        self.play(Write(b8_title))
        self.wait(1.5)
        g8a = MathTex(r"1220 - 1060 = 160 \text{ m rise}").scale(0.9).shift(band_shift(8) + UP * 1.5)
        g8b = MathTex(r"4.8 \text{ cm} \times 0.5 = 2.4 \text{ km} = 2400 \text{ m}").scale(0.9).shift(band_shift(8) + UP * 0.6)
        g8c = MathTex(r"2400 / 160 = 15 \Rightarrow \text{gradient } 1\text{ in }15").scale(0.9).shift(band_shift(8) + DOWN * 0.3)
        self.play(Write(g8a))
        self.wait(1.5)
        self.play(Write(g8b))
        self.wait(1.5)
        self.play(Write(g8c))
        self.play(Create(SurroundingRectangle(g8c, color=GREEN)))
        self.wait(2.5)
        # station model: circle, wind shaft, temps
        st = Circle(radius=0.55, color=WHITE, stroke_width=4).shift(band_shift(8) + LEFT * 2.5 + DOWN * 2.3)
        shaft = Line(band_shift(8) + LEFT * 2.5 + DOWN * 2.3 + UP * 0.55,
                     band_shift(8) + LEFT * 3.6 + DOWN * 1.0, stroke_width=4)
        self.play(Create(st), Create(shaft))
        t_lab = Tex("18").scale(0.7).shift(band_shift(8) + LEFT * 3.5 + DOWN * 2.0)
        dp_lab = Tex("16").scale(0.7).shift(band_shift(8) + LEFT * 3.5 + DOWN * 2.8)
        self.play(Write(t_lab), Write(dp_lab))
        st_lab = Tex("cloud in eighths; shaft from the wind's origin;").scale(0.75).shift(band_shift(8) + RIGHT * 2.4 + DOWN * 2.0)
        st_lab2 = Tex("temp and dew point close $\\Rightarrow$ rain near").scale(0.75).shift(band_shift(8) + RIGHT * 2.4 + DOWN * 2.7)
        self.play(Write(st_lab))
        self.play(Write(st_lab2))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): the tar road at noon ---
        self.next_band(9)
        b9_title = Tex("The tar road at noon").scale(1.15).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        r1 = Tex("The shimmer: ground heats air — from below").scale(0.9).shift(band_shift(9) + UP * 1.3)
        r2 = Tex("The sweating can: cooled air passes dew point").scale(0.9).shift(band_shift(9) + UP * 0.5)
        self.play(Write(r1))
        self.wait(2)
        self.play(Write(r2))
        self.wait(2.5)
        r3 = Tex("Three lifts: hot floor (Bloemfontein),").scale(0.9).shift(band_shift(9) + DOWN * 0.4)
        r4 = Tex("wall (George/Oudtshoorn), wedge (Cape front)").scale(0.9).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(r3))
        self.play(Write(r4))
        self.wait(2.5)
        r5 = Tex("Blanket keeps heat in; sunscreen keeps UV out").scale(0.9).shift(band_shift(9) + DOWN * 2.2)
        self.play(Write(r5))
        self.play(Create(SurroundingRectangle(r5, color=GREEN)))
        self.wait(2.5)

        # --- Band 10 (subtopic_6): the dry mud pan ---
        self.next_band(10)
        b10_title = Tex("The dry mud pan").scale(1.15).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        e1 = Tex("Cracked plates on soft creeping mud beneath").scale(0.9).shift(band_shift(10) + UP * 1.3)
        e2 = Tex("Three moves: apart (rift), together (crumple),").scale(0.9).shift(band_shift(10) + UP * 0.5)
        e3 = Tex("past (locked strain, then the jolt)").scale(0.9).shift(band_shift(10) + DOWN * 0.3)
        self.play(Write(e1))
        self.wait(2)
        self.play(Write(e2))
        self.play(Write(e3))
        self.wait(2.5)
        e4 = Tex("Rug pushed = folds; ruler snapped = fault").scale(0.9).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(e4))
        self.play(Create(SurroundingRectangle(e4, color=GREEN)))
        self.wait(2)
        e5 = Tex("Focus below, epicentre above;").scale(0.9).shift(band_shift(10) + DOWN * 2.2)
        e6 = Tex("one magnitude, many intensities").scale(0.9).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(e5))
        self.play(Write(e6))
        self.wait(2.5)

        # --- Band 11 (subtopic_7): the dam in a drought ---
        self.next_band(11)
        b11_title = Tex("The dam in a drought").scale(1.15).shift(band_shift(11) + UP * 2.3)
        self.play(Write(b11_title))
        self.wait(2)
        w1 = Tex("Falling water leaves rings: contours —").scale(0.9).shift(band_shift(11) + UP * 1.3)
        w2 = Tex("crowded rings steep, spaced rings gentle").scale(0.9).shift(band_shift(11) + UP * 0.5)
        self.play(Write(w1))
        self.play(Write(w2))
        self.wait(2.5)
        w3 = Tex("Spoken gradient: 160 m rise, 2 400 m distance,").scale(0.9).shift(band_shift(11) + DOWN * 0.4)
        w4 = Tex("2400 over 160 gives 15 — say 1 in 15").scale(0.9).shift(band_shift(11) + DOWN * 1.2)
        self.play(Write(w3))
        self.play(Write(w4))
        self.play(Create(SurroundingRectangle(w4, color=GREEN)))
        self.wait(2.5)
        w5 = Tex("Scorecard: cloud eighths, wind shaft, temp and").scale(0.85).shift(band_shift(11) + DOWN * 2.1)
        w6 = Tex("dew point; front passes — SW wind, cold, showers").scale(0.85).shift(band_shift(11) + DOWN * 2.9)
        self.play(Write(w5))
        self.play(Write(w6))
        self.wait(3)
