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
        title = Tex("Physics Essentials — Revision Sweep").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Distance: scalar path. Displacement: vector arrow").scale(0.9).shift(UP * 1.0)
        self.play(Write(d1))
        self.wait(2.5)
        d2 = Tex("Speed vs velocity: the same split").scale(0.9).shift(UP * 0.1)
        self.play(Write(d2))
        self.wait(2)
        d3 = MathTex(r"a = \frac{\Delta v}{\Delta t}").scale(1.1).shift(DOWN * 1.0)
        self.play(Write(d3))
        self.play(Create(SurroundingRectangle(d3, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the minibus, three equations ---
        self.next_band(1)
        b1t = Tex("The minibus: rest, 3 m/s$^2$, 4 s").scale(1.1).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1t))
        self.wait(2)
        b1a = MathTex(r"v = u + at = 0 + 3 \times 4 = 12 \text{ m/s}").scale(0.95).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1a))
        self.wait(2.5)
        b1b = MathTex(r"\Delta x = ut + \tfrac{1}{2}at^2 = \tfrac{1}{2} \times 3 \times 16 = 24 \text{ m}").scale(0.95).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1b))
        self.wait(2.5)
        b1c = MathTex(r"v^2 = u^2 + 2a\Delta x = 2 \times 3 \times 24 = 144").scale(0.95).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1c))
        self.wait(2.5)
        b1d = Tex("$\\sqrt{144} = 12$ — two routes, one answer").scale(0.95).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1d))
        self.play(Create(SurroundingRectangle(b1d, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_1): the graph rules ---
        self.next_band(2)
        b2t = Tex("The graph rules").scale(1.2).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2t))
        self.wait(2)
        b2a = Tex("Position-time: gradient $=$ velocity").scale(0.95).shift(band_shift(2) + UP * 1.3)
        self.play(Write(b2a))
        self.wait(2.5)
        b2b = Tex("Velocity-time: gradient $=$ acceleration").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2b))
        self.wait(2)
        b2c = Tex("Velocity-time: AREA $=$ displacement").scale(0.95).shift(band_shift(2) + DOWN * 0.5)
        self.play(Write(b2c))
        self.wait(2)
        # triangle: v-t graph of the minibus
        ax1 = Line(band_shift(2) + DOWN * 2.8 + LEFT * 3.0, band_shift(2) + DOWN * 2.8 + RIGHT * 1.5)
        ax2 = Line(band_shift(2) + DOWN * 2.8 + LEFT * 3.0, band_shift(2) + DOWN * 1.2 + LEFT * 3.0)
        hyp = Line(band_shift(2) + DOWN * 2.8 + LEFT * 3.0, band_shift(2) + DOWN * 1.4 + RIGHT * 1.0)
        self.play(Create(ax1), Create(ax2), Create(hyp))
        self.wait(2)
        b2d = MathTex(r"\tfrac{1}{2} \times 4 \times 12 = 24 \text{ m}").scale(0.9).move_to(band_shift(2) + DOWN * 1.8 + RIGHT * 2.9)
        self.play(Write(b2d))
        self.wait(3)

        # --- Band 3 (subtopic_2): the energy accounts ---
        self.next_band(3)
        b3t = Tex("Energy: the ledger that never lies").scale(1.1).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3t))
        self.wait(2)
        b3a = MathTex(r"E_p = mgh \qquad E_k = \tfrac{1}{2}mv^2").scale(1.0).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3a))
        self.wait(2.5)
        b3b = MathTex(r"E_{k1} + E_{p1} = E_{k2} + E_{p2}").scale(1.1).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3b))
        self.play(Create(SurroundingRectangle(b3b, color=GREEN)))
        self.wait(2.5)
        b3c = Tex("Condition: no friction, no air resistance").scale(0.95).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3c))
        self.wait(2)
        b3d = Tex("g $=$ 9,8 m/s$^2$, written at the top, every time").scale(0.9).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3d))
        self.wait(3)

        # --- Band 4 (subtopic_2): the three snapshots ---
        self.next_band(4)
        b4t = Tex("A 5 kg ball from 8 m").scale(1.15).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4t))
        self.wait(2)
        b4a = MathTex(r"\text{Top: } E_p = 5 \times 9{,}8 \times 8 = 392 \text{ J}, \; E_k = 0").scale(0.9).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4a))
        self.wait(2.5)
        b4b = MathTex(r"\text{At 4 m: } 196 + 196, \; v^2 = 78{,}4, \; v = 8{,}85 \text{ m/s}").scale(0.9).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4b))
        self.wait(2.5)
        b4c = MathTex(r"\text{Ground: } 0 + 392, \; v^2 = 156{,}8, \; v = 12{,}52 \text{ m/s}").scale(0.9).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4c))
        self.play(Create(SurroundingRectangle(b4c, color=GREEN)))
        self.wait(2.5)
        b4d = MathTex(r"\tfrac{1}{2}mv^2 = mgh \Rightarrow v^2 = 2gh \text{ — mass cancels}").scale(0.9).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4d))
        self.wait(3)

        # --- Band 5 (subtopic_3): charge and its two rules ---
        self.next_band(5)
        b5t = Tex("Charge: two unbreakable rules").scale(1.1).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5t))
        self.wait(2)
        b5a = Tex("Conserved: never created, never destroyed").scale(0.95).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5a))
        self.wait(2.5)
        b5b = MathTex(r"\text{Quantised: } Q = nq, \; q = 1{,}6 \times 10^{-19} \text{ C}").scale(0.9).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5b))
        self.wait(2.5)
        b5c = MathTex(r"-4{,}8 \times 10^{-19} \text{ C} \Rightarrow \frac{4{,}8}{1{,}6} = 3 \text{ electrons}").scale(0.9).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5c))
        self.play(Create(SurroundingRectangle(b5c, color=GREEN)))
        self.wait(2.5)
        b5d = Tex("Always a whole number — charge has no fractions").scale(0.9).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5d))
        self.wait(3)

        # --- Band 6 (subtopic_3): spheres, current, potential difference ---
        self.next_band(6)
        b6t = Tex("Spheres, current, potential difference").scale(1.05).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6t))
        self.wait(2)
        b6a = MathTex(r"+8 \text{ nC and } -2 \text{ nC} \to \text{total } +6 \to +3 \text{ nC each}").scale(0.85).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6a))
        self.wait(2.5)
        b6b = MathTex(r"I = \frac{Q}{\Delta t} = \frac{20}{5} = 4 \text{ A}").scale(0.95).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6b))
        self.wait(2.5)
        b6c = MathTex(r"V = \frac{W}{Q} = \frac{30}{2} = 15 \text{ V}").scale(0.95).shift(band_shift(6) + DOWN * 1.0)
        self.play(Write(b6c))
        self.wait(2.5)
        b6d = Tex("Ammeter in series; voltmeter in parallel").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6d))
        self.play(Create(SurroundingRectangle(b6d, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the series circuit, drawn and solved ---
        self.next_band(7)
        b7t = Tex("Series: 18 V, 3 $\\Omega$ and 6 $\\Omega$").scale(1.05).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7t))
        self.wait(2)
        # simple loop: battery left, two resistors on top, wires
        wl = Line(band_shift(7) + DOWN * 1.8 + LEFT * 3.4, band_shift(7) + UP * 1.4 + LEFT * 3.4, stroke_width=4)
        batt = Rectangle(width=0.5, height=1.0).shift(band_shift(7) + DOWN * 0.2 + LEFT * 3.4)
        wt = Line(band_shift(7) + UP * 1.4 + LEFT * 3.4, band_shift(7) + UP * 1.4 + LEFT * 1.6, stroke_width=4)
        r1 = Rectangle(width=1.4, height=0.6).shift(band_shift(7) + UP * 1.4 + LEFT * 0.9)
        r1l = Tex("3 $\\Omega$").scale(0.7).move_to(band_shift(7) + UP * 2.1 + LEFT * 0.9)
        wm = Line(band_shift(7) + UP * 1.4 + LEFT * 0.2, band_shift(7) + UP * 1.4 + RIGHT * 0.8, stroke_width=4)
        r2 = Rectangle(width=1.4, height=0.6).shift(band_shift(7) + UP * 1.4 + RIGHT * 1.5)
        r2l = Tex("6 $\\Omega$").scale(0.7).move_to(band_shift(7) + UP * 2.1 + RIGHT * 1.5)
        wr = Line(band_shift(7) + UP * 1.4 + RIGHT * 2.2, band_shift(7) + UP * 1.4 + RIGHT * 3.4, stroke_width=4)
        wr2 = Line(band_shift(7) + UP * 1.4 + RIGHT * 3.4, band_shift(7) + DOWN * 1.8 + RIGHT * 3.4, stroke_width=4)
        wb = Line(band_shift(7) + DOWN * 1.8 + RIGHT * 3.4, band_shift(7) + DOWN * 1.8 + LEFT * 3.4, stroke_width=4)
        self.play(Create(wl), Create(batt), Create(wt))
        self.play(Create(r1), Write(r1l), Create(wm), Create(r2), Write(r2l))
        self.play(Create(wr), Create(wr2), Create(wb))
        self.wait(2.5)
        b7a = MathTex(r"R = 9\,\Omega, \; I = \frac{18}{9} = 2 \text{ A}").scale(0.9).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(b7a))
        self.wait(2.5)
        b7b = Tex("V's: 6 V and 12 V — and $6+12=18$: audit").scale(0.85).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7b))
        self.play(Create(SurroundingRectangle(b7b, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_4): parallel, same components ---
        self.next_band(8)
        b8t = Tex("Parallel: same parts, new numbers").scale(1.1).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("Each branch feels the full 18 V").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8a))
        self.wait(2.5)
        b8b = MathTex(r"I_1 = \frac{18}{3} = 6 \text{ A}, \quad I_2 = \frac{18}{6} = 3 \text{ A}").scale(0.9).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8b))
        self.wait(2.5)
        b8c = MathTex(r"I = 9 \text{ A}, \quad R = \frac{18}{9} = 2\,\Omega").scale(0.95).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8c))
        self.play(Create(SurroundingRectangle(b8c, color=GREEN)))
        self.wait(2.5)
        b8d = Tex("Always smaller than the smallest branch").scale(0.9).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8d))
        self.wait(3)

        # --- Band 9 (subtopic_4): magnetism in three facts ---
        self.next_band(9)
        b9t = Tex("Magnetism in three facts").scale(1.15).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Two poles: like repel, unlike attract").scale(0.95).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9a))
        self.wait(2.5)
        b9b = Tex("Field lines: north to south, never crossing").scale(0.95).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = Tex("The Earth is a magnet — the compass answers it").scale(0.95).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9c))
        self.play(Create(SurroundingRectangle(b9c, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 10 (subtopic_5): the three pictures ---
        self.next_band(10)
        b10t = Tex("Three pictures carry the year").scale(1.15).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("LOGBOOK: odometer distance, arrow displacement").scale(0.85).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10a))
        self.wait(2.5)
        b10b = Tex("WALLET: 392 $\\to$ 196$+$196 $\\to$ 0$+$392").scale(0.9).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10b))
        self.wait(2.5)
        b10c = Tex("PIPES: pump, flow, narrow sections, pressure drops").scale(0.85).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10c))
        self.wait(2.5)
        b10d = Tex("Charge circulates; energy is spent").scale(0.95).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10d))
        self.play(Create(SurroundingRectangle(b10d, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_6): series and parallel without tears ---
        self.next_band(11)
        b11t = Tex("Series and parallel without tears").scale(1.1).shift(band_shift(11) + UP * 2.3)
        self.play(Write(b11t))
        self.wait(2)
        b11a = Tex("One loop: same flow, pressure bites add").scale(0.9).shift(band_shift(11) + UP * 1.2)
        self.play(Write(b11a))
        self.wait(2.5)
        b11b = Tex("Fork: full pressure each branch, flows add").scale(0.9).shift(band_shift(11) + UP * 0.3)
        self.play(Write(b11b))
        self.wait(2.5)
        b11c = Tex("Second channel opens: total resistance FALLS").scale(0.9).shift(band_shift(11) + DOWN * 0.6)
        self.play(Write(b11c))
        self.wait(2.5)
        b11d = Tex("Bulb in series added: both dim").scale(0.9).shift(band_shift(11) + DOWN * 1.5)
        self.play(Write(b11d))
        self.wait(2)
        b11e = Tex("Bulb in parallel added: brightness holds, battery drains").scale(0.85).shift(band_shift(11) + DOWN * 2.4)
        self.play(Write(b11e))
        self.wait(3)

        # --- Band 12 (subtopic_7): the trap list and the final check ---
        self.next_band(12)
        b12t = Tex("The trap list and the final check").scale(1.1).shift(band_shift(12) + UP * 2.3)
        self.play(Write(b12t))
        self.wait(2)
        b12a = Tex("g $=$ 10").scale(0.95).shift(band_shift(12) + UP * 1.3 + LEFT * 3.0)
        self.play(Write(b12a))
        self.play(Create(strike(b12a)))
        self.wait(2)
        b12b = Tex("Unsquared speed; dropped half").scale(0.85).shift(band_shift(12) + UP * 1.3 + RIGHT * 1.5)
        self.play(Write(b12b))
        self.wait(2)
        b12c = Tex("Junction? — the one circuit question").scale(0.9).shift(band_shift(12) + UP * 0.3)
        self.play(Write(b12c))
        self.wait(2)
        b12d = Tex("Scalar or vector — label before answering").scale(0.9).shift(band_shift(12) + DOWN * 0.6)
        self.play(Write(b12d))
        self.wait(2)
        b12e = Tex("Ammeter through; voltmeter across").scale(0.9).shift(band_shift(12) + DOWN * 1.5)
        self.play(Write(b12e))
        self.wait(2)
        b12f = Tex("Check every answer by its second route").scale(0.95).shift(band_shift(12) + DOWN * 2.5)
        self.play(Write(b12f))
        self.play(Create(SurroundingRectangle(b12f, color=GREEN)))
        self.wait(4)
