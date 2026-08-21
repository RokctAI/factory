# Part 1 — Expert

A sequence lists numbers; a series ADDS them. This session turns both sequence families into machinery for summing hundreds of terms in a single line: sigma notation to state precisely what is being added, the arithmetic sum formula with the folding argument that proves it, the geometric sum formula with its collapsing proof, and the most startling theorem of the year — an endless list of numbers whose total is a single finite value.

## Subtopic: Sigma Notation — Reading and Writing the Instruction

A series is the sum of a sequence's terms, and sigma notation is the instruction that builds one. The capital sigma commands: add. Beneath it sit the counter and its starting value; above it, the stopping value; beside it, the recipe for each term. The sum from k equals 1 to 6 of the expression 3 k plus 2 says: let k walk through 1, 2, 3, 4, 5, 6, feed each into 3 k plus 2, and add what comes out. That is 5 plus 8 plus 11 plus 14 plus 17 plus 20, which is 75.

Two mechanical facts carry most of the marks in this notation. First, the count of terms: top value minus bottom value, plus one. From k equals 1 to 6 there are six terms; from k equals 4 to 25 there are twenty-two, not twenty-one — the plus one includes both endpoints, the same fence-post count that governed inserted means. Second, the counter is disposable: call it k, i or m, the sum is identical, and the letter never survives into the answer.

Writing a series IN sigma notation runs the reading in reverse. Take 7 plus 11 plus 15, continuing up to 83. The terms are arithmetic with a equal to 7 and d equal to 4, so the recipe is 4 k plus 3. The first term uses k equals 1; the last demands 4 k plus 3 equal to 83, so k is 20. The instruction: sum from k equals 1 to 20 of 4 k plus 3.

Pause here — the questions for this section are with you now. Count terms as top minus bottom plus one, build the recipe from the general term, and treat the counter as scaffolding that never reaches the answer.

## Subtopic: The Arithmetic Sum — Folding the List in Half

The sum of the first n terms is written S n, and for arithmetic series a formula exists whose proof is a trick worth owning, since the derivation itself can be asked. Write the sum forwards: S n equals a, plus a plus d, marching up to the last term l. Write it again backwards underneath: l, plus l minus d, marching down to a. Add the two rows column by column. Every column totals the same amount, a plus l — the smallest term pairs with the largest, the second smallest with the second largest, every deficit cancelling a surplus. With n columns, twice S n equals n times the quantity a plus l, so S n equals n over 2, times a plus l.

When the last term is hidden, substitute l equals a plus n minus one d to get the working form: S n equals n over 2, times the quantity 2 a plus n minus one d. One formula, two costumes: wear a-plus-l when the last term shows itself, and the 2 a form when only a and d do.

Forwards case. The series 6 plus 10 plus 14, taken to thirty terms: S 30 equals 30 over 2, times the quantity 2 times 6, plus 29 times 4. Inside the bracket: 12 plus 116, which is 128. Fifteen times 128 is 1920.

Backwards case, the exam favourite: how many terms of 3 plus 7 plus 11 add up to 210? Set n over 2, times the quantity 6 plus 4 times n minus one, equal to 210. The bracket is 4 n plus 2, so n times 2 n plus 1 equals 210, giving the quadratic 2 n squared plus n minus 210 equals zero. The formula delivers n equals minus 1 plus or minus the square root of 1681, all over 4. The root of 1681 is 41, so n is 10 or a negative value — and a count of terms must be a positive natural number, so n is 10. Check: S 10 is 5 times the quantity 6 plus 36, which is 210. Correct.

Stop for this section's questions now — fold the list to reconstruct the formula, pick the costume that matches the given data, and dismiss the negative root in writing.

## Subtopic: The Geometric Sum and Its Collapsing Proof

The geometric series has its own formula and its own elegant proof. Let S n be a plus a r plus a r squared, up to a r to the power n minus one. Multiply the entire line by r: r S n is a r plus a r squared, up to a r to the power n. Subtract the second line from the first and watch the middle collapse — every term cancels except the first of one row and the last of the other. So S n minus r S n equals a minus a r to the power n. Factor both sides: S n times one minus r equals a times one minus r to the power n, and therefore S n equals a times the quantity one minus r to the power n, all over one minus r. The twin version, r to the n minus one over r minus one, is the same formula multiplied through by minus one — choose whichever keeps the denominator positive.

Worked case. The series 2 plus 6 plus 18, for nine terms: r is 3, so S 9 equals 2 times the quantity 3 to the ninth minus one, over 3 minus 1. Three to the ninth is 19 683, so S 9 is 19 682 — the twos cancel beautifully.

Backwards case. How many terms of 3 plus 6 plus 12 make 381? The sum is 3 times the quantity 2 to the n minus one, so set 2 to the n, minus one, equal to 127: then 2 to the n is 128, which is 2 to the seventh, and n is 7. Same-base exponents once more — the sum formula and the exponent skills from the geometric sequence lesson work as a team.

One warning: the formula requires r not equal to one. When r is one, every term equals a and the sum is simply n times a — the denominator's division by zero is the algebra's way of saying the collapsing subtraction had nothing to collapse.

The questions on this section are in front of you now — multiply by r, subtract, let the telescope fold shut, and match bases when the question runs backwards.

## Subtopic: Sum to Infinity — When Forever Adds Up

Add 27 plus 9 plus 3 plus 1 plus a third, and never stop. The running totals read 27, then 36, then 39, then 40, then 40 and a third — every step closes two thirds of the remaining distance to 40,5, and the total creeps toward 40,5 without ever passing it. Infinitely many positive numbers, one finite destination. The mechanism sits inside the sum formula: S n equals a times the quantity one minus r to the n, over one minus r, and when r lies strictly between minus one and one, the term r to the n withers toward zero as n grows. Remove it and the sum settles at S infinity equals a over one minus r. For this series: 27 over one minus a third, which is 27 over two thirds, giving 40,5 — exactly where the totals were creeping.

