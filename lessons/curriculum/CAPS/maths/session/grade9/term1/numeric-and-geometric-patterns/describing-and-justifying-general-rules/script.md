# Part 1 — Expert

This session describes and justifies general rules for observed relationships, in plain words and in algebraic language. The anchor pattern is a row of tables each seating people around it: 1 table seats 4, 2 tables joined in a row seat 6, 3 seat 8, with general rule 2n plus 2, justified from the structure — two people along each long side and one at each end. A second anchor is the border of an n by n square of dots, 4n minus 4, which can be seen and written in several equivalent ways. A rule is justified when its parts are explained by the structure, not when it merely fits the given terms.

## Subtopic: From Words to Algebra and Back

A rule can be stated in words or in algebra, and you must be able to translate in both directions. "Start at 5 and add 3 each time" is a recursive description; its position rule is T n equals 3n plus 2, because the step 3 becomes the coefficient and the value one step before the first term, 2, becomes the constant. "Double the position and add 1" is already a position rule: T n equals 2n plus 1, producing 3, 5, 7, 9. "Square the position and subtract 1" is T n equals n squared minus 1, producing 0, 3, 8, 15.

Going back, the algebra must be read aloud faithfully. T n equals 3 times the quantity n minus 1 plus 5 reads "take one less than the position, multiply by 3, add 5" and produces 5, 8, 11, 14 — the same pattern as 3n plus 2, described differently. T n equals 4 times 2 to the power n minus 1 reads "start at 4 and double for each position after the first".

The notation needs care. T n is the term in position n; n is a position, always a counting number 1, 2, 3; T 5 is a specific term, not T times 5. In "T n plus 1" the plus 1 may belong to the position or to the term, so write T subscript n plus 1 for the next term and T n plus 1 for one more than this term, and in speech say "the term after T n" or "T n, plus one".

Variables other than n are common in context. The number of people seated at t tables is P equals 2t plus 2; the cost of k kilometres is C equals 3k plus 2. The letter names the quantity, and the rule is the same relationship. In Grade 10 this becomes y equals 2x plus 2, a straight line with gradient 2 and y-intercept 2 — the pattern language and the function language describe the same thing.

A rule in words is complete when a stranger could produce the fifth term from it. "It goes up by 3" is incomplete — from where? "Start at 5 and go up by 3 each time" is complete. "Square it" is incomplete — square what? "Square the position" is complete.

The questions for this section are with you now: translating between words and algebra, reading notation correctly, and judging whether a description is complete.

## Subtopic: Justifying a Rule From the Structure

A rule is justified when each part of it is explained by the way the pattern is built. Take the anchor: square tables placed in a row, each seating one person per side. One table seats 4. Two tables pushed together seat 6, because the two sides that touch are lost. Three tables seat 8. The numbers 4, 6, 8 have constant difference 2, so the rule is 2n plus 2. That is the finding. Now the justification: along the top of a row of n tables sit n people; along the bottom, n more; and one person sits at each end of the row. That is n plus n plus 2, which is 2n plus 2. The 2n is the two long sides; the plus 2 is the two ends. The rule must keep working because every row of tables, however long, has two long sides and two ends.

Compare that with "it works for n equals 1, 2 and 3". Fitting three terms is evidence; it is not a reason. The structural argument is a reason, and the examiner awards the justification mark for the sentence that links each part of the rule to a part of the picture.

The matchstick squares again: 3n plus 1. Justification: each square after the first shares a side with the one before it, so every square contributes 3 sticks — that is 3n — and the first square needs one extra stick to close it — that is plus 1. Or seen differently: there are n top sticks, n bottom sticks, and n plus 1 vertical sticks, giving 3n plus 1 directly.

The border of an n by n square of dots: 4n minus 4. Justification: four sides each with n dots is 4n, but the four corner dots have each been counted twice, once for each side they belong to, so subtract 4. Test: n equals 3 gives 8, and a 3 by 3 square has 9 dots of which 1 is interior, so 8 on the border. Correct.

A number pattern can be justified too. The triangular numbers 1, 3, 6, 10 have rule n times n plus 1 over 2 because two staircases of n rows fit into an n by n plus 1 rectangle. The pattern 2, 6, 12, 20 has rule n times n plus 1 because each term is a rectangle of dots n wide and n plus 1 tall — and 2, 6, 12, 20 is exactly twice 1, 3, 6, 10, which the pictures also explain.

Take this section's questions now: linking each part of a rule to the structure, and distinguishing "it fits" from "it must".

## Subtopic: Equivalent Rules

