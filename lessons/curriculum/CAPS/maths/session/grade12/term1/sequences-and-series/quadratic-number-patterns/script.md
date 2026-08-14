# Part 1 — Expert

Grade twelve opens with a piece of grade eleven business that Paper 1 refuses to let go of: the quadratic number pattern, where the SECOND difference is constant. It sits at the front of the sequences section almost every year, and it rewards a fixed drill. Four pieces of equipment by the end: the difference table that sorts linear patterns from quadratic ones, the three equations that recover a, b and c in T n equals a n squared plus b n plus c, the algebra that finds which position holds a given value, and the two exam favourites — an unknown hiding inside the terms, and the term where a pattern bottoms out.

## Subtopic: The Difference Table Verdict

Every number-pattern question starts the same way: line the terms up and subtract neighbours. Take 3; 7; 11; 15. First differences: 7 minus 3 is 4, 11 minus 7 is 4, 15 minus 11 is 4. Constant at the first level, so the pattern is linear, and its general term takes the shape T n equals d n plus c. The recipe from grade eleven still works: the coefficient of n is the constant difference, 4, and the constant is the first term minus that difference, 3 minus 4, which is minus 1. So T n equals 4 n minus 1, written in one line, and tested on a visible term: T4 is four fours minus one, 15. Correct.

Now take 6; 15; 28; 45. First differences: 15 minus 6 is 9, 28 minus 15 is 13, 45 minus 28 is 17. Not constant, so not linear. Go one level deeper and subtract the differences themselves. Second differences: 13 minus 9 is 4, and 17 minus 13 is 4. Constant at the SECOND level, so the pattern is quadratic, and its general term takes the shape T n equals a n squared plus b n plus c.

That is the whole verdict rule. Constant first difference: linear. Constant second difference: quadratic. Two disciplines attach to it. Subtract in order, each term minus the one before it, so a decreasing pattern shows its negative differences honestly. And demand at least four terms before announcing a quadratic, because four terms give three first differences and two second differences — one matching pair at the second level, not just a single number standing alone.

Pause here — the questions for this section are with you now. Build the table, subtract in order, and let the level where the differences settle name the pattern.

## Subtopic: Three Equations Recover a, b and c

Once a pattern is certified quadratic, the general term T n equals a n squared plus b n plus c is waiting, and three facts pin down its three letters. Substitute positions one, two and three into the shape: T1 is a plus b plus c. T2 is 4 a plus 2 b plus c. T3 is 9 a plus 3 b plus c. Subtracting down the list turns those into the three working equations. The second difference equals 2 a. The first of the first differences, T2 minus T1, equals 3 a plus b. And T1 itself equals a plus b plus c. Solve them in exactly that order — a first, then b, then c — and each equation hands you one new letter.

Run the machine on 6; 15; 28; 45. The second difference is 4, so 2 a is 4 and a is 2. The first of the first differences is 9, so 3 a plus b is 9; three twos make 6, so b is 3. The first term is 6, so a plus b plus c is 6; two plus three is five, so c is 1. The general term is T n equals 2 n squared plus 3 n plus 1.

Never leave that line unchecked. Test it on a term the formula has not met: T3 should be 28, and two nines are 18, plus three threes, 9, plus 1 — and 18 + 9 + 1 = 28. Certified. Now the formula earns its keep on a position no table reaches: T50 is two times 2 500, which is 5 000, plus 150, plus 1 — and 5000 + 150 + 1 = 5151. Term fifty is 5 151, found in one line.

Stop for this section's questions now — half the second difference gives a, the first gap gives b through 3 a plus b, the first term gives c, and a check on a visible term certifies all three.

## Subtopic: Which Position Holds a Given Value

The reverse question carries the most marks: a value is named, and the position must be found. The method never changes — set T n equal to the value and solve the quadratic equation, then interrogate the answer.

Which term of 2 n squared plus 3 n plus 1 equals 190? Set it up: 2 n squared plus 3 n plus 1 equals 190, so 2 n squared plus 3 n minus 189 equals 0. This factorises: two n plus twenty-one, times n minus nine, equals zero. So n is 9, or n is minus 10,5. A position must be a natural number, so minus 10,5 is discarded without ceremony, and the answer is term nine. Confirm it: T9 is two times 81, which is 162, plus 27, plus 1 — and 162 + 27 + 1 = 190. Correct.

Now the trap version: is 300 a term of the same pattern? Set 2 n squared plus 3 n plus 1 equal to 300, so 2 n squared plus 3 n minus 299 equals 0. The discriminant is 9 plus 2 392, which is 2 401, and its square root is 49. Then n is minus 3 plus 49, over 4, which is 11,5 — or a negative value, discarded. And 11,5 is not a natural number either. Conclusion, written as a sentence: since n is not a natural number, 300 is not a term of the pattern. The pattern actually confirms it. T11 is 242 plus 33 plus 1, and 242 + 33 + 1 = 276. T12 is 288 plus 36 plus 1, and 288 + 36 + 1 = 325. The pattern steps from 276 straight to 325 and never lands on 300. Rounding 11,5 to 12 would claim that 325 and 300 are the same number — the sentence, not a rounded n, is the answer.

The questions on this section are in front of you now — set T n equal to the value, solve the quadratic, and let n prove itself a natural number before you accept it.

## Subtopic: Hidden Unknowns and the Smallest Term

