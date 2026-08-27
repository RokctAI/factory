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

# Band-layout whiteboard scene for "Station models and cold fronts" (Part 1
# Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7). Isobars are nested
# Circles, the station model is built from a Circle + Lines + Tex, the front
# is a Line with triangle ticks drawn as short Line pairs. Add-only
# lifecycle; camera moves down band by band.
# Subtopic durations (s): 215/255/210/270/175/195/180 of 1500.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class StationModelsColdFrontsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the chart, H and L ---
        title = Tex("Reading the Synoptic Chart").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        h1 = Circle(radius=1.5, color=WHITE).shift(LEFT * 3.1 + DOWN * 0.9)
        h2 = Circle(radius=0.9, color=WHITE).shift(LEFT * 3.1 + DOWN * 0.9)
        hl = Tex("H").scale(1.2).shift(LEFT * 3.1 + DOWN * 0.9)
        self.play(Create(h1), Create(h2), Write(hl))
        l1 = Circle(radius=1.5, color=WHITE).shift(RIGHT * 3.1 + DOWN * 0.9)
        l2 = Circle(radius=0.9, color=WHITE).shift(RIGHT * 3.1 + DOWN * 0.9)
        ll = Tex("L").scale(1.2).shift(RIGHT * 3.1 + DOWN * 0.9)
        self.play(Create(l1), Create(l2), Write(ll))
        self.wait(2)
        ht = Tex(r"air sinks: clear, settled").scale(0.8).shift(LEFT * 3.1 + DOWN * 2.9)
        lt = Tex(r"air rises: cloud, rain").scale(0.8).shift(RIGHT * 3.1 + DOWN * 2.9)
        self.play(Write(ht))
        self.play(Write(lt))
        self.wait(2)
        iso = Tex(r"Isobars: contours of pressure, in hPa").scale(0.95).shift(UP * 1.4)
        self.play(Write(iso))
        self.wait(3)

        # --- Band 1 (subtopic_1): spacing = wind ---
        self.next_band(1)
        b1t = Tex("Isobar spacing is a wind gauge").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        w_lines = VGroup(*[
            Line(UP * 0.6, DOWN * 0.6).shift(band_shift(1) + UP * 0.2 + LEFT * (4.2 - i * 1.2))
            for i in range(3)
        ])
        w_lab = Tex("wide: light air").scale(0.85).shift(band_shift(1) + DOWN * 1.2 + LEFT * 3.0)
        self.play(Create(w_lines), Write(w_lab))
        self.wait(2)
        t_lines = VGroup(*[
            Line(UP * 0.6, DOWN * 0.6).shift(band_shift(1) + UP * 0.2 + RIGHT * (1.8 + i * 0.35))
            for i in range(4)
        ])
        t_lab = Tex("crowded: strong wind").scale(0.85).shift(band_shift(1) + DOWN * 1.2 + RIGHT * 2.4)
        self.play(Create(t_lines), Write(t_lab))
        self.wait(2)
        b1c = Tex(r"Steep pressure gradient = fast air").scale(1.0).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1c))
        self.play(Create(SurroundingRectangle(b1c, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): building the station model ---
        self.next_band(2)
        b2t = Tex("The station model, piece by piece").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        stn = Circle(radius=0.7, color=WHITE).shift(band_shift(2) + DOWN * 0.4)
        self.play(Create(stn))
        temp = Tex("21").scale(0.9).shift(band_shift(2) + DOWN * 0.4 + LEFT * 1.5 + UP * 0.9)
        dew = Tex("18").scale(0.9).shift(band_shift(2) + DOWN * 0.4 + LEFT * 1.5 + DOWN * 0.6)
        self.play(Write(temp))
        self.wait(1.5)
        self.play(Write(dew))
        self.wait(1.5)
        shaft = Line(band_shift(2) + DOWN * 0.4 + UP * 0.5 + LEFT * 0.5,
                     band_shift(2) + UP * 1.6 + LEFT * 2.4)
        f1 = Line(band_shift(2) + UP * 1.6 + LEFT * 2.4, band_shift(2) + UP * 1.9 + LEFT * 1.8)
        f2 = Line(band_shift(2) + UP * 1.25 + LEFT * 2.05, band_shift(2) + UP * 1.42 + LEFT * 1.72)
        self.play(Create(shaft))
        self.play(Create(f1), Create(f2))
        self.wait(1.5)
        lab1 = Tex(r"temp 21, dew point 18 — gap 3").scale(0.9).shift(band_shift(2) + RIGHT * 2.9 + UP * 0.6)
        lab2 = Tex(r"7/8 oktas shaded").scale(0.9).shift(band_shift(2) + RIGHT * 2.6 + DOWN * 0.2)
        lab3 = Tex(r"NW shaft, 1½ feathers = 15 kt").scale(0.9).shift(band_shift(2) + RIGHT * 2.9 + DOWN * 1.0)
        self.play(Write(lab1))
        self.wait(1.5)
        self.play(Write(lab2))
        self.wait(1.5)
        self.play(Write(lab3))
        self.wait(3)

        # --- Band 3 (subtopic_2): reading the station ---
        self.next_band(3)
        b3t = Tex("Read it in one breath").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        r1 = Tex(r"Warm: $21^\circ$C").scale(1.0).shift(band_shift(3) + UP * 1.2)
        r2 = Tex(r"Nearly saturated: dew point $18^\circ$C").scale(1.0).shift(band_shift(3) + UP * 0.4)
        r3 = Tex(r"Sky closing: 7 oktas").scale(1.0).shift(band_shift(3) + DOWN * 0.4)
        r4 = Tex(r"Moist feed: NW at 15 knots").scale(1.0).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(r1))
        self.wait(1.5)
        self.play(Write(r2))
        self.wait(1.5)
        self.play(Write(r3))
        self.wait(1.5)
        self.play(Write(r4))
        self.wait(2)
        r5 = Tex(r"Every reading says: weather incoming").scale(1.0).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(r5))
        self.play(Create(SurroundingRectangle(r5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the cold front symbol ---
        self.next_band(4)
        b4t = Tex("The cold front: a line with teeth").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        fr = Line(band_shift(4) + LEFT * 4.2 + DOWN * 1.8, band_shift(4) + RIGHT * 3.6 + UP * 0.8, stroke_width=6, color=BLUE)
        self.play(Create(fr))
        # triangle teeth as line pairs on the advancing (upper-left) side
        for i in range(3):
            base = band_shift(4) + LEFT * (2.9 - i * 2.2) + DOWN * (1.35 - i * 0.72)
            t1 = Line(base, base + UP * 0.55 + LEFT * 0.1)
            t2 = Line(base + UP * 0.55 + LEFT * 0.1, base + RIGHT * 0.55 + UP * 0.18)
            self.play(Create(t1), Create(t2), run_time=0.6)
        self.wait(1.5)
        b4a = Tex(r"Teeth point where the front is going: NE").scale(0.95).shift(band_shift(4) + RIGHT * 1.2 + DOWN * 1.6)
        self.play(Write(b4a))
        self.wait(2)
        b4b = Tex(r"From the SW, under a passing depression").scale(0.95).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4b))
        self.wait(3)

        # --- Band 5 (subtopic_3): the wedge in cross-section ---
        self.next_band(5)
        b5t = Tex("Prove it with the evidence").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        wedge = Line(band_shift(5) + LEFT * 4.4 + DOWN * 2.2, band_shift(5) + RIGHT * 1.6 + DOWN * 0.2, color=BLUE)
        gnd = Line(band_shift(5) + LEFT * 4.6 + DOWN * 2.4, band_shift(5) + RIGHT * 4.6 + DOWN * 2.4, stroke_width=5)
        self.play(Create(gnd), Create(wedge))
        up1 = Arrow(band_shift(5) + RIGHT * 1.8 + DOWN * 2.2, band_shift(5) + RIGHT * 2.6 + UP * 0.6, buff=0, color=RED)
        self.play(Create(up1))
        b5a = Tex(r"Cold wedge under, warm air pitched up").scale(0.9).shift(band_shift(5) + LEFT * 1.4 + UP * 1.1)
        b5b = Tex(r"Cumulonimbus wall on the line").scale(0.9).shift(band_shift(5) + RIGHT * 2.6 + UP * 1.6)
        self.play(Write(b5a))
        self.wait(2)
        self.play(Write(b5b))
        self.wait(2)
        b5c = Tex(r"Ahead: warm NW, dew point close, cloud").scale(0.9).shift(band_shift(5) + DOWN * 0.6 + RIGHT * 1.4)
        b5d = Tex(r"Isobars kink where they cross the line").scale(0.9).shift(band_shift(5) + DOWN * 1.4 + RIGHT * 1.4)
        self.play(Write(b5c))
        self.wait(2)
        self.play(Write(b5d))
        self.play(Create(SurroundingRectangle(b5d, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): behind the front ---
        self.next_band(6)
        b6t = Tex("Behind the front: report it like a station").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        p1 = Tex(r"Temperature: 21 down to about 11").scale(1.0).shift(band_shift(6) + UP * 1.2)
        p2 = Tex(r"Wind: NW swings to SW").scale(1.0).shift(band_shift(6) + UP * 0.4)
        p3 = Tex(r"Pressure: falling turns to rising").scale(1.0).shift(band_shift(6) + DOWN * 0.4)
        p4 = Tex(r"Sky: showers, then clearing cold blue").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(p1))
        self.wait(2)
        self.play(Write(p2))
        self.wait(2)
        self.play(Write(p3))
        self.wait(2)
        self.play(Write(p4))
        self.wait(2)
        p5 = Tex(r"Colder, showery, clearing").scale(1.05).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(p5))
        self.play(Create(SurroundingRectangle(p5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the five-step checklist ---
        self.next_band(7)
        b7t = Tex("The synoptic checklist").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(1.5)
        s1 = Tex(r"1. Label cells: sinking-clear, rising-wet").scale(0.95).shift(band_shift(7) + UP * 1.2)
        s2 = Tex(r"2. Spacing $\rightarrow$ wind strength").scale(0.95).shift(band_shift(7) + UP * 0.5)
        s3 = Tex(r"3. Decode stations: temp, gap, oktas, wind").scale(0.95).shift(band_shift(7) + DOWN * 0.2)
        s4 = Tex(r"4. Fronts: symbol + evidence both sides").scale(0.95).shift(band_shift(7) + DOWN * 0.9)
        s5 = Tex(r"5. Observations, never impressions").scale(0.95).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(s1))
        self.wait(1.5)
        self.play(Write(s2))
        self.wait(1.5)
        self.play(Write(s3))
        self.wait(1.5)
        self.play(Write(s4))
        self.wait(1.5)
        self.play(Write(s5))
        self.play(Create(SurroundingRectangle(s5, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): pump and spray can ---
        self.next_band(8)
        b8t = Tex("Pump warm, spray cold").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex(r"Bicycle pump heats: compression warms").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8b = Tex(r"Deodorant can chills: expansion cools").scale(0.95).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8a))
        self.wait(2)
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex(r"H: air sinks, squeezed, warms — sky clears").scale(0.95).shift(band_shift(8) + DOWN * 0.5)
        b8d = Tex(r"L: air climbs, expands, chills — rain").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8c))
        self.wait(2)
        self.play(Write(b8d))
        self.wait(2)
        b8e = Tex(r"Wind: air rolling downhill from H to L").scale(0.95).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8e))
        self.play(Create(SurroundingRectangle(b8e, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the shirt-button report ---
        self.next_band(9)
        b9t = Tex("A weather report the size of a button").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        stn2 = Circle(radius=0.6, color=WHITE).shift(band_shift(9) + LEFT * 3.0 + DOWN * 0.2)
        self.play(Create(stn2))
        b9a = Tex(r"Circle = the sky in 8 milk-tart slices").scale(0.9).shift(band_shift(9) + RIGHT * 1.6 + UP * 1.0)
        b9b = Tex(r"21 over 18: three degrees from wet").scale(0.9).shift(band_shift(9) + RIGHT * 1.7 + UP * 0.2)
        b9c = Tex(r"Shaft flies in FROM the source: NW").scale(0.9).shift(band_shift(9) + RIGHT * 1.7 + DOWN * 0.6)
        b9d = Tex(r"Feathers: 10 + 5 = 15 knots").scale(0.9).shift(band_shift(9) + RIGHT * 1.3 + DOWN * 1.4)
        self.play(Write(b9a))
        self.wait(2)
        self.play(Write(b9b))
        self.wait(2)
        self.play(Write(b9c))
        self.wait(2)
        self.play(Write(b9d))
        self.wait(2)
        b9e = Tex(r"Order: sky, temp, gap, wind").scale(0.95).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9e))
        self.play(Create(SurroundingRectangle(b9e, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): three acts, three instruments ---
        self.next_band(10)
        b10t = Tex("Before, during, after").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        a1 = Tex(r"Before: warm, sticky, NW, cloud closing").scale(0.95).shift(band_shift(10) + UP * 1.2)
        a2 = Tex(r"During: dark, gusts, a downpour with attitude").scale(0.95).shift(band_shift(10) + UP * 0.4)
        a3 = Tex(r"After: cold SW, pressure climbing, clearing").scale(0.95).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(a1))
        self.wait(2)
        self.play(Write(a2))
        self.wait(2)
        self.play(Write(a3))
        self.wait(2)
        b10a = Tex(r"Three instruments: vane, thermometer,").scale(0.95).shift(band_shift(10) + DOWN * 1.4)
        b10b = Tex(r"barometer — all three must agree").scale(0.95).shift(band_shift(10) + DOWN * 2.1)
        self.play(Write(b10a))
        self.play(Write(b10b))
        self.play(Create(SurroundingRectangle(b10b, color=GREEN)))
        self.wait(4)