Different people see the same picture differently, and so produce rules that look different but are the same. The border of the n by n square can be counted as four sides minus four corners, 4n minus 4; or as four sides of n minus 1 dots each, where each side runs from one corner up to but not including the next, 4 times the quantity n minus 1; or as two full sides of n dots, top and bottom, plus two partial sides of n minus 2 dots each, 2n plus 2 times the quantity n minus 2; or as all the dots minus the interior, n squared minus the quantity n minus 2 squared.

Are these the same rule? Expand each. 4 times the quantity n minus 1 is 4n minus 4. 2n plus 2 times the quantity n minus 2 is 2n plus 2n minus 4, which is 4n minus 4. n squared minus the quantity n minus 2 squared is n squared minus n squared plus 4n minus 4, which is 4n minus 4 — that expansion uses the square of a binomial you will meet in Term 2, and you may verify it numerically for now. All four are 4n minus 4, and all four are correct justifications, each reading the picture a different way.

Two methods test equivalence. The first is algebraic: expand and simplify both rules using the distributive property, and compare. The second is numerical: substitute two or three values of n into both and compare the results — n equals 3 gives 8 from all four border rules, n equals 5 gives 16. Numerical agreement at a few values is strong evidence; algebraic equality is proof. Use the numerical check to catch slips and the algebraic expansion to settle the matter.

The tables again: 2n plus 2 can be seen as 4n minus 2 times the quantity n minus 1 — four seats per table, minus two lost at each of the n minus 1 joins — which expands to 4n minus 2n plus 2, which is 2n plus 2. Same rule, different story. Or as 2 times the quantity n plus 1: pairs of people, one pair per table plus one pair at the ends.

The lesson for the examination: if your rule looks different from the memorandum's, do not assume you are wrong. Expand both. If they agree, your rule is correct and your justification is your own. If they disagree, substitute n equals 1 and n equals 2 to find which one fails.

This section's questions are available now: expanding to compare rules, the numerical check, and reading one picture several ways.

## Subtopic: When a Rule Fails and the Error Museum

A rule that fits the given terms can still be wrong, and one example is enough to break it. Place n points on a circle and join every pair with a straight line; count the regions the circle is cut into. 1 point, 1 region. 2 points, 2 regions. 3 points, 4. 4 points, 8. 5 points, 16. Every student writes 2 to the power n minus 1 and predicts 32 for 6 points. The actual count is 31. The doubling pattern was a coincidence of the first five terms, and the sixth term exposes it. Fitting terms is never a justification; only an explanation of why the structure forces the rule is.

To show a rule is wrong you need one counter-example: one value of n for which the rule and the pattern disagree. To show a rule is right you need an argument that covers every n, which is what the structural justification provides. This asymmetry is the heart of mathematical proof, and Grade 10 geometry will rely on it.

The error museum for this topic has five exhibits. One: writing T n equals n plus 3 for 5, 8, 11 — confusing the recursive step "add 3" with a position rule; T n equals n plus 3 gives 4, 5, 6. Two: writing T n equals 5n — multiplying the first term by the position, which fits T 1 only. Three: "the rule works because it gives the right answers for n equals 1, 2 and 3" offered as a justification — that is a check, not a reason. Four: claiming two rules are different because they look different, without expanding — 4 times n minus 1 and 4n minus 4 are identical. Five: a justification that explains the coefficient but not the constant — "each table adds 2 people" is half the story; the 2 at the ends must be explained too.

Layout for full marks on a "describe and justify" question: state the rule in algebra; state it in words; explain the coefficient from the structure; explain the constant from the structure; test on two terms. Five lines, five marks, and the two explanations are the ones most often missing.

A final habit: when you extend a pattern, write the differences explicitly, state what you observe, write the rule, and then write one sentence beginning "This works because". If you cannot finish that sentence from the structure, your rule is a conjecture, and you should say so.

The questions for this section are ready: the circle pattern that breaks, counter-examples, and the five exhibits of the museum.

# Part 2 — Simplifier

Now the same ideas again through a long table at a family lunch, a square of dots seen four ways and a magic trick that stops working — plain words, same rules.

## Subtopic: Saying It in Words First

Before any algebra, say the rule out loud as if to a friend who cannot see the pattern. For 5, 8, 11, 14: "start at 5 and go up by 3 every time." For 3, 5, 7, 9: "double the position and add 1." For 0, 3, 8, 15: "square the position and take away 1." If your friend can write the next term from your words alone, your description is complete. If they have to ask "start where?" or "square what?", it is not.

