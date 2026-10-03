# Part 1 — Expert

This session investigates patterns that are not limited to a constant difference or a constant ratio: square-based patterns with a constant second difference, triangular numbers, patterns defined by the previous terms such as the Fibonacci sequence, and patterns of the learner's own creation. The anchor patterns are 2, 5, 10, 17, with general term n squared plus 1, and 1, 3, 6, 10, 15, the triangular numbers, with general term n times n plus 1, over 2. Each type is identified by a specific test, and the tests are examinable.

## Subtopic: Second Differences and Square Patterns

Start with the square numbers 1, 4, 9, 16, 25. The first differences are 3, 5, 7, 9 — not constant, so this is not a constant-difference pattern. The ratios are not constant either. Now take the differences of the differences: 2, 2, 2. The second difference is constant. A constant second difference is the fingerprint of a pattern built on n squared, exactly as a constant first difference is the fingerprint of a pattern built on n.

The general term of the squares is T n equals n squared. Every square-based pattern is a shifted or scaled version of this. For 2, 5, 10, 17: first differences 3, 5, 7; second difference 2; so compare with the squares. 2 is 1 plus 1, 5 is 4 plus 1, 10 is 9 plus 1, 17 is 16 plus 1. The rule is T n equals n squared plus 1. Test: T 4 is 16 plus 1, which is 17. T 10 is 101.

For 0, 3, 8, 15, 24: second difference 2; each term is one less than a square; T n equals n squared minus 1. For 3, 6, 11, 18: second difference 2; each term is a square plus 2; T n equals n squared plus 2. When the second difference is 2, the rule is n squared plus or minus a constant, and the constant is T 1 minus 1.

When the second difference is not 2, the squares are scaled. 2, 8, 18, 32: first differences 6, 10, 14; second difference 4. Each term is twice a square: 2 times 1, 2 times 4, 2 times 9, 2 times 16. T n equals 2n squared. The coefficient of n squared is half the second difference — second difference 4 gives 2n squared, second difference 6 would give 3n squared. Grade 11 proves this in general; for now, halve the second difference and test.

Squares can also appear through another pattern. 1, 9, 25, 49 are the squares of 1, 3, 5, 7, the odd numbers, and the odd numbers have rule 2n minus 1, so T n equals the quantity 2n minus 1, all squared. Test: n equals 3 gives 5 squared, which is 25. Correct. Composing a known rule inside a square is a legitimate way to describe a pattern, and the test at two terms is what makes it trustworthy.

The questions for this section are with you now: taking the second difference, comparing with the squares, and halving the second difference for a scaled square pattern.

## Subtopic: Triangular Numbers and Patterns From Previous Terms

The triangular numbers 1, 3, 6, 10, 15 count dots in triangles: one dot, then a row of two below it, then a row of three. The first differences are 2, 3, 4, 5 — the counting numbers — and the second difference is 1, constant. T n is the sum of 1 up to n, and the general term is T n equals n times the quantity n plus 1, over 2. Test: n equals 4 gives 4 times 5 over 2, which is 10. T 10 is 10 times 11 over 2, which is 55. The formula says that two triangles of n rows fit together into an n by n plus 1 rectangle, which is why the division by 2 appears.

Related: 1, 2, 4, 7, 11, 16 has first differences 1, 2, 3, 4, 5 and second difference 1. Each term is one more than a triangular number of the previous position: T n equals n times the quantity n minus 1, over 2, plus 1. Test: n equals 6 gives 6 times 5 over 2 plus 1, which is 16. Correct.

Now a different kind of rule entirely. The Fibonacci sequence 1, 1, 2, 3, 5, 8, 13, 21 has no constant difference, ratio or second difference. Each term is the SUM of the two terms before it: 1 plus 1 is 2, 1 plus 2 is 3, 2 plus 3 is 5, 5 plus 8 is 13. The rule is written T n equals T n minus 1 plus T n minus 2, with the first two terms given. A rule that refers to earlier terms is called recursive, and it is a complete description provided the starting terms are stated — without them, 2, 2, 4, 6, 10 obeys the same rule.

A recursive description exists for every pattern we have met. 5, 8, 11, 14 is T n equals T n minus 1 plus 3 with T 1 equal to 5; 3, 6, 12, 24 is T n equals 2 times T n minus 1 with T 1 equal to 3. The position rule, T n in terms of n, is more powerful because it reaches the 100th term in one step; the recursive rule is often easier to see and is the honest description when no position rule is available, as with Fibonacci at this level.

Alternating signs are a ratio pattern with a negative ratio. 1, negative 2, 4, negative 8, 16 has ratio negative 2, so T n equals negative 2 in brackets to the power n minus 1. Test: n equals 4 gives negative 2 cubed, which is negative 8. Correct. The sign alternates because the power of a negative number alternates.

Take this section's questions now: the triangular formula, recursive rules with their starting terms, and a negative ratio.

## Subtopic: Identifying the Type

