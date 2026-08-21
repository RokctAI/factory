# Part 1 — Expert

Last year every pattern you met grew by the same amount at every step — linear, first difference constant, general term hanging off n. This year the patterns pick up speed: each jump is bigger than the one before, yet the speeding-up itself is perfectly regular, and that regularity lives one layer down, where the SECOND difference settles to a constant. This session teaches you to diagnose that signature, to assemble the general term T n equals a n squared plus b n plus c from any quadratic sequence, and then to run the finished formula in both directions — positions into terms, term values back into positions — before finishing inside picture patterns built from bricks and rows.

## Subtopic: First and Second Differences — the Diagnosis

Start with the sequence 4; 10; 18; 28; 40. Take the first differences — each term minus its predecessor: 10 minus 4 is 6, then 8, then 10, then 12. They are not constant, so this is not a linear pattern. Now difference the differences: 8 minus 6 is 2, then 2 again, then 2 again. The second differences hold steady, and that steadiness is the diagnostic signature: a constant second difference announces a QUADRATIC pattern, whose general term takes the shape T n equals a n squared plus b n plus c.

Why does squaring leave exactly this trace? Watch the squares themselves: 1, 4, 9, 16, 25 climb by 3, then 5, then 7, then 9 — the odd numbers, each one exactly 2 more than the last — so the squares carry a constant second difference of 2. Any quadratic in n behaves the same way: the n squared piece supplies jumps that grow by a fixed amount every step, while the b n plus c piece supplies only steady jumps that disappear entirely at the second layer.

So the diagnosis runs: difference once — constant means linear, and you stop there. Difference again — constant at the second layer means quadratic. Better still, the layer carries a measurement, not just a label: the constant second difference is exactly TWO a, double the coefficient of n squared. A second difference of 2 forces a equals 1. A second difference of 8 forces a equals 4. A second difference of minus 6 forces a equals minus 3, and warns you the pattern will eventually crest and fall.

One warning before you commit: any three terms can be fitted by almost anything. Build your difference rows from at least four terms — all five when five are printed — and write both rows into your answer, because the rows themselves carry marks.

Pause here — the questions for this section are with you now. Difference twice, name the type, and halve the steady number to read a.

## Subtopic: Building the General Term

The target is T n equals a n squared plus b n plus c, and three facts, read straight off the difference table, pin down the three unknowns. The route is fast, but it deserves understanding rather than memorising.

Fact one: the second difference equals 2 a. For 4; 10; 18; 28; 40 the second difference is 2, so a equals 1.

Fact two: the very FIRST first-difference — T 2 minus T 1 — equals 3 a plus b. Derive it once from the formula: T 2 is 4 a plus 2 b plus c, T 1 is a plus b plus c, and the subtraction leaves 3 a plus b. Our first jump is 6, so 3 plus b equals 6, and b equals 3.

Fact three: T 1 itself equals a plus b plus c. Here 1 plus 3 plus c equals 4, so c equals 0. Assembled: T n equals n squared plus 3 n. Now test it on a term that played no part in the building: T 4 should be 16 plus 12, which is 28 — it matches. T 5 gives 25 plus 15, which is 40 — matches again. A formula tested only on the terms that built it has proved nothing; always test on an unused term.

A second worked example, this time with a dip: 12; 7; 4; 3; 4. First differences: minus 5, minus 3, minus 1, 1. Second difference: a steady 2, so a equals 1. First jump: 3 a plus b equals minus 5, so b equals minus 8. Then a plus b plus c equals 12 gives 1 minus 8 plus c equals 12, so c equals 19. The general term: T n equals n squared minus 8 n plus 19. Check T 5: 25 minus 40 plus 19 is 4 — correct. This sequence slides down, touches bottom, and climbs back up — and completing the square shows why: T n equals the quantity n minus 4 squared, plus 3, so the smallest term is T 4 equals 3, and the mirror symmetry either side of position four is the symmetry of a parabola.

The fallback route — substitute n equals 1, 2 and 3 into a n squared plus b n plus c and solve three simultaneous equations — always works and always agrees; the difference-table facts are simply quicker and display more method.