Then turn the words into algebra, piece by piece. "Double the position" is 2n. "Add 1" makes it 2n plus 1. "Square the position" is n squared; "take away 1" makes it n squared minus 1. "Go up by 3 every time" means the step is 3, so 3n, and "start at 5" means the term before the start is 2, so 3n plus 2. The algebra is just the words with the position called n.

And back again: read algebra like a sentence. 3 times the quantity n minus 1, plus 5, says "take one off the position, times by 3, add 5". Try n equals 1: 0 times 3 plus 5 is 5. n equals 2: 3 plus 5 is 8. It is the 5, 8, 11 pattern again, told from a different starting place.

A small warning about the symbols. T n means "the term in position n" — the n is a label, not a multiplier. T 5 is the fifth term, not T times 5. And letters other than n are fine: P for people, t for tables, C for cost. P equals 2t plus 2 is the same kind of sentence as T n equals 2n plus 2; only the names changed.

Keep the friend who cannot see the pattern in mind and try the questions for this part: words to algebra, algebra to words, and spotting a description with a hole in it.

## Subtopic: Why It Works, Not Just That It Works

Picture a family lunch. Square tables, one person on each side. One table seats 4. Push two tables together and the touching sides are lost: 6 people. Three tables in a row: 8. The numbers go up by 2, so the rule is 2n plus 2. Fine — but WHY?

Look at the row from above. Along the top edge, one person per table: n people. Along the bottom, another n. And one person at each end of the row: 2 more. n plus n plus 2 is 2n plus 2. Now you are not guessing — you can see that any row of tables, ten long or a thousand long, has two long sides and two ends. That is a justification. "It works for 1, 2 and 3 tables" is just a check.

Every piece of the rule should point at something in the picture. The 2n points at the two long sides. The plus 2 points at the two ends. If a piece of your rule does not point at anything, you have not finished explaining. For the matchstick squares, 3n plus 1: the 3n is the three new sticks each square needs because it shares a wall; the plus 1 is the one stick that closes the first square. Both pieces explained.

Here is why this matters. A rule you can explain is a rule you can rebuild in an exam when you have forgotten it. Picture the tables, count the sides and the ends, and 2n plus 2 comes back by itself. A rule you only memorised is gone when the memory goes.

So after every rule, finish this sentence: "This works because..." If the sentence talks about the picture — sides, ends, shared walls, corners — you have a justification. If it only says "because it gives the right numbers", you have a check, and you should keep looking.

Hold the family lunch table in mind and try this part's questions: pointing each part of the rule at the picture, and the difference between checking and explaining.

## Subtopic: One Pattern, Many Rules

Draw a square of dots, 4 by 4, and count the dots on the border. One friend says: four sides of 4 is 16, but I counted each corner twice, so take 4 off — 12. Rule: 4n minus 4. Another says: each side has 3 dots if I stop before the corner, four sides — 12. Rule: 4 times the quantity n minus 1. A third says: top and bottom rows are 4 each, that is 8, plus the two side columns with the corners already counted, 2 each, 4 more — 12. Rule: 2n plus 2 times the quantity n minus 2. A fourth says: 16 dots in total, minus the 4 in the middle — 12. Rule: n squared minus the quantity n minus 2 squared.

Four rules, four stories, one picture. Are they really the same? Try n equals 5: 20 minus 4 is 16; 4 times 4 is 16; 10 plus 6 is 16; 25 minus 9 is 16. They agree. Try n equals 3: 8, 8, 8, 8. Agree again. Then the algebra settles it: multiply out the brackets and every one of them turns into 4n minus 4. Same rule, dressed differently.

This is good news for exams. If your answer looks different from the memorandum's, do not panic and do not cross it out. Substitute two values of n into both. If they match, expand yours and show it equals theirs — full marks, and your own justification. If they do not match, one of the two is wrong, and the mismatch tells you to look again at the picture.

Now the magic trick that stops working. Put dots on a circle and join every pair with lines. Count the pieces inside: 1, 2, 4, 8, 16. Everyone shouts "32 next!" Draw it carefully with 6 dots and count: 31. The doubling was a coincidence that lasted five terms. This is the lesson of the whole week in one picture: numbers that fit are not a reason. Only a "this works because" that talks about the structure can promise the next term.

Pocket summary of the lesson. Say the rule in words a friend could use. Turn the words into algebra, piece by piece. Point every piece of the rule at something in the picture — that is the justification. If two rules look different, test two values and then expand; they may be the same rule. And remember the circle: five terms that fit prove nothing, one term that fails proves everything.

Hold the lunch table, the four stories and the circle that breaks, and take the final questions of the lesson: equivalent rules, the counter-example, and the sentence that begins "this works because".
