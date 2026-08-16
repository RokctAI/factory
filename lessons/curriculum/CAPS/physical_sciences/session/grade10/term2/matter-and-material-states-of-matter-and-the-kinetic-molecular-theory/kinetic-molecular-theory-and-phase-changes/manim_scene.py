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

# Band-layout whiteboard scene for kinetic-molecular-theory-and-phase-changes
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe mobjects only; add-only lifecycle; heating curve hand-built
# from Line segments and Arrow axes (no Axes/Polygon).
# Time apportioned to subtopics.json (215/220/225/280/180/185/185 of 1490 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class KineticMolecularTheoryPhaseChangesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the five statements ---
        title = Tex("Kinetic Molecular Theory").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        a1 = Tex("1. All matter is made of particles").scale(1.0).shift(UP * 1.0)
        a2 = Tex("2. in constant, random motion").scale(1.0).shift(UP * 0.2)
        a3 = Tex("3. average $E_k$ rises with temperature").scale(1.0).shift(DOWN * 0.6)
        a4 = Tex("4. spaces between the particles").scale(1.0).shift(DOWN * 1.4)
        a5 = Tex("5. forces of attraction between them").scale(1.0).shift(DOWN * 2.2)
        for m in (a1, a2, a3, a4, a5):
            self.play(Write(m))
            self.wait(1.6)
        a6 = Tex("Forces vs kinetic energy decides the state").scale(0.95).shift(DOWN * 3.0)
        self.play(Write(a6))
        self.wait(3)

        # --- Band 1 (subtopic_1): the evidence ---
        self.next_band(1)
        b1_t = Tex("The evidence for particles").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_1 = Tex("Diffusion: vanilla crosses the kitchen").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_1))
        self.wait(2)
        b1_2 = Tex("faster in gases, faster when hot").scale(1.0).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_2))
        self.wait(2)
        b1_3 = Tex("Brownian motion: smoke specks jerk about").scale(1.0).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_3))
        self.wait(2)
        b1_4 = Tex("bombarded by unseen air particles").scale(1.0).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(b1_4))
        self.wait(2)
        b1_5 = Tex("Temperature = AVERAGE $E_k$; heat = energy").scale(0.95).shift(band_shift(1) + DOWN * 2.3)
        b1_6 = Tex("transferred by a temperature difference").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_5))
        self.play(Write(b1_6))
        self.wait(3)

        # --- Band 2 (subtopic_2): the three states, drawn ---
        self.next_band(2)
        b2_t = Tex("Solid, liquid, gas").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        # solid: neat 3x3 grid in a box
        sC = band_shift(2) + UP * 0.6 + LEFT * 3.6
        sBox = Rectangle(width=1.9, height=1.9).move_to(sC)
        sDots = VGroup(*[Dot(sC + RIGHT * (j - 1) * 0.55 + UP * (i - 1) * 0.55)
                         for i in range(3) for j in range(3)])
        sLab = Tex("solid: lattice,").scale(0.8).move_to(sC + DOWN * 1.4)
        sLab2 = Tex("vibrate in place").scale(0.8).move_to(sC + DOWN * 1.95)
        self.play(Create(sBox))
        self.play(Create(sDots), Write(sLab), Write(sLab2))
        self.wait(2)
        # liquid: irregular cluster
        lC = band_shift(2) + UP * 0.6
        lBox = Rectangle(width=1.9, height=1.9).move_to(lC)
        lDots = VGroup(Dot(lC + LEFT * 0.55 + DOWN * 0.55), Dot(lC + DOWN * 0.6),
                       Dot(lC + RIGHT * 0.5 + DOWN * 0.5), Dot(lC + LEFT * 0.3 + DOWN * 0.05),
                       Dot(lC + RIGHT * 0.25 + UP * 0.05), Dot(lC + LEFT * 0.6 + UP * 0.45),
                       Dot(lC + RIGHT * 0.6 + UP * 0.4), Dot(lC + UP * 0.5))
        lLab = Tex("liquid: close,").scale(0.8).move_to(lC + DOWN * 1.4)
        lLab2 = Tex("slide past").scale(0.8).move_to(lC + DOWN * 1.95)
        self.play(Create(lBox))
        self.play(Create(lDots), Write(lLab), Write(lLab2))
        self.wait(2)
        # gas: sparse with velocity arrows
        gC = band_shift(2) + UP * 0.6 + RIGHT * 3.6
        gBox = Rectangle(width=1.9, height=1.9).move_to(gC)
        gDots = VGroup(Dot(gC + LEFT * 0.6 + UP * 0.5), Dot(gC + RIGHT * 0.55 + DOWN * 0.6),
                       Dot(gC + RIGHT * 0.4 + UP * 0.35), Dot(gC + LEFT * 0.35 + DOWN * 0.4))
        gArr = VGroup(Arrow(gC + LEFT * 0.6 + UP * 0.5, gC + LEFT * 0.15 + UP * 0.75, buff=0),
                      Arrow(gC + RIGHT * 0.55 + DOWN * 0.6, gC + RIGHT * 0.1 + DOWN * 0.25, buff=0))
        gLab = Tex("gas: far apart,").scale(0.8).move_to(gC + DOWN * 1.4)
        gLab2 = Tex("fast, random").scale(0.8).move_to(gC + DOWN * 1.95)
        self.play(Create(gBox))
        self.play(Create(gDots), Create(gArr), Write(gLab), Write(gLab2))
        self.wait(2.5)
        b2_r = Tex("Pressure = collisions with the walls").scale(0.95).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_r))
        self.wait(3)

        # --- Band 3 (subtopic_2): the contest ---
        self.next_band(3)
        b3_t = Tex("A contest: forces vs kinetic energy").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_1 = Tex("Forces win: SOLID (fixed shape, volume)").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_1))
        self.wait(2)
        b3_2 = Tex("Roughly matched: LIQUID (volume only)").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_2))
        self.wait(2)
        b3_3 = Tex("Energy wins: GAS (fills the container)").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_3))
        self.wait(2)
        b3_4 = Tex("Heating adds $E_k$; cooling removes it").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_4))
        self.wait(2)
        b3_5 = Tex("Every change of state = the contest tipping").scale(0.95).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_5))
        self.play(Create(SurroundingRectangle(b3_5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the six changes of state ---
        self.next_band(4)
        b4_t = Tex("Six changes of state").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        sol = Tex("SOLID").scale(1.0).shift(band_shift(4) + UP * 1.0 + LEFT * 4.0)
        liq = Tex("LIQUID").scale(1.0).shift(band_shift(4) + UP * 1.0)
        gas = Tex("GAS").scale(1.0).shift(band_shift(4) + UP * 1.0 + RIGHT * 4.0)
        self.play(Write(sol), Write(liq), Write(gas))
        self.wait(1)
        ar1 = Arrow(band_shift(4) + UP * 1.25 + LEFT * 3.1, band_shift(4) + UP * 1.25 + LEFT * 1.1, buff=0)
        ar1l = Tex("melting").scale(0.75).shift(band_shift(4) + UP * 1.6 + LEFT * 2.1)
        ar2 = Arrow(band_shift(4) + UP * 0.75 + LEFT * 1.1, band_shift(4) + UP * 0.75 + LEFT * 3.1, buff=0)
        ar2l = Tex("freezing").scale(0.75).shift(band_shift(4) + UP * 0.35 + LEFT * 2.1)
        ar3 = Arrow(band_shift(4) + UP * 1.25 + RIGHT * 1.2, band_shift(4) + UP * 1.25 + RIGHT * 3.3, buff=0)
        ar3l = Tex("boiling / evaporation").scale(0.7).shift(band_shift(4) + UP * 1.6 + RIGHT * 2.2)
        ar4 = Arrow(band_shift(4) + UP * 0.75 + RIGHT * 3.3, band_shift(4) + UP * 0.75 + RIGHT * 1.2, buff=0)
        ar4l = Tex("condensation").scale(0.7).shift(band_shift(4) + UP * 0.35 + RIGHT * 2.2)
        self.play(Create(ar1), Write(ar1l))
        self.play(Create(ar2), Write(ar2l))
        self.wait(1.5)
        self.play(Create(ar3), Write(ar3l))
        self.play(Create(ar4), Write(ar4l))
        self.wait(1.5)
        b4_1 = Tex("Sublimation: solid straight to gas (dry ice)").scale(0.95).shift(band_shift(4) + DOWN * 0.6)
        b4_2 = Tex("Deposition: gas straight to solid (frost)").scale(0.95).shift(band_shift(4) + DOWN * 1.4)
        self.play(Write(b4_1))
        self.wait(2)
        self.play(Write(b4_2))
        self.wait(2)
        b4_3 = Tex("Melt, evaporate, sublime: ABSORB energy").scale(0.95).shift(band_shift(4) + DOWN * 2.2)
        b4_4 = Tex("Freeze, condense, deposit: RELEASE energy").scale(0.95).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_3))
        self.wait(2)
        self.play(Write(b4_4))
        self.wait(3)

        # --- Band 5 (subtopic_3): definitions + evaporation vs boiling ---
        self.next_band(5)
        b5_t = Tex("Melting point, boiling point").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_1 = Tex("Melting point = freezing point").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_1))
        self.wait(2)
        b5_2 = Tex(r"Pure water: 0 $^\circ$C and 100 $^\circ$C (sea level)").scale(0.95).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_2))
        self.wait(2)
        b5_3 = Tex("Evaporation: any temperature, surface only").scale(0.95).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_3))
        self.wait(2)
        b5_4 = Tex("Boiling: at boiling point, bubbles throughout").scale(0.95).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_4))
        self.wait(2)
        b5_5 = Tex(r"Highveld: lower pressure, boils near 95 $^\circ$C").scale(0.95).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_5))
        self.play(Create(SurroundingRectangle(b5_5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the heating curve, drawn ---
        self.next_band(6)
        b6_t = Tex("The heating curve of water (2 kg ice)").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        o = band_shift(6) + DOWN * 2.0 + LEFT * 3.2
        xax = Arrow(o, o + RIGHT * 6.6, buff=0)
        yax = Arrow(o, o + UP * 4.0, buff=0)
        xlab = Tex("time").scale(0.8).move_to(o + RIGHT * 6.3 + DOWN * 0.4)
        ylab = Tex(r"T ($^\circ$C)").scale(0.8).move_to(o + UP * 3.9 + LEFT * 0.1 + RIGHT * 0.9)
        self.play(Create(xax), Create(yax), Write(xlab), Write(ylab))
        self.wait(1)
        seg1 = Line(o + RIGHT * 0.2 + UP * 0.3, o + RIGHT * 1.0 + UP * 1.2)
        l1 = Tex(r"$-20$").scale(0.7).move_to(o + RIGHT * 0.2 + DOWN * 0.3)
        self.play(Create(seg1), Write(l1))
        self.wait(1.5)
        seg2 = Line(o + RIGHT * 1.0 + UP * 1.2, o + RIGHT * 2.0 + UP * 1.2)
        l2 = Tex(r"0 $^\circ$C: melting").scale(0.7).move_to(o + RIGHT * 1.5 + UP * 0.7)
        self.play(Create(seg2), Write(l2))
        self.wait(2)
        seg3 = Line(o + RIGHT * 2.0 + UP * 1.2, o + RIGHT * 3.2 + UP * 2.6)
        self.play(Create(seg3))
        self.wait(1.5)
        seg4 = Line(o + RIGHT * 3.2 + UP * 2.6, o + RIGHT * 5.2 + UP * 2.6)
        l4 = Tex(r"100 $^\circ$C: boiling (longer)").scale(0.7).move_to(o + RIGHT * 4.2 + UP * 2.1)
        self.play(Create(seg4), Write(l4))
        self.wait(2)
        seg5 = Line(o + RIGHT * 5.2 + UP * 2.6, o + RIGHT * 6.0 + UP * 3.5)
        l5 = Tex("steam").scale(0.7).move_to(o + RIGHT * 6.1 + UP * 3.0)
        self.play(Create(seg5), Write(l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): why the plateau + the traps ---
        self.next_band(7)
        b7_t = Tex("Why does the temperature stop rising?").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_trap = Tex("``No energy is being added''").scale(1.0).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_trap))
        self.play(Create(strike(b7_trap)))
        self.wait(2)
        b7_1 = Tex("Energy pours in the whole time, but it").scale(1.0).shift(band_shift(7) + UP * 0.3)
        b7_2 = Tex("breaks forces: POTENTIAL energy rises,").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_3 = Tex("not kinetic — particles separate, not speed up").scale(0.95).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(b7_1))
        self.wait(1.5)
        self.play(Write(b7_2))
        self.wait(1.5)
        self.play(Write(b7_3))
        self.play(Create(SurroundingRectangle(b7_3, color=GREEN)))
        self.wait(2.5)
        b7_4 = MathTex(r"T_K = T_C + 273: \; 0\,^\circ\text{C} = 273\ \text{K}").scale(1.0).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7_4))
        self.wait(2)
        b7_5 = Tex("Cooling curve: the exact mirror, energy OUT").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): assembly, corridor, field ---
        self.next_band(8)
        b8_t = Tex("The assembly, the crowd, the field").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_1 = Tex("Assembly rows, fidgeting on the spot: SOLID").scale(0.95).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_1))
        self.wait(2)
        b8_2 = Tex("Corridor crush, sliding past: LIQUID").scale(0.95).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_2))
        self.wait(2)
        b8_3 = Tex("Sports field, scattered and fast: GAS").scale(0.95).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_3))
        self.wait(2)
        b8_4 = Tex("Tug-of-war: jiggle vs pull decides the state").scale(0.95).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_4))
        self.play(Create(SurroundingRectangle(b8_4, color=GREEN)))
        self.wait(2)
        b8_5 = Tex("Proof: vanilla smell; jittering smoke specks").scale(0.95).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_5))
        self.wait(3)

        # --- Band 9 (subtopic_6): why the pot sticks at one hundred ---
        self.next_band(9)
        b9_t = Tex("Why the pot sticks at one hundred").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_1 = Tex("40, 60, 80, 99, 100... then it STOPS").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_1))
        self.wait(2)
        b9_2 = Tex("Stove still on — energy pays a DEBT:").scale(1.0).shift(band_shift(9) + UP * 0.2)
        b9_3 = Tex("breaking every grip between particles").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_2))
        self.wait(2)
        self.play(Write(b9_3))
        self.play(Create(SurroundingRectangle(b9_3, color=GREEN)))
        self.wait(2)
        b9_4 = Tex("Same at 0: slush until the last ice melts").scale(0.95).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_4))
        self.wait(2)
        b9_5 = Tex("Steam burns: separation energy dumped back").scale(0.95).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_5))
        self.wait(3)

        # --- Band 10 (subtopic_7): six words and the traps ---
        self.next_band(10)
        b10_t = Tex("Six words, three traps").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_1 = Tex("Loosening grip needs energy IN:").scale(0.95).shift(band_shift(10) + UP * 1.2)
        b10_2 = Tex("melt, evaporate, sublime").scale(0.95).shift(band_shift(10) + UP * 0.5)
        self.play(Write(b10_1))
        self.play(Write(b10_2))
        self.wait(2)
        b10_3 = Tex("Tightening gives energy OUT:").scale(0.95).shift(band_shift(10) + DOWN * 0.3)
        b10_4 = Tex("freeze, condense, deposit").scale(0.95).shift(band_shift(10) + DOWN * 1.0)
        self.play(Write(b10_3))
        self.play(Write(b10_4))
        self.wait(2)
        b10_5 = Tex("Traps: flat graph $\\neq$ no energy;").scale(0.95).shift(band_shift(10) + DOWN * 1.8)
        b10_6 = Tex("heat $\\neq$ temperature; boiling $\\neq$ evaporation").scale(0.95).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10_5))
        self.wait(2)
        self.play(Write(b10_6))
        self.play(Create(SurroundingRectangle(b10_6, color=GREEN)))
        self.wait(4)
