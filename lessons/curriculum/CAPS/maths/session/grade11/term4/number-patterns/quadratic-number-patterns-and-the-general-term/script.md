# Part 1 — Expert

Grade ten patterns grew by the same amount every step — linear, first difference constant, general term built on n. Grade eleven's patterns accelerate: the jumps themselves grow, but in a controlled way, and the control shows up one layer down, where the SECOND difference is constant. This session teaches the diagnosis, builds the general term T n equals a n squared plus b n plus c from any quadratic pattern, then runs the machine in both directions — finding terms from positions, positions from terms, and reading patterns out of stacked-tile pictures.

## Subtopic: First and Second Differences — the Diagnosis

Take the sequence 3; 8; 15; 24; 35. Check the first differences — each term minus the one before: 8 minus 3 is 5, then 7, then 9, then 11. Not constant, so the pattern is not linear. Now difference the differences: 7 minus 5 is 2, then 2, then 2. The second differences are constant, and that is the fingerprint: a constant second difference means a QUADRATIC pattern, one whose general term has the form T n equals a n squared plus b n plus c.

Why does squared produce exactly this signature? Look at the squares themselves: 1, 4, 9, 16, 25 have first differences 3, 5, 7, 9 — the odd numbers, climbing by 2 each time — so their second difference is the constant 2. Any quadratic in n inherits this behaviour: the n squared part contributes an ever-growing jump, growing by the same amount each step, while the b n plus c part contributes only constant jumps that vanish at the second layer.

The diagnosis procedure, then: difference once — constant means linear, stop. Difference twice — constant means quadratic. And the layers carry exact information: for a quadratic, the second difference equals TWO a, twice the coefficient of n squared. Second difference 2 means a is 1; second difference 6 would mean a is 3; second difference minus 4 would mean a is minus 2 and the pattern eventually turns downward.

One caution: three terms can look like anything. Compute differences from at least four terms — five when given — before announcing the type, and write both difference rows in your answer; the rows themselves earn marks.

Pause here — the questions for this section are with you now. Difference twice, name the type, and read a from half the second difference.

## Subtopic: Building the General Term

The target: T n equals a n squared plus b n plus c, and three facts pin down the three letters. The fastest route uses the structure of the difference table, and it is worth understanding, not just memorising.

Fact one: the second difference equals 2 a. For 3; 8; 15; 24; 35 the second difference is 2, so a equals 1.

Fact two: the FIRST first-difference — T 2 minus T 1 — equals 3 a plus b. Check it from the formula: T 2 is 4 a plus 2 b plus c, T 1 is a plus b plus c, and subtracting gives 3 a plus b. Here the first jump is 5, so 3 plus b equals 5, giving b equals 2.

Fact three: T 1 itself equals a plus b plus c. Here 1 plus 2 plus c equals 3, so c is 0. The general term: T n equals n squared plus 2 n. Test it beyond where you built it: T 4 should be 16 plus 8, which is 24 — matches. T 5 is 25 plus 10, which is 35 — matches. Always test on a term you did NOT use in the building.

Second worked example, with a dip: 6; 3; 2; 3; 6. First differences: minus 3, minus 1, 1, 3. Second difference: constant 2, so a is 1. First jump: 3 a plus b equals minus 3, so b equals minus 6. And a plus b plus c equals 6 gives 1 minus 6 plus c equals 6, so c is 11. T n equals n squared minus 6 n plus 11. Check T 4: 16 minus 24 plus 11 is 3 — matches. This pattern falls, bottoms out, and rises again — completing the square gives T n equals the quantity n minus 3 squared, plus 2, so the minimum term is T 3 equals 2, and the symmetry of the parabola explains the mirror-image sequence.

The alternative route — substituting n equals 1, 2, 3 to get three simultaneous equations — always works and matches this one; the difference-table route is simply faster and shows more method.

Stop for this section's questions now — half the second difference, then the first jump, then the first term: a, then b, then c, in that order.

## Subtopic: Using the General Term in Both Directions

