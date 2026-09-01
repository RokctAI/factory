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

# Band-layout whiteboard scene for the revision session "Physics Essentials:
# Motion, Energy and Electricity" (Part 1 — Expert: subtopics 1-4; Part 2 —
# Simplifier: subtopics 5-7). Exporter-safe mobjects only; the series circuit
# is hand-built from Rectangles and Lines. Add-only lifecycle. Band time
# apportioned to subtopics.json (245/245/235/250/195/190/185 of 1545 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PhysicsEssentialsRevisionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(15)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the vocabulary pairs ---
        title = Tex("Physics Essentials: the Revision Sweep").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Distance: path, scalar. Displacement: arrow, vector").scale(0.95).shift(UP * 0.9)
        self.play(Write(d1))
        self.wait(2.5)
        d2 = Tex("Speed: $\\tfrac{D}{t}$; velocity adds direction").scale(1.05).shift(DOWN * 0.1)
        self.play(Write(d2))
        self.wait(2.5)
        d3 = MathTex(r"a = \frac{\Delta v}{\Delta t}").scale(1.2).shift(DOWN * 1.3)
        self.play(Write(d3))
        self.wait(3)

        # --- Band 1 (subtopic_1): the car, three equations ---
        self.next_band(1)
        b1t = Tex("From rest, $a = 2$ m/s$^2$, for 5 s").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = MathTex(r"v = u + at = 0 + 2 \times 5 = 10 \text{ m/s}").scale(1.05).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1a))
        self.wait(2.5)
        b1b = MathTex(r"\Delta x = \tfrac{1}{2}at^2 = \tfrac{1}{2} \times 2 \times 25 = 25 \text{ m}").scale(1.0).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1b))
        self.wait(2.5)
        b1c = MathTex(r"v^2 = 2a\Delta x = 100, \; v = 10 \text{ m/s}").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1c))
        self.play(Create(SurroundingRectangle(b1c, color=GREEN)))
        self.wait(2.5)
        b1d = Tex("Two equations, one answer — that is your proof").scale(0.95).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1d))
        self.wait(3)

        # --- Band 2 (subtopic_1): the graph rules ---
        self.next_band(2)
        b2t = Tex("Half the motion marks live in graphs").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = Tex("$x$-$t$ graph: gradient $=$ velocity").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2a))
        self.wait(2)
        b2b = Tex("$v$-$t$ graph: gradient $=$ $a$; area $=$ $\\Delta x$").scale(1.05).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2b))
        self.wait(2.5)
        b2c = MathTex(r"\text{Triangle: } \tfrac{1}{2} \times 5 \times 10 = 25 \text{ m}").scale(1.05).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2c))
        self.play(Create(SurroundingRectangle(b2c, color=GREEN)))
        self.wait(2.5)
        b2d = Tex("No $\\Delta x$: use $v = u + at$. No $t$: use $v^2$").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2d))
        self.wait(2)
        b2e = Tex("List the knowns; the equation chooses itself").scale(0.95).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2e))
        self.wait(3)

        # --- Band 3 (subtopic_2): the energy accounts ---
        self.next_band(3)
        b3t = Tex("Energy: the ledger that never lies").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = MathTex(r"E_p = mgh \qquad E_k = \tfrac{1}{2}mv^2").scale(1.1).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3a))
        self.wait(2.5)
        b3b = MathTex(r"E_{k1} + E_{p1} = E_{k2} + E_{p2}").scale(1.1).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3b))
        self.play(Create(SurroundingRectangle(b3b, color=GREEN)))
        self.wait(2.5)
        b3c = Tex("3 kg ball from 10 m, ground $=$ reference:").scale(1.0).shift(band_shift(3) + DOWN * 1.0)
        self.play(Write(b3c))
        self.wait(2)
        b3d = MathTex(r"E_p = 3 \times 9{,}8 \times 10 = 294 \text{ J, sealed}").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3d))
        self.wait(3)

        # --- Band 4 (subtopic_2): the three snapshots ---
        self.next_band(4)
        b4t = Tex("Three snapshots, one total").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        b4a = MathTex(r"\text{At 5 m: } 147 + 147, \; v^2 = 98").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4a))
        self.wait(2)
        b4b = MathTex(r"v = 9{,}90 \text{ m/s}").scale(1.1).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4b))
        self.wait(2)
        b4c = MathTex(r"\text{Ground: } v^2 = 196, \; v = 14 \text{ m/s}").scale(1.05).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4c))
        self.play(Create(SurroundingRectangle(b4c, color=GREEN)))
        self.wait(2.5)
        b4d = MathTex(r"v^2 = 2gh \quad \text{(mass cancels)}").scale(1.05).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4d))
        self.wait(2)
        b4e = Tex("`Ignore air resistance' is the licence — underline it").scale(0.9).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4e))
        self.wait(3)

        # --- Band 5 (subtopic_3): charge and its two rules ---
        self.next_band(5)
        b5t = Tex("Charge: two unbreakable rules").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = Tex("Conserved: never created or destroyed").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5a))
        self.wait(2)
        b5b = MathTex(r"\text{Quantised: multiples of } 1{,}6 \times 10^{-19} \text{ C}").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5b))
        self.wait(2.5)
        b5c = MathTex(r"Q = nq: \; n = \frac{8 \times 10^{-19}}{1{,}6 \times 10^{-19}} = 5").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5c))
        self.play(Create(SurroundingRectangle(b5c, color=GREEN)))
        self.wait(2.5)
        b5d = Tex("Five excess electrons — counted, not guessed").scale(0.95).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5d))
        self.wait(3)

        # --- Band 6 (subtopic_3): spheres, current, potential difference ---
        self.next_band(6)
        b6t = Tex("The identical spheres, and the flow").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = MathTex(r"+6 + (-2) = +4 \text{ nC} \Rightarrow +2 \text{ nC each}").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6a))
        self.play(Create(SurroundingRectangle(b6a, color=GREEN)))
        self.wait(2.5)
        b6b = MathTex(r"I = \frac{Q}{\Delta t} = \frac{12}{4} = 3 \text{ A}").scale(1.05).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6b))
        self.wait(2.5)
        b6c = MathTex(r"V = \frac{W}{Q} = \frac{24}{2} = 12 \text{ V}").scale(1.05).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6c))
        self.wait(2.5)
        b6d = Tex("Ammeter in SERIES; voltmeter in PARALLEL").scale(1.0).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6d))
        self.wait(3)

        # --- Band 7 (subtopic_4): the series circuit, drawn and solved ---
        self.next_band(7)
        b7t = Tex("Series: 12 V, then 4 $\\Omega$ and 8 $\\Omega$").scale(1.1).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7t))
        self.wait(2)
        # circuit loop from primitives
        c7 = band_shift(7) + UP * 0.3
        r1 = Rectangle(width=1.2, height=0.5).move_to(c7 + LEFT * 1.6 + UP * 1.0)
        r1l = MathTex(r"4\,\Omega").scale(0.8).move_to(c7 + LEFT * 1.6 + UP * 1.7)
        r2 = Rectangle(width=1.2, height=0.5).move_to(c7 + RIGHT * 1.6 + UP * 1.0)
        r2l = MathTex(r"8\,\Omega").scale(0.8).move_to(c7 + RIGHT * 1.6 + UP * 1.7)
        batt = Rectangle(width=1.2, height=0.5).move_to(c7 + DOWN * 1.0)
        battl = MathTex(r"12 \text{ V}").scale(0.8).move_to(c7 + DOWN * 1.7)
        w1 = Line(c7 + LEFT * 3.2 + UP * 1.0, c7 + LEFT * 2.2 + UP * 1.0, stroke_width=4)
        w2 = Line(c7 + LEFT * 1.0 + UP * 1.0, c7 + RIGHT * 1.0 + UP * 1.0, stroke_width=4)
        w3 = Line(c7 + RIGHT * 2.2 + UP * 1.0, c7 + RIGHT * 3.2 + UP * 1.0, stroke_width=4)
        w4 = Line(c7 + RIGHT * 3.2 + UP * 1.0, c7 + RIGHT * 3.2 + DOWN * 1.0, stroke_width=4)
        w5 = Line(c7 + RIGHT * 3.2 + DOWN * 1.0, c7 + RIGHT * 0.6 + DOWN * 1.0, stroke_width=4)
        w6 = Line(c7 + LEFT * 0.6 + DOWN * 1.0, c7 + LEFT * 3.2 + DOWN * 1.0, stroke_width=4)
        w7 = Line(c7 + LEFT * 3.2 + DOWN * 1.0, c7 + LEFT * 3.2 + UP * 1.0, stroke_width=4)
        self.play(Create(batt), Write(battl))
        self.play(Create(r1), Write(r1l), Create(r2), Write(r2l))
        self.play(Create(w1), Create(w2), Create(w3), Create(w4), Create(w5), Create(w6), Create(w7))
        self.wait(2)
        b7a = MathTex(r"R = 4 + 8 = 12\,\Omega, \quad I = \frac{12}{12} = 1 \text{ A}").scale(1.0).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7a))
        self.wait(2.5)
        b7b = MathTex(r"V: 4 + 8 = 12 \text{ V — audit closes}").scale(1.0).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(b7b))
        self.play(Create(SurroundingRectangle(b7b, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_4): parallel, same components ---
        self.next_band(8)
        b8t = Tex("Parallel: same parts, new numbers").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("Each branch feels the full 12 V").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8a))
        self.wait(2)
        b8b = MathTex(r"I: \frac{12}{4} = 3 \text{ A}, \;\; \frac{12}{8} = 1{,}5 \text{ A}").scale(1.05).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8b))
        self.wait(2.5)
        b8c = MathTex(r"I_{total} = 3 + 1{,}5 = 4{,}5 \text{ A}").scale(1.05).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8c))
        self.wait(2)
        b8d = MathTex(r"R = \frac{12}{4{,}5} = 2{,}67\,\Omega").scale(1.05).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8d))
        self.play(Create(SurroundingRectangle(b8d, color=GREEN)))
        self.wait(2)
        b8e = Tex("Always SMALLER than the smallest branch").scale(1.0).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8e))
        self.wait(3)

        # --- Band 9 (subtopic_4): magnetism in three facts ---
        self.next_band(9)
        b9t = Tex("Magnetism closes the year").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Two poles: like repel, unlike attract").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9a))
        self.wait(2)
        b9b = Tex("Field lines: N to S outside, never crossing").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9b))
        self.wait(2)
        b9c = Tex("Earth's field: why the compass settles north").scale(1.05).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9c))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 10 (subtopic_5): the three pictures ---
        self.next_band(10)
        b10t = Tex("Three pictures carry every method").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("Logbook: odometer $=$ distance; arrow $=$ displacement").scale(0.9).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10a))
        self.wait(2.5)
        b10b = Tex("Needle climbing 2 per second: 2, 4, 6, 8, 10").scale(0.95).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10b))
        self.wait(2.5)
        b10c = Tex("Wallet: $294 + 0 \\to 147 + 147 \\to 0 + 294$").scale(0.95).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10c))
        self.play(Create(SurroundingRectangle(b10c, color=GREEN)))
        self.wait(2.5)
        b10d = Tex("Pipes: pump $=$ battery, flow $=$ current").scale(0.95).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10d))
        self.wait(2)
        b10e = Tex("Charge circulates; energy is spent").scale(0.95).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10e))
        self.wait(3)

        # --- Band 11 (subtopic_6): series and parallel without tears ---
        self.next_band(11)
        b11t = Tex("Series and parallel without tears").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11t))
        self.wait(2)
        b11a = Tex("One loop: same flow; pressure bites add").scale(1.0).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11a))
        self.wait(2.5)
        b11b = Tex("Fork: full pressure each side; streams add").scale(1.0).shift(band_shift(11) + UP * 0.2)
        self.play(Write(b11b))
        self.wait(2.5)
        b11c = Tex("A second channel makes flow EASIER — smaller $R$").scale(0.95).shift(band_shift(11) + DOWN * 0.8)
        self.play(Write(b11c))
        self.play(Create(SurroundingRectangle(b11c, color=GREEN)))
        self.wait(2.5)
        b11d = Tex("Bulb added in series: both dim").scale(1.0).shift(band_shift(11) + DOWN * 1.8)
        self.play(Write(b11d))
        self.wait(2)
        b11e = Tex("Added in parallel: brightness holds, battery drains").scale(0.95).shift(band_shift(11) + DOWN * 2.7)
        self.play(Write(b11e))
        self.wait(3)

        # --- Band 12 (subtopic_7): the trap list and the final check ---
        self.next_band(12)
        b12t = Tex("The trap list and the final check").scale(1.15).shift(band_shift(12) + UP * 2.2)
        self.play(Write(b12t))
        self.wait(2)
        b12a = MathTex(r"g = 10: \; 294 \to 300 \text{ J}").scale(1.0).shift(band_shift(12) + UP * 1.2)
        self.play(Write(b12a))
        self.play(Create(strike(b12a)))
        self.wait(2)
        b12b = MathTex(r"\tfrac{1}{2} \times 3 \times 14^2 = 294 \text{ — say it aloud}").scale(0.95).shift(band_shift(12) + UP * 0.2)
        self.play(Write(b12b))
        self.wait(2.5)
        b12c = Tex("Junction? Parallel. No junction? Series").scale(1.0).shift(band_shift(12) + DOWN * 0.8)
        self.play(Write(b12c))
        self.wait(2)
        b12d = Tex("Ammeter: turnstile. Voltmeter: stands across").scale(0.95).shift(band_shift(12) + DOWN * 1.7)
        self.play(Write(b12d))
        self.wait(2)
        b12e = Tex("Check by a second route — the proof is free").scale(1.0).shift(band_shift(12) + DOWN * 2.7)
        self.play(Write(b12e))
        self.play(Create(SurroundingRectangle(b12e, color=GREEN)))
        self.wait(4)
