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

# Band-layout whiteboard scene for "Mechanical Energy and Conservation"
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7).
# Exporter-safe mobjects only, add-only lifecycle, the rooftop ball worked
# with the script's exact numbers at every position. Band time apportioned to
# subtopics.json (220/230/240/260/180/190/180 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MechanicalEnergyConservationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): two accounts, one total ---
        title = Tex("Mechanical Energy and Conservation").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = MathTex(r"E_p = mgh").scale(1.2).shift(UP * 0.9 + LEFT * 2.5)
        d2 = MathTex(r"E_k = \tfrac{1}{2}mv^2").scale(1.2).shift(UP * 0.9 + RIGHT * 2.5)
        self.play(Write(d1))
        self.play(Write(d2))
        self.wait(2.5)
        d3 = MathTex(r"E_M = E_k + E_p").scale(1.3).shift(DOWN * 0.5)
        self.play(Write(d3))
        self.play(Create(SurroundingRectangle(d3, color=GREEN)))
        self.wait(2.5)
        d4 = Tex("Joules; scalars — size only, no direction").scale(0.95).shift(DOWN * 1.8)
        self.play(Write(d4))
        self.wait(2)
        d5 = Tex("g $=$ 9,8 m/s$^2$ — every time").scale(0.95).shift(DOWN * 2.7)
        self.play(Write(d5))
        self.wait(3)

        # --- Band 1 (subtopic_1): the ball on the roof ---
        self.next_band(1)
        b1t = Tex("A 4 kg ball, 15 m up, at rest").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = MathTex(r"E_p = 4 \times 9{,}8 \times 15 = 588 \text{ J}").scale(1.1).shift(band_shift(1) + UP * 1.0)
        self.play(Write(b1a))
        self.wait(2.5)
        b1b = MathTex(r"E_k = 0 \quad \text{at rest}").scale(1.1).shift(band_shift(1) + UP * 0.0)
        self.play(Write(b1b))
        self.wait(2)
        b1c = MathTex(r"E_M = 0 + 588 = 588 \text{ J}").scale(1.15).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(b1c))
        self.play(Create(SurroundingRectangle(b1c, color=GREEN)))
        self.wait(2.5)
        b1d = Tex("Reference chosen: the ground, $h = 0$").scale(0.95).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1d))
        self.wait(2)
        b1e = Tex("Once chosen, the reference holds all problem long").scale(0.9).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1e))
        self.wait(3)

        # --- Band 2 (subtopic_2): the law and its special case ---
        self.next_band(2)
        b2t = Tex("The law, then the special case").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = Tex("Energy: never created, never destroyed —").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2b = Tex("only transferred or converted").scale(1.0).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2a))
        self.play(Write(b2b))
        self.wait(2.5)
        b2c = Tex("No friction, no air resistance $\\Rightarrow$ $E_M$ constant").scale(0.95).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2c))
        self.wait(2.5)
        b2d = MathTex(r"E_{k1} + E_{p1} = E_{k2} + E_{p2}").scale(1.2).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2d))
        self.play(Create(SurroundingRectangle(b2d, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the fine print ---
        self.next_band(3)
        b3t = Tex("What the principle does and does not claim").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = Tex("$E_p$ stays fixed during the fall").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3a))
        self.play(Create(strike(b3a)))
        self.wait(2)
        b3b = Tex("The SUM stays fixed — accounts trade, total stands").scale(0.95).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3b))
        self.wait(2.5)
        b3c = Tex("Friction present: $E_M$ leaks to heat and sound").scale(0.95).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3c))
        self.wait(2.5)
        b3d = Tex("`Ignore air resistance' $=$ your licence — underline it").scale(0.9).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3d))
        self.play(Create(SurroundingRectangle(b3d, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): halfway down ---
        self.next_band(4)
        b4t = Tex("Halfway down: 7,5 m").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        b4a = MathTex(r"E_p = 4 \times 9{,}8 \times 7{,}5 = 294 \text{ J}").scale(1.05).shift(band_shift(4) + UP * 1.0)
        self.play(Write(b4a))
        self.wait(2.5)
        b4b = MathTex(r"E_k = 588 - 294 = 294 \text{ J}").scale(1.05).shift(band_shift(4) + UP * 0.0)
        self.play(Write(b4b))
        self.wait(2.5)
        b4c = MathTex(r"\tfrac{1}{2} \times 4 \times v^2 = 294 \;\Rightarrow\; v^2 = 147").scale(1.0).shift(band_shift(4) + DOWN * 1.0)
        self.play(Write(b4c))
        self.wait(2.5)
        b4d = MathTex(r"v = 12{,}12 \text{ m/s}").scale(1.15).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4d))
        self.play(Create(SurroundingRectangle(b4d, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the ground, and the audit line ---
        self.next_band(5)
        b5t = Tex("The instant before the ground").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = MathTex(r"E_p = 0, \quad E_k = 588 \text{ J}").scale(1.05).shift(band_shift(5) + UP * 1.0)
        self.play(Write(b5a))
        self.wait(2.5)
        b5b = MathTex(r"\tfrac{1}{2} \times 4 \times v^2 = 588 \;\Rightarrow\; v^2 = 294").scale(1.0).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5b))
        self.wait(2.5)
        b5c = MathTex(r"v = 17{,}15 \text{ m/s}").scale(1.15).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5c))
        self.play(Create(SurroundingRectangle(b5c, color=GREEN)))
        self.wait(2.5)
        b5d = Tex("Audit: $588+0$; \\; $294+294$; \\; $0+588$").scale(1.0).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5d))
        self.wait(3)

        # --- Band 6 (subtopic_3): the mass cancels ---
        self.next_band(6)
        b6t = Tex("Why mass never mattered").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = MathTex(r"\tfrac{1}{2}mv^2 = mgh").scale(1.1).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6a))
        self.wait(2.5)
        b6b = MathTex(r"v^2 = 2gh").scale(1.2).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6b))
        self.play(Create(SurroundingRectangle(b6b, color=GREEN)))
        self.wait(2.5)
        b6c = Tex("4 kg ball or 40 kg toolbox: both land at 17,15 m/s").scale(0.95).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6c))
        self.wait(2.5)
        b6d = Tex("More energy carried, more energy needed — exact cancel").scale(0.9).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6d))
        self.wait(3)

        # --- Band 7 (subtopic_4): the four steps ---
        self.next_band(7)
        b7t = Tex("The method in four steps").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex("1. Check the licence: no friction, no air resistance").scale(0.9).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7a))
        self.wait(2)
        b7b = Tex("2. Choose and declare the $h=0$ reference").scale(0.9).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7b))
        self.wait(2)
        b7c = Tex("3. Write all four terms — zeros explicitly").scale(0.9).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7c))
        self.wait(2)
        b7d = Tex("4. Solve the lone unknown; attach the unit").scale(0.9).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7d))
        self.wait(2)
        b7e = Tex("J for energies; m/s for speeds").scale(0.9).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7e))
        self.wait(3)

        # --- Band 8 (subtopic_4): the traps ---
        self.next_band(8)
        b8t = Tex("The five traps").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("g $=$ 10 by habit: 588 J corrupts to 600").scale(0.9).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8a))
        self.wait(2)
        b8b = Tex("Unsquared speed, or the half dropped").scale(0.9).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex("Reference point switched mid-problem").scale(0.9).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8c))
        self.wait(2)
        b8d = Tex("Conservation applied on a rough surface").scale(0.9).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8d))
        self.wait(2)
        b8e = Tex("Energy given a direction").scale(0.9).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8e))
        self.play(Create(strike(b8e)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 9 (subtopic_5): the two-pocket wallet ---
        self.next_band(9)
        b9t = Tex("The two-pocket wallet").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        p1 = Rectangle(width=2.6, height=1.4).shift(band_shift(9) + UP * 0.7 + LEFT * 2.0)
        p1l = Tex("HEIGHT: $mgh$").scale(0.8).move_to(band_shift(9) + UP * 0.7 + LEFT * 2.0)
        p2 = Rectangle(width=2.6, height=1.4).shift(band_shift(9) + UP * 0.7 + RIGHT * 2.0)
        p2l = Tex("SPEED: $\\tfrac{1}{2}mv^2$").scale(0.8).move_to(band_shift(9) + UP * 0.7 + RIGHT * 2.0)
        self.play(Create(p1), Write(p1l))
        self.play(Create(p2), Write(p2l))
        self.wait(2.5)
        b9a = Tex("No rubbing $\\Rightarrow$ the wallet is SEALED").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9a))
        self.play(Create(SurroundingRectangle(b9a, color=GREEN)))
        self.wait(2.5)
        b9b = Tex("Coins move between pockets; the total never budges").scale(0.9).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9b))
        self.wait(2)
        b9c = Tex("You choose the floor where $h = 0$ — once").scale(0.9).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9c))
        self.wait(3)

        # --- Band 10 (subtopic_6): counting the ball's money ---
        self.next_band(10)
        b10t = Tex("Counting the ball's money").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = MathTex(r"\text{Top: } 588 + 0 = 588 \text{ J}").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10a))
        self.wait(2.5)
        b10b = MathTex(r"\text{Halfway: } 294 + 294, \; v = 12{,}12 \text{ m/s}").scale(1.0).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10b))
        self.wait(2.5)
        b10c = MathTex(r"\text{Ground: } 0 + 588, \; v = 17{,}15 \text{ m/s}").scale(1.0).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10c))
        self.play(Create(SurroundingRectangle(b10c, color=GREEN)))
        self.wait(2.5)
        b10d = Tex("About 62 km/h — respect rooftops").scale(0.95).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(b10d))
        self.wait(2)
        b10e = Tex("Pockets must always add to the sealed total").scale(0.9).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10e))
        self.wait(3)

        # --- Band 11 (subtopic_7): where the money leaks ---
        self.next_band(11)
        b11t = Tex("Where the money leaks").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11t))
        self.wait(2)
        b11a = Tex("Heavier: richer wallet AND pricier speed").scale(0.95).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11a))
        self.wait(2)
        b11b = Tex("The two cancel exactly — same 17,15 m/s").scale(0.95).shift(band_shift(11) + UP * 0.2)
        self.play(Write(b11b))
        self.wait(2.5)
        b11c = Tex("Rubbing springs a leak: joules leave as heat").scale(0.95).shift(band_shift(11) + DOWN * 0.8)
        self.play(Write(b11c))
        self.wait(2.5)
        b11d = Tex("Leaked joules destroyed").scale(0.95).shift(band_shift(11) + DOWN * 1.7)
        self.play(Write(b11d))
        self.play(Create(strike(b11d)))
        self.wait(2)
        b11e = Tex("Out of the wallet — never out of the universe").scale(0.95).shift(band_shift(11) + DOWN * 2.7)
        self.play(Write(b11e))
        self.play(Create(SurroundingRectangle(b11e, color=GREEN)))
        self.wait(4)