A general term is a machine with two directions. Forward: feed in a position, receive a term. For T n equals n squared plus 2 n, the fiftieth term is 2 500 plus 100, which is 2 600. No listing of forty-nine intermediate terms — that is the machine's entire point.

Backward: given a term's VALUE, find its position. Which term equals 120? Set n squared plus 2 n equal to 120, so n squared plus 2 n minus 120 equals zero. Factorise: n plus 12, times n minus 10. So n is minus 12 or 10 — and here the pattern context imposes a rule the algebra does not know: n counts positions, so it must be a positive whole number. Reject minus 12 with a written reason. The tenth term is 120.

The backward direction also answers membership questions: is 200 a term of this pattern? Set n squared plus 2 n minus 200 equal to zero and test the discriminant: b squared minus 4 a c is 4 plus 800, which is 804 — not a perfect square, so n is irrational, and no position produces 200. The sentence to write: 200 is not a term, because the equation has no natural-number solution. Membership questions are quadratic equations wearing pattern clothing — the term three of last year's work returning in this year's uniform.

And when a is negative, the parabola opens downward and the pattern has a LARGEST term before descending — found at the turning point, by completing the square or symmetry, exactly as with our dipping pattern's minimum of 2 at position 3. The link to functions is deliberate: T n is a parabola sampled at whole numbers, and everything known about parabolas transfers.

The questions on this section are in front of you now — forward is substitution, backward is a quadratic equation, and n must always be a positive whole number.

## Subtopic: Patterns in Context — Tiles, Stacks and Real Counts

Examinations love to dress quadratic patterns in pictures: paving stones, stacked cans, growing rectangular decks. The method is always the same — count the first few figures, difference twice, build T n, then answer the questions in context.

The worked context: a builder lays rectangular tile decks. Figure 1 uses 3 tiles, figure 2 uses 8, figure 3 uses 15, figure 4 uses 24. These are our familiar numbers, so the work is done: T n equals n squared plus 2 n. But context offers a second route — see the STRUCTURE instead of differencing. Each figure n is a rectangle of n rows by n plus 2 columns: figure 1 is 1 by 3, figure 2 is 2 by 4, figure 3 is 3 by 5. Then T n equals n times n plus 2 — the same n squared plus 2 n, read straight off the geometry. When a picture has visible structure, the structural route is faster and impresses markers; the difference table is the guaranteed fallback.

Context questions then run the machine both ways. How many tiles in figure 20? Forward: 400 plus 40, which is 440 tiles. Which figure uses exactly 224 tiles? Backward: n squared plus 2 n minus 224 equals zero, factorising as n plus 16, times n minus 14, so n is 14 — figure 14, rejecting minus 16 since figures carry positive numbers. Could any figure use exactly 200 tiles? The discriminant test says no — and in context the sentence becomes: no figure uses exactly 200 tiles, since no whole-number position solves the equation.

Two context disciplines. Units and wording: answers are 440 TILES, figure 14 — echo the story. And check smallness by hand: your formula must reproduce figure 1 and figure 2 exactly; ten seconds of substitution catches a wrong c before it costs the whole question.

The final questions of this part are with you now — count, difference or read the structure, build the machine, and answer in the language of the story.

# Part 2 — Simplifier

Now the same machinery from a staircase and a filling taxi — same numbers, same formulae, with a picture for every move.

## Subtopic: The Fingerprint at the Second Layer

A detective identifies people by fingerprints; you identify patterns by difference rows. Line the sequence up and take the gaps: 3 to 8 is 5, 8 to 15 is 7, 15 to 24 is 9, 24 to 35 is 11. The gaps are growing — so this is not the grade ten kind, where every step repeats. But now check the gaps BETWEEN the gaps: 5 to 7, 7 to 9, 9 to 11 — always 2. Steady at the second layer. That steadiness is the fingerprint of a quadratic pattern: the family of n squared.

