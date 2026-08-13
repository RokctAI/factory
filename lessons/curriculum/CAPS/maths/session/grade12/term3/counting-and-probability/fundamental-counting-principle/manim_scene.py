from manim import *

# Band-layout whiteboard scene: sequential vertical bands, one per teaching
# beat, camera moves down between bands, add-only lifecycle. Exporter-safe
# mobjects only (Tex/MathTex/Line/Rectangle); every working line is a
# single-string MathTex revealed with Write. Covers all seven subtopics of
# the duo (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7); band time
# apportioned to subtopics.json (220/240/230/260/190/210/230 of 1580 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FundamentalCountingPrincipleSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the principle — choices multiply
        title = Tex("The Fundamental Counting Principle").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex(r"Task 1 in $m$ ways, task 2 in $n$ ways for EACH:").scale(1.05).shift(UP * 0.9)
        s0_l2 = MathTex(r"\text{together: } m \times n \text{ ways}").scale(1.2).shift(UP * 0.0)
        self.play(Write(s0_l1))
        self.play(Write(s0_l2))
        self.wait(2.5)
        s0_l3 = MathTex(r"4 \text{ shirts} \times 3 \text{ trousers} = 12 \text{ outfits}").scale(1.1).shift(DOWN * 1.1)
        s0_l4 = MathTex(r"\times\, 2 \text{ shoes} = 24 \text{ complete outfits}").scale(1.1).shift(DOWN * 2.0)
        self.play(Write(s0_l3))
        self.wait(2)
        self.play(Write(s0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): the slot method; multiply along, add across
        self.next_band(1)
        b1_title = Tex("Draw the slots").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        slot_xs = [-1.6, 0.0, 1.6]
        slot_ns = ["5", "7", "4"]
        slot_lines = [Line(band_shift(1) + UP * 0.8 + RIGHT * (x - 0.45),
                           band_shift(1) + UP * 0.8 + RIGHT * (x + 0.45),
                           stroke_width=4) for x in slot_xs]
        slot_nums = [MathTex(n).scale(1.2).move_to(band_shift(1) + UP * 1.3 + RIGHT * x)
                     for x, n in zip(slot_xs, slot_ns)]
        self.play(Create(slot_lines[0]), Create(slot_lines[1]), Create(slot_lines[2]))
        self.play(Write(slot_nums[0]), Write(slot_nums[1]), Write(slot_nums[2]))
        self.wait(2)
        b1_l2 = MathTex(r"5 \times 7 \times 4 = 140 \text{ meals}").scale(1.15).shift(band_shift(1) + DOWN * 0.2)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex(r"Multiply along a sequence of decisions").scale(1.05).shift(band_shift(1) + DOWN * 1.2)
        b1_l4 = Tex(r"Add only across exclusive cases (taxi OR walk)").scale(1.05).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): arrangements and the factorial
        self.next_band(2)
        b2_title = Tex("Six learners line up for a photo").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        p_xs = [-2.5, -1.5, -0.5, 0.5, 1.5, 2.5]
        p_ns = ["6", "5", "4", "3", "2", "1"]
        p_lines = [Line(band_shift(2) + UP * 0.8 + RIGHT * (x - 0.35),
                        band_shift(2) + UP * 0.8 + RIGHT * (x + 0.35),
                        stroke_width=4) for x in p_xs]
        p_nums = [MathTex(n).scale(1.1).move_to(band_shift(2) + UP * 1.3 + RIGHT * x)
                  for x, n in zip(p_xs, p_ns)]
        self.play(Create(p_lines[0]), Create(p_lines[1]), Create(p_lines[2]),
                  Create(p_lines[3]), Create(p_lines[4]), Create(p_lines[5]))
        self.play(Write(p_nums[0]), Write(p_nums[1]), Write(p_nums[2]),
                  Write(p_nums[3]), Write(p_nums[4]), Write(p_nums[5]))
        self.wait(2)
        b2_l2 = MathTex(r"6! = 6 \times 5 \times 4 \times 3 \times 2 \times 1 = 720").scale(1.1).shift(band_shift(2) + DOWN * 0.1)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = Tex(r"$n$ distinct objects: $n!$ arrangements").scale(1.1).shift(band_shift(2) + DOWN * 1.2)
        b2_l4 = Tex(r"Options shrink — arrangement forbids reuse").scale(1.05).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): restrictions — forced, glued, complement
        self.next_band(3)
        b3_title = Tex("Fussy first, glue for together, complement for apart").scale(1.0).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"\text{Left end forced: } 1 \times 5! = 120").scale(1.1).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"\text{Two together (glue): } 5! \times 2 = 240").scale(1.1).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"\text{Two apart: } 720 - 240 = 480").scale(1.1).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex(r"The complement is often the shortest road").scale(1.05).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): codes — ask about repetition first
        self.next_band(4)
        b4_title = Tex("Codes: is repetition allowed?").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{4-digit PIN, repetition allowed: } 10^4 = 10\,000").scale(1.05).shift(band_shift(4) + UP * 1.0)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"\text{Repetition forbidden: } 10 \times 9 \times 8 \times 7 = 5\,040").scale(1.05).shift(band_shift(4) + UP * 0.0)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex(r"Same slots, different discipline —").scale(1.05).shift(band_shift(4) + DOWN * 1.2)
        b4_l4 = Tex(r"nearly half the codes gone").scale(1.05).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): restricted slots first; letters of a word
        self.next_band(5)
        b5_title = Tex("Restricted slots are filled first").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"\text{Vowel + 2 different digits: } 5 \times 10 \times 9 = 450").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex(r"May not start with 0: first slot drops to 9").scale(1.05).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"\text{MATHS: 5 distinct letters} \Rightarrow 5! = 120").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
        b5_l4 = MathTex(r"\text{Begins with M: } 1 \times 4! = 24").scale(1.05).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): probability by counting — the PIN case
        self.next_band(6)
        b6_title = Tex("Probability by counting").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"P(\text{event}) = \frac{\text{favourable}}{\text{total}}").scale(1.15).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=YELLOW)))
        self.wait(2.5)
        b6_l2 = Tex(r"Random PIN: all four digits different?").scale(1.05).shift(band_shift(6) + DOWN * 0.2)
        b6_l3 = MathTex(r"P = \frac{5\,040}{10\,000} = 0{,}504").scale(1.15).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex(r"Better than half — surprisingly high").scale(1.05).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): friends together; MATHS begins with M
        self.next_band(7)
        b7_title = Tex("The same machine, run twice").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"P(\text{friends together}) = \frac{240}{720} = \frac{1}{3}").scale(1.1).shift(band_shift(7) + UP * 1.0)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"P(\text{separated}) = 1 - \frac{1}{3} = \frac{2}{3}").scale(1.1).shift(band_shift(7) + UP * 0.0)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"P(\text{MATHS begins with M}) = \frac{24}{120} = 0{,}2").scale(1.05).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        b7_l4 = Tex(r"Shortcut view: one fair pick among 5 letters").scale(1.0).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): outfits from a small cupboard
        self.next_band(8)
        b8_title = Tex("Outfits from a small cupboard").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_wrong = MathTex(r"4 \text{ shirts} + 3 \text{ trousers} = 7?").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_wrong))
        self.play(Create(strike(b8_wrong)))
        self.wait(2)
        b8_l1 = MathTex(r"4 \times 3 = 12 \text{ outfits}, \;\; \times 2 \text{ shoes} = 24").scale(1.05).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l1))
        self.play(Create(SurroundingRectangle(b8_l1, color=GREEN)))
        self.wait(2.5)
        b8_l2 = MathTex(r"\text{Tuck shop: } 5 \times 7 \times 4 = 140 \text{ lunches}").scale(1.05).shift(band_shift(8) + DOWN * 1.0)
        b8_l3 = MathTex(r"\text{Combo OR lunchbox: } 140 + 3").scale(1.05).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(3)

        # --- Band 9 (subtopic_6): the class photo and the glued friends
        self.next_band(9)
        b9_title = Tex("The class photo and the glued friends").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"6 \times 5 \times 4 \times 3 \times 2 \times 1 = 6! = 720").scale(1.1).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"\text{Head learner at left end: } 1 \times 5! = 120").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"\text{Invisible string: } 5! \times 2 = 240").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = MathTex(r"\text{Kept apart: } 720 - 240 = 480").scale(1.05).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        b9_l5 = Tex(r"Fussy first, string for together, subtract for apart").scale(1.0).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): what are the chances, counted
        self.next_band(10)
        b10_title = Tex("What are the chances, counted").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"P(\text{PIN, all different}) = \frac{5\,040}{10\,000} = 0{,}504").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"P(\text{friends together}) = \frac{240}{720} = \frac{1}{3}").scale(1.05).shift(band_shift(10) + UP * 0.0)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"P(\text{apart}) = \frac{2}{3}, \quad P(\text{M first}) = 0{,}2").scale(1.0).shift(band_shift(10) + DOWN * 1.1)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex(r"Count the world, count your wish, divide").scale(1.1).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(4)
