from manim import *

# BAND LAYOUT reference implementation (see manim_exporter.py):
# content is laid out in sequential vertical bands along a long virtual
# canvas — one band per teaching step, each sized to be framed full-screen
# on a phone. Nothing is ever faded out or overwritten; at each step the
# camera moves down to clean space and earlier work stays on the canvas.
#
# WORKED-TRANSFORM CONVENTION: within a band, an equation is never replaced
# by a fresh Write of its successor. The current state morphs into the next
# one on matched sub-parts (Transform), or the next line is derived from the
# previous one by copies flying out of it (TransformFromCopy) so the earlier
# line still stays on the canvas. TransformMatchingTex is deliberately NOT
# used: it keys sub-parts by tex substring, and these equations repeat
# tokens ("+", "3", "x"), so it would pair them arbitrarily and crossfade
# the parts that matter (5x has no string match in 2x + 3x). Explicit
# part-index maps keep every glyph's journey intentional.

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k (k=0 is the
    default frame; each band is one frame-height further down)."""
    return DOWN * BAND * k


def strike(m):
    """Diagonal cancellation stroke through a term, teacher-style."""
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class QuadraticFactoring(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def swap_in(self, *targets, loose=()):
        """Post-transform bookkeeping: a piecewise transform leaves the scene
        holding loose fragments that already look exactly like `targets`;
        swap them for the clean parent mobjects between frames (no visible
        change) so later animations can address the parents' parts.

        Each loose mobject is removed together with its whole family:
        animating a temporary slice-group makes Scene.add dismantle the
        sliced parent, promoting its other children to top level, where a
        plain remove(parent) would no longer reach them."""
        for m in loose:
            self.remove(m, *m.get_family())
        self.add(*targets)

    def construct(self):
        # Opening intro beat: the player shows the TOPIC full-screen while
        # the tutor speaks the intro; board work must not start until the
        # intro lands. The exporter measures the first primitive's time and
        # the manifest publishes it as topic_display duration — this wait is
        # what makes that a designed beat instead of a coincidence.
        self.wait(4)

        # --- Band 0: Review and Introduction ---
        title = Tex("Factoring Quadratic Equations").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        expansion_text = Tex(r"Expansion: $(x+1)(x+2) \rightarrow x^2 + 3x + 2$").scale(1.1).shift(UP * 0.5)
        factoring_text = Tex(r"Factoring: $x^2 + 3x + 2 \rightarrow (x+1)(x+2)$").scale(1.1).shift(DOWN * 0.7)
        self.play(Write(expansion_text))
        self.wait(3)
        self.play(Write(factoring_text))
        self.wait(4)

        # --- Band 1: Standard form ---
        self.next_band(1)
        std_form_title = Tex("Standard Form").scale(1.2).shift(band_shift(1) + UP * 1.5)
        std_form = MathTex("a", "x^2 + ", "b", "x + ", "c", " = 0").scale(1.4).shift(band_shift(1))
        self.play(Write(std_form_title), Write(std_form))
        self.wait(3)

        # --- Band 2: The example problem and its coefficients ---
        self.next_band(2)
        eq_title = Tex("Example Problem").scale(1.2).shift(band_shift(2) + UP * 2)
        eq = MathTex("2", "x^2 + ", "5", "x + ", "3", " = 0").scale(1.4).shift(band_shift(2) + UP * 0.8)
        self.play(Write(eq_title), Write(eq))
        self.wait(2)
        coef_a = MathTex("a", "=", "2").scale(1.1).shift(band_shift(2) + LEFT * 3 + DOWN * 0.5)
        coef_b = MathTex("b", "=", "5").scale(1.1).shift(band_shift(2) + DOWN * 0.5)
        coef_c = MathTex("c", "=", "3").scale(1.1).shift(band_shift(2) + RIGHT * 3 + DOWN * 0.5)
        # Identify a, b, c by lifting each number out of the equation itself.
        self.play(
            Write(coef_a[0]), Write(coef_a[1]),
            Write(coef_b[0]), Write(coef_b[1]),
            Write(coef_c[0]), Write(coef_c[1]),
            TransformFromCopy(eq[0], coef_a[2]),
            TransformFromCopy(eq[2], coef_b[2]),
            TransformFromCopy(eq[4], coef_c[2]),
        )
        self.swap_in(coef_a, coef_b, coef_c,
                     loose=(coef_a[0], coef_a[1], coef_a[2],
                            coef_b[0], coef_b[1], coef_b[2],
                            coef_c[0], coef_c[1], coef_c[2]))
        self.wait(3)
        target_prod = MathTex(r"a \times c = 2 \times 3 = 6").scale(1.1).shift(band_shift(2) + LEFT * 2 + DOWN * 1.8)
        target_sum = MathTex("b = 5").scale(1.1).shift(band_shift(2) + RIGHT * 2.5 + DOWN * 1.8)
        self.play(Write(target_prod), Write(target_sum))
        self.wait(4)

        # --- Band 3: Finding the factor pair ---
        self.next_band(3)
        factors_text = Tex("Factors of 6 that add to 5:").scale(1.2).shift(band_shift(3) + UP * 1.3)
        factors_1 = Tex(r"$1 \times 6 = 6$, \quad $1 + 6 = 7$ \quad (No)").scale(1.1).shift(band_shift(3))
        factors_2 = Tex(r"$2 \times 3 = 6$, \quad $2 + 3 = 5$ \quad (Yes!)").scale(1.1).shift(band_shift(3) + DOWN * 1)
        self.play(Write(factors_text))
        self.wait(1)
        self.play(Write(factors_1))
        self.wait(2)
        self.play(Write(factors_2))
        self.wait(3)

        # --- Band 4: Split the middle term and group ---
        self.next_band(4)
        split_title = Tex("Split the middle term").scale(1.2).shift(band_shift(4) + UP * 1.8)
        eq_recall = MathTex("2x^2", "+", "5x", "+", "3", "=", "0").scale(1.3).shift(band_shift(4) + UP * 0.6)
        self.play(Write(split_title), Write(eq_recall))
        self.wait(1)
        # The 5x is about to be rewritten — flag it, then split it in place.
        self.play(Indicate(eq_recall[2]))
        eq_split = MathTex("2x^2", "+", "2x", "+", "3x", "+", "3", "=", "0").scale(1.3).shift(band_shift(4) + UP * 0.6)
        self.play(
            Transform(eq_recall[0], eq_split[0]),
            Transform(eq_recall[1], eq_split[1]),
            Transform(eq_recall[2], eq_split[2:5]),  # 5x becomes 2x + 3x
            Transform(eq_recall[3], eq_split[5]),
            Transform(eq_recall[4], eq_split[6]),
            Transform(eq_recall[5], eq_split[7]),
            Transform(eq_recall[6], eq_split[8]),
            run_time=1.4,
        )
        self.swap_in(eq_split, loose=(eq_recall,))
        self.wait(3)
        # The four terms drop into two bracketed pairs below (copies, so the
        # split line stays on the canvas above).
        group_full = MathTex("(", "2x^2 + 2x", ")", "+", "(", "3x + 3", ")", "=", "0").scale(1.3).shift(band_shift(4) + DOWN * 0.9)
        self.play(
            TransformFromCopy(eq_split[0:3], group_full[1]),
            TransformFromCopy(eq_split[3], group_full[3]),
            TransformFromCopy(eq_split[4:7], group_full[5]),
            TransformFromCopy(eq_split[7], group_full[7]),
            TransformFromCopy(eq_split[8], group_full[8]),
            FadeIn(group_full[0]), FadeIn(group_full[2]),
            FadeIn(group_full[4]), FadeIn(group_full[6]),
            run_time=1.4,
        )
        self.swap_in(group_full, loose=tuple(group_full[i] for i in range(9)))
        self.wait(3)

        # --- Band 5: Factor each group, spot the common binomial ---
        self.next_band(5)
        gcf_title = Tex("Factor out the GCF of each group").scale(1.1).shift(band_shift(5) + UP * 1.8)
        work = MathTex("(", "2x^2", "+", "2x", ")", "+", "(", "3x", "+", "3", ")",
                       "=", "0").scale(1.3).shift(band_shift(5) + UP * 0.5)
        self.play(Write(gcf_title), Write(work))
        self.wait(1)
        # Point at the shared factor of each pair before extracting it.
        self.play(Indicate(work[1]), Indicate(work[3]))   # 2x^2 and 2x share 2x
        self.play(Indicate(work[7]), Indicate(work[9]))   # 3x and 3 share 3
        factor_full = MathTex("2x", "(", "x", "+", "1", ")", "+", "3", "(", "x", "+", "1", ")",
                              "=", "0").scale(1.3).shift(band_shift(5) + UP * 0.5)
        # Extraction: each GCF slides out to the front of its bracket, the
        # quotients (x, 1) are what its terms morph into / leave behind.
        self.play(
            Transform(work[3], factor_full[0]),            # shared 2x slides out front
            Transform(work[0], factor_full[1]),
            Transform(work[1], factor_full[2]),            # 2x^2 / 2x leaves x
            Transform(work[2], factor_full[3]),
            TransformFromCopy(work[3], factor_full[4]),    # 2x / 2x leaves 1
            Transform(work[4], factor_full[5]),
            Transform(work[5], factor_full[6]),
            Transform(work[9], factor_full[7]),            # shared 3 slides out front
            Transform(work[6], factor_full[8]),
            Transform(work[7], factor_full[9]),            # 3x / 3 leaves x
            Transform(work[8], factor_full[10]),
            TransformFromCopy(work[9], factor_full[11]),   # 3 / 3 leaves 1
            Transform(work[10], factor_full[12]),
            Transform(work[11], factor_full[13]),
            Transform(work[12], factor_full[14]),
            run_time=1.8,
        )
        self.swap_in(factor_full, loose=(work, factor_full[4], factor_full[11]))
        self.wait(3)
        # "Look, these match": ring both binomials, then hold them in yellow.
        self.play(
            Circumscribe(factor_full[1:6], color=YELLOW),
            Circumscribe(factor_full[8:13], color=YELLOW),
            *[p.animate.set_color(YELLOW) for p in (*factor_full[1:6], *factor_full[8:13])],
        )
        self.wait(2)
        final_factored = MathTex("(x + 1)", "(", "2x", "+", "3", ")", "=", "0").scale(1.4).shift(band_shift(5) + DOWN * 1.2)
        final_factored[0].set_color(YELLOW)
        # The two matching binomials converge into the single (x + 1); the
        # leftover coefficients 2x and 3 fly down into the second bracket.
        merge_ghost = final_factored[0].copy()
        self.play(
            TransformFromCopy(factor_full[1:6], final_factored[0]),
            TransformFromCopy(factor_full[8:13], merge_ghost),
            TransformFromCopy(factor_full[0], final_factored[2]),
            TransformFromCopy(factor_full[6], final_factored[3]),
            TransformFromCopy(factor_full[7], final_factored[4]),
            TransformFromCopy(factor_full[13], final_factored[6]),
            TransformFromCopy(factor_full[14], final_factored[7]),
            FadeIn(final_factored[1]), FadeIn(final_factored[5]),
            run_time=1.5,
        )
        self.swap_in(final_factored,
                     loose=(merge_ghost, *[final_factored[i] for i in range(8)]))
        self.wait(4)

        # --- Band 6: Zero-product property — the equation splits in two ---
        self.next_band(6)
        zpp_title = Tex("Zero-Product Property").scale(1.2).shift(band_shift(6) + UP * 2)
        self.play(Write(zpp_title))
        self.wait(3)
        fact_recall = MathTex("(x + 1)", "(2x + 3)", "=", "0").scale(1.2).shift(band_shift(6) + UP * 1.3)
        fact_recall[0].set_color(YELLOW)
        self.play(Write(fact_recall))
        self.wait(1)
        eq1 = MathTex("x + 1", "=", "0").scale(1.2).shift(band_shift(6) + LEFT * 3 + UP * 0.5)
        eq2 = MathTex("2x + 3", "=", "0").scale(1.2).shift(band_shift(6) + RIGHT * 3 + UP * 0.5)
        # The factored equation literally splits apart: each factor flies to
        # its own linear equation, each getting an "= 0" of its own.
        self.play(
            Transform(fact_recall[0], eq1[0]),
            Transform(fact_recall[1], eq2[0]),
            Transform(fact_recall[2], eq1[1]),
            Transform(fact_recall[3], eq1[2]),
            TransformFromCopy(fact_recall[2], eq2[1]),
            TransformFromCopy(fact_recall[3], eq2[2]),
            run_time=1.4,
        )
        self.swap_in(eq1, eq2, loose=(fact_recall, eq2[1], eq2[2]))
        self.wait(3)
        # Each solution is worked out of its equation, not written beside it.
        sol1 = MathTex("x = -1").scale(1.2).shift(band_shift(6) + LEFT * 3 + DOWN * 0.7)
        self.play(TransformFromCopy(eq1, sol1))
        self.wait(2)
        step1_eq2 = MathTex("2x = -3").scale(1.2).shift(band_shift(6) + RIGHT * 3 + DOWN * 0.7)
        sol2 = MathTex("x = -\\frac{3}{2}").scale(1.2).shift(band_shift(6) + RIGHT * 3 + DOWN * 1.9)
        self.play(TransformFromCopy(eq2, step1_eq2))
        self.wait(2)
        self.play(TransformFromCopy(step1_eq2, sol2))
        self.wait(3)
        box1 = SurroundingRectangle(sol1, color=GREEN)
        box2 = SurroundingRectangle(sol2, color=GREEN)
        self.play(Create(box1), Create(box2))
        self.wait(5)

        # --- Band 7: Check the answer by working the substitution down ---
        self.next_band(7)
        check_title = Tex("Check").scale(1.2).shift(band_shift(7) + UP * 1.3)
        self.play(Write(check_title))
        c1 = MathTex("2(-1)^2", "+", "5(-1)", "+", "3").scale(1.1).move_to(band_shift(7))
        self.play(Write(c1))
        self.wait(1.5)
        # Each arithmetic step is done on the line itself.
        c2 = MathTex("2", "-", "5", "+", "3").scale(1.1).move_to(band_shift(7))
        self.play(
            Transform(c1[0], c2[0]),
            Transform(c1[1], c2[1]),
            Transform(c1[2], c2[2]),
            Transform(c1[3], c2[3]),
            Transform(c1[4], c2[4]),
        )
        self.swap_in(c2, loose=(c1,))
        self.wait(1.5)
        c3 = MathTex("-3", "+", "3", "=", "0", r"\checkmark").scale(1.1).move_to(band_shift(7))
        c3[5].set_color(GREEN)
        merge = c2[0:3]
        self.play(
            Transform(merge, c3[0]),   # 2 - 5 collapses into -3
            Transform(c2[3], c3[1]),
            Transform(c2[4], c3[2]),
        )
        self.swap_in(c3[0], c3[1], c3[2], loose=(c2, merge))
        # -3 and +3 cancel: strike both, fade them, and the zero remains.
        s1 = strike(c3[0])
        s2 = strike(VGroup(c3[1], c3[2]))
        self.play(Create(s1), Create(s2))
        self.play(
            c3[0].animate.set_opacity(0.35),
            c3[1].animate.set_opacity(0.35),
            c3[2].animate.set_opacity(0.35),
            Write(c3[3]), Write(c3[4]), Write(c3[5]),
        )
        self.wait(4)
