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

# Band-layout whiteboard scene for "Heating of the atmosphere and heat
# transfer" (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Energy flows are Arrows, the budget split is labelled Tex, currents are
# curved Line chains. Add-only lifecycle; camera moves down band by band.
# Subtopic durations (s): 220/220/240/250/185/185/190 of 1490.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class HeatingOfTheAtmosphereSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the 30-20-50 split ---
        title = Tex("Heating of the Atmosphere").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        sun = Circle(radius=0.5, color=YELLOW).shift(UP * 1.6 + LEFT * 4.5)
        self.play(Create(sun))
        a30 = Arrow(UP * 1.2 + LEFT * 3.9, UP * 2.2 + LEFT * 1.9, buff=0, color=RED)
        t30 = Tex(r"30 reflected — the ALBEDO").scale(0.9).shift(UP * 2.0 + RIGHT * 0.9)
        self.play(Create(a30), Write(t30))
        self.wait(2)
        a20 = Arrow(UP * 1.2 + LEFT * 4.0, UP * 0.0 + LEFT * 1.8, buff=0, color=YELLOW)
        t20 = Tex(r"20 absorbed on the way in").scale(0.9).shift(UP * 0.1 + RIGHT * 1.3)
        self.play(Create(a20), Write(t20))
        self.wait(2)
        ground = Line(LEFT * 5.5 + DOWN * 2.2, RIGHT * 5.5 + DOWN * 2.2, stroke_width=6)
        a50 = Arrow(UP * 1.0 + LEFT * 4.3, DOWN * 2.0 + LEFT * 2.6, buff=0, color=GREEN)
        t50 = Tex(r"50 warm the surface").scale(0.9).shift(DOWN * 1.5 + RIGHT * 0.6)
        self.play(Create(ground))
        self.play(Create(a50), Write(t50))
        self.wait(2)
        t_out = Tex(r"Out again as LONG-WAVE — and caught").scale(0.9).shift(DOWN * 2.9)
        self.play(Write(t_out))
        self.play(Create(SurroundingRectangle(t_out, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): surplus, deficit, circulation ---
        self.next_band(1)
        b1t = Tex("The budget balances — but only globally").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        b1a = Tex(r"Within 40°N–40°S: permanent SURPLUS").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1b = Tex(r"Poleward of 40°: permanent DEFICIT").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1a))
        self.wait(2)
        self.play(Write(b1b))
        self.wait(2)
        eq = Line(band_shift(1) + LEFT * 4.0 + DOWN * 0.8, band_shift(1) + RIGHT * 4.0 + DOWN * 0.8)
        ar1 = Arrow(band_shift(1) + LEFT * 1.0 + DOWN * 0.8, band_shift(1) + LEFT * 1.0 + DOWN * 2.2, buff=0, color=RED)
        ar2 = Arrow(band_shift(1) + RIGHT * 1.0 + DOWN * 0.8, band_shift(1) + RIGHT * 1.0 + DOWN * 2.2, buff=0, color=RED)
        b1c = Tex(r"Winds + currents carry the surplus poleward").scale(0.95).shift(band_shift(1) + DOWN * 2.8)
        self.play(Create(eq))
        self.play(Create(ar1), Create(ar2))
        self.play(Write(b1c))
        self.play(Create(SurroundingRectangle(b1c, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the four processes ---
        self.next_band(2)
        b2t = Tex("Four ways heat moves").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        p1 = Tex(r"RADIATION: waves, no medium needed").scale(1.0).shift(band_shift(2) + UP * 1.2)
        p2 = Tex(r"CONDUCTION: contact — lowest metres only").scale(1.0).shift(band_shift(2) + UP * 0.4)
        p3 = Tex(r"CONVECTION: warm air rises — vertical").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        p4 = Tex(r"ADVECTION: wind carries heat — horizontal").scale(1.0).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(p1))
        self.wait(2)
        self.play(Write(p2))
        self.wait(2)
        self.play(Write(p3))
        self.wait(2)
        self.play(Write(p4))
        self.wait(2)
        p5 = Tex(r"Sea breeze at Gqeberha; berg wind in June").scale(0.9).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(p5))
        self.wait(3)

        # --- Band 3 (subtopic_2): heated from below ---
        self.next_band(3)
        b3t = Tex("The atmosphere is heated FROM BELOW").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        g2 = Line(band_shift(3) + LEFT * 4.5 + DOWN * 2.4, band_shift(3) + RIGHT * 4.5 + DOWN * 2.4, stroke_width=6)
        self.play(Create(g2))
        u1 = Arrow(band_shift(3) + LEFT * 2.0 + DOWN * 2.2, band_shift(3) + LEFT * 2.0 + UP * 0.6, buff=0, color=RED)
        u2 = Arrow(band_shift(3) + RIGHT * 0.2 + DOWN * 2.2, band_shift(3) + RIGHT * 0.2 + UP * 0.6, buff=0, color=RED)
        b3a = Tex(r"Ground absorbs sun, then heats the air").scale(1.0).shift(band_shift(3) + UP * 1.2)
        self.play(Create(u1), Create(u2))
        self.play(Write(b3a))
        self.wait(2)
        b3b = Tex(r"So climbing = leaving the heater:").scale(1.0).shift(band_shift(3) + DOWN * 0.4 + RIGHT * 1.8)
        b3c = Tex(r"temperature falls with height").scale(1.0).shift(band_shift(3) + DOWN * 1.1 + RIGHT * 1.8)
        self.play(Write(b3b))
        self.play(Write(b3c))
        self.play(Create(SurroundingRectangle(b3c, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): greenhouse mechanism in order ---
        self.next_band(4)
        b4t = Tex("The greenhouse mechanism, in order").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        s1 = Tex(r"1. Short-wave passes through").scale(0.95).shift(band_shift(4) + UP * 1.2)
        s2 = Tex(r"2. Surface absorbs and warms").scale(0.95).shift(band_shift(4) + UP * 0.5)
        s3 = Tex(r"3. Surface re-emits LONG-WAVE").scale(0.95).shift(band_shift(4) + DOWN * 0.2)
        s4 = Tex(r"4. Greenhouse gases absorb it").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        s5 = Tex(r"5. COUNTER-RADIATION returns part down").scale(0.95).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(s1))
        self.wait(1.5)
        self.play(Write(s2))
        self.wait(1.5)
        self.play(Write(s3))
        self.wait(1.5)
        self.play(Write(s4))
        self.wait(1.5)
        self.play(Write(s5))
        self.wait(2)
        b4a = Tex(r"Natural effect: $15^\circ$C, not $-18^\circ$C").scale(1.0).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4a))
        self.play(Create(SurroundingRectangle(b4a, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): enhanced warming and Africa ---
        self.next_band(5)
        b5t = Tex("Enhanced warming: the human surcharge").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        b5a = Tex(r"Sources: fossil fuels, deforestation,").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5a2 = Tex(r"cattle + paddies, landfills, cement").scale(0.95).shift(band_shift(5) + UP * 0.6)
        self.play(Write(b5a))
        self.play(Write(b5a2))
        self.wait(2)
        b5b = Tex(r"Africa: faster warming, erratic rain,").scale(0.95).shift(band_shift(5) + DOWN * 0.3)
        b5b2 = Tex(r"maize losses, rising seas, malaria uphill").scale(0.95).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5b))
        self.play(Write(b5b2))
        self.wait(2)
        b5c = Tex(r"Natural = keeps us alive").scale(1.0).shift(band_shift(5) + DOWN * 1.8)
        b5d = Tex(r"Enhanced = the intensification we caused").scale(1.0).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5c))
        self.play(Write(b5d))
        self.play(Create(SurroundingRectangle(b5d, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): latitude and altitude ---
        self.next_band(6)
        b6t = Tex("Factor 1: latitude. Factor 2: altitude").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        beam1 = Arrow(band_shift(6) + LEFT * 3.4 + UP * 1.4, band_shift(6) + LEFT * 3.4 + DOWN * 0.4, buff=0, color=YELLOW)
        lab1 = Tex(r"overhead: concentrated").scale(0.85).shift(band_shift(6) + LEFT * 3.2 + DOWN * 1.0)
        beam2 = Arrow(band_shift(6) + RIGHT * 1.4 + UP * 1.4, band_shift(6) + RIGHT * 3.6 + DOWN * 0.4, buff=0, color=YELLOW)
        lab2 = Tex(r"slanted: spread + longer path").scale(0.85).shift(band_shift(6) + RIGHT * 2.9 + DOWN * 1.0)
        self.play(Create(beam1), Write(lab1))
        self.wait(2)
        self.play(Create(beam2), Write(lab2))
        self.wait(2)
        b6a = Tex(r"Altitude: $-6{,}5^\circ$C per 1 000 m").scale(1.0).shift(band_shift(6) + DOWN * 1.9)
        b6b = Tex(r"Bloemfontein 1 400 m $\approx$ 9$^\circ$C cooler than Durban").scale(0.95).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6a))
        self.wait(1.5)
        self.play(Write(b6b))
        self.play(Create(SurroundingRectangle(b6b, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): sea, currents, cloud, aspect ---
        self.next_band(7)
        b7t = Tex("Factors 3, 4, 5: sea, currents, sky").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(1.5)
        b7a = Tex(r"Sea cushions: small annual range at coast").scale(0.95).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7a))
        self.wait(2)
        cur1 = Arrow(band_shift(7) + RIGHT * 3.4 + UP * 0.6, band_shift(7) + RIGHT * 3.4 + DOWN * 1.4, buff=0, color=RED)
        cl1 = Tex(r"warm Agulhas, east").scale(0.8).shift(band_shift(7) + RIGHT * 3.3 + DOWN * 1.9)
        cur2 = Arrow(band_shift(7) + LEFT * 3.6 + DOWN * 1.4, band_shift(7) + LEFT * 3.6 + UP * 0.6, buff=0, color=BLUE)
        cl2 = Tex(r"cold Benguela, west").scale(0.8).shift(band_shift(7) + LEFT * 3.4 + DOWN * 1.9)
        self.play(Create(cur1), Write(cl1))
        self.play(Create(cur2), Write(cl2))
        self.wait(2)
        b7b = Tex(r"Cloud: cooler days, warmer nights").scale(0.95).shift(band_shift(7) + DOWN * 0.2)
        b7c = Tex(r"Aspect: north-facing slopes get the sun").scale(0.95).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7b))
        self.wait(1.5)
        self.play(Write(b7c))
        self.play(Create(SurroundingRectangle(b7c, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): one hundred buckets ---
        self.next_band(8)
        b8t = Tex("One hundred buckets of sunlight").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex(r"30 tipped back at the gate = albedo").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8b = Tex(r"20 leak on the way down").scale(1.0).shift(band_shift(8) + UP * 0.4)
        b8c = Tex(r"50 delivered to the ground").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8a))
        self.wait(2)
        self.play(Write(b8b))
        self.wait(2)
        self.play(Write(b8c))
        self.wait(2)
        b8d = Tex(r"Poured back in a NEW form: long-wave").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        b8e = Tex(r"Gales = trucks balancing the accounts").scale(1.0).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8d))
        self.play(Create(SurroundingRectangle(b8d, color=GREEN)))
        self.wait(2)
        self.play(Write(b8e))
        self.wait(3)

        # --- Band 9 (subtopic_6): hot sand, cool breeze ---
        self.next_band(9)
        b9t = Tex("Hot sand, cool breeze").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        sand = Line(band_shift(9) + LEFT * 4.5 + DOWN * 2.3, band_shift(9) + RIGHT * 4.5 + DOWN * 2.3, stroke_width=6, color=YELLOW)
        self.play(Create(sand))
        b9a = Tex(r"Sun on your face = radiation").scale(0.95).shift(band_shift(9) + UP * 1.2)
        b9b = Tex(r"Burnt soles = conduction").scale(0.95).shift(band_shift(9) + UP * 0.4)
        b9c = Tex(r"The shimmer = convection").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        b9d = Tex(r"Three o'clock sea breeze = advection").scale(0.95).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(b9a))
        self.wait(2)
        self.play(Write(b9b))
        self.wait(2)
        self.play(Write(b9c))
        self.wait(2)
        self.play(Write(b9d))
        self.wait(2)
        b9e = Tex(r"Scalding sand, mild air: heated from BELOW").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9e))
        self.play(Create(SurroundingRectangle(b9e, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): five dials, two towns ---
        self.next_band(10)
        b10t = Tex("Musina swelters, Molteno freezes").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        d1 = Tex(r"1. Angle: hosepipe straight vs tilted").scale(0.95).shift(band_shift(10) + UP * 1.2)
        d2 = Tex(r"2. Height: 6,5$^\circ$C lost per 1 000 m").scale(0.95).shift(band_shift(10) + UP * 0.4)
        d3 = Tex(r"3. Sea: coast cushioned, interior swings").scale(0.95).shift(band_shift(10) + DOWN * 0.4)
        d4 = Tex(r"4. Currents: Agulhas warm, Benguela cold").scale(0.95).shift(band_shift(10) + DOWN * 1.2)
        d5 = Tex(r"5. Sky + slope: cloud shields, north faces sun").scale(0.95).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(d1))
        self.wait(1.5)
        self.play(Write(d2))
        self.wait(1.5)
        self.play(Write(d3))
        self.wait(1.5)
        self.play(Write(d4))
        self.wait(1.5)
        self.play(Write(d5))
        self.wait(2)
        b10e = Tex(r"Five dials set every town's thermometer").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10e))
        self.play(Create(SurroundingRectangle(b10e, color=GREEN)))
        self.wait(4)
