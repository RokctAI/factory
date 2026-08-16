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

# Band-layout whiteboard scene for "Station models and cold fronts" (Part 1
# Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7). The station model,
# isobar cells, cold-front teeth and the frontal wedge cross-section are all
# hand-built from Line/Arrow/Dot/Circle/Tex, element by element with the
# script. Subtopic durations (s): 215/255/210/270/175/195/180 of 1500.

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
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the synoptic chart, H and L ---
        title = Tex("Synoptic Charts: Stations and Fronts").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex(r"One snapshot, everywhere at once").scale(1.0).shift(UP * 1.4)
        self.play(Write(d1))
        self.wait(1.5)
        h1 = Circle(radius=1.5, color=WHITE).shift(DOWN * 1.2 + LEFT * 3.2)
        h2 = Circle(radius=0.9, color=WHITE).shift(DOWN * 1.2 + LEFT * 3.2)
        hl = Tex("H").scale(1.2).shift(DOWN * 1.2 + LEFT * 3.2)
        self.play(Create(h1), Create(h2))
        self.play(Write(hl))
        ht = Tex(r"air sinks: clear, settled").scale(0.85).shift(DOWN * 3.0 + LEFT * 3.2)
        self.play(Write(ht))
        self.wait(2)
        l1 = Circle(radius=1.5, color=WHITE).shift(DOWN * 1.2 + RIGHT * 3.2)
        l2 = Circle(radius=0.9, color=WHITE).shift(DOWN * 1.2 + RIGHT * 3.2)
        ll = Tex("L").scale(1.2).shift(DOWN * 1.2 + RIGHT * 3.2)
        self.play(Create(l1), Create(l2))
        self.play(Write(ll))
        lt = Tex(r"air rises: cloud, rain").scale(0.85).shift(DOWN * 3.0 + RIGHT * 3.2)
        self.play(Write(lt))
        self.wait(2)
        iso = Tex(r"Isobars in hPa — pressure contours").scale(0.95).shift(UP * 0.6)
        self.play(Write(iso))
        self.wait(3)

        # --- Band 1 (subtopic_1): spacing = wind ---
        self.next_band(1)
        b1t = Tex("Isobar spacing is wind strength").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        b1a = Tex(r"Packed isobars: steep gradient,").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1a2 = Tex(r"strong winds").scale(1.05).shift(band_shift(1) + UP * 0.5)
        b1b = Tex(r"Wide spacing: gentle winds").scale(1.05).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1a))
        self.play(Write(b1a2))
        self.wait(2)
        self.play(Write(b1b))
        self.wait(2)
        b1c = Tex(r"Sinking = clear; rising = wet").scale(1.1).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1c))
        self.play(Create(SurroundingRectangle(b1c, color=GREEN)))
        b1d = Tex(r"Station models: circles with symbols").scale(0.95).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1d))
        self.wait(3)

        # --- Band 2 (subtopic_2): building the station model ---
        self.next_band(2)
        b2t = Tex("Decoding the station model").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        st_c = Circle(radius=0.6, color=WHITE).shift(band_shift(2) + LEFT * 2.6 + DOWN * 0.6)
        self.play(Create(st_c))
        c_lab = Tex(r"circle = cloud cover: 6/8 oktas").scale(0.9).shift(band_shift(2) + RIGHT * 2.2 + UP * 1.2)
        self.play(Write(c_lab))
        self.wait(2)
        t_val = Tex("18").scale(0.9).shift(band_shift(2) + LEFT * 3.8 + UP * 0.3)
        t_lab = Tex(r"upper left: temp $18^\circ$C").scale(0.9).shift(band_shift(2) + RIGHT * 2.0 + UP * 0.4)
        self.play(Write(t_val), Write(t_lab))
        self.wait(2)
        d_val = Tex("16").scale(0.9).shift(band_shift(2) + LEFT * 3.8 + DOWN * 1.4)
        d_lab = Tex(r"below: dew point $16^\circ$C").scale(0.9).shift(band_shift(2) + RIGHT * 2.0 + DOWN * 0.4)
        self.play(Write(d_val), Write(d_lab))
        self.wait(2)
        shaft = Line(band_shift(2) + LEFT * 4.4 + UP * 1.2, band_shift(2) + LEFT * 3.0 + DOWN * 0.2)
        f1 = Line(band_shift(2) + LEFT * 4.4 + UP * 1.2, band_shift(2) + LEFT * 4.8 + UP * 1.5)
        f2 = Line(band_shift(2) + LEFT * 4.1 + UP * 0.9, band_shift(2) + LEFT * 4.5 + UP * 1.2)
        self.play(Create(shaft))
        self.play(Create(f1), Create(f2))
        w_lab = Tex(r"shaft from NW; 2 feathers = 20 kt").scale(0.9).shift(band_shift(2) + RIGHT * 2.2 + DOWN * 1.2)
        self.play(Write(w_lab))
        self.wait(2)
        rule = Tex(r"Wind is named for its ORIGIN").scale(0.95).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(rule))
        self.play(Create(SurroundingRectangle(rule, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): reading the station ---
        self.next_band(3)
        b3t = Tex("Read the station in one breath").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        g1 = MathTex(r"18^\circ - 16^\circ = 2^\circ \text{ gap}").scale(1.1).shift(band_shift(3) + UP * 1.1)
        self.play(Write(g1))
        self.wait(2)
        g2 = Tex(r"Narrow gap = humid, rain close").scale(1.05).shift(band_shift(3) + UP * 0.2)
        g3 = Tex(r"Wide gap ($25^\circ$ vs $5^\circ$) = dry air").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(g2))
        self.play(Create(SurroundingRectangle(g2, color=GREEN)))
        self.wait(2)
        self.play(Write(g3))
        self.wait(2)
        g4 = Tex(r"Mild, humid, 6/8 cloud, fresh NW").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        g4b = Tex(r"at 20 kt — weather is coming").scale(1.0).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(g4))
        self.play(Write(g4b))
        self.wait(3)

        # --- Band 4 (subtopic_3): the cold front symbol ---
        self.next_band(4)
        b4t = Tex("Finding the cold front").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        fr = Line(band_shift(4) + LEFT * 4.6 + DOWN * 0.4, band_shift(4) + RIGHT * 1.6 + DOWN * 0.4, stroke_width=6, color=BLUE)
        self.play(Create(fr))
        for x in (-3.6, -2.0, -0.4):
            ta = Line(band_shift(4) + RIGHT * x + DOWN * 0.4, band_shift(4) + RIGHT * (x + 0.35) + UP * 0.25)
            tb = Line(band_shift(4) + RIGHT * (x + 0.35) + UP * 0.25, band_shift(4) + RIGHT * (x + 0.7) + DOWN * 0.4)
            self.play(Create(ta), Create(tb), run_time=0.6)
        te_l = Tex(r"teeth point where it is GOING (NE)").scale(0.95).shift(band_shift(4) + UP * 1.2)
        self.play(Write(te_l))
        self.wait(2)
        mv = Arrow(band_shift(4) + RIGHT * 2.0 + DOWN * 0.4, band_shift(4) + RIGHT * 3.6 + UP * 0.4, buff=0, color=YELLOW)
        self.play(Create(mv))
        self.wait(1.5)
        b4a = Tex(r"Ahead: warm moist NW flow, cloud").scale(0.95).shift(band_shift(4) + DOWN * 1.4)
        b4b = Tex(r"At the line: cumulonimbus; isobars kink").scale(0.95).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(b4a))
        self.wait(2)
        self.play(Write(b4b))
        self.wait(3)

        # --- Band 5 (subtopic_3): the wedge in cross-section ---
        self.next_band(5)
        b5t = Tex("The cold wedge lifts the warm air").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        gnd5 = Line(band_shift(5) + LEFT * 5.0 + DOWN * 2.4, band_shift(5) + RIGHT * 5.0 + DOWN * 2.4, stroke_width=6)
        self.play(Create(gnd5))
        wedge = Line(band_shift(5) + LEFT * 4.6 + UP * 0.6, band_shift(5) + RIGHT * 1.4 + DOWN * 2.4, color=BLUE)
        w_lab5 = Tex("cold dense air").scale(0.9).shift(band_shift(5) + LEFT * 3.0 + DOWN * 1.5)
        self.play(Create(wedge), Write(w_lab5))
        self.wait(2)
        lift = Arrow(band_shift(5) + RIGHT * 1.8 + DOWN * 2.2, band_shift(5) + RIGHT * 2.6 + UP * 0.8, buff=0, color=RED)
        lift_l = Tex("warm moist air forced up").scale(0.9).shift(band_shift(5) + RIGHT * 3.0 + DOWN * 1.5)
        self.play(Create(lift), Write(lift_l))
        self.wait(2)
        cb = Rectangle(width=1.4, height=1.3).shift(band_shift(5) + RIGHT * 2.4 + UP * 1.4)
        cb_l = Tex("cumulonimbus line").scale(0.85).shift(band_shift(5) + RIGHT * 2.4 + UP * 2.4 + LEFT * 2.6)
        self.play(Create(cb), Write(cb_l))
        self.wait(3)

        # --- Band 6 (subtopic_4): behind the front ---
        self.next_band(6)
        b6t = Tex("Behind the front — four observations").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        o1 = Tex(r"Temp: $18^\circ$ falls to 8–$10^\circ$").scale(1.0).shift(band_shift(6) + UP * 1.2)
        o2 = Tex(r"Wind: NW swings to SW").scale(1.0).shift(band_shift(6) + UP * 0.4)
        o3 = Tex(r"Pressure: rising — next high builds").scale(1.0).shift(band_shift(6) + DOWN * 0.4)
        o4 = Tex(r"Cloud: showers, then clearing skies").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(o1))
        self.wait(2)
        self.play(Write(o2))
        self.wait(2)
        self.play(Write(o3))
        self.wait(2)
        self.play(Write(o4))
        self.wait(2)
        o5 = Tex(r"Cold, showery, clearing").scale(1.1).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(o5))
        self.play(Create(SurroundingRectangle(o5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the exam checklist ---
        self.next_band(7)
        b7t = Tex("Synoptic method — five steps").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(1.5)
        s1 = Tex(r"1. Label highs and lows").scale(0.95).shift(band_shift(7) + UP * 1.2)
        s2 = Tex(r"2. Isobar spacing = wind strength").scale(0.95).shift(band_shift(7) + UP * 0.5)
        s3 = Tex(r"3. Decode every station model").scale(0.95).shift(band_shift(7) + DOWN * 0.2)
        s4 = Tex(r"4. Fronts: symbol + evidence both sides").scale(0.95).shift(band_shift(7) + DOWN * 0.9)
        s5 = Tex(r"5. Answer in observations, not vibes").scale(0.95).shift(band_shift(7) + DOWN * 1.6)
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
        # --- Band 8 (subtopic_5): sink-clear, rise-rain ---
        self.next_band(8)
        b8t = Tex("Which way is the air going?").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        k1 = Tex(r"Pressure = how hard the air leans").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(k1))
        self.wait(2)
        k2 = Tex(r"H: air sinks, warms — clouds vanish").scale(1.0).shift(band_shift(8) + UP * 0.4)
        k3 = Tex(r"L: air rises, cools — water lets go").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(k2))
        self.wait(2)
        self.play(Write(k3))
        self.wait(2)
        k4 = Tex(r"Kettle spout: invisible, then cloud").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(k4))
        self.wait(2)
        k5 = Tex(r"Sink, clear; rise, rain").scale(1.1).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(k5))
        self.play(Create(SurroundingRectangle(k5, color=GREEN)))
        k6 = Tex(r"Squeezed isobars: steep hill, fast wind").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(k6))
        self.wait(3)

        # --- Band 9 (subtopic_6): the little circle ---
        self.next_band(9)
        b9t = Tex("A weather report in a thumbnail").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        pz = Circle(radius=0.8, color=WHITE).shift(band_shift(9) + LEFT * 3.4 + UP * 0.6)
        pz1 = Line(band_shift(9) + LEFT * 3.4 + UP * 1.4, band_shift(9) + LEFT * 3.4 + DOWN * 0.2)
        pz2 = Line(band_shift(9) + LEFT * 4.2 + UP * 0.6, band_shift(9) + LEFT * 2.6 + UP * 0.6)
        self.play(Create(pz))
        self.play(Create(pz1), Create(pz2))
        p_lab = Tex(r"the sky cut into 8 pizza slices —").scale(0.95).shift(band_shift(9) + RIGHT * 1.9 + UP * 1.0)
        p_lab2 = Tex(r"6 shaded = properly grey day").scale(0.95).shift(band_shift(9) + RIGHT * 1.8 + UP * 0.3)
        self.play(Write(p_lab))
        self.play(Write(p_lab2))
        self.wait(2)
        p2 = Tex(r"Dew point = a wetness meter:").scale(0.95).shift(band_shift(9) + DOWN * 0.7)
        p2b = Tex(r"18 and 16 — two degrees from sweating").scale(0.95).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(p2))
        self.play(Write(p2b))
        self.wait(2)
        p3 = Tex(r"Arrow flies in FROM the north-west;").scale(0.95).shift(band_shift(9) + DOWN * 2.2)
        p3b = Tex(r"two feathers = 20 kt, washing moving").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(p3))
        self.play(Write(p3b))
        self.wait(3)

        # --- Band 10 (subtopic_7): before, during, after ---
        self.next_band(10)
        b10t = Tex("Before, during and after the front").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        a1 = Tex(r"Before: warm, sticky, NW breeze,").scale(0.95).shift(band_shift(10) + UP * 1.2)
        a1b = Tex(r"cloud thickening").scale(0.95).shift(band_shift(10) + UP * 0.6)
        a2 = Tex(r"During: dark sky, gusts, hard rain").scale(0.95).shift(band_shift(10) + DOWN * 0.2)
        a3 = Tex(r"After: cold SW wind, pressure climbs,").scale(0.95).shift(band_shift(10) + DOWN * 1.0)
        a3b = Tex(r"showers break up, sky clears").scale(0.95).shift(band_shift(10) + DOWN * 1.6)
        self.play(Write(a1))
        self.play(Write(a1b))
        self.wait(2)
        self.play(Write(a2))
        self.wait(2)
        self.play(Write(a3))
        self.play(Write(a3b))
        self.wait(2)
        a4 = Tex(r"Three witnesses: wind, temp, pressure").scale(1.0).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(a4))
        self.play(Create(SurroundingRectangle(a4, color=GREEN)))
        self.wait(4)
