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

# Band-layout whiteboard scene for "Water Availability in South Africa"
# (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier 5-7). Exporter-safe
# primitives only: the east-west rainfall gradient is a stepped Line profile
# with Dot+Tex markers, and the Orange-Vaal river journey is an Arrow chain.
# Add-only lifecycle; camera moves down band by band. Band time apportioned
# to subtopics.json (235/240/240/235/190/185/175 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class WaterAvailabilitySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(11)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the master statistics ---
        title = Tex("Water Availability in South Africa").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        n1 = MathTex(r"\text{SA rain} \approx 465 \text{ mm/yr}").scale(1.1).shift(UP * 1.0)
        n2 = MathTex(r"\text{World} \approx 860 \text{ mm/yr}").scale(1.1).shift(UP * 0.1)
        self.play(Write(n1))
        self.play(Write(n2))
        self.play(Create(SurroundingRectangle(VGroup(n1, n2), color=GREEN)))
        self.wait(2.5)
        n3 = Tex("Evaporation exceeds rainfall over most of").scale(0.95).shift(DOWN * 1.0)
        n4 = Tex("the interior (Northern Cape $>2\\,500$ mm)").scale(0.95).shift(DOWN * 1.8)
        self.play(Write(n3))
        self.play(Write(n4))
        self.wait(2)
        n5 = Tex("Only $\\approx 9\\%$ of rainfall reaches the rivers").scale(1.0).shift(DOWN * 2.8)
        self.play(Write(n5))
        self.play(Create(SurroundingRectangle(n5, color=GREEN)))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): unevenness in space and time ---
        self.next_band(1)
        b1_title = Tex("Uneven in space and time").scale(1.15).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_title))
        self.wait(1.5)
        # east-west rainfall staircase (east on the right)
        pts = [(-5.0, -1.6, "$<50$"), (-2.6, -1.1, "200"), (-0.2, -0.5, "400--600"), (2.4, 0.4, "$>1\\,000$ mm")]
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
        s1 = Tex("Two thirds of SA below the 500 mm").scale(0.9).shift(band_shift(1) + RIGHT * 3.4 + UP * 1.8)
        s2 = Tex("needed for rain-fed crops").scale(0.9).shift(band_shift(1) + RIGHT * 3.4 + UP * 1.1)
        self.play(Write(s1), Write(s2))
        self.wait(2)
        s3 = Tex("Summer rain inland, winter rain SW Cape,").scale(0.9).shift(band_shift(1) + DOWN * 3.0)
        s4 = Tex("wild swings between years").scale(0.9).shift(band_shift(1) + DOWN * 3.7)
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
        vaal = Tex("Orange (Gariep), 2 200 km; Vaal feeds Gauteng").scale(0.85).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(vaal))
        self.wait(2)
        r1 = Tex("East: Thukela, Limpopo, Komati — short,").scale(0.85).shift(band_shift(2) + DOWN * 1.3)
        r2 = Tex("steep, strong. South: Breede. SW: Berg").scale(0.85).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(r1))
        self.play(Write(r2))
        self.wait(2)
        r3 = Tex("Perennial (east) $\\to$ periodic $\\to$ episodic (west);").scale(0.85).shift(band_shift(2) + DOWN * 2.8)
        r4 = Tex("heavy silt loads, strongly seasonal flow").scale(0.85).shift(band_shift(2) + DOWN * 3.5)
        self.play(Write(r3))
        self.play(Write(r4))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): lakes, dams, groundwater ---
        self.next_band(3)
        b3_title = Tex("Lakes, dams and groundwater").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        k1 = Tex("Almost no natural lakes (Fundudzi, Sibaya):").scale(0.9).shift(band_shift(3) + UP * 1.2)
        k2 = Tex("so SA built 500+ large dams").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(k1))
        self.play(Write(k2))
        self.wait(2.5)
        k3 = Tex("Gariep + Vanderkloof: the Orange, irrigation, power").scale(0.85).shift(band_shift(3) + DOWN * 0.5)
        k4 = Tex("Vaal Dam: Gauteng. Sterkfontein: drought reserve").scale(0.85).shift(band_shift(3) + DOWN * 1.2)
        k5 = Tex("Theewaterskloof: Cape Town — Day Zero 2018").scale(0.85).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(k3))
        self.wait(1.5)
        self.play(Write(k4))
        self.wait(1.5)
        self.play(Write(k5))
        self.wait(2)
        k6 = Tex("Groundwater: aquifers, boreholes, windpumps —").scale(0.85).shift(band_shift(3) + DOWN * 2.7)
        k7 = Tex("hidden from the sun, but slow to recharge").scale(0.85).shift(band_shift(3) + DOWN * 3.4)
        self.play(Write(k6))
        self.play(Write(k7))
        self.wait(2.5)

        # --- Band 4 (subtopic_4): the factor lists ---
        self.next_band(4)
        b4_title = Tex("What decides availability?").scale(1.15).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        f1 = Tex("PHYSICAL: rainfall amount and spread,").scale(0.9).shift(band_shift(4) + UP * 1.3)
        f2 = Tex("seasonality, evaporation, relief and").scale(0.9).shift(band_shift(4) + UP * 0.6)
        f3 = Tex("geology, the 9\\% runoff ratio").scale(0.9).shift(band_shift(4) + DOWN * 0.1)
        self.play(Write(f1))
        self.play(Write(f2))
        self.play(Write(f3))
        self.wait(2.5)
        f4 = Tex("HUMAN: Gauteng far from rivers, demand growth").scale(0.85).shift(band_shift(4) + DOWN * 1.0)
        f5 = Tex("(irrigation $\\approx 60\\%$), pollution and acid mine").scale(0.85).shift(band_shift(4) + DOWN * 1.7)
        f6 = Tex("drainage, alien plants, leaks, management").scale(0.85).shift(band_shift(4) + DOWN * 2.4)
        self.play(Write(f4))
        self.play(Write(f5))
        self.play(Write(f6))
        self.wait(2.5)
        f7 = Tex("Modest rain, 9\\% harvested, fierce evaporation,").scale(0.85).shift(band_shift(4) + DOWN * 3.2)
        f8 = Tex("mismatched to the people — then leaks and pollution").scale(0.85).shift(band_shift(4) + DOWN * 3.9)
        self.play(Write(f7))
        self.play(Write(f8))
        self.play(Create(SurroundingRectangle(f8, color=GREEN)))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): the bucket under a hot sky ---
        self.next_band(5)
        b5_title = Tex("The bucket under a hot sky").scale(1.15).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(2)
        w1 = Tex("Weak tap: 465 mm vs the world's 860").scale(0.95).shift(band_shift(5) + UP * 1.3)
        self.play(Write(w1))
        self.wait(2)
        w2 = Tex("Thirsty sun: it can take back more").scale(0.95).shift(band_shift(5) + UP * 0.5)
        w3 = Tex("than it drops — dams steam away").scale(0.95).shift(band_shift(5) + DOWN * 0.3)
        self.play(Write(w2))
        self.play(Write(w3))
        self.wait(2.5)
        w4 = Tex("Splashy tap: only 9 litres in every 100").scale(0.95).shift(band_shift(5) + DOWN * 1.2)
        w5 = Tex("ever reach a river").scale(0.95).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(w4))
        self.play(Write(w5))
        self.play(Create(SurroundingRectangle(w5, color=GREEN)))
        self.wait(2.5)
        w6 = Tex("And the tap hangs over the east —").scale(0.95).shift(band_shift(5) + DOWN * 2.9)
        w7 = Tex("maize on rain there, sheep on boreholes west").scale(0.9).shift(band_shift(5) + DOWN * 3.6)
        self.play(Write(w6))
        self.play(Write(w7))
        self.wait(2.5)

        # --- Band 6 (subtopic_6): one river wearing two names ---
        self.next_band(6)
        b6_title = Tex("One river wearing two names").scale(1.15).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(2)
        j1 = Tex("Born in Lesotho's storms, the Orange--Gariep").scale(0.9).shift(band_shift(6) + UP * 1.3)
        j2 = Tex("carries mountain water west through near-desert").scale(0.9).shift(band_shift(6) + UP * 0.5)
        self.play(Write(j1))
        self.play(Write(j2))
        self.wait(2.5)
        j3 = Tex("The Vaal: hardest-working river — Gauteng").scale(0.9).shift(band_shift(6) + DOWN * 0.4)
        j4 = Tex("has no big river, so the Vaal is fed like a patient").scale(0.9).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(j3))
        self.play(Write(j4))
        self.wait(2.5)
        j5 = Tex("Rule for the rest: rivers flow the way rain falls —").scale(0.9).shift(band_shift(6) + DOWN * 2.1)
        j6 = Tex("year-round east, seasonal middle, rare-storm west").scale(0.9).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(j5))
        self.play(Write(j6))
        self.play(Create(SurroundingRectangle(j6, color=GREEN)))
        self.wait(2.5)

        # --- Band 7 (subtopic_7): the country that built its own lakes ---
        self.next_band(7)
        b7_title = Tex("The country that built its own lakes").scale(1.1).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7_title))
        self.wait(2)
        c1 = Tex("A necklace of dams: Gariep and Vanderkloof,").scale(0.9).shift(band_shift(7) + UP * 1.3)
        c2 = Tex("the Vaal Dam tank, Sterkfontein the savings").scale(0.9).shift(band_shift(7) + UP * 0.5)
        c3 = Tex("account, Theewaterskloof and Day Zero").scale(0.9).shift(band_shift(7) + DOWN * 0.3)
        self.play(Write(c1))
        self.play(Write(c2))
        self.play(Write(c3))
        self.wait(2.5)
        c4 = Tex("The tax: the sun skims every surface,").scale(0.9).shift(band_shift(7) + DOWN * 1.2)
        c5 = Tex("and silt slowly fills every wall").scale(0.9).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(c4))
        self.play(Write(c5))
        self.wait(2.5)
        c6 = Tex("The hidden sponge: pump no faster than rain").scale(0.9).shift(band_shift(7) + DOWN * 2.9)
        c7 = Tex("refills it, and never let poison seep down").scale(0.9).shift(band_shift(7) + DOWN * 3.6)
        self.play(Write(c6))
        self.play(Write(c7))
        self.play(Create(SurroundingRectangle(c7, color=GREEN)))
        self.wait(3)
