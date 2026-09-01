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

# Band-layout whiteboard scene for the session duo "Circular Flow: Leakages
# and Injections" (grade 10, term 1). One band per teaching beat; the camera
# moves down to fresh space and earlier work stays on the canvas. Only
# exporter-safe mobjects are used (Tex/MathTex/Line/Arrow/Dot/Circle/
# Rectangle/SurroundingRectangle/VGroup); reveals are write-only.
#
# Subtopic time shares (subtopics.json, total 1420 s):
# 210/210/180/240/190/200/190 -> bands are apportioned accordingly.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CircularFlowLeakagesInjectionsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): households and firms, the first loop ---
        title = Tex("The Circular Flow").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        hh = Tex("HOUSEHOLDS").scale(1.05).shift(LEFT * 3 + UP * 0.4)
        fm = Tex("FIRMS").scale(1.05).shift(RIGHT * 3 + UP * 0.4)
        self.play(Write(hh), Write(fm))
        self.wait(1.5)
        top = Arrow(LEFT * 1.6 + UP * 1.0, RIGHT * 1.6 + UP * 1.0, buff=0)
        bot = Arrow(RIGHT * 1.6 + DOWN * 0.4, LEFT * 1.6 + DOWN * 0.4, buff=0)
        self.play(Create(top))
        t1 = Tex("factors of production").scale(0.85).shift(UP * 1.5)
        self.play(Write(t1))
        self.wait(2)
        self.play(Create(bot))
        t2 = Tex("wages, rent, interest, profit").scale(0.85).shift(DOWN * 0.9)
        self.play(Write(t2))
        self.wait(2.5)
        d1 = Tex(r"Income spent on goods — the circle turns").scale(1.0).shift(DOWN * 2.0)
        self.play(Write(d1))
        self.wait(3)

        # --- Band 1 (subtopic_1): real vs money flows, two markets ---
        self.next_band(1)
        b1t = Tex("Two markets, two lanes").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        b1a = Tex(r"FACTOR market: work finds employers").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1b = Tex(r"GOODS market: money finds goods").scale(1.05).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1a))
        self.play(Write(b1b))
        self.wait(2.5)
        b1c = Tex(r"REAL flows: factors and goods").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        b1d = Tex(r"MONEY flows: the opposite lane").scale(1.05).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1c))
        self.play(Write(b1d))
        self.wait(2.5)
        b1e = Tex(r"Simple CLOSED economy: the skeleton").scale(1.05).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1e))
        self.play(Create(SurroundingRectangle(b1e, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): savings leak, investment injects ---
        self.next_band(2)
        b2t = Tex("The first drain and the first tap").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        b2a = Tex(r"R600 banked: SAVINGS leak out —").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2b = Tex(r"earned, not passed back to firms").scale(1.05).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2a))
        self.play(Write(b2b))
        self.wait(2.5)
        b2c = Tex(r"Banks lend onward: firms buy machines").scale(1.0).shift(band_shift(2) + DOWN * 0.6)
        b2d = Tex(r"INVESTMENT injects back in").scale(1.05).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(b2c))
        self.play(Write(b2d))
        self.wait(2.5)
        b2e = Tex(r"Financial sector: the connecting pipe").scale(1.0).shift(band_shift(2) + DOWN * 2.3)
        self.play(Write(b2e))
        self.play(Create(SurroundingRectangle(b2e, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the equilibrium comparison ---
        self.next_band(3)
        b3t = Tex("The comparison that decides everything").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        b3a = Tex(r"Leakages $>$ injections: circle tightens").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3b = Tex(r"Injections $>$ leakages: circle widens").scale(1.05).shift(band_shift(3) + UP * 0.3)
        b3c = Tex(r"Equal: EQUILIBRIUM").scale(1.05).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(b3a))
        self.wait(2)
        self.play(Write(b3b))
        self.wait(2)
        self.play(Write(b3c))
        self.play(Create(SurroundingRectangle(b3c, color=GREEN)))
        self.wait(2.5)
        b3w = Tex(r"``Leakages are bad, injections good''").scale(1.0).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3w))
        self.play(Create(strike(b3w)))
        self.wait(2)
        b3d = Tex(r"Direction of flow — never virtue").scale(1.05).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3d))
        self.wait(3)

        # --- Band 4 (subtopic_3): adding government ---
        self.next_band(4)
        b4t = Tex("Adding government").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        b4a = Tex(r"TAXES leak: SARS collects,").scale(1.05).shift(band_shift(4) + UP * 1.1)
        b4b = Tex(r"the stream cannot spend it").scale(1.05).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4a))
        self.play(Write(b4b))
        self.wait(2.5)
        b4c = Tex(r"SPENDING injects: teachers, nurses,").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        b4d = Tex(r"roads tarred, grants deposited").scale(1.0).shift(band_shift(4) + DOWN * 1.4)
        self.play(Write(b4c))
        self.play(Write(b4d))
        self.wait(2.5)
        b4e = Tex(r"Tally: 2 leakages, 2 injections —").scale(1.0).shift(band_shift(4) + DOWN * 2.2)
        b4f = Tex(r"still a CLOSED economy").scale(1.0).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4e))
        self.play(Write(b4f))
        self.wait(3)

        # --- Band 5 (subtopic_4): the foreign sector opens the economy ---
        self.next_band(5)
        b5t = Tex("The foreign sector opens the doors").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        b5a = Tex(r"IMPORTS leak: Korean laptops,").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5b = Tex(r"rands paid to producers outside").scale(1.0).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5a))
        self.play(Write(b5b))
        self.wait(2.5)
        b5c = Tex(r"EXPORTS inject: citrus to Rotterdam,").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        b5d = Tex(r"platinum to Japan — money pours in").scale(1.0).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5c))
        self.play(Write(b5d))
        self.wait(2.5)
        b5e = Tex(r"Four participants: OPEN economy").scale(1.05).shift(band_shift(5) + DOWN * 2.3)
        self.play(Write(b5e))
        self.play(Create(SurroundingRectangle(b5e, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): master lists and the three doors ---
        self.next_band(6)
        b6t = Tex("The master lists").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        b6a = Tex(r"Leakages: savings, taxes, imports").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6b = Tex(r"Injections: investment, gov spending,").scale(1.05).shift(band_shift(6) + UP * 0.3)
        b6c = Tex(r"exports").scale(1.05).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6a))
        self.wait(2)
        self.play(Write(b6b))
        self.play(Write(b6c))
        self.wait(2.5)
        b6d = Tex(r"Three doors, traffic both ways:").scale(1.0).shift(band_shift(6) + DOWN * 1.3)
        b6e = Tex(r"bank, government, border").scale(1.05).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6d))
        self.play(Write(b6e))
        self.play(Create(SurroundingRectangle(b6e, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): Friday in the neighbourhood ---
        self.next_band(7)
        b7t = Tex("Friday in the neighbourhood").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex(r"Pay lands Friday; by Saturday it moves:").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7b = Tex(r"supermarket, barber, hardware").scale(1.0).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7a))
        self.play(Write(b7b))
        self.wait(2.5)
        b7c = Tex(r"Their takings pay THEIR people...").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        b7d = Tex(r"the money never rests — it CIRCLES").scale(1.05).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(b7c))
        self.play(Write(b7d))
        self.wait(2.5)
        b7e = Tex(r"Hiring side + till side, two lanes").scale(1.0).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7e))
        self.play(Create(SurroundingRectangle(b7d, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): three drains and three taps ---
        self.next_band(8)
        b8t = Tex("Three drains, three taps").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex(r"Bank door: deposit out, mixer loan in").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8a))
        self.wait(2)
        b8b = Tex(r"Government door: tax out, tar road in").scale(1.0).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex(r"Border door: laptop out, oranges in").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8c))
        self.wait(2.5)
        b8d = Tex(r"Learn three doors, not six facts").scale(1.05).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(b8d))
        self.play(Create(SurroundingRectangle(b8d, color=GREEN)))
        self.wait(2)
        b8e = Tex(r"Drains are not villains — direction only").scale(1.0).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8e))
        self.wait(3)

        # --- Band 9 (subtopic_7): reading the water level ---
        self.next_band(9)
        b9t = Tex("Reading the water level").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex(r"Drains win: level drops — quiet tills,").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9b = Tex(r"shorter shifts, thinner pay").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9a))
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = Tex(r"Taps win: level rises — the good spiral").scale(1.0).shift(band_shift(9) + DOWN * 0.5)
        b9d = Tex(r"Equal: steady — equilibrium").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9c))
        self.play(Write(b9d))
        self.wait(2.5)
        b9e = Tex(r"Every headline is a drain or a tap —").scale(1.0).shift(band_shift(9) + DOWN * 2.1)
        b9f = Tex(r"push it through its door").scale(1.0).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9e))
        self.play(Write(b9f))
        self.play(Create(SurroundingRectangle(b9f, color=GREEN)))
        self.wait(4)