Stop for this section's questions now — halve the second difference for a, feed a into the first jump for b, feed both into the first term for c.

## Subtopic: Using the General Term in Both Directions

A general term is an engine that runs two ways. Forward: give it a position, it returns the term. For T n equals n squared plus 3 n, the fiftieth term is 2 500 plus 150 — 2 650 — with no need to list the forty-nine terms in between. Skipping the list is the entire reason the formula exists.

Backward: given a term's VALUE, recover its position. Which term equals 130? Set n squared plus 3 n equal to 130, so n squared plus 3 n minus 130 equals zero. It factorises: n plus 13, times n minus 10. So n is minus 13 or 10 — and now the pattern imposes a condition the algebra cannot see: n numbers positions, so it must be a positive whole number. Reject minus 13, in writing, with that reason. The tenth term is 130.

The backward direction also settles membership questions: does 150 ever appear in this pattern? Set n squared plus 3 n minus 150 equal to zero and consult the discriminant: b squared minus 4 a c is 9 plus 600, which is 609 — not a perfect square, so the roots are irrational and no counting number solves the equation. Write the sentence: 150 is not a term, because no natural-number position produces it. Membership questions are quadratic equations dressed as patterns — the nature-of-roots theory you already own, reporting for new duty.

When a is negative the parabola opens downward, and the pattern owns a LARGEST term at its turning point before descending — found by completing the square or by symmetry, exactly as our dipping sequence revealed its minimum of 3 at position four. The connection is deliberate: T n is a parabola sampled at the whole numbers, and every fact you know about parabolas transfers for free.

The questions on this section are in front of you now — substitute forward, solve a quadratic backward, and keep n positive and whole every time.

## Subtopic: Patterns in Context — Tiles, Stacks and Real Counts

Assessments love to costume quadratic patterns as pictures: paving bricks, stacked crates, growing seating banks. The method never changes — count the first figures, difference twice, build T n, then answer in the story's own language.

The worked context: a landscaper lays rectangular brick pads. Pad 1 uses 4 bricks, pad 2 uses 10, pad 3 uses 18, pad 4 uses 28. These are our opening numbers, so the algebra is already done: T n equals n squared plus 3 n. But pictures offer a second route — read the STRUCTURE instead of differencing. Pad n is a rectangle n rows deep and n plus 3 bricks wide: pad 1 is 1 by 4, pad 2 is 2 by 5, pad 3 is 3 by 6. So T n equals n times n plus 3 — expand it and the same n squared plus 3 n appears, straight from the geometry. When the structure is visible, reading it is faster and shows insight; the difference table remains the guaranteed fallback for any picture, visible structure or not.

Context questions then drive the engine both ways. How many bricks in pad 20? Forward: 400 plus 60, which is 460 bricks. Which pad uses exactly 154 bricks? Backward: n squared plus 3 n minus 154 equals zero, factorising as n plus 14, times n minus 11, so n equals 11 — pad eleven, with minus 14 rejected because pads carry positive numbers. Could a pad use exactly 150 bricks? The discriminant answers no — and in context the sentence becomes: no pad uses exactly 150 bricks, because no whole-number pad position solves the equation.

Two context habits protect your marks. Speak the story's language, with units: 460 BRICKS, pad eleven — never a bare number. And verify small cases by hand: your formula must reproduce pads one and two exactly, and ten seconds of substitution exposes a wrong c before it poisons every later answer.

The final questions of this part are with you now — count, difference or read the structure, build the engine, and answer inside the story.

# Part 2 — Simplifier

Now the same machinery again, through a staircase and a delivery van — same numbers, same formulae, and a picture attached to every move.

## Subtopic: The Fingerprint at the Second Layer

A detective identifies a visitor by the fingerprint left behind; you identify a pattern by its difference rows. Lay the sequence out and measure the gaps: 4 to 10 is 6, 10 to 18 is 8, 18 to 28 is 10, 28 to 40 is 12. Growing gaps — so this is not last year's kind, where every step repeated. But now measure the gaps BETWEEN the gaps: 6 to 8, 8 to 10, 10 to 12 — always 2. Steady at the second layer. That steadiness is the fingerprint of a quadratic pattern — the family built on n squared.