Faced with an unfamiliar pattern, run the tests in order. One: first differences constant? Then T n equals d n plus c. Two: ratios constant? Then T n equals T 1 times r to the power n minus 1, and a negative ratio alternates signs. Three: second differences constant? Then the rule involves n squared, with coefficient half the second difference; compare with the squares to find the rest. Four: is each term built from the previous ones — the sum of the last two, or the last term times something that changes? Then write the recursive rule with its starting terms. Five: are the terms recognisable — squares, cubes, triangular numbers, powers of 2, primes? Name them and use the known rule.

Three terms are never enough to decide. 1, 2, 4 continues as 8 under doubling, as 7 under differences 1, 2, 3, and as 8 again under "sum of all previous terms plus 1", with the three rules diverging afterwards. An examination gives four or five terms or a description; use all of them. Compute every first difference and every ratio available, not just the first.

Worked identification. 2, 6, 12, 20, 30: first differences 4, 6, 8, 10; second difference 2; so n squared plus something — 2 is 1 plus 1, 6 is 4 plus 2, 12 is 9 plus 3, so T n equals n squared plus n, which is n times the quantity n plus 1. Test: n equals 5 gives 25 plus 5, which is 30. Also recognisable as twice the triangular numbers.

1, 8, 27, 64, 125: first differences 7, 19, 37, 61, second differences 12, 18, 24 — not constant, and the third difference would be. Faster: recognise the cubes. T n equals n cubed.

4, 7, 12, 19, 28: first differences 3, 5, 7, 9; second difference 2; each term is a square plus 3; T n equals n squared plus 3. Test: n equals 5 gives 28. Correct.

Layout for marks: write the first differences on a line, the second differences below them, state what is constant, name the type, write the rule, and test on two terms. Every one of those is a mark, and the explicit differences are the marks most often thrown away by students who guess the rule and write only the answer.

This section's questions are available now: running the tests in order, why three terms are not enough, and recognising the famous sequences.

## Subtopic: Creating and Describing Your Own Patterns

The CAPS curriculum asks you to create your own patterns, which is the reverse skill: start from a rule and generate terms, then describe the rule in words and in algebra precisely enough that someone else could continue the pattern.

From a position rule. Choose T n equals 3n squared minus 1. Generate: 2, 11, 26, 47, 74. Check the fingerprint: first differences 9, 15, 21, 27; second difference 6, which is twice the coefficient 3, as expected. In words: "square the position, multiply by 3, subtract 1."

From a recursive rule. Choose "start at 2 and 5; each term is the sum of the previous two". Generate: 2, 5, 7, 12, 19, 31. In algebra: T n equals T n minus 1 plus T n minus 2, with T 1 equal to 2 and T 2 equal to 5. Without the starting terms the description is incomplete.

From a picture. Draw squares of dots with a border: a 2 by 2 square has 4 border dots, 3 by 3 has 8, 4 by 4 has 12. Rule: 4 times the quantity n minus 1, or 4n minus 4, where n is the side. In words: "four sides of n dots, with the four corners counted twice, so take away 4." Next lesson is about justifying rules like this from their structure.

Precision in the description is what is marked. "Add more each time" describes nothing; "the differences increase by 2, starting at 3" describes the squares. "Multiply by the position" is ambiguous; "multiply the position by itself, then add 1" is a rule. Algebraic language removes the ambiguity: T n equals n squared plus 1 can be checked by anyone.

The error museum for this topic has five exhibits. One: declaring a pattern arithmetic from the first difference alone — 1, 4, 9 has first difference 3 but is not 1, 4, 7. Two: stopping at three terms. Three: a recursive rule without its starting terms. Four: writing n squared plus 1 from the second difference without comparing the terms — 0, 3, 8, 15 has the same second difference and a different constant. Five: describing a pattern in words so vague that two different continuations fit.

Layout for a created pattern: state the rule in algebra, list at least five terms, show the fingerprint — differences, ratio or recursion — and write one sentence in plain words. That is a complete answer and it is also a fair puzzle for a classmate.

The questions for this section are ready: generating from a rule, describing precisely, and the five exhibits of the museum.

# Part 2 — Simplifier

Now the same patterns again through staircases of blocks, a pair of rabbits and a recipe for inventing a puzzle of your own — plain words, same rules.

## Subtopic: Staircases and Squares

Build a staircase from blocks: one block, then a step of two next to it, then three, then four. The totals are 1, 3, 6, 10. How much did each step add? 2, then 3, then 4 — a bit more every time. That is the sign of a pattern that is NOT a taxi meter. A taxi adds the same amount each time; a staircase adds a bigger amount each time. But look at how much bigger: the extra goes up by exactly 1 each step. The "difference of the differences" is steady, and that steadiness is the new fingerprint.

The square numbers do the same. Draw a square of dots: 1, then 2 by 2 is 4, then 3 by 3 is 9, then 16. Each new square wraps an L-shaped layer around the old one, and each layer is 2 dots bigger than the last: 3, 5, 7, 9. Differences growing by 2 every time. Whenever you see that, the rule has n squared in it, and the simplest case is T n equals n squared itself.

