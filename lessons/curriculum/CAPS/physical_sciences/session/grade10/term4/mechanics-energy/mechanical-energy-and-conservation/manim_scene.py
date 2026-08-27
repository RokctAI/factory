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
        title = Tex("Mechanical Energy and Conservation").scale(1.2).to_edge(UP)
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
        d4 = Tex("Both in joules; both scalars — no direction").scale(1.0).shift(DOWN * 1.8)
        self.play(Write(d4))
        self.wait(3)

        # --- Band 1 (subtopic_1): the ball on the roof ---
        self.next_band(1)
        b1t = Tex("2 kg ball, at rest, 20 m up").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = MathTex(r"E_p = 2 \times 9{,}8 \times 20 = 392 \text{ J}").scale(1.1).shift(band_shift(1) + UP * 1.0)
        self.play(Write(b1a))
        self.wait(2.5)
        b1b = MathTex(r"E_k = 0 \quad \text{(at rest)}").scale(1.1).shift(band_shift(1) + UP * 0.0)
        self.play(Write(b1b))
        self.wait(2)
        b1c = MathTex(r"E_M = 0 + 392 = 392 \text{ J}").scale(1.15).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(b1c))
        self.play(Create(SurroundingRectangle(b1c, color=GREEN)))
        self.wait(2.5)
        b1d = Tex("Reference chosen: the ground, $h = 0$").scale(1.0).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1d))
        self.wait(2)
        b1e = Tex("Once chosen, it holds for the whole problem").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1e))
        self.wait(3)

        # --- Band 2 (subtopic_2): the law and its special case ---
        self.next_band(2)
        b2t = Tex("The law of conservation of energy").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = Tex("Energy is never created or destroyed —").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2b = Tex("only transferred or converted").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2a))
        self.play(Write(b2b))
        self.wait(2.5)
        b2c = Tex("No friction, no air resistance:").scale(1.0).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2c))
        self.wait(1.5)
        b2d = MathTex(r"E_{k1} + E_{p1} = E_{k2} + E_{p2}").scale(1.2).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(b2d))
        self.play(Create(SurroundingRectangle(b2d, color=GREEN)))
        self.wait(2.5)
        b2e = Tex("Each account trades; the SUM stands still").scale(1.0).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2e))
        self.wait(3)

        # --- Band 3 (subtopic_2): the fine print ---
        self.next_band(3)
        b3t = Tex("The fine print").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = Tex("With friction: mechanical energy leaks").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3a))
        self.wait(2)
        b3b = Tex("...as heat and sound — but TOTAL energy holds").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3b))
        self.wait(2.5)
        b3c = Tex("`Ignore air resistance', `frictionless'").scale(1.05).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3c))
        self.wait(2)
        b3d = Tex("— that phrase is your licence. Underline it").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3d))
        self.play(Create(SurroundingRectangle(b3d, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): halfway down ---
        self.next_band(4)
        b4t = Tex("The ledger halfway down: $h = 10$ m").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        b4a = MathTex(r"E_p = 2 \times 9{,}8 \times 10 = 196 \text{ J}").scale(1.1).shift(band_shift(4) + UP * 1.0)
        self.play(Write(b4a))
        self.wait(2.5)
        b4b = MathTex(r"E_k = 392 - 196 = 196 \text{ J}").scale(1.1).shift(band_shift(4) + UP * 0.0)
        self.play(Write(b4b))
        self.wait(2.5)
        b4c = MathTex(r"\tfrac{1}{2} \times 2 \times v^2 = 196 \;\Rightarrow\; v^2 = 196").scale(1.05).shift(band_shift(4) + DOWN * 1.0)
        self.play(Write(b4c))
        self.wait(2)
        b4d = MathTex(r"v = 14 \text{ m/s}").scale(1.15).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4d))
        self.play(Create(SurroundingRectangle(b4d, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the ground, and the audit line ---
        self.next_band(5)
        b5t = Tex("The instant before the ground").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = MathTex(r"E_p = 0, \quad E_k = 392 \text{ J}").scale(1.1).shift(band_shift(5) + UP * 1.0)
        self.play(Write(b5a))
        self.wait(2)
        b5b = MathTex(r"\tfrac{1}{2} \times 2 \times v^2 = 392 \;\Rightarrow\; v^2 = 392").scale(1.05).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5b))
        self.wait(2)
        b5c = MathTex(r"v = 19{,}80 \text{ m/s}").scale(1.15).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5c))
        self.play(Create(SurroundingRectangle(b5c, color=GREEN)))
        self.wait(2.5)
        b5d = MathTex(r"392 + 0 \;\to\; 196 + 196 \;\to\; 0 + 392").scale(1.0).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5d))
        self.wait(2)
        b5e = Tex("Three snapshots, one unchanging total").scale(1.0).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5e))
        self.wait(3)

        # --- Band 6 (subtopic_3): the mass cancels ---
        self.next_band(6)
        b6t = Tex("Why the mass never mattered").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = MathTex(r"\tfrac{1}{2}mv^2 = mgh").scale(1.15).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6a))
        self.wait(2)
        b6b = MathTex(r"v^2 = 2gh \quad \text{(mass cancels)}").scale(1.1).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6b))
        self.play(Create(SurroundingRectangle(b6b, color=GREEN)))
        self.wait(2.5)
        b6c = Tex("2 kg or 5 kg: both land at 19,80 m/s").scale(1.05).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6c))
        self.wait(2)
        b6d = Tex("More energy carried, more needed — exact cancel").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6d))
        self.wait(3)

        # --- Band 7 (subtopic_4): the four steps ---
        self.next_band(7)
        b7t = Tex("The method, four steps").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex("1. Confirm the licence — no dissipation").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7a))
        self.wait(2)
        b7b = Tex("2. Declare the reference: lowest point, $h = 0$").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7b))
        self.wait(2)
        b7c = Tex("3. Fill every term; write the zeros explicitly").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7c))
        self.wait(2)
        b7d = Tex("4. Solve, and attach the unit").scale(1.05).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7d))
        self.wait(3)

        # --- Band 8 (subtopic_4): the traps ---
        self.next_band(8)
        b8t = Tex("The traps, named").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = MathTex(r"g = 10: \; 392 \to 400 \text{ J}").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8a))
        self.play(Create(strike(b8a)))
        self.wait(2)
        b8b = Tex("CAPS uses $g = 9{,}8$ m/s$^2$").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8b))
        self.wait(2)
        b8c = MathTex(r"\tfrac{1}{2} \times 2 \times 14 = 28 \text{ J}").scale(1.05).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8c))
        self.play(Create(strike(b8c)))
        self.wait(2)
        b8d = MathTex(r"\tfrac{1}{2} \times 2 \times 14^2 = 196 \text{ J}").scale(1.05).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8d))
        self.play(Create(SurroundingRectangle(b8d, color=GREEN)))
        self.wait(2)
        b8e = Tex("One reference point; no directions on energy").scale(0.95).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8e))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 9 (subtopic_5): the two-pocket wallet ---
        self.next_band(9)
        b9t = Tex("The two-pocket wallet").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Height pocket: $mgh$ — filled by climbing").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9a))
        self.wait(2)
        b9b = Tex("Speed pocket: $\\tfrac{1}{2}mv^2$ — filled by hurrying").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = Tex("No rubbing $=$ sealed wallet: total never budges").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9c))
        self.play(Create(SurroundingRectangle(b9c, color=GREEN)))
        self.wait(2.5)
        b9d = Tex("You choose the floor — then never change it").scale(1.0).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9d))
        self.wait(3)

        # --- Band 10 (subtopic_6): counting the ball's money ---
        self.next_band(10)
        b10t = Tex("Counting the ball's money").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = MathTex(r"\text{Top: } 392 + 0 = 392 \text{ J, sealed}").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10a))
        self.wait(2.5)
        b10b = MathTex(r"\text{Halfway: } 196 + 196, \; v = 14 \text{ m/s}").scale(1.05).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10b))
        self.wait(2.5)
        b10c = MathTex(r"\text{Ground: } 0 + 392, \; v = 19{,}80 \text{ m/s}").scale(1.05).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10c))
        self.play(Create(SurroundingRectangle(b10c, color=GREEN)))
        self.wait(2.5)
        b10d = Tex("About 71 km/h — stay out from under rooftops").scale(0.95).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(b10d))
        self.wait(2)
        b10e = Tex("Pockets must always add to the sealed total").scale(0.95).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10e))
        self.wait(3)

        # --- Band 11 (subtopic_7): where the money leaks ---
        self.next_band(11)
        b11t = Tex("Where the money leaks").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11t))
        self.wait(2)
        b11a = Tex("Heavier ball: richer wallet, pricier speed").scale(1.05).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11a))
        self.wait(2)
        b11b = Tex("The two cancel to the cent — same 19,80 m/s").scale(1.0).shift(band_shift(11) + UP * 0.2)
        self.play(Write(b11b))
        self.wait(2.5)
        b11c = Tex("Rubbing springs a leak: joules go to heat").scale(1.0).shift(band_shift(11) + DOWN * 0.8)
        self.play(Write(b11c))
        self.wait(2)
        b11d = Tex("Feel a brake rim: that is the speed money").scale(1.0).shift(band_shift(11) + DOWN * 1.7)
        self.play(Write(b11d))
        self.wait(2)
        b11e = Tex("Leaked from the wallet — never from the universe").scale(0.95).shift(band_shift(11) + DOWN * 2.7)
        self.play(Write(b11e))
        self.play(Create(SurroundingRectangle(b11e, color=GREEN)))
        self.wait(4)
