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

# Band-layout whiteboard scene for the revision session "Atmosphere,
# Geomorphology and Mapwork Essentials" (Part 1 — Expert subtopics 1-4,
# Part 2 — Simplifier 5-7). Exporter-safe primitives only: the atmosphere's
# four layers are a stack of Rectangles, the orographic-rain mountain is a
# two-Line profile with Arrows, and the gradient calculation is written line
# by line in MathTex with the NSC 1-in-20 answer boxed. Add-only lifecycle;
# camera moves down band by band. Band time apportioned to subtopics.json
# (250/245/255/250/190/190/180 of 1560 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class Grade10PhysicalRevisionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): what the air is ---
        title = Tex("Grade 10 Physical Geography Revision").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        g1 = Tex("Nitrogen $\\approx 78\\%$, Oxygen $\\approx 21\\%$").scale(1.05).shift(UP * 1.0)
        self.play(Write(g1))
        self.wait(2)
        g2 = Tex("Traces that matter: CO$_2$ 0,04\\%,").scale(1.0).shift(UP * 0.1)
        g3 = Tex("water vapour 0--4\\%, ozone").scale(1.0).shift(DOWN * 0.7)
        self.play(Write(g2))
        self.play(Write(g3))
        self.wait(2)
        g4 = Tex("CO$_2$ + vapour absorb outgoing heat;").scale(0.95).shift(DOWN * 1.7)
        g5 = Tex("ozone absorbs incoming ultraviolet").scale(0.95).shift(DOWN * 2.5)
        self.play(Write(g4))
        self.play(Write(g5))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the four layers, stacked ---
        self.next_band(1)
        b1_title = Tex("Four layers, four behaviours").scale(1.15).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_title))
        self.wait(1.5)
        layers = [
            ("troposphere: weather, temp FALLS", -1.9),
            ("stratosphere: ozone, temp RISES", -0.7),
            ("mesosphere: coldest, meteors burn", 0.5),
            ("thermosphere: temp climbs steeply", 1.7),
        ]
        for name, y in layers:
            box = Rectangle(width=8.6, height=1.1).shift(band_shift(1) + LEFT * 1.2 + UP * y)
            lab = Tex(name).scale(0.85).shift(band_shift(1) + LEFT * 1.2 + UP * y)
            self.play(Create(box), Write(lab))
            self.wait(1.2)
        n1 = Tex("lapse rate").scale(0.75).shift(band_shift(1) + RIGHT * 4.7 + DOWN * 1.6)
        n2 = Tex("6,5$^\\circ$C/km").scale(0.75).shift(band_shift(1) + RIGHT * 4.7 + DOWN * 2.2)
        self.play(Write(n1), Write(n2))
        self.wait(2)
        n3 = Tex("Ozone layer = the shield (Montreal Protocol)").scale(0.9).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(n3))
        self.wait(2.5)

        # --- Band 2 (subtopic_1): heated from below ---
        self.next_band(2)
        b2_title = Tex("Heated from BELOW").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.play(Create(SurroundingRectangle(b2_title, color=GREEN)))
        self.wait(2)
        h1 = Tex("Shortwave insolation in, about half reaches ground;").scale(0.9).shift(band_shift(2) + UP * 1.2)
        h2 = Tex("warm surface radiates LONGWAVE back up").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(h1))
        self.play(Write(h2))
        self.wait(2.5)
        h3 = Tex("Radiation, conduction, convection, advection").scale(0.95).shift(band_shift(2) + DOWN * 0.5)
        self.play(Write(h3))
        self.wait(2)
        h4 = Tex("Greenhouse effect: natural, keeps us above $-18^\\circ$C;").scale(0.9).shift(band_shift(2) + DOWN * 1.4)
        h5 = Tex("ENHANCED greenhouse = the warming problem").scale(0.9).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(h4))
        self.play(Write(h5))
        self.wait(2)
        h6 = Tex("Joburg at 1 700 m cooler than Durban: altitude").scale(0.9).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(h6))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): moisture and clouds ---
        self.next_band(3)
        b3_title = Tex("Moisture: the road to rain").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        m1 = Tex("Relative humidity: vapour held as \\% of").scale(0.95).shift(band_shift(3) + UP * 1.2)
        m2 = Tex("the maximum at that temperature").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(m1))
        self.play(Write(m2))
        self.wait(2)
        m3 = Tex("Cool to DEW POINT: saturation, then condensation").scale(0.9).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(m3))
        self.play(Create(SurroundingRectangle(m3, color=GREEN)))
        self.wait(2.5)
        m4 = Tex("Cirrus: high wisps. Cumulus: heaped towers").scale(0.9).shift(band_shift(3) + DOWN * 1.5)
        m5 = Tex("(cumulonimbus = thunder). Stratus: grey layers").scale(0.9).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(m4))
        self.play(Write(m5))
        self.wait(2)
        m6 = Tex("All significant rain needs air to RISE").scale(0.95).shift(band_shift(3) + DOWN * 3.1)
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
        w_lab = Tex("moist air rises, rains").scale(0.75).shift(band_shift(4) + LEFT * 4.0 + UP * 1.9)
        self.play(Create(wind), Write(w_lab))
        dry = Arrow(band_shift(4) + RIGHT * 0.2 + UP * 1.0, band_shift(4) + RIGHT * 2.8 + UP * 0.0,
                    buff=0, color=RED, stroke_width=5)
        d_lab = Tex("descends dry: rain shadow").scale(0.75).shift(band_shift(4) + RIGHT * 3.3 + UP * 1.5)
        self.play(Create(dry), Write(d_lab))
        self.wait(2.5)
        t1 = Tex("Convectional: Highveld afternoon thunderstorm").scale(0.9).shift(band_shift(4) + DOWN * 1.4)
        t2 = Tex("Orographic: wet Drakensberg face, dry interior").scale(0.9).shift(band_shift(4) + DOWN * 2.2)
        t3 = Tex("Frontal: Western Cape winter cold fronts").scale(0.9).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(t1))
        self.wait(2)
        self.play(Write(t2))
        self.wait(2)
        self.play(Write(t3))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): plates and boundaries ---
        self.next_band(5)
        b5_title = Tex("The restless crust").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        p1 = Tex("Crust, mantle, core; lithosphere plates").scale(0.95).shift(band_shift(5) + UP * 1.2)
        p2 = Tex("ride mantle convection currents").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(p1))
        self.play(Write(p2))
        self.wait(2)
        p3 = Tex("Wegener's evidence: jigsaw fit, fossils,").scale(0.9).shift(band_shift(5) + DOWN * 0.5)
        p4 = Tex("matching rocks, glacial scars").scale(0.9).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(p3))
        self.play(Write(p4))
        self.wait(2)
        p5 = Tex("Divergent: ridges, rifts. Convergent: subduction,").scale(0.85).shift(band_shift(5) + DOWN * 2.2)
        p6 = Tex("volcanoes, fold mountains. Transform: earthquakes").scale(0.85).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(p5))
        self.play(Write(p6))
        self.wait(2.5)

        # --- Band 6 (subtopic_3): folds, faults, quakes ---
        self.next_band(6)
        b6_title = Tex("Bend or snap").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        # a fold drawn as a zigzag of lines: anticline and syncline
        f_pts = [(-4.6, -0.2), (-3.2, 1.0), (-1.8, -0.2), (-0.4, 1.0), (1.0, -0.2)]
        for a, b in zip(f_pts[:-1], f_pts[1:]):
            seg = Line(band_shift(6) + RIGHT * a[0] + UP * a[1],
                       band_shift(6) + RIGHT * b[0] + UP * b[1], stroke_width=5, color=YELLOW)
            self.play(Create(seg), run_time=0.5)
        anti = Tex("anticline (up)").scale(0.75).shift(band_shift(6) + LEFT * 3.2 + UP * 1.6)
        syn = Tex("syncline (down)").scale(0.75).shift(band_shift(6) + LEFT * 1.8 + DOWN * 0.9)
        self.play(Write(anti), Write(syn))
        self.wait(2)
        q1 = Tex("Cape Fold Mountains: folded 300 Ma ago").scale(0.85).shift(band_shift(6) + RIGHT * 3.4 + UP * 0.9)
        self.play(Write(q1))
        self.wait(2)
        q2 = Tex("Normal fault (tension), reverse (compression);").scale(0.85).shift(band_shift(6) + DOWN * 1.7)
        q3 = Tex("graben = rift valley, horst = block mountain").scale(0.85).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(q2))
        self.play(Write(q3))
        self.wait(2)
        q4 = Tex("Focus below, epicentre above; Richter = energy,").scale(0.85).shift(band_shift(6) + DOWN * 3.1)
        q5 = Tex("Mercalli = observed damage").scale(0.85).shift(band_shift(6) + DOWN * 3.7)
        self.play(Write(q4))
        self.play(Write(q5))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): scale, declination, contours ---
        self.next_band(7)
        b7_title = Tex("Mapwork: the toolkit").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        s1 = Tex("1:50 000 sheet: 2 cm = 1 km;").scale(0.95).shift(band_shift(7) + UP * 1.2)
        s2 = Tex("contour interval 20 m").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(s1))
        self.play(Write(s2))
        self.wait(2)
        s3 = Tex("Magnetic declination: true bearing adjusted").scale(0.9).shift(band_shift(7) + DOWN * 0.5)
        s4 = Tex("by the current year's angle").scale(0.9).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(s3))
        self.play(Write(s4))
        self.wait(2)
        s5 = Tex("Contours never cross; close = steep;").scale(0.9).shift(band_shift(7) + DOWN * 2.2)
        s6 = Tex("river V points UPSTREAM").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(s5))
        self.play(Write(s6))
        self.play(Create(SurroundingRectangle(s6, color=GREEN)))
        self.wait(2.5)

        # --- Band 8 (subtopic_4): gradient worked + station model ---
        self.next_band(8)
        b8_title = Tex("Gradient, worked in full").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        c1 = MathTex(r"\text{gradient} = \frac{\text{vertical rise}}{\text{horizontal distance}}").scale(0.89).shift(band_shift(8) + UP * 1.1)
        self.play(Write(c1))
        self.wait(2)
        c2 = MathTex(r"= \frac{200 \text{ m}}{4\,000 \text{ m}}").scale(1.05).shift(band_shift(8) + UP * 0.0)
        self.play(Write(c2))
        self.wait(2)
        c3 = MathTex(r"= 1:20 \;\; (1 \text{ in } 20)").scale(1.1).shift(band_shift(8) + DOWN * 1.0)
        self.play(Write(c3))
        self.play(Create(SurroundingRectangle(c3, color=GREEN)))
        self.wait(2)
        c4 = Tex("Station model: cloud eighths, wind shaft + knots,").scale(0.85).shift(band_shift(8) + DOWN * 2.0)
        c5 = Tex("temp upper left, dew point lower left; isobars in hPa").scale(0.85).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(c4))
        self.play(Write(c5))
        self.wait(2)
        c6 = Tex("Cold front passes: SW wind, temp drops, pressure up").scale(0.85).shift(band_shift(8) + DOWN * 3.5)
        self.play(Write(c6))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): the pot on the stove ---
        self.next_band(9)
        b9_title = Tex("The pot on the stove").scale(1.2).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("The flame is upside down: sun heats the GROUND,").scale(0.9).shift(band_shift(9) + UP * 1.3)
        b9_l2 = Tex("the ground heats the air — from below").scale(0.95).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = Tex("Warm air = thirsty sponge; cool it to dew point").scale(0.9).shift(band_shift(9) + DOWN * 0.4)
        b9_l4 = Tex("and the water squeezes out as cloud").scale(0.9).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("Three lifts: hot ground, mountain, cold-front wedge").scale(0.9).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l5))
        self.wait(2)
        b9_l6 = Tex("Blanket (greenhouse, heat out) vs").scale(0.9).shift(band_shift(9) + DOWN * 2.9)
        b9_l7 = Tex("sunscreen (ozone, UV in)").scale(0.9).shift(band_shift(9) + DOWN * 3.6)
        self.play(Write(b9_l6))
        self.play(Write(b9_l7))
        self.wait(2.5)

        # --- Band 10 (subtopic_6): the cracked eggshell ---
        self.next_band(10)
        b10_title = Tex("The cracked eggshell").scale(1.2).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Thin cracked shell on a soft inside:").scale(0.95).shift(band_shift(10) + UP * 1.3)
        b10_l2 = Tex("plates jostled by churning mantle below").scale(0.95).shift(band_shift(10) + UP * 0.5)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Apart: ridges and rifts. Together: dive and").scale(0.9).shift(band_shift(10) + DOWN * 0.4)
        b10_l4 = Tex("volcanoes, or crumple into Himalayas.").scale(0.9).shift(band_shift(10) + DOWN * 1.2)
        b10_l5 = Tex("Past each other: earthquakes").scale(0.9).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2)
        self.play(Write(b10_l5))
        self.wait(2)
        b10_l6 = Tex("Towel pushed slowly = folds; snapped = faults;").scale(0.9).shift(band_shift(10) + DOWN * 2.8)
        b10_l7 = Tex("two rulers: magnitude vs Mercalli").scale(0.9).shift(band_shift(10) + DOWN * 3.5)
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.wait(2.5)

        # --- Band 11 (subtopic_7): the bathtub rings ---
        self.next_band(11)
        b11_title = Tex("The bathtub rings").scale(1.2).shift(band_shift(11) + UP * 2.4)
        self.play(Write(b11_title))
        self.wait(2)
        # concentric contour "rings" as circles around a summit dot
        centre = band_shift(11) + LEFT * 3.4 + UP * 0.6
        for r in (1.5, 1.0, 0.55):
            ring = Circle(radius=r, color=YELLOW).move_to(centre)
            self.play(Create(ring), run_time=0.6)
        summit = Dot(centre, color=RED)
        s_lab = Tex("summit").scale(0.7).shift(centre + UP * 1.9)
        self.play(FadeIn(summit), Write(s_lab))
        self.wait(2)
        r1 = Tex("Rings close together = steep;").scale(0.9).shift(band_shift(11) + RIGHT * 2.9 + UP * 1.1)
        r2 = Tex("far apart = gentle; V points upstream").scale(0.9).shift(band_shift(11) + RIGHT * 2.9 + UP * 0.3)
        self.play(Write(r1))
        self.play(Write(r2))
        self.wait(2.5)
        r3 = MathTex(r"4\,000 \div 200 = 20 \;\Rightarrow\; 1 \text{ in } 20").scale(1.0).shift(band_shift(11) + DOWN * 1.4)
        self.play(Write(r3))
        self.play(Create(SurroundingRectangle(r3, color=GREEN)))
        self.wait(2.5)
        r4 = Tex("Station badge: cloud, wind tail with feathers,").scale(0.85).shift(band_shift(11) + DOWN * 2.4)
        r5 = Tex("temp and dew point close together = rain near").scale(0.85).shift(band_shift(11) + DOWN * 3.1)
        self.play(Write(r4))
        self.play(Write(r5))
        self.wait(3)
