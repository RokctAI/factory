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

# Band-layout whiteboard scene for "Heating of the atmosphere and heat
# transfer" (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# The heat budget, convection loop and coast/current sketches are hand-built
# from Line/Arrow/Dot/Circle/Tex, element by element with the script.
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
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): insolation and the 30-20-50 split ---
        title = Tex("Heating of the Atmosphere").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        sun = Circle(radius=0.5, color=YELLOW).shift(UP * 1.6 + LEFT * 4.5)
        sun_l = Tex("Sun: 100 units in").scale(0.9).shift(UP * 1.6 + LEFT * 2.2)
        self.play(Create(sun), Write(sun_l))
        self.wait(1.5)
        ground = Line(LEFT * 5.5, RIGHT * 5.5, stroke_width=6).shift(DOWN * 2.6)
        self.play(Create(ground))
        a30 = Arrow(UP * 1.0 + LEFT * 3.0, UP * 2.6 + LEFT * 1.6, buff=0, color=BLUE)
        l30 = Tex(r"30 reflected (albedo)").scale(0.9).shift(UP * 2.4 + RIGHT * 1.4)
        self.play(Create(a30), Write(l30))
        self.wait(2)
        a20 = Dot(UP * 0.2 + LEFT * 2.0, color=YELLOW)
        l20 = Tex(r"20 absorbed in the air").scale(0.9).shift(UP * 0.3 + RIGHT * 1.4)
        self.play(FadeIn(a20), Write(l20))
        self.wait(2)
        a50 = Arrow(UP * 0.9 + LEFT * 4.2, DOWN * 2.5 + LEFT * 3.4, buff=0, color=YELLOW)
        l50 = Tex(r"50 reach and warm the surface").scale(0.9).shift(DOWN * 1.4 + RIGHT * 1.8)
        self.play(Create(a50), Write(l50))
        self.wait(2)
        lw = Tex(r"Out: LONG-wave terrestrial radiation").scale(0.9).shift(DOWN * 3.1 + RIGHT * 1.2)
        self.play(Write(lw))
        self.wait(3)

        # --- Band 1 (subtopic_1): the budget and the transfer ---
        self.next_band(1)
        b1t = Tex("The heat budget").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        b1a = Tex(r"Short-wave in passes through;").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1a2 = Tex(r"long-wave out gets absorbed").scale(1.0).shift(band_shift(1) + UP * 0.6)
        self.play(Write(b1a))
        self.play(Write(b1a2))
        self.wait(2)
        b1b = Tex(r"Whole planet: in = out each year").scale(1.0).shift(band_shift(1) + DOWN * 0.3)
        self.play(Write(b1b))
        self.wait(2)
        b1c = Tex(r"40N–40S: surplus; poleward: deficit").scale(1.0).shift(band_shift(1) + DOWN * 1.1)
        b1d = Tex(r"Winds + currents settle the debt").scale(1.05).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1c))
        self.wait(2)
        self.play(Write(b1d))
        self.play(Create(SurroundingRectangle(b1d, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the four processes ---
        self.next_band(2)
        b2t = Tex("Four ways heat moves").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        p1 = Tex(r"Radiation: waves, no medium needed").scale(0.95).shift(band_shift(2) + UP * 1.2)
        p2 = Tex(r"Conduction: contact — lowest metres").scale(0.95).shift(band_shift(2) + UP * 0.5)
        p3 = Tex(r"Convection: warm air rises (vertical)").scale(0.95).shift(band_shift(2) + DOWN * 0.2)
        p4 = Tex(r"Advection: wind moves heat sideways").scale(0.95).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(p1))
        self.wait(2)
        self.play(Write(p2))
        self.wait(2)
        self.play(Write(p3))
        self.wait(2)
        self.play(Write(p4))
        self.wait(2)
        # convection loop from straight arrows
        c_up = Arrow(band_shift(2) + LEFT * 3.6 + DOWN * 2.9, band_shift(2) + LEFT * 3.6 + DOWN * 1.7, buff=0, color=RED)
        c_top = Arrow(band_shift(2) + LEFT * 3.6 + DOWN * 1.7, band_shift(2) + LEFT * 1.8 + DOWN * 1.7, buff=0, color=RED)
        c_dn = Arrow(band_shift(2) + LEFT * 1.8 + DOWN * 1.7, band_shift(2) + LEFT * 1.8 + DOWN * 2.9, buff=0, color=BLUE)
        c_bot = Arrow(band_shift(2) + LEFT * 1.8 + DOWN * 2.9, band_shift(2) + LEFT * 3.6 + DOWN * 2.9, buff=0, color=BLUE)
        c_lab = Tex("convection current").scale(0.85).shift(band_shift(2) + RIGHT * 1.6 + DOWN * 2.3)
        self.play(Create(c_up))
        self.play(Create(c_top))
        self.play(Create(c_dn))
        self.play(Create(c_bot))
        self.play(Write(c_lab))
        self.wait(3)

        # --- Band 3 (subtopic_2): heated from below ---
        self.next_band(3)
        b3t = Tex("The atmosphere is heated from BELOW").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        b3w = Tex(r"The sun heats the air directly").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3w))
        self.play(Create(strike(b3w)))
        self.wait(2)
        b3a = Tex(r"Insolation passes through the air,").scale(1.0).shift(band_shift(3) + UP * 0.2)
        b3a2 = Tex(r"warms the ground first").scale(1.0).shift(band_shift(3) + DOWN * 0.4)
        b3b = Tex(r"Ground heats air: conduction,").scale(1.0).shift(band_shift(3) + DOWN * 1.2)
        b3b2 = Tex(r"convection, long-wave radiation").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3a))
        self.play(Write(b3a2))
        self.wait(2)
        self.play(Write(b3b))
        self.play(Write(b3b2))
        self.wait(2)
        b3c = Tex(r"So temperature falls with height").scale(1.05).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3c))
        self.play(Create(SurroundingRectangle(b3c, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): greenhouse mechanism in order ---
        self.next_band(4)
        b4t = Tex("Greenhouse effect — the strict order").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        g1 = Tex(r"1. Short-wave passes through the air").scale(0.95).shift(band_shift(4) + UP * 1.2)
        g2 = Tex(r"2. Surface absorbs it and warms").scale(0.95).shift(band_shift(4) + UP * 0.5)
        g3 = Tex(r"3. Surface re-radiates LONG-wave").scale(0.95).shift(band_shift(4) + DOWN * 0.2)
        g4 = Tex(r"4. Greenhouse gases absorb it").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        g5 = Tex(r"5. Re-radiate down: counter-radiation").scale(0.95).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(g1))
        self.wait(1.5)
        self.play(Write(g2))
        self.wait(1.5)
        self.play(Write(g3))
        self.wait(1.5)
        self.play(Write(g4))
        self.wait(1.5)
        self.play(Write(g5))
        self.wait(2)
        g6 = Tex(r"Natural: $15^\circ$C, not $-18^\circ$C").scale(1.0).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(g6))
        self.play(Create(SurroundingRectangle(g6, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): enhanced warming and Africa ---
        self.next_band(5)
        b5t = Tex("Enhanced greenhouse effect").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        e1 = Tex(r"Sources: fossil fuels, deforestation,").scale(0.95).shift(band_shift(5) + UP * 1.2)
        e1b = Tex(r"agriculture, landfills, cement").scale(0.95).shift(band_shift(5) + UP * 0.6)
        self.play(Write(e1))
        self.play(Write(e1b))
        self.wait(2)
        e2 = Tex(r"SA: coal-heavy electricity").scale(0.95).shift(band_shift(5) + DOWN * 0.2)
        self.play(Write(e2))
        self.wait(2)
        e3 = Tex(r"Africa: faster warming, failing rains,").scale(0.95).shift(band_shift(5) + DOWN * 1.0)
        e3b = Tex(r"maize yields down, malaria shifting").scale(0.95).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(e3))
        self.play(Write(e3b))
        self.wait(2)
        e4 = Tex(r"Natural = needed; enhanced = caused").scale(1.0).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(e4))
        self.play(Create(SurroundingRectangle(e4, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): latitude and altitude ---
        self.next_band(6)
        b6t = Tex("Temperature factors 1–2").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        f1 = Tex(r"Latitude: vertical rays concentrate,").scale(0.95).shift(band_shift(6) + UP * 1.2)
        f1b = Tex(r"oblique rays spread + longer path").scale(0.95).shift(band_shift(6) + UP * 0.6)
        self.play(Write(f1))
        self.play(Write(f1b))
        self.wait(2)
        f2 = Tex(r"Altitude: about $6{,}5^\circ$C per 1 000 m").scale(0.95).shift(band_shift(6) + DOWN * 0.3)
        self.play(Write(f2))
        self.wait(2)
        calc1 = MathTex(r"1\,750 \text{ m} \times \frac{6{,}5}{1\,000}").scale(1.05).shift(band_shift(6) + DOWN * 1.3)
        calc2 = MathTex(r"\approx 11^\circ \text{C cooler}").scale(1.05).shift(band_shift(6) + DOWN * 2.3)
        self.play(Write(calc1))
        self.wait(2)
        self.play(Write(calc2))
        self.play(Create(SurroundingRectangle(calc2, color=GREEN)))
        b6n = Tex(r"Johannesburg vs Durban").scale(0.9).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6n))
        self.wait(3)

        # --- Band 7 (subtopic_4): sea, currents, cloud, aspect ---
        self.next_band(7)
        b7t = Tex("Temperature factors 3–5").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(1.5)
        h1 = Tex(r"Sea moderates: small annual range").scale(0.95).shift(band_shift(7) + UP * 1.3)
        h1b = Tex(r"Interior swings: Upington, Kimberley").scale(0.95).shift(band_shift(7) + UP * 0.7)
        self.play(Write(h1))
        self.play(Write(h1b))
        self.wait(2)
        # two coasts, two currents: simple map sketch
        coast_w = Line(band_shift(7) + LEFT * 3.6 + DOWN * 2.6, band_shift(7) + LEFT * 3.2 + UP * 0.1)
        coast_e = Line(band_shift(7) + LEFT * 0.6 + DOWN * 2.6, band_shift(7) + LEFT * 1.2 + UP * 0.1)
        base = Line(band_shift(7) + LEFT * 3.6 + DOWN * 2.6, band_shift(7) + LEFT * 0.6 + DOWN * 2.6)
        self.play(Create(coast_w), Create(coast_e), Create(base))
        ag = Arrow(band_shift(7) + LEFT * 0.3 + UP * 0.1, band_shift(7) + RIGHT * 0.3 + DOWN * 2.2, buff=0, color=RED)
        ag_l = Tex(r"warm Agulhas: Durban humid").scale(0.85).shift(band_shift(7) + RIGHT * 3.0 + DOWN * 0.6)
        self.play(Create(ag), Write(ag_l))
        self.wait(2)
        bg = Arrow(band_shift(7) + LEFT * 4.4 + DOWN * 2.2, band_shift(7) + LEFT * 3.9 + UP * 0.1, buff=0, color=BLUE)
        bg_l = Tex(r"cold Benguela: fog, Namib").scale(0.85).shift(band_shift(7) + RIGHT * 3.1 + DOWN * 1.4)
        self.play(Create(bg), Write(bg_l))
        self.wait(2)
        h3 = Tex(r"Cloud shrinks daily range; north-facing").scale(0.9).shift(band_shift(7) + DOWN * 3.0 + LEFT * 0.6)
        h3b = Tex(r"slopes warmer").scale(0.9).shift(band_shift(7) + DOWN * 3.0 + RIGHT * 4.0)
        self.play(Write(h3), Write(h3b))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): one hundred rand of sunshine ---
        self.next_band(8)
        b8t = Tex("One hundred rand of sunshine").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        m1 = Tex(r"R30 bounces off clouds and bright").scale(1.0).shift(band_shift(8) + UP * 1.2)
        m1b = Tex(r"ground — the albedo").scale(1.0).shift(band_shift(8) + UP * 0.6)
        m2 = Tex(r"R20 taken as commission in the air").scale(1.0).shift(band_shift(8) + DOWN * 0.2)
        m3 = Tex(r"R50 lands on the ground — it warms").scale(1.0).shift(band_shift(8) + DOWN * 1.0)
        self.play(Write(m1))
        self.play(Write(m1b))
        self.wait(2)
        self.play(Write(m2))
        self.wait(2)
        self.play(Write(m3))
        self.play(Create(SurroundingRectangle(m3, color=GREEN)))
        self.wait(2)
        m4 = Tex(r"Spent back in a new currency:").scale(1.0).shift(band_shift(8) + DOWN * 1.9)
        m4b = Tex(r"long-wave — and the air grabs it").scale(1.0).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(m4))
        self.play(Write(m4b))
        self.wait(3)

        # --- Band 9 (subtopic_6): the pot on the stove ---
        self.next_band(9)
        b9t = Tex("The pot on the stove").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex(r"The stove plate is the GROUND —").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9a2 = Tex(r"heat comes from underneath").scale(1.0).shift(band_shift(9) + UP * 0.6)
        self.play(Write(b9a))
        self.play(Write(b9a2))
        self.wait(2)
        k1 = Tex(r"Braai face = radiation").scale(1.0).shift(band_shift(9) + DOWN * 0.3)
        k2 = Tex(r"Hot pot handle = conduction").scale(1.0).shift(band_shift(9) + DOWN * 1.0)
        k3 = Tex(r"Churning pap = convection").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        k4 = Tex(r"Sea breeze = advection").scale(1.0).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(k1))
        self.wait(1.5)
        self.play(Write(k2))
        self.wait(1.5)
        self.play(Write(k3))
        self.wait(1.5)
        self.play(Write(k4))
        self.play(Create(SurroundingRectangle(VGroup(k1, k2, k3, k4), color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): five reasons, one thermometer ---
        self.next_band(10)
        b10t = Tex("Why Upington bakes, Sutherland freezes").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        r1 = Tex(r"1. Torch angle — latitude").scale(1.0).shift(band_shift(10) + UP * 1.2)
        r2 = Tex(r"2. Height — $6{,}5^\circ$C per km climbed").scale(1.0).shift(band_shift(10) + UP * 0.4)
        r3 = Tex(r"3. Sea: slow cooker; land: frying pan").scale(1.0).shift(band_shift(10) + DOWN * 0.4)
        r4 = Tex(r"4. Agulhas east warm, Benguela west cold").scale(1.0).shift(band_shift(10) + DOWN * 1.2)
        r5 = Tex(r"5. Cloud blanket + north-facing slopes").scale(1.0).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(r1))
        self.wait(1.5)
        self.play(Write(r2))
        self.wait(1.5)
        self.play(Write(r3))
        self.wait(1.5)
        self.play(Write(r4))
        self.wait(1.5)
        self.play(Write(r5))
        self.wait(2)
        r6 = Tex(r"Torch, height, sea, currents, sky").scale(1.05).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(r6))
        self.play(Create(SurroundingRectangle(r6, color=GREEN)))
        self.wait(4)
