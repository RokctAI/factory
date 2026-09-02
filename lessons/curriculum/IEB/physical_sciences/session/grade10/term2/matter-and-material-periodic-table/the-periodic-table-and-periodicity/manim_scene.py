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

# Band-layout whiteboard scene for "The Periodic Table and Periodicity"
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe mobjects only; write-only reveals; camera moves down band by
# band. Band time apportioned to subtopics.json
# (235/230/240/240/180/185/190 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class PeriodicTableSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the table's architecture ---
        title = Tex("The Periodic Table and Periodicity").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("ordered by ATOMIC NUMBER — protons, never mass").scale(0.9).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("period = number of occupied energy levels").scale(0.95).shift(UP * 0.1)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("group = number of valence electrons").scale(0.95).shift(DOWN * 0.8)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2)
        b0_l4 = Tex("position and configuration: two spellings, one fact").scale(0.85).shift(DOWN * 1.8)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): translate both ways ---
        self.next_band(1)
        b1_t = Tex("Translate both ways").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex(r"1s$^2$ 2s$^2$ 2p$^6$ 3s$^2$ 3p$^4$:").scale(0.95).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("three levels, six valence — period 3, group 16: sulphur").scale(0.8).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)
        b1_l3 = Tex(r"period 2, group 1 $\to$ 1s$^2$ 2s$^1$: lithium").scale(0.9).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("transition metals: the hard, dense central slab").scale(0.85).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the staircase and the three kingdoms ---
        self.next_band(2)
        b2_t = Tex("The staircase and the three kingdoms").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        # staircase sketch
        p0 = band_shift(2) + UP * 1.2 + RIGHT * 0.5
        stair = [p0, p0 + DOWN * 0.5, p0 + DOWN * 0.5 + RIGHT * 0.7,
                 p0 + DOWN * 1.0 + RIGHT * 0.7, p0 + DOWN * 1.0 + RIGHT * 1.4,
                 p0 + DOWN * 1.5 + RIGHT * 1.4]
        for a, b in zip(stair, stair[1:]):
            self.play(Create(Line(a, b, color=YELLOW)), run_time=0.3)
        b2_l1 = Tex("left: METALS — shiny, bend, conduct, form cations").scale(0.8).shift(band_shift(2) + DOWN * 0.2 + LEFT * 2.0)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex("upper right: NON-METALS — dull, brittle, insulate, form anions").scale(0.75).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("on the line: METALLOIDS — silicon semiconducts").scale(0.8).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_l4 = Tex("magnetic club: iron, cobalt, nickel").scale(0.8).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_3): trends across a period ---
        self.next_band(3)
        b3_t = Tex("Across a period: the nucleus wins").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex("more protons, same outer level — grip tightens").scale(0.85).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("radius DECREASES").scale(0.9).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l2))
        self.wait(1.5)
        b3_l3 = Tex("ionisation energy INCREASES").scale(0.9).shift(band_shift(3) + DOWN * 0.3)
        self.play(Write(b3_l3))
        self.wait(1.5)
        b3_l4 = Tex("electron affinity and electronegativity RISE").scale(0.85).shift(band_shift(3) + DOWN * 1.0)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): trends down a group + the corners ---
        self.next_band(4)
        b4_t = Tex("Down a group: distance and screening win").scale(1.0).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("each row adds a level — further out, more screened").scale(0.85).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex("radius INCREASES; ionisation energy DECREASES").scale(0.85).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex("electronegativity FALLS — noble gases sit out").scale(0.85).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex("corners: fluorine pulls fiercest; bottom-left barely holds on").scale(0.75).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): groups 1 and 2 ---
        self.next_band(5)
        b5_t = Tex("Groups 1 and 2: the giving metals").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("alkali metals: one cheap electron — fiercest metals,").scale(0.85).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("stored under oil, fizz and flame in water, +1 ions").scale(0.85).shift(band_shift(5) + UP * 0.5)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("reactivity INCREASES downward — longer rope").scale(0.85).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_l4 = Tex("alkaline earths: two electrons, calmer, +2 ions —").scale(0.85).shift(band_shift(5) + DOWN * 1.3)
        b5_l5 = Tex("magnesium's white flare; calcium in cement and bones").scale(0.8).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): groups 17 and 18 + the mirror ---
        self.next_band(6)
        b6_t = Tex("Groups 17 and 18: hunters and the content").scale(1.0).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex("halogens: seven electrons, hunting one — $-1$ ions,").scale(0.85).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("most reactive non-metals").scale(0.85).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("their reactivity DECREASES downward — the mirror").scale(0.85).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex("noble gases: full levels, inert, single atoms —").scale(0.85).shift(band_shift(6) + DOWN * 1.3)
        b6_l5 = Tex("everyone else's ambition").scale(0.85).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the street map ---
        self.next_band(7)
        b7_t = Tex("The street map of the elements").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("house numbers: the proton count, in strict order").scale(0.85).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("your street (period): how many floors of electrons").scale(0.85).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("your column (group): who shares your top floor count").scale(0.85).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("sulphur: row 3, column 16 — read both ways").scale(0.85).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): the tug-of-war ---
        self.next_band(8)
        b8_t = Tex("The tug-of-war for electrons").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("across: more pullers, same rope — grip tightens").scale(0.85).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("down: longer rope, muffled pull — grip weakens").scale(0.85).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("every trend answer: MORE PULL or LONGER ROPE").scale(0.85).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex("fluorine: short rope, big team — fiercest puller").scale(0.85).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_7): four families you already know ---
        self.next_band(9)
        b9_t = Tex("Four families you already know").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("column 1: the kid with one marble — +1, wilder downward").scale(0.75).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("column 2: careful givers — +2, calmer").scale(0.8).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex(r"column 17: collectors, one empty slot — $-1$, tamer downward").scale(0.75).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("column 18: the full album — inert, everyone's ambition").scale(0.75).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(4)
