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

# Band-layout whiteboard scene for "Humidity, condensation and rainfall
# types" (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Rising parcels are Arrows, mountains are Line ramps, cloud bases are
# dashed-effect Line rows, all labelled with Tex as drawn. Add-only
# lifecycle; camera moves down band by band.
# Subtopic durations (s): 215/240/240/250/180/185/190 of 1500.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class HumidityRainfallSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): humidity definitions ---
        title = Tex("Moisture in the Atmosphere").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        h1 = Tex(r"Absolute humidity: grams per m$^3$").scale(1.0).shift(UP * 1.2)
        h2 = Tex(r"Relative humidity: \% of the maximum").scale(1.0).shift(UP * 0.4)
        h3 = Tex(r"Law: warm air carries far more vapour").scale(1.0).shift(DOWN * 0.5)
        self.play(Write(h1))
        self.wait(2)
        self.play(Write(h2))
        self.wait(2)
        self.play(Write(h3))
        self.play(Create(SurroundingRectangle(h3, color=GREEN)))
        self.wait(2)
        h4 = Tex(r"Vapour is invisible — cloud is liquid").scale(0.95).shift(DOWN * 1.6)
        self.play(Write(h4))
        self.wait(3)

        # --- Band 1 (subtopic_1): the RH calculation and dew point ---
        self.next_band(1)
        b1t = Tex("From 50\\% to saturation, no water added").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        c1 = Tex(r"At $25^\circ$C: max 23 g, holds 11,5 g").scale(1.0).shift(band_shift(1) + UP * 1.2)
        c2 = Tex(r"$11{,}5 \div 23 \times 100 = 50\%$").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.wait(2)
        c3 = Tex(r"Cool to $13^\circ$C: max falls to 11,5 g").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        c4 = Tex(r"$11{,}5 \div 11{,}5 = 100\%$ — SATURATED").scale(1.0).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(c3))
        self.wait(2)
        self.play(Write(c4))
        self.play(Create(SurroundingRectangle(c4, color=GREEN)))
        self.wait(2)
        c5 = Tex(r"Dew point = temperature of saturation").scale(1.0).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(c5))
        self.wait(3)

        # --- Band 2 (subtopic_2): dew, frost, mist, fog ---
        self.next_band(2)
        b2t = Tex("Where the cooling happens decides the form").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        f1 = Tex(r"Dew: clear still night, dew point above 0").scale(0.95).shift(band_shift(2) + UP * 1.2)
        f2 = Tex(r"Frost: dew point below 0 — straight to ice").scale(0.95).shift(band_shift(2) + UP * 0.4)
        f3 = Tex(r"Mist/fog: a whole layer cooled — fog < 1 km").scale(0.95).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(f1))
        self.wait(2)
        self.play(Write(f2))
        self.wait(2)
        self.play(Write(f3))
        self.wait(2)
        f4 = Tex(r"Radiation fog: Hex River valley dawns").scale(0.95).shift(band_shift(2) + DOWN * 1.3)
        f5 = Tex(r"Advection fog: sea air over cold Benguela").scale(0.95).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(f4))
        self.wait(2)
        self.play(Write(f5))
        self.play(Create(SurroundingRectangle(f5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): adiabatic cooling + condensation level ---
        self.next_band(3)
        b3t = Tex("Rising air cools by expanding").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        up = Arrow(band_shift(3) + LEFT * 3.6 + DOWN * 2.4, band_shift(3) + LEFT * 3.6 + UP * 1.6, buff=0, color=RED)
        self.play(Create(up))
        r1 = Tex(r"Dry rate: $1^\circ$C per 100 m").scale(0.95).shift(band_shift(3) + LEFT * 0.4 + UP * 1.2)
        r2 = Tex(r"Saturated rate: $0{,}5^\circ$C per 100 m").scale(0.95).shift(band_shift(3) + RIGHT * 0.1 + UP * 0.4)
        self.play(Write(r1))
        self.wait(2)
        self.play(Write(r2))
        self.wait(2)
        base = Line(band_shift(3) + LEFT * 4.4 + DOWN * 0.4, band_shift(3) + LEFT * 2.8 + DOWN * 0.4, color=BLUE)
        bl = Tex(r"cloud base = condensation level").scale(0.85).shift(band_shift(3) + LEFT * 0.6 + DOWN * 0.4)
        self.play(Create(base), Write(bl))
        self.wait(2)
        calc1 = Tex(r"$28^\circ$C surface, dew point $16^\circ$C").scale(0.95).shift(band_shift(3) + DOWN * 1.4)
        calc2 = Tex(r"12 degrees at $1^\circ$/100 m = 1 200 m base").scale(0.95).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(calc1))
        self.wait(2)
        self.play(Write(calc2))
        self.play(Create(SurroundingRectangle(calc2, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): naming clouds ---
        self.next_band(4)
        b4t = Tex("Four Latin bricks build every name").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        n1 = Tex(r"CIRRO high wisps · ALTO middle").scale(1.0).shift(band_shift(4) + UP * 1.2)
        n2 = Tex(r"STRATO flat sheet · CUMULO heaped").scale(1.0).shift(band_shift(4) + UP * 0.4)
        n3 = Tex(r"NIMBUS: raining right now").scale(1.0).shift(band_shift(4) + DOWN * 0.4)
        self.play(Write(n1))
        self.wait(2)
        self.play(Write(n2))
        self.wait(2)
        self.play(Write(n3))
        self.play(Create(SurroundingRectangle(n3, color=GREEN)))
        self.wait(2)
        n4 = Tex(r"High = ice: cirrus feathers,").scale(0.95).shift(band_shift(4) + DOWN * 1.4)
        n5 = Tex(r"cirrostratus halo — front tomorrow").scale(0.95).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(n4))
        self.play(Write(n5))
        self.wait(3)

        # --- Band 5 (subtopic_3): middle, low, vertical clouds ---
        self.next_band(5)
        b5t = Tex("Middle, low, and the tall ones").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        m1 = Tex(r"Altostratus: sun behind frosted glass").scale(0.95).shift(band_shift(5) + UP * 1.2)
        m2 = Tex(r"Stratus: grey blanket — fog when grounded").scale(0.95).shift(band_shift(5) + UP * 0.4)
        m3 = Tex(r"Nimbostratus: dark, steady all-day rain").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(m1))
        self.wait(2)
        self.play(Write(m2))
        self.wait(2)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Cumulus: flat base on the shared shelf").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        m5 = Tex(r"Cumulonimbus: anvil, thunder, hail").scale(0.95).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(m4))
        self.wait(2)
        self.play(Write(m5))
        self.play(Create(SurroundingRectangle(m5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): relief rainfall ---
        self.next_band(6)
        b6t = Tex("Relief rain: the mountain ramp").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        up_slope = Line(band_shift(6) + LEFT * 4.4 + DOWN * 2.2, band_shift(6) + DOWN * 0.0, stroke_width=5)
        down_slope = Line(band_shift(6) + DOWN * 0.0, band_shift(6) + RIGHT * 4.4 + DOWN * 2.2, stroke_width=5)
        self.play(Create(up_slope), Create(down_slope))
        wind = Arrow(band_shift(6) + LEFT * 5.2 + DOWN * 1.6, band_shift(6) + LEFT * 3.4 + DOWN * 1.2, buff=0, color=BLUE)
        wl = Tex("moist sea air").scale(0.8).shift(band_shift(6) + LEFT * 4.2 + DOWN * 0.7)
        self.play(Create(wind), Write(wl))
        self.wait(2)
        g1 = Tex(r"Windward: cools, condenses, rains").scale(0.9).shift(band_shift(6) + LEFT * 2.6 + UP * 1.0)
        g2 = Tex(r"Leeward: warms, dries — RAIN SHADOW").scale(0.9).shift(band_shift(6) + RIGHT * 2.6 + UP * 1.0)
        self.play(Write(g1))
        self.wait(2)
        self.play(Write(g2))
        self.wait(2)
        g3 = Tex(r"Outeniquas: George green, Klein Karoo dry").scale(0.9).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(g3))
        self.play(Create(SurroundingRectangle(g3, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): convectional and frontal ---
        self.next_band(7)
        b7t = Tex("The fire and the wedge").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(1.5)
        c1a = Tex(r"Convectional: baked ground, thermals up,").scale(0.95).shift(band_shift(7) + UP * 1.2)
        c1b = Tex(r"late-afternoon cloudburst — Highveld summer").scale(0.95).shift(band_shift(7) + UP * 0.5)
        self.play(Write(c1a))
        self.play(Write(c1b))
        self.wait(2)
        c2a = Tex(r"Frontal: dense cold air wedges under").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        c2b = Tex(r"warm moist air — rain along the boundary").scale(0.95).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(c2a))
        self.play(Write(c2b))
        self.wait(2)
        c3 = Tex(r"Western Cape winter: SW fronts, May–August").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(c3))
        self.play(Create(SurroundingRectangle(c3, color=GREEN)))
        self.wait(2)
        c4 = Tex(r"Classify by the LIFT, never the violence").scale(0.95).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(c4))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): squeezing the sponge ---
        self.next_band(8)
        b8t = Tex("Squeezing the sponge").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        big = Rectangle(width=2.6, height=1.6, color=YELLOW).shift(band_shift(8) + LEFT * 2.8 + UP * 0.6)
        bl2 = Tex("warm: big sponge").scale(0.8).shift(band_shift(8) + LEFT * 2.8 + DOWN * 0.5)
        small = Rectangle(width=1.3, height=0.8, color=BLUE).shift(band_shift(8) + RIGHT * 2.6 + UP * 0.6)
        sl = Tex("cold: small sponge").scale(0.8).shift(band_shift(8) + RIGHT * 2.6 + DOWN * 0.5)
        self.play(Create(big), Write(bl2))
        self.wait(1.5)
        self.play(Create(small), Write(sl))
        self.wait(2)
        b8a = Tex(r"Cooling shrinks the sponge — full = saturated").scale(0.95).shift(band_shift(8) + DOWN * 1.4)
        b8b = Tex(r"Glasses misting outside the mall: same physics").scale(0.95).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8a))
        self.play(Create(SurroundingRectangle(b8a, color=GREEN)))
        self.wait(2)
        self.play(Write(b8b))
        self.wait(3)

        # --- Band 9 (subtopic_6): clouds have surnames ---
        self.next_band(9)
        b9t = Tex("Clouds have surnames").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        s1 = Tex(r"Cirro · Alto · Strato · Cumulo + Nimbus").scale(1.0).shift(band_shift(9) + UP * 1.2)
        self.play(Write(s1))
        self.wait(2)
        s2 = Tex(r"High feathers: cirrus — front tomorrow").scale(0.95).shift(band_shift(9) + UP * 0.4)
        s3 = Tex(r"Halo ring: cirrostratus — front closer").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        s4 = Tex(r"Grey blanket: stratus; grounded = fog").scale(0.95).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(s2))
        self.wait(2)
        self.play(Write(s3))
        self.wait(2)
        self.play(Write(s4))
        self.wait(2)
        s5 = Tex(r"Cauliflower to thundercloud: cumulus $\rightarrow$ cumulonimbus").scale(0.9).shift(band_shift(9) + DOWN * 2.2)
        self.play(Write(s5))
        self.play(Create(SurroundingRectangle(s5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): ramp, fire, wedge ---
        self.next_band(10)
        b10t = Tex("The ramp, the fire and the wedge").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        w1 = Tex(r"RAMP: up the mountain — wet front, dry back").scale(0.95).shift(band_shift(10) + UP * 1.2)
        w2 = Tex(r"FIRE: baked ground — 4 o'clock cloudburst").scale(0.95).shift(band_shift(10) + UP * 0.4)
        w3 = Tex(r"WEDGE: cold air under warm — winter Cape rain").scale(0.95).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(w1))
        self.wait(2)
        self.play(Write(w2))
        self.wait(2)
        self.play(Write(w3))
        self.wait(2)
        w4 = Tex(r"Rain judged by its violence").scale(0.95).shift(band_shift(10) + DOWN * 1.4)
        self.play(Write(w4))
        self.play(Create(strike(w4)))
        w5 = Tex(r"Rain judged by what lifted the air").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(w5))
        self.play(Create(SurroundingRectangle(w5, color=GREEN)))
        self.wait(4)
