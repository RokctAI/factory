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

# Band-layout whiteboard scene for "Labour Rights and Collective Bargaining"
# (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier subtopics 5-7).
# Exporter-safe primitives only; add-only lifecycle; camera moves down band
# by band. Subtopic durations: 220/230/210/230/190/190/190 of 1460 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class LabourRightsCollectiveBargainingSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===================== Part 1 — Expert =====================
        # --- Band 0 (subtopic_1): the imbalance and the constitutional rights ---
        title = Tex("Labour Rights and Collective Bargaining").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0a = Tex("Lone applicant vs the firm: unequal bargain").scale(1.05).shift(UP * 1.2)
        self.play(Write(b0a))
        self.wait(2)
        b0b = Tex("Labour law civilises it:").scale(1.1).shift(UP * 0.3)
        b0c = Tex("minimum floors beneath, procedures around,").scale(1.05).shift(DOWN * 0.4)
        b0d = Tex("collective strength behind the weaker party").scale(1.05).shift(DOWN * 1.1)
        self.play(Write(b0b))
        self.play(Write(b0c))
        self.play(Write(b0d))
        self.wait(2)
        b0e = Tex("Bill of Rights: fair practices, join unions,").scale(1.0).shift(DOWN * 2.0)
        b0f = Tex("organise, bargain, strike $\\cdot$ mirror: lock-out").scale(1.0).shift(DOWN * 2.7)
        self.play(Write(b0e))
        self.play(Write(b0f))
        self.wait(3)

        # --- Band 1 (subtopic_1): the LRA's three principles ---
        self.next_band(1)
        b1t = Tex("Three principles running through the LRA").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = Tex("SELF-GOVERNMENT: the parties negotiate their").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1a2 = Tex("own terms — the state builds the arena, not the wage").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1a))
        self.play(Write(b1a2))
        self.wait(2)
        b1b = Tex("MAJORITARIANISM: the majority union becomes").scale(1.05).shift(band_shift(1) + DOWN * 0.5)
        b1b2 = Tex("the recognised voice — one voice, not fragments").scale(1.05).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1b))
        self.play(Write(b1b2))
        self.wait(2)
        b1c = Tex("CONSULTATION: consult and disclose before").scale(1.05).shift(band_shift(1) + DOWN * 2.1)
        b1c2 = Tex("decisions that land on workers — retrenchment first").scale(1.0).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1c))
        self.play(Write(b1c2))
        self.wait(3)

        # --- Band 2 (subtopic_2): the three Acts matched to their jobs ---
        self.next_band(2)
        b2t = Tex("Three statutes, three jobs").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        r2a = Rectangle(width=2.6, height=0.9).shift(band_shift(2) + UP * 1.0 + LEFT * 5.0)
        t2a = Tex("LRA").scale(1.0).move_to(r2a.get_center())
        d2a = Tex("ENGAGEMENT: bargaining, strikes, dismissal, CCMA").scale(0.9).shift(band_shift(2) + UP * 1.0 + RIGHT * 1.6)
        self.play(Create(r2a), Write(t2a))
        self.play(Write(d2a))
        self.wait(2.5)
        r2b = Rectangle(width=2.6, height=0.9).shift(band_shift(2) + DOWN * 0.2 + LEFT * 5.0)
        t2b = Tex("BCEA").scale(1.0).move_to(r2b.get_center())
        d2b = Tex("the FLOOR: hours, overtime, leave, notice").scale(0.95).shift(band_shift(2) + DOWN * 0.2 + RIGHT * 1.3)
        self.play(Create(r2b), Write(t2b))
        self.play(Write(d2b))
        self.wait(2.5)
        r2c = Rectangle(width=2.6, height=0.9).shift(band_shift(2) + DOWN * 1.4 + LEFT * 5.0)
        t2c = Tex("COIDA").scale(1.0).move_to(r2c.get_center())
        d2c = Tex("SAFETY NET: the fund pays, no lawsuit needed").scale(0.95).shift(band_shift(2) + DOWN * 1.4 + RIGHT * 1.4)
        self.play(Create(r2c), Write(t2c))
        self.play(Write(d2c))
        self.wait(3)

        # --- Band 3 (subtopic_2): the floor-never-ceiling rule ---
        self.next_band(3)
        b3t = Tex("The BCEA floor: a minimum, never a menu").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        b3a = Tex("Hour ceilings + overtime multipliers; four leaves").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3b = Tex("Notice periods; child and forced labour banned").scale(1.05).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3a))
        self.wait(2)
        self.play(Write(b3b))
        self.wait(2)
        b3wrong = Tex("A signature can lower the floor").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3wrong))
        self.play(Create(strike(b3wrong)))
        self.wait(2)
        b3right = Tex("Contracts may improve the floor — never lower it").scale(1.05).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3right))
        self.play(Create(SurroundingRectangle(b3right, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): collective bargaining institutions ---
        self.next_band(4)
        b4t = Tex("The machinery of collective bargaining").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        b4a = Tex("Unions: recruit, stand beside members,").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4a2 = Tex("negotiate, organise lawful strikes").scale(1.0).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4a))
        self.play(Write(b4a2))
        self.wait(2)
        b4b = Tex("Employers' organisations: the mirror bodies").scale(1.0).shift(band_shift(4) + DOWN * 0.4)
        self.play(Write(b4b))
        self.wait(2)
        b4c = Tex("Bargaining councils: permanent sector chambers;").scale(1.0).shift(band_shift(4) + DOWN * 1.2)
        b4c2 = Tex("agreements EXTENDED across the whole sector").scale(1.0).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4c))
        self.play(Write(b4c2))
        self.wait(2)
        b4d = Tex("Workplace forums: consultation inside one workplace").scale(0.95).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4d))
        self.wait(3)

        # --- Band 5 (subtopic_3): three chambers, three conversations ---
        self.next_band(5)
        b5t = Tex("Three chambers, three conversations").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        r5a = Rectangle(width=4.6, height=1.5).shift(band_shift(5) + UP * 0.7 + LEFT * 4.2)
        t5a = Tex("Union").scale(0.85).move_to(r5a.get_center() + UP * 0.35)
        t5a2 = Tex("organises, negotiates").scale(0.75).move_to(r5a.get_center() + DOWN * 0.35)
        self.play(Create(r5a), Write(t5a), Write(t5a2))
        self.wait(1.5)
        r5b = Rectangle(width=4.6, height=1.5).shift(band_shift(5) + UP * 0.7 + RIGHT * 4.2)
        t5b = Tex("Bargaining council").scale(0.85).move_to(r5b.get_center() + UP * 0.35)
        t5b2 = Tex("sector-wide negotiation").scale(0.75).move_to(r5b.get_center() + DOWN * 0.35)
        self.play(Create(r5b), Write(t5b), Write(t5b2))
        self.wait(1.5)
        r5c = Rectangle(width=4.8, height=1.5).shift(band_shift(5) + DOWN * 1.3)
        t5c = Tex("Workplace forum").scale(0.85).move_to(r5c.get_center() + UP * 0.35)
        t5c2 = Tex("consults in one workplace").scale(0.75).move_to(r5c.get_center() + DOWN * 0.35)
        self.play(Create(r5c), Write(t5c), Write(t5c2))
        self.wait(2)
        b5e = Tex("Forums consult — wages are bargained elsewhere").scale(1.0).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5e))
        self.play(Create(SurroundingRectangle(b5e, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the CCMA ladder ---
        self.next_band(6)
        b6t = Tex("The CCMA — statutory, independent, free").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = Tex("1. CONCILIATION: the parties' own settlement").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6a))
        self.wait(2)
        ar6a = Arrow(band_shift(6) + UP * 0.75 + LEFT * 5.2, band_shift(6) + UP * 0.15 + LEFT * 5.2, buff=0)
        b6b = Tex("2. MEDIATION: solutions put forward, refusable").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Create(ar6a), Write(b6b))
        self.wait(2)
        ar6b = Arrow(band_shift(6) + DOWN * 0.15 + LEFT * 5.2, band_shift(6) + DOWN * 0.75 + LEFT * 5.2, buff=0)
        b6c = Tex("3. ARBITRATION: an AWARD that binds").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        self.play(Create(ar6b), Write(b6c))
        self.wait(2)
        b6d = Tex("Let them talk, offer options, impose only last").scale(1.05).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6d))
        self.play(Create(SurroundingRectangle(b6d, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): courts above, pressure tools outside ---
        self.next_band(7)
        b7t = Tex("Above the CCMA, and beyond it").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex("Labour Court: reviews awards, interprets statutes,").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7a2 = Tex("rules on strikes; Labour Appeal Court above it").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7a))
        self.play(Write(b7a2))
        self.wait(2)
        b7b = Tex("Protected strike: dispute referred, notice delivered").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7c = Tex("— strikers shielded from dismissal for striking").scale(1.0).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7b))
        self.play(Write(b7c))
        self.wait(2)
        b7d = Tex("Confrontation translated into procedure").scale(1.1).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7d))
        self.play(Create(SurroundingRectangle(b7d, color=GREEN)))
        self.wait(3)

        # ===================== Part 2 — Simplifier =====================
        # --- Band 8 (subtopic_5): one voice against the wind ---
        self.next_band(8)
        b8t = Tex("One voice against the wind").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("Thabo alone at the office door,").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8a2 = Tex("the queue at the fence behind him: no weight").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8a))
        self.play(Write(b8a2))
        self.wait(2)
        b8b = Tex("Every packer, one spokesperson: a negotiation").scale(1.05).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex("A union works the way a choir works").scale(1.05).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(b8c))
        self.play(Create(SurroundingRectangle(b8c, color=GREEN)))
        self.wait(2)
        b8d = Tex("State = referee: rules, majority voice, consult first").scale(0.95).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8d))
        self.wait(3)

        # --- Band 9 (subtopic_6): three rulebooks, three days ---
        self.next_band(9)
        b9t = Tex("Three rulebooks, three kinds of day").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("LRA — the ARGUMENT day: strikes, deadlocks").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9a))
        self.wait(2)
        b9b = Tex("BCEA — the ORDINARY day: the legal floor").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9b))
        self.wait(2)
        b9c = Tex("COIDA — the WORST day: the fund, no lawsuit").scale(1.05).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9c))
        self.wait(2)
        b9d = Tex("An offer beneath the floor is unlawful when made").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9d))
        self.wait(2)
        b9e = Tex("Identify the day — the Act names itself").scale(1.1).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9e))
        self.play(Create(SurroundingRectangle(b9e, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the ladder in the referee's room ---
        self.next_band(10)
        b10t = Tex("The ladder in the referee's room").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("Rung 1 — Conciliation: the parties decide").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10a))
        self.wait(2)
        b10b = Tex("Rung 2 — Mediation: the referee proposes").scale(1.05).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10b))
        self.wait(2)
        b10c = Tex("Rung 3 — Arbitration: the referee rules, binding").scale(1.05).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b10c))
        self.wait(2)
        b10box = SurroundingRectangle(VGroup(b10a, b10b, b10c), color=GREEN)
        self.play(Create(b10box))
        self.wait(2)
        b10d = Tex("Skip the rungs — the strike walks unprotected").scale(1.0).shift(band_shift(10) + DOWN * 1.6)
        self.play(Write(b10d))
        self.wait(2)
        b10e = Tex("Deadlock becomes steps, not shouting").scale(1.05).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10e))
        self.wait(4)
