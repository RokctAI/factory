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

# Band-layout whiteboard scene for the session duo "Atmosphere layers and
# composition" (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Diagrams are hand-built from Line/Arrow/Dot/Circle/Rectangle/Tex only, in
# sync with the script; add-only lifecycle, camera moves down band by band.
# Subtopic durations (s): 215/245/230/225/185/190/180 of 1470 — band dwell
# times are apportioned to match.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AtmosphereLayersSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the four figures for dry air ---
        title = Tex("Composition and Structure of the Atmosphere").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        c1 = Tex(r"Dry air, by volume:").scale(1.1).shift(UP * 1.3 + LEFT * 3)
        self.play(Write(c1))
        self.wait(1.5)
        c2 = Tex(r"Nitrogen — 78\%").scale(1.1).shift(UP * 0.5)
        c3 = Tex(r"Oxygen — 21\%").scale(1.1).shift(DOWN * 0.3)
        c4 = Tex(r"Argon — 0,93\%").scale(1.1).shift(DOWN * 1.1)
        c5 = Tex(r"Carbon dioxide — 0,04\%").scale(1.1).shift(DOWN * 1.9)
        self.play(Write(c2))
        self.wait(1.5)
        self.play(Write(c3))
        self.wait(1.5)
        self.play(Write(c4))
        self.wait(1.5)
        self.play(Write(c5))
        self.play(Create(SurroundingRectangle(VGroup(c2, c3, c4, c5), color=GREEN)))
        trap = Tex(r"Quoted for DRY air — say so").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(trap))
        self.wait(3)

        # --- Band 1 (subtopic_1): permanent vs variable + one job each ---
        self.next_band(1)
        b1t = Tex("Permanent gases vs variable components").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        b1a = Tex(r"Permanent: N$_2$, O$_2$, Ar — steady everywhere").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1b = Tex(r"Variable: water vapour, aerosols, ozone").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1a))
        self.wait(2)
        self.play(Write(b1b))
        self.wait(2)
        b1c = Tex(r"N$_2$: dilutes O$_2$, fixed into nitrates").scale(1.0).shift(band_shift(1) + DOWN * 0.6)
        b1d = Tex(r"CO$_2$: photosynthesis + greenhouse gas").scale(1.0).shift(band_shift(1) + DOWN * 1.4)
        b1e = Tex(r"Aerosols = condensation nuclei for cloud").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1c))
        self.wait(2)
        self.play(Write(b1d))
        self.wait(2)
        self.play(Write(b1e))
        self.wait(3)

        # --- Band 2 (subtopic_2): the four-layer stack, built upward ---
        self.next_band(2)
        b2t = Tex("Four layers, one test: temperature").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        ground = Line(LEFT * 4.5, RIGHT * 1.0, stroke_width=6).shift(band_shift(2) + DOWN * 2.7)
        self.play(Create(ground))
        l_tropo = Line(LEFT * 4.5, RIGHT * 1.0).shift(band_shift(2) + DOWN * 1.4)
        t_tropo = Tex(r"Troposphere 0–12 km: cools upward").scale(0.9).shift(band_shift(2) + DOWN * 2.05 + LEFT * 1.2)
        self.play(Create(l_tropo), Write(t_tropo))
        r_tropo = Tex(r"warmed from below; all weather").scale(0.8).shift(band_shift(2) + DOWN * 1.65 + RIGHT * 3.9)
        self.play(Write(r_tropo))
        self.wait(2)
        l_strato = Line(LEFT * 4.5, RIGHT * 1.0).shift(band_shift(2) + DOWN * 0.1)
        t_strato = Tex(r"Stratosphere to 50 km: warms upward").scale(0.9).shift(band_shift(2) + DOWN * 0.75 + LEFT * 1.2)
        self.play(Create(l_strato), Write(t_strato))
        r_strato = Tex(r"ozone heats it; still; airliners").scale(0.8).shift(band_shift(2) + DOWN * 0.35 + RIGHT * 3.9)
        self.play(Write(r_strato))
        self.wait(2)
        l_meso = Line(LEFT * 4.5, RIGHT * 1.0).shift(band_shift(2) + UP * 1.2)
        t_meso = Tex(r"Mesosphere to 80 km: cools again").scale(0.9).shift(band_shift(2) + UP * 0.55 + LEFT * 1.2)
        self.play(Create(l_meso), Write(t_meso))
        r_meso = Tex(r"mesopause $-90^\circ$C; meteors burn").scale(0.8).shift(band_shift(2) + UP * 0.95 + RIGHT * 3.9)
        self.play(Write(r_meso))
        self.wait(2)
        t_thermo = Tex(r"Thermosphere above 80 km: warms fast").scale(0.9).shift(band_shift(2) + UP * 1.75 + LEFT * 1.0)
        r_thermo = Tex(r"ionosphere + auroras").scale(0.8).shift(band_shift(2) + UP * 1.7 + RIGHT * 4.2)
        self.play(Write(t_thermo))
        self.play(Write(r_thermo))
        self.wait(3)

        # --- Band 3 (subtopic_2): zigzag graph read from the elbows ---
        self.next_band(3)
        b3t = Tex("Temperature against height: three elbows").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        ax_v = Arrow(band_shift(3) + LEFT * 3.2 + DOWN * 2.5, band_shift(3) + LEFT * 3.2 + UP * 1.6, buff=0)
        ax_h = Arrow(band_shift(3) + LEFT * 3.2 + DOWN * 2.5, band_shift(3) + RIGHT * 2.8 + DOWN * 2.5, buff=0)
        ax_vl = Tex("Height").scale(0.8).shift(band_shift(3) + LEFT * 4.2 + UP * 1.3)
        ax_hl = Tex("Temperature").scale(0.8).shift(band_shift(3) + RIGHT * 3.0 + DOWN * 2.9)
        self.play(Create(ax_v), Create(ax_h))
        self.play(Write(ax_vl), Write(ax_hl))
        self.wait(1.5)
        p0 = band_shift(3) + RIGHT * 1.2 + DOWN * 2.5
        p1 = band_shift(3) + LEFT * 1.6 + DOWN * 1.3
        p2 = band_shift(3) + RIGHT * 0.4 + DOWN * 0.1
        p3 = band_shift(3) + LEFT * 1.0 + UP * 0.9
        p4 = band_shift(3) + RIGHT * 1.8 + UP * 1.6
        seg1 = Line(p0, p1, color=BLUE)
        self.play(Create(seg1))
        d1 = Dot(p1, color=YELLOW)
        n1 = Tex(r"tropopause $-55^\circ$C").scale(0.75).shift(p1 + LEFT * 1.7)
        self.play(FadeIn(d1), Write(n1))
        self.wait(1.5)
        seg2 = Line(p1, p2, color=BLUE)
        self.play(Create(seg2))
        d2 = Dot(p2, color=YELLOW)
        n2 = Tex(r"stratopause $0^\circ$C").scale(0.75).shift(p2 + RIGHT * 2.0)
        self.play(FadeIn(d2), Write(n2))
        self.wait(1.5)
        seg3 = Line(p2, p3, color=BLUE)
        self.play(Create(seg3))
        d3 = Dot(p3, color=YELLOW)
        n3 = Tex(r"mesopause $-90^\circ$C").scale(0.75).shift(p3 + LEFT * 1.9)
        self.play(FadeIn(d3), Write(n3))
        self.wait(1.5)
        seg4 = Line(p3, p4, color=BLUE)
        self.play(Create(seg4))
        b3r = Tex("Label the pauses, place the layers").scale(0.95).shift(band_shift(3) + RIGHT * 2.6 + UP * 0.3)
        self.play(Write(b3r))
        self.wait(3)

        # --- Band 4 (subtopic_3): the shield and its destroyer ---
        self.next_band(4)
        b4t = Tex("Ozone: a shield 3 mm thin").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        b4a = Tex(r"O$_3$ at 20–30 km soaks up UV-B and UV-C").scale(1.05).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4a))
        self.wait(2)
        b4b = Tex(r"CFCs: spray cans, fridges, foams, solvents").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4c = Tex(r"Too stable for rain to remove — they climb").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        b4d = Tex(r"Stratospheric UV cracks them: chlorine freed").scale(1.0).shift(band_shift(4) + DOWN * 1.5)
        b4e = Tex(r"1 Cl atom $\rightarrow$ tens of thousands of O$_3$ lost").scale(1.0).shift(band_shift(4) + DOWN * 2.4)
        self.play(Write(b4b))
        self.wait(2)
        self.play(Write(b4c))
        self.wait(2)
        self.play(Write(b4d))
        self.wait(2)
        self.play(Write(b4e))
        self.play(Create(SurroundingRectangle(b4e, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the hole, the harm, the healing ---
        self.next_band(5)
        b5t = Tex("The hole, the harm, the healing").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        b5a = Tex(r"Antarctic thinning opens each southern spring").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5b = Tex(r"South Africa: next door, fierce sun,").scale(1.0).shift(band_shift(5) + UP * 0.4)
        b5b2 = Tex(r"world-ranking skin-cancer rates").scale(1.0).shift(band_shift(5) + DOWN * 0.2)
        b5c = Tex(r"Harm: cancer, cataracts, weak immunity,").scale(1.0).shift(band_shift(5) + DOWN * 1.0)
        b5c2 = Tex(r"phytoplankton and crop losses").scale(1.0).shift(band_shift(5) + DOWN * 1.6)
        b5d = Tex(r"Montreal Protocol 1987 — recovery measured").scale(1.0).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5a))
        self.wait(2)
        self.play(Write(b5b))
        self.play(Write(b5b2))
        self.wait(2)
        self.play(Write(b5c))
        self.play(Write(b5c2))
        self.wait(2)
        self.play(Write(b5d))
        self.play(Create(SurroundingRectangle(b5d, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): what the envelope does for us ---
        self.next_band(6)
        b6t = Tex("What the atmosphere does for us").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        b6a = Tex(r"O$_2$ for breathing, CO$_2$ for plants").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6b = Tex(r"Blanket: $15^\circ$C, not $-18^\circ$C").scale(1.0).shift(band_shift(6) + UP * 0.4)
        b6c = Tex(r"Filters UV; burns space debris").scale(1.0).shift(band_shift(6) + DOWN * 0.4)
        b6d = Tex(r"Runs the water cycle; exports heat").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        b6e = Tex(r"No moon-style day-night extremes").scale(1.0).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6a))
        self.wait(1.5)
        self.play(Write(b6b))
        self.wait(1.5)
        self.play(Write(b6c))
        self.wait(1.5)
        self.play(Write(b6d))
        self.wait(1.5)
        self.play(Write(b6e))
        self.wait(3)

        # --- Band 7 (subtopic_4): the working method + vocabulary guard ---
        self.next_band(7)
        b7t = Tex("The working method").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(1.5)
        b7a = Tex(r"1. Layers upward: height, direction,").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7a2 = Tex(r"reason, feature — all four, every time").scale(1.0).shift(band_shift(7) + UP * 0.6)
        b7b = Tex(r"2. Graphs: label the elbows first").scale(1.0).shift(band_shift(7) + DOWN * 0.2)
        b7c = Tex(r"3. Ozone: layer, cause, consequence").scale(1.0).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7a))
        self.play(Write(b7a2))
        self.wait(2)
        self.play(Write(b7b))
        self.wait(2)
        self.play(Write(b7c))
        self.wait(2)
        b7trap = Tex(r"Street-level ozone = the shield").scale(1.0).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7trap))
        self.play(Create(strike(b7trap)))
        b7fix = Tex(r"Street-level ozone is a pollutant").scale(1.0).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7fix))
        self.play(Create(SurroundingRectangle(b7fix, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the recipe — a choir of 100 ---
        self.next_band(8)
        b8t = Tex("The air recipe: a choir of 100").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        stage = Circle(radius=1.1, color=WHITE).shift(band_shift(8) + LEFT * 3.2 + UP * 0.2)
        self.play(Create(stage))
        s1 = Dot(band_shift(8) + LEFT * 3.6 + UP * 0.5, color=GREY)
        s2 = Dot(band_shift(8) + LEFT * 3.0 + UP * 0.6, color=GREY)
        s3 = Dot(band_shift(8) + LEFT * 3.5 + DOWN * 0.1, color=BLUE)
        s4 = Dot(band_shift(8) + LEFT * 2.8 + UP * 0.1, color=YELLOW)
        self.play(FadeIn(s1), FadeIn(s2), FadeIn(s3), FadeIn(s4))
        b8a = Tex(r"78 basses = nitrogen").scale(1.0).shift(band_shift(8) + RIGHT * 1.6 + UP * 1.0)
        b8b = Tex(r"21 tenors = oxygen").scale(1.0).shift(band_shift(8) + RIGHT * 1.5 + UP * 0.2)
        b8c = Tex(r"1 lone singer = the rest (mostly argon)").scale(1.0).shift(band_shift(8) + RIGHT * 2.0 + DOWN * 0.6)
        self.play(Write(b8a))
        self.wait(1.5)
        self.play(Write(b8b))
        self.wait(1.5)
        self.play(Write(b8c))
        self.wait(2)
        b8d = Tex(r"CO$_2$: 4 voices in a 10 000 stadium").scale(1.0).shift(band_shift(8) + DOWN * 1.6)
        b8e = Tex(r"Water vapour won't hold still — DRY air").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8d))
        self.wait(2)
        self.play(Write(b8e))
        self.play(Create(SurroundingRectangle(b8e, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): four camps, fires in the wrong places ---
        self.next_band(9)
        b9t = Tex("Four camps, fires in the wrong places").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        slope = Line(band_shift(9) + LEFT * 4.6 + DOWN * 2.8,
                     band_shift(9) + LEFT * 1.4 + UP * 1.8)
        self.play(Create(slope))
        c1m = Dot(band_shift(9) + LEFT * 4.3 + DOWN * 2.5, color=YELLOW)
        c2m = Dot(band_shift(9) + LEFT * 3.3 + DOWN * 1.1, color=YELLOW)
        c3m = Dot(band_shift(9) + LEFT * 2.4 + UP * 0.2, color=YELLOW)
        c4m = Dot(band_shift(9) + LEFT * 1.6 + UP * 1.5, color=YELLOW)
        self.play(FadeIn(c1m), FadeIn(c2m), FadeIn(c3m), FadeIn(c4m))
        g1 = Tex(r"Base: fire in the ground — cools up").scale(0.85).shift(band_shift(9) + RIGHT * 2.4 + DOWN * 2.3)
        g2 = Tex(r"Camp 2: fire overhead — warms up").scale(0.85).shift(band_shift(9) + RIGHT * 2.4 + DOWN * 1.2)
        g3 = Tex(r"Camp 3: no fire — coldest roof").scale(0.85).shift(band_shift(9) + RIGHT * 2.2 + DOWN * 0.05)
        g4 = Tex(r"Summit: raging fire, no air to warm").scale(0.85).shift(band_shift(9) + RIGHT * 2.3 + UP * 1.1)
        self.play(Write(g1))
        self.wait(2)
        self.play(Write(g2))
        self.wait(2)
        self.play(Write(g3))
        self.wait(2)
        self.play(Write(g4))
        self.wait(2)
        b9r = Tex(r"Climbing: DOWN, UP, DOWN, UP").scale(1.05).shift(band_shift(9) + RIGHT * 1.5 + UP * 2.0)
        self.play(Write(b9r))
        self.play(Create(SurroundingRectangle(b9r, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the shade net and the moth ---
        self.next_band(10)
        b10t = Tex("The shade net and the moth").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex(r"Ozone: a 3 mm shade net, 25 km up").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10b = Tex(r"CFC moths from old fridges eat it —").scale(1.0).shift(band_shift(10) + UP * 0.4)
        b10b2 = Tex(r"one Cl atom, a hole-punch that never blunts").scale(1.0).shift(band_shift(10) + DOWN * 0.2)
        b10c = Tex(r"Biggest tear: Antarctica, each spring").scale(1.0).shift(band_shift(10) + DOWN * 1.0)
        b10d = Tex(r"Montreal Protocol: the net re-weaving").scale(1.0).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10a))
        self.wait(2)
        self.play(Write(b10b))
        self.play(Write(b10b2))
        self.wait(2)
        self.play(Write(b10c))
        self.wait(2)
        self.play(Write(b10d))
        self.wait(2)
        b10e = Tex(r"Ozone: UV leaks IN at camp 2.").scale(0.95).shift(band_shift(10) + DOWN * 2.5)
        b10e2 = Tex(r"Greenhouse: heat locked at base camp").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10e))
        self.play(Write(b10e2))
        self.play(Create(SurroundingRectangle(VGroup(b10e, b10e2), color=GREEN)))
        self.wait(4)