Think of climbing a strange staircase. The first step is 5 high, the next 7, the next 9 — every step taller than the last, but always by the same extra 2. The climb accelerates, yet the acceleration itself is constant. That is precisely what squared growth feels like: 1, 4, 9, 16, 25 — jumps of 3, 5, 7, 9, each jump 2 more than the last.

And the fingerprint does more than classify; it measures. The steady second-layer number is always DOUBLE the coefficient of n squared. See it in the simplest case: for n squared itself, second difference 2, coefficient 1 — double. Second difference 6? The pattern is built on 3 n squared. Second difference negative? The staircase eventually turns and comes back down. One number, read off the table, and you know the family and its leading coefficient before any algebra begins.

Just do not fingerprint from too few smudges: three terms cannot commit a pattern to anything. Take differences across every term you are given, write both rows, and let the steadiness show itself twice before you name it.

Quick check before we carry on — questions on this are with you right now. Gaps, then gaps of gaps, and read the family from the steady number.

## Subtopic: Three Screws Fix the Machine

The general term T n equals a n squared plus b n plus c is a machine with three screws, and the difference table hands you a screwdriver for each, in order.

Screw one, a: the steady second difference is exactly 2 a — halve it. Our staircase's steady 2 gives a equals 1.

Screw two, b: the very first gap — from term one to term two — is worth 3 a plus b. First gap 5, a already 1, so b is 2. Notice the order matters: b cannot be found before a, because a sits inside this equation.

Screw three, c: the first term itself is a plus b plus c — everything at position 1. Three plus c equals... careful: 1 plus 2 plus c equals 3, so c is 0. Machine assembled: T n equals n squared plus 2 n.

Now the two tests every assembled machine must pass. Reproduce a term you did NOT use in the assembly — T 4 gives 16 plus 8, which is 24, matching the list. And make the machine's claim make sense: at position 5 it predicts 35, and the list agrees. If either test fails, one screw is loose, and the order of suspicion is c first — it absorbs arithmetic slips — then b, then a.

For the dipping sequence 6; 3; 2; 3; 6, the same three screws give a is 1, b is minus 6, c is 11 — and the machine explains the dip: the pattern is a parabola visiting whole-number positions, sliding down to its lowest term, 2 at position 3, then climbing back up its own mirror image. Patterns are parabolas in disguise; everything you know about turning points comes along free.

Your questions for this part are up now — halve the steady number, then the first gap, then the first term, and always test the machine on unseen terms.

## Subtopic: Driving the Machine Forwards and in Reverse

A taxi's odometer converts a journey into a number. The general term is the same kind of instrument, and it drives both ways.

Forwards is effortless: want the fiftieth term? Feed 50 into n squared plus 2 n — 2 500 plus 100 — and 2 600 comes out. Nobody lists fifty terms; the whole point of building the machine was to skip the listing.

Reverse takes more care, because you are handed the reading and asked for the position. Which position shows 120? Set the machine equal to 120 and solve the quadratic: n squared plus 2 n minus 120 equals zero, which splits into n plus 12, times n minus 10. Algebra offers two answers, 10 and minus 12 — but positions are seats in a taxi: seat 10 exists, seat minus 12 does not. Reject the negative with a written reason, and answer: the tenth term.

Sometimes reverse gear reports that no seat exists at all. Is 200 ever shown on this odometer? The equation n squared plus 2 n minus 200 equals zero refuses to give a whole number — its discriminant, 804, is no perfect square — so 200 simply never appears in the pattern. Write that as a sentence, with the reason. It feels strange that a pattern can skip a number, but the staircase only lands where its steps land: 15, then 24 — it never touches 20.

And in the tiling story, reverse gear is the builder's question: which deck uses 224 tiles? Solve, get 14 and minus 16, keep 14, answer in context: figure 14. Forward for values, reverse for positions, context for the final sentence — the same machine, driven with intention, in whichever direction the question points.

And here come the last questions of the lesson, right now — feed positions forward, solve values backward, reject impossible seats aloud, and let the discriminant say when a number is simply never visited.
