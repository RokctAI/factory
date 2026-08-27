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

# Band-layout whiteboard scene for "Water Availability in South Africa"
# (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier 5-7). Exporter-safe
# primitives only: the east-west rainfall gradient is a stepped Line profile
# with Dot+Tex markers, and the Orange river journey is an Arrow chain.
# Add-only lifecycle; camera moves down band by band. Band time apportioned
# to subtopics.json (235/240/240/235/190/185/175 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class WaterAvailabilitySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(12)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the two master numbers ---
        title = Tex("Water Availability in South Africa").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        n1 = MathTex(r"\text{SA rainfall} \approx 465 \text{ mm/yr}").scale(1.1).shift(UP * 1.0)
        n2 = MathTex(r"\text{World average} \approx 860 \text{ mm/yr}").scale(1.1).shift(UP * 0.1)
        self.play(Write(n1))
        self.play(Write(n2))
        self.play(Create(SurroundingRectangle(VGroup(n1, n2), color=GREEN)))
        self.wait(2.5)
        n3 = Tex("The sun can lift more off an open surface").scale(0.95).shift(DOWN * 1.0)
        n4 = Tex("than the sky delivers (N Cape $>2\\,500$ mm)").scale(0.95).shift(DOWN * 1.8)
        self.play(Write(n3))
        self.play(Write(n4))
        self.wait(2)
        n5 = Tex("Only $\\approx 9\\%$ of rainfall becomes river flow").scale(1.0).shift(DOWN * 2.8)
        self.play(Write(n5))
        self.play(Create(SurroundingRectangle(n5, color=GREEN)))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the east-west slide ---
        self.next_band(1)
        b1_title = Tex("Uneven in space and time").scale(1.15).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_title))
        self.wait(1.5)
        # east-west rainfall staircase (east on the right)
        pts = [(-5.0, -1.6, "$<50$"), (-2.6, -1.1, "$<200$"), (-0.2, -0.5, "400--600"), (2.4, 0.4, "$>1\\,000$ mm")]
        prev = None
        for x, y, lab in pts:
            p = band_shift(1) + RIGHT * x + UP * y
            if prev is not None:
                self.play(Create(Line(prev, p, color=BLUE, stroke_width=5)), run_time=0.6)
            d = Dot(p, color=BLUE)
            t = Tex(lab).scale(0.7).shift(p + UP * 0.55)
            self.play(FadeIn(d), Write(t), run_time=0.6)
            prev = p
        w_lab = Tex("WEST").scale(0.8).shift(band_shift(1) + LEFT * 5.0 + DOWN * 2.4)
        e_lab = Tex("EAST").scale(0.8).shift(band_shift(1) + RIGHT * 3.4 + DOWN * 2.4)
        self.play(Write(w_lab), Write(e_lab))
        self.wait(2)
        s1 = Tex("Two thirds of the country below the").scale(0.9).shift(band_shift(1) + RIGHT * 3.3 + UP * 1.8)
        s2 = Tex("500 mm that rain-fed crops need").scale(0.9).shift(band_shift(1) + RIGHT * 3.3 + UP * 1.1)
        self.play(Write(s1), Write(s2))
        self.wait(2)
        s3 = Tex("Summer storms inland, winter fronts SW Cape,").scale(0.9).shift(band_shift(1) + DOWN * 3.0)
        s4 = Tex("drought and deluge trading years").scale(0.9).shift(band_shift(1) + DOWN * 3.7)
        self.play(Write(s3))
        self.play(Write(s4))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the rivers ---
        self.next_band(2)
        b2_title = Tex("Rivers: the arteries").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        # Orange river journey as an arrow chain, east (Lesotho) to west (Atlantic)
        p1 = band_shift(2) + RIGHT * 4.6 + UP * 1.2
        p2 = band_shift(2) + RIGHT * 0.8 + UP * 0.9
        p3 = band_shift(2) + LEFT * 2.6 + UP * 0.7
        p4 = band_shift(2) + LEFT * 5.2 + UP * 0.5
        les = Dot(p1, color=BLUE)
        les_lab = Tex("Lesotho highlands").scale(0.7).shift(p1 + UP * 0.5)
        self.play(FadeIn(les), Write(les_lab))
        a1 = Arrow(p1, p2, buff=0.1, color=BLUE, stroke_width=5)
        a2 = Arrow(p2, p3, buff=0.1, color=BLUE, stroke_width=5)
        a3 = Arrow(p3, p4, buff=0.1, color=BLUE, stroke_width=5)
        self.play(Create(a1))
        self.play(Create(a2), Create(a3))
        sea_lab = Tex("Atlantic (Alexander Bay)").scale(0.7).shift(p4 + DOWN * 0.5 + RIGHT * 0.6)
        self.play(Write(sea_lab))
        self.wait(1.5)
        vaal = Tex("Orange (Gariep) $\\approx 2\\,200$ km; the Vaal carries Gauteng").scale(0.85).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(vaal))
        self.wait(2)
        r1 = Tex("East: Thukela, Phongolo, Komati, Limpopo —").scale(0.85).shift(band_shift(2) + DOWN * 1.3)
        r2 = Tex("short, steep, strong. South: Gouritz, Breede. SW: Berg").scale(0.8).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(r1))
        self.play(Write(r2))
        self.wait(2)
        r3 = Tex("Perennial (east) $\\to$ periodic $\\to$ episodic (west);").scale(0.85).shift(band_shift(2) + DOWN * 2.8)
        r4 = Tex("brown with silt, breathing with the seasons").scale(0.85).shift(band_shift(2) + DOWN * 3.5)
        self.play(Write(r3))
        self.play(Write(r4))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): lakes, dams, groundwater ---
        self.next_band(3)
        b3_title = Tex("Lakes, dams and groundwater").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        l1 = Tex("Natural lakes: almost none —").scale(0.9).shift(band_shift(3) + UP * 1.4)
        l2 = Tex("Fundudzi, Chrissiesmeer pans, Sibaya").scale(0.9).shift(band_shift(3) + UP * 0.7)
        self.play(Write(l1))
        self.play(Write(l2))
        self.wait(2)
        l3 = Tex("$>500$ large dams: Gariep + Vanderkloof (Orange),").scale(0.85).shift(band_shift(3) + DOWN * 0.2)
        l4 = Tex("Vaal Dam (Gauteng), Sterkfontein (reserve),").scale(0.85).shift(band_shift(3) + DOWN * 0.9)
        l5 = Tex("Theewaterskloof (Day Zero), Midmar, Jozini").scale(0.85).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(l3))
        self.play(Write(l4))
        self.play(Write(l5))
        self.wait(2.5)
        l6 = Tex("Groundwater: aquifers, boreholes, windpumps —").scale(0.85).shift(band_shift(3) + DOWN * 2.5)
        l7 = Tex("hidden from the sun; over-pumping and seeped").scale(0.85).shift(band_shift(3) + DOWN * 3.2)
        l8 = Tex("pollution are the invisible dangers").scale(0.85).shift(band_shift(3) + DOWN * 3.9)
        self.play(Write(l6))
        self.play(Write(l7))
        self.play(Write(l8))
        self.wait(2.5)

        # --- Band 4 (subtopic_4): the factor lists ---
        self.next_band(4)
        b4_title = Tex("The factors behind availability").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        f1 = Tex("Physical: amount, distribution, seasonality,").scale(0.9).shift(band_shift(4) + UP * 1.4)
        f2 = Tex("variability, evaporation, relief and geology, 9\\% runoff").scale(0.85).shift(band_shift(4) + UP * 0.7)
        self.play(Write(f1))
        self.play(Write(f2))
        self.wait(2.5)
        f3 = Tex("Human: Gauteng on a dry watershed, rising demand").scale(0.85).shift(band_shift(4) + DOWN * 0.3)
        f4 = Tex("(irrigation $\\approx 60\\%$), pollution and acid mine").scale(0.85).shift(band_shift(4) + DOWN * 1.0)
        f5 = Tex("drainage, alien invasive plants, leaking systems").scale(0.85).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(f3))
        self.play(Write(f4))
        self.play(Write(f5))
        self.wait(2.5)
        f6 = Tex("Half-ration of rain, harvested at 9\\%,").scale(0.9).shift(band_shift(4) + DOWN * 2.7)
        f7 = Tex("delivered to the wrong side of the country").scale(0.9).shift(band_shift(4) + DOWN * 3.4)
        self.play(Write(f6))
        self.play(Write(f7))
        self.play(Create(SurroundingRectangle(VGroup(f6, f7), color=GREEN)))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): the tank behind the house ---
        self.next_band(5)
        b5_title = Tex("The tank behind the house").scale(1.2).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(2)
        t1 = Tex("1. The gutter runs weak: 465 vs 860 mm").scale(0.95).shift(band_shift(5) + UP * 1.3)
        t2 = Tex("2. The sun drinks from the open tank").scale(0.95).shift(band_shift(5) + UP * 0.5)
        self.play(Write(t1))
        self.wait(2)
        self.play(Write(t2))
        self.wait(2)
        t3 = Tex("3. Only 9 litres in every 100 reach the gutter").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        t4 = Tex("4. The gutter hangs on the east side of the roof").scale(0.95).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(t3))
        self.wait(2)
        self.play(Write(t4))
        self.wait(2)
        t5 = Tex("Maize on rain in the east;").scale(0.95).shift(band_shift(5) + DOWN * 2.1)
        t6 = Tex("sheep between windpumps in the west").scale(0.95).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(t5))
        self.play(Write(t6))
        self.play(Create(SurroundingRectangle(t6, color=GREEN)))
        self.wait(2.5)

        # --- Band 6 (subtopic_6): a road trip from wet to dry ---
        self.next_band(6)
        b6_title = Tex("A road trip from wet to dry").scale(1.15).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(2)
        d1 = Tex("Durban: Thukela — perennial, full every day").scale(0.9).shift(band_shift(6) + UP * 1.3)
        d2 = Tex("Plateau: the Vaal working for Gauteng;").scale(0.9).shift(band_shift(6) + UP * 0.5)
        d3 = Tex("streams keeping seasonal hours — periodic").scale(0.9).shift(band_shift(6) + DOWN * 0.3)
        self.play(Write(d1))
        self.wait(2)
        self.play(Write(d2))
        self.play(Write(d3))
        self.wait(2.5)
        d4 = Tex("Kalahari edge: Molopo, Auob — episodic,").scale(0.9).shift(band_shift(6) + DOWN * 1.2)
        d5 = Tex("dry sand for years, loud for days").scale(0.9).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(d4))
        self.play(Write(d5))
        self.wait(2.5)
        d6 = Tex("The exception: the Orange — Lesotho's rain").scale(0.9).shift(band_shift(6) + DOWN * 2.9)
        d7 = Tex("crossing the desert to Alexander Bay").scale(0.9).shift(band_shift(6) + DOWN * 3.6)
        self.play(Write(d6))
        self.play(Write(d7))
        self.play(Create(SurroundingRectangle(d7, color=GREEN)))
        self.wait(2.5)

        # --- Band 7 (subtopic_7): the country that built its own lakes ---
        self.next_band(7)
        b7_title = Tex("The country that built its own lakes").scale(1.1).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(2)
        k1 = Tex("Gariep the biggest; Vaal Dam the tank;").scale(0.9).shift(band_shift(7) + UP * 1.3)
        k2 = Tex("Sterkfontein the fixed deposit; Theewaterskloof").scale(0.9).shift(band_shift(7) + UP * 0.5)
        k3 = Tex("the Day Zero dam; Midmar and Jozini at work").scale(0.9).shift(band_shift(7) + DOWN * 0.3)
        self.play(Write(k1))
        self.play(Write(k2))
        self.play(Write(k3))
        self.wait(2.5)
        k4 = Tex("Two taxes: the sun off the top,").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        k5 = Tex("silt filling from the bottom").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(k4))
        self.play(Write(k5))
        self.wait(2.5)
        k6 = Tex("Underground account: withdraw no faster than").scale(0.9).shift(band_shift(7) + DOWN * 2.9)
        k7 = Tex("rain deposits, and keep the poison out").scale(0.9).shift(band_shift(7) + DOWN * 3.6)
        self.play(Write(k6))
        self.play(Write(k7))
        self.play(Create(SurroundingRectangle(k7, color=GREEN)))
        self.wait(3)
