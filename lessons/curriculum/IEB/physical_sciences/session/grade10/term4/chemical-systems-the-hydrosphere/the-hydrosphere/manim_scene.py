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

# Band-layout whiteboard scene for "The Hydrosphere" (Part 1 — Expert:
# subtopics 1-4; Part 2 — Simplifier: subtopics 5-7). Exporter-safe mobjects
# only (Tex/MathTex/Line/Dot/Circle/Rectangle/VGroup); the proportion bars are
# hand-built Rectangles. Add-only lifecycle, one band per teaching beat. Band
# time apportioned to subtopics.json (230/240/250/260/180/200/210 of 1570 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class TheHydrosphereSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(15)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): what the hydrosphere contains ---
        title = Tex("The Hydrosphere").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("ALL the Earth's water — three states").scale(1.0).shift(UP * 1.3)
        self.play(Write(d1))
        self.wait(2)
        d2 = Tex("Liquid: oceans, rivers, lakes, GROUNDWATER").scale(0.95).shift(UP * 0.3)
        self.play(Write(d2))
        self.wait(2.5)
        d3 = Tex("Frozen: ice sheets, glaciers, permafrost").scale(0.95).shift(DOWN * 0.6)
        self.play(Write(d3))
        self.wait(2.5)
        d4 = Tex("Vapour: the invisible gas in the atmosphere").scale(0.95).shift(DOWN * 1.5)
        self.play(Write(d4))
        self.wait(2)
        d5 = Tex("A STORE, not a cycle — the water, not the moving").scale(0.9).shift(DOWN * 2.6)
        self.play(Write(d5))
        self.wait(3)

        # --- Band 1 (subtopic_1): the proportions, as bars ---
        self.next_band(1)
        b1t = Tex("Who gets to drink?").scale(1.2).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1t))
        self.wait(2)
        bar1 = Rectangle(width=9.7, height=0.6, color=BLUE).shift(band_shift(1) + UP * 1.0 + LEFT * 0.15)
        l1 = Tex("Ocean salt water: about 97\\%").scale(0.85).shift(band_shift(1) + UP * 1.9)
        self.play(Create(bar1), Write(l1))
        self.wait(2.5)
        bar2 = Rectangle(width=2.4, height=0.6, color=WHITE).shift(band_shift(1) + DOWN * 0.2 + LEFT * 3.8)
        l2 = Tex("Fresh — but mostly frozen ice").scale(0.85).shift(band_shift(1) + DOWN * 0.2 + RIGHT * 1.6)
        self.play(Create(bar2), Write(l2))
        self.wait(2.5)
        bar3 = Rectangle(width=0.3, height=0.6, color=GREEN).shift(band_shift(1) + DOWN * 1.4 + LEFT * 4.85)
        l3 = Tex("Reachable fresh liquid: under 1\\%").scale(0.85).shift(band_shift(1) + DOWN * 1.4 + RIGHT * 1.2)
        self.play(Create(bar3), Write(l3))
        self.wait(2.5)
        b1c = Tex("Drenched planet, thirsty humanity — both true").scale(0.95).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1c))
        self.play(Create(SurroundingRectangle(b1c, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): into the atmosphere ---
        self.next_band(2)
        b2t = Tex("One water, four spheres").scale(1.2).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2t))
        self.wait(2)
        b2a = Tex("Sun $\\to$ EVAPORATION: water rises as vapour").scale(0.95).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2a))
        self.wait(2.5)
        b2b = Tex("Cooling $\\to$ CONDENSATION: vapour to cloud").scale(0.95).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2b))
        self.wait(2.5)
        b2c = Tex("Precipitation returns it: rain, snow, hail").scale(0.95).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2c))
        self.wait(2)
        b2d = Tex("Warming lifts water; cooling drops it").scale(1.0).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2d))
        self.play(Create(SurroundingRectangle(b2d, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): rock and life ---
        self.next_band(3)
        b3t = Tex("Through rock, through life").scale(1.15).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3t))
        self.wait(2)
        b3a = Tex("Rain soaks in $\\to$ groundwater creeps through pores").scale(0.9).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3a))
        self.wait(2.5)
        b3b = Tex("The polar solvent DISSOLVES minerals from rock").scale(0.9).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3b))
        self.wait(2.5)
        b3c = Tex("...and DEPOSITS them: dripstone caves, kettle scale").scale(0.9).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3c))
        self.wait(2.5)
        b3d = Tex("Biosphere: your body is about 60\\% water").scale(0.95).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3d))
        self.wait(2)
        b3e = Tex("Plants exhale vapour: TRANSPIRATION").scale(0.95).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3e))
        self.wait(3)

        # --- Band 4 (subtopic_3): why dam a river ---
        self.next_band(4)
        b4t = Tex("Dams: the case for the wall").scale(1.15).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4t))
        self.wait(2)
        b4a = Tex("Rain is seasonal; thirst is daily").scale(1.0).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4a))
        self.wait(2.5)
        b4b = Tex("Store the flood for the drought").scale(1.0).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4b))
        self.wait(2)
        b4c = Tex("Drinking water, irrigation, hydroelectric power").scale(0.95).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4c))
        self.wait(2.5)
        b4d = Tex("Katse feeds Gauteng; Theewaterskloof carried Cape Town").scale(0.85).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4d))
        self.wait(3)

        # --- Band 5 (subtopic_3): the costs, and how to study them ---
        self.next_band(5)
        b5t = Tex("The costs, upstream to downstream").scale(1.1).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5t))
        self.wait(2)
        b5a = Tex("Upstream: the valley drowns; people are moved").scale(0.9).shift(band_shift(5) + UP * 1.3)
        self.play(Write(b5a))
        self.wait(2.5)
        b5b = Tex("Downstream: floods stop, fish blocked at the wall").scale(0.9).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5b))
        self.wait(2.5)
        b5c = Tex("SEDIMENT trapped: reservoir fills, floodplains starve").scale(0.9).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(b5c))
        self.wait(2.5)
        b5d = Tex("Study it: interview residents, read the literature").scale(0.9).shift(band_shift(5) + DOWN * 1.5)
        self.play(Write(b5d))
        self.wait(2)
        b5e = Tex("Weigh benefits AND costs — no slogans").scale(0.95).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5e))
        self.play(Create(SurroundingRectangle(b5e, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): testing water ---
        self.next_band(6)
        b6t = Tex("Testing a water sample").scale(1.2).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6t))
        self.wait(2)
        b6a = Tex("pH first: 0 — acid, 7 — neutral, 14 — alkali").scale(0.95).shift(band_shift(6) + UP * 1.3)
        self.play(Write(b6a))
        self.wait(2.5)
        b6b = Tex("HNO$_3$ then AgNO$_3$: white $\\to$ Cl$^-$").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6b))
        self.wait(2.5)
        b6c = Tex("HNO$_3$ then Ba(NO$_3$)$_2$: lasting white $\\to$ SO$_4^{2-}$").scale(0.9).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6c))
        self.wait(2.5)
        b6d = Tex("Nitrates/nitrites high: fertiliser or sewage warning").scale(0.9).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(b6d))
        self.wait(2)
        b6e = Tex("Microscope: a drop of dam water is a zoo").scale(0.9).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6e))
        self.wait(3)

        # --- Band 7 (subtopic_4): purifying water ---
        self.next_band(7)
        b7t = Tex("Purifying: three stages in order").scale(1.15).shift(band_shift(7) + UP * 2.3)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex("1. SEDIMENTATION — stand still, grit sinks").scale(0.95).shift(band_shift(7) + UP * 1.3)
        self.play(Write(b7a))
        self.wait(2.5)
        b7b = Tex("2. FILTRATION — sand and gravel trap particles").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7b))
        self.wait(2.5)
        b7c = Tex("3. DISINFECTION — chlorine or a boil kills microbes").scale(0.9).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7c))
        self.wait(2.5)
        b7d = Tex("Filters never catch microbes; boils never remove salt").scale(0.85).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7d))
        self.wait(2)
        b7e = Tex("Dissolved ions: only distillation removes them").scale(0.9).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7e))
        self.play(Create(SurroundingRectangle(b7e, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the bucket planet ---
        self.next_band(8)
        b8t = Tex("The bucket planet").scale(1.2).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("All Earth's water: one twenty-litre bucket").scale(1.0).shift(band_shift(8) + UP * 1.3)
        self.play(Write(b8a))
        self.wait(2.5)
        b8b = Tex("Just over nineteen litres: salty sea").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex("Most of the rest: ice, out of reach").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8c))
        self.wait(2)
        b8d = Tex("Your share: a few TABLESPOONS").scale(1.1).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8d))
        self.play(Create(SurroundingRectangle(b8d, color=GREEN)))
        self.wait(2.5)
        b8e = Tex("Groundwater: the invisible sponge under your feet").scale(0.9).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8e))
        self.wait(3)

        # --- Band 9 (subtopic_6): the longest round trip ---
        self.next_band(9)
        b9t = Tex("One drop's round trip").scale(1.2).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Ocean $\\to$ vapour $\\to$ cloud $\\to$ mountain rain").scale(0.95).shift(band_shift(9) + UP * 1.3)
        self.play(Write(b9a))
        self.wait(2.5)
        b9b = Tex("Soaks in — dissolves rock on the way down").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = Tex("River $\\to$ maize root $\\to$ leaf $\\to$ cloud again").scale(0.95).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9c))
        self.wait(2.5)
        b9d = Tex("Dam $\\to$ treatment works $\\to$ a school tap").scale(0.95).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9d))
        self.wait(2)
        b9e = Tex("Rivers deliver salts; evaporation leaves them: salty sea").scale(0.85).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9e))
        self.wait(3)

        # --- Band 10 (subtopic_7): two banks of opinions ---
        self.next_band(10)
        b10t = Tex("The river with two banks of opinions").scale(1.1).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("This bank: taps, fields, turbines — the drought beaten").scale(0.85).shift(band_shift(10) + UP * 1.3)
        self.play(Write(b10a))
        self.wait(2.5)
        b10b = Tex("That bank: drowned valley, tamed river, trapped silt").scale(0.85).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10b))
        self.wait(2.5)
        b10c = Tex("Wrong question: good or bad?").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10c))
        self.wait(2)
        b10d = Tex("Right questions: who gains, who loses, what softens it?").scale(0.85).shift(band_shift(10) + DOWN * 1.6)
        self.play(Write(b10d))
        self.play(Create(SurroundingRectangle(b10d, color=GREEN)))
        self.wait(2.5)
        b10e = Tex("Fish ladders, managed releases, fair compensation").scale(0.85).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10e))
        self.wait(3)

        # --- Band 11 (subtopic_7): the chemist's checkpoint ---
        self.next_band(11)
        b11t = Tex("The chemist's checkpoint").scale(1.2).shift(band_shift(11) + UP * 2.3)
        self.play(Write(b11t))
        self.wait(2)
        b11a = Tex("Settle it $\\to$ filter it $\\to$ chlorinate or boil").scale(0.95).shift(band_shift(11) + UP * 1.2)
        self.play(Write(b11a))
        self.wait(2.5)
        b11b = Tex("Filters catch particles, never microbes").scale(0.95).shift(band_shift(11) + UP * 0.3)
        self.play(Write(b11b))
        self.wait(2.5)
        b11c = Tex("Boiling kills microbes, never removes salt").scale(0.95).shift(band_shift(11) + DOWN * 0.6)
        self.play(Write(b11c))
        self.wait(2.5)
        b11d = Tex("The tablespoons are precious — chemistry keeps them safe").scale(0.85).shift(band_shift(11) + DOWN * 1.7)
        self.play(Write(b11d))
        self.play(Create(SurroundingRectangle(b11d, color=GREEN)))
        self.wait(4)
