# Part 1 — Expert

Sequences list numbers; series ADD them. This session upgrades both families of sequence into machinery for adding hundreds of terms in one line: sigma notation to say exactly what is being added, the arithmetic sum formula and the folding trick that proves it, the geometric sum formula, and the strangest result in the whole grade — an infinite list of numbers whose sum is a single finite value.

## Subtopic: Sigma Notation — Reading and Writing the Instruction

A series is the sum of the terms of a sequence, and sigma notation is the instruction set for building one. The capital sigma means add. Below it sits the counter and its starting value; above it, the stopping value; to its right, the recipe for each term. The sum from k equals 1 to 5 of the expression 2 k plus 1 means: let k run through 1, 2, 3, 4, 5, feed each into 2 k plus 1, and add the results. That is 3 plus 5 plus 7 plus 9 plus 11, which is 35.

Two mechanical facts carry most of the marks. First, the number of terms: the top value minus the bottom value, plus one. From k equals 1 to 5 there are five terms; from k equals 3 to 20 there are eighteen, not seventeen — the plus one counts both endpoints, the same fence-post counting as inserted means. Second, the counter is private: it can be k, i, or any letter, and it vanishes in the answer. The sum from k equals 1 to 5 of 2 k plus 1 and the sum from i equals 1 to 5 of 2 i plus 1 are the same number.

Writing a series IN sigma notation reverses the reading. Take 4 plus 7 plus 10, continuing to 61. The terms are arithmetic with a equal to 4 and d equal to 3, so the recipe is 3 k plus 1. The first term uses k equals 1; the last needs 3 k plus 1 equal to 61, so k is 20. The instruction: sum from k equals 1 to 20 of 3 k plus 1.

Pause here — the questions for this section are with you now. Count terms as top minus bottom plus one, build the recipe from the general term, and remember the counter is scaffolding, not part of the answer.

## Subtopic: The Arithmetic Sum — Folding the List in Half

The sum of the first n terms of a sequence is written S n. For arithmetic series there is a formula, and its proof is a trick worth owning because the examiner may ask for the derivation. Write the sum forwards: S n equals a, plus a plus d, and so on up to the last term l. Write it backwards underneath: l, plus l minus d, downwards to a. Add the two rows column by column. Every column gives the same total, a plus l — the small first term pairs with the large last term, the second with the second last, the deficits and surpluses cancelling exactly. There are n columns, so twice S n equals n times the quantity a plus l, and S n equals n over 2, times a plus l.

When the last term is not known, substitute l equals a plus n minus one d, giving the second form: S n equals n over 2, times the quantity 2 a plus n minus one d. Two forms, one formula: use a-plus-l when the last term is visible, and the 2 a form when only a and d are.

Worked forwards. The series 5 plus 8 plus 11, for forty terms: S 40 equals 40 over 2, times the quantity 2 times 5, plus 39 times 3. Inside the bracket: 10 plus 117, which is 127. Twenty times 127 is 2540.

Worked backwards, the exam favourite: how many terms of 2 plus 5 plus 8 add to 155? Set n over 2, times the quantity 4 plus 3 times n minus one, equal to 155. The bracket is 3 n plus 1, so n times 3 n plus 1 equals 310, giving the quadratic 3 n squared plus n minus 310 equals zero. The formula delivers n equals minus 1 plus or minus the square root of 3721, all over 6. The root of 3721 is 61, so n is 10 or a negative value, and a count of terms must be a positive natural number — n is 10. Check: S 10 is 5 times the quantity 4 plus 27, which is 155. Correct.

Stop for this section's questions now — fold the list to remember the formula, choose the form that matches what is given, and reject the negative root of the quadratic in writing.

## Subtopic: The Geometric Sum and Its Collapsing Proof

Geometric series have their own formula with its own beautiful proof. Let S n be a plus a r plus a r squared, up to a r to the power n minus one. Multiply the whole line by r: r S n is a r plus a r squared, up to a r to the power n. Subtract the second line from the first, and almost everything cancels — every term except the very first of one line and the very last of the other. So S n minus r S n equals a minus a r to the power n. Factor both sides: S n times one minus r equals a times one minus r to the power n, and therefore S n equals a times the quantity one minus r to the power n, all over one minus r. The twin form, with r minus one in the denominator and r to the n minus one on top, is the same formula multiplied through by minus one — use whichever keeps the denominator positive.

Worked case. The series 3 plus 6 plus 12, for ten terms: r is 2, so S 10 equals 3 times the quantity 2 to the tenth minus one, over 2 minus 1. Two to the tenth is 1024, so S 10 is 3 times 1023, which is 3069.

Backwards case. How many terms of 1 plus 2 plus 4 make 255? Set 2 to the power n, minus one, equal to 255, so 2 to the n is 256, which is 2 to the eighth: n is 8. Same-base exponents again — the sum formula plus the exponent techniques from the geometric sequence lesson solve the whole family.

One warning: the formula demands r not equal to one. If r is one, every term equals a and the sum is simply n times a — the formula's denominator would divide by zero precisely because the collapsing subtraction has nothing to cancel.

The questions on this section are in front of you now — multiply by r, subtract, and let the telescope collapse; then match bases when the question runs in reverse.

## Subtopic: Sum to Infinity — When Forever Adds Up