The condition is the whole story: the sum to infinity EXISTS only when minus one is strictly less than r, strictly less than one, with r not zero. Such a series is called convergent. Let r reach one or beyond and the terms refuse to shrink, so the total runs off to infinity; at r equal to minus one the totals oscillate between two values and never choose.

The condition gets examined directly. For which values of x does a series with ratio 3 x minus 2 converge? Demand minus one less than 3 x minus 2 less than one. Add two throughout: one less than 3 x less than three, so one third less than x less than one, with the ratio-not-zero exclusion at x equal to two thirds. State the interval first, then compute whatever sum is requested.

The most satisfying customer: recurring decimals. The decimal zero comma seven seven seven repeating is the series seven tenths, plus seven hundredths, plus seven thousandths — geometric with a equal to seven tenths and r equal to one tenth. Sum to infinity: seven tenths over nine tenths, which is seven ninths. The repeating decimal IS a fraction, and the formula names it.

The final questions of this part are with you now — verify the ratio sits strictly between minus one and one before promising a total, solve the inequality when x lives in the ratio, and let every repeating decimal confess its fraction through a over one minus r.

# Part 2 — Simplifier

Now the same series from a packing crate and a shared bag of oranges — identical formulas, identical answers, built from things you can picture.

## Subtopic: The Instruction on the Crate

Sigma notation intimidates because it looks imported from another alphabet, so read it as the packing instruction stapled to a crate. The big sigma says: pack and add. Below it, where the counting starts. On top, where it stops. To the right, what each packed item looks like. Sum from k equals 1 to 6 of 3 k plus 2 says: for each k from one to six, manufacture the number 3 k plus 2 and drop it in the crate. In go 5, 8, 11, 14, 17 and 20. Total: 75.

How many items does a crate hold? Stop value minus start value, plus one. From k equals 4 to 25 that is twenty-two items, because both ends count — number the boxes in a row from the fourth to the twenty-fifth and your finger touches twenty-two boxes, not twenty-one. Dropping the plus one is the most common slip in this entire topic, and it is the fence-post miscount in a new uniform.

And the letter k? It is the packer's tally sheet. Once the crate is sealed, the tally sheet goes in the bin — no answer ever contains k. Swap k for i or for m and the crate holds exactly the same cargo.

Quick check before we carry on — questions on reading the instruction are coming to you right now. Start at the bottom, stop at the top, build each item from the recipe, and count the cargo with the plus one.

## Subtopic: Gauss Folds the Queue

An old story tells of a teacher who, wanting a quiet hour, ordered the class to add every number from 1 to 100 — and one child stood up almost immediately with 5050. The child's move is the entire arithmetic sum formula. Fold the queue. Pair the front number with the back one: 1 plus 100 is 101. Pair the second with the second last: 2 plus 99 is 101. Every pair totals 101, and one hundred numbers make fifty pairs: fifty times 101 is 5050.

The formula S n equals n over 2 times a plus l is that fold in symbols — n over 2 pairs, each worth first plus last. When the last term hides, replace l with a plus n minus one d and use the working costume: n over 2, times 2 a plus n minus one d. Nothing here needs blind memorising; anyone who can fold a queue can rebuild the formula in a margin.

Put it to work. A wall of bricks has 6 bricks in its top row, 10 in the next, then 14, for thirty rows. Total bricks: 30 over 2, times 12 plus 29 times 4 — fifteen times 128, which is 1920 bricks. Now backwards: a fundraising drive collects 3 rand in envelope one, 7 in the next, then 11, each envelope 4 rand more; how many envelopes reach exactly 210 rand? The formula produces the quadratic 2 n squared plus n minus 210 equals zero, and solving gives 10 or a negative number. Envelopes cannot be negative, so ten envelopes — and always write down why the other root died.

Your questions for this part are up now. Fold, pair, count the pairs — and when the answer counts real objects, execute the negative root by name.

## Subtopic: Half the Oranges, Forever

Here is the puzzle that teaches infinity manners. A bag holds 24 oranges. Someone takes half the bag: 12. Then half of what remains: 6. Then half again: 3, then one and a half, then three quarters, without end. Add every taking: 12 plus 6 plus 3 and onwards forever. The total can never EXCEED 24 — there was only ever one bag — yet it creeps as close to 24 as anyone demands. So the infinite sum is exactly 24. Forever, added up, came to a number.

The machine underneath: each taking is the previous one times a half — a geometric series with r equal to one half. Whenever the ratio is a genuine fraction, strictly between minus one and one, the leftover shrivels to nothing and the total settles at a over one minus r. Twelve over one minus a half is 24. But push the ratio to one or beyond and the takings stop shrinking: the pile grows without ceiling and no final number exists. The condition minus one less than r less than one is not decoration; it is the difference between a bag with a bottom and a bag without one.

The party trick that banks real marks: zero comma seven seven seven repeating. That decimal is takings of seven tenths, seven hundredths, seven thousandths — ratio one tenth. Total: seven tenths over nine tenths, which is seven ninths. Type 7 divided by 9 into a calculator and watch the sevens march. Every repeating decimal is an infinite geometric series that finished converging long ago; the formula simply reveals which fraction it has been all along.

And here come the last questions of the lesson, right now: confirm the ratio is a genuine fraction before promising a total, creep-to-a-limit means a over one minus r, and make every repeating decimal admit the fraction it truly is.
