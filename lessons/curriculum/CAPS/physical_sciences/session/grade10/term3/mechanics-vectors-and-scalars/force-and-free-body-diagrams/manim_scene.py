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

# Band-layout whiteboard scene for "Force and Free-Body Diagrams" (Part 1 —
# Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7). Exporter-safe
# mobjects only (Tex/MathTex/Line/Arrow/Dot/DashedLine/SurroundingRectangle),
# add-only lifecycle; free-body diagrams hand-built arrow by arrow. Band time
# apportioned to subtopics.json (230/220/240/260/170/180/170 of 1470 s).

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
        title = Tex("Force and Free-Body Diagrams").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("A force is a push or a pull —").scale(1.1).shift(UP * 0.9)
        d2 = Tex("an interaction between TWO objects").scale(1.1).shift(UP * 0.0)
        self.play(Write(d1))
        self.play(Write(d2))
        self.wait(2.5)
        d3 = Tex("No responsible object $=$ no force").scale(1.1).shift(DOWN * 1.2)
        self.play(Write(d3))
        self.play(Create(SurroundingRectangle(d3, color=GREEN)))
        self.wait(2.5)
        d4 = Tex("5 kg box, rope at $30^\\circ$, constant velocity").scale(1.0).shift(DOWN * 2.4)
        self.play(Write(d4))
        self.wait(3)

        # --- Band 1 (subtopic_1): weight, and mass vs weight ---
        self.next_band(1)
        b1t = Tex("First force: the Earth pulls — weight").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = MathTex(r"w = mg").scale(1.2).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1a))
        self.wait(2)
        b1b = MathTex(r"w = 5 \times 9{,}8 = 49 \text{ N down}").scale(1.15).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1b))
        self.play(Create(SurroundingRectangle(b1b, color=GREEN)))
        self.wait(2.5)
        b1c = Tex("Mass: 5 kg — scalar, same on the Moon").scale(1.05).shift(band_shift(1) + DOWN * 1.1)
        self.play(Write(b1c))
        self.wait(2)
        b1d = Tex("Weight: 49 N — a force, a vector").scale(1.05).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1d))
        self.wait(3)

        # --- Band 2 (subtopic_1): the cast of four ---
        self.next_band(2)
        b2t = Tex("The cast around the box").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = Tex(r"Earth $\to$ weight $w$, down").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2a))
        self.wait(2)
        b2b = Tex(r"Floor $\to$ normal force $N$, up").scale(1.05).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2b))
        self.wait(2)
        b2c = Tex(r"Rope $\to$ $F_{app}$ at $30^\circ$").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2c))
        self.wait(2)
        b2d = Tex(r"Rough floor $\to$ friction $f$, backward").scale(1.05).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2d))
        self.wait(2)
        b2e = Tex("`force of motion' pushing it along").scale(1.0).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2e))
        self.play(Create(strike(b2e)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the free-body diagram, arrow by arrow ---
        self.next_band(3)
        b3t = Tex("The free-body diagram: a dot, four arrows").scale(1.1).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3t))
        self.wait(2)
        c = band_shift(3) + DOWN * 0.4
        dot = Dot(c, radius=0.1)
        self.play(Create(dot))
        self.wait(1.5)
        aw = Arrow(c, c + DOWN * 2.2, buff=0, color=YELLOW, stroke_width=6)
        lw = MathTex(r"w = 49 \text{ N}").scale(0.95).move_to(c + DOWN * 2.3 + RIGHT * 1.6)
        self.play(Create(aw), Write(lw))
        self.wait(2)
        an = Arrow(c, c + UP * 1.8, buff=0, color=BLUE, stroke_width=6)
        ln = MathTex(r"N").scale(1.0).move_to(c + UP * 2.1 + LEFT * 0.5)
        self.play(Create(an), Write(ln))
        self.wait(2)
        href = DashedLine(c, c + RIGHT * 2.6, stroke_width=3)
        aa = Arrow(c, c + RIGHT * 2.3 + UP * 1.33, buff=0, color=GREEN, stroke_width=6)
        la = MathTex(r"F_{app}").scale(1.0).move_to(c + RIGHT * 3.0 + UP * 1.6)
        ang = MathTex(r"30^\circ").scale(0.85).move_to(c + RIGHT * 1.9 + UP * 0.4)
        self.play(Create(href))
        self.play(Create(aa), Write(la))
        self.play(Write(ang))
        self.wait(2)
        af = Arrow(c, c + LEFT * 2.0, buff=0, color=RED, stroke_width=6)
        lf = MathTex(r"f").scale(1.0).move_to(c + LEFT * 2.3 + UP * 0.4)
        self.play(Create(af), Write(lf))
        self.wait(3)

        # --- Band 4 (subtopic_2): the marker's quality rules ---
        self.next_band(4)
        b4t = Tex("What the marker checks").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        b4a = Tex("Every arrow starts ON the dot, points away").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4a))
        self.wait(2)
        b4b = Tex("Arrowhead $+$ label on every arrow").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4b))
        self.wait(2)
        b4c = Tex("Mark the $30^\\circ$ against the horizontal").scale(1.05).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4c))
        self.wait(2)
        b4d = Tex("No floor, no rope, no scenery").scale(1.05).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4d))
        self.wait(2)
        b4e = Tex("a velocity arrow among the forces").scale(1.05).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4e))
        self.play(Create(strike(b4e)))
        self.wait(3)

        # --- Band 5 (subtopic_3): constant velocity = balance ---
        self.next_band(5)
        b5t = Tex("`Constant velocity' is physics in disguise").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = Tex("Newton I: constant velocity $\\Rightarrow$ net force 0").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5a))
        self.wait(2.5)
        b5b = Tex("Horizontal balance:").scale(1.05).shift(band_shift(5) + UP * 0.2 + LEFT * 3.0)
        b5c = MathTex(r"F_{app}\cos 30^\circ = f").scale(1.15).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5b))
        self.play(Write(b5c))
        self.play(Create(SurroundingRectangle(b5c, color=GREEN)))
        self.wait(2.5)
        b5d = Tex("Vertical balance:").scale(1.05).shift(band_shift(5) + DOWN * 1.5 + LEFT * 3.2)
        b5e = MathTex(r"N + F_{app}\sin 30^\circ = w").scale(1.15).shift(band_shift(5) + DOWN * 2.3)
        self.play(Write(b5d))
        self.play(Write(b5e))
        self.play(Create(SurroundingRectangle(b5e, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_3): the normal-force subtlety ---
        self.next_band(6)
        b6t = Tex("The subtlety that splits the top answers").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = MathTex(r"N = w \text{ (always)}").scale(1.1).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6a))
        self.play(Create(strike(b6a)))
        self.wait(2)
        b6b = MathTex(r"N = w - F_{app}\sin 30^\circ < 49 \text{ N}").scale(1.1).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6b))
        self.play(Create(SurroundingRectangle(b6b, color=GREEN)))
        self.wait(2.5)
        b6c = Tex("The rope carries part of the load").scale(1.05).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6c))
        self.wait(2)
        b6d = Tex("Less $N$ $\\to$ less friction: easier to drag").scale(1.05).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6d))
        self.wait(3)

        # --- Band 7 (subtopic_4): the five-step method ---
        self.next_band(7)
        b7t = Tex("The method, five steps").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex("1. Isolate: forces ON the object only").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7a))
        self.wait(2)
        b7b = Tex("2. Hunt: gravity first, then every toucher").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7b))
        self.wait(2)
        b7c = Tex("3. Dot $+$ labelled arrows, angles marked").scale(1.05).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7c))
        self.wait(2)
        b7d = Tex("4. Read the motion state").scale(1.05).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7d))
        self.wait(2)
        b7e = Tex("5. Balance statements, direction by direction").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
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
        b8b = Tex("Only CHANGES of motion need force").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex("2. $N = w$ assumed — read the balance").scale(1.05).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8c))
        self.wait(2)
        b8d = Tex("3. Friction opposes the SLIDING").scale(1.05).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8d))
        self.wait(2)
        b8e = Tex("4. Floating, unlabelled, headless arrows").scale(1.05).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8e))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 9 (subtopic_5): who is actually pulling on the box ---
        self.next_band(9)
        b9t = Tex("Who is actually pulling on the box?").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("The gas bottle in the yard — name the culprits").scale(1.0).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9a))
        self.wait(2)
        b9b = MathTex(r"\text{Earth: } w = 5 \times 9{,}8 = 49 \text{ N down}").scale(1.05).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9b))
        self.play(Create(SurroundingRectangle(b9b, color=GREEN)))
        self.wait(2.5)
        b9c = Tex("Concrete: pushes up. Rope: pulls forward-up").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9c))
        self.wait(2)
        b9d = Tex("Rough ground: drags back").scale(1.05).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9d))
        self.wait(2)
        b9e = Tex("`Moving' is not a culprit — no such force").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9e))
        self.wait(3)

        # --- Band 10 (subtopic_6): a dot and four arrows, rebuilt ---
        self.next_band(10)
        b10t = Tex("A dot and four arrows").scale(1.2).shift(band_shift(10) + UP * 2.4)
        self.play(Write(b10t))
        self.wait(2)
        c2 = band_shift(10) + DOWN * 0.4
        dot2 = Dot(c2, radius=0.1)
        self.play(Create(dot2))
        self.wait(1.5)
        a2w = Arrow(c2, c2 + DOWN * 2.2, buff=0, color=YELLOW, stroke_width=6)
        l2w = MathTex(r"w").scale(1.0).move_to(c2 + DOWN * 2.5 + RIGHT * 0.4)
        self.play(Create(a2w), Write(l2w))
        self.wait(1.5)
        a2n = Arrow(c2, c2 + UP * 1.8, buff=0, color=BLUE, stroke_width=6)
        l2n = MathTex(r"N").scale(1.0).move_to(c2 + UP * 2.1 + LEFT * 0.5)
        self.play(Create(a2n), Write(l2n))
        self.wait(1.5)
        a2a = Arrow(c2, c2 + RIGHT * 2.3 + UP * 1.33, buff=0, color=GREEN, stroke_width=6)
        l2a = MathTex(r"F_{app}").scale(1.0).move_to(c2 + RIGHT * 3.0 + UP * 1.6)
        ang2 = MathTex(r"30^\circ").scale(0.85).move_to(c2 + RIGHT * 1.9 + UP * 0.4)
        self.play(Create(a2a), Write(l2a), Write(ang2))
        self.wait(1.5)
        a2f = Arrow(c2, c2 + LEFT * 2.0, buff=0, color=RED, stroke_width=6)
        l2f = MathTex(r"f").scale(1.0).move_to(c2 + LEFT * 2.3 + UP * 0.4)
        self.play(Create(a2f), Write(l2f))
        self.wait(2)
        b10r = Tex("Four spokes — say them out loud, in order").scale(1.0).move_to(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10r))
        self.wait(3)

        # --- Band 11 (subtopic_7): the slant and `constant speed' ---
        self.next_band(11)
        b11t = Tex("Why the slant helps").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11t))
        self.wait(2)
        b11a = Tex("Steady speed: nothing is winning").scale(1.05).shift(band_shift(11) + UP * 1.2)
        self.play(Write(b11a))
        self.wait(2)
        b11b = Tex("One pull, two jobs — the suitcase handle").scale(1.05).shift(band_shift(11) + UP * 0.3)
        self.play(Write(b11b))
        self.wait(2.5)
        b11c = MathTex(r"F_{app}\cos 30^\circ = f").scale(1.1).shift(band_shift(11) + DOWN * 0.7)
        self.play(Write(b11c))
        self.wait(2)
        b11d = MathTex(r"N + F_{app}\sin 30^\circ = w").scale(1.1).shift(band_shift(11) + DOWN * 1.6)
        self.play(Write(b11d))
        self.wait(2)
        b11e = Tex("The floor pushes with LESS than 49 N").scale(1.05).shift(band_shift(11) + DOWN * 2.6)
        self.play(Write(b11e))
        self.play(Create(SurroundingRectangle(b11e, color=GREEN)))
        self.wait(4)