Two exam patterns close this part. The first hides an unknown inside the terms. The pattern x; 13; 30; 53 is quadratic with a constant second difference of 6 — find x. Build the difference table with the letter riding along. First differences: 13 minus x; 17; 23. Second differences: 17 minus the quantity 13 minus x, which is 4 plus x, and 23 minus 17, which is 6. Constant second difference means 4 plus x equals 6, so x is 2. Substitute back and read the honest table: the terms are 2; 13; 30; 53, the first differences are 11; 17; 23, and the second differences are 6 and 6. Now the machine from earlier: 2 a is 6, so a is 3. Then 3 a plus b is 11; three threes are 9, so b is 2. Then a plus b plus c is 2; three plus two is five, so c is minus 3. The general term is T n equals 3 n squared plus 2 n minus 3, and the check on T4: three times 16 is 48, and 48 + 8 − 3 = 53. Certified.

The second favourite is the turning pattern. The pattern 29; 20; 13; 8; 5; 4; 5 falls, bottoms out and rises again — its first differences run minus 9; minus 7; minus 5; minus 3; minus 1; 1, climbing by a constant 2. Its general term is T n equals n squared minus 12 n plus 40, and the question asks for the smallest term. A quadratic in n bottoms out where n equals minus b over 2 a, here 12 over 2, which is position 6. Position six is a natural number, so it is a genuine term, and T6 is 36 minus 72 plus 40 — and 36 − 72 + 40 = 4. The smallest term is 4, sitting at position six. If the vertex lands between whole positions, test the whole numbers on either side and take the smaller — the pattern only exists at natural positions, whatever the parabola does in between.

The final questions of this part are with you now — let the unknown ride through the difference table, and send the vertex position through the natural-number gate before naming the smallest term.

# Part 2 — Simplifier

Now the same quadratic patterns built from cans in a shop display and paving stones in a yard — same rules, same answers, with pictures attached.

## Subtopic: Stacks Where the Gaps Grow

Picture cans stacked in a triangle at the front of a shop. One can on top. The next display uses 3, then 6, then 10. Write the pattern down: 1; 3; 6; 10. Now measure the gaps: 2, then 3, then 4. The gaps are NOT the same — this is no staircase with equal steps. But look at the gaps themselves: they grow by exactly 1 each time. The gap of the gaps is constant.

That is the entire idea of a quadratic pattern. A linear pattern climbs like a staircase with equal steps. A quadratic pattern climbs like a staircase that steepens as you go — every step is taller than the last, and always by the same extra amount. The steepening amount is the second difference; here it is 1.

The picture also predicts. The next gap must be 5, so the next display uses 10 plus 5, which is 15 cans. And the picture warns. If someone claims 1; 3; 6; 10 is linear because "it just keeps growing", the gaps expose the claim in one line: 2, 3, 4 — growing steps, not equal ones. Always measure the gaps, and then measure the gaps of the gaps; the level where the numbers settle down tells you which family the pattern belongs to.

Quick check before we carry on — questions on spotting the growing gaps are coming to you right now. Gaps first, then gaps of gaps, and a constant second level means quadratic.

## Subtopic: Three Facts Build the Whole Formula

A paving contractor lays stone patios in a growing series of designs: 5 stones, then 12, then 23, then 38. Gaps: 7, 11, 15. Gaps of gaps: 4 and 4 — quadratic. Now build the formula T n equals a n squared plus b n plus c from three facts, each one a single sentence.

Fact one: a is HALF the second difference. The second difference is 4, so a is 2. Fact two: the first gap equals 3 a plus b. The first gap is 7, and three twos are 6, so b is 1. Fact three: the first term equals a plus b plus c. The first term is 5, and two plus one is three, so c is 2. The formula is T n equals 2 n squared plus n plus 2 — built in three sentences.

Now make it face the evidence. Design four should use 38 stones: two times 16 is 32, and 32 + 4 + 2 = 38. The formula tells the truth. So trust it on a design too big to draw: design twenty uses two times 400, which is 800, plus 20, plus 2 — and 800 + 20 + 2 = 822 stones. No sketching, no counting, one line.

Your questions for this part are up now. Half the second difference, first gap through 3 a plus b, first term for c — and always test the formula on a design you can still count by hand.

## Subtopic: Which Stack Holds 212 Stones

The contractor's question runs backwards: a client orders a patio of exactly 212 stones — which design is that? Set the formula equal to the order: 2 n squared plus n plus 2 equals 212, so 2 n squared plus n minus 210 equals 0. Factorise: two n plus twenty-one, times n minus ten, equals zero. So n is 10, or n is minus 10,5 — and no patio has design number minus 10,5. Design ten it is. Check: two times 100 is 200, and 200 + 10 + 2 = 212. Exactly the order.

Now back to the can stacks 1; 3; 6; 10; 15, whose formula is T n equals n times n plus 1, over 2. A shopkeeper wants a display of exactly 120 cans. Solve n times n plus one, over two, equals 120: that is n squared plus n minus 240 equals 0, which factorises as n minus fifteen, times n plus sixteen. So n is 15 — stack fifteen holds exactly 120 cans, because fifteen times sixteen is 240, and half of that is 120.

But a display of exactly 100 cans? Stack thirteen holds half of thirteen times fourteen: half of 182, which is 91. Stack fourteen holds half of fourteen times fifteen: half of 210, which is 105. The stacks jump from 91 straight to 105 — no stack holds 100. The algebra says the same thing: n squared plus n minus 200 equals 0 has no natural-number solution, because the square root of 801 is not a whole number. When n refuses to come out whole, the order cannot be filled, and saying so in a sentence is the answer.

And here come the last questions of the lesson, right now: set the formula equal to the order, solve, and only a natural number n names a real design — anything else means the pattern skips that number entirely.