Picture an unusual staircase. The first step rises 6, the next 8, the next 10 — every step taller than the last, but always taller by the same extra 2. The climb accelerates, yet the acceleration never changes. That is exactly what squared growth feels like: 1, 4, 9, 16, 25, with jumps of 3, 5, 7, 9, each jump 2 more than the one before.

And the fingerprint measures as well as identifies. The steady second-layer number is always DOUBLE the coefficient of n squared. Confirm it on the simplest case: n squared itself has second difference 2 and coefficient 1 — double. A steady 8 at the second layer? The pattern is built on 4 n squared. A steady negative number? The staircase eventually turns and walks back down. One number from the table, and you know both the family and its leading coefficient before touching any algebra.

Only never fingerprint from too few smudges: three terms commit a pattern to nothing. Difference across every printed term, write both rows, and let the steadiness confirm itself at least twice before you name the type.

Quick check before we move on — questions on this are with you right now. Gaps, then gaps of gaps, and read the family from the steady number.

## Subtopic: Three Screws Fix the Machine

The general term T n equals a n squared plus b n plus c is a machine held together by three screws, and the difference table hands you the right screwdriver for each, in a fixed order.

Screw one, a: the steady second difference is exactly 2 a — so halve it. Our staircase's steady 2 gives a equals 1.

Screw two, b: the very first gap — from term one to term two — is worth 3 a plus b. First gap 6, and a already fixed at 1, so b equals 3. The order is not optional: b cannot be tightened before a, because a sits inside b's equation.

Screw three, c: the first term itself equals a plus b plus c — the whole formula standing at position one. So 1 plus 3 plus c equals 4, and c equals 0. Machine assembled: T n equals n squared plus 3 n.

Every assembled machine must then pass two tests. Reproduce a term you did NOT use during assembly — T 4 returns 16 plus 12, which is 28, matching the list. And check the far end: at position five the machine predicts 40, and the list agrees. If a test fails, one screw is loose, and suspicion runs in order: c first, because it absorbs small arithmetic slips, then b, then a.

For the dipping sequence 12; 7; 4; 3; 4, the same three screws deliver a equals 1, b equals minus 8, c equals 19 — and the machine explains the dip: the pattern is a parabola visiting the whole numbers, sliding to its lowest value, 3 at position four, then climbing back up its own reflection. Patterns are parabolas in disguise, and everything you know about turning points rides along free of charge.

Your questions for this part are up now — halve the steady number, then the first gap, then the first term, and always test the machine on terms it has never seen.

## Subtopic: Driving the Machine Forwards and in Reverse

A delivery van's trip meter turns a journey into a single reading. The general term is the same kind of instrument, and it drives in both directions.

Forwards is effortless: want the fiftieth term? Feed 50 into n squared plus 3 n — 2 500 plus 150 — and out comes 2 650. Nobody lists fifty terms to get there; skipping the list is the machine's whole purpose.

Reverse asks for more care, because you hold the reading and must recover the position. Which position shows 130? Set the machine equal to 130 and solve: n squared plus 3 n minus 130 equals zero, which splits into n plus 13, times n minus 10. The algebra offers two answers, 10 and minus 13 — but positions are parking bays outside the depot: bay 10 exists, bay minus 13 does not. Reject the negative with a written reason, and answer: the tenth term.

Sometimes reverse gear reports that no bay exists at all. Does the meter ever read 150? The equation n squared plus 3 n minus 150 equals zero refuses to produce a whole number — its discriminant, 609, is not a perfect square — so 150 simply never appears in this pattern. Write that as a sentence with its reason. It can feel strange that a pattern skips numbers, but the staircase only lands where its steps land: 18, then 28 — it never touches 22.

And in the paving story, reverse gear is the landscaper's question: which pad needs 154 bricks? Solve, obtain 11 and minus 14, keep 11, and answer in context: pad eleven. Forward for values, reverse for positions, context wording for the finish — one machine, driven deliberately, in whichever direction the question points.

And here come the last questions of the lesson, right now — feed positions forward, solve values backward, reject impossible bays aloud, and let the discriminant declare when a number is never visited at all.
