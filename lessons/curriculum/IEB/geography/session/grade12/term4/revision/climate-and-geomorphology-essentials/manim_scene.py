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

# Band-layout whiteboard scene for the IEB Grade 12 Geography session duo
# "Climate and Geomorphology Essentials" (term 4 revision, week one). Bands
# cover all seven subtopics (Part 1 — Expert: subtopics 1-4; Part 2 —
# Simplifier: subtopics 5-7) with dwell time proportional to subtopics.json
# (260/250/250/260/200/200/200 of 1620 s). The cyclone anatomy, valley night
# and longitudinal profile are hand-built from exporter-safe primitives only
# (Tex/MathTex/Line/Arrow/Dot/Circle/Rectangle/VGroup); add-only lifecycle,
# the camera moves down between bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ClimateGeomorphologyEssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(15)

        # --- Band 0 (subtopic_1): mid-latitude cyclone essentials ---
        title = Tex("Climate and Geomorphology Essentials").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Mid-latitude cyclone: born on the polar front,").scale(0.95).shift(UP * 0.9)
        b0_l2 = Tex(r"30--60$^\circ$S, cold air refusing to blend with warm").scale(0.92).shift(UP * 0.2)
        self.play(Write(b0_l1)); self.wait(1.8)
        self.play(Write(b0_l2)); self.wait(2)
        b0_l3 = Tex(r"Ingredients: temperature contrast, Coriolis spin,").scale(0.92).shift(DOWN * 0.6)
        b0_l4 = Tex(r"upper-air divergence beneath the jet stream").scale(0.95).shift(DOWN * 1.3)
        self.play(Write(b0_l3)); self.wait(1.6)
        self.play(Write(b0_l4)); self.wait(1.8)
        b0_l5 = Tex(r"Three acts: wave $\rightarrow$ mature $\rightarrow$ occlusion").scale(1.0).shift(DOWN * 2.2)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(2)
        b0_l6 = Tex(r"Winter rainfall for the Western Cape").scale(0.95).shift(DOWN * 3.0)
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_1): tropical cyclone anatomy, drawn ---
        self.next_band(1)
        b1_t = Tex("Tropical cyclone: fuel, spin, calm aloft").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex(r"Sea warmer than 26,5$^\circ$C, 5--30$^\circ$ latitude,").scale(0.95).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex(r"late summer; never born on the equator").scale(0.95).shift(band_shift(1) + UP * 0.55)
        self.play(Write(b1_l1)); self.wait(1.6)
        self.play(Write(b1_l2)); self.wait(1.8)
        sc1 = band_shift(1) + DOWN * 1.5 + LEFT * 2.6
        eye = Circle(radius=0.35, color=WHITE).shift(sc1)
        wall = Circle(radius=1.05, color=RED).shift(sc1)
        self.play(Create(wall))
        self.play(Create(eye))
        l_eye = Tex(r"eye: sinking air, still and clear").scale(0.8).shift(sc1 + UP * 1.6)
        l_wall = Tex(r"eye wall: the screaming winds").scale(0.8).shift(sc1 + DOWN * 1.6)
        self.play(Write(l_eye)); self.wait(1.2)
        self.play(Write(l_wall)); self.wait(1.5)
        b1_l3 = Tex(r"Stages: disturbance, depression,").scale(0.9).shift(band_shift(1) + DOWN * 1.0 + RIGHT * 3.2)
        b1_l4 = Tex(r"storm (named), cyclone").scale(0.9).shift(band_shift(1) + DOWN * 1.6 + RIGHT * 3.2)
        b1_l5 = Tex(r"Collapses over land or cool water").scale(0.85).shift(band_shift(1) + DOWN * 2.2 + RIGHT * 3.2)
        self.play(Write(b1_l3)); self.wait(1.4)
        self.play(Write(b1_l4)); self.wait(1.4)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): the three highs and their seasons ---
        self.next_band(2)
        b2_t = Tex("Three highs write the rainfall timetable").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex(r"South Atlantic, South Indian, Kalahari").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1)); self.wait(1.8)
        b2_l2 = Tex(r"Winter: highs drift north, the Kalahari High").scale(1.0).shift(band_shift(2) + UP * 0.3)
        b2_l3 = Tex(r"caps the plateau --- inversion, frost, sun").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2_l2)); self.wait(1.6)
        self.play(Write(b2_l3)); self.wait(1.8)
        b2_l4 = Tex(r"Summer: highs slide south, the inversion lifts,").scale(0.95).shift(band_shift(2) + DOWN * 1.2)
        b2_l5 = Tex(r"moist air pushes in --- thunderstorm season").scale(0.95).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4)); self.wait(1.6)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(VGroup(b2_l4, b2_l5), color=GREEN)))
        self.wait(2)
        b2_l6 = Tex(r"Disturbances: moisture front, coastal low, berg wind").scale(0.9).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): the valley on a winter night, drawn ---
        self.next_band(3)
        b3_t = Tex("A winter night in the valley").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        sc3 = band_shift(3) + DOWN * 0.7
        vp = VGroup(
            Line(sc3 + LEFT * 4.2 + UP * 1.9, sc3 + LEFT * 1.2 + DOWN * 0.5, stroke_width=4),
            Line(sc3 + LEFT * 1.2 + DOWN * 0.5, sc3 + RIGHT * 1.2 + DOWN * 0.5, stroke_width=4),
            Line(sc3 + RIGHT * 1.2 + DOWN * 0.5, sc3 + RIGHT * 4.2 + UP * 1.9, stroke_width=4),
        )
        for seg in vp:
            self.play(Create(seg), run_time=0.6)
        a1 = Arrow(sc3 + LEFT * 3.3 + UP * 1.3, sc3 + LEFT * 1.9 + UP * 0.1, color=BLUE, buff=0.1)
        a2 = Arrow(sc3 + RIGHT * 3.3 + UP * 1.3, sc3 + RIGHT * 1.9 + UP * 0.1, color=BLUE, buff=0.1)
        l_kat = Tex(r"katabatic winds drain the cold air down").scale(0.85).shift(sc3 + UP * 2.0)
        self.play(Create(a1), Create(a2), Write(l_kat))
        self.wait(1.8)
        l_floor = Tex(r"cold pool: frost, radiation fog").scale(0.8).shift(sc3 + DOWN * 1.1)
        self.play(Write(l_floor))
        self.wait(1.4)
        d_tb = Dot(sc3 + LEFT * 2.7 + UP * 0.7, color=GREEN)
        l_tb = Tex(r"thermal belt: orchards").scale(0.8).shift(sc3 + LEFT * 3.3 + UP * 0.1)
        self.play(Create(d_tb), Write(l_tb))
        self.wait(1.5)
        b3_l1 = Tex(r"Aspect: the north-facing slope catches the sun").scale(0.9).shift(sc3 + DOWN * 1.9)
        self.play(Write(b3_l1))
        self.wait(1.8)
        b3_l2 = Tex(r"City: heat island + pollution dome").scale(0.9).shift(sc3 + DOWN * 2.6)
        self.play(Write(b3_l2))
        self.wait(3)

        # --- Band 4 (subtopic_3): basins, patterns, density ---
        self.next_band(4)
        b4_t = Tex("Drainage: basins and patterns").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex(r"Basin: every square metre one river drains,").scale(0.95).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex(r"fenced by the watershed").scale(1.0).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1)); self.wait(1.5)
        self.play(Write(b4_l2)); self.wait(1.8)
        b4_l3 = Tex(r"Patterns are geology speaking: dendritic--uniform,").scale(0.9).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex(r"trellis--folded, radial--dome, rectangular--joints").scale(0.9).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4_l3)); self.wait(1.6)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = MathTex(r"\text{Density} = \frac{\text{total stream length}}{\text{basin area}}").scale(0.93).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4_l5))
        self.wait(1.8)
        b4_l6 = Tex(r"Order rises only when two equal orders meet").scale(0.9).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_3): the longitudinal profile, drawn ---
        self.next_band(5)
        b5_t = Tex("Profiles and grading").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        sc5 = band_shift(5) + DOWN * 0.4
        # concave longitudinal profile as a 3-segment chain
        prof = VGroup(
            Line(sc5 + LEFT * 4.0 + UP * 1.8, sc5 + LEFT * 2.0 + UP * 0.0, color=BLUE, stroke_width=4),
            Line(sc5 + LEFT * 2.0 + UP * 0.0, sc5 + RIGHT * 0.6 + DOWN * 0.9, color=BLUE, stroke_width=4),
            Line(sc5 + RIGHT * 0.6 + DOWN * 0.9, sc5 + RIGHT * 4.0 + DOWN * 1.2, color=BLUE, stroke_width=4),
        )
        l_src = Tex(r"source: steep").scale(0.8).shift(sc5 + LEFT * 4.0 + UP * 2.3)
        l_mouth = Tex(r"mouth: nearly flat").scale(0.8).shift(sc5 + RIGHT * 4.0 + DOWN * 0.6)
        self.play(Create(prof[0]), Write(l_src))
        self.play(Create(prof[1]))
        self.play(Create(prof[2]), Write(l_mouth))
        self.wait(1.8)
        b5_l1 = Tex(r"Graded: smooth concave, energy matches load").scale(0.95).shift(sc5 + DOWN * 1.8)
        b5_l2 = Tex(r"Ungraded: knickpoints, working toward base level").scale(0.95).shift(sc5 + DOWN * 2.5)
        self.play(Write(b5_l1)); self.wait(1.6)
        self.play(Write(b5_l2))
        self.wait(3)

        # --- Band 6 (subtopic_4): landforms and rejuvenation ---
        self.next_band(6)
        b6_t = Tex("Landforms, and a river made young").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex(r"Upper: waterfalls, rapids (vertical cutting)").scale(0.95).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex(r"Middle-lower: meanders, oxbows, floodplain,").scale(0.95).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex(r"levees, delta if the sea is too weak").scale(0.95).shift(band_shift(6) + DOWN * 0.3)
        for m in (b6_l1, b6_l2, b6_l3):
            self.play(Write(m))
            self.wait(1.7)
        b6_l4 = Tex(r"Rejuvenation: uplift or a lower base level").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_l4)); self.wait(1.8)
        b6_l5 = Tex(r"Evidence: knickpoint, paired terraces,").scale(0.95).shift(band_shift(6) + DOWN * 2.0)
        b6_l6 = Tex(r"valley-in-valley, incised meanders").scale(0.95).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l5)); self.wait(1.5)
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): capture and catchment care ---
        self.next_band(7)
        b7_t = Tex("River capture and catchment management").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex(r"Captor gnaws headward, beheads its neighbour:").scale(0.95).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex(r"elbow of capture, wind gap, misfit stream").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1)); self.wait(1.6)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2)
        b7_l3 = Tex(r"Human pressure: eutrophication, overgrazing,").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex(r"deforestation, homes on the floodplain").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l3)); self.wait(1.6)
        self.play(Write(b7_l4)); self.wait(1.8)
        b7_l5 = Tex(r"Case: the Vaal's sewage and algae crises;").scale(0.95).shift(band_shift(7) + DOWN * 2.1)
        b7_l6 = Tex(r"fix: wetlands, Working for Water, fencing").scale(0.95).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l5)); self.wait(1.5)
        self.play(Write(b7_l6))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): three storms, three characters ---
        self.next_band(8)
        b8_t = Tex("Three storms, three characters").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex(r"Winter visitor from the west: the cold front,").scale(0.95).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex(r"signature NW wind $\rightarrow$ wild wet spell $\rightarrow$ SW wind").scale(0.9).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1)); self.wait(1.7)
        self.play(Write(b8_l2)); self.wait(2)
        b8_l3 = Tex(r"Summer bully from the warm sea: a calm eye,").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex(r"starves once off the warm water").scale(0.95).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(b8_l3)); self.wait(1.6)
        self.play(Write(b8_l4)); self.wait(1.8)
        b8_l5 = Tex(r"Quiet giant: sits and squashes --- sinking air,").scale(0.95).shift(band_shift(8) + DOWN * 1.9)
        b8_l6 = Tex(r"sunny frost, and the fire-fanning berg wind").scale(0.95).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l5)); self.wait(1.6)
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): a river's whole life in one walk ---
        self.next_band(9)
        b9_t = Tex("A river's whole life in one walk").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex(r"Infant in the mountains: V-valley, waterfalls").scale(0.95).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex(r"Middle age: meanders wander, oxbow scars").scale(0.95).shift(band_shift(9) + UP * 0.4)
        b9_l3 = Tex(r"Old age: floodplain, levees, delta").scale(0.95).shift(band_shift(9) + DOWN * 0.3)
        for m in (b9_l1, b9_l2, b9_l3):
            self.play(Write(m))
            self.wait(1.8)
        b9_l4 = Tex(r"Twist 1: rejuvenation --- strong coffee for").scale(0.95).shift(band_shift(9) + DOWN * 1.2)
        b9_l5 = Tex(r"the pensioner; incised meanders, terraces").scale(0.95).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l4)); self.wait(1.5)
        self.play(Write(b9_l5)); self.wait(1.8)
        b9_l6 = Tex(r"Twist 2: capture --- the wind gap is the evidence").scale(0.9).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the marks you can bank tonight ---
        self.next_band(10)
        b10_t = Tex("The marks you can bank tonight").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex(r"1. Draw the three synoptic portraits + winds").scale(0.95).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex(r"2. Write the cold front in six short lines").scale(0.95).shift(band_shift(10) + UP * 0.4)
        b10_l3 = Tex(r"3. Seven patterns, each with its rock clue").scale(0.95).shift(band_shift(10) + DOWN * 0.3)
        b10_l4 = Tex(r"4. One paragraph: $4 \times 2$, full sentences").scale(0.95).shift(band_shift(10) + DOWN * 1.0)
        b10_l5 = Tex(r"5. Case-study flashcards, one line each").scale(0.95).shift(band_shift(10) + DOWN * 1.7)
        for m in (b10_l1, b10_l2, b10_l3, b10_l4, b10_l5):
            self.play(Write(m))
            self.wait(1.8)
        b10_l6 = Tex(r"Definitions are gifts --- say them aloud").scale(0.9).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
