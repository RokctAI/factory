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

# Band-layout whiteboard scene for "Urban Heat Islands and Pollution Domes"
# (grade 12, term 1). All seven subtopics: Part 1 Expert (1-4), Part 2
# Simplifier (5-7). Band time apportioned to subtopics.json
# (235/245/245/250/200/200/210 of 1585 s). Exporter-safe primitives only;
# the heat-island profile and the inversion lid are hand-built from
# Line/Dot/Tex, element by element.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class UrbanClimatesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): city vs farm — surfaces and moisture
        title = Tex("Urban Climates").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"City vs farm, element by element —").scale(0.95).shift(UP * 1.4)
        b0_l2 = Tex(r"a mechanism for every difference").scale(0.95).shift(UP * 0.7)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex(r"Surfaces: dark, dry, low-albedo tar and").scale(0.95).shift(DOWN * 0.2)
        b0_l4 = Tex(r"concrete absorb and store; soil reflects").scale(0.95).shift(DOWN * 0.9)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(2.5)
        b0_l5 = Tex(r"Moisture: rural ground breathes and sweats;").scale(0.95).shift(DOWN * 1.8)
        b0_l6 = Tex(r"the sealed city drains its rain away —").scale(0.95).shift(DOWN * 2.5)
        b0_l7 = Tex(r"lower humidity, no evaporative cooling").scale(0.95).shift(DOWN * 3.2)
        self.play(Write(b0_l5))
        self.play(Write(b0_l6))
        self.play(Write(b0_l7))
        self.play(Create(SurroundingRectangle(b0_l7, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): wind, rain, sunshine
        self.next_band(1)
        b1_title = Tex("Wind, rain, fog, sunshine").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Wind: slower overall, but gusty funnels").scale(0.95).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex(r"between the towers").scale(0.95).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex(r"Rain: a few percent more, on and downwind").scale(0.95).shift(band_shift(1) + DOWN * 0.4)
        b1_l4 = Tex(r"of the city — convection $+$ condensation").scale(0.95).shift(band_shift(1) + DOWN * 1.1)
        b1_l5 = Tex(r"nuclei from smoke and exhaust").scale(0.95).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(2.5)
        b1_l6 = Tex(r"Fog: thicker, more frequent (same nuclei);").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        b1_l7 = Tex(r"sunshine: filtered by the haze, yet warmer").scale(0.95).shift(band_shift(1) + DOWN * 3.4)
        self.play(Write(b1_l6))
        self.play(Write(b1_l7))
        self.wait(3)

        # --- Band 2 (subtopic_2): UHI definition and temperature profile
        self.next_band(2)
        b2_title = Tex("The urban heat island").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"Dome of warmer air over the city — strongest").scale(0.9).shift(band_shift(2) + UP * 1.3)
        b2_l2 = Tex(r"at night and in winter, peaking over the CBD").scale(0.9).shift(band_shift(2) + UP * 0.6)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        # Temperature profile: rural - suburbs - park dip - CBD peak - rural.
        base = Line(band_shift(2) + DOWN * 2.6 + LEFT * 5.4, band_shift(2) + DOWN * 2.6 + RIGHT * 5.4)
        p1 = Line(band_shift(2) + DOWN * 2.3 + LEFT * 5.0, band_shift(2) + DOWN * 1.5 + LEFT * 2.6, color=ORANGE)
        p2 = Line(band_shift(2) + DOWN * 1.5 + LEFT * 2.6, band_shift(2) + DOWN * 1.9 + LEFT * 1.4, color=ORANGE)
        p3 = Line(band_shift(2) + DOWN * 1.9 + LEFT * 1.4, band_shift(2) + DOWN * 0.7 + RIGHT * 0.8, color=ORANGE)
        p4 = Line(band_shift(2) + DOWN * 0.7 + RIGHT * 0.8, band_shift(2) + DOWN * 2.3 + RIGHT * 5.0, color=ORANGE)
        self.play(Create(base))
        self.play(Create(p1), Create(p2), Create(p3), Create(p4))
        dip_lab = Tex("park dip").scale(0.75).shift(band_shift(2) + DOWN * 1.3 + LEFT * 2.0)
        peak_lab = Tex("CBD peak").scale(0.75).shift(band_shift(2) + DOWN * 0.3 + RIGHT * 0.8)
        self.play(Write(dip_lab), Write(peak_lab))
        self.wait(2.5)
        b2_l3 = Tex(r"The park dips PROVE vegetation cools").scale(0.95).shift(band_shift(2) + DOWN * 3.4)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the five causes
        self.next_band(3)
        b3_title = Tex("Five causes, five mechanisms").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"1. Dark surfaces bank heat by day,").scale(0.9).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"pay it out by night").scale(0.9).shift(band_shift(3) + UP * 0.5)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex(r"2. Anthropogenic heat: engines, heaters,").scale(0.9).shift(band_shift(3) + DOWN * 0.3)
        b3_l4 = Tex(r"bodies — swells in winter").scale(0.9).shift(band_shift(3) + DOWN * 1.0)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex(r"3. No evaporation: budget spent on heat").scale(0.9).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l5))
        self.wait(2)
        b3_l6 = Tex(r"4. Canyons trap radiation; narrow sky").scale(0.9).shift(band_shift(3) + DOWN * 2.6)
        b3_l7 = Tex(r"slows night cooling").scale(0.9).shift(band_shift(3) + DOWN * 3.3)
        b3_l8 = Tex(r"5. Haze blanket re-radiates heat down").scale(0.9).shift(band_shift(3) + DOWN * 4.0)
        self.play(Write(b3_l6))
        self.play(Write(b3_l7))
        self.play(Write(b3_l8))
        self.wait(3)

        # --- Band 4 (subtopic_3): effects, grouped
        self.next_band(4)
        b4_title = Tex("Effects, grouped for the essay").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Health: hot nights kill in heat waves —").scale(0.9).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex(r"elderly, infants, zinc-roofed homes worst").scale(0.9).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex(r"Energy and water: aircon peak load,").scale(0.9).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex(r"thirstier parks in drier air").scale(0.9).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex(r"Weather: sharper storms over and downwind;").scale(0.9).shift(band_shift(4) + DOWN * 1.9)
        b4_l6 = Tex(r"rising air props up the pollution dome").scale(0.9).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l5))
        self.play(Write(b4_l6))
        self.wait(2)
        b4_l7 = Tex(r"Ecology: early budding, surviving pests,").scale(0.9).shift(band_shift(4) + DOWN * 3.4)
        b4_l8 = Tex(r"blurred seasons at the core").scale(0.9).shift(band_shift(4) + DOWN * 4.1)
        self.play(Write(b4_l7))
        self.play(Write(b4_l8))
        self.wait(3)

        # --- Band 5 (subtopic_3): strategies matched to causes
        self.next_band(5)
        b5_title = Tex("Strategies matched to causes").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Albedo $\to$ light roofs and paving").scale(0.9).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex(r"Lost vegetation $\to$ street trees, parks,").scale(0.9).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex(r"green roofs — shade $+$ transpiration").scale(0.9).shift(band_shift(5) + DOWN * 0.3)
        self.play(Write(b5_l2))
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex(r"Sealed ground $\to$ permeable paving,").scale(0.9).shift(band_shift(5) + DOWN * 1.1)
        b5_l5 = Tex(r"ponds and wetlands").scale(0.9).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(2)
        b5_l6 = Tex(r"Waste heat $\to$ insulation, public transport;").scale(0.9).shift(band_shift(5) + DOWN * 2.6)
        b5_l7 = Tex(r"geometry $\to$ ventilated streets, wind corridors").scale(0.85).shift(band_shift(5) + DOWN * 3.3)
        b5_l8 = Tex(r"Local example: Tshwane's street-tree avenues").scale(0.85).shift(band_shift(5) + DOWN * 4.0)
        self.play(Write(b5_l6))
        self.play(Write(b5_l7))
        self.play(Write(b5_l8))
        self.wait(3)

        # --- Band 6 (subtopic_4): dome vs plume and the inversion seal
        self.next_band(6)
        b6_title = Tex("Dome, plume and the seal").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Calm: pollution DOME over the city;").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"wind: stretched into a PLUME downwind").scale(0.95).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        # Inversion sketch: ground, rising smoke flattening under a lid.
        ground = Line(band_shift(6) + DOWN * 2.8 + LEFT * 5.0, band_shift(6) + DOWN * 2.8 + RIGHT * 5.0)
        lid = Line(band_shift(6) + DOWN * 1.0 + LEFT * 5.0, band_shift(6) + DOWN * 1.0 + RIGHT * 5.0, color=ORANGE)
        smoke1 = Line(band_shift(6) + DOWN * 2.8 + LEFT * 2.0, band_shift(6) + DOWN * 1.0 + LEFT * 2.0, color=GRAY)
        smoke2 = Line(band_shift(6) + DOWN * 1.0 + LEFT * 2.0, band_shift(6) + DOWN * 1.0 + RIGHT * 1.4, color=GRAY)
        lid_lab = Tex("inversion lid: warm over cold").scale(0.8).shift(band_shift(6) + DOWN * 0.5 + RIGHT * 2.9)
        self.play(Create(ground), Create(lid), Write(lid_lab))
        self.play(Create(smoke1), Create(smoke2))
        self.wait(2.5)
        b6_l3 = Tex(r"Winter anticyclone deepens the lid —").scale(0.9).shift(band_shift(6) + DOWN * 3.4)
        b6_l4 = Tex(r"priority areas: Vaal Triangle, South Durban").scale(0.9).shift(band_shift(6) + DOWN * 4.1)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): sources, effects, strategies
        self.next_band(7)
        b7_title = Tex("Fill, suffer, shrink").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"Sources: exhausts, stacks, domestic coal").scale(0.9).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex(r"and wood, dust, veld fires").scale(0.9).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex(r"Effects: asthma and bronchitis where burning").scale(0.9).shift(band_shift(7) + DOWN * 0.3)
        b7_l4 = Tex(r"meets the inversion — the poorest breathe").scale(0.9).shift(band_shift(7) + DOWN * 1.0)
        b7_l5 = Tex(r"the worst air; smog; acid downwind").scale(0.9).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2.5)
        b7_l6 = Tex(r"Cut sources: electrify homes, scrub stacks,").scale(0.9).shift(band_shift(7) + DOWN * 2.6)
        b7_l7 = Tex(r"cleaner fuels; work with weather: no burning").scale(0.9).shift(band_shift(7) + DOWN * 3.3)
        b7_l8 = Tex(r"on still days, industry zoned downwind").scale(0.9).shift(band_shift(7) + DOWN * 4.0)
        self.play(Write(b7_l6))
        self.play(Write(b7_l7))
        self.play(Write(b7_l8))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the city is a storage heater
        self.next_band(8)
        b8_title = Tex("The city is a storage heater").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Brick wall warm an hour after sunset;").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex(r"farm fence post cold — cities are built").scale(0.95).shift(band_shift(8) + UP * 0.5)
        b8_l3 = Tex(r"from the warm-wall stuff").scale(0.95).shift(band_shift(8) + DOWN * 0.2)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex(r"Charge by day, glow by night; and the").scale(0.95).shift(band_shift(8) + DOWN * 1.1)
        b8_l5 = Tex(r"city CANNOT SWEAT — rain is drained away").scale(0.95).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(2.5)
        b8_l6 = Tex(r"Plus: a million small heaters, stairwell").scale(0.95).shift(band_shift(8) + DOWN * 2.7)
        b8_l7 = Tex(r"canyons, and the haze blanket —").scale(0.95).shift(band_shift(8) + DOWN * 3.4)
        b8_l8 = Tex(r"the HEAT ISLAND, dipping over parks").scale(0.95).shift(band_shift(8) + DOWN * 4.1)
        self.play(Write(b8_l6))
        self.play(Write(b8_l7))
        self.play(Write(b8_l8))
        self.wait(3)

        # --- Band 9 (subtopic_6): undo each cause
        self.next_band(9)
        b9_title = Tex("Cooling: run the list backwards").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Dark surfaces $\to$ lighten the city").scale(0.95).shift(band_shift(9) + UP * 1.3)
        b9_l2 = Tex(r"(the white car vs the black car)").scale(0.9).shift(band_shift(9) + UP * 0.6)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex(r"No sweat $\to$ trees, parks, roof gardens —").scale(0.95).shift(band_shift(9) + DOWN * 0.2)
        b9_l4 = Tex(r"a tree cools twice; park dips are the proof").scale(0.95).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex(r"Sealed ground $\to$ let water stay;").scale(0.95).shift(band_shift(9) + DOWN * 1.8)
        b9_l6 = Tex(r"small heaters $\to$ leak less; canyons $\to$").scale(0.95).shift(band_shift(9) + DOWN * 2.5)
        b9_l7 = Tex(r"build for breeze").scale(0.95).shift(band_shift(9) + DOWN * 3.2)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.play(Write(b9_l7))
        self.wait(2)
        b9_l8 = Tex(r"Heat kills selectively: health, justice, energy").scale(0.9).shift(band_shift(9) + DOWN * 4.0)
        self.play(Write(b9_l8))
        self.wait(3.5)

        # --- Band 10 (subtopic_7): the pot lid of smoke
        self.next_band(10)
        b10_title = Tex("The pot lid of smoke").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Still winter night: inversion closes like").scale(0.95).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex(r"a lid; smoke flattens as under glass").scale(0.95).shift(band_shift(10) + UP * 0.5)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex(r"Calm $=$ DOME (the brown dawn skyline);").scale(0.95).shift(band_shift(10) + DOWN * 0.3)
        b10_l4 = Tex(r"wind $=$ PLUME streaming downwind").scale(0.95).shift(band_shift(10) + DOWN * 1.0)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2.5)
        b10_l5 = Tex(r"Thickest where coal fires must burn —").scale(0.95).shift(band_shift(10) + DOWN * 1.9)
        b10_l6 = Tex(r"children's lungs pay first").scale(0.95).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.wait(2.5)
        b10_l7 = Tex(r"Fixes: electrify, scrub the stacks, no open").scale(0.9).shift(band_shift(10) + DOWN * 3.4)
        b10_l8 = Tex(r"burning on still days, industry downwind").scale(0.9).shift(band_shift(10) + DOWN * 4.1)
        self.play(Write(b10_l7))
        self.play(Write(b10_l8))
        self.wait(4)