Add 8 plus 4 plus 2 plus 1 plus a half, and keep going forever. The running totals are 8, 12, 14, 15, 15 comma 5 — each step closes half the remaining gap to 16, and the total creeps toward 16 without ever passing it. Infinitely many positive numbers, finite total. The reason lives in the sum formula: S n equals a times the quantity one minus r to the n, over one minus r, and when r is between minus one and one, the r to the n part shrinks toward zero as n grows. Kill that term and the sum settles at S infinity equals a over one minus r. For our series: 8 over one minus a half, which is 16, exactly as the creeping totals promised.

The condition is everything: the sum to infinity EXISTS only when minus one is strictly less than r, strictly less than one, and r is not zero. Such a series is called convergent. If r is one or bigger the terms refuse to shrink and the total runs away to infinity; at r equal to minus one the totals bounce between two values and never settle.

Examiners test the condition directly. For which values of x does the series with ratio 2 x minus 1 converge? Demand minus one less than 2 x minus 1 less than one. Add one throughout: zero less than 2 x less than two, so zero less than x less than one, with r not zero excluded at x equal to a half. State the interval, then compute whatever sum the question wants.

The most satisfying application: recurring decimals. The decimal zero comma five five five repeating is the series five tenths, plus five hundredths, plus five thousandths — geometric with a equal to five tenths and r equal to one tenth. Sum to infinity: five tenths over nine tenths, which is five ninths. The recurring decimal IS a fraction, and the formula finds it.

The final questions of this part are with you now — check the ratio strictly between minus one and one before summing, solve the inequality when x is in the ratio, and turn any repeating decimal into a over one minus r.

# Part 2 — Simplifier

Now the same series from a stack of bricks and a shared bag of oranges — same formulas, same answers, built from things you can picture.

## Subtopic: The Instruction on the Crate

Sigma notation frightens people because it looks like a foreign alphabet, so read it as a packing instruction on a crate. The big sigma says: add things up. Underneath, where the counting starts. On top, where it stops. On the right, what each item looks like. Sum from k equals 1 to 5 of 2 k plus 1 says: for each k from one to five, make the number 2 k plus 1 and throw it in the crate. In go 3, 5, 7, 9 and 11. Total: 35.

How many items are in the crate? Stop value minus start value, plus one. From 3 to 20 is eighteen items, because both ends are included — count the oranges from the third to the twentieth in a row and you will touch eighteen oranges, not seventeen. Forgetting the plus one is the single most common error in this topic, and it is the fence-post miscount wearing new clothes.

And the letter k? It is the tally on the packer's clipboard. Once the crate is packed, the clipboard is wiped — the answer never contains k. Swap k for i or for m and the crate holds exactly the same numbers.

Quick check before we carry on — questions on reading the instruction are coming to you right now. Start at the bottom, stop at the top, build each item from the recipe, and count items with the plus one.

## Subtopic: Gauss Folds the Queue

The story goes that a teacher, wanting quiet, told the class to add every number from 1 to 100 — and one learner answered almost at once: 5050. The learner's trick is the whole arithmetic sum formula. Fold the queue. Pair the first number with the last: 1 plus 100 is 101. Pair the second with the second last: 2 plus 99 is 101. Every pair gives 101, and a hundred numbers make fifty pairs: fifty times 101 is 5050.

The formula S n equals n over 2 times a plus l is that fold written in symbols — n over 2 pairs, each worth first plus last. When you cannot see the last term, swap in a plus n minus one d for l and get the working form: n over 2, times 2 a plus n minus one d. Nothing to memorise blindly; if you can fold a queue, you can rebuild the formula in the margin.

Use it on something real. A brick stack has 5 bricks in the top row, 8 in the next, 11 in the next, forty rows down. Total bricks: 40 over 2, times 10 plus 39 times 3 — twenty times 127, which is 2540 bricks. Now backwards: charity envelopes collect 2 rand, then 5, then 8, each envelope 3 rand more; how many envelopes to reach exactly 155 rand? The formula hands you a quadratic, 3 n squared plus n minus 310 equals zero, and the formula for quadratics gives 10 or a negative number. Envelopes cannot be negative, so ten envelopes — and always say why you dropped the other root.

Your questions for this part are up now. Fold, pair, count the pairs — and when the answer must count real things, throw the negative root out by name.

## Subtopic: Half the Oranges, Forever

Here is the puzzle that makes infinity behave. A bag holds 16 oranges. Someone takes half the bag: 8. Then half of what remains: 4. Then half again: 2, then 1, then a half orange, forever. Add up everything ever taken: 8 plus 4 plus 2 plus 1 and on and on. The total can never PASS 16 — there was only ever one bag — and it creeps as close to 16 as you like. So the infinite sum is exactly 16. Forever added up, and it came to a number.

The machine behind it: each taking is the previous times a half, a geometric series with r equal to one half. Whenever the ratio is a genuine fraction — strictly between minus one and one — the leftover shrinks to nothing and the total settles at a over one minus r. Eight over one minus a half is 16. But let the ratio reach one or beyond, and each taking no longer shrinks: the pile grows without limit and no final number exists. The condition minus one less than r less than one is not fine print; it is the difference between a bag with a bottom and a bag without one.

The party trick that earns real marks: zero comma five five five repeating. That decimal is takings of five tenths, five hundredths, five thousandths — ratio one tenth. Total: five tenths over nine tenths, which is five ninths. Punch 5 divided by 9 into a calculator and watch the fives repeat. Every repeating decimal is an infinite geometric series that has already converged; the formula just tells you to which fraction.

And here come the last questions of the lesson, right now: check that the ratio is a genuine fraction before promising a total, creep-to-a-limit means a over one minus r, and let repeating decimals confess the fraction they have been all along.
