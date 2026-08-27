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

# Band-layout whiteboard scene for the IEB session "Soil Erosion in South
# Africa" (grade 11, term 4). Seven subtopics of the duo: Part 1 Expert
# (subtopics 1-4), Part 2 Simplifier (subtopics 5-7). Band time apportioned
# to subtopics.json (225/240/225/240/185/200/205 of 1520 s). Exporter-safe
# primitives only; diagrams (horizon stack, erosion staircase, gabion channel)
# hand-built from Line/Arrow/Dot/Rectangle/Tex element by element.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class SoilErosionSouthAfricaSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the living skin and its horizons
        title = Tex("Soil Erosion in South Africa").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        # Horizon stack: three rectangles labelled.
        top_h = Rectangle(width=4.6, height=0.6, color=GREEN).shift(UP * 1.0 + LEFT * 2.4)
        top_lab = Tex("topsoil: humus, fertility").scale(0.7).shift(UP * 1.0 + RIGHT * 2.6)
        mid_h = Rectangle(width=4.6, height=0.8, color=YELLOW).shift(UP * 0.25 + LEFT * 2.4)
        mid_lab = Tex("subsoil: poorer").scale(0.7).shift(UP * 0.25 + RIGHT * 2.6)
        bot_h = Rectangle(width=4.6, height=1.0, color=GREY).shift(DOWN * 0.7 + LEFT * 2.4)
        bot_lab = Tex("weathered $\\to$ parent rock").scale(0.7).shift(DOWN * 0.7 + RIGHT * 2.6)
        self.play(Create(top_h), Write(top_lab))
        self.play(Create(mid_h), Write(mid_lab))
        self.play(Create(bot_h), Write(bot_lab))
        self.wait(2)
        b0_l1 = Tex(r"Centuries to build a few cm — one storm to strip it").scale(0.85).shift(DOWN * 1.9)
        self.play(Write(b0_l1))
        self.play(Create(SurroundingRectangle(b0_l1, color=GREEN)))
        self.wait(2)
        b0_l2 = Tex(r"Arable: $\approx$ 12\%; high-potential: $\approx$ 3\%").scale(0.9).shift(DOWN * 2.8)
        self.play(Write(b0_l2))
        self.wait(3)

        # --- Band 1 (subtopic_1): the asymmetry and the bodyguard
        self.next_band(1)
        b1_title = Tex("Non-renewable, and the bodyguard").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Loss: several hundred million tonnes a year,").scale(0.9).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex(r"riding the rivers to the ocean").scale(0.9).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex(r"Vegetation $=$ the soil's bodyguard:").scale(0.95).shift(band_shift(1) + DOWN * 0.5)
        self.play(Write(b1_l3))
        self.wait(1.5)
        b1_l4 = Tex(r"leaves soften rain, roots bind crumbs,").scale(0.9).shift(band_shift(1) + DOWN * 1.3)
        b1_l5 = Tex(r"litter feeds the binding humus").scale(0.9).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(2)
        b1_l6 = Tex(r"Every cause of erosion fires the bodyguard").scale(0.95).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l6))
        self.play(Create(SurroundingRectangle(b1_l6, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): physical causes — the water sequence
        self.next_band(2)
        b2_title = Tex("Physical causes: the water staircase").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        # Four-step staircase of labels joined by arrows.
        steps = [
            ("splash", UP * 1.2 + LEFT * 4.2),
            ("sheet", UP * 0.4 + LEFT * 1.6),
            ("rill", DOWN * 0.4 + RIGHT * 1.0),
            ("gully / donga", DOWN * 1.2 + RIGHT * 3.6),
        ]
        prev = None
        for name, pos in steps:
            lab = Tex(name).scale(0.9).shift(band_shift(2) + pos)
            self.play(Write(lab))
            if prev is not None:
                ar = Arrow(prev.get_right(), lab.get_left(), buff=0.1)
                self.play(Create(ar), run_time=0.5)
            prev = lab
            self.wait(1.2)
        b2_l1 = Tex(r"Wind lifts fine dry soil: the Dust Bowl lesson").scale(0.9).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex(r"Bare ground is the precondition — usually made").scale(0.9).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): human and animal causes
        self.next_band(3)
        b3_title = Tex("Human and animal causes").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Overcultivation mines the humus; downslope").scale(0.9).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"furrows become drains; deforestation").scale(0.9).shift(band_shift(3) + UP * 0.5)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex(r"Mining, construction, settlement edges").scale(0.9).shift(band_shift(3) + DOWN * 0.3)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex(r"Past: homelands packed people and stock").scale(0.9).shift(band_shift(3) + DOWN * 1.1)
        b3_l5 = Tex(r"onto the poorest land — scars remain").scale(0.9).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(2.5)
        b3_l6 = Tex(r"Animals: overgrazing bares the surface;").scale(0.9).shift(band_shift(3) + DOWN * 2.6)
        b3_l7 = Tex(r"trampled paths become the first channels").scale(0.9).shift(band_shift(3) + DOWN * 3.3)
        self.play(Write(b3_l6))
        self.play(Write(b3_l7))
        self.wait(3)

        # --- Band 4 (subtopic_3): evidence on the landscape
        self.next_band(4)
        b4_title = Tex("Evidence on the landscape").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Dongas: Eastern Cape, Thukela basin,").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex(r"Sekhukhune — densest in former homelands").scale(0.9).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex(r"Brown rivers after storms: topsoil in transit").scale(0.9).shift(band_shift(4) + DOWN * 0.4)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex(r"Hazelmere Dam, Mdloti River: silt swallowed").scale(0.9).shift(band_shift(4) + DOWN * 1.3)
        b4_l5 = Tex(r"storage — the wall had to be raised").scale(0.9).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(2.5)
        b4_l6 = Tex(r"Dust plumes, naked roots, fence-post pedestals").scale(0.85).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_3): effects on people and environment
        self.next_band(5)
        b5_title = Tex("Effects: people and environment").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_mid = Line(band_shift(5) + UP * 1.6, band_shift(5) + DOWN * 2.4)
        self.play(Create(b5_mid))
        b5_ph = Tex("People", color=YELLOW).scale(1.0).shift(band_shift(5) + UP * 1.3 + LEFT * 3.2)
        b5_eh = Tex("Environment", color=GREEN).scale(1.0).shift(band_shift(5) + UP * 1.3 + RIGHT * 3.2)
        self.play(Write(b5_ph), Write(b5_eh))
        self.wait(1.5)
        b5_p1 = Tex(r"yields fall,\\ incomes shrink").scale(0.85).shift(band_shift(5) + UP * 0.4 + LEFT * 3.2)
        b5_e1 = Tex(r"sediment chokes\\ rivers, wetlands").scale(0.85).shift(band_shift(5) + UP * 0.4 + RIGHT * 3.2)
        self.play(Write(b5_p1))
        self.play(Write(b5_e1))
        self.wait(2)
        b5_p2 = Tex(r"dams silt up;\\ water security paid").scale(0.85).shift(band_shift(5) + DOWN * 0.8 + LEFT * 3.2)
        b5_e2 = Tex(r"sponge lost: floods\\ up, dry flows down").scale(0.85).shift(band_shift(5) + DOWN * 0.8 + RIGHT * 3.2)
        self.play(Write(b5_p2))
        self.play(Write(b5_e2))
        self.wait(2)
        b5_p3 = Tex(r"livelihoods collapse;\\ migration to towns").scale(0.85).shift(band_shift(5) + DOWN * 2.0 + LEFT * 3.2)
        b5_e3 = Tex(r"biodiversity thins;\\ desertification").scale(0.85).shift(band_shift(5) + DOWN * 2.0 + RIGHT * 3.2)
        self.play(Write(b5_p3))
        self.play(Write(b5_e3))
        self.wait(2)
        b5_l1 = Tex(r"A disaster in slow motion").scale(1.0).shift(band_shift(5) + DOWN * 3.1)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): prevention
        self.next_band(6)
        b6_title = Tex("Prevention: keep the cloth covered").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Contour ploughing: furrows as tiny dams").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"Strip cropping; rotation and rest").scale(0.95).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex(r"Mulch and stubble: the winter blanket").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        b6_l4 = Tex(r"Windbreak rows against dry-season wind").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(1.6)
        b6_l5 = Tex(r"Grazing: carrying capacity, camp rotation,").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        b6_l6 = Tex(r"spread the watering routes").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): control and the GIS toolkit
        self.next_band(7)
        b7_title = Tex("Control, and the GIS toolkit").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        # Gabion channel: channel line with three block rectangles.
        chan = Line(band_shift(7) + UP * 1.4 + LEFT * 4.0, band_shift(7) + UP * 0.6 + RIGHT * 4.0)
        self.play(Create(chan))
        g1 = Rectangle(width=0.5, height=0.5).shift(band_shift(7) + UP * 1.25 + LEFT * 2.4)
        g2 = Rectangle(width=0.5, height=0.5).shift(band_shift(7) + UP * 1.0 + LEFT * 0.2)
        g3 = Rectangle(width=0.5, height=0.5).shift(band_shift(7) + UP * 0.8 + RIGHT * 2.0)
        self.play(Create(g1), Create(g2), Create(g3))
        b7_l1 = Tex(r"Gabions: speed bumps that trap sediment").scale(0.9).shift(band_shift(7) + DOWN * 0.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex(r"Re-vegetate banks; fence healing land;").scale(0.9).shift(band_shift(7) + DOWN * 0.9)
        b7_l3 = Tex(r"LandCare, Working for Water, Working on Fire").scale(0.85).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l2))
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex(r"GIS: spatially referenced data; spatial and").scale(0.85).shift(band_shift(7) + DOWN * 2.4)
        b7_l5 = Tex(r"spectral resolution; point, line, area layers").scale(0.85).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the teaspoon bank account
        self.next_band(8)
        b8_title = Tex("The bank account that fills by teaspoons").scale(1.05).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Deposits: one teaspoon a year — centuries").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex(r"for a few centimetres of fertile ground").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"Withdrawals: one storm, decades gone brown").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex(r"Ten plates: one arable, a corner first-class —").scale(0.9).shift(band_shift(8) + DOWN * 1.3)
        b8_l5 = Tex(r"sixty million people eat from it").scale(0.95).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2.5)
        b8_l6 = Tex(r"Every cause $=$ the bodyguard was fired").scale(0.95).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_6): footpath to canyon
        self.next_band(9)
        b9_title = Tex("How a footpath becomes a canyon").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Act 1: overgrazing bares a patch").scale(0.9).shift(band_shift(9) + UP * 1.3)
        b9_l2 = Tex(r"Act 2: raindrop hammers splash soil loose").scale(0.9).shift(band_shift(9) + UP * 0.6)
        b9_l3 = Tex(r"Act 3: compacted ground refuses to drink — sheetwash").scale(0.8).shift(band_shift(9) + DOWN * 0.1)
        b9_l4 = Tex(r"Act 4: finger-channels — rills — easy to ignore").scale(0.85).shift(band_shift(9) + DOWN * 0.8)
        b9_l5 = Tex(r"Act 5: rills merge — a DONGA opens").scale(0.9).shift(band_shift(9) + DOWN * 1.5)
        for m in (b9_l1, b9_l2, b9_l3, b9_l4, b9_l5):
            self.play(Write(m))
            self.wait(1.5)
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(1.5)
        b9_l6 = Tex(r"The hardened cattle path was the first drain;").scale(0.85).shift(band_shift(9) + DOWN * 2.4)
        b9_l7 = Tex(r"history crowded the hooves — past cause, present scar").scale(0.8).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(b9_l6))
        self.play(Write(b9_l7))
        self.wait(3)

        # --- Band 10 (subtopic_7): stitching the land back together
        self.next_band(10)
        b10_title = Tex("Stitching the land back together").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Prevent: plough along the slope; blanket the").scale(0.9).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex(r"fields; rotate crops; rest the camps").scale(0.9).shift(band_shift(10) + UP * 0.5)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex(r"Control: gabion speed bumps, planted banks,").scale(0.9).shift(band_shift(10) + DOWN * 0.4)
        b10_l4 = Tex(r"fences and years of patience").scale(0.9).shift(band_shift(10) + DOWN * 1.1)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex(r"From orbit: infrared betrays bare ground;").scale(0.9).shift(band_shift(10) + DOWN * 2.0)
        b10_l6 = Tex(r"point, line and area layers rank the valleys").scale(0.9).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.wait(2.5)
        b10_l7 = Tex(r"Hold the wound and the cure together").scale(0.95).shift(band_shift(10) + DOWN * 3.5)
        self.play(Write(b10_l7))
        self.play(Create(SurroundingRectangle(b10_l7, color=GREEN)))
        self.wait(4)
