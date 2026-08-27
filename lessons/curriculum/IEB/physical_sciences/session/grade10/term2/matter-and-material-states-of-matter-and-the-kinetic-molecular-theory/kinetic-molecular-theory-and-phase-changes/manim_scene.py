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

# Band-layout whiteboard scene for "Kinetic Molecular Theory and Phase
# Changes" (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe mobjects only; write-only reveals; camera moves down band by
# band. Band time apportioned to subtopics.json
# (215/220/225/280/180/185/185 of 1490 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class KineticTheorySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the five statements ---
        title = Tex("Kinetic Molecular Theory and Phase Changes").scale(1.0).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("1. matter is particles  2. always moving").scale(0.9).shift(UP * 1.0)
        b0_l2 = Tex("3. temperature tracks average kinetic energy").scale(0.9).shift(UP * 0.2)
        b0_l3 = Tex("4. spaces between  5. forces between").scale(0.9).shift(DOWN * 0.6)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the evidence ---
        self.next_band(1)
        b1_t = Tex("The evidence").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("diffusion: the peeled orange crosses the room;").scale(0.85).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex("colouring drifts through still water").scale(0.85).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Brownian motion: pollen grains jitter —").scale(0.85).shift(band_shift(1) + DOWN * 0.5)
        b1_l4 = Tex("bombarded by unseen, moving particles").scale(0.85).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)
        b1_l5 = Tex("heat = energy transferred; temperature = average KE").scale(0.8).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): the three states, drawn ---
        self.next_band(2)
        b2_t = Tex("Three states, one model").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        # solid: ordered 3x3 grid of dots
        for i in range(3):
            for j in range(3):
                self.play(Create(Dot(band_shift(2) + UP * (1.0 - i * 0.4) + LEFT * (3.4 - j * 0.4), radius=0.06)), run_time=0.15)
        b2_l1 = Tex("solid: lattice, vibrate").scale(0.7).shift(band_shift(2) + DOWN * 0.6 + LEFT * 3.0)
        self.play(Write(b2_l1))
        # liquid: jumbled cluster
        for k, off in enumerate([UP * 0.9, UP * 0.55 + RIGHT * 0.35, UP * 0.75 + LEFT * 0.35,
                                 UP * 0.3, UP * 0.15 + RIGHT * 0.4, UP * 0.45 + LEFT * 0.15]):
            self.play(Create(Dot(band_shift(2) + off, radius=0.06)), run_time=0.15)
        b2_l2 = Tex("liquid: close, sliding").scale(0.7).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_l2))
        # gas: sparse dots
        for off in [UP * 1.0 + RIGHT * 2.6, UP * 0.2 + RIGHT * 3.4, UP * 0.7 + RIGHT * 3.9, DOWN * 0.1 + RIGHT * 2.9]:
            self.play(Create(Dot(band_shift(2) + off, radius=0.06)), run_time=0.15)
        b2_l3 = Tex("gas: far apart, fast").scale(0.7).shift(band_shift(2) + DOWN * 0.6 + RIGHT * 3.1)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("properties follow: shape, volume, compressibility").scale(0.8).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): the contest ---
        self.next_band(3)
        b3_t = Tex("The contest").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex("kinetic energy versus attractive forces").scale(0.95).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("forces win: solid; even match: liquid; energy wins: gas").scale(0.8).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = Tex("heating adds KE; cooling removes it —").scale(0.9).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = Tex("every change of state is the contest tipping").scale(0.9).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): the six changes of state ---
        self.next_band(4)
        b4_t = Tex("Six changes of state").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex(r"melt / freeze; evaporate-boil / condense").scale(0.9).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex("sublime: solid straight to gas — dry ice, mothballs").scale(0.85).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex("deposit: gas straight to solid — overnight frost").scale(0.85).shift(band_shift(4) + DOWN * 0.4)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex("loosening absorbs energy; tightening releases it").scale(0.85).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): definitions + evaporation vs boiling ---
        self.next_band(5)
        b5_t = Tex("Definitions that must be exact").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("melting point = freezing point, met from either side").scale(0.85).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex("boiling: throughout the liquid, vapour pressure").scale(0.85).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex("equals atmospheric pressure").scale(0.85).shift(band_shift(5) + DOWN * 0.3)
        self.play(Write(b5_l2))
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex("evaporation: any temperature, surface only —").scale(0.85).shift(band_shift(5) + DOWN * 1.2)
        b5_l5 = Tex("altitude: about 95 degrees in Johannesburg").scale(0.85).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the heating curve, drawn ---
        self.next_band(6)
        b6_t = Tex("The heating curve").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        # axes
        origin = band_shift(6) + DOWN * 1.8 + LEFT * 4.2
        self.play(Create(Line(origin, origin + UP * 3.4, color=WHITE)),
                  Create(Line(origin, origin + RIGHT * 8.0, color=WHITE)))
        # staircase: rise, plateau, rise, long plateau, rise
        p = [origin + UP * 0.4,
             origin + UP * 1.0 + RIGHT * 1.2,
             origin + UP * 1.0 + RIGHT * 2.4,
             origin + UP * 2.2 + RIGHT * 3.6,
             origin + UP * 2.2 + RIGHT * 6.4,
             origin + UP * 3.0 + RIGHT * 7.6]
        self.play(Create(Line(p[0], p[1], color=YELLOW)))
        self.play(Create(Line(p[1], p[2], color=BLUE)))
        self.play(Create(Line(p[2], p[3], color=YELLOW)))
        self.play(Create(Line(p[3], p[4], color=BLUE)))
        self.play(Create(Line(p[4], p[5], color=YELLOW)))
        b6_l1 = Tex("plateaus: 0 and 100 — flat while heating continues").scale(0.75).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_l1))
        self.wait(3)

        # --- Band 7 (subtopic_4): why the plateau + the traps ---
        self.next_band(7)
        b7_t = Tex("Why the plateau").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex("energy goes into POTENTIAL energy —").scale(0.9).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("separating particles, not speeding them up").scale(0.9).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2)
        b7_l3 = Tex("boiling plateau longer: full separation is the bigger job").scale(0.8).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("traps: 'no energy added'; heat = temperature;").scale(0.8).shift(band_shift(7) + DOWN * 1.4)
        b7_l5 = Tex("kelvin: add 273 to Celsius").scale(0.85).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): assembly, corridor, field ---
        self.next_band(8)
        b8_t = Tex("Assembly, corridor, field").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("assembly rows fidgeting on the spot: SOLID").scale(0.85).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("corridor crowd sliding past each other: LIQUID").scale(0.85).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("break-time field, far apart and fast: GAS").scale(0.85).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("jiggle versus pull decides the picture").scale(0.9).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): why the pot sticks at one hundred ---
        self.next_band(9)
        b9_t = Tex("Why the pot sticks at one hundred").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("thermometer stuck = jiggle not increasing").scale(0.85).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("the energy is breaking grips — paying the debt").scale(0.85).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2)
        b9_l3 = Tex("debt settled, savings climb: temperature rises again").scale(0.8).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("steam burns: the debt paid back into your skin").scale(0.8).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9_l4))
        self.wait(3)

        # --- Band 10 (subtopic_7): six words and the traps ---
        self.next_band(10)
        b10_t = Tex("Six words, three traps").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("melt, freeze, boil-evaporate, condense,").scale(0.85).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("sublime, deposit — loosening in, tightening out").scale(0.85).shift(band_shift(10) + UP * 0.5)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("1. energy IS still going in at the plateau").scale(0.85).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(b10_l3))
        self.wait(1.5)
        b10_l4 = Tex("2. heat is not temperature").scale(0.85).shift(band_shift(10) + DOWN * 1.1)
        self.play(Write(b10_l4))
        self.wait(1.5)
        b10_l5 = Tex("3. evaporation is not boiling").scale(0.85).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(4)
