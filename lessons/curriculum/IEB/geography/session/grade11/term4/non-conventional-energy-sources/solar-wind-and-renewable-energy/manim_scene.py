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

# Band-layout whiteboard scene for the IEB session "Solar, Wind and Renewable
# Energy" (grade 11, term 4). Seven subtopics of the duo: Part 1 Expert
# (subtopics 1-4), Part 2 Simplifier (subtopics 5-7). Band time apportioned
# to subtopics.json (230/235/230/235/195/200/200 of 1525 s). Exporter-safe
# primitives only; diagrams (CSP mirror field, turbine, relay track)
# hand-built from Line/Arrow/Dot/Circle/Rectangle/Tex element by element.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class SolarWindRenewableEnergySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the family and its two properties
        title = Tex("Solar, Wind and Renewable Energy").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Non-conventional: solar, wind, biomass,").scale(0.95).shift(UP * 1.3)
        b0_l2 = Tex(r"biogas, geothermal, wave, small hydro").scale(0.95).shift(UP * 0.6)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex(r"Property 1: the fuel costs NOTHING").scale(1.0).shift(DOWN * 0.4)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex(r"Property 2: the supply is INTERMITTENT").scale(1.0).shift(DOWN * 1.2)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex(r"Free but moody — costly but steady").scale(1.0).shift(DOWN * 2.2)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the endowment and REIPPPP
        self.next_band(1)
        b1_title = Tex("The endowment and the auctions").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Interior: $>$ 2 500 sunshine hours a year").scale(0.95).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex(r"Northern Cape: world-ranking radiation").scale(0.95).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex(r"Two oceans drive wind onto the coasts").scale(0.95).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex(r"Germany: half our sun, world solar leader").scale(0.95).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex(r"REIPPPP: auctions since 2011, 100+ plants,").scale(0.95).shift(band_shift(1) + DOWN * 2.1)
        b1_l6 = Tex(r"new sun and wind now undercut new coal").scale(0.95).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.play(Create(SurroundingRectangle(b1_l6, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): PV against CSP — the mirror field
        self.next_band(2)
        b2_title = Tex("PV against CSP").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"PV: light $\to$ current in a cell; no moving parts").scale(0.9).shift(band_shift(2) + UP * 1.3)
        self.play(Write(b2_l1))
        self.wait(2)
        # CSP mirror field: three tilted mirror lines aiming rays at a tower dot.
        tower = Line(band_shift(2) + DOWN * 1.6 + RIGHT * 2.6, band_shift(2) + UP * 0.2 + RIGHT * 2.6)
        receiver = Dot(band_shift(2) + UP * 0.3 + RIGHT * 2.6, color=YELLOW)
        self.play(Create(tower), Create(receiver))
        m1 = Line(band_shift(2) + DOWN * 1.4 + LEFT * 3.6, band_shift(2) + DOWN * 1.1 + LEFT * 2.9)
        m2 = Line(band_shift(2) + DOWN * 1.5 + LEFT * 1.9, band_shift(2) + DOWN * 1.2 + LEFT * 1.2)
        m3 = Line(band_shift(2) + DOWN * 1.6 + LEFT * 0.3, band_shift(2) + DOWN * 1.3 + RIGHT * 0.4)
        self.play(Create(m1), Create(m2), Create(m3))
        r1 = Line(band_shift(2) + DOWN * 1.2 + LEFT * 3.2, band_shift(2) + UP * 0.3 + RIGHT * 2.5, color=YELLOW)
        r2 = Line(band_shift(2) + DOWN * 1.3 + LEFT * 1.5, band_shift(2) + UP * 0.3 + RIGHT * 2.5, color=YELLOW)
        r3 = Line(band_shift(2) + DOWN * 1.4 + LEFT * 0.0, band_shift(2) + UP * 0.3 + RIGHT * 2.55, color=YELLOW)
        self.play(Create(r1), Create(r2), Create(r3))
        self.wait(2)
        b2_l2 = Tex(r"CSP: mirrors cook molten salt $\to$ steam").scale(0.9).shift(band_shift(2) + DOWN * 2.3)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex(r"Salt tanks stay hot for hours: sun after sunset").scale(0.9).shift(band_shift(2) + DOWN * 3.1)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): solar examples, SA and world
        self.next_band(3)
        b3_title = Tex("Solar examples").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"PV farms: Jasper, Droogfontein —").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"Kimberley and De Aar country").scale(0.95).shift(band_shift(3) + UP * 0.5)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex(r"CSP: Kathu ($\approx$ 4.5 h salt), Bokpoort").scale(0.9).shift(band_shift(3) + DOWN * 0.4)
        b3_l4 = Tex(r"($\approx$ 9 h), Ilanga near Upington").scale(0.9).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(2.5)
        b3_l5 = Tex(r"Cheapest solar of all: the solar water heater").scale(0.9).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_l5))
        self.wait(2)
        b3_l6 = Tex(r"World: China's fleets; Germany's policy;").scale(0.9).shift(band_shift(3) + DOWN * 2.8)
        b3_l7 = Tex(r"Spain's salt carried the night first").scale(0.9).shift(band_shift(3) + DOWN * 3.5)
        self.play(Write(b3_l6))
        self.play(Write(b3_l7))
        self.wait(3)

        # --- Band 4 (subtopic_3): the turbine and the cube law
        self.next_band(4)
        b4_title = Tex("Wind: the turbine and the cube law").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        # A turbine: tower line, hub dot, three blade lines.
        t_tower = Line(band_shift(4) + DOWN * 1.8 + LEFT * 3.0, band_shift(4) + UP * 0.2 + LEFT * 3.0)
        hub = Dot(band_shift(4) + UP * 0.2 + LEFT * 3.0)
        bl1 = Line(band_shift(4) + UP * 0.2 + LEFT * 3.0, band_shift(4) + UP * 1.4 + LEFT * 3.4)
        bl2 = Line(band_shift(4) + UP * 0.2 + LEFT * 3.0, band_shift(4) + DOWN * 0.3 + LEFT * 4.2)
        bl3 = Line(band_shift(4) + UP * 0.2 + LEFT * 3.0, band_shift(4) + DOWN * 0.4 + LEFT * 1.9)
        self.play(Create(t_tower), Create(hub))
        self.play(Create(bl1), Create(bl2), Create(bl3))
        self.wait(2)
        b4_l1 = Tex(r"air $\to$ blades $\to$ shaft $\to$ generator").scale(0.9).shift(band_shift(4) + UP * 1.3 + RIGHT * 2.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex(r"Power $\propto$ swept area $\times$ wind speed$^3$").scale(0.9).shift(band_shift(4) + UP * 0.3 + RIGHT * 2.2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex(r"Double the wind $=$ 8$\times$ the power").scale(0.95).shift(band_shift(4) + DOWN * 0.7 + RIGHT * 2.0)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex(r"Towers past 100 m; blades outmeasure").scale(0.9).shift(band_shift(4) + DOWN * 2.3)
        b4_l5 = Tex(r"a rugby field; siting decides everything").scale(0.9).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): wind examples and the two-column check
        self.next_band(5)
        b5_title = Tex("Wind examples and the check").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Eastern Cape: Gibson Bay, Kouga,").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex(r"Amakhala Emoyeni near Bedford").scale(0.95).shift(band_shift(5) + UP * 0.5)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex(r"Western Cape: Gouda; west coast: Sere;").scale(0.9).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex(r"Northern Cape: Loeriesfontein").scale(0.9).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex(r"World: Denmark $\approx$ half on wind; China's").scale(0.9).shift(band_shift(5) + DOWN * 2.0)
        b5_l6 = Tex(r"fleet; North Sea offshore frontier").scale(0.9).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(2.5)
        b5_l7 = Tex(r"Costs: intermittency, neighbours, birds, backup").scale(0.85).shift(band_shift(5) + DOWN * 3.5)
        self.play(Write(b5_l7))
        self.wait(3)

        # --- Band 6 (subtopic_4): economic effects, both columns
        self.next_band(6)
        b6_title = Tex("Economy: both columns").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"$+$ cheapest new power: tariffs restrained").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"$+$ hundreds of billions invested; rural jobs").scale(0.95).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex(r"$+$ community trusts; green manufacturing").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6_l1))
        self.wait(1.8)
        self.play(Write(b6_l2))
        self.wait(1.8)
        self.play(Write(b6_l3))
        self.wait(1.8)
        b6_l4 = Tex(r"$-$ coal: $\approx$ 90 000 jobs concentrated in").scale(0.95).shift(band_shift(6) + DOWN * 1.3)
        b6_l5 = Tex(r"Mpumalanga; renewables employ fewer, elsewhere").scale(0.9).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(2.5)
        b6_l6 = Tex(r"Answer: the JUST transition — retrain, fund, rebuild").scale(0.85).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): environment, obstacles, conclusion
        self.next_band(7)
        b7_title = Tex("Environment, obstacles, verdict").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"$+$ no CO$_2$, no smog, almost no water").scale(0.95).shift(band_shift(7) + UP * 1.3)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex(r"$-$ land, birds and bats, panel disposal").scale(0.95).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex(r"Obstacle 1: the saturated grid to Gauteng").scale(0.9).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex(r"Obstacle 2: intermittency — solved by the mix").scale(0.9).shift(band_shift(7) + DOWN * 1.2)
        b7_l5 = Tex(r"Obstacle 3: policy certainty in the auctions").scale(0.9).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l3))
        self.wait(1.8)
        self.play(Write(b7_l4))
        self.wait(1.8)
        self.play(Write(b7_l5))
        self.wait(2)
        b7_l6 = Tex(r"Resource world-class; the race is delivery").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): fuel that falls from the sky
        self.next_band(8)
        b8_title = Tex("Fuel that falls from the sky").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"The filling station with free petrol:").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex(r"pay for the pumps, the fuel just arrives").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"Coal: dug, railed, burned daily —").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex(r"a panel harvests free for 25 years").scale(0.95).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex(r"Catch: the fuel keeps its own diary").scale(0.95).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l5))
        self.wait(2)
        b8_l6 = Tex(r"Free but moody, costly but steady").scale(1.0).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): sun traps and wind catchers
        self.next_band(9)
        b9_title = Tex("Sun traps and wind catchers").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"PV: light in, current out, no moving parts").scale(0.9).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex(r"CSP: a field-sized magnifying glass plus a").scale(0.9).shift(band_shift(9) + UP * 0.4)
        b9_l3 = Tex(r"building-sized thermos — Bokpoort $\approx$ 9 h").scale(0.9).shift(band_shift(9) + DOWN * 0.3)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex(r"Turbine: skyscraper pinwheel; cube law —").scale(0.9).shift(band_shift(9) + DOWN * 1.2)
        b9_l5 = Tex(r"double wind, EIGHT times power").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(2.5)
        b9_l6 = Tex(r"Gibson Bay, Kouga, Gouda, Sere, Loeriesfontein;").scale(0.8).shift(band_shift(9) + DOWN * 2.9)
        b9_l7 = Tex(r"sheep graze, farmers rent, communities share").scale(0.85).shift(band_shift(9) + DOWN * 3.6)
        self.play(Write(b9_l6))
        self.play(Write(b9_l7))
        self.wait(3)

        # --- Band 10 (subtopic_7): the relay race and the baton
        self.next_band(10)
        b10_title = Tex("The relay race and the baton").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        # Relay track: a line with two runner dots and a baton arrow between.
        track = Line(band_shift(10) + UP * 1.2 + LEFT * 4.0, band_shift(10) + UP * 1.2 + RIGHT * 4.0)
        old_runner = Dot(band_shift(10) + UP * 1.2 + LEFT * 1.0, color=GREY)
        new_runner = Dot(band_shift(10) + UP * 1.2 + RIGHT * 1.0, color=GREEN)
        baton = Arrow(band_shift(10) + UP * 1.2 + LEFT * 0.8, band_shift(10) + UP * 1.2 + RIGHT * 0.8, color=YELLOW)
        self.play(Create(track))
        self.play(Create(old_runner), Create(new_runner))
        self.play(Create(baton))
        self.wait(2)
        b10_l1 = Tex(r"Fumble 1: the extension cord — full grid,").scale(0.9).shift(band_shift(10) + UP * 0.3)
        b10_l2 = Tex(r"new lines are the real bottleneck").scale(0.9).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex(r"Fumble 2: the night shift — salt, batteries,").scale(0.9).shift(band_shift(10) + DOWN * 1.2)
        b10_l4 = Tex(r"pumped storage, night wind: the MIX covers 24 h").scale(0.85).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex(r"Fumble 3: the coal towns — pass justly:").scale(0.9).shift(band_shift(10) + DOWN * 2.7)
        b10_l6 = Tex(r"retrain, pension, rebuild — a JUST transition").scale(0.9).shift(band_shift(10) + DOWN * 3.4)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
