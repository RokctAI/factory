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

# Band-layout whiteboard scene for the-periodic-table-and-periodicity session
# duo (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe mobjects only; add-only lifecycle; one band per teaching step.
# Time apportioned to subtopics.json (235/230/240/240/180/185/190 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PeriodicTableAndPeriodicitySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the table's architecture ---
        title = Tex("The Periodic Table and Periodicity").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        a1 = Tex("Ordered by ATOMIC NUMBER (protons)").scale(1.05).shift(UP * 1.0)
        self.play(Write(a1))
        self.wait(2)
        a2 = Tex("Row = PERIOD = number of energy levels").scale(1.05).shift(UP * 0.1)
        self.play(Write(a2))
        self.wait(2)
        a3 = Tex("Column = GROUP = valence electrons").scale(1.05).shift(DOWN * 0.8)
        self.play(Write(a3))
        self.wait(2)
        a4 = Tex("Groups 13--18: units digit = valence count").scale(1.0).shift(DOWN * 1.7)
        self.play(Write(a4))
        self.wait(2)
        a5 = Tex("Centre slab: the transition metals").scale(1.0).shift(DOWN * 2.6)
        self.play(Write(a5))
        self.wait(3)

        # --- Band 1 (subtopic_1): translate both ways ---
        self.next_band(1)
        b1_t = Tex("Position and configuration: two spellings").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_1 = MathTex(r"1s^2\,2s^2\,2p^6\,3s^2\,3p^5").scale(1.15).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_1))
        self.wait(2)
        b1_2 = Tex("3 levels: period 3; 7 valence: group 17").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_2))
        self.wait(2)
        b1_3 = Tex("the element is CHLORINE").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_3))
        self.play(Create(SurroundingRectangle(b1_3, color=GREEN)))
        self.wait(2)
        b1_4 = Tex("Reverse: period 2, group 2").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_4))
        self.wait(1.5)
        b1_5 = MathTex(r"1s^2\,2s^2 \; \text{— beryllium}").scale(1.05).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_5))
        self.play(Create(SurroundingRectangle(b1_5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the staircase and the three kingdoms ---
        self.next_band(2)
        b2_t = Tex("Metals, non-metals, metalloids").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        # sketch: table outline with a staircase line
        tb = band_shift(2) + UP * 0.4
        outline = Rectangle(width=6.4, height=2.6).move_to(tb)
        self.play(Create(outline))
        stair = VGroup(
            Line(tb + UP * 1.3 + RIGHT * 1.0, tb + UP * 0.65 + RIGHT * 1.0),
            Line(tb + UP * 0.65 + RIGHT * 1.0, tb + UP * 0.65 + RIGHT * 1.7),
            Line(tb + UP * 0.65 + RIGHT * 1.7, tb + RIGHT * 1.7),
            Line(tb + RIGHT * 1.7, tb + RIGHT * 2.4),
            Line(tb + RIGHT * 2.4, tb + DOWN * 0.65 + RIGHT * 2.4),
            Line(tb + DOWN * 0.65 + RIGHT * 2.4, tb + DOWN * 0.65 + RIGHT * 3.1),
            Line(tb + DOWN * 0.65 + RIGHT * 3.1, tb + DOWN * 1.3 + RIGHT * 3.1),
        )
        self.play(Create(stair))
        m_lab = Tex("metals").scale(0.9).move_to(tb + LEFT * 1.6)
        n_lab = Tex("non-metals").scale(0.8).move_to(tb + UP * 0.8 + RIGHT * 2.5)
        self.play(Write(m_lab), Write(n_lab))
        self.wait(2)
        s_lab = Tex("metalloids on the staircase (Si, Ge)").scale(0.9).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(s_lab))
        self.wait(2)
        b2_1 = Tex("Metals lose $e^-$: $+$ ions; conduct").scale(1.0).shift(band_shift(2) + DOWN * 2.1)
        b2_2 = Tex("Non-metals gain $e^-$: $-$ ions; insulate").scale(1.0).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_1))
        self.wait(2)
        self.play(Write(b2_2))
        self.wait(3)

        # --- Band 3 (subtopic_3): trends across a period ---
        self.next_band(3)
        b3_t = Tex("Across a period: the nucleus wins").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_1 = Tex("More protons, SAME outer level").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_1))
        self.wait(2)
        b3_2 = Tex("Atomic radius DECREASES").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_2))
        self.wait(2)
        b3_3 = Tex("Ionisation energy INCREASES").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_3))
        self.wait(2)
        b3_4 = Tex("Electron affinity: gains more readily").scale(1.0).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_4))
        self.wait(2)
        b3_5 = Tex("Electronegativity RISES").scale(1.05).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_5))
        self.wait(3)

        # --- Band 4 (subtopic_3): trends down a group + the corners ---
        self.next_band(4)
        b4_t = Tex("Down a group: distance wins").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_1 = Tex("New level each row + more screening").scale(1.0).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_1))
        self.wait(2)
        # mini table with trend arrows
        tt = band_shift(4) + DOWN * 0.1
        box = Rectangle(width=4.6, height=2.0).move_to(tt)
        ar_across = Arrow(tt + UP * 1.4 + LEFT * 2.3, tt + UP * 1.4 + RIGHT * 2.3, buff=0)
        al_across = Tex("smaller, tighter grip").scale(0.75).move_to(tt + UP * 1.85)
        ar_down = Arrow(tt + LEFT * 2.9 + UP * 1.0, tt + LEFT * 2.9 + DOWN * 1.0, buff=0)
        al_down = Tex("bigger, weaker grip").scale(0.75).rotate(0).move_to(tt + LEFT * 2.9 + DOWN * 1.45)
        self.play(Create(box))
        self.play(Create(ar_across), Write(al_across))
        self.wait(1.5)
        self.play(Create(ar_down), Write(al_down))
        self.wait(2)
        b4_2 = Tex("F (top right): strongest puller").scale(1.0).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_2))
        self.wait(2)
        b4_3 = Tex("Noble gases sit the trend out").scale(1.0).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_3))
        self.wait(3)

        # --- Band 5 (subtopic_4): groups 1 and 2 ---
        self.next_band(5)
        b5_t = Tex("Group portraits: the metals").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_1 = Tex("Group 1 alkali metals: 1 valence $e^-$").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_1))
        self.wait(2)
        b5_2 = Tex("most reactive metals; stored under oil").scale(1.0).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_2))
        self.wait(2)
        b5_3 = Tex("reactivity INCREASES down; $+1$ ions").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_3))
        self.play(Create(SurroundingRectangle(b5_3, color=GREEN)))
        self.wait(2)
        b5_4 = Tex("Group 2 alkaline earth: 2 $e^-$, $+2$ ions").scale(1.0).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_4))
        self.wait(2)
        b5_5 = Tex("calmer: losing two costs more (Mg, Ca)").scale(1.0).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_5))
        self.wait(3)

        # --- Band 6 (subtopic_4): groups 17 and 18 + the mirror ---
        self.next_band(6)
        b6_t = Tex("Halogens and noble gases").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_1 = Tex("Group 17 halogens: 7 $e^-$, want one more").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_1))
        self.wait(2)
        b6_2 = Tex("most reactive non-metals; $-1$ ions").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_2))
        self.wait(2)
        b6_3 = Tex("reactivity DECREASES down (F fierce, I mild)").scale(0.95).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_3))
        self.wait(2)
        b6_4 = Tex("Mirror: metals up, non-metals down").scale(1.0).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_4))
        self.play(Create(SurroundingRectangle(b6_4, color=GREEN)))
        self.wait(2)
        b6_5 = Tex("Group 18: full level, inert, single atoms").scale(1.0).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the street map ---
        self.next_band(7)
        b7_t = Tex("The street map of the elements").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_1 = Tex("House numbers = proton count, no gaps").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_1))
        self.wait(2)
        b7_2 = Tex("Street (row) = floors of electrons").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_2))
        self.wait(2)
        b7_3 = Tex("Side of town (column) = top-floor count").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_3))
        self.wait(2)
        b7_4 = Tex("Chlorine: row 3, column 17 — 3 floors,").scale(1.0).shift(band_shift(7) + DOWN * 1.6)
        b7_5 = Tex("7 upstairs; ending $2s^2$: beryllium").scale(1.0).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_4))
        self.wait(2)
        self.play(Write(b7_5))
        self.play(Create(SurroundingRectangle(b7_5, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): the tug-of-war ---
        self.next_band(8)
        b8_t = Tex("The tug-of-war for electrons").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_1 = Tex("Pullers = protons; rope = distance").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_1))
        self.wait(2)
        b8_2 = Tex("Across: more pullers, same rope").scale(1.0).shift(band_shift(8) + UP * 0.2)
        b8_3 = Tex("smaller atoms, harder to steal from").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_2))
        self.wait(2)
        self.play(Write(b8_3))
        self.wait(2)
        b8_4 = Tex("Down: longer rope, muffled pull").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        b8_5 = Tex("bigger atoms, electrons fall off easily").scale(1.0).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8_4))
        self.wait(2)
        self.play(Write(b8_5))
        self.play(Create(SurroundingRectangle(b8_5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): four families you already know ---
        self.next_band(9)
        b9_t = Tex("Four families you already know").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_1 = Tex("Col 1: impulsive givers, one coin, $+1$").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_1))
        self.wait(2)
        b9_2 = Tex("wilder going down (K beats Na)").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_2))
        self.wait(2)
        b9_3 = Tex("Col 2: careful givers, two coins, $+2$").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_3))
        self.wait(2)
        b9_4 = Tex("Col 17: collectors, $-1$, weaken down").scale(1.0).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_4))
        self.wait(2)
        b9_5 = Tex("Col 18: need nothing — everyone's goal").scale(1.0).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_5))
        self.play(Create(SurroundingRectangle(b9_5, color=GREEN)))
        self.wait(4)
