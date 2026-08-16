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

# Band-layout whiteboard scene for "Applying Conservation of Mechanical
# Energy" (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics
# 5-7). Exporter-safe mobjects only, add-only lifecycle, every worked example
# reproduced line by line with the script's numbers. Band time apportioned to
# subtopics.json (220/240/240/250/190/190/180 of 1510 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ApplyingConservationOfEnergySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the working tool ---
        title = Tex("Applying Conservation of Energy").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = MathTex(r"E_{k1} + E_{p1} = E_{k2} + E_{p2}").scale(1.3).shift(UP * 0.8)
        self.play(Write(d1))
        self.play(Create(SurroundingRectangle(d1, color=GREEN)))
        self.wait(2.5)
        d2 = Tex("...provided no friction or air resistance").scale(1.0).shift(DOWN * 0.4)
        self.play(Write(d2))
        self.wait(2)
        d3 = MathTex(r"E_p = mgh \qquad E_k = \tfrac{1}{2}mv^2").scale(1.15).shift(DOWN * 1.5)
        self.play(Write(d3))
        self.wait(3)

        # --- Band 1 (subtopic_1): the four moves and the zeros ---
        self.next_band(1)
        b1t = Tex("Four moves, and watch the zeros").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = Tex("1. Choose two points \\; 2. Zero at the lowest").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1a))
        self.wait(2)
        b1b = Tex("3. Write all four terms \\; 4. Solve the unknown").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1b))
        self.wait(2.5)
        b1c = Tex("Dropped: $E_k = 0$. \\; At the peak: $E_k = 0$").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1c))
        self.wait(2)
        b1d = Tex("At the reference level: $E_p = 0$").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1d))
        self.wait(2)
        b1e = Tex("Blind to time, acceleration and path").scale(1.0).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1e))
        self.wait(3)

        # --- Band 2 (subtopic_2): the vertical throw ---
        self.next_band(2)
        b2t = Tex("Throw: 15 m/s straight up — how high?").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = MathTex(r"\tfrac{1}{2}m(15)^2 = mgh").scale(1.1).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2a))
        self.wait(2)
        b2b = MathTex(r"112{,}5 = 9{,}8\,h \quad \text{(mass cancels)}").scale(1.1).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2b))
        self.wait(2)
        b2c = MathTex(r"h = 11{,}48 \text{ m}").scale(1.15).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2c))
        self.play(Create(SurroundingRectangle(b2c, color=GREEN)))
        self.wait(2.5)
        b2d = Tex("Mirror: falling 11,48 m lands at 15 m/s").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2d))
        self.wait(3)

        # --- Band 3 (subtopic_2): the pendulum ---
        self.next_band(3)
        b3t = Tex("Pendulum released 0,2 m up — speed below?").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = Tex("Curved arc: equations of motion are helpless").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3a))
        self.wait(2)
        b3b = MathTex(r"mg(0{,}2) = \tfrac{1}{2}mv^2").scale(1.1).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3b))
        self.wait(2)
        b3c = MathTex(r"v^2 = 2 \times 9{,}8 \times 0{,}2 = 3{,}92").scale(1.1).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3c))
        self.wait(2)
        b3d = MathTex(r"v = 1{,}98 \text{ m/s}").scale(1.15).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3d))
        self.play(Create(SurroundingRectangle(b3d, color=GREEN)))
        self.wait(2)
        b3e = Tex("Far side: rises to exactly 0,2 m — never more").scale(0.95).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3e))
        self.wait(3)

        # --- Band 4 (subtopic_3): the coaster — account at the top ---
        self.next_band(4)
        b4t = Tex("The coaster: 200 kg, 25 m hill, 3 m/s").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        b4a = Tex("Point 1 the crest; point 2 the bottom ($h = 0$)").scale(0.95).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4a))
        self.wait(2)
        b4b = MathTex(r"E_{k1} = \tfrac{1}{2} \times 200 \times 3^2 = 900 \text{ J}").scale(1.05).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4b))
        self.wait(2.5)
        b4c = MathTex(r"E_{p1} = 200 \times 9{,}8 \times 25 = 49\,000 \text{ J}").scale(1.05).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4c))
        self.wait(2.5)
        b4d = MathTex(r"E_{top} = 900 + 49\,000 = 49\,900 \text{ J}").scale(1.05).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4d))
        self.play(Create(SurroundingRectangle(b4d, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): solve at the bottom, and the trap ---
        self.next_band(5)
        b5t = Tex("At the bottom, all of it is kinetic").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = MathTex(r"\tfrac{1}{2} \times 200 \times v^2 = 49\,900").scale(1.1).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5a))
        self.wait(2)
        b5b = MathTex(r"100\,v^2 = 49\,900 \;\Rightarrow\; v^2 = 499").scale(1.1).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5b))
        self.wait(2)
        b5c = MathTex(r"v = 22{,}34 \text{ m/s} \; (\approx 80 \text{ km/h})").scale(1.1).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5c))
        self.play(Create(SurroundingRectangle(b5c, color=GREEN)))
        self.wait(2.5)
        b5d = MathTex(r"\text{Drop the } 900: v^2 = 490, \; v = 22{,}14").scale(1.0).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5d))
        self.play(Create(strike(b5d)))
        self.wait(2)
        b5e = Tex("Moving at the start: $E_{k1}$ is NOT zero").scale(1.0).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5e))
        self.wait(3)

        # --- Band 6 (subtopic_3): the halfway check ---
        self.next_band(6)
        b6t = Tex("Any point surrenders its speed: $h = 10$ m").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = MathTex(r"E_p = 200 \times 9{,}8 \times 10 = 19\,600 \text{ J}").scale(1.05).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6a))
        self.wait(2.5)
        b6b = MathTex(r"E_k = 49\,900 - 19\,600 = 30\,300 \text{ J}").scale(1.05).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6b))
        self.wait(2.5)
        b6c = MathTex(r"v^2 = 303 \;\Rightarrow\; v = 17{,}41 \text{ m/s}").scale(1.1).shift(band_shift(6) + DOWN * 1.0)
        self.play(Write(b6c))
        self.play(Create(SurroundingRectangle(b6c, color=GREEN)))
        self.wait(2)
        b6d = Tex("The ledger at full power").scale(1.0).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6d))
        self.wait(3)

        # --- Band 7 (subtopic_4): the incline and path independence ---
        self.next_band(7)
        b7t = Tex("Skateboard ramp: 5 m high, from rest").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = MathTex(r"mgh = \tfrac{1}{2}mv^2").scale(1.1).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7a))
        self.wait(2)
        b7b = MathTex(r"v^2 = 2 \times 9{,}8 \times 5 = 98").scale(1.1).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7b))
        self.wait(2)
        b7c = MathTex(r"v = 9{,}90 \text{ m/s}").scale(1.15).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7c))
        self.play(Create(SurroundingRectangle(b7c, color=GREEN)))
        self.wait(2.5)
        b7d = Tex("Cliff, gentle slope, curved bowl: identical").scale(1.0).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7d))
        self.wait(2)
        b7e = Tex("Only height and speed matter — never the path").scale(0.95).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7e))
        self.wait(3)

        # --- Band 8 (subtopic_4): the boundary of the tool ---
        self.next_band(8)
        b8t = Tex("Where the licence expires").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("Every later hill is lower: the budget was banked").scale(0.95).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8a))
        self.wait(2.5)
        b8b = Tex("Friction shrinks the account all ride long").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex("Friction or air resistance present:").scale(1.0).shift(band_shift(8) + DOWN * 0.8)
        b8d = MathTex(r"E_{k1} + E_{p1} = E_{k2} + E_{p2}").scale(1.05).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8c))
        self.play(Write(b8d))
        self.play(Create(strike(b8d)))
        self.wait(2)
        b8e = Tex("Then: say the energy decreased, and where it went").scale(0.9).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8e))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 9 (subtopic_5): the swing knows your height ---
        self.next_band(9)
        b9t = Tex("The swing knows your height").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Two kinds of money: height and speed").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9a))
        self.wait(2)
        b9b = Tex("Bottom of the arc: all speed — stomach drops").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9b))
        self.wait(2)
        b9c = Tex("Far side: same height as release. Never higher").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9c))
        self.play(Create(SurroundingRectangle(b9c, color=GREEN)))
        self.wait(2.5)
        b9d = MathTex(r"v = \sqrt{2 \times 9{,}8 \times 0{,}2} = 1{,}98 \text{ m/s}").scale(1.0).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9d))
        self.wait(2)
        b9e = Tex("The dying swing: air takes a tiny toll each pass").scale(0.95).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9e))
        self.wait(3)

        # --- Band 10 (subtopic_6): only the drop counts ---
        self.next_band(10)
        b10t = Tex("Only the drop counts").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("Steep ramp vs lazy slope, both 5 m: who wins?").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10a))
        self.wait(2.5)
        b10b = Tex("Neither: both arrive at 9,90 m/s").scale(1.05).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10b))
        self.play(Create(SurroundingRectangle(b10b, color=GREEN)))
        self.wait(2.5)
        b10c = Tex("Steeper means SOONER, not faster").scale(1.05).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10c))
        self.wait(2)
        b10d = MathTex(r"\text{Coaster: } 900 + 49\,000 = 49\,900 \text{ J}").scale(1.0).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10d))
        self.wait(2)
        b10e = Tex("The ledger counts every cent — keep the 900").scale(0.95).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10e))
        self.wait(3)

        # --- Band 11 (subtopic_7): why the second hill is lower ---
        self.next_band(11)
        b11t = Tex("Why the second hill is always lower").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11t))
        self.wait(2)
        b11a = Tex("Everything is paid for at the first crest").scale(1.0).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11a))
        self.wait(2)
        b11b = Tex("Real tracks rub: each hill shaved to fit").scale(1.0).shift(band_shift(11) + UP * 0.2)
        self.play(Write(b11b))
        self.wait(2)
        b11c = Tex("`Ignore friction and air resistance' is the seal").scale(0.95).shift(band_shift(11) + DOWN * 0.8)
        self.play(Write(b11c))
        self.play(Create(SurroundingRectangle(b11c, color=GREEN)))
        self.wait(2.5)
        b11d = Tex("Two snapshots, one unchanging total").scale(1.0).shift(band_shift(11) + DOWN * 1.8)
        self.play(Write(b11d))
        self.wait(2)
        b11e = Tex("Rubbing is the only thief — it steals to heat").scale(1.0).shift(band_shift(11) + DOWN * 2.7)
        self.play(Write(b11e))
        self.wait(4)
