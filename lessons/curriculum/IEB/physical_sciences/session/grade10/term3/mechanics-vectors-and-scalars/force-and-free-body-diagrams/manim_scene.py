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

# Band-layout whiteboard scene for "Force and Free-Body Diagrams" (Part 1 —
# Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7). Exporter-safe
# mobjects only, add-only lifecycle; free-body diagrams hand-built arrow by
# arrow. Band time apportioned to subtopics.json
# (230/220/240/260/170/180/170 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ForceAndFreeBodyDiagramsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): a force is an interaction ---
        title = Tex("Force and Free-Body Diagrams").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("A force $=$ a push or a pull").scale(1.1).shift(UP * 0.8)
        self.play(Write(d1))
        self.wait(2)
        d2 = Tex("an INTERACTION between two objects").scale(1.05).shift(DOWN * 0.1)
        self.play(Write(d2))
        self.wait(2)
        d3 = Tex("No responsible object $\\Rightarrow$ no force").scale(1.05).shift(DOWN * 1.3)
        self.play(Write(d3))
        self.play(Create(SurroundingRectangle(d3, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): weight, and mass vs weight ---
        self.next_band(1)
        b1t = Tex("The Earth acts first: weight").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = MathTex(r"w = mg = 8 \times 9{,}8 = 78{,}4 \text{ N down}").scale(1.05).shift(band_shift(1) + UP * 1.0)
        self.play(Write(b1a))
        self.play(Create(SurroundingRectangle(b1a, color=GREEN)))
        self.wait(2.5)
        b1b = Tex("Mass: 8 kg of matter — scalar, same on the Moon").scale(0.95).shift(band_shift(1) + DOWN * 0.2)
        self.play(Write(b1b))
        self.wait(2.5)
        b1c = Tex("Weight: 78,4 N of force — vector, less on the Moon").scale(0.95).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1c))
        self.wait(2)
        b1d = Tex("kg for mass, N for weight").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1d))
        self.wait(3)

        # --- Band 2 (subtopic_1): the cast of four ---
        self.next_band(2)
        b2t = Tex("The cast around the box").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = Tex("Earth $\\to$ weight $w$, down").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2a))
        self.wait(2)
        b2b = Tex("Floor $\\to$ normal force $N$, perpendicular").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2b))
        self.wait(2)
        b2c = Tex("Strap $\\to$ applied force at 25$^\\circ$").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2c))
        self.wait(2)
        b2d = Tex("Rough floor $\\to$ friction $f$, backward").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2d))
        self.wait(2)
        b2e = Tex("`Force of motion'").scale(1.0).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2e))
        self.play(Create(strike(b2e)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the free-body diagram, arrow by arrow ---
        self.next_band(3)
        b3t = Tex("The free-body diagram: a dot, then arrows").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        c = band_shift(3) + DOWN * 0.4
        dot = Dot(c, radius=0.1)
        self.play(Create(dot))
        aw = Arrow(c, c + DOWN * 2.0, buff=0, color=BLUE, stroke_width=6)
        lw = MathTex(r"w = 78{,}4 \text{ N}").scale(0.85).move_to(c + DOWN * 2.3 + RIGHT * 1.4)
        self.play(Create(aw), Write(lw))
        self.wait(2)
        an = Arrow(c, c + UP * 1.6, buff=0, color=YELLOW, stroke_width=6)
        ln = MathTex(r"N").scale(0.95).move_to(c + UP * 1.9 + LEFT * 0.4)
        self.play(Create(an), Write(ln))
        self.wait(2)
        aa = Arrow(c, c + RIGHT * 2.2 + UP * 1.0, buff=0, color=GREEN, stroke_width=6)
        la = MathTex(r"F_{\text{applied}} \; (25^\circ)").scale(0.85).move_to(c + RIGHT * 3.1 + UP * 1.3)
        self.play(Create(aa), Write(la))
        self.wait(2)
        af = Arrow(c, c + LEFT * 1.8, buff=0, color=RED, stroke_width=6)
        lf = MathTex(r"f").scale(0.95).move_to(c + LEFT * 2.2 + UP * 0.4)
        self.play(Create(af), Write(lf))
        self.wait(3)

        # --- Band 4 (subtopic_2): the marker's quality rules ---
        self.next_band(4)
        b4t = Tex("Quality rules markers apply").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        b4a = Tex("Every arrow starts ON the dot, points away").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4a))
        self.wait(2)
        b4b = Tex("Arrowhead $+$ label on every force").scale(1.0).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4b))
        self.wait(2)
        b4c = Tex("Mark the 25$^\\circ$ angle against the horizontal").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4c))
        self.wait(2)
        b4d = Tex("No floor, no strap, no scenery").scale(1.0).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4d))
        self.wait(2)
        b4e = Tex("A velocity arrow among the forces").scale(1.0).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4e))
        self.play(Create(strike(b4e)))
        self.wait(3)

        # --- Band 5 (subtopic_3): constant velocity = balance ---
        self.next_band(5)
        b5t = Tex("`Constant velocity' $=$ zero net force").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = Tex("Newton I: balanced forces, unchanged motion").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5a))
        self.wait(2.5)
        b5b = MathTex(r"\text{Horizontal: } F\cos 25^\circ = f").scale(1.1).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5b))
        self.play(Create(SurroundingRectangle(b5b, color=GREEN)))
        self.wait(2.5)
        b5c = MathTex(r"\text{Vertical: } N + F\sin 25^\circ = w").scale(1.1).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5c))
        self.play(Create(SurroundingRectangle(b5c, color=GREEN)))
        self.wait(2.5)
        b5d = Tex("One slanted force, two jobs: components").scale(1.0).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(b5d))
        self.wait(3)

        # --- Band 6 (subtopic_3): the normal-force subtlety ---
        self.next_band(6)
        b6t = Tex("The subtlety: $N$ is NOT the weight here").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = MathTex(r"N = w - F\sin 25^\circ < 78{,}4 \text{ N}").scale(1.1).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6a))
        self.play(Create(SurroundingRectangle(b6a, color=GREEN)))
        self.wait(2.5)
        b6b = Tex("The strap carries part of the load").scale(1.05).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6b))
        self.wait(2.5)
        b6c = Tex("`$N$ always equals $w$'").scale(1.05).shift(band_shift(6) + DOWN * 1.0)
        self.play(Write(b6c))
        self.play(Create(strike(b6c)))
        self.wait(2)
        b6d = Tex("Less $N$ $\\to$ less friction $\\to$ easier dragging").scale(1.0).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6d))
        self.wait(3)

        # --- Band 7 (subtopic_4): the five-step method ---
        self.next_band(7)
        b7t = Tex("The method, five steps").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex("1. Isolate: forces ON one object only").scale(1.0).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7a))
        self.wait(2)
        b7b = Tex("2. Hunt: gravity first, then every toucher").scale(1.0).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7b))
        self.wait(2)
        b7c = Tex("3. Draw: dot, labelled arrows, angles").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7c))
        self.wait(2)
        b7d = Tex("4. Read the motion state").scale(1.0).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7d))
        self.wait(2)
        b7e = Tex("5. Write the balances, direction by direction").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7e))
        self.wait(3)

        # --- Band 8 (subtopic_4): the error museum ---
        self.next_band(8)
        b8t = Tex("The error museum").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("1. The phantom `force of motion'").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8a))
        self.play(Create(strike(b8a)))
        self.wait(2)
        b8b = Tex("2. Assuming $N = w$ without reading").scale(1.05).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex("3. Friction vs the pull, not vs the sliding").scale(1.05).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8c))
        self.wait(2)
        b8d = Tex("4. Floating, unlabelled, headless arrows").scale(1.05).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8d))
        self.wait(2)
        b8e = Tex("Only CHANGES of motion need force").scale(1.05).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8e))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 9 (subtopic_5): who is actually pulling on the box ---
        self.next_band(9)
        b9t = Tex("Who is actually pulling on the trommel?").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Earth: 78,4 N straight down").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9a))
        self.wait(2)
        b9b = Tex("Floor: pushes up, square to the surface").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9b))
        self.wait(2)
        b9c = Tex("Strap: forward and slightly up").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9c))
        self.wait(2)
        b9d = Tex("Roughness: rubs backward").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9d))
        self.wait(2)
        b9e = Tex("Can't name the culprit? Not a force.").scale(1.0).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9e))
        self.play(Create(SurroundingRectangle(b9e, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_6): a dot and four arrows, rebuilt ---
        self.next_band(10)
        b10t = Tex("A dot and four arrows").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        c2 = band_shift(10) + DOWN * 0.5
        dot2 = Dot(c2, radius=0.1)
        self.play(Create(dot2))
        self.wait(1)
        w2 = Arrow(c2, c2 + DOWN * 1.8, buff=0, color=BLUE, stroke_width=6)
        self.play(Create(w2))
        self.wait(1.5)
        n2 = Arrow(c2, c2 + UP * 1.4, buff=0, color=YELLOW, stroke_width=6)
        self.play(Create(n2))
        self.wait(1.5)
        a2 = Arrow(c2, c2 + RIGHT * 2.0 + UP * 0.9, buff=0, color=GREEN, stroke_width=6)
        self.play(Create(a2))
        self.wait(1.5)
        f2 = Arrow(c2, c2 + LEFT * 1.6, buff=0, color=RED, stroke_width=6)
        self.play(Create(f2))
        self.wait(2)
        b10a = Tex("Down, up, slanted forward, backwards").scale(1.0).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10a))
        self.wait(3)

        # --- Band 11 (subtopic_7): the slant and `constant speed' ---
        self.next_band(11)
        b11t = Tex("Why the slant helps").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11t))
        self.wait(2)
        b11a = Tex("Steady speed: nothing is winning").scale(1.05).shift(band_shift(11) + UP * 1.2)
        self.play(Write(b11a))
        self.wait(2)
        b11b = MathTex(r"F\cos 25^\circ = f \quad ; \quad N + F\sin 25^\circ = w").scale(1.0).shift(band_shift(11) + UP * 0.2)
        self.play(Write(b11b))
        self.wait(2.5)
        b11c = Tex("The strap carries a slice of the load").scale(1.05).shift(band_shift(11) + DOWN * 0.8)
        self.play(Write(b11c))
        self.wait(2)
        b11d = MathTex(r"N < 78{,}4 \text{ N}").scale(1.15).shift(band_shift(11) + DOWN * 1.7)
        self.play(Write(b11d))
        self.play(Create(SurroundingRectangle(b11d, color=GREEN)))
        self.wait(2)
        b11e = Tex("Less $N$, less friction — your arms knew").scale(1.0).shift(band_shift(11) + DOWN * 2.7)
        self.play(Write(b11e))
        self.wait(4)