Most square patterns are the squares with something done to them. 2, 5, 10, 17: the differences are 3, 5, 7 — growing by 2 — so compare each term to a square. 2 is 1 plus 1; 5 is 4 plus 1; 10 is 9 plus 1. Every term is a square plus 1, so T n equals n squared plus 1. 0, 3, 8, 15: every term is a square minus 1. Spot the growing-by-2 differences, line the terms up next to 1, 4, 9, 16, and the shift jumps out.

If the differences grow by 4 instead of 2, the squares have been doubled: 2, 8, 18, 32 is 2 times each of 1, 4, 9, 16. Growing by 6 means tripled. Halve the growth to find the multiplier, then compare.

And the staircase? The totals 1, 3, 6, 10, 15 are the triangular numbers. Two staircases fit together into a rectangle n long and n plus 1 tall, so one staircase is half of that: n times n plus 1, over 2. Ten steps: 10 times 11 over 2, which is 55 blocks.

Keep the staircase and the wrapping layers in mind and try the questions for this part: differences that grow steadily, and lining a pattern up against the squares.

## Subtopic: Rabbits and Spirals

Here is a pattern with a story. A pair of rabbits is born. After a month they are grown; the month after, they have a pair of babies, and every month after that another pair. Each new pair does the same. Count the pairs each month: 1, 1, 2, 3, 5, 8, 13, 21. No steady difference, no steady ratio, no steady difference-of-differences. The rule is different in kind: each number is the two before it added together. 1 plus 1 is 2; 1 plus 2 is 3; 2 plus 3 is 5; 3 plus 5 is 8; 8 plus 13 is 21. That is the Fibonacci sequence, and it shows up in sunflower seeds, pine cones and the spiral of a shell.

A rule like that — "add the two before" — is a recipe that looks backwards instead of a formula that looks at the position. It is called recursive. To make it complete you MUST say where it starts. "Add the two before" starting from 2 and 5 gives 2, 5, 7, 12, 19 — a completely different list. Rule plus starting terms, or it is not a description.

Every pattern you know has a backwards recipe too. The taxi meter 5, 8, 11, 14 is "add 3 to the one before, starting at 5". The chain message 3, 6, 12, 24 is "double the one before, starting at 3". The position formula is better for jumping to the 100th term; the backwards recipe is often easier to spot, and for Fibonacci it is the only one you will use this year.

One more exotic animal: 1, negative 2, 4, negative 8, 16. The sizes double and the signs flip. That is a chain message with a multiplier of negative 2: each term is the one before times negative 2, and the position formula is negative 2 in brackets to the power n minus 1. A negative multiplier is the only way to get a pattern that swings from positive to negative and back forever.

Hold the rabbits and the backwards recipe and try this part's questions: spotting "add the two before", why the start matters, and the flipping sign.

## Subtopic: Make Your Own Pattern

Now you are the puzzle-setter. Pick a rule, generate the terms, and describe it so clearly that a friend could continue it without you. Here is the recipe.

Step one, pick a rule from the menu. A taxi rule: a step and a flag fall, like 4n plus 1. A chain rule: a first term and a multiplier, like 5 times 2 to the power n minus 1. A square rule: like n squared plus 3 or 2n squared. A backwards rule: like "start at 3 and 4, add the two before".

Step two, generate at least five terms, carefully. For n squared plus 3: 4, 7, 12, 19, 28. For "start at 3 and 4, add the two before": 3, 4, 7, 11, 18, 29.

Step three, check the fingerprint yourself, so you know your puzzle is fair. n squared plus 3 should have differences growing by 2: 3, 5, 7, 9. Yes. If your terms do not show the fingerprint you expected, you made an arithmetic slip, and the puzzle would be impossible.

Step four, describe it twice: once in plain words and once in algebra. Words: "square the position and add 3." Algebra: T n equals n squared plus 3. For the backwards one: "start with 3 and 4; every term after is the sum of the two before it", and T n equals T n minus 1 plus T n minus 2 with T 1 equal to 3 and T 2 equal to 4.

The words must be precise. "It goes up by more each time" is not a rule; "the differences are 3, 5, 7, 9, growing by 2" is. "Multiply by the position" could mean several things; "multiply the position by itself" means one thing. If two different continuations fit your words, your words are not finished.

Pocket summary of the lesson. Steady differences: taxi. Steady ratios: chain message. Differences that grow steadily: squares — compare with 1, 4, 9, 16 and halve the growth for a multiplier. Each term from the two before: rabbits, and say where it starts. Three terms never decide; use them all. And when you make your own, give the rule in words and algebra, with five terms and the fingerprint checked.

Hold the staircase, the rabbits and the puzzle recipe, and take the final questions of the lesson: generating from a rule, describing it precisely, and spotting a description that is too vague to use.
