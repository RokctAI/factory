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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex keep the export to the
# allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (220/230/230/230/190/190/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class NaziElectionSupportAndTheEnablingActSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The Elections of 1932
        title = Tex('The elections of 1932').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('Presidential: Hindenburg 53 percent; Hitler 36,8').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('July 1932: Nazis 37,3 percent, 230 seats').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('November 1932: Nazis 33,1 percent, 196 seats').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('Never a majority in a free election').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Hitler Becomes Chancellor, 30 January 1933
        self.next_band(1)
        b1_title = Tex('Hitler becomes chancellor').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('Papen and conservatives make a deal').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('30 January 1933: Hindenburg appoints Hitler').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('Only three Nazis in the cabinet').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('The conservatives thought they could control him').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): The Reichstag Fire and the Enabling Act
        self.next_band(2)
        b2_title = Tex('The fire and the Enabling Act').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('27 February 1933: the Reichstag burns').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('Decree: civil rights suspended').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('March 1933: Nazis 43,9 percent').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('23 March 1933: Enabling Act passed 444 to 94').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Building the Dictatorship and the Error Museum
        self.next_band(3)
        b3_title = Tex('Building the dictatorship').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('May 1933: trade unions abolished').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('July 1933: a one-party state').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('June 1934: the Night of the Long Knives').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('August 1934: Hitler becomes Führer').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Building the Dictatorship and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Most Germans voted Nazi in free elections''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Hitler seized power by force in 1933''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``The Enabling Act vote was free and fair''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``The Long Knives targeted Jews''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): The Scoreboard of Votes
        self.next_band(5)
        b5_title = Tex('The scoreboard of votes').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('1928: 2,6. 1930: 18,3. July 1932: 37,3.').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('The biggest party, but never more than half').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('Farmers, shopkeepers, office workers, the young').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('Fear of communism drove many votes').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): The Back Door into Power
        self.next_band(6)
        b6_title = Tex('The back door into power').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Conservatives: use his voters, keep him on a leash').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('30 January 1933: Hitler made chancellor').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('The Reichstag burns; rights cancelled').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('Thousands arrested; Dachau opens').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): A Parliament That Switched Itself Off
        self.next_band(7)
        b7_title = Tex('Parliament switches itself off').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('Opera house, stormtroopers on the walls').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('Enabling Act: 444 for, 94 against').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('All other parties banned by July 1933').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('August 1934: Hitler is Führer').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l2, color=YELLOW)))
        self.wait(4)
